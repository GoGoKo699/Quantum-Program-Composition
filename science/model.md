# Model and composition law

The resource is a collection of quantum states encoding two unknown operations. The task is to combine those states into a state encoding the product operation. No classical reconstruction of either operation is required by the task.

This page fixes the model and exact theorem statements. The [construction](construction.md), [converse](converse.md) and [implementation](implementation.md) supply their proofs and charged circuit realization.

## Programs, inputs and outputs

Let $d\geq2$ and let $U,V\in U(d)$ be arbitrary fixed unitaries. In a fixed computational basis, define the normalized Choi vector

$$
|U\rangle=(U\otimes I)|\Phi_d\rangle
=\frac1{\sqrt d}\sum_{i,j=0}^{d-1}U_{ij}|i\rangle|j\rangle,
\qquad
|\Phi_d\rangle=\frac1{\sqrt d}\sum_{j=0}^{d-1}|j,j\rangle.
$$

The first register is the matrix row and the second its column. Multiplication order is therefore fixed: contracting the column of a $U$ program with the row of a $V$ program produces $|UV\rangle/d$. A global phase of either matrix is immaterial to the corresponding program density operator and to the target density operator.

The input consists of $m\geq1$ independent identical copies of $|U\rangle$ and $n\geq1$ of $|V\rangle$ in labelled, ordered registers. Both halves of every copy are accessible. The processor knows $d,m,n$ and a requested accuracy; it has no classical description of $U,V$, query to either operation, inverse state preparation, controlled unknown operation, or reflection about an unknown state. Arbitrary known gates and ancillas initially independent of $U,V$ are allowed. Quantum memory and known gates are accounted for separately from supplied copies.

The basic output target is $|UV\rangle$. The construction proves the stronger joint guarantee with target

$$
|w_{U,V}\rangle
=|UV\rangle\otimes|U\rangle^{\otimes(m-1)}
\otimes|V\rangle^{\otimes(n-1)}.
$$

For a pure target $|w\rangle$, fidelity means $F(\rho,w)=\langle w|\rho|w\rangle$, the squared convention. All stated error parameters are infidelities in this convention. The output registers have dimension $d^{2(m+n-1)}$ for the joint-return task.

## Theorem 1: a universal collective construction

There is a completely positive, trace-preserving map, fixed by $d,m,n$, such that for every $U,V$ its joint output satisfies

$$
F_{\mathrm{global}}\geq
\frac{mn}{mn+d^2-1}
\geq1-\frac{d^2-1}{mn}.
\tag{1}
$$

This is an unconditional output guarantee. An intermediate measurement has a successful branch, but the final map also assigns an output on failure. The successful state is generally approximate. The mathematical map is the polar normalization of a known contraction; the [finite circuit](implementation.md) attains the same copy scaling with explicit larger constants and gate-synthesis error.

For $0<\epsilon<1$, the exact channel satisfies $F_{\mathrm{global}}\geq1-\epsilon$ whenever

$$
mn\geq\frac{1-\epsilon}{\epsilon}(d^2-1).
\tag{2}
$$

Equation (2) is a sufficient allocation, not an optimal dependence on a vanishing error parameter. In particular, balanced pools of $O(d/\sqrt\epsilon)$ copies suffice for this construction.

## Theorem 2: an unrestricted converse

Let a quantum instrument use at most $m$ and $n$ copies of the two programs. Suppose that for every fixed $U,V$ it declares success with probability at least $p_0>0$, and its normalized successful output has fidelity at least $F_0\geq d^{-2}$ with $|UV\rangle$. Then

$$
mn\geq\frac{p_0}{2}(d^2F_0-1).
\tag{3}
$$

The source budgets are worst-case bounds. The theorem permits arbitrary collective operations, independent ancillary memory and adaptive measurements. A protocol with bounded sequential access can precollect all its copies and is therefore included. The converse already holds when no leftover programs are requested, so it also bounds the joint-return task. It holds in every dimension and for every allocation, including $m=1$ and $n$ much larger than $d$.

The proof first bounds the distinguishability of two averaged input states, then converts any sufficiently accurate composer into a test distinguishing them. The representation argument concerns the image of the mixed-tensor commutant; it does not assume that an abstract walled Brauer algebra acts faithfully.

The same proof gives a precise Haar-average statement. If $\bar p$ is the average success probability and $\bar s$ is the average unnormalized successful overlap for independent Haar $U,V$, then

$$
\bar s-\frac{\bar p}{d^2}\leq\frac{2mn}{d^2}.
\tag{4}
$$

For deterministic processing, $\bar p=1$. For heralded processing, $\bar s/\bar p$ is the success-weighted conditional fidelity. An unweighted average of conditional fidelities is a different statistic; see the [converse](converse.md).

## What is optimal

Fix an infidelity $\epsilon\in(0,1)$ independently of $d$, and consider deterministic universal processing. Equations (1) and (3) give the necessary and sufficient copy-product scale

$$
mn=\Theta(d^2).
\tag{5}
$$

Here “threshold” means that products below a suitable constant multiple of $d^2$ cannot achieve the specified fidelity, while products above another constant multiple suffice. The constants depend on the chosen fidelity. It does not mean that every allocation with product exactly $d^2$ attains every constant accuracy.

Let $F^*_{\mathrm{out}}(d,m,n)$ denote the best worst-case fidelity of a deterministic processor for the composed program alone. The proved finite bounds are

$$
\frac{mn}{mn+d^2-1}
\leq F^*_{\mathrm{out}}(d,m,n)
\leq\min\{1,\frac{2mn+1}{d^2}\}.
\tag{6}
$$

They determine the fidelity scale up to constants across copy budgets, while leaving the exact optimum and its approach to one unresolved. The lower end of (6) comes from a processor with the additional joint-return guarantee.

| Allocation | Necessary scale at fixed positive success and fidelity | Sufficient scale at fixed deterministic fidelity |
|---|---|---|
| Balanced sources | Each pool has order $d$ copies | Each pool has order $d$ copies |
| One copy of one source | The other pool has order $d^2$ copies | The other pool has order $d^2$ copies |
| General allocation | Product has order at least $d^2$ | A sufficiently large constant times $d^2$ in product |

Minimizing $m+n$ subject to the product law gives total copy complexity $\Theta(d)$. This is the operational role of balancing the supplies.

## Resources and boundaries

The finite implementation uses known gates with conservative cost

$$
\widetilde O\!\left(d(m^2+n^2)(\log d+\log(m+n))\right),
$$

where omitted factors are logarithmic in the dimensions, budgets and inverse accuracy. With balanced supplies and fixed error this is $\widetilde O(d^3)$ gates, in addition to the supplied program states. The result establishes copy efficiency, without a claimed total-runtime improvement. The dimension $d$ is the Hilbert-space dimension; for a $q$-qubit operation it equals $2^q$.

The task assumes ideal pure unitary Choi copies. Its output is a state encoding a composed operation, rather than an application of that operation to arbitrary fresh data. A joint fidelity promise for returned copies is a one-shot guarantee; repeated use requires its own error accounting. [Interpretation and limits](interpretation.md) explains these distinctions and the high-precision alternative.
