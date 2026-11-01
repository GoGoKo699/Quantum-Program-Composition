#!/usr/bin/env python3
"""Finite checks of the all-dimensional Choi-moment converse.

This evaluates Haar integrals from permutation-invariant Gram matrices, not
Monte Carlo samples and not the representation-block formulas being checked.
The Moore-Penrose inverse handles dependent invariant tensors when d < k.
The resulting floating-point matrices are checked against the harmonic-block
ordering, commutation, and trace-distance claims in science/converse.md.

Run from the repository root:
    OPENBLAS_NUM_THREADS=1 python verification/check_mixed_moments.py

Only NumPy is needed. The fixed small cases include m+n > d, including an
unbalanced allocation. These checks test finite matrix identities and
normalizations; they do not replace the proof for arbitrary dimensions.
"""

from __future__ import annotations

import itertools
import json
from functools import lru_cache

import numpy as np


TOLERANCE = 2e-8


@lru_cache(maxsize=None)
def haar_choi_moment(d: int, k: int) -> np.ndarray:
    """E (|U><U|)^tensor k in grouped (all rows, all columns) order.

    The invariant-tensor Gram matrix has entries d^cycles(sigma^-1 tau).
    Its pseudoinverse gives the unitary Haar integral even below the stable
    dimension range. Reshuffling that integral gives the Choi moment.
    """
    dimension = d**k
    tuples = np.array(list(itertools.product(range(d), repeat=k)), dtype=int)
    powers = d ** np.arange(k - 1, -1, -1, dtype=int)
    permutations = list(itertools.permutations(range(k)))
    matrices = np.zeros((len(permutations), dimension, dimension))
    for index, permutation in enumerate(permutations):
        destinations = tuples[:, permutation] @ powers
        matrices[index, destinations, np.arange(dimension)] = 1.0
    flat = matrices.reshape(len(permutations), -1)
    gram = flat @ flat.T
    weingarten = np.linalg.pinv(gram, rcond=1e-12, hermitian=True)
    moment = np.einsum(
        "pq,pij,qab->iajb", weingarten, matrices, matrices, optimize=True
    ).reshape(dimension**2, dimension**2)
    return (moment + moment.T) / (2 * dimension)


def partial_transpose_programs(
    matrix: np.ndarray, d: int, k: int, slots: range
) -> np.ndarray:
    """Transpose both Choi halves of each selected whole program copy."""
    axes = list(range(4 * k))
    for slot in slots:
        for row_axis in (slot, k + slot):
            column_axis = 2 * k + row_axis
            axes[row_axis], axes[column_axis] = axes[column_axis], axes[row_axis]
    return matrix.reshape([d] * (4 * k)).transpose(axes).reshape(matrix.shape)


def independent_moment(d: int, m: int, n: int) -> np.ndarray:
    """Product of the two independently Haar-averaged program pools."""
    k = m + n
    raw = np.kron(haar_choi_moment(d, m), haar_choi_moment(d, n).T)
    # Raw row order is (A_first, B_first, A_second, B_second).
    grouped_rows = (
        list(range(m))
        + list(range(2 * m, 2 * m + n))
        + list(range(m, 2 * m))
        + list(range(2 * m + n, 2 * k))
    )
    axes = grouped_rows + [axis + 2 * k for axis in grouped_rows]
    return raw.reshape([d] * (4 * k)).transpose(axes).reshape(raw.shape)


def harmonic_projector(d: int, m: int, n: int) -> np.ndarray:
    """Kernel of the stacked cross-pool contraction maps on one Choi half."""
    k = m + n
    tuples = list(itertools.product(range(d), repeat=k))
    rows = []
    for first in range(m):
        for second in range(m, k):
            retained = [r for r in range(k) if r not in (first, second)]
            for rest in itertools.product(range(d), repeat=k - 2):
                rows.append(
                    [
                        float(
                            value[first] == value[second]
                            and tuple(value[r] for r in retained) == rest
                        )
                        for value in tuples
                    ]
                )
    _, singular_values, vh = np.linalg.svd(np.array(rows), full_matrices=True)
    rank = np.count_nonzero(singular_values > 1e-10)
    basis = vh[rank:].T
    return basis @ basis.T


