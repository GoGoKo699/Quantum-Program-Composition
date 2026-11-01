#!/usr/bin/env python3
"""Finite checks of the ordered-register collective composition instrument.

The numerical matrices grow exponentially with the number of copies. These are
small-instance algebra and register-order checks, not an implementation of the
polynomial-gate processor. Fidelity means pure-target overlap (squared overlap).

Run from the repository root:
    OPENBLAS_NUM_THREADS=1 python verification/check_construction.py
"""

from __future__ import annotations

import argparse
import json
from functools import reduce

import numpy as np


SPECTRAL_CASES = (
    (2, 1, 1), (2, 1, 2), (2, 1, 5), (2, 2, 2), (2, 3, 3), (2, 4, 4),
    (3, 1, 1), (3, 1, 3), (3, 2, 2),
    (4, 1, 1), (4, 1, 2), (4, 2, 2),
)
PHYSICAL_CASES = ((2, 1, 1), (2, 1, 2), (2, 2, 2), (2, 1, 4), (3, 1, 2))
SEED = 20261101


def check(condition: bool, message: str) -> None:
    """Keep verification active even when Python is invoked with -O."""
    if not condition:
        raise AssertionError(message)


def close(actual: np.ndarray | float, expected: np.ndarray | float,
          message: str, atol: float = 2e-10) -> None:
    check(bool(np.allclose(actual, expected, rtol=2e-10, atol=atol)), message)


