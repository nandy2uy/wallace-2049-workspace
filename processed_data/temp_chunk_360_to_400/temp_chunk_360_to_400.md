# temp_chunk_360_to_400



## Page 1

Exercises
347
Function ﬁtting and interpolation
6.9 Minimax rational function ﬁtting. Show that the following problem is quasiconvex:
minimize
max
i=1,...,k

p(ti)
q(ti) −yi

where
p(t) = a0 + a1t + a2t2 + · · · + amtm,
q(t) = 1 + b1t + · · · + bntn,
and the domain of the objective function is deﬁned as
D = {(a, b) ∈Rm+1 × Rn | q(t) > 0, α ≤t ≤β}.
In this problem we ﬁt a rational function p(t)/q(t) to given data, while constraining the
denominator polynomial to be positive on the interval [α, β]. The optimization variables
are the numerator and denominator coeﬃcients ai, bi. The interpolation points ti ∈[α, β],
and desired function values yi, i = 1, . . . , k, are given.
6.10 Fitting data with a concave nonnegative nondecreasing quadratic function. We are given
the data
x1, . . . , xN ∈Rn,
y1, . . . , yN ∈R,
and wish to ﬁt a quadratic function of the form
f(x) = (1/2)xT Px + qT x + r,
where P ∈Sn, q ∈Rn, and r ∈R are the parameters in the model (and, therefore, the
variables in the ﬁtting problem).
Our model will be used only on the box B = {x ∈Rn | l ⪯x ⪯u}. You can assume that
l ≺u, and that the given data points xi are in this box.
We will use the simple sum of squared errors objective,
N
X
i=1
(f(xi) −yi)2,
as the criterion for the ﬁt. We also impose several constraints on the function f. First,
it must be concave. Second, it must be nonnegative on B, i.e., f(z) ≥0 for all z ∈B.
Third, f must be nondecreasing on B, i.e., whenever z, ˜z ∈B satisfy z ⪯˜z, we have
f(z) ≤f(˜z).
Show how to formulate this ﬁtting problem as a convex problem. Simplify your formula-
tion as much as you can.
6.11 Least-squares direction interpolation. Suppose F1, . . . , Fn : Rk →Rp, and we form the
linear combination F : Rk →Rp,
F(u) = x1F1(u) + · · · + xnFn(u),
where x is the variable in the interpolation problem.
In this problem we require that̸
(F(vj), qj) = 0, j = 1, . . . , m, where qj are given vectors
in Rp, which we assume satisfy ∥qj∥2 = 1. In other words, we require the direction of
F to take on speciﬁed values at the points vj. To ensure that F(vj) is not zero (which
makes the angle undeﬁned), we impose the minimum length constraints ∥F(vj)∥2 ≥ǫ,
j = 1, . . . , m, where ǫ > 0 is given.
Show how to ﬁnd x that minimizes ∥x∥2, and satisﬁes the direction (and minimum length)
conditions above, using convex optimization.
6.12 Interpolation with monotone functions. A function f : Rk →R is monotone nondecreas-
ing (with respect to Rk
+) if f(u) ≥f(v) whenever u ⪰v.


## Page 2

348
6
Approximation and ﬁtting
(a) Show that there exists a monotone nondecreasing function f : Rk →R, that satisﬁes
f(ui) = yi for i = 1, . . . , m, if and only if
yi ≥yj whenever ui ⪰uj,
i, j = 1, . . . , m.
(b) Show that there exists a convex monotone nondecreasing function f : Rk →R, with
dom f = Rk, that satisﬁes f(ui) = yi for i = 1, . . . , m, if and only if there exist
gi ∈Rk, i = 1, . . . , m, such that
gi ⪰0,
i = 1, . . . , m,
yj ≥yi + gT
i (uj −ui),
i, j = 1, . . . , m.
6.13 Interpolation with quasiconvex functions. Show that there exists a quasiconvex function
f : Rk →R, that satisﬁes f(ui) = yi for i = 1, . . . , m, if and only if there exist gi ∈Rk,
i = 1, . . . , m, such that
gT
i (uj −ui) ≤−1 whenever yj < yi,
i, j = 1, . . . , m.
6.14 [Nes00] Interpolation with positive-real functions. Suppose z1, . . . , zn ∈C are n distinct
points with |zi| > 1. We deﬁne Knp as the set of vectors y ∈Cn for which there exists a
function f : C →C that satisﬁes the following conditions.
• f is positive-real, which means it is analytic outside the unit circle (i.e., for |z| > 1),
and its real part is nonnegative outside the unit circle (ℜf(z) ≥0 for |z| > 1).
• f satisﬁes the interpolation conditions
f(z1) = y1,
f(z2) = y2,
. . . ,
f(zn) = yn.
If we denote the set of positive-real functions as F, then we can express Knp as
Knp = {y ∈Cn | ∃f ∈F, yk = f(zk), k = 1, . . . , n}.
(a) It can be shown that f is positive-real if and only if there exists a nondecreasing
function ρ such that for all z with |z| > 1,
f(z) = iℑf(∞) +
Z 2π
0
eiθ + z−1
eiθ −z−1 dρ(θ),
where i = √−1 (see [KN77, page 389]). Use this representation to show that Knp
is a closed convex cone.
(b) We will use the inner product ℜ(xHy) between vectors x, y ∈Cn, where xH denotes
the complex conjugate transpose of x. Show that the dual cone of Knp is given by
K∗
np =
(
x ∈Cn
 ℑ(1T x) = 0, ℜ
 
n
X
l=1
xl
e−iθ + ¯z−1
l
e−iθ −¯z−1
l
!
≥0 ∀θ ∈[0, 2π]
)
.
(c) Show that
K∗
np =
(
x ∈Cn
 ∃Q ∈Hn
+, xl =
n
X
k=1
Qkl
1 −z−1
k ¯z−1
l
, l = 1, . . . , n
)
where Hn
+ denotes the set of positive semideﬁnite Hermitian matrices of size n × n.
Use the following result (known as Riesz-Fej´er theorem; see [KN77, page 60]). A
function of the form
n
X
k=0
(yke−ikθ + ¯ykeikθ)
is nonnegative for all θ if and only if there exist a0, . . . , an ∈C such that
n
X
k=0
(yke−ikθ + ¯ykeikθ) =

n
X
k=0
akeikθ

2
.


## Page 3

Exercises
349
(d) Show that Knp = {y ∈Cn | P(y) ⪰0} where P(y) ∈Hn is deﬁned as
P(y)kl =
yk + yl
1 −z−1
k ¯z−1
l
,
l, k = 1, . . . , n.
The matrix P(y) is called the Nevanlinna-Pick matrix associated with the points
zk, yk.
Hint. As we noted in part (a), Knp is a closed convex cone, so Knp = K∗∗
np.
(e) As an application, pose the following problem as a convex optimization problem:
minimize
Pn
k=1 |f(zk) −wk|2
subject to
f ∈F.
The problem data are n points zk with |zk| > 1 and n complex numbers w1, . . . ,
wn. We optimize over all positive-real functions f.


## Page 4



## Page 5

Chapter 7
Statistical estimation
7.1
Parametric distribution estimation
7.1.1
Maximum likelihood estimation
We consider a family of probability distributions on Rm, indexed by a vector
x ∈Rn, with densities px(·). When considered as a function of x, for ﬁxed y ∈Rm,
the function px(y) is called the likelihood function. It is more convenient to work
with its logarithm, which is called the log-likelihood function, and denoted l:
l(x) = log px(y).
There are often constraints on the values of the parameter x, which can repre-
sent prior knowledge about x, or the domain of the likelihood function. These
constraints can be explicitly given, or incorporated into the likelihood function by
assigning px(y) = 0 (for all y) whenever x does not satisfy the prior information
constraints. (Thus, the log-likelihood function can be assigned the value −∞for
parameters x that violate the prior information constraints.)
Now consider the problem of estimating the value of the parameter x, based
on observing one sample y from the distribution. A widely used method, called
maximum likelihood (ML) estimation, is to estimate x as
ˆxml = argmaxxpx(y) = argmaxxl(x),
i.e., to choose as our estimate a value of the parameter that maximizes the like-
lihood (or log-likelihood) function for the observed value of y. If we have prior
information about x, such as x ∈C ⊆Rn, we can add the constraint x ∈C
explicitly, or impose it implicitly, by redeﬁning px(y) to be zero for x̸ ∈C.
The problem of ﬁnding a maximum likelihood estimate of the parameter vector
x can be expressed as
maximize
l(x) = log px(y)
subject to
x ∈C,
(7.1)
where x ∈C gives the prior information or other constraints on the parameter
vector x. In this optimization problem, the vector x ∈Rn (which is the parameter


## Page 6

352
7
Statistical estimation
in the probability density) is the variable, and the vector y ∈Rm (which is the
observed sample) is a problem parameter.
The maximum likelihood estimation problem (7.1) is a convex optimization
problem if the log-likelihood function l is concave for each value of y, and the set
C can be described by a set of linear equality and convex inequality constraints, a
situation which occurs in many estimation problems. For these problems we can
compute an ML estimate using convex optimization.
Linear measurements with IID noise
We consider a linear measurement model,
yi = aT
i x + vi,
i = 1, . . . , m,
where x ∈Rn is a vector of parameters to be estimated, yi ∈R are the measured
or observed quantities, and vi are the measurement errors or noise. We assume
that vi are independent, identically distributed (IID), with density p on R. The
likelihood function is then
px(y) =
m
Y
i=1
p(yi −aT
i x),
so the log-likelihood function is
l(x) = log px(y) =
m
X
i=1
log p(yi −aT
i x).
The ML estimate is any optimal point for the problem
maximize
Pm
i=1 log p(yi −aT
i x),
(7.2)
with variable x. If the density p is log-concave, this problem is convex, and has the
form of a penalty approximation problem ((6.2), page 294), with penalty function
−log p.
Example 7.1 ML estimation for some common noise densities.
• Gaussian noise. When vi are Gaussian with zero mean and variance σ2, the
density is p(z) = (2πσ2)−1/2e−z2/2σ2, and the log-likelihood function is
l(x) = −(m/2) log(2πσ2) −
1
2σ2 ∥Ax −y∥2
2,
where A is the matrix with rows aT
1 , . . . , aT
m. Therefore the ML estimate of
x is xml = argminx ∥Ax −y∥2
2, the solution of a least-squares approximation
problem.
• Laplacian noise. When vi are Laplacian, i.e., have density p(z) = (1/2a)e−|z|/a
(where a > 0), the ML estimate is ˆx = argminx ∥Ax −y∥1, the solution of the
ℓ1-norm approximation problem.
• Uniform noise. When vi are uniformly distributed on [−a, a], we have p(z) =
1/(2a) on [−a, a], and an ML estimate is any x satisfying ∥Ax −y∥∞≤a.


