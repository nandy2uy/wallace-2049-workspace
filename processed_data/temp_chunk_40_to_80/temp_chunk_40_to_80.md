# temp_chunk_40_to_80



## Page 1

2.2
Some important examples
27
2.2
Some important examples
In this section we describe some important examples of convex sets which we will
encounter throughout the rest of the book. We start with some simple examples.
• The empty set ∅, any single point (i.e., singleton) {x0}, and the whole space
Rn are aﬃne (hence, convex) subsets of Rn.
• Any line is aﬃne. If it passes through zero, it is a subspace, hence also a
convex cone.
• A line segment is convex, but not aﬃne (unless it reduces to a point).
• A ray, which has the form {x0 + θv | θ ≥0}, where v̸ = 0, is convex, but not
aﬃne. It is a convex cone if its base x0 is 0.
• Any subspace is aﬃne, and a convex cone (hence convex).
2.2.1
Hyperplanes and halfspaces
A hyperplane is a set of the form
{x | aT x = b},
where a ∈Rn, a̸ = 0, and b ∈R. Analytically it is the solution set of a nontrivial
linear equation among the components of x (and hence an aﬃne set). Geometri-
cally, the hyperplane {x | aT x = b} can be interpreted as the set of points with a
constant inner product to a given vector a, or as a hyperplane with normal vector
a; the constant b ∈R determines the oﬀset of the hyperplane from the origin. This
geometric interpretation can be understood by expressing the hyperplane in the
form
{x | aT (x −x0) = 0},
where x0 is any point in the hyperplane (i.e., any point that satisﬁes aT x0 = b).
This representation can in turn be expressed as
{x | aT (x −x0) = 0} = x0 + a⊥,
where a⊥denotes the orthogonal complement of a, i.e., the set of all vectors or-
thogonal to it:
a⊥= {v | aT v = 0}.
This shows that the hyperplane consists of an oﬀset x0, plus all vectors orthog-
onal to the (normal) vector a. These geometric interpretations are illustrated in
ﬁgure 2.6.
A hyperplane divides Rn into two halfspaces. A (closed) halfspace is a set of
the form
{x | aT x ≤b},
(2.1)
where a̸ = 0, i.e., the solution set of one (nontrivial) linear inequality. Halfspaces
are convex, but not aﬃne. This is illustrated in ﬁgure 2.7.


## Page 2

28
2
Convex sets
a
x
aT x = b
x0
Figure 2.6 Hyperplane in R2, with normal vector a and a point x0 in the
hyperplane. For any point x in the hyperplane, x −x0 (shown as the darker
arrow) is orthogonal to a.
a
aT x ≥b
aT x ≤b
x0
Figure 2.7 A hyperplane deﬁned by aT x = b in R2 determines two halfs-
paces. The halfspace determined by aT x ≥b (not shaded) is the halfspace
extending in the direction a. The halfspace determined by aT x ≤b (which
is shown shaded) extends in the direction −a. The vector a is the outward
normal of this halfspace.


## Page 3

2.2
Some important examples
29
a
x1
x2
x0
Figure 2.8 The shaded set is the halfspace determined by aT (x −x0) ≤0.
The vector x1−x0 makes an acute angle with a, so x1 is not in the halfspace.
The vector x2 −x0 makes an obtuse angle with a, and so is in the halfspace.
The halfspace (2.1) can also be expressed as
{x | aT (x −x0) ≤0},
(2.2)
where x0 is any point on the associated hyperplane, i.e., satisﬁes aT x0 = b. The
representation (2.2) suggests a simple geometric interpretation: the halfspace con-
sists of x0 plus any vector that makes an obtuse (or right) angle with the (outward
normal) vector a. This is illustrated in ﬁgure 2.8.
The boundary of the halfspace (2.1) is the hyperplane {x | aT x = b}. The set
{x | aT x < b}, which is the interior of the halfspace {x | aT x ≤b}, is called an
open halfspace.
2.2.2
Euclidean balls and ellipsoids
A (Euclidean) ball (or just ball) in Rn has the form
B(xc, r) = {x | ∥x −xc∥2 ≤r} = {x | (x −xc)T (x −xc) ≤r2},
where r > 0, and ∥· ∥2 denotes the Euclidean norm, i.e., ∥u∥2 = (uT u)1/2. The
vector xc is the center of the ball and the scalar r is its radius; B(xc, r) consists
of all points within a distance r of the center xc. Another common representation
for the Euclidean ball is
B(xc, r) = {xc + ru | ∥u∥2 ≤1}.


## Page 4

30
2
Convex sets
xc
Figure 2.9 An ellipsoid in R2, shown shaded. The center xc is shown as a
dot, and the two semi-axes are shown as line segments.
A Euclidean ball is a convex set: if ∥x1 −xc∥2 ≤r, ∥x2 −xc∥2 ≤r, and
0 ≤θ ≤1, then
∥θx1 + (1 −θ)x2 −xc∥2
=
∥θ(x1 −xc) + (1 −θ)(x2 −xc)∥2
≤
θ∥x1 −xc∥2 + (1 −θ)∥x2 −xc∥2
≤
r.
(Here we use the homogeneity property and triangle inequality for ∥·∥2; see §A.1.2.)
A related family of convex sets is the ellipsoids, which have the form
E = {x | (x −xc)T P −1(x −xc) ≤1},
(2.3)
where P = P T ≻0, i.e., P is symmetric and positive deﬁnite. The vector xc ∈Rn
is the center of the ellipsoid. The matrix P determines how far the ellipsoid extends
in every direction from xc; the lengths of the semi-axes of E are given by √λi, where
λi are the eigenvalues of P. A ball is an ellipsoid with P = r2I. Figure 2.9 shows
an ellipsoid in R2.
Another common representation of an ellipsoid is
E = {xc + Au | ∥u∥2 ≤1},
(2.4)
where A is square and nonsingular. In this representation we can assume without
loss of generality that A is symmetric and positive deﬁnite. By taking A = P 1/2,
this representation gives the ellipsoid deﬁned in (2.3). When the matrix A in (2.4)
is symmetric positive semideﬁnite but singular, the set in (2.4) is called a degenerate
ellipsoid; its aﬃne dimension is equal to the rank of A. Degenerate ellipsoids are
also convex.
2.2.3
Norm balls and norm cones
Suppose ∥·∥is any norm on Rn (see §A.1.2). From the general properties of norms it
can be shown that a norm ball of radius r and center xc, given by {x | ∥x−xc∥≤r},
is convex. The norm cone associated with the norm ∥· ∥is the set
C = {(x, t) | ∥x∥≤t} ⊆Rn+1.


## Page 5

2.2
Some important examples
31
x1
x2
t
−1
0
1
−1
0
1
0
0.5
1
Figure 2.10 Boundary of second-order cone in R3, {(x1, x2, t) | (x2
1+x2
2)1/2 ≤
t}.
It is (as the name suggests) a convex cone.
Example 2.3 The second-order cone is the norm cone for the Euclidean norm, i.e.,
C
=
{(x, t) ∈Rn+1 | ∥x∥2 ≤t}
=
(
x
t
 

x
t
T 
I
0
0
−1
 
x
t

≤0, t ≥0
)
.
The second-order cone is also known by several other names. It is called the quadratic
cone, since it is deﬁned by a quadratic inequality. It is also called the Lorentz cone
or ice-cream cone. Figure 2.10 shows the second-order cone in R3.
2.2.4
Polyhedra
A polyhedron is deﬁned as the solution set of a ﬁnite number of linear equalities
and inequalities:
P = {x | aT
j x ≤bj, j = 1, . . . , m, cT
j x = dj, j = 1, . . . , p}.
(2.5)
A polyhedron is thus the intersection of a ﬁnite number of halfspaces and hyper-
planes. Aﬃne sets (e.g., subspaces, hyperplanes, lines), rays, line segments, and
halfspaces are all polyhedra. It is easily shown that polyhedra are convex sets.
A bounded polyhedron is sometimes called a polytope, but some authors use the
opposite convention (i.e., polytope for any set of the form (2.5), and polyhedron


## Page 6

32
2
Convex sets
a1
a2
a3
a4
a5
P
Figure 2.11 The polyhedron P (shown shaded) is the intersection of ﬁve
halfspaces, with outward normal vectors a1, . . . . , a5.
when it is bounded). Figure 2.11 shows an example of a polyhedron deﬁned as the
intersection of ﬁve halfspaces.
It will be convenient to use the compact notation
P = {x | Ax ⪯b, Cx = d}
(2.6)
for (2.5), where
A =


aT
1
...
aT
m

,
C =


cT
1
...
cT
p

,
and the symbol ⪯denotes vector inequality or componentwise inequality in Rm:
u ⪯v means ui ≤vi for i = 1, . . . , m.
Example 2.4 The nonnegative orthant is the set of points with nonnegative compo-
nents, i.e.,
Rn
+ = {x ∈Rn | xi ≥0, i = 1, . . . , n} = {x ∈Rn | x ⪰0}.
(Here R+ denotes the set of nonnegative numbers: R+ = {x ∈R | x ≥0}.) The
nonnegative orthant is a polyhedron and a cone (and therefore called a polyhedral
cone).
Simplexes
Simplexes are another important family of polyhedra. Suppose the k + 1 points
v0, . . . , vk ∈Rn are aﬃnely independent, which means v1 −v0, . . . , vk −v0 are
linearly independent. The simplex determined by them is given by
C = conv{v0, . . . , vk} = {θ0v0 + · · · + θkvk | θ ⪰0, 1T θ = 1},
(2.7)


## Page 7

2.2
Some important examples
33
where 1 denotes the vector with all entries one. The aﬃne dimension of this simplex
is k, so it is sometimes referred to as a k-dimensional simplex in Rn.
Example 2.5 Some common simplexes. A 1-dimensional simplex is a line segment;
a 2-dimensional simplex is a triangle (including its interior); and a 3-dimensional
simplex is a tetrahedron.
The unit simplex is the n-dimensional simplex determined by the zero vector and the
unit vectors, i.e., 0, e1, . . . , en ∈Rn. It can be expressed as the set of vectors that
satisfy
x ⪰0,
1T x ≤1.
The probability simplex is the (n −1)-dimensional simplex determined by the unit
vectors e1, . . . , en ∈Rn. It is the set of vectors that satisfy
x ⪰0,
1T x = 1.
Vectors in the probability simplex correspond to probability distributions on a set
with n elements, with xi interpreted as the probability of the ith element.
To describe the simplex (2.7) as a polyhedron, i.e., in the form (2.6), we proceed
as follows. By deﬁnition, x ∈C if and only if x = θ0v0 + θ1v1 + · · · + θkvk for some
θ ⪰0 with 1T θ = 1. Equivalently, if we deﬁne y = (θ1, . . . , θk) and
B =
 v1 −v0
