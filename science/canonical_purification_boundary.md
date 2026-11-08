# Coherent contraction and exact canonical purification

[Scientific account](README.md) · [Composition construction](construction.md) · [Interpretation](interpretation.md) · [Canonical-purification sister project][canonical]

The [Canonical-Purification-Cost][canonical] project and quantum program composition share a physical design question: a linear contraction has the desired action on unknown supplied states, but how can it be normalized into a legal quantum operation on the whole input space? They answer that question for different input orbits and different correctness requirements. The exact canonical-purification frontier belongs to the sister project; it is not a consequence of the unitary-Choi composition theorem.

## Two tasks with different supplied correlations

In this repository, a program is the normalized pure Choi vector of an arbitrary unknown unitary:

```math
|U\rangle=\frac{\mathrm{vec}(U)}{\sqrt d},
\qquad
\mathrm{Tr}_{1}|U\rangle\langle U|
=\mathrm{Tr}_{2}|U\rangle\langle U|=\frac{I}{d}.
```

Both registers of every supplied program are accessible. Contracting the inner halves of one program from each pool produces

```math
(\langle\Phi_d|_{BC}\otimes I_{AD})
\bigl(|U\rangle_{AB}|V\rangle_{CD}\bigr)
=\frac{|UV\rangle_{AD}}{d}.
```

The [model](model.md) specifies the register order and hard program budgets. The collective construction controls squared fidelity with the composed program and all returned specimens. Its successful state is generally approximate.

For the sister task, fix a known signal space $`V\cong\mathbb C^d`$ orthogonal to a known vacuum. Its mixed sources and prescribed target are

```math
\rho_\psi=\frac{|\mathrm{vac}\rangle\langle\mathrm{vac}|
+|\psi\rangle\langle\psi|}{2},
\qquad
\rho_\psi^*=\frac{|\mathrm{vac}\rangle\langle\mathrm{vac}|
+|\bar\psi\rangle\langle\bar\psi|}{2},
```

```math
|T_\psi\rangle
=\frac{|\mathrm{vac},\mathrm{vac}\rangle
+|\psi\rangle|\bar\psi\rangle}{\sqrt2}.
```

Conjugation is in the fixed supplied basis. The two sources are independent conditional on the unknown ray. Their inaccessible purification environments are not supplied. The target's vacuum/signal relative coherence is part of its definition; producing its two marginals separately does not prepare this target.

| Operational feature | Unitary-program composition | Exact canonical purification |
|---|---|---|
| Supplied pure objects | Two-register unitary Choi states | State/conjugate vectors after extracting known signal sectors |
| Key marginal | Every inner Choi half is maximally mixed | A retained signal is rank one |
| Unknown parameters | Two arbitrary unitaries | One ray and its supplied conjugate |
| Useful output | Program for the ordered matrix product | Prescribed vacuum/signal coherent purification |
| Collective correctness | Approximate global squared fidelity | Exact target conditional on success |
| Remaining registers | Included in a global approximate return promise | May be discarded after exact target/residual factorization |
| Mixed-source environment | No mixed-source environment is needed | Inaccessible; not an available record or program |

These distinctions are assumptions at the boundary of a proposed transfer, not changes of notation.

## The shared physical normalization problem