## Page 7

7.1
Parametric distribution estimation
353
ML interpretation of penalty function approximation
Conversely, we can interpret any penalty function approximation problem
minimize
Pm
i=1 φ(bi −aT
i x)
as a maximum likelihood estimation problem, with noise density
p(z) =
e−φ(z)
R
e−φ(u) du,
and measurements b.
This observation gives a statistical interpretation of the
penalty function approximation problem. Suppose, for example, that the penalty
function φ grows very rapidly for large values, which means that we attach a very
large cost or penalty to large residuals. The corresponding noise density function
p will have very small tails, and the ML estimator will avoid (if possible) estimates
with any large residuals because these correspond to very unlikely events.
We can also understand the robustness of ℓ1-norm approximation to large errors
in terms of maximum likelihood estimation. We interpret ℓ1-norm approximation
as maximum likelihood estimation with a noise density that is Laplacian; ℓ2-norm
approximation is maximum likelihood estimation with a Gaussian noise density.
The Laplacian density has larger tails than the Gaussian, i.e., the probability of a
very large vi is far larger with a Laplacian than a Gaussian density. As a result,
the associated maximum likelihood method expects to see greater numbers of large
residuals.
Counting problems with Poisson distribution
In a wide variety of problems the random variable y is nonnegative integer valued,
with a Poisson distribution with mean µ > 0:
prob(y = k) = e−µµk
k!
.
Often y represents the count or number of events (such as photon arrivals, traﬃc
accidents, etc.) of a Poisson process over some period of time.
In a simple statistical model, the mean µ is modeled as an aﬃne function of a
vector u ∈Rn:
µ = aT u + b.
Here u is called the vector of explanatory variables, and the vector a ∈Rn and
number b ∈R are called the model parameters. For example, if y is the number
of traﬃc accidents in some region over some period, u1 might be the total traﬃc
ﬂow through the region during the period, u2 the rainfall in the region during the
period, and so on.
We are given a number of observations which consist of pairs (ui, yi), i =
1, . . . , m, where yi is the observed value of y for which the value of the explanatory
variable is ui ∈Rn. Our job is to ﬁnd a maximum likelihood estimate of the model
parameters a ∈Rn and b ∈R from these data.


## Page 8

354
7
Statistical estimation
The likelihood function has the form
m
Y
i=1
(aT ui + b)yi exp(−(aT ui + b))
yi!
,
so the log-likelihood function is
l(a, b) =
m
X
i=1
(yi log(aT ui + b) −(aT ui + b) −log(yi!)).
We can ﬁnd an ML estimate of a and b by solving the convex optimization problem
maximize
Pm
i=1(yi log(aT ui + b) −(aT ui + b)),
where the variables are a and b.
Logistic regression
We consider a random variable y ∈{0, 1}, with
prob(y = 1) = p,
prob(y = 0) = 1 −p,
where p ∈[0, 1], and is assumed to depend on a vector of explanatory variables
u ∈Rn. For example, y = 1 might mean that an individual in a population acquires
a certain disease. The probability of acquiring the disease is p, which is modeled
as a function of some explanatory variables u, which might represent weight, age,
height, blood pressure, and other medically relevant variables.
The logistic model has the form
p =
exp(aT u + b)
1 + exp(aT u + b),
(7.3)
where a ∈Rn and b ∈R are the model parameters that determine how the
probability p varies as a function of the explanatory variable u.
Now suppose we are given some data consisting of a set of values of the explana-
tory variables u1, . . . , um ∈Rn along with the corresponding outcomes y1, . . . , ym ∈
{0, 1}. Our job is to ﬁnd a maximum likelihood estimate of the model parameters
a ∈Rn and b ∈R. Finding an ML estimate of a and b is sometimes called logistic
regression.
We can re-order the data so for u1, . . . , uq, the outcome is y = 1, and for
uq+1, . . . , um the outcome is y = 0. The likelihood function then has the form
q
Y
i=1
pi
m
Y
i=q+1
(1 −pi),
where pi is given by the logistic model with explanatory variable ui.
The log-
likelihood function has the form
l(a, b)
=
q
X
i=1
log pi +
m
X
i=q+1
log(1 −pi)


## Page 9

7.1
Parametric distribution estimation
355
u
prob(y = 1)
0
2
4
6
8
10
0
0.2
0.4
0.6
0.8
1
Figure 7.1 Logistic regression.
The circles show 50 points (ui, yi), where
ui ∈R is the explanatory variable, and yi ∈{0, 1} is the outcome. The
data suggest that for u < 5 or so, the outcome is more likely to be y = 0,
while for u > 5 or so, the outcome is more likely to be y = 1. The data
also suggest that for u < 2 or so, the outcome is very likely to be y = 0,
and for u > 8 or so, the outcome is very likely to be y = 1.
The solid
curve shows prob(y = 1) = exp(au + b)/(1 + exp(au + b)) for the maximum
likelihood parameters a, b. This maximum likelihood model is consistent
with our informal observations about the data set.
=
q
X
i=1
log
exp(aT ui + b)
1 + exp(aT ui + b) +
m
X
i=q+1
log
1
1 + exp(aT ui + b)
=
q
X
i=1
(aT ui + b) −
m
X
i=1
log(1 + exp(aT ui + b)).
Since l is a concave function of a and b, the logistic regression problem can be solved
as a convex optimization problem. Figure 7.1 shows an example with u ∈R.
Covariance estimation for Gaussian variables
Suppose y ∈Rn is a Gaussian random variable with zero mean and covariance
matrix R = E yyT , so its density is
pR(y) = (2π)−n/2 det(R)−1/2 exp(−yT R−1y/2),
where R ∈Sn
++. We want to estimate the covariance matrix R based on N in-
dependent samples y1, . . . , yN ∈Rn drawn from the distribution, and using prior
knowledge about R.
The log-likelihood function has the form
l(R)
=
log pR(y1, . . . , yN)


## Page 10

356
7
Statistical estimation
=
−(Nn/2) log(2π) −(N/2) log det R −(1/2)
N
X
k=1
yT
k R−1yk
=
−(Nn/2) log(2π) −(N/2) log det R −(N/2) tr(R−1Y ),
where
Y = 1
N
N
X
k=1
ykyT
k
is the sample covariance of y1, . . . , yN. This log-likelihood function is not a concave
function of R (although it is concave on a subset of its domain Sn
++; see exercise 7.4),
but a change of variable yields a concave log-likelihood function. Let S denote the
inverse of the covariance matrix, S = R−1 (which is called the information matrix).
Using S in place of R as a new parameter, the log-likelihood function has the form
l(S) = −(Nn/2) log(2π) + (N/2) log det S −(N/2) tr(SY ),
which is a concave function of S.
Therefore the ML estimate of S (hence, R) is found by solving the problem
maximize
log det S −tr(SY )
subject to
S ∈S
(7.4)
where S is our prior knowledge of S = R−1. (We also have the implicit constraint
that S ∈Sn
++.) Since the objective function is concave, this is a convex problem
if the set S can be described by a set of linear equality and convex inequality
constraints.
First we examine the case in which no prior assumptions are made on R (hence,
S), other than R ≻0. In this case the problem (7.4) can be solved analytically. The
gradient of the objective is S−1−Y , so the optimal S satisﬁes S−1 = Y if Y ∈Sn
++.
(If Y̸ ∈Sn
++, the log-likelihood function is unbounded above.) Therefore, when
we have no prior assumptions about R, the maximum likelihood estimate of the
covariance is, simply, the sample covariance: ˆRml = Y .
Now we consider some examples of constraints on R that can be expressed as
convex constraints on the information matrix S. We can handle lower and upper
(matrix) bounds on R, of the form
L ⪯R ⪯U,
where L and U are symmetric and positive deﬁnite, as
U −1 ⪯R−1 ⪯L−1.
A condition number constraint on R,
λmax(R) ≤κmaxλmin(R),
can be expressed as
λmax(S) ≤κmaxλmin(S).


## Page 11

7.1
Parametric distribution estimation
357
This is equivalent to the existence of u > 0 such that uI ⪯S ⪯κmaxuI. We can
therefore solve the ML problem, with the condition number constraint on R, by
solving the convex problem
maximize
log det S −tr(SY )
subject to
uI ⪯S ⪯κmaxuI
(7.5)
where the variables are S ∈Sn and u ∈R.
As another example, suppose we are given bounds on the variance of some linear
functions of the underlying random vector y,
E(cT
i y)2 ≤αi,
i = 1, . . . , K.
These prior assumptions can be expressed as
E(cT
i y)2 = cT
i Rci = cT
i S−1ci ≤αi,
i = 1, . . . , K.
Since cT
i S−1ci is a convex function of S (provided S ≻0, which holds here), these
bounds can be imposed in the ML problem.
7.1.2
Maximum a posteriori probability estimation
Maximum a posteriori probability (MAP) estimation can be considered a Bayesian
version of maximum likelihood estimation, with a prior probability density on the
underlying parameter x. We assume that x (the vector to be estimated) and y (the
observation) are random variables with a joint probability density p(x, y). This
is in contrast to the statistical estimation setup, where x is a parameter, not a
random variable.
The prior density of x is given by
px(x) =
Z
p(x, y) dy.
This density represents our prior information about what the values of the vector x
might be, before we observe the vector y. Similarly, the prior density of y is given
by
py(y) =
Z
p(x, y) dx.
This density represents the prior information about what the measurement or ob-
servation vector y will be.
The conditional density of y, given x, is given by
py|x(x, y) = p(x, y)
px(x) .
In the MAP estimation method, py|x plays the role of the parameter dependent
density px in the maximum likelihood estimation setup. The conditional density
of x, given y, is given by
px|y(x, y) = p(x, y)
py(y) = py|x(x, y)px(x)
py(y) .