· · ·
vk −v0

∈Rn×k,
we can say that x ∈C if and only if
x = v0 + By
(2.8)
for some y ⪰0 with 1T y ≤1.
Now we note that aﬃne independence of the
points v0, . . . , vk implies that the matrix B has rank k. Therefore there exists a
nonsingular matrix A = (A1, A2) ∈Rn×n such that
AB =

A1
A2

B =

I
0

.
Multiplying (2.8) on the left with A, we obtain
A1x = A1v0 + y,
A2x = A2v0.
From this we see that x ∈C if and only if A2x = A2v0, and the vector y =
A1x −A1v0 satisﬁes y ⪰0 and 1T y ≤1. In other words we have x ∈C if and only
if
A2x = A2v0,
A1x ⪰A1v0,
1T A1x ≤1 + 1T A1v0,
which is a set of linear equalities and inequalities in x, and so describes a polyhe-
dron.


## Page 8

34
2
Convex sets
Convex hull description of polyhedra
The convex hull of the ﬁnite set {v1, . . . , vk} is
conv{v1, . . . , vk} = {θ1v1 + · · · + θkvk | θ ⪰0, 1T θ = 1}.
This set is a polyhedron, and bounded, but (except in special cases, e.g., a simplex)
it is not simple to express it in the form (2.5), i.e., by a set of linear equalities and
inequalities.
A generalization of this convex hull description is
{θ1v1 + · · · + θkvk | θ1 + · · · + θm = 1, θi ≥0, i = 1, . . . , k},
(2.9)
where m ≤k. Here we consider nonnegative linear combinations of vi, but only
the ﬁrst m coeﬃcients are required to sum to one. Alternatively, we can inter-
pret (2.9) as the convex hull of the points v1, . . . , vm, plus the conic hull of the
points vm+1, . . . , vk.
The set (2.9) deﬁnes a polyhedron, and conversely, every
polyhedron can be represented in this form (although we will not show this).
The question of how a polyhedron is represented is subtle, and has very im-
portant practical consequences. As a simple example consider the unit ball in the
ℓ∞-norm in Rn,
C = {x | |xi| ≤1, i = 1, . . . , n}.
The set C can be described in the form (2.5) with 2n linear inequalities ±eT
i x ≤1,
where ei is the ith unit vector. To describe it in the convex hull form (2.9) requires
at least 2n points:
C = conv{v1, . . . , v2n},
where v1, . . . , v2n are the 2n vectors all of whose components are 1 or −1. Thus
the size of the two descriptions diﬀers greatly, for large n.
2.2.5
The positive semideﬁnite cone
We use the notation Sn to denote the set of symmetric n × n matrices,
Sn = {X ∈Rn×n | X = XT },
which is a vector space with dimension n(n + 1)/2. We use the notation Sn
+ to
denote the set of symmetric positive semideﬁnite matrices:
Sn
+ = {X ∈Sn | X ⪰0},
and the notation Sn
++ to denote the set of symmetric positive deﬁnite matrices:
Sn
++ = {X ∈Sn | X ≻0}.
(This notation is meant to be analogous to R+, which denotes the nonnegative
reals, and R++, which denotes the positive reals.)


## Page 9

2.3
Operations that preserve convexity
35
x
y
z
0
0.5
1
−1
0
1
0
0.5
1
Figure 2.12 Boundary of positive semideﬁnite cone in S2.
The set Sn
+ is a convex cone: if θ1, θ2 ≥0 and A, B ∈Sn
+, then θ1A+θ2B ∈Sn
+.
This can be seen directly from the deﬁnition of positive semideﬁniteness: for any
x ∈Rn, we have
xT (θ1A + θ2B)x = θ1xT Ax + θ2xT Bx ≥0,
if A ⪰0, B ⪰0 and θ1, θ2 ≥0.
Example 2.6 Positive semideﬁnite cone in S2. We have
X =

x
y
y
z

∈S2
+
⇐⇒
x ≥0,
z ≥0,
xz ≥y2.
The boundary of this cone is shown in ﬁgure 2.12, plotted in R3 as (x, y, z).
2.3
Operations that preserve convexity
In this section we describe some operations that preserve convexity of sets, or
allow us to construct convex sets from others. These operations, together with the
simple examples described in §2.2, form a calculus of convex sets that is useful for
determining or establishing convexity of sets.


## Page 10

36
2
Convex sets
2.3.1
Intersection
Convexity is preserved under intersection: if S1 and S2 are convex, then S1 ∩S2 is
convex. This property extends to the intersection of an inﬁnite number of sets: if
Sα is convex for every α ∈A, then T
α∈A Sα is convex. (Subspaces, aﬃne sets, and
convex cones are also closed under arbitrary intersections.) As a simple example,
a polyhedron is the intersection of halfspaces and hyperplanes (which are convex),
and therefore is convex.
Example 2.7 The positive semideﬁnite cone Sn
+ can be expressed as
\
z̸=0
{X ∈Sn | zT Xz ≥0}.
For each z̸ = 0, zT Xz is a (not identically zero) linear function of X, so the sets
{X ∈Sn | zT Xz ≥0}
are, in fact, halfspaces in Sn. Thus the positive semideﬁnite cone is the intersection
of an inﬁnite number of halfspaces, and so is convex.
Example 2.8 We consider the set
S = {x ∈Rm | |p(t)| ≤1 for |t| ≤π/3},
(2.10)
where p(t) = Pm
k=1 xk cos kt. The set S can be expressed as the intersection of an
inﬁnite number of slabs: S = T
|t|≤π/3 St, where
St = {x | −1 ≤(cos t, . . . , cos mt)T x ≤1},
and so is convex. The deﬁnition and the set are illustrated in ﬁgures 2.13 and 2.14,
for m = 2.
In the examples above we establish convexity of a set by expressing it as a
(possibly inﬁnite) intersection of halfspaces. We will see in §2.5.1 that a converse
holds: every closed convex set S is a (usually inﬁnite) intersection of halfspaces.
In fact, a closed convex set S is the intersection of all halfspaces that contain it:
S =
\
{H | H halfspace, S ⊆H}.
2.3.2
Aﬃne functions
Recall that a function f : Rn →Rm is aﬃne if it is a sum of a linear function and
a constant, i.e., if it has the form f(x) = Ax + b, where A ∈Rm×n and b ∈Rm.
Suppose S ⊆Rn is convex and f : Rn →Rm is an aﬃne function. Then the image
of S under f,
f(S) = {f(x) | x ∈S},


## Page 11

2.3
Operations that preserve convexity
37
0
π/3
2π/3
π
−1
0
1
t
p(t)
Figure 2.13 Three trigonometric polynomials associated with points in the
set S deﬁned in (2.10), for m = 2. The trigonometric polynomial plotted
with dashed line type is the average of the other two.
x1
x2
S
−2
−1
0
1
2
−2
−1
0
1
2
Figure 2.14 The set S deﬁned in (2.10), for m = 2, is shown as the white
area in the middle of the plot.
The set is the intersection of an inﬁnite
number of slabs (20 of which are shown), hence convex.


## Page 12

38
2
Convex sets
is convex. Similarly, if f : Rk →Rn is an aﬃne function, the inverse image of S
under f,
f −1(S) = {x | f(x) ∈S},
is convex.
Two simple examples are scaling and translation. If S ⊆Rn is convex, α ∈R,
and a ∈Rn, then the sets αS and S + a are convex, where
αS = {αx | x ∈S},
S + a = {x + a | x ∈S}.
The projection of a convex set onto some of its coordinates is convex: if S ⊆
Rm × Rn is convex, then
T = {x1 ∈Rm | (x1, x2) ∈S for some x2 ∈Rn}
is convex.
The sum of two sets is deﬁned as
S1 + S2 = {x + y | x ∈S1, y ∈S2}.
If S1 and S2 are convex, then S1 + S2 is convex. To see this, if S1 and S2 are
convex, then so is the direct or Cartesian product
S1 × S2 = {(x1, x2) | x1 ∈S1, x2 ∈S2}.
The image of this set under the linear function f(x1, x2) = x1 + x2 is the sum
S1 + S2.
We can also consider the partial sum of S1, S2 ∈Rn × Rm, deﬁned as
S = {(x, y1 + y2) | (x, y1) ∈S1, (x, y2) ∈S2},
where x ∈Rn and yi ∈Rm. For m = 0, the partial sum gives the intersection of
S1 and S2; for n = 0, it is set addition. Partial sums of convex sets are convex (see
exercise 2.16).
Example 2.9 Polyhedron. The polyhedron {x | Ax ⪯b, Cx = d} can be expressed as
the inverse image of the Cartesian product of the nonnegative orthant and the origin
under the aﬃne function f(x) = (b −Ax, d −Cx):
{x | Ax ⪯b, Cx = d} = {x | f(x) ∈Rm
+ × {0}}.
Example 2.10 Solution set of linear matrix inequality. The condition
A(x) = x1A1 + · · · + xnAn ⪯B,
(2.11)
where B, Ai ∈Sm, is called a linear matrix inequality (LMI) in x. (Note the similarity
to an ordinary linear inequality,
aT x = x1a1 + · · · + xnan ≤b,
with b, ai ∈R.)
The solution set of a linear matrix inequality, {x | A(x) ⪯B}, is convex. Indeed,
it is the inverse image of the positive semideﬁnite cone under the aﬃne function
f : Rn →Sm given by f(x) = B −A(x).


## Page 13