def minimum_eigenvalue(matrix: np.ndarray) -> float:
    return float(np.linalg.eigvalsh((matrix + matrix.T) / 2)[0])


def require(condition: bool, description: str) -> None:
    """Keep checks active under python -O."""
    if not condition:
        raise AssertionError(description)


def check_case(d: int, m: int, n: int) -> dict[str, float | int | bool]:
    k = m + n
    correlated = partial_transpose_programs(
        haar_choi_moment(d, k), d, k, range(m, k)
    )
    independent = independent_moment(d, m, n)
    p = harmonic_projector(d, m, n)
    pi = np.kron(p, p)
    a = pi @ correlated @ pi
    b = pi @ independent @ pi
    q = float(1 - np.trace(p) / d**k)
    delta = float(np.trace(a - b))
    distance = float(np.abs(np.linalg.eigvalsh(correlated - independent)).sum() / 2)
    result = {
        "d": d,
        "m": m,
        "n": n,
        "outside_faithful_range": k > d,
        "q": q,
        "trace_a": float(np.trace(a)),
        "trace_b": float(np.trace(b)),
        "delta": delta,
        "correlated_commutator_norm": float(np.linalg.norm(pi @ correlated - correlated @ pi)),
        "independent_commutator_norm": float(np.linalg.norm(pi @ independent - independent @ pi)),
        "minimum_compressed_difference_eigenvalue": minimum_eigenvalue(a - b),
        "trace_distance": distance,
        "dimension_bound": min(1.0, 2 * m * n / d**2),
        "harmonic_bound": min(1.0, 2 * q),
    }
    for name, moment in (("correlated", correlated), ("independent", independent)):
        require(abs(float(np.trace(moment)) - 1) < TOLERANCE, f"{name}: trace one")
        require(minimum_eigenvalue(moment) > -TOLERANCE, f"{name}: positivity")
        require(np.linalg.norm(moment - moment.T) < TOLERANCE, f"{name}: Hermiticity")
    require(np.linalg.norm(p @ p - p) < TOLERANCE, "harmonic projection")
    require(q <= m * n / d**2 + TOLERANCE, "harmonic dimension bound")
    require(result["correlated_commutator_norm"] < TOLERANCE, "correlated block diagonality")
    require(result["independent_commutator_norm"] < TOLERANCE, "independent block diagonality")
    require(result["minimum_compressed_difference_eigenvalue"] > -TOLERANCE, "A >= B")
    require(abs(float(np.trace(a)) - (1 - q)) < TOLERANCE, "trace A = 1-q")
    require(float(np.trace(b)) >= 1 - 2 * q - TOLERANCE, "trace B >= 1-2q")
    require(-TOLERANCE <= delta <= q + TOLERANCE, "0 <= delta <= q")
    require(minimum_eigenvalue(correlated - a) > -TOLERANCE, "positive correlated remainder")
    require(minimum_eigenvalue(independent - b) > -TOLERANCE, "positive independent remainder")
    require(distance <= q + delta + TOLERANCE, "trace distance <= q+delta")
    require(distance <= result["harmonic_bound"] + TOLERANCE, "trace-distance bound")
    if m == n == 1:
        # Direct scalar-plus-adjoint calculation gives this closed form.
        expected = 2 * (d**2 - 1) / d**4
        require(abs(distance - expected) < TOLERANCE, "one-pair analytic calibration")
    return result


def main() -> None:
    for d, m, n in ((2, 1, 1), (3, 1, 1), (3, 1, 2), (2, 1, 3), (2, 2, 2)):
        print(json.dumps(check_case(d, m, n), sort_keys=True), flush=True)
    print("PASS: finite mixed-Haar moment checks, including unbalanced m+n>d.")


if __name__ == "__main__":
    main()