## Page 12

358
7
Statistical estimation
When we substitute the observed value y into px|y, we obtain the posterior density
of x. It represents our knowledge of x after the observation.
In the MAP estimation method, our estimate of x, given the observation y, is
given by
ˆxmap
=
argmaxxpx|y(x, y)
=
argmaxxpy|x(x, y)px(x)
=
argmaxxp(x, y).
In other words, we take as estimate of x the value that maximizes the conditional
density of x, given the observed value of y.
The only diﬀerence between this
estimate and the maximum likelihood estimate is the second term, px(x), appearing
here. This term can be interpreted as taking our prior knowledge of x into account.
Note that if the prior density of x is uniform over a set C, then ﬁnding the MAP
estimate is the same as maximizing the likelihood function subject to x ∈C, which
is the ML estimation problem (7.1).
Taking logarithms, we can express the MAP estimate as
ˆxmap = argmaxx(log py|x(x, y) + log px(x)).
(7.6)
The ﬁrst term is essentially the same as the log-likelihood function; the second
term penalizes choices of x that are unlikely, according to the prior density (i.e., x
with px(x) small).
Brushing aside the philosophical diﬀerences in setup, the only diﬀerence between
ﬁnding the MAP estimate (via (7.6)) and the ML estimate (via (7.1)) is the presence
of an extra term in the optimization problem, associated with the prior density of
x. Therefore, for any maximum likelihood estimation problem with concave log-
likelihood function, we can add a prior density for x that is log-concave, and the
resulting MAP estimation problem will be convex.
Linear measurements with IID noise
Suppose that x ∈Rn and y ∈Rm are related by
yi = aT
i x + vi,
i = 1, . . . , m,
where vi are IID with density pv on R, and x has prior density px on Rn. The
joint density of x and y is then
p(x, y) = px(x)
m
Y
i=1
pv(yi −aT
i x),
and the MAP estimate can be found by solving the optimization problem
maximize
log px(x) + Pm
i=1 log pv(yi −aT
i x).
(7.7)
If px and pv are log-concave, this problem is convex. The only diﬀerence between
the MAP estimation problem (7.7) and the associated ML estimation problem (7.2)
is the extra term log px(x).


## Page 13

7.2
Nonparametric distribution estimation
359
For example, if vi are uniform on [−a, a], and the prior distribution of x is
Gaussian with mean ¯x and covariance Σ, the MAP estimate is found by solving
the QP
minimize
(x −¯x)T Σ−1(x −¯x)
subject to
∥Ax −y∥∞≤a,
with variable x.
MAP with perfect linear measurements
Suppose x ∈Rn is a vector of parameters to be estimated, with prior density
px. We have m perfect (noise free, deterministic) linear measurements, given by
y = Ax. In other words, the conditional distribution of y, given x, is a point mass
with value one at the point Ax. The MAP estimate can be found by solving the
problem
maximize
log px(x)
subject to
Ax = y.
If px is log-concave, this is a convex problem.
If under the prior distribution, the parameters xi are IID with density p on R,
then the MAP estimation problem has the form
maximize
Pn
i=1 log p(xi)
subject to
Ax = y,
which is a least-penalty problem ((6.6), page 304), with penalty function φ(u) =
−log p(u).
Conversely, we can interpret any least-penalty problem,
minimize
φ(x1) + · · · + φ(xn)
subject to
Ax = b
as a MAP estimation problem, with m perfect linear measurements (i.e., Ax = b)
and xi IID with density
p(z) =
e−φ(z)
R
e−φ(u) du.
7.2
Nonparametric distribution estimation
We consider a random variable X with values in the ﬁnite set {α1, . . . , αn} ⊆R.
(We take the values to be in R for simplicity; the same ideas can be applied when
the values are in Rk, for example.)
The distribution of X is characterized by
p ∈Rn, with prob(X = αk) = pk. Clearly, p satisﬁes p ⪰0, 1T p = 1. Conversely,
if p ∈Rn satisﬁes p ⪰0, 1T p = 1, then it deﬁnes a probability distribution for a
random variable X, deﬁned as prob(X = αk) = pk. Thus, the probability simplex
{p ∈Rn | p ⪰0, 1T p = 1}


## Page 14

360
7
Statistical estimation
is in one-to-one correspondence with all possible probability distributions for a
random variable X taking values in {α1, . . . , αn}.
In this section we discuss methods used to estimate the distribution p based on
a combination of prior information and, possibly, observations and measurements.
Prior information
Many types of prior information about p can be expressed in terms of linear equality
constraints or inequalities. If f : R →R is any function, then
E f(X) =
n
X
i=1
pif(αi)
is a linear function of p. As a special case, if C ⊆R, then prob(X ∈C) is a linear
function of p:
prob(X ∈C) = cT p,
ci =

1
αi ∈C
0
αi̸ ∈C.
It follows that known expected values of certain functions (e.g., moments) or known
probabilities of certain sets can be incorporated as linear equality constraints on
p ∈Rn. Inequalities on expected values or probabilities can be expressed as linear
inequalities on p ∈Rn.
For example, suppose we know that X has mean E X = α, second moment
E X2 = β, and prob(X ≥0) ≤0.3. This prior information can be expressed as
E X =
n
X
i=1
αipi = α,
E X2 =
n
X
i=1
α2
i pi = β,
X
αi≥0
pi ≤0.3,
which are two linear equalities and one linear inequality in p.
We can also include some prior constraints that involve nonlinear functions of
p. As an example, the variance of X is given by
var(X) = E X2 −(E X)2 =
n
X
i=1
α2
i pi −
 n
X
i=1
αipi
!2
.
The ﬁrst term is a linear function of p and the second term is concave quadratic
in p, so the variance of X is a concave function of p. It follows that a lower bound
on the variance of X can be expressed as a convex quadratic inequality on p.
As another example, suppose A and B are subsets of R, and consider the
conditional probability of A given B:
prob(X ∈A|X ∈B) = prob(X ∈A ∩B)
prob(X ∈B)
.
This function is linear-fractional in p ∈Rn: it can be expressed as
prob(X ∈A|X ∈B) = cT p/dT p,
where
ci =
 1
αi ∈A ∩B
0
αi̸ ∈A ∩B
,
di =
 1
αi ∈B
0
αi̸ ∈B.


## Page 15

7.2
Nonparametric distribution estimation
361
Therefore we can express the prior constraints
l ≤prob(X ∈A|X ∈B) ≤u
as the linear inequality constraints on p
ldT p ≤cT p ≤udT p.
Several other types of prior information can be expressed in terms of nonlinear
convex inequalities. For example, the entropy of X, given by
−
n
X
i=1
pi log pi,
is a concave function of p, so we can impose a minimum value of entropy as a convex
inequality on p. If q represents another distribution, i.e., q ⪰0, 1T q = 1, then
the Kullback-Leibler divergence between the distribution q and the distribution p
is given by
n
X
i=1
pi log(pi/qi),
which is convex in p (and q as well; see example 3.19, page 90). It follows that
we can impose a maximum Kullback-Leibler divergence between p and a given
distribution q, as a convex inequality on p.
In the next few paragraphs we express the prior information about the distribu-
tion p as p ∈P. We assume that P can be described by a set of linear equalities and
convex inequalities. We include in the prior information P the basic constraints
p ⪰0, 1T p = 1.
Bounding probabilities and expected values
Given prior information about the distribution, say p ∈P, we can compute upper
or lower bounds on the expected value of a function, or probability of a set. For
example to determine a lower bound on E f(X) over all distributions that satisfy
the prior information p ∈P, we solve the convex problem
minimize
Pn
i=1 f(αi)pi
subject to
p ∈P.
Maximum likelihood estimation
We can use maximum likelihood estimation to estimate p based on observations
from the distribution. Suppose we observe N independent samples x1, . . . , xN from
the distribution. Let ki denote the number of these samples with value αi, so that
k1 + · · · + kn = N, the total number of observed samples.
The log-likelihood
function is then
l(p) =
n
X
i=1
ki log pi,


## Page 16

362
7
Statistical estimation
which is a concave function of p. The maximum likelihood estimate of p can be
found by solving the convex problem
maximize
l(p) = Pn
i=1 ki log pi
subject to
p ∈P,
with variable p.
Maximum entropy
The maximum entropy distribution consistent with the prior assumptions can be
found by solving the convex problem
minimize
Pn
i=1 pi log pi
subject to
p ∈P.
Enthusiasts describe the maximum entropy distribution as the most equivocal or
most random, among those consistent with the prior information.
Minimum Kullback-Leibler divergence
We can ﬁnd the distribution p that has minimum Kullback-Leibler divergence from
a given prior distribution q, among those consistent with prior information, by
solving the convex problem
minimize
Pn
i=1 pi log(pi/qi)
subject to
p ∈P,
Note that when the prior distribution is the uniform distribution, i.e., q = (1/n)1,
this problem reduces to the maximum entropy problem.
Example 7.2 We consider a probability distribution on 100 equidistant points αi in
the interval [−1, 1]. We impose the following prior assumptions:
E X
∈
[−0.1, 0.1]
E X2
∈
[0.5, 0.6]
E(3X3 −2X)
∈
[−0.3, −0.2]
prob(X < 0)
∈
[0.3, 0.4].
(7.8)
Along with the constraints 1T p = 1, p ⪰0, these constraints describe a polyhedron
of probability distributions.
Figure 7.2 shows the maximum entropy distribution that satisﬁes these constraints.
The maximum entropy distribution satisﬁes
E X
=
0.056
E X2
=
0.5
E(3X3 −2X)
=
−0.2
prob(X < 0)
=
0.4.
To illustrate bounding probabilities, we compute upper and lower bounds on the
cumulative distribution prob(X ≤αi), for i = 1, . . . , 100.
For each value of i,


## Page 17

