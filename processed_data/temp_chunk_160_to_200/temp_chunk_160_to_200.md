# temp_chunk_160_to_200



## Page 1

4.3
Linear optimization problems
147
P
x⋆
−c
Figure 4.4 Geometric interpretation of an LP. The feasible set P, which
is a polyhedron, is shaded. The objective cT x is linear, so its level curves
are hyperplanes orthogonal to c (shown as dashed lines). The point x⋆is
optimal; it is the point in P as far as possible in the direction −c.
twise nonnegativity constraints x ⪰0:
minimize
cT x
subject to
Ax = b
x ⪰0.
(4.28)
If the LP has no equality constraints, it is called an inequality form LP, usually
written as
minimize
cT x
subject to
Ax ⪯b.
(4.29)
Converting LPs to standard form
It is sometimes useful to transform a general LP (4.27) to one in standard form (4.28)
(for example in order to use an algorithm for standard form LPs). The ﬁrst step
is to introduce slack variables si for the inequalities, which results in
minimize
cT x + d
subject to
Gx + s = h
Ax = b
s ⪰0.
The second step is to express the variable x as the diﬀerence of two nonnegative
variables x+ and x−, i.e., x = x+ −x−, x+, x−⪰0. This yields the problem
minimize
cT x+ −cT x−+ d
subject to
Gx+ −Gx−+ s = h
Ax+ −Ax−= b
x+ ⪰0,
x−⪰0,
s ⪰0,


## Page 2

148
4
Convex optimization problems
which is an LP in standard form, with variables x+, x−, and s. (For equivalence
of this problem and the original one (4.27), see exercise 4.10.)
These techniques for manipulating problems (along with many others we will
see in the examples and exercises) can be used to formulate many problems as linear
programs. With some abuse of terminology, it is common to refer to a problem
that can be formulated as an LP as an LP, even if it does not have the form (4.27).
4.3.1
Examples
LPs arise in a vast number of ﬁelds and applications; here we give a few typical
examples.
Diet problem
A healthy diet contains m diﬀerent nutrients in quantities at least equal to b1, . . . ,
bm. We can compose such a diet by choosing nonnegative quantities x1, . . . , xn of
n diﬀerent foods. One unit quantity of food j contains an amount aij of nutrient
i, and has a cost of cj. We want to determine the cheapest diet that satisﬁes the
nutritional requirements. This problem can be formulated as the LP
minimize
cT x
subject to
Ax ⪰b
x ⪰0.
Several variations on this problem can also be formulated as LPs. For example,
we can insist on an exact amount of a nutrient in the diet (which gives a linear
equality constraint), or we can impose an upper bound on the amount of a nutrient,
in addition to the lower bound as above.
Chebyshev center of a polyhedron
We consider the problem of ﬁnding the largest Euclidean ball that lies in a poly-
hedron described by linear inequalities,
P = {x ∈Rn | aT
i x ≤bi, i = 1, . . . , m}.
(The center of the optimal ball is called the Chebyshev center of the polyhedron;
it is the point deepest inside the polyhedron, i.e., farthest from the boundary;
see §8.5.1.) We represent the ball as
B = {xc + u | ∥u∥2 ≤r}.
The variables in the problem are the center xc ∈Rn and the radius r; we wish to
maximize r subject to the constraint B ⊆P.
We start by considering the simpler constraint that B lies in one halfspace
aT
i x ≤bi, i.e.,
∥u∥2 ≤r =⇒aT
i (xc + u) ≤bi.
(4.30)
Since
sup{aT
i u | ∥u∥2 ≤r} = r∥ai∥2


## Page 3

4.3
Linear optimization problems
149
we can write (4.30) as
aT
i xc + r∥ai∥2 ≤bi,
(4.31)
which is a linear inequality in xc and r. In other words, the constraint that the
ball lies in the halfspace determined by the inequality aT
i x ≤bi can be written as
a linear inequality.
Therefore B ⊆P if and only if (4.31) holds for all i = 1, . . . , m. Hence the
Chebyshev center can be determined by solving the LP
maximize
r
subject to
aT
i xc + r∥ai∥2 ≤bi,
i = 1, . . . , m,
with variables r and xc. (For more on the Chebyshev center, see §8.5.1.)
Dynamic activity planning
We consider the problem of choosing, or planning, the activity levels of n activities,
or sectors of an economy, over N time periods. We let xj(t) ≥0, t = 1, . . . , N,
denote the activity level of sector j, in period t. The activities both consume and
produce products or goods in proportion to their activity levels. The amount of
good i produced per unit of activity j is given by aij. Similarly, the amount of good i
consumed per unit of activity j is bij. The total amount of goods produced in period
t is given by Ax(t) ∈Rm, and the amount of goods consumed is Bx(t) ∈Rm.
(Although we refer to these products as ‘goods’, they can also include unwanted
products such as pollutants.)
The goods consumed in a period cannot exceed those produced in the previous
period: we must have Bx(t + 1) ⪯Ax(t) for t = 1, . . . , N. A vector g0 ∈Rm of
initial goods is given, which constrains the ﬁrst period activity levels: Bx(1) ⪯g0.
The (vectors of) excess goods not consumed by the activities are given by
s(0)
=
g0 −Bx(1)
s(t)
=
Ax(t) −Bx(t + 1),
t = 1, . . . , N −1
s(N)
=
Ax(N).
The objective is to maximize a discounted total value of excess goods:
cT s(0) + γcT s(1) + · · · + γNcT s(N),
where c ∈Rm gives the values of the goods, and γ > 0 is a discount factor. (The
value ci is negative if the ith product is unwanted, e.g., a pollutant; |ci| is then the
cost of disposal per unit.)
Putting it all together we arrive at the LP
maximize
cT s(0) + γcT s(1) + · · · + γNcT s(N)
subject to
x(t) ⪰0,
t = 1, . . . , N
s(t) ⪰0,
t = 0, . . . , N
s(0) = g0 −Bx(1)
s(t) = Ax(t) −Bx(t + 1),
t = 1, . . . , N −1
s(N) = Ax(N),
with variables x(1), . . . , x(N), s(0), . . . , s(N). This problem is a standard form LP;
the variables s(t) are the slack variables associated with the constraints Bx(t+1) ⪯
Ax(t).


## Page 4

150
4
Convex optimization problems
Chebyshev inequalities
We consider a probability distribution for a discrete random variable x on a set
{u1, . . . , un} ⊆R with n elements. We describe the distribution of x by a vector
p ∈Rn, where
pi = prob(x = ui),
so p satisﬁes p ⪰0 and 1T p = 1. Conversely, if p satisﬁes p ⪰0 and 1T p = 1, then
it deﬁnes a probability distribution for x. We assume that ui are known and ﬁxed,
but the distribution p is not known.
If f is any function of x, then
E f =
n
X
i=1
pif(ui)
is a linear function of p. If S is any subset of R, then
prob(x ∈S) =
X
ui∈S
pi
is a linear function of p.
Although we do not know p, we are given prior knowledge of the following form:
We know upper and lower bounds on expected values of some functions of x, and
probabilities of some subsets of R. This prior knowledge can be expressed as linear
inequality constraints on p,
αi ≤aT
i p ≤βi,
i = 1, . . . , m.
The problem is to give lower and upper bounds on E f0(x) = aT
0 p, where f0 is some
function of x.
To ﬁnd a lower bound we solve the LP
minimize
aT
0 p
subject to
p ⪰0,
1T p = 1
αi ≤aT
i p ≤βi,
i = 1, . . . , m,
with variable p. The optimal value of this LP gives the lowest possible value of
E f0(X) for any distribution that is consistent with the prior information. More-
over, the bound is sharp: the optimal solution gives a distribution that is consistent
with the prior information and achieves the lower bound. In a similar way, we can
ﬁnd the best upper bound by maximizing aT
0 p subject to the same constraints. (We
will consider Chebyshev inequalities in more detail in §7.4.1.)
Piecewise-linear minimization
Consider the (unconstrained) problem of minimizing the piecewise-linear, convex
function
f(x) =
max
i=1,...,m(aT
i x + bi).
This problem can be transformed to an equivalent LP by ﬁrst forming the epigraph
problem,
minimize
t
subject to
maxi=1,...,m(aT
i x + bi) ≤t,


## Page 5

4.3
Linear optimization problems
151
and then expressing the inequality as a set of m separate inequalities:
minimize
t
subject to
aT
i x + bi ≤t,
i = 1, . . . , m.
This is an LP (in inequality form), with variables x and t.
4.3.2
Linear-fractional programming
The problem of minimizing a ratio of aﬃne functions over a polyhedron is called a
linear-fractional program:
minimize
f0(x)
subject to
Gx ⪯h
Ax = b
(4.32)
where the objective function is given by
f0(x) = cT x + d
eT x + f ,
dom f0 = {x | eT x + f > 0}.
The objective function is quasiconvex (in fact, quasilinear) so linear-fractional pro-
grams are quasiconvex optimization problems.
Transforming to a linear program
If the feasible set
{x | Gx ⪯h, Ax = b, eT x + f > 0}
is nonempty, the linear-fractional program (4.32) can be transformed to an equiv-
alent linear program
minimize
cT y + dz
subject to
Gy −hz ⪯0
Ay −bz = 0
eT y + fz = 1
z ≥0
(4.33)
with variables y, z.
To show the equivalence, we ﬁrst note that if x is feasible in (4.32) then the
pair
y =
x
eT x + f ,
z =
1
eT x + f
is feasible in (4.33), with the same objective value cT y +dz = f0(x). It follows that
the optimal value of (4.32) is greater than or equal to the optimal value of (4.33).
Conversely, if (y, z) is feasible in (4.33), with z̸ = 0, then x = y/z is feasible
in (4.32), with the same objective value f0(x) = cT y + dz.
If (y, z) is feasible
in (4.33) with z = 0, and x0 is feasible for (4.32), then x = x0 + ty is feasible
in (4.32) for all t ≥0. Moreover, limt→∞f0(x0 + ty) = cT y + dz, so we can ﬁnd
feasible points in (4.32) with objective values arbitrarily close to the objective value
of (y, z). We conclude that the optimal value of (4.32) is less than or equal to the
optimal value of (4.33).


## Page 6

