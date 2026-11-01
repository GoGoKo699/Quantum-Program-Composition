# Quantum Program Composition

**How many quantum programs are needed to compose two unknown operations?**

This project studies a processor supplied with copies of the Choi states of two arbitrary unknown $d$-dimensional unitaries $U$ and $V$. It must produce the Choi state of $UV$, using known quantum operations and no classical descriptions or queries to either unitary.

The optimal copy-product threshold at fixed error is

$$
mn=\Theta(d^2),
$$

where $m$ and $n$ are the two copy budgets. Balanced supplies therefore require and suffice with $\Theta(d)$ copies of each program. The construction additionally returns the remaining programs within one global fidelity guarantee.

## Principal results

| Result | Established guarantee | Scientific account |
|---|---|---|
| Collective composition | Global squared fidelity at least $mn/(mn+d^2-1)$ | [Construction](science/construction.md) |
| Arbitrary-processor converse | $mn\geq p_0(d^2F_0-1)/2$ for uniform success $p_0$ and conditional fidelity $F_0$ | [Converse](science/converse.md) |
| Balanced copy cost | Optimal total copies of order $d$ at fixed error | [Model](science/model.md) |
| Explicit known-gate circuit | Approximately $d^3$ gates, up to logarithmic factors, with balanced fixed-error supplies | [Implementation](science/implementation.md) |

The lower bound holds for every allocation and dimension, including one copy of one program and order $d^2$ copies of the other. It allows collective processing, adaptive measurements and independent ancillary memory. The exact hypotheses and fidelity convention are in the [model](science/model.md).

## How the result works

A Bell contraction of one program pair gives the desired matrix product with probability $d^{-2}$. The collective processor uses a square-root measurement over all pairs of ports in the two pools. Its Gram operator has explicit first and second moments, which bound the distortion of the composed program and all returned specimens.

For the converse, a sufficiently accurate composer would distinguish inverse-correlated unknown operations from independent ones. Their averaged Choi inputs remain close when the product of copy budgets is small. Mixed-tensor symmetry makes this comparison valid without a stable-dimension assumption.

The [related-work account](references/RELATED_WORK.md) credits Choi-state composition, pretty-good measurements, port-based teleportation, mixed Schur–Weyl duality and singular-value transformation. The contribution is the universal program-composition resource law and its construction/converse, rather than a new general measurement or representation-theory method.

## Reading and reproduction

Choose a route according to the question you want to answer:

| Reader's question | Starting point |
|---|---|
| What is the task, and what is proved? | [Scientific account](science/README.md) and [exact model](science/model.md) |
| How does a stored operation become a composed program? | [Worked tutorial](learning/TUTORIAL.md) |
| Which foundations connect to the proofs? | [Watrous bridge](learning/WATROUS_BRIDGE.md) |
| How do the ideas fit into one learning route? | [Learning guide](learning/README.md) and [30 milestones](learning/MILESTONES.md) |
| How can I reproduce the finite checks? | [Verification guide](verification/README.md) |

The single educational anchor is John Watrous's *The Theory of Quantum Information* (2018). The bridge identifies relevant sections and translates the Choi normalization and fidelity conventions. The specialist proofs remain in the scientific account.

From the repository root, with Python 3.11 or later:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_construction.py
python verification/check_mixed_moments.py
python verification/check_projected_encoding.py
```

These scripts check physical-register routing, Gram moments, mixed Choi ensembles and the projected circuit encoding in small dimensions. They do not constitute a proof of the asymptotic theorems or a simulation of a fault-tolerant implementation.

## Scope

Both halves of each ideal pure Choi copy are accessible. The output is a quantum state encoding $UV$; executing $UV$ on fresh data is a separate task. The gain is in program copies, while the known gates and memory are charged explicitly. Optimal vanishing-error dependence, noisy-source robustness and repeated reuse of returned programs are not established. See [Interpretation and limits](science/interpretation.md).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