7.2
Nonparametric distribution estimation
363
αi
pi = prob(X = αi)
−1
−0.5
0
0.5
1
0
0.01
0.02
0.03
0.04
Figure 7.2 Maximum entropy distribution that satisﬁes the constraints (7.8).
we solve two LPs: one that maximizes prob(X ≤αi), and one that minimizes
prob(X ≤αi), over all distributions consistent with the prior assumptions (7.8).
The results are shown in ﬁgure 7.3. The upper and lower curves show the upper and
lower bounds, respectively; the middle curve shows the cumulative distribution of the
maximum entropy distribution.
Example 7.3 Bounding risk probability with known marginal distributions. Suppose X
and Y are two random variables that give the return on two investments. We assume
that X takes values in {α1, . . . , αn} ⊆R and Y takes values in {β1, . . . , βm} ⊆R,
with pij = prob(X = αi, Y = βj). The marginal distributions of the two returns X
and Y are known, i.e.,
m
X
j=1
pij = ri,
i = 1, . . . , n,
n
X
i=1
pij = qj,
j = 1, . . . , m,
(7.9)
but otherwise nothing is known about the joint distribution p. This deﬁnes a poly-
hedron of joint distributions consistent with the given marginals.
Now suppose we make both investments, so our total return is the random variable
X + Y . We are interested in computing an upper bound on the probability of some
level of loss, or low return, i.e., prob(X + Y < γ). We can compute a tight upper
bound on this probability by solving the LP
maximize
P
{pij | αi + βj < γ}
subject to
(7.9),
pij ≥0,
i = 1, . . . n,
j = 1, . . . , m.
The optimal value of this LP is the maximum probability of loss.
The optimal
solution p⋆is the joint distribution, consistent with the given marginal distributions,
that maximizes the probability of the loss.
The same method can be applied to a derivative of the two investments. Let R(X, Y )
be the return of the derivative, where R : R2 →R. We can compute sharp lower


## Page 18

364
7
Statistical estimation
αi
prob(X ≤αi)
−1
−0.5
0
0.5
1
0
0.2
0.4
0.6
0.8
1
Figure 7.3 The top and bottom curves show the maximum and minimum
possible values of the cumulative distribution function, prob(X ≤αi), over
all distributions that satisfy (7.8). The middle curve is the cumulative dis-
tribution of the maximum entropy distribution that satisﬁes (7.8).
and upper bounds on prob(R < γ) by solving a similar LP, with objective function
X
{pij | R(αi, βj) < γ} ,
which we can minimize and maximize.
7.3
Optimal detector design and hypothesis testing
Suppose X is a random variable with values in {1, . . . , n}, with a distribution that
depends on a parameter θ ∈{1, . . . , m}. The distributions of X, for the m possible
values of θ, can be represented by a matrix P ∈Rn×m, with elements
pkj = prob(X = k | θ = j).
The jth column of P gives the probability distribution associated with the param-
eter value θ = j.
We consider the problem of estimating θ, based on an observed sample of X. In
other words, the sample X is generated from one of the m possible distributions,
and we are to guess which one. The m values of θ are called hypotheses, and guessing
which hypothesis is correct (i.e., which distribution generated the observed sample
X) is called hypothesis testing. In many cases one of the hypotheses corresponds
to some normal situation, and each of the other hypotheses corresponds to some
abnormal event. In this case hypothesis testing can be interpreted as observing a


## Page 19

7.3
Optimal detector design and hypothesis testing
365
value of X, and then guessing whether or not an abnormal event has occurred, and
if so, which one. For this reason hypothesis testing is also called detection.
In most cases there is no signiﬁcance to the ordering of the hypotheses; they are
simply m diﬀerent hypotheses, arbitrarily labeled θ = 1, . . . , m. If ˆθ = θ, where ˆθ
denotes the estimate of θ, then we have correctly guessed the parameter value θ. If
ˆθ̸ = θ, then we have (incorrectly) guessed the parameter value θ; we have mistaken
ˆθ for θ. In other cases, there is signiﬁcance in the ordering of the hypotheses. In this
case, an event such as ˆθ > θ, i.e., the event that we overestimate θ, is meaningful.
It is also possible to parametrize θ by values other than {1, . . . , m}, say as θ ∈
{θ1, . . . , θm}, where θi are (distinct) values. These values could be real numbers, or
vectors, for example, specifying the mean and variance of the kth distribution. In
this case, a quantity such as ∥ˆθ−θ∥, which is the norm of the parameter estimation
error, is meaningful.
7.3.1
Deterministic and randomized detectors
A (deterministic) estimator or detector is a function ψ from {1, . . . , n} (the set of
possible observed values) into {1, . . . , m} (the set of hypotheses). If X is observed
to have value k, then our guess for the value of θ is ˆθ = ψ(k).
One obvious
deterministic detector is the maximum likelihood detector, given by
ˆθ = ψml(k) = argmax
j
pkj.
(7.10)
When we observe the value X = k, the maximum likelihood estimate of θ is a
value that maximizes the probability of observing X = k, over the set of possible
distributions.
We will consider a generalization of the deterministic detector, in which the
estimate of θ, given an observed value of X, is random. A randomized detector
of θ is a random variable ˆθ ∈{1, . . . , m}, with a distribution that depends on the
observed value of X. A randomized detector can be deﬁned in terms of a matrix
T ∈Rm×n with elements
tik = prob(ˆθ = i | X = k).
The interpretation is as follows: if we observe X = k, then the detector gives ˆθ = i
with probability tik.
The kth column of T, which we will denote tk, gives the
probability distribution of ˆθ, when we observe X = k. If each column of T is a
unit vector, then the randomized detector is a deterministic detector, i.e., ˆθ is a
(deterministic) function of the observed value of X.
At ﬁrst glance, it seems that intentionally introducing additional randomiza-
tion into the estimation or detection process can only make the estimator worse.
But we will see below examples in which a randomized detector outperforms all
deterministic estimators.
We are interested in designing the matrix T that deﬁnes the randomized detec-
tor. Obviously the columns tk of T must satisfy the (linear equality and inequality)
constraints
tk ⪰0,
1T tk = 1.
(7.11)


## Page 20

366
7
Statistical estimation
7.3.2
Detection probability matrix
For the randomized detector deﬁned by the matrix T, we deﬁne the detection
probability matrix as D = TP. We have
Dij = (TP)ij = prob(ˆθ = i | θ = j),
so Dij is the probability of guessing ˆθ = i, when in fact θ = j.
The m × m
detection probability matrix D characterizes the performance of the randomized
detector deﬁned by T. The diagonal entry Dii is the probability of guessing ˆθ = i
when θ = i, i.e., the probability of correctly detecting that θ = i. The oﬀ-diagonal
entry Dij (with i̸ = j) is the probability of mistaking θ = i for θ = j, i.e., the
probability that our guess is ˆθ = i, when in fact θ = j. If D = I, the detector is
perfect: no matter what the parameter θ is, we correctly guess ˆθ = θ.
The diagonal entries of D, arranged in a vector, are called the detection proba-
bilities, and denoted P d:
P d
i = Dii = prob(ˆθ = i | θ = i).
The error probabilities are the complements, and are denoted P e:
P e
i = 1 −Dii = prob(ˆθ̸ = i | θ = i).
Since the columns of the detection probability matrix D add up to one, we can
express the error probabilities as
P e
i =
X
j̸=i
Dji.
7.3.3
Optimal detector design
In this section we show that a wide variety of objectives for detector design are
linear, aﬃne, or convex piecewise-linear functions of D, and therefore also of T
(which is the optimization variable). Similarly, a variety of constraints for detector
design can be expressed in terms of linear inequalities in D. It follows that a wide
variety of optimal detector design problems can be expressed as LPs. We will see
in §7.3.4 that some of these LPs have simple solutions; in this section we simply
formulate the problem.
Limits on errors and detection probabilities
We can impose a lower bound on the probability of correctly detecting the jth
hypothesis,
P d
j = Djj ≥Lj,
which is a linear inequality in D (hence, T). Similarly, we can impose a maximum
allowable probability for mistaking θ = i for θ = j:
Dij ≤Uij,


## Page 21

7.3
Optimal detector design and hypothesis testing
367
which are also linear constraints on T. We can take any of the detection prob-
abilities as an objective to be maximized, or any of the error probabilities as an
objective to be minimized.
Minimax detector design
We can take as objective (to be minimized) the minimax error probability, maxj P e
j ,
which is a piecewise-linear convex function of D (hence, also of T). With this as
the only objective, we have the problem of minimizing the maximum probability
of detection error,
minimize
maxj P e
j
subject to
tk ⪰0,
1T tk = 1,
k = 1, . . . , n,
where the variables are t1, . . . , tn ∈Rm. This can be reformulated as an LP. The
minimax detector minimizes the worst-case (largest) probability of error over all m
hypotheses.
We can, of course, add further constraints to the minimax detector design prob-
lem.
Bayes detector design
In Bayes detector design, we have a prior distribution for the hypotheses, given by
q ∈Rm, where
qi = prob(θ = i).
In this case, the probabilities pij are interpreted as conditional probabilities of X,
given θ. The probability of error for the detector is then given by qT P e, which is
an aﬃne function of T. The Bayes optimal detector is the solution of the LP
minimize
qT P e
subject to
tk ⪰0,
1T tk = 1,
k = 1, . . . , n.
We will see in §7.3.4 that this problem has a simple analytical solution.
One special case is when q = (1/m)1. In this case the Bayes optimal detector
minimizes the average probability of error, where the (unweighted) average is over
the hypotheses. In §7.3.4 we will see that the maximum likelihood detector (7.10)
is optimal for this problem.
Bias, mean-square error, and other quantities
In this section we assume that the ordering of the values of θ have some signiﬁcance,
i.e., that the value θ = i can be interpreted as a larger value of the parameter than
θ = j, when i > j. This might be the case, for example, when θ = i corresponds to
the hypothesis that i events have occurred. Here we may be interested in quantities
such as
prob(ˆθ > θ | θ = i),
which is the probability that we overestimate θ when θ = i.
This is an aﬃne
function of D:
prob(ˆθ > θ | θ = i) =
X
j>i
Dji,


## Page 22

