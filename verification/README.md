# Reproducing the finite checks

The analytical arguments in [science](../science/README.md) establish the theorem. The scripts here independently test sensitive finite-dimensional identities: physical routing and normalization, the mixed-moment block comparison, and the symmetry-compressed circuit encoding. Every check uses an explicit failure condition that remains active under optimized Python execution.

## Environment and commands

Use Python 3.11 or later and the pinned NumPy version:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_construction.py
python verification/check_mixed_moments.py
python verification/check_projected_encoding.py
```

The recorded checks were run with Python 3.12 and NumPy 2.3.5. Setting `OPENBLAS_NUM_THREADS=1` is optional and keeps small dense calculations inexpensive on highly threaded machines. The construction and mixed-moment scripts accept `--json` for detailed numerical output. The first returns one JSON report; the second returns one JSON object per case followed by its pass summary.

No network access, credentials, quantum device or operation oracle is needed. These are small classical checks of the displayed operators, rather than a classical implementation of the asymptotically large quantum algorithm.

## Construction and physical registers

`check_construction.py` forms the Bell-sum operator on the inner halves and diagonalizes it. Twelve cases range over local dimensions two to four, with largest inner Hilbert-space dimension 256. The script checks both exact moments, spectral success probability, the polar target overlap and the proved finite-budget bound.

Five physical-register cases each use two seeded complex Haar program pairs. They verify the order of multiplication, the entire leftover-program tensor, equality of all routed branches and agreement with the spectral formulas. A generic input outside the identical-copy promise also tests the instrument's support effect.

Representative polar-branch contributions to global fidelity are:

| Dimension | U copies | V copies | Computed contribution | Proved lower bound |
|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 0.2500000000 | 0.2500000000 |
| 2 | 2 | 2 | 0.6575883570 | 0.5714285714 |
| 2 | 4 | 4 | 0.9303774110 | 0.8421052632 |
| 3 | 2 | 2 | 0.3902651626 | 0.3333333333 |

These values omit any nonnegative fidelity supplied by the channel's arbitrary failure output. They are not claims that the displayed instrument attains the optimal fidelity.

## Mixed-Haar moment comparison

`check_mixed_moments.py` evaluates Haar integrals through invariant-tensor Gram pseudoinverses, independently of the harmonic-block expressions used in the proof. It then constructs the cross-traceless projector and checks positivity, normalization, commutation, the ordering of compressed blocks, positive complementary blocks and the trace-distance bound.

The cases are $(d,m,n)=(2,1,1),(3,1,1),(3,1,2),(2,1,3),(2,2,2)$. The final two have $m+n>d$, so they directly exercise the dimension issue, including an unbalanced supply. The one-pair cases also match an independently derived exact trace-distance formula.

| Dimension | U copies | V copies | Computed trace distance | Dimension bound |
|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 0.3750000000 | 0.5000000000 |
| 3 | 1 | 1 | 0.1975308642 | 0.2222222222 |
| 3 | 1 | 2 | 0.3614962461 | 0.4444444444 |
| 2 | 1 | 3 | 0.5818301169 | 1.0000000000 |
| 2 | 2 | 2 | 0.6583116296 | 1.0000000000 |

The script also tests the sharper intermediate bound from the actual discarded and compressed weights, rather than relying only on the final bound when it becomes one. Floating-point negative eigenvalues at roundoff scale are evaluated with explicit tolerances.

## Projected encoding and clean ancillas

`check_projected_encoding.py` builds full ordered-copy symmetry projectors and Bell contractions. Five cases test the Gram normalization and the exact target action for local dimensions two and three. Separate permutation-average encodings for two and three qubit programs verify a nontrivial symmetry phase and clean ancilla return. The observed largest discrepancy in these cases is below $4\times10^{-15}$.

The test distinguishes the restricted Bell block from the unrestricted binary-spectrum Bell projector. Its small dense matrices verify the operator identity; the charged addressed-swap construction in [Implementation](../science/implementation.md) supplies the asymptotic gate bound.

## What these checks do not establish

Finite floating-point calculations do not prove the asymptotic lower bound, certify novelty, or establish optimal small-error dependence. The circuit test does not synthesize an entire QSVT phase sequence or simulate fault-tolerant gates. Polynomial approximation, phase construction and gate synthesis use the cited primary theorems. The public proof explains their hypotheses and how the program inputs meet them.

## Hosted mathematical display

The separate [hosted review](hosted/README.md) visits commit-pinned GitHub pages in a fresh browser, compares the rendered mathematics with the tracked source, and saves wide and narrow screenshots. Its read-only workflow uses public pages and temporary dependencies. The report records the exact revision, page scope and expression counts, including inline formulas and table cells.

This display check requires network access. It supplements the finite scientific checks above: matching MathML structure does not establish a proof, and screenshots still need inspection for legibility and navigation. The hosted guide documents the command, dependency versions and report files.
