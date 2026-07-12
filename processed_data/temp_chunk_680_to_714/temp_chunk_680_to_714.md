# temp_chunk_680_to_714



## Page 1

C.2
Solving linear equations with factored matrices
667
so that
x = A−1b = A−1
k A−1
k−1 · · · A−1
1 b.
We can compute x using this formula, working from right to left:
z1
:=
A−1
1 b
z2
:=
A−1
2 z1 = A−1
2 A−1
1 b
...
zk−1
:=
A−1
k−1zk−2 = A−1
k−1 · · · A−1
1 b
x
:=
A−1
k zk−1 = A−1
k
· · · A−1
1 b.
The ith step of this process requires computing zi = A−1
i zi−1, i.e., solving the
linear equations Aizi = zi−1. If each of these equations is easy to solve (e.g., if Ai
is diagonal, lower or upper triangular, a permutation, etc.), this gives a method for
computing x = A−1b.
The step of expressing A in factored form (i.e., computing the factors Ai) is
called the factorization step, and the process of computing x = A−1b recursively,
by solving a sequence problems of the form Aizi = zi−1, is often called the solve
step. The total ﬂop count for solving Ax = b using this factor-solve method is f +s,
where f is the ﬂop count for computing the factorization, and s is the total ﬂop
count for the solve step. In many cases, the cost of the factorization, f, dominates
the total solve cost s. In this case, the cost of solving Ax = b, i.e., computing
x = A−1b, is just f.
Solving equations with multiple righthand sides
Suppose we need to solve the equations
Ax1 = b1,
Ax2 = b2,
. . . ,
Axm = bm,
where A ∈Rn×n is nonsingular.
In other words, we need to solve m sets of
linear equations, with the same coeﬃcient matrix, but diﬀerent righthand sides.
Alternatively, we can think of this as computing the matrix
X = A−1B
where
X =

x1
x2
· · ·
xm

∈Rn×m,
B =

b1
b2
· · ·
bm

∈Rn×m.
To do this, we ﬁrst factor A, which costs f. Then for i = 1, . . . , m we compute
A−1bi using the solve step. Since we only factor A once, the total eﬀort is
f + ms.
In other words, we amortize the factorization cost over the set of m solves. Had we
(needlessly) repeated the factorization step for each i, the cost would be m(f + s).
When the factorization cost f dominates the solve cost s, the factor-solve
method allows us to solve a small number of linear systems, with the same co-
eﬃcient matrix, at essentially the same cost as solving one. This is because the
most expensive step, the factorization, is done only once.


## Page 2

668
C
Numerical linear algebra background
We can use the factor-solve method to compute the inverse A−1 by solving
Ax = ei for i = 1, . . . , n, i.e., by computing A−1I. This requires one factorization
and n solves, so the cost is f + ns.
C.3
LU, Cholesky, and LDLT factorization
C.3.1
LU factorization
Every nonsingular matrix A ∈Rn×n can be factored as
A = PLU
where P ∈Rn×n is a permutation matrix, L ∈Rn×n is unit lower triangular, and
U ∈Rn×n is upper triangular and nonsingular. This is called the LU factorization
of A. We can also write the factorization as P T A = LU, where the matrix P T A is
obtained from A by re-ordering the rows. The standard algorithm for computing an
LU factorization is called Gaussian elimination with partial pivoting or Gaussian
elimination with row pivoting. The cost is (2/3)n3 ﬂops if no structure in A is
exploited, which is the case we consider ﬁrst.
Solving sets of linear equations using the LU factorization
The LU factorization, combined with the factor-solve approach, is the standard
method for solving a general set of linear equations Ax = b.
Algorithm C.1 Solving linear equations by LU factorization.
given a set of linear equations Ax = b, with A nonsingular.
1. LU factorization. Factor A as A = PLU ((2/3)n3 ﬂops).
2. Permutation. Solve Pz1 = b (0 ﬂops).
3. Forward substitution. Solve Lz2 = z1 (n2 ﬂops).
4. Backward substitution. Solve Ux = z2 (n2 ﬂops).
The total cost is (2/3)n3 + 2n2, or (2/3)n3 ﬂops if we keep only the leading term.
If we need to solve multiple sets of linear equations with diﬀerent righthand
sides, i.e., Axi = bi, i = 1, . . . , m, the cost is
(2/3)n3 + 2mn2,
since we factor A once, and carry out m pairs of forward and backward substi-
tutions. For example, we can solve two sets of linear equations, with the same
coeﬃcient matrix but diﬀerent righthand sides, at essentially the same cost as
solving one. We can compute the inverse A−1 by solving the equations Axi = ei,
where xi is the ith column of A−1, and ei is the ith unit vector. This costs (8/3)n3,
i.e., about 3n3 ﬂops.
If the matrix A has certain structure, for example banded or sparse, the LU fac-
torization can be computed in less than (2/3)n3 ﬂops, and the associated forward
and backward substitutions can also be carried out more eﬃciently.


## Page 3

C.3
LU, Cholesky, and LDLT factorization
669
LU factorization of banded matrices
Suppose the matrix A ∈Rn×n is banded, i.e., aij = 0 if |i −j| > k, where
k < n −1 is called the bandwidth of A. We are interested in the case where k ≪n,
i.e., the bandwidth is much smaller than the size of the matrix. In this case an
LU factorization of A can be computed in roughly 4nk2 ﬂops. The resulting upper
triangular matrix U has bandwidth at most 2k, and the lower triangular matrix L
has at most k + 1 nonzeros per column, so the forward and back substitutions can
be carried out in order 6nk ﬂops. Therefore if A is banded, the linear equations
Ax = b can be solved in about 4nk2 ﬂops.
LU factorization of sparse matrices
When the matrix A is sparse, the LU factorization usually includes both row and
column permutations, i.e., A is factored as
A = P1LUP2,
where P1 and P2 are permutation matrices, L is lower triangular, and U is upper
triangular. If the factors L and U are sparse, the forward and backward substi-
tutions can be carried out eﬃciently, and we have an eﬃcient method for solving
Ax = b. The sparsity of the factors L and U depends on the permutations P1 and
P2, which are chosen in part to yield relatively sparse factors.
The cost of computing the sparse LU factorization depends in a complicated
way on the size of A, the number of nonzero elements, its sparsity pattern, and
the particular algorithm used, but is often dramatically smaller than the cost of a
dense LU factorization. In many cases the cost grows approximately linearly with
n, when n is large. This means that when A is sparse, we can solve Ax = b very
eﬃciently, often with an order approximately n.
C.3.2
Cholesky factorization
If A ∈Rn×n is symmetric and positive deﬁnite, then it can be factored as
A = LLT
where L is lower triangular and nonsingular with positive diagonal elements. This
is called the Cholesky factorization of A, and can be interpreted as a symmetric
LU factorization (with L = U T ). The matrix L, which is uniquely determined
by A, is called the Cholesky factor of A. The cost of computing the Cholesky
factorization of a dense matrix, i.e., without exploiting any structure, is (1/3)n3
ﬂops, half the cost of an LU factorization.
Solving positive deﬁnite sets of equations using Cholesky factorization
The Cholesky factorization can be used to solve Ax = b when A is symmetric
positive deﬁnite.


## Page 4

670
C
Numerical linear algebra background
Algorithm C.2 Solving linear equations by Cholesky factorization.
given a set of linear equations Ax = b, with A ∈Sn
++.
1. Cholesky factorization. Factor A as A = LLT ((1/3)n3 ﬂops).
2. Forward substitution. Solve Lz1 = b (n2 ﬂops).
3. Backward substitution. Solve LT x = z1 (n2 ﬂops).
The total cost is (1/3)n3 + 2n2, or roughly (1/3)n3 ﬂops.
There are specialized algorithms, with a complexity much lower than (1/3)n3,
for Cholesky factorization of banded and sparse matrices.
Cholesky factorization of banded matrices
If A is symmetric positive deﬁnite and banded with bandwidth k, then its Cholesky
factor L is banded with bandwidth k, and can be calculated in nk2 ﬂops. The cost
of the associated solve step is 4nk ﬂops.
Cholesky factorization of sparse matrices
When A is symmetric positive deﬁnite and sparse, it is usually factored as
A = PLLT P T ,
where P is a permutation matrix and L is lower triangular with positive diagonal
elements. We can also express this as P T AP = LLT , i.e., LLT is the Cholesky
factorization of P T AP. We can interpret this as ﬁrst re-ordering the variables and
equations, and then forming the (standard) Cholesky factorization of the resulting
permuted matrix. Since P T AP is positive deﬁnite for any permutation matrix P,
we are free to choose any permutation matrix; for each choice there is a unique
associated Cholesky factor L. The choice of P, however, can greatly aﬀect the
sparsity of the factor L, which in turn can greatly aﬀect the eﬃciency of solving
Ax = b. Various heuristic methods are used to select a permutation P that leads
to a sparse factor L.
Example C.1
Cholesky factorization with an arrow sparsity pattern.
Consider a
sparse matrix of the form
A =

1
uT
u
D

where D ∈Rn×n is positive diagonal, and u ∈Rn. It can be shown that A is positive
deﬁnite if uT D−1u < 1. The Cholesky factorization of A is

1
uT
u
D

=

1
0
u
L
 
1
uT
0
LT

(C.2)
where L is lower triangular with LLT = D −uuT . For general u, the matrix D −uuT
is dense, so we can expect L to be dense.
Although the matrix A is very sparse
(most of its rows have just two nonzero elements), its Cholesky factors are almost
completely dense.


## Page 5

C.3
LU, Cholesky, and LDLT factorization
671
On the other hand, suppose we permute the ﬁrst row and column of A to the end.
After this re-ordering, we obtain the Cholesky factorization

D
u
uT
1

=

D1/2
0
uT D−1/2
√
1 −uT D−1u
 
D1/2
D−1/2u
0
√
1 −uT D−1u