2.3
Operations that preserve convexity
39
Example 2.11 Hyperbolic cone. The set
{x | xT Px ≤(cT x)2, cT x ≥0}
where P ∈Sn
+ and c ∈Rn, is convex, since it is the inverse image of the second-order
cone,
{(z, t) | zT z ≤t2, t ≥0},
under the aﬃne function f(x) = (P 1/2x, cT x).
Example 2.12 Ellipsoid. The ellipsoid
E = {x | (x −xc)T P −1(x −xc) ≤1},
where P ∈Sn
++, is the image of the unit Euclidean ball {u | ∥u∥2 ≤1} under the
aﬃne mapping f(u) = P 1/2u + xc. (It is also the inverse image of the unit ball under
the aﬃne mapping g(x) = P −1/2(x −xc).)
2.3.3
Linear-fractional and perspective functions
In this section we explore a class of functions, called linear-fractional, that is more
general than aﬃne but still preserves convexity.
The perspective function
We deﬁne the perspective function P : Rn+1 →Rn, with domain dom P = Rn ×
R++, as P(z, t) = z/t. (Here R++ denotes the set of positive numbers: R++ =
{x ∈R | x > 0}.) The perspective function scales or normalizes vectors so the last
component is one, and then drops the last component.
Remark 2.1
We can interpret the perspective function as the action of a pin-hole
camera. A pin-hole camera (in R3) consists of an opaque horizontal plane x3 = 0,
with a single pin-hole at the origin, through which light can pass, and a horizontal
image plane x3 = −1. An object at x, above the camera (i.e., with x3 > 0), forms
an image at the point −(x1/x3, x2/x3, 1) on the image plane.
Dropping the last
component of the image point (since it is always −1), the image of a point at x
appears at y = −(x1/x3, x2/x3) = −P(x) on the image plane. This is illustrated in
ﬁgure 2.15.
If C ⊆dom P is convex, then its image
P(C) = {P(x) | x ∈C}
is convex. This result is certainly intuitive: a convex object, viewed through a
pin-hole camera, yields a convex image. To establish this fact we show that line
segments are mapped to line segments under the perspective function. (This too


## Page 14

40
2
Convex sets
x3 = 0
x3 = −1
Figure 2.15 Pin-hole camera interpretation of perspective function.
The
dark horizontal line represents the plane x3 = 0 in R3, which is opaque,
except for a pin-hole at the origin. Objects or light sources above the plane
appear on the image plane x3 = −1, which is shown as the lighter horizontal
line. The mapping of the position of a source to the position of its image is
related to the perspective function.
makes sense: a line segment, viewed through a pin-hole camera, yields a line seg-
ment image.) Suppose that x = (˜x, xn+1), y = (˜y, yn+1) ∈Rn+1 with xn+1 > 0,
yn+1 > 0. Then for 0 ≤θ ≤1,
P(θx + (1 −θ)y) =
θ˜x + (1 −θ)˜y
θxn+1 + (1 −θ)yn+1
= µP(x) + (1 −µ)P(y),
where
µ =
θxn+1
θxn+1 + (1 −θ)yn+1
∈[0, 1].
This correspondence between θ and µ is monotonic: as θ varies between 0 and 1
(which sweeps out the line segment [x, y]), µ varies between 0 and 1 (which sweeps
out the line segment [P(x), P(y)]). This shows that P([x, y]) = [P(x), P(y)].
Now suppose C is convex with C ⊆dom P (i.e., xn+1 > 0 for all x ∈C), and
x, y ∈C. To establish convexity of P(C) we need to show that the line segment
[P(x), P(y)] is in P(C). But this line segment is the image of the line segment
[x, y] under P, and so lies in P(C).
The inverse image of a convex set under the perspective function is also convex:
if C ⊆Rn is convex, then
P −1(C) = {(x, t) ∈Rn+1 | x/t ∈C, t > 0}
is convex. To show this, suppose (x, t) ∈P −1(C), (y, s) ∈P −1(C), and 0 ≤θ ≤1.
We need to show that
θ(x, t) + (1 −θ)(y, s) ∈P −1(C),
i.e., that
θx + (1 −θ)y
θt + (1 −θ)s ∈C


## Page 15

2.3
Operations that preserve convexity
41
(θt + (1 −θ)s > 0 is obvious). This follows from
θx + (1 −θ)y
θt + (1 −θ)s = µ(x/t) + (1 −µ)(y/s),
where
µ =
θt
θt + (1 −θ)s ∈[0, 1].
Linear-fractional functions
A linear-fractional function is formed by composing the perspective function with
an aﬃne function. Suppose g : Rn →Rm+1 is aﬃne, i.e.,
g(x) =
 A
cT

x +
 b
d

,
(2.12)
where A ∈Rm×n, b ∈Rm, c ∈Rn, and d ∈R. The function f : Rn →Rm given
by f = P ◦g, i.e.,
f(x) = (Ax + b)/(cT x + d),
dom f = {x | cT x + d > 0},
(2.13)
is called a linear-fractional (or projective) function. If c = 0 and d > 0, the domain
of f is Rn, and f is an aﬃne function. So we can think of aﬃne and linear functions
as special cases of linear-fractional functions.
Remark 2.2
Projective interpretation. It is often convenient to represent a linear-
fractional function as a matrix
Q =

A
b
cT
d

∈R(m+1)×(n+1)
(2.14)
that acts on (multiplies) points of form (x, 1), which yields (Ax + b, cT x + d). This
result is then scaled or normalized so that its last component is one, which yields
(f(x), 1).
This representation can be interpreted geometrically by associating Rn with a set
of rays in Rn+1 as follows. With each point z in Rn we associate the (open) ray
P(z) = {t(z, 1) | t > 0} in Rn+1. The last component of this ray takes on positive
values. Conversely any ray in Rn+1, with base at the origin and last component
which takes on positive values, can be written as P(v) = {t(v, 1) | t ≥0} for some
v ∈Rn. This (projective) correspondence P between Rn and the halfspace of rays
with positive last component is one-to-one and onto.
The linear-fractional function (2.13) can be expressed as
f(x) = P−1(QP(x)).
Thus, we start with x ∈dom f, i.e., cT x + d > 0. We then form the ray P(x) in
Rn+1. The linear transformation with matrix Q acts on this ray to produce another
ray QP(x). Since x ∈dom f, the last component of this ray assumes positive values.
Finally we take the inverse projective transformation to recover f(x).


## Page 16

42
2
Convex sets
x1
x2
C
−1
0
1
−1
0
1
x1
x2
f(C)
−1
0
1
−1
0
1
Figure 2.16 Left. A set C ⊆R2. The dashed line shows the boundary of
the domain of the linear-fractional function f(x) = x/(x1 + x2 + 1) with
dom f = {(x1, x2) | x1 + x2 + 1 > 0}. Right. Image of C under f. The
dashed line shows the boundary of the domain of f −1.
Like the perspective function, linear-fractional functions preserve convexity. If
C is convex and lies in the domain of f (i.e., cT x + d > 0 for x ∈C), then its
image f(C) is convex. This follows immediately from results above: the image of C
under the aﬃne mapping (2.12) is convex, and the image of the resulting set under
the perspective function P, which yields f(C), is convex. Similarly, if C ⊆Rm is
convex, then the inverse image f −1(C) is convex.
Example 2.13
Conditional probabilities.
Suppose u and v are random variables
that take on values in {1, . . . , n} and {1, . . . , m}, respectively, and let pij denote
prob(u = i, v = j). Then the conditional probability fij = prob(u = i|v = j) is
given by
fij =
pij
Pn
k=1 pkj
.
Thus f is obtained by a linear-fractional mapping from p.
It follows that if C is a convex set of joint probabilities for (u, v), then the associated
set of conditional probabilities of u given v is also convex.
Figure 2.16 shows a set C ⊆R2, and its image under the linear-fractional
function
f(x) =
1
x1 + x2 + 1x,
dom f = {(x1, x2) | x1 + x2 + 1 > 0}.


## Page 17

2.4
Generalized inequalities
43
2.4
Generalized inequalities
2.4.1
Proper cones and generalized inequalities
A cone K ⊆Rn is called a proper cone if it satisﬁes the following:
• K is convex.
• K is closed.
• K is solid, which means it has nonempty interior.
• K is pointed, which means that it contains no line (or equivalently, x ∈
K, −x ∈K =⇒x = 0).
A proper cone K can be used to deﬁne a generalized inequality, which is a partial
ordering on Rn that has many of the properties of the standard ordering on R.
We associate with the proper cone K the partial ordering on Rn deﬁned by
x ⪯K y ⇐⇒y −x ∈K.
We also write x ⪰K y for y ⪯K x. Similarly, we deﬁne an associated strict partial
ordering by
x ≺K y ⇐⇒y −x ∈int K,
and write x ≻K y for y ≺K x.
(To distinguish the generalized inequality ⪯K
from the strict generalized inequality, we sometimes refer to ⪯K as the nonstrict
generalized inequality.)
When K = R+, the partial ordering ⪯K is the usual ordering ≤on R, and
the strict partial ordering ≺K is the same as the usual strict ordering < on R.
So generalized inequalities include as a special case ordinary (nonstrict and strict)
inequality in R.
Example 2.14 Nonnegative orthant and componentwise inequality. The nonnegative
orthant K = Rn
+ is a proper cone. The associated generalized inequality ⪯K corre-
sponds to componentwise inequality between vectors: x ⪯K y means that xi ≤yi,
i = 1, . . . , n. The associated strict inequality corresponds to componentwise strict
inequality: x ≺K y means that xi < yi, i = 1, . . . , n.
The nonstrict and strict partial orderings associated with the nonnegative orthant
arise so frequently that we drop the subscript Rn
+; it is understood when the symbol
⪯or ≺appears between vectors.
Example 2.15 Positive semideﬁnite cone and matrix inequality. The positive semidef-
inite cone Sn
+ is a proper cone in Sn. The associated generalized inequality ⪯K is the
usual matrix inequality: X ⪯K Y means Y −X is positive semideﬁnite. The inte-
rior of Sn
+ (in Sn) consists of the positive deﬁnite matrices, so the strict generalized
inequality also agrees with the usual strict inequality between symmetric matrices:
X ≺K Y means Y −X is positive deﬁnite.
Here, too, the partial ordering arises so frequently that we drop the subscript: for
symmetric matrices we write simply X ⪯Y or X ≺Y . It is understood that the
generalized inequalities are with respect to the positive semideﬁnite cone.


## Page 18

