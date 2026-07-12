# temp_chunk_440_to_480



## Page 1

8.6
Classiﬁcation
427
Figure 8.11 Approximate linear discrimination via support vector classiﬁer,
with γ = 0.1. The support vector classiﬁer, shown as the solid line, misclas-
siﬁes three points. Fifteen points are correctly classiﬁed but lie in the slab
deﬁned by −1 < aT z −b < 1, bounded by the dashed lines.
{y1, . . . , yM} is deﬁned as the solution of
minimize
∥a∥2 + γ(1T u + 1T v)
subject to
aT xi −b ≥1 −ui,
i = 1, . . . , N
aT yi −b ≤−(1 −vi),
i = 1, . . . , M
u ⪰0,
v ⪰0,
The ﬁrst term is proportional to the inverse of the width of the slab deﬁned by
−1 ≤aT z −b ≤1. The second term has the same interpretation as above, i.e., it
is a convex relaxation for the number of misclassiﬁed points (including the points
in the slab). The parameter γ, which is positive, gives the relative weight of the
number of misclassiﬁed points (which we want to minimize), compared to the width
of the slab (which we want to maximize). Figure 8.11 shows an example.
Approximate linear discrimination via logistic modeling
Another approach to ﬁnding an aﬃne function that approximately classiﬁes two
sets of points that cannot be linearly separated is based on the logistic model
described in §7.1.1. We start by ﬁtting the two sets of points with a logistic model.
Suppose z is a random variable with values 0 or 1, with a distribution that depends
on some (deterministic) explanatory variable u ∈Rn, via a logistic model of the
form
prob(z = 1) = (exp(aT u −b))/(1 + exp(aT u −b))
prob(z = 0) = 1/(1 + exp(aT u −b)).
(8.26)
Now we assume that the given sets of points, {x1, . . . , xN} and {y1, . . . , yM},
arise as samples from the logistic model. Speciﬁcally, {x1, . . . , xN} are the values


## Page 2

428
8
Geometric problems
of u for the N samples for which z = 1, and {y1, . . . , yM} are the values of u for
the M samples for which z = 0. (This allows us to have xi = yj, which would rule
out discrimination between the two sets. In a logistic model, it simply means that
we have two samples, with the same value of explanatory variable but diﬀerent
outcomes.)
We can determine a and b by maximum likelihood estimation from the observed
samples, by solving the convex optimization problem
minimize
−l(a, b)
(8.27)
with variables a, b, where l is the log-likelihood function
l(a, b) = PN
i=1(aT xi −b)
−PN
i=1 log(1 + exp(aT xi −b)) −PM
i=1 log(1 + exp(aT yi −b))
(see §7.1.1). If the two sets of points can be linearly separated, i.e., if there exist a,
b with aT xi > b and aT yi < b, then the optimization problem (8.27) is unbounded
below.
Once we ﬁnd the maximum likelihood values of a and b, we can form a linear
classiﬁer f(x) = aT x −b for the two sets of points. This classiﬁer has the following
property: Assuming the data points are in fact generated from a logistic model
with parameters a and b, it has the smallest probability of misclassiﬁcation, over
all linear classiﬁers.
The hyperplane aT u = b corresponds to the points where
prob(z = 1) = 1/2, i.e., the two outcomes are equally likely. An example is shown
in ﬁgure 8.12.
Remark 8.1 Bayesian interpretation. Let x and z be two random variables, taking
values in Rn and in {0, 1}, respectively. We assume that
prob(z = 1) = prob(z = 0) = 1/2,
and we denote by p0(x) and p1(x) the conditional probability densities of x, given
z = 0 and given z = 1, respectively. We assume that p0 and p1 satisfy
p1(x)
p0(x) = eaT x−b
for some a and b. Many common distributions satisfy this property. For example,
p0 and p1 could be two normal densities on Rn with equal covariance matrices and
diﬀerent means, or they could be two exponential densities on Rn
+.
It follows from Bayes’ rule that
prob(z = 1 | x = u)
=
p1(u)
p1(u) + p0(u)
prob(z = 0 | x = u)
=
p0(u)
p1(u) + p0(u),
from which we obtain
prob(z = 1 | x = u)
=
exp(aT u −b)
1 + exp(aT u −b)
prob(z = 0 | x = u)
=
1
1 + exp(aT u −b).


## Page 3

8.6
Classiﬁcation
429
Figure 8.12 Approximate linear discrimination via logistic modeling. The
points x1, . . . , x50, shown as open circles, cannot be linearly separated from
the points y1, . . . , y50, shown as ﬁlled circles. The maximum likelihood lo-
gistic model yields the hyperplane shown as a dark line, which misclassiﬁes
only two points. The two dashed lines show aT u−b = ±1, where the proba-
bility of each outcome, according to the logistic model, is 73%. Three points
are correctly classiﬁed, but lie in between the dashed lines.
The logistic model (8.26) can therefore be interpreted as the posterior distribution of
z, given that x = u.
8.6.2
Nonlinear discrimination
We can just as well seek a nonlinear function f, from a given subspace of functions,
that is positive on one set and negative on another:
f(xi) > 0,
i = 1, . . . , N,
f(yi) < 0,
i = 1, . . . , M.
Provided f is linear (or aﬃne) in the parameters that deﬁne it, these inequalities
can be solved in exactly the same way as in linear discrimination. In this section
we examine some interesting special cases.
Quadratic discrimination
Suppose we take f to be quadratic: f(x) = xT Px + qT x + r. The parameters
P ∈Sn, q ∈Rn, r ∈R must satisfy the inequalities
xT
i Pxi + qT xi + r > 0,
i = 1, . . . , N
yT
i Pyi + qT yi + r < 0,
i = 1, . . . , M,


## Page 4

430
8
Geometric problems
which is a set of strict linear inequalities in the variables P, q, r. As in linear
discrimination, we note that f is homogeneous in P, q, and r, so we can ﬁnd a
solution to the strict inequalities by solving the nonstrict feasibility problem
xT
i Pxi + qT xi + r ≥1,
i = 1, . . . , N
yT
i Pyi + qT yi + r ≤−1,
i = 1, . . . , M.
The separating surface {z | zT Pz + qT z + r = 0} is a quadratic surface, and
the two classiﬁcation regions
{z | zT Pz + qT z + r ≤0},
{z | zT Pz + qT z + r ≥0},
are deﬁned by quadratic inequalities. Solving the quadratic discrimination problem,
then, is the same as determining whether the two sets of points can be separated
by a quadratic surface.
We can impose conditions on the shape of the separating surface or classiﬁcation
regions by adding constraints on P, q, and r. For example, we can require that
P ≺0, which means the separating surface is ellipsoidal. More speciﬁcally, it means
that we seek an ellipsoid that contains all the points x1, . . . , xN, but none of the
points y1, . . . , yM. This quadratic discrimination problem can be solved as an SDP
feasibility problem
ﬁnd
P, q, r
subject to
xT
i Pxi + qT xi + r ≥1,
i = 1, . . . , N
yT
i Pyi + qT yi + r ≤−1,
i = 1, . . . , M
P ⪯−I,
with variables P ∈Sn, q ∈Rn, and r ∈R. (Here we use homogeneity in P, q, r
to express the constraint P ≺0 as P ⪯−I.) Figure 8.13 shows an example.
Polynomial discrimination
We consider the set of polynomials on Rn with degree less than or equal to d:
f(x) =
X
i1+···+in≤d
ai1···idxi1
1 · · · xin
n .
We can determine whether or not two sets {x1, . . . , xN} and {y1, . . . , yM} can be
separated by such a polynomial by solving a set of linear inequalities in the variables
ai1···id. Geometrically, we are checking whether the two sets can be separated by
an algebraic surface (deﬁned by a polynomial of degree less than or equal to d).
As an extension, the problem of determining the minimum degree polynomial on
Rn that separates two sets of points can be solved via quasiconvex programming,
since the degree of a polynomial is a quasiconvex function of the coeﬃcients. This
can be carried out by bisection on d, solving a feasibility linear program at each
step. An example is shown in ﬁgure 8.14.


## Page 5

8.6
Classiﬁcation
431
Figure 8.13 Quadratic discrimination, with the condition that P ≺0. This
means that we seek an ellipsoid containing all of xi (shown as open circles)
and none of the yi (shown as ﬁlled circles). This can be solved as an SDP
feasibility problem.
Figure 8.14 Minimum degree polynomial discrimination in R2. In this ex-
ample, there exists no cubic polynomial that separates the points x1, . . . , xN
(shown as open circles) from the points y1, . . . , yM (shown as ﬁlled circles),
but they can be separated by fourth-degree polynomial, the zero level set of
which is shown.


## Page 6

432
8
Geometric problems
8.7
Placement and location
In this section we discuss a few variations on the following problem.
We have
N points in R2 or R3, and a list of pairs of points that must be connected by
links. The positions of some of the N points are ﬁxed; our task is to determine the
positions of the remaining points, i.e., to place the remaining points. The objective
is to place the points so that some measure of the total interconnection length of
the links is minimized, subject to some additional constraints on the positions.
As an example application, we can think of the points as locations of plants or
warehouses of a company, and the links as the routes over which goods must be
shipped. The goal is to ﬁnd locations that minimize the total transportation cost.
In another application, the points represent the position of modules or cells on an
integrated circuit, and the links represent wires that connect pairs of cells. Here
the goal might be to place the cells in such a way that the total length of wire used
to interconnect the cells is minimized.
The problem can be described in terms of an undirected graph with N nodes,
representing the N points. With each node we associate a variable xi ∈Rk, where
k = 2 or k = 3, which represents its location or position.
The problem is to
minimize
X
(i,j)∈A
fij(xi, xj)
where A is the set of all links in the graph, and fij : Rk × Rk →R is a cost
function associated with arc (i, j). (Alternatively, we can sum over all i and j, or
over i < j, and simply set fij = 0 when links i and j are not connected.) Some of
the coordinate vectors xi are given. The optimization variables are the remaining
coordinates. Provided the functions fij are convex, this is a convex optimization
problem.
8.7.1
Linear facility location problems
In the simplest version of the problem the cost associated with arc (i, j) is the
distance between nodes i and j: fij(xi, xj) = ∥xi −xj∥, i.e., we minimize
X
(i,j)∈A
∥xi −xj∥.
We can use any norm, but the most common applications involve the Euclidean
norm or the ℓ1-norm. For example, in circuit design it is common to route the wires
between cells along piecewise-linear paths, with each segment either horizontal or
vertical. (This is called Manhattan routing, since paths along the streets in a city
with a rectangular grid are also piecewise-linear, with each street aligned with one
of two orthogonal axes.) In this case, the length of wire required to connect cell i
and cell j is given by ∥xi −xj∥1.
We can include nonnegative weights that reﬂect diﬀerences in the cost per unit


