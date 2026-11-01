# Why the copy budgets must have product of order d²

The lower bound allows an arbitrary collective quantum processor. It therefore
tests the information present in the supplied programs, rather than the
limitations of a chosen Bell measurement or circuit. The construction and this
converse meet in their dependence on dimension at every fixed target error.

The proof has two parts. First, two ensembles of program states remain close
until the product of their copy counts reaches order d². Second, a successful
universal composer would distinguish those ensembles by asking whether their
product is the identity.

## Theorem: universal composition requires a large copy product

For a unitary $U\in\mathrm U(d)$, use the normalized Choi convention

**Equation (1).**

$$
|U\rangle=\frac{1}{\sqrt d}\sum_{i,j=1}^d U_{ij}|i\rangle|j\rangle,
\qquad \psi_U=|U\rangle\langle U|.
$$

Let a quantum instrument receive $m\geq1$ copies of $\psi_U$ and $n\geq1$
copies of $\psi_V$. Both halves of every program are accessible. Its other
ancillas, gates and controls are independent of the unknown $U,V$; in
particular, it has no further calls to their channels, state-preparation
unitaries or inverses. Suppose that, for every pair $U,V$, the instrument
declares success with probability at least $p_0>0$ and its conditional output
has fidelity at least $F_0$ with $|UV\rangle$. Throughout this page, fidelity
with a pure target means $\langle UV|\rho|UV\rangle$.

For $d\geq2$ and $F_0\geq d^{-2}$,

$$
\boxed{mn\geq\frac{p_0}{2}\bigl(d^2F_0-1\bigr).}
$$

The copy budgets are worst-case bounds, including all branches of an adaptive
protocol. A protocol with those bounds can precollect its copies and apply
one instrument, so adaptive measurements and arbitrary ancillary memory are
covered. No bound is imposed on the processor's known-gate complexity.

For fixed positive $p_0,F_0$, equation (1) gives $mn=\Omega(d^2)$ as
$d\to\infty$. Thus balanced supplies require $m+n=\Omega(d)$, while a single
copy in one pool requires order d² copies in the other. The lower bound asks
only for the composed output. It also applies to a processor promising a
larger joint output with returned programs, since tracing those out can only
increase the fidelity with the corresponding pure target.

## 1. Correlated programs and independent programs

Define two density operators, using normalized Haar measure:

**Equation (2).**

$$
\begin{aligned}
\Omega_{\mathrm c}
 &=\mathbb E_U
   \psi_U^{\otimes m}\otimes\psi_{\overline U}^{\otimes n},\\
\Omega_{\mathrm i}
 &=\mathbb E_{U,W}
   \psi_U^{\otimes m}\otimes\psi_{\overline W}^{\otimes n}.
\end{aligned}
$$

Here $U,W$ are independent in the second line. Complex conjugation in this
definition describes an ensemble; it is not an operation that the processor
is allowed to perform on an unknown state. In the eventual reduction, a
physical SWAP of the halves of $|U^\dagger\rangle$ produces
$|\overline U\rangle$.

**Moment comparison.** For every $d\geq2$ and $m,n\geq1$,

**Equation (3).**

$$
\mathrm{TD}(\Omega_{\mathrm c},\Omega_{\mathrm i})
:=\frac12\Vert\Omega_{\mathrm c}-\Omega_{\mathrm i}\Vert_1
\leq\min\lbrace1,\frac{2mn}{d^2}\rbrace.
$$

The proof of (3) uses the mixed-tensor commutant and its traceless subspace.
Its generators and the centrality of the traceless projector hold in every
dimension; a faithful representation of the abstract walled Brauer algebra
is unnecessary. Precise primary references are Goncharov, Theorem 2.3 and
Proposition 2.4, and Grinko–Ozols, Theorem 3.8 [1,2]. The moment comparison
below is an application of those established representation facts.

### 1.1 A large common harmonic subspace

Regroup the first halves of all Choi copies into $K_A$ and their second halves
into $K_B$, where

**Equation (4).**

$$
K=(\mathbb C^d)^{\otimes m}\otimes
  (\overline{\mathbb C^d})^{\otimes n},
\qquad D=\dim K=d^{m+n}.
$$

In standard coordinates the conjugate factors have the same underlying
Hilbert space as $\mathbb C^d$. The two moments in (2) are obtained by
twirling the first half of $|\Phi_D\rangle\langle\Phi_D|$ under

