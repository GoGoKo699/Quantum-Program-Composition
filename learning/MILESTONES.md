# Thirty milestones for understanding program composition

[Scientific account](../science/README.md) · [Exact model and statements](../science/model.md) · [Proof dependencies](../references/RELATED_WORK.md)

This map describes the understanding needed to connect the supplied programs, collective measurement, converse and circuit into one scientific account. Its targets follow the project, independently of a reader's starting knowledge. It covers the load-bearing ideas and their connections; specialist details remain in the canonical scientific pages.

## Structure and educational anchor

The single educational anchor is John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018): [author's page](https://cs.uwaterloo.ca/~watrous/TQI/) and [author's online text][watrous]. The section numbers below refer to that text. PDF links open the beginning of the cited section; the section number is authoritative if a viewer ignores the page fragment.

| Phase | Milestones | Allocation and direction |
|---|---|---|
| Background / preliminaries | M01–M13: 13 targets | Assemble individual operators and states into referenced programs, physical processing, error measures, spectral probability and symmetry; finish with the complete supplied-program task. |
| Narrative / innovation | M14–M30: 17 targets | Follow the local contraction through the collective construction, then the distinguishing converse and charged implementation; finish with the allocation law, precision regimes and complete operational interpretation. |

Thirteen background targets are needed because this project joins matrix multiplication to the physics of referenced states, probabilistic instruments, spectral bounds and group averages. Seventeen narrative targets connect three substantial arguments: how the processor works, why arbitrary processors need enough copies, and how known gates implement it. The allocation reflects those connections, rather than a fixed division inherited from another project.

Three source conventions matter throughout:

- Watrous writes vectors and adjoints as $u$ and $A^*$. The science pages also use $\lvert u\rangle$ and $A^\dagger$. The normalized program is $\mathrm{vec}(U)/\sqrt d$; the normalized Choi density is the channel's Choi operator divided by $d$.
- Watrous's fidelity in §3.2 is the root convention. Here $F(\rho,w)=\langle w\rvert\rho\lvert w\rangle$ is its square for a normalized pure target. A success probability and a conditional fidelity are separate quantities.
- Anchor pointers provide foundations. The mixed-tensor ingredients, two-pool derivations, QSVT and compilation results are supplied or cited in the scientific pages. Those primary research sources remain proof dependencies, not additional educational anchors. Projector symbols are local to each proof: whole-copy symmetry in the construction and the harmonic projector in the converse are different objects.

## Phase I — Background / preliminaries

### M01 — Finite registers and linear operators

