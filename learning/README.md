# Learning quantum program composition

Two sources supply quantum states that encode unknown operations. A processor
must combine those states into a program for the product operation. This
learning route explains the physical task, the collective construction and
the reason every processor faces the same copy-product scale.

The single educational anchor is **John Watrous, *The Theory of Quantum
Information* (2018)**. The [Watrous bridge](WATROUS_BRIDGE.md) identifies
targeted sections of the author's manuscript, translates its notation and
normalization conventions, and supplies the connections needed here. The
book is a foundation for the project; the project's theorem and its
research-level dependencies have their own cited scientific sources.

## Choose a starting point

| Aim | Route |
|---|---|
| See what a program represents and what composition does | [Worked tutorial](TUTORIAL.md) |
| Build the complete conceptual picture | [Thirty-milestone map](MILESTONES.md) |
| Connect familiar quantum-information foundations to this task | [Watrous bridge](WATROUS_BRIDGE.md) |
| Inspect exact quantifiers and proofs | [Scientific account](../science/README.md) |
| Reproduce the small-system checks | [Verification guide](../verification/README.md) |
| Compare the method with exact state preparation | [Canonical-purification boundary](../science/canonical_purification_boundary.md) |

The milestone map is defined by the scientific project and is shared by all
readers. Its background phase builds the operational and mathematical
framework; its narrative phase connects the construction, converse,
implementation and final resource interpretation. Each milestone has an
understanding target, dependencies and source pointers. The worked tutorial
provides a connected entry into that map, while specialist derivations stay
in their authoritative scientific pages.

## Keep the physical resources visible

The supplied inputs are complete, ideal, pure Choi copies. Both halves are
accessible, but no classical matrix or query access to the unknown
operations is supplied. The output is one composed program state. The
construction also controls the joint state of all returned specimens.

Fidelity in this project is the **squared** pure-target overlap. A finite
copy guarantee and an implementation's gate cost answer different
questions. A good single-use return guarantee does not establish a
repeated-reuse rate. These conventions and boundaries are carried through
the learning route and stated precisely in the [model](../science/model.md)
and [interpretation](../science/interpretation.md).

The same Watrous foundations support the sister canonical-purification task, but its learning route has different understanding targets. The final milestones here use the [comparison](../science/canonical_purification_boundary.md) to audit a proposed transfer: check the accessible correlations, the exact or approximate output promise, every source charge, and the residual systems. Shared contraction machinery does not make the two resource laws interchangeable.
