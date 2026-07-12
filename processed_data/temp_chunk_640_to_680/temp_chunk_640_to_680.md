# temp_chunk_640_to_680



## Page 1

Exercises
627
11.12 Barrier method for convex-concave games.
We consider a convex-concave game with
inequality constraints,
minimizew maximizez
f0(w, z)
subject to
fi(w) ≤0,
i = 1, . . . , m
˜fi(z) ≤0,
i = 1, . . . , ˜m.
Here w ∈Rn is the variable associated with minimizing the objective, and z ∈R˜n is
the variable associated with maximizing the objective. The constraint functions fi and ˜fi
are convex and diﬀerentiable, and the objective function f0 is diﬀerentiable and convex-
concave, i.e., convex in w, for each z, and concave in z, for each w.
We assume for
simplicity that dom f0 = Rn × R˜n.
A solution or saddle-point for the game is a pair w⋆, z⋆, for which
f0(w⋆, z) ≤f0(w⋆, z⋆) ≤f0(w, z⋆)
holds for every feasible w and z. (For background on convex-concave games and functions,
see §5.4.3, §10.3.4 and exercises 3.14, 5.24, 5.25, 10.10, and 10.13.) In this exercise we
show how to solve this game using an extension of the barrier method, and the infeasible
start Newton method (see §10.3).
(a) Let t > 0. Explain why the function
tf0(w, z) −
m
X
i=1
log(−fi(w)) +
˜
m
X
i=1
log(−˜fi(z))
is convex-concave in (w, z).
We will assume that it has a unique saddle-point,
(w⋆(t), z⋆(t)), which can be found using the infeasible start Newton method.
(b) As in the barrier method for solving a convex optimization problem, we can derive
a simple bound on the suboptimality of (w⋆(t), z⋆(t)), which depends only on the
problem dimensions, and decreases to zero as t increases. Let W and Z denote the
feasible sets for w and z,
W = {w | fi(w) ≤0, i = 1, . . . , m},
Z = {z | ˜fi(z) ≤0, i = 1, . . . , ˜m}.
Show that
f0(w⋆(t), z⋆(t))
≤
inf
w∈W
f0(w, z⋆(t)) + m
t ,
f0(w⋆(t), z⋆(t))
≥
sup
z∈Z
f0(w⋆(t), z) −˜m
t ,
and therefore
sup
z∈Z
f0(w⋆(t), z) −inf
w∈W
f0(w, z⋆(t)) ≤m + ˜m
t
.
Self-concordance and complexity analysis
11.13 Self-concordance and negative entropy.
(a) Show that the negative entropy function x log x (on R++) is not self-concordant.
(b) Show that for any t > 0, tx log x −log x is self-concordant (on R++).
11.14 Self-concordance and the centering problem. Let φ be the logarithmic barrier function of
problem (11.1). Suppose that the sublevel sets of (11.1) are bounded, and that tf0 + φ is
closed and self-concordant. Show that t∇2f0(x) + ∇2φ(x) ≻0, for all x ∈dom φ. Hint.
See exercises 9.17 and 11.3.


## Page 2

628
11
Interior-point methods
Barrier method for generalized inequalities
11.15 Generalized logarithm is K-increasing. Let ψ be a generalized logarithm for the proper
cone K. Suppose y ≻K 0.
(a) Show that ∇ψ(y) ⪰K∗0, i.e., that ψ is K-nondecreasing. Hint. If ∇ψ(y)̸ ⪰K∗0,
then there is some w ≻K 0 for which wT ∇ψ(y) ≤0. Use the inequality ψ(sw) ≤
ψ(y) + ∇ψ(y)T (sw −y), with s > 0.
(b) Now show that ∇ψ(y) ≻K∗0, i.e., that ψ is K-increasing.
Hint.
Show that
∇2ψ(y) ≺0, ∇ψ(y) ⪰K∗0 imply ∇ψ(y) ≻K∗0.
11.16 [NN94, page 41] Properties of a generalized logarithm. Let ψ be a generalized logarithm
for the proper cone K, with degree θ. Prove that the following properties hold at any
y ≻K 0.
(a) ∇ψ(sy) = ∇ψ(y)/s for all s > 0.
(b) ∇ψ(y) = −∇2ψ(y)y.
(c) yT ∇ψ2(y)y = −θ.
(d) ∇ψ(y)T ∇2ψ(y)−1∇ψ(y) = −θ.
11.17 Dual generalized logarithm. Let ψ be a generalized logarithm for the proper cone K, with
degree θ. Show that the dual generalized logarithm ψ, deﬁned in (11.49), satisﬁes
ψ(sv) = ψ(v) + θ log s,
for v ≻K∗0, s > 0.
11.18 Is the function
ψ(y) = log

yn+1 −
Pn
i=1 y2
i
yn+1

,
with dom ψ = {y ∈Rn+1 | yn+1 > Pn
i=1 y2
i }, a generalized logarithm for the second-
order cone in Rn+1?
Implementation
11.19 Yet another method for computing the Newton step. Show that the Newton step for the
barrier method, which is given by the solution of the linear equations (11.14), can be
found by solving a larger set of linear equations with coeﬃcient matrix


t∇2f0(x) + P
i
1
−fi(x)∇2fi(x)
Df(x)T
AT
Df(x)
−diag(f(x))2
0
A
0
0


where f(x) = (f1(x), . . . , fm(x)).
For what types of problem structure might solving this larger system be interesting?
11.20 Network rate optimization via the dual problem. In this problem we examine a dual method
for solving the network rate optimization problem of §11.8.4. To simplify the presentation
we assume that the utility functions Ui are strictly concave, with dom Ui = R++, and
that they satisfy U ′
i(xi) →∞as xi →0 and U ′
i(xi) →0 as xi →∞.
(a) Express the dual problem of (11.62) in terms of the conjugate utility functions
Vi = (−Ui)∗, deﬁned as
Vi(λ) = sup
x>0
(λx + Ui(x)).
Show that dom Vi = −R++, and that for each λ < 0 there is a unique x with
U ′
i(x) = −λ.
(b) Describe a barrier method for the dual problem. Compare the complexity per iter-
ation with the complexity of the method in §11.8.4. Distinguish the same two cases
as in §11.8.4 (AT A is sparse and AAT is sparse).


## Page 3

Exercises
629
Numerical experiments
11.21 Log-Chebyshev approximation with bounds. We consider an approximation problem: ﬁnd
x ∈Rn, that satisﬁes the variable bounds l ⪯x ⪯u, and yields Ax ≈b, where b ∈Rm.
You can assume that l ≺u, and b ≻0 (for reasons we explain below). We let aT
i denote
the ith row of the matrix A.
We judge the approximation Ax ≈b by the maximum fractional deviation, which is
max
i=1,...,n max{(aT
i x)/bi, bi/(aT
i x)} =
max
i=1,...,n
max{aT
i x, bi}
min{aT
i x, bi} ,
when Ax ≻0; we deﬁne the maximum fractional deviation as ∞if Ax̸ ≻0.
The problem of minimizing the maximum fractional deviation is called the fractional
Chebyshev approximation problem, or the logarithmic Chebyshev approximation problem,
since it is equivalent to minimizing the objective
max
i=1,...,n | log aT
i x −log bi|.
(See also exercise 6.3, part (c).)
(a) Formulate the fractional Chebyshev approximation problem (with variable bounds)
as a convex optimization problem with twice diﬀerentiable objective and constraint
functions.
(b) Implement a barrier method that solves the fractional Chebyshev approximation
problem. You can assume an initial point x(0), satisfying l ≺x(0) ≺u, Ax(0) ≻0, is
known.
11.22 Maximum volume rectangle inside a polyhedron. Consider the problem described in exer-
cise 8.16, i.e., ﬁnding the maximum volume rectangle R = {x | l ⪯x ⪯u} that lies in
a polyhedron described by a set of linear inequalities, P = {x | Ax ⪯b}. Implement a
barrier method for solving this problem. You can assume that b ≻0, which means that
for small l ≺0 and u ≻0, the rectangle R lies inside P.
Test your implementation on several simple examples. Find the maximum volume rect-
angle that lies in the polyhedron deﬁned by
A =


0
−1
2
−4
2
1
−4
4
−4
0

,
b = 1.
Plot this polyhedron, and the maximum volume rectangle that lies inside it.
11.23 SDP bounds and heuristics for the two-way partitioning problem.
In this exercise we
consider the two-way partitioning problem (5.7), described on page 219, and also in ex-
ercise 5.39:
minimize
xT Wx
subject to
x2
i = 1,
i = 1, . . . , n,
(11.65)
with variable x ∈Rn.
We assume, without loss of generality, that W ∈Sn satisﬁes
Wii = 0. We denote the optimal value of the partitioning problem as p⋆, and x⋆will
denote an optimal partition. (Note that −x⋆is also an optimal partition.)
The Lagrange dual of the two-way partitioning problem (11.65) is given by the SDP
maximize
−1T ν
subject to
W + diag(ν) ⪰0,
(11.66)


## Page 4