368
7
Statistical estimation
so a maximum allowable value for this probability can be expressed as a linear
inequality on D (hence, T). As another example, the probability of misclassifying
θ by more than one, when θ = i,
prob(|ˆθ −θ| > 1 | θ = i) =
X
|j−i|>1
Dji,
is also a linear function of D.
We now suppose that the parameters have values {θ1, . . . , θm} ⊆R. The es-
timation or detection (parameter) error is then given by ˆθ −θ, and a number of
quantities of interest are given by linear functions of D. Examples include:
• Bias. The bias of the detector, when θ = θi, is given by the linear function
E
i (ˆθ −θ) =
m
X
j=1
(θj −θi)Dji,
where the subscript on E means the expectation is with respect to the dis-
tribution of the hypothesis θ = θi.
• Mean square error. The mean square error of the detector, when θ = θi, is
given by the linear function
E
i (ˆθ −θ)2 =
m
X
j=1
(θj −θi)2Dji.
• Average absolute error. The average absolute error of the detector, when
θ = θi, is given by the linear function
E
i |ˆθ −θ| =
m
X
j=1
|θj −θi|Dji.
7.3.4
Multicriterion formulation and scalarization
The optimal detector design problem can be considered a multicriterion problem,
with the constraints (7.11), and the m(m −1) objectives given by the oﬀ-diagonal
entries of D, which are the probabilities of the diﬀerent types of detection error:
minimize (w.r.t. Rm(m−1)
+
)
Dij,
i, j = 1, . . . , m,
i̸ = j
subject to
tk ⪰0,
1T tk = 1,
k = 1, . . . , n,
(7.12)
with variables t1, . . . , tn ∈Rm. Since each objective Dij is a linear function of the
variables, this is a multicriterion linear program.
We can scalarize this multicriterion problem by forming the weighted sum ob-
jective
m
X
i,j=1
WijDij = tr(W T D)


## Page 23

7.3
Optimal detector design and hypothesis testing
369
where the weight matrix W ∈Rm×m satisﬁes
Wii = 0,
i = 1, . . . , m,
Wij > 0,
i, j = 1, . . . , m,
i̸ = j.
This objective is a weighted sum of the m(m −1) error probabilities, with weight
Wij associated with the error of guessing ˆθ = i when in fact θ = j. The weight
matrix is sometimes called the loss matrix.
To ﬁnd a Pareto optimal point for the multicriterion problem (7.12), we form
the scalar optimization problem
minimize
tr(W T D)
subject to
tk ⪰0,
1T tk = 1,
k = 1, . . . , n,
(7.13)
which is an LP. This LP is separable in the variables t1, . . . , tn. The objective can
be expressed as a sum of (linear) functions of tk:
tr(W T D) = tr(W T TP) = tr(PW T T) =
n
X
k=1
cT
k tk,
where ck is the kth column of WP T . The constraints are separable (i.e., we have
separate constraints on each ti). Therefore we can solve the LP (7.13) by separately
solving
minimize
cT
k tk
subject to
tk ⪰0,
1T tk = 1,
for k = 1, . . . , n. Each of these LPs has a simple analytical solution (see exer-
cise 4.8). We ﬁrst ﬁnd an index q such that ckq = minj ckj. Then we take t⋆
k = eq.
This optimal point corresponds to a deterministic detector: when X = k is ob-
served, our estimate is
ˆθ = argmin
j
(WP T )jk.
(7.14)
Thus, for every weight matrix W with positive oﬀ-diagonal elements we can ﬁnd
a deterministic detector that minimizes the weighted sum objective. This seems
to suggest that randomized detectors are not needed, but we will see this is not
the case. The Pareto optimal trade-oﬀsurface for the multicriterion LP (7.12) is
piecewise-linear; the deterministic detectors of the form (7.14) correspond to the
vertices on the Pareto optimal surface.
MAP and ML detectors
Consider a Bayes detector design with prior distribution q. The mean probability
of error is
qT P e =
m
X
j=1
qj
X
i̸=j
Dij =
m
X
i,j=1
WijDij,
if we deﬁne the weight matrix W as
Wij = qj,
i, j = 1, . . . , m,
i̸ = j,
Wii = 0,
i = 1, . . . , m.


## Page 24

370
7
Statistical estimation
Thus, a Bayes optimal detector is given by the deterministic detector (7.14), with
(WP T )jk =
X
i̸=j
qipki =
m
X
i=1
qipki −qjpkj.
The ﬁrst term is independent of j, so the optimal detector is simply
ˆθ = argmax
j
(pkjqj),
when X = k is observed. The solution has a simple interpretation: Since pkjqj
gives the probability that θ = j and X = k, this detector is a maximum a posteriori
probability (MAP) detector.
For the special case q = (1/m)1, i.e., a uniform prior distribution on θ, this
MAP detector reduces to a maximum likelihood (ML) detector:
ˆθ = argmax
j
pkj.
Thus, a maximum likelihood detector minimizes the (unweighted) average or mean
probability of error.
7.3.5
Binary hypothesis testing
As an illustration, we consider the special case m = 2, which is called binary
hypothesis testing. The random variable X is generated from one of two distribu-
tions, which we denote p ∈Rn and q ∈Rn, to simplify the notation. Often the
hypothesis θ = 1 corresponds to some normal situation, and the hypothesis θ = 2
corresponds to some abnormal event that we are trying to detect. If ˆθ = 1, we say
the test is negative (i.e., we guess that the event did not occur); if ˆθ = 2, we say
the test is positive (i.e., we guess that the event did occur).
The detection probability matrix D ∈R2×2 is traditionally expressed as
D =

1 −Pfp
Pfn
Pfp
1 −Pfn

.
Here Pfn is the probability of a false negative (i.e., the test is negative when in fact
the event has occurred) and Pfp is the probability of a false positive (i.e., the test
is positive when in fact the event has not occurred), which is also called the false
alarm probability. The optimal detector design problem is a bi-criterion problem,
with objectives Pfn and Pfp.
The optimal trade-oﬀcurve between Pfn and Pfp is called the receiver operating
characteristic (ROC), and is determined by the distributions p and q. The ROC
can be found by scalarizing the bi-criterion problem, as described in §7.3.4. For
the weight matrix W, an optimal detector (7.14) is
ˆθ =
 1
W21pk > W12qk
2
W21pk ≤W12qk


## Page 25

7.3
Optimal detector design and hypothesis testing
371
Pfp
Pfn
1
2
3
4
0
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
Figure 7.4 Optimal trade-oﬀcurve between probability of a false negative,
and probability of a false positive test result, for the matrix P given in (7.15).
The vertices of the trade-oﬀcurve, labeled 1–3, correspond to deterministic
detectors; the point labeled 4, which is a randomized detector, is the mini-
max detector. The dashed line shows Pfn = Pfp, the points where the error
probabilities are equal.
when X = k is observed. This is called a likelihood ratio threshold test: if the
ratio pk/qk is more than the threshold W12/W21, the test is negative (i.e., ˆθ =
1); otherwise the test is positive. By choosing diﬀerent values of the threshold,
we obtain (deterministic) Pareto optimal detectors that give diﬀerent levels of
false positive versus false negative error probabilities.
This result is known as
the Neyman-Pearson lemma.
The likelihood ratio detectors do not give all the Pareto optimal detectors; they
are the vertices of the optimal trade-oﬀcurve, which is piecewise-linear.
Example 7.4 We consider a binary hypothesis testing example with n = 4, and
P =


0.70
0.10
0.20
0.10
0.05
0.70
0.05
0.10

.
(7.15)
The optimal trade-oﬀcurve between Pfn and Pfp, i.e., the receiver operating curve,
is shown in ﬁgure 7.4. The left endpoint corresponds to the detector which is always
negative, independent of the observed value of X; the right endpoint corresponds to
the detector that is always positive. The vertices labeled 1, 2, and 3 correspond to
the deterministic detectors
T (1)
=

1
1
0
1
0
0
1
0

,
T (2)
=

1
1
0
0
0
0
1
1

,


## Page 26

372
7
Statistical estimation
T (3)
=

1
0
0
0
0
1
1
1

,
respectively. The point labeled 4 corresponds to the nondeterministic detector
T (4) =

1
2/3
0
0
0
1/3
1
1

,
which is the minimax detector. This minimax detector yields equal probability of
a false positive and false negative, which in this case is 1/6.
Every deterministic
detector has either a false positive or false negative probability that exceeds 1/6,
so this is an example where a randomized detector outperforms every deterministic
detector.
7.3.6
Robust detectors
So far we have assumed that P, which gives the distribution of the observed variable
X, for each value of the parameter θ, is known. In this section we consider the case
where these distributions are not known, but certain prior information about them
is given. We assume that P ∈P, where P is the set of possible distributions. With
a randomized detector characterized by T, the detection probability matrix D now
depends on the particular value of P. We will judge the error probabilities by
their worst-case values, over P ∈P. We deﬁne the worst-case detection probability
matrix Dwc as
Dwc
ij = sup
P ∈P
Dij,
i, j = 1, . . . , m,
i̸ = j
and
Dwc
ii = inf
P ∈P Dii,
i = 1, . . . , m.
The oﬀ-diagonal entries give the largest possible probability of errors, and the
diagonal entries give the smallest possible probability of detection, over P ∈P.
Note that Pn
i=1 Dwc
ij̸
= 1 in general, i.e., the columns of a worst-case detection
probability matrix do not necessarily add up to one.
We deﬁne the worst-case probability of error as
P wce
i
= 1 −Dwc
ii .
Thus, P wce
i
is the largest probability of error, when θ = i, over all possible distri-
butions in P.
Using the worst-case detection probability matrix, or the worst-case probability
of error vector, we can develop various robust versions of detector design problems.
In the rest of this section we concentrate on the robust minimax detector design
problem, as a generic example that illustrates the ideas.
We deﬁne the robust minimax detector as the detector that minimizes the worst-
case probability of error, over all hypotheses, i.e., minimizes the objective
max
i
P wce
i
=
max
i=1,...,m sup
P ∈P
(1 −(TP)ii) = 1 −
min
i=1,...,m inf
P ∈P(TP)ii.
The robust minimax detector minimizes the worst possible probability of error,
over all m hypotheses, and over all P ∈P.


