# Implementing the collective composer

The [collective construction](construction.md) defines a processor by the polar part of a known contraction. This page gives a circuit using ordered program copies, known permutations, Bell-state preparation, and quantum singular value transformation (QSVT). Its resource count includes coherent addressing of the program registers.

At global infidelity $\epsilon$, the circuit achieves the target using a copy-budget product $mn=O(d^2/\epsilon)$, chosen with the sufficient constant in (7), and uses

$$
\widetilde O\!\left(
 d(m^2+n^2)(\log d+\log(m+n))
\right)
$$

known elementary gates. The suppressed factors are logarithmic in $d,m,n,1/\epsilon$. For balanced pools at fixed error, this is $\widetilde O(d^3)$ gates. The copy-complexity improvement therefore does not establish a runtime improvement. No operation depending on a classical description of $U$ or $V$ is used.

## 1. A projected encoding on physical registers

Let $d\geq2$, $m,n\geq1$, and define the normalized input and ideal output

$$
\begin{aligned}
|v\rangle&=|U\rangle^{\otimes m}|V\rangle^{\otimes n},\\
|w\rangle&=|UV\rangle
 |U\rangle^{\otimes(m-1)}|V\rangle^{\otimes(n-1)}.
\end{aligned}
$$

Each Choi program has a row register and a column register. All copies occupy distinct, ordered physical registers. Define $P$ to be the orthogonal projector onto

$$
\mathcal S=\operatorname{Sym}^{m}(\mathbb C^{d^2})
\otimes\operatorname{Sym}^{n}(\mathbb C^{d^2}).
$$

The permutations defining $P$ exchange **whole two-register programs**. In particular, $P|v\rangle=|v\rangle$ for every pair $U,V$. No occupation-number encoding or bosonic hardware is assumed.

Choose the first program in each pool. Let $Q$ project the column register of the selected $U$ program and the row register of the selected $V$ program onto

$$
|\Phi_d\rangle=d^{-1/2}\sum_{j=0}^{d-1}|j,j\rangle.
$$

On the range of $Q$, let $J$ remove this fixed Bell ket and order the remaining registers as the selected outer pair, the remaining $U$ programs, and the remaining $V$ programs. Equivalently, $B=JQ$ is the corresponding Bell bra followed by this known routing. Then $B^\dagger B=Q$ and the rectangular contraction is

$$
A=BP=JQP.
$$

Before applying $J$, the triple $(Q,I,P)$ is a projected unitary encoding: the encoded operator is $QP$, between the right subspace $\mathcal S$ and the left subspace $\operatorname{range}Q$. Both projectors are known from $d,m,n$.

The Bell contraction gives the exact physical normalization

$$
A|v\rangle=\frac1d|w\rangle.
\tag{1}
$$

For comparison with the [polar construction](construction.md), set $M=\sqrt{dmn}\,A$ on $\mathcal S$. Thus

$$
M|v\rangle=\sqrt{\frac{mn}{d}}|w\rangle.
$$

There is no output symmetry measurement: after the chosen contraction, all unselected copies remain symmetric within their respective pools.

### The compressed Gram operator

Write $E_{rs}$ for the Bell projector between the inner halves of program $r$ in the first pool and program $s$ in the second. Separate permutation invariance implies

$$
PQP=\frac1{mn}P\left(\sum_{r=1}^{m}\sum_{s=1}^{n}E_{rs}\right)P.
$$

The sum commutes with $P$, although an individual summand generally does not. Writing $G_{\mathcal S}=G|_{\mathcal S}$ as in the construction, on $\mathcal S$ one has

$$
G=d\sum_{r,s}E_{rs},
\qquad
M^\dagger M=G_{\mathcal S},
\qquad
A^\dagger A=\frac{G_{\mathcal S}}{dmn}.
\tag{2}
$$

Equation (2) also proves $\|A\|\leq1$ and $\|M\|\leq\sqrt{dmn}$. The relevant singular spectrum is that of the **restricted block** $QP$. The unrestricted Bell projector has only zero and unit singular values and cannot by itself implement this polar transformation.

## 2. Approximating the polar map on the supplied states

The [moment calculation](construction.md) gives, for the spectral distribution of $G$ in $|v\rangle$,

$$
\mu=\mathbb E G=\frac{mn}{d},
\qquad
\operatorname{Var}(G)=mn(1-d^{-2}).
$$

Define

$$
X=\frac{G}{\mu},
\qquad
r=\mathbb E(X-1)^2=\frac{d^2-1}{mn}.
$$

The exact polar Kraus operator is $K=MG_{\mathcal S}^{-1/2}$, with the inverse zero on the kernel. Its target amplitude satisfies

$$
\langle w|K|v\rangle=\mathbb E\sqrt X\geq1-\frac r2.
\tag{3}
$$

For example, the scalar inequality $\sqrt{x}\geq(3x-x^2)/2$ for $x\geq0$ proves (3) using only the first two moments.

A circuit need not approximate the polar map uniformly on arbitrarily small nonzero singular values. Fix $0<\eta<1/2$. The bounded odd sign-approximation polynomial of Gilyén, Su, Low and Wiebe [1, Lemma 25] can be chosen so that