## Page 7

8.7
Placement and location
433
distance along diﬀerent arcs:
X
(i,j)∈A
wij∥xi −xj∥.
By assigning a weight wij = 0 to pairs of nodes that are not connected, we can
express this problem more simply using the objective
X
i<j
wij∥xi −xj∥.
(8.28)
This placement problem is convex.
Example 8.4 One free point. Consider the case where only one point (u, v) ∈R2 is
free, and we minimize the sum of the distances to ﬁxed points (u1, v1), . . . , (uK, vK).
• ℓ1-norm. We can ﬁnd a point that minimizes
K
X
i=1
(|u −ui| + |v −vi|)
analytically. An optimal point is any median of the ﬁxed points. In other words,
u can be taken to be any median of the points {u1, . . . , uK}, and v can be taken
to be any median of the points {v1, . . . , vK}. (If K is odd, the minimizer is
unique; if K is even, there can be a rectangle of optimal points.)
• Euclidean norm.
The point (u, v) that minimizes the sum of the Euclidean
distances,
K
X
i=1
 (u −ui)2 + (v −vi)21/2 ,
is called the Weber point of the given ﬁxed points.
8.7.2
Placement constraints
We now list some interesting constraints that can be added to the basic placement
problem, preserving convexity. We can require some positions xi to lie in a speciﬁed
convex set, e.g., a particular line, interval, square, or ellipsoid. We can constrain
the relative position of one point with respect to one or more other points, for
example, by limiting the distance between a pair of points. We can impose relative
position constraints, e.g., that one point must lie to the left of another point.
The bounding box of a group of points is the smallest rectangle that contains
the points. We can impose a constraint that limits the points x1, . . . , xp (say) to lie
in a bounding box with perimeter not exceeding Pmax, by adding the constraints
u ⪯xi ⪯v,
i = 1, . . . , p,
21T (v −u) ≤Pmax,
where u, v are additional variables.


## Page 8

434
8
Geometric problems
8.7.3
Nonlinear facility location problems
More generally, we can associate a cost with each arc that is a nonlinear increasing
function of the length, i.e.,
minimize
P
i<j wijh(∥xi −xj∥)
where h is an increasing (on R+) and convex function, and wij ≥0. We call this
a nonlinear placement or nonlinear facility location problem.
One common example uses the Euclidean norm, and the function h(z) = z2,
i.e., we minimize
X
i<j
wij∥xi −xj∥2
2.
This is called a quadratic placement problem. The quadratic placement problem
can be solved analytically when the only constraints are linear equalities; it can be
solved as a QP if the constraints are linear equalities and inequalities.
Example 8.5 One free point. Consider the case where only one point x is free, and we
minimize the sum of the squares of the Euclidean distances to ﬁxed points x1, . . . , xK,
∥x −x1∥2
2 + ∥x −x2∥2
2 + · · · + ∥x −xK∥2
2.
Taking derivatives, we see that the optimal x is given by
1
K (x1 + x2 + · · · + xK),
i.e., the average of the ﬁxed points.
Some other interesting possibilities are the ‘deadzone’ function h with deadzone
width 2γ, deﬁned as
h(z) =
 0
|z| ≤γ
|z −γ|
|z| ≥γ,
and the ‘quadratic-linear’ function h, deﬁned as
h(z) =

z2
|z| ≤γ
2γ|z| −γ2
|z| ≥γ.
Example 8.6
We consider a placement problem in R2 with 6 free points, 8 ﬁxed
points, and 27 links. Figures 8.15–8.17 show the optimal solutions for the criteria
X
(i,j)∈A
∥xi −xj∥2,
X
(i,j)∈A
∥xi −xj∥2
2,
X
(i,j)∈A
∥xi −xj∥4
2,
i.e., using the penalty functions h(z) = z, h(z) = z2, and h(z) = z4. The ﬁgures also
show the resulting distributions of the link lengths.
Comparing the results, we see that the linear placement concentrates the free points in
a small area, while the quadratic and fourth-order placements spread the points over
larger areas. The linear placement includes many very short links, and a few very long
ones (3 lengths under 0.2 and 2 lengths above 1.5.). The quadratic penalty function


## Page 9

8.7
Placement and location
435
−1
0
1
−1
0
1
0
0.5
1
1.5
2
0
1
2
3
4
Figure 8.15 Linear placement. Placement problem with 6 free points (shown
as dots), 8 ﬁxed points (shown as squares), and 27 links. The coordinates of
the free points minimize the sum of the Euclidean lengths of the links. The
right plot is the distribution of the 27 link lengths. The dashed curve is the
(scaled) penalty function h(z) = z.
−1
0
1
−1
0
1
0
0.5
1
1.5
0
1
2
3
4
Figure 8.16 Quadratic placement.
Placement that minimizes the sum of
squares of the Euclidean lengths of the links, for the same data as in ﬁg-
ure 8.15. The dashed curve is the (scaled) penalty function h(z) = z2.


## Page 10

436
8
Geometric problems
−1
0
1
−1
0
1
0
0.5
1
1.5
0
1
2
3
4
5
6
Figure 8.17 Fourth-order placement. Placement that minimizes the sum of
the fourth powers of the Euclidean lengths of the links. The dashed curve
is the (scaled) penalty function h(z) = z4.
puts a higher penalty on long lengths relative to short lengths, and for lengths under
0.1, the penalty is almost negligible. As a result, the maximum length is shorter (less
than 1.4), but we also have fewer short links. The fourth-order function puts an even
higher penalty on long lengths, and has a wider interval (between zero and about
0.4) where it is negligible. As a result, the maximum length is shorter than for the
quadratic placement, but we also have more lengths close to the maximum.
8.7.4
Location problems with path constraints
Path constraints
A p-link path along the points x1, . . . , xN is described by a sequence of nodes,
i0, . . . , ip ∈{1, . . . , N}. The length of the path is given by
∥xi1 −xi0∥+ ∥xi2 −xi1∥+ · · · + ∥xip −xip−1∥,
which is a convex function of x1, . . . , xN, so imposing an upper bound on the length
of a path is a convex constraint. Several interesting placement problems involve
path constraints, or have an objective based on path lengths. We describe one
typical example, in which the objective is based on a maximum path length over a
set of paths.
Minimax delay placement
We consider a directed acyclic graph with nodes 1, . . . , N, and arcs or links repre-
sented by a set A of ordered pairs: (i, j) ∈A if and only if an arc points from i
to j. We say node i is a source node if no arc A points to it; it is a sink node or
destination node if no arc in A leaves from it. We will be interested in the maximal
paths in the graph, which begin at a source node and end at a sink node.
The arcs of the graph are meant to model some kind of ﬂow, say of goods or
information, in a network with nodes at positions x1, . . . , xN. The ﬂow starts at


## Page 11

8.7
Placement and location
437
a source node, then moves along a path from node to node, ending at a sink or
destination node. We use the distance between successive nodes to model prop-
agation time, or shipment time, of the goods between nodes; the total delay or
propagation time of a path is (proportional to) the sum of the distances between
successive nodes.
Now we can describe the minimax delay placement problem. Some of the node
locations are ﬁxed, and the others are free, i.e., optimization variables. The goal
is to choose the free node locations in order to minimize the maximum total delay,
for any path from a source node to a sink node. Evidently this is a convex problem,
since the objective
Tmax = max{∥xi1 −xi0∥+ · · · + ∥xip −xip−1∥| i0, . . . , ip is a source-sink path}
(8.29)
is a convex function of the locations x1, . . . , xN.
While the problem of minimizing (8.29) is convex, the number of source-sink
paths can be very large, exponential in the number of nodes or arcs. There is
a useful reformulation of the problem, which avoids enumerating all sink-source
paths.
We ﬁrst explain how we can evaluate the maximum delay Tmax far more ef-
ﬁciently than by evaluating the delay for every source-sink path, and taking the
maximum. Let τk be the maximum total delay of any path from node k to a sink
node. Clearly we have τk = 0 when k is a sink node. Consider a node k, which has
outgoing arcs to nodes j1, . . . , jp. For a path starting at node k and ending at a
sink node, its ﬁrst arc must lead to one of the nodes j1, . . . , jp. If such a path ﬁrst
takes the arc leading to ji, and then takes the longest path from there to a sink
node, the total length is
∥xji −xk∥+ τji,
i.e., the length of the arc to ji, plus the total length of the longest path from ji to
a sink node. It follows that the maximum delay of a path starting at node k and
leading to a sink node satisﬁes
τk = max{∥xj1 −xk∥+ τj1, . . . , ∥xjp −xk∥+ τjp}.
(8.30)
(This is a simple dynamic programming argument.)
The equations (8.30) give a recursion for ﬁnding the maximum delay from any
node: we start at the sink nodes (which have maximum delay zero), and then
work backward using the equations (8.30), until we reach all source nodes. The
maximum delay over any such path is then the maximum of all the τk, which will
occur at one of the source nodes.
This dynamic programming recursion shows
how the maximum delay along any source-sink path can be computed recursively,
without enumerating all the paths. The number of arithmetic operations required
for this recursion is approximately the number of links.
Now we show how the recursion based on (8.30) can be used to formulate the
minimax delay placement problem. We can express the problem as
minimize
max{τk | k a source node}
subject to
τk = 0,
k a sink node
τk = max{∥xj −xk∥+ τj | there is an arc from k to j},


