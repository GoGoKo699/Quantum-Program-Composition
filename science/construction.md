# Collective construction and returned programs

The composition processor selects one pair of ports jointly from two pools. Its measurement acts on the inner halves of the programs; a known permutation then routes the selected outer halves to the output. A square-root normalization accounts for all possible port pairs without applying any correction that depends on the unknown unitaries.

This page proves the construction on ordinary ordered registers. The finite circuit and its charged gate cost are given in [Implementation](implementation.md); the information-theoretic lower bound is proved in [Converse](converse.md).

## The global output guarantee

Fix $d\geq2$ and integers $m,n\geq1$. Use the row-first convention

**Equation (1).**

$$
|U\rangle=\frac1{\sqrt d}\sum_{i,j=0}^{d-1}U_{ij}|i\rangle|j\rangle,
\qquad
|V\rangle=\frac1{\sqrt d}\sum_{j,k=0}^{d-1}V_{jk}|j\rangle|k\rangle.
$$

The input and ideal global output are

$$
v=|U\rangle^{\otimes m}|V\rangle^{\otimes n},
\qquad
w=|UV\rangle\otimes|U\rangle^{\otimes(m-1)}
             \otimes|V\rangle^{\otimes(n-1)}.
$$

All factors in these expressions are normalized. Fidelity with a pure target means the squared-overlap convention $F(\rho,w)=\langle w|\rho|w\rangle$.

**Construction theorem.** There is a completely positive, trace-preserving processor depending only on $d,m,n$ whose output obeys, for every pair of unitaries $U,V$,

$$
F_{\mathrm{global}}
\geq \frac{mn}{mn+d^2-1}
\geq 1-\frac{d^2-1}{mn}.
$$

The processor receives only the stated copies. Both halves of every copy are accessible. It receives no unitary description, query access, preparation inverse, or reflection about an unknown program state. The copies returned in $w$ are part of the same global fidelity guarantee; they are not asserted to be exact or indefinitely reusable.

## 1. A physical instrument on two pools

Write the copy indexed by $r$ of $U$ on registers $(A_r,B_r)$ and the copy indexed by $s$ of $V$ on $(C_s,D_s)$. The inner registers are $B_1,\ldots,B_m,C_1,\ldots,C_n$. Let

**Equation (2).**

$$
|\Phi_d\rangle=\frac1{\sqrt d}\sum_{j=0}^{d-1}|j,j\rangle,
\qquad
E_{rs}=|\Phi_d\rangle\langle\Phi_d|_{B_rC_s}\otimes I_{\mathrm{rest}},
\qquad
G=d\sum_{r=1}^m\sum_{s=1}^n E_{rs}.
$$

The identity in each $E_{rs}$ acts on the other inner registers. The same operators act as the identity on every outer register when used on the full input. Different $E_{rs}$ need not commute.

Let $L_{rs}$ contract $B_rC_s$ with $\langle\Phi_d|$, then route $A_r,D_s$ into the two output registers. It places the remaining whole $U$ copies first and the remaining whole $V$ copies second, in increasing original index order. Thus all $L_{rs}$ have the same output Hilbert space, and

**Equation (3).**

$$
L_{rs}^{\dagger}L_{rs}=E_{rs}.
$$

Define inverse square roots to vanish on the kernel, and set

**Equation (4).**

$$
J_{rs}=\sqrt dL_{rs}G^{-1/2}.
$$

These maps form a valid incomplete instrument on the entire ordered input space, since

**Equation (5).**

$$
\sum_{r,s}J_{rs}^{\dagger}J_{rs}
=G^{-1/2}\left(d\sum_{r,s}E_{rs}\right)G^{-1/2}
=\Pi_{\mathrm{supp}G}\leq I.
$$

On the complementary effect, discard the input and prepare any fixed normalized state $\sigma_0$ on the output space. This defines the channel

**Equation (6).**

$$
\mathcal E(\rho)=\sum_{r,s}J_{rs}\rho J_{rs}^{\dagger}
 +\mathrm{Tr}\left[(I-\Pi_{\mathrm{supp}G})\rho\right]\sigma_0.
$$

The first term can be implemented with a classical outcome $(r,s)$ followed by the prescribed register routing. Equation (6) discards that outcome. The second term supplies a deterministic completion; it does not assert an exact target state upon a success flag.

### Relation to the pretty-good measurement

On the $m+n$ inner registers, the known density operators

**Equation (7).**

$$
\sigma_{rs}=\frac{E_{rs}}{d^{m+n-2}}
$$

with equal priors $1/(mn)$ have average $G/(mnd^{m+n-1})$. Their pretty-good measurement has effects

$$
dG^{-1/2}E_{rs}G^{-1/2}=J_{rs}^{\dagger}J_{rs}.
$$

The square-root measurement is established machinery [1]. Its use in port-based teleportation, second-moment fidelity bounds, and approximate preservation of unused resource ports are developed in [2]. Here the index set selects one port from each of two unknown-program pools. The normalization itself is not a new general measurement method.