630
11
Interior-point methods
with variable ν ∈Rn. The dual of this SDP is
minimize
tr(WX)
subject to
X ⪰0
Xii = 1,
i = 1, . . . , n,
(11.67)
with variable X ∈Sn.
(This SDP can be interpreted as a relaxation of the two-way
partitioning problem (11.65); see exercise 5.39.) The optimal values of these two SDPs
are equal, and give a lower bound, which we denote d⋆, on the optimal value p⋆. Let ν⋆
and X⋆denote optimal points for the two SDPs.
(a) Implement a barrier method that solves the SDP (11.66) and its dual (11.67), given
the weight matrix W. Explain how you obtain nearly optimal ν and X, give for-
mulas for any Hessians and gradients that your method requires, and explain how
you compute the Newton step. Test your implementation on some small problem
instances, comparing the bound you ﬁnd with the optimal value (which can be found
by checking the objective value of all 2n partitions). Try your implementation on a
randomly chosen problem instance large enough that you cannot ﬁnd the optimal
partition by exhaustive search (e.g., n = 100).
(b) A heuristic for partitioning. In exercise 5.39, you found that if X⋆has rank one,
then it must have the form X⋆= x⋆(x⋆)T , where x⋆is optimal for the two-way
partitioning problem. This suggests the following simple heuristic for ﬁnding a good
partition (if not the best): solve the SDPs above, to ﬁnd X⋆(and the bound d⋆).
Let v denote an eigenvector of X⋆associated with its largest eigenvalue, and let
ˆx = sign(v). The vector ˆx is our guess for a good partition.
Try this heuristic on some small problem instances, and the large problem instance
you used in part (a). Compare the objective value of your heuristic partition, ˆxT W ˆx,
with the lower bound d⋆.
(c) A randomized method.
Another heuristic technique for ﬁnding a good partition,
given the solution X⋆of the SDP (11.67), is based on randomization. The method
is simple: we generate independent samples x(1), . . . , x(K) from a normal distribution
on Rn, with zero mean and covariance X⋆. For each sample we consider the heuristic
approximate solution ˆx(k) = sign(x(k)). We then take the best among these, i.e.,
the one with lowest cost. Try out this procedure on some small problem instances,
and the large problem instance you considered in part (a).
(d) A greedy heuristic reﬁnement. Suppose you are given a partition x, i.e., xi ∈{−1, 1},
i = 1, . . . , n. How does the objective value change if we move element i from one
set to the other, i.e., change xi to −xi? Now consider the following simple greedy
algorithm: given a starting partition x, move the element that gives the largest
reduction in the objective. Repeat this procedure until no reduction in objective
can be obtained by moving an element from one set to the other.
Try this heuristic on some problem instances, including the large one, starting from
various initial partitions, including x = 1, the heuristic approximate solution found
in part (b), and the randomly generated approximate solutions found in part (c).
How much does this greedy reﬁnement improve your approximate solutions from
parts (b) and (c)?
11.24 Barrier and primal-dual interior-point methods for quadratic programming. Implement
a barrier method, and a primal-dual method, for solving the QP (without equality con-
straints, for simplicity)
minimize
(1/2)xT Px + qT x
subject to
Ax ⪯b,
with A ∈Rm×n. You can assume a strictly feasible initial point is given. Test your codes
on several examples. For the barrier method, plot the duality gap versus Newton steps.
For the primal-dual interior-point method, plot the surrogate duality gap and the norm
of the dual residual versus iteration number.


## Page 5

Appendices


## Page 6



## Page 7

Appendix A
Mathematical background
In this appendix we give a brief review of some basic concepts from analysis and
linear algebra. The treatment is by no means complete, and is meant mostly to set
out our notation.
A.1
Norms
A.1.1
Inner product, Euclidean norm, and angle
The standard inner product on Rn, the set of real n-vectors, is given by
⟨x, y⟩= xT y =
n
X
i=1
xiyi,
for x, y ∈Rn.
In this book we use the notation xT y, instead of ⟨x, y⟩.
The
Euclidean norm, or ℓ2-norm, of a vector x ∈Rn is deﬁned as
∥x∥2 = (xT x)1/2 = (x2
1 + · · · + x2
n)1/2.
(A.1)
The Cauchy-Schwartz inequality states that |xT y| ≤∥x∥2∥y∥2 for any x, y ∈Rn.
The (unsigned) angle between nonzero vectors x, y ∈Rn is deﬁned as̸
(x, y) = cos−1

xT y
∥x∥2∥y∥2

,
where we take cos−1(u) ∈[0, π]. We say x and y are orthogonal if xT y = 0.
The standard inner product on Rm×n, the set of m × n real matrices, is given
by
⟨X, Y ⟩= tr(XT Y ) =
m
X
i=1
n
X
j=1
XijYij,
for X, Y ∈Rm×n. (Here tr denotes trace of a matrix, i.e., the sum of its diagonal
elements.) We use the notation tr(XT Y ) instead of ⟨X, Y ⟩. Note that the inner


## Page 8

634
A
Mathematical background
product of two matrices is the inner product of the associated vectors, in Rmn,
obtained by listing the coeﬃcients of the matrices in some order, such as row
major.
The Frobenius norm of a matrix X ∈Rm×n is given by
∥X∥F =
 tr(XT X)
1/2 =


m
X
i=1
n
X
j=1
X2
ij


1/2
.
(A.2)
The Frobenius norm is the Euclidean norm of the vector obtained by listing the
coeﬃcients of the matrix. (The ℓ2-norm of a matrix is a diﬀerent norm; see §A.1.5.)
The standard inner product on Sn, the set of symmetric n×n matrices, is given
by
⟨X, Y ⟩= tr(XY ) =
n
X
i=1
n
X
j=1
XijYij =
n
X
i=1
XiiYii + 2
X
i<j
XijYij.
A.1.2
Norms, distance, and unit ball
A function f : Rn →R with dom f = Rn is called a norm if
• f is nonnegative: f(x) ≥0 for all x ∈Rn
• f is deﬁnite: f(x) = 0 only if x = 0
• f is homogeneous: f(tx) = |t|f(x), for all x ∈Rn and t ∈R
• f satisﬁes the triangle inequality: f(x + y) ≤f(x) + f(y), for all x, y ∈Rn
We use the notation f(x) = ∥x∥, which is meant to suggest that a norm is a
generalization of the absolute value on R. When we specify a particular norm,
we use the notation ∥x∥symb, where the subscript is a mnemonic to indicate which
norm is meant.
A norm is a measure of the length of a vector x; we can measure the distance
between two vectors x and y as the length of their diﬀerence, i.e.,
dist(x, y) = ∥x −y∥.
We refer to dist(x, y) as the distance between x and y, in the norm ∥· ∥.
The set of all vectors with norm less than or equal to one,
B = {x ∈Rn | ∥x∥≤1},
is called the unit ball of the norm ∥· ∥. The unit ball satisﬁes the following prop-
erties:
• B is symmetric about the origin, i.e., x ∈B if and only if −x ∈B
• B is convex
• B is closed, bounded, and has nonempty interior
Conversely, if C ⊆Rn is any set satisfying these three conditions, then it is the
unit ball of a norm, which is given by
∥x∥= (sup{t ≥0 | tx ∈C})−1 .


## Page 9

A.1
Norms
635
A.1.3
Examples
The simplest example of a norm is the absolute value on R.
Another simple
example is the Euclidean or ℓ2-norm on Rn, deﬁned above in (A.1). Two other
frequently used norms on Rn are the sum-absolute-value, or ℓ1-norm, given by
∥x∥1 = |x1| + · · · + |xn|,
and the Chebyshev or ℓ∞-norm, given by
∥x∥∞= max{|x1|, . . . , |xn|}.
These three norms are part of a family parametrized by a constant traditionally
denoted p, with p ≥1: the ℓp-norm is deﬁned by
∥x∥p = (|x1|p + · · · + |xn|p)1/p.
This yields the ℓ1-norm when p = 1 and the Euclidean norm when p = 2. It is easy
to show that for any x ∈Rn,
lim
p→∞∥x∥p = max{|x1|, . . . , |xn|},
so the ℓ∞-norm also ﬁts in this family, as a limit.
Another important family of norms are the quadratic norms. For P ∈Sn
++, we
deﬁne the P-quadratic norm as
∥x∥P = (xT Px)1/2 = ∥P 1/2x∥2.
The unit ball of a quadratic norm is an ellipsoid (and conversely, if the unit ball of
a norm is an ellipsoid, the norm is a quadratic norm).
Some common norms on Rm×n are the Frobenius norm, deﬁned above in (A.2),
the sum-absolute-value norm,
∥X∥sav =
m
X
i=1
n
X
j=1
|Xij|,
and the maximum-absolute-value norm,
∥X∥mav = max{|Xij| | i = 1, . . . , m, j = 1, . . . , n}.
We will encounter several other important norms of matrices in §A.1.5.
A.1.4
Equivalence of norms
Suppose that ∥· ∥a and ∥· ∥b are norms on Rn. A basic result of analysis is that
there exist positive constants α and β such that, for all x ∈Rn,
α∥x∥a ≤∥x∥b ≤β∥x∥a.


## Page 10

636
A
Mathematical background
This means that the norms are equivalent, i.e., they deﬁne the same set of open
subsets, the same set of convergent sequences, and so on (see §A.2). (We con-
clude that any norms on any ﬁnite-dimensional vector space are equivalent, but on
inﬁnite-dimensional vector spaces, the result need not hold.) Using convex analy-
sis, we can give a more speciﬁc result: If ∥· ∥is any norm on Rn, then there exists
a quadratic norm ∥· ∥P for which
∥x∥P ≤∥x∥≤√n∥x∥P
holds for all x. In other words, any norm on Rn can be uniformly approximated,
within a factor of √n, by a quadratic norm. (See §8.4.1.)
A.1.5
Operator norms
Suppose ∥· ∥a and ∥· ∥b are norms on Rm and Rn, respectively. We deﬁne the
operator norm of X ∈Rm×n, induced by the norms ∥· ∥a and ∥· ∥b, as
∥X∥a,b = sup {∥Xu∥a | ∥u∥b ≤1} .
(It can be shown that this deﬁnes a norm on Rm×n.)
When ∥· ∥a and ∥· ∥b are both Euclidean norms, the operator norm of X is its
maximum singular value, and is denoted ∥X∥2:
∥X∥2 = σmax(X) = (λmax(XT X))1/2.
(This agrees with the Euclidean norm on Rm, when X ∈Rm×1, so there is no
clash of notation.) This norm is also called the spectral norm or ℓ2-norm of X.
As another example, the norm induced by the ℓ∞-norm on Rm and Rn, denoted
∥X∥∞, is the max-row-sum norm,
∥X∥∞= sup {∥Xu∥∞| ∥u∥∞≤1} =
max
i=1,...,m
n
X
j=1
|Xij|.
The norm induced by the ℓ1-norm on Rm and Rn, denoted ∥X∥1, is the max-
column-sum norm,
∥X∥1 =
max
j=1,...,n
m
X
i=1
|Xij|.
A.1.6
Dual norm
Let ∥· ∥be a norm on Rn. The associated dual norm, denoted ∥· ∥∗, is deﬁned as
∥z∥∗= sup{zT x | ∥x∥≤1}.
(This can be shown to be a norm.)
The dual norm can be interpreted as the
operator norm of zT , interpreted as a 1 × n matrix, with the norm ∥· ∥on Rn, and
the absolute value on R:
∥z∥∗= sup{|zT x| | ∥x∥≤1}.