$$
|f(s)|\leq1\quad(-1\leq s\leq1),
\qquad
|f(s)-1|\leq\eta\quad\left(\frac1{2d}\leq s\leq1\right),
$$

with degree $T=O(d\log(1/\eta))$. Their real-polynomial projected-QSVT construction [1, Corollary 18] realizes $f^{\mathrm{SV}}(QP)$ as a block of a unitary, using a single additional control qubit and $O(T)$ controlled phases about $P$ and $Q$. The inverse in that construction is the inverse of a **known circuit**. It is not an inverse of either unknown program.

After removing the Bell ket, the successful Kraus operator is $Jf^{\mathrm{SV}}(QP)$. By (1) and (2), its target amplitude is

$$
a_f=\langle w|Jf^{\mathrm{SV}}(QP)|v\rangle
 =\mathbb E\left[\sqrt X\,f\!\left(\frac{\sqrt X}{d}\right)\right].
\tag{4}
$$

To verify (4), use an SVD $A=L\Sigma R^\dagger$: the identity $|w\rangle=dA|v\rangle$ assigns a factor $d\sigma=\sqrt X$ to the left singular component. An odd polynomial has $f(0)=0$, so zero singular values cause no extra term.

### Controlling the small-singular-value tail

The polynomial approximation applies whenever $X\geq1/4$. Chebyshev's inequality and $\sqrt X\leq1/2$ on the complementary event give

$$
\Pr[X<1/4]\leq\frac{16r}{9},
\qquad
\mathbb E[\sqrt X\,\mathbf1_{X<1/4}]\leq\frac{8r}{9}.
$$

On the large-singular-value event, the amplitude loss relative to (3) is at most $\eta\mathbb E\sqrt X\leq\eta$. On the complementary event, $|f|\leq1$ bounds that loss by twice its weighted mass. Thus

$$
a_f\geq1-\frac{41r}{18}-\eta.
\tag{5}
$$

No minimum-nonzero-singular-value promise was used. The cutoff is justified by the spectral weight of the actual program inputs.

## 3. Deterministic completion and finite precision

The QSVT circuit has an explicit success flag: the control qubit is projected back onto its designated state and the physical state lies in the range of $Q$. On that event, unprepare the known Bell ket, discard its now fixed registers, and use the remaining wires as the output. On failure, discard the registers and prepare any fixed state in the same output space. This defines a trace-preserving channel. Its failure contribution to the overlap with $|w\rangle$ is nonnegative.

Suppose the implemented circuit differs from the ideal QSVT unitary by at most $\nu$ in operator norm. Projection and removal of the Bell ket cannot increase that error. Equations (4) and (5) therefore give

$$
F_{\mathrm{global}}
\geq1-\frac{41}{9}r-2\eta-2\nu,
\tag{6}
$$

whenever $41r/18+\eta+\nu\leq1$. Here fidelity means the pure-target overlap, as throughout the repository.

A concrete sufficient allocation for any $0<\epsilon<1$ is

$$
mn\geq\frac{41(d^2-1)}{3\epsilon},
\qquad
\eta\leq\frac\epsilon6,
\qquad
\nu\leq\frac\epsilon6.
\tag{7}
$$

Then (6) is at least $1-\epsilon$. The constants in (7) describe this cutoff implementation; the exact polar channel satisfies the stronger bound $1/(1+r)\geq1-r$ proved in the construction. Neither statement establishes optimal dependence on $\epsilon\to0$.

## 4. Known phases about the symmetric input subspace

It remains to implement the phases required by QSVT without invoking an unknown-state reflection. For a pool of $k$ whole programs, use a Fisher–Yates encoding of permutations. At step $t=2,\ldots,k$, a register $j_t$ ranges uniformly over $0,\ldots,t-1$, and the selected transposition exchanges positions $t-1$ and $j_t$. Every permutation occurs once among the $k!$ valid choice strings.

Let $F_k$ prepare the product of these uniform-range states and let $\mathrm{SELECT}_k$ apply the corresponding whole-copy permutations. Padding labels outside the valid ranges may be assigned any known unitary. They have zero initial amplitude. Define

$$
V_k=(F_k^\dagger\otimes I)\,\mathrm{SELECT}_k\,(F_k\otimes I).
$$

Its clean-ancilla block is exactly the symmetry projector:

$$
(\langle0|\otimes I)V_k(|0\rangle\otimes I)
 =\frac1{k!}\sum_{\pi\in S_k}U_\pi
 =P_k.
\tag{8}
$$

For the two pools take $V=V_m\otimes V_n$ and let $\Pi_0$ project all permutation ancillas onto zero. Equation (8) gives

$$
(\langle0|\otimes I)V^\dagger(2\Pi_0-I)V(|0\rangle\otimes I)
 =2P-I.
\tag{9}
$$

The right-hand side is unitary. Since the full operator on the left is also unitary, there can be no norm left in nonzero ancilla states for any clean-ancilla input. Thus (9) is an exact deterministic symmetry reflection with clean ancilla return.

More generally,