## 2. Symmetry identifies the common successful state

The input belongs to the known subspace

$$
\mathcal S=\mathrm{Sym}^{m}(\mathbb C^{d^2})
          \otimes\mathrm{Sym}^{n}(\mathbb C^{d^2}),
$$

where the symmetrization permutes **whole two-register copies** within each pool. Let $P$ be its orthogonal projector. The sum $G$ commutes with these permutations and therefore preserves $\mathcal S$. After the common routing convention, symmetry also gives

$$
L_{rs}P=L_{11}P
\qquad\text{for every }r,s.
$$

Indeed, a permutation can send the selected copy in either pool to the first position. It fixes every vector in $\mathcal S$; any resulting permutation of the surviving whole copies fixes their separately symmetric output. This proves (7) on the full subspace, including states other than identical-copy products.

Let $L$ be the restriction of $L_{11}$ to $\mathcal S$, and let $G_{\mathcal S}$ be the restriction of $G$ to $\mathcal S$. Introduce the scaled contraction

**Equation (8).**

$$
M=\sqrt{dmn}L.
$$

For vectors in $\mathcal S$, equations (3) and (7) imply

$$
M^{\dagger}M=G_{\mathcal S}.
$$

Here the adjoint of $M$ is taken with domain $\mathcal S$. Equivalently, on the full input space $(\sqrt{dmn}L_{11}P)^{\dagger}(\sqrt{dmn}L_{11}P)=PGP$. Individual Bell projectors need not preserve $\mathcal S$; their complete sum does.

The row-first convention fixes the product order. Direct contraction gives

**Equation (9).**

$$
(\langle\Phi_d|_{B_1C_1}\otimes I)
   (|U\rangle_{A_1B_1}|V\rangle_{C_1D_1})
=\frac1d|UV\rangle_{A_1D_1}.
$$

Consequently,

**Equation (10).**

$$
Lv=\frac1d w,
\qquad
Mv=\sqrt\muw,
\qquad
\mu=\frac{mn}{d}.
$$

Let $K=MG_{\mathcal S}^{-1/2}$ be the polar partial isometry, zero on the kernel. It is a contraction, with $K^{\dagger}K=\Pi_{\mathrm{supp}G_{\mathcal S}}$. Since $G^{-1/2}$ preserves $\mathcal S$, every routed physical branch satisfies

**Equation (11).**

$$
J_{rs}v=\frac1{\sqrt{mn}}Kv.
$$

Summing the $mn$ branches therefore produces the unnormalized pure state $Kv\langle v|K^{\dagger}$. In particular, the useful contribution to global fidelity is exactly

**Equation (12).**

$$
f_{\mathrm{pol}}=|\langle w|Kv\rangle|^2
=\frac{\langle v|\sqrt G|v\rangle^2}{\mu}.
$$

Equation (12) uses $w=Mv/\sqrt\mu$ and (8). It is an identity for the actual instrument, not an assumption that coherent port labels or physical bosonic modes are available.

## 3. Exact first and second moments

Every inner half of a unitary Choi state is maximally mixed. Since the supplied specimens are independent copies, the joint inner marginal of $v$ is $I/d^{m+n}$. Thus, for any spectral function $h$ of the inner operator $G$,

**Equation (13).**

$$
\langle v|h(G)|v\rangle
=\frac{\mathrm{Tr}_{\mathrm{inner}}h(G)}{d^{m+n}}.
$$

The distribution is independent of $U,V$. Put $Q_{rs}=dE_{rs}$ and write $\mathbb E$ for this normalized trace. Then

**Equation (14).**

$$
\mathbb E Q_{rs}=\frac1d,
\qquad
\mathbb E Q_{rs}^{2}=1,
\qquad
\mathbb E(Q_{rs}Q_{tu})=\frac1{d^2}
\quad\text{if }(r,s)\ne(t,u).
$$

For disjoint pairs the last identity factors. For pairs sharing one register, take the partial trace over the two unshared registers: each Bell projector has reduced operator $I/d$, giving the same normalized trace. This calculation does not replace the noncommuting projectors by independent classical variables.

There are $mn$ diagonal terms and $(mn)^2-mn$ ordered off-diagonal terms in $G^2$. Therefore

**Equation (15).**

$$
\begin{aligned}
\mathbb E G&=\frac{mn}{d}=\mu,\\
\mathbb E G^2&=mn+\frac{m^2n^2-mn}{d^2},\\
\mathrm{Var}G&=mn(1-d^{-2}).
\end{aligned}
$$

For $X=G/\mu$, these identities become

**Equation (16).**

$$
\mathbb E X=1,
\qquad
\mathbb E X^2=1+r,
\qquad
r=\frac{d^2-1}{mn}.
$$

## 4. Fidelity and success probability

By Hölder's inequality with exponents $3/2$ and $3$,