.
Now the Cholesky factor has a diagonal 1,1 block, so it is very sparse.
This example illustrates that the re-ordering greatly aﬀects the sparsity of the Cholesky
factors. Here it was quite obvious what the best permutation is, and all good re-
ordering heuristics would select this re-ordering and permute the dense row and
column to the end. For more complicated sparsity patterns, it can be very diﬃcult
to ﬁnd the ‘best’ re-ordering (i.e., resulting in the greatest number of zero elements
in L), but various heuristics provide good suboptimal permutations.
For the sparse Cholesky factorization, the re-ordering permutation P is often
determined using only sparsity pattern of the matrix A, and not the particular
numerical values of the nonzero elements of A. Once P is chosen, we can also
determine the sparsity pattern of L without knowing the numerical values of the
nonzero entries of A. These two steps combined are called the symbolic factorization
of A, and form the ﬁrst step in a sparse Cholesky factorization. In contrast, the
permutation matrices in a sparse LU factorization do depend on the numerical
values in A, in addition to its sparsity pattern.
The symbolic factorization is then followed by the numerical factorization, i.e.,
the calculation of the nonzero elements of L. Software packages for sparse Cholesky
factorization often include separate routines for the symbolic and the numerical
factorization. This is useful in many applications, because the cost of the symbolic
factorization is signiﬁcant, and often comparable to the numerical factorization.
Suppose, for example, that we need to solve m sets of linear equations
A1x = b1,
A2x = b2,
. . . ,
Amx = bm
where the matrices Ai are symmetric positive deﬁnite, with diﬀerent numerical
values, but the same sparsity pattern. Suppose the cost of a symbolic factorization
is fsymb, the cost of a numerical factorization is fnum, and the cost of the solve step
is s. Then we can solve the m sets of linear equations in
fsymb + m(fnum + s)
ﬂops, since we only need to carry out the symbolic factorization once, for all m sets
of equations. If instead we carry out a separate symbolic factorization for each set
of linear equations, the ﬂop count is m(fsymb + fnum + s).
C.3.3
LDLT factorization
Every nonsingular symmetric matrix A can be factored as
A = PLDLT P T


## Page 6

672
C
Numerical linear algebra background
where P is a permutation matrix, L is lower triangular with positive diagonal
elements, and D is block diagonal, with nonsingular 1 × 1 and 2 × 2 diagonal
blocks. This is called an LDLT factorization of A. (The Cholesky factorization
can be considered a special case of LDLT factorization, with P = I and D = I.)
An LDLT factorization can be computed in (1/3)n3 ﬂops, if no structure of A is
exploited.
Algorithm C.3 Solving linear equations by LDLT factorization.
given a set of linear equations Ax = b, with A ∈Sn nonsingular.
1. LDLT factorization. Factor A as A = PLDLT P ((1/3)n3 ﬂops).
2. Permutation. Solve Pz1 = b (0 ﬂops).
3. Forward substitution. Solve Lz2 = z1 (n2 ﬂops).
4. (Block) diagonal solve. Solve Dz3 = z2 (order n ﬂops).
5. Backward substitution. Solve LT z4 = z3 (n2 ﬂops).
6. Permutation. Solve P T x = z4 (0 ﬂops).
The total cost is, keeping only the dominant term, (1/3)n3 ﬂops.
LDLT factorization of banded and sparse matrices
As with the LU and Cholesky factorizations, there are specialized methods for
calculating the LDLT factorization of a sparse or banded matrix. These are similar
to the analogous methods for Cholesky factorization, with the additional factor D.
In a sparse LDLT factorization, the permutation matrix P cannot be chosen only
on the basis of the sparsity pattern of A (as in a sparse Cholesky factorization); it
also depends on the particular nonzero values in the matrix A.
C.4
Block elimination and Schur complements
C.4.1
Eliminating a block of variables
In this section we describe a general method that can be used to solve Ax = b
by ﬁrst eliminating a subset of the variables, and then solving a smaller system
of linear equations for the remaining variables. For a dense unstructured matrix,
this approach gives no advantage. But when the submatrix of A associated with
the eliminated variables is easily factored (for example, if it is block diagonal or
banded) the method can be substantially more eﬃcient than a general method.
Suppose we partition the variable x ∈Rn into two blocks or subvectors,
x =
 x1
x2

,
where x1 ∈Rn1, x2 ∈Rn2. We conformally partition the linear equations Ax = b
as
 A11
A12
A21
A22
  x1
x2

=
 b1
b2

(C.3)


## Page 7

C.4
Block elimination and Schur complements
673
where A11 ∈Rn1×n1, A22 ∈Rn2×n2. Assuming that the submatrix A11 is invert-
ible, we can eliminate x1 from the equations, as follows. Using the ﬁrst equation,
we can express x1 in terms of x2:
x1 = A−1
11 (b1 −A12x2).
(C.4)
Substituting this expression into the second equation yields
(A22 −A21A−1
11 A12)x2 = b2 −A21A−1
11 b1.
(C.5)
We refer to this as the reduced equation obtained by eliminating x1 from the orig-
inal equation. The reduced equation (C.5) and the equation (C.4) together are
equivalent to the original equations (C.3). The matrix appearing in the reduced
equation is called the Schur complement of the ﬁrst block A11 in A:
S = A22 −A21A−1
11 A12
(see also §A.5.5).
The Schur complement S is nonsingular if and only if A is
nonsingular.
The two equations (C.5) and (C.4) give us an alternative approach to solving
the original system of equations (C.3). We ﬁrst form the Schur complement S, then
ﬁnd x2 by solving (C.5), and then calculate x1 from (C.4). We can summarize this
method as follows.
Algorithm C.4 Solving linear equations by block elimination.
given a nonsingular set of linear equations (C.3), with A11 nonsingular.
1. Form A−1
11 A12 and A−1
11 b1.
2. Form S = A22 −A21A−1
11 A12 and ˜b = b2 −A21A−1
11 b1.
3. Determine x2 by solving Sx2 = ˜b.
4. Determine x1 by solving A11x1 = b1 −A12x2.
Remark C.1 Interpretation as block factor-solve. Block elimination can be interpreted
in terms of the factor-solve approach described in §C.2.2, based on the factorization

A11
A12
A21
A22

=

A11
0
A21
S
 
I
A−1
11 A12
0
I

,
which can be considered a block LU factorization. This block LU factorization sug-
gests the following method for solving (C.3). We ﬁrst do a ‘block forward substitution’
to solve

A11
0
A21
S
 
z1
z2

=

b1
b2

,
and then solve

I
A−1
11 A12
0
I
 
x1
x2

=

z1
z2



## Page 8

674
C
Numerical linear algebra background
by ‘block backward substitution’.
This yields the same expressions as the block
elimination method:
z1
=
A−1
11 b1
z2
=
S−1(b2 −A21z1)
x2
=
z2
x1
=
z1 −A−1
11 A12z2.
In fact, the modern approach to the factor-solve method is based on block factor
and solve steps like these, with the block sizes optimally chosen for the processor (or
processors), cache sizes, etc.
Complexity analysis of block elimination method
To analyze the (possible) advantage of solving the set of linear equations using
block elimination, we carry out a ﬂop count. We let f and s denote the cost of
factoring A11 and carrying out the associated solve step, respectively. To keep the
analysis simple we assume (for now) that A12, A22, and A21 are treated as dense,
unstructured matrices. The ﬂop counts for each of the four steps in solving Ax = b
using block elimination are:
1. Computing A−1
11 A12 and A−1
11 b1 requires factoring A11 and n2 + 1 solves, so
it costs f + (n2 + 1)s, or just f + n2s, dropping the dominated term s.
2. Forming the Schur complement S requires the matrix multiply A21(A−1
11 A12),
which costs 2n2
2n1, and an n2 × n2 matrix subtraction, which costs n2
2 (and
can be dropped). The cost of forming ˜b = b2 −A21A−1
11 b1 is dominated by the
cost of forming S, and so can be ignored. The total cost of step 2, ignoring
dominated terms, is then 2n2
2n1.
3. To compute x2 = S−1˜b, we factor S and solve, which costs (2/3)n3
2.
4. Forming b1−A12x2 costs 2n1n2+n1 ﬂops. To compute x1 = A−1
11 (b1−A12x2),
we can use the factorization of A11 already computed in step 1, so only the
solve is necessary, which costs s. Both of these costs are dominated by other
terms, and can be ignored.
The total cost is then
f + n2s + 2n2
2n1 + (2/3)n3
2
(C.6)
ﬂops.
Eliminating an unstructured matrix
We ﬁrst consider the case when no structure in A11 is exploited. We factor A11
using a standard LU factorization, so f = (2/3)n3
1, and then solve using a forward
and a backward substitution, so s = 2n2
1. The ﬂop count for solving the equations
via block elimination is then
(2/3)n3
1 + n2(2n2
1) + 2n2
2n1 + (2/3)n3
2 = (2/3)(n1 + n2)3,


## Page 9

C.4
Block elimination and Schur complements
675
which is the same as just solving the larger set of equations using a standard LU
factorization. In other words, solving a set of equations by block elimination gives
no advantage when no structure of A11 is exploited.
On the other hand, when the structure of A11 allows us to factor and solve
more eﬃciently than the standard method, block elimination can be more eﬃcient
than applying the standard method.
Eliminating a diagonal matrix
If A11 is diagonal, no factorization is needed, and we can carry out a solve in n1
ﬂops, so we have f = 0 and s = n1. Substituting these values into (C.6) and
keeping only the leading terms yields
2n2
2n1 + (2/3)n3
2,
ﬂops, which is far smaller than (2/3)(n1+n2)3, the cost using the standard method.
In particular, the ﬂop count of the standard method grows cubicly in n1, whereas
for block elimination the ﬂop count grows only linearly in n1.
Eliminating a banded matrix
If A11 is banded with bandwidth k, we can carry out the factorization in about
f = 4k2n1 ﬂops, and the solve can be done in about s = 6kn1 ﬂops. The overall
complexity of solving Ax = b using block elimination is
4k2n1 + 6n2kn1 + 2n2
2n1 + (2/3)n3
2
ﬂops. Assuming k is small compared to n1 and n2, this simpliﬁes to 2n2
2n1+(2/3)n3
2,
the same as when A11 is diagonal. In particular, the complexity grows linearly in
n1, as opposed to cubicly in n1 for the standard method.
A matrix for which A11 is banded is sometimes called an arrow matrix since the
sparsity pattern, when n1 ≫n2, looks like an arrow pointing down and right. Block
elimination can solve linear equations with arrow structure far more eﬃciently than
the standard method.
Eliminating a block diagonal matrix
Suppose that A11 is block diagonal, with (square) block sizes m1, . . . , mk, where
n1 = m1 + · · · + mk.
In this case we can factor A11 by factoring each block
separately, and similarly we can carry out the solve step on each block separately.
Using standard methods for these we ﬁnd
f = (2/3)m3
1 + · · · + (2/3)m3
k,
s = 2m2
1 + · · · + 2m2
k,
so the overall complexity of block elimination is
(2/3)
k
X
i=1
m3
i + 2n2
k
X
i=1
m2
i + 2n2
2
k
X
i=1
mi + (2/3)n3
2.
If the block sizes are small compared to n1 and n1 ≫n2, the savings obtained by
block elimination is dramatic.


## Page 10