## Page 11

A.2
Analysis
637
From the deﬁnition of dual norm we have the inequality
zT x ≤∥x∥∥z∥∗,
which holds for all x and z. This inequality is tight, in the following sense: for any
x there is a z for which the inequality holds with equality. (Similarly, for any z
there is an x that gives equality.) The dual of the dual norm is the original norm:
we have ∥x∥∗∗= ∥x∥for all x. (This need not hold in inﬁnite-dimensional vector
spaces.)
The dual of the Euclidean norm is the Euclidean norm, since
sup{zT x | ∥x∥2 ≤1} = ∥z∥2.
(This follows from the Cauchy-Schwarz inequality; for nonzero z, the value of x
that maximizes zT x over ∥x∥2 ≤1 is z/∥z∥2.)
The dual of the ℓ∞-norm is the ℓ1-norm:
sup{zT x | ∥x∥∞≤1} =
n
X
i=1
|zi| = ∥z∥1,
and the dual of the ℓ1-norm is the ℓ∞-norm. More generally, the dual of the ℓp-norm
is the ℓq-norm, where q satisﬁes 1/p + 1/q = 1, i.e., q = p/(p −1).
As another example, consider the ℓ2- or spectral norm on Rm×n. The associated
dual norm is
∥Z∥2∗= sup{tr(ZT X) | ∥X∥2 ≤1},
which turns out to be the sum of the singular values,
∥Z∥2∗= σ1(Z) + · · · + σr(Z) = tr(ZT Z)1/2,
where r = rank Z. This norm is sometimes called the nuclear norm.
A.2
Analysis
A.2.1
Open and closed sets
An element x ∈C ⊆Rn is called an interior point of C if there exists an ǫ > 0 for
which
{y | ∥y −x∥2 ≤ǫ} ⊆C,
i.e., there exists a ball centered at x that lies entirely in C. The set of all points
interior to C is called the interior of C and is denoted int C. (Since all norms
on Rn are equivalent to the Euclidean norm, all norms generate the same set of
interior points.) A set C is open if int C = C, i.e., every point in C is an interior
point. A set C ⊆Rn is closed if its complement Rn \ C = {x ∈Rn | x̸ ∈C} is
open.


## Page 12

638
A
Mathematical background
The closure of a set C is deﬁned as
cl C = Rn \ int(Rn \ C),
i.e., the complement of the interior of the complement of C. A point x is in the
closure of C if for every ǫ > 0, there is a y ∈C with ∥x −y∥2 ≤ǫ.
We can also describe closed sets and the closure in terms of convergent sequences
and limit points. A set C is closed if and only if it contains the limit point of every
convergent sequence in it. In other words, if x1, x2, . . . converges to x, and xi ∈C,
then x ∈C. The closure of C is the set of all limit points of convergent sequences
in C.
The boundary of the set C is deﬁned as
bd C = cl C \ int C.
A boundary point x (i.e., a point x ∈bd C) satisﬁes the following property: For
all ǫ > 0, there exists y ∈C and z̸ ∈C with
∥y −x∥2 ≤ǫ,
∥z −x∥2 ≤ǫ,
i.e., there exist arbitrarily close points in C, and also arbitrarily close points not in
C. We can characterize closed and open sets in terms of the boundary operation:
C is closed if it contains its boundary, i.e., bd C ⊆C. It is open if it contains no
boundary points, i.e., C ∩bd C = ∅.
A.2.2
Supremum and inﬁmum
Suppose C ⊆R. A number a is an upper bound on C if for each x ∈C, x ≤a.
The set of upper bounds on a set C is either empty (in which case we say C is
unbounded above), all of R (only when C = ∅), or a closed inﬁnite interval [b, ∞).
The number b is called the least upper bound or supremum of the set C, and is
denoted sup C. We take sup ∅= −∞, and sup C = ∞if C is unbounded above.
When sup C ∈C, we say the supremum of C is attained or achieved.
When the set C is ﬁnite, sup C is the maximum of its elements. Some authors
use the notation max C to denote supremum, when it is attained, but we follow
standard mathematical convention, using max C only when the set C is ﬁnite.
We deﬁne lower bound, and inﬁmum, in a similar way. A number a is a lower
bound on C ⊆R if for each x ∈C, a ≤x. The inﬁmum (or greatest lower bound)
of a set C ⊆R is deﬁned as inf C = −sup(−C). When C is ﬁnite, the inﬁmum
is the minimum of its elements.
We take inf ∅= ∞, and inf C = −∞if C is
unbounded below, i.e., has no lower bound.


## Page 13

A.3
Functions
639
A.3
Functions
A.3.1
Function notation
Our notation for functions is mostly standard, with one exception. When we write
f : A →B
we mean that f is a function on the set dom f ⊆A into the set B; in particular
we can have dom f a proper subset of the set A. Thus the notation f : Rn →Rm
means that f maps (some) n-vectors into m-vectors; it does not mean that f(x)
is deﬁned for every x ∈Rn. This convention is similar to function declarations in
computer languages. Specifying the data types of the input and output arguments
of a function gives the syntax of that function; it does not guarantee that any input
argument with the speciﬁed data type is valid.
As an example consider the function f : Sn →R, given by
f(X) = log det X,
(A.3)
with dom f = Sn
++. The notation f : Sn →R speciﬁes the syntax of f: it takes
as argument a symmetric n × n matrix, and returns a real number. The notation
dom f = Sn
++ speciﬁes which symmetric n × n matrices are valid input arguments
for f (i.e., only positive deﬁnite ones). The formula (A.3) speciﬁes what f(X) is,
for X ∈dom f.
A.3.2
Continuity
A function f : Rn →Rm is continuous at x ∈dom f if for all ǫ > 0 there exists a
δ such that
y ∈dom f,
∥y −x∥2 ≤δ =⇒∥f(y) −f(x)∥2 ≤ǫ.
Continuity can be described in terms of limits: whenever the sequence x1, x2, . . .
in dom f converges to a point x ∈dom f, the sequence f(x1), f(x2), . . . converges
to f(x), i.e.,
lim
i→∞f(xi) = f( lim
i→∞xi).
A function f is continuous if it is continuous at every point in its domain.
A.3.3
Closed functions
A function f : Rn →R is said to be closed if, for each α ∈R, the sublevel set
{x ∈dom f | f(x) ≤α}
is closed. This is equivalent to the condition that the epigraph of f,
epi f = {(x, t) ∈Rn+1 | x ∈dom f, f(x) ≤t},


## Page 14

640
A
Mathematical background
is closed. (This deﬁnition is general, but is usually only applied to convex func-
tions.)
If f : Rn →R is continuous, and dom f is closed, then f is closed. If f : Rn →
R is continuous, with dom f open, then f is closed if and only if f converges to ∞
along every sequence converging to a boundary point of dom f. In other words, if
limi→∞xi = x ∈bd dom f, with xi ∈dom f, we have limi→∞f(xi) = ∞.
Example A.1 Examples on R.
• The function f : R →R, with f(x) = x log x, dom f = R++, is not closed.
• The function f : R →R, with
f(x) =

x log x
x > 0
0
x = 0,
dom f = R+,
is closed.
• The function f(x) = −log x, dom f = R++, is closed.
A.4
Derivatives
A.4.1
Derivative and gradient
Suppose f : Rn →Rm and x ∈int dom f. The function f is diﬀerentiable at x if
there exists a matrix Df(x) ∈Rm×n that satisﬁes
lim
z∈dom f, z̸=x, z→x
∥f(z) −f(x) −Df(x)(z −x)∥2
∥z −x∥2
= 0,
(A.4)
in which case we refer to Df(x) as the derivative (or Jacobian) of f at x. (There
can be at most one matrix that satisﬁes (A.4).) The function f is diﬀerentiable if
dom f is open, and it is diﬀerentiable at every point in its domain.
The aﬃne function of z given by
f(x) + Df(x)(z −x)
is called the ﬁrst-order approximation of f at (or near) x. Evidently this function
agrees with f at z = x; when z is close to x, this aﬃne function is very close to f.
The derivative can be found by deriving the ﬁrst-order approximation of the
function f at x (i.e., the matrix Df(x) that satisﬁes (A.4)), or from partial deriva-
tives:
Df(x)ij = ∂fi(x)
∂xj
,
i = 1, . . . , m,
j = 1, . . . , n.


## Page 15

A.4
Derivatives
641
Gradient
When f is real-valued (i.e., f : Rn →R) the derivative Df(x) is a 1 × n matrix,
i.e., it is a row vector. Its transpose is called the gradient of the function:
∇f(x) = Df(x)T ,
which is a (column) vector, i.e., in Rn. Its components are the partial derivatives
of f:
∇f(x)i = ∂f(x)
∂xi
,
i = 1, . . . , n.
The ﬁrst-order approximation of f at a point x ∈int dom f can be expressed as
(the aﬃne function of z)
f(x) + ∇f(x)T (z −x).
Examples
As a simple example consider the quadratic function f : Rn →R,
f(x) = (1/2)xT Px + qT x + r,
where P ∈Sn, q ∈Rn, and r ∈R. Its derivative at x is the row vector Df(x) =
xT P + qT , and its gradient is
∇f(x) = Px + q.
As a more interesting example, we consider the function f : Sn →R, given by
f(X) = log det X,
dom f = Sn
++.
One (tedious) way to ﬁnd the gradient of f is to introduce a basis for Sn, ﬁnd
the gradient of the associated function, and ﬁnally translate the result back to Sn.
Instead, we will directly ﬁnd the ﬁrst-order approximation of f at X ∈Sn
++. Let
Z ∈Sn
++ be close to X, and let ∆X = Z −X (which is assumed to be small). We
have
log det Z
=
log det(X + ∆X)
=
log det

