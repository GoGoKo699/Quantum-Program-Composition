#!/usr/bin/env python3
"""Finite checks of the physical projected encoding and symmetry phases.

The tests construct ordered qudit registers, not a bosonic occupation model.
They verify the normalization of the symmetrized Bell block, its action on
independent random unitary Choi inputs, and clean ancilla return for a
permutation-average implementation of a symmetry phase.

These finite checks do not prove asymptotic gate counts, construct a QSVT phase
sequence, or replace the analytical bounds in science/implementation.md.
"""
from __future__ import annotations

import itertools
import math

import numpy as np

ATOL = 2e-10


def check_close(actual: np.ndarray, expected: np.ndarray, label: str) -> float:
    error = float(np.linalg.norm(actual - expected))
    if error > ATOL:
        raise AssertionError(f"{label}: Frobenius/vector error {error:.3g}")
    return error


def tensor_permutation(local_dim: int, order: tuple[int, ...]) -> np.ndarray:
    """Return the matrix mapping |x> to |x[order[0]], ..., x[order[-1]]>."""
    k = len(order)
    size = local_dim**k
    digits = np.array(list(itertools.product(range(local_dim), repeat=k)))
    target = np.ravel_multi_index(digits[:, order].T, (local_dim,) * k)
    result = np.zeros((size, size))
    result[target, np.arange(size)] = 1
    return result


def whole_copy_symmetrizer(d: int, m: int, n: int) -> np.ndarray:
    k = m + n
    result = np.zeros((d ** (2 * k),) * 2)
    for a in itertools.permutations(range(m)):
        for b in itertools.permutations(range(n)):
            order = tuple(a) + tuple(m + j for j in b)
            result += tensor_permutation(d * d, order)
    return result / (math.factorial(m) * math.factorial(n))


def bell_projector(d: int, k: int, first: int, second: int) -> np.ndarray:
    """Bell projector on two of the 2k physical qudit registers."""
    size = d ** (2 * k)
    basis = list(itertools.product(range(d), repeat=2 * k))
    result = np.zeros((size, size))
    for column, values in enumerate(basis):
        if values[first] != values[second]:
            continue
        for replacement in range(d):
            output = list(values)
            output[first] = output[second] = replacement
            row = np.ravel_multi_index(tuple(output), (d,) * (2 * k))
            result[row, column] += 1 / d
    return result


def bell_bra_and_route(d: int, m: int, n: int) -> np.ndarray:
    """Contract first U tail with first V head, routing UV then leftovers."""
    k = m + n
    inner = (1, 2 * m)
    remaining = (0, 2 * m + 1) + tuple(range(2, 2 * m)) + tuple(
        range(2 * m + 2, 2 * k)
    )
    result = np.zeros((d ** (2 * k - 2), d ** (2 * k)))
    for column, values in enumerate(itertools.product(range(d), repeat=2 * k)):
        if values[inner[0]] != values[inner[1]]:
            continue
        output = tuple(values[j] for j in remaining)
        row = np.ravel_multi_index(output, (d,) * (2 * k - 2))
        result[row, column] = 1 / np.sqrt(d)
    return result


def random_unitary(d: int, rng: np.random.Generator) -> np.ndarray:
    matrix = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    q, r = np.linalg.qr(matrix)
    phases = np.diag(r) / np.abs(np.diag(r))
    return q * phases.conjugate()


def tensor_vectors(vectors: list[np.ndarray]) -> np.ndarray:
    result = np.ones(1, dtype=complex)
    for vector in vectors:
        result = np.kron(result, vector)
    return result