676
C
Numerical linear algebra background
The linear equations Ax = b, where A11 is block diagonal, are called partially
separable for the following reason.
If the subvector x2 is ﬁxed, the remaining
equations decouple into k sets of independent linear equations (which can be solved
separately). The subvector x2 is sometimes called the complicating variable since
the equations are much simpler when x2 is ﬁxed.
Using block elimination, we
can solve partially separable linear equations far more eﬃciently than by using a
standard method.
Eliminating a sparse matrix
If A11 is sparse, we can eliminate A11 using a sparse factorization and sparse solve
steps, so the values of f and s in (C.6) are much less than for unstructured A11.
When A11 in (C.3) is sparse and the other blocks are dense, and n2 ≪n1, we
say that A is a sparse matrix with a few dense rows and columns. Eliminating
the sparse block A11 provides an eﬃcient method for solving equations which are
sparse except for a few dense rows and columns.
An alternative is to simply apply a sparse factorization algorithm to the entire
matrix A. Most sparse solvers will handle dense rows and columns, and select a
permutation that results in sparse factors, and hence fast factorization and solve
times. This is more straightforward than using block elimination, but often slower,
especially in applications where we can exploit structure in the other blocks (see,
e.g., example C.4).
Remark C.2 As already suggested in remark C.1, these two methods for solving sys-
tems with a few dense rows and columns are closely related. Applying the elimination
method by factoring A11 and S as
A11 = P1L1U1P2,
S = P3L2U2,
can be interpreted as factoring A as

A11
A12
A21
A22

=

P1
0
0
P3
 
L1
0
P T
3 A21P T
2 U −1
1
L2
 
U1
L−1
1 P T
1 A12
0
U2
 
P2
0
0
I

,
followed by forward and backward substitutions.
C.4.2
Block elimination and structure
Symmetry and positive deﬁniteness
There are variants of the block elimination method that can be used when A is
symmetric, or symmetric and positive deﬁnite. When A is symmetric, so are A11
and the Schur complement S, so a symmetric factorization can be used for A11
and S. Symmetry can also be exploited in the other operations, such as the matrix
multiplies. Overall the savings over the nonsymmetric case is around a factor of
two.


## Page 11

C.4
Block elimination and Schur complements
677
Positive deﬁniteness can also be exploited in block elimination. When A is sym-
metric and positive deﬁnite, so are A11 and the Schur complement S, so Cholesky
factorizations can be used.
Exploiting structure in other blocks
Our complexity analysis above assumes that we exploit no structure in the matrices
A12, A21, A22, and the Schur complement S, i.e., they are treated as dense. But in
many cases there is structure in these blocks that can be exploited in forming the
Schur complement, factoring it, and carrying out the solve steps. In such cases the
computational savings of the block elimination method over a standard method
can be even higher.
Example C.2
Block triangular equations.
Suppose that A12 = 0, i.e., the linear
equations Ax = b have block lower triangular structure:

A11
0
A21
A22
 
x1
x2

=

b1
b2

.
In this case the Schur complement is just S = A22, and the block elimination method
reduces to block forward substitution:
x1
:=
A−1
11 b1
x2
:=
A−1
22 (b2 −A21x1).
Example C.3 Block diagonal and banded systems. Suppose that A11 is block diagonal,
with maximum block size l × l, and that A12, A21, and A22 are banded, say with
bandwidth k. In this case, A−1
11 is also block diagonal, with the same block sizes as
A11. Therefore the product A−1
11 A12 is also banded, with bandwidth k + l, and the
Schur complement, S = A22 −A21A−1
11 A12 is banded with bandwidth 2k + l. This
means that forming the Schur complement S can be done more eﬃciently, and that
the factorization and solve steps with S can be done eﬃciently. In particular, for
ﬁxed maximum block size l and bandwidth k, we can solve Ax = b with a number of
ﬂops that grows linearly with n.
Example C.4 KKT structure. Suppose that the matrix A has KKT structure, i.e.,
A =

A11
A12
AT
12
0

,
where A11 ∈Sp
++, and A12 ∈Rp×m with rank A12 = m. Since A11 ≻0, we can
use a Cholesky factorization. The Schur complement S = −AT
12A−1
11 A12 is negative
deﬁnite, so we can factor −S using a Cholesky factorization.


## Page 12

678
C
Numerical linear algebra background
C.4.3
The matrix inversion lemma
The idea of block elimination is to remove variables, and then solve a smaller set of
equations that involve the Schur complement of the original matrix with respect to
the eliminated variables. The same idea can be turned around: When we recognize
a matrix as a Schur complement, we can introduce new variables, and create a
larger set of equations to solve. In most cases there is no advantage to doing this,
since we end up with a larger set of equations. But when the larger set of equations
has some special structure that can be exploited to solve it, introducing variables
can lead to an eﬃcient method. The most common case is when another block of
variables can be eliminated from the larger matrix.
We start with the linear equations
(A + BC)x = b,
(C.7)
where A ∈Rn×n is nonsingular, and B ∈Rn×p, C ∈Rp×n. We introduce a new
variable y = Cx, and rewrite the equations as
Ax + By = b,
y = Cx,
or, in matrix form,
 A
B
C
−I
  x
y

=
 b
0

.
(C.8)
Note that our original coeﬃcient matrix, A + BC, is the Schur complement of −I
in the larger matrix that appears in (C.8). If we were to eliminate the variable y
from (C.8), we would get back the original equation (C.7).
In some cases, it can be more eﬃcient to solve the larger set of equations (C.8)
than the original, smaller set of equations (C.7).
This would be the case, for
example, if A, B, and C were relatively sparse, but the matrix A + BC were far
less sparse.
After introducing the new variable y, we can eliminate the original variable x
from the larger set of equations (C.8), using x = A−1(b −By). Substituting this
into the second equation y = Cx, we obtain
(I + CA−1B)y = CA−1b,
so that
y = (I + CA−1B)−1CA−1b.
Using x = A−1(b −By), we get
x =
 A−1 −A−1B(I + CA−1B)−1CA−1
b.
(C.9)
Since b is arbitrary, we conclude that
(A + BC)−1 = A−1 −A−1B
 I + CA−1B
−1 CA−1.
This is known as the matrix inversion lemma, or the Sherman-Woodbury-Morrison
formula.
The matrix inversion lemma has many applications. For example if p is small
(or even just not very large), it gives us a method for solving (A + BC)x = b,
provided we have an eﬃcient method for solving Au = v.


## Page 13

C.4
Block elimination and Schur complements
679
Diagonal or sparse plus low rank
Suppose that A is diagonal with nonzero diagonal elements, and we want to solve
an equation of the form (C.7). The straightforward solution would consist in ﬁrst
forming the matrix D = A + BC, and then solving Dx = b. If the product BC
is dense, then the complexity of this method is 2pn2 ﬂops to form A + BC, plus
(2/3)n3 ﬂops for the LU factorization of D, so the total cost is
2pn2 + (2/3)n3
ﬂops.
The matrix inversion lemma suggests a more eﬃcient method.
We can
calculate x by evaluating the expression (C.9) from right to left, as follows. We
ﬁrst evaluate z = A−1b (n ﬂops, since A is diagonal). Then we form the matrix
E = I + CA−1B (2p2n ﬂops). Next we solve Ew = Cz, which is a set of p linear
equations in p variables. The cost is (2/3)p3 ﬂops, plus 2pn to form Cz. Finally,
we evaluate x = z −A−1Bw (2pn ﬂops for the matrix-vector product Bw, plus
lower order terms). The total cost is
2p2n + (2/3)p3
ﬂops, dropping dominated terms. Comparing with the ﬁrst method, we see that
the second method is more eﬃcient when p < n. In particular if p is small and
ﬁxed, the complexity grows linearly with n.
Another important application of the matrix inversion lemma occurs when A is
sparse and nonsingular, and the matrices B and C are dense. Again we can compare
two methods. The ﬁrst method is to form the (dense) matrix A + BC, and to
solve (C.7) using a dense LU factorization. The cost of this method is 2pn2+(2/3)n3
ﬂops. The second method is based on evaluating the expression (C.9), using a
sparse LU factorization of A. Speciﬁcally, suppose that f is the cost of factoring
A as A = P1LUP2, and s is the cost of solving the factored system P1LUP2x = d.
We can evaluate (C.9) from right to left as follows. We ﬁrst factor A, and solve
p + 1 linear systems
Az = b,
AD = B,
to ﬁnd z ∈Rn, and D ∈Rn×p. The cost is f + (p + 1)s ﬂops. Next, we form the
matrix E = I + CD, and solve
Ew = Cz,
which is a set of p linear equations in p variables w.
The cost of this step is
2p2n + (2/3)p3 plus lower order terms. Finally, we evaluate x = z −Dw, at a cost
of 2pn ﬂops. This gives us a total cost of
f + ps + 2p2n + (2/3)p3
ﬂops. If f ≪(2/3)n3 and s ≪2n2, this is much lower than the complexity of the
ﬁrst method.
Remark C.3
The augmented system approach. A diﬀerent approach to exploiting
sparse plus low rank structure is to solve (C.8) directly using a sparse LU-solver. The
system (C.8) is a set of p + n linear equations in p + n variables, and is sometimes


## Page 14

680
C
Numerical linear algebra background
called the augmented system associated with (C.7). If A is very sparse and p is small,
then solving the augmented system using a sparse solver can be much faster than
solving the system (C.7) using a dense solver.
The augmented system approach is closely related to the method that we described
above. Suppose
A = P1LUP2
is a sparse LU factorization of A, and
I + CA−1B = P3 ˜L ˜U
is a dense LU factorization of I + CA−1B. Then

A
B
C
−I

=

P1
0
0
P3
 
L
0
P T
3 CP T
2 U −1
−˜L
 
U
L−1P T
1 B
0
˜U
 
P2
0
0
I

,
(C.10)
and this factorization can be used to solve the augmented system. It can be veriﬁed
that this is equivalent to the method based on the matrix inversion lemma that we
described above.
Of course, if we solve the augmented system using a sparse LU solver, we have no
control over the permutations that are selected. The solver might choose a factor-
ization diﬀerent from (C.10), and more expensive to compute. In spite of this, the
augmented system approach remains an attractive option. It is easier to implement
than the method based on the matrix inversion lemma, and it is numerically more
stable.
Low rank updates
Suppose A ∈Rn×n is nonsingular, u, v ∈Rn with 1 + vT A−1u̸ = 0, and we want
to solve two sets of linear equations
Ax = b,
(A + uvT )˜x = b.
The solution ˜x of the second system is called a rank-one update of x. The matrix
inversion lemma allows us to calculate the rank-one update ˜x very cheaply, once
we have computed x. We have
˜x
=
(A + uvT )−1b
=
(A−1 −
1
1 + vT A−1uA−1uvT A−1)b
=
x −
vT x
1 + vT A−1uA−1u.
We can therefore solve both systems by factoring A, computing x = A−1b and
w = A−1u, and then evaluating
˜x = x −
vT x
1 + vT ww.
The overall cost is f + 2s, as opposed to 2(f + s) if we were to solve for ˜x from
scratch.


## Page 15