## Page 12

438
8
Geometric problems
with variables τ1, . . . , τN and the free positions. This problem is not convex, but
we can express it in an equivalent form that is convex, by replacing the equality
constraints with inequalities. We introduce new variables T1, . . . , TN, which will be
upper bounds on τ1, . . . , τN, respectively. We will take Tk = 0 for all sink nodes,
and in place of (8.30) we take the inequalities
Tk ≥max{∥xj1 −xk∥+ Tj1, . . . , ∥xjp −xk∥+ Tjp}.
If these inequalities are satisﬁed, then Tk ≥τk. Now we form the problem
minimize
max{Tk | k a source node}
subject to
Tk = 0,
k a sink node
Tk ≥max{∥xj −xk∥+ Tj | there is an arc from k to j}.
This problem, with variables T1, . . . , TN and the free locations, is convex, and solves
the minimax delay location problem.
8.8
Floor planning
In placement problems, the variables represent the coordinates of a number of
points that are to be optimally placed. A ﬂoor planning problem can be considered
an extension of a placement problem in two ways:
• The objects to be placed are rectangles or boxes aligned with the axes (as
opposed to points), and must not overlap.
• Each rectangle or box to be placed can be reconﬁgured, within some limits.
For example we might ﬁx the area of each rectangle, but not the length and
height separately.
The objective is usually to minimize the size (e.g., area, volume, perimeter) of the
bounding box, which is the smallest box that contains the boxes to be conﬁgured
and placed.
The non-overlap constraints make the general ﬂoor planning problem a compli-
cated combinatorial optimization problem or rectangle packing problem. However,
if the relative positioning of the boxes is speciﬁed, several types of ﬂoor planning
problems can be formulated as convex optimization problems. We explore some
of these in this section. We consider the two-dimensional case, and make a few
comments on extensions to higher dimensions (when they are not obvious).
We have N cells or modules C1, . . . , CN that are to be conﬁgured and placed
in a rectangle with width W and height H, and lower left corner at the position
(0, 0). The geometry and position of the ith cell is speciﬁed by its width wi and
height hi, and the coordinates (xi, yi) of its lower left corner. This is illustrated in
ﬁgure 8.18.
The variables in the problem are xi, yi, wi, hi for i = 1, . . . , N, and the width
W and height H of the bounding rectangle. In all ﬂoor planning problems, we
require that the cells lie inside the bounding rectangle, i.e.,
xi ≥0,
yi ≥0,
xi + wi ≤W,
yi + hi ≤H,
i = 1, . . . , N.
(8.31)


## Page 13

8.8
Floor planning
439
W
H
hi
wi
(xi, yi)
Ci
Figure 8.18 Floor planning problem. Non-overlapping rectangular cells are
placed in a rectangle with width W, height H, and lower left corner at (0, 0).
The ith cell is speciﬁed by its width wi, height hi, and the coordinates of its
lower left corner, (xi, yi).
We also require that the cells do not overlap, except possibly on their boundaries:
int (Ci ∩Cj) = ∅
for i̸ = j.
(It is also possible to require a positive minimum clearance between the cells.) The
non-overlap constraint int(Ci ∩Cj) = ∅holds if and only if for i̸ = j,
Ci is left of Cj, or Ci is right of Cj, or Ci is below Cj, or Ci is above Cj.
These four geometric conditions correspond to the inequalities
xi + wi ≤xj, or xj + wj ≤xi, or yi + hi ≤yj, or yj + hj ≤yi,
(8.32)
at least one of which must hold for each i̸ = j. Note the combinatorial nature of
these constraints: for each pair i̸ = j, at least one of the four inequalities above
must hold.
8.8.1
Relative positioning constraints
The idea of relative positioning constraints is to specify, for each pair of cells,
one of the four possible relative positioning conditions, i.e., left, right, above, or
below. One simple method to specify these constraints is to give two relations on
{1, . . . , N}: L (meaning ‘left of’) and B (meaning ‘below’). We then impose the
constraint that Ci is to the left of Cj if (i, j) ∈L, and Ci is below Cj if (i, j) ∈B.
This yields the constraints
xi + wi ≤xj for (i, j) ∈L,
yi + hi ≤yj for (i, j) ∈B,
(8.33)


## Page 14

440
8
Geometric problems
for i, j = 1, . . . , N.
To ensure that the relations L and B specify the relative
positioning of each pair of cells, we require that for each (i, j) with i̸ = j, one of
the following holds:
(i, j) ∈L,
(j, i) ∈L,
(i, j) ∈B,
(j, i) ∈B,
and that (i, i)̸ ∈L, (i, i)̸ ∈B. The inequalities (8.33) are a set of N(N −1)/2 linear
inequalities in the variables.
These inequalities imply the non-overlap inequali-
ties (8.32), which are a set of N(N −1)/2 disjunctions of four linear inequalities.
We can assume that the relations L and B are anti-symmetric (i.e., (i, j) ∈
L ⇒(j, i)̸ ∈L) and transitive (i.e., (i, j) ∈L, (j, k) ∈L ⇒(i, k) ∈L). (If this
were not the case, the relative positioning constraints would clearly be infeasible.)
Transitivity corresponds to the obvious condition that if cell Ci is to the left of cell
Cj, which is to the left of cell Ck, then cell Ci must be to the left of cell Ck. In
this case the inequality corresponding to (i, k) ∈L is redundant; it is implied by
the other two. By exploiting transitivity of the relations L and B we can remove
redundant constraints, and obtain a compact set of relative positioning inequalities.
A minimal set of relative positioning constraints is conveniently described using
two directed acyclic graphs H and V (for horizontal and vertical). Both graphs have
N nodes, corresponding to the N cells in the ﬂoor planning problem. The graph
H generates the relation L as follows: we have (i, j) ∈L if and only if there is
a (directed) path in H from i to j. Similarly, the graph V generates the relation
B: (i, j) ∈B if and only if there is a (directed) path in V from i to j. To ensure
that a relative positioning constraint is given for every pair of cells, we require that
for every pair of cells, there is a directed path from one to the other in one of the
graphs.
Evidently, we only need to impose the inequalities that correspond to the edges
of the graphs H and V; the others follow from transitivity. We arrive at the set of
inequalities
xi + wi ≤xj for (i, j) ∈H,
yi + hi ≤yj for (i, j) ∈V,
(8.34)
which is a set of linear inequalities, one for each edge in H and V. The set of
inequalities (8.34) is a subset of the set of inequalities (8.33), and equivalent.
In a similar way, the 4N inequalities (8.31) can be reduced to a minimal, equiv-
alent set. The constraint xi ≥0 only needs to be imposed on the left-most cells,
i.e., for i that are minimal in the relation L. These correspond to the sources in
the graph H, i.e., those nodes that have no edges pointing to them. Similarly, the
inequalities xi + wi ≤W only need to be imposed for the right-most cells. In the
same way the vertical bounding box inequalities can be pruned to a minimal set.
This yields the minimal equivalent set of bounding box inequalities
xi ≥0 for i L minimal,
xi + wi ≤W for i L maximal,
yi ≥0 for i B minimal,
yi + hi ≤H for i B maximal.
(8.35)
A simple example is shown in ﬁgure 8.19. In this example, the L minimal or
left-most cells are C1, C2, and C4, and the only right-most cell is C5. The minimal
set of inequalities specifying the horizontal relative positioning is given by
x1 ≥0,
x2 ≥0,
x4 ≥0,
x5 + w5 ≤W,
x1 + w1 ≤x3,
x2 + w2 ≤x3,
x3 + w3 ≤x5,
x4 + w4 ≤x5.


## Page 15

8.8
Floor planning
441
H
V
1
2
3
4
5
1
2
3
4
5
1
2
3
4
5
Figure 8.19 Example illustrating the horizontal and vertical graphs H and
V that specify the relative positioning of the cells. If there is a path from
node i to node j in H, then cell i must be placed to the left of cell j. If there
is a path from node i to node j in V, then cell i must be placed below cell
j. The ﬂoorplan shown at right satisﬁes the relative positioning speciﬁed by
the two graphs.
The minimal set of inequalities specifying the vertical relative positioning is given
by
y2 ≥0,
y3 ≥0,
y5 ≥0,
y4 + h4 ≤H,
y5 + h5 ≤H,
y2 + h2 ≤y1,
y1 + h1 ≤y4,
y3 + h3 ≤y4.
8.8.2
Floor planning via convex optimization
In this formulation, the variables are the bounding box width and height W and
H, and the cell widths, heights, and positions: wi, hi, xi, and wi, for i = 1, . . . , N.
We impose the bounding box constraints (8.35) and the relative positioning con-
straints (8.34), which are linear inequalities. As objective, we take the perimeter
of the bounding box, i.e., 2(W + H), which is a linear function of the variables.
We now list some of the constraints that can be expressed as convex inequalities
or linear equalities in the variables.
Minimum spacing
We can impose a minimum spacing ρ > 0 between cells by changing the relative
position constraints from xi + wi ≤xj for (i, j) ∈H, to xi + wi + ρ ≤xj for
(i, j) ∈H, and similarly for the vertical graph. We can have a diﬀerent minimum
spacing associated with each edge in H and V. Another possibility is to ﬁx W and
H, and maximize the minimum spacing ρ as objective.


## Page 16

