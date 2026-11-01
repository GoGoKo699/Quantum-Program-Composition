# Scientific account

Unknown quantum operations can be stored as Choi states. This account asks how many such states are needed to create a program for the product of two operations when neither operation can be queried or described classically. A collective measurement achieves a constant-error copy-product threshold of order the square of the operation dimension, and a converse proves that arbitrary processors cannot improve that order.

Read the account in this order:

1. [Model and composition law](model.md): supplied resources, exact targets, fidelity convention, theorem statements and the copy-allocation tradeoff.
2. [Collective construction](construction.md): the two-pool physical instrument, its symmetry, exact moments and global return guarantee.
3. [Converse](converse.md): correlated and independent Choi ensembles, mixed harmonic tensors, and the all-dimensional lower bound.
4. [Implementation](implementation.md): projected singular-value transformation, known symmetry phases, finite precision and charged gates.
5. [Interpretation and limits](interpretation.md): what program composition enables, how the copy advantage arises, and the boundaries of the result.

The [related-work comparison](../references/RELATED_WORK.md) identifies inherited techniques and the distinct input models of earlier teleportation and program-processing tasks. The [verification guide](../verification/README.md) provides the commands and the tested scope of the finite checks. Those checks complement the analytical proofs; they do not replace them.

For the foundations and a worked example before the full proofs, use the [learning route](../learning/README.md). Its [Watrous bridge](../learning/WATROUS_BRIDGE.md) translates textbook conventions into the normalized programs used here.