152
4
Convex optimization problems
Generalized linear-fractional programming
A generalization of the linear-fractional program (4.32) is the generalized linear-
fractional program in which
f0(x) = max
i=1,...,r
cT
i x + di
eT
i x + fi
,
dom f0 = {x | eT
i x + fi > 0, i = 1, . . . , r}.
The objective function is the pointwise maximum of r quasiconvex functions, and
therefore quasiconvex, so this problem is quasiconvex. When r = 1 it reduces to
the standard linear-fractional program.
Example 4.7
Von Neumann growth problem.
We consider an economy with n
sectors, and activity levels xi > 0 in the current period, and activity levels x+
i > 0 in
the next period. (In this problem we only consider one period.) There are m goods
which are consumed, and also produced, by the activity: An activity level x consumes
goods Bx ∈Rm, and produces goods Ax. The goods consumed in the next period
cannot exceed the goods produced in the current period, i.e., Bx+ ⪯Ax. The growth
rate in sector i, over the period, is given by x+
i /xi.
Von Neumann’s growth problem is to ﬁnd an activity level vector x that maximizes
the minimum growth rate across all sectors of the economy. This problem can be
expressed as a generalized linear-fractional problem
maximize
mini=1,...,n x+
i /xi
subject to
x+ ⪰0
Bx+ ⪯Ax
with domain {(x, x+) | x ≻0}. Note that this problem is homogeneous in x and x+,
so we can replace the implicit constraint x ≻0 by the explicit constraint x ⪰1.
4.4
Quadratic optimization problems
The convex optimization problem (4.15) is called a quadratic program (QP) if the
objective function is (convex) quadratic, and the constraint functions are aﬃne. A
quadratic program can be expressed in the form
minimize
(1/2)xT Px + qT x + r
subject to
Gx ⪯h
Ax = b,
(4.34)
where P ∈Sn
+, G ∈Rm×n, and A ∈Rp×n. In a quadratic program, we minimize
a convex quadratic function over a polyhedron, as illustrated in ﬁgure 4.5.
If the objective in (4.15) as well as the inequality constraint functions are (con-
vex) quadratic, as in
minimize
(1/2)xT P0x + qT
0 x + r0
subject to
(1/2)xT Pix + qT
i x + ri ≤0,
i = 1, . . . , m
Ax = b,
(4.35)


## Page 7

4.4
Quadratic optimization problems
153
P
x⋆
−∇f0(x⋆)
Figure 4.5 Geometric illustration of QP. The feasible set P, which is a poly-
hedron, is shown shaded. The contour lines of the objective function, which
is convex quadratic, are shown as dashed curves. The point x⋆is optimal.
where Pi ∈Sn
+, i = 0, 1 . . . , m, the problem is called a quadratically constrained
quadratic program (QCQP). In a QCQP, we minimize a convex quadratic function
over a feasible region that is the intersection of ellipsoids (when Pi ≻0).
Quadratic programs include linear programs as a special case, by taking P = 0
in (4.34). Quadratically constrained quadratic programs include quadratic pro-
grams (and therefore also linear programs) as a special case, by taking Pi = 0
in (4.35), for i = 1, . . . , m.
4.4.1
Examples
Least-squares and regression
The problem of minimizing the convex quadratic function
∥Ax −b∥2
2 = xT AT Ax −2bT Ax + bT b
is an (unconstrained) QP. It arises in many ﬁelds and has many names, e.g., re-
gression analysis or least-squares approximation. This problem is simple enough to
have the well known analytical solution x = A†b, where A† is the pseudo-inverse
of A (see §A.5.4).
When linear inequality constraints are added, the problem is called constrained
regression or constrained least-squares, and there is no longer a simple analytical
solution. As an example we can consider regression with lower and upper bounds
on the variables, i.e.,
minimize
∥Ax −b∥2
2
subject to
li ≤xi ≤ui,
i = 1, . . . , n,


## Page 8

154
4
Convex optimization problems
which is a QP. (We will study least-squares and regression problems in far more
depth in chapters 6 and 7.)
Distance between polyhedra
The (Euclidean) distance between the polyhedra P1 = {x | A1x ⪯b1} and P2 =
{x | A2x ⪯b2} in Rn is deﬁned as
dist(P1, P2) = inf{∥x1 −x2∥2 | x1 ∈P1, x2 ∈P2}.
If the polyhedra intersect, the distance is zero.
To ﬁnd the distance between P1 and P2, we can solve the QP
minimize
∥x1 −x2∥2
2
subject to
A1x1 ⪯b1,
A2x2 ⪯b2,
with variables x1, x2 ∈Rn. This problem is infeasible if and only if one of the
polyhedra is empty. The optimal value is zero if and only if the polyhedra intersect,
in which case the optimal x1 and x2 are equal (and is a point in the intersection
P1∩P2). Otherwise the optimal x1 and x2 are the points in P1 and P2, respectively,
that are closest to each other. (We will study geometric problems involving distance
in more detail in chapter 8.)
Bounding variance
We consider again the Chebyshev inequalities example (page 150), where the vari-
able is an unknown probability distribution given by p ∈Rn, about which we have
some prior information. The variance of a random variable f(x) is given by
E f 2 −(E f)2 =
n
X
i=1
f 2
i pi −
 n
X
i=1
fipi
!2
,
(where fi = f(ui)), which is a concave quadratic function of p.
It follows that we can maximize the variance of f(x), subject to the given prior
information, by solving the QP
maximize
Pn
i=1 f 2
i pi −(Pn
i=1 fipi)2
subject to
p ⪰0,
1T p = 1
αi ≤aT
i p ≤βi,
i = 1, . . . , m.
The optimal value gives the maximum possible variance of f(x), over all distribu-
tions that are consistent with the prior information; the optimal p gives a distri-
bution that achieves this maximum variance.
Linear program with random cost
We consider an LP,
minimize
cT x
subject to
Gx ⪯h
Ax = b,


## Page 9

4.4
Quadratic optimization problems
155
with variable x ∈Rn.
We suppose that the cost function (vector) c ∈Rn is
random, with mean value c and covariance E(c −c)(c −c)T = Σ. (We assume
for simplicity that the other problem parameters are deterministic.) For a given
x ∈Rn, the cost cT x is a (scalar) random variable with mean E cT x = cT x and
variance
var(cT x) = E(cT x −E cT x)2 = xT Σx.
In general there is a trade-oﬀbetween small expected cost and small cost vari-
ance. One way to take variance into account is to minimize a linear combination
of the expected value and the variance of the cost, i.e.,
E cT x + γ var(cT x),
which is called the risk-sensitive cost. The parameter γ ≥0 is called the risk-
aversion parameter, since it sets the relative values of cost variance and expected
value. (For γ > 0, we are willing to trade oﬀan increase in expected cost for a
suﬃciently large decrease in cost variance).
To minimize the risk-sensitive cost we solve the QP
minimize
cT x + γxT Σx
subject to
Gx ⪯h
Ax = b.
Markowitz portfolio optimization
We consider a classical portfolio problem with n assets or stocks held over a period
of time. We let xi denote the amount of asset i held throughout the period, with
xi in dollars, at the price at the beginning of the period. A normal long position
in asset i corresponds to xi > 0; a short position in asset i (i.e., the obligation to
buy the asset at the end of the period) corresponds to xi < 0. We let pi denote
the relative price change of asset i over the period, i.e., its change in price over
the period divided by its price at the beginning of the period. The overall return
on the portfolio is r = pT x (given in dollars). The optimization variable is the
portfolio vector x ∈Rn.
A wide variety of constraints on the portfolio can be considered. The simplest
set of constraints is that xi ≥0 (i.e., no short positions) and 1T x = B (i.e., the
total budget to be invested is B, which is often taken to be one).
We take a stochastic model for price changes: p ∈Rn is a random vector, with
known mean p and covariance Σ. Therefore with portfolio x ∈Rn, the return r
is a (scalar) random variable with mean pT x and variance xT Σx. The choice of
portfolio x involves a trade-oﬀbetween the mean of the return, and its variance.
The classical portfolio optimization problem, introduced by Markowitz, is the
QP
minimize
xT Σx
subject to
pT x ≥rmin
1T x = 1,
x ⪰0,
where x, the portfolio, is the variable. Here we ﬁnd the portfolio that minimizes
the return variance (which is associated with the risk of the portfolio) subject to


## Page 10

156
4
Convex optimization problems
achieving a minimum acceptable mean return rmin, and satisfying the portfolio
budget and no-shorting constraints.
Many extensions are possible. One standard extension, for example, is to allow
short positions, i.e., xi < 0. To do this we introduce variables xlong and xshort,
with
xlong ⪰0,
xshort ⪰0,
x = xlong −xshort,
1T xshort ≤η1T xlong.
The last constraint limits the total short position at the beginning of the period to
some fraction η of the total long position at the beginning of the period.
As another extension we can include linear transaction costs in the portfolio
optimization problem. Starting from a given initial portfolio xinit we buy and sell
assets to achieve the portfolio x, which we then hold over the period as described
above. We are charged a transaction fee for buying and selling assets, which is
proportional to the amount bought or sold. To handle this, we introduce variables
ubuy and usell, which determine the amount of each asset we buy and sell before
the holding period. We have the constraints
x = xinit + ubuy −usell,
ubuy ⪰0,
usell ⪰0.
We replace the simple budget constraint 1T x = 1 with the condition that the initial
buying and selling, including transaction fees, involves zero net cash:
(1 −fsell)1T usell = (1 + fbuy)1T ubuy
Here the lefthand side is the total proceeds from selling assets, less the selling
transaction fee, and the righthand side is the total cost, including transaction fee,
of buying assets. The constants fbuy ≥0 and fsell ≥0 are the transaction fee rates
for buying and selling (assumed the same across assets, for simplicity).
The problem of minimizing return variance, subject to a minimum mean return,
and the budget and trading constraints, is a QP with variables x, ubuy, usell.
4.4.2
Second-order cone programming
A problem that is closely related to quadratic programming is the second-order
cone program (SOCP):
minimize
f T x
subject to
∥Aix + bi∥2 ≤cT
i x + di,
i = 1, . . . , m
Fx = g,
(4.36)
where x ∈Rn is the optimization variable, Ai ∈Rni×n, and F ∈Rp×n. We call a
constraint of the form
∥Ax + b∥2 ≤cT x + d,
where A ∈Rk×n, a second-order cone constraint, since it is the same as requiring
the aﬃne function (Ax + b, cT x + d) to lie in the second-order cone in Rk+1.
When ci = 0, i = 1, . . . , m, the SOCP (4.36) is equivalent to a QCQP (which
is obtained by squaring each of the constraints). Similarly, if Ai = 0, i = 1, . . . , m,
then the SOCP (4.36) reduces to a (general) LP. Second-order cone programs are,
however, more general than QCQPs (and of course, LPs).


## Page 11

4.4
Quadratic optimization problems
157
Robust linear programming
We consider a linear program in inequality form,
minimize
cT x
subject to
aT
i x ≤bi,
i = 1, . . . , m,
in which there is some uncertainty or variation in the parameters c, ai, bi. To
simplify the exposition we assume that c and bi are ﬁxed, and that ai are known
to lie in given ellipsoids:
ai ∈Ei = {ai + Piu | ∥u∥2 ≤1},
where Pi ∈Rn×n. (If Pi is singular we obtain ‘ﬂat’ ellipsoids, of dimension rank Pi;
Pi = 0 means that ai is known perfectly.)
We will require that the constraints be satisﬁed for all possible values of the
parameters ai, which leads us to the robust linear program
minimize
cT x
subject to
aT
i x ≤bi for all ai ∈Ei,
i = 1, . . . , m.
(4.37)
The robust linear constraint, aT
i x ≤bi for all ai ∈Ei, can be expressed as
sup{aT
i x | ai ∈Ei} ≤bi,
the lefthand side of which can be expressed as
sup{aT
i x | ai ∈Ei}
=
aT
i x + sup{uT P T
i x | ∥u∥2 ≤1}
=
aT
i x + ∥P T
i x∥2.
Thus, the robust linear constraint can be expressed as
aT
i x + ∥P T
i x∥2 ≤bi,
which is evidently a second-order cone constraint. Hence the robust LP (4.37) can
be expressed as the SOCP
minimize
cT x
subject to
aT
i x + ∥P T
i x∥2 ≤bi,
i = 1, . . . , m.
Note that the additional norm terms act as regularization terms; they prevent x
from being large in directions with considerable uncertainty in the parameters ai.
Linear programming with random constraints
The robust LP described above can also be considered in a statistical framework.
Here we suppose that the parameters ai are independent Gaussian random vectors,
with mean ai and covariance Σi. We require that each constraint aT
i x ≤bi should
hold with a probability (or conﬁdence) exceeding η, where η ≥0.5, i.e.,
prob(aT
i x ≤bi) ≥η.
(4.38)