442
8
Geometric problems
Minimum cell area
For each cell we specify a minimum area, i.e., we require that wihi ≥Ai, where
Ai > 0. These minimum cell area constraints can be expressed as convex inequali-
ties in several ways, e.g., wi ≥Ai/hi, (wihi)1/2 ≥A1/2
i
, or log wi + log hi ≥log Ai.
Aspect ratio constraints
We can impose upper and lower bounds on the aspect ratio of each cell, i.e.,
li ≤hi/wi ≤ui.
Multiplying through by wi transforms these constraints into linear inequalities. We
can also ﬁx the aspect ratio of a cell, which results in a linear equality constraint.
Alignment constraints
We can impose the constraint that two edges, or a center line, of two cells are
aligned. For example, the horizontal center line of cell i aligns with the top of cell
j when
yi + hi/2 = yj + hj.
These are linear equality constraints. In a similar way we can require that a cell is
ﬂushed against the bounding box boundary.
Symmetry constraints
We can require pairs of cells to be symmetric about a vertical or horizontal axis,
that can be ﬁxed or ﬂoating (i.e., whose position is ﬁxed or not). For example, to
specify that the pair of cells i and j are symmetric about the vertical axis x = xaxis,
we impose the linear equality constraint
xaxis −(xi + wi/2) = xj + wj/2 −xaxis.
We can require that several pairs of cells be symmetric about an unspeciﬁed vertical
axis by imposing these equality constraints, and introducing xaxis as a new variable.
Similarity constraints
We can require that cell i be an a-scaled translate of cell j by the equality con-
straints wi = awj, hi = ahj. Here the scaling factor a must be ﬁxed. By imposing
only one of these constraints, we require that the width (or height) of one cell be
a given factor times the width (or height) of the other cell.
Containment constraints
We can require that a particular cell contains a given point, which imposes two lin-
ear inequalities. We can require that a particular cell lie inside a given polyhedron,
again by imposing linear inequalities.


## Page 17

8.8
Floor planning
443
Distance constraints
We can impose a variety of constraints that limit the distance between pairs of
cells. In the simplest case, we can limit the distance between the center points
of cell i and j (or any other ﬁxed points on the cells, such as lower left corners).
For example, to limit the distance between the centers of cells i and j, we use the
(convex) inequality
∥(xi + wi/2, yi + hi/2) −(xj + wj/2, yj + hj/2)∥≤Dij.
As in placement problems, we can limit sums of distances, or use sums of distances
as the objective.
We can also limit the distance dist(Ci, Cj) between cell i and cell j, i.e., the
minimum distance between a point in cell i and a point in cell j. In the general
case this can be done as follows. To limit the distance between cells i and j in the
norm ∥· ∥, we can introduce four new variables ui, vi, uj, vj. The pair (ui, vi)
will represent a point in Ci, and the pair (uj, vj) will represent a point in Cj. To
ensure this we impose the linear inequalities
xi ≤ui ≤xi + wi,
yi ≤vi ≤yi + hi,
and similarly for cell j. Finally, to limit dist(Ci, Cj), we add the convex inequality
∥(ui, vi) −(uj, vj)∥≤Dij.
In many speciﬁc cases we can express these distance constraints more eﬃciently,
by exploiting the relative positioning constraints or deriving a more explicit formu-
lation. As an example consider the ℓ∞-norm, and suppose cell i lies to the left of
cell j (by a relative positioning constraint). The horizontal displacement between
the two cells is xj −(xi + wi) Then we have dist(Ci, Cj) ≤Dij if and only if
xj −(xi + wi) ≤Dij,
yj −(yi + hi) ≤Dij,
yi −(yj + hj) ≤Dij.
The ﬁrst inequality states that the horizontal displacement between the right edge
of cell i and the left edge of cell j does not exceed Dij. The second inequality
requires that the bottom of cell j is no more than Dij above the top of cell i, and
the third inequality requires that the bottom of cell i is no more than Dij above the
top of cell j. These three inequalities together are equivalent to dist(Ci, Cj) ≤Dij.
In this case, we do not need to introduce any new variables.
We can limit the ℓ1- (or ℓ2-) distance between two cells in a similar way. Here
we introduce one new variable dv, which will serve as a bound on the vertical
displacement between the cells. To limit the ℓ1-distance, we add the constraints
yj −(yi + hi) ≤dv,
yi −(yj + hj) ≤dv,
dv ≥0
and the constraints
xj −(xi + wi) + dv ≤Dij.
(The ﬁrst term is the horizontal displacement and the second is an upper bound
on the vertical displacement.) To limit the Euclidean distance between the cells,
we replace this last constraint with
(xj −(xi + wi))2 + d2
v ≤D2
ij.


## Page 18

444
8
Geometric problems
1
1
1
1
2
2
2
2
3
3
3
3
4
4
4
4
5
5
5
5
Figure 8.20 Four instances of an optimal ﬂoor plan, using the relative po-
sitioning constraints shown in ﬁgure 8.19. In each case the objective is to
minimize the perimeter, and the same minimum spacing constraint between
cells is imposed. We also require the aspect ratios to lie between 1/5 and 5.
The four cases diﬀer in the minimum areas required for each cell. The sum
of the minimum areas is the same for each case.
Example 8.7 Figure 8.20 shows an example with 5 cells, using the ordering constraints
of ﬁgure 8.19, and four diﬀerent sets of constraints.
In each case we impose the
same minimum required spacing constraint, and the same aspect ratio constraint
1/5 ≤wi/hi ≤5. The four cases diﬀer in the minimum required cell areas Ai. The
values of Ai are chosen so that the total minimum required area P5
i=1 Ai is the same
for each case.
8.8.3
Floor planning via geometric programming
The ﬂoor planning problem can also be formulated as a geometric program in the
variables xi, yi, wi, hi, W, H. The objectives and constraints that can be handled
in this formulation are a bit diﬀerent from those that can be expressed in the convex
formulation.
First we note that the bounding box constraints (8.35) and the relative po-


## Page 19

8.8
Floor planning
445
sitioning constraints (8.34) are posynomial inequalities, since the lefthand sides
are sums of variables, and the righthand sides are single variables, hence monomi-
als. Dividing these inequalities by the righthand side yields standard posynomial
inequalities.
In the geometric programming formulation we can minimize the bounding box
area, since WH is a monomial, hence posynomial. We can also exactly specify
the area of each cell, since wihi = Ai is a monomial equality constraint. On the
other hand alignment, symmetry, and distance constraints cannot be handled in
the geometric programming formulation. Similarity, however, can be; indeed it
is possible to require that one cell be similar to another, without specifying the
scaling ratio (which can be treated as just another variable).


## Page 20