The program construction restricts a known Bell contraction to the separately symmetric space of whole programs. With the notation of [Construction](construction.md#2-symmetry-identifies-the-common-successful-state), its scaled map satisfies

```math
Mv=\sqrt{\mu}\,w,
\qquad M^\dagger M=G,
\qquad \mu=\frac{mn}{d}.
```

This target-action identity alone does not make $`M`$ a success operator. The physical processor uses the polar partial isometry

```math
K=MG^{-1/2},
\qquad K^\dagger K=\Pi_{\mathrm{supp}G}\leq I.
```

The inverse vanishes on the kernel. It acts differently on different singular directions, so $`Kv`$ need not remain parallel to $`w`$. The exact moment calculation bounds the resulting distortion:

```math
F_{\mathrm{global}}\geq\frac{mn}{mn+d^2-1}.
```

An exact mathematical definition of this channel specifies its operation before gate-synthesis error; it does not mean exact accepted output. The [success and fidelity calculation](construction.md#4-fidelity-and-success-probability) keeps these quantities separate.

The canonical task instead combines a coherent scalar contraction and extraction of the signal pair. On the pure input space

```math
R_{n,m}=\mathrm{Sym}^n(V)\otimes
\mathrm{Sym}^m(\overline V),
```

let $`a_i,b_i`$ be normalized symmetric-tensor annihilation maps and define

```math
C=\sum_i a_i b_i,
\qquad
E_{n,m}=\frac1{\sqrt{nm}}\sum_{i,j}|i,j\rangle\otimes a_i b_j,
```

```math
W_{n,m}
=\frac1{\sqrt2}
\left(
|\mathrm{vac},\mathrm{vac}\rangle\otimes\frac{C}{\sqrt{nm}}
+E_{n,m}
\right).
```

For positive $`n,m`$, $`E_{n,m}`$ is an isometry and

```math
W_{n,m}\bigl(\psi^{\otimes n}\bar\psi^{\otimes m}\bigr)
=T_\psi\otimes
\psi^{\otimes(n-1)}\bar\psi^{\otimes(m-1)}.
```

Again, this exact action on the promised orbit is not a contractivity proof. The [canonical exact-frontier account][exact] characterizes all admissible residual positive operators $`X`$ through

```math
W_{n,m}^\dagger(I_{\mathrm{out}}\otimes X)W_{n,m}\leq I,
\qquad X\geq0.
```

This condition is imposed on the entire symmetric input space and extended by zero on its orthogonal complement. Every feasible operator gives a completely positive trace-nonincreasing success map, with a complementary failure effect. Normalized occupation notation represents ordinary finite-dimensional symmetric tensors; it does not supply free bosonic hardware.

For one conjugate pure specimen, the residual space is $`\mathrm{Sym}^{n-1}(V)`$ and

```math
CC^\dagger=(d+n-1)I,
\qquad
\|W_{n,1}\|^2=\frac{d+2n-1}{2n}.
```

Scaling by this norm gives success $`2n/(d+2n-1)`$. The sister project's exact-output rigidity argument proves that this is optimal over arbitrary processors, rather than only over this displayed filter.

The shared method is therefore useful at the level of coherent contraction, separately symmetric copy pools, target/residual factorization and whole-space physical normalization. The suitable normalization and its performance analysis must be derived for the actual target and source orbit.

## What the exact frontier adds

The canonical result starts from arbitrary accepting Kraus operators. Exact output forces their vacuum and signal amplitudes to obey a polynomial identity. After homogenization, the vacuum amplitude is divisible by $`\sum_i z_iw_i`$, leaving residual bidegree $`(n-1,m-1)`$. This is an exact-output restriction absent from an approximate fidelity promise.

The [authoritative pure-frontier proof][exact] derives the charged harmonic weights and an attained linear program with $`\min(n,m)`$ variables. It covers every pure-copy allocation and arbitrary ancillas, multiple accepted outcomes and discarded systems. In particular,

```math
q_d^*(n,1)=\frac{2n}{d+2n-1},
\qquad
q_d^*(n,0)=q_d^*(0,m)=0
\quad(d\geq2).
```

The full finite LP, rather than a guessed product formula, is the exact all-allocation statement. For example, $`q_2^*(2,2)=12/13`$; the earlier top-residual projection filter attains $`1/2`$ for that input. Optimizing the whole admissible residual operator can matter substantially even in a small system.

For hard mixed-source caps $`A,B`$, the [mixed-frontier proof][mixed] shows that measuring the known vacuum/signal sectors loses no information. Their signal counts are independent,

```math
K\sim\mathrm{Bin}(A,1/2),
\qquad
L\sim\mathrm{Bin}(B,1/2),
```

and the exact optimum is

```math
Q_d^*(A,B)=\mathbb E\,q_d^*(K,L).
```

Every requested specimen counts, including vacuum outcomes, surplus signals and rejected filters. Bounded adaptive source order is included by precollection under these separate caps. An additional stricter total cap requires its own analysis.

The zero-count sectors imply

```math
Q_d^*(A,B)\leq(1-2^{-A})(1-2^{-B}).
```

Thus a single conjugate mixed specimen limits success to $`1/2`$, however large the ordinary supply becomes. A product of supplied budgets alone cannot describe this full fixed-success frontier. The interpretation that $`nm`$ of order $`d`$ sets a general canonical-purification scale remains conjectural here; no fixed-approximate-fidelity product law is asserted.

## Why the composition theorem does not transfer

The [composition moment proof](construction.md#3-exact-first-and-second-moments) replaces expectations of functions of $`G`$ by normalized traces because the complete inner marginal is $`I/d^{m+n}`$. Rank-one signal specimens do not satisfy that hypothesis. The composition converse also compares two Haar-unitary priors, not a state/conjugate orbit. Substituting $`d`$ for $`d^2`$ in its result would supply neither the missing moment identity nor the required converse.

Likewise, applying a polar normalization to $`W_{n,m}`$ is not an exact-purification protocol merely because it produces a contraction. A direction-dependent rescaling can change the vacuum/signal relative amplitude and the exact accepted state. The residual-operator constraint and polynomial rigidity handle this exactness requirement directly.

The independent source model supplies neither matched purification gauges nor a coherent record identifying how a mixed specimen was prepared. A proof that introduces environments to represent a completely positive map does not make the source's inaccessible environment physically available.

Finally, whole-copy symmetry and known register permutations can be used in either setting, but the [program implementation](implementation.md) does not automatically implement an optimal canonical residual filter or prove its gate cost. The canonical frontier is a copy-information result; its efficient gate synthesis is a separate question.

## Ownership and reading route

This repository owns the unitary-program construction, its arbitrary-processor composition converse, the fixed-error $`mn=\Theta(d^2)`$ law and its charged implementation. The sister project owns the prescribed-purification model and the [exact pure][exact] and [mixed-source][mixed] frontier proofs. Its inherited balanced total-copy approximate theorem retains its original hypotheses and is distinct from the new exact unequal-budget characterization.

For the common foundations, use the [Watrous bridge](../learning/WATROUS_BRIDGE.md): completely positive maps and Stinespring contractions in §2.2.2, symmetric tensor spaces in §7.1.1, and Haar averaging in §7.2.1. General positive-kernel stochastic conversion is inherited theory, discussed and attributed in the canonical proof; the task-specific polynomial support and coefficients are derived there.

[canonical]: https://github.com/GoGoKo699/Canonical-Purification-Cost
[exact]: https://github.com/GoGoKo699/Canonical-Purification-Cost/blob/c0e1cac831e7bc6073042974c5f440bd847b37a0/science/exact_frontier.md
[mixed]: https://github.com/GoGoKo699/Canonical-Purification-Cost/blob/c0e1cac831e7bc6073042974c5f440bd847b37a0/science/mixed_frontier.md

