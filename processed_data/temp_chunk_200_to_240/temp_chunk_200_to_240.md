# temp_chunk_200_to_240



## Page 1

4.7
Vector optimization
187
mean return
0%
10%
20%
0%
5%
10%
15%
standard deviation of return
allocation
x(1)
x(2)
x(3)
x(4)
0%
10%
20%
0
0.5
1
Figure 4.12 Top. Optimal risk-return trade-oﬀcurve for a simple portfolio
optimization problem.
The lefthand endpoint corresponds to putting all
resources in the risk-free asset, and so has zero standard deviation.
The
righthand endpoint corresponds to putting all resources in asset 1, which
has highest mean return. Bottom. Corresponding optimal allocations.


## Page 2

188
4
Convex optimization problems
Bibliography
Linear programming has been studied extensively since the 1940s, and is the subject of
many excellent books, including Dantzig [Dan63], Luenberger [Lue84], Schrijver [Sch86],
Papadimitriou and Steiglitz [PS98], Bertsimas and Tsitsiklis [BT97], Vanderbei [Van96],
and Roos, Terlaky, and Vial [RTV97]. Dantzig and Schrijver also provide detailed ac-
counts of the history of linear programming. For a recent survey, see Todd [Tod02].
Schaible [Sch82, Sch83] gives an overview of fractional programming, which includes
linear-fractional problems and extensions such as convex-concave fractional problems (see
exercise 4.7). The model of a growing economy in example 4.7 appears in von Neumann
[vN46].
Research on quadratic programming began in the 1950s (see, e.g., Frank and Wolfe
[FW56], Markowitz [Mar56], Hildreth [Hil57]), and was in part motivated by the portfo-
lio optimization problem discussed on page 155 (Markowitz [Mar52]), and the LP with
random cost discussed on page 154 (see Freund [Fre56]).
Interest in second-order cone programming is more recent, and started with Nesterov
and Nemirovski [NN94, §6.2.3]. The theory and applications of SOCPs are surveyed by
Alizadeh and Goldfarb [AG03], Ben-Tal and Nemirovski [BTN01, lecture 3] (where the
problem is referred to as conic quadratic programming), and Lobo, Vandenberghe, Boyd,
and Lebret [LVBL98].
Robust linear programming, and robust convex optimization in general, originated with
Ben-Tal and Nemirovski [BTN98, BTN99] and El Ghaoui and Lebret [EL97]. Goldfarb
and Iyengar [GI03a, GI03b] discuss robust QCQPs and applications in portfolio optimiza-
tion. El Ghaoui, Oustry, and Lebret [EOL98] focus on robust semideﬁnite programming.
Geometric programming has been known since the 1960s. Its use in engineering design
was ﬁrst advocated by Duﬃn, Peterson, and Zener [DPZ67] and Zener [Zen71]. Peterson
[Pet76] and Ecker [Eck80] describe the progress made during the 1970s. These articles
and books also include examples of engineering applications, in particular in chemical
and civil engineering. Fishburn and Dunlop [FD85], Sapatnekar, Rao, Vaidya, and Kang
[SRVK93], and Hershenson, Boyd, and Lee [HBL01]) apply geometric programming to
problems in integrated circuit design. The cantilever beam design example (page 163)
is from Vanderplaats [Van84, page 147]. The variational characterization of the Perron-
Frobenius eigenvalue (page 165) is proved in Berman and Plemmons [BP94, page 31].
Nesterov and Nemirovski [NN94, chapter 4] introduced the conic form problem (4.49)
as a standard problem format in nonlinear convex optimization. The cone programming
approach is further developed in Ben-Tal and Nemirovski [BTN01], who also describe
numerous applications.
Alizadeh [Ali91] and Nesterov and Nemirovski [NN94, §6.4] were the ﬁrst to make a
systematic study of semideﬁnite programming, and to point out the wide variety of
applications in convex optimization. Subsequent research in semideﬁnite programming
during the 1990s was driven by applications in combinatorial optimization (Goemans
and Williamson [GW95]), control (Boyd, El Ghaoui, Feron, and Balakrishnan [BEFB94],
Scherer, Gahinet, and Chilali [SGC97], Dullerud and Paganini [DP00]), communications
and signal processing (Luo [Luo03], Davidson, Luo, Wong, and Ma [DLW00, MDW+02]),
and other areas of engineering. The book edited by Wolkowicz, Saigal, and Vandenberghe
[WSV00] and the articles by Todd [Tod01], Lewis and Overton [LO96], and Vandenberghe
and Boyd [VB95] provide overviews and extensive bibliographies. Connections between
SDP and moment problems, of which we give a simple example on page 170, are explored
in detail by Bertsimas and Sethuraman [BS00], Nesterov [Nes00], and Lasserre [Las02].
The fastest mixing Markov chain problem is from Boyd, Diaconis, and Xiao [BDX04].
Multicriterion optimization and Pareto optimality are fundamental tools in economics;
see Pareto [Par71], Debreu [Deb59] and Luenberger [Lue95]. The result in example 4.9 is
known as the Gauss-Markov theorem (Kailath, Sayed, and Hassibi [KSH00, page 97]).


## Page 3

Exercises
189
Exercises
Basic terminology and optimality conditions
4.1 Consider the optimization problem
minimize
f0(x1, x2)
subject to
2x1 + x2 ≥1
x1 + 3x2 ≥1
x1 ≥0,
x2 ≥0.
Make a sketch of the feasible set. For each of the following objective functions, give the
optimal set and the optimal value.
(a) f0(x1, x2) = x1 + x2.
(b) f0(x1, x2) = −x1 −x2.
(c) f0(x1, x2) = x1.
(d) f0(x1, x2) = max{x1, x2}.
(e) f0(x1, x2) = x2
1 + 9x2
2.
4.2 Consider the optimization problem
minimize
f0(x) = −Pm
i=1 log(bi −aT
i x)
with domain dom f0 = {x | Ax ≺b}, where A ∈Rm×n (with rows aT
i ). We assume that
dom f0 is nonempty.
Prove the following facts (which include the results quoted without proof on page 141).
(a) dom f0 is unbounded if and only if there exists a v̸ = 0 with Av ⪯0.
(b) f0 is unbounded below if and only if there exists a v with Av ⪯0, Av̸ = 0. Hint.
There exists a v such that Av ⪯0, Av̸ = 0 if and only if there exists no z ≻0
such that AT z = 0. This follows from the theorem of alternatives in example 2.21,
page 50.
(c) If f0 is bounded below then its minimum is attained, i.e., there exists an x that
satisﬁes the optimality condition (4.23).
(d) The optimal set is aﬃne: Xopt = {x⋆+ v | Av = 0}, where x⋆is any optimal point.
4.3 Prove that x⋆= (1, 1/2, −1) is optimal for the optimization problem
minimize
(1/2)xT Px + qT x + r
subject to
−1 ≤xi ≤1,
i = 1, 2, 3,
where
P =
"
13
12
−2
12
17
6
−2
6
12
#
,
q =
" −22.0
−14.5
13.0
#
,
r = 1.
4.4 [P. Parrilo] Symmetries and convex optimization. Suppose G = {Q1, . . . , Qk} ⊆Rn×n is a
group, i.e., closed under products and inverse. We say that the function f : Rn →R is G-
invariant, or symmetric with respect to G, if f(Qix) = f(x) holds for all x and i = 1, . . . , k.
We deﬁne x = (1/k) Pk
i=1 Qix, which is the average of x over its G-orbit. We deﬁne the
ﬁxed subspace of G as
F = {x | Qix = x, i = 1, . . . , k}.
(a) Show that for any x ∈Rn, we have x ∈F.


## Page 4

190
4
Convex optimization problems
(b) Show that if f : Rn →R is convex and G-invariant, then f(x) ≤f(x).
(c) We say the optimization problem
minimize
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m
is G-invariant if the objective f0 is G-invariant, and the feasible set is G-invariant,
which means
f1(x) ≤0, . . . , fm(x) ≤0 =⇒f1(Qix) ≤0, . . . , fm(Qix) ≤0,
for i = 1, . . . , k. Show that if the problem is convex and G-invariant, and there exists
an optimal point, then there exists an optimal point in F. In other words, we can
adjoin the equality constraints x ∈F to the problem, without loss of generality.
(d) As an example, suppose f is convex and symmetric, i.e., f(Px) = f(x) for every
permutation P. Show that if f has a minimizer, then it has a minimizer of the form
α1. (This means to minimize f over x ∈Rn, we can just as well minimize f(t1)
over t ∈R.)
4.5 Equivalent convex problems. Show that the following three convex problems are equiva-
lent. Carefully explain how the solution of each problem is obtained from the solution of
the other problems. The problem data are the matrix A ∈Rm×n (with rows aT
i ), the
vector b ∈Rm, and the constant M > 0.
(a) The robust least-squares problem
minimize
Pm
i=1 φ(aT
i x −bi),
with variable x ∈Rn, where φ : R →R is deﬁned as
φ(u) =

u2
|u| ≤M
M(2|u| −M)
|u| > M.
(This function is known as the Huber penalty function; see §6.1.2.)
(b) The least-squares problem with variable weights
minimize
Pm
i=1(aT
i x −bi)2/(wi + 1) + M 21T w
subject to
w ⪰0,
with variables x ∈Rn and w ∈Rm, and domain D = {(x, w) ∈Rn×Rm | w ≻−1}.
Hint. Optimize over w assuming x is ﬁxed, to establish a relation with the problem
in part (a).
(This problem can be interpreted as a weighted least-squares problem in which we
are allowed to adjust the weight of the ith residual. The weight is one if wi = 0, and
decreases if we increase wi. The second term in the objective penalizes large values
of w, i.e., large adjustments of the weights.)
(c) The quadratic program
minimize
Pm
i=1(u2
i + 2Mvi)
subject to
−u −v ⪯Ax −b ⪯u + v
0 ⪯u ⪯M1
v ⪰0.


## Page 5

Exercises
191
4.6 Handling convex equality constraints. A convex optimization problem can have only linear
equality constraint functions.
In some special cases, however, it is possible to handle
convex equality constraint functions, i.e., constraints of the form h(x) = 0, where h is
convex. We explore this idea in this problem.
Consider the optimization problem
minimize
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m
h(x) = 0,
(4.65)
where fi and h are convex functions with domain Rn. Unless h is aﬃne, this is not a
convex optimization problem. Consider the related problem
minimize
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m,
h(x) ≤0,
(4.66)
where the convex equality constraint has been relaxed to a convex inequality. This prob-
lem is, of course, convex.
Now suppose we can guarantee that at any optimal solution x⋆of the convex prob-
lem (4.66), we have h(x⋆) = 0, i.e., the inequality h(x) ≤0 is always active at the solution.
Then we can solve the (nonconvex) problem (4.65) by solving the convex problem (4.66).
Show that this is the case if there is an index r such that
• f0 is monotonically increasing in xr
• f1, . . . , fm are nondecreasing in xr
• h is monotonically decreasing in xr.
We will see speciﬁc examples in exercises 4.31 and 4.58.
4.7 Convex-concave fractional problems.
Consider a problem of the form
minimize
f0(x)/(cT x + d)
subject to
fi(x) ≤0,
i = 1, . . . , m
Ax = b
where f0, f1, . . . , fm are convex, and the domain of the objective function is deﬁned as
{x ∈dom f0 | cT x + d > 0}.
(a) Show that this is a quasiconvex optimization problem.
(b) Show that the problem is equivalent to
minimize
g0(y, t)
subject to
gi(y, t) ≤0,
i = 1, . . . , m
Ay = bt
cT y + dt = 1,
where gi is the perspective of fi (see §3.2.6). The variables are y ∈Rn and t ∈R.
Show that this problem is convex.
(c) Following a similar argument, derive a convex formulation for the convex-concave
fractional problem
minimize
f0(x)/h(x)
subject to
fi(x) ≤0,
i = 1, . . . , m
Ax = b


