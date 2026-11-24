# Exact composition with exact return of unused programs

Given copies of two unknown unitary programs, how often can a processor deliver their exact product and return every unused program in its original state? The sharp probability depends on the larger input pool. This is the same dependence as in exact-return multicopy teleportation, even when the composer can operate on both halves of every supplied program.

## Model and optimum

Let $d\geq2$ and $m,n\geq1$. Use the normalized row-first Choi vector $|X\rangle=\mathrm{vec}(X)/\sqrt d$. The input and required accepted output are

```math
v=|U\rangle^{\otimes m}\otimes|V\rangle^{\otimes n},
\qquad
w=|UV\rangle\otimes|U\rangle^{\otimes(m-1)}\otimes|V\rangle^{\otimes(n-1)}.
```

Both halves of each program are accessible. The processor receives no descriptions or queries to the unknown unitaries. It can use an arbitrary known quantum instrument, with ancillas, adaptive measurements, discard and outcome-dependent register order. We test the accepted state after the prescribed routing to a common order. Every accepted output must be exactly the joint pure state $|w\rangle$. Rejection can disturb or consume the programs.

**Theorem.** For $M=\max(m,n)$, the optimal worst-case success probability is

```math
p_{\mathrm{exact}}(d,m,n)=\frac{M}{d(M+d-1)}.
```

The optimum is uniform in $U,V$. A Bell instrument that measures the inner registers and then routes the outputs attains the bound. The converse allows arbitrary global processing on the full programs.

## Bell contractions and their norm

Let $L_{rs}$ contract the inner halves of program copies $r,s$ with the normalized Bell bra, then route the selected outer halves to the product-program output and the surviving whole programs to the residual registers. Set $E_{rs}=L_{rs}^{\dagger}L_{rs}$ and $G=d\sum_{r,s}E_{rs}$. The effect $E_{rs}$ is a Bell projector on the two selected inner registers with identities on the other registers, and $L_{rs}v=w/d$. On the separately symmetric space $\mathcal S$ of **whole** Choi copies, the $L_{rs}$ have identical restrictions. This follows by permuting the programs before contraction and permuting their separately symmetric survivors afterward. Writing $W=dL_{11}|_{\mathcal S}$ gives

```math
W^\dagger W=\frac{d}{mn}G\big|_{\mathcal S}.
```

The largest eigenvalue of $G$ on the full ordered space is attained on the separately symmetric **inner** registers. In the product basis its matrix entries on the inner registers are nonnegative. Taking the entrywise moduli of a top eigenvector cannot decrease its Rayleigh quotient. Averaging the nonnegative top eigenvector over the two inner permutation groups gives a nonzero symmetric top eigenvector. Tensoring it with fixed, separately symmetric outer product vectors places a top eigenvector in $\mathcal S$. Thus $G|_{\mathcal S}$ has the same norm as $G$ on all ordered registers.

On the separately symmetric inner space, let $a_j,b_j$ lower the occupations in the two pools, with the coefficient $\sqrt{k_j}$ for removing one particle from occupation $k_j$. Expanding the ordered Bell sum on this space yields $G=C^\dagger C$ with $C=\sum_j a_jb_j$. If $\Lambda_{m,n}$ denotes this norm at degrees $m,n$, the commutator $[C,C^\dagger]=d+N_a+N_b$ on the degree-$(m-1,n-1)$ space gives

```math
\begin{aligned}
\Lambda_{m,n}&=\Lambda_{m-1,n-1}+d+m+n-2,\\
\Lambda_{m,0}&=\Lambda_{0,n}=0,\\
\|G\|&=\min(m,n)(M+d-1).
\end{aligned}
```