C.5
Solving underdetermined linear equations
681
C.5
Solving underdetermined linear equations
To conclude this appendix, we mention a few important facts about underdeter-
mined linear equations
Ax = b,
(C.11)
where A ∈Rp×n with p < n. We assume that rank A = p, so there is at least one
solution for all b.
In many applications it is suﬃcient to ﬁnd just one particular solution ˆx. In
other situations we might need a complete parametrization of all solutions as
{x | Ax = b} = {Fz + ˆx | z ∈Rn−p}
(C.12)
where F is a matrix whose columns form a basis for the nullspace of A.
Inverting a nonsingular submatrix of A
The solution of the underdetermined system is straightforward if a p×p nonsingular
submatrix of A is known. We start by assuming that the ﬁrst p columns of A are
independent. Then we can write the equation Ax = b as
Ax =

A1
A2
 
x1
x2

= A1x1 + A2x2 = b,
where A1 ∈Rp×p is nonsingular. We can express x1 as
x1 = A−1
1 (b −A2x2) = A−1
1 b −A−1
1 A2x2.
This expression allows us to easily calculate a solution: we simply take ˆx2 = 0,
ˆx1 = A−1
1 b. The cost is equal to the cost of solving one square set of p linear
equations A1ˆx1 = b.
We can also parametrize all solutions of Ax = b, using x2 ∈Rn−p as a free
parameter. The general solution of Ax = b can be expressed as
x =
 x1
x2

=

−A−1
1 A2
I

x2 +

A−1
1 b
0

.
This gives a parametrization of the form (C.12) with
F =

−A−1
1 A2
I

,
ˆx =

A−1
1 b
0

.
To summarize, assume that the cost of factoring A1 is f and the cost of solving one
system of the form A1x = d is s. Then the cost of ﬁnding one solution of (C.11)
is f + s.
The cost of parametrizing all solutions (i.e., calculating F and ˆx) is
f + s(n −p + 1).
Now we consider the general case, when the ﬁrst p columns of A need not be
independent. Since rank A = p, we can select a set of p columns of A that is
independent, permute them to the front, and then apply the method described


## Page 16

682
C
Numerical linear algebra background
above.
In other words, we ﬁnd a permutation matrix P such that the ﬁrst p
columns of ˜A = AP are independent, i.e.,
˜A = AP =

A1
A2

,
where A1 is invertible. The general solution of ˜A˜x = b, where ˜x = P T x, is then
given by
˜x =

−A−1
1 A2
I

˜x2 +

A−1
1 b
0

.
The general solution of Ax = b is then given by
x = P ˜x = P

−A−1
1 A2
I

z + P

A−1
1 b
0

,
where z ∈Rn−p is a free parameter. This idea is useful when it is easy to identify
a nonsingular or easily inverted submatrix of A, for example, a diagonal matrix
with nonzero diagonal elements.
The QR factorization
If C ∈Rn×p with p ≤n and rank C = p, then it can be factored as
C =
 Q1
Q2
 
R
0

,
where Q1 ∈Rn×p and Q2 ∈Rn×(n−p) satisfy
QT
1 Q1 = I,
QT
2 Q2 = I,
QT
1 Q2 = 0,
and R ∈Rp×p is upper triangular with nonzero diagonal elements. This is called
the QR factorization of C. The QR factorization can be calculated in 2p2(n−p/3)
ﬂops. (The matrix Q is stored in a factored form that makes it possible to eﬃciently
compute matrix-vector products Qx and QT x.)
The QR factorization can be used to solve the underdetermined set of linear
equations (C.11). Suppose
AT =
 Q1
Q2
 
R
0

is the QR factorization of AT . Substituting in the equations it is clear that ˆx =
Q1R−T b satisﬁes the equations:
Aˆx = RT QT
1 Q1R−T b = b.
Moreover, the columns of Q2 form a basis for the nullspace of A, so the complete
solution set can be parametrized as
{x = ˆx + Q2z | z ∈Rn−p}.
The QR factorization method is the most common method for solving under-
determined equations. One drawback is that it is diﬃcult to exploit sparsity. The
factor Q is usually dense, even when C is very sparse.


## Page 17

C.5
Solving underdetermined linear equations
683
LU factorization of a rectangular matrix
If C ∈Rn×p with p ≤n and rank C = p, then it can be factored as
C = PLU
where P ∈Rn×n is a permutation matrix, L ∈Rn×p is unit lower triangular (i.e.,
lij = 0 for i < j and lii = 1), and U ∈Rp×p is nonsingular and upper triangular.
The cost is (2/3)p3 + p2(n −p) ﬂops if no structure in C is exploited.
If the matrix C is sparse, the LU factorization usually includes row and column
permutations, i.e., we factor C as
C = P1LUP2
where P1, P2 ∈Rp×p are permutation matrices. The LU factorization of a sparse
rectangular matrix can be calculated very eﬃciently, at a cost that is much lower
than for dense matrices.
The LU factorization can be used to solve underdetermined sets of linear equa-
tions. Suppose AT = PLU is the LU factorization of the matrix AT in (C.11), and
we partition L as
L =
 L1
L2

,
where L1 ∈Rp×p and L2 ∈R(n−p)×p. It is easily veriﬁed that the solution set can
be parametrized as (C.12) with
ˆx = P

L−T
1
U −T b
0

,
F = P

−L−T
1
LT
2
I

.


## Page 18

684
C
Numerical linear algebra background
Bibliography
Standard references for dense numerical linear algebra are Golub and Van Loan [GL89],
Demmel [Dem97], Trefethen and Bau [TB97], and Higham [Hig96]. The sparse Cholesky
factorization is covered in George and Liu [GL81]. Duﬀ, Erisman, and Reid [DER86] and
Duﬀ[Duf93] discuss the sparse LU and LDLT factorizations. The books by Gill, Murray,
and Wright [GMW81, §2.2], Wright [Wri97, chapter 11], and Nocedal and Wright [NW99,
§A.2] include introductions to numerical linear algebra that focus on problems arising in
numerical optimization.
High-quality implementations of common dense linear algebra algorithms are included
in the LAPACK package [ABB+99]. LAPACK is built upon the Basic Linear Algebra
Subprograms (BLAS), a library of routines for basic vector and matrix operations that can
be easily customized to take advantage of speciﬁc computer architectures. Several codes
for solving sparse linear equations are also available, including SPOOLES [APWW99],
SuperLU [DGL03], UMFPACK [Dav03], and WSMP [Gup00], to mention only a few.


## Page 19

References
[ABB+99]
E. Anderson, Z. Bai, C. Bischof, S. Blackford, J. Demmel, J. Dongarra, J. Du
Croz, A. Greenbaum, S. Hammarling, A. McKenney, and D. Sorensen. LA-
PACK Users’ Guide. Society for Industrial and Applied Mathematics, third
edition, 1999. Available from www.netlib.org/lapack.
[AE61]
K. J. Arrow and A. C. Enthoven. Quasi-concave programming. Econometrica,
29(4):779–800, 1961.
[AG03]
F. Alizadeh and D. Goldfarb. Second-order cone programming. Mathematical
Programming Series B, 95:3–51, 2003.
[AHO98]
F. Alizadeh, J.-P. A. Haeberly, and M. L. Overton.
Primal-dual interior-
point methods for semideﬁnite programming: Convergence rates, stability
and numerical results. SIAM Journal on Optimization, 8(3):746–768, 1998.
[Ali91]
F. Alizadeh. Combinatorial Optimization with Interior-Point Methods and
Semi-Deﬁnite Matrices. PhD thesis, University of Minnesota, 1991.
[And70]
T. W. Anderson. Estimation of covariance matrices which are linear com-
binations or whose inverses are linear combinations of given matrices.
In
R. C. Bose et al., editor, Essays in Probability and Statistics, pages 1–24.
University of North Carolina Press, 1970.
[APWW99] C. Ashcraft, D. Pierce, D. K. Wah, and J. Wu.
The Reference Man-
ual for SPOOLES Version 2.2:
An Object Oriented Software Library
for Solving Sparse Linear Systems of Equations, 1999.
Available from
www.netlib.org/linalg/spooles/spooles.2.2.html.
[AY98]
E. D. Andersen and Y. Ye.
A computational study of the homogeneous
algorithm for large-scale convex optimization. Computational Optimization
and Applications, 10:243–269, 1998.
[Bar02]
A. Barvinok.
A Course in Convexity, volume 54 of Graduate Studies in
Mathematics. American Mathematical Society, 2002.
[BB65]
E. F. Beckenbach and R. Bellman. Inequalities. Springer, second edition,
1965.
[BB91]
S. Boyd and C. Barratt. Linear Controller Design: Limits of Performance.
Prentice-Hall, 1991.
[BBI71]
A. Berman and A. Ben-Israel. More on linear inequalities with applications to
matrix theory. Journal of Mathematical Analysis and Applications, 33:482–
496, 1971.
[BD77]
P. J. Bickel and K. A. Doksum. Mathematical Statistics. Holden-Day, 1977.
[BDX04]
S. Boyd, P. Diaconis, and L. Xiao. Fastest mixing Markov chain on a graph.
SIAM Review, 46(4):667–689, 2004.
[BE93]
S. Boyd and L. El Ghaoui. Method of centers for minimizing generalized
eigenvalues. Linear Algebra and Its Applications, 188:63–111, 1993.


## Page 20