X1/2(I + X−1/2∆XX−1/2)X1/2
=
log det X + log det(I + X−1/2∆XX−1/2)
=
log det X +
n
X
i=1
log(1 + λi),
where λi is the ith eigenvalue of X−1/2∆XX−1/2. Now we use the fact that ∆X is
small, which implies λi are small, so to ﬁrst order we have log(1 + λi) ≈λi. Using
this ﬁrst-order approximation in the expression above, we get
log det Z
≈
log det X +
n
X
i=1
λi
=
log det X + tr(X−1/2∆XX−1/2)
=
log det X + tr(X−1∆X)
=
log det X + tr
 X−1(Z −X)

,


## Page 16

642
A
Mathematical background
where we have used the fact that the sum of the eigenvalues is the trace, and the
property tr(AB) = tr(BA).
Thus, the ﬁrst-order approximation of f at X is the aﬃne function of Z given
by
f(Z) ≈f(X) + tr
 X−1(Z −X)

.
Noting that the second term on the righthand side is the standard inner product
of X−1 and Z −X, we can identify X−1 as the gradient of f at X. Thus, we can
write the simple formula
∇f(X) = X−1.
This result should not be surprising, since the derivative of log x, on R++, is 1/x.
A.4.2
Chain rule
Suppose f : Rn →Rm is diﬀerentiable at x ∈int dom f and g : Rm →Rp
is diﬀerentiable at f(x) ∈int dom g. Deﬁne the composition h : Rn →Rp by
h(z) = g(f(z)). Then h is diﬀerentiable at x, with derivative
Dh(x) = Dg(f(x))Df(x).
(A.5)
As an example, suppose f : Rn →R, g : R →R, and h(x) = g(f(x)). Taking
the transpose of Dh(x) = Dg(f(x))Df(x) yields
∇h(x) = g′(f(x))∇f(x).
(A.6)
Composition with aﬃne function
Suppose f : Rn →Rm is diﬀerentiable, A ∈Rn×p, and b ∈Rn. Deﬁne g : Rp →
Rm as g(x) = f(Ax + b), with dom g = {x | Ax + b ∈dom f}. The derivative of
g is, by the chain rule (A.5), Dg(x) = Df(Ax + b)A.
When f is real-valued (i.e., m = 1), we obtain the formula for the gradient of
a composition of a function with an aﬃne function,
∇g(x) = AT ∇f(Ax + b).
For example, suppose that f : Rn →R, x, v ∈Rn, and we deﬁne the function
˜f : R →R by ˜f(t) = f(x + tv). (Roughly speaking, ˜f is f, restricted to the line
{x + tv | t ∈R}.) Then we have
D ˜f(t) = ˜f ′(t) = ∇f(x + tv)T v.
(The scalar ˜f ′(0) is the directional derivative of f, at x, in the direction v.)
Example A.2 Consider the function f : Rn →R, with dom f = Rn and
f(x) = log
m
X
i=1
exp(aT
i x + bi),


## Page 17

A.4
Derivatives
643
where a1, . . . , am ∈Rn, and b1, . . . , bm ∈R. We can ﬁnd a simple expression for
its gradient by noting that it is the composition of the aﬃne function Ax + b, where
A ∈Rm×n with rows aT
1 , . . . , aT
m, and the function g : Rm →R given by g(y) =
log(Pm
i=1 exp yi). Simple diﬀerentiation (or the formula (A.6)) shows that
∇g(y) =
1
Pm
i=1 exp yi


exp y1
...
exp ym

,
(A.7)
so by the composition formula we have
∇f(x) =
1
1T z AT z
where zi = exp(aT
i x + bi), i = 1, . . . , m.
Example A.3 We derive an expression for ∇f(x), where
f(x) = log det(F0 + x1F1 + · · · + xnFn),
where F0, . . . , Fn ∈Sp, and
dom f = {x ∈Rn | F0 + x1F1 + · · · + xnFn ≻0}.
The function f is the composition of the aﬃne mapping from x ∈Rn to F0 + x1F1 +
· · · + xnFn ∈Sp, with the function log det X. We use the chain rule to evaluate
∂f(x)
∂xi
= tr(Fi∇log det(F)) = tr(F −1Fi),
where F = F0 + x1F1 + · · · + xnFn. Thus we have
∇f(x) =


tr(F −1F1)
...
tr(F −1Fn)

.
A.4.3
Second derivative
In this section we review the second derivative of a real-valued function f : Rn →
R.
The second derivative or Hessian matrix of f at x ∈int dom f, denoted
∇2f(x), is given by
∇2f(x)ij = ∂2f(x)
∂xi∂xj
,
i = 1, . . . n,
j = 1, . . . , n,
provided f is twice diﬀerentiable at x, where the partial derivatives are evaluated
at x. The second-order approximation of f, at or near x, is the quadratic function
of z deﬁned by
bf(z) = f(x) + ∇f(x)T (z −x) + (1/2)(z −x)T ∇2f(x)(z −x).


## Page 18

644
A
Mathematical background
This second-order approximation satisﬁes
lim
z∈dom f, z̸=x, z→x
|f(z) −bf(z)|
∥z −x∥2
2
= 0.
Not surprisingly, the second derivative can be interpreted as the derivative of
the ﬁrst derivative.
If f is diﬀerentiable, the gradient mapping is the function
∇f : Rn →Rn, with dom ∇f = dom f, with value ∇f(x) at x. The derivative
of this mapping is
D∇f(x) = ∇2f(x).
Examples
As a simple example consider the quadratic function f : Rn →R,
f(x) = (1/2)xT Px + qT x + r,
where P ∈Sn, q ∈Rn, and r ∈R. Its gradient is ∇f(x) = Px + q, so its Hessian
is given by ∇2f(x) = P. The second-order approximation of a quadratic function
is itself.
As a more complicated example, we consider again the function f : Sn →R,
given by f(X) = log det X, with dom f = Sn
++. To ﬁnd the second-order approxi-
mation (and therefore, the Hessian), we will derive a ﬁrst-order approximation of
the gradient, ∇f(X) = X−1. For Z ∈Sn
++ near X ∈Sn
++, and ∆X = Z −X, we
have
Z−1
=
(X + ∆X)−1
=

X1/2(I + X−1/2∆XX−1/2)X1/2−1
=
X−1/2(I + X−1/2∆XX−1/2)−1X−1/2
≈
X−1/2(I −X−1/2∆XX−1/2)X−1/2
=
X−1 −X−1∆XX−1,
using the ﬁrst-order approximation (I + A)−1 ≈I −A, valid for A small.
This approximation is enough for us to identify the Hessian of f at X. The
Hessian is a quadratic form on Sn. Such a quadratic form is cumbersome to de-
scribe in the general case, since it requires four indices. But from the ﬁrst-order
approximation of the gradient above, the quadratic form can be expressed as
−tr(X−1UX−1V ),
where U, V ∈Sn are the arguments of the quadratic form. (This generalizes the
expression for the scalar case: (log x)′′ = −1/x2.)
Now we have the second-order approximation of f near X:
f(Z)
=
f(X + ∆X)
≈
f(X) + tr(X−1∆X) −(1/2) tr(X−1∆XX−1∆X)
≈
f(X) + tr
 X−1(Z −X)

−(1/2) tr
 X−1(Z −X)X−1(Z −X)

.


## Page 19

A.5
Linear algebra
645
A.4.4
Chain rule for second derivative
A general chain rule for the second derivative is cumbersome in most cases, so we
will state it only for some special cases that we will need.
Composition with scalar function
Suppose f : Rn →R, g : R →R, and h(x) = g(f(x)). Simply working out the
partial derivatives yields
∇2h(x) = g′(f(x))∇2f(x) + g′′(f(x))∇f(x)∇f(x)T .
(A.8)
Composition with aﬃne function
Suppose f : Rn →R, A ∈Rn×m, and b ∈Rn. Deﬁne g : Rm →R by g(x) =
f(Ax + b). Then we have
∇2g(x) = AT ∇2f(Ax + b)A.
As an example, consider the restriction of a real-valued function f to a line, i.e.,
the function ˜f(t) = f(x + tv), where x and v are ﬁxed. Then we have
∇2 ˜f(t) = ˜f ′′(t) = vT ∇2f(x + tv)v.
Example A.4 We consider the function f : Rn →R from example A.2,
f(x) = log
m
X
i=1
exp(aT
i x + bi),
where a1, . . . , am ∈Rn, and b1, . . . , bm ∈R. By noting that f(x) = g(Ax + b), where
g(y) = log(Pm
i=1 exp yi), we can obtain a simple formula for the Hessian of f. Taking
partial derivatives, or using the formula (A.8), noting that g is the composition of
log with Pm
i=1 exp yi, yields
∇2g(y) = diag(∇g(y)) −∇g(y)∇g(y)T ,
where ∇g(y) is given in (A.7). By the composition formula we have
∇2f(x) = AT

1
1T z diag(z) −
1
(1T z)2 zzT

A,
where zi = exp(aT
i x + bi), i = 1, . . . , m.
A.5
Linear algebra
A.5.1
Range and nullspace
Let A ∈Rm×n (i.e., A is a real matrix with m rows and n columns). The range
of A, denoted R(A), is the set of all vectors in Rm that can be written as linear


## Page 20