## Page 27

7.3
Optimal detector design and hypothesis testing
373
Robust minimax detector for ﬁnite P
When the set of possible distributions is ﬁnite, the robust minimax detector design
problem is readily formulated as an LP. With P = {P1, . . . , Pk}, we can ﬁnd the
robust minimax detector by solving
maximize
mini=1,...,m infP ∈P(TP)ii = mini=1,...,m minj=1,...,k(TPj)ii
subject to
ti ⪰0,
1T ti = 1,
i = 1, . . . , n,
The objective is piecewise-linear and concave, so this problem can be expressed as
an LP. Note that we can just as well consider P to be the polyhedron conv P;
the associated worst-case detection matrix, and robust minimax detector, are the
same.
Robust minimax detector for polyhedral P
It is also possible to eﬃciently formulate the robust minimax detector problem as an
LP when P is a polyhedron described by linear equality and inequality constraints.
This formulation is less obvious, and relies on a dual representation of P.
To simplify the discussion, we assume that P has the form
P =

P = [p1 · · · pm]
 Akpk = bk, 1T pk = 1, pk ⪰0
	
.
(7.16)
In other words, for each distribution pk, we are given some expected values Akpk =
bk. (These might represent known moments, probabilities, etc.) The extension to
the case where we are given inequalities on expected values is straightforward.
The robust minimax design problem is
maximize
γ
subject to
inf{˜tT
i p | Aip = bi, 1T p = 1, p ⪰0} ≥γ,
i = 1, . . . , m
ti ⪰0,
1T ti = 1,
i = 1, . . . , n,
where ˜tT
i denotes the ith row of T (so that (TP)ii = ˜tT
i pi). By LP duality,
inf{˜tT
i p | Aip = bi, 1T p = 1, p ⪰0} = sup{νT bi + µ | AT
i ν + µ1 ⪯˜ti}.
Using this, the robust minimax detector design problem can be expressed as the
LP
maximize
γ
subject to
νT
i bi + µi ≥γ,
i = 1, . . . , m
AT
i νi + µi1 ⪯˜ti,
i = 1, . . . , m
ti ⪰0,
1T ti = 1,
i = 1, . . . , n,
with variables ν1, . . . , νm, µ1, . . . , µn, and T (which has columns ti and rows ˜tT
i ).
Example 7.5 Robust binary hypothesis testing. Suppose m = 2 and the set P in (7.16)
is deﬁned by
A1 = A2 = A =

a1
a2
· · ·
an
a2
1
a2
2
· · ·
a2
n

,
b1 =

α1
α2

,
b2 =

β1
β2

.
Designing a robust minimax detector for this set P can be interpreted as a binary
hypothesis testing problem: based on an observation of a random variable X ∈
{a1, . . . , an}, choose between the following two hypotheses:


## Page 28

374
7
Statistical estimation
1. E X = α1, E X2 = α2
2. E X = β1, E X2 = β2.
Let ˜tT denote the ﬁrst row of T (and so, (1 −˜t)T is the second row). For given ˜t, the
worst-case probabilities of correct detection are
Dwc
11
=
inf
(
˜tT p

n
X
i=1
aipi = α1,
n
X
i=1
a2
i pi = α2, 1T p = 1, p ⪰0
)
Dwc
22
=
inf
(
(1 −˜t)T p

n
X
i=1
aipi = β1,
n
X
i=1
a2
i pi = β2, 1T p = 1, p ⪰0
)
.
Using LP duality we can express Dwc
11 as the optimal value of the LP
maximize
z0 + z1α1 + z2α2
subject to
z0 + aiz1 + a2
i z2 ≤˜ti,
i = 1, . . . , n,
with variables z0, z1, z2 ∈R. Similarly Dwc
22 is the optimal value of the LP
maximize
w0 + w1β1 + w2β2
subject to
w0 + aiw1 + a2
i w2 ≤1 −˜ti,
i = 1, . . . , n,
with variables w0, w1, w2 ∈R. To obtain the minimax detector, we have to maximize
the minimum of Dwc
11 and Dwc
22 , i.e., solve the LP
maximize
γ
subject to
z0 + z1α2 + z2α2 ≥γ
w0 + β1w1 + β2w2 ≥γ
z0 + z1ai + z2a2
i ≤˜ti,
i = 1, . . . , n
w0 + w1ai + w2a2
i ≤1 −˜ti,
i = 1, . . . , n
0 ⪯˜t ⪯1.
The variables are z0, z1, z2, w0, w1, w2 and ˜t.
7.4
Chebyshev and Chernoﬀbounds
In this section we consider two types of classical bounds on the probability of a set,
and show that generalizations of each can be cast as convex optimization problems.
The original classical bounds correspond to simple convex optimization problems
with analytical solutions; the convex optimization formulation of the general cases
allow us to compute better bounds, or bounds for more complex situations.
7.4.1
Chebyshev bounds
Chebyshev bounds give an upper bound on the probability of a set based on known
expected values of certain functions (e.g., mean and variance). The simplest ex-
ample is Markov’s inequality: If X is a random variable on R+ with E X = µ,


## Page 29

7.4
Chebyshev and Chernoﬀbounds
375
then we have prob(X ≥1) ≤µ, no matter what the distribution of X is. An-
other simple example is Chebyshev’s bound: If X is a random variable on R with
E X = µ and E(X −µ)2 = σ2, then we have prob(|X −µ| ≥1) ≤σ2, again no
matter what the distribution of X is. The idea behind these simple bounds can be
generalized to a setting in which convex optimization is used to compute a bound
on the probability.
Let X be a random variable on S ⊆Rm, and C ⊆S be the set for which we
want to bound prob(X ∈C). Let 1C denote the 0-1 indicator function of the set
C, i.e., 1C(z) = 1 if z ∈C and 1C(z) = 0 if z̸ ∈C.
Our prior knowledge of the distribution consists of known expected values of
some functions:
E fi(X) = ai,
i = 1, . . . , n,
where fi : Rm →R. We take f0 to be the constant function with value one, for
which we always have E f0(X) = a0 = 1. Consider a linear combination of the
functions fi, given by
f(z) =
n
X
i=0
xifi(z),
where xi ∈R, i = 0, . . . , n. From our knowledge of E fi(X), we have E f(X) =
aT x.
Now suppose that f satisﬁes the condition f(z) ≥1C(z) for all z ∈S, i.e., f
is pointwise greater than or equal to the indicator function of C (on S). Then we
have
E f(X) = aT x ≥E 1C(X) = prob(X ∈C).
In other words, aT x is an upper bound on prob(X ∈C), valid for all distributions
supported on S, with E fi(X) = ai.
We can search for the best such upper bound on prob(X ∈C), by solving the
problem
minimize
x0 + a1x1 + · · · + anxn
subject to
f(z) = Pn
i=0 xifi(z) ≥1 for z ∈C
f(z) = Pn
i=0 xifi(z) ≥0 for z ∈S, z /∈C,
(7.17)
with variable x ∈Rn+1. This problem is always convex, since the constraints can
be expressed as
g1(x) = 1 −inf
z∈C f(z) ≤0,
g2(x) = −
inf
z∈S\C f(z) ≤0
(g1 and g2 are convex). The problem (7.17) can also be thought of as a semi-inﬁnite
linear program, i.e., an optimization problem with a linear objective and an inﬁnite
number of linear inequalities, one for each z ∈S.
In simple cases we can solve the problem (7.17) analytically. As an example, we
take S = R+, C = [1, ∞), f0(z) = 1, and f1(z) = z, with E f1(X) = E X = µ ≤1
as our prior information. The constraint f(z) ≥0 for z ∈S reduces to x0 ≥0,
x1 ≥0. The constraint f(z) ≥1 for z ∈C, i.e., x0 + x1z ≥1 for all z ≥1, reduces
to x0 + x1 ≥1. The problem (7.17) is then
minimize
x0 + µx1
subject to
x0 ≥0,
x1 ≥0
x0 + x1 ≥1.


## Page 30

376
7
Statistical estimation
Since 0 ≤µ ≤1, the optimal point for this simple LP is x0 = 0, x1 = 1. This gives
the classical Markov bound prob(X ≥1) ≤µ.
In other cases we can solve the problem (7.17) using convex optimization.
Remark 7.1 Duality and the Chebyshev bound problem. The Chebyshev bound prob-
lem (7.17) determines a bound on prob(X ∈C) for all probability measures that
satisfy the given expected value constraints. Thus we can think of the Chebyshev
bound problem (7.17) as producing a bound on the optimal value of the inﬁnite-
dimensional problem
maximize
R
C π(dz)
subject to
R
S fi(z)π(dz) = ai,
i = 1, . . . , n
R
S π(dz) = 1
π ≥0,
(7.18)
where the variable is the measure π, and π ≥0 means that the measure is nonnegative.
Since the Chebyshev problem (7.17) produces a bound on the problem (7.18), it
should not be a surprise that they are related by duality. While semi-inﬁnite and
inﬁnite-dimensional problems are beyond the scope of this book, we can still formally
construct a dual of the problem (7.17), introducing a Lagrange multiplier function
p : S →R, with p(z) the Lagrange multiplier associated with the inequality f(z) ≥1
(for z ∈C) or f(z) ≥0 (for z ∈S\C). Using an integral over z where we would have
a sum in the ﬁnite-dimensional case, we arrive at the formal dual
maximize
R
C p(z) dz
subject to
R
S fi(z)p(z) dz = ai,
i = 1, . . . , n
R
S p(z) dz = 1
p(z) ≥0 for all z ∈S,
where the optimization variable is the function p.
This is, essentially, the same
as (7.18).
Probability bounds with known ﬁrst and second moments
As an example, suppose that S = Rm, and that we are given the ﬁrst and second
moments of the random variable X:
E X = a ∈Rm,
E XXT = Σ ∈Sm.
In other words, we are given the expected value of the m functions zi, i = 1, . . . , m,
and the m(m+1)/2 functions zizj, i, j = 1, . . . , m, but no other information about
the distribution.
In this case we can express f as the general quadratic function
f(z) = zT Pz + 2qT z + r,
where the variables (i.e., the vector x in the discussion above) are P ∈Sm, q ∈Rm,
and r ∈R. From our knowledge of the ﬁrst and second moments, we ﬁnd that
E f(X)
=
E(XT PX + 2qT X + r)
=
E tr(PXXT ) + 2 E qT X + r
=
tr(ΣP) + 2qT a + r.