$$
R(U)=U^{\otimes m}\otimes\overline U^{\otimes n},
\qquad
S(U,W)=U^{\otimes m}\otimes\overline W^{\otimes n}.
$$

For each pair consisting of one first-pool factor and one second-pool
factor, let $C_{ij}$ contract those factors by the canonical pairing
$\langle\Phi_d|\sqrt d$. Define

**Equation (5).**

$$
H=\bigcap_{i=1}^m\bigcap_{j=1}^n\ker C_{ij},
\qquad P=\Pi_H,
\qquad q=1-\frac{\dim H}{D}.
$$

Every contraction has rank $d^{m+n-2}$. The codimension of an intersection
is at most the sum of the codimensions, so

**Equation (6).**

$$
q\leq\frac{mn}{d^2}.
$$

The projection $P$ is real in the standard basis. It commutes with $R(U)$
and with permutations inside each pool. It need not commute with $S(U,W)$.
That last distinction matters: the independent moment will commute with
$P\otimes\overline P$ for a different reason established below.

### 1.2 Why the harmonic decomposition works in every dimension

Let $\mathcal B$ be the commutant of the representation $R$. By mixed
Schur–Weyl duality, $\mathcal B$ is generated by within-pool permutations and
the contraction-insertion operators $Q_{ij}=C_{ij}^\dagger C_{ij}$ [1,2].
Each $Q_{ij}$ is self-adjoint and annihilates $H$, hence
$Q_{ij}P=PQ_{ij}=0$. Therefore $P$ commutes with every generator of
$\mathcal B$. Since $P$ also commutes with $R(U)$, it lies in $\mathcal B$
and is central there.

For a unitary representation, central projections of its commutant select
entire isotypic components. Thus no irreducible representation of $R$ occurs
both in $H$ and in $H^\perp$. This establishes the absence of cross terms
when the correlated Choi moment is projected onto $H$ on both halves.

To identify the multiplicities on $H$, first apply ordinary Schur–Weyl
duality separately to the two pools:

**Equation (7).**

$$
K=\bigoplus_a V_a\otimes M_a,
\qquad
V_a=V_\lambda\otimes\overline{V_\nu},
\qquad M_a=M_\lambda\otimes M_\nu.
$$

The index $a=(\lambda,\nu)$ ranges over partitions of $m,n$ with at most d
rows. The spaces $V_a$ are inequivalent irreducible representations of the
product group in (4), while $M_a$ are the corresponding inequivalent
irreducible representations of $S_m\times S_n$. Write
$v_a=\dim V_a$ and $f_a=\dim M_a$.

Because $P$ commutes with the within-pool permutation algebra, its range has
the form

**Equation (8).**

$$
H=\bigoplus_a W_a\otimes M_a,
\qquad W_a\subseteq V_a,
\qquad 0\leq w_a:=\dim W_a\leq v_a.
$$

The compressed commutant $P\mathcal B P$ is exactly the represented
within-pool permutation algebra on $H$. Indeed, in any word in the
generators of $\mathcal B$, a contraction-insertion factor can be moved next
to $P$ and kills the compression. Words with only permutation factors give
the whole remaining algebra. Centrality also means that any operator on
$H$ commuting with $R|_H$ extends by zero to an element of $\mathcal B$.
Consequently this compressed algebra is the full commutant of $R|_H$.

The finite-dimensional double-commutant theorem now shows that every nonzero
$W_a$ is irreducible under $R$ and that distinct nonzero $W_a$ are
inequivalent. Their multiplicity spaces are exactly the $M_a$ in (8).
Some $W_a$ vanish in small dimensions; those sectors are simply omitted.
This argument uses the represented matrix algebra and has no restriction
such as $m+n\leq d$.

### 1.3 The two harmonic moment blocks are ordered

For clarity, the general Choi-twirl formula is useful. If a D-dimensional
unitary representation has decomposition
$\bigoplus_a V_a\otimes M_a$ with inequivalent irreducible $V_a$, its
maximally entangled vector decomposes as

**Equation (9).**

$$
|\Phi_D\rangle
=\bigoplus_a\sqrt{\frac{v_af_a}{D}}
   |\Phi_{V_a}\rangle\otimes|\Phi_{M_a}\rangle.
$$

Schur orthogonality removes cross terms between inequivalent $V_a$ and
replaces the density operator on each $V_a$ by $I_{V_a}/v_a$. The resulting
Choi moment is therefore