446
8
Geometric problems
Bibliography
The characterization of Euclidean distance matrices in §8.3.3 appears in Schoenberg
[Sch35]; see also Gower [Gow85].
Our use of the term L¨owner-John ellipsoid follows Gr¨otschel, Lov´asz, and Schrijver
[GLS88, page 69]. The eﬃciency results for ellipsoidal approximations in §8.4 were proved
by John [Joh85]. Boyd, El Ghaoui, Feron, and Balakrishnan [BEFB94, §3.7] give con-
vex formulations of several ellipsoidal approximation problems involving sets deﬁned as
unions, intersections or sums of ellipsoids.
The diﬀerent centers deﬁned in §8.5 have applications in design centering (see, for exam-
ple, Seiﬁ, Ponnambalan, and Vlach [SPV99]), and cutting-plane methods (Elzinga and
Moore [EM75], Tarasov, Khachiyan, and `Erlikh [TKE88], and Ye [Ye97, chapter 8]). The
inner ellipsoid deﬁned by the Hessian of the logarithmic barrier function (page 420) is
sometimes called the Dikin ellipsoid, and is the basis of Dikin’s algorithm for linear and
quadratic programming [Dik67]. The expression for the outer ellipsoid at the analytic
center was given by Sonnevend [Son86]. For extensions to nonpolyhedral convex sets, see
Boyd and El Ghaoui [BE93], Jarre [Jar94], and Nesterov and Nemirovski [NN94, page
34].
Convex optimization has been applied to linear and nonlinear discrimination problems
since the 1960s; see Mangasarian [Man65] and Rosen [Ros65]. Standard texts that dis-
cuss pattern classiﬁcation include Duda, Hart, and Stork [DHS99] and Hastie, Tibshirani,
and Friedman [HTF01]. For a detailed discussion of support vector classiﬁers, see Vap-
nik [Vap00] or Sch¨olkopf and Smola [SS01].
The Weber point deﬁned in example 8.4 is named after Weber [Web71].
Linear and
quadratic placement is used in circuit design (Kleinhaus, Sigl, Johannes, and Antre-
ich [KSJA91, SDJ91]). Sherwani [She99] is a recent overview of algorithms for placement,
layout, ﬂoor planning, and other geometric optimization problems in VLSI circuit design.


## Page 21

Exercises
447
Exercises
Projection on a set
8.1 Uniqueness of projection. Show that if C ⊆Rn is nonempty, closed and convex, and the
norm ∥· ∥is strictly convex, then for every x0 there is exactly one x ∈C closest to x0. In
other words the projection of x0 on C is unique.
8.2 [Web94, Val64] Chebyshev characterization of convexity. A set C ∈Rn is called a Cheby-
shev set if for every x0 ∈Rn, there is a unique point in C closest (in Euclidean norm)
to x0. From the result in exercise 8.1, every nonempty, closed, convex set is a Chebyshev
set. In this problem we show the converse, which is known as Motzkin’s theorem.
Let C ∈Rn be a Chebyshev set.
(a) Show that C is nonempty and closed.
(b) Show that PC, the Euclidean projection on C, is continuous.
(c) Suppose x0̸ ∈C. Show that PC(x) = PC(x0) for all x = θx0 + (1 −θ)PC(x0) with
0 ≤θ ≤1.
(d) Suppose x0̸ ∈C. Show that PC(x) = PC(x0) for all x = θx0 + (1 −θ)PC(x0) with
θ ≥1.
(e) Combining parts (c) and (d), we can conclude that all points on the ray with base
PC(x0) and direction x0 −PC(x0) have projection PC(x0). Show that this implies
that C is convex.
8.3 Euclidean projection on proper cones.
(a) Nonnegative orthant. Show that Euclidean projection onto the nonnegative orthant
is given by the expression on page 399.
(b) Positive semideﬁnite cone. Show that Euclidean projection onto the positive semidef-
inite cone is given by the expression on page 399.
(c) Second-order cone. Show that the Euclidean projection of (x0, t0) on the second-
order cone
K = {(x, t) ∈Rn+1 | ∥x∥2 ≤t}
is given by
PK(x0, t0) =
( 0
∥x0∥2 ≤−t0
(x0, t0)
∥x0∥2 ≤t0
(1/2)(1 + t0/∥x0∥2)(x0, ∥x0∥2)
∥x0∥2 ≥|t0|.
8.4 The Euclidean projection of a point on a convex set yields a simple separating hyperplane
(PC(x0) −x0)T (x −(1/2)(x0 + PC(x0))) = 0.
Find a counterexample that shows that this construction does not work for general norms.
8.5 [HUL93, volume 1, page 154] Depth function and signed distance to boundary. Let C ⊆Rn
be a nonempty convex set, and let dist(x, C) be the distance of x to C in some norm.
We already know that dist(x, C) is a convex function of x.
(a) Show that the depth function,
depth(x, C) = dist(x, Rn \ C),
is concave for x ∈C.
(b) The signed distance to the boundary of C is deﬁned as
s(x) =

dist(x, C)
x̸ ∈C
−depth(x, C)
x ∈C.
Thus, s(x) is positive outside C, zero on its boundary, and negative on its interior.
Show that s is a convex function.


## Page 22

448
8
Geometric problems
Distance between sets
8.6 Let C, D be convex sets.
(a) Show that dist(C, x + D) is a convex function of x.
(b) Show that dist(tC, x + tD) is a convex function of (x, t) for t > 0.
8.7 Separation of ellipsoids. Let E1 and E2 be two ellipsoids deﬁned as
E1 = {x | (x −x1)T P −1
1
(x −x1) ≤1},
E2 = {x | (x −x2)T P −1
2
(x −x2) ≤1},
where P1, P2 ∈Sn
++. Show that E1 ∩E2 = ∅if and only if there exists an a ∈Rn with
∥P 1/2
2
a∥2 + ∥P 1/2
1
a∥2 < aT (x1 −x2).
8.8 Intersection and containment of polyhedra. Let P1 and P2 be two polyhedra deﬁned as
P1 = {x | Ax ⪯b},
P2 = {x | Fx ⪯g},
with A ∈Rm×n, b ∈Rm, F ∈Rp×n, g ∈Rp. Explain how to carry out the tasks below
by solving one or a modest number of LP feasibility problems.
(a) Find a point in the intersection P1 ∩P2.
(b) Determine whether P1 ⊆P2.
Repeat the question for two polyhedra deﬁned as
P1 = conv{v1, . . . , vK},
P2 = conv{w1, . . . , wL},
with v1, . . . , vK, w1, . . . , wL ∈Rn.
Euclidean distance and angle problems
8.9 Closest Euclidean distance matrix to given data. We are given data ˆdij, for i, j = 1, . . . , n,
which are corrupted measurements of the Euclidean distances between vectors in Rk:
ˆdij = ∥xi −xj∥2 + vij,
i, j = 1, . . . , n,
where vij is some noise or error. These data satisfy ˆdij ≥0 and ˆdij = ˆdji, for all i, j. The
dimension k is not speciﬁed.
Show how to solve the following problem using convex optimization. Find a dimension
k and x1, . . . , xn ∈Rk so that Pn
i,j=1(dij −ˆdij)2 is minimized, where dij = ∥xi −xj∥2,
i, j = 1, . . . , n. In other words, given some data that are approximate Euclidean distances,
you are to ﬁnd the closest set of actual Euclidean distances, in the least-squares sense.
8.10 Minimax angle ﬁtting. Suppose that y1, . . . , ym ∈Rk are aﬃne functions of a variable
x ∈Rn:
yi = Aix + bi,
i = 1, . . . , m,
and z1, . . . , zm ∈Rk are given nonzero vectors. We want to choose the variable x, subject
to some convex constraints, (e.g., linear inequalities) to minimize the maximum angle
between yi and zi,
max{̸ (y1, z1), . . . ,̸
(ym, zm)}.
The angle between nonzero vectors is deﬁned as usual:̸
(u, v) = cos−1

uT v
∥u∥2∥v∥2

,
where we take cos−1(a) ∈[0, π]. We are only interested in the case when the optimal
objective value does not exceed π/2.
Formulate this problem as a convex or quasiconvex optimization problem.
When the
constraints on x are linear inequalities, what kind of problem (or problems) do you have
to solve?


## Page 23

Exercises
449
8.11 Smallest Euclidean cone containing given points. In Rn, we deﬁne a Euclidean cone, with
center direction c̸ = 0, and angular radius θ, with 0 ≤θ ≤π/2, as the set
{x ∈Rn |̸
(c, x) ≤θ}.
(A Euclidean cone is a second-order cone, i.e., it can be represented as the image of the
second-order cone under a nonsingular linear mapping.)
Let a1, . . . , am ∈Rn. How would you ﬁnd the Euclidean cone, of smallest angular radius,
that contains a1, . . . , am? (In particular, you should explain how to solve the feasibility
problem, i.e., how to determine whether there is a Euclidean cone which contains the
points.)
Extremal volume ellipsoids
8.12 Show that the maximum volume ellipsoid enclosed in a set is unique.
Show that the
L¨owner-John ellipsoid of a set is unique.
8.13 L¨owner-John ellipsoid of a simplex. In this exercise we show that the L¨owner-John el-
lipsoid of a simplex in Rn must be shrunk by a factor n to ﬁt inside the simplex. Since
the L¨owner-John ellipsoid is aﬃnely invariant, it is suﬃcient to show the result for one
particular simplex.
Derive the L¨owner-John ellipsoid Elj for the simplex C = conv{0, e1, . . . , en}. Show that
Elj must be shrunk by a factor 1/n to ﬁt inside the simplex.
8.14 Eﬃciency of ellipsoidal inner approximation. Let C be a polyhedron in Rn described as
C = {x | Ax ⪯b}, and suppose that {x | Ax ≺b} is nonempty.
(a) Show that the maximum volume ellipsoid enclosed in C, expanded by a factor n
about its center, is an ellipsoid that contains C.
(b) Show that if C is symmetric about the origin, i.e., of the form C = {x | −1 ⪯Ax ⪯
1}, then expanding the maximum volume inscribed ellipsoid by a factor √n gives
an ellipsoid that contains C.
8.15 Minimum volume ellipsoid covering union of ellipsoids. Formulate the following problem
as a convex optimization problem. Find the minimum volume ellipsoid E = {x | (x −
x0)T A−1(x −x0) ≤1} that contains K given ellipsoids
Ei = {x | xT Aix + 2bT
i x + ci ≤0},
i = 1, . . . , K.
Hint. See appendix B.
8.16 Maximum volume rectangle inside a polyhedron. Formulate the following problem as a
convex optimization problem. Find the rectangle
R = {x ∈Rn | l ⪯x ⪯u}
of maximum volume, enclosed in a polyhedron P = {x | Ax ⪯b}. The variables are
l, u ∈Rn. Your formulation should not involve an exponential number of constraints.
Centering
8.17 Aﬃne invariance of analytic center. Show that the analytic center of a set of inequalities is
aﬃne invariant. Show that it is invariant with respect to positive scaling of the inequalities.
8.18 Analytic center and redundant inequalities. Two sets of linear inequalities that describe
the same polyhedron can have diﬀerent analytic centers. Show that by adding redundant
inequalities, we can make any interior point x0 of a polyhedron
P = {x ∈Rn | Ax ⪯b}


## Page 24

450
8
Geometric problems
the analytic center. More speciﬁcally, suppose A ∈Rm×n and Ax0 ≺b. Show that there
exist c ∈Rn, γ ∈R, and a positive integer q, such that P is the solution set of the m + q
inequalities
Ax ⪯b,
cT x ≤γ,
cT x ≤γ,
. . . ,
cT x ≤γ
(8.36)
(where the inequality cT x ≤γ is added q times), and x0 is the analytic center of (8.36).
8.19 Let xac be the analytic center of a set of linear inequalities
aT
i x ≤bi,
i = 1, . . . , m,
and deﬁne H as the Hessian of the logarithmic barrier function at xac:
H =
m
X
i=1
1
(bi −aT
i xac)2 aiaT
i .
Show that the kth inequality is redundant (i.e., it can be deleted without changing the
feasible set) if
bk −aT
k xac ≥m(aT
k H−1ak)1/2.
8.20 Ellipsoidal approximation from analytic center of linear matrix inequality. Let C be the
solution set of the LMI
x1A1 + x2A2 + · · · + xnAn ⪯B,
where Ai, B ∈Sm, and let xac be its analytic center. Show that
Einner ⊆C ⊆Eouter,
where
Einner
=
{x | (x −xac)T H(x −xac) ≤1},
Eouter
=
{x | (x −xac)T H(x −xac) ≤m(m −1)},
and H is the Hessian of the logarithmic barrier function
−log det(B −x1A1 −x2A2 −· · · −xnAn)
evaluated at xac.
8.21 [BYT99] Maximum likelihood interpretation of analytic center. We use the linear mea-
surement model of page 352,
y = Ax + v,
where A ∈Rm×n. We assume the noise components vi are IID with support [−1, 1]. The
set of parameters x consistent with the measurements y ∈Rm is the polyhedron deﬁned
by the linear inequalities
−1 + y ⪯Ax ⪯1 + y.
(8.37)
Suppose the probability density function of vi has the form
p(v) =

αr(1 −v2)r
−1 ≤v ≤1
0
otherwise,
where r ≥1 and αr > 0. Show that the maximum likelihood estimate of x is the analytic
center of (8.37).
8.22 Center of gravity. The center of gravity of a set C ⊆Rn with nonempty interior is deﬁned
as
xcg =
R
C u du
R
C 1 du .


## Page 25

Exercises
451
The center of gravity is aﬃne invariant, and (clearly) a function of the set C, and not
its particular description. Unlike the centers described in the chapter, however, it is very
diﬃcult to compute the center of gravity, except in simple cases (e.g., ellipsoids, balls,
simplexes).
Show that the center of gravity xcg is the minimizer of the convex function
f(x) =
Z
C
∥u −x∥2
2 du.
Classiﬁcation
8.23 Robust linear discrimination. Consider the robust linear discrimination problem given
in (8.23).
(a) Show that the optimal value t⋆is positive if and only if the two sets of points can
be linearly separated. When the two sets of points can be linearly separated, show
that the inequality ∥a∥2 ≤1 is tight, i.e., we have ∥a⋆∥2 = 1, for the optimal a⋆.
(b) Using the change of variables ˜a = a/t, ˜b = b/t, prove that the problem (8.23) is
equivalent to the QP
minimize
∥˜a∥2
subject to
˜aT xi −˜b ≥1,
i = 1, . . . , N
˜aT yi −˜b ≤−1,
i = 1, . . . , M.
8.24 Linear discrimination maximally robust to weight errors. Suppose we are given two sets of
points {x1, . . . , xN} and and {y1, . . . , yM} in Rn that can be linearly separated. In §8.6.1
we showed how to ﬁnd the aﬃne function that discriminates the sets, and gives the largest
gap in function values. We can also consider robustness with respect to changes in the
vector a, which is sometimes called the weight vector.
For a given a and b for which
f(x) = aT x −b separates the two sets, we deﬁne the weight error margin as the norm of
the smallest u ∈Rn such that the aﬃne function (a + u)T x −b no longer separates the
two sets of points. In other words, the weight error margin is the maximum ρ such that
(a + u)T xi ≥b,
i = 1, . . . , N,
(a + u)T yj ≤b,
i = 1, . . . , M,
holds for all u with ∥u∥2 ≤ρ.
Show how to ﬁnd a and b that maximize the weight error margin, subject to the normal-
ization constraint ∥a∥2 ≤1.
8.25 Most spherical separating ellipsoid. We are given two sets of vectors x1, . . . , xN ∈Rn,
and y1, . . . , yM ∈Rn, and wish to ﬁnd the ellipsoid E with minimum eccentricity (i.e.,
minimum condition number of the deﬁning matrix) that satisﬁes xi ∈E, i = 1, . . . , N,
and yi̸ ∈int E, i = 1, . . . , M. Formulate this as a convex optimization problem.
Placement and ﬂoor planning
8.26 Quadratic placement. We consider a placement problem in R2, deﬁned by an undirected
graph A with N nodes, and with quadratic costs:
minimize
P
(i,j)∈A ∥xi −xj∥2
2.
The variables are the positions xi ∈R2, i = 1, . . . , M. The positions xi, i = M +1, . . . , N
are given. We deﬁne two vectors u, v ∈RM by
u = (x11, x21, . . . , xM1),
v = (x12, x22, . . . , xM2),
containing the ﬁrst and second components, respectively, of the free nodes.


## Page 26

452
8
Geometric problems
Show that u and v can be found by solving two sets of linear equations,
Cu = d1,
Cv = d2,
where C ∈SM. Give a simple expression for the coeﬃcients of C in terms of the graph A.
8.27 Problems with minimum distance constraints.
We consider a problem with variables
x1, . . . , xN ∈Rk. The objective, f0(x1, . . . , xN), is convex, and the constraints
fi(x1, . . . , xN) ≤0,
i = 1, . . . , m,
are convex (i.e., the functions fi : RNk →R are convex).
In addition, we have the
minimum distance constraints
∥xi −xj∥2 ≥Dmin,
i̸ = j,
i, j = 1, . . . , N.
In general, this is a hard nonconvex problem.
Following the approach taken in ﬂoorplanning, we can form a convex restriction of the
problem, i.e., a problem which is convex, but has a smaller feasible set. (Solving the
restricted problem is therefore easy, and any solution is guaranteed to be feasible for the
nonconvex problem.) Let aij ∈Rk, for i < j, i, j = 1, . . . , N, satisfy ∥aij∥2 = 1.
Show that the restricted problem
minimize
f0(x1, . . . , xN)
subject to
fi(x1, . . . , xN) ≤0,
i = 1, . . . , m
aT
ij(xi −xj) ≥Dmin,
i < j, i, j = 1, . . . , N,
is convex, and that every feasible point satisﬁes the minimum distance constraint.
Remark. There are many good heuristics for choosing the directions aij. One simple
one starts with an approximate solution ˆx1, . . . , ˆxN (that need not satisfy the minimum
distance constraints). We then set aij = (ˆxi −ˆxj)/∥ˆxi −ˆxj∥2.
Miscellaneous problems
8.28 Let P1 and P2 be two polyhedra described as
P1 = {x | Ax ⪯b} ,
P2 = {x | −1 ⪯Cx ⪯1} ,
where A ∈Rm×n, C ∈Rp×n, and b ∈Rm. The polyhedron P2 is symmetric about the
origin. For t ≥0 and xc ∈Rn, we use the notation tP2 + xc to denote the polyhedron
tP2 + xc = {tx + xc | x ∈P2},
which is obtained by ﬁrst scaling P2 by a factor t about the origin, and then translating
its center to xc.
Show how to solve the following two problems, via an LP, or a set of LPs.
(a) Find the largest polyhedron tP2 + xc enclosed in P1, i.e.,
maximize
t
subject to
tP2 + xc ⊆P1
t ≥0.
(b) Find the smallest polyhedron tP2 + xc containing P1, i.e.,
minimize
t
subject to
P1 ⊆tP2 + xc
t ≥0.


## Page 27

Exercises
453
In both problems the variables are t ∈R and xc ∈Rn.
8.29 Outer polyhedral approximations. Let P = {x ∈Rn | Ax ⪯b} be a polyhedron, and
C ⊆Rn a given set (not necessarily convex). Use the support function SC to formulate
the following problem as an LP:
minimize
t
subject to
C ⊆tP + x
t ≥0.
Here tP +x = {tu+x | u ∈P}, the polyhedron P scaled by a factor of t about the origin,
and translated by x. The variables are t ∈R and x ∈Rn.
8.30 Interpolation with piecewise-arc curve. A sequence of points a1, . . . , an ∈R2 is given. We
construct a curve that passes through these points, in order, and is an arc (i.e., part of a
circle) or line segment (which we think of as an arc of inﬁnite radius) between consecutive
points. Many arcs connect ai and ai+1; we parameterize these arcs by giving the angle
θi ∈(−π, π) between its tangent at ai and the line segment [ai, ai+1]. Thus, θi = 0 means
the arc between ai and ai+1 is in fact the line segment [ai, ai+1]; θi = π/2 means the arc
between ai and ai+1 is a half-circle (above the linear segment [a1, a2]); θi = −π/2 means
the arc between ai and ai+1 is a half-circle (below the linear segment [a1, a2]). This is
illustrated below.
ai
ai+1
θi = 0
θi = π/4
θi = π/2
θi = 3π/4
Our curve is completely speciﬁed by the angles θ1, . . . , θn, which can be chosen in the
interval (−π, π). The choice of θi aﬀects several properties of the curve, for example, its
total arc length L, or the joint angle discontinuities, which can be described as follows.
At each point ai, i = 2, . . . , n −1, two arcs meet, one coming from the previous point and
one going to the next point. If the tangents to these arcs exactly oppose each other, so the
curve is diﬀerentiable at ai, we say there is no joint angle discontinuity at ai. In general,
we deﬁne the joint angle discontinuity at ai as |θi−1+θi+ψi|, where ψi is the angle between
the line segment [ai, ai+1] and the line segment [ai−1, ai], i.e., ψi ≠
(ai −ai+1, ai−1 −ai).
This is shown below. Note that the angles ψi are known (since the ai are known).
θi−1
θi
ψi
ai−1
ai
ai+1
We deﬁne the total joint angle discontinuity as
D =
n
X
i=2
|θi−1 + θi + ψi|.
Formulate the problem of minimizing total arc length length L, and total joint angle
discontinuity D, as a bi-criterion convex optimization problem. Explain how you would
ﬁnd the extreme points on the optimal trade-oﬀcurve.


## Page 28



## Page 29

Part III
Algorithms


## Page 30



## Page 31

Chapter 9
Unconstrained minimization
9.1
Unconstrained minimization problems
In this chapter we discuss methods for solving the unconstrained optimization
problem
minimize
f(x)
(9.1)
where f : Rn →R is convex and twice continuously diﬀerentiable (which implies
that dom f is open). We will assume that the problem is solvable, i.e., there exists
an optimal point x⋆. (More precisely, the assumptions later in the chapter will
imply that x⋆exists and is unique.) We denote the optimal value, infx f(x) =
f(x⋆), as p⋆.
Since f is diﬀerentiable and convex, a necessary and suﬃcient condition for a
point x⋆to be optimal is
∇f(x⋆) = 0
(9.2)
(see §4.2.3). Thus, solving the unconstrained minimization problem (9.1) is the
same as ﬁnding a solution of (9.2), which is a set of n equations in the n variables
x1, . . . , xn. In a few special cases, we can ﬁnd a solution to the problem (9.1) by
analytically solving the optimality equation (9.2), but usually the problem must
be solved by an iterative algorithm. By this we mean an algorithm that computes
a sequence of points x(0), x(1), . . . ∈dom f with f(x(k)) →p⋆as k →∞. Such
a sequence of points is called a minimizing sequence for the problem (9.1). The
algorithm is terminated when f(x(k)) −p⋆≤ǫ, where ǫ > 0 is some speciﬁed
tolerance.
Initial point and sublevel set
The methods described in this chapter require a suitable starting point x(0). The
starting point must lie in dom f, and in addition the sublevel set
S = {x ∈dom f | f(x) ≤f(x(0))}
(9.3)
must be closed. This condition is satisﬁed for all x(0) ∈dom f if the function f is
closed, i.e., all its sublevel sets are closed (see §A.3.3). Continuous functions with


## Page 32

458
9
Unconstrained minimization
dom f = Rn are closed, so if dom f = Rn, the initial sublevel set condition is
satisﬁed by any x(0). Another important class of closed functions are continuous
functions with open domains, for which f(x) tends to inﬁnity as x approaches
bd dom f.
9.1.1
Examples
Quadratic minimization and least-squares
The general convex quadratic minimization problem has the form
minimize
(1/2)xT Px + qT x + r,
(9.4)
where P ∈Sn
+, q ∈Rn, and r ∈R. This problem can be solved via the optimality
conditions, Px⋆+ q = 0, which is a set of linear equations. When P ≻0, there is
a unique solution, x⋆= −P −1q. In the more general case when P is not positive
deﬁnite, any solution of Px⋆= −q is optimal for (9.4); if Px⋆= −q does not
have a solution, then the problem (9.4) is unbounded below (see exercise 9.1). Our
ability to analytically solve the quadratic minimization problem (9.4) is the basis
for Newton’s method, a powerful method for unconstrained minimization described
in §9.5.
One special case of the quadratic minimization problem that arises very fre-
quently is the least-squares problem
minimize
∥Ax −b∥2
2 = xT (AT A)x −2(AT b)T x + bT b.
The optimality conditions
AT Ax⋆= AT b
are called the normal equations of the least-squares problem.
Unconstrained geometric programming
As a second example, we consider an unconstrained geometric program in convex
form,
minimize
f(x) = log
 Pm
i=1 exp(aT
i x + bi)

.
The optimality condition is
∇f(x⋆) =
1
Pm
j=1 exp(aT
j x⋆+ bj)
m
X
i=1
exp(aT
i x⋆+ bi)ai = 0,
which in general has no analytical solution, so here we must resort to an iterative
algorithm. For this problem, dom f = Rn, so any point can be chosen as the
initial point x(0).
Analytic center of linear inequalities
We consider the optimization problem
minimize
f(x) = −Pm
i=1 log(bi −aT
i x),
(9.5)


## Page 33

9.1
Unconstrained minimization problems
459
where the domain of f is the open set
dom f = {x | aT
i x < bi, i = 1, . . . , m}.
The objective function f in this problem is called the logarithmic barrier for the
inequalities aT
i x ≤bi.
The solution of (9.5), if it exists, is called the analytic
center of the inequalities. The initial point x(0) must satisfy the strict inequalities
aT
i x(0) < bi, i = 1, . . . , m. Since f is closed, the sublevel set S for any such point
is closed.
Analytic center of a linear matrix inequality
A closely related problem is
minimize
f(x) = log det F(x)−1
(9.6)
where F : Rn →Sp is aﬃne, i.e.,
F(x) = F0 + x1F1 + · · · + xnFn,
with Fi ∈Sp. Here the domain of f is
dom f = {x | F(x) ≻0}.
The objective function f is called the logarithmic barrier for the linear matrix
inequality F(x) ⪰0, and the solution (if it exists) is called the analytic center of
the linear matrix inequality. The initial point x(0) must satisfy the strict linear
matrix inequality F(x(0)) ≻0. As in the previous example, the sublevel set of any
such point will be closed, since f is closed.
9.1.2
Strong convexity and implications
In much of this chapter (with the exception of §9.6) we assume that the objective
function is strongly convex on S, which means that there exists an m > 0 such that
∇2f(x) ⪰mI
(9.7)
for all x ∈S. Strong convexity has several interesting consequences. For x, y ∈S
we have
f(y) = f(x) + ∇f(x)T (y −x) + 1
2(y −x)T ∇2f(z)(y −x)
for some z on the line segment [x, y]. By the strong convexity assumption (9.7), the
last term on the righthand side is at least (m/2)∥y −x∥2
2, so we have the inequality
f(y) ≥f(x) + ∇f(x)T (y −x) + m
2 ∥y −x∥2
2
(9.8)
for all x and y in S. When m = 0, we recover the basic inequality characterizing
convexity; for m > 0 we obtain a better lower bound on f(y) than follows from
convexity alone.


## Page 34

460
9
Unconstrained minimization
We will ﬁrst show that the inequality (9.8) can be used to bound f(x) −p⋆,
which is the suboptimality of the point x, in terms of ∥∇f(x)∥2. The righthand
side of (9.8) is a convex quadratic function of y (for ﬁxed x). Setting the gradient
with respect to y equal to zero, we ﬁnd that ˜y = x −(1/m)∇f(x) minimizes the
righthand side. Therefore we have
f(y)
≥
f(x) + ∇f(x)T (y −x) + m
2 ∥y −x∥2
2
≥
f(x) + ∇f(x)T (˜y −x) + m
2 ∥˜y −x∥2
2
=
f(x) −1
2m∥∇f(x)∥2
2.
Since this holds for any y ∈S, we have
p⋆≥f(x) −1
2m∥∇f(x)∥2
2.
(9.9)
This inequality shows that if the gradient is small at a point, then the point is
nearly optimal.
The inequality (9.9) can also be interpreted as a condition for
suboptimality which generalizes the optimality condition (9.2):
∥∇f(x)∥2 ≤(2mǫ)1/2 =⇒f(x) −p⋆≤ǫ.
(9.10)
We can also derive a bound on ∥x −x⋆∥2, the distance between x and any
optimal point x⋆, in terms of ∥∇f(x)∥2:
∥x −x⋆∥2 ≤2
m∥∇f(x)∥2.
(9.11)
To see this, we apply (9.8) with y = x⋆to obtain
p⋆= f(x⋆)
≥
f(x) + ∇f(x)T (x⋆−x) + m
2 ∥x⋆−x∥2
2
≥
f(x) −∥∇f(x)∥2∥x⋆−x∥2 + m
2 ∥x⋆−x∥2
2,
where we use the Cauchy-Schwarz inequality in the second inequality. Since p⋆≤
f(x), we must have
−∥∇f(x)∥2 ∥x⋆−x∥2 + m
2 ∥x⋆−x∥2
2 ≤0,
from which (9.11) follows. One consequence of (9.11) is that the optimal point x⋆
is unique.
Upper bound on ∇2f(x)
The inequality (9.8) implies that the sublevel sets contained in S are bounded, so in
particular, S is bounded. Therefore the maximum eigenvalue of ∇2f(x), which is a
continuous function of x on S, is bounded above on S, i.e., there exists a constant
M such that
∇2f(x) ⪯MI
(9.12)


## Page 35

9.1
Unconstrained minimization problems
461
for all x ∈S. This upper bound on the Hessian implies for any x, y ∈S,
f(y) ≤f(x) + ∇f(x)T (y −x) + M
2 ∥y −x∥2
2,
(9.13)
which is analogous to (9.8). Minimizing each side over y yields
p⋆≤f(x) −
1
2M ∥∇f(x)∥2
2,
(9.14)
the counterpart of (9.9).
Condition number of sublevel sets
From the strong convexity inequality (9.7) and the inequality (9.12), we have
mI ⪯∇2f(x) ⪯MI
(9.15)
for all x ∈S.
The ratio κ = M/m is thus an upper bound on the condition
number of the matrix ∇2f(x), i.e., the ratio of its largest eigenvalue to its smallest
eigenvalue. We can also give a geometric interpretation of (9.15) in terms of the
sublevel sets of f.
We deﬁne the width of a convex set C ⊆Rn, in the direction q, where ∥q∥2 = 1,
as
W(C, q) = sup
z∈C
qT z −inf
z∈C qT z.
The minimum width and maximum width of C are given by
Wmin =
inf
∥q∥2=1 W(C, q),
Wmax =
sup
∥q∥2=1
W(C, q).
The condition number of the convex set C is deﬁned as
cond(C) = W 2
max
W 2
min
,
i.e., the square of the ratio of its maximum width to its minimum width. The
condition number of C gives a measure of its anisotropy or eccentricity. If the
condition number of a set C is small (say, near one) it means that the set has
approximately the same width in all directions, i.e., it is nearly spherical. If the
condition number is large, it means that the set is far wider in some directions than
in others.
Example 9.1 Condition number of an ellipsoid. Let E be the ellipsoid
E = {x | (x −x0)T A−1(x −x0) ≤1},
where A ∈Sn
++. The width of E in the direction q is
sup
z∈E
qT z −inf
z∈E qT z
=
(∥A1/2q∥2 + qT x0) −(−∥A1/2q∥2 + qT x0)
=
2∥A1/2q∥2.


## Page 36

462
9
Unconstrained minimization
It follows that its minimum and maximum width are
Wmin = 2λmin(A)1/2,
Wmax = 2λmax(A)1/2,
and its condition number is
cond(E) = λmax(A)
λmin(A) = κ(A),
where κ(A) denotes the condition number of the matrix A, i.e., the ratio of its
maximum singular value to its minimum singular value. Thus the condition number
of the ellipsoid E is the same as the condition number of the matrix A that deﬁnes
it.
Now suppose f satisﬁes mI ⪯∇2f(x) ⪯MI for all x ∈S. We will derive
a bound on the condition number of the α-sublevel Cα = {x | f(x) ≤α}, where
p⋆< α ≤f(x(0)). Applying (9.13) and (9.8) with x = x⋆, we have
p⋆+ (M/2)∥y −x⋆∥2
2 ≥f(y) ≥p⋆+ (m/2)∥y −x⋆∥2
2.
This implies that Binner ⊆Cα ⊆Bouter where
Binner
=
{y | ∥y −x⋆∥2 ≤(2(α −p⋆)/M)1/2},
Bouter
=
{y | ∥y −x⋆∥2 ≤(2(α −p⋆)/m)1/2}.
In other words, the α-sublevel set contains Binner, and is contained in Bouter, which
are balls with radii
(2(α −p⋆)/M)1/2,
(2(α −p⋆)/m)1/2,
respectively. The ratio of the radii squared gives an upper bound on the condition
number of Cα:
cond(Cα) ≤M
m .
We can also give a geometric interpretation of the condition number κ(∇2f(x⋆))
of the Hessian at the optimum. From the Taylor series expansion of f around x⋆,
f(y) ≈p⋆+ 1
2(y −x⋆)T ∇2f(x⋆)(y −x⋆),
we see that, for α close to p⋆,
Cα ≈{y | (y −x⋆)T ∇2f(x⋆)(y −x⋆) ≤2(α −p⋆)},
i.e., the sublevel set is well approximated by an ellipsoid with center x⋆. Therefore
lim
α→p⋆cond(Cα) = κ(∇2f(x⋆)).
We will see that the condition number of the sublevel sets of f (which is bounded
by M/m) has a strong eﬀect on the eﬃciency of some common methods for uncon-
strained minimization.


## Page 37

9.2
Descent methods
463
The strong convexity constants
It must be kept in mind that the constants m and M are known only in rare cases,
so the inequality (9.10) cannot be used as a practical stopping criterion. It can be
considered a conceptual stopping criterion; it shows that if the gradient of f at x
is small enough, then the diﬀerence between f(x) and p⋆is small. If we terminate
an algorithm when ∥∇f(x(k))∥2 ≤η, where η is chosen small enough to be (very
likely) smaller than (mǫ)1/2, then we have f(x(k)) −p⋆≤ǫ (very likely).
In the following sections we give convergence proofs for algorithms, which in-
clude bounds on the number of iterations required before f(x(k)) −p⋆≤ǫ, where
ǫ is some positive tolerance. Many of these bounds involve the (usually unknown)
constants m and M, so the same comments apply. These results are at least con-
ceptually useful; they establish that the algorithm converges, even if the bound on
the number of iterations required to reach a given accuracy depends on constants
that are unknown.
We will encounter one important exception to this situation. In §9.6 we will
study a special class of convex functions, called self-concordant, for which we can
provide a complete convergence analysis (for Newton’s method) that does not de-
pend on any unknown constants.
9.2
Descent methods
The algorithms described in this chapter produce a minimizing sequence x(k), k =
1, . . . , where
x(k+1) = x(k) + t(k)∆x(k)
and t(k) > 0 (except when x(k) is optimal). Here the concatenated symbols ∆and
x that form ∆x are to be read as a single entity, a vector in Rn called the step or
search direction (even though it need not have unit norm), and k = 0, 1, . . . denotes
the iteration number. The scalar t(k) ≥0 is called the step size or step length at
iteration k (even though it is not equal to ∥x(k+1) −x(k)∥unless ∥∆x(k)∥= 1).
The terms ‘search step’ and ‘scale factor’ are more accurate, but ‘search direction’
and ‘step length’ are the ones widely used. When we focus on one iteration of
an algorithm, we sometimes drop the superscripts and use the lighter notation
x+ = x + t∆x, or x := x + t∆x, in place of x(k+1) = x(k) + t(k)∆x(k).
All the methods we study are descent methods, which means that
f(x(k+1)) < f(x(k)),
except when x(k) is optimal. This implies that for all k we have x(k) ∈S, the initial
sublevel set, and in particular we have x(k) ∈dom f. From convexity we know
that ∇f(x(k))T (y −x(k)) ≥0 implies f(y) ≥f(x(k)), so the search direction in a
descent method must satisfy
∇f(x(k))T ∆x(k) < 0,
i.e., it must make an acute angle with the negative gradient.
We call such a
direction a descent direction (for f, at x(k)).


## Page 38

464
9
Unconstrained minimization
The outline of a general descent method is as follows. It alternates between two
steps: determining a descent direction ∆x, and the selection of a step size t.
Algorithm 9.1 General descent method.
given a starting point x ∈dom f.
repeat
1. Determine a descent direction ∆x.
2. Line search. Choose a step size t > 0.
3. Update. x := x + t∆x.
until stopping criterion is satisﬁed.
The second step is called the line search since selection of the step size t deter-
mines where along the line {x + t∆x | t ∈R+} the next iterate will be. (A more
accurate term might be ray search.)
A practical descent method has the same general structure, but might be or-
ganized diﬀerently. For example, the stopping criterion is often checked while, or
immediately after, the descent direction ∆x is computed. The stopping criterion
is often of the form ∥∇f(x)∥2 ≤η, where η is small and positive, as suggested by
the suboptimality condition (9.9).
Exact line search
One line search method sometimes used in practice is exact line search, in which t
is chosen to minimize f along the ray {x + t∆x | t ≥0}:
t = argmins≥0 f(x + s∆x).
(9.16)
An exact line search is used when the cost of the minimization problem with one
variable, required in (9.16), is low compared to the cost of computing the search
direction itself. In some special cases the minimizer along the ray can be found an-
alytically, and in others it can be computed eﬃciently. (This is discussed in §9.7.1.)
Backtracking line search
Most line searches used in practice are inexact: the step length is chosen to ap-
proximately minimize f along the ray {x + t∆x | t ≥0}, or even to just reduce
f ‘enough’. Many inexact line search methods have been proposed. One inexact
line search method that is very simple and quite eﬀective is called backtracking line
search. It depends on two constants α, β with 0 < α < 0.5, 0 < β < 1.
Algorithm 9.2 Backtracking line search.
given a descent direction ∆x for f at x ∈dom f, α ∈(0, 0.5), β ∈(0, 1).
t := 1.
while f(x + t∆x) > f(x) + αt∇f(x)T ∆x,
t := βt.


## Page 39

9.2
Descent methods
465
t
f(x + t∆x)
t = 0
t0
f(x) + αt∇f(x)T ∆x
f(x) + t∇f(x)T ∆x
Figure 9.1 Backtracking line search. The curve shows f, restricted to the line
over which we search. The lower dashed line shows the linear extrapolation
of f, and the upper dashed line has a slope a factor of α smaller.
The
backtracking condition is that f lies below the upper dashed line, i.e., 0 ≤
t ≤t0.
The line search is called backtracking because it starts with unit step size and
then reduces it by the factor β until the stopping condition f(x + t∆x) ≤f(x) +
αt∇f(x)T ∆x holds. Since ∆x is a descent direction, we have ∇f(x)T ∆x < 0, so
for small enough t we have
f(x + t∆x) ≈f(x) + t∇f(x)T ∆x < f(x) + αt∇f(x)T ∆x,
which shows that the backtracking line search eventually terminates. The constant
α can be interpreted as the fraction of the decrease in f predicted by linear extrap-
olation that we will accept. (The reason for requiring α to be smaller than 0.5 will
become clear later.)
The backtracking condition is illustrated in ﬁgure 9.1. This ﬁgure suggests,
and it can be shown, that the backtracking exit inequality f(x + t∆x) ≤f(x) +
αt∇f(x)T ∆x holds for t ≥0 in an interval (0, t0]. It follows that the backtracking
line search stops with a step length t that satisﬁes
t = 1,
or
t ∈(βt0, t0].
The ﬁrst case occurs when the step length t = 1 satisﬁes the backtracking condition,
i.e., 1 ≤t0. In particular, we can say that the step length obtained by backtracking
line search satisﬁes
t ≥min{1, βt0}.
When dom f is not all of Rn, the condition f(x + t∆x) ≤f(x) + αt∇f(x)T ∆x
in the backtracking line search must be interpreted carefully. By our convention
that f is inﬁnite outside its domain, the inequality implies that x + t∆x ∈dom f.
In a practical implementation, we ﬁrst multiply t by β until x + t∆x ∈dom f;


## Page 40

466
9
Unconstrained minimization
then we start to check whether the inequality f(x + t∆x) ≤f(x) + αt∇f(x)T ∆x
holds.
The parameter α is typically chosen between 0.01 and 0.3, meaning that we
accept a decrease in f between 1% and 30% of the prediction based on the linear
extrapolation. The parameter β is often chosen to be between 0.1 (which corre-
sponds to a very crude search) and 0.8 (which corresponds to a less crude search).
9.3
Gradient descent method
A natural choice for the search direction is the negative gradient ∆x = −∇f(x).
The resulting algorithm is called the gradient algorithm or gradient descent method.
Algorithm 9.3 Gradient descent method.
given a starting point x ∈dom f.
repeat
1. ∆x := −∇f(x).
2. Line search. Choose step size t via exact or backtracking line search.
3. Update. x := x + t∆x.
until stopping criterion is satisﬁed.
The stopping criterion is usually of the form ∥∇f(x)∥2 ≤η, where η is small and
positive. In most implementations, this condition is checked after step 1, rather
than after the update.
9.3.1
Convergence analysis
In this section we present a simple convergence analysis for the gradient method,
using the lighter notation x+ = x + t∆x for x(k+1) = x(k) + t(k)∆x(k), where ∆x =
−∇f(x). We assume f is strongly convex on S, so there are positive constants m
and M such that mI ⪯∇2f(x) ⪯MI for all x ∈S. Deﬁne the function ˜f : R →R
by ˜f(t) = f(x −t∇f(x)), i.e., f as a function of the step length t in the negative
gradient direction. In the following discussion we will only consider t for which
x −t∇f(x) ∈S. From the inequality (9.13), with y = x −t∇f(x), we obtain a
quadratic upper bound on ˜f:
˜f(t) ≤f(x) −t∥∇f(x)∥2
2 + Mt2
2
∥∇f(x)∥2
2.
(9.17)
Analysis for exact line search
We now assume that an exact line search is used, and minimize over t both sides
of the inequality (9.17). On the lefthand side we get ˜f(texact), where texact is the