646
A
Mathematical background
combinations of the columns of A, i.e.,
R(A) = {Ax | x ∈Rn}.
The range R(A) is a subspace of Rm, i.e., it is itself a vector space. Its dimension
is the rank of A, denoted rank A. The rank of A can never be greater than the
minimum of m and n. We say A has full rank if rank A = min{m, n}.
The nullspace (or kernel) of A, denoted N(A), is the set of all vectors x mapped
into zero by A:
N(A) = {x | Ax = 0}.
The nullspace is a subspace of Rn.
Orthogonal decomposition induced by A
If V is a subspace of Rn, its orthogonal complement, denoted V⊥, is deﬁned as
V⊥= {x | zT x = 0 for all z ∈V}.
(As one would expect of a complement, we have V⊥⊥= V.)
A basic result of linear algebra is that, for any A ∈Rm×n, we have
N(A) = R(AT )⊥.
(Applying the result to AT we also have R(A) = N(AT )⊥.) This result is often
stated as
N(A)
⊥⊕R(AT ) = Rn.
(A.9)
Here the symbol
⊥⊕refers to orthogonal direct sum, i.e., the sum of two subspaces
that are orthogonal. The decomposition (A.9) of Rn is called the orthogonal de-
composition induced by A.
A.5.2
Symmetric eigenvalue decomposition
Suppose A ∈Sn, i.e., A is a real symmetric n × n matrix. Then A can be factored
as
A = QΛQT ,
(A.10)
where Q ∈Rn×n is orthogonal, i.e., satisﬁes QT Q = I, and Λ = diag(λ1, . . . , λn).
The (real) numbers λi are the eigenvalues of A, and are the roots of the charac-
teristic polynomial det(sI −A). The columns of Q form an orthonormal set of
eigenvectors of A. The factorization (A.10) is called the spectral decomposition or
(symmetric) eigenvalue decomposition of A.
We order the eigenvalues as λ1 ≥λ2 ≥· · · ≥λn. We use the notation λi(A)
to refer to the ith largest eigenvalue of A ∈S. We usually write the largest or
maximum eigenvalue as λ1(A) = λmax(A), and the least or minimum eigenvalue as
λn(A) = λmin(A).


## Page 21

A.5
Linear algebra
647
The determinant and trace can be expressed in terms of the eigenvalues,
det A =
n
Y
i=1
λi,
tr A =
n
X
i=1
λi,
as can the spectral and Frobenius norms,
∥A∥2 =
max
i=1,...,n |λi| = max{λ1, −λn},
∥A∥F =
 n
X
i=1
λ2
i
!1/2
.
Deﬁniteness and matrix inequalities
The largest and smallest eigenvalues satisfy
λmax(A) = sup
x̸=0
xT Ax
xT x ,
λmin(A) = inf
x̸=0
xT Ax
xT x .
In particular, for any x, we have
λmin(A)xT x ≤xT Ax ≤λmax(A)xT x,
with both inequalities tight for (diﬀerent) choices of x.
A matrix A ∈Sn is called positive deﬁnite if for all x̸ = 0, xT Ax > 0. We
denote this as A ≻0. By the inequality above, we see that A ≻0 if and only all
its eigenvalues are positive, i.e., λmin(A) > 0. If −A is positive deﬁnite, we say A
is negative deﬁnite, which we write as A ≺0. We use Sn
++ to denote the set of
positive deﬁnite matrices in Sn.
If A satisﬁes xT Ax ≥0 for all x, we say that A is positive semideﬁnite or
nonnegative deﬁnite. If −A is nonnegative deﬁnite, i.e., if xT Ax ≤0 for all x, we
say that A is negative semideﬁnite or nonpositive deﬁnite. We use Sn
+ to denote
the set of nonnegative deﬁnite matrices in Sn.
For A, B ∈Sn, we use A ≺B to mean B −A ≻0, and so on. These inequal-
ities are called matrix inequalities, or generalized inequalities associated with the
positive semideﬁnite cone.
Symmetric squareroot
Let A ∈Sn
+, with eigenvalue decomposition A = Q diag(λ1, . . . , λn)QT . We deﬁne
the (symmetric) squareroot of A as
A1/2 = Q diag(λ1/2
1
, . . . , λ1/2
n )QT .
The squareroot A1/2 is the unique symmetric positive semideﬁnite solution of the
equation X2 = A.
A.5.3
Generalized eigenvalue decomposition
The generalized eigenvalues of a pair of symmetric matrices (A, B) ∈Sn × Sn are
deﬁned as the roots of the polynomial det(sB −A).


## Page 22

648
A
Mathematical background
We are usually interested in matrix pairs with B ∈Sn
++.
In this case the
generalized eigenvalues are also the eigenvalues of B−1/2AB−1/2 (which are real).
As with the standard eigenvalue decomposition, we order the generalized eigen-
values in nonincreasing order, as λ1 ≥λ2 ≥· · · ≥λn, and denote the maximum
generalized eigenvalue by λmax(A, B).
When B ∈Sn
++, the pair of matrices can be factored as
A = V ΛV T ,
B = V V T ,
(A.11)
where V ∈Rn×n is nonsingular, and Λ = diag(λ1, . . . , λn), where λi are the
generalized eigenvalues of the pair (A, B). The decomposition (A.11) is called the
generalized eigenvalue decomposition.
The generalized eigenvalue decomposition is related to the standard eigenvalue
decomposition of the matrix B−1/2AB−1/2. If QΛQT is the eigenvalue decompo-
sition of B−1/2AB−1/2, then (A.11) holds with V = B1/2Q.
A.5.4
Singular value decomposition
Suppose A ∈Rm×n with rank A = r. Then A can be factored as
A = UΣV T ,
(A.12)
where U ∈Rm×r satisﬁes U T U = I, V ∈Rn×r satisﬁes V T V = I, and Σ =
diag(σ1, . . . , σr), with
σ1 ≥σ2 ≥· · · ≥σr > 0.
The factorization (A.12) is called the singular value decomposition (SVD) of A.
The columns of U are called left singular vectors of A, the columns of V are right
singular vectors, and the numbers σi are the singular values. The singular value
decomposition can be written
A =
r
X
i=1
σiuivT
i ,
where ui ∈Rm are the left singular vectors, and vi ∈Rn are the right singular
vectors.
The singular value decomposition of a matrix A is closely related to the eigen-
value decomposition of the (symmetric, nonnegative deﬁnite) matrix AT A. Us-
ing (A.12) we can write
AT A = V Σ2V T =

V
˜V
 
Σ2
0
0
0
 
V
˜V
T ,
where ˜V is any matrix for which [V ˜V ] is orthogonal. The righthand expression is
the eigenvalue decomposition of AT A, so we conclude that its nonzero eigenvalues
are the singular values of A squared, and the associated eigenvectors of AT A are
the right singular vectors of A. A similar analysis of AAT shows that its nonzero


## Page 23

A.5
Linear algebra
649
eigenvalues are also the squares of the singular values of A, and the associated
eigenvectors are the left singular vectors of A.
The ﬁrst or largest singular value is also written as σmax(A). It can be expressed
as
σmax(A) = sup
x,y̸=0
xT Ay
∥x∥2∥y∥2
= sup
y̸=0
∥Ay∥2
∥y∥2
.
The righthand expression shows that the maximum singular value is the ℓ2 operator
norm of A. The minimum singular value of A ∈Rm×n is given by
σmin(A) =
 σr(A)
r = min{m, n}
0
r < min{m, n},
which is positive if and only if A is full rank.
The singular values of a symmetric matrix are the absolute values of its nonzero
eigenvalues, sorted into descending order.
The singular values of a symmetric
positive semideﬁnite matrix are the same as its nonzero eigenvalues.
The condition number of a nonsingular A ∈Rn×n, denoted cond(A) or κ(A),
is deﬁned as
cond(A) = ∥A∥2∥A−1∥2 = σmax(A)/σmin(A).
Pseudo-inverse
Let A = UΣV T be the singular value decomposition of A ∈Rm×n, with rank A =
r. We deﬁne the pseudo-inverse or Moore-Penrose inverse of A as
A† = V Σ−1U T ∈Rn×m.
Alternative expressions are
A† = lim
ǫ→0(AT A + ǫI)−1AT = lim
ǫ→0 AT (AAT + ǫI)−1,
where the limits are taken with ǫ > 0, which ensures that the inverses in the
expressions exist. If rank A = n, then A† = (AT A)−1AT . If rank A = m, then
A† = AT (AAT )−1. If A is square and nonsingular, then A† = A−1.
The pseudo-inverse comes up in problems involving least-squares, minimum
norm, quadratic minimization, and (Euclidean) projection. For example, A†b is a
solution of the least-squares problem
minimize
∥Ax −b∥2
2
in general. When the solution is not unique, A†b gives the solution with minimum
(Euclidean) norm. As another example, the matrix AA† = UU T gives (Euclidean)
projection on R(A).
The matrix A†A = V V T gives (Euclidean) projection on
R(AT ).
The optimal value p⋆of the (general, nonconvex) quadratic optimization prob-
lem
minimize
(1/2)xT Px + qT x + r,
where P ∈Sn, can be expressed as
p⋆=

−(1/2)qT P †q + r
P ⪰0,
q ∈R(P)
−∞
otherwise.
(This generalizes the expression p⋆= −(1/2)qT P −1q + r, valid for P ≻0.)


## Page 24

650
A
Mathematical background
A.5.5
Schur complement
Consider a matrix X ∈Sn partitioned as
X =

A
B
BT
C

,
where A ∈Sk. If det A̸ = 0, the matrix
S = C −BT A−1B
is called the Schur complement of A in X. Schur complements arise in several
contexts, and appear in many important formulas and theorems. For example, we
have
det X = det A det S.
Inverse of block matrix
The Schur complement comes up in solving linear equations, by eliminating one
block of variables. We start with

A
B
BT
C
 
x
y

=

u
v

,
and assume that det A̸ = 0. If we eliminate x from the top block equation and
substitute it into the bottom block equation, we obtain v = BT A−1u + Sy, so
y = S−1(v −BT A−1u).
Substituting this into the ﬁrst equation yields
x =
 A−1 + A−1BS−1BT A−1
u −A−1BS−1v.
We can express these two equations as a formula for the inverse of a block matrix:

A
B
BT
C
−1
=

A−1 + A−1BS−1BT A−1
−A−1BS−1
−S−1BT A−1
S−1