## Page 12

158
4
Convex optimization problems
We will show that this probability constraint can be expressed as a second-order
cone constraint.
Letting u = aT
i x, with σ2 denoting its variance, this constraint can be written
as
prob
u −u
σ
≤bi −u
σ

≥η.
Since (u −u)/σ is a zero mean unit variance Gaussian variable, the probability
above is simply Φ((bi −u)/σ), where
Φ(z) =
1
√
2π
Z z
−∞
e−t2/2 dt
is the cumulative distribution function of a zero mean unit variance Gaussian ran-
dom variable. Thus the probability constraint (4.38) can be expressed as
bi −u
σ
≥Φ−1(η),
or, equivalently,
u + Φ−1(η)σ ≤bi.
From u = aT
i x and σ = (xT Σix)1/2 we obtain
aT
i x + Φ−1(η)∥Σ1/2
i
x∥2 ≤bi.
By our assumption that η ≥1/2, we have Φ−1(η) ≥0, so this constraint is a
second-order cone constraint.
In summary, the problem
minimize
cT x
subject to
prob(aT
i x ≤bi) ≥η,
i = 1, . . . , m
can be expressed as the SOCP
minimize
cT x
subject to
aT
i x + Φ−1(η)∥Σ1/2
i
x∥2 ≤bi,
i = 1, . . . , m.
(We will consider robust convex optimization problems in more depth in chapter 6.
See also exercises 4.13, 4.28, and 4.59.)
Example 4.8 Portfolio optimization with loss risk constraints. We consider again the
classical Markowitz portfolio problem described above (page 155). We assume here
that the price change vector p ∈Rn is a Gaussian random variable, with mean p
and covariance Σ. Therefore the return r is a Gaussian random variable with mean
r = pT x and variance σ2
r = xT Σx.
Consider a loss risk constraint of the form
prob(r ≤α) ≤β,
(4.39)
where α is a given unwanted return level (e.g., a large loss) and β is a given maximum
probability.


## Page 13

4.4
Quadratic optimization problems
159
As in the stochastic interpretation of the robust LP given above, we can express this
constraint using the cumulative distribution function Φ of a unit Gaussian random
variable. The inequality (4.39) is equivalent to
pT x + Φ−1(β) ∥Σ1/2x∥2 ≥α.
Provided β ≤1/2 (i.e., Φ−1(β) ≤0), this loss risk constraint is a second-order cone
constraint. (If β > 1/2, the loss risk constraint becomes nonconvex in x.)
The problem of maximizing the expected return subject to a bound on the loss
risk (with β ≤1/2), can therefore be cast as an SOCP with one second-order cone
constraint:
maximize
pT x
subject to
pT x + Φ−1(β) ∥Σ1/2x∥2 ≥α
x ⪰0,
1T x = 1.
There are many extensions of this problem. For example, we can impose several loss
risk constraints, i.e.,
prob(r ≤αi) ≤βi,
i = 1, . . . , k,
(where βi ≤1/2), which expresses the risks (βi) we are willing to accept for various
levels of loss (αi).
Minimal surface
Consider a diﬀerentiable function f : R2 →R with dom f = C. The surface area
of its graph is given by
A =
Z
C
q
1 + ∥∇f(x)∥2
2 dx =
Z
C
∥(∇f(x), 1)∥2 dx,
which is a convex functional of f.
The minimal surface problem is to ﬁnd the
function f that minimizes A subject to some constraints, for example, some given
values of f on the boundary of C.
We will approximate this problem by discretizing the function f.
Let C =
[0, 1] × [0, 1], and let fij denote the value of f at the point (i/K, j/K), for i, j =
0, . . . , K.
An approximate expression for the gradient of f at the point x =
(i/K, j/K) can be found using forward diﬀerences:
∇f(x) ≈K

fi+1,j −fi,j
fi,j+1 −fi,j

.
Substituting this into the expression for the area of the graph, and approximating
the integral as a sum, we obtain an approximation for the area of the graph:
A ≈Adisc =
1
K2
K−1
X
i,j=0



K(fi+1,j −fi,j)
K(fi,j+1 −fi,j)
1



2
The discretized area approximation Adisc is a convex function of fij.
We can consider a wide variety of constraints on fij, such as equality or in-
equality constraints on any of its entries (for example, on the boundary values), or


## Page 14

160
4
Convex optimization problems
on its moments. As an example, we consider the problem of ﬁnding the minimal
area surface with ﬁxed boundary values on the left and right edges of the square:
minimize
Adisc
subject to
f0j = lj,
j = 0, . . . , K
fKj = rj,
j = 0, . . . , K
(4.40)
where fij, i, j = 0, . . . , K, are the variables, and lj, rj are the given boundary
values on the left and right sides of the square.
We can transform the problem (4.40) into an SOCP by introducing new vari-
ables tij, i, j = 0, . . . , K −1:
minimize
(1/K2) PK−1
i,j=0 tij
subject to



K(fi+1,j −fi,j)
K(fi,j+1 −fi,j)
1



2
≤tij,
i, j = 0, . . . , K −1
f0j = lj,
j = 0, . . . , K
fKj = rj,
j = 0, . . . , K.
4.5
Geometric programming
In this section we describe a family of optimization problems that are not convex
in their natural form. These problems can, however, be transformed to convex op-
timization problems, by a change of variables and a transformation of the objective
and constraint functions.
4.5.1
Monomials and posynomials
A function f : Rn →R with dom f = Rn
++, deﬁned as
f(x) = cxa1
1 xa2
2 · · · xan
n ,
(4.41)
where c > 0 and ai ∈R, is called a monomial function, or simply, a monomial.
The exponents ai of a monomial can be any real numbers, including fractional or
negative, but the coeﬃcient c can only be positive. (The term ‘monomial’ conﬂicts
with the standard deﬁnition from algebra, in which the exponents must be non-
negative integers, but this should not cause any confusion.) A sum of monomials,
i.e., a function of the form
f(x) =
K
X
k=1
ckxa1k
1
xa2k
2
· · · xank
n
,
(4.42)
where ck > 0, is called a posynomial function (with K terms), or simply, a posyn-
omial.


## Page 15

4.5
Geometric programming
161
Posynomials are closed under addition, multiplication, and nonnegative scal-
ing. Monomials are closed under multiplication and division. If a posynomial is
multiplied by a monomial, the result is a posynomial; similarly, a posynomial can
be divided by a monomial, with the result a posynomial.
4.5.2
Geometric programming
An optimization problem of the form
minimize
f0(x)
subject to
fi(x) ≤1,
i = 1, . . . , m
hi(x) = 1,
i = 1, . . . , p
(4.43)
where f0, . . . , fm are posynomials and h1, . . . , hp are monomials, is called a geomet-
ric program (GP). The domain of this problem is D = Rn
++; the constraint x ≻0
is implicit.
Extensions of geometric programming
Several extensions are readily handled. If f is a posynomial and h is a monomial,
then the constraint f(x) ≤h(x) can be handled by expressing it as f(x)/h(x) ≤1
(since f/h is posynomial).
This includes as a special case a constraint of the
form f(x) ≤a, where f is posynomial and a > 0. In a similar way if h1 and h2
are both nonzero monomial functions, then we can handle the equality constraint
h1(x) = h2(x) by expressing it as h1(x)/h2(x) = 1 (since h1/h2 is monomial). We
can maximize a nonzero monomial objective function, by minimizing its inverse
(which is also a monomial).
For example, consider the problem
maximize
x/y
subject to
2 ≤x ≤3
x2 + 3y/z ≤√y
x/y = z2,
with variables x, y, z ∈R (and the implicit constraint x, y, z > 0).
Using
the simple transformations described above, we obtain the equivalent standard
form GP
minimize
x−1y
subject to
2x−1 ≤1,
(1/3)x ≤1
x2y−1/2 + 3y1/2z−1 ≤1
xy−1z−2 = 1.
We will refer to a problem like this one, that is easily transformed to an equiva-
lent GP in the standard form (4.43), also as a GP. (In the same way that we refer
to a problem easily transformed to an LP as an LP.)


## Page 16

162
4
Convex optimization problems
4.5.3
Geometric program in convex form
Geometric programs are not (in general) convex optimization problems, but they
can be transformed to convex problems by a change of variables and a transforma-
tion of the objective and constraint functions.
We will use the variables deﬁned as yi = log xi, so xi = eyi. If f is the monomial
function of x given in (4.41), i.e.,
f(x) = cxa1
1 xa2
2 · · · xan
n ,
then
f(x)
=
f(ey1, . . . , eyn)
=
c(ey1)a1 · · · (eyn)an
=
eaT y+b,
where b = log c. The change of variables yi = log xi turns a monomial function
into the exponential of an aﬃne function.
Similarly, if f is the posynomial given by (4.42), i.e.,
f(x) =
K
X
k=1
ckxa1k
1
xa2k
2
· · · xank
n
,
then
f(x) =
K
X
k=1
eaT
k y+bk,
where ak = (a1k, . . . , ank) and bk = log ck. After the change of variables, a posyn-
omial becomes a sum of exponentials of aﬃne functions.
The geometric program (4.43) can be expressed in terms of the new variable y
as
minimize
PK0
k=1 eaT
0ky+b0k
subject to
PKi
k=1 eaT
iky+bik ≤1,
i = 1, . . . , m
egT
i y+hi = 1,
i = 1, . . . , p,
where aik ∈Rn, i = 0, . . . , m, contain the exponents of the posynomial inequality
constraints, and gi ∈Rn, i = 1, . . . , p, contain the exponents of the monomial
equality constraints of the original geometric program.
Now we transform the objective and constraint functions, by taking the loga-
rithm. This results in the problem
minimize
˜f0(y) = log
PK0
k=1 eaT
0ky+b0k

subject to
˜fi(y) = log
PKi
k=1 eaT
iky+bik

≤0,
i = 1, . . . , m
˜hi(y) = gT
i y + hi = 0,
i = 1, . . . , p.
(4.44)
Since the functions ˜fi are convex, and ˜hi are aﬃne, this problem is a convex
optimization problem. We refer to it as a geometric program in convex form. To


## Page 17

