# Interpretation and limits

The [composition law](model.md) concerns information already supplied in quantum form. A Choi program is a physical state whose two halves retain the correlations of an unknown operation. Combining two such programs requires eliminating the intermediate matrix index coherently. The Bell contraction performs that algebraic operation, but one selected pair succeeds with probability only $d^{-2}$.

## Why two pools help

Independent trials use a fresh pair of programs for each Bell projection. The collective construction instead normalizes a measurement over all $mn$ possible cross-pool pairs. These alternatives overlap and their Bell projectors do not generally commute, so they cannot be treated as independent classical trials. The square-root measurement handles their overlap, and whole-copy symmetry makes every successful routed branch coincide.

The decisive normalized variance is

$$
r=\frac{d^2-1}{mn}.
$$

It controls the distortion caused by polar normalization. A large product of supplies reduces that distortion even if neither individual pair has appreciable success probability. For balanced supplies, order $d$ programs per pool already make the global output accurate to a fixed constant.

The converse shows that this effect has a limit. A universal composer would reveal whether the two unknown operations were inverses or independent. With too few program pairs, those two averaged quantum inputs are nearly indistinguishable. The mixed-tensor moment comparison limits every quantum procedure that could extract this correlation, not only the displayed Bell or PGM construction.

## Program composition and program execution

The produced state is $|UV\rangle$. It can serve as an input to a later quantum-information task that accepts Choi programs. Applying the unknown operation $UV$ to an arbitrary fresh data state is a different task and can consume further resources. The theorem does not provide a classical circuit description of $U$, $V$ or their product.

The scope still includes noncommuting operations of arbitrary dimension. No promise of a common eigenbasis, low rank, a particular gate set for the unknown operations, or access to a preparation circuit is used. The known processor may be expensive: its explicit gate count is approximately cubic in $d$ for fixed-error balanced composition. The optimality statement is about supplied copies.

## A joint return guarantee

The target contains one fewer copy from each pool together with the composed program. Fidelity is assessed against that entire product state. This is stronger than separate marginal fidelity guarantees and controls residual correlations in the same one-shot statement.

The actual returned registers need not be exact independent copies. In particular, counting only the two selected specimens as permanently consumed would omit the accumulated approximation error if the leftovers were reused. No indefinite catalyst, long-chain composition rate or many-output cost follows from the one-output theorem alone.

## Precision and alternative strategies

The exact collective channel gives global infidelity at most $(d^2-1)/(mn+d^2-1)$. Its explicit circuit can achieve the requested infidelity with copy product $mn=O(d^2/\epsilon)$, with larger constants specified in [Implementation](implementation.md). The converse matches the constant-error product scale, rather than the dependence on $\epsilon$ as it tends to zero.

For the composed output alone, independent paired Bell trials provide a useful alternative. On each successful trial the target is exact. After $k$ fresh pairs, the probability of no success is

$$
\left(1-\frac1{d^2}\right)^k\leq e^{-k/d^2}.
$$

Assigning an arbitrary output on failure therefore gives infidelity at most $\epsilon$ with $k=\lceil d^2\log(1/\epsilon)\rceil$ pairs. This alternative does not return all but one specimen from each input pool. For extremely small error it can use fewer copies than the sufficient balanced collective allocation $O(d/\sqrt\epsilon)$. A precision-sensitive comparison must retain both alternatives.

## Exact purification as a related contraction task

The sister project [Canonical-Purification-Cost](https://github.com/GoGoKo699/Canonical-Purification-Cost) must prepare a specified vacuum/signal coherent purification exactly on success. Both projects use contraction on separately symmetric copy pools and require physical normalization on the whole input space. Their normalizations answer different correctness requirements: the polar map here permits controlled distortion, whereas exact purification must retain the prescribed coherence.

The [self-contained comparison](canonical_purification_boundary.md) explains why maximally mixed Choi marginals and the unitary-prior converse do not apply to independent rank-two state/conjugate samples. Its exact pure frontier is a finite all-allocation LP; mixed hard caps require averaging over the actual binomial signal counts. Those results have their authoritative proof in the sister repository. They do not follow by replacing $d^2$ with $d$ in this project's theorem.

## What the present theorem leaves open

The supported result fixes the order of the copy-product threshold and provides an implementable universal construction. Exact optimal fidelity, sharp small-error rates, improved gate counts, robustness to mixed or noisy programs, expected-budget protocols and repeated composition are separate questions. They are not needed to justify the stated constant-error law, and no result about them is assumed in its proof.