686
References
[BEFB94]
S. Boyd, L. El Ghaoui, E. Feron, and V. Balakrishnan. Linear Matrix In-
equalities in System and Control Theory. Society for Industrial and Applied
Mathematics, 1994.
[Ber73]
A. Berman. Cones, Matrices and Mathematical Programming. Springer, 1973.
[Ber90]
M. Berger. Convexity. The American Mathematical Monthly, 97(8):650–678,
1990.
[Ber99]
D. P. Bertsekas. Nonlinear Programming. Athena Scientiﬁc, second edition,
1999.
[Ber03]
D. P. Bertsekas. Convex Analysis and Optimization. Athena Scientiﬁc, 2003.
With A. Nedi´c and A. E. Ozdaglar.
[BF48]
T. Bonnesen and W. Fenchel. Theorie der konvexen K¨orper. Chelsea Pub-
lishing Company, 1948. First published in 1934.
[BF63]
R. Bellman and K. Fan. On systems of linear inequalities in Hermitian matrix
variables. In V. L. Klee, editor, Convexity, volume VII of Proceedings of the
Symposia in Pure Mathematics, pages 1–11. American Mathematical Society,
1963.
[BGT81]
R. G. Bland, D. Goldfarb, and M. J. Todd. The ellipsoid method: A survey.
Operations Research, 29(6):1039–1091, 1981.
[BI69]
A. Ben-Israel. Linear equations and inequalities on ﬁnite dimensional, real or
complex vector spaces: A uniﬁed theory. Journal of Mathematical Analysis
and Applications, 27:367–389, 1969.
[Bj¨o96]
A. Bj¨orck. Numerical Methods for Least Squares Problems. Society for In-
dustrial and Applied Mathematics, 1996.
[BKMR98] A. Brooke, D. Kendrick, A. Meeraus, and R. Raman. GAMS: A User’s Guide.
The Scientiﬁc Press, 1998.
[BL00]
J. M. Borwein and A. S. Lewis. Convex Analysis and Nonlinear Optimization.
Springer, 2000.
[BN78]
O. Barndorﬀ-Nielsen.
Information and Exponential Families in Statistical
Theory. John Wiley & Sons, 1978.
[Bon94]
J. V. Bondar. Comments on and complements to Inequalities: Theory of Ma-
jorization and Its Applications. Linear Algebra and Its Applications, 199:115–
129, 1994.
[Bor02]
B.
Borchers.
CSDP
User’s
Guide,
2002.
Available
from
www.nmt.edu/~borchers/csdp.html.
[BP94]
A. Berman and R. J. Plemmons. Nonnegative Matrices in the Mathemati-
cal Sciences. Society for Industrial and Applied Mathematics, 1994. First
published in 1979 by Academic Press.
[Bri61]
L. Brickman. On the ﬁeld of values of a matrix. Proceedings of the American
Mathematical Society, 12:61–66, 1961.
[BS00]
D. Bertsimas and J. Sethuraman. Moment problems and semideﬁnite opti-
mization. In H. Wolkowicz, R. Saigal, and L. Vandenberghe, editors, Hand-
book of Semideﬁnite Programming, chapter 16, pages 469–510. Kluwer Aca-
demic Publishers, 2000.
[BSS93]
M. S. Bazaraa, H. D. Sherali, and C. M. Shetty. Nonlinear Programming.
Theory and Algorithms. John Wiley & Sons, second edition, 1993.
[BT97]
D. Bertsimas and J. N. Tsitsiklis.
Introduction to Linear Optimization.
Athena Scientiﬁc, 1997.
[BTN98]
A. Ben-Tal and A. Nemirovski. Robust convex optimization. Mathematics
of Operations Research, 23(4):769–805, 1998.


## Page 21

References
687
[BTN99]
A. Ben-Tal and A. Nemirovski. Robust solutions of uncertain linear programs.
Operations Research Letters, 25(1):1–13, 1999.
[BTN01]
A. Ben-Tal and A. Nemirovski. Lectures on Modern Convex Optimization.
Analysis, Algorithms, and Engineering Applications. Society for Industrial
and Applied Mathematics, 2001.
[BY02]
S. J. Benson and Y. Ye. DSDP — A Software Package Implementing the
Dual-Scaling Algorithm for Semideﬁnite Programming, 2002. Available from
www-unix.mcs.anl.gov/~benson.
[BYT99]
E. Bai, Y. Ye, and R. Tempo. Bounded error parameter estimation: A se-
quential analytic center approach. IEEE Transactions on Automatic control,
44(6):1107–1117, 1999.
[Cal64]
E. Calabi. Linear systems of real quadratic forms. Proceedings of the Amer-
ican Mathematical Society, 15(5):844–846, 1964.
[CDS01]
S. S. Chen, D. L. Donoho, and M. A. Saunders. Atomic decomposition by
basis pursuit. SIAM Review, 43(1):129–159, 2001.
[CGGS98]
S. Chandrasekaran, G. H. Golub, M. Gu, and A. H. Sayed. Parameter es-
timation in the presence of bounded data uncertainties. SIAM Journal of
Matrix Analysis and Applications, 19(1):235–252, 1998.
[CH53]
R. Courant and D. Hilbert.
Method of Mathematical Physics. Volume 1.
Interscience Publishers, 1953. Tranlated and revised from the 1937 German
original.
[CK77]
B. D. Craven and J. J. Koliha. Generalizations of Farkas’ theorem. SIAM
Journal on Numerical Analysis, 8(6), 1977.
[CT91]
T. M. Cover and J. A. Thomas. Elements of Information Theory. John Wiley
& Sons, 1991.
[Dan63]
G. B. Dantzig. Linear Programming and Extensions. Princeton University
Press, 1963.
[Dav63]
C. Davis. Notions generalizing convexity for functions deﬁned on spaces of
matrices.
In V. L. Klee, editor, Convexity, volume VII of Proceedings of
the Symposia in Pure Mathematics, pages 187–201. American Mathematical
Society, 1963.
[Dav03]
T.
A.
Davis.
UMFPACK
User
Guide,
2003.
Available
from
www.cise.ufl.edu/research/sparse/umfpack.
[DDB95]
M. A. Dahleh and I. J. Diaz-Bobillo. Control of Uncertain Systems: A Linear
Programming Approach. Prentice-Hall, 1995.
[Deb59]
G. Debreu. Theory of Value: An Axiomatic Analysis of Economic Equilib-
rium. Yale University Press, 1959.
[Dem97]
J. W. Demmel. Applied Numerical Linear Algebra. Society for Industrial and
Applied Mathematics, 1997.
[DER86]
I. S. Duﬀ, A. M. Erismann, and J. K. Reid.
Direct Methods for Sparse
Matrices. Clarendon Press, 1986.
[DGL03]
J. W. Demmel, J. R. Gilbert, and X. S. Li. SuperLU Users’ Guide, 2003.
Available from crd.lbl.gov/~xiaoye/SuperLU.
[dH93]
D. den Hertog. Interior Point Approach to Linear, Quadratic and Convex
Programming. Kluwer, 1993.
[DHS99]
R. O. Duda, P. E. Hart, and D. G. Stork. Pattern Classiﬁcation. John Wiley
& Sons, second edition, 1999.
[Dik67]
I. Dikin. Iterative solution of problems of linear and quadratic programming.
Soviet Mathematics Doklady, 8(3):674–675, 1967.


## Page 22

688
References
[DLW00]
T. N. Davidson, Z.-Q. Luo, and K. M. Wong. Design of orthogonal pulse
shapes for communications via semideﬁnite programming. IEEE Transactions
on Signal Processing, 48(5):1433–1445, 2000.
[DP00]
G. E. Dullerud and F. Paganini. A Course in Robust Control Theory: A
Convex Approach. Springer, 2000.
[DPZ67]
R. J. Duﬃn, E. L. Peterson, and C. Zener. Geometric Programming. Theory
and Applications. John Wiley & Sons, 1967.
[DS96]
J. E. Dennis and R. S. Schnabel. Numerical Methods for Unconstrained Opti-
mization and Nonlinear Equations. Society for Industrial and Applied Math-
ematics, 1996. First published in 1983 by Prentice-Hall.
[Duf93]
I. S. Duﬀ. The solution of augmented systems. In D. F. Griﬃths and G. A.
Watson, editors, Numerical Analysis 1993. Proceedings of the 15th Dundee
Conference, pages 40–55. Longman Scientiﬁc & Technical, 1993.
[Eck80]
J. G. Ecker. Geometric programming: Methods, computations and applica-
tions. SIAM Review, 22(3):338–362, 1980.
[Egg58]
H. G. Eggleston. Convexity. Cambridge University Press, 1958.
[EL97]
L. El Ghaoui and H. Lebret.
Robust solutions to least-squares problems
with uncertain data.
SIAM Journal of Matrix Analysis and Applications,
18(4):1035–1064, 1997.
[EM75]
J. Elzinga and T. G. Moore. A central cutting plane algorithm for the convex
programming problem. Mathematical Programming Studies, 8:134–145, 1975.
[EN00]
L. El Ghaoui and S. Niculescu, editors. Advances in Linear Matrix Inequality
Methods in Control. Society for Industrial and Applied Mathematics, 2000.
[EOL98]
L. El Ghaoui, F. Oustry, and H. Lebret.
Robust solutions to uncertain
semideﬁnite programs. SIAM Journal on Optimization, 9(1):33–52, 1998.
[ET99]
I. Ekeland and R. T´emam.
Convex Analysis and Variational Inequalities.
Classics in Applied Mathematics. Society for Industrial and Applied Mathe-
matics, 1999. Originally published in 1976.
[Far02]
J. Farkas. Theorie der einfachen Ungleichungen. Journal f¨ur die Reine und
Angewandte Mathematik, 124:1–27, 1902.
[FD85]
J. P. Fishburn and A. E. Dunlop. TILOS: A posynomial programming ap-
proach to transistor sizing. In IEEE International Conference on Computer-
Aided Design: ICCAD-85. Digest of Technical Papers, pages 326–328. IEEE
Computer Society Press, 1985.
[Fen83]
W. Fenchel. Convexity through the ages. In P. M. Gruber and J. M. Wills,
editors, Convexity and Its Applications, pages 120–130. Birkh¨auser Verlag,
1983.
[FGK99]
R. Fourer, D. M. Gay, and B. W. Kernighan. AMPL: A Modeling Language
for Mathematical Programming. Duxbury Press, 1999.
[FGW02]
A. Forsgren, P. E. Gill, and M. H. Wright. Interior methods for nonlinear
optimization. SIAM Review, 44(4):525–597, 2002.
[FKN98]
K. Fujisawa, M. Kojima, and K. Nakata. SDPA User’s Manual, 1998. Avail-
able from grid.r.dendai.ac.jp/sdpa.
[FL01]
M. Florenzano and C. Le Van. Finite Dimensional Convexity and Optimiza-
tion. Number 13 in Studies in Economic Theory. Springer, 2001.
[FM90]
A. V. Fiacco and G. P. McCormick.
Nonlinear Programming. Sequential
Unconstrained Minimization Techniques. Society for Industrial and Applied
Mathematics, 1990. First published in 1968 by Research Analysis Corpora-
tion.


## Page 23