4.5
Geometric programming
163
distinguish it from the original geometric program, we refer to (4.43) as a geometric
program in posynomial form.
Note that the transformation between the posynomial form geometric pro-
gram (4.43) and the convex form geometric program (4.44) does not involve any
computation; the problem data for the two problems are the same.
It simply
changes the form of the objective and constraint functions.
If the posynomial objective and constraint functions all have only one term,
i.e., are monomials, then the convex form geometric program (4.44) reduces to a
(general) linear program. We can therefore consider geometric programming to be
a generalization, or extension, of linear programming.
4.5.4
Examples
Frobenius norm diagonal scaling
Consider a matrix M ∈Rn×n, and the associated linear function that maps u
into y = Mu. Suppose we scale the coordinates, i.e., change variables to ˜u = Du,
˜y = Dy, where D is diagonal, with Dii > 0. In the new coordinates the linear
function is given by ˜y = DMD−1˜u.
Now suppose we want to choose the scaling in such a way that the resulting
matrix, DMD−1, is small. We will use the Frobenius norm (squared) to measure
the size of the matrix:
∥DMD−1∥2
F
=
tr
 DMD−1T  DMD−1
=
n
X
i,j=1
 DMD−12
ij
=
n
X
i,j=1
M 2
ijd2
i /d2
j,
where D = diag(d). Since this is a posynomial in d, the problem of choosing the
scaling d to minimize the Frobenius norm is an unconstrained geometric program,
minimize
Pn
i,j=1 M 2
ijd2
i /d2
j,
with variable d. The only exponents in this geometric program are 0, 2, and −2.
Design of a cantilever beam
We consider the design of a cantilever beam, which consists of N segments, num-
bered from right to left as 1, . . . , N, as shown in ﬁgure 4.6. Each segment has unit
length and a uniform rectangular cross-section with width wi and height hi. A
vertical load (force) F is applied at the right end of the beam. This load causes
the beam to deﬂect (downward), and induces stress in each segment of the beam.
We assume that the deﬂections are small, and that the material is linearly elastic,
with Young’s modulus E.


## Page 18

164
4
Convex optimization problems
F
segment 4
segment 3
segment 2
segment 1
Figure 4.6 Segmented cantilever beam with 4 segments. Each segment has
unit length and a rectangular proﬁle. A vertical force F is applied at the
right end of the beam.
The design variables in the problem are the widths wi and heights hi of the N
segments. We seek to minimize the total volume of the beam (which is proportional
to its weight),
w1h1 + · · · + wNhN,
subject to some design constraints. We impose upper and lower bounds on width
and height of the segments,
wmin ≤wi ≤wmax,
hmin ≤hi ≤hmax,
i = 1, . . . , N,
as well as the aspect ratios,
Smin ≤hi/wi ≤Smax.
In addition, we have a limit on the maximum allowable stress in the material, and
on the vertical deﬂection at the end of the beam.
We ﬁrst consider the maximum stress constraint. The maximum stress in seg-
ment i, which we denote σi, is given by σi = 6iF/(wih2
i ). We impose the constraints
6iF
wih2
i
≤σmax,
i = 1, . . . , N,
to ensure that the stress does not exceed the maximum allowable value σmax any-
where in the beam.
The last constraint is a limit on the vertical deﬂection at the end of the beam,
which we will denote y1:
y1 ≤ymax.
The deﬂection y1 can be found by a recursion that involves the deﬂection and slope
of the beam segments:
vi = 12(i −1/2)
F
Ewih3
i
+ vi+1,
yi = 6(i −1/3)
F
Ewih3
i
+ vi+1 + yi+1,
(4.45)
for i = N, N −1, . . . , 1, with starting values vN+1 = yN+1 = 0. In this recursion,
yi is the deﬂection at the right end of segment i, and vi is the slope at that point.
We can use the recursion (4.45) to show that these deﬂection and slope quantities


## Page 19

4.5
Geometric programming
165
are in fact posynomial functions of the variables w and h. We ﬁrst note that vN+1
and yN+1 are zero, and therefore posynomials. Now assume that vi+1 and yi+1 are
posynomial functions of w and h. The lefthand equation in (4.45) shows that vi is
the sum of a monomial and a posynomial (i.e., vi+1), and therefore is a posynomial.
From the righthand equation in (4.45), we see that the deﬂection yi is the sum of
a monomial and two posynomials (vi+1 and yi+1), and so is a posynomial.
In
particular, the deﬂection at the end of the beam, y1, is a posynomial.
The problem is then
minimize
PN
i=1 wihi
subject to
wmin ≤wi ≤wmax,
i = 1, . . . , N
hmin ≤hi ≤hmax,
i = 1, . . . , N
Smin ≤hi/wi ≤Smax,
i = 1, . . . , N
6iF/(wih2
i ) ≤σmax,
i = 1, . . . , N
y1 ≤ymax,
(4.46)
with variables w and h. This is a GP, since the objective is a posynomial, and
the constraints can all be expressed as posynomial inequalities. (In fact, the con-
straints can be all be expressed as monomial inequalities, with the exception of the
deﬂection limit, which is a complicated posynomial inequality.)
When the number of segments N is large, the number of monomial terms ap-
pearing in the posynomial y1 grows approximately as N 2. Another formulation of
this problem, explored in exercise 4.31, is obtained by introducing v1, . . . , vN and
y1, . . . , yN as variables, and including a modiﬁed version of the recursion as a set
of constraints. This formulation avoids this growth in the number of monomial
terms.
Minimizing spectral radius via Perron-Frobenius theory
Suppose the matrix A ∈Rn×n is elementwise nonnegative, i.e., Aij ≥0 for i, j =
1, . . . , n, and irreducible, which means that the matrix (I + A)n−1 is elementwise
positive. The Perron-Frobenius theorem states that A has a positive real eigenvalue
λpf equal to its spectral radius, i.e., the largest magnitude of its eigenvalues. The
Perron-Frobenius eigenvalue λpf determines the asymptotic rate of growth or decay
of Ak, as k →∞; in fact, the matrix ((1/λpf)A)k converges. Roughly speaking,
this means that as k →∞, Ak grows like λk
pf, if λpf > 1, or decays like λk
pf, if
λpf < 1.
A basic result in the theory of nonnegative matrices states that the Perron-
Frobenius eigenvalue is given by
λpf = inf{λ | Av ⪯λv for some v ≻0}
(and moreover, that the inﬁmum is achieved). The inequality Av ⪯λv can be
expressed as
n
X
j=1
Aijvj/(λvi) ≤1,
i = 1, . . . , n,
(4.47)
which is a set of posynomial inequalities in the variables Aij, vi, and λ. Thus,
the condition that λpf ≤λ can be expressed as a set of posynomial inequalities


## Page 20

166
4
Convex optimization problems
in A, v, and λ. This allows us to solve some optimization problems involving the
Perron-Frobenius eigenvalue using geometric programming.
Suppose that the entries of the matrix A are posynomial functions of some
underlying variable x ∈Rk. In this case the inequalities (4.47) are posynomial
inequalities in the variables x ∈Rk, v ∈Rn, and λ ∈R. We consider the problem
of choosing x to minimize the Perron-Frobenius eigenvalue (or spectral radius) of
A, possibly subject to posynomial inequalities on x,
minimize
λpf(A(x))
subject to
fi(x) ≤1,
i = 1, . . . , p,
where fi are posynomials. Using the characterization above, we can express this
problem as the GP
minimize
λ
subject to
Pn
j=1 Aijvj/(λvi) ≤1,
i = 1, . . . , n
fi(x) ≤1,
i = 1, . . . , p,
where the variables are x, v, and λ.
As a speciﬁc example, we consider a simple model for the population dynamics
for a bacterium, with time or period denoted by t = 0, 1, 2, . . ., in hours. The vector
p(t) ∈R4
+ characterizes the population age distribution at period t: p1(t) is the
total population between 0 and 1 hours old; p2(t) is the total population between
1 and 2 hours old; and so on. We (arbitrarily) assume that no bacteria live more
than 4 hours. The population propagates in time as p(t + 1) = Ap(t), where
A =


b1
b2
b3
b4
s1
0
0
0
0
s2
0
0
0
0
s3
0

.
Here bi is the birth rate among bacteria in age group i, and si is the survival rate
from age group i into age group i + 1. We assume that bi > 0 and 0 < si < 1,
which implies that the matrix A is irreducible.
The Perron-Frobenius eigenvalue of A determines the asymptotic growth or
decay rate of the population. If λpf < 1, the population converges to zero like
λt
pf, and so has a half-life of −1/ log2 λpf hours. If λpf > 1 the population grows
geometrically like λt
pf, with a doubling time of 1/ log2 λpf hours. Minimizing the
spectral radius of A corresponds to ﬁnding the fastest decay rate, or slowest growth
rate, for the population.
As our underlying variables, on which the matrix A depends, we take c1 and c2,
the concentrations of two chemicals in the environment that aﬀect the birth and
survival rates of the bacteria. We model the birth and survival rates as monomial
functions of the two concentrations:
bi
=
bnom
i
(c1/cnom
1
)αi(c2/cnom
2
)βi,
i = 1, . . . , 4
si
=
snom
i
(c1/cnom
1
)γi(c2/cnom
2
)δi,
i = 1, . . . , 3.
Here, bnom
i
is nominal birth rate, snom
i
is nominal survival rate, and cnom
i
is nominal
concentration of chemical i. The constants αi, βi, γi, and δi give the eﬀect on the


## Page 21

4.6
Generalized inequality constraints
167
birth and survival rates due to changes in the concentrations of the chemicals away
from the nominal values. For example α2 = −0.3 and γ1 = 0.5 means that an
increase in concentration of chemical 1, over the nominal concentration, causes a
decrease in the birth rate of bacteria that are between 1 and 2 hours old, and an
increase in the survival rate of bacteria from 0 to 1 hours old.
We assume that the concentrations c1 and c2 can be independently increased or
decreased (say, within a factor of 2), by administering drugs, and pose the problem
of ﬁnding the drug mix that maximizes the population decay rate (i.e., minimizes
λpf(A)). Using the approach described above, this problem can be posed as the
GP
minimize
λ
subject to
b1v1 + b2v2 + b3v3 + b4v4 ≤λv1
s1v1 ≤λv2
s2v2 ≤λv3
s3v3 ≤λv4
1/2 ≤ci/cnom
i
≤2,
i = 1, 2
bi = bnom
i
(c1/cnom
1
)αi(c2/cnom
2
)βi,
i = 1, . . . , 4
si = snom
i
(c1/cnom
1
)γi(c2/cnom
2
)δi,
i = 1, . . . , 3,
with variables bi, si, ci, vi, and λ.
4.6
Generalized inequality constraints
One very useful generalization of the standard form convex optimization prob-
lem (4.15) is obtained by allowing the inequality constraint functions to be vector
valued, and using generalized inequalities in the constraints:
minimize
f0(x)
subject to
fi(x) ⪯Ki 0,
i = 1, . . . , m
Ax = b,
(4.48)
where f0 : Rn →R, Ki ⊆Rki are proper cones, and fi : Rn →Rki are Ki-convex.
We refer to this problem as a (standard form) convex optimization problem with
generalized inequality constraints. Problem (4.15) is a special case with Ki = R+,
i = 1, . . . , m.
Many of the results for ordinary convex optimization problems hold for problems
with generalized inequalities. Some examples are:
• The feasible set, any sublevel set, and the optimal set are convex.
• Any point that is locally optimal for the problem (4.48) is globally optimal.
• The optimality condition for diﬀerentiable f0, given in §4.2.3, holds without
any change.
We will also see (in chapter 11) that convex optimization problems with generalized
inequality constraints can often be solved as easily as ordinary convex optimization
problems.