$$
V^\dagger e^{i\phi(2\Pi_0-I)}V
$$

implements $e^{i\phi(2P-I)}$ on clean ancillas. This follows by expanding the exponential into $\cos\phi\,I+i\sin\phi(2\Pi_0-I)$ and using (9). Adding the single QSVT control qubit changes the gate count by a constant factor. The Bell-subspace phases are implemented by preparing and unpreparing the known $|\Phi_d\rangle$ and phasing the all-zero state.

## 5. Charged circuit resources

Let $q=\lceil\log_2d\rceil$. Embed each physical qudit in $q$ qubits. Whole-copy permutations preserve the valid $d$-dimensional subspaces, and the Bell projector has its stated action on them.

A controlled swap of two whole Choi programs costs $O(q)$ elementary gates. At Fisher–Yates step $t$, the address $j_t$ is quantum. Implement its selected swap by visiting all $t$ possible addresses, computing an equality flag, swapping under that flag, and uncomputing. This costs

$$
O\bigl(t(q+\log t)\bigr)
$$

gates. Summing over the steps costs $O(k^2(q+\log k))$. This explicit loop is why the count is quadratic in the pool size; it assumes neither QRAM nor free coherent routing.

Uniform-range state preparation uses only known angles. One explicit construction follows the binary prefixes of the allowed interval: branch amplitudes are square roots of the numbers of allowed completions. At each depth there is at most one partially filled prefix; all fully filled branches use Hadamards. Controlled rotations at the boundary give an $O(\log^2 t)$ preparation for a range of length $t$. Its inverse has the same cost. The same construction prepares a uniform range of length $d$ for Bell-state preparation, followed by copying its binary label with CNOTs.

The resulting resources are:

| Resource | Conservative upper bound |
|---|---:|
| Supplied program qubits | $2(m+n)\lceil\log_2d\rceil$ |
| Permutation registers and reversible work | $O(m\log(m+1)+n\log(n+1)+\log d)$ qubits |
| QSVT control | One additional qubit |
| Controlled symmetry phase | $\widetilde O((m^2+n^2)(\log d+\log(m+n)))$ gates |
| QSVT degree | $O(d\log(1/\epsilon))$ |
| Complete circuit | $\widetilde O(d(m^2+n^2)(\log d+\log(m+n)))$ gates |

All gate descriptions depend only on $d,m,n,\epsilon$. The polynomial and QSVT phases can be computed classically using the constructive results of [1]; this known preprocessing is separate from the quantum gate count. For a fixed finite inverse-closed universal gate set, approximate each of the $L$ known elementary gates to operator error at most $\nu/L$. A telescoping bound gives total unitary error at most $\nu$. Standard constructive gate synthesis adds a polylogarithmic factor in $L/\nu$ [2], included in the displayed soft-$O$ bounds.

With $m=n=O(d/\sqrt\epsilon)$ chosen large enough for (7), the circuit uses $\widetilde O(d^3/\epsilon)$ gates and $O((d/\sqrt\epsilon)\log(d/\epsilon))$ qubits. This is polynomial in the dimension and supplied-copy counts. It is not a claim of a gate complexity polynomial in $\log d$.

The entire returned state is covered by the same global fidelity in (6). That one-shot statement does not establish an indefinite catalyst or the accumulated error of a long sequence of compositions.

## 6. Finite verification and its limits

Run:

```bash
OPENBLAS_NUM_THREADS=1 python verification/check_projected_encoding.py
```

The script constructs full ordered-register projectors and Bell contractions. It checks the compressed Gram normalization (2), the action $A|v\rangle=|w\rangle/d$ on seeded random unitary programs, and the distinction between the binary Bell spectrum and the compressed spectrum. Its cases are $d=2$ with $(m,n)=(1,1),(2,1),(2,2),(3,1)$, and $d=3$ with $(m,n)=(1,2)$.

A second check constructs the padded permutation registers explicitly for pools of two and three qubit programs. It verifies the clean-ancilla block (8), a nontrivial symmetry phase, and zero leakage from clean ancillas. The dense uniform-state matrix used in this small test verifies the operator identity; the elementary gate count is established by the addressed-swap and prefix-preparation constructions above.

The script does not synthesize a QSVT phase sequence or simulate a fault-tolerant circuit. The uniform polynomial approximation, phase construction, and gate-synthesis bounds are imported theorems; the state-dependent cutoff, normalization, fidelity estimate, and charged projector implementation are the application proved here.

## References

1. A. Gilyén, Y. Su, G. H. Low and N. Wiebe, *Quantum singular value transformation and beyond: exponential improvements for quantum matrix arithmetics*, STOC 2019, pp. 193–204. [arXiv:1806.01838v1](https://arxiv.org/abs/1806.01838v1), Corollary 18, Lemma 25 and Theorem 26. The numbered statements refer to the full arXiv version.
2. C. M. Dawson and M. A. Nielsen, *The Solovay–Kitaev algorithm*, Quantum Information & Computation **6**, 81–95 (2006). [arXiv:quant-ph/0505030v2](https://arxiv.org/abs/quant-ph/0505030v2).