## Page 6

192
4
Convex optimization problems
where f0, f1, . . . , fm are convex, h is concave, the domain of the objective function
is deﬁned as {x ∈dom f0 ∩dom h | h(x) > 0} and f0(x) ≥0 everywhere.
As an example, apply your technique to the (unconstrained) problem with
f0(x) = (tr F(x))/m,
h(x) = (det(F(x))1/m,
with dom(f0/h) = {x | F(x) ≻0}, where F(x) = F0 + x1F1 + · · · + xnFn for given
Fi ∈Sm. In this problem, we minimize the ratio of the arithmetic mean over the
geometric mean of the eigenvalues of an aﬃne matrix function F(x).
Linear optimization problems
4.8 Some simple LPs. Give an explicit solution of each of the following LPs.
(a) Minimizing a linear function over an aﬃne set.
minimize
cT x
subject to
Ax = b.
(b) Minimizing a linear function over a halfspace.
minimize
cT x
subject to
aT x ≤b,
where a̸ = 0.
(c) Minimizing a linear function over a rectangle.
minimize
cT x
subject to
l ⪯x ⪯u,
where l and u satisfy l ⪯u.
(d) Minimizing a linear function over the probability simplex.
minimize
cT x
subject to
1T x = 1,
x ⪰0.
What happens if the equality constraint is replaced by an inequality 1T x ≤1?
We can interpret this LP as a simple portfolio optimization problem. The vector
x represents the allocation of our total budget over diﬀerent assets, with xi the
fraction invested in asset i. The return of each investment is ﬁxed and given by −ci,
so our total return (which we want to maximize) is −cT x. If we replace the budget
constraint 1T x = 1 with an inequality 1T x ≤1, we have the option of not investing
a portion of the total budget.
(e) Minimizing a linear function over a unit box with a total budget constraint.
minimize
cT x
subject to
1T x = α,
0 ⪯x ⪯1,
where α is an integer between 0 and n. What happens if α is not an integer (but
satisﬁes 0 ≤α ≤n)? What if we change the equality to an inequality 1T x ≤α?
(f) Minimizing a linear function over a unit box with a weighted budget constraint.
minimize
cT x
subject to
dT x = α,
0 ⪯x ⪯1,
with d ≻0, and 0 ≤α ≤1T d.


## Page 7

Exercises
193
4.9 Square LP. Consider the LP
minimize
cT x
subject to
Ax ⪯b
with A square and nonsingular. Show that the optimal value is given by
p⋆=

cT A−1b
A−T c ⪯0
−∞
otherwise.
4.10 Converting general LP to standard form.
Work out the details on page 147 of §4.3.
Explain in detail the relation between the feasible sets, the optimal solutions, and the
optimal values of the standard form LP and the original LP.
4.11 Problems involving ℓ1- and ℓ∞-norms. Formulate the following problems as LPs. Explain
in detail the relation between the optimal solution of each problem and the solution of its
equivalent LP.
(a) Minimize ∥Ax −b∥∞(ℓ∞-norm approximation).
(b) Minimize ∥Ax −b∥1 (ℓ1-norm approximation).
(c) Minimize ∥Ax −b∥1 subject to ∥x∥∞≤1.
(d) Minimize ∥x∥1 subject to ∥Ax −b∥∞≤1.
(e) Minimize ∥Ax −b∥1 + ∥x∥∞.
In each problem, A ∈Rm×n and b ∈Rm are given. (See §6.1 for more problems involving
approximation and constrained approximation.)
4.12 Network ﬂow problem. Consider a network of n nodes, with directed links connecting each
pair of nodes. The variables in the problem are the ﬂows on each link: xij will denote the
ﬂow from node i to node j. The cost of the ﬂow along the link from node i to node j is
given by cijxij, where cij are given constants. The total cost across the network is
C =
n
X
i,j=1
cijxij.
Each link ﬂow xij is also subject to a given lower bound lij (usually assumed to be
nonnegative) and an upper bound uij.
The external supply at node i is given by bi, where bi > 0 means an external ﬂow enters
the network at node i, and bi < 0 means that at node i, an amount |bi| ﬂows out of the
network. We assume that 1T b = 0, i.e., the total external supply equals total external
demand. At each node we have conservation of ﬂow: the total ﬂow into node i along links
and the external supply, minus the total ﬂow out along the links, equals zero.
The problem is to minimize the total cost of ﬂow through the network, subject to the
constraints described above. Formulate this problem as an LP.
4.13 Robust LP with interval coeﬃcients. Consider the problem, with variable x ∈Rn,
minimize
cT x
subject to
Ax ⪯b for all A ∈A,
where A ⊆Rm×n is the set
A = {A ∈Rm×n | ¯Aij −Vij ≤Aij ≤¯Aij + Vij, i = 1, . . . , m, j = 1, . . . , n}.
(The matrices ¯A and V are given.) This problem can be interpreted as an LP where each
coeﬃcient of A is only known to lie in an interval, and we require that x must satisfy the
constraints for all possible values of the coeﬃcients.
Express this problem as an LP. The LP you construct should be eﬃcient, i.e., it should
not have dimensions that grow exponentially with n or m.


## Page 8

194
4
Convex optimization problems
4.14 Approximating a matrix in inﬁnity norm. The ℓ∞-norm induced norm of a matrix A ∈
Rm×n, denoted ∥A∥∞, is given by
∥A∥∞= sup
x̸=0
∥Ax∥∞
∥x∥∞
=
max
i=1,...,m
n
X
j=1
|aij|.
This norm is sometimes called the max-row-sum norm, for obvious reasons (see §A.1.5).
Consider the problem of approximating a matrix, in the max-row-sum norm, by a linear
combination of other matrices. That is, we are given k + 1 matrices A0, . . . , Ak ∈Rm×n,
and need to ﬁnd x ∈Rk that minimizes
∥A0 + x1A1 + · · · + xkAk∥∞.
Express this problem as a linear program. Explain the signiﬁcance of any extra variables
in your LP. Carefully explain how your LP formulation solves this problem, e.g., what is
the relation between the feasible set for your LP and this problem?
4.15 Relaxation of Boolean LP. In a Boolean linear program, the variable x is constrained to
have components equal to zero or one:
minimize
cT x
subject to
Ax ⪯b
xi ∈{0, 1},
i = 1, . . . , n.
(4.67)
In general, such problems are very diﬃcult to solve, even though the feasible set is ﬁnite
(containing at most 2n points).
In a general method called relaxation, the constraint that xi be zero or one is replaced
with the linear inequalities 0 ≤xi ≤1:
minimize
cT x
subject to
Ax ⪯b
0 ≤xi ≤1,
i = 1, . . . , n.
(4.68)
We refer to this problem as the LP relaxation of the Boolean LP (4.67). The LP relaxation
is far easier to solve than the original Boolean LP.
(a) Show that the optimal value of the LP relaxation (4.68) is a lower bound on the
optimal value of the Boolean LP (4.67). What can you say about the Boolean LP
if the LP relaxation is infeasible?
(b) It sometimes happens that the LP relaxation has a solution with xi ∈{0, 1}. What
can you say in this case?
4.16 Minimum fuel optimal control. We consider a linear dynamical system with state x(t) ∈
Rn, t = 0, . . . , N, and actuator or input signal u(t) ∈R, for t = 0, . . . , N −1.
The
dynamics of the system is given by the linear recurrence
x(t + 1) = Ax(t) + bu(t),
t = 0, . . . , N −1,
where A ∈Rn×n and b ∈Rn are given. We assume that the initial state is zero, i.e.,
x(0) = 0.
The minimum fuel optimal control problem is to choose the inputs u(0), . . . , u(N −1) so
as to minimize the total fuel consumed, which is given by
F =
N−1
X
t=0
f(u(t)),


## Page 9

Exercises
195
subject to the constraint that x(N) = xdes, where N is the (given) time horizon, and
xdes ∈Rn is the (given) desired ﬁnal or target state. The function f : R →R is the fuel
use map for the actuator, and gives the amount of fuel used as a function of the actuator
signal amplitude. In this problem we use
f(a) =

|a|
|a| ≤1
2|a| −1
|a| > 1.
This means that fuel use is proportional to the absolute value of the actuator signal, for
actuator signals between −1 and 1; for larger actuator signals the marginal fuel eﬃciency
is half.
Formulate the minimum fuel optimal control problem as an LP.
4.17 Optimal activity levels. We consider the selection of n nonnegative activity levels, denoted
x1, . . . , xn. These activities consume m resources, which are limited. Activity j consumes
Aijxj of resource i, where Aij are given. The total resource consumption is additive, so
the total of resource i consumed is ci = Pn
j=1 Aijxj. (Ordinarily we have Aij ≥0, i.e.,
activity j consumes resource i. But we allow the possibility that Aij < 0, which means
that activity j actually generates resource i as a by-product.) Each resource consumption
is limited: we must have ci ≤cmax
i
, where cmax
i
are given. Each activity generates revenue,
which is a piecewise-linear concave function of the activity level:
rj(xj) =

pjxj
0 ≤xj ≤qj
pjqj + pdisc
j
(xj −qj)
xj ≥qj.
Here pj > 0 is the basic price, qj > 0 is the quantity discount level, and pdisc
j
is the
quantity discount price, for (the product of) activity j. (We have 0 < pdisc
j
< pj.) The
total revenue is the sum of the revenues associated with each activity, i.e., Pn
j=1 rj(xj).
The goal is to choose activity levels that maximize the total revenue while respecting the
resource limits. Show how to formulate this problem as an LP.
4.18 Separating hyperplanes and spheres.
Suppose you are given two sets of points in Rn,
{v1, v2, . . . , vK} and {w1, w2, . . . , wL}. Formulate the following two problems as LP fea-
sibility problems.
(a) Determine a hyperplane that separates the two sets, i.e., ﬁnd a ∈Rn and b ∈R
with a̸ = 0 such that
aT vi ≤b,
i = 1, . . . , K,
aT wi ≥b,
i = 1, . . . , L.
Note that we require a̸ = 0, so you have to make sure that your formulation excludes
the trivial solution a = 0, b = 0. You can assume that
rank

v1
v2
· · ·
vK
w1
w2
· · ·
wL
1
1
· · ·
1
1
1
· · ·
1

= n + 1
(i.e., the aﬃne hull of the K + L points has dimension n).
(b) Determine a sphere separating the two sets of points, i.e., ﬁnd xc ∈Rn and R ≥0
such that
∥vi −xc∥2 ≤R,
i = 1, . . . , K,
∥wi −xc∥2 ≥R,
i = 1, . . . , L.
(Here xc is the center of the sphere; R is its radius.)
(See chapter 8 for more on separating hyperplanes, separating spheres, and related topics.)


## Page 10

196
4
Convex optimization problems
4.19 Consider the problem
minimize
∥Ax −b∥1/(cT x + d)
subject to
∥x∥∞≤1,
where A ∈Rm×n, b ∈Rm, c ∈Rn, and d ∈R. We assume that d > ∥c∥1, which implies
that cT x + d > 0 for all feasible x.
(a) Show that this is a quasiconvex optimization problem.
(b) Show that it is equivalent to the convex optimization problem
minimize
∥Ay −bt∥1
subject to
∥y∥∞≤t
cT y + dt = 1,
with variables y ∈Rn, t ∈R.
4.20 Power assignment in a wireless communication system. We consider n transmitters with
powers p1, . . . , pn ≥0, transmitting to n receivers. These powers are the optimization
variables in the problem. We let G ∈Rn×n denote the matrix of path gains from the
transmitters to the receivers; Gij ≥0 is the path gain from transmitter j to receiver i.
The signal power at receiver i is then Si = Giipi, and the interference power at receiver i
is Ii = P
k̸=i Gikpk. The signal to interference plus noise ratio, denoted SINR, at receiver
i, is given by Si/(Ii + σi), where σi > 0 is the (self-) noise power in receiver i. The
objective in the problem is to maximize the minimum SINR ratio, over all receivers, i.e.,
to maximize
min
i=1,...,n
Si
Ii + σi .
There are a number of constraints on the powers that must be satisﬁed, in addition to the
obvious one pi ≥0. The ﬁrst is a maximum allowable power for each transmitter, i.e.,
pi ≤P max
i
, where P max
i
> 0 is given. In addition, the transmitters are partitioned into
groups, with each group sharing the same power supply, so there is a total power constraint
for each group of transmitter powers.
More precisely, we have subsets K1, . . . , Km of
{1, . . . , n} with K1 ∪· · · ∪Km = {1, . . . , n}, and Kj ∩Kl = 0 if j̸ = l. For each group Kl,
the total associated transmitter power cannot exceed P gp
l
> 0:
X
k∈Kl
pk ≤P gp
l ,
l = 1, . . . , m.
Finally, we have a limit P rc
k > 0 on the total received power at each receiver:
n
X
k=1
Gikpk ≤P rc
i ,
i = 1, . . . , n.
(This constraint reﬂects the fact that the receivers will saturate if the total received power
is too large.)
Formulate the SINR maximization problem as a generalized linear-fractional program.
Quadratic optimization problems
4.21 Some simple QCQPs. Give an explicit solution of each of the following QCQPs.
(a) Minimizing a linear function over an ellipsoid centered at the origin.
minimize
cT x
subject to
xT Ax ≤1,
where A ∈Sn
++ and c̸ = 0.
What is the solution if the problem is not convex
(A̸ ∈Sn
+)?


## Page 11

Exercises
197
(b) Minimizing a linear function over an ellipsoid.
minimize
cT x
subject to
(x −xc)T A(x −xc) ≤1,
where A ∈Sn
++ and c̸ = 0.
(c) Minimizing a quadratic form over an ellipsoid centered at the origin.
minimize
xT Bx
subject to
xT Ax ≤1,
where A ∈Sn
++ and B ∈Sn
+. Also consider the nonconvex extension with B̸ ∈Sn
+.
(See §B.1.)
4.22 Consider the QCQP
minimize
(1/2)xT Px + qT x + r
subject to
xT x ≤1,
with P ∈Sn
++. Show that x⋆= −(P + λI)−1q where λ = max{0, ¯λ} and ¯λ is the largest
solution of the nonlinear equation
qT (P + λI)−2q = 1.
4.23 ℓ4-norm approximation via QCQP. Formulate the ℓ4-norm approximation problem
minimize
∥Ax −b∥4 = (Pm
i=1(aT
i x −bi)4)1/4
as a QCQP. The matrix A ∈Rm×n (with rows aT
i ) and the vector b ∈Rm are given.
4.24 Complex ℓ1-, ℓ2- and ℓ∞-norm approximation. Consider the problem
minimize
∥Ax −b∥p,
where A ∈Cm×n, b ∈Cm, and the variable is x ∈Cn. The complex ℓp-norm is deﬁned
by
∥y∥p =
 m
X
i=1
|yi|p
!1/p
for p ≥1, and ∥y∥∞= maxi=1,...,m |yi|. For p = 1, 2, and ∞, express the complex ℓp-norm
approximation problem as a QCQP or SOCP with real variables and data.
4.25 Linear separation of two sets of ellipsoids. Suppose we are given K + L ellipsoids
Ei = {Piu + qi | ∥u∥2 ≤1},
i = 1, . . . , K + L,
where Pi ∈Sn. We are interested in ﬁnding a hyperplane that strictly separates E1, . . . ,
EK from EK+1, . . . , EK+L, i.e., we want to compute a ∈Rn, b ∈R such that
aT x + b > 0 for x ∈E1 ∪· · · ∪EK,
aT x + b < 0 for x ∈EK+1 ∪· · · ∪EK+L,
or prove that no such hyperplane exists. Express this problem as an SOCP feasibility
problem.
4.26 Hyperbolic constraints as SOC constraints. Verify that x ∈Rn, y, z ∈R satisfy
xT x ≤yz,
y ≥0,
z ≥0
if and only if


2x
y −z

2
≤y + z,
y ≥0,
z ≥0.
Use this observation to cast the following problems as SOCPs.


## Page 12

198
4
Convex optimization problems
(a) Maximizing harmonic mean.
maximize
 Pm
i=1 1/(aT
i x −bi)−1 ,
with domain {x | Ax ≻b}, where aT
i is the ith row of A.
(b) Maximizing geometric mean.
maximize
 Qm
i=1(aT
i x −bi)1/m ,
with domain {x | Ax ⪰b}, where aT
i is the ith row of A.
4.27 Matrix fractional minimization via SOCP. Express the following problem as an SOCP:
minimize
(Ax + b)T (I + B diag(x)BT )−1(Ax + b)
subject to
x ⪰0,
with A ∈Rm×n, b ∈Rm, B ∈Rm×n. The variable is x ∈Rn.
Hint. First show that the problem is equivalent to
minimize
vT v + wT diag(x)−1w
subject to
v + Bw = Ax + b
x ⪰0,
with variables v ∈Rm, w, x ∈Rn. (If xi = 0 we interpret w2
i /xi as zero if wi = 0 and as
∞otherwise.) Then use the results of exercise 4.26.
4.28 Robust quadratic programming. In §4.4.2 we discussed robust linear programming as an
application of second-order cone programming.
In this problem we consider a similar
robust variation of the (convex) quadratic program
minimize
(1/2)xT Px + qT x + r
subject to
Ax ⪯b.
For simplicity we assume that only the matrix P is subject to errors, and the other
parameters (q, r, A, b) are exactly known. The robust quadratic program is deﬁned as
minimize
supP ∈E((1/2)xT Px + qT x + r)
subject to
Ax ⪯b
where E is the set of possible matrices P.
For each of the following sets E, express the robust QP as a convex problem. Be as speciﬁc
as you can. If the problem can be expressed in a standard form (e.g., QP, QCQP, SOCP,
SDP), say so.
(a) A ﬁnite set of matrices: E = {P1, . . . , PK}, where Pi ∈Sn
+, i = 1, . . . , K.
(b) A set speciﬁed by a nominal value P0 ∈Sn
+ plus a bound on the eigenvalues of the
deviation P −P0:
E = {P ∈Sn | −γI ⪯P −P0 ⪯γI}
where γ ∈R and P0 ∈Sn
+,
(c) An ellipsoid of matrices:
E =
(
P0 +
K
X
i=1
Piui
 ∥u∥2 ≤1
)
.
You can assume Pi ∈Sn
+, i = 0, . . . , K.


## Page 13

Exercises
199
4.29 Maximizing probability of satisfying a linear inequality. Let c be a random variable in Rn,
normally distributed with mean ¯c and covariance matrix R. Consider the problem
maximize
prob(cT x ≥α)
subject to
Fx ⪯g,
Ax = b.
Assuming there exists a feasible point ˜x for which ¯cT ˜x ≥α, show that this problem is
equivalent to a convex or quasiconvex optimization problem. Formulate the problem as a
QP, QCQP, or SOCP (if the problem is convex), or explain how you can solve it by solving
a sequence of QP, QCQP, or SOCP feasibility problems (if the problem is quasiconvex).
Geometric programming
4.30 A heated ﬂuid at temperature T (degrees above ambient temperature) ﬂows in a pipe
with ﬁxed length and circular cross section with radius r. A layer of insulation, with
thickness w ≪r, surrounds the pipe to reduce heat loss through the pipe walls. The
design variables in this problem are T, r, and w.
The heat loss is (approximately) proportional to Tr/w, so over a ﬁxed lifetime, the energy
cost due to heat loss is given by α1Tr/w. The cost of the pipe, which has a ﬁxed wall
thickness, is approximately proportional to the total material, i.e., it is given by α2r. The
cost of the insulation is also approximately proportional to the total insulation material,
i.e., α3rw (using w ≪r). The total cost is the sum of these three costs.
The heat ﬂow down the pipe is entirely due to the ﬂow of the ﬂuid, which has a ﬁxed
velocity, i.e., it is given by α4Tr2. The constants αi are all positive, as are the variables
T, r, and w.
Now the problem: maximize the total heat ﬂow down the pipe, subject to an upper limit
Cmax on total cost, and the constraints
Tmin ≤T ≤Tmax,
rmin ≤r ≤rmax,
wmin ≤w ≤wmax,
w ≤0.1r.
Express this problem as a geometric program.
4.31 Recursive formulation of optimal beam design problem. Show that the GP (4.46) is equiv-
alent to the GP
minimize
PN
i=1 wihi
subject to
wi/wmax ≤1,
wmin/wi ≤1,
i = 1, . . . , N
hi/hmax ≤1,
hmin/hi ≤1,
i = 1, . . . , N
hi/(wiSmax) ≤1,
Sminwi/hi ≤1,
i = 1, . . . , N
6iF/(σmaxwih2
i ) ≤1,
i = 1, . . . , N
(2i −1)di/vi + vi+1/vi ≤1,
i = 1, . . . , N
(i −1/3)di/yi + vi+1/yi + yi+1/yi ≤1,
i = 1, . . . , N
y1/ymax ≤1
Ewih3
i di/(6F) = 1,
i = 1, . . . , N.
The variables are wi, hi, vi, di, yi for i = 1, . . . , N.
4.32 Approximating a function as a monomial. Suppose the function f : Rn →R is diﬀer-
entiable at a point x0 ≻0, with f(x0) > 0. How would you ﬁnd a monomial function
ˆf : Rn →R such that f(x0) = ˆf(x0) and for x near x0, ˆf(x) is very near f(x)?
4.33 Express the following problems as convex optimization problems.
(a) Minimize max{p(x), q(x)}, where p and q are posynomials.
(b) Minimize exp(p(x)) + exp(q(x)), where p and q are posynomials.
(c) Minimize p(x)/(r(x) −q(x)), subject to r(x) > q(x), where p, q are posynomials,
and r is a monomial.


## Page 14

200
4
Convex optimization problems
4.34 Log-convexity of Perron-Frobenius eigenvalue. Let A ∈Rn×n be an elementwise positive
matrix, i.e., Aij > 0.
(The results of this problem hold for irreducible nonnegative
matrices as well.) Let λpf(A) denotes its Perron-Frobenius eigenvalue, i.e., its eigenvalue
of largest magnitude.
(See the deﬁnition and the example on page 165.)
Show that
log λpf(A) is a convex function of log Aij. This means, for example, that we have the
inequality
λpf(C) ≤(λpf(A)λpf(B))1/2 ,
where Cij = (AijBij)1/2, and A and B are elementwise positive matrices.
Hint.
Use the characterization of the Perron-Frobenius eigenvalue given in (4.47), or,
alternatively, use the characterization
log λpf(A) = lim
k→∞(1/k) log(1T Ak1).
4.35 Signomial and geometric programs. A signomial is a linear combination of monomials of
some positive variables x1, . . . , xn. Signomials are more general than posynomials, which
are signomials with all positive coeﬃcients.
A signomial program is an optimization
problem of the form
minimize
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m
hi(x) = 0,
i = 1, . . . , p,
where f0, . . . , fm and h1, . . . , hp are signomials. In general, signomial programs are very
diﬃcult to solve.
Some signomial programs can be transformed to GPs, and therefore solved eﬃciently.
Show how to do this for a signomial program of the following form:
• The objective signomial f0 is a posynomial, i.e., its terms have only positive coeﬃ-
cients.
• Each inequality constraint signomial f1, . . . , fm has exactly one term with a negative
coeﬃcient: fi = pi −qi where pi is posynomial, and qi is monomial.
• Each equality constraint signomial h1, . . . , hp has exactly one term with a positive
coeﬃcient and one term with a negative coeﬃcient: hi = ri −si where ri and si are
monomials.
4.36 Explain how to reformulate a general GP as an equivalent GP in which every posynomial
(in the objective and constraints) has at most two monomial terms. Hint. Express each
sum (of monomials) as a sum of sums, each with two terms.
4.37 Generalized posynomials and geometric programming. Let x1, . . . , xn be positive variables,
and suppose the functions fi : Rn →R, i = 1, . . . , k, are posynomials of x1, . . . , xn. If
φ : Rk →R is a polynomial with nonnegative coeﬃcients, then the composition
h(x) = φ(f1(x), . . . , fk(x))
(4.69)
is a posynomial, since posynomials are closed under products, sums, and multiplication
by nonnegative scalars. For example, suppose f1 and f2 are posynomials, and consider
the polynomial φ(z1, z2) = 3z2
1z2 + 2z1 + 3z3
2 (which has nonnegative coeﬃcients). Then
h = 3f 2
1 f2 + 2f1 + f 3
2 is a posynomial.
In this problem we consider a generalization of this idea, in which φ is allowed to be
a posynomial, i.e., can have fractional exponents. Speciﬁcally, assume that φ : Rk →
R is a posynomial, with all its exponents nonnegative.
In this case we will call the
function h deﬁned in (4.69) a generalized posynomial. As an example, suppose f1 and f2
are posynomials, and consider the posynomial (with nonnegative exponents) φ(z1, z2) =
2z0.3
1 z1.2
2
+ z1z0.5
2
+ 2. Then the function
h(x) = 2f1(x)0.3f2(x)1.2 + f1(x)f2(x)0.5 + 2


## Page 15

Exercises
201
is a generalized posynomial. Note that it is not a posynomial, however (unless f1 and f2
are monomials or constants).
A generalized geometric program (GGP) is an optimization problem of the form
minimize
h0(x)
subject to
hi(x) ≤1,
i = 1, . . . , m
gi(x) = 1,
i = 1, . . . , p,
(4.70)
where g1, . . . , gp are monomials, and h0, . . . , hm are generalized posynomials.
Show how to express this generalized geometric program as an equivalent geometric pro-
gram. Explain any new variables you introduce, and explain how your GP is equivalent
to the GGP (4.70).
Semideﬁnite programming and conic form problems
4.38 LMIs and SDPs with one variable. The generalized eigenvalues of a matrix pair (A, B),
where A, B ∈Sn, are deﬁned as the roots of the polynomial det(λB −A) (see §A.5.3).
Suppose B is nonsingular, and that A and B can be simultaneously diagonalized by a
congruence, i.e., there exists a nonsingular R ∈Rn×n such that
RT AR = diag(a),
RT BR = diag(b),
where a, b ∈Rn. (A suﬃcient condition for this to hold is that there exists t1, t2 such
that t1A + t2B ≻0.)
(a) Show that the generalized eigenvalues of (A, B) are real, and given by λi = ai/bi,
i = 1, . . . , n.
(b) Express the solution of the SDP
minimize
ct
subject to
tB ⪯A,
with variable t ∈R, in terms of a and b.
4.39 SDPs and congruence transformations. Consider the SDP
minimize
cT x
subject to
x1F1 + x2F2 + · · · + xnFn + G ⪯0,
with Fi, G ∈Sk, c ∈Rn.
(a) Suppose R ∈Rk×k is nonsingular. Show that the SDP is equivalent to the SDP
minimize
cT x
subject to
x1 ˜F1 + x2 ˜F2 + · · · + xn ˜Fn + ˜G ⪯0,
where ˜Fi = RT FiR, ˜G = RT GR.
(b) Suppose there exists a nonsingular R such that ˜Fi and ˜G are diagonal. Show that
the SDP is equivalent to an LP.
(c) Suppose there exists a nonsingular R such that ˜Fi and ˜G have the form
˜Fi =

αiI
ai
aT
i
αi

,
i = 1, . . . , n,
˜G =

βI
b
bT
β

,
where αi, β ∈R, ai, b ∈Rk−1. Show that the SDP is equivalent to an SOCP with
a single second-order cone constraint.


## Page 16

202
4
Convex optimization problems
4.40 LPs, QPs, QCQPs, and SOCPs as SDPs. Express the following problems as SDPs.
(a) The LP (4.27).
(b) The QP (4.34), the QCQP (4.35) and the SOCP (4.36). Hint. Suppose A ∈Sr
++,
C ∈Ss, and B ∈Rr×s. Then

A
B
BT
C

⪰0 ⇐⇒C −BT A−1B ⪰0.
For a more complete statement, which applies also to singular A, and a proof,
see §A.5.5.
(c) The matrix fractional optimization problem
minimize
(Ax + b)T F(x)−1(Ax + b)
where A ∈Rm×n, b ∈Rm,
F(x) = F0 + x1F1 + · · · + xnFn,
with Fi ∈Sm, and we take the domain of the objective to be {x | F(x) ≻0}. You
can assume the problem is feasible (there exists at least one x with F(x) ≻0).
4.41 LMI tests for copositive matrices and P0-matrices. A matrix A ∈Sn is said to be copositive
if xT Ax ≥0 for all x ⪰0 (see exercise 2.35). A matrix A ∈Rn×n is said to be a P0-
matrix if maxi=1,...,n xi(Ax)i ≥0 for all x. Checking whether a matrix is copositive or
a P0-matrix is very diﬃcult in general. However, there exist useful suﬃcient conditions
that can be veriﬁed using semideﬁnite programming.
(a) Show that A is copositive if it can be decomposed as a sum of a positive semideﬁnite
and an elementwise nonnegative matrix:
A = B + C,
B ⪰0,
Cij ≥0,
i, j = 1, . . . , n.
(4.71)
Express the problem of ﬁnding B and C that satisfy (4.71) as an SDP feasibility
problem.
(b) Show that A is a P0-matrix if there exists a positive diagonal matrix D such that
DA + AT D ⪰0.
(4.72)
Express the problem of ﬁnding a D that satisﬁes (4.72) as an SDP feasibility problem.
4.42 Complex LMIs and SDPs. A complex LMI has the form
x1F1 + · · · + xnFn + G ⪯0
where F1, . . . , Fn, G are complex n × n Hermitian matrices, i.e., F H
i
= Fi, GH = G, and
x ∈Rn is a real variable. A complex SDP is the problem of minimizing a (real) linear
function of x subject to a complex LMI constraint.
Complex LMIs and SDPs can be transformed to real LMIs and SDPs, using the fact that
X ⪰0 ⇐⇒

ℜX
−ℑX
ℑX
ℜX

⪰0,
where ℜX ∈Rn×n is the real part of the complex Hermitian matrix X, and ℑX ∈Rn×n
is the imaginary part of X.
Verify this result, and show how to pose a complex SDP as a real SDP.


## Page 17

Exercises
203
4.43 Eigenvalue optimization via SDP. Suppose A : Rn →Sm is aﬃne, i.e.,
A(x) = A0 + x1A1 + · · · + xnAn
where Ai ∈Sm. Let λ1(x) ≥λ2(x) ≥· · · ≥λm(x) denote the eigenvalues of A(x). Show
how to pose the following problems as SDPs.
(a) Minimize the maximum eigenvalue λ1(x).
(b) Minimize the spread of the eigenvalues, λ1(x) −λm(x).
(c) Minimize the condition number of A(x), subject to A(x) ≻0. The condition number
is deﬁned as κ(A(x)) = λ1(x)/λm(x), with domain {x | A(x) ≻0}. You may assume
that A(x) ≻0 for at least one x.
Hint. You need to minimize λ/γ, subject to
0 ≺γI ⪯A(x) ⪯λI.
Change variables to y = x/γ, t = λ/γ, s = 1/γ.
(d) Minimize the sum of the absolute values of the eigenvalues, |λ1(x)| + · · · + |λm(x)|.
Hint. Express A(x) as A(x) = A+ −A−, where A+ ⪰0, A−⪰0.
4.44 Optimization over polynomials. Pose the following problem as an SDP. Find the polyno-
mial p : R →R,
p(t) = x1 + x2t + · · · + x2k+1t2k,
that satisﬁes given bounds li ≤p(ti) ≤ui, at m speciﬁed points ti, and, of all the
polynomials that satisfy these bounds, has the greatest minimum value:
maximize
inft p(t)
subject to
li ≤p(ti) ≤ui,
i = 1, . . . , m.
The variables are x ∈R2k+1.
Hint. Use the LMI characterization of nonnegative polynomials derived in exercise 2.37,
part (b).
4.45 [Nes00, Par00] Sum-of-squares representation via LMIs. Consider a polynomial p : Rn →
R of degree 2k. The polynomial is said to be positive semideﬁnite (PSD) if p(x) ≥0
for all x ∈Rn. Except for special cases (e.g., n = 1 or k = 1), it is extremely diﬃcult
to determine whether or not a given polynomial is PSD, let alone solve an optimization
problem, with the coeﬃcients of p as variables, with the constraint that p be PSD.
A famous suﬃcient condition for a polynomial to be PSD is that it have the form
p(x) =
r
X
i=1
qi(x)2,
for some polynomials qi, with degree no more than k.
A polynomial p that has this
sum-of-squares form is called SOS.
The condition that a polynomial p be SOS (viewed as a constraint on its coeﬃcients)
turns out to be equivalent to an LMI, and therefore a variety of optimization problems,
with SOS constraints, can be posed as SDPs. You will explore these ideas in this problem.
(a) Let f1, . . . , fs be all monomials of degree k or less. (Here we mean monomial in
the standard sense, i.e., xm1
1
· · · xmn
n
, where mi ∈Z+, and not in the sense used in
geometric programming.) Show that if p can be expressed as a positive semideﬁnite
quadratic form p = f T V f, with V ∈Ss
+, then p is SOS. Conversely, show that if
p is SOS, then it can be expressed as a positive semideﬁnite quadratic form in the
monomials, i.e., p = f T V f, for some V ∈Ss
+.


## Page 18

204
4
Convex optimization problems
(b) Show that the condition p = f T V f is a set of linear equality constraints relating the
coeﬃcients of p and the matrix V . Combined with part (a) above, this shows that
the condition that p be SOS is equivalent to a set of linear equalities relating V and
the coeﬃcients of p, and the matrix inequality V ⪰0.
(c) Work out the LMI conditions for SOS explicitly for the case where p is polynomial
of degree four in two variables.
4.46 Multidimensional moments. The moments of a random variable t on R2 are deﬁned as
µij = E ti
1tj
2, where i, j are nonnegative integers. In this problem we derive necessary
conditions for a set of numbers µij, 0 ≤i, j ≤2k, i + j ≤2k, to be the moments of a
distribution on R2.
Let p : R2 →R be a polynomial of degree k with coeﬃcients cij,
p(t) =
k
X
i=0
k−i
X
j=0
cijti
1tj
2,
and let t be a random variable with moments µij. Suppose c ∈R(k+1)(k+2)/2 contains
the coeﬃcients cij in some speciﬁc order, and µ ∈R(k+1)(2k+1) contains the moments µij
in the same order. Show that E p(t)2 can be expressed as a quadratic form in c:
E p(t)2 = cT H(µ)c,
where H : R(k+1)(2k+1) →S(k+1)(k+2)/2 is a linear function of µ. From this, conclude
that µ must satisfy the LMI H(µ) ⪰0.
Remark: For random variables on R, the matrix H can be taken as the Hankel matrix
deﬁned in (4.52). In this case, H(µ) ⪰0 is a necessary and suﬃcient condition for µ to be
the moments of a distribution, or the limit of a sequence of moments. On R2, however,
the LMI is only a necessary condition.
4.47 Maximum determinant positive semideﬁnite matrix completion.
We consider a matrix
A ∈Sn, with some entries speciﬁed, and the others not speciﬁed. The positive semideﬁnite
matrix completion problem is to determine values of the unspeciﬁed entries of the matrix
so that A ⪰0 (or to determine that such a completion does not exist).
(a) Explain why we can assume without loss of generality that the diagonal entries of
A are speciﬁed.
(b) Show how to formulate the positive semideﬁnite completion problem as an SDP
feasibility problem.
(c) Assume that A has at least one completion that is positive deﬁnite, and the diag-
onal entries of A are speciﬁed (i.e., ﬁxed). The positive deﬁnite completion with
largest determinant is called the maximum determinant completion. Show that the
maximum determinant completion is unique. Show that if A⋆is the maximum de-
terminant completion, then (A⋆)−1 has zeros in all the entries of the original matrix
that were not speciﬁed. Hint. The gradient of the function f(X) = log det X is
∇f(X) = X−1 (see §A.4.1).
(d) Suppose A is speciﬁed on its tridiagonal part, i.e., we are given A11, . . . , Ann and
A12, . . . , An−1,n. Show that if there exists a positive deﬁnite completion of A, then
there is a positive deﬁnite completion whose inverse is tridiagonal.
4.48 Generalized eigenvalue minimization.
Recall (from example 3.37, or §A.5.3) that the
largest generalized eigenvalue of a pair of matrices (A, B) ∈Sk × Sk
++ is given by
λmax(A, B) = sup
u̸=0
uT Au
uT Bu = max{λ | det(λB −A) = 0}.
As we have seen, this function is quasiconvex (if we take Sk × Sk
++ as its domain).


## Page 19

Exercises
205
We consider the problem
minimize
λmax(A(x), B(x))
(4.73)
where A, B : Rn →Sk are aﬃne functions, deﬁned as
A(x) = A0 + x1A1 + · · · + xnAn,
B(x) = B0 + x1B1 + · · · + xnBn.
with Ai, Bi ∈Sk.
(a) Give a family of convex functions φt : Sk × Sk →R, that satisfy
λmax(A, B) ≤t ⇐⇒φt(A, B) ≤0
for all (A, B) ∈Sk × Sk
++. Show that this allows us to solve (4.73) by solving a
sequence of convex feasibility problems.
(b) Give a family of matrix-convex functions Φt : Sk × Sk →Sk that satisfy
λmax(A, B) ≤t ⇐⇒Φt(A, B) ⪯0
for all (A, B) ∈Sk × Sk
++. Show that this allows us to solve (4.73) by solving a
sequence of convex feasibility problems with LMI constraints.
(c) Suppose B(x) = (aT x+b)I, with a̸ = 0. Show that (4.73) is equivalent to the convex
problem
minimize
λmax(sA0 + y1A1 + · · · + ynAn)
subject to
aT y + bs = 1
s ≥0,
with variables y ∈Rn, s ∈R.
4.49 Generalized fractional programming.
Let K ∈Rm be a proper cone.
Show that the
function f0 : Rn →Rm, deﬁned by
f0(x) = inf{t | Cx + d ⪯K t(Fx + g)},
dom f0 = {x | Fx + g ≻K 0},
with C, F ∈Rm×n, d, g ∈Rm, is quasiconvex.
A quasiconvex optimization problem with objective function of this form is called a gen-
eralized fractional program. Express the generalized linear-fractional program of page 152
and the generalized eigenvalue minimization problem (4.73) as generalized fractional pro-
grams.
Vector and multicriterion optimization
4.50 Bi-criterion optimization. Figure 4.11 shows the optimal trade-oﬀcurve and the set of
achievable values for the bi-criterion optimization problem
minimize (w.r.t. R2
+)
(∥Ax −b∥2, ∥x∥2
2),
for some A ∈R100×10, b ∈R100. Answer the following questions using information from
the plot. We denote by xls the solution of the least-squares problem
minimize
∥Ax −b∥2
2.
(a) What is ∥xls∥2?
(b) What is ∥Axls −b∥2?
(c) What is ∥b∥2?


## Page 20

206
4
Convex optimization problems
(d) Give the optimal value of the problem
minimize
∥Ax −b∥2
2
subject to
∥x∥2
2 = 1.
(e) Give the optimal value of the problem
minimize
∥Ax −b∥2
2
subject to
∥x∥2
2 ≤1.
(f) Give the optimal value of the problem
minimize ∥Ax −b∥2
2 + ∥x∥2
2.
(g) What is the rank of A?
4.51 Monotone transformation of objective in vector optimization. Consider the vector opti-
mization problem (4.56). Suppose we form a new vector optimization problem by replacing
the objective f0 with φ ◦f0, where φ : Rq →Rq satisﬁes
u ⪯K v, u̸ = v =⇒φ(u) ⪯K φ(v), φ(u)̸ = φ(v).
Show that a point x is Pareto optimal (or optimal) for one problem if and only if it is
Pareto optimal (optimal) for the other, so the two problems are equivalent. In particular,
composing each objective in a multicriterion problem with an increasing function does
not aﬀect the Pareto optimal points.
4.52 Pareto optimal points and the boundary of the set of achievable values. Consider a vector
optimization problem with cone K. Let P denote the set of Pareto optimal values, and
let O denote the set of achievable objective values. Show that P ⊆O ∩bd O, i.e., every
Pareto optimal value is an achievable objective value that lies in the boundary of the set
of achievable objective values.
4.53 Suppose the vector optimization problem (4.56) is convex. Show that the set
A = O + K = {t ∈Rq | f0(x) ⪯K t for some feasible x},
is convex. Also show that the minimal elements of A are the same as the minimal points
of O.
4.54 Scalarization and optimal points. Suppose a (not necessarily convex) vector optimization
problem has an optimal point x⋆. Show that x⋆is a solution of the associated scalarized
problem for any choice of λ ≻K∗0. Also show the converse: If a point x is a solution of
the scalarized problem for any choice of λ ≻K∗0, then it is an optimal point for the (not
necessarily convex) vector optimization problem.
4.55 Generalization of weighted-sum scalarization. In §4.7.4 we showed how to obtain Pareto
optimal solutions of a vector optimization problem by replacing the vector objective f0 :
Rn →Rq with the scalar objective λT f0, where λ ≻K∗0.
Let ψ : Rq →R be a
K-increasing function, i.e., satisfying
u ⪯K v, u̸ = v =⇒ψ(u) < ψ(v).
Show that any solution of the problem
minimize
ψ(f0(x))
subject to
fi(x) ≤0,
i = 1, . . . , m
hi(x) = 0,
i = 1, . . . , p


## Page 21

Exercises
207
is Pareto optimal for the vector optimization problem
minimize (w.r.t. K)
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m
hi(x) = 0,
i = 1, . . . , p.
Note that ψ(u) = λT u, where λ ≻K∗0, is a special case.
As a related example, show that in a multicriterion optimization problem (i.e., a vector
optimization problem with f0 = F : Rn →Rq, and K = Rq
+), a unique solution of the
scalar optimization problem
minimize
maxi=1,...,q Fi(x)
subject to
fi(x) ≤0,
i = 1, . . . , m
hi(x) = 0,
i = 1, . . . , p,
is Pareto optimal.
Miscellaneous problems
4.56 [P. Parrilo] We consider the problem of minimizing the convex function f0 : Rn →R
over the convex hull of the union of some convex sets, conv  Sq
i=1 Ci

. These sets are
described via convex inequalities,
Ci = {x | fij(x) ≤0, j = 1, . . . , ki},
where fij : Rn →R are convex.
Our goal is to formulate this problem as a convex
optimization problem.
The obvious approach is to introduce variables x1, . . . , xq ∈Rn, with xi ∈Ci, θ ∈Rq
with θ ⪰0, 1T θ = 1, and a variable x ∈Rn, with x = θ1x1 + · · · + θqxq. This equality
constraint is not aﬃne in the variables, so this approach does not yield a convex problem.
A more sophisticated formulation is given by
minimize
f0(x)
subject to
sifij(zi/si) ≤0,
i = 1, . . . , q,
j = 1, . . . , ki
1T s = 1,
s ⪰0
x = z1 + · · · + zq,
with variables z1, . . . , zq ∈Rn, x ∈Rn, and s1, . . . , sq ∈R. (When si = 0, we take
sifij(zi/si) to be 0 if zi = 0 and ∞if zi̸ = 0.) Explain why this problem is convex, and
equivalent to the original problem.
4.57 Capacity of a communication channel. We consider a communication channel, with input
X(t) ∈{1, . . . , n}, and output Y (t) ∈{1, . . . , m}, for t = 1, 2, . . . (in seconds, say). The
relation between the input and the output is given statistically:
pij = prob(Y (t) = i|X(t) = j),
i = 1, . . . , m,
j = 1, . . . , n.
The matrix P ∈Rm×n is called the channel transition matrix, and the channel is called
a discrete memoryless channel.
A famous result of Shannon states that information can be sent over the communication
channel, with arbitrarily small probability of error, at any rate less than a number C,
called the channel capacity, in bits per second. Shannon also showed that the capacity of
a discrete memoryless channel can be found by solving an optimization problem. Assume
that X has a probability distribution denoted x ∈Rn, i.e.,
xj = prob(X = j),
j = 1, . . . , n.


## Page 22

208
4
Convex optimization problems
The mutual information between X and Y is given by
I(X; Y ) =
m
X
i=1
n
X
j=1
xjpij log2
pij
Pn
k=1 xkpik
.
Then the channel capacity C is given by
C = sup
x
I(X; Y ),
where the supremum is over all possible probability distributions for the input X, i.e.,
over x ⪰0, 1T x = 1.
Show how the channel capacity can be computed using convex optimization.
Hint.
Introduce the variable y = Px, which gives the probability distribution of the
output Y , and show that the mutual information can be expressed as
I(X; Y ) = cT x −
m
X
i=1
yi log2 yi,
where cj = Pm
i=1 pij log2 pij, j = 1, . . . , n.
4.58 Optimal consumption. In this problem we consider the optimal way to consume (or spend)
an initial amount of money (or other asset) k0 over time. The variables are c0, . . . , cT ,
where ct ≥0 denotes the consumption in period t. The utility derived from a consumption
level c is given by u(c), where u : R →R is an increasing concave function. The present
value of the utility derived from the consumption is given by
U =
T
X
t=0
βtu(ct),
where 0 < β < 1 is a discount factor.
Let kt denote the amount of money available for investment in period t.
We assume
that it earns an investment return given by f(kt), where f : R →R is an increasing,
concave investment return function, which satisﬁes f(0) = 0. For example if the funds
earn simple interest at rate R percent per period, we have f(a) = (R/100)a. The amount
to be consumed, i.e., ct, is withdrawn at the end of the period, so we have the recursion
kt+1 = kt + f(kt) −ct,
t = 0, . . . , T.
The initial sum k0 > 0 is given. We require kt ≥0, t = 1, . . . , T +1 (but more sophisticated
models, which allow kt < 0, can be considered).
Show how to formulate the problem of maximizing U as a convex optimization problem.
Explain how the problem you formulate is equivalent to this one, and exactly how the
two are related.
Hint. Show that we can replace the recursion for kt given above with the inequalities
kt+1 ≤kt + f(kt) −ct,
t = 0, . . . , T.
(Interpretation: the inequalities give you the option of throwing money away in each
period.) For a more general version of this trick, see exercise 4.6.
4.59 Robust optimization.
In some optimization problems there is uncertainty or variation
in the objective and constraint functions, due to parameters or factors that are either
beyond our control or unknown. We can model this situation by making the objective
and constraint functions f0, . . . , fm functions of the optimization variable x ∈Rn and
a parameter vector u ∈Rk that is unknown, or varies. In the stochastic optimization


## Page 23

Exercises
209
approach, the parameter vector u is modeled as a random variable with a known dis-
tribution, and we work with the expected values Eu fi(x, u). In the worst-case analysis
approach, we are given a set U that u is known to lie in, and we work with the maximum
or worst-case values supu∈U fi(x, u). To simplify the discussion, we assume there are no
equality constraints.
(a) Stochastic optimization. We consider the problem
minimize
E f0(x, u)
subject to
E fi(x, u) ≤0,
i = 1, . . . , m,
where the expectation is with respect to u. Show that if fi are convex in x for each
u, then this stochastic optimization problem is convex.
(b) Worst-case optimization. We consider the problem
minimize
supu∈U f0(x, u)
subject to
supu∈U fi(x, u) ≤0,
i = 1, . . . , m.
Show that if fi are convex in x for each u, then this worst-case optimization problem
is convex.
(c) Finite set of possible parameter values. The observations made in parts (a) and (b)
are most useful when we have analytical or easily evaluated expressions for the
expected values E fi(x, u) or the worst-case values supu∈U fi(x, u).
Suppose we are given the set of possible values of the parameter is ﬁnite, i.e., we
have u ∈{u1, . . . , uN}. For the stochastic case, we are also given the probabilities
of each value: prob(u = ui) = pi, where p ∈RN, p ⪰0, 1T p = 1. In the worst-case
formulation, we simply take U ∈{u1, . . . , uN}.
Show how to set up the worst-case and stochastic optimization problems explicitly
(i.e., give explicit expressions for supu∈U fi and Eu fi).
4.60 Log-optimal investment strategy. We consider a portfolio problem with n assets held over
N periods. At the beginning of each period, we re-invest our total wealth, redistributing
it over the n assets using a ﬁxed, constant, allocation strategy x ∈Rn, where x ⪰0,
1T x = 1. In other words, if W(t −1) is our wealth at the beginning of period t, then
during period t we invest xiW(t−1) in asset i. We denote by λ(t) the total return during
period t, i.e., λ(t) = W(t)/W(t −1). At the end of the N periods our wealth has been
multiplied by the factor QN
t=1 λ(t). We call
1
N
N
X
t=1
log λ(t)
the growth rate of the investment over the N periods. We are interested in determining
an allocation strategy x that maximizes growth of our total wealth for large N.
We use a discrete stochastic model to account for the uncertainty in the returns. We
assume that during each period there are m possible scenarios, with probabilities πj,
j = 1, . . . , m.
In scenario j, the return for asset i over one period is given by pij.
Therefore, the return λ(t) of our portfolio during period t is a random variable, with
m possible values pT
1 x, . . . , pT
mx, and distribution
πj = prob(λ(t) = pT
j x),
j = 1, . . . , m.
We assume the same scenarios for each period, with (identical) independent distributions.
Using the law of large numbers, we have
lim
N→∞
1
N log

W(N)
W(0)

= lim
N→∞
1
N
N
X
t=1
log λ(t) = E log λ(t) =
m
X
j=1
πj log(pT
j x).


## Page 24

210
4
Convex optimization problems
In other words, with investment strategy x, the long term growth rate is given by
Rlt =
m
X
j=1
πj log(pT
j x).
The investment strategy x that maximizes this quantity is called the log-optimal invest-
ment strategy, and can be found by solving the optimization problem
maximize
Pm
j=1 πj log(pT
j x)
subject to
x ⪰0,
1T x = 1,
with variable x ∈Rn.
Show that this is a convex optimization problem.
4.61 Optimization with logistic model. A random variable X ∈{0, 1} satisﬁes
prob(X = 1) = p =
exp(aT x + b)
1 + exp(aT x + b),
where x ∈Rn is a vector of variables that aﬀect the probability, and a and b are known
parameters. We can think of X = 1 as the event that a consumer buys a product, and
x as a vector of variables that aﬀect the probability, e.g., advertising eﬀort, retail price,
discounted price, packaging expense, and other factors. The variable x, which we are to
optimize over, is subject to a set of linear constraints, Fx ⪯g.
Formulate the following problems as convex optimization problems.
(a) Maximizing buying probability. The goal is to choose x to maximize p.
(b) Maximizing expected proﬁt. Let cT x+d be the proﬁt derived from selling the product,
which we assume is positive for all feasible x. The goal is to maximize the expected
proﬁt, which is p(cT x + d).
4.62 Optimal power and bandwidth allocation in a Gaussian broadcast channel. We consider a
communication system in which a central node transmits messages to n receivers. (‘Gaus-
sian’ refers to the type of noise that corrupts the transmissions.) Each receiver channel
is characterized by its (transmit) power level Pi ≥0 and its bandwidth Wi ≥0. The
power and bandwidth of a receiver channel determine its bit rate Ri (the rate at which
information can be sent) via
Ri = αiWi log(1 + βiPi/Wi),
where αi and βi are known positive constants. For Wi = 0, we take Ri = 0 (which is
what you get if you take the limit as Wi →0).
The powers must satisfy a total power constraint, which has the form
P1 + · · · + Pn = Ptot,
where Ptot > 0 is a given total power available to allocate among the channels. Similarly,
the bandwidths must satisfy
W1 + · · · + Wn = Wtot,
where Wtot > 0 is the (given) total available bandwidth. The optimization variables in
this problem are the powers and bandwidths, i.e., P1, . . . , Pn, W1, . . . , Wn.
The objective is to maximize the total utility,
n
X
i=1
ui(Ri),


## Page 25

Exercises
211
where ui : R →R is the utility function associated with the ith receiver.
(You can
think of ui(Ri) as the revenue obtained for providing a bit rate Ri to receiver i, so the
objective is to maximize the total revenue.) You can assume that the utility functions ui
are nondecreasing and concave.
Pose this problem as a convex optimization problem.
4.63 Optimally balancing manufacturing cost and yield. The vector x ∈Rn denotes the nomi-
nal parameters in a manufacturing process. The yield of the process, i.e., the fraction of
manufactured goods that is acceptable, is given by Y (x). We assume that Y is log-concave
(which is often the case; see example 3.43). The cost per unit to manufacture the product
is given by cT x, where c ∈Rn. The cost per acceptable unit is cT x/Y (x). We want to
minimize cT x/Y (x), subject to some convex constraints on x such as a linear inequalities
Ax ⪯b. (You can assume that over the feasible set we have cT x > 0 and Y (x) > 0.)
This problem is not a convex or quasiconvex optimization problem, but it can be solved
using convex optimization and a one-dimensional search. The basic ideas are given below;
you must supply all details and justiﬁcation.
(a) Show that the function f : R →R given by
f(a) = sup{Y (x) | Ax ⪯b, cT x = a},
which gives the maximum yield versus cost, is log-concave.
This means that by
solving a convex optimization problem (in x) we can evaluate the function f.
(b) Suppose that we evaluate the function f for enough values of a to give a good approx-
imation over the range of interest. Explain how to use these data to (approximately)
solve the problem of minimizing cost per good product.
4.64 Optimization with recourse. In an optimization problem with recourse, also called two-
stage optimization, the cost function and constraints depend not only on our choice of
variables, but also on a discrete random variable s ∈{1, . . . , S}, which is interpreted as
specifying which of S scenarios occurred. The scenario random variable s has known
probability distribution π, with πi = prob(s = i), i = 1, . . . , S.
In two-stage optimization, we are to choose the values of two variables, x ∈Rn and
z ∈Rq. The variable x must be chosen before the particular scenario s is known; the
variable z, however, is chosen after the value of the scenario random variable is known.
In other words, z is a function of the scenario random variable s. To describe our choice
z, we list the values we would choose under the diﬀerent scenarios, i.e., we list the vectors
z1, . . . , zS ∈Rq.
Here z3 is our choice of z when s = 3 occurs, and so on. The set of values
x ∈Rn,
z1, . . . , zS ∈Rq
is called the policy, since it tells us what choice to make for x (independent of which
scenario occurs), and also, what choice to make for z in each possible scenario.
The variable z is called the recourse variable (or second-stage variable), since it allows
us to take some action or make a choice after we know which scenario occurred.
In
contrast, our choice of x (which is called the ﬁrst-stage variable) must be made without
any knowledge of the scenario.
For simplicity we will consider the case with no constraints. The cost function is given by
f : Rn × Rq × {1, . . . , S} →R,
where f(x, z, i) gives the cost when the ﬁrst-stage choice x is made, second-stage choice
z is made, and scenario i occurs. We will take as the overall objective, to be minimized
over all policies, the expected cost
E f(x, zs, s) =
S
X
i=1
πif(x, zi, i).


## Page 26

212
4
Convex optimization problems
Suppose that f is a convex function of (x, z), for each scenario i = 1, . . . , S. Explain
how to ﬁnd an optimal policy, i.e., one that minimizes the expected cost over all possible
policies, using convex optimization.
4.65 Optimal operation of a hybrid vehicle. A hybrid vehicle has an internal combustion engine,
a motor/generator connected to a storage battery, and a conventional (friction) brake. In
this exercise we consider a (highly simpliﬁed) model of a parallel hybrid vehicle, in which
both the motor/generator and the engine are directly connected to the drive wheels. The
engine can provide power to the wheels, and the brake can take power from the wheels,
turning it into heat. The motor/generator can act as a motor, when it uses energy stored
in the battery to deliver power to the wheels, or as a generator, when it takes power from
the wheels or engine, and uses the power to charge the battery. When the generator takes
power from the wheels and charges the battery, it is called regenerative braking; unlike
ordinary friction braking, the energy taken from the wheels is stored, and can be used
later. The vehicle is judged by driving it over a known, ﬁxed test track to evaluate its
fuel eﬃciency.
A diagram illustrating the power ﬂow in the hybrid vehicle is shown below. The arrows
indicate the direction in which the power ﬂow is considered positive. The engine power
peng, for example, is positive when it is delivering power; the brake power pbr is positive
when it is taking power from the wheels. The power preq is the required power at the
wheels. It is positive when the wheels require power (e.g., when the vehicle accelerates,
climbs a hill, or cruises on level terrain). The required wheel power is negative when the
vehicle must decelerate rapidly, or descend a hill.
Engine
Brake
Motor/
generator
Battery
peng
pmg
pbr
preq
wheels
All of these powers are functions of time, which we discretize in one second intervals, with
t = 1, 2, . . . , T. The required wheel power preq(1), . . . , preq(T) is given. (The speed of
the vehicle on the track is speciﬁed, so together with known road slope information, and
known aerodynamic and other losses, the power required at the wheels can be calculated.)
Power is conserved, which means we have
preq(t) = peng(t) + pmg(t) −pbr(t),
t = 1, . . . , T.
The brake can only dissipate power, so we have pbr(t) ≥0 for each t. The engine can only
provide power, and only up to a given limit P max
eng , i.e., we have
0 ≤peng(t) ≤P max
eng ,
t = 1, . . . , T.
The motor/generator power is also limited: pmg must satisfy
P min
mg ≤pmg(t) ≤P max
mg ,
t = 1, . . . , T.
Here P max
mg
> 0 is the maximum motor power, and −P min
mg > 0 is the maximum generator
power.
The battery charge or energy at time t is denoted E(t), t = 1, . . . , T + 1. The battery
energy satisﬁes
E(t + 1) = E(t) −pmg(t) −η|pmg(t)|,
t = 1, . . . , T,


## Page 27

Exercises
213
where η > 0 is a known parameter. (The term −pmg(t) represents the energy removed
or added the battery by the motor/generator, ignoring any losses. The term −η|pmg(t)|
represents energy lost through ineﬃciencies in the battery or motor/generator.)
The battery charge must be between 0 (empty) and its limit Emax
batt (full), at all times. (If
E(t) = 0, the battery is fully discharged, and no more energy can be extracted from it;
when E(t) = Emax
batt, the battery is full and cannot be charged.) To make the comparison
with non-hybrid vehicles fair, we ﬁx the initial battery charge to equal the ﬁnal battery
charge, so the net energy change is zero over the track: E(1) = E(T + 1). We do not
specify the value of the initial (and ﬁnal) energy.
The objective in the problem (to be minimized) is the total fuel consumed by the engine,
which is
Ftotal =
T
X
t=1
F(peng(t)),
where F : R →R is the fuel use characteristic of the engine.
We assume that F is
positive, increasing, and convex.
Formulate this problem as a convex optimization problem, with variables peng(t), pmg(t),
and pbr(t) for t = 1, . . . , T, and E(t) for t = 1, . . . , T + 1. Explain why your formulation
is equivalent to the problem described above.


## Page 28



## Page 29

Chapter 5
Duality
5.1
The Lagrange dual function
5.1.1
The Lagrangian
We consider an optimization problem in the standard form (4.1):
minimize
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m
hi(x) = 0,
i = 1, . . . , p,
(5.1)
with variable x ∈Rn. We assume its domain D = Tm
i=0 dom fi ∩Tp
i=1 dom hi
is nonempty, and denote the optimal value of (5.1) by p⋆. We do not assume the
problem (5.1) is convex.
The basic idea in Lagrangian duality is to take the constraints in (5.1) into
account by augmenting the objective function with a weighted sum of the constraint
functions. We deﬁne the Lagrangian L : Rn × Rm × Rp →R associated with the
problem (5.1) as
L(x, λ, ν) = f0(x) +
m
X
i=1
λifi(x) +
p
X
i=1
νihi(x),
with dom L = D × Rm × Rp. We refer to λi as the Lagrange multiplier associated
with the ith inequality constraint fi(x) ≤0; similarly we refer to νi as the Lagrange
multiplier associated with the ith equality constraint hi(x) = 0. The vectors λ and
ν are called the dual variables or Lagrange multiplier vectors associated with the
problem (5.1).


## Page 30

216
5
Duality
5.1.2
The Lagrange dual function
We deﬁne the Lagrange dual function (or just dual function) g : Rm × Rp →R as
the minimum value of the Lagrangian over x: for λ ∈Rm, ν ∈Rp,
g(λ, ν) = inf
x∈D L(x, λ, ν) = inf
x∈D
 
f0(x) +
m
X
i=1
λifi(x) +
p
X
i=1
νihi(x)
!
.
When the Lagrangian is unbounded below in x, the dual function takes on the
value −∞. Since the dual function is the pointwise inﬁmum of a family of aﬃne
functions of (λ, ν), it is concave, even when the problem (5.1) is not convex.
5.1.3
Lower bounds on optimal value
The dual function yields lower bounds on the optimal value p⋆of the problem (5.1):
For any λ ⪰0 and any ν we have
g(λ, ν) ≤p⋆.
(5.2)
This important property is easily veriﬁed. Suppose ˜x is a feasible point for the
problem (5.1), i.e., fi(˜x) ≤0 and hi(˜x) = 0, and λ ⪰0. Then we have
m
X
i=1
λifi(˜x) +
p
X
i=1
νihi(˜x) ≤0,
since each term in the ﬁrst sum is nonpositive, and each term in the second sum is
zero, and therefore
L(˜x, λ, ν) = f0(˜x) +
m
X
i=1
λifi(˜x) +
p
X
i=1
νihi(˜x) ≤f0(˜x).
Hence
g(λ, ν) = inf
x∈D L(x, λ, ν) ≤L(˜x, λ, ν) ≤f0(˜x).
Since g(λ, ν) ≤f0(˜x) holds for every feasible point ˜x, the inequality (5.2) follows.
The lower bound (5.2) is illustrated in ﬁgure 5.1, for a simple problem with x ∈R
and one inequality constraint.
The inequality (5.2) holds, but is vacuous, when g(λ, ν) = −∞.
The dual
function gives a nontrivial lower bound on p⋆only when λ ⪰0 and (λ, ν) ∈dom g,
i.e., g(λ, ν) > −∞. We refer to a pair (λ, ν) with λ ⪰0 and (λ, ν) ∈dom g as dual
feasible, for reasons that will become clear later.
5.1.4
Linear approximation interpretation
The Lagrangian and lower bound property can be given a simple interpretation,
based on a linear approximation of the indicator functions of the sets {0} and −R+.


## Page 31

5.1
The Lagrange dual function
217
x
−1
−0.5
0
0.5
1
−2
−1
0
1
2
3
4
5
Figure 5.1 Lower bound from a dual feasible point. The solid curve shows the
objective function f0, and the dashed curve shows the constraint function f1.
The feasible set is the interval [−0.46, 0.46], which is indicated by the two
dotted vertical lines. The optimal point and value are x⋆= −0.46, p⋆= 1.54
(shown as a circle). The dotted curves show L(x, λ) for λ = 0.1, 0.2, . . . , 1.0.
Each of these has a minimum value smaller than p⋆, since on the feasible set
(and for λ ≥0) we have L(x, λ) ≤f0(x).
λ
g(λ)
0
0.2
0.4
0.6
0.8
1
1
1.1
1.2
1.3
1.4
1.5
1.6
Figure 5.2 The dual function g for the problem in ﬁgure 5.1. Neither f0 nor
f1 is convex, but the dual function is concave. The horizontal dashed line
shows p⋆, the optimal value of the problem.


## Page 32

218
5
Duality
We ﬁrst rewrite the original problem (5.1) as an unconstrained problem,
minimize
f0(x) + Pm
i=1 I−(fi(x)) + Pp
i=1 I0(hi(x)),
(5.3)
where I−: R →R is the indicator function for the nonpositive reals,
I−(u) =

0
u ≤0
∞
u > 0,
and similarly, I0 is the indicator function of {0}. In the formulation (5.3), the func-
tion I−(u) can be interpreted as expressing our irritation or displeasure associated
with a constraint function value u = fi(x): It is zero if fi(x) ≤0, and inﬁnite if
fi(x) > 0. In a similar way, I0(u) gives our displeasure for an equality constraint
value u = hi(x). We can think of I−as a “brick wall” or “inﬁnitely hard” displea-
sure function; our displeasure rises from zero to inﬁnite as fi(x) transitions from
nonpositive to positive.
Now suppose in the formulation (5.3) we replace the function I−(u) with the
linear function λiu, where λi ≥0, and the function I0(u) with νiu. The objective
becomes the Lagrangian function L(x, λ, ν), and the dual function value g(λ, ν) is
the optimal value of the problem
minimize
L(x, λ, ν) = f0(x) + Pm
i=1 λifi(x) + Pp
i=1 νihi(x).
(5.4)
In this formulation, we use a linear or “soft” displeasure function in place of I−
and I0. For an inequality constraint, our displeasure is zero when fi(x) = 0, and is
positive when fi(x) > 0 (assuming λi > 0); our displeasure grows as the constraint
becomes “more violated”. Unlike the original formulation, in which any nonpositive
value of fi(x) is acceptable, in the soft formulation we actually derive pleasure from
constraints that have margin, i.e., from fi(x) < 0.
Clearly the approximation of the indicator function I−(u) with a linear function
λiu is rather poor. But the linear function is at least an underestimator of the
indicator function. Since λiu ≤I−(u) and νiu ≤I0(u) for all u, we see immediately
that the dual function yields a lower bound on the optimal value of the original
problem.
The idea of replacing the “hard” constraints with “soft” versions will come up
again when we consider interior-point methods (§11.2.1).
5.1.5
Examples
In this section we give some examples for which we can derive an analytical ex-
pression for the Lagrange dual function.
Least-squares solution of linear equations
We consider the problem
minimize
xT x
subject to
Ax = b,
(5.5)
where A ∈Rp×n. This problem has no inequality constraints and p (linear) equality
constraints. The Lagrangian is L(x, ν) = xT x + νT (Ax −b), with domain Rn ×


## Page 33

5.1
The Lagrange dual function
219
Rp. The dual function is given by g(ν) = infx L(x, ν). Since L(x, ν) is a convex
quadratic function of x, we can ﬁnd the minimizing x from the optimality condition
∇xL(x, ν) = 2x + AT ν = 0,
which yields x = −(1/2)AT ν. Therefore the dual function is
g(ν) = L(−(1/2)AT ν, ν) = −(1/4)νT AAT ν −bT ν,
which is a concave quadratic function, with domain Rp. The lower bound prop-
erty (5.2) states that for any ν ∈Rp, we have
−(1/4)νT AAT ν −bT ν ≤inf{xT x | Ax = b}.
Standard form LP
Consider an LP in standard form,
minimize
cT x
subject to
Ax = b
x ⪰0,
(5.6)
which has inequality constraint functions fi(x) = −xi, i = 1, . . . , n.
To form
the Lagrangian we introduce multipliers λi for the n inequality constraints and
multipliers νi for the equality constraints, and obtain
L(x, λ, ν) = cT x −
n
X
i=1
λixi + νT (Ax −b) = −bT ν + (c + AT ν −λ)T x.
The dual function is
g(λ, ν) = inf
x L(x, λ, ν) = −bT ν + inf
x (c + AT ν −λ)T x,
which is easily determined analytically, since a linear function is bounded below
only when it is identically zero. Thus, g(λ, ν) = −∞except when c+AT ν −λ = 0,
in which case it is −bT ν:
g(λ, ν) =

−bT ν
AT ν −λ + c = 0
−∞
otherwise.
Note that the dual function g is ﬁnite only on a proper aﬃne subset of Rm × Rp.
We will see that this is a common occurrence.
The lower bound property (5.2) is nontrivial only when λ and ν satisfy λ ⪰0
and AT ν −λ + c = 0. When this occurs, −bT ν is a lower bound on the optimal
value of the LP (5.6).
Two-way partitioning problem
We consider the (nonconvex) problem
minimize
xT Wx
subject to
x2
i = 1,
i = 1, . . . , n,
(5.7)


## Page 34

220
5
Duality
where W ∈Sn. The constraints restrict the values of xi to 1 or −1, so the problem
is equivalent to ﬁnding the vector with components ±1 that minimizes xT Wx. The
feasible set here is ﬁnite (it contains 2n points) so this problem can in principle
be solved by simply checking the objective value of each feasible point. Since the
number of feasible points grows exponentially, however, this is possible only for
small problems (say, with n ≤30). In general (and for n larger than, say, 50) the
problem (5.7) is very diﬃcult to solve.
We can interpret the problem (5.7) as a two-way partitioning problem on a set
of n elements, say, {1, . . . , n}: A feasible x corresponds to the partition
{1, . . . , n} = {i | xi = −1} ∪{i | xi = 1}.
The matrix coeﬃcient Wij can be interpreted as the cost of having the elements i
and j in the same partition, and −Wij is the cost of having i and j in diﬀerent
partitions. The objective in (5.7) is the total cost, over all pairs of elements, and
the problem (5.7) is to ﬁnd the partition with least total cost.
We now derive the dual function for this problem. The Lagrangian is
L(x, ν)
=
xT Wx +
n
X
i=1
νi(x2
i −1)
=
xT (W + diag(ν))x −1T ν.
We obtain the Lagrange dual function by minimizing over x:
g(ν)
=
inf
x xT (W + diag(ν))x −1T ν
=

−1T ν
W + diag(ν) ⪰0
−∞
otherwise,
where we use the fact that the inﬁmum of a quadratic form is either zero (if the
form is positive semideﬁnite) or −∞(if the form is not positive semideﬁnite).
This dual function provides lower bounds on the optimal value of the diﬃcult
problem (5.7). For example, we can take the speciﬁc value of the dual variable
ν = −λmin(W)1,
which is dual feasible, since
W + diag(ν) = W −λmin(W)I ⪰0.
This yields the bound on the optimal value p⋆
p⋆≥−1T ν = nλmin(W).
(5.8)
Remark 5.1 This lower bound on p⋆can also be obtained without using the Lagrange
dual function. First, we replace the constraints x2
1 = 1, . . . , x2
n = 1 with Pn
i=1 x2
i = n,
to obtain the modiﬁed problem
minimize
xT Wx
subject to
Pn
i=1 x2
i = n.
(5.9)


## Page 35

5.1
The Lagrange dual function
221
The constraints of the original problem (5.7) imply the constraint here, so the optimal
value of the problem (5.9) is a lower bound on p⋆, the optimal value of (5.7). But the
modiﬁed problem (5.9) is easily solved as an eigenvalue problem, with optimal value
nλmin(W).
5.1.6
The Lagrange dual function and conjugate functions
Recall from §3.3 that the conjugate f ∗of a function f : Rn →R is given by
f ∗(y) =
sup
x∈dom f
 yT x −f(x)

.
The conjugate function and Lagrange dual function are closely related. To see one
simple connection, consider the problem
minimize
f(x)
subject to
x = 0
(which is not very interesting, and solvable by inspection).
This problem has
Lagrangian L(x, ν) = f(x) + νT x, and dual function
g(ν) = inf
x
 f(x) + νT x

= −sup
x
 (−ν)T x −f(x)

= −f ∗(−ν).
More generally (and more usefully), consider an optimization problem with
linear inequality and equality constraints,
minimize
f0(x)
subject to
Ax ⪯b
Cx = d.
(5.10)
Using the conjugate of f0 we can write the dual function for the problem (5.10) as
g(λ, ν)
=
inf
x
 f0(x) + λT (Ax −b) + νT (Cx −d)

=
−bT λ −dT ν + inf
x
 f0(x) + (AT λ + CT ν)T x

=
−bT λ −dT ν −f ∗
0 (−AT λ −CT ν).
(5.11)
The domain of g follows from the domain of f ∗
0 :
dom g = {(λ, ν) | −AT λ −CT ν ∈dom f ∗
0 }.
Let us illustrate this with a few examples.
Equality constrained norm minimization
Consider the problem
minimize
∥x∥
subject to
Ax = b,
(5.12)


## Page 36

222
5
Duality
where ∥· ∥is any norm. Recall (from example 3.26 on page 93) that the conjugate
of f0 = ∥· ∥is given by
f ∗
0 (y) =

0
∥y∥∗≤1
∞
otherwise,
the indicator function of the dual norm unit ball.
Using the result (5.11) above, the dual function for the problem (5.12) is given
by
g(ν) = −bT ν −f ∗
0 (−AT ν) =

−bT ν
∥AT ν∥∗≤1
−∞
otherwise.
Entropy maximization
Consider the entropy maximization problem
minimize
f0(x) = Pn
i=1 xi log xi
subject to
Ax ⪯b
1T x = 1
(5.13)
where dom f0 = Rn
++. The conjugate of the negative entropy function u log u,
with scalar variable u, is ev−1 (see example 3.21 on page 91). Since f0 is a sum of
negative entropy functions of diﬀerent variables, we conclude that its conjugate is
f ∗
0 (y) =
n
X
i=1
eyi−1,
with dom f ∗
0 = Rn. Using the result (5.11) above, the dual function of (5.13) is
given by
g(λ, ν) = −bT λ −ν −
n
X
i=1
e−aT
i λ−ν−1 = −bT λ −ν −e−ν−1
n
X
i=1
e−aT
i λ
where ai is the ith column of A.
Minimum volume covering ellipsoid
Consider the problem with variable X ∈Sn,
minimize
f0(X) = log det X−1
subject to
aT
i Xai ≤1,
i = 1, . . . , m,
(5.14)
where dom f0 = Sn
++. The problem (5.14) has a simple geometric interpretation.
With each X ∈Sn
++ we associate the ellipsoid, centered at the origin,
EX = {z | zT Xz ≤1}.
The volume of this ellipsoid is proportional to
 det X−11/2, so the objective
of (5.14) is, except for a constant and a factor of two, the logarithm of the volume


## Page 37

5.2
The Lagrange dual problem
223
of EX. The constraints of the problem (5.14) are that ai ∈EX. Thus the prob-
lem (5.14) is to determine the minimum volume ellipsoid, centered at the origin,
that includes the points a1, . . . , am.
The inequality constraints in problem (5.14) are aﬃne; they can be expressed
as
tr
 (aiaT
i )X

≤1.
In example 3.23 (page 92) we found that the conjugate of f0 is
f ∗
0 (Y ) = log det(−Y )−1 −n,
with dom f ∗
0 = −Sn
++. Applying the result (5.11) above, the dual function for the
problem (5.14) is given by
g(λ) =

log det
 Pm
i=1 λiaiaT
i

−1T λ + n
Pm
i=1 λiaiaT
i ≻0
−∞
otherwise.
(5.15)
Thus, for any λ ⪰0 with Pm
i=1 λiaiaT
i ≻0, the number
log det
 m
X
i=1
λiaiaT
i
!
−1T λ + n
is a lower bound on the optimal value of the problem (5.14).
5.2
The Lagrange dual problem
For each pair (λ, ν) with λ ⪰0, the Lagrange dual function gives us a lower bound
on the optimal value p⋆of the optimization problem (5.1). Thus we have a lower
bound that depends on some parameters λ, ν. A natural question is: What is the
best lower bound that can be obtained from the Lagrange dual function?
This leads to the optimization problem
maximize
g(λ, ν)
subject to
λ ⪰0.
(5.16)
This problem is called the Lagrange dual problem associated with the problem (5.1).
In this context the original problem (5.1) is sometimes called the primal problem.
The term dual feasible, to describe a pair (λ, ν) with λ ⪰0 and g(λ, ν) > −∞,
now makes sense. It means, as the name implies, that (λ, ν) is feasible for the dual
problem (5.16). We refer to (λ⋆, ν⋆) as dual optimal or optimal Lagrange multipliers
if they are optimal for the problem (5.16).
The Lagrange dual problem (5.16) is a convex optimization problem, since the
objective to be maximized is concave and the constraint is convex. This is the case
whether or not the primal problem (5.1) is convex.


## Page 38

224
5
Duality
5.2.1
Making dual constraints explicit
The examples above show that it is not uncommon for the domain of the dual
function,
dom g = {(λ, ν) | g(λ, ν) > −∞},
to have dimension smaller than m + p. In many cases we can identify the aﬃne
hull of dom g, and describe it as a set of linear equality constraints.
Roughly
speaking, this means we can identify the equality constraints that are ‘hidden’ or
‘implicit’ in the objective g of the dual problem (5.16). In this case we can form
an equivalent problem, in which these equality constraints are given explicitly as
constraints. The following examples demonstrate this idea.
Lagrange dual of standard form LP
On page 219 we found that the Lagrange dual function for the standard form LP
minimize
cT x
subject to
Ax = b
x ⪰0
(5.17)
is given by
g(λ, ν) =

−bT ν
AT ν −λ + c = 0
−∞
otherwise.
Strictly speaking, the Lagrange dual problem of the standard form LP is to maxi-
mize this dual function g subject to λ ⪰0, i.e.,
maximize
g(λ, ν) =

−bT ν
AT ν −λ + c = 0
−∞
otherwise
subject to
λ ⪰0.
(5.18)
Here g is ﬁnite only when AT ν −λ + c = 0. We can form an equivalent problem
by making these equality constraints explicit:
maximize
−bT ν
subject to
AT ν −λ + c = 0
λ ⪰0.
(5.19)
This problem, in turn, can be expressed as
maximize
−bT ν
subject to
AT ν + c ⪰0,
(5.20)
which is an LP in inequality form.
Note the subtle distinctions between these three problems. The Lagrange dual
of the standard form LP (5.17) is the problem (5.18), which is equivalent to (but
not the same as) the problems (5.19) and (5.20). With some abuse of terminology,
we refer to the problem (5.19) or the problem (5.20) as the Lagrange dual of the
standard form LP (5.17).


## Page 39

5.2
The Lagrange dual problem
225
Lagrange dual of inequality form LP
In a similar way we can ﬁnd the Lagrange dual problem of a linear program in
inequality form
minimize
cT x
subject to
Ax ⪯b.
(5.21)
The Lagrangian is
L(x, λ) = cT x + λT (Ax −b) = −bT λ + (AT λ + c)T x,
so the dual function is
g(λ) = inf
x L(x, λ) = −bT λ + inf
x (AT λ + c)T x.
The inﬁmum of a linear function is −∞, except in the special case when it is
identically zero, so the dual function is
g(λ) =

−bT λ
AT λ + c = 0
−∞
otherwise.
The dual variable λ is dual feasible if λ ⪰0 and AT λ + c = 0.
The Lagrange dual of the LP (5.21) is to maximize g over all λ ⪰0. Again
we can reformulate this by explicitly including the dual feasibility conditions as
constraints, as in
maximize
−bT λ
subject to
AT λ + c = 0
λ ⪰0,
(5.22)
which is an LP in standard form.
Note the interesting symmetry between the standard and inequality form LPs
and their duals: The dual of a standard form LP is an LP with only inequality
constraints, and vice versa. One can also verify that the Lagrange dual of (5.22) is
(equivalent to) the primal problem (5.21).
5.2.2
Weak duality
The optimal value of the Lagrange dual problem, which we denote d⋆, is, by def-
inition, the best lower bound on p⋆that can be obtained from the Lagrange dual
function. In particular, we have the simple but important inequality
d⋆≤p⋆,
(5.23)
which holds even if the original problem is not convex. This property is called weak
duality.
The weak duality inequality (5.23) holds when d⋆and p⋆are inﬁnite.
For
example, if the primal problem is unbounded below, so that p⋆= −∞, we must
have d⋆= −∞, i.e., the Lagrange dual problem is infeasible. Conversely, if the
dual problem is unbounded above, so that d⋆= ∞, we must have p⋆= ∞, i.e., the
primal problem is infeasible.


## Page 40

226
5
Duality
We refer to the diﬀerence p⋆−d⋆as the optimal duality gap of the original
problem, since it gives the gap between the optimal value of the primal problem
and the best (i.e., greatest) lower bound on it that can be obtained from the
Lagrange dual function. The optimal duality gap is always nonnegative.
The bound (5.23) can sometimes be used to ﬁnd a lower bound on the optimal
value of a problem that is diﬃcult to solve, since the dual problem is always convex,
and in many cases can be solved eﬃciently, to ﬁnd d⋆. As an example, consider
the two-way partitioning problem (5.7) described on page 219. The dual problem
is an SDP,
maximize
−1T ν
subject to
W + diag(ν) ⪰0,
with variable ν ∈Rn. This problem can be solved eﬃciently, even for relatively
large values of n, such as n = 1000. Its optimal value is a lower bound on the
optimal value of the two-way partitioning problem, and is always at least as good
as the lower bound (5.8) based on λmin(W).
5.2.3
Strong duality and Slater’s constraint qualiﬁcation
If the equality
d⋆= p⋆
(5.24)
holds, i.e., the optimal duality gap is zero, then we say that strong duality holds.
This means that the best bound that can be obtained from the Lagrange dual
function is tight.
Strong duality does not, in general, hold. But if the primal problem (5.1) is
convex, i.e., of the form
minimize
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m,
Ax = b,
(5.25)
with f0, . . . , fm convex, we usually (but not always) have strong duality. There are
many results that establish conditions on the problem, beyond convexity, under
which strong duality holds. These conditions are called constraint qualiﬁcations.
One simple constraint qualiﬁcation is Slater’s condition: There exists an x ∈
relint D such that
fi(x) < 0,
i = 1, . . . , m,
Ax = b.
(5.26)
Such a point is sometimes called strictly feasible, since the inequality constraints
hold with strict inequalities. Slater’s theorem states that strong duality holds, if
Slater’s condition holds (and the problem is convex).
Slater’s condition can be reﬁned when some of the inequality constraint func-
tions fi are aﬃne. If the ﬁrst k constraint functions f1, . . . , fk are aﬃne, then
strong duality holds provided the following weaker condition holds: There exists
an x ∈relint D with
fi(x) ≤0,
i = 1, . . . , k,
fi(x) < 0,
i = k + 1, . . . , m,
Ax = b.
(5.27)