## Page 22

168
4
Convex optimization problems
4.6.1
Conic form problems
Among the simplest convex optimization problems with generalized inequalities are
the conic form problems (or cone programs), which have a linear objective and one
inequality constraint function, which is aﬃne (and therefore K-convex):
minimize
cT x
subject to
Fx + g ⪯K 0
Ax = b.
(4.49)
When K is the nonnegative orthant, the conic form problem reduces to a linear
program. We can view conic form problems as a generalization of linear programs
in which componentwise inequality is replaced with a generalized linear inequality.
Continuing the analogy to linear programming, we refer to the conic form prob-
lem
minimize
cT x
subject to
x ⪰K 0
Ax = b
as a conic form problem in standard form. Similarly, the problem
minimize
cT x
subject to
Fx + g ⪯K 0
is called a conic form problem in inequality form.
4.6.2
Semideﬁnite programming
When K is Sk
+, the cone of positive semideﬁnite k × k matrices, the associated
conic form problem is called a semideﬁnite program (SDP), and has the form
minimize
cT x
subject to
x1F1 + · · · + xnFn + G ⪯0
Ax = b,
(4.50)
where G, F1, . . . , Fn ∈Sk, and A ∈Rp×n. The inequality here is a linear matrix
inequality (see example 2.10).
If the matrices G, F1, . . . , Fn are all diagonal, then the LMI in (4.50) is equiva-
lent to a set of n linear inequalities, and the SDP (4.50) reduces to a linear program.
Standard and inequality form semideﬁnite programs
Following the analogy to LP, a standard form SDP has linear equality constraints,
and a (matrix) nonnegativity constraint on the variable X ∈Sn:
minimize
tr(CX)
subject to
tr(AiX) = bi,
i = 1, . . . , p
X ⪰0,
(4.51)


## Page 23

4.6
Generalized inequality constraints
169
where C, A1, . . . , Ap ∈Sn. (Recall that tr(CX) = Pn
i,j=1 CijXij is the form of a
general real-valued linear function on Sn.) This form should be compared to the
standard form linear program (4.28). In LP and SDP standard forms, we minimize
a linear function of the variable, subject to p linear equality constraints on the
variable, and a nonnegativity constraint on the variable.
An inequality form SDP, analogous to an inequality form LP (4.29), has no
equality constraints, and one LMI:
minimize
cT x
subject to
x1A1 + · · · + xnAn ⪯B,
with variable x ∈Rn, and parameters B, A1, . . . , An ∈Sk, c ∈Rn.
Multiple LMIs and linear inequalities
It is common to refer to a problem with linear objective, linear equality and in-
equality constraints, and several LMI constraints, i.e.,
minimize
cT x
subject to
F (i)(x) = x1F (i)
1
+ · · · + xnF (i)
n
+ G(i) ⪯0,
i = 1, . . . , K
Gx ⪯h,
Ax = b,
as an SDP as well. Such problems are readily transformed to an SDP, by forming
a large block diagonal LMI from the individual LMIs and linear inequalities:
minimize
cT x
subject to
diag(Gx −h, F (1)(x), . . . , F (K)(x)) ⪯0
Ax = b.
4.6.3
Examples
Second-order cone programming
The SOCP (4.36) can be expressed as a conic form problem
minimize
cT x
subject to
−(Aix + bi, cT
i x + di) ⪯Ki 0,
i = 1, . . . , m
Fx = g,
in which
Ki = {(y, t) ∈Rni+1 | ∥y∥2 ≤t},
i.e., the second-order cone in Rni+1. This explains the name second-order cone
program for the optimization problem (4.36).
Matrix norm minimization
Let A(x) = A0 + x1A1 + · · · + xnAn, where Ai ∈Rp×q. We consider the uncon-
strained problem
minimize
∥A(x)∥2,


## Page 24

170
4
Convex optimization problems
where ∥· ∥2 denotes the spectral norm (maximum singular value), and x ∈Rn is
the variable. This is a convex problem since ∥A(x)∥2 is a convex function of x.
Using the fact that ∥A∥2 ≤s if and only if AT A ⪯s2I (and s ≥0), we can
express the problem in the form
minimize
s
subject to
A(x)T A(x) ⪯sI,
with variables x and s. Since the function A(x)T A(x) −sI is matrix convex in
(x, s), this is a convex optimization problem with a single q × q matrix inequality
constraint.
We can also formulate the problem using a single linear matrix inequality of
size (p + q) × (p + q), using the fact that
AT A ⪯t2I (and t ≥0) ⇐⇒
 tI
A
AT
tI

⪰0.
(see §A.5.5). This results in the SDP
minimize
t
subject to

tI
A(x)
A(x)T
tI

⪰0
in the variables x and t.
Moment problems
Let t be a random variable in R. The expected values E tk (assuming they exist)
are called the (power) moments of the distribution of t. The following classical
results give a characterization of a moment sequence.
If there is a probability distribution on R such that xk = E tk, k = 0, . . . , 2n,
then x0 = 1 and
H(x0, . . . , x2n) =


x0
x1
x2
. . .
xn−1
xn
x1
x2
x3
. . .
xn
xn+1
x2
x3
x4
. . .
xn+1
xn+2
...
...
...
...
...
xn−1
xn
xn+1
. . .
x2n−2
x2n−1
xn
xn+1
xn+2
. . .
x2n−1
x2n


⪰0.
(4.52)
(The matrix H is called the Hankel matrix associated with x0, . . . , x2n.) This is
easy to see: Let xi = E ti, i = 0, . . . , 2n be the moments of some distribution, and
let y = (y0, y1, . . . yn) ∈Rn+1. Then we have
yT H(x0, . . . , x2n)y =
n
X
i,j=0
yiyj E ti+j = E(y0 + y1t1 + · · · + yntn)2 ≥0.
The following partial converse is less obvious: If x0 = 1 and H(x) ≻0, then there
exists a probability distribution on R such that xi = E ti, i = 0, . . . , 2n. (For a


## Page 25

4.6
Generalized inequality constraints
171
proof, see exercise 2.37.) Now suppose that x0 = 1, and H(x) ⪰0 (but possibly
H(x)̸ ≻0), i.e., the linear matrix inequality (4.52) holds, but possibly not strictly.
In this case, there is a sequence of distributions on R, whose moments converge to
x. In summary: the condition that x0, . . . , x2n be the moments of some distribution
on R (or the limit of the moments of a sequence of distributions) can be expressed
as the linear matrix inequality (4.52) in the variable x, together with the linear
equality x0 = 1. Using this fact, we can cast some interesting problems involving
moments as SDPs.
Suppose t is a random variable on R. We do not know its distribution, but we
do know some bounds on the moments, i.e.,
µk ≤E tk ≤µk,
k = 1, . . . , 2n
(which includes, as a special case, knowing exact values of some of the moments).
Let p(t) = c0 + c1t + · · · + c2nt2n be a given polynomial in t. The expected value
of p(t) is linear in the moments E ti:
E p(t) =
2n
X
i=0
ci E ti =
2n
X
i=0
cixi.
We can compute upper and lower bounds for E p(t),
minimize (maximize)
E p(t)
subject to
µk ≤E tk ≤µk,
k = 1, . . . , 2n,
over all probability distributions that satisfy the given moment bounds, by solving
the SDP
minimize (maximize)
c1x1 + · · · + c2nx2n
subject to
µk ≤xk ≤µk,
k = 1, . . . , 2n
H(1, x1, . . . , x2n) ⪰0
with variables x1, . . . , x2n. This gives bounds on E p(t), over all probability dis-
tributions that satisfy the known moment constraints. The bounds are sharp in
the sense that there exists a sequence of distributions, whose moments satisfy the
given moment bounds, for which E p(t) converges to the upper and lower bounds
found by these SDPs.
Bounding portfolio risk with incomplete covariance information
We consider once again the setup for the classical Markowitz portfolio problem (see
page 155). We have a portfolio of n assets or stocks, with xi denoting the amount
of asset i that is held over some investment period, and pi denoting the relative
price change of asset i over the period. The change in total value of the portfolio
is pT x. The price change vector p is modeled as a random vector, with mean and
covariance
p = E p,
Σ = E(p −p)(p −p)T .
The change in value of the portfolio is therefore a random variable with mean pT x
and standard deviation σ = (xT Σx)1/2. The risk of a large loss, i.e., a change
in portfolio value that is substantially below its expected value, is directly related


## Page 26

172
4
Convex optimization problems
to the standard deviation σ, and increases with it. For this reason the standard
deviation σ (or the variance σ2) is used as a measure of the risk associated with
the portfolio.
In the classical portfolio optimization problem, the portfolio x is the optimiza-
tion variable, and we minimize the risk subject to a minimum mean return and
other constraints. The price change statistics p and Σ are known problem param-
eters. In the risk bounding problem considered here, we turn the problem around:
we assume the portfolio x is known, but only partial information is available about
the covariance matrix Σ. We might have, for example, an upper and lower bound
on each entry:
Lij ≤Σij ≤Uij,
i, j = 1, . . . , n,
where L and U are given. We now pose the question: what is the maximum risk
for our portfolio, over all covariance matrices consistent with the given bounds?
We deﬁne the worst-case variance of the portfolio as
σ2
wc = sup{xT Σx | Lij ≤Σij ≤Uij, i, j = 1, . . . , n, Σ ⪰0}.
We have added the condition Σ ⪰0, which the covariance matrix must, of course,
satisfy.
We can ﬁnd σwc by solving the SDP
maximize
xT Σx
subject to
Lij ≤Σij ≤Uij,
i, j = 1, . . . , n
Σ ⪰0
with variable Σ ∈Sn (and problem parameters x, L, and U). The optimal Σ is
the worst covariance matrix consistent with our given bounds on the entries, where
‘worst’ means largest risk with the (given) portfolio x. We can easily construct
a distribution for p that is consistent with the given bounds, and achieves the
worst-case variance, from an optimal Σ for the SDP. For example, we can take
p = p + Σ1/2v, where v is any random vector with E v = 0 and E vvT = I.
Evidently we can use the same method to determine σwc for any prior informa-
tion about Σ that is convex. We list here some examples.
• Known variance of certain portfolios. We might have equality constraints
such as
uT
k Σuk = σ2
k,
where uk and σk are given. This corresponds to prior knowledge that certain
known portfolios (given by uk) have known (or very accurately estimated)
variance.
• Including eﬀects of estimation error. If the covariance Σ is estimated from
empirical data, the estimation method will give an estimate ˆΣ, and some in-
formation about the reliability of the estimate, such as a conﬁdence ellipsoid.
This can be expressed as
C(Σ −ˆΣ) ≤α,
where C is a positive deﬁnite quadratic form on Sn, and the constant α
determines the conﬁdence level.


## Page 27