44
2
Convex sets
Example 2.16 Cone of polynomials nonnegative on [0, 1]. Let K be deﬁned as
K = {c ∈Rn | c1 + c2t + · · · + cntn−1 ≥0 for t ∈[0, 1]},
(2.15)
i.e., K is the cone of (coeﬃcients of) polynomials of degree n−1 that are nonnegative
on the interval [0, 1]. It can be shown that K is a proper cone; its interior is the set
of coeﬃcients of polynomials that are positive on the interval [0, 1].
Two vectors c, d ∈Rn satisfy c ⪯K d if and only if
c1 + c2t + · · · + cntn−1 ≤d1 + d2t + · · · + dntn−1
for all t ∈[0, 1].
Properties of generalized inequalities
A generalized inequality ⪯K satisﬁes many properties, such as
• ⪯K is preserved under addition: if x ⪯K y and u ⪯K v, then x+u ⪯K y +v.
• ⪯K is transitive: if x ⪯K y and y ⪯K z then x ⪯K z.
• ⪯K is preserved under nonnegative scaling: if x ⪯K y and α ≥0 then
αx ⪯K αy.
• ⪯K is reﬂexive: x ⪯K x.
• ⪯K is antisymmetric: if x ⪯K y and y ⪯K x, then x = y.
• ⪯K is preserved under limits: if xi ⪯K yi for i = 1, 2, . . ., xi →x and yi →y
as i →∞, then x ⪯K y.
The corresponding strict generalized inequality ≺K satisﬁes, for example,
• if x ≺K y then x ⪯K y.
• if x ≺K y and u ⪯K v then x + u ≺K y + v.
• if x ≺K y and α > 0 then αx ≺K αy.
• x̸ ≺K x.
• if x ≺K y, then for u and v small enough, x + u ≺K y + v.
These properties are inherited from the deﬁnitions of ⪯K and ≺K, and the prop-
erties of proper cones; see exercise 2.30.


## Page 19

2.4
Generalized inequalities
45
2.4.2
Minimum and minimal elements
The notation of generalized inequality (i.e., ⪯K, ≺K) is meant to suggest the
analogy to ordinary inequality on R (i.e., ≤, <). While many properties of ordinary
inequality do hold for generalized inequalities, some important ones do not. The
most obvious diﬀerence is that ≤on R is a linear ordering: any two points are
comparable, meaning either x ≤y or y ≤x.
This property does not hold for
other generalized inequalities. One implication is that concepts like minimum and
maximum are more complicated in the context of generalized inequalities.
We
brieﬂy discuss this in this section.
We say that x ∈S is the minimum element of S (with respect to the general-
ized inequality ⪯K) if for every y ∈S we have x ⪯K y. We deﬁne the maximum
element of a set S, with respect to a generalized inequality, in a similar way. If a
set has a minimum (maximum) element, then it is unique. A related concept is
minimal element. We say that x ∈S is a minimal element of S (with respect to
the generalized inequality ⪯K) if y ∈S, y ⪯K x only if y = x. We deﬁne maxi-
mal element in a similar way. A set can have many diﬀerent minimal (maximal)
elements.
We can describe minimum and minimal elements using simple set notation. A
point x ∈S is the minimum element of S if and only if
S ⊆x + K.
Here x + K denotes all the points that are comparable to x and greater than or
equal to x (according to ⪯K). A point x ∈S is a minimal element if and only if
(x −K) ∩S = {x}.
Here x −K denotes all the points that are comparable to x and less than or equal
to x (according to ⪯K); the only point in common with S is x.
For K = R+, which induces the usual ordering on R, the concepts of minimal
and minimum are the same, and agree with the usual deﬁnition of the minimum
element of a set.
Example 2.17
Consider the cone R2
+, which induces componentwise inequality in
R2. Here we can give some simple geometric descriptions of minimal and minimum
elements. The inequality x ⪯y means y is above and to the right of x. To say that
x ∈S is the minimum element of a set S means that all other points of S lie above
and to the right. To say that x is a minimal element of a set S means that no other
point of S lies to the left and below x. This is illustrated in ﬁgure 2.17.
Example 2.18 Minimum and minimal elements of a set of symmetric matrices. We
associate with each A ∈Sn
++ an ellipsoid centered at the origin, given by
EA = {x | xT A−1x ≤1}.
We have A ⪯B if and only if EA ⊆EB.
Let v1, . . . , vk ∈Rn be given and deﬁne
S = {P ∈Sn
++ | vT
i P −1vi ≤1, i = 1, . . . , k},


## Page 20

46
2
Convex sets
x1
x2
S1
S2
Figure 2.17 Left. The set S1 has a minimum element x1 with respect to
componentwise inequality in R2. The set x1 + K is shaded lightly; x1 is
the minimum element of S1 since S1 ⊆x1 + K. Right. The point x2 is a
minimal point of S2. The set x2 −K is shown lightly shaded. The point x2
is minimal because x2 −K and S2 intersect only at x2.
which corresponds to the set of ellipsoids that contain the points v1, . . . , vk. The
set S does not have a minimum element: for any ellipsoid that contains the points
v1, . . . , vk we can ﬁnd another one that contains the points, and is not comparable
to it. An ellipsoid is minimal if it contains the points, but no smaller ellipsoid does.
Figure 2.18 shows an example in R2 with k = 2.
2.5
Separating and supporting hyperplanes
2.5.1
Separating hyperplane theorem
In this section we describe an idea that will be important later: the use of hyper-
planes or aﬃne functions to separate convex sets that do not intersect. The basic
result is the separating hyperplane theorem: Suppose C and D are nonempty dis-
joint convex sets, i.e., C ∩D = ∅. Then there exist a̸ = 0 and b such that aT x ≤b
for all x ∈C and aT x ≥b for all x ∈D. In other words, the aﬃne function aT x−b
is nonpositive on C and nonnegative on D. The hyperplane {x | aT x = b} is called
a separating hyperplane for the sets C and D, or is said to separate the sets C and
D. This is illustrated in ﬁgure 2.19.
Proof of separating hyperplane theorem
Here we consider a special case, and leave the extension of the proof to the gen-
eral case as an exercise (exercise 2.22). We assume that the (Euclidean) distance
between C and D, deﬁned as
dist(C, D) = inf{∥u −v∥2 | u ∈C, v ∈D},


## Page 21

2.5
Separating and supporting hyperplanes
47
E1
E2
E3
Figure 2.18 Three ellipsoids in R2, centered at the origin (shown as the
lower dot), that contain the points shown as the upper dots. The ellipsoid
E1 is not minimal, since there exist ellipsoids that contain the points, and
are smaller (e.g., E3). E3 is not minimal for the same reason. The ellipsoid
E2 is minimal, since no other ellipsoid (centered at the origin) contains the
points and is contained in E2.
D
C
a
aT x ≥b
aT x ≤b
Figure 2.19 The hyperplane {x | aT x = b} separates the disjoint convex sets
C and D. The aﬃne function aT x −b is nonpositive on C and nonnegative
on D.


## Page 22

48
2
Convex sets
D
C
a
d
c
Figure 2.20 Construction of a separating hyperplane between two convex
sets. The points c ∈C and d ∈D are the pair of points in the two sets that
are closest to each other. The separating hyperplane is orthogonal to, and
bisects, the line segment between c and d.
is positive, and that there exist points c ∈C and d ∈D that achieve the minimum
distance, i.e., ∥c −d∥2 = dist(C, D). (These conditions are satisﬁed, for example,
when C and D are closed and one set is bounded.)
Deﬁne
a = d −c,
b = ∥d∥2
2 −∥c∥2
2
2
.
We will show that the aﬃne function
f(x) = aT x −b = (d −c)T (x −(1/2)(d + c))
is nonpositive on C and nonnegative on D, i.e., that the hyperplane {x | aT x = b}
separates C and D. This hyperplane is perpendicular to the line segment between
c and d, and passes through its midpoint, as shown in ﬁgure 2.20.
We ﬁrst show that f is nonnegative on D. The proof that f is nonpositive on
C is similar (or follows by swapping C and D and considering −f). Suppose there
were a point u ∈D for which
f(u) = (d −c)T (u −(1/2)(d + c)) < 0.
(2.16)
We can express f(u) as
f(u) = (d −c)T (u −d + (1/2)(d −c)) = (d −c)T (u −d) + (1/2)∥d −c∥2
2.
We see that (2.16) implies (d −c)T (u −d) < 0. Now we observe that
d
dt∥d + t(u −d) −c∥2
2

t=0
= 2(d −c)T (u −d) < 0,
so for some small t > 0, with t ≤1, we have
∥d + t(u −d) −c∥2 < ∥d −c∥2,


## Page 23

2.5
Separating and supporting hyperplanes
49
i.e., the point d + t(u −d) is closer to c than d is. Since D is convex and contains
d and u, we have d + t(u −d) ∈D. But this is impossible, since d is assumed to be
the point in D that is closest to C.
Example 2.19
Separation of an aﬃne and a convex set. Suppose C is convex and
D is aﬃne, i.e., D = {Fu + g | u ∈Rm}, where F ∈Rn×m. Suppose C and D are
disjoint, so by the separating hyperplane theorem there are a̸ = 0 and b such that
aT x ≤b for all x ∈C and aT x ≥b for all x ∈D.
Now aT x ≥b for all x ∈D means aT Fu ≥b −aT g for all u ∈Rm. But a linear
function is bounded below on Rm only when it is zero, so we conclude aT F = 0 (and
hence, b ≤aT g).
Thus we conclude that there exists a̸ = 0 such that F T a = 0 and aT x ≤aT g for all
x ∈C.
Strict separation
The separating hyperplane we constructed above satisﬁes the stronger condition
that aT x < b for all x ∈C and aT x > b for all x ∈D.
This is called strict
separation of the sets C and D. Simple examples show that in general, disjoint
convex sets need not be strictly separable by a hyperplane (even when the sets are
closed; see exercise 2.23). In many special cases, however, strict separation can be
established.
Example 2.20 Strict separation of a point and a closed convex set. Let C be a closed
convex set and x0̸ ∈C. Then there exists a hyperplane that strictly separates x0
from C.
To see this, note that the two sets C and B(x0, ǫ) do not intersect for some ǫ > 0.
By the separating hyperplane theorem, there exist a̸ = 0 and b such that aT x ≤b for
x ∈C and aT x ≥b for x ∈B(x0, ǫ).
Using B(x0, ǫ) = {x0 + u | ∥u∥2 ≤ǫ}, the second condition can be expressed as
aT (x0 + u) ≥b for all ∥u∥2 ≤ǫ.
The u that minimizes the lefthand side is u = −ǫa/∥a∥2; using this value we have
aT x0 −ǫ∥a∥2 ≥b.
Therefore the aﬃne function
f(x) = aT x −b −ǫ∥a∥2/2
is negative on C and positive at x0.
As an immediate consequence we can establish a fact that we already mentioned
above: a closed convex set is the intersection of all halfspaces that contain it. Indeed,
let C be closed and convex, and let S be the intersection of all halfspaces containing
C. Obviously x ∈C ⇒x ∈S. To show the converse, suppose there exists x ∈S,
x̸ ∈C. By the strict separation result there exists a hyperplane that strictly separates
x from C, i.e., there is a halfspace containing C but not x. In other words, x̸ ∈S.