def bell_projector(d: int, registers: int, a: int, b: int) -> np.ndarray:
    """Normalized |Phi_d><Phi_d| on tensor positions a,b, identity elsewhere."""
    dimension = d**registers
    powers = d ** np.arange(registers - 1, -1, -1, dtype=np.int64)
    indices = np.arange(dimension, dtype=np.int64)
    digits = (indices[:, None] // powers[None, :]) % d
    columns = indices[digits[:, a] == digits[:, b]]
    old_digit = digits[columns, a]
    result = np.zeros((dimension, dimension), dtype=float)
    for new_digit in range(d):
        rows = columns + (new_digit - old_digit) * (powers[a] + powers[b])
        result[rows, columns] = 1.0 / d
    return result


def gram_operator(d: int, m: int, n: int) -> np.ndarray:
    """G=d sum_(r,s) Phi_(r,m+s) on m+n inner registers."""
    dimension = d ** (m + n)
    result = np.zeros((dimension, dimension), dtype=float)
    for r in range(m):
        for s in range(n):
            result += d * bell_projector(d, m + n, r, m + s)
    return result


def spectral_data(gram: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    values, vectors = np.linalg.eigh(gram)
    cutoff = 1e-10 * max(1.0, float(values.max()))
    check(float(values.min()) >= -cutoff, "Bell-sum Gram operator is not positive")
    # These finite cases have a separated nonzero spectrum. The threshold is a
    # numerical kernel convention, not an assumption used by the theorem.
    positive = values > cutoff
    values = np.where(positive, values, 0.0)
    inverse_values = np.zeros_like(values)
    inverse_values[positive] = 1.0 / np.sqrt(values[positive])
    inverse = (vectors * inverse_values) @ vectors.conj().T
    support = (vectors * positive) @ vectors.conj().T
    return values, inverse, support


def check_spectrum(d: int, m: int, n: int) -> dict[str, float | int]:
    gram = gram_operator(d, m, n)
    values, _, _ = spectral_data(gram)
    mean = m * n / d
    variance = m * n * (1.0 - d**-2)
    close(float(values.mean()), mean, "incorrect first moment")
    close(float(values.var()), variance, "incorrect variance")
    close(float(np.trace(gram @ gram) / len(gram)),
          m * n + (m * m * n * n - m * n) / (d * d),
          "incorrect second moment")
    fidelity = float(np.sqrt(values).mean() ** 2 / mean)
    success = float(np.count_nonzero(values) / len(values))
    lower = m * n / (m * n + d * d - 1)
    check(fidelity + 2e-10 >= lower, "Holder fidelity bound failed")
    check(success + 2e-10 >= lower, "support-probability bound failed")
    check(-2e-10 <= fidelity <= success + 2e-10 <= 1.0 + 4e-10,
          "fidelity/success probabilities out of range")
    if m == n == 1:
        close(fidelity, d**-2, "single-pair Bell fidelity is incorrect")
        close(success, d**-2, "single-pair Bell probability is incorrect")
    return {
        "d": d, "m": m, "n": n, "inner_dimension": len(values),
        "mean": float(values.mean()), "variance": float(values.var()),
        "polar_global_fidelity": fidelity, "success_probability": success,
        "proved_fidelity_lower_bound": lower,
    }


def haar_unitary(d: int, rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    q, r = np.linalg.qr(z)
    phases = np.diag(r) / np.abs(np.diag(r))
    result = q @ np.diag(phases)
    close(result.conj().T @ result, np.eye(d), "QR sample is not unitary")
    return result


def tensor_product(states: list[np.ndarray]) -> np.ndarray:
    return reduce(np.kron, states, np.array([1.0 + 0.0j]))


def apply_on_axes(state: np.ndarray, operator: np.ndarray, axes: list[int],
                  d: int, registers: int) -> np.ndarray:
    remaining = [axis for axis in range(registers) if axis not in axes]
    permutation = axes + remaining
    reordered = state.reshape([d] * registers).transpose(permutation)
    matrix = reordered.reshape(d ** len(axes), -1)
    transformed = (operator @ matrix).reshape([d] * registers)
    return transformed.transpose(np.argsort(permutation)).reshape(-1)


def bell_contract_and_route(state: np.ndarray, d: int, m: int, n: int,
                           r: int, s: int) -> np.ndarray:
    """L_rs: normalized Bell bra, then selected outer halves and whole residue."""
    contracted = [2 * r + 1, 2 * m + 2 * s]
    output_order = [2 * r, 2 * m + 2 * s + 1]
    for other_r in range(m):
        if other_r != r:
            output_order.extend([2 * other_r, 2 * other_r + 1])
    for other_s in range(n):
        if other_s != s:
            output_order.extend([2 * m + 2 * other_s, 2 * m + 2 * other_s + 1])
    reordered = state.reshape([d] * (2 * (m + n))).transpose(
        contracted + output_order
    ).reshape(d, d, -1)
    return np.einsum("iik->k", reordered) / np.sqrt(d)


def physical_branches(state: np.ndarray, d: int, m: int, n: int,
                      inverse: np.ndarray) -> list[np.ndarray]:
    inner = [2 * r + 1 for r in range(m)] + [2 * m + 2 * s for s in range(n)]
    filtered = apply_on_axes(state, inverse, inner, d, 2 * (m + n))
    return [np.sqrt(d) * bell_contract_and_route(filtered, d, m, n, r, s)
            for r in range(m) for s in range(n)]


def check_physical_case(d: int, m: int, n: int,
                        rng: np.random.Generator) -> dict[str, float | int]:
    gram = gram_operator(d, m, n)
    values, inverse, support = spectral_data(gram)
    predicted_fidelity = float(np.sqrt(values).mean() ** 2 / (m * n / d))
    predicted_success = float(np.count_nonzero(values) / len(values))
    max_bare_error = 0.0
    max_branch_difference = 0.0
    for _ in range(2):
        u_matrix, v_matrix = haar_unitary(d, rng), haar_unitary(d, rng)
        u = u_matrix.reshape(-1) / np.sqrt(d)
        v = v_matrix.reshape(-1) / np.sqrt(d)
        state = tensor_product([u] * m + [v] * n)
        target = tensor_product([(u_matrix @ v_matrix).reshape(-1) / np.sqrt(d)]
                                + [u] * (m - 1) + [v] * (n - 1))
        close(float(np.vdot(target, target).real), 1.0, "target not normalized")
        # The target is independently formed by ordinary matrix multiplication.
        # This catches wrong transposes, wrong product order and leftover routing.
        for r in range(m):
            for s in range(n):
                bare = bell_contract_and_route(state, d, m, n, r, s)
                error = float(np.linalg.norm(d * bare - target))
                max_bare_error = max(max_bare_error, error)
                check(error < 2e-10, "Bell contraction did not produce UV and residues")
        branches = physical_branches(state, d, m, n, inverse)
        difference = max(float(np.linalg.norm(branch - branches[0]))
                         for branch in branches)
        max_branch_difference = max(max_branch_difference, difference)
        check(difference < 2e-10, "routed collective branches disagree")
        fidelity = sum(abs(np.vdot(target, branch)) ** 2 for branch in branches)
        success = sum(float(np.vdot(branch, branch).real) for branch in branches)
        close(float(fidelity), predicted_fidelity, "physical/spectral fidelity mismatch")
        close(success, predicted_success, "physical/spectral success mismatch")

    # Legality on general inputs must not rely on the program-family promise.
    dimension = d ** (2 * (m + n))
    generic = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    generic /= np.linalg.norm(generic)
    branches = physical_branches(generic, d, m, n, inverse)
    success_generic = sum(float(np.vdot(branch, branch).real) for branch in branches)
    inner = [2 * r + 1 for r in range(m)] + [2 * m + 2 * s for s in range(n)]
    projected = apply_on_axes(generic, support, inner, d, 2 * (m + n))
    probability_support = float(np.vdot(projected, projected).real)
    close(success_generic, probability_support, "general-input instrument is not normalized")
    check(success_generic <= 1.0 + 2e-10, "general-input probability exceeds one")
    return {
        "d": d, "m": m, "n": n, "program_trials": 2,
        "max_bare_contraction_error": max_bare_error,
        "max_branch_difference": max_branch_difference,
        "polar_global_fidelity": predicted_fidelity,
        "success_probability": predicted_success,
        "general_input_support_error": abs(success_generic - probability_support),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit structured results")
    args = parser.parse_args()
    rng = np.random.default_rng(SEED)
    spectra = [check_spectrum(*case) for case in SPECTRAL_CASES]
    physical = [check_physical_case(*case, rng) for case in PHYSICAL_CASES]
    if args.json:
        print(json.dumps({"seed": SEED, "numpy_version": np.__version__,
                          "spectral_checks": spectra, "physical_checks": physical,
                          "status": "PASS"}, indent=2))
    else:
        for row in spectra:
            print("spectrum d={d} m={m} n={n}: "
                  "F_pol={polar_global_fidelity:.9f} "
                  "p={success_probability:.9f} "
                  "bound={proved_fidelity_lower_bound:.9f} PASS".format(**row))
        for row in physical:
            print("physical d={d} m={m} n={n}: UV order, returned programs, "
                  "branch equality and general-input normalization PASS".format(**row))
        print(f"PASS: {len(spectra)} spectra; {len(physical)} physical cases "
              f"with two seeded program pairs and one general input each; seed={SEED}")


if __name__ == "__main__":
    main()