4.6
Generalized inequality constraints
173
• Factor models. The covariance might have the form
Σ = FΣfactorF T + D,
where F ∈Rn×k, Σfactor ∈Sk, and D is diagonal. This corresponds to a
model of the price changes of the form
p = Fz + d,
where z is a random variable (the underlying factors that aﬀect the price
changes) and di are independent (additional volatility of each asset price).
We assume that the factors are known. Since Σ is linearly related to Σfactor
and D, we can impose any convex constraint on them (representing prior
information) and still compute σwc using convex optimization.
• Information about correlation coeﬃcients. In the simplest case, the diagonal
entries of Σ (i.e., the volatilities of each asset price) are known, and bounds
on correlation coeﬃcients between price changes are known:
lij ≤ρij =
Σij
Σ1/2
ii Σ1/2
jj
≤uij,
i, j = 1, . . . , n.
Since Σii are known, but Σij for i̸ = j are not, these are linear inequalities.
Fastest mixing Markov chain on a graph
We consider an undirected graph, with nodes 1, . . . , n, and a set of edges
E ⊆{1, . . . , n} × {1, . . . , n}.
Here (i, j) ∈E means that nodes i and j are connected by an edge. Since the
graph is undirected, E is symmetric: (i, j) ∈E if and only if (j, i) ∈E. We allow
the possibility of self-loops, i.e., we can have (i, i) ∈E.
We deﬁne a Markov chain, with state X(t) ∈{1, . . . , n}, for t ∈Z+ (the set
of nonnegative integers), as follows.
With each edge (i, j) ∈E we associate a
probability Pij, which is the probability that X makes a transition between nodes
i and j. State transitions can only occur across edges; we have Pij = 0 for (i, j)̸ ∈E.
The probabilities associated with the edges must be nonnegative, and for each node,
the sum of the probabilities of links connected to the node (including a self-loop,
if there is one) must equal one.
The Markov chain has transition probability matrix
Pij = prob(X(t + 1) = i | X(t) = j),
i, j = 1, . . . , n.
This matrix must satisfy
Pij ≥0,
i, j = 1, . . . , n,
1T P = 1T ,
P = P T ,
(4.53)
and also
Pij = 0
for (i, j)̸ ∈E.
(4.54)


## Page 28

174
4
Convex optimization problems
Since P is symmetric and 1T P = 1T , we conclude P1 = 1, so the uniform
distribution (1/n)1 is an equilibrium distribution for the Markov chain. Conver-
gence of the distribution of X(t) to (1/n)1 is determined by the second largest (in
magnitude) eigenvalue of P, i.e., by r = max{λ2, −λn}, where
1 = λ1 ≥λ2 ≥· · · ≥λn
are the eigenvalues of P. We refer to r as the mixing rate of the Markov chain.
If r = 1, then the distribution of X(t) need not converge to (1/n)1 (which means
the Markov chain does not mix). When r < 1, the distribution of X(t) approaches
(1/n)1 asymptotically as rt, as t →∞.
Thus, the smaller r is, the faster the
Markov chain mixes.
The fastest mixing Markov chain problem is to ﬁnd P, subject to the con-
straints (4.53) and (4.54), that minimizes r. (The problem data is the graph, i.e.,
E.) We will show that this problem can be formulated as an SDP.
Since the eigenvalue λ1 = 1 is associated with the eigenvector 1, we can express
the mixing rate as the norm of the matrix P, restricted to the subspace 1⊥: r =
∥QPQ∥2, where Q = I −(1/n)11T is the matrix representing orthogonal projection
on 1⊥. Using the property P1 = 1, we have
r
=
∥QPQ∥2
=
∥(I −(1/n)11T )P(I −(1/n)11T )∥2
=
∥P −(1/n)11T ∥2.
This shows that the mixing rate r is a convex function of P, so the fastest mixing
Markov chain problem can be cast as the convex optimization problem
minimize
∥P −(1/n)11T ∥2
subject to
P1 = 1
Pij ≥0,
i, j = 1, . . . , n
Pij = 0 for (i, j)̸ ∈E,
with variable P ∈Sn. We can express the problem as an SDP by introducing a
scalar variable t to bound the norm of P −(1/n)11T :
minimize
t
subject to
−tI ⪯P −(1/n)11T ⪯tI
P1 = 1
Pij ≥0,
i, j = 1, . . . , n
Pij = 0 for (i, j)̸ ∈E.
(4.55)
4.7
Vector optimization
4.7.1
General and convex vector optimization problems
In §4.6 we extended the standard form problem (4.1) to include vector-valued
constraint functions. In this section we investigate the meaning of a vector-valued


## Page 29

4.7
Vector optimization
175
objective function. We denote a general vector optimization problem as
minimize (with respect to K)
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m
hi(x) = 0,
i = 1, . . . , p.
(4.56)
Here x ∈Rn is the optimization variable, K ⊆Rq is a proper cone, f0 : Rn →Rq
is the objective function, fi : Rn →R are the inequality constraint functions, and
hi : Rn →R are the equality constraint functions. The only diﬀerence between this
problem and the standard optimization problem (4.1) is that here, the objective
function takes values in Rq, and the problem speciﬁcation includes a proper cone
K, which is used to compare objective values. In the context of vector optimization,
the standard optimization problem (4.1) is sometimes called a scalar optimization
problem.
We say the vector optimization problem (4.56) is a convex vector optimization
problem if the objective function f0 is K-convex, the inequality constraint functions
f1, . . . , fm are convex, and the equality constraint functions h1, . . . , hp are aﬃne.
(As in the scalar case, we usually express the equality constraints as Ax = b, where
A ∈Rp×n.)
What meaning can we give to the vector optimization problem (4.56)? Suppose
x and y are two feasible points (i.e., they satisfy the constraints). Their associated
objective values, f0(x) and f0(y), are to be compared using the generalized inequal-
ity ⪯K. We interpret f0(x) ⪯K f0(y) as meaning that x is ‘better than or equal’ in
value to y (as judged by the objective f0, with respect to K). The confusing aspect
of vector optimization is that the two objective values f0(x) and f0(y) need not be
comparable; we can have neither f0(x) ⪯K f0(y) nor f0(y) ⪯K f0(x), i.e., neither
is better than the other. This cannot happen in a scalar objective optimization
problem.
4.7.2
Optimal points and values
We ﬁrst consider a special case, in which the meaning of the vector optimization
problem is clear. Consider the set of objective values of feasible points,
O = {f0(x) | ∃x ∈D, fi(x) ≤0, i = 1, . . . , m, hi(x) = 0, i = 1, . . . , p} ⊆Rq,
which is called the set of achievable objective values. If this set has a minimum
element (see §2.4.2), i.e., there is a feasible x such that f0(x) ⪯K f0(y) for all
feasible y, then we say x is optimal for the problem (4.56), and refer to f0(x) as
the optimal value of the problem. (When a vector optimization problem has an
optimal value, it is unique.) If x⋆is an optimal point, then f0(x⋆), the objective
at x⋆, can be compared to the objective at every other feasible point, and is better
than or equal to it. Roughly speaking, x⋆is unambiguously a best choice for x,
among feasible points.
A point x⋆is optimal if and only if it is feasible and
O ⊆f0(x⋆) + K
(4.57)


## Page 30

176
4
Convex optimization problems
O
f0(x⋆)
Figure 4.7 The set O of achievable values for a vector optimization with
objective values in R2, with cone K = R2
+, is shown shaded. In this case,
the point labeled f0(x⋆) is the optimal value of the problem, and x⋆is an
optimal point. The objective value f0(x⋆) can be compared to every other
achievable value f0(y), and is better than or equal to f0(y). (Here, ‘better
than or equal to’ means ‘is below and to the left of’.) The lightly shaded
region is f0(x⋆)+K, which is the set of all z ∈R2 corresponding to objective
values worse than (or equal to) f0(x⋆).
(see §2.4.2). The set f0(x⋆) + K can be interpreted as the set of values that are
worse than, or equal to, f0(x⋆), so the condition (4.57) states that every achievable
value falls in this set. This is illustrated in ﬁgure 4.7. Most vector optimization
problems do not have an optimal point and an optimal value, but this does occur
in some special cases.
Example 4.9 Best linear unbiased estimator.
Suppose y = Ax + v, where v ∈Rm is
a measurement noise, y ∈Rm is a vector of measurements, and x ∈Rn is a vector to
be estimated, given the measurement y. We assume that A has rank n, and that the
measurement noise satisﬁes E v = 0, E vvT = I, i.e., its components are zero mean
and uncorrelated.
A linear estimator of x has the form bx = Fy. The estimator is called unbiased if for
all x we have E bx = x, i.e., if FA = I. The error covariance of an unbiased estimator
is
E(bx −x)(bx −x)T = E FvvT F T = FF T .
Our goal is to ﬁnd an unbiased estimator that has a ‘small’ error covariance matrix.
We can compare error covariances using matrix inequality, i.e., with respect to Sn
+.
This has the following interpretation: Suppose bx1 = F1y, bx2 = F2y are two unbiased
estimators. Then the ﬁrst estimator is at least as good as the second, i.e., F1F T
1 ⪯
F2F T
2 , if and only if for all c,
E(cT bx1 −cT x)2 ≤E(cT bx2 −cT x)2.
In other words, for any linear function of x, the estimator F1 yields at least as good
an estimate as does F2.


## Page 31

4.7
Vector optimization
177
We can express the problem of ﬁnding an unbiased estimator for x as the vector
optimization problem
minimize (w.r.t. Sn
+)
FF T
subject to
FA = I,
(4.58)
with variable F ∈Rn×m. The objective FF T is convex with respect to Sn
+, so the
problem (4.58) is a convex vector optimization problem. An easy way to see this is
to observe that vT FF T v = ∥F T v∥2
2 is a convex function of F for any ﬁxed v.
It is a famous result that the problem (4.58) has an optimal solution, the least-squares
estimator, or pseudo-inverse,
F ⋆= A† = (AT A)−1AT .
For any F with FA = I, we have FF T ⪰F ⋆F ⋆T . The matrix
F ⋆F ⋆T = A†A†T = (AT A)−1
is the optimal value of the problem (4.58).
4.7.3
Pareto optimal points and values
We now consider the case (which occurs in most vector optimization problems of
interest) in which the set of achievable objective values does not have a minimum
element, so the problem does not have an optimal point or optimal value. In these
cases minimal elements of the set of achievable values play an important role. We
say that a feasible point x is Pareto optimal (or eﬃcient) if f0(x) is a minimal
element of the set of achievable values O.
In this case we say that f0(x) is a
Pareto optimal value for the vector optimization problem (4.56). Thus, a point x
is Pareto optimal if it is feasible and, for any feasible y, f0(y) ⪯K f0(x) implies
f0(y) = f0(x). In other words: any feasible point y that is better than or equal to
x (i.e., f0(y) ⪯K f0(x)) has exactly the same objective value as x.
A point x is Pareto optimal if and only if it is feasible and
(f0(x) −K) ∩O = {f0(x)}
(4.59)
(see §2.4.2). The set f0(x) −K can be interpreted as the set of values that are
better than or equal to f0(x), so the condition (4.59) states that the only achievable
value better than or equal to f0(x) is f0(x) itself. This is illustrated in ﬁgure 4.8.
A vector optimization problem can have many Pareto optimal values (and
points). The set of Pareto optimal values, denoted P, satisﬁes
P ⊆O ∩bd O,
i.e., every Pareto optimal value is an achievable objective value that lies in the
boundary of the set of achievable objective values (see exercise 4.52).


