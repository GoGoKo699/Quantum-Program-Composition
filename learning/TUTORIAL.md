# Composing quantum programs: a worked route through the result

A processor is handed quantum states encoding two unknown operations. It
must produce a state encoding their product. It receives no classical
descriptions, calls to the operations, or inverses of their preparation
circuits. The available resource is a counted supply of program states.

This tutorial follows the [30-milestone map](MILESTONES.md). The single
educational anchor is Watrous's *The Theory of Quantum Information*;
[the source bridge](WATROUS_BRIDGE.md) identifies the relevant sections and
convention changes. The exact assumptions and bounds are in
[Model and composition law](../science/model.md).

## 1. What a program state contains

**Milestones M01–M05 and M13.** A d-dimensional unitary $U$ is encoded in
the normalized bipartite state

$$
|U\rangle
=\frac1{\sqrt d}\sum_{i,j=0}^{d-1}U_{ij}|i\rangle|j\rangle.
$$

The first register labels the matrix row and the second labels its column.
This ordering fixes the multiplication performed below. A global phase of
$U$ changes only the global phase of the ket, so the physical program
$|U\rangle\langle U|$ is unaffected.

For a unitary, either half alone has state $I/d$. The information about the
operation is in the correlations. The model supplies both halves of every
copy, so collective processing can use those correlations. The supply is
$m$ identical copies of the first program and $n$ identical copies of the
second, each in its own physical registers.

These are pure programs because the encoded operations are unitary. A
general channel's normalized Choi state can be mixed; the
[source bridge](WATROUS_BRIDGE.md#two-convention-conversions) gives an
explicit example. Producing a program for $UV$ is also different from
applying $UV$ to an additional data register: no such data register is the
output target here.

## 2. A complete qubit example

**Milestones M06–M08 and M14.** Take $d=2$ and, for a worked example, choose

$$
H|0\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},\qquad H|1\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}.
$$

$$
S|0\rangle=|0\rangle,\qquad S|1\rangle=i|1\rangle.
$$

Their programs are

$$
|H\rangle_{AB}
=\frac{|00\rangle+|01\rangle+|10\rangle-|11\rangle}{2},
\qquad
|S\rangle_{CD}
=\frac{|00\rangle+i|11\rangle}{\sqrt2}.
$$

The four input qubits are ordered $A,B,C,D$. Project the two middle qubits
$B,C$ onto
$|\Phi_2\rangle=(|00\rangle+|11\rangle)/\sqrt2$, and retain the outer
qubits $A,D$. The unnormalized state on those outer qubits is

$$
\begin{aligned}
(I_A\otimes\langle\Phi_2|_{BC}\otimes I_D)
  |H\rangle_{AB}|S\rangle_{CD}
&=\frac{|00\rangle+i|01\rangle+|10\rangle-i|11\rangle}{4}\\
&=\frac12|HS\rangle_{AD}.
\end{aligned}
$$

Its squared norm is $1/4$. Thus the two-outcome measurement
$\lbrace|\Phi_2\rangle\langle\Phi_2|,I-|\Phi_2\rangle\langle\Phi_2|\rbrace$
has a designated successful outcome with probability $1/4$. Conditioned on
that outcome, the output is exactly the normalized program

$$
|HS\rangle
=\frac{|00\rangle+i|01\rangle+|10\rangle-i|11\rangle}{2}.
$$

The order matters: the program for $SH$ instead has coefficients
$(1,1,i,-i)/2$ in the same basis. These two vectors are not related by a
global phase. The contraction consequently distinguishes the order of the
operations, rather than merely changing an unobservable phase.

The matrices above let us verify the calculation. The processor does not
need to know them: it performs the same middle-register Bell projection for
every supplied pair. It uses four program qubits and returns a two-qubit
program on the designated outcome. The other outcome occurs with probability
$3/4$; it is not declared an exact composition.

The calculation extends directly to every dimension:

$$
(I_A\otimes\langle\Phi_d|_{BC}\otimes I_D)
 |U\rangle_{AB}|V\rangle_{CD}
=\frac{|UV\rangle_{AD}}{d}.
$$

The normalization factors therefore give amplitude $1/d$ and probability
$1/d^2$. Conditional fidelity is one, while this branch's contribution to
unconditional fidelity is only $1/d^2$. Assigning a fixed output on failure
makes a trace-preserving processor, whose fidelity includes both outcomes.

## 3. Pooling the programs without pretending the pairs are independent

**Milestones M10–M12 and M15–M19.** With $m$ first-program copies and $n$
second-program copies, there are $mn$ candidate cross-pool pairs. They
overlap: a copy can participate in several candidates, and their Bell
projectors generally do not commute. Measuring every candidate as an
independent classical trial would not be a legal use of the same copies.