.
In particular, we see that the Schur complement is the inverse of the 2, 2 block
entry of the inverse of X.
Minimization and deﬁniteness
The Schur complement arises when you minimize a quadratic form over some of
the variables. Suppose A ≻0, and consider the minimization problem
minimize
uT Au + 2vT BT u + vT Cv
(A.13)
with variable u. The solution is u = −A−1Bv, and the optimal value is
inf
u

u
v
T 
A
B
BT
C
 
u
v

= vT Sv.
(A.14)
From this we can derive the following characterizations of positive deﬁniteness or
semideﬁniteness of the block matrix X:
• X ≻0 if and only if A ≻0 and S ≻0.
• If A ≻0, then X ⪰0 if and only if S ⪰0.


## Page 25

A.5
Linear algebra
651
Schur complement with singular A
Some Schur complement results have generalizations to the case when A is singular,
although the details are more complicated. As an example, if A ⪰0 and Bv ∈
R(A), then the quadratic minimization problem (A.13) (with variable u) is solvable,
and has optimal value
vT (C −BT A†B)v,
where A† is the pseudo-inverse of A. The problem is unbounded if Bv̸ ∈R(A) or
if A̸ ⪰0.
The range condition Bv ∈R(A) can also be expressed as (I −AA†)Bv = 0,
so we have the following characterization of positive semideﬁniteness of the block
matrix X:
X ⪰0
⇐⇒
A ⪰0,
(I −AA†)B = 0,
C −BT A†B ⪰0.
Here the matrix C −BT A†B serves as a generalization of the Schur complement,
when A is singular.


## Page 26

652
A
Mathematical background
Bibliography
Some basic references for the material in this appendix are Rudin [Rud76] for analysis, and
Strang [Str80] and Meyer [Mey00] for linear algebra. More advanced linear algebra texts
include Horn and Johnson [HJ85, HJ91], Parlett [Par98], Golub and Van Loan [GL89],
Trefethen and Bau [TB97], and Demmel [Dem97].
The concept of closed function (§A.3.3) appears frequently in convex optimization, al-
though the terminology varies. The term is used by Rockafellar [Roc70, page 51], Hiriart-
Urruty and Lemar´echal [HUL93, volume 1, page 149], Borwein and Lewis [BL00, page
76], and Bertsekas, Nedi´c, and Ozdaglar [Ber03, page 28].


## Page 27

Appendix B
Problems involving two
quadratic functions
In this appendix we consider some optimization problems that involve two quadratic,
but not necessarily convex, functions. Several strong results hold for these prob-
lems, even when they are not convex.
B.1
Single constraint quadratic optimization
We consider the problem with one constraint
minimize
xT A0x + 2bT
0 x + c0
subject to
xT A1x + 2bT
1 x + c1 ≤0,
(B.1)
with variable x ∈Rn, and problem parameters Ai ∈Sn, bi ∈Rn, ci ∈R. We do
not assume that Ai ⪰0, so problem (B.1) is not a convex optimization problem.
The Lagrangian of (B.1) is
L(x, λ) = xT (A0 + λA1)x + 2(b0 + λb1)T x + c0 + λc1,
and the dual function is
g(λ) = inf
x L(x, λ)
=



c0 + λc1 −(b0 + λb1)T (A0 + λA1)†(b0 + λb1)
A0 + λA1 ⪰0,
b0 + λb1 ∈R(A0 + λA1)
−∞
otherwise
(see §A.5.4). Using a Schur complement, we can express the dual problem as
maximize
γ
subject to
λ ≥0

A0 + λA1
b0 + λb1
(b0 + λb1)T
c0 + λc1 −γ

⪰0,
(B.2)


## Page 28

654
B
Problems involving two quadratic functions
an SDP with two variables γ, λ ∈R.
The ﬁrst result is that strong duality holds for problem (B.1) and its Lagrange
dual (B.2), provided Slater’s constraint qualiﬁcation is satisﬁed, i.e., there exists
an x with xT A1x + 2bT
1 x + c1 < 0. In other words, if (B.1) is strictly feasible, the
optimal values of (B.1) and (B.2) are equal. (A proof is given in §B.4.)
Relaxation interpretation
The dual of the SDP (B.2) is
minimize
tr(A0X) + 2bT
0 x + c0
subject to
tr(A1X) + 2bT
1 x + c1 ≤0
 X
x
xT
1

⪰0,
(B.3)
an SDP with variables X ∈Sn, x ∈Rn.
This dual SDP has an interesting
interpretation in terms of the original problem (B.1).
We ﬁrst note that (B.1) is equivalent to
minimize
tr(A0X) + 2bT
0 x + c0
subject to
tr(A1X) + 2bT
1 x + c1 ≤0
X = xxT .
(B.4)
In this formulation we express the quadratic terms xT Aix as tr(AixxT ), and then
introduce a new variable X = xxT . Problem (B.4) has a linear objective function,
one linear inequality constraint, and a nonlinear equality constraint X = xxT . The
next step is to replace the equality constraint by an inequality X ⪰xxT :
minimize
tr(A0X) + bT
0 x + c0
subject to
tr(A1X) + bT
1 x + c1 ≤0
X ⪰xxT .
(B.5)
This problem is called a relaxation of (B.4), since we have replaced one of the
constraints with a looser constraint. Finally we note that the inequality in (B.5)
can be expressed as a linear matrix inequality by using a Schur complement, which
gives (B.3).
A number of interesting facts follow immediately from this interpretation of (B.3)
as a relaxation of (B.1). First, it is obvious that the optimal value of (B.3) is less
than or equal to the optimal value of (B.1), since we minimize the same objec-
tive function over a larger set. Second, we can conclude that if X = xxT at the
optimum of (B.3), then x must be optimal in (B.1).
Combining the result above, that strong duality holds between (B.1) and (B.2)
(if (B.1) is strictly feasible), with strong duality between the dual SDPs (B.2)
and (B.3), we conclude that strong duality holds between the original, nonconvex
quadratic problem (B.1), and the SDP relaxation (B.3), provided (B.1) is strictly
feasible.


## Page 29

B.2
The S-procedure
655
B.2
The S-procedure
The next result is a theorem of alternatives for a pair of (nonconvex) quadratic
inequalities. Let A1, A2 ∈Sn, b1, b2 ∈Rn, c1, c2 ∈R, and suppose there exists an
ˆx with
ˆxT A2ˆx + 2bT
2 ˆx + c2 < 0.
Then there exists an x ∈Rn satisfying
xT A1x + 2bT
1 x + c1 < 0,
xT A2x + 2bT
2 x + c2 ≤0,
(B.6)
if and only if there exists no λ such that
λ ≥0,
 A1
b1
bT
1
c1

+ λ
 A2
b2
bT
2
c2

⪰0.
(B.7)
In other words, (B.6) and (B.7) are strong alternatives.
This result is readily shown to be equivalent to the result from §B.1, and a proof
is given in §B.4. Here we point out that the two inequality systems are clearly weak
alternatives, since (B.6) and (B.7) together lead to a contradiction:
0
≤

x
1
T  A1
b1
bT
1
c1

+ λ
 A2
b2
bT
2
c2
 
x
1

=
xT A1x + 2bT
1 x + c1 + λ(xT A2x + 2bT
2 x + c2)
<
0.
This theorem of alternatives is sometimes called the S-procedure, and is usually
stated in the following form: the implication
xT F1x + 2gT
1 x + h1 ≤0
=⇒
xT F2x + 2gT
2 x + h2 ≤0,
where Fi ∈Sn, gi ∈Rn, hi ∈R, holds if and only if there exists a λ such that
λ ≥0,
 F2
g2
gT
2
h2

⪯λ
 F1
g1
gT
1
h1

,
provided there exists a point ˆx with ˆxT F1ˆx+2gT
1 ˆx+h1 < 0. (Note that suﬃciency
is clear.)
Example B.1
Ellipsoid containment. An ellipsoid E ⊆Rn with nonempty interior
can be represented as the sublevel set of a quadratic function,
E = {x | xT Fx + 2gT x + h ≤0},
where F ∈S++ and h −gT F −1g < 0. Suppose ˜E is another ellipsoid with similar
representation,
˜E = {x | xT ˜Fx + 2˜gT x + ˜h ≤0},
with ˜F ∈S++, ˜h −˜gT ˜F −1˜g < 0. By the S-procedure, we see that E ⊆˜E if and only
if there is a λ > 0 such that

˜F
˜g
˜gT
˜h

⪯λ

F
g
gT
h

.


## Page 30

656
B
Problems involving two quadratic functions
B.3
The ﬁeld of values of two symmetric matrices
The following result is the basis for the proof of the strong duality result in §B.1
and the S-procedure in §B.2. If A, B ∈Sn, then for all X ∈Sn
+, there exists an
x ∈Rn such that
xT Ax = tr(AX),
xT Bx = tr(BX).
(B.8)
Remark B.1 Geometric interpretation. This result has an interesting interpretation
in terms of the set
W(A, B) = {(xT Ax, xT Bx) | x ∈Rn},
which is a cone in R2. It is the cone generated by the set
F(A, B) = {(xT Ax, xT Bx) | ∥x∥2 = 1},
which is called the 2-dimensional ﬁeld of values of the pair (A, B). Geometrically,
W(A, B) is the image of the set of rank-one positive semideﬁnite matrices under the
linear transformation f : Sn →R2 deﬁned by
f(X) = (tr(AX), tr(BX)).
The result that for every X ∈Sn
+ there exists an x satisfying (B.8) means that
W(A, B) = f(Sn
+).
In other words, W(A, B) is a convex cone.
The proof is constructive and uses induction on the rank of X. Suppose it is
true for all X ∈Sn
+ with 1 ≤rank X ≤k, where k ≥2, that there exists an x such
that (B.8) holds. Then the result also holds if rank X = k + 1, as can be seen as
follows. A matrix X ∈Sn
+ with rank X = k + 1 can be expressed as X = yyT + Z
where y̸ = 0 and Z ∈Sn
+ with rank Z = k. By assumption, there exists a z such
that tr(AZ) = zT Az, tr(BZ) = zT Bz. Therefore
tr(AX) = tr(A(yyT + zzT )),
tr(BX) = tr(B(yyT + zzT )).
The rank of yyT + zzT is one or two, so by assumption there exists an x such
that (B.8) holds.
It is therefore suﬃcient to prove the result if rank X ≤2. If rank X = 0 and
rank X = 1 there is nothing to prove. If rank X = 2, we can factor X as X = V V T
where V ∈Rn×2, with linearly independent columns v1 and v2. Without loss of
generality we can assume that V T AV is diagonal. (If V T AV is not diagonal we
replace V with V P where V T AV = P diag(λ)P T is the eigenvalue decomposition
of V T AV .) We will write V T AV and V T BV as
V T AV =