## Page 32

178
4
Convex optimization problems
O
f0(xpo)
Figure 4.8 The set O of achievable values for a vector optimization problem
with objective values in R2, with cone K = R2
+, is shown shaded. This
problem does not have an optimal point or value, but it does have a set of
Pareto optimal points, whose corresponding values are shown as the dark-
ened curve on the lower left boundary of O. The point labeled f0(xpo) is a
Pareto optimal value, and xpo is a Pareto optimal point. The lightly shaded
region is f0(xpo) −K, which is the set of all z ∈R2 corresponding to objec-
tive values better than (or equal to) f0(xpo).
4.7.4
Scalarization
Scalarization is a standard technique for ﬁnding Pareto optimal (or optimal) points
for a vector optimization problem, based on the characterization of minimum and
minimal points via dual generalized inequalities given in §2.6.3. Choose any λ ≻K∗
0, i.e., any vector that is positive in the dual generalized inequality. Now consider
the scalar optimization problem
minimize
λT f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m
hi(x) = 0,
i = 1, . . . , p,
(4.60)
and let x be an optimal point. Then x is Pareto optimal for the vector optimization
problem (4.56). This follows from the dual inequality characterization of minimal
points given in §2.6.3, and is also easily shown directly. If x were not Pareto optimal,
then there is a y that is feasible, satisﬁes f0(y) ⪯K f0(x), and f0(x)̸ = f0(y).
Since f0(x) −f0(y) ⪰K 0 and is nonzero, we have λT (f0(x) −f0(y)) > 0, i.e.,
λT f0(x) > λT f0(y). This contradicts the assumption that x is optimal for the
scalar problem (4.60).
Using scalarization, we can ﬁnd Pareto optimal points for any vector opti-
mization problem by solving the ordinary scalar optimization problem (4.60). The
vector λ, which is sometimes called the weight vector, must satisfy λ ≻K∗0. The
weight vector is a free parameter; by varying it we obtain (possibly) diﬀerent Pareto
optimal solutions of the vector optimization problem (4.56). This is illustrated in
ﬁgure 4.9. The ﬁgure also shows an example of a Pareto optimal point that cannot


## Page 33

4.7
Vector optimization
179
O
f0(x1)
λ1
f0(x2)
λ2
f0(x3)
Figure 4.9 Scalarization. The set O of achievable values for a vector opti-
mization problem with cone K = R2
+. Three Pareto optimal values f0(x1),
f0(x2), f0(x3) are shown. The ﬁrst two values can be obtained by scalar-
ization: f0(x1) minimizes λT
1 u over all u ∈O and f0(x2) minimizes λT
2 u,
where λ1, λ2 ≻0. The value f0(x3) is Pareto optimal, but cannot be found
by scalarization.
be obtained via scalarization, for any value of the weight vector λ ≻K∗0.
The method of scalarization can be interpreted geometrically.
A point x is
optimal for the scalarized problem, i.e., minimizes λT f0 over the feasible set, if
and only if λT (f0(y) −f0(x)) ≥0 for all feasible y. But this is the same as saying
that {u | −λT (u −f0(x)) = 0} is a supporting hyperplane to the set of achievable
objective values O at the point f0(x); in particular
{u | λT (u −f0(x)) < 0} ∩O = ∅.
(4.61)
(See ﬁgure 4.9.) Thus, when we ﬁnd an optimal point for the scalarized problem, we
not only ﬁnd a Pareto optimal point for the original vector optimization problem;
we also ﬁnd an entire halfspace in Rq, given by (4.61), of objective values that
cannot be achieved.
Scalarization of convex vector optimization problems
Now suppose the vector optimization problem (4.56) is convex. Then the scalarized
problem (4.60) is also convex, since λT f0 is a (scalar-valued) convex function (by
the results in §3.6). This means that we can ﬁnd Pareto optimal points of a convex
vector optimization problem by solving a convex scalar optimization problem. For
each choice of the weight vector λ ≻K∗0 we get a (usually diﬀerent) Pareto optimal
point.
For convex vector optimization problems we have a partial converse: For every
Pareto optimal point xpo, there is some nonzero λ ⪰K∗0 such that xpo is a solution
of the scalarized problem (4.60). So, roughly speaking, for convex problems the
method of scalarization yields all Pareto optimal points, as the weight vector λ


## Page 34

180
4
Convex optimization problems
varies over the K∗-nonnegative, nonzero values. We have to be careful here, because
it is not true that every solution of the scalarized problem, with λ ⪰K∗0 and λ̸ = 0,
is a Pareto optimal point for the vector problem. (In contrast, every solution of
the scalarized problem with λ ≻K∗0 is Pareto optimal.)
In some cases we can use this partial converse to ﬁnd all Pareto optimal points
of a convex vector optimization problem. Scalarization with λ ≻K∗0 gives a set
of Pareto optimal points (as it would in a nonconvex vector optimization problem
as well).
To ﬁnd the remaining Pareto optimal solutions, we have to consider
nonzero weight vectors λ that satisfy λ ⪰K∗0. For each such weight vector, we
ﬁrst identify all solutions of the scalarized problem. Then among these solutions we
must check which are, in fact, Pareto optimal for the vector optimization problem.
These ‘extreme’ Pareto optimal points can also be found as the limits of the Pareto
optimal points obtained from positive weight vectors.
To establish this partial converse, we consider the set
A = O + K = {t ∈Rq | f0(x) ⪯K t for some feasible x},
(4.62)
which consists of all values that are worse than or equal to (with respect to ⪯K)
some achievable objective value. While the set O of achievable objective values
need not be convex, the set A is convex, when the problem is convex. Moreover,
the minimal elements of A are exactly the same as the minimal elements of the
set O of achievable values, i.e., they are the same as the Pareto optimal values.
(See exercise 4.53.) Now we use the results of §2.6.3 to conclude that any minimal
element of A minimizes λT z over A for some nonzero λ ⪰K∗0. This means that
every Pareto optimal point for the vector optimization problem is optimal for the
scalarized problem, for some nonzero weight λ ⪰K∗0.
Example 4.10 Minimal upper bound on a set of matrices. We consider the (convex)
vector optimization problem, with respect to the positive semideﬁnite cone,
minimize (w.r.t. Sn
+)
X
subject to
X ⪰Ai,
i = 1, . . . , m,
(4.63)
where Ai ∈Sn, i = 1, . . . , m, are given. The constraints mean that X is an upper
bound on the given matrices A1, . . . , Am; a Pareto optimal solution of (4.63) is a
minimal upper bound on the matrices.
To ﬁnd a Pareto optimal point, we apply scalarization: we choose any W ∈Sn
++ and
form the problem
minimize
tr(WX)
subject to
X ⪰Ai,
i = 1, . . . , m,
(4.64)
which is an SDP. Diﬀerent choices for W will, in general, give diﬀerent minimal
solutions.
The partial converse tells us that if X is Pareto optimal for the vector problem (4.63)
then it is optimal for the SDP (4.64), for some nonzero weight matrix W ⪰0.
(In this case, however, not every solution of (4.64) is Pareto optimal for the vector
optimization problem.)
We can give a simple geometric interpretation for this problem. We associate with
each A ∈Sn
++ an ellipsoid centered at the origin, given by
EA = {u | uT A−1u ≤1},


## Page 35

4.7
Vector optimization
181
X1
X2
Figure 4.10 Geometric interpretation of the problem (4.63).
The three
shaded ellipsoids correspond to the data A1, A2, A3 ∈S2
++; the Pareto
optimal points correspond to minimal ellipsoids that contain them. The two
ellipsoids, with boundaries labeled X1 and X2, show two minimal ellipsoids
obtained by solving the SDP (4.64) for two diﬀerent weight matrices W1 and
W2.
so that A ⪯B if and only if EA ⊆EB. A Pareto optimal point X for the prob-
lem (4.63) corresponds to a minimal ellipsoid that contains the ellipsoids associated
with A1, . . . , Am. An example is shown in ﬁgure 4.10.
4.7.5
Multicriterion optimization
When a vector optimization problem involves the cone K = Rq
+, it is called a
multicriterion or multi-objective optimization problem.
The components of f0,
say, F1, . . . , Fq, can be interpreted as q diﬀerent scalar objectives, each of which
we would like to minimize. We refer to Fi as the ith objective of the problem. A
multicriterion optimization problem is convex if f1, . . . , fm are convex, h1, . . . , hp
are aﬃne, and the objectives F1, . . . , Fq are convex.
Since multicriterion problems are vector optimization problems, all of the ma-
terial of §4.7.1–§4.7.4 applies. For multicriterion problems, though, we can be a
bit more speciﬁc in the interpretations. If x is feasible, we can think of Fi(x) as
its score or value, according to the ith objective. If x and y are both feasible,
Fi(x) ≤Fi(y) means that x is at least as good as y, according to the ith objective;
Fi(x) < Fi(y) means that x is better than y, or x beats y, according to the ith ob-
jective. If x and y are both feasible, we say that x is better than y, or x dominates
y, if Fi(x) ≤Fi(y) for i = 1, . . . , q, and for at least one j, Fj(x) < Fj(y). Roughly
speaking, x is better than y if x meets or beats y on all objectives, and beats it in
at least one objective.
In a multicriterion problem, an optimal point x⋆satisﬁes
Fi(x⋆) ≤Fi(y),
i = 1, . . . , q,


## Page 36

182
4
Convex optimization problems
for every feasible y. In other words, x⋆is simultaneously optimal for each of the
scalar problems
minimize
Fj(x)
subject to
fi(x) ≤0,
i = 1, . . . , m
hi(x) = 0,
i = 1, . . . , p,
for j = 1, . . . , q. When there is an optimal point, we say that the objectives are
noncompeting, since no compromises have to be made among the objectives; each
objective is as small as it could be made, even if the others were ignored.
A Pareto optimal point xpo satisﬁes the following: if y is feasible and Fi(y) ≤
Fi(xpo) for i = 1, . . . , q, then Fi(xpo) = Fi(y), i = 1, . . . , q. This can be restated
as: a point is Pareto optimal if and only if it is feasible and there is no better
feasible point. In particular, if a feasible point is not Pareto optimal, there is at
least one other feasible point that is better. In searching for good points, then, we
can clearly limit our search to Pareto optimal points.
Trade-oﬀanalysis
Now suppose that x and y are Pareto optimal points with, say,
Fi(x) < Fi(y),
i ∈A
Fi(x) = Fi(y),
i ∈B
Fi(x) > Fi(y),
i ∈C,
where A∪B ∪C = {1, . . . , q}. In other words, A is the set of (indices of) objectives
for which x beats y, B is the set of objectives for which the points x and y are tied,
and C is the set of objectives for which y beats x. If A and C are empty, then
the two points x and y have exactly the same objective values. If this is not the
case, then both A and C must be nonempty. In other words, when comparing two
Pareto optimal points, they either obtain the same performance (i.e., all objectives
equal), or, each beats the other in at least one objective.
In comparing the point x to y, we say that we have traded or traded oﬀbetter
objective values for i ∈A for worse objective values for i ∈C. Optimal trade-oﬀ
analysis (or just trade-oﬀanalysis) is the study of how much worse we must do
in one or more objectives in order to do better in some other objectives, or more
generally, the study of what sets of objective values are achievable.
As an example, consider a bi-criterion (i.e., two criterion) problem. Suppose
x is a Pareto optimal point, with objectives F1(x) and F2(x). We might ask how
much larger F2(z) would have to be, in order to obtain a feasible point z with
F1(z) ≤F1(x) −a, where a > 0 is some constant. Roughly speaking, we are asking
how much we must pay in the second objective to obtain an improvement of a in
the ﬁrst objective. If a large increase in F2 must be accepted to realize a small
decrease in F1, we say that there is a strong trade-oﬀbetween the objectives, near
the Pareto optimal value (F1(x), F2(x)). If, on the other hand, a large decrease
in F1 can be obtained with only a small increase in F2, we say that the trade-oﬀ
between the objectives is weak (near the Pareto optimal value (F1(x), F2(x))).
We can also consider the case in which we trade worse performance in the ﬁrst
objective for an improvement in the second. Here we ﬁnd how much smaller F2(z)