References
689
[Fre56]
R. J. Freund. The introduction of risk into a programming model. Econo-
metrica, 24(3):253–263, 1956.
[FW56]
M. Frank and P. Wolfe. An algorithm for quadratic programming. Naval
Research Logistics Quarterly, 3:95–110, 1956.
[Gau95]
C. F. Gauss. Theory of the Combination of Observations Least Subject to
Errors. Society for Industrial and Applied Mathematics, 1995. Translated
from original 1820 manuscript by G. W. Stewart.
[GI03a]
D. Goldfarb and G. Iyengar. Robust convex quadratically constrained pro-
grams. Mathematical Programming Series B, 97:495–515, 2003.
[GI03b]
D. Goldfarb and G. Iyengar. Robust portfolio selection problems. Mathemat-
ics of Operations Research, 28(1):1–38, 2003.
[GKT51]
D. Gale, H. W. Kuhn, and A. W. Tucker.
Linear programming and the
theory of games. In T. C. Koopmans, editor, Activity Analysis of Production
and Allocation, volume 13 of Cowles Commission for Research in Economics
Monographs, pages 317–335. John Wiley & Sons, 1951.
[GL81]
A. George and J. W.-H. Liu.
Computer solution of large sparse positive
deﬁnite systems. Prentice-Hall, 1981.
[GL89]
G. Golub and C. F. Van Loan. Matrix Computations. Johns Hopkins Uni-
versity Press, second edition, 1989.
[GLS88]
M. Gr¨otschel, L. Lovasz, and A. Schrijver. Geometric Algorithms and Com-
binatorial Optimization. Springer, 1988.
[GLY96]
J.-L. Goﬃn, Z.-Q. Luo, and Y. Ye. Complexity analysis of an interior cutting
plane method for convex feasibility problems. SIAM Journal on Optimization,
6:638–652, 1996.
[GMS+86]
P. E. Gill, W. Murray, M. A. Saunders, J. A. Tomlin, and M. H. Wright. On
projected newton barrier methods for linear programming and an equivalence
to Karmarkar’s projective method. Mathematical Programming, 36:183–209,
1986.
[GMW81]
P. E. Gill, W. Murray, and M. H. Wright. Practical Optimization. Academic
Press, 1981.
[Gon92]
C. C. Gonzaga. Path-following methods for linear programming. SIAM Re-
view, 34(2):167–224, 1992.
[Gow85]
J. C. Gower. Properties of Euclidean and non-Euclidean distance matrices.
Linear Algebra and Its Applications, 67:81–97, 1985.
[Gup00]
A. Gupta. WSMP: Watson Sparse Matrix Package. Part I — Direct Solution
of Symmetric Sparse Systems. Part II — Direct Solution of General Sparse
Systems, 2000. Available from www.cs.umn.edu/~agupta/wsmp.
[GW95]
M. X. Goemans and D. P. Williamson. Improved approximation algorithms
for maximum cut and satisﬁability problems using semideﬁnite programming.
Journal of the Association for Computing Machinery, 42(6):1115–1145, 1995.
[Han98]
P. C. Hansen. Rank-Deﬁcient and Discrete Ill-Posed Problems. Numerical
Aspects of Linear Inversion. Society for Industrial and Applied Mathematics,
1998.
[HBL01]
M. del Mar Hershenson, S. P. Boyd, and T. H. Lee. Optimal design of a CMOS
op-amp via geometric programming. IEEE Transactions on Computer-Aided
Design of Integrated Circuits and Systems, 20(1):1–21, 2001.
[Hes68]
M. R. Hestenes. Pairs of quadratic forms. Linear Algebra and Its Applications,
1:397–407, 1968.
[Hig96]
N. J. Higham. Accuracy and Stability of Numerical Algorithms. Society for
Industrial and Applied Mathematics, 1996.


## Page 24

690
References
[Hil57]
C. Hildreth. A quadratic programming procedure. Naval Research Logistics
Quarterly, 4:79–85, 1957.
[HJ85]
R. A. Horn and C. A. Johnson. Matrix Analysis. Cambridge University Press,
1985.
[HJ91]
R. A. Horn and C. A. Johnson.
Topics in Matrix Analysis.
Cambridge
University Press, 1991.
[HLP52]
G. H. Hardy, J. E. Littlewood, and G. P´olya. Inequalities. Cambridge Uni-
versity Press, second edition, 1952.
[HP94]
R. Horst and P. Pardalos. Handbook of Global Optimization. Kluwer, 1994.
[HRVW96] C. Helmberg, F. Rendl, R. Vanderbei, and H. Wolkowicz.
An interior-
point method for semideﬁnite programming. SIAM Journal on Optimization,
6:342–361, 1996.
[HTF01]
T. Hastie, R. Tibshirani, and J. Friedman. The Elements of Statistical Learn-
ing. Data Mining, Inference, and Prediction. Springer, 2001.
[Hub64]
P. J. Huber.
Robust estimation of a location parameter.
The Annals of
Mathematical Statistics, 35(1):73–101, 1964.
[Hub81]
P. J. Huber. Robust Statistics. John Wiley & Sons, 1981.
[HUL93]
J.-B. Hiriart-Urruty and C. Lemar´echal. Convex Analysis and Minimization
Algorithms. Springer, 1993. Two volumes.
[HUL01]
J.-B. Hiriart-Urruty and C. Lemar´echal.
Fundamentals of Convex Analy-
sis. Springer, 2001. Abridged version of Convex Analysis and Minimization
Algorithms volumes 1 and 2.
[Isi64]
K. Isii. Inequalities of the types of Chebyshev and Cram´er-Rao and math-
ematical programming. Annals of The Institute of Statistical Mathematics,
16:277–293, 1964.
[Jar94]
F. Jarre.
Optimal ellipsoidal approximations around the analytic center.
Applied Mathematics and Optimization, 30:15–19, 1994.
[Jen06]
J. L. W. V. Jensen.
Sur les fonctions convexes et les in´egalit´es entre les
valeurs moyennes. Acta Mathematica, 30:175–193, 1906.
[Joh85]
F. John. Extremum problems with inequalities as subsidiary conditions. In
J. Moser, editor, Fritz John, Collected Papers, pages 543–560. Birkh¨auser
Verlag, 1985. First published in 1948.
[Kan52]
L. V. Kantorovich. Functional Analysis and Applied Mathematics. National
Bureau of Standards, 1952. Translated from Russian by C. D. Benster. First
published in 1948.
[Kan60]
L. V. Kantorovich. Mathematical methods of organizing and planning pro-
duction. Management Science, 6(4):366–422, 1960. Translated from Russian.
First published in 1939.
[Kar84]
N. Karmarkar. A new polynomial-time algorithm for linear programming.
Combinatorica, 4(4):373–395, 1984.
[Kel60]
J. E. Kelley. The cutting-plane method for solving convex programs. Journal
of the Society for Industrial and Applied Mathematics, 8(4):703–712, 1960.
[Kle63]
V. L. Klee, editor. Convexity, volume 7 of Proceedings of Symposia in Pure
Mathematics. American Mathematical Society, 1963.
[Kle71]
V. Klee.
What is a convex set?
The American Mathematical Monthly,
78(6):616–631, 1971.
[KN77]
M. G. Krein and A. A. Nudelman. The Markov Moment Problem and Ex-
tremal Problems.
American Mathematical Society, 1977.
Translated from
Russian. First published in 1973.


## Page 25

References
691
[Koo51]
T. C. Koopmans, editor.
Activity Analysis of Production and Allocation,
volume 13 of Cowles Commission for Research in Economics Monographs.
John Wiley & Sons, 1951.
[KS66]
S. Karlin and W. J. Studden. TchebycheﬀSystems: With Applications in
Analysis and Statistics. John Wiley & Sons, 1966.
[KSH97]
M. Kojima, S. Shindoh, and S. Hara. Interior-point methods for the monotone
semideﬁnite linear complementarity problem in symmetric matrices. SIAM
Journal on Optimization, 7(1):86–125, 1997.
[KSH00]
T. Kailath, A. H. Sayed, and B. Hassibi. Linear Estimation. Prentice-Hall,
2000.
[KSJA91]
J. M. Kleinhaus, G. Sigl, F. M. Johannes, and K. J. Antreich. GORDIAN:
VLSI placement by quadratic programming and slicing optimization. IEEE
Transactions on Computer-Aided Design of Integrated Circuits and Systems,
10(3):356–200, 1991.
[KT51]
H. W. Kuhn and A. W. Tucker. Nonlinear programming. In J. Neyman, ed-
itor, Proceedings of the Second Berkeley Symposium on Mathematical Statis-
tics and Probability, pages 481–492. University of California Press, 1951.
[Kuh76]
H. W. Kuhn. Nonlinear programming. A historical view. In R. W. Cottle
and C. E. Lemke, editors, Nonlinear Programming, volume 9 of SIAM-AMS
Proceedings, pages 1–26. American Mathematical Society, 1976.
[Las95]
J. B. Lasserre. A new Farkas lemma for positive semideﬁnite matrices. IEEE
Transactions on Automatic Control, 40(6):1131–1133, 1995.
[Las02]
J. B. Lasserre.
Bounds on measures satisfying moment conditions.
The
Annals of Applied Probability, 12(3):1114–1137, 2002.
[Lay82]
S. R. Lay. Convex Sets and Their Applications. John Wiley & Sons, 1982.
[LH66]
B. Liˆe˜u and P. Huard. La m´ethode des centres dans un espace topologique.
Numerische Mathematik, 8:56–67, 1966.
[LH95]
C. L. Lawson and R. J. Hanson. Solving Least Squares Problems. Society
for Industrial and Applied Mathematics, 1995. First published in 1974 by
Prentice-Hall.
[LMS94]
I. J. Lustig, R. E. Marsten, and D. F. Shanno. Interior point methods for
linear programming: Computational state of the art.
ORSA Journal on
Computing, 6(1):1–14, 1994.
[LO96]
A. S. Lewis and M. L. Overton. Eigenvalue optimization. Acta Numerica,
5:149–190, 1996.
[L¨of04]
J. L¨ofberg. YALMIP : A toolbox for modeling and optimization in MAT-
LAB.
In Proceedings of the IEEE International Symposium on Com-
puter Aided Control Systems Design, pages 284–289, 2004. Available from
control.ee.ethz.ch/~joloef/yalmip.php.
[L¨ow34]
K. L¨owner.
¨Uber monotone Matrixfunktionen. Mathematische Zeitschrift,
38:177–216, 1934.
[LSZ00]
Z.-Q. Luo, J. F. Sturm, and S. Zhang. Conic convex programming and self-
dual embedding. Optimization Methods and Software, 14:169–218, 2000.
[Lue68]
D. G. Luenberger. Quasi-convex programming. SIAM Journal on Applied
Mathematics, 16(5), 1968.
[Lue69]
D. G. Luenberger. Optimization by Vector Space Methods. John Wiley &
Sons, 1969.
[Lue84]
D. G. Luenberger.
Linear and Nonlinear Programming.
Addison-Wesley,
second edition, 1984.


## Page 26