λ1
0
0
λ2

,
V T BV =

σ1
γ
γ
σ2

,
and deﬁne
w =
 tr(AX)
tr(BX)

=
 λ1 + λ2
σ1 + σ2

.


## Page 31

B.4
Proofs of the strong duality results
657
We need to show that w = (xT Ax, xT Bx) for some x.
We distinguish two cases. First, assume (0, γ) is a linear combination of the
vectors (λ1, σ1) and (λ2, σ2):
0 = z1λ1 + z2λ2,
γ = z1σ1 + z2σ2,
for some z1, z2. In this case we choose x = αv1+βv2, where α and β are determined
by solving two quadratic equations in two variables
α2 + 2αβz1 = 1,
β2 + 2αβz2 = 1.
(B.9)
This will give the desired result, since
 (αv1 + βv2)T A(αv1 + βv2)
(αv1 + βv2)T B(αv1 + βv2)

=
α2
 λ1
σ1

+ 2αβ
 0
γ

+ β2
 λ2
σ2

=
(α2 + 2αβz1)

λ1
σ1

+ (β2 + 2αβz2)

λ2
σ2

=
 λ1 + λ2
σ1 + σ2

.
It remains to show that the equations (B.9) are solvable. To see this, we ﬁrst note
that α and β must be nonzero, so we can write the equations equivalently as
α2(1 + 2(β/α)z1) = 1,
(β/α)2 + 2(β/α)(z2 −z1) = 1.
The equation t2 + 2t(z2 −z1) = 1 has a positive and a negative root. At least one
of these roots (the root with the same sign as z1) satisﬁes 1 + 2tz1 > 0, so we can
choose
α = ±1/
√
1 + 2tz1,
β = tα.
This yields two solutions (α, β) that satisfy (B.9). (If both roots of t2+2t(z2−z1) =
1 satisfy 1 + 2tz1 > 0, we obtain four solutions.)
Next, assume that (0, γ) is not a linear combination of (λ1, σ1) and (λ2, σ2). In
particular, this means that (λ1, σ1) and (λ2, σ2) are linearly dependent. Therefore
their sum w = (λ1 + λ2, σ1 + σ2) is a nonnegative multiple of (λ1, σ1), or (λ2, σ2),
or both. If w = α2(λ1, σ1) for some α, we can choose x = αv1. If w = β2(λ2, σ2)
for some β, we can choose x = βv2.
B.4
Proofs of the strong duality results
We ﬁrst prove the S-procedure result given in §B.2.
The assumption of strict
feasibility of ˆx implies that the matrix
 A2
b2
bT
2
c2



## Page 32

658
B
Problems involving two quadratic functions
has at least one negative eigenvalue. Therefore
τ ≥0,
τ
 A2
b2
bT
2
c2

⪰0
=⇒
τ = 0.
We can apply the theorem of alternatives for nonstrict linear matrix inequalities,
given in example 5.14, which states that (B.7) is infeasible if and only if
X ⪰0,
tr

X
 A1
b1
bT
1
c1

< 0,
tr

X
 A2
b2
bT
2
c2

≤0
is feasible. From §B.3 this is equivalent to feasibility of

v
w
T  A1
b1
bT
1
c1
 
v
w

< 0,

v
w
T  A2
b2
bT
2
c2
 
v
w

≤0.
If w̸ = 0, then x = v/w is feasible in (B.6).
If w = 0, we have vT A1v < 0,
vT A2v ≤0, so x = ˆx + tv satisﬁes
xT A1x + 2bT
1 x + c1
=
ˆxT A1ˆx + 2bT
1 ˆx + c1 + t2vT A1v + 2t(A1ˆx + b1)T v
xT A2x + 2bT
2 x + c2
=
ˆxT A2ˆx + 2bT
2 ˆx + c2 + t2vT A2v + 2t(A2ˆx + b2)T v
<
2t(A2ˆx + b2)T v,
i.e., x becomes feasible as t →±∞, depending on the sign of (A2ˆx + b2)T v.
Finally, we prove the result in §B.1, i.e., that the optimal values of (B.1)
and (B.2) are equal if (B.1) is strictly feasible. To do this we note that γ is a
lower bound for the optimal value of (B.1) if
xT A1x + bT
1 x + c1 ≤0
=⇒
xT A0x + bT
0 x + c0 ≥γ.
By the S-procedure this is true if and only if there exists a λ ≥0 such that
 A0
b0
bT
0
c0 −γ

+ λ
 A1
b1
bT
1
c1

⪰0,
i.e., γ, λ are feasible in (B.2).


## Page 33

Bibliography
659
Bibliography
The results in this appendix are known under diﬀerent names in diﬀerent disciplines.
The term S-procedure is from control; see Boyd, El Ghaoui, Feron, and Balakrishnan
[BEFB94, pages 23, 33] for a survey and references. Variations of the S-procedure are
known in linear algebra in the context of joint diagonalization of a pair of symmetric
matrices; see, for example, Calabi [Cal64] and Uhlig [Uhl79]. Special cases of the strong
duality result are studied in the nonlinear programming literature on trust-region methods
(Stern and Wolkowicz [SW95], Nocedal and Wright [NW99, page 78]).
Brickman [Bri61] proves that the ﬁeld of values of a pair of matrices A, B ∈Sn (i.e., the
set F(A, B) deﬁned in remark B.1) is a convex set if n > 2, and that the set W(A, B)
is a convex cone (for any n). Our proof in §B.3 is based on Hestenes [Hes68]. Many
related results and additional references can be found in Horn and Johnson [HJ91, §1.8]
and Ben-Tal and Nemirovski [BTN01, §4.10.5].


## Page 34



## Page 35

Appendix C
Numerical linear algebra
background
In this appendix we give a brief overview of some basic numerical linear algebra,
concentrating on methods for solving one or more sets of linear equations. We focus
on direct (i.e., noniterative) methods, and how problem structure can be exploited
to improve eﬃciency. There are many important issues and methods in numerical
linear algebra that we do not consider here, including numerical stability, details
of matrix factorizations, methods for parallel or multiple processors, and iterative
methods. For these (and other) topics, we refer the reader to the references given
at the end of this appendix.
C.1
Matrix structure and algorithm complexity
We concentrate on methods for solving the set of linear equations
Ax = b
(C.1)
where A ∈Rn×n and b ∈Rn. We assume A is nonsingular, so the solution is
unique for all values of b, and given by x = A−1b. This basic problem arises in
many optimization algorithms, and often accounts for most of the computation. In
the context of solving the linear equations (C.1), the matrix A is often called the
coeﬃcient matrix, and the vector b is called the righthand side.
The standard generic methods for solving (C.1) require a computational eﬀort
that grows approximately like n3. These methods assume nothing more about A
than nonsingularity, and so are generally applicable.
For n several hundred or
smaller, these generic methods are probably the best methods to use, except in the
most demanding real-time applications. For n more than a thousand or so, the
generic methods of solving Ax = b become less practical.


## Page 36

662
C
Numerical linear algebra background
Coeﬃcient matrix structure
In many cases the coeﬃcient matrix A has some special structure or form that can
be exploited to solve the equation Ax = b more eﬃciently, using methods tailored
for the special structure.
For example, in the Newton system ∇2f(x)∆xnt =
−∇f(x), the coeﬃcient matrix is symmetric and positive deﬁnite, which allows us
to use a solution method that is around twice as fast as the generic method (and
also has better roundoﬀproperties). There are many other types of structure that
can be exploited, with computational savings (or algorithm speedup) that is usually
far more than a factor of two. In many cases, the eﬀort is reduced to something
proportional to n2 or even n, as compared to n3 for the generic methods. Since
these methods are usually applied when n is at least a hundred, and often far larger,
the savings can be dramatic.
A wide variety of coeﬃcient matrix structures can be exploited. Simple exam-
ples related to the sparsity pattern (i.e., the pattern of zero and nonzero entries
in the matrix) include banded, block diagonal, or sparse matrices. A more subtle
exploitable structure is diagonal plus low rank. Many common forms of convex
optimization problems lead to linear equations with coeﬃcient matrices that have
these exploitable structures. (There are many other matrix structures that can be
exploited, e.g., Toeplitz, Hankel, and circulant, that we will not consider in this
appendix.)
We refer to a generic method that does not exploit any sparsity pattern in the
matrices as one for dense matrices. We refer to a method that does not exploit any
structure at all in the matrices as one for unstructured matrices.
C.1.1
Complexity analysis via ﬂop count
The cost of a numerical linear algebra algorithm is often expressed by giving the
total number of ﬂoating-point operations or ﬂops required to carry it out, as a
function of various problem dimensions. We deﬁne a ﬂop as one addition, sub-
traction, multiplication, or division of two ﬂoating-point numbers. (Some authors
deﬁne a ﬂop as one multiplication followed by one addition, so their ﬂop counts
are smaller by a factor up to two.) To evaluate the complexity of an algorithm, we
count the total number of ﬂops, express it as a function (usually a polynomial) of
the dimensions of the matrices and vectors involved, and simplify the expression
by ignoring all terms except the leading (i.e., highest order or dominant) terms.
As an example, suppose that a particular algorithm requires a total of
m3 + 3m2n + mn + 4mn2 + 5m + 22
ﬂops, where m and n are problem dimensions. We would normally simplify this
ﬂop count to
m3 + 3m2n + 4mn2
ﬂops, since these are the leading terms in the problem dimensions m and n. If
in addition we assumed that m ≪n, we would further simplify the ﬂop count to
4mn2.