## Page 31

7.4
Chebyshev and Chernoﬀbounds
377
The constraint that f(z) ≥0 for all z can be expressed as the linear matrix in-
equality
 P
q
qT
r

⪰0.
In particular, we have P ⪰0.
Now suppose that the set C is the complement of an open polyhedron,
C = Rm \ P,
P = {z | aT
i z < bi, i = 1, . . . , k}.
The condition that f(z) ≥1 for all z ∈C is the same as requiring that
aT
i z ≥bi =⇒zT Pz + 2qT z + r ≥1
for i = 1, . . . , k. This, in turn, can be expressed as: there exist τ1, . . . , τk ≥0 such
that
 P
q
qT
r −1

⪰τi

0
ai/2
aT
i /2
−bi

,
i = 1, . . . , k.
(See §B.2.)
Putting it all together, the Chebyshev bound problem (7.17) can be expressed
as
minimize
tr(ΣP) + 2qT a + r
subject to
 P
q
qT
r −1

⪰τi

0
ai/2
aT
i /2
−bi

,
i = 1, . . . , k
τi ≥0,
i = 1, . . . , k
 P
q
qT
r

⪰0,
(7.19)
which is a semideﬁnite program in the variables P, q, r, and τ1, . . . , τk.
The
optimal value, say α, is an upper bound on prob(X ∈C) over all distributions
with mean a and second moment Σ. Or, turning it around, 1 −α is a lower bound
on prob(X ∈P).
Remark 7.2
Duality and the Chebyshev bound problem. The dual SDP associated
with (7.19) can be expressed as
maximize
Pk
i=1 λi
subject to
aT
i zi ≥bλi,
i = 1, . . . , k
Pk
i=1

Zi
zi
zT
i
λi

⪯

Σ
a
aT
1


Zi
zi
zT
i
λi

⪰0,
i = 1, . . . , k.
The variables are Zi ∈Sm, zi ∈Rm, and λi ∈R, for i = 1, . . . , k.
Since the
SDP (7.19) is strictly feasible, strong duality holds and the dual optimum is attained.
We can give an interesting probability interpretation to the dual problem. Suppose
Zi, zi, λi are dual feasible and that the ﬁrst r components of λ are positive, and the


## Page 32

378
7
Statistical estimation
rest are zero. For simplicity we also assume that Pk
i=1 λi < 1. We deﬁne
xi
=
(1/λi)zi,
i = 1, . . . , r,
w0
=
1
µ
 
a −
r
X
i=1
λixi
!
,
W
=
1
µ
 
Σ −
r
X
i=1
λixixT
i
!
,
where µ = 1 −Pk
i=1 λi. With these deﬁnitions the dual feasibility constraints can be
expressed as
aT
i xi ≥bi,
i = 1, . . . , r
and
r
X
i=1
λi

xixT
i
xi
xT
i
1

+ µ

W
w0
wT
0
1

=

Σ
a
aT
1

.
Moreover, from dual feasibility,
µ

W
w0
wT
0
1

=

Σ
a
aT
1

−
r
X
i=1
λi

xixT
i
xi
xT
i
1

=

Σ
a
aT
1

−
r
X
i=1

(1/λi)zizT
i
zi
zT
i
λi

⪰

Σ
a
aT
1

−
r
X
i=1

Zi
zi
zT
i
λi

⪰
0.
Therefore, W ⪰w0wT
0 , so it can be factored as W −w0wT
0 = Ps
i=1 wiwT
i . Now
consider a discrete random variable X with the following distribution. If s ≥1, we
take
X = xi
with probability λi, i = 1, . . . , r
X = w0 + √s wi
with probability µ/(2s), i = 1, . . . , s
X = w0 −√s wi
with probability µ/(2s), i = 1, . . . , s.
If s = 0, we take
X = xi
with probability λi, i = 1, . . . , r
X = w0
with probability µ.
It is easily veriﬁed that E X = a and E XXT = Σ, i.e., the distribution matches the
given moments. Furthermore, since xi ∈C,
prob(X ∈C) ≥
r
X
i=1
λi.
In particular, by applying this interpretation to the dual optimal solution, we can
construct a distribution that satisﬁes the Chebyshev bound from (7.19) with equality,
which shows that the Chebyshev bound is sharp for this case.


## Page 33

7.4
Chebyshev and Chernoﬀbounds
379
7.4.2
Chernoﬀbounds
Let X be a random variable on R. The Chernoﬀbound states that
prob(X ≥u) ≤inf
λ≥0 E eλ(X−u),
which can be expressed as
log prob(X ≥u) ≤inf
λ≥0{−λu + log E eλX}.
(7.20)
Recall (from example 3.41, page 106) that the righthand term, log E eλX, is called
the cumulant generating function of the distribution, and is always convex, so the
function to be minimized is convex. The bound (7.20) is most useful in cases when
the cumulant generating function has an analytical expression, and the minimiza-
tion over λ can be carried out analytically.
For example, if X is Gaussian with zero mean and unit variance, the cumulant
generating function is
log E eλX = λ2/2,
and the inﬁmum over λ ≥0 of −λu + λ2/2 occurs with λ = u (if u ≥0), so the
Chernoﬀbound is (for u ≥0)
prob(X ≥u) ≤e−u2/2.
The idea behind the Chernoﬀbound can be extended to a more general setting,
in which convex optimization is used to compute a bound on the probability of a
set in Rm. Let C ⊆Rm, and as in the description of Chebyshev bounds above,
let 1C denote the 0-1 indicator function of C. We will derive an upper bound on
prob(X ∈C). (In principle we can compute prob(X ∈C), for example by Monte
Carlo simulation, or numerical integration, but either of these can be a daunting
computational task, and neither method produces guaranteed bounds.)
Let λ ∈Rm and µ ∈R, and consider the function f : Rm →R given by
f(z) = eλT z+µ.
As in the development of Chebyshev bounds, if f satisﬁes f(z) ≥1C(z) for all z,
then we can conclude that
prob(X ∈C) = E 1C(X) ≤E f(X).
Clearly we have f(z) ≥0 for all z; to have f(z) ≥1 for z ∈C is the same as
λT z + µ ≥0 for all z ∈C, i.e., −λT z ≤µ for all z ∈C. Thus, if −λT z ≤µ for all
z ∈C, we have the bound
prob(X ∈C) ≤E exp(λT X + µ),
or, taking logarithms,
log prob(X ∈C) ≤µ + log E exp(λT X).


## Page 34

380
7
Statistical estimation
From this we obtain a general form of Chernoﬀ’s bound:
log prob(X ∈C)
≤
inf{µ + log E exp(λT X) | −λT z ≤µ for all z ∈C}
=
inf
λ

sup
z∈C
(−λT z) + log E exp(λT X)

=
inf
 SC(−λ) + log E exp(λT X)

,
where SC is the support function of C. Note that the second term, log E exp(λT X),
is the cumulant generating function of the distribution, and is always convex (see
example 3.41, page 106). Evaluating this bound is, in general, a convex optimiza-
tion problem.
Chernoﬀbound for a Gaussian variable on a polyhedron
As a speciﬁc example, suppose that X is a Gaussian random vector on Rm with
zero mean and covariance I, so its cumulant generating function is
log E exp(λT X) = λT λ/2.
We take C to be a polyhedron described by inequalities:
C = {x | Ax ⪯b},
which we assume is nonempty.
For use in the Chernoﬀbound, we use a dual characterization of the support
function SC:
SC(y)
=
sup{yT x | Ax ⪯b}
=
−inf{−yT x | Ax ⪯b}
=
−sup{−bT u | AT u = y, u ⪰0}
=
inf{bT u | AT u = y, u ⪰0}
where in the third line we use LP duality:
inf{cT x | Ax ⪯b} = sup{−bT u | AT u + c = 0, u ⪰0}
with c = −y. Using this expression for SC in the Chernoﬀbound we obtain
log prob(X ∈C)
≤
inf
λ
 SC(−λ) + log E exp(λT X)

=
inf
λ inf
u {bT u + λT λ/2
 u ⪰0, AT u + λ = 0}.
Thus, the Chernoﬀbound on prob(X ∈C) is the exponential of the optimal value
of the QP
minimize
bT u + λT λ/2
subject to
u ⪰0,
AT u + λ = 0,
(7.21)
where the variables are u and λ.


## Page 35

7.4
Chebyshev and Chernoﬀbounds
381
This problem has an interesting geometric interpretation. It is equivalent to
minimize
bT u + (1/2)∥AT u∥2
2
subject to
u ⪰0,
which is the dual of
maximize
−(1/2)∥x∥2
2
subject to
Ax ⪯b.
In other words, the Chernoﬀbound is
prob(X ∈C) ≤exp(−dist(0, C)2/2),
(7.22)
where dist(0, C) is the Euclidean distance of the origin to C.
Remark 7.3 The bound (7.22) can also be derived without using Chernoﬀ’s inequality.
If the distance between 0 and C is d, then there is a halfspace H = {z | aT z ≥d},
with ∥a∥2 = 1, that contains C. The random variable aT X is N(0, 1), so
prob(X ∈C) ≤prob(X ∈H) = Φ(−d),
where Φ is the cumulative distribution function of a zero mean, unit variance Gaus-
sian. Since Φ(−d) ≤e−d2/2 for d ≥0, this bound is at least as sharp as the Chernoﬀ
bound (7.22).
7.4.3
Example
In this section we illustrate the Chebyshev and Chernoﬀprobability bounding
methods with a detection example. We have a set of m possible symbols or signals
s ∈{s1, s2, . . . , sm} ⊆Rn, which is called the signal constellation. One of these
signals is transmitted over a noisy channel.
The received signal is x = s + v,
where v is a noise, modeled as a random variable. We assume that E v = 0 and
E vvT = σ2I, i.e., the noise components v1, . . . , vn are zero mean, uncorrelated,
and have variance σ2. The receiver must estimate which signal was sent on the
basis of the received signal x = s + v. The minimum distance detector chooses as
estimate the symbol sk closest (in Euclidean norm) to x. (If the noise v is Gaussian,
then minimum distance decoding is the same as maximum likelihood decoding.)
If the signal sk is transmitted, correct detection occurs if sk is the estimate,
given x. This occurs when the signal sk is closer to x than the other signals, i.e.,
∥x −sk∥2 < ∥x −sj∥2,
j̸ = k.
Thus, correct detection of symbol sk occurs if the random variable v satisﬁes the
linear inequalities
2(sj −sk)T (sk + v) < ∥sj∥2
2 −∥sk∥2
2,
j̸ = k.
These inequalities deﬁne the Voronoi region Vk of sk in the signal constellation,
i.e., the set of points closer to sk than any other signal in the constellation. The
probability of correct detection of sk is prob(sk + v ∈Vk).
Figure 7.5 shows a simple example with m = 7 signals, with dimension n = 2.