- **Central question:** What mathematical objects describe a program register and an operation acting on it?
- **Understanding target:** Relate a finite register to a complex vector space, its dimension to a basis, and a linear operator to its matrix entries. Distinguish the local operation dimension $d$ from the $d^2$ dimensions of a two-register program and from the number of physical qubits used to encode it.
- **Dependencies and story role:** No earlier milestone. Establishes the objects whose tensor products, transformations and resource counts appear throughout the project.
- **Conceptual connection:** The dimension in the copy law is a physical Hilbert-space dimension, so a scaling statement in $d$ must be interpreted before comparing it with a qubit count.
- **Sources:** [Watrous §§1.1.1][w111]–[1.1.2][w112]; [programs, inputs and outputs](../science/model.md#programs-inputs-and-outputs), [charged circuit resources](../science/implementation.md#5-charged-circuit-resources).

### M02 — Pure states, mixtures, and irrelevant phase

- **Central question:** What information belongs to a quantum state, and which changes leave that state unchanged?
- **Understanding target:** Connect normalized vectors with pure density operators, distinguish a coherent vector from a probabilistic mixture, and explain why multiplying a program vector by a global phase changes no state-level prediction. Understand that an unknown fixed state and an averaged ensemble are different descriptions used for different purposes.
- **Dependencies and story role:** M01. Gives the physical meaning of the vectors and density operators used later in both construction and converse.
- **Conceptual connection:** The target program remains well defined even though unitary Choi states do not encode an observable global phase of their matrices.
- **Sources:** [Watrous §2.1.2][w212]; [program convention and phase](../science/model.md#programs-inputs-and-outputs), [averaged program ensembles](../science/converse.md#1-correlated-programs-and-independent-programs).

### M03 — Composite registers and accessible correlations

- **Central question:** Why do both halves of a Choi specimen matter when either half alone is maximally mixed?
- **Understanding target:** Explain tensor products, joint states and reduced states, and distinguish independence across supplied specimens from entanglement within each specimen. Identify which registers the processor can access and which correlations disappear when a register is discarded.
- **Dependencies and story role:** M01–M02. Moves from an isolated state to the multi-register setting in which the physical task lives.
- **Conceptual connection:** Full access to both halves is a material input promise. The construction uses the maximally mixed inner marginal while preserving useful information in the joint state.
- **Sources:** [Watrous §§2.1.2][w212]–[2.1.3][w213]; [input access and joint target](../science/model.md#programs-inputs-and-outputs), [inner-register marginal](../science/construction.md#3-exact-first-and-second-moments).

### M04 — Unitary products, adjoints, and order

- **Central question:** How do matrix multiplication and adjoints determine the meaning of the desired composed operation?
- **Understanding target:** Explain unitarity, the distinction between transpose, complex conjugate and adjoint, and why $UV$ and $VU$ generally differ. Separate the mathematical identity $U^\dagger U=I$ from operational permission to query or implement an unknown inverse.
- **Dependencies and story role:** M01–M03. Supplies the algebra that fixes the composition target and the inverse-correlated prior used by the converse.
- **Conceptual connection:** A register-order mistake can change the task. A mathematical conjugate in an ensemble definition does not supply a physical conjugation procedure.
- **Sources:** [Watrous §1.1.2][w112]; [row-first program convention](../science/model.md#programs-inputs-and-outputs), [correlated programs](../science/converse.md#1-correlated-programs-and-independent-programs).

### M05 — Vectorization and normalized Choi programs

- **Central question:** How can a matrix be represented by a bipartite quantum state without supplying its classical entries?
- **Understanding target:** Identify the row and column registers in $\lvert U\rangle=\mathrm{vec}(U)/\sqrt d$, account for normalization, and relate this vector to the Choi representation of a unitary channel. Distinguish possessing the state from possessing an executable gate or a matrix description.
- **Dependencies and story role:** M02–M04. Turns the abstract matrix product into a state-conversion problem with explicit physical input specimens.
- **Conceptual connection:** The same matrix indices that describe composition become quantum registers; the processor must eliminate the shared index while retaining coherence.
- **Sources:** [Watrous §§1.1.2][w112] and [2.2.2][w222]; [program definition](../science/model.md#programs-inputs-and-outputs), [composition and execution](../science/interpretation.md#program-composition-and-program-execution).

### M06 — Bell pairs and teleportation contractions

- **Central question:** How does projection onto a maximally entangled pair connect two register indices?
- **Understanding target:** Explain a Bell ket, its corresponding bra and projector, and the coherent sum produced by contracting two registers. Track the difference between an unnormalized branch vector, its squared norm as an outcome probability, and its normalized conditional state. Understand the role of outcome-dependent corrections in ordinary teleportation.
- **Dependencies and story role:** M03–M05. Introduces the generic physical contraction before its program-specific action is derived in the narrative.
- **Conceptual connection:** The normalization of an entangled projection determines its probability; obtaining a useful contraction is not itself a deterministic operation.
- **Sources:** [Watrous §§1.1.2][w112] and [6.3.1][w631]; [Bell projectors and routing maps](../science/construction.md#1-a-physical-instrument-on-two-pools).

### M07 — Channels, instruments, and success flags

- **Central question:** What makes a collection of probabilistic branches a legal quantum processor?
- **Understanding target:** Distinguish a channel, a completely positive branch and a quantum instrument. Explain how Kraus effects determine probabilities, why their sum must satisfy a normalization condition, and how retaining or discarding a classical success flag changes the output description.
- **Dependencies and story role:** M02–M03, M06. Extends one Bell outcome into the framework for a complete physical procedure.
- **Conceptual connection:** The composer must act legally on the entire input space, even though its accuracy promise concerns a special family of identical-copy states. Preparing a fixed output on failure completes a channel.
- **Sources:** [Watrous §§2.2.1][w221]–[2.2.2][w222] and [2.3.2][w232], including instruments; [physical instrument](../science/construction.md#1-a-physical-instrument-on-two-pools).

### M08 — Squared fidelity and joint targets

- **Central question:** What does it mean for the composed program and returned specimens to be accurate together?
- **Understanding target:** Translate Watrous's root fidelity into the project's squared convention. Distinguish unconditional overlap, successful conditional overlap and success probability. Explain why fidelity with one full product target controls the joint returned state more strongly than a statement about the composed output alone.
- **Dependencies and story role:** M02–M03, M07. Fixes the correctness criterion before any resource bound is interpreted.
- **Conceptual connection:** The promise includes residual correlations and approximation error, so returned registers cannot automatically be counted as exact fresh copies.
- **Sources:** [Watrous §3.2.1][w321], especially Proposition 3.13, and [§3.2.2][w322]; [global target](../science/construction.md#the-global-output-guarantee), [joint return interpretation](../science/interpretation.md#a-joint-return-guarantee).

### M09 — Trace distance and operational distinguishability

- **Central question:** How does closeness of two input ensembles limit every possible measurement strategy?
- **Understanding target:** Interpret $\mathrm{TD}(\rho,\sigma)=\tfrac12\lVert\rho-\sigma\rVert_1$ as the maximum difference between the probabilities of a measurement event. Explain why physical processing followed by a test cannot create a larger distinguishing advantage than was available in the input states.
- **Dependencies and story role:** M02, M07. Introduces the operational measure used to constrain arbitrary composers, complementing the fidelity measure used to certify an output.
- **Conceptual connection:** A lower bound can follow from a task reduction: an accurate composer would enable a discrimination experiment forbidden by the supplied information.
- **Sources:** [Watrous §3.1.1][w311]; [moment comparison](../science/converse.md#1-correlated-programs-and-independent-programs), [composer-to-test reduction](../science/converse.md#2-turning-a-composer-into-a-correlation-test).

### M10 — Positive operators, support, and polar maps

- **Central question:** How can a known contraction be normalized when it has a nontrivial kernel?
- **Understanding target:** Relate positive operators to their spectral square roots and support projectors, and interpret inverse powers that vanish on the kernel. Explain how singular values separate the magnitude of a rectangular map from its polar partial isometry, without mistaking that partial isometry for a unitary on the full input space.
- **Dependencies and story role:** M01, M04, M07. Supplies the algebra behind the PGM effects and the exact collective channel.
- **Conceptual connection:** Support-aware normalization produces legal success effects and leaves a complementary failure effect; it does not require inverting an unknown preparation.
- **Sources:** [Watrous §1.1.3][w113], including singular values, polar decompositions and the pseudoinverse; [instrument normalization](../science/construction.md#1-a-physical-instrument-on-two-pools), [polar map](../science/construction.md#2-symmetry-identifies-the-common-successful-state).

### M11 — Spectral probability and moment bounds

- **Central question:** How can a few operator moments control fidelity without solving a complete large spectrum?
- **Understanding target:** Interpret the eigenvalues of a positive operator, weighted by a state, as a nonnegative random variable. Relate its first two moments to mean and variance, and explain how scalar inequalities bound its square-root average or a low-value tail. Distinguish this spectral distribution from a claim that overlapping measurements are independent.
- **Dependencies and story role:** M08, M10. Connects operator normalization to quantitative probability bounds.
- **Conceptual connection:** The construction and finite circuit use different consequences of the same exact moments: a global overlap bound and control of the small-singular-value region.
- **Sources:** [Watrous §§1.1.3][w113] and [1.2.2][w122]; [exact moments](../science/construction.md#3-exact-first-and-second-moments), [fidelity inequality](../science/construction.md#4-fidelity-and-success-probability), [spectral tail](../science/implementation.md#controlling-the-small-singular-value-tail).

### M12 — Permutation symmetry and Haar averaging

- **Central question:** What do symmetries of repeated copies and averages over unknown unitaries each accomplish?
- **Understanding target:** Explain the symmetric subspace, a known permutation average and an invariant operator. Separately explain Haar averaging and its invariance under known unitary changes of basis. Distinguish a projector onto symmetry of whole copies from a state averaged over an ensemble of unknown matrices.
- **Dependencies and story role:** M03–M05, M07, M11. Connects the physical and probabilistic ingredients into the symmetry framework shared by all three proof strands.
- **Conceptual connection:** Whole-copy symmetry identifies output branches; Haar symmetry simplifies the converse. Neither operation provides a reflection about an unknown program state.
- **Sources:** [Watrous §§7.1.1][w711]–[7.1.2][w712] and [7.2.1][w721]; [common successful state](../science/construction.md#2-symmetry-identifies-the-common-successful-state), [averaged priors](../science/converse.md#1-correlated-programs-and-independent-programs).

### M13 — The complete supplied-program task

- **Central question:** Which inputs, operations, outputs and accuracy promises define the theorem being studied?
- **Understanding target:** Assemble the full model: $m$ copies of the first unknown unitary program, $n$ of the second, access to both halves, a fixed known processor, the ordered product target and optional joint return. Interpret universal quantifiers, worst-case copy budgets, deterministic versus heralded performance, and separate accounting of copies, gates and memory.
- **Dependencies and story role:** M01–M12. Integrates the background into one operational specification, completing this phase.
- **Conceptual connection:** A copy law has meaning only with this resource boundary. State conversion, gate execution and classical reconstruction are distinct requested outputs.
- **Sources:** [Watrous §§2.2.1][w221], [2.3.2][w232] and [3.2.1][w321] for the processing and accuracy language; [complete model](../science/model.md), [composition and execution](../science/interpretation.md#program-composition-and-program-execution).

## Phase II — Narrative / innovation

### M14 — One pair contracts to the ordered product

- **Central question:** What exactly happens when the inner halves of one $U$ program and one $V$ program meet a Bell bra?
- **Understanding target:** Follow the row and column indices to obtain $L(\lvert U\rangle\otimes\lvert V\rangle)=\lvert UV\rangle/d$. Account for every normalization factor and infer success probability $d^{-2}$. Explain why the accepted target is exact for this single trial and why its probability establishes only a baseline, not an arbitrary-processor lower bound.
- **Dependencies and story role:** M04–M06, M08, M13. Begins the narrative with its smallest complete physical mechanism.
- **Conceptual connection:** The matrix product is already present in one coherent contraction; the collective construction changes the copy cost of obtaining a useful output.
- **Sources:** [Watrous §§1.1.2][w112] and [6.3.1][w631]; [ordered contraction, equation (9)](../science/construction.md#2-symmetry-identifies-the-common-successful-state), [paired-trial baseline](../science/construction.md#5-copy-budgets-and-the-precision-boundary).

### M15 — All cross-pool pairs form one Bell-sum operator

- **Central question:** How are all $mn$ potential contractions combined without treating them as independent trials?
- **Understanding target:** Identify the pair-labelled Bell effects $E_{rs}$ and the known positive operator $G=d\sum_{r,s}E_{rs}$. Explain why shared registers make some effects noncommuting and why counting port pairs alone does not yield a classical success formula.
- **Dependencies and story role:** M10–M11, M14. Moves from one contraction to the collective operator whose fluctuations determine performance.
- **Conceptual connection:** The useful product of copy budgets enters through a jointly normalized family of overlapping alternatives, rather than through $mn$ disjoint pairs of specimens.
- **Sources:** [Watrous §§1.1.2][w112]–[1.1.3][w113] and [2.3.2][w232]; [Bell-sum definition](../science/construction.md#1-a-physical-instrument-on-two-pools), [why two pools help](../science/interpretation.md#why-two-pools-help).

### M16 — A universal PGM instrument and deterministic completion

- **Central question:** How does square-root normalization turn the overlapping alternatives into a valid universal processor?
- **Understanding target:** Explain $J_{rs}=\sqrt dL_{rs}G^{-1/2}$ and the support identity for the sum of its effects. Relate these effects to the pretty-good measurement for a known Bell-signal ensemble, and account for the kernel by a separate failure output. Distinguish the effects from the routed quantum outputs that make this an instrument.
- **Dependencies and story role:** M07, M10, M15. Establishes physical legality before claiming fidelity on the promised inputs.
- **Conceptual connection:** The measured signals and their normalization are known from $d,m,n$; no program-dependent correction is supplied. The generic PGM prescription is inherited machinery.
- **Sources:** [Watrous §§2.3.2][w232] and [3.1.2][w312], including its PGM discussion; [instrument and completion](../science/construction.md#1-a-physical-instrument-on-two-pools), [PGM relation](../science/construction.md#relation-to-the-pretty-good-measurement).

### M17 — Whole-copy symmetry identifies every routed branch

- **Central question:** Why can the port label be discarded without mixing different useful output states?
- **Understanding target:** Explain why permutation symmetry acts on complete two-register programs, why $G$ preserves that subspace, and why the routing maps agree there. Connect $M^\dagger M=G$ on the restricted domain to the common branch vector $Kv/\sqrt{mn}$, where $K$ is the polar map.
- **Dependencies and story role:** M10, M12, M14–M16. Converts a many-outcome instrument into one analyzable successful state.
- **Conceptual connection:** Physical ordered-register symmetry supplies the simplification. No coherent port-label output, occupation encoding or bosonic access is assumed, and the leftover registers remain part of the state being analyzed.
- **Sources:** [Watrous §§1.1.3][w113] and [7.1.1][w711]; [common successful state, equations (7)–(12)](../science/construction.md#2-symmetry-identifies-the-common-successful-state).

### M18 — Exact Gram moments expose the copy product

- **Central question:** Why is the normalized spectral variance exactly $(d^2-1)/(mn)$ for every pair of unitaries?
- **Understanding target:** Use the maximally mixed joint inner marginal to turn expectations into normalized traces. Distinguish diagonal, disjoint-pair and shared-register terms in $G^2$, and explain why the last two have the same trace despite noncommutation. Connect the resulting mean $mn/d$ and variance $mn(1-d^{-2})$ to the dimensionless ratio $r$.
- **Dependencies and story role:** M03, M11, M15, M17. Supplies the quantitative input for both the exact channel and its finite implementation.
- **Conceptual connection:** Uniformity over unknown $U,V$ follows from the marginal structure, not from averaging the accuracy guarantee over those unitaries.
- **Sources:** [Watrous §§2.1.3][w213] and [1.2.2][w122]; [exact moment derivation](../science/construction.md#3-exact-first-and-second-moments).

### M19 — Polar normalization preserves the full joint target

- **Central question:** How do the moments certify the composed program and every returned specimen together?
- **Understanding target:** Connect the polar overlap to $(\mathbb E\sqrt X)^2$, with $X=G/\mathbb EG$, and follow the Hölder step yielding $F_{\rm global}\geq1/(1+r)=mn/(mn+d^2-1)$. Keep this unconditional contribution distinct from the support probability $p$ and the conditional fidelity $f_{\rm pol}/p$.
- **Dependencies and story role:** M08, M11, M16–M18. Completes the constructive argument by joining physical branches to a global error guarantee.
- **Conceptual connection:** The bound remains informative when $1-r$ is negative. It certifies approximate joint return without asserting that every successful output is exact or that the bound is optimal.
- **Sources:** [Watrous §§1.1.3][w113], [1.2.2][w122] and [3.2.1][w321] for the spectral and fidelity language; [local Hölder derivation and success probability](../science/construction.md#4-fidelity-and-success-probability), [global theorem](../science/model.md#theorem-1-a-universal-collective-construction).

### M20 — Correlated and independent program priors

- **Central question:** Which two collections of programs would an accurate universal composer help distinguish?
- **Understanding target:** Explain the inverse-correlated and independent Haar hypotheses, their averaged input density operators, and the known SWAP that converts an inverse program into the conjugate notation used in the moment proof. Distinguish correlations between unknown source matrices from the identical-copy structure inside each pool.
- **Dependencies and story role:** M04–M05, M09, M12–M13. Begins the converse with an information-theoretic experiment rather than a restriction to the proposed measurement.
- **Conceptual connection:** The product is the identity in one hypothesis and Haar distributed in the other. Conjugation in the mathematical ensemble is not an extra access operation granted to the processor.
- **Sources:** [Watrous §§3.1.1][w311] and [7.2.1][w721]; [two averaged priors](../science/converse.md#1-correlated-programs-and-independent-programs), [physical reduction](../science/converse.md#2-turning-a-composer-into-a-correlation-test).

### M21 — Harmonic subspaces beyond the faithful range

- **Central question:** What large common part of the mixed tensor space prevents the two priors from being easily distinguished?
- **Understanding target:** Interpret the harmonic subspace as the intersection of all cross-pool contraction kernels and obtain its discarded dimension fraction $q\leq mn/d^2$. Explain the role of a central projector and why the argument concerns the represented matrix algebra even when $m+n>d$.
- **Dependencies and story role:** M10, M12, M20. Identifies the geometric structure carrying the lower bound before comparing its moment blocks.
- **Conceptual connection:** Vanishing small-dimension sectors can be omitted without assuming faithful abstract algebra action. The mixed-centralizer and centrality ingredients are research dependencies, not consequences asserted from the anchor alone.
- **Sources:** [Watrous §§1.1.2][w112] and [7.1.2][w712], including the double-commutant framework; [harmonic dimension bound](../science/converse.md#11-a-large-common-harmonic-subspace), [all-dimensional representation argument](../science/converse.md#12-why-the-harmonic-decomposition-works-in-every-dimension) and its primary references.

### M22 — Ordered compressed moments limit distinguishability

- **Central question:** How does the common harmonic structure yield a quantitative trace-distance bound?
- **Understanding target:** Explain the common positive blocks of the compressed moments, their ordering $A\succeq B$, and the control of their missing masses. Connect these facts to $\mathrm{TD}(\Omega_{\rm c},\Omega_{\rm i})\leq\min\lbrace1,2mn/d^2\rbrace$. Distinguish commutation of an averaged moment with the compression from invariance of the harmonic subspace under every independent group element.
- **Dependencies and story role:** M09–M10, M20–M21. Converts representation structure and dimension counting into an operational information bound.
- **Conceptual connection:** The independent moment's block structure is essential; pretending its underlying representation preserves the harmonic subspace would omit a load-bearing step.
- **Sources:** [Watrous §§1.1.3][w113], [3.1.1][w311] and [7.2.2][w722] for norms, discrimination and invariant averages; [ordered compressed moments](../science/converse.md#13-the-two-harmonic-moment-blocks-are-ordered).

### M23 — A composer becomes a correlation test

- **Central question:** How does the moment bound constrain every successful processor, including adaptive ones?
- **Understanding target:** Follow symmetrization and the final maximally entangled output test to obtain $mn\geq p_0(d^2F_0-1)/2$. Explain why worst-case bounded sequential access can be precollected. For Haar averages, identify $\bar s-\bar p/d^2\leq2mn/d^2$ and distinguish success-weighted conditional fidelity $\bar s/\bar p$ from an unweighted conditional average.
- **Dependencies and story role:** M07–M09, M12–M13, M20–M22. Completes the unrestricted converse and its precise averaging extension.
- **Conceptual connection:** The test uses only the composed output, so requesting leftovers cannot evade the bound. The statement does not cover merely expected copy budgets or arbitrary non-Haar promise distributions.
- **Sources:** [Watrous §§2.3.2][w232], [3.1.1][w311] and [7.2.1][w721]; [composer-to-test proof](../science/converse.md#2-turning-a-composer-into-a-correlation-test), [Haar-average statement](../science/converse.md#haar-average-performance).

### M24 — The physical projected block for QSVT

- **Central question:** Which known operator must a circuit encode to reproduce the polar mechanism?
- **Understanding target:** Identify the right whole-copy symmetry projector $P$, the left Bell projector $Q$, and the routed contraction $A=JQP$. Explain $A v=w/d$ and $A^\dagger A=G/(dmn)$ on the symmetric domain. Distinguish the nontrivial singular spectrum of the compressed block from the binary spectrum of an unrestricted Bell projector.
- **Dependencies and story role:** M10, M12, M17–M19. Begins the implementation argument by locating the exact physical operator, before invoking a transformation theorem.
- **Conceptual connection:** QSVT is applied to a block defined by known subspaces. Its applicability does not supply a free reflection about an unknown input state.
- **Sources:** [Watrous §§1.1.3][w113] and [2.2.2][w222] for singular values and operator representations; [projected encoding](../science/implementation.md#1-a-projected-encoding-on-physical-registers), [compressed Gram operator](../science/implementation.md#the-compressed-gram-operator). The QSVT theorem is a primary dependency cited in that page.

### M25 — Spectral tails and finite circuit accuracy

- **Central question:** Why can a finite circuit work without a lower bound on every nonzero singular value?
- **Understanding target:** Explain the polynomial cutoff at singular value $1/(2d)$, the corresponding event $X<1/4$, and the small weighted contribution bounded by the exact moments. Track the separate errors from polar distortion, polynomial approximation and gate synthesis, including deterministic completion on failure.
- **Dependencies and story role:** M07–M08, M11, M18–M19, M24. Connects the exact mathematical channel to a finite implementation with an explicit fidelity budget.
- **Conceptual connection:** The approximation is justified on the promised states. A uniform inverse approximation near zero is unnecessary; the finite circuit uses larger sufficient copy constants than the exact polar channel.
- **Sources:** [Watrous §§1.1.3][w113] and [1.2.2][w122] for spectra and probability bounds; [polar approximation](../science/implementation.md#2-approximating-the-polar-map-on-the-supplied-states), [tail estimate](../science/implementation.md#controlling-the-small-singular-value-tail), [finite-precision guarantee](../science/implementation.md#3-deterministic-completion-and-finite-precision).

### M26 — Known symmetry phases and charged addressing

- **Central question:** What resources implement the known symmetry operations when coherent routing is charged?
- **Understanding target:** Relate a uniform permutation encoding to its symmetry-projector block and explain why the resulting reflection returns clean ancillas. Account for the explicit loop over possible swap addresses, its quadratic pool-size cost and multiplication by the QSVT degree. Interpret the resulting balanced fixed-error gate bound $\widetilde O(d^3)$ separately from the copy count.
- **Dependencies and story role:** M01, M07, M12, M24–M25. Completes the circuit argument by making its access assumptions and known-gate costs concrete.
- **Conceptual connection:** Mathematical symmetry does not make controlled routing free. Gate synthesis concerns known operations and contributes precision overhead; it does not compile unknown $U$ or $V$.
- **Sources:** [Watrous §§2.2.2][w222] and [7.1.1][w711] for isometries and permutation projectors; [clean symmetry phases](../science/implementation.md#4-known-phases-about-the-symmetric-input-subspace), [charged resources and synthesis references](../science/implementation.md#5-charged-circuit-resources).

### M27 — The balanced and unbalanced allocation law

- **Central question:** What becomes optimal when the construction and unrestricted converse are put together?
- **Understanding target:** Explain the fixed-error threshold $mn=\Theta(d^2)$, the balanced total scale $\Theta(d)$, and the $\Theta(d^2)$ requirement on one pool when the other has one copy. Interpret the finite upper and lower bounds on achievable output fidelity without equating them or reading a threshold as an exact constant.
- **Dependencies and story role:** M13, M19, M23, M26. Joins the three proof strands into a resource statement that applies across allocations.
- **Conceptual connection:** A construction with a joint-return promise meets, in dimension scaling, a lower bound that asks only for one composed output. Its proven optimality concerns supplied copies at fixed error, not gates or vanishing-error dependence.
- **Sources:** [Watrous §§2.2.1][w221], [3.1.1][w311] and [3.2.1][w321] for the operational framework; [finite fidelity interval and allocation table](../science/model.md#what-is-optimal), [resources and boundaries](../science/model.md#resources-and-boundaries).

### M28 — Precision regimes and exact Bell repetition

- **Central question:** How does the preferred sufficient strategy change when the requested error becomes very small?
- **Understanding target:** Compare the collective sufficient product $mn=O(d^2/\epsilon)$ and balanced supplies $O(d/\sqrt\epsilon)$ with independent paired Bell trials using $O(d^2\log(1/\epsilon))$ pairs. Explain the latter's exact accepted target, its failure completion and the different treatment of leftover specimens.
- **Dependencies and story role:** M08, M14, M19, M25, M27. Refines the global resource law by retaining the error parameter and the promised output.
- **Conceptual connection:** A strategy that wins at constant error need not win at extreme precision. The available converse does not settle the optimal approach to unit fidelity.
- **Sources:** [Watrous §§1.2.2][w122], [2.3.2][w232] and [6.3.1][w631]; [copy budgets and precision boundary](../science/construction.md#5-copy-budgets-and-the-precision-boundary), [precision comparison](../science/interpretation.md#precision-and-alternative-strategies).

### M29 — Returned programs and operational limits

- **Central question:** Which further capabilities do the established promises leave unresolved?
- **Understanding target:** Explain why approximate joint return is a one-shot statement, why successive reuse needs accumulated-error accounting, and why a Choi output does not itself execute the product on arbitrary fresh data. Retain the pure-unitary-program and full-access assumptions when considering noise, mixed programs, many outputs or expected budgets. Translate the gate count into its dependence on a qubit operation's dimension.
- **Dependencies and story role:** M03, M08, M13, M19, M23, M26–M28. Interprets the integrated result under its material assumptions and resource costs.
- **Conceptual connection:** The theorem establishes a capability for manipulating supplied quantum information. It does not establish an indefinite catalyst, a noisy-program theorem or a practical runtime advantage.
- **Sources:** [Watrous §§2.1.3][w213], [2.2.1][w221] and [3.2.1][w321] for joint states, channels and fidelity; [interpretation and limits](../science/interpretation.md), [converse boundaries](../science/converse.md#3-verification-and-boundaries), [charged resources](../science/implementation.md#5-charged-circuit-resources).

### M30 — The integrated result, evidence, and inherited tools

- **Central question:** How do the mechanism, obstruction, implementation and attribution support one coherent scientific claim?
- **Understanding target:** Trace the complete chain from Bell contraction and collective normalization through moments and joint fidelity, then from correlated priors and harmonic blocks to the universal converse, and finally to charged gates. Identify which finite checks test consequential identities, which arguments establish the all-dimensional theorem, and which tools are inherited from prior research.
- **Dependencies and story role:** M14–M29, drawing on the complete background phase. Integrates the narrative into the project's final scientific interpretation.
- **Conceptual connection:** The result is an optimal fixed-error copy-allocation law for the stated program task, with a stronger constructive return guarantee and an explicit implementation. PGM, representation theory and QSVT retain their prior attribution; finite numerical agreement does not replace proof or determine priority.
- **Sources:** [Watrous §§2.2.2][w222], [3.1.1][w311], [3.1.2][w312] and [7.1.2][w712] as foundations; [canonical model](../science/model.md), [scientific account](../science/README.md), [verification scope](../verification/README.md), [operational comparisons and inherited ingredients](../references/RELATED_WORK.md).

[watrous]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf
[w111]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=9
[w112]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=16
[w113]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=32
[w122]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=55
[w212]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=69
[w213]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=75
[w221]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=80
[w222]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=85
[w232]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=113
[w311]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=133
[w312]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=140
[w321]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=148
[w322]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=152
[w631]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=367
[w711]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=399
[w712]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=408
[w721]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=416
[w722]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=428
