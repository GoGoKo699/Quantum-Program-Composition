# Related work and proof dependencies

[Scientific overview](../science/README.md) · [Construction](../science/construction.md) · [Converse](../science/converse.md) · [Structured bibliography](bibliography.json)

The question here concerns a fixed processor supplied with independent copies of two complete, unknown unitary Choi states. It must output the Choi state of their matrix product, uniformly over the two unitaries. The [model](../science/model.md) distinguishes this state-conversion task from executing a program on an arbitrary fresh input, learning a classical unitary description, or querying an unknown unitary.

The contribution is the constant-error allocation law $mn=\Theta(d^2)$, including balanced copy cost $\Theta(d)$, a construction with a single global guarantee for the composed program and returned specimens, an arbitrary-processor converse, and a charged circuit. The proof uses established measurement, representation-theory and compilation tools. The following comparisons identify those dependencies and the limits of transfers from nearby tasks.

## Closest operational comparisons

| Source | Supplied resources and task | Relationship to this result |
|---|---|---|
| [Wang (2020)](https://doi.org/10.1103/PhysRevA.101.052311), Sections III–IV | Choi programs; composition and execution using a symmetry-based teleportation processor with program-dependent corrections. | Establishes the composition setting and elementary Bell-contraction mechanism. Its deterministic correction requires information beyond unknown Choi copies supplied to a fixed processor. |
| [Strelchuk, Horodecki and Oppenheim (2013)](https://doi.org/10.1103/PhysRevLett.110.010505), Lemma 1 and recycling results | A fixed input message, a shared port resource, and generalized correction sets; serial and bulk teleportation with residual-resource preservation. | Supplies square-root measurement, signal-purity and recycling ancestry. The present instrument selects a port from each of two program pools. |
| [Grosshans et al. (2026)](https://doi.org/10.22331/q-2026-05-13-2105), Sections 2–3 | Several identical copies of an unknown pure qudit and one shared maximally entangled pair; exact teleportation without a receiver correction. | Multiple input copies are a useful resource in both settings. Here each source specimen is a complete referenced Choi state, and both source pools vary. |
| [Kopszak et al. (2026)](https://doi.org/10.1109/TIT.2026.3656762), Sections 2 and 7 | Two successive uses of one port-based resource for two messages, with fidelity and degradation analysis. | Relevant to preservation of unused resources, but the protocol transmits two messages rather than composing two unknown program pools. |

### Known-program composition and fixed processors

Wang's adjoint correction has entries determined by the encoded gate. The authors' later [account, Section 4.4](https://pmc.ncbi.nlm.nih.gov/articles/PMC10453143/), explicitly requires known programs to perform this correction. The present model supplies no such description or correction oracle. Its collective measurement is determined entirely by $d,m,n$. This access distinction is necessary when comparing a deterministic known-program scheme with the copy costs proved here. The comparison concerns resources; it does not claim that the Choi-composition problem or Bell-contraction identity is new.

### Square-root measurements and preservation of ports

The effects in the [construction](../science/construction.md#relation-to-the-pretty-good-measurement) are exactly the pretty-good measurement for a known ensemble of Bell-pair signals. The generic measurement prescription is due to [Hausladen and Wootters (1994)](https://doi.org/10.1080/09500349414552221). The use of second moments and preservation of remaining ports has direct ancestry in Strelchuk–Horodecki–Oppenheim. The present proof derives its own two-pool Gram moments and fidelity estimate, and does not import a numerical recycling constant from that work.

**Publication note.** The original article is *Physical Review Letters* **110**, **010505** (2013). The [2013 note, 069902](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.110.069902), and [2014 note, 129901](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.112.129901), both correct acknowledgments or funding information. They are separate records; 069902 is not the original article number, despite its appearance in the arXiv journal-reference field.

### Multicopy teleportation is related but has a different promise

Grosshans et al. prove optimal exact success probability

$$
p(d,k)=\frac{k}{d(k-1+d)}
$$

for their one-pair, multiple-input-copy task. Section 6 discusses extending it to multiple shared ports. The theorem here does not solve that entire proposed extension: it assumes the complete halves of unitary Choi specimens, allows an approximate output, and controls a different global target. Likewise, the present return guarantee does not establish the serial-use performance studied by Kopszak et al.; repeated compositions require their own error analysis.

## Collective extraction of amplitude products

The public research repository [Quantum-Coherent-Collisions](https://github.com/GoGoKo699/Quantum-Coherent-Collisions/tree/219f590010247124f48feffaf244a60f306335f4) is a close methodological antecedent. Its [model](https://github.com/GoGoKo699/Quantum-Coherent-Collisions/blob/219f590010247124f48feffaf244a60f306335f4/science/model.md) concerns the pointwise amplitude power of one unknown pure state. Its [exact construction](https://github.com/GoGoKo699/Quantum-Coherent-Collisions/blob/219f590010247124f48feffaf244a60f306335f4/science/coherent_extraction.md) pools copies, corrects occupation multiplicities and factors the target from an accepted residual.

Those collective-copy ideas are shared. Matrix multiplication additionally sums coherently over a contracted index between two sources, and its Gram operator is a sum of noncommuting Bell projectors. The amplitude-power theorem does not directly implement this contraction or supply the mixed-unitary moment converse. The source is a scientific repository at a pinned revision, not a claim of an independently published article.

## Exact canonical purification and the normalization boundary

[Canonical-Purification-Cost](https://github.com/GoGoKo699/Canonical-Purification-Cost) is a sister task rather than a specialization of the unitary-Choi theorem. Its [earlier model and balanced construction](https://github.com/GoGoKo699/Canonical-Purification-Cost/tree/823c42ab394e6764263aeb670a7d86292cec5341/science) prescribe the canonical purification of a flat rank-two state with a known vacuum, supplied through independent state/conjugate streams. Their inaccessible environments are not part of the input.

The shared method is coherent contraction across separately symmetric copy pools, exact target/residual factorization before normalization, and a norm check on the whole physical input space. The [pure exact frontier](https://github.com/GoGoKo699/Canonical-Purification-Cost/blob/f2dc023a98242739929ef01eb4f9478d4bb96782/science/exact_frontier.md) additionally uses exact-output polynomial rigidity and charged harmonic kernels to characterize every pure allocation by a finite LP. Its [mixed frontier](https://github.com/GoGoKo699/Canonical-Purification-Cost/blob/f2dc023a98242739929ef01eb4f9478d4bb96782/science/mixed_frontier.md) is the lossless binomial average over known vacuum/signal occupancy counts. These proofs belong in that repository; they do not use the unitary-Choi composition theorem as a premise.

The [local comparison](../science/canonical_purification_boundary.md) gives the task definitions, the one-conjugate exact optimum, the mixed-source success ceiling, and the transfer obstruction. Choi inner marginals are maximally mixed; canonical signals are rank one. The polar normalization here generally changes the accepted direction and supports an approximate joint-fidelity guarantee; exact purification requires the specified coherent direction on every accepted output. Neither a substitution of $d$ for $d^2$ nor the common symmetry notation supplies the missing proof. No exact canonical frontier is credited as a second unitary-program theorem, and no approximate-fidelity product law is inferred.

## Representation theory used by the converse

The [converse](../science/converse.md) compares correlated and independent Haar-unitary program ensembles. Its representation-theoretic foundation is inherited:

- [Grinko and Ozols (2024), Theorem 3.8](https://link.springer.com/article/10.1007/s00220-024-05108-1), gives mixed Schur–Weyl mutual centralizers on the represented tensor space. The centralizer statement holds without $d\geq m+n$; that additional inequality is used for faithfulness of the abstract walled Brauer representation. This distinction matters for unequal copy budgets.
- [Goncharov (2025), Proposition 2.4](https://arxiv.org/html/2511.00303v1), establishes centrality of the mixed traceless projector for every positive local dimension and both positive tensor degrees. Its represented-algebra formulation avoids an unnecessary stable-dimension restriction.

The application here is the comparison of the two compressed Choi moment operators, the trace-distance bound controlled by $mn/d^2$, and the reduction from composition to distinguishing the two priors. No new Schur–Weyl duality or traceless-projector theorem is claimed. [Collins and Śniady (2006)](https://doi.org/10.1007/s00220-006-1554-3) supplies the Haar-integration machinery used in finite verification; the analytic converse uses the stated centralizer and dimension argument.

## Circuit and finite-precision ingredients

[Gilyén, Su, Low and Wiebe (2019)](https://doi.org/10.1145/3313276.3316366) supplies projected-unitary quantum singular value transformation and the polynomial approximation tools used in [Implementation](../science/implementation.md). Here the encoded operator is a Bell contraction restricted to the symmetry of whole Choi copies. Its lower singular tail is controlled on the promised input by the exact Gram moments; no lower bound on every nonzero singular value is assumed.

[Dawson and Nielsen (2006)](https://doi.org/10.26421/QIC6.1-6) is the compilation reference for replacing known finite-dimensional gates by gates from a fixed finite universal set, with logarithmic-power precision overhead. The construction explicitly charges controlled register permutations rather than assuming free quantum random access.

These ingredients establish an implementable sample law. They do not imply that the processor has a total-runtime advantage, and the result does not identify the optimal dependence on an error tending to zero.

## Reference scope

The bibliography records the primary versions used for these comparisons and proof dependencies. The distinctions above refer to their stated resources, correctness criteria and outputs. They support the specific composition claim; they are not an exhaustive priority certificate for every use of collective measurements or quantum programs. Exact statements and quantitative limitations remain in the linked scientific pages.