692
References
[Lue95]
D. G. Luenberger. Microeconomic Theory. McGraw-Hill, 1995.
[Lue98]
D. G. Luenberger. Investment Science. Oxford University Press, 1998.
[Luo03]
Z.-Q. Luo.
Applications of convex optimization in signal processing and
digital communication.
Mathematical Programming Series B, 97:177–207,
2003.
[LVBL98]
M. S. Lobo, L. Vandenberghe, S. Boyd, and H. Lebret. Applications of second-
order cone programming. Linear Algebra and Its Applications, 284:193–228,
1998.
[Man65]
O. Mangasarian. Linear and nonlinear separation of patterns by linear pro-
gramming. Operations Research, 13(3):444–452, 1965.
[Man94]
O. Mangasarian. Nonlinear Programming. Society for Industrial and Applied
Mathematics, 1994. First published in 1969 by McGraw-Hill.
[Mar52]
H. Markowitz. Portfolio selection. The Journal of Finance, 7(1):77–91, 1952.
[Mar56]
H. Markowitz. The optimization of a quadratic function subject to linear
constraints. Naval Research Logistics Quarterly, 3:111–133, 1956.
[MDW+02] W.-K. Ma, T. N. Davidson, K. M. Wong, Z.-Q. Luo, and P.-C. Ching. Quasi-
maximum-likelihood multiuser detection using semi-deﬁnite relaxation with
application to synchronous CDMA. IEEE Transactions on Signal Processing,
50:912–922, 2002.
[Meh92]
S. Mehrotra. On the implementation of a primal-dual interior point method.
SIAM Journal on Optimization, 2(4):575–601, 1992.
[Mey00]
C. D. Meyer. Matrix Analysis and Applied Linear Algebra. Society for In-
dustrial and Applied Mathematics, 2000.
[ML57]
M. Marcus and L. Lopes. Inequalities for symmetric functions and Hermitian
matrices. Canadian Journal of Mathematics, 9:305–312, 1957.
[MO60]
A. W. Marshall and I. Olkin. Multivariate Chebyshev inequalities. Annals
of Mathematical Statistics, 32(4):1001–1014, 1960.
[MO79]
A. W. Marshall and I. Olkin. Inequalities: Theory of Majorization and Its
Applications. Academic Press, 1979.
[Mon97]
R. D. C. Monteiro. Primal-dual path-following algorithms for semideﬁnite
programming. SIAM Journal on Optimization, 7(3):663–678, 1997.
[MOS02]
MOSEK ApS. The MOSEK Optimization Tools. User’s Manual and Refer-
ence, 2002. Available from www.mosek.com.
[Mot33]
T. Motzkin. Beitr¨age zur Theorie der linearen Ungleichungen. PhD thesis,
University of Basel, 1933.
[MP68]
R. F. Meyer and J. W. Pratt. The consistent assessment and fairing of pref-
erence functions. IEEE Transactions on Systems Science and Cybernetics,
4(3):270–278, 1968.
[MR95]
R. Motwani and P. Raghavan. Randomized Algorithms. Cambridge University
Press, 1995.
[MZ89]
M. Morari and E. Zaﬁriou. Robust Process Control. Prentice-Hall, 1989.
[Nes98]
Y. Nesterov. Semideﬁnite relaxations and nonconvex quadratic optimization.
Optimization Methods and Software, 9(1-3):141–160, 1998.
[Nes00]
Y. Nesterov.
Squared functional systems and optimization problems.
In
J. Frenk, C. Roos, T. Terlaky, and S. Zhang, editors, High Performance
Optimization Techniques, pages 405–440. Kluwer, 2000.
[Nik54]
H. Nikaidˆo. On von Neumann’s minimax theorem. Paciﬁc Journal of Math-
ematics, 1954.


## Page 27

References
693
[NN94]
Y. Nesterov and A. Nemirovskii. Interior-Point Polynomial Methods in Con-
vex Programming. Society for Industrial and Applied Mathematics, 1994.
[NT98]
Y. E. Nesterov and M. J. Todd. Primal-dual interior-point methods for self-
scaled cones. SIAM Journal on Optimization, 8(2):324–364, 1998.
[NW99]
J. Nocedal and S. J. Wright. Numerical Optimization. Springer, 1999.
[NWY00]
Y. Nesterov, H. Wolkowicz, and Y. Ye. Semideﬁnite programming relaxations
of nonconvex quadratic optimization. In H. Wolkowicz, R. Saigal, and L. Van-
denberghe, editors, Handbook of Semideﬁnite Programming, chapter 13, pages
361–419. Kluwer Academic Publishers, 2000.
[NY83]
A. Nemirovskii and D. Yudin. Problem Complexity and Method Eﬃciency in
Optimization. John Wiley & Sons, 1983.
[OR00]
J. M. Ortega and W. C. Rheinboldt. Iterative Solution of Nonlinear Equations
in Several Variables. Society for Industrial and Applied Mathematics, 2000.
First published in 1970 by Academic Press.
[Par71]
V. Pareto. Manual of Political Economy. A. M. Kelley Publishers, 1971.
Translated from the French edition. First published in Italian in 1906.
[Par98]
B. N. Parlett. The Symmetric Eigenvalue Problem. Society for Industrial and
Applied Mathematics, 1998. First published in 1980 by Prentice-Hall.
[Par00]
P. A. Parrilo. Structured Semideﬁnite Programs and Semialgebraic Geometry
Methods in Robustness and Optimization. PhD thesis, California Institute of
Technology, 2000.
[Par03]
P. A. Parrilo. Semideﬁnite programming relaxations for semialgebraic prob-
lems. Mathematical Programming Series B, 96:293–320, 2003.
[Pet76]
E. L. Peterson. Geometric programming. SIAM Review, 18(1):1–51, 1976.
[Pin95]
J. Pinter. Global Optimization in Action, volume 6 of Nonconvex Optimiza-
tion and Its Applications. Kluwer, 1995.
[Pol87]
B. T. Polyak. Introduction to Optimization. Optimization Software, 1987.
Translated from Russian.
[Pon67]
J. Ponstein. Seven kinds of convexity. SIAM Review, 9(1):115–119, 1967.
[Pr´e71]
A. Pr´ekopa. Logarithmic concave measures with application to stochastic
programming. Acta Scientiarum Mathematicarum, 32:301–315, 1971.
[Pr´e73]
A. Pr´ekopa. On logarithmic concave measures and functions. Acta Scien-
tiarum Mathematicarum, 34:335–343, 1973.
[Pr´e80]
A. Pr´ekopa. Logarithmic concave measures and related topics. In M. A. H.
Dempster, editor, Stochastic Programming, pages 63–82. Academic Press,
1980.
[Pro01]
J. G. Proakis. Digital Communications. McGraw-Hill, fourth edition, 2001.
[PRT02]
J. Peng, C. Roos, and T. Terlaky.
Self-Regularity. A New Paradigm for
Primal-Dual Interior-Point Algorithms. Princeton University Press, 2002.
[PS98]
C. H. Papadimitriou and K. Steiglitz.
Combinatorial Optimization. Algo-
rithms and Complexity. Dover Publications, 1998. First published in 1982 by
Prentice-Hall.
[PSU88]
A. L. Peressini, F. E. Sullivan, and J. J. Uhl. The Mathematics of Nonlinear
Programming. Undergraduate Texts in Mathematics. Springer, 1988.
[Puk93]
F. Pukelsheim. Optimal Design of Experiments. Wiley & Sons, 1993.
[Ren01]
J. Renegar. A Mathematical View of Interior-Point Methods in Convex Op-
timization. Society for Industrial and Applied Mathematics, 2001.
[Roc70]
R. T. Rockafellar. Convex Analysis. Princeton University Press, 1970.


## Page 28

694
References
[Roc89]
R. T. Rockafellar. Conjugate Duality and Optimization. Society for Industrial
and Applied Mathematics, 1989. First published in 1974.
[Roc93]
R. T. Rockafellar.
Lagrange multipliers and optimality.
SIAM Review,
35:183–283, 1993.
[ROF92]
L. Rudin, S. J. Osher, and E. Fatemi. Nonlinear total variation based noise
removal algorithms. Physica D, 60:259–268, 1992.
[Ros65]
J. B. Rosen. Pattern separation by convex programming. Journal of Mathe-
matical Analysis and Applications, 10:123–134, 1965.
[Ros99]
S. M. Ross. An Introduction to Mathematical Finance: Options and Other
Topics. Cambridge University Press, 1999.
[RTV97]
C. Roos, T. Terlaky, and J.-Ph. Vial.
Theory and Algorithms for Linear
Optimization. An Interior Point Approach. John Wiley & Sons, 1997.
[Rud76]
W. Rudin. Principles of Mathematical Analysis. McGraw-Hill, 1976.
[RV73]
A. W. Roberts and D. E. Varberg. Convex Functions. Academic Press, 1973.
[RW97]
D. Ralph and S. J. Wright.
Superlinear convergence of an interior-point
method for monotone variational inequalities. In M. C. Ferris and J.-S. Pang,
editors, Complementarity and Variational Problems: State of the Art, pages
345–385. Society for Industrial and Applied Mathematics, 1997.
[RWR98]
C. V. Rao, S. J. Wright, and J. B. Rawlings. Application of interior-point
methods to model predictive control. Journal of Optimization Theory and
Applications, 99(3):723–757, 1998.
[Sch35]
I. J. Schoenberg.
Remarks to Maurice Fr´echet’s article “Sur la d´eﬁnition
axiomatique d’une classe d’espaces distanci´es vectoriellement applicable sur
l’espace de Hilbert”. Annals of Mathematics, 38(3):724–732, 1935.
[Sch82]
S. Schaible. Bibliography in fractional programming. Zeitschrift f¨ur Opera-
tions Research, 26:211–241, 1982.
[Sch83]
S. Schaible. Fractional programming. Zeitschrift f¨ur Operations Research,
27:39–54, 1983.
[Sch86]
A. Schrijver.
Theory of Linear and Integer Programming.
John Wiley &
Sons, 1986.
[Sch91]
L. L. Scharf. Statistical Signal Processing. Detection, Estimation, and Time
Series Analysis. Addison Wesley, 1991. With C´edric Demeure.
[SDJ91]
G. Sigl, K. Doll, and F. M. Johannes. Analytical placement: A linear or
quadratic objective function? In Proceedings of the 28th ACM/IEEE Design
Automation Conference, pages 427–432, 1991.
[SGC97]
C. Scherer, P. Gahinet, and M. Chilali.
Multiobjective output-feedback
control via LMI optimization.
IEEE Transactions on Automatic Control,
42(7):896–906, 1997.
[She99]
N. Sherwani. Algorithms for VLSI Design Automation. Kluwer Academic
Publishers, third edition, 1999.
[Sho85]
N. Z. Shor. Minimization Methods for Non-diﬀerentiable Functions. Springer
Series in Computational Mathematics. Springer, 1985.
[Sho91]
N. Z. Shor. The development of numerical methods for nonsmooth optimiza-
tion in the USSR. In J. K. Lenstra, A. H. G. Rinnooy Kan, and A. Schri-
jver, editors, History of Mathematical Programming. A Collection of Personal
Reminiscences, pages 135–139. Centrum voor Wiskunde en Informatica and
North-Holland, Amsterdam, 1991.
[Son86]
G. Sonnevend.
An ‘analytical centre’ for polyhedrons and new classes of
global algorithms for linear (smooth, convex) programming. In Lecture Notes
in Control and Information Sciences, volume 84, pages 866–878. Springer,
1986.