## Page 24

50
2
Convex sets
Converse separating hyperplane theorems
The converse of the separating hyperplane theorem (i.e., existence of a separating
hyperplane implies that C and D do not intersect) is not true, unless one imposes
additional constraints on C or D, even beyond convexity. As a simple counterex-
ample, consider C = D = {0} ⊆R. Here the hyperplane x = 0 separates C and
D.
By adding conditions on C and D various converse separation theorems can be
derived. As a very simple example, suppose C and D are convex sets, with C open,
and there exists an aﬃne function f that is nonpositive on C and nonnegative on
D. Then C and D are disjoint. (To see this we ﬁrst note that f must be negative
on C; for if f were zero at a point of C then f would take on positive values near
the point, which is a contradiction. But then C and D must be disjoint since f
is negative on C and nonnegative on D.) Putting this converse together with the
separating hyperplane theorem, we have the following result: any two convex sets
C and D, at least one of which is open, are disjoint if and only if there exists a
separating hyperplane.
Example 2.21
Theorem of alternatives for strict linear inequalities. We derive the
necessary and suﬃcient conditions for solvability of a system of strict linear inequal-
ities
Ax ≺b.
(2.17)
These inequalities are infeasible if and only if the (convex) sets
C = {b −Ax | x ∈Rn},
D = Rm
++ = {y ∈Rm | y ≻0}
do not intersect. The set D is open; C is an aﬃne set. Hence by the result above, C
and D are disjoint if and only if there exists a separating hyperplane, i.e., a nonzero
λ ∈Rm and µ ∈R such that λT y ≤µ on C and λT y ≥µ on D.
Each of these conditions can be simpliﬁed. The ﬁrst means λT (b −Ax) ≤µ for all x.
This implies (as in example 2.19) that AT λ = 0 and λT b ≤µ. The second inequality
means λT y ≥µ for all y ≻0. This implies µ ≤0 and λ ⪰0, λ̸ = 0.
Putting it all together, we ﬁnd that the set of strict inequalities (2.17) is infeasible if
and only if there exists λ ∈Rm such that
λ̸ = 0,
λ ⪰0,
AT λ = 0,
λT b ≤0.
(2.18)
This is also a system of linear inequalities and linear equations in the variable λ ∈Rm.
We say that (2.17) and (2.18) form a pair of alternatives: for any data A and b, exactly
one of them is solvable.
2.5.2
Supporting hyperplanes
Suppose C ⊆Rn, and x0 is a point in its boundary bd C, i.e.,
x0 ∈bd C = cl C \ int C.
If a̸ = 0 satisﬁes aT x ≤aT x0 for all x ∈C, then the hyperplane {x | aT x = aT x0}
is called a supporting hyperplane to C at the point x0. This is equivalent to saying


## Page 25

2.6
Dual cones and generalized inequalities
51
C
a
x0
Figure 2.21 The hyperplane {x | aT x = aT x0} supports C at x0.
that the point x0 and the set C are separated by the hyperplane {x | aT x = aT x0}.
The geometric interpretation is that the hyperplane {x | aT x = aT x0} is tangent
to C at x0, and the halfspace {x | aT x ≤aT x0} contains C. This is illustrated in
ﬁgure 2.21.
A basic result, called the supporting hyperplane theorem, states that for any
nonempty convex set C, and any x0 ∈bd C, there exists a supporting hyperplane to
C at x0. The supporting hyperplane theorem is readily proved from the separating
hyperplane theorem. We distinguish two cases. If the interior of C is nonempty,
the result follows immediately by applying the separating hyperplane theorem to
the sets {x0} and int C. If the interior of C is empty, then C must lie in an aﬃne
set of dimension less than n, and any hyperplane containing that aﬃne set contains
C and x0, and is a (trivial) supporting hyperplane.
There is also a partial converse of the supporting hyperplane theorem: If a set
is closed, has nonempty interior, and has a supporting hyperplane at every point
in its boundary, then it is convex. (See exercise 2.27.)
2.6
Dual cones and generalized inequalities
2.6.1
Dual cones
Let K be a cone. The set
K∗= {y | xT y ≥0 for all x ∈K}
(2.19)
is called the dual cone of K. As the name suggests, K∗is a cone, and is always
convex, even when the original cone K is not (see exercise 2.31).
Geometrically, y ∈K∗if and only if −y is the normal of a hyperplane that
supports K at the origin. This is illustrated in ﬁgure 2.22.
Example 2.22 Subspace. The dual cone of a subspace V ⊆Rn (which is a cone) is
its orthogonal complement V ⊥= {y | vT y = 0 for all v ∈V }.


## Page 26

52
2
Convex sets
K
K
y
z
Figure 2.22 Left. The halfspace with inward normal y contains the cone K,
so y ∈K∗. Right. The halfspace with inward normal z does not contain K,
so z̸ ∈K∗.
Example 2.23 Nonnegative orthant. The cone Rn
+ is its own dual:
xT y ≥0 for all x ⪰0 ⇐⇒y ⪰0.
We call such a cone self-dual.
Example 2.24
Positive semideﬁnite cone. On the set of symmetric n × n matrices
Sn, we use the standard inner product tr(XY ) = Pn
i,j=1 XijYij (see §A.1.1). The
positive semideﬁnite cone Sn
+ is self-dual, i.e., for X, Y ∈Sn,
tr(XY ) ≥0 for all X ⪰0 ⇐⇒Y ⪰0.
We will establish this fact.
Suppose Y̸ ∈Sn
+. Then there exists q ∈Rn with
qT Y q = tr(qqT Y ) < 0.
Hence the positive semideﬁnite matrix X = qqT satisﬁes tr(XY ) < 0; it follows that
Y̸ ∈(Sn
+)∗.
Now suppose X, Y ∈Sn
+. We can express X in terms of its eigenvalue decomposition
as X = Pn
i=1 λiqiqT
i , where (the eigenvalues) λi ≥0, i = 1, . . . , n. Then we have
tr(Y X) = tr
 
Y
n
X
i=1
λiqiqT
i
!
=
n
X
i=1
λiqT
i Y qi ≥0.
This shows that Y ∈(Sn
+)∗.
Example 2.25
Dual of a norm cone. Let ∥· ∥be a norm on Rn. The dual of the
associated cone K = {(x, t) ∈Rn+1 | ∥x∥≤t} is the cone deﬁned by the dual norm,
i.e.,
K∗= {(u, v) ∈Rn+1 | ∥u∥∗≤v},


## Page 27

2.6
Dual cones and generalized inequalities
53
where the dual norm is given by ∥u∥∗= sup{uT x | ∥x∥≤1} (see (A.1.6)).
To prove the result we have to show that
xT u + tv ≥0 whenever ∥x∥≤t ⇐⇒∥u∥∗≤v.
(2.20)
Let us start by showing that the righthand condition on (u, v) implies the lefthand
condition. Suppose ∥u∥∗≤v, and ∥x∥≤t for some t > 0. (If t = 0, x must be zero,
so obviously uT x + vt ≥0.) Applying the deﬁnition of the dual norm, and the fact
that ∥−x/t∥≤1, we have
uT (−x/t) ≤∥u∥∗≤v,
and therefore uT x + vt ≥0.
Next we show that the lefthand condition in (2.20) implies the righthand condition
in (2.20). Suppose ∥u∥∗> v, i.e., that the righthand condition does not hold. Then
by the deﬁnition of the dual norm, there exists an x with ∥x∥≤1 and xT u > v.
Taking t = 1, we have
uT (−x) + v < 0,
which contradicts the lefthand condition in (2.20).
Dual cones satisfy several properties, such as:
• K∗is closed and convex.
• K1 ⊆K2 implies K∗
2 ⊆K∗
1.
• If K has nonempty interior, then K∗is pointed.
• If the closure of K is pointed then K∗has nonempty interior.
• K∗∗is the closure of the convex hull of K. (Hence if K is convex and closed,
K∗∗= K.)
(See exercise 2.31.) These properties show that if K is a proper cone, then so is its
dual K∗, and moreover, that K∗∗= K.
2.6.2
Dual generalized inequalities
Now suppose that the convex cone K is proper, so it induces a generalized inequality
⪯K. Then its dual cone K∗is also proper, and therefore induces a generalized
inequality. We refer to the generalized inequality ⪯K∗as the dual of the generalized
inequality ⪯K.
Some important properties relating a generalized inequality and its dual are:
• x ⪯K y if and only if λT x ≤λT y for all λ ⪰K∗0.
• x ≺K y if and only if λT x < λT y for all λ ⪰K∗0, λ̸ = 0.
Since K = K∗∗, the dual generalized inequality associated with ⪯K∗is ⪯K, so
these properties hold if the generalized inequality and its dual are swapped. As a
speciﬁc example, we have λ ⪯K∗µ if and only if λT x ≤µT x for all x ⪰K 0.


## Page 28