def check_projected_block(d: int, m: int, n: int, rng: np.random.Generator) -> None:
    k = m + n
    p = whole_copy_symmetrizer(d, m, n)
    b = bell_bra_and_route(d, m, n)
    q = bell_projector(d, k, 1, 2 * m)
    bell_sum = sum(
        bell_projector(d, k, 2 * a + 1, 2 * (m + c))
        for a in range(m)
        for c in range(n)
    )
    check_close(p @ p, p, "P is a projector")
    rank = math.comb(d * d + m - 1, m) * math.comb(d * d + n - 1, n)
    if abs(np.trace(p) - rank) > ATOL:
        raise AssertionError("Incorrect whole-copy symmetric dimension")
    check_close(b.T @ b, q, "Bell bra is Q with fixed ket removed")
    check_close(p @ bell_sum, bell_sum @ p, "Full Bell sum preserves symmetry")
    a = b @ p
    gram = a.T @ a
    normalization_error = check_close(
        gram, p @ bell_sum @ p / (m * n), "A* A = G_S/(dmn)"
    )
    # A plain Bell projector is binary, while the compressed block generally is not.
    check_close(q @ q, q, "Bare Bell projector is binary")
    if k > 2:
        values = np.linalg.eigvalsh(gram)
        if not np.any((values > 1e-8) & (values < 1 - 1e-8)):
            raise AssertionError("Expected nontrivial compressed singular spectrum")
    u = random_unitary(d, rng)
    v = random_unitary(d, rng)
    choi_u, choi_v = u.reshape(-1) / np.sqrt(d), v.reshape(-1) / np.sqrt(d)
    input_state = tensor_vectors([choi_u] * m + [choi_v] * n)
    ideal = tensor_vectors(
        [(u @ v).reshape(-1) / np.sqrt(d)]
        + [choi_u] * (m - 1)
        + [choi_v] * (n - 1)
    )
    check_close(p @ input_state, input_state, "Unknown input belongs to P")
    target_error = check_close(a @ input_state, ideal / d, "A v = w/d, UV order")
    print(
        f"projected block d={d} m={m} n={n}: PASS "
        f"(Gram error {normalization_error:.2e}, target error {target_error:.2e})"
    )


def prepare_uniform_range(t: int) -> np.ndarray:
    """A small explicit unitary preparing a uniform range in padded qubits.

    Householder form is used only to check the operator identity numerically;
    the gate count uses the prefix-rotation construction explained in the text.
    """
    size = 1 << (t - 1).bit_length()
    target = np.zeros(size)
    target[:t] = 1 / np.sqrt(t)
    e0 = np.zeros(size)
    e0[0] = 1
    direction = e0 - target
    if np.linalg.norm(direction) < 1e-14:
        return np.eye(size)
    direction /= np.linalg.norm(direction)
    return np.eye(size) - 2 * np.outer(direction, direction)


def check_clean_symmetry_phase(d: int, k: int, phi: float = 0.371) -> None:
    h = d * d
    physical = h**k
    prepare = np.ones((1, 1))
    ranges = []
    for t in range(2, k + 1):
        factor = prepare_uniform_range(t)
        ranges.append(factor.shape[0])
        prepare = np.kron(prepare, factor)
    ancilla = prepare.shape[0]
    select = np.zeros((ancilla * physical,) * 2)
    for label, choices in enumerate(itertools.product(*(range(s) for s in ranges))):
        order = list(range(k))
        # Invalid padding labels receive a valid arbitrary unitary (identity).
        if all(choice < t for t, choice in zip(range(2, k + 1), choices)):
            for t, choice in zip(range(2, k + 1), choices):
                order[t - 1], order[choice] = order[choice], order[t - 1]
        block = tensor_permutation(h, tuple(order))
        sl = slice(label * physical, (label + 1) * physical)
        select[sl, sl] = block
    f = np.kron(prepare, np.eye(physical))
    encoding = f.T @ select @ f
    p = sum(tensor_permutation(h, perm) for perm in itertools.permutations(range(k)))
    p /= math.factorial(k)
    check_close(encoding[:physical, :physical], p, "Permutation-average block")
    # V* exp(i phi (2 Pi_0-I)) V is an exact phase about P on clean ancillas.
    phases = np.full(ancilla * physical, np.exp(-1j * phi))
    phases[:physical] = np.exp(1j * phi)
    lifted = encoding.T.conj() @ (phases[:, None] * encoding)
    expected = np.cos(phi) * np.eye(physical) + 1j * np.sin(phi) * (2 * p - np.eye(physical))
    block_error = check_close(lifted[:physical, :physical], expected, "Symmetry phase")
    leakage = check_close(lifted[physical:, :physical], np.zeros_like(lifted[physical:, :physical]), "Clean ancilla return")
    print(
        f"symmetry phase d={d} copies={k}: PASS "
        f"(block error {block_error:.2e}, leakage {leakage:.2e})"
    )


def main() -> None:
    rng = np.random.default_rng(20261101)
    for d, m, n in [(2, 1, 1), (2, 2, 1), (2, 2, 2), (2, 3, 1), (3, 1, 2)]:
        check_projected_block(d, m, n, rng)
    for copies in (2, 3):
        check_clean_symmetry_phase(2, copies)
    print("All projected-encoding and clean-ancilla checks passed.")


if __name__ == "__main__":
    main()