The collective construction instead forms the known positive operator

$$
G=d\sum_{r=1}^m\sum_{s=1}^n E_{rs},
$$

where $E_{rs}$ is the Bell projector on the two chosen inner halves and the
identity on the others. If $L_{rs}$ contracts that pair and routes its outer
halves to the output, the useful instrument operators are

$$
J_{rs}=\sqrt dL_{rs}G^{-1/2}.
$$

The inverse vanishes on the kernel. These operators satisfy
$\sum_{r,s}J_{rs}^\dagger J_{rs}=\Pi_{\mathrm{supp}G}\leq I$.
Adding a failure outcome gives a complete physical instrument. Its
square-root normalization is the pretty-good measurement construction;
[the source bridge](WATROUS_BRIDGE.md) relates it to Watrous §3.1.2.

All copies in either pool are identical. Permuting **whole programs**
within a pool therefore fixes the input. After the selected outer halves
are routed consistently, every useful outcome produces the same
unnormalized global vector, up to the common branch factor. This is why
the analysis can compare the entire output with

$$
|w\rangle=|UV\rangle
 |U\rangle^{\otimes(m-1)}|V\rangle^{\otimes(n-1)}.
$$

The joint inner marginal is exactly maximally mixed. Consequently the
spectral distribution of $G$ on the supplied state has moments

$$
\mathbb E G=\frac{mn}{d},
\qquad
\mathrm{Var}(G)=mn(1-d^{-2}).
$$

The relative variance $r=(d^2-1)/(mn)$ controls the distortion from the
square-root normalization. The moment argument in
[Construction](../science/construction.md) proves

$$
F_{\mathrm{global}}\geq\frac1{1+r}
=\frac{mn}{mn+d^2-1}.
$$

This fidelity includes the composed program and all returned programs in a
single target. It is an unconditional guarantee for the completed channel.
The useful branches are generally approximate, unlike the designated
single-pair Bell outcome.

For example, with qubit programs and $m=n=6$, the exact collective channel
guarantees global fidelity at least $36/39=12/13$, approximately $0.923$.
The input comprises twelve two-qubit programs. The joint target comprises
eleven: one composed program and five from each original pool. Six
independent paired Bell trials have success probability
$1-(3/4)^6\approx0.822$, and do not provide that joint-return promise.
These are guaranteed bounds and a baseline success probability, not claims
about the exact optimal fidelity or the constants of the finite QSVT
circuit.

## 4. The lower bound applies to every processor

**Milestones M09, M12 and M20–M23.** Consider two ways to supply the
unknown operations. In the first, $U$ is Haar random and $V=U^\dagger$,
so the product is always the identity. In the second, $U,V$ are independent
Haar unitaries, so their product is Haar random.

A composer could help distinguish these situations: run it and test the
output against the known identity program $|I\rangle=|\Phi_d\rangle$.
After averaging known changes of basis, a successful universal composer has
constant success probability $p$ and conditional target fidelity $F$. The
event “success and identity test accepts” then has probabilities $pF$ and
$p/d^2$ in the two situations.

The hard part is bounding how distinguishable the supplied inputs were
before this processing. Swapping the physical halves of each second-program
copy turns the correlated input into programs for $U$ and $\overline U$.
The relevant symmetry is $U^{\otimes m}\otimes\overline U^{\otimes n}$.

After regrouping the Choi halves, the proof works with a harmonic subspace
on a space of dimension $D=d^{m+n}$. Its vectors vanish under every
cross-pool contraction, and its lost dimension fraction is at most
$mn/d^2$. This is a different subspace from the whole-program symmetric
subspace used in the construction. The mixed-tensor centralizer theorem
makes its projector central, which permits an ordered comparison of the
two averaged Choi states. The result is

$$
\mathrm{TD}(\Omega_{\mathrm c},\Omega_{\mathrm i})
\leq\frac{2mn}{d^2}.
$$

No later measurement can create a larger probability gap than this trace
distance. Therefore

$$
p\left(F-\frac1{d^2}\right)\leq\frac{2mn}{d^2},
\qquad
mn\geq\frac p2(d^2F-1).
$$