$$
\bigoplus_a\frac{f_a}{D v_a}
 I_{V_a,A}\otimes I_{\overline{V_a},B}
 \otimes|\Phi_{M_a}\rangle\langle\Phi_{M_a}|.
$$

Paired conjugate bases are used on the two Choi halves. Applying (9) to the
independent group gives $\Omega_{\mathrm i}$. Put
$\Pi=P_A\otimes\overline P_B$; since $P$ is real, this is also $P\otimes P$.
The identity operators in (9), together with the block form (8), imply that
$\Omega_{\mathrm i}$ commutes with $\Pi$ even though $P$ is not invariant
under the independent group.

Set $B=\Pi\Omega_{\mathrm i}\Pi$. Its expression is (9) with both $V_a$
factors restricted to $W_a$, while retaining the denominator $v_a$.
For the correlated moment, centrality and the irreducibility established
above give

**Equation (10).**

$$
A:=\Pi\Omega_{\mathrm c}\Pi
=\bigoplus_{a:w_a>0}\frac{f_a}{D w_a}
 I_{W_a,A}\otimes I_{\overline{W_a},B}
 \otimes|\Phi_{M_a}\rangle\langle\Phi_{M_a}|.
$$

The correlated moment also commutes with $\Pi$, because $H$ and $H^\perp$
contain disjoint correlated-group irreducible representations. The two
compressed moments have the same positive blocks and $w_a\leq v_a$.
Consequently,

**Equation (11).**

$$
A\succeq B,
\qquad
\mathrm{tr}A=\frac1D\sum_a f_aw_a=1-q.
$$

Moreover, using $w^2/v\geq2w-v$,

**Equation (12).**

$$
\mathrm{tr}B
=\frac1D\sum_a\frac{f_aw_a^2}{v_a}
\geq1-2q.
$$

Let $\delta=\mathrm{tr}(A-B)$. Equations (11)–(12) give
$0\leq\delta\leq q$. Block diagonality implies that
$\Omega_{\mathrm c}-A$ and $\Omega_{\mathrm i}-B$ are positive, with traces
$q$ and $q+\delta$. The triangle inequality therefore gives

**Equation (13).**

$$
\begin{aligned}
\frac12\Vert\Omega_{\mathrm c}-\Omega_{\mathrm i}\Vert_1
&\leq\frac12\bigl(\delta+q+(q+\delta)\bigr)\\
&=q+\delta\leq2q\leq\frac{2mn}{d^2}.
\end{aligned}
$$

Together with the universal trace-distance bound of one, this proves (3).

## 2. Turning a composer into a correlation test

Let $\Lambda_{\mathrm s}$ be the successful completely positive map of a
purported composer, after any unwanted output registers have been traced
out. Introduce independent known Haar unitaries $A,B,C$ and transform every
input copy according to

**Equation (14).**

$$
(U,V)\longmapsto(AUB^\dagger,\ BVC^\dagger).
$$

These transformations are the known gates $A\otimes\overline B$ on the
first pool and $B\otimes\overline C$ on the second. Run the original
composer and, on success, apply $A^\dagger\otimes C^T$ to its output. Haar
averaging defines a new admissible instrument. An information-theoretic
converse may grant this randomization without claiming an efficient circuit
for continuous Haar sampling.

The action (14) is transitive on unitary pairs. The symmetrized instrument
therefore has constant success probability $p$ and constant conditional
target fidelity $F$, with $p\geq p_0$ and $F\geq F_0$. These inequalities
remain true for a state-dependent success probability in the original
instrument: target fidelity is a linear constraint on its unnormalized
successful output, and can be averaged before dividing by $p$.

At $(U,V)=(I,I)$, the stabilizer of (14) is $A=B=C=g$. It acts on the
output as $g\otimes\overline g$. The two inequivalent irreducible sectors
are the span of $|\Phi_d\rangle$ and its orthogonal complement, corresponding
to scalar and traceless matrices. Covariance consequently gives the
successful normalized output

**Equation (15).**

$$
\rho_{U,V}
=F\psi_{UV}+\frac{1-F}{d^2-1}(I-\psi_{UV}).
$$

Now compare two priors on the original input programs:

1. $U$ is Haar and $V=U^\dagger$. The target is always $|I\rangle$.
2. $U,V$ are independent Haar unitaries. Their product is Haar.