## Page 29

References
695
[SPV99]
A. Seiﬁ, K. Ponnambalam, and J. Vlach.
A uniﬁed approach to statisti-
cal design centering of integrated circuits with correlated parameters. IEEE
Transactions on Circuits and Systems — I. Fundamental Theory and Appli-
cations, 46(1):190–196, 1999.
[SRVK93]
S. S. Sapatnekar, V. B. Rao, P. M. Vaidya, and S.-M. Kang.
An exact
solution to the transistor sizing problem for CMOS circuits using convex
optimization. IEEE Transactions on Computer-Aided Design of Integrated
Circuits and Systems, 12(11):1621–1634, 1993.
[SS01]
B. Sch¨olkopf and A. Smola. Learning with Kernels: Support Vector Machines,
Regularization, Optimization, and Beyond. MIT Press, 2001.
[Str80]
G. Strang. Linear Algebra and its Applications. Academic Press, 1980.
[Stu99]
J. F. Sturm. Using SEDUMI 1.02, a MATLAB toolbox for optimization over
symmetric cones. Optimization Methods and Software, 11-12:625–653, 1999.
Available from sedumi.mcmaster.ca.
[SW70]
J. Stoer and C. Witzgall. Convexity and Optimization in Finite Dimensions I.
Springer-Verlag, 1970.
[SW95]
R. J. Stern and H. Wolkowicz. Indeﬁnite trust region subproblems and non-
symmetric eigenvalue perturbations. SIAM Journal on Optimization, 15:286–
313, 1995.
[TA77]
A. N. Tikhonov and V. Y. Arsenin.
Solutions of Ill-Posed Problems.
V. H. Winston & Sons, 1977. Translated from Russian.
[TB97]
L. N. Trefethen and D. Bau, III.
Numerical Linear Algebra.
Society for
Industrial and Applied Mathematics, 1997.
[Ter96]
T. Terlaky, editor. Interior Point Methods of Mathematical Programming,
volume 5 of Applied Optimization. Kluwer Academic Publishers, 1996.
[Tib96]
R. Tibshirani. Regression shrinkage and selection via the lasso. Journal of
the Royal Statistical Society, Series B, 58(1):267–288, 1996.
[Tik90]
V. M. Tikhomorov. Convex analysis. In R. V. Gamkrelidze, editor, Analy-
sis II: Convex Analysis and Approximation Theory, volume 14, pages 1–92.
Springer, 1990.
[Tit75]
D. M. Titterington.
Optimal design:
Some geometrical aspects of D-
optimality. Biometrika, 62(2):313–320, 1975.
[TKE88]
S. Tarasov, L. Khachiyan, and I. `Erlikh. The method of inscribed ellipsoids.
Soviet Mathematics Doklady, 37(1):226–230, 1988.
[Tod01]
M. J. Todd. Semideﬁnite optimization. Acta Numerica, 10:515–560, 2001.
[Tod02]
M. J. Todd. The many facets of linear programming. Mathematical Program-
ming Series B, 91:417–436, 2002.
[TTT98]
M. J. Todd, K. C. Toh, and R. H. T¨ut¨unc¨u. On the Nesterov-Todd direction
in semideﬁnite programming. SIAM Journal on Optimization, 8(3):769–796,
1998.
[TTT02]
K. C. Toh, R. H. T¨ut¨unc¨u, and M. J. Todd.
SDPT3. A Matlab soft-
ware for semideﬁnite-quadratic-linear programming, 2002.
Available from
www.math.nus.edu.sg/~mattohkc/sdpt3.html.
[Tuy98]
H. Tuy. Convex Analysis and Global Optimization, volume 22 of Nonconvex
Optimization and Its Applications. Kluwer, 1998.
[Uhl79]
F. Uhlig. A recurring theorem about pairs of quadratic forms and extensions.
A survey. Linear Algebra and Its Applications, 25:219–237, 1979.
[Val64]
F. A. Valentine. Convex Sets. McGraw-Hill, 1964.


## Page 30

696
References
[Van84]
G. N. Vanderplaats.
Numerical Optimization Techniques for Engineering
Design. McGraw-Hill, 1984.
[Van96]
R. J. Vanderbei. Linear Programming: Foundations and Extensions. Kluwer,
1996.
[Van97]
R.
J.
Vanderbei.
LOQO
User’s
Manual,
1997.
Available
from
www.orfe.princeton.edu/~rvdb.
[Vap00]
V. N. Vapnik. The Nature of Statistical Learning Theory. Springer, second
edition, 2000.
[Vav91]
S. A. Vavasis. Nonlinear Optimization: Complexity Issues. Oxford University
Press, 1991.
[VB95]
L. Vandenberghe and S. Boyd. Semideﬁnite programming. SIAM Review,
pages 49–95, 1995.
[vN63]
J. von Neumann. Discussion of a maximum problem. In A. H. Taub, editor,
John von Neumann. Collected Works, volume VI, pages 89–95. Pergamon
Press, 1963. Unpublished working paper from 1947.
[vN46]
J. von Neumann. A model of general economic equilibrium. Review of Eco-
nomic Studies, 13(1):1–9, 1945-46.
[vNM53]
J. von Neumann and O. Morgenstern. Theory of Games and Economic Be-
havior. Princeton University Press, third edition, 1953. First published in
1944.
[vT84]
J. van Tiel. Convex Analysis. An Introductory Text. John Wiley & Sons,
1984.
[Web71]
A. Weber. Theory of the Location of Industries. Russell & Russell, 1971.
Translated from German by C. J. Friedrich. First published in 1929.
[Web94]
R. Webster. Convexity. Oxford University Press, 1994.
[Whi71]
P. Whittle. Optimization under Constraints. John Wiley & Sons, 1971.
[Wol81]
H. Wolkowicz. Some applications of optimization in matrix theory. Linear
Algebra and Its Applications, 40:101–118, 1981.
[Wri97]
S. J. Wright. Primal-Dual Interior-Point Methods. Society for Industrial and
Applied Mathematics, 1997.
[WSV00]
H. Wolkowicz, R. Saigal, and L. Vandenberghe, editors. Handbook of Semidef-
inite Programming. Kluwer Academic Publishers, 2000.
[XHY96]
X. Xu, P. Hung, and Y. Ye.
A simpliﬁed homogeneous and self-dual lin-
ear programming algorithm and its implementation. Annals of Operations
Research, 62:151–172, 1996.
[Ye97]
Y. Ye. Interior Point Algorithms. Theory and Analysis. John Wiley & Sons,
1997.
[Ye99]
Y. Ye. Approximating quadratic programming with bound and quadratic
constraints. Mathematical Programming, 84:219–226, 1999.
[YTM94]
Y. Ye, M. J. Todd, and S. Mizuno. An O(√nL)-iteration homogeneous and
self-dual linear programming algorithm. Mathematics of Operations Research,
19:53–67, 1994.
[Zen71]
C. Zener. Engineering Design by Geometric Programming. John Wiley &
Sons, 1971.
[Zha98]
Y. Zhang.
On extending some primal-dual interior-point algorithms from
linear programming to semideﬁnite programming. SIAM Journal on Opti-
mization, 8(2):365–386, 1998.


## Page 31

Notation
Some speciﬁc sets
R
Real numbers.
Rn
Real n-vectors (n × 1 matrices).
Rm×n
Real m × n matrices.
R+, R++
Nonnegative, positive real numbers.
C
Complex numbers.
Cn
Complex n-vectors.
Cm×n
Complex m × n matrices.
Z
Integers.
Z+
Nonnegative integers.
Sn
Symmetric n × n matrices.
Sn
+, Sn
++
Symmetric positive semideﬁnite, positive deﬁnite, n × n
matrices.
Vectors and matrices
1
Vector with all components one.
ei
ith standard basis vector.
I
Identity matrix.
XT
Transpose of matrix X.
XH
Hermitian (complex conjugate) transpose of matrix X.
tr X
Trace of matrix X.
λi(X)
ith largest eigenvalue of symmetric matrix X.
λmax(X), λmin(X)
Maximum, minimum eigenvalue of symmetric matrix X.
σi(X)
ith largest singular value of matrix X.
σmax(X), σmin(X)
Maximum, minimum singular value of matrix X.
X†
Moore-Penrose or pseudo-inverse of matrix X.
x ⊥y
Vectors x and y are orthogonal: xT y = 0.
V ⊥
Orthogonal complement of subspace V .
diag(x)
Diagonal matrix with diagonal entries x1, . . . , xn.
diag(X, Y, . . .)
Block diagonal matrix with diagonal blocks X, Y, . . ..
rank A
Rank of matrix A.
R(A)
Range of matrix A.
N(A)
Nullspace of matrix A.


## Page 32

698
Notation
Norms and distances
∥· ∥
A norm.
∥· ∥∗
Dual of norm ∥· ∥.
∥x∥2
Euclidean (or ℓ2-) norm of vector x.
∥x∥1
ℓ1-norm of vector x.
∥x∥∞
ℓ∞-norm of vector x.
∥X∥2
Spectral norm (maximum singular value) of matrix X.
B(c, r)
Ball with center c and radius r.
dist(A, B)
Distance between sets (or points) A and B.
Generalized inequalities
x ⪯y
Componentwise inequality between vectors x and y.
x ≺y
Strict componentwise inequality between vectors x and y
X ⪯Y
Matrix inequality between symmetric matrices X and Y .
X ≺Y
Strict matrix inequality between symmetric matrices X
and Y .
x ⪯K y
Generalized inequality induced by proper cone K.
x ≺K y
Strict generalized inequality induced by proper cone K.
x ⪯K∗y
Dual generalized inequality.
x ≺K∗y
Dual strict generalized inequality.
Topology and convex analysis
card C
Cardinality of set C.
int C
Interior of set C.
relint C
Relative interior of set C.
cl C
Closure of set C.
bd C
Boundary of set C: bd C = cl C \ int C.
conv C
Convex hull of set C.
aﬀC
Aﬃne hull of set C.
K∗
Dual cone associated with K.
IC
Indicator function of set C.
SC
Support function of set C.
f ∗
Conjugate function of f.
Probability
E X
Expected value of random vector X.
prob S
Probability of event S.
var X
Variance of scalar random variable X.
N(c, Σ)
Gaussian distribution with mean c, covariance (matrix) Σ.
Φ
Cumulative distribution function of N(0, 1) random vari-
able.


## Page 33

Notation
699
Functions and derivatives
f : A →B
f is a function on the set dom f ⊆A into the set B.
dom f
Domain of function f.
epi f
Epigraph of function f.
∇f
Gradient of function f.
∇2f
Hessian of function f.
Df
Derivative (Jacobian) matrix of function f.


## Page 34