This argument permits arbitrary collective gates, ancillary memory and
adaptive measurements with bounded source budgets. Its all-dimensional
representation step is given in [Converse](../science/converse.md), with
the research-level dependencies distinguished from the textbook foundation
in [the source bridge](WATROUS_BRIDGE.md#research-bridges-supplied-by-the-project).

## 5. A known mathematical operation still needs a charged circuit

**Milestones M24–M26.** The polar normalization defines a valid processor,
but that alone does not count its gates. The explicit circuit uses two known
projectors: one onto whole-copy symmetry and one onto a selected Bell
subspace. Its projected block has the normalization needed for the polar
map; the Bell projector alone has the wrong singular spectrum.

Projected QSVT approximates the required singular-value transformation.
The actual input's spectral moments bound the weight of the troublesome
small singular values, so the proof does not assume a lower bound on every
nonzero singular value. Known permutation averaging implements the symmetry
phases. A quantum address is processed by visiting its possible register
locations explicitly, and those gates are counted.

The resulting conservative count is

$$
\widetilde O\left(d(m^2+n^2)(\log d+\log(m+n))\right)
$$

known gates, with logarithmic accuracy factors suppressed. At balanced,
fixed-error budgets, this gives a $\widetilde O(d^3)$ upper bound. The
physical program storage alone is $2(m+n)\lceil\log_2d\rceil$ qubits.
The circuit also uses $O(m\log(m+1)+n\log(n+1)+\log d)$ permutation and
work qubits and one QSVT control qubit. Computing the known QSVT phases
classically is separate from the quantum gate count. These costs, their
finite-error allocation and their imported QSVT ingredients are in
[Implementation](../science/implementation.md).

## 6. Read the resource law with its scope

**Milestones M27–M29.** At fixed accuracy and success requirements, a
sufficiently large constant times $d^2$ in copy product suffices for the
construction. The converse requires at least another constant times $d^2$.
Thus the threshold is $mn=\Theta(d^2)$, with constants depending on those
requirements. It does not claim an exact finite-copy optimum.

Balancing the supplies gives $m=n=\Theta(d)$ and minimizes the total
number supplied. If one pool has only one copy, the other needs order d²
copies. A scarcity in one pool can therefore be compensated by more of the
other, subject to the product law.

For small infidelity $\epsilon$, the collective construction has the
sufficient balanced allocation $O(d/\sqrt\epsilon)$. Independent paired
Bell trials give a different output-only allocation,
$O(d^2\log(1/\epsilon))$, because their designated successful outputs are
exact. The latter can use fewer copies at extremely small error. The fixed
error theorem does not determine the optimal precision dependence.

Returned programs are covered by one joint fidelity bound, but they need
not be exact, independent specimens. Reusing them in a long sequence would
require accumulated-error accounting. Finally, $d$ is a Hilbert-space
dimension: for a q-qubit operation, $d=2^q$. A linear copy count in d and a
cubic gate count in d do not mean polynomial complexity in q.

## 7. Connect the evidence to the result

**Milestone M30.** The central conclusion combines a legal collective
instrument, its dimension-dependent fidelity guarantee, a converse for
all processors, and an explicit charged implementation. Each part has a
separate role. The [verification guide](../verification/README.md) explains
the finite checks of register ordering, Gram moments, mixed Choi ensembles
and projected encodings, and distinguishes them from the all-dimensional
proofs.

Watrous provides the shared language. The
[related-work account](../references/RELATED_WORK.md) supplies attribution
for the PGM, teleportation, mixed-tensor representation theory and QSVT.
The project's conclusion is the composition resource law under the stated
copy access model. Return to the [milestone map](MILESTONES.md) to locate
the individual conceptual dependencies, or to the
[scientific account](../science/README.md) for the complete proofs.


## 8. Test the scope of a shared contraction method

**Milestones M19, M29–M30.** A related exact task is to prepare the canonical purification of a known-vacuum rank-two family from state/conjugate samples. The [comparison page](../science/canonical_purification_boundary.md) supplies its source states and target.

Both constructions begin with a linear map that has the desired coherent action. A physical success operator must also be a contraction on the whole input space. For the program composer, polar normalization produces a legal map and the Choi marginal moments control its distortion. Exact purification requires the accepted target direction to be preserved, so the sister proof first derives a residual-polynomial restriction from exactness and then optimizes the physical residual effect.

This gives a useful way to assess a proposed transfer. Check what correlations are supplied, what systems remain inaccessible, whether successful output is exact, and whether every rejected source request counts. Unitary Choi halves are maximally mixed, but extracted signal specimens are rank one. The corresponding moment proof therefore does not transfer. With one conjugate mixed specimen, a vacuum outcome alone prevents exact success and imposes a ceiling of one-half, regardless of the other budget.

The [canonical pure frontier](https://github.com/GoGoKo699/Canonical-Purification-Cost/blob/c0e1cac831e7bc6073042974c5f440bd847b37a0/science/exact_frontier.md) and [mixed-source frontier](https://github.com/GoGoKo699/Canonical-Purification-Cost/blob/c0e1cac831e7bc6073042974c5f440bd847b37a0/science/mixed_frontier.md) own those exact proofs. This repository's result remains the fixed-error unitary-program composition law. Shared methods explain the relationship without turning one theorem into a premise of the other.