## Page 37

C.1
Matrix structure and algorithm complexity
663
Flop counts were originally popularized when ﬂoating-point operations were rel-
atively slow, so counting the number gave a good estimate of the total computation
time. This is no longer the case: Issues such as cache boundaries and locality of
reference can dramatically aﬀect the computation time of a numerical algorithm.
However, ﬂop counts can still give us a good rough estimate of the computation
time of a numerical algorithm, and how the time grows with increasing problem
size. Since a ﬂop count no longer accurately predicts the computation time of an
algorithm, we usually pay most attention to its order or orders, i.e., its largest
exponents, and ignore diﬀerences in ﬂop counts smaller than a factor of two or so.
For example, an algorithm with ﬂop count 5n2 is considered comparable to one
with a ﬂop count 4n2, but faster than an algorithm with ﬂop count (1/3)n3.
C.1.2
Cost of basic matrix-vector operations
Vector operations
To compute the inner product xT y of two vectors x, y ∈Rn we form the products
xiyi, and then add them, which requires n multiplies and n−1 additions, or 2n−1
ﬂops. As mentioned above, we keep only the leading term, and say that the inner
product requires 2n ﬂops, or even more approximately, order n ﬂops. A scalar-
vector multiplication αx, where α ∈R and x ∈Rn costs n ﬂops. The addition
x + y of two vectors x, y ∈Rn also costs n ﬂops.
If the vectors x and y are sparse, i.e., have only a few nonzero terms, these
basic operations can be carried out faster (assuming the vectors are stored using
an appropriate data structure). For example, if x is a sparse vector with N nonzero
entries, then the inner product xT y can be computed in 2N ﬂops.
Matrix-vector multiplication
A matrix-vector multiplication y = Ax where A ∈Rm×n costs 2mn ﬂops: We have
to calculate m components of y, each of which is the product of a row of A with
x, i.e., an inner product of two vectors in Rn.
Matrix-vector products can often be accelerated by taking advantage of struc-
ture in A. For example, if A is diagonal, then Ax can be computed in n ﬂops,
instead of 2n2 ﬂops for multiplication by a general n×n matrix. More generally, if
A is sparse, with only N nonzero elements (out of mn), then 2N ﬂops are needed
to form Ax, since we can skip multiplications and additions with zero.
As a less obvious example, suppose the matrix A has rank p ≪min{m, n}, and
is represented (stored) in the factored form A = UV , where U ∈Rm×p, V ∈Rp×n.
Then we can compute Ax by ﬁrst computing V x (which costs 2pn ﬂops), and then
computing U(V x) (which costs 2mp ﬂops), so the total is 2p(m + n) ﬂops. Since
p ≪min{m, n}, this is small compared to 2mn.
Matrix-matrix multiplication
The matrix-matrix product C = AB, where A ∈Rm×n and B ∈Rn×p, costs 2mnp
ﬂops. We have mp elements in C to calculate, each of which is an inner product of


## Page 38

664
C
Numerical linear algebra background
two vectors of length n. Again, we can often make substantial savings by taking
advantage of structure in A and B. For example, if A and B are sparse, we can
accelerate the multiplication by skipping additions and multiplications with zero.
If m = p and we know that C is symmetric, then we can calculate the matrix
product in m2n ﬂops, since we only have to compute the (1/2)m(m + 1) elements
in the lower triangular part.
To form the product of several matrices, we can carry out the matrix-matrix
multiplications in diﬀerent ways, which have diﬀerent ﬂop counts in general. The
simplest example is computing the product D = ABC, where A ∈Rm×n, B ∈
Rn×p, and C ∈Rp×q. Here we can compute D in two ways, using matrix-matrix
multiplies. One method is to ﬁrst form the product AB (2mnp ﬂops), and then form
D = (AB)C (2mpq ﬂops), so the total is 2mp(n+q) ﬂops. Alternatively, we can ﬁrst
form the product BC (2npq ﬂops), and then form D = A(BC) (2mnq ﬂops), with a
total of 2nq(m+p) ﬂops. The ﬁrst method is better when 2mp(n+q) < 2nq(m+p),
i.e., when
1
n + 1
q < 1
m + 1
p.
This assumes that no structure of the matrices is exploited in carrying out matrix-
matrix products.
For products of more than three matrices, there are many ways to parse the
product into matrix-matrix multiplications. Although it is not hard to develop an
algorithm that determines the best parsing (i.e., the one with the fewest required
ﬂops) given the matrix dimensions, in most applications the best parsing is clear.
C.2
Solving linear equations with factored matrices
C.2.1
Linear equations that are easy to solve
We start by examining some cases for which Ax = b is easily solved, i.e., x = A−1b
is easily computed.
Diagonal matrices
Suppose A is diagonal and nonsingular (i.e., aii̸ = 0 for all i). The set of linear
equations Ax = b can be written as aiixi = bi, i = 1, . . . , n. The solution is given
by xi = bi/aii, and can be calculated in n ﬂops.
Lower triangular matrices
A matrix A ∈Rn×n is lower triangular if aij = 0 for j > i. A lower triangular
matrix is called unit lower triangular if the diagonal elements are equal to one. A
lower triangular matrix is nonsingular if and only if aii̸ = 0 for all i.


## Page 39

C.2
Solving linear equations with factored matrices
665
Suppose A is lower triangular and nonsingular. The equations Ax = b are


a11
0
· · ·
0
a21
a22
· · ·
0
...
...
...
...
an1
an2
· · ·
ann




x1
x2
...
xn

=


b1
b2
...
bn

.
From the ﬁrst row, we have a11x1 = b1, from which we conclude x1 = b1/a11.
From the second row we have a21x1 + a22x2 = b2, so we can express x2 as x2 =
(b2−a21x1)/a22. (We have already computed x1, so every number on the righthand
side is known.) Continuing this way, we can express each component of x in terms
of previous components, yielding the algorithm
x1
:=
b1/a11
x2
:=
(b2 −a21x1)/a22
x3
:=
(b3 −a31x1 −a32x2)/a33
...
xn
:=
(bn −an1x1 −an2x2 −· · · −an,n−1xn−1)/ann.
This procedure is called forward substitution, since we successively compute the
components of x by substituting the known values into the next equation.
Let us give a ﬂop count for forward substitution. We start by calculating x1 (1
ﬂop). We substitute x1 in the second equation to ﬁnd x2 (3 ﬂops), then substitute
x1 and x2 in the third equation to ﬁnd x3 (5 ﬂops), etc. The total number of ﬂops
is
1 + 3 + 5 + · · · + (2n −1) = n2.
Thus, when A is lower triangular and nonsingular, we can compute x = A−1b in
n2 ﬂops.
If the matrix A has additional structure, in addition to being lower triangular,
then forward substitution can be more eﬃcient than n2 ﬂops. For example, if A
is sparse (or banded), with at most k nonzero entries per row, then each forward
substitution step requires at most 2k+1 ﬂops, so the overall ﬂop count is 2(k+1)n,
or 2kn after dropping the term 2n.
Upper triangular matrices
A matrix A ∈Rn×n is upper triangular if AT is lower triangular, i.e., if aij = 0 for
j < i. We can solve linear equations with nonsingular upper triangular coeﬃcient
matrix in a way similar to forward substitution, except that we start by calculating
xn, then xn−1, and so on. The algorithm is
xn
:=
bn/ann
xn−1
:=
(bn−1 −an−1,nxn)/an−1,n−1
xn−2
:=
(bn−2 −an−2,n−1xn−1 −an−2,nxn)/an−2,n−2
...
x1
:=
(b1 −a12x2 −a13x3 −· · · −a1nxn)/a11.


## Page 40

666
C
Numerical linear algebra background
This is called backward substitution or back substitution since we determine the
coeﬃcients in backward order.
The cost to compute x = A−1b via backward
substitution is n2 ﬂops. If A is upper triangular and sparse (or banded), with at
most k nonzero entries per row, then back substitution costs 2kn ﬂops.
Orthogonal matrices
A matrix A ∈Rn×n is orthogonal if AT A = I, i.e., A−1 = AT . In this case we can
compute x = A−1b by a simple matrix-vector product x = AT b, which costs 2n2
in general.
If the matrix A has additional structure, we can compute x = A−1b even more
eﬃciently than 2n2 ﬂops. For example, if A has the form A = I −2uuT , where
∥u∥2 = 1, we can compute
x = A−1b = (I −2uuT )T b = b −2(uT b)u
by ﬁrst computing uT b, then forming b −2(uT b)u, which costs 4n ﬂops.
Permutation matrices
Let π = (π1, . . . , πn) be a permutation of (1, 2, . . . , n). The associated permutation
matrix A ∈Rn×n is given by
Aij =

1
j = πi
0
otherwise.
In each row (or column) of a permutation matrix there is exactly one entry with
value one; all other entries are zero. Multiplying a vector by a permutation matrix
simply permutes its coeﬃcients:
Ax = (xπ1, . . . , xπn) .
The inverse of a permutation matrix is the permutation matrix associated with the
inverse permutation π−1. This turns out to be AT , which shows that permutation
matrices are orthogonal.
If A is a permutation matrix, solving Ax = b is very easy: x is obtained by
permuting the entries of b by π−1.
This requires no ﬂoating point operations,
according to our deﬁnition (but, depending on the implementation, might involve
copying ﬂoating point numbers).
We can reach the same conclusion from the
equation x = AT b. The matrix AT (like A) has only one nonzero entry per row, with
value one. Thus no additions are required, and the only multiplications required
are by one.
C.2.2
The factor-solve method
The basic approach to solving Ax = b is based on expressing A as a product of
nonsingular matrices,
A = A1A2 · · · Ak,