54
2
Convex sets
Example 2.26 Theorem of alternatives for linear strict generalized inequalities. Sup-
pose K ⊆Rm is a proper cone. Consider the strict generalized inequality
Ax ≺K b,
(2.21)
where x ∈Rn.
We will derive a theorem of alternatives for this inequality. Suppose it is infeasible,
i.e., the aﬃne set {b −Ax | x ∈Rn} does not intersect the open convex set int K.
Then there is a separating hyperplane, i.e., a nonzero λ ∈Rm and µ ∈R such that
λT (b −Ax) ≤µ for all x, and λT y ≥µ for all y ∈int K. The ﬁrst condition implies
AT λ = 0 and λT b ≤µ. The second condition implies λT y ≥µ for all y ∈K, which
can only happen if λ ∈K∗and µ ≤0.
Putting it all together we ﬁnd that if (2.21) is infeasible, then there exists λ such that
λ̸ = 0,
λ ⪰K∗0,
AT λ = 0,
λT b ≤0.
(2.22)
Now we show the converse: if (2.22) holds, then the inequality system (2.21) cannot
be feasible. Suppose that both inequality systems hold. Then we have λT (b −Ax) >
0, since λ̸ = 0, λ ⪰K∗0, and b −Ax ≻K 0.
But using AT λ = 0 we ﬁnd that
λT (b −Ax) = λT b ≤0, which is a contradiction.
Thus, the inequality systems (2.21) and (2.22) are alternatives: for any data A, b,
exactly one of them is feasible. (This generalizes the alternatives (2.17), (2.18) for
the special case K = Rm
+ .)
2.6.3
Minimum and minimal elements via dual inequalities
We can use dual generalized inequalities to characterize minimum and minimal
elements of a (possibly nonconvex) set S ⊆Rm with respect to the generalized
inequality induced by a proper cone K.
Dual characterization of minimum element
We ﬁrst consider a characterization of the minimum element: x is the minimum
element of S, with respect to the generalized inequality ⪯K, if and only if for all
λ ≻K∗0, x is the unique minimizer of λT z over z ∈S. Geometrically, this means
that for any λ ≻K∗0, the hyperplane
{z | λT (z −x) = 0}
is a strict supporting hyperplane to S at x. (By strict supporting hyperplane, we
mean that the hyperplane intersects S only at the point x.) Note that convexity
of the set S is not required. This is illustrated in ﬁgure 2.23.
To show this result, suppose x is the minimum element of S, i.e., x ⪯K z for
all z ∈S, and let λ ≻K∗0. Let z ∈S, z̸ = x. Since x is the minimum element of
S, we have z −x ⪰K 0. From λ ≻K∗0 and z −x ⪰K 0, z −x̸ = 0, we conclude
λT (z −x) > 0. Since z is an arbitrary element of S, not equal to x, this shows
that x is the unique minimizer of λT z over z ∈S. Conversely, suppose that for all
λ ≻K∗0, x is the unique minimizer of λT z over z ∈S, but x is not the minimum


## Page 29

2.6
Dual cones and generalized inequalities
55
x
S
Figure 2.23 Dual characterization of minimum element. The point x is the
minimum element of the set S with respect to R2
+. This is equivalent to:
for every λ ≻0, the hyperplane {z | λT (z −x) = 0} strictly supports S at
x, i.e., contains S on one side, and touches it only at x.
element of S. Then there exists z ∈S with z̸ ⪰K x. Since z −x̸ ⪰K 0, there exists
˜λ ⪰K∗0 with ˜λT (z−x) < 0. Hence λT (z−x) < 0 for λ ≻K∗0 in the neighborhood
of ˜λ. This contradicts the assumption that x is the unique minimizer of λT z over
S.
Dual characterization of minimal elements
We now turn to a similar characterization of minimal elements. Here there is a gap
between the necessary and suﬃcient conditions. If λ ≻K∗0 and x minimizes λT z
over z ∈S, then x is minimal. This is illustrated in ﬁgure 2.24.
To show this, suppose that λ ≻K∗0, and x minimizes λT z over S, but x is not
minimal, i.e., there exists a z ∈S, z̸ = x, and z ⪯K x. Then λT (x −z) > 0, which
contradicts our assumption that x is the minimizer of λT z over S.
The converse is in general false: a point x can be minimal in S, but not a
minimizer of λT z over z ∈S, for any λ, as shown in ﬁgure 2.25.
This ﬁgure
suggests that convexity plays an important role in the converse, which is correct.
Provided the set S is convex, we can say that for any minimal element x there
exists a nonzero λ ⪰K∗0 such that x minimizes λT z over z ∈S.
To show this, suppose x is minimal, which means that ((x −K) \ {x}) ∩S = ∅.
Applying the separating hyperplane theorem to the convex sets (x −K) \ {x} and
S, we conclude that there is a λ̸ = 0 and µ such that λT (x −y) ≤µ for all y ∈K,
and λT z ≥µ for all z ∈S. From the ﬁrst inequality we conclude λ ⪰K∗0. Since
x ∈S and x ∈x −K, we have λT x = µ, so the second inequality implies that µ
is the minimum value of λT z over S. Therefore, x is a minimizer of λT z over S,
where λ̸ = 0, λ ⪰K∗0.
This converse theorem cannot be strengthened to λ ≻K∗0. Examples show
that a point x can be a minimal point of a convex set S, but not a minimizer of


## Page 30

56
2
Convex sets
S
x1
x2
λ1
λ2
Figure 2.24 A set S ⊆R2. Its set of minimal points, with respect to R2
+, is
shown as the darker section of its (lower, left) boundary. The minimizer of
λT
1 z over S is x1, and is minimal since λ1 ≻0. The minimizer of λT
2 z over
S is x2, which is another minimal point of S, since λ2 ≻0.
S
x
Figure 2.25 The point x is a minimal element of S ⊆R2 with respect to
R2
+. However there exists no λ for which x minimizes λT z over z ∈S.


## Page 31

2.6
Dual cones and generalized inequalities
57
S1
S2
x1
x2
Figure 2.26 Left. The point x1 ∈S1 is minimal, but is not a minimizer of
λT z over S1 for any λ ≻0. (It does, however, minimize λT z over z ∈S1 for
λ = (1, 0).) Right. The point x2 ∈S2 is not minimal, but it does minimize
λT z over z ∈S2 for λ = (0, 1) ⪰0.
λT z over z ∈S for any λ ≻K∗0. (See ﬁgure 2.26, left.) Nor is it true that any
minimizer of λT z over z ∈S, with λ ⪰K∗0, is minimal (see ﬁgure 2.26, right.)
Example 2.27
Pareto optimal production frontier.
We consider a product which
requires n resources (such as labor, electricity, natural gas, water) to manufacture.
The product can be manufactured or produced in many ways. With each production
method, we associate a resource vector x ∈Rn, where xi denotes the amount of
resource i consumed by the method to manufacture the product. We assume that xi ≥
0 (i.e., resources are consumed by the production methods) and that the resources
are valuable (so using less of any resource is preferred).
The production set P ⊆Rn is deﬁned as the set of all resource vectors x that
correspond to some production method.
Production methods with resource vectors that are minimal elements of P, with
respect to componentwise inequality, are called Pareto optimal or eﬃcient. The set
of minimal elements of P is called the eﬃcient production frontier.
We can give a simple interpretation of Pareto optimality. We say that one production
method, with resource vector x, is better than another, with resource vector y, if
xi ≤yi for all i, and for some i, xi < yi. In other words, one production method
is better than another if it uses no more of each resource than another method, and
for at least one resource, actually uses less. This corresponds to x ⪯y, x̸ = y. Then
we can say: A production method is Pareto optimal or eﬃcient if there is no better
production method.
We can ﬁnd Pareto optimal production methods (i.e., minimal resource vectors) by
minimizing
λT x = λ1x1 + · · · + λnxn
over the set P of production vectors, using any λ that satisﬁes λ ≻0.
Here the vector λ has a simple interpretation: λi is the price of resource i.
By
minimizing λT x over P we are ﬁnding the overall cheapest production method (for
the resource prices λi). As long as the prices are positive, the resulting production
method is guaranteed to be eﬃcient.
These ideas are illustrated in ﬁgure 2.27.


## Page 32

58
2
Convex sets
x4
x2
x1
x5
x3
λ
P
labor
fuel
Figure 2.27 The production set P, for a product that requires labor and
fuel to produce, is shown shaded. The two dark curves show the eﬃcient
production frontier. The points x1, x2 and x3 are eﬃcient. The points x4
and x5 are not (since in particular, x2 corresponds to a production method
that uses no more fuel, and less labor). The point x1 is also the minimum
cost production method for the price vector λ (which is positive). The point
x2 is eﬃcient, but cannot be found by minimizing the total cost λT x for any
price vector λ ⪰0.


## Page 33

Bibliography
59
Bibliography
Minkowski is generally credited with the ﬁrst systematic study of convex sets, and the
introduction of fundamental concepts such as supporting hyperplanes and the supporting
hyperplane theorem, the Minkowski distance function (exercise 3.34), extreme points of
a convex set, and many others.
Some well known early surveys are Bonnesen and Fenchel [BF48], Eggleston [Egg58], Klee
[Kle63], and Valentine [Val64]. More recent books devoted to the geometry of convex sets
include Lay [Lay82] and Webster [Web94]. Klee [Kle71], Fenchel [Fen83], Tikhomorov
[Tik90], and Berger [Ber90] give very readable overviews of the history of convexity and
its applications throughout mathematics.
Linear inequalities and polyhedral sets are studied extensively in connection with the lin-
ear programming problem, for which we give references at the end of chapter 4. Some
landmark publications in the history of linear inequalities and linear programming are
Motzkin [Mot33], von Neumann and Morgenstern [vNM53], Kantorovich [Kan60], Koop-
mans [Koo51], and Dantzig [Dan63]. Dantzig [Dan63, Chapter 2] includes an historical
survey of linear inequalities, up to around 1963.
Generalized inequalities were introduced in nonlinear optimization during the 1960s (see
Luenberger [Lue69, §8.2] and Isii [Isi64]), and are used extensively in cone programming
(see the references in chapter 4). Bellman and Fan [BF63] is an early paper on sets of
generalized linear inequalities (with respect to the positive semideﬁnite cone).
For extensions and a proof of the separating hyperplane theorem we refer the reader
to Rockafellar [Roc70, part III], and Hiriart-Urruty and Lemar´echal [HUL93, volume
1, §III4].
Dantzig [Dan63, page 21] attributes the term theorem of the alternative to
von Neumann and Morgenstern [vNM53, page 138]. For more references on theorems of
alternatives, see chapter 5.
The terminology of example 2.27 (including Pareto optimality, eﬃcient production, and
the price interpretation of λ) is discussed in detail by Luenberger [Lue95].
Convex geometry plays a prominent role in the classical theory of moments (Krein and
Nudelman [KN77], Karlin and Studden [KS66]). A famous example is the duality between
the cone of nonnegative polynomials and the cone of power moments; see exercise 2.37.


## Page 34