**Equation (17).**

$$
1=\mathbb E X
=\mathbb E\left[(\sqrt X)^{2/3}(X^2)^{1/3}\right]
\leq (\mathbb E\sqrt X)^{2/3}(\mathbb E X^2)^{1/3}.
$$

It follows that

$$
f_{\mathrm{pol}}=(\mathbb E\sqrt X)^2
\geq\frac1{1+r}=\frac{mn}{mn+d^2-1}.
$$

The failure term in (6) adds a nonnegative target overlap, so $F_{\mathrm{global}}\geq f_{\mathrm{pol}}$. The second inequality in (1) is the elementary relation $1/(1+r)\geq1-r$. This proves the theorem, including budgets for which the simpler $1-r$ bound is negative.

The success probability of the incomplete instrument is

**Equation (18).**

$$
p=\langle v|\Pi_{\mathrm{supp}G}|v\rangle
=\frac{\mathrm{rank}G}{d^{m+n}}
\geq\frac{(\mathbb E G)^2}{\mathbb E G^2}
=\frac1{1+r}.
$$

The inequality follows from Cauchy–Schwarz applied to $G1_{G>0}$. Conditional on success, the normalized output is $Kv/\sqrt p$ and has global fidelity $f_{\mathrm{pol}}/p$. In general it is only approximately $w$. Equations (17) and (18) must not be interpreted as exact composition on every successful branch.

## 5. Copy budgets and the precision boundary

For $0<\epsilon<1$, the exact channel achieves global infidelity at most $\epsilon$ whenever

**Equation (19).**

$$
mn\geq\frac{(1-\epsilon)(d^2-1)}{\epsilon}.
$$

The convenient sufficient condition $mn\geq(d^2-1)/\epsilon$ follows from the simpler form of (1). Balanced supplies therefore use $O(d/\sqrt\epsilon)$ copies of each source. At any fixed error, $O(d)$ copies per source suffice. With $m=1$, the sufficient budget for the other source is $n=O(d^2/\epsilon)$.

A single paired Bell trial produces exactly $|UV\rangle$ on its designated outcome, with probability $1/d^2$ by (9). With $k$ disjoint pairs, accepting the first such outcome gives failure probability $(1-d^{-2})^k$. Completing that protocol with a fixed failure output therefore gives output-only infidelity at most $\exp(-k/d^2)$. Its $O(d^2\log(1/\epsilon))$ copy cost can improve on the collective bound when $\epsilon$ is extremely small. The present result establishes the constant-error copy-product law; it does not establish optimal dependence on vanishing error. The elementary Choi-composition and Bell-teleportation setting is discussed in [3].

Global return in (1) is stronger than an output-only guarantee, but by itself it is not a theorem about a sequence of many compositions. Subsequent use would require an accumulated-error analysis. Likewise, a lower copy count does not establish a lower gate count: [Implementation](implementation.md) separately charges the known collective operations.

## 6. Reproduction and its scope

Run:

```bash
OPENBLAS_NUM_THREADS=1 python verification/check_construction.py
```

The script constructs the Bell-sum operator on finite inner-register spaces, checks both moments and the fidelity bound, and independently applies the physical instrument to complete ordered program states. Seeded complex unitaries test the order $UV$, the routing of leftover copies, and the equality of branches. Generic inputs outside the identical-copy family test the normalization of the incomplete instrument. The reported spectral fidelity is the successful branches' unconditional contribution $f_{\mathrm{pol}}$; a chosen failure state can increase the complete channel's fidelity.

These checks address normalization, register-order and spectral mistakes in the displayed construction. They do not prove the all-dimensional theorem, implement a scalable hardware circuit, or determine literature priority.

## References

1. P. Hausladen and W. K. Wootters, “A ‘Pretty Good’ Measurement for Distinguishing Quantum States,” *Journal of Modern Optics* **41**, 2385–2390 (1994), [doi:10.1080/09500349414552221](https://doi.org/10.1080/09500349414552221).
2. S. Strelchuk, M. Horodecki and J. Oppenheim, “Generalized Teleportation and Entanglement Recycling,” *Physical Review Letters* **110**, 010505 (2013), [doi:10.1103/PhysRevLett.110.010505](https://doi.org/10.1103/PhysRevLett.110.010505), [arXiv:1209.2683v2](https://arxiv.org/abs/1209.2683v2). Lemma 1 and Supplement Section 1 give the signal-purity route; the recycling theorems treat preservation of remaining ports.
3. D.-S. Wang, “Choi states, symmetry-based quantum gate teleportation, and stored-program quantum computing,” *Physical Review A* **101**, 052311 (2020), [doi:10.1103/PhysRevA.101.052311](https://doi.org/10.1103/PhysRevA.101.052311), [arXiv:1912.05418](https://arxiv.org/abs/1912.05418). Sections III–IV describe the composition setting; its deterministic corrections depend on the programs.