The first identity uses equality of the norms of $C^\dagger C$ on the original sector and $CC^\dagger$ on the lower sector. The lower-sector commutator adds the displayed scalar to its own $C^\dagger C$. See the [routed construction](construction.md#2-symmetry-identifies-the-common-successful-state) and the [ordered-space norm argument in Multicopy Teleportation][teleportation-norm].

## Exact joint output fixes every success map

Take a Kraus representation of the routed accepted map. Its output is proportional to a pure state on every promised input, so each Kraus map $K$ sends $v$ to a vector proportional to $w$, including when that vector is zero. Every coordinate of $Kv$ and $w$ is a polynomial homogeneous of degrees $m,n$ in the entries of the two matrices. Each two-coordinate minor that expresses their proportionality vanishes on every pair of unitary matrices.

These minors vanish on all complex matrix pairs. Choose a real basis $H_j$ of Hermitian matrices. It is also a complex basis of all $d$ by $d$ matrices. In each argument, substitute $\exp(i\sum_j z_j H_j)$ with independent coefficients. For real coefficients the matrices are unitary. Repeated use of the one-variable identity theorem extends the vanishing to complex coefficients near zero. The matrix exponential parametrizations have invertible complex derivatives there, so their images contain an open neighborhood of the identity pair. A polynomial that vanishes on this neighborhood vanishes everywhere.

Now treat $X,Y$ as formal matrices. Two coordinates of the extended $w$ are proportional to

```math
(XY)_{11}X_{11}^{m-1}Y_{11}^{n-1},
\qquad
(XY)_{22}X_{22}^{m-1}Y_{22}^{n-1}.
```

They use disjoint variable sets, because they involve different rows of $X$ and different columns of $Y$. Their greatest common divisor is one. The minors therefore express $Kv$ as a rational scalar times $w$ whose denominator in lowest terms divides every coordinate of $w$. This denominator is constant. The degrees of $Kv$ and $w$ then force the scalar itself to be constant.

The unitary input vectors span $\mathcal S$. A linear functional that vanishes on all those vectors gives a vanishing bihomogeneous polynomial by the same density argument. Its coefficients are precisely the symmetric-tensor coordinates, up to nonzero normalization factors. Thus each accepted $K$ restricts to $\alpha_K W$ on $\mathcal S$. Since the accepted effects sum to at most the identity and $Wv=w$, the success probability $p=\sum_K |\alpha_K|^2$ satisfies

```math
p W^\dagger W\leq I,
\qquad
p\leq\frac{mn}{d\|G\|}=\frac{M}{d(M+d-1)}.
```

The fixed-target polynomial method is shared with the [canonical purification rigidity proof][purification-rigidity]. Here the two unknown matrices vary independently on their unitary orbits, and the return requirement fixes the full output degrees.

## Attaining the bound

Use the routed success Kraus operators

```math
J_{rs}=\sqrt{\frac{d}{\|G\|}}\,L_{rs},
\qquad
\sum_{r,s}J_{rs}^\dagger J_{rs}=\frac{G}{\|G\|}\leq I.
```

The residual effect completes the instrument with failure on the full ordered input. Each accepted branch has the exact joint output and probability $1/(d\|G\|)$, giving the claimed optimum when summed over $mn$ branches. Since the optimum depends only on $M$, it can also be reached by using one specimen from the smaller pool and passing its other specimens through untouched.

## What the return promise changes

| Qubit supplies | Optimal exact joint-return success |
|---|---:|
| 1 + 1 | 1/4 |
| 2 + 2 | 1/3 |
| 1 + 3 | 3/8 |

At fixed total supply the exact-return optimum is highest at the most uneven allocation. Equal supplies maximize the product in the [deterministic approximate composition guarantee](construction.md). At $m=n=d$, their exact-return success is $1/(2d-1)$, while the approximate composition channel gives global squared fidelity at least $d^2/(2d^2-1)$. These probabilities answer different operational questions.

If the processor can spend the unused programs, independent Bell trials give a different exact-output protocol. For two specimens from each qubit source, two such trials give success $1-(3/4)^2=7/16$, above the exact joint-return optimum $1/3$. The theorem concerns one heralded transformation with ideal supplied Choi states. Its success probability is an instrument-level optimum. Gate costs and protocols that reuse resources after a failed attempt require separate analysis.

[Quantum Multicopy Teleportation][teleportation] obtains the same exact success probability in its Alice-only, correction-free port model with exact return of unselected Bell pairs. The two converses use different access constraints and share the contraction norm. [Canonical Purification Cost][purification] uses that norm for the exact return of pure state and conjugate specimens. Its two coherent target branches give the success $2M/(2M+d-1)$. For the Bell contraction, prior state-conversion criteria and the one-Bell-pair endpoint, see the [related-work comparison](../references/RELATED_WORK.md).

[purification]: https://github.com/GoGoKo699/Canonical-Purification-Cost/blob/main/science/exact_joint_return.md
[purification-rigidity]: https://github.com/GoGoKo699/Canonical-Purification-Cost/blob/fc4651999bff3c65ab7992cda015751ae8b5715f/science/exact_frontier.md#rigidity-of-every-exact-processor
[teleportation]: https://github.com/GoGoKo699/Quantum-Multicopy-Teleportation/blob/main/science/exact-return.md
[teleportation-norm]: https://github.com/GoGoKo699/Quantum-Multicopy-Teleportation/blob/18d2d163ce1f5d8575d8c954856614df76879209/science/exact-return.md#the-two-covariant-effects-and-their-joint-norm