60
2
Convex sets
Exercises
Deﬁnition of convexity
2.1 Let C ⊆Rn be a convex set, with x1, . . . , xk ∈C, and let θ1, . . . , θk ∈R satisfy θi ≥0,
θ1 + · · · + θk = 1. Show that θ1x1 + · · · + θkxk ∈C. (The deﬁnition of convexity is that
this holds for k = 2; you must show it for arbitrary k.) Hint. Use induction on k.
2.2 Show that a set is convex if and only if its intersection with any line is convex. Show that
a set is aﬃne if and only if its intersection with any line is aﬃne.
2.3 Midpoint convexity. A set C is midpoint convex if whenever two points a, b are in C, the
average or midpoint (a + b)/2 is in C. Obviously a convex set is midpoint convex. It can
be proved that under mild conditions midpoint convexity implies convexity. As a simple
case, prove that if C is closed and midpoint convex, then C is convex.
2.4 Show that the convex hull of a set S is the intersection of all convex sets that contain S.
(The same method can be used to show that the conic, or aﬃne, or linear hull of a set S
is the intersection of all conic sets, or aﬃne sets, or subspaces that contain S.)
Examples
2.5 What is the distance between two parallel hyperplanes {x ∈Rn | aT x = b1} and {x ∈
Rn | aT x = b2}?
2.6 When does one halfspace contain another? Give conditions under which
{x | aT x ≤b} ⊆{x | ˜aT x ≤˜b}
(where a̸ = 0, ˜a̸ = 0). Also ﬁnd the conditions under which the two halfspaces are equal.
2.7 Voronoi description of halfspace. Let a and b be distinct points in Rn. Show that the set
of all points that are closer (in Euclidean norm) to a than b, i.e., {x | ∥x−a∥2 ≤∥x−b∥2},
is a halfspace. Describe it explicitly as an inequality of the form cT x ≤d. Draw a picture.
2.8 Which of the following sets S are polyhedra?
If possible, express S in the form S =
{x | Ax ⪯b, Fx = g}.
(a) S = {y1a1 + y2a2 | −1 ≤y1 ≤1, −1 ≤y2 ≤1}, where a1, a2 ∈Rn.
(b) S = {x ∈Rn | x ⪰0, 1T x = 1, Pn
i=1 xiai = b1, Pn
i=1 xia2
i = b2}, where
a1, . . . , an ∈R and b1, b2 ∈R.
(c) S = {x ∈Rn | x ⪰0, xT y ≤1 for all y with ∥y∥2 = 1}.
(d) S = {x ∈Rn | x ⪰0, xT y ≤1 for all y with Pn
i=1 |yi| = 1}.
2.9 Voronoi sets and polyhedral decomposition. Let x0, . . . , xK ∈Rn be distinct. Consider
the set of points that are closer (in Euclidean norm) to x0 than the other xi, i.e.,
V = {x ∈Rn | ∥x −x0∥2 ≤∥x −xi∥2, i = 1, . . . , K}.
V is called the Voronoi region around x0 with respect to x1, . . . , xK.
(a) Show that V is a polyhedron. Express V in the form V = {x | Ax ⪯b}.
(b) Conversely, given a polyhedron P with nonempty interior, show how to ﬁnd x0, . . . , xK
so that the polyhedron is the Voronoi region of x0 with respect to x1, . . . , xK.
(c) We can also consider the sets
Vk = {x ∈Rn | ∥x −xk∥2 ≤∥x −xi∥2, i̸ = k}.
The set Vk consists of points in Rn for which the closest point in the set {x0, . . . , xK}
is xk.


## Page 35

Exercises
61
The sets V0, . . . , VK give a polyhedral decomposition of Rn. More precisely, the sets
Vk are polyhedra with nonempty interior, SK
k=0 Vk = Rn, and int Vi ∩int Vj = ∅
for i̸ = j, i.e., Vi and Vj intersect at most along a boundary.
Suppose that P1, . . . , Pm are polyhedra with nonempty interior such that Sm
i=1 Pi =
Rn, int Pi ∩int Pj = ∅for i̸ = j. Can this polyhedral decomposition of Rn be
described as the Voronoi regions generated by an appropriate set of points?
2.10 Solution set of a quadratic inequality. Let C ⊆Rn be the solution set of a quadratic
inequality,
C = {x ∈Rn | xT Ax + bT x + c ≤0},
with A ∈Sn, b ∈Rn, and c ∈R.
(a) Show that C is convex if A ⪰0.
(b) Show that the intersection of C and the hyperplane deﬁned by gT x + h = 0 (where
g̸ = 0) is convex if A + λggT ⪰0 for some λ ∈R.
Are the converses of these statements true?
2.11 Hyperbolic sets. Show that the hyperbolic set {x ∈R2
+ | x1x2 ≥1} is convex. As a
generalization, show that {x ∈Rn
+ | Qn
i=1 xi ≥1} is convex.
Hint.
If a, b ≥0 and
0 ≤θ ≤1, then aθb1−θ ≤θa + (1 −θ)b; see §3.1.9.
2.12 Which of the following sets are convex?
(a) A slab, i.e., a set of the form {x ∈Rn | α ≤aT x ≤β}.
(b) A rectangle, i.e., a set of the form {x ∈Rn | αi ≤xi ≤βi, i = 1, . . . , n}. A rectangle
is sometimes called a hyperrectangle when n > 2.
(c) A wedge, i.e., {x ∈Rn | aT
1 x ≤b1, aT
2 x ≤b2}.
(d) The set of points closer to a given point than a given set, i.e.,
{x | ∥x −x0∥2 ≤∥x −y∥2 for all y ∈S}
where S ⊆Rn.
(e) The set of points closer to one set than another, i.e.,
{x | dist(x, S) ≤dist(x, T)},
where S, T ⊆Rn, and
dist(x, S) = inf{∥x −z∥2 | z ∈S}.
(f) [HUL93, volume 1, page 93] The set {x | x + S2 ⊆S1}, where S1, S2 ⊆Rn with S1
convex.
(g) The set of points whose distance to a does not exceed a ﬁxed fraction θ of the
distance to b, i.e., the set {x | ∥x −a∥2 ≤θ∥x −b∥2}. You can assume a̸ = b and
0 ≤θ ≤1.
2.13 Conic hull of outer products.
Consider the set of rank-k outer products, deﬁned as
{XXT | X ∈Rn×k, rank X = k}. Describe its conic hull in simple terms.
2.14 Expanded and restricted sets.
Let S ⊆Rn, and let ∥· ∥be a norm on Rn.
(a) For a ≥0 we deﬁne Sa as {x | dist(x, S) ≤a}, where dist(x, S) = infy∈S ∥x −y∥.
We refer to Sa as S expanded or extended by a. Show that if S is convex, then Sa
is convex.
(b) For a ≥0 we deﬁne S−a = {x | B(x, a) ⊆S}, where B(x, a) is the ball (in the norm
∥· ∥), centered at x, with radius a. We refer to S−a as S shrunk or restricted by a,
since S−a consists of all points that are at least a distance a from Rn\S. Show that
if S is convex, then S−a is convex.


## Page 36

62
2
Convex sets
2.15 Some sets of probability distributions.
Let x be a real-valued random variable with
prob(x = ai) = pi, i = 1, . . . , n, where a1 < a2 < · · · < an. Of course p ∈Rn lies
in the standard probability simplex P = {p | 1T p = 1, p ⪰0}. Which of the following
conditions are convex in p? (That is, for which of the following conditions is the set of
p ∈P that satisfy the condition convex?)
(a) α ≤E f(x) ≤β, where E f(x) is the expected value of f(x), i.e., E f(x) =
Pn
i=1 pif(ai). (The function f : R →R is given.)
(b) prob(x > α) ≤β.
(c) E |x3| ≤α E |x|.
(d) E x2 ≤α.
(e) E x2 ≥α.
(f) var(x) ≤α, where var(x) = E(x −E x)2 is the variance of x.
(g) var(x) ≥α.
(h) quartile(x) ≥α, where quartile(x) = inf{β | prob(x ≤β) ≥0.25}.
(i) quartile(x) ≤α.
Operations that preserve convexity
2.16 Show that if S1 and S2 are convex sets in Rm+n, then so is their partial sum
S = {(x, y1 + y2) | x ∈Rm, y1, y2 ∈Rn, (x, y1) ∈S1, (x, y2) ∈S2}.
2.17 Image of polyhedral sets under perspective function. In this problem we study the image
of hyperplanes, halfspaces, and polyhedra under the perspective function P(x, t) = x/t,
with dom P = Rn × R++. For each of the following sets C, give a simple description of
P(C) = {v/t | (v, t) ∈C, t > 0}.
(a) The polyhedron C = conv{(v1, t1), . . . , (vK, tK)} where vi ∈Rn and ti > 0.
(b) The hyperplane C = {(v, t) | f T v + gt = h} (with f and g not both zero).
(c) The halfspace C = {(v, t) | f T v + gt ≤h} (with f and g not both zero).
(d) The polyhedron C = {(v, t) | Fv + gt ⪯h}.
2.18 Invertible linear-fractional functions. Let f : Rn →Rn be the linear-fractional function
f(x) = (Ax + b)/(cT x + d),
dom f = {x | cT x + d > 0}.
Suppose the matrix
Q =

A
b
cT
d

is nonsingular. Show that f is invertible and that f −1 is a linear-fractional mapping.
Give an explicit expression for f −1 and its domain in terms of A, b, c, and d. Hint. It
may be easier to express f −1 in terms of Q.
2.19 Linear-fractional functions and convex sets. Let f : Rm →Rn be the linear-fractional
function
f(x) = (Ax + b)/(cT x + d),
dom f = {x | cT x + d > 0}.
In this problem we study the inverse image of a convex set C under f, i.e.,
f −1(C) = {x ∈dom f | f(x) ∈C}.
For each of the following sets C ⊆Rn, give a simple description of f −1(C).
(a) The halfspace C = {y | gT y ≤h} (with g̸ = 0).
(b) The polyhedron C = {y | Gy ⪯h}.
(c) The ellipsoid {y | yT P −1y ≤1} (where P ∈Sn
++).
(d) The solution set of a linear matrix inequality, C = {y | y1A1 + · · · + ynAn ⪯B},
where A1, . . . , An, B ∈Sp.


## Page 37