## Page 36

382
7
Statistical estimation
s1
s2
s3
s4
s5
s6
s7
Figure 7.5 A constellation of 7 signals s1, . . . , s7 ∈R2, shown as small circles.
The line segments show the boundaries of the corresponding Voronoi regions.
The minimum distance detector selects symbol sk when the received signal
lies closer to sk than to any of the other points, i.e., if the received signal is
in the interior of the Voronoi region around symbol sk. The circles around
each point have radius one, to show the scale.
Chebyshev bounds
The SDP bound (7.19) provides a lower bound on the probability of correct detec-
tion, and is plotted in ﬁgure 7.6, as a function of the noise standard deviation σ,
for the three symbols s1, s2, and s3. These bounds hold for any noise distribution
with zero mean and covariance σ2I. They are tight in the sense that there exists
a noise distribution with zero mean and covariance Σ = σ2I, for which the proba-
bility of error is equal to the lower bound. This is illustrated in ﬁgure 7.7, for the
ﬁrst Voronoi set, and σ = 1.
Chernoﬀbounds
We use the same example to illustrate the Chernoﬀbound. Here we assume that the
noise is Gaussian, i.e., v ∼N(0, σ2I). If symbol sk is transmitted, the probability
of correct detection is the probability that sk + v ∈Vk. To ﬁnd a lower bound for
this probability, we use the QP (7.21) to compute upper bounds on the probability
that the ML detector selects symbol i, i = 1, . . . , m, i̸ = k. (Each of these upper
bounds is related to the distance of sk to the Voronoi set Vi.) Adding these upper
bounds on the probabilities of mistaking sk for si, we obtain an upper bound on
the probability of error, and therefore, a lower bound on the probability of correct
detection of symbol sk. The resulting lower bound, for s1, is shown in ﬁgure 7.8,
along with an estimate of the probability of correct detection obtained using Monte
Carlo analysis.


## Page 37

7.4
Chebyshev and Chernoﬀbounds
383
1
2
3
σ
probability of correct detection
0
0.5
1
1.5
2
2.5
0
0.2
0.4
0.6
0.8
1
Figure 7.6 Chebyshev lower bounds on the probability of correct detection
for symbols s1, s2, and s3. These bounds are valid for any noise distribution
that has zero mean and covariance σ2I.
s1
s2
s3
s4
s5
s6
s7
Figure 7.7 The Chebyshev lower bound on the probability of correct detec-
tion of symbol 1 is equal to 0.2048 when σ = 1. This bound is achieved by
the discrete distribution illustrated in the ﬁgure. The solid circles are the
possible values of the received signal s1 + v. The point in the center of the
ellipse has probability 0.2048. The ﬁve points on the boundary have a total
probability 0.7952. The ellipse is deﬁned by xT Px + 2qT x + r = 1, where
P, q, and r are the optimal solution of the SDP (7.19).


## Page 38

384
7
Statistical estimation
σ
probability of correct detection
0.2
0.3
0.4
0.5
0.9
0.95
1
Figure 7.8 The Chernoﬀlower bound (solid line) and a Monte Carlo esti-
mate (dashed line) of the probability of correct detection of symbol s1, as
a function of σ. In this example the noise is Gaussian with zero mean and
covariance σ2I.
7.5
Experiment design
We consider the problem of estimating a vector x ∈Rn from measurements or
experiments
yi = aT
i x + wi,
i = 1, . . . , m,
where wi is measurement noise.
We assume that wi are independent Gaussian
random variables with zero mean and unit variance, and that the measurement
vectors a1, . . . , am span Rn. The maximum likelihood estimate of x, which is the
same as the minimum variance estimate, is given by the least-squares solution
ˆx =
 m
X
i=1
aiaT
i
!−1
m
X
i=1
yiai.
The associated estimation error e = ˆx −x has zero mean and covariance matrix
E = E eeT =
 m
X
i=1
aiaT
i
!−1
.
The matrix E characterizes the accuracy of the estimation, or the informativeness
of the experiments. For example the α-conﬁdence level ellipsoid for x is given by
E = {z | (z −ˆx)T E−1(z −ˆx) ≤β},
where β is a constant that depends on n and α.
We suppose that the vectors a1, . . . , am, which characterize the measurements,
can be chosen among p possible test vectors v1, . . . , vp ∈Rn, i.e., each ai is one of


## Page 39

7.5
Experiment design
385
the vj. The goal of experiment design is to choose the vectors ai, from among the
possible choices, so that the error covariance E is small (in some sense). In other
words, each of m experiments or measurements can be chosen from a ﬁxed menu
of p possible experiments; our job is to ﬁnd a set of measurements that (together)
are maximally informative.
Let mj denote the number of experiments for which ai is chosen to have the
value vj, so we have
m1 + · · · + mp = m.
We can express the error covariance matrix as
E =
 m
X
i=1
aiaT
i
!−1
=


p
X
j=1
mjvjvT
j


−1
.
This shows that the error covariance depends only on the numbers of each type of
experiment chosen (i.e., m1, . . . , mp).
The basic experiment design problem is as follows. Given the menu of possible
choices for experiments, i.e., v1, . . . , vp, and the total number m of experiments to
be carried out, choose the numbers of each type of experiment, i.e., m1, . . . , mp,
to make the error covariance E small (in some sense). The variables m1, . . . , mp
must, of course, be integers and sum to m, the given total number of experiments.
This leads to the optimization problem
minimize (w.r.t. Sn
+)
E =
Pp
j=1 mjvjvT
j
−1
subject to
mi ≥0,
m1 + · · · + mp = m
mi ∈Z,
(7.23)
where the variables are the integers m1, . . . , mp.
The basic experiment design problem (7.23) is a vector optimization problem
over the positive semideﬁnite cone. If one experiment design results in E, and
another in ˜E, with E ⪯˜E, then certainly the ﬁrst experiment design is as good
as or better than the second. For example, the conﬁdence ellipsoid for the ﬁrst
experiment design (translated to the origin for comparison) is contained in the
conﬁdence ellipsoid of the second. We can also say that the ﬁrst experiment design
allows us to estimate qT x better (i.e., with lower variance) than the second experi-
ment design, for any vector q, since the variance of our estimate of qT x is given by
qT Eq for the ﬁrst experiment design and qT ˜Eq for the second. We will see below
several common scalarizations for the problem.
7.5.1
The relaxed experiment design problem
The basic experiment design problem (7.23) can be a hard combinatorial problem
when m, the total number of experiments, is comparable to p, since in this case
the mi are all small integers. In the case when m is large compared to p, however,
a good approximate solution of (7.23) can be found by ignoring, or relaxing, the
constraint that the mi are integers.
Let λi = mi/m, which is the fraction of


## Page 40

386
7
Statistical estimation
the total number of experiments for which aj = vi, or the relative frequency of
experiment i. We can express the error covariance in terms of λi as
E = 1
m
 p
X
i=1
λivivT
i
!−1
.
(7.24)
The vector λ ∈Rp satisﬁes λ ⪰0, 1T λ = 1, and also, each λi is an integer multiple
of 1/m. By ignoring this last constraint, we arrive at the problem
minimize (w.r.t. Sn
+)
E = (1/m)
 Pp
i=1 λivivT
i
−1
subject to
λ ⪰0,
1T λ = 1,
(7.25)
with variable λ ∈Rp. To distinguish this from the original combinatorial experi-
ment design problem (7.23), we refer to it as the relaxed experiment design problem.
The relaxed experiment design problem (7.25) is a convex optimization problem,
since the objective E is an Sn
+-convex function of λ.
Several statements can be made about the relation between the (combinato-
rial) experiment design problem (7.23) and the relaxed problem (7.25). Clearly
the optimal value of the relaxed problem provides a lower bound on the optimal
value of the combinatorial one, since the combinatorial problem has an additional
constraint. From a solution of the relaxed problem (7.25) we can construct a sub-
optimal solution of the combinatorial problem (7.23) as follows. First, we apply
simple rounding to get
mi = round(mλi),
i = 1, . . . , p.
Corresponding to this choice of m1, . . . , mp is the vector ˜λ,
˜λi = (1/m)round(mλi),
i = 1, . . . , p.
The vector ˜λ satisﬁes the constraint that each entry is an integer multiple of 1/m.
Clearly we have |λi −˜λi| ≤1/(2m), so for m large, we have λ ≈˜λ. This implies
that the constraint 1T ˜λ = 1 is nearly satisﬁed, for large m, and also that the error
covariance matrices associated with ˜λ and λ are close.
We can also give an alternative interpretation of the relaxed experiment design
problem (7.25).
We can interpret the vector λ ∈Rp as deﬁning a probability
distribution on the experiments v1, . . . , vp. Our choice of λ corresponds to a random
experiment: each experiment ai takes the form vj with probability λj.
In the rest of this section, we consider only the relaxed experiment design
problem, so we drop the qualiﬁer ‘relaxed’ in our discussion.
7.5.2
Scalarizations
Several scalarizations have been proposed for the experiment design problem (7.25),
which is a vector optimization problem over the positive semideﬁnite cone.