Swapping the two physical halves of every V program changes the first input
ensemble into $\Omega_{\mathrm c}$ and the second into
$\Omega_{\mathrm i}$. This is a unitary change of registers, so their trace
distance is exactly the one bounded in (3).

Consider the event that the composer succeeds and its output passes the
projection onto $|I\rangle=|\Phi_d\rangle$. By (15), its probability is
$pF$ under the first prior. Under the second prior,
$\mathbb E_{U,V}\psi_{UV}=I/d^2$, so its probability is $p/d^2$.
Contractivity of trace distance under the entire instrument and final test
gives

**Equation (16).**

$$
p\left(F-\frac1{d^2}\right)
\leq\mathrm{TD}(\Omega_{\mathrm c},\Omega_{\mathrm i})
\leq\frac{2mn}{d^2}.
$$

Substituting $p\geq p_0$ and $F\geq F_0\geq d^{-2}$ proves (1).

### Haar-average performance

The same symmetrization also identifies a useful scope detail. For any fixed
pair $U,V$, the two transformed unitaries in (14) are independent Haar
unitaries. If the original instrument has Haar-average success probability
$\bar p$ and Haar-average unnormalized target overlap

**Equation (17).**

$$
\bar s=\mathbb E_{U,V}
\langle UV|\Lambda_{\mathrm s}
 (\psi_U^{\otimes m}\otimes\psi_V^{\otimes n})|UV\rangle,
$$

then the symmetrized instrument has $p=\bar p$ and $pF=\bar s$.
Thus (16) also implies

$$
\bar s-\frac{\bar p}{d^2}\leq\frac{2mn}{d^2}.
$$

In particular, deterministic Haar-average fidelity is covered. For heralded
procedures, the relevant average conditional fidelity is
$\bar s/\bar p$, weighted by success probability. An unweighted average of
conditional fidelities is a different statistic and should not be silently
substituted into (17). No conclusion for an arbitrary non-Haar promise
distribution is asserted here.

## 3. Verification and boundaries

The mathematical proof establishes (1) in every dimension. The script
[`verification/check_mixed_moments.py`](../verification/check_mixed_moments.py)
provides a separate finite-matrix check: it evaluates Haar moments through
the pseudoinverse of the invariant-tensor Gram matrix, then constructs the
two ensembles by partial transposition and independent tensor products.
This route uses Haar-integration identities [3], rather than the harmonic
block formulas being tested.

The script checks positivity and normalization of both ensembles,
commutation with $P\otimes P$, the positive ordering $A\succeq B$, the two
discarded masses, and the trace-distance estimate. Its fixed cases include
$d=2,(m,n)=(1,3)$ and $(2,2)$, where $m+n>d$. In the one-copy case it also
checks the analytic calibration

$$
\mathrm{TD}(\Omega_{\mathrm c},\Omega_{\mathrm i})
=\frac{2(d^2-1)}{d^4}\qquad(m=n=1).
$$

These computations use floating-point arithmetic, with tolerance stated in
the script. They test normalization and the potentially delicate block
relations at those sizes; they are not an independent asymptotic proof.

The converse matches the construction's dimension dependence at fixed error.
It does not establish optimal constants, optimal dependence on an error that
vanishes with d, a runtime lower bound, or a theorem for merely expected copy
budgets. Returning the unused programs is an additional constructive
guarantee, not an assumption used in the lower bound.

## References

1. Y. O. Goncharov, *Traceless projection of mixed tensor products, and walled
   Brauer algebras*, arXiv:2511.00303v1 (2025).
   [Primary text](https://arxiv.org/html/2511.00303v1), Theorem 2.3 and
   Proposition 2.4. These give the all-dimensional commutant generators and
   central traceless projector.
2. D. Grinko and M. Ozols, *Linear Programming with Unitary-Equivariant
   Constraints*, Communications in Mathematical Physics **405**, 278 (2024).
   [DOI](https://doi.org/10.1007/s00220-024-05108-1);
   [arXiv:2207.05713v2](https://arxiv.org/abs/2207.05713v2).
   Theorem 3.8 states the mixed Schur–Weyl mutual-centralizer relation.
3. B. Collins and P. Śniady, *Integration with Respect to the Haar Measure on
   Unitary, Orthogonal and Symplectic Group*, Communications in Mathematical
   Physics **264**, 773–795 (2006).
   [DOI](https://doi.org/10.1007/s00220-006-1554-3);
   [arXiv:math-ph/0402073](https://arxiv.org/abs/math-ph/0402073).