Exercises
63
Separation theorems and supporting hyperplanes
2.20 Strictly positive solution of linear equations. Suppose A ∈Rm×n, b ∈Rm, with b ∈R(A).
Show that there exists an x satisfying
x ≻0,
Ax = b
if and only if there exists no λ with
AT λ ⪰0,
AT λ̸ = 0,
bT λ ≤0.
Hint.
First prove the following fact from linear algebra: cT x = d for all x satisfying
Ax = b if and only if there is a vector λ such that c = AT λ, d = bT λ.
2.21 The set of separating hyperplanes. Suppose that C and D are disjoint subsets of Rn.
Consider the set of (a, b) ∈Rn+1 for which aT x ≤b for all x ∈C, and aT x ≥b for all
x ∈D. Show that this set is a convex cone (which is the singleton {0} if there is no
hyperplane that separates C and D).
2.22 Finish the proof of the separating hyperplane theorem in §2.5.1: Show that a separating
hyperplane exists for two disjoint convex sets C and D. You can use the result proved
in §2.5.1, i.e., that a separating hyperplane exists when there exist points in the two sets
whose distance is equal to the distance between the two sets.
Hint. If C and D are disjoint convex sets, then the set {x −y | x ∈C, y ∈D} is convex
and does not contain the origin.
2.23 Give an example of two closed convex sets that are disjoint but cannot be strictly sepa-
rated.
2.24 Supporting hyperplanes.
(a) Express the closed convex set {x ∈R2
+ | x1x2 ≥1} as an intersection of halfspaces.
(b) Let C = {x ∈Rn | ∥x∥∞≤1}, the ℓ∞-norm unit ball in Rn, and let ˆx be a point
in the boundary of C. Identify the supporting hyperplanes of C at ˆx explicitly.
2.25 Inner and outer polyhedral approximations. Let C ⊆Rn be a closed convex set, and
suppose that x1, . . . , xK are on the boundary of C. Suppose that for each i, aT
i (x−xi) = 0
deﬁnes a supporting hyperplane for C at xi, i.e., C ⊆{x | aT
i (x −xi) ≤0}. Consider the
two polyhedra
Pinner = conv{x1, . . . , xK},
Pouter = {x | aT
i (x −xi) ≤0, i = 1, . . . , K}.
Show that Pinner ⊆C ⊆Pouter. Draw a picture illustrating this.
2.26 Support function. The support function of a set C ⊆Rn is deﬁned as
SC(y) = sup{yT x | x ∈C}.
(We allow SC(y) to take on the value +∞.) Suppose that C and D are closed convex sets
in Rn. Show that C = D if and only if their support functions are equal.
2.27 Converse supporting hyperplane theorem.
Suppose the set C is closed, has nonempty
interior, and has a supporting hyperplane at every point in its boundary. Show that C is
convex.
Convex cones and generalized inequalities
2.28 Positive semideﬁnite cone for n = 1, 2, 3. Give an explicit description of the positive
semideﬁnite cone Sn
+, in terms of the matrix coeﬃcients and ordinary inequalities, for
n = 1, 2, 3. To describe a general element of Sn, for n = 1, 2, 3, use the notation
x1,

x1
x2
x2
x3

,
" x1
x2
x3
x2
x4
x5
x3
x5
x6
#
.


## Page 38

64
2
Convex sets
2.29 Cones in R2. Suppose K ⊆R2 is a closed convex cone.
(a) Give a simple description of K in terms of the polar coordinates of its elements
(x = r(cos φ, sin φ) with r ≥0).
(b) Give a simple description of K∗, and draw a plot illustrating the relation between
K and K∗.
(c) When is K pointed?
(d) When is K proper (hence, deﬁnes a generalized inequality)? Draw a plot illustrating
what x ⪯K y means when K is proper.
2.30 Properties of generalized inequalities. Prove the properties of (nonstrict and strict) gen-
eralized inequalities listed in §2.4.1.
2.31 Properties of dual cones. Let K∗be the dual cone of a convex cone K, as deﬁned in (2.19).
Prove the following.
(a) K∗is indeed a convex cone.
(b) K1 ⊆K2 implies K∗
2 ⊆K∗
1.
(c) K∗is closed.
(d) The interior of K∗is given by int K∗= {y | yT x > 0 for all x ∈cl K}.
(e) If K has nonempty interior then K∗is pointed.
(f) K∗∗is the closure of K. (Hence if K is closed, K∗∗= K.)
(g) If the closure of K is pointed then K∗has nonempty interior.
2.32 Find the dual cone of {Ax | x ⪰0}, where A ∈Rm×n.
2.33 The monotone nonnegative cone. We deﬁne the monotone nonnegative cone as
Km+ = {x ∈Rn | x1 ≥x2 ≥· · · ≥xn ≥0}.
i.e., all nonnegative vectors with components sorted in nonincreasing order.
(a) Show that Km+ is a proper cone.
(b) Find the dual cone K∗
m+. Hint. Use the identity
n
X
i=1
xiyi
=
(x1 −x2)y1 + (x2 −x3)(y1 + y2) + (x3 −x4)(y1 + y2 + y3) + · · ·
+ (xn−1 −xn)(y1 + · · · + yn−1) + xn(y1 + · · · + yn).
2.34 The lexicographic cone and ordering. The lexicographic cone is deﬁned as
Klex = {0} ∪{x ∈Rn | x1 = · · · = xk = 0, xk+1 > 0, for some k, 0 ≤k < n},
i.e., all vectors whose ﬁrst nonzero coeﬃcient (if any) is positive.
(a) Verify that Klex is a cone, but not a proper cone.
(b) We deﬁne the lexicographic ordering on Rn as follows: x ≤lex y if and only if
y −x ∈Klex. (Since Klex is not a proper cone, the lexicographic ordering is not a
generalized inequality.) Show that the lexicographic ordering is a linear ordering:
for any x, y ∈Rn, either x ≤lex y or y ≤lex x. Therefore any set of vectors can be
sorted with respect to the lexicographic cone, which yields the familiar sorting used
in dictionaries.
(c) Find K∗
lex.
2.35 Copositive matrices. A matrix X ∈Sn is called copositive if zT Xz ≥0 for all z ⪰0.
Verify that the set of copositive matrices is a proper cone. Find its dual cone.


## Page 39

Exercises
65
2.36 Euclidean distance matrices. Let x1, . . . , xn ∈Rk. The matrix D ∈Sn deﬁned by Dij =
∥xi −xj∥2
2 is called a Euclidean distance matrix. It satisﬁes some obvious properties such
as Dij = Dji, Dii = 0, Dij ≥0, and (from the triangle inequality) D1/2
ik
≤D1/2
ij
+ D1/2
jk .
We now pose the question: When is a matrix D ∈Sn a Euclidean distance matrix (for
some points in Rk, for some k)? A famous result answers this question: D ∈Sn is a
Euclidean distance matrix if and only if Dii = 0 and xT Dx ≤0 for all x with 1T x = 0.
(See §8.3.3.)
Show that the set of Euclidean distance matrices is a convex cone.
2.37 Nonnegative polynomials and Hankel LMIs. Let Kpol be the set of (coeﬃcients of) non-
negative polynomials of degree 2k on R:
Kpol = {x ∈R2k+1 | x1 + x2t + x3t2 + · · · + x2k+1t2k ≥0 for all t ∈R}.
(a) Show that Kpol is a proper cone.
(b) A basic result states that a polynomial of degree 2k is nonnegative on R if and only
if it can be expressed as the sum of squares of two polynomials of degree k or less.
In other words, x ∈Kpol if and only if the polynomial
p(t) = x1 + x2t + x3t2 + · · · + x2k+1t2k
can be expressed as
p(t) = r(t)2 + s(t)2,
where r and s are polynomials of degree k.
Use this result to show that
Kpol =
(
x ∈R2k+1
 xi =
X
m+n=i+1
Ymn for some Y ∈Sk+1
+
)
.
In other words, p(t) = x1 + x2t + x3t2 + · · · + x2k+1t2k is nonnegative if and only if
there exists a matrix Y ∈Sk+1
+
such that
x1
=
Y11
x2
=
Y12 + Y21
x3
=
Y13 + Y22 + Y31
...
x2k+1
=
Yk+1,k+1.
(c) Show that K∗
pol = Khan where
Khan = {z ∈R2k+1 | H(z) ⪰0}
and
H(z) =


z1
z2
z3
· · ·
zk
zk+1
z2
z3
z4
· · ·
zk+1
zk+2
z3
z4
z5
· · ·
zk+2
zk+4
...
...
...
...
...
...
zk
zk+1
zk+2
· · ·
z2k−1
z2k
zk+1
zk+2
zk+3
· · ·
z2k
z2k+1


.
(This is the Hankel matrix with coeﬃcients z1, . . . , z2k+1.)


## Page 40

66
2
Convex sets
(d) Let Kmom be the conic hull of the set of all vectors of the form (1, t, t2, . . . , t2k),
where t ∈R. Show that y ∈Kmom if and only if y1 ≥0 and
y = y1(1, E u, E u2, . . . , E u2k)
for some random variable u. In other words, the elements of Kmom are nonnegative
multiples of the moment vectors of all possible distributions on R. Show that Kpol =
K∗
mom.
(e) Combining the results of (c) and (d), conclude that Khan = cl Kmom.
As an example illustrating the relation between Kmom and Khan, take k = 2 and
z = (1, 0, 0, 0, 1). Show that z ∈Khan, z̸ ∈Kmom. Find an explicit sequence of
points in Kmom which converge to z.
2.38 [Roc70, pages 15, 61] Convex cones constructed from sets.
(a) The barrier cone of a set C is deﬁned as the set of all vectors y such that yT x is
bounded above over x ∈C. In other words, a nonzero vector y is in the barrier cone
if and only if it is the normal vector of a halfspace {x | yT x ≤α} that contains C.
Verify that the barrier cone is a convex cone (with no assumptions on C).
(b) The recession cone (also called asymptotic cone) of a set C is deﬁned as the set of
all vectors y such that for each x ∈C, x −ty ∈C for all t ≥0. Show that the
recession cone of a convex set is a convex cone. Show that if C is nonempty, closed,
and convex, then the recession cone of C is the dual of the barrier cone.
(c) The normal cone of a set C at a boundary point x0 is the set of all vectors y such
that yT (x −x0) ≤0 for all x ∈C (i.e., the set of vectors that deﬁne a supporting
hyperplane to C at x0).
Show that the normal cone is a convex cone (with no
assumptions on C). Give a simple description of the normal cone of a polyhedron
{x | Ax ⪯b} at a point in its boundary.
2.39 Separation of cones. Let K and ˜K be two convex cones whose interiors are nonempty and
disjoint. Show that there is a nonzero y such that y ∈K∗, −y ∈˜K∗.