## Page 37

4.7
Vector optimization
183
can be made, to obtain a feasible point z with F1(z) ≤F1(x) + a, where a > 0
is some constant. In this case we receive a beneﬁt in the second objective, i.e., a
reduction in F2 compared to F2(x). If this beneﬁt is large (i.e., by increasing F1
a small amount we obtain a large reduction in F2), we say the objectives exhibit
a strong trade-oﬀ. If it is small, we say the objectives trade oﬀweakly (near the
Pareto optimal value (F1(x), F2(x))).
Optimal trade-oﬀsurface
The set of Pareto optimal values for a multicriterion problem is called the optimal
trade-oﬀsurface (in general, when q > 2) or the optimal trade-oﬀcurve (when
q = 2). (Since it would be foolish to accept any point that is not Pareto optimal,
we can restrict our trade-oﬀanalysis to Pareto optimal points.) Trade-oﬀanalysis
is also sometimes called exploring the optimal trade-oﬀsurface. (The optimal trade-
oﬀsurface is usually, but not always, a surface in the usual sense. If the problem
has an optimal point, for example, the optimal trade-oﬀsurface consists of a single
point, the optimal value.)
An optimal trade-oﬀcurve is readily interpreted.
An example is shown in
ﬁgure 4.11, on page 185, for a (convex) bi-criterion problem. From this curve we
can easily visualize and understand the trade-oﬀs between the two objectives.
• The endpoint at the right shows the smallest possible value of F2, without
any consideration of F1.
• The endpoint at the left shows the smallest possible value of F1, without any
consideration of F2.
• By ﬁnding the intersection of the curve with a vertical line at F1 = α, we can
see how large F2 must be to achieve F1 ≤α.
• By ﬁnding the intersection of the curve with a horizontal line at F2 = β, we
can see how large F1 must be to achieve F2 ≤β.
• The slope of the optimal trade-oﬀcurve at a point on the curve (i.e., a Pareto
optimal value) shows the local optimal trade-oﬀbetween the two objectives.
Where the slope is steep, small changes in F1 are accompanied by large
changes in F2.
• A point of large curvature is one where small decreases in one objective can
only be accomplished by a large increase in the other. This is the prover-
bial knee of the trade-oﬀcurve, and in many applications represents a good
compromise solution.
All of these have simple extensions to a trade-oﬀsurface, although visualizing a
surface with more than three objectives is diﬃcult.
Scalarizing multicriterion problems
When we scalarize a multicriterion problem by forming the weighted sum objective
λT f0(x) =
q
X
i=1
λiFi(x),


## Page 38

184
4
Convex optimization problems
where λ ≻0, we can interpret λi as the weight we attach to the ith objective.
The weight λi can be thought of as quantifying our desire to make Fi small (or
our objection to having Fi large).
In particular, we should take λi large if we
want Fi to be small; if we care much less about Fi, we can take λi small. We can
interpret the ratio λi/λj as the relative weight or relative importance of the ith
objective compared to the jth objective. Alternatively, we can think of λi/λj as
exchange rate between the two objectives, since in the weighted sum objective a
decrease (say) in Fi by α is considered the same as an increase in Fj in the amount
(λi/λj)α.
These interpretations give us some intuition about how to set or change the
weights while exploring the optimal trade-oﬀsurface. Suppose, for example, that
the weight vector λ ≻0 yields the Pareto optimal point xpo, with objective values
F1(xpo), . . . , Fq(xpo). To ﬁnd a (possibly) new Pareto optimal point which trades
oﬀa better kth objective value (say), for (possibly) worse objective values for the
other objectives, we form a new weight vector ˜λ with
˜λk > λk,
˜λj = λj,
j̸ = k,
j = 1, . . . , q,
i.e., we increase the weight on the kth objective. This yields a new Pareto optimal
point ˜xpo with Fk(˜xpo) ≤Fk(xpo) (and usually, Fk(˜xpo) < Fk(xpo)), i.e., a new
Pareto optimal point with an improved kth objective.
We can also see that at any point where the optimal trade-oﬀsurface is smooth,
λ gives the inward normal to the surface at the associated Pareto optimal point.
In particular, when we choose a weight vector λ and apply scalarization, we obtain
a Pareto optimal point where λ gives the local trade-oﬀs among objectives.
In practice, optimal trade-oﬀsurfaces are explored by ad hoc adjustment of the
weights, based on the intuitive ideas above. We will see later (in chapter 5) that
the basic idea of scalarization, i.e., minimizing a weighted sum of objectives, and
then adjusting the weights to obtain a suitable solution, is the essence of duality.
4.7.6
Examples
Regularized least-squares
We are given A ∈Rm×n and b ∈Rm, and want to choose x ∈Rn taking into
account two quadratic objectives:
• F1(x) = ∥Ax −b∥2
2 = xT AT Ax −2bT Ax + bT b is a measure of the misﬁt
between Ax and b,
• F2(x) = ∥x∥2
2 = xT x is a measure of the size of x.
Our goal is to ﬁnd x that gives a good ﬁt (i.e., small F1) and that is not large (i.e.,
small F2). We can formulate this problem as a vector optimization problem with
respect to the cone R2
+, i.e., a bi-criterion problem (with no constraints):
minimize (w.r.t. R2
+)
f0(x) = (F1(x), F2(x)).


## Page 39

4.7
Vector optimization
185
F1(x) = ∥Ax −b∥2
2
F2(x) = ∥x∥2
2
0
5
10
15
0
5
10
15
Figure 4.11 Optimal trade-oﬀcurve for a regularized least-squares problem.
The shaded set is the set of achievable values (∥Ax−b∥2
2, ∥x∥2
2). The optimal
trade-oﬀcurve, shown darker, is the lower left part of the boundary.
We can scalarize this problem by taking λ1 > 0 and λ2 > 0 and minimizing the
scalar weighted sum objective
λT f0(x)
=
λ1F1(x) + λ2F2(x)
=
xT (λ1AT A + λ2I)x −2λ1bT Ax + λ1bT b,
which yields
x(µ) = (λ1AT A + λ2I)−1λ1AT b = (AT A + µI)−1AT b,
where µ = λ2/λ1. For any µ > 0, this point is Pareto optimal for the bi-criterion
problem. We can interpret µ = λ2/λ1 as the relative weight we assign F2 compared
to F1.
This method produces all Pareto optimal points, except two, associated with
the extremes µ →∞and µ →0. In the ﬁrst case we have the Pareto optimal
solution x = 0, which would be obtained by scalarization with λ = (0, 1). At the
other extreme we have the Pareto optimal solution A†b, where A† is the pseudo-
inverse of A. This Pareto optimal solution is obtained as the limit of the optimal
solution of the scalarized problem as µ →0, i.e., as λ →(1, 0). (We will encounter
the regularized least-squares problem again in §6.3.2.)
Figure 4.11 shows the optimal trade-oﬀcurve and the set of achievable values
for a regularized least-squares problem with problem data A ∈R100×10, b ∈R100.
(See exercise 4.50 for more discussion.)
Risk-return trade-oﬀin portfolio optimization
The classical Markowitz portfolio optimization problem described on page 155 is
naturally expressed as a bi-criterion problem, where the objectives are the negative


## Page 40

186
4
Convex optimization problems
mean return (since we wish to maximize mean return) and the variance of the
return:
minimize (w.r.t. R2
+)
(F1(x), F2(x)) = (−pT x, xT Σx)
subject to
1T x = 1,
x ⪰0.
In forming the associated scalarized problem, we can (without loss of generality)
take λ1 = 1 and λ2 = µ > 0:
minimize
−pT x + µxT Σx
subject to
1T x = 1,
x ⪰0,
which is a QP. In this example too, we get all Pareto optimal portfolios except for
the two limiting cases corresponding to µ →0 and µ →∞. Roughly speaking, in
the ﬁrst case we get a maximum mean return, without regard for return variance;
in the second case we form a minimum variance return, without regard for mean
return. Assuming that pk > pi for i̸ = k, i.e., that asset k is the unique asset with
maximum mean return, the portfolio allocation x = ek is the only one correspond-
ing to µ →0. (In other words, we concentrate the portfolio entirely in the asset
that has maximum mean return.) In many portfolio problems asset n corresponds
to a risk-free investment, with (deterministic) return rrf. Assuming that Σ, with its
last row and column (which are zero) removed, is full rank, then the other extreme
Pareto optimal portfolio is x = en, i.e., the portfolio is concentrated entirely in the
risk-free asset.
As a speciﬁc example, we consider a simple portfolio optimization problem with
4 assets, with price change mean and standard deviations given in the following
table.
Asset
pi
Σ1/2
ii
1
12%
20%
2
10%
10%
3
7%
5%
4
3%
0%
Asset 4 is a risk-free asset, with a (certain) 3% return. Assets 3, 2, and 1 have
increasing mean returns, ranging from 7% to 12%, as well as increasing standard
deviations, which range from 5% to 20%. The correlation coeﬃcients between the
assets are ρ12 = 30%, ρ13 = −40%, and ρ23 = 0%.
Figure 4.12 shows the optimal trade-oﬀcurve for this portfolio optimization
problem. The plot is given in the conventional way, with the horizontal axis show-
ing standard deviation (i.e., squareroot of variance) and the vertical axis showing
expected return. The lower plot shows the optimal asset allocation vector x for
each Pareto optimal point.
The results in this simple example agree with our intuition. For small risk,
the optimal allocation consists mostly of the risk-free asset, with a mixture of the
other assets in smaller quantities. Note that a mixture of asset 3 and asset 1, which
are negatively correlated, gives some hedging, i.e., lowers variance for a given level
of mean return. At the other end of the trade-oﬀcurve, we see that aggressive
growth portfolios (i.e., those with large mean returns) concentrate the allocation
in assets 1 and 2, the ones with the largest mean returns (and variances).
