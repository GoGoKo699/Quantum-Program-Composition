# From Watrous to quantum program composition

The educational anchor is **John Watrous, *The Theory of Quantum
Information*** (Cambridge University Press, 2018). The
[author's official page](https://cs.uwaterloo.ca/~watrous/TQI/) provides
individual chapters, a pre-publication manuscript and errata. The source
locations below refer to that author-hosted manuscript. It is available for
personal use; this repository links to it and supplies its own explanations.

The project asks how many copies of two unknown unitary programs are needed
to construct a program for their product. Watrous supplies the language of
states, channels, measurements, distinguishability and symmetry. The
[milestone map](MILESTONES.md) organizes those foundations around this
particular task; the [tutorial](TUTORIAL.md) connects them through a worked
example. The specialist statements remain in the
[scientific account](../science/README.md).

## Targeted source map

There is no need to read the whole book before approaching the project.

| Source location | Foundation to extract | Where it enters the project |
|---|---|---|
| [§§1.1.2–1.1.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf): operator-vector correspondence, decompositions and norms | Matrix entries can be stored in a bipartite vector; an SVD separates directions from singular values. | The Choi convention in [Model](../science/model.md) and the polar contraction in [Construction](../science/construction.md). |
| [§1.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), especially Theorem 1.13: random variables and Markov's inequality | Moments of a nonnegative random variable bound its tail probabilities. | Applying those bounds to the Gram operator's spectral weights in [Construction](../science/construction.md) and [Implementation](../science/implementation.md), as used in M11 and M25. |
| [§§2.1.2–2.1.3 and §2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf): states, reductions, channel representations | Distinguish a channel from a physical state representing it, and track partial traces. | Normalized unitary Choi programs and their maximally mixed inner halves. |
| [§2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf): measurements and instruments | A measurement can return both a classical outcome and an unnormalized quantum output. | Port selection, register routing, success probability and failure completion. |
| [§3.1.1 and §3.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf): binary discrimination and the pretty-good measurement | Trace distance bounds observable probability differences; square-root normalization defines a legal measurement. | The correlation test in [Converse](../science/converse.md) and the two-pool measurement in [Construction](../science/construction.md). |
| [§3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf): fidelity | Read approximation guarantees with the convention conversion below. | Joint output fidelity, successful-branch overlap and returned programs. |
| [§6.3.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf): teleportation and dense coding | Bell measurements connect entanglement to operational transformations. | The single-pair Bell contraction and its dimension-dependent probability. |
| [§§7.1.1–7.1.2 and §7.2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf), including Theorem 7.14: permutation symmetry, double commutants and Haar measure | Permutation invariance, commutants and unitary averaging have separate roles. | Whole-copy symmetry, Haar-correlated ensembles, and the representation framework for M21–M22; the required mixed-tensor theorem is supplied below. |

## Two convention conversions

### A Choi operator becomes a physical state only after normalization

Watrous defines the Choi representation in §2.2.2, equations (2.64)–(2.65),
using the unnormalized vector $\mathrm{vec}(I)$. For a channel
$\mathcal E$ with d-dimensional input,

$$
J(\mathcal E)
=(\mathcal E\otimes\mathrm{id})
  \bigl(\mathrm{vec}(I)\mathrm{vec}(I)^\dagger\bigr),
\qquad
\mathrm{Tr}J(\mathcal E)=d.
$$

The normalized Choi state is therefore $\omega_{\mathcal E}=J(\mathcal E)/d$.
For the unitary channel $\mathcal U(X)=UXU^\dagger$,

$$
J(\mathcal U)=\mathrm{vec}(U)\mathrm{vec}(U)^\dagger,
\qquad
\omega_{\mathcal U}=|U\rangle\langle U|,
\qquad
|U\rangle=\frac{\mathrm{vec}(U)}{\sqrt d}.
$$

The tensor order is output followed by input, matching this project's
row-first convention. Both halves have reduced state $I/d$ for a unitary.

**Normalization does not imply purity.** For example, the qubit dephasing
channel $\mathcal D(X)=\sum_{j=0}^1|j\rangle\langle j|X|j\rangle\langle j|$
has normalized Choi state

$$
\omega_{\mathcal D}
=\frac12\bigl(|00\rangle\langle00|+|11\rangle\langle11|\bigr),
$$

which has rank two. The supplied programs in this project are pure because
the channels are unitary, not because Choi states are always pure.

### Watrous's fidelity is the square root of the project's fidelity

Watrous's Definition 3.11 uses

$$
F_{\mathrm W}(\rho,\sigma)
=\Vert\sqrt\rho\sqrt\sigma\Vert_1.
$$

For a normalized pure target $|w\rangle$, this project uses

$$
F_{\mathrm{project}}(\rho,w)
=\langle w|\rho|w\rangle
=F_{\mathrm W}(\rho,|w\rangle\langle w|)^2.
$$

Thus the project's infidelity $\epsilon$ means
$F_{\mathrm W}\geq\sqrt{1-\epsilon}$. For an unnormalized successful output
$\tau=p\rho_{\mathrm s}$, its unconditional target contribution is
$\langle w|\tau|w\rangle=pF_{\mathrm{project}}(\rho_{\mathrm s},w)$.
Dividing by the success probability changes the quantity being reported.

## Translating the measurement and symmetry language

The pretty-good measurement appears in Watrous §3.1.2, equations
(3.49)–(3.52). For a singular average state, the inverse is a pseudoinverse
on its support and the kernel needs a completion. Here that completion is a
separate failure outcome with a fixed output state; the useful outcomes
select a pair $(r,s)$ of ports. The derivation of their action and fidelity
is in [Construction](../science/construction.md), rather than being supplied
by a general PGM theorem.

In §7.1.1, take one textbook tensor factor to be an **entire two-register
program**, of dimension $d^2$. The relevant input subspace is

$$
\mathrm{Sym}^m(\mathbb C^{d^2})
\otimes\mathrm{Sym}^n(\mathbb C^{d^2}).
$$

Permuting only one half changes which registers are paired and need not
preserve the promised input state. The permutation projector is known from
the register dimensions and copy counts, whereas a
reflection about an unknown supplied program is not an available primitive.

In the converse, Haar averaging concerns unitaries in $U(d)$ and their Choi
states. It does not mean drawing a uniformly random pure vector in
$\mathbb C^{d^2}$. Those are different ensembles. The local
[converse](../science/converse.md) explains the correlated and independent
priors before applying the discrimination bound.

## Research bridges supplied by the project

The following are research dependencies, not additional educational anchors.
They are introduced where the project needs them.

**From symmetry to the universal converse.** The lower bound uses the
represented commutant of $U^{\otimes m}\otimes\overline U^{\otimes n}$.
Its cross-contractions define a harmonic subspace; centrality of that
subspace's projector allows the two Choi moments to be compared without a
square-root loss. These mixed-tensor facts go beyond the foundation mapped
above. The exact inputs are Goncharov's Theorem 2.3 and Proposition 2.4 in
[arXiv:2511.00303v1](https://arxiv.org/html/2511.00303v1), together with the
mixed Schur–Weyl formulation in Grinko–Ozols,
[arXiv:2207.05713v2](https://arxiv.org/abs/2207.05713v2). The
[converse proof](../science/converse.md) supplies their application, including
the all-dimensional argument and the final identity-program test.

**From a polar operator to a circuit.** The textbook's SVD and polar
decomposition explain the desired transformation. They do not by themselves
give an economical circuit for it. Projected QSVT is imported from Gilyén,
Su, Low and Wiebe,
[arXiv:1806.01838v1](https://arxiv.org/abs/1806.01838v1). The
[implementation proof](../science/implementation.md) supplies the specific
block $QP$, a known singular-value cutoff justified by the supplied input's
spectral-tail bound, known symmetry phases, and the charged gate count. It
invokes no inverse of an unknown program preparation.

**From teleportation to two-pool composition.** The Bell contraction and
square-root normalization have established antecedents. The project derives
the port-pair instrument, its exact Gram moments, the joint-return fidelity
and the matching constant-error copy-product law. The
[related-work account](../references/RELATED_WORK.md) identifies what comes
from teleportation and quantum-programming literature and what the present
task adds.

Return to the [learning overview](README.md) for the map and tutorial, or go
directly to the [model](../science/model.md) for the exact assumptions and
bounds.
