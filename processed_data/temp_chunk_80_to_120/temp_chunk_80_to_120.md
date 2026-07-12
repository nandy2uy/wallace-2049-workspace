# temp_chunk_80_to_120



## Page 1

Chapter 3
Convex functions
3.1
Basic properties and examples
3.1.1
Deﬁnition
A function f : Rn →R is convex if dom f is a convex set and if for all x,
y ∈dom f, and θ with 0 ≤θ ≤1, we have
f(θx + (1 −θ)y) ≤θf(x) + (1 −θ)f(y).
(3.1)
Geometrically, this inequality means that the line segment between (x, f(x)) and
(y, f(y)), which is the chord from x to y, lies above the graph of f (ﬁgure 3.1).
A function f is strictly convex if strict inequality holds in (3.1) whenever x̸ = y
and 0 < θ < 1. We say f is concave if −f is convex, and strictly concave if −f is
strictly convex.
For an aﬃne function we always have equality in (3.1), so all aﬃne (and therefore
also linear) functions are both convex and concave. Conversely, any function that
is convex and concave is aﬃne.
A function is convex if and only if it is convex when restricted to any line that
intersects its domain. In other words f is convex if and only if for all x ∈dom f and
(x, f(x))
(y, f(y))
Figure 3.1 Graph of a convex function. The chord (i.e., line segment) be-
tween any two points on the graph lies above the graph.


## Page 2

68
3
Convex functions
all v, the function g(t) = f(x+tv) is convex (on its domain, {t | x+tv ∈dom f}).
This property is very useful, since it allows us to check whether a function is convex
by restricting it to a line.
The analysis of convex functions is a well developed ﬁeld, which we will not
pursue in any depth. One simple result, for example, is that a convex function is
continuous on the relative interior of its domain; it can have discontinuities only
on its relative boundary.
3.1.2
Extended-value extensions
It is often convenient to extend a convex function to all of Rn by deﬁning its value
to be ∞outside its domain. If f is convex we deﬁne its extended-value extension
˜f : Rn →R ∪{∞} by
˜f(x) =

f(x)
x ∈dom f
∞
x̸ ∈dom f.
The extension ˜f is deﬁned on all Rn, and takes values in R∪{∞}. We can recover
the domain of the original function f from the extension ˜f as dom f = {x | ˜f(x) <
∞}.
The extension can simplify notation, since we do not need to explicitly describe
the domain, or add the qualiﬁer ‘for all x ∈dom f’ every time we refer to f(x).
Consider, for example, the basic deﬁning inequality (3.1). In terms of the extension
˜f, we can express it as: for 0 < θ < 1,
˜f(θx + (1 −θ)y) ≤θ ˜f(x) + (1 −θ) ˜f(y)
for any x and y. (For θ = 0 or θ = 1 the inequality always holds.) Of course here we
must interpret the inequality using extended arithmetic and ordering. For x and y
both in dom f, this inequality coincides with (3.1); if either is outside dom f, then
the righthand side is ∞, and the inequality therefore holds. As another example
of this notational device, suppose f1 and f2 are two convex functions on Rn. The
pointwise sum f = f1 +f2 is the function with domain dom f = dom f1 ∩dom f2,
with f(x) = f1(x) + f2(x) for any x ∈dom f. Using extended-value extensions we
can simply say that for any x, ˜f(x) = ˜f1(x) + ˜f2(x). In this equation the domain
of f has been automatically deﬁned as dom f = dom f1 ∩dom f2, since ˜f(x) = ∞
whenever x̸ ∈dom f1 or x̸ ∈dom f2. In this example we are relying on extended
arithmetic to automatically deﬁne the domain.
In this book we will use the same symbol to denote a convex function and its
extension, whenever there is no harm from the ambiguity. This is the same as
assuming that all convex functions are implicitly extended, i.e., are deﬁned as ∞
outside their domains.
Example 3.1 Indicator function of a convex set. Let C ⊆Rn be a convex set, and
consider the (convex) function IC with domain C and IC(x) = 0 for all x ∈C. In
other words, the function is identically zero on the set C. Its extended-value extension


## Page 3

3.1
Basic properties and examples
69
(x, f(x))
f(y)
f(x) + ∇f(x)T (y −x)
Figure 3.2 If f is convex and diﬀerentiable, then f(x)+∇f(x)T (y−x) ≤f(y)
for all x, y ∈dom f.
is given by
˜IC(x) =

0
x ∈C
∞
x̸ ∈C.
The convex function ˜IC is called the indicator function of the set C.
We can play several notational tricks with the indicator function ˜IC. For example
the problem of minimizing a function f (deﬁned on all of Rn, say) on the set C is the
same as minimizing the function f + ˜IC over all of Rn. Indeed, the function f + ˜IC
is (by our convention) f restricted to the set C.
In a similar way we can extend a concave function by deﬁning it to be −∞
outside its domain.
3.1.3
First-order conditions
Suppose f is diﬀerentiable (i.e., its gradient ∇f exists at each point in dom f,
which is open). Then f is convex if and only if dom f is convex and
f(y) ≥f(x) + ∇f(x)T (y −x)
(3.2)
holds for all x, y ∈dom f. This inequality is illustrated in ﬁgure 3.2.
The aﬃne function of y given by f(x)+∇f(x)T (y−x) is, of course, the ﬁrst-order
Taylor approximation of f near x. The inequality (3.2) states that for a convex
function, the ﬁrst-order Taylor approximation is in fact a global underestimator of
the function. Conversely, if the ﬁrst-order Taylor approximation of a function is
always a global underestimator of the function, then the function is convex.
The inequality (3.2) shows that from local information about a convex function
(i.e., its value and derivative at a point) we can derive global information (i.e., a
global underestimator of it). This is perhaps the most important property of convex
functions, and explains some of the remarkable properties of convex functions and
convex optimization problems. As one simple example, the inequality (3.2) shows
that if ∇f(x) = 0, then for all y ∈dom f, f(y) ≥f(x), i.e., x is a global minimizer
of the function f.


## Page 4

70
3
Convex functions
Strict convexity can also be characterized by a ﬁrst-order condition: f is strictly
convex if and only if dom f is convex and for x, y ∈dom f, x̸ = y, we have
f(y) > f(x) + ∇f(x)T (y −x).
(3.3)
For concave functions we have the corresponding characterization: f is concave
if and only if dom f is convex and
f(y) ≤f(x) + ∇f(x)T (y −x)
for all x, y ∈dom f.
Proof of ﬁrst-order convexity condition
To prove (3.2), we ﬁrst consider the case n = 1: We show that a diﬀerentiable
function f : R →R is convex if and only if
f(y) ≥f(x) + f ′(x)(y −x)
(3.4)
for all x and y in dom f.
Assume ﬁrst that f is convex and x, y ∈dom f. Since dom f is convex (i.e.,
an interval), we conclude that for all 0 < t ≤1, x + t(y −x) ∈dom f, and by
convexity of f,
f(x + t(y −x)) ≤(1 −t)f(x) + tf(y).
If we divide both sides by t, we obtain
f(y) ≥f(x) + f(x + t(y −x)) −f(x)
t
,
and taking the limit as t →0 yields (3.4).
To show suﬃciency, assume the function satisﬁes (3.4) for all x and y in dom f
(which is an interval). Choose any x̸ = y, and 0 ≤θ ≤1, and let z = θx + (1 −θ)y.
Applying (3.4) twice yields
f(x) ≥f(z) + f ′(z)(x −z),
f(y) ≥f(z) + f ′(z)(y −z).
Multiplying the ﬁrst inequality by θ, the second by 1 −θ, and adding them yields
θf(x) + (1 −θ)f(y) ≥f(z),
which proves that f is convex.
Now we can prove the general case, with f : Rn →R. Let x, y ∈Rn and
consider f restricted to the line passing through them, i.e., the function deﬁned by
g(t) = f(ty + (1 −t)x), so g′(t) = ∇f(ty + (1 −t)x)T (y −x).
First assume f is convex, which implies g is convex, so by the argument above
we have g(1) ≥g(0) + g′(0), which means
f(y) ≥f(x) + ∇f(x)T (y −x).
Now assume that this inequality holds for any x and y, so if ty + (1 −t)x ∈dom f
and ˜ty + (1 −˜t)x ∈dom f, we have
f(ty + (1 −t)x) ≥f(˜ty + (1 −˜t)x) + ∇f(˜ty + (1 −˜t)x)T (y −x)(t −˜t),
i.e., g(t) ≥g(˜t) + g′(˜t)(t −˜t). We have seen that this implies that g is convex.


## Page 5

3.1
Basic properties and examples
71
3.1.4
Second-order conditions
We now assume that f is twice diﬀerentiable, that is, its Hessian or second deriva-
tive ∇2f exists at each point in dom f, which is open. Then f is convex if and
only if dom f is convex and its Hessian is positive semideﬁnite: for all x ∈dom f,
∇2f(x) ⪰0.
For a function on R, this reduces to the simple condition f ′′(x) ≥0 (and dom f
convex, i.e., an interval), which means that the derivative is nondecreasing. The
condition ∇2f(x) ⪰0 can be interpreted geometrically as the requirement that the
graph of the function have positive (upward) curvature at x. We leave the proof
of the second-order condition as an exercise (exercise 3.8).
Similarly, f is concave if and only if dom f is convex and ∇2f(x) ⪯0 for
all x ∈dom f. Strict convexity can be partially characterized by second-order
conditions.
If ∇2f(x) ≻0 for all x ∈dom f, then f is strictly convex.
The
converse, however, is not true: for example, the function f : R →R given by
f(x) = x4 is strictly convex but has zero second derivative at x = 0.
Example 3.2 Quadratic functions. Consider the quadratic function f : Rn →R, with
dom f = Rn, given by
f(x) = (1/2)xT Px + qT x + r,
with P ∈Sn, q ∈Rn, and r ∈R. Since ∇2f(x) = P for all x, f is convex if and only
if P ⪰0 (and concave if and only if P ⪯0).
For quadratic functions, strict convexity is easily characterized: f is strictly convex
if and only if P ≻0 (and strictly concave if and only if P ≺0).
Remark 3.1 The separate requirement that dom f be convex cannot be dropped from
the ﬁrst- or second-order characterizations of convexity and concavity. For example,
the function f(x) = 1/x2, with dom f = {x ∈R | x̸ = 0}, satisﬁes f ′′(x) > 0 for all
x ∈dom f, but is not a convex function.
3.1.5
Examples
We have already mentioned that all linear and aﬃne functions are convex (and
concave), and have described the convex and concave quadratic functions. In this
section we give a few more examples of convex and concave functions. We start
with some functions on R, with variable x.
• Exponential. eax is convex on R, for any a ∈R.
• Powers. xa is convex on R++ when a ≥1 or a ≤0, and concave for 0 ≤a ≤1.
• Powers of absolute value. |x|p, for p ≥1, is convex on R.
• Logarithm. log x is concave on R++.


## Page 6

72
3
Convex functions
x
y
f(x, y)
−2
0
2
0
1
2
0
1
2
Figure 3.3 Graph of f(x, y) = x2/y.
• Negative entropy. x log x (either on R++, or on R+, deﬁned as 0 for x = 0)
is convex.
Convexity or concavity of these examples can be shown by verifying the ba-
sic inequality (3.1), or by checking that the second derivative is nonnegative or
nonpositive. For example, with f(x) = x log x we have
f ′(x) = log x + 1,
f ′′(x) = 1/x,
so that f ′′(x) > 0 for x > 0. This shows that the negative entropy function is
(strictly) convex.
We now give a few interesting examples of functions on Rn.
• Norms. Every norm on Rn is convex.
• Max function. f(x) = max{x1, . . . , xn} is convex on Rn.
• Quadratic-over-linear function. The function f(x, y) = x2/y, with
dom f = R × R++ = {(x, y) ∈R2 | y > 0},
is convex (ﬁgure 3.3).
• Log-sum-exp.
The function f(x) = log (ex1 + · · · + exn) is convex on Rn.
This function can be interpreted as a diﬀerentiable (in fact, analytic) approx-
imation of the max function, since
max{x1, . . . , xn} ≤f(x) ≤max{x1, . . . , xn} + log n
for all x. (The second inequality is tight when all components of x are equal.)
Figure 3.4 shows f for n = 2.


## Page 7

3.1
Basic properties and examples
73
x
y
f(x, y)
−2
0
2
−2
0
2
−2
0
2
4
Figure 3.4 Graph of f(x, y) = log(ex + ey).
• Geometric mean. The geometric mean f(x) = (Qn
i=1 xi)1/n is concave on
dom f = Rn
++.
• Log-determinant. The function f(X) = log det X is concave on dom f =
Sn
++.
Convexity (or concavity) of these examples can be veriﬁed in several ways,
such as directly verifying the inequality (3.1), verifying that the Hessian is positive
semideﬁnite, or restricting the function to an arbitrary line and verifying convexity
of the resulting function of one variable.
Norms.
If f : Rn →R is a norm, and 0 ≤θ ≤1, then
f(θx + (1 −θ)y) ≤f(θx) + f((1 −θ)y) = θf(x) + (1 −θ)f(y).
The inequality follows from the triangle inequality, and the equality follows from
homogeneity of a norm.
Max function.
The function f(x) = maxi xi satisﬁes, for 0 ≤θ ≤1,
f(θx + (1 −θ)y)
=
max
i (θxi + (1 −θ)yi)
≤
θ max
i
xi + (1 −θ) max
i
yi
=
θf(x) + (1 −θ)f(y).
Quadratic-over-linear function.
To show that the quadratic-over-linear function
f(x, y) = x2/y is convex, we note that (for y > 0),
∇2f(x, y) = 2
y3

y2
−xy
−xy
x2

= 2
y3

y
−x
 
y
−x
T
⪰0.


## Page 8

74
3
Convex functions
Log-sum-exp.
The Hessian of the log-sum-exp function is
∇2f(x) =
1
(1T z)2
 (1T z) diag(z) −zzT 
,
where z = (ex1, . . . , exn). To verify that ∇2f(x) ⪰0 we must show that for all v,
vT ∇2f(x)v ≥0, i.e.,
vT ∇2f(x)v =
1
(1T z)2


 n
X
i=1
zi
! n
X
i=1
v2
i zi
!
−
 n
X
i=1
vizi
!2
≥0.
But this follows from the Cauchy-Schwarz inequality (aT a)(bT b) ≥(aT b)2 applied
to the vectors with components ai = vi√zi, bi = √zi.
Geometric mean.
In a similar way we can show that the geometric mean f(x) =
(Qn
i=1 xi)1/n is concave on dom f = Rn
++. Its Hessian ∇2f(x) is given by
∂2f(x)
∂x2
k
= −(n −1)(Qn
i=1 xi)1/n
n2x2
k
,
∂2f(x)
∂xk∂xl
= (Qn
i=1 xi)1/n
n2xkxl
for k̸ = l,
and can be expressed as
∇2f(x) = −
Qn
i=1 x1/n
i
n2
 n diag(1/x2
1, . . . , 1/x2
n) −qqT 
where qi = 1/xi. We must show that ∇2f(x) ⪯0, i.e., that
vT ∇2f(x)v = −
Qn
i=1 x1/n
i
n2

n
n
X
i=1
v2
i /x2
i −
 n
X
i=1
vi/xi
!2
≤0
for all v. Again this follows from the Cauchy-Schwarz inequality (aT a)(bT b) ≥
(aT b)2, applied to the vectors a = 1 and bi = vi/xi.
Log-determinant.
For the function f(X) = log det X, we can verify concavity by
considering an arbitrary line, given by X = Z + tV , where Z, V ∈Sn. We deﬁne
g(t) = f(Z + tV ), and restrict g to the interval of values of t for which Z + tV ≻0.
Without loss of generality, we can assume that t = 0 is inside this interval, i.e.,
Z ≻0. We have
g(t)
=
log det(Z + tV )
=
log det(Z1/2(I + tZ−1/2V Z−1/2)Z1/2)
=
n
X
i=1
log(1 + tλi) + log det Z
where λ1, . . . , λn are the eigenvalues of Z−1/2V Z−1/2. Therefore we have
g′(t) =
n
X
i=1
λi
1 + tλi
,
g′′(t) = −
n
X
i=1
λ2
i
(1 + tλi)2 .
Since g′′(t) ≤0, we conclude that f is concave.


## Page 9

3.1
Basic properties and examples
75
3.1.6
Sublevel sets
The α-sublevel set of a function f : Rn →R is deﬁned as
Cα = {x ∈dom f | f(x) ≤α}.
Sublevel sets of a convex function are convex, for any value of α. The proof is
immediate from the deﬁnition of convexity: if x, y ∈Cα, then f(x) ≤α and
f(y) ≤α, and so f(θx+(1−θ)y) ≤α for 0 ≤θ ≤1, and hence θx+(1−θ)y ∈Cα.
The converse is not true: a function can have all its sublevel sets convex, but
not be a convex function. For example, f(x) = −ex is not convex on R (indeed, it
is strictly concave) but all its sublevel sets are convex.
If f is concave, then its α-superlevel set, given by {x ∈dom f | f(x) ≥α}, is a
convex set. The sublevel set property is often a good way to establish convexity of
a set, by expressing it as a sublevel set of a convex function, or as the superlevel
set of a concave function.
Example 3.3 The geometric and arithmetic means of x ∈Rn
+ are, respectively,
G(x) =
 n
Y
i=1
xi
!1/n
,
A(x) = 1
n
n
X
i=1
xi,
(where we take 01/n = 0 in our deﬁnition of G). The arithmetic-geometric mean
inequality states that G(x) ≤A(x).
Suppose 0 ≤α ≤1, and consider the set
{x ∈Rn
+ | G(x) ≥αA(x)},
i.e., the set of vectors with geometric mean at least as large as a factor α times the
arithmetic mean. This set is convex, since it is the 0-superlevel set of the function
G(x) −αA(x), which is concave. In fact, the set is positively homogeneous, so it is a
convex cone.
3.1.7
Epigraph
The graph of a function f : Rn →R is deﬁned as
{(x, f(x)) | x ∈dom f},
which is a subset of Rn+1. The epigraph of a function f : Rn →R is deﬁned as
epi f = {(x, t) | x ∈dom f, f(x) ≤t},
which is a subset of Rn+1. (‘Epi’ means ‘above’ so epigraph means ‘above the
graph’.) The deﬁnition is illustrated in ﬁgure 3.5.
The link between convex sets and convex functions is via the epigraph: A
function is convex if and only if its epigraph is a convex set. A function is concave
if and only if its hypograph, deﬁned as
hypo f = {(x, t) | t ≤f(x)},
is a convex set.


## Page 10

76
3
Convex functions
epi f
f
Figure 3.5 Epigraph of a function f, shown shaded. The lower boundary,
shown darker, is the graph of f.
Example 3.4 Matrix fractional function. The function f : Rn × Sn →R, deﬁned as
f(x, Y ) = xT Y −1x
is convex on dom f = Rn×Sn
++. (This generalizes the quadratic-over-linear function
f(x, y) = x2/y, with dom f = R × R++.)
One easy way to establish convexity of f is via its epigraph:
epi f
=
{(x, Y, t) | Y ≻0, xT Y −1x ≤t}
=

(x, Y, t)


Y
x
xT
t

⪰0, Y ≻0

,
using the Schur complement condition for positive semideﬁniteness of a block matrix
(see §A.5.5). The last condition is a linear matrix inequality in (x, Y, t), and therefore
epi f is convex.
For the special case n = 1, the matrix fractional function reduces to the quadratic-
over-linear function x2/y, and the associated LMI representation is

y
x
x
t

⪰0,
y > 0
(the graph of which is shown in ﬁgure 3.3).
Many results for convex functions can be proved (or interpreted) geometrically
using epigraphs, and applying results for convex sets. As an example, consider the
ﬁrst-order condition for convexity:
f(y) ≥f(x) + ∇f(x)T (y −x),
where f is convex and x, y ∈dom f.
We can interpret this basic inequality
geometrically in terms of epi f. If (y, t) ∈epi f, then
t ≥f(y) ≥f(x) + ∇f(x)T (y −x).


## Page 11

3.1
Basic properties and examples
77
epi f
(∇f(x), −1)
(x, f(x))
Figure 3.6 For a diﬀerentiable convex function f, the vector (∇f(x), −1)
deﬁnes a supporting hyperplane to the epigraph of f at x.
We can express this as:
(y, t) ∈epi f =⇒
 ∇f(x)
−1
T  y
t

−

x
f(x)

≤0.
This means that the hyperplane deﬁned by (∇f(x), −1) supports epi f at the
boundary point (x, f(x)); see ﬁgure 3.6.
3.1.8
Jensen’s inequality and extensions
The basic inequality (3.1), i.e.,
f(θx + (1 −θ)y) ≤θf(x) + (1 −θ)f(y),
is sometimes called Jensen’s inequality. It is easily extended to convex combinations
of more than two points: If f is convex, x1, . . . , xk ∈dom f, and θ1, . . . , θk ≥0
with θ1 + · · · + θk = 1, then
f(θ1x1 + · · · + θkxk) ≤θ1f(x1) + · · · + θkf(xk).
As in the case of convex sets, the inequality extends to inﬁnite sums, integrals, and
expected values. For example, if p(x) ≥0 on S ⊆dom f,
R
S p(x) dx = 1, then
f
Z
S
p(x)x dx

≤
Z
S
f(x)p(x) dx,
provided the integrals exist. In the most general case we can take any probability
measure with support in dom f. If x is a random variable such that x ∈dom f
with probability one, and f is convex, then we have
f(E x) ≤E f(x),
(3.5)
provided the expectations exist. We can recover the basic inequality (3.1) from
this general form, by taking the random variable x to have support {x1, x2}, with


## Page 12

78
3
Convex functions
prob(x = x1) = θ, prob(x = x2) = 1 −θ. Thus the inequality (3.5) characterizes
convexity: If f is not convex, there is a random variable x, with x ∈dom f with
probability one, such that f(E x) > E f(x).
All of these inequalities are now called Jensen’s inequality, even though the
inequality studied by Jensen was the very simple one
f
x + y
2

≤f(x) + f(y)
2
.
Remark 3.2 We can interpret (3.5) as follows. Suppose x ∈dom f ⊆Rn and z is
any zero mean random vector in Rn. Then we have
E f(x + z) ≥f(x).
Thus, randomization or dithering (i.e., adding a zero mean random vector to the
argument) cannot decrease the value of a convex function on average.
3.1.9
Inequalities
Many famous inequalities can be derived by applying Jensen’s inequality to some
appropriate convex function. (Indeed, convexity and Jensen’s inequality can be
made the foundation of a theory of inequalities.) As a simple example, consider
the arithmetic-geometric mean inequality:
√
ab ≤(a + b)/2
(3.6)
for a, b ≥0. The function −log x is convex; Jensen’s inequality with θ = 1/2 yields
−log
a + b
2

≤−log a −log b
2
.
Taking the exponential of both sides yields (3.6).
As a less trivial example we prove H¨older’s inequality: for p > 1, 1/p+1/q = 1,
and x, y ∈Rn,
n
X
i=1
xiyi ≤
 n
X
i=1
|xi|p
!1/p n
X
i=1
|yi|q
!1/q
.
By convexity of −log x, and Jensen’s inequality with general θ, we obtain the more
general arithmetic-geometric mean inequality
aθb1−θ ≤θa + (1 −θ)b,
valid for a, b ≥0 and 0 ≤θ ≤1. Applying this with
a =
|xi|p
Pn
j=1 |xj|p ,
b =
|yi|q
Pn
j=1 |yj|q ,
θ = 1/p,
yields
 
|xi|p
Pn
j=1 |xj|p
!1/p 
|yi|q
Pn
j=1 |yj|q
!1/q
≤
|xi|p
p Pn
j=1 |xj|p +
|yi|q
q Pn
j=1 |yj|q .
Summing over i then yields H¨older’s inequality.


## Page 13

3.2
Operations that preserve convexity
79
3.2
Operations that preserve convexity
In this section we describe some operations that preserve convexity or concavity
of functions, or allow us to construct new convex and concave functions. We start
with some simple operations such as addition, scaling, and pointwise supremum,
and then describe some more sophisticated operations (some of which include the
simple operations as special cases).
3.2.1
Nonnegative weighted sums
Evidently if f is a convex function and α ≥0, then the function αf is convex.
If f1 and f2 are both convex functions, then so is their sum f1 + f2. Combining
nonnegative scaling and addition, we see that the set of convex functions is itself a
convex cone: a nonnegative weighted sum of convex functions,
f = w1f1 + · · · + wmfm,
is convex. Similarly, a nonnegative weighted sum of concave functions is concave. A
nonnegative, nonzero weighted sum of strictly convex (concave) functions is strictly
convex (concave).
These properties extend to inﬁnite sums and integrals. For example if f(x, y)
is convex in x for each y ∈A, and w(y) ≥0 for each y ∈A, then the function g
deﬁned as
g(x) =
Z
A
w(y)f(x, y) dy
is convex in x (provided the integral exists).
The fact that convexity is preserved under nonnegative scaling and addition is
easily veriﬁed directly, or can be seen in terms of the associated epigraphs. For
example, if w ≥0 and f is convex, we have
epi(wf) =
 I
0
0
w

epi f,
which is convex because the image of a convex set under a linear mapping is convex.
3.2.2
Composition with an aﬃne mapping
Suppose f : Rn →R, A ∈Rn×m, and b ∈Rn. Deﬁne g : Rm →R by
g(x) = f(Ax + b),
with dom g = {x | Ax + b ∈dom f}. Then if f is convex, so is g; if f is concave,
so is g.


## Page 14

80
3
Convex functions
3.2.3
Pointwise maximum and supremum
If f1 and f2 are convex functions then their pointwise maximum f, deﬁned by
f(x) = max{f1(x), f2(x)},
with dom f = dom f1 ∩dom f2, is also convex. This property is easily veriﬁed: if
0 ≤θ ≤1 and x, y ∈dom f, then
f(θx + (1 −θ)y)
=
max{f1(θx + (1 −θ)y), f2(θx + (1 −θ)y)}
≤
max{θf1(x) + (1 −θ)f1(y), θf2(x) + (1 −θ)f2(y)}
≤
θ max{f1(x), f2(x)} + (1 −θ) max{f1(y), f2(y)}
=
θf(x) + (1 −θ)f(y),
which establishes convexity of f. It is easily shown that if f1, . . . , fm are convex,
then their pointwise maximum
f(x) = max{f1(x), . . . , fm(x)}
is also convex.
Example 3.5 Piecewise-linear functions. The function
f(x) = max{aT
1 x + b1, . . . , aT
Lx + bL}
deﬁnes a piecewise-linear (or really, aﬃne) function (with L or fewer regions). It is
convex since it is the pointwise maximum of aﬃne functions.
The converse can also be shown: any piecewise-linear convex function with L or fewer
regions can be expressed in this form. (See exercise 3.29.)
Example 3.6
Sum of r largest components. For x ∈Rn we denote by x[i] the ith
largest component of x, i.e.,
x[1] ≥x[2] ≥· · · ≥x[n]
are the components of x sorted in nonincreasing order. Then the function
f(x) =
r
X
i=1
x[i],
i.e., the sum of the r largest elements of x, is a convex function. This can be seen by
writing it as
f(x) =
r
X
i=1
x[i] = max{xi1 + · · · + xir | 1 ≤i1 < i2 < · · · < ir ≤n},
i.e., the maximum of all possible sums of r diﬀerent components of x. Since it is the
pointwise maximum of n!/(r!(n −r)!) linear functions, it is convex.
As an extension it can be shown that the function Pr
i=1 wix[i] is convex, provided
w1 ≥w2 ≥· · · ≥wr ≥0. (See exercise 3.19.)


## Page 15

3.2
Operations that preserve convexity
81
The pointwise maximum property extends to the pointwise supremum over an
inﬁnite set of convex functions. If for each y ∈A, f(x, y) is convex in x, then the
function g, deﬁned as
g(x) = sup
y∈A
f(x, y)
(3.7)
is convex in x. Here the domain of g is
dom g = {x | (x, y) ∈dom f for all y ∈A, sup
y∈A
f(x, y) < ∞}.
Similarly, the pointwise inﬁmum of a set of concave functions is a concave function.
In terms of epigraphs, the pointwise supremum of functions corresponds to the
intersection of epigraphs: with f, g, and A as deﬁned in (3.7), we have
epi g =
\
y∈A
epi f(·, y).
Thus, the result follows from the fact that the intersection of a family of convex
sets is convex.
Example 3.7 Support function of a set.
Let C ⊆Rn, with C̸ = ∅.
The support
function SC associated with the set C is deﬁned as
SC(x) = sup{xT y | y ∈C}
(and, naturally, dom SC = {x | supy∈C xT y < ∞}).
For each y ∈C, xT y is a linear function of x, so SC is the pointwise supremum of a
family of linear functions, hence convex.
Example 3.8 Distance to farthest point of a set. Let C ⊆Rn. The distance (in any
norm) to the farthest point of C,
f(x) = sup
y∈C
∥x −y∥,
is convex. To see this, note that for any y, the function ∥x −y∥is convex in x. Since
f is the pointwise supremum of a family of convex functions (indexed by y ∈C), it
is a convex function of x.
Example 3.9 Least-squares cost as a function of weights. Let a1, . . . , an ∈Rm. In a
weighted least-squares problem we minimize the objective function Pn
i=1 wi(aT
i x −
bi)2 over x ∈Rm. We refer to wi as weights, and allow negative wi (which opens the
possibility that the objective function is unbounded below).
We deﬁne the (optimal) weighted least-squares cost as
g(w) = inf
x
n
X
i=1
wi(aT
i x −bi)2,
with domain
dom g =
(
w
 inf
x
n
X
i=1
wi(aT
i x −bi)2 > −∞
)
.


## Page 16

82
3
Convex functions
Since g is the inﬁmum of a family of linear functions of w (indexed by x ∈Rm), it is
a concave function of w.
We can derive an explicit expression for g, at least on part of its domain.
Let
W = diag(w), the diagonal matrix with elements w1, . . . , wn, and let A ∈Rn×m
have rows aT
i , so we have
g(w) = inf
x (Ax −b)T W(Ax −b) = inf
x (xT AT WAx −2bT WAx + bT Wb).
From this we see that if AT WA̸ ⪰0, the quadratic function is unbounded below
in x, so g(w) = −∞, i.e., w̸ ∈dom g.
We can give a simple expression for g
when AT WA ≻0 (which deﬁnes a strict linear matrix inequality), by analytically
minimizing the quadratic function:
g(w)
=
bT Wb −bT WA(AT WA)−1AT Wb
=
n
X
i=1
wib2
i −
n
X
i=1
w2
i b2
i aT
i
 
n
X
j=1
wjajaT
j
!−1
ai.
Concavity of g from this expression is not immediately obvious (but does follow, for
example, from convexity of the matrix fractional function; see example 3.4).
Example 3.10
Maximum eigenvalue of a symmetric matrix. The function f(X) =
λmax(X), with dom f = Sm, is convex. To see this, we express f as
f(X) = sup{yT Xy | ∥y∥2 = 1},
i.e., as the pointwise supremum of a family of linear functions of X (i.e., yT Xy)
indexed by y ∈Rm.
Example 3.11
Norm of a matrix. Consider f(X) = ∥X∥2 with dom f = Rp×q,
where ∥· ∥2 denotes the spectral norm or maximum singular value. Convexity of f
follows from
f(X) = sup{uT Xv | ∥u∥2 = 1, ∥v∥2 = 1},
which shows it is the pointwise supremum of a family of linear functions of X.
As a generalization suppose ∥· ∥a and ∥· ∥b are norms on Rp and Rq, respectively.
The induced norm of a matrix X ∈Rp×q is deﬁned as
∥X∥a,b = sup
v̸=0
∥Xv∥a
∥v∥b .
(This reduces to the spectral norm when both norms are Euclidean.) The induced
norm can be expressed as
∥X∥a,b
=
sup{∥Xv∥a | ∥v∥b = 1}
=
sup{uT Xv | ∥u∥a∗= 1, ∥v∥b = 1},
where ∥· ∥a∗is the dual norm of ∥· ∥a, and we use the fact that
∥z∥a = sup{uT z | ∥u∥a∗= 1}.
Since we have expressed ∥X∥a,b as a supremum of linear functions of X, it is a convex
function.


## Page 17

3.2
Operations that preserve convexity
83
Representation as pointwise supremum of aﬃne functions
The examples above illustrate a good method for establishing convexity of a func-
tion: by expressing it as the pointwise supremum of a family of aﬃne functions.
Except for a technical condition, a converse holds: almost every convex function
can be expressed as the pointwise supremum of a family of aﬃne functions. For
example, if f : Rn →R is convex, with dom f = Rn, then we have
f(x) = sup{g(x) | g aﬃne, g(z) ≤f(z) for all z}.
In other words, f is the pointwise supremum of the set of all aﬃne global under-
estimators of it. We give the proof of this result below, and leave the case where
dom f̸ = Rn as an exercise (exercise 3.28).
Suppose f is convex with dom f = Rn. The inequality
f(x) ≥sup{g(x) | g aﬃne, g(z) ≤f(z) for all z}
is clear, since if g is any aﬃne underestimator of f, we have g(x) ≤f(x). To
establish equality, we will show that for each x ∈Rn, there is an aﬃne function g,
which is a global underestimator of f, and satisﬁes g(x) = f(x).
The epigraph of f is, of course, a convex set. Hence we can ﬁnd a supporting
hyperplane to it at (x, f(x)), i.e., a ∈Rn and b ∈R with (a, b)̸ = 0 and
 a
b
T 
x −z
f(x) −t

≤0
for all (z, t) ∈epi f. This means that
aT (x −z) + b(f(x) −f(z) −s) ≤0
(3.8)
for all z ∈dom f = Rn and all s ≥0 (since (z, t) ∈epi f means t = f(z) + s for
some s ≥0). For the inequality (3.8) to hold for all s ≥0, we must have b ≥0.
If b = 0, then the inequality (3.8) reduces to aT (x −z) ≤0 for all z ∈Rn, which
implies a = 0 and contradicts (a, b)̸ = 0. We conclude that b > 0, i.e., that the
supporting hyperplane is not vertical.
Using the fact that b > 0 we rewrite (3.8) for s = 0 as
g(z) = f(x) + (a/b)T (x −z) ≤f(z)
for all z. The function g is an aﬃne underestimator of f, and satisﬁes g(x) = f(x).
3.2.4
Composition
In this section we examine conditions on h : Rk →R and g : Rn →Rk that
guarantee convexity or concavity of their composition f = h ◦g : Rn →R, deﬁned
by
f(x) = h(g(x)),
dom f = {x ∈dom g | g(x) ∈dom h}.


## Page 18

84
3
Convex functions
Scalar composition
We ﬁrst consider the case k = 1, so h : R →R and g : Rn →R. We can restrict
ourselves to the case n = 1 (since convexity is determined by the behavior of a
function on arbitrary lines that intersect its domain).
To discover the composition rules, we start by assuming that h and g are twice
diﬀerentiable, with dom g = dom h = R. In this case, convexity of f reduces to
f ′′ ≥0 (meaning, f ′′(x) ≥0 for all x ∈R).
The second derivative of the composition function f = h ◦g is given by
f ′′(x) = h′′(g(x))g′(x)2 + h′(g(x))g′′(x).
(3.9)
Now suppose, for example, that g is convex (so g′′ ≥0) and h is convex and
nondecreasing (so h′′ ≥0 and h′ ≥0). It follows from (3.9) that f ′′ ≥0, i.e., f is
convex. In a similar way, the expression (3.9) gives the results:
f is convex if h is convex and nondecreasing, and g is convex,
f is convex if h is convex and nonincreasing, and g is concave,
f is concave if h is concave and nondecreasing, and g is concave,
f is concave if h is concave and nonincreasing, and g is convex.
(3.10)
These statements are valid when the functions g and h are twice diﬀerentiable and
have domains that are all of R. It turns out that very similar composition rules
hold in the general case n > 1, without assuming diﬀerentiability of h and g, or
that dom g = Rn and dom h = R:
f is convex if h is convex, ˜h is nondecreasing, and g is convex,
f is convex if h is convex, ˜h is nonincreasing, and g is concave,
f is concave if h is concave, ˜h is nondecreasing, and g is concave,
f is concave if h is concave, ˜h is nonincreasing, and g is convex.
(3.11)
Here ˜h denotes the extended-value extension of the function h, which assigns the
value ∞(−∞) to points not in dom h for h convex (concave). The only diﬀerence
between these results, and the results in (3.10), is that we require that the extended-
value extension function ˜h be nonincreasing or nondecreasing, on all of R.
To understand what this means, suppose h is convex, so ˜h takes on the value ∞
outside dom h. To say that ˜h is nondecreasing means that for any x, y ∈R, with
x < y, we have ˜h(x) ≤˜h(y). In particular, this means that if y ∈dom h, then x ∈
dom h. In other words, the domain of h extends inﬁnitely in the negative direction;
it is either R, or an interval of the form (−∞, a) or (−∞, a]. In a similar way, to
say that h is convex and ˜h is nonincreasing means that h is nonincreasing and
dom h extends inﬁnitely in the positive direction. This is illustrated in ﬁgure 3.7.
Example 3.12 Some simple examples will illustrate the conditions on h that appear
in the composition theorems.
• The function h(x) = log x, with dom h = R++, is concave and satisﬁes ˜h
nondecreasing.


## Page 19

3.2
Operations that preserve convexity
85
x
epi f
0
1
0
1
x
epi f
0
1
0
1
Figure 3.7 Left. The function x2, with domain R+, is convex and nonde-
creasing on its domain, but its extended-value extension is not nondecreas-
ing. Right. The function max{x, 0}2, with domain R, is convex, and its
extended-value extension is nondecreasing.
• The function h(x) = x1/2, with dom h = R+, is concave and satisﬁes the
condition ˜h nondecreasing.
• The function h(x) = x3/2, with dom h = R+, is convex but does not satisfy the
condition ˜h nondecreasing. For example, we have ˜h(−1) = ∞, but ˜h(1) = 1.
• The function h(x) = x3/2 for x ≥0, and h(x) = 0 for x < 0, with dom h = R,
is convex and does satisfy the condition ˜h nondecreasing.
The composition results (3.11) can be proved directly, without assuming dif-
ferentiability, or using the formula (3.9). As an example, we will prove the fol-
lowing composition theorem: if g is convex, h is convex, and ˜h is nondecreasing,
then f = h ◦g is convex. Assume that x, y ∈dom f, and 0 ≤θ ≤1. Since
x, y ∈dom f, we have that x, y ∈dom g and g(x), g(y) ∈dom h. Since dom g
is convex, we conclude that θx + (1 −θ)y ∈dom g, and from convexity of g, we
have
g(θx + (1 −θ)y) ≤θg(x) + (1 −θ)g(y).
(3.12)
Since g(x), g(y) ∈dom h, we conclude that θg(x) + (1 −θ)g(y) ∈dom h, i.e.,
the righthand side of (3.12) is in dom h.
Now we use the assumption that ˜h
is nondecreasing, which means that its domain extends inﬁnitely in the negative
direction. Since the righthand side of (3.12) is in dom h, we conclude that the
lefthand side, i.e., g(θx+(1−θ)y) ∈dom h. This means that θx+(1−θ)y ∈dom f.
At this point, we have shown that dom f is convex.
Now using the fact that ˜h is nondecreasing and the inequality (3.12), we get
h(g(θx + (1 −θ)y)) ≤h(θg(x) + (1 −θ)g(y)).
(3.13)
From convexity of h, we have
h(θg(x) + (1 −θ)g(y)) ≤θh(g(x)) + (1 −θ)h(g(y)).
(3.14)


## Page 20

86
3
Convex functions
Putting (3.13) and (3.14) together, we have
h(g(θx + (1 −θ)y)) ≤θh(g(x)) + (1 −θ)h(g(y)).
which proves the composition theorem.
Example 3.13 Simple composition results.
• If g is convex then exp g(x) is convex.
• If g is concave and positive, then log g(x) is concave.
• If g is concave and positive, then 1/g(x) is convex.
• If g is convex and nonnegative and p ≥1, then g(x)p is convex.
• If g is convex then −log(−g(x)) is convex on {x | g(x) < 0}.
Remark 3.3 The requirement that monotonicity hold for the extended-value extension
˜h, and not just the function h, cannot be removed. For example, consider the function
g(x) = x2, with dom g = R, and h(x) = 0, with dom h = [1, 2]. Here g is convex,
and h is convex and nondecreasing. But the function f = h ◦g, given by
f(x) = 0,
dom f = [−
√
2, −1] ∪[1,
√
2],
is not convex, since its domain is not convex. Here, of course, the function ˜h is not
nondecreasing.
Vector composition
We now turn to the more complicated case when k ≥1. Suppose
f(x) = h(g(x)) = h(g1(x), . . . , gk(x)),
with h : Rk →R, gi : Rn →R. Again without loss of generality we can assume n =
1. As in the case k = 1, we start by assuming the functions are twice diﬀerentiable,
with dom g = R and dom h = Rk, in order to discover the composition rules. We
have
f ′′(x) = g′(x)T ∇2h(g(x))g′(x) + ∇h(g(x))T g′′(x),
(3.15)
which is the vector analog of (3.9). Again the issue is to determine conditions under
which f ′′(x) ≥0 for all x (or f ′′(x) ≤0 for all x for concavity). From (3.15) we
can derive many rules, for example:
f is convex if h is convex, h is nondecreasing in each argument,
and gi are convex,
f is convex if h is convex, h is nonincreasing in each argument,
and gi are concave,
f is concave if h is concave, h is nondecreasing in each argument,
and gi are concave.


## Page 21

3.2
Operations that preserve convexity
87
As in the scalar case, similar composition results hold in general, with n > 1, no as-
sumption of diﬀerentiability of h or g, and general domains. For the general results,
the monotonicity condition on h must hold for the extended-value extension ˜h.
To understand the meaning of the condition that the extended-value exten-
sion ˜h be monotonic, we consider the case where h : Rk →R is convex, and ˜h
nondecreasing, i.e., whenever u ⪯v, we have ˜h(u) ≤˜h(v). This implies that if
v ∈dom h, then so is u: the domain of h must extend inﬁnitely in the −Rk
+
directions. We can express this compactly as dom h −Rk
+ = dom h.
Example 3.14 Vector composition examples.
• Let h(z) = z[1] +· · ·+z[r], the sum of the r largest components of z ∈Rk. Then
h is convex and nondecreasing in each argument. Suppose g1, . . . , gk are convex
functions on Rn. Then the composition function f = h ◦g, i.e., the pointwise
sum of the r largest gi’s, is convex.
• The function h(z) = log(Pk
i=1 ezi) is convex and nondecreasing in each argu-
ment, so log(Pk
i=1 egi) is convex whenever gi are.
• For 0 < p ≤1, the function h(z) = (Pk
i=1 zp
i )1/p on Rk
+ is concave, and
its extension (which has the value −∞for z̸ ⪰0) is nondecreasing in each
component. So if gi are concave and nonnegative, we conclude that f(x) =
(Pk
i=1 gi(x)p)1/p is concave.
• Suppose p ≥1, and g1, . . . , gk are convex and nonnegative. Then the function
(Pk
i=1 gi(x)p)1/p is convex.
To show this, we consider the function h : Rk →R deﬁned as
h(z) =
 
k
X
i=1
max{zi, 0}p
!1/p
,
with dom h = Rk, so h = ˜h. This function is convex, and nondecreasing, so
we conclude h(g(x)) is a convex function of x.
For z ⪰0, we have h(z) =
(Pk
i=1 zp
i )1/p, so our conclusion is that (Pk
i=1 gi(x)p)1/p is convex.
• The geometric mean h(z) = (Qk
i=1 zi)1/k on Rk
+ is concave and its extension
is nondecreasing in each argument. It follows that if g1, . . . , gk are nonnegative
concave functions, then so is their geometric mean, (Qk
i=1 gi)1/k.
3.2.5
Minimization
We have seen that the maximum or supremum of an arbitrary family of convex
functions is convex. It turns out that some special forms of minimization also yield
convex functions. If f is convex in (x, y), and C is a convex nonempty set, then
the function
g(x) = inf
y∈C f(x, y)
(3.16)


## Page 22

88
3
Convex functions
is convex in x, provided g(x) > −∞for all x. The domain of g is the projection of
dom f on its x-coordinates, i.e.,
dom g = {x | (x, y) ∈dom f for some y ∈C}.
We prove this by verifying Jensen’s inequality for x1, x2 ∈dom g. Let ǫ > 0.
Then there are y1, y2 ∈C such that f(xi, yi) ≤g(xi) + ǫ for i = 1, 2. Now let
θ ∈[0, 1]. We have
g(θx1 + (1 −θ)x2)
=
inf
y∈C f(θx1 + (1 −θ)x2, y)
≤
f(θx1 + (1 −θ)x2, θy1 + (1 −θ)y2)
≤
θf(x1, y1) + (1 −θ)f(x2, y2)
≤
θg(x1) + (1 −θ)g(x2) + ǫ.
Since this holds for any ǫ > 0, we have
g(θx1 + (1 −θ)x2) ≤θg(x1) + (1 −θ)g(x2).
The result can also be seen in terms of epigraphs. With f, g, and C deﬁned as
in (3.16), and assuming the inﬁmum over y ∈C is attained for each x, we have
epi g = {(x, t) | (x, y, t) ∈epi f for some y ∈C}.
Thus epi g is convex, since it is the projection of a convex set on some of its
components.
Example 3.15 Schur complement. Suppose the quadratic function
f(x, y) = xT Ax + 2xT By + yT Cy,
(where A and C are symmetric) is convex in (x, y), which means

A
B
BT
C

⪰0.
We can express g(x) = infy f(x, y) as
g(x) = xT (A −BC†BT )x,
where C† is the pseudo-inverse of C (see §A.5.4). By the minimization rule, g is
convex, so we conclude that A −BC†BT ⪰0.
If C is invertible, i.e., C ≻0, then the matrix A −BC−1BT is called the Schur
complement of C in the matrix

A
B
BT
C

(see §A.5.5).
Example 3.16 Distance to a set. The distance of a point x to a set S ⊆Rn, in the
norm ∥· ∥, is deﬁned as
dist(x, S) = inf
y∈S ∥x −y∥.
The function ∥x−y∥is convex in (x, y), so if the set S is convex, the distance function
dist(x, S) is a convex function of x.


## Page 23

3.2
Operations that preserve convexity
89
Example 3.17 Suppose h is convex. Then the function g deﬁned as
g(x) = inf{h(y) | Ay = x}
is convex. To see this, we deﬁne f by
f(x, y) =

h(y)
if Ay = x
∞
otherwise,
which is convex in (x, y). Then g is the minimum of f over y, and hence is convex.
(It is not hard to show directly that g is convex.)
3.2.6
Perspective of a function
If f : Rn →R, then the perspective of f is the function g : Rn+1 →R deﬁned by
g(x, t) = tf(x/t),
with domain
dom g = {(x, t) | x/t ∈dom f, t > 0}.
The perspective operation preserves convexity: If f is a convex function, then so
is its perspective function g. Similarly, if f is concave, then so is g.
This can be proved several ways, for example, direct veriﬁcation of the deﬁning
inequality (see exercise 3.33). We give a short proof here using epigraphs and the
perspective mapping on Rn+1 described in §2.3.3 (which will also explain the name
‘perspective’). For t > 0 we have
(x, t, s) ∈epi g
⇐⇒
tf(x/t) ≤s
⇐⇒
f(x/t) ≤s/t
⇐⇒
(x/t, s/t) ∈epi f.
Therefore epi g is the inverse image of epi f under the perspective mapping that
takes (u, v, w) to (u, w)/v. It follows (see §2.3.3) that epi g is convex, so the function
g is convex.
Example 3.18
Euclidean norm squared.
The perspective of the convex function
f(x) = xT x on Rn is
g(x, t) = t(x/t)T (x/t) = xT x
t
,
which is convex in (x, t) for t > 0.
We can deduce convexity of g using several other methods. First, we can express g as
the sum of the quadratic-over-linear functions x2
i /t, which were shown to be convex
in §3.1.5. We can also express g as a special case of the matrix fractional function
xT (tI)−1x (see example 3.4).


## Page 24

90
3
Convex functions
Example 3.19 Negative logarithm. Consider the convex function f(x) = −log x on
R++. Its perspective is
g(x, t) = −t log(x/t) = t log(t/x) = t log t −t log x,
and is convex on R2
++. The function g is called the relative entropy of t and x. For
x = 1, g reduces to the negative entropy function.
From convexity of g we can establish convexity or concavity of several interesting
related functions. First, the relative entropy of two vectors u, v ∈Rn
++, deﬁned as
n
X
i=1
ui log(ui/vi),
is convex in (u, v), since it is a sum of relative entropies of ui, vi.
A closely related function is the Kullback-Leibler divergence between u, v ∈Rn
++,
given by
Dkl(u, v) =
n
X
i=1
(ui log(ui/vi) −ui + vi) ,
(3.17)
which is convex, since it is the relative entropy plus a linear function of (u, v). The
Kullback-Leibler divergence satisﬁes Dkl(u, v) ≥0, and Dkl(u, v) = 0 if and only if
u = v, and so can be used as a measure of deviation between two positive vectors; see
exercise 3.13. (Note that the relative entropy and the Kullback-Leibler divergence
are the same when u and v are probability vectors, i.e., satisfy 1T u = 1T v = 1.)
If we take vi = 1T u in the relative entropy function, we obtain the concave (and
homogeneous) function of u ∈Rn
++ given by
n
X
i=1
ui log(1T u/ui) = (1T u)
n
X
i=1
zi log(1/zi),
where z = u/(1T u), which is called the normalized entropy function. The vector
z = u/1T u is a normalized vector or probability distribution, since its components
sum to one; the normalized entropy of u is 1T u times the entropy of this normalized
distribution.
Example 3.20
Suppose f : Rm →R is convex, and A ∈Rm×n, b ∈Rm, c ∈Rn,
and d ∈R. We deﬁne
g(x) = (cT x + d)f  (Ax + b)/(cT x + d)
,
with
dom g = {x | cT x + d > 0, (Ax + b)/(cT x + d) ∈dom f}.
Then g is convex.
3.3
The conjugate function
In this section we introduce an operation that will play an important role in later
chapters.


## Page 25

3.3
The conjugate function
91
f(x)
(0, −f ∗(y))
xy
x
Figure 3.8 A function f : R →R, and a value y ∈R.
The conjugate
function f ∗(y) is the maximum gap between the linear function yx and
f(x), as shown by the dashed line in the ﬁgure. If f is diﬀerentiable, this
occurs at a point x where f ′(x) = y.
3.3.1
Deﬁnition and examples
Let f : Rn →R. The function f ∗: Rn →R, deﬁned as
f ∗(y) =
sup
x∈dom f
 yT x −f(x)

,
(3.18)
is called the conjugate of the function f. The domain of the conjugate function
consists of y ∈Rn for which the supremum is ﬁnite, i.e., for which the diﬀerence
yT x −f(x) is bounded above on dom f. This deﬁnition is illustrated in ﬁgure 3.8.
We see immediately that f ∗is a convex function, since it is the pointwise
supremum of a family of convex (indeed, aﬃne) functions of y. This is true whether
or not f is convex. (Note that when f is convex, the subscript x ∈dom f is not
necessary since, by convention, yT x −f(x) = −∞for x̸ ∈dom f.)
We start with some simple examples, and then describe some rules for conjugat-
ing functions. This allows us to derive an analytical expression for the conjugate
of many common convex functions.
Example 3.21 We derive the conjugates of some convex functions on R.
• Aﬃne function. f(x) = ax + b. As a function of x, yx −ax −b is bounded if
and only if y = a, in which case it is constant. Therefore the domain of the
conjugate function f ∗is the singleton {a}, and f ∗(a) = −b.
• Negative logarithm. f(x) = −log x, with dom f = R++. The function xy+log x
is unbounded above if y ≥0 and reaches its maximum at x = −1/y otherwise.
Therefore, dom f ∗= {y | y < 0} = −R++ and f ∗(y) = −log(−y)−1 for y < 0.
• Exponential. f(x) = ex. xy −ex is unbounded if y < 0. For y > 0, xy −ex
reaches its maximum at x = log y, so we have f ∗(y) = y log y −y. For y = 0,


## Page 26

92
3
Convex functions
f ∗(y) = supx −ex = 0. In summary, dom f ∗= R+ and f ∗(y) = y log y −y
(with the interpretation 0 log 0 = 0).
• Negative entropy.
f(x) = x log x, with dom f = R+ (and f(0) = 0).
The
function xy −x log x is bounded above on R+ for all y, hence dom f ∗= R. It
attains its maximum at x = ey−1, and substituting we ﬁnd f ∗(y) = ey−1.
• Inverse. f(x) = 1/x on R++. For y > 0, yx −1/x is unbounded above. For
y = 0 this function has supremum 0; for y < 0 the supremum is attained at
x = (−y)−1/2. Therefore we have f ∗(y) = −2(−y)1/2, with dom f ∗= −R+.
Example 3.22
Strictly convex quadratic function. Consider f(x) =
1
2xT Qx, with
Q ∈Sn
++. The function yT x −1
2xT Qx is bounded above as a function of x for all y.
It attains its maximum at x = Q−1y, so
f ∗(y) = 1
2yT Q−1y.
Example 3.23
Log-determinant.
We consider f(X) = log det X−1 on Sn
++.
The
conjugate function is deﬁned as
f ∗(Y ) = sup
X≻0
(tr(Y X) + log det X) ,
since tr(Y X) is the standard inner product on Sn. We ﬁrst show that tr(Y X) +
log det X is unbounded above unless Y ≺0. If Y̸ ≺0, then Y has an eigenvector v,
with ∥v∥2 = 1, and eigenvalue λ ≥0. Taking X = I + tvvT we ﬁnd that
tr(Y X) + log det X = tr Y + tλ + log det(I + tvvT ) = tr Y + tλ + log(1 + t),
which is unbounded above as t →∞.
Now consider the case Y ≺0. We can ﬁnd the maximizing X by setting the gradient
with respect to X equal to zero:
∇X (tr(Y X) + log det X) = Y + X−1 = 0
(see §A.4.1), which yields X = −Y −1 (which is, indeed, positive deﬁnite). Therefore
we have
f ∗(Y ) = log det(−Y )−1 −n,
with dom f ∗= −Sn
++.
Example 3.24 Indicator function. Let IS be the indicator function of a (not neces-
sarily convex) set S ⊆Rn, i.e., IS(x) = 0 on dom IS = S. Its conjugate is
I∗
S(y) = sup
x∈S
yT x,
which is the support function of the set S.


## Page 27

3.3
The conjugate function
93
Example 3.25
Log-sum-exp function. To derive the conjugate of the log-sum-exp
function f(x) = log(Pn
i=1 exi), we ﬁrst determine the values of y for which the
maximum over x of yT x −f(x) is attained. By setting the gradient with respect to
x equal to zero, we obtain the condition
yi =
exi
Pn
j=1 exj ,
i = 1, . . . , n.
These equations are solvable for x if and only if y ≻0 and 1T y = 1. By substituting
the expression for yi into yT x−f(x) we obtain f ∗(y) = Pn
i=1 yi log yi. This expression
for f ∗is still correct if some components of y are zero, as long as y ⪰0 and 1T y = 1,
and we interpret 0 log 0 as 0.
In fact the domain of f ∗is exactly given by 1T y = 1, y ⪰0. To show this, suppose
that a component of y is negative, say, yk < 0. Then we can show that yT x −f(x) is
unbounded above by choosing xk = −t, and xi = 0, i̸ = k, and letting t go to inﬁnity.
If y ⪰0 but 1T y̸ = 1, we choose x = t1, so that
yT x −f(x) = t1T y −t −log n.
If 1T y > 1, this grows unboundedly as t →∞; if 1T y < 1, it grows unboundedly as
t →−∞.
In summary,
f ∗(y) =
 Pn
i=1 yi log yi
if y ⪰0 and 1T y = 1
∞
otherwise.
In other words, the conjugate of the log-sum-exp function is the negative entropy
function, restricted to the probability simplex.
Example 3.26 Norm.
Let ∥· ∥be a norm on Rn, with dual norm ∥· ∥∗. We will
show that the conjugate of f(x) = ∥x∥is
f ∗(y) =

0
∥y∥∗≤1
∞
otherwise,
i.e., the conjugate of a norm is the indicator function of the dual norm unit ball.
If ∥y∥∗> 1, then by deﬁnition of the dual norm, there is a z ∈Rn with ∥z∥≤1 and
yT z > 1. Taking x = tz and letting t →∞, we have
yT x −∥x∥= t(yT z −∥z∥) →∞,
which shows that f ∗(y) = ∞. Conversely, if ∥y∥∗≤1, then we have yT x ≤∥x∥∥y∥∗
for all x, which implies for all x, yT x −∥x∥≤0. Therefore x = 0 is the value that
maximizes yT x −∥x∥, with maximum value 0.
Example 3.27 Norm squared. Now consider the function f(x) = (1/2)∥x∥2, where ∥·∥
is a norm, with dual norm ∥·∥∗. We will show that its conjugate is f ∗(y) = (1/2)∥y∥2
∗.
From yT x ≤∥y∥∗∥x∥, we conclude
yT x −(1/2)∥x∥2 ≤∥y∥∗∥x∥−(1/2)∥x∥2


## Page 28

94
3
Convex functions
for all x. The righthand side is a quadratic function of ∥x∥, which has maximum
value (1/2)∥y∥2
∗. Therefore for all x, we have
yT x −(1/2)∥x∥2 ≤(1/2)∥y∥2
∗,
which shows that f ∗(y) ≤(1/2)∥y∥2
∗.
To show the other inequality, let x be any vector with yT x = ∥y∥∗∥x∥, scaled so that
∥x∥= ∥y∥∗. Then we have, for this x,
yT x −(1/2)∥x∥2 = (1/2)∥y∥2
∗,
which shows that f ∗(y) ≥(1/2)∥y∥2
∗.
Example 3.28 Revenue and proﬁt functions. We consider a business or enterprise that
consumes n resources and produces a product that can be sold. We let r = (r1, . . . , rn)
denote the vector of resource quantities consumed, and S(r) denote the sales revenue
derived from the product produced (as a function of the resources consumed). Now
let pi denote the price (per unit) of resource i, so the total amount paid for resources
by the enterprise is pT r. The proﬁt derived by the ﬁrm is then S(r) −pT r. Let us ﬁx
the prices of the resources, and ask what is the maximum proﬁt that can be made, by
wisely choosing the quantities of resources consumed. This maximum proﬁt is given
by
M(p) = sup
r
 S(r) −pT r
.
The function M(p) gives the maximum proﬁt attainable, as a function of the resource
prices. In terms of conjugate functions, we can express M as
M(p) = (−S)∗(−p).
Thus the maximum proﬁt (as a function of resource prices) is closely related to the
conjugate of gross sales (as a function of resources consumed).
3.3.2
Basic properties
Fenchel’s inequality
From the deﬁnition of conjugate function, we immediately obtain the inequality
f(x) + f ∗(y) ≥xT y
for all x, y. This is called Fenchel’s inequality (or Young’s inequality when f is
diﬀerentiable).
For example with f(x) = (1/2)xT Qx, where Q ∈Sn
++, we obtain the inequality
xT y ≤(1/2)xT Qx + (1/2)yT Q−1y.
Conjugate of the conjugate
The examples above, and the name ‘conjugate’, suggest that the conjugate of the
conjugate of a convex function is the original function. This is the case provided a
technical condition holds: if f is convex, and f is closed (i.e., epi f is a closed set;
see §A.3.3), then f ∗∗= f. For example, if dom f = Rn, then we have f ∗∗= f,
i.e., the conjugate of the conjugate of f is f again (see exercise 3.39).


## Page 29

3.4
Quasiconvex functions
95
Diﬀerentiable functions
The conjugate of a diﬀerentiable function f is also called the Legendre transform
of f. (To distinguish the general deﬁnition from the diﬀerentiable case, the term
Fenchel conjugate is sometimes used instead of conjugate.)
Suppose f is convex and diﬀerentiable, with dom f = Rn. Any maximizer x∗
of yT x −f(x) satisﬁes y = ∇f(x∗), and conversely, if x∗satisﬁes y = ∇f(x∗), then
x∗maximizes yT x −f(x). Therefore, if y = ∇f(x∗), we have
f ∗(y) = x∗T ∇f(x∗) −f(x∗).
This allows us to determine f ∗(y) for any y for which we can solve the gradient
equation y = ∇f(z) for z.
We can express this another way. Let z ∈Rn be arbitrary and deﬁne y = ∇f(z).
Then we have
f ∗(y) = zT ∇f(z) −f(z).
Scaling and composition with aﬃne transformation
For a > 0 and b ∈R, the conjugate of g(x) = af(x) + b is g∗(y) = af ∗(y/a) −b.
Suppose A ∈Rn×n is nonsingular and b ∈Rn. Then the conjugate of g(x) =
f(Ax + b) is
g∗(y) = f ∗(A−T y) −bT A−T y,
with dom g∗= AT dom f ∗.
Sums of independent functions
If f(u, v) = f1(u) + f2(v), where f1 and f2 are convex functions with conjugates
f ∗
1 and f ∗
2 , respectively, then
f ∗(w, z) = f ∗
1 (w) + f ∗
2 (z).
In other words, the conjugate of the sum of independent convex functions is the sum
of the conjugates. (‘Independent’ means they are functions of diﬀerent variables.)
3.4
Quasiconvex functions
3.4.1
Deﬁnition and examples
A function f : Rn →R is called quasiconvex (or unimodal) if its domain and all
its sublevel sets
Sα = {x ∈dom f | f(x) ≤α},
for α ∈R, are convex. A function is quasiconcave if −f is quasiconvex, i.e., every
superlevel set {x | f(x) ≥α} is convex. A function that is both quasiconvex and
quasiconcave is called quasilinear. If a function f is quasilinear, then its domain,
and every level set {x | f(x) = α} is convex.


## Page 30

96
3
Convex functions
α
β
a
b
c
Figure 3.9 A quasiconvex function on R. For each α, the α-sublevel set Sα
is convex, i.e., an interval. The sublevel set Sα is the interval [a, b]. The
sublevel set Sβ is the interval (−∞, c].
For a function on R, quasiconvexity requires that each sublevel set be an interval
(including, possibly, an inﬁnite interval). An example of a quasiconvex function on
R is shown in ﬁgure 3.9.
Convex functions have convex sublevel sets, and so are quasiconvex. But simple
examples, such as the one shown in ﬁgure 3.9, show that the converse is not true.
Example 3.29 Some examples on R:
• Logarithm. log x on R++ is quasiconvex (and quasiconcave, hence quasilinear).
• Ceiling function. ceil(x) = inf{z ∈Z | z ≥x} is quasiconvex (and quasicon-
cave).
These examples show that quasiconvex functions can be concave, or discontinuous.
We now give some examples on Rn.
Example 3.30
Length of a vector. We deﬁne the length of x ∈Rn as the largest
index of a nonzero component, i.e.,
f(x) = max{i | xi̸ = 0}.
(We deﬁne the length of the zero vector to be zero.) This function is quasiconvex on
Rn, since its sublevel sets are subspaces:
f(x) ≤α ⇐⇒xi = 0 for i = ⌊α⌋+ 1, . . . , n.
Example 3.31 Consider f : R2 →R, with dom f = R2
+ and f(x1, x2) = x1x2. This
function is neither convex nor concave since its Hessian
∇2f(x) =

0
1
1
0



## Page 31

3.4
Quasiconvex functions
97
is indeﬁnite; it has one positive and one negative eigenvalue.
The function f is
quasiconcave, however, since the superlevel sets
{x ∈R2
+ | x1x2 ≥α}
are convex sets for all α. (Note, however, that f is not quasiconcave on R2.)
Example 3.32 Linear-fractional function. The function
f(x) = aT x + b
cT x + d,
with dom f = {x | cT x + d > 0}, is quasiconvex, and quasiconcave, i.e., quasilinear.
Its α-sublevel set is
Sα
=
{x | cT x + d > 0, (aT x + b)/(cT x + d) ≤α}
=
{x | cT x + d > 0, aT x + b ≤α(cT x + d)},
which is convex, since it is the intersection of an open halfspace and a closed halfspace.
(The same method can be used to show its superlevel sets are convex.)
Example 3.33 Distance ratio function. Suppose a, b ∈Rn, and deﬁne
f(x) = ∥x −a∥2
∥x −b∥2 ,
i.e., the ratio of the Euclidean distance to a to the distance to b. Then f is quasiconvex
on the halfspace {x | ∥x −a∥2 ≤∥x −b∥2}. To see this, we consider the α-sublevel
set of f, with α ≤1 since f(x) ≤1 on the halfspace {x | ∥x −a∥2 ≤∥x −b∥2}. This
sublevel set is the set of points satisfying
∥x −a∥2 ≤α∥x −b∥2.
Squaring both sides, and rearranging terms, we see that this is equivalent to
(1 −α2)xT x −2(a −α2b)T x + aT a −α2bT b ≤0.
This describes a convex set (in fact a Euclidean ball) if α ≤1.
Example 3.34
Internal rate of return. Let x = (x0, x1, . . . , xn) denote a cash ﬂow
sequence over n periods, where xi > 0 means a payment to us in period i, and xi < 0
means a payment by us in period i. We deﬁne the present value of a cash ﬂow, with
interest rate r ≥0, to be
PV(x, r) =
n
X
i=0
(1 + r)−ixi.
(The factor (1 + r)−i is a discount factor for a payment by or to us in period i.)
Now we consider cash ﬂows for which x0 < 0 and x0 + x1 + · · · + xn > 0. This
means that we start with an investment of |x0| in period 0, and that the total of the


## Page 32

98
3
Convex functions
remaining cash ﬂow, x1 + · · · + xn, (not taking any discount factors into account)
exceeds our initial investment.
For such a cash ﬂow, PV(x, 0) > 0 and PV(x, r) →x0 < 0 as r →∞, so it follows
that for at least one r ≥0, we have PV(x, r) = 0. We deﬁne the internal rate of
return of the cash ﬂow as the smallest interest rate r ≥0 for which the present value
is zero:
IRR(x) = inf{r ≥0 | PV(x, r) = 0}.
Internal rate of return is a quasiconcave function of x (restricted to x0 < 0, x1 +· · ·+
xn > 0). To see this, we note that
IRR(x) ≥R ⇐⇒PV(x, r) > 0 for 0 ≤r < R.
The lefthand side deﬁnes the R-superlevel set of IRR.
The righthand side is the
intersection of the sets {x | PV(x, r) > 0}, indexed by r, over the range 0 ≤r < R.
For each r, PV(x, r) > 0 deﬁnes an open halfspace, so the righthand side deﬁnes a
convex set.
3.4.2
Basic properties
The examples above show that quasiconvexity is a considerable generalization of
convexity. Still, many of the properties of convex functions hold, or have analogs,
for quasiconvex functions. For example, there is a variation on Jensen’s inequality
that characterizes quasiconvexity: A function f is quasiconvex if and only if dom f
is convex and for any x, y ∈dom f and 0 ≤θ ≤1,
f(θx + (1 −θ)y) ≤max{f(x), f(y)},
(3.19)
i.e., the value of the function on a segment does not exceed the maximum of
its values at the endpoints.
The inequality (3.19) is sometimes called Jensen’s
inequality for quasiconvex functions, and is illustrated in ﬁgure 3.10.
Example 3.35
Cardinality of a nonnegative vector.
The cardinality or size of a
vector x ∈Rn is the number of nonzero components, and denoted card(x). The
function card is quasiconcave on Rn
+ (but not Rn). This follows immediately from
the modiﬁed Jensen inequality
card(x + y) ≥min{card(x), card(y)},
which holds for x, y ⪰0.
Example 3.36 Rank of positive semideﬁnite matrix. The function rank X is quasi-
concave on Sn
+. This follows from the modiﬁed Jensen inequality (3.19),
rank(X + Y ) ≥min{rank X, rank Y }
which holds for X, Y ∈Sn
+. (This can be considered an extension of the previous
example, since rank(diag(x)) = card(x) for x ⪰0.)


## Page 33

3.4
Quasiconvex functions
99
(x, f(x))
(y, f(y))
max{f(x), f(y)}
Figure 3.10 A quasiconvex function on R. The value of f between x and y
is no more than max{f(x), f(y)}.
Like convexity, quasiconvexity is characterized by the behavior of a function f
on lines: f is quasiconvex if and only if its restriction to any line intersecting its
domain is quasiconvex. In particular, quasiconvexity of a function can be veriﬁed by
restricting it to an arbitrary line, and then checking quasiconvexity of the resulting
function on R.
Quasiconvex functions on R
We can give a simple characterization of quasiconvex functions on R. We consider
continuous functions, since stating the conditions in the general case is cumbersome.
A continuous function f : R →R is quasiconvex if and only if at least one of the
following conditions holds:
• f is nondecreasing
• f is nonincreasing
• there is a point c ∈dom f such that for t ≤c (and t ∈dom f), f is
nonincreasing, and for t ≥c (and t ∈dom f), f is nondecreasing.
The point c can be chosen as any point which is a global minimizer of f. Figure 3.11
illustrates this.
3.4.3
Diﬀerentiable quasiconvex functions
First-order conditions
Suppose f : Rn →R is diﬀerentiable. Then f is quasiconvex if and only if dom f
is convex and for all x, y ∈dom f
f(y) ≤f(x) =⇒∇f(x)T (y −x) ≤0.
(3.20)


## Page 34

100
3
Convex functions
c
t
Figure 3.11 A quasiconvex function on R. The function is nonincreasing for
t ≤c and nondecreasing for t ≥c.
x
∇f(x)
Figure 3.12 Three level curves of a quasiconvex function f are shown. The
vector ∇f(x) deﬁnes a supporting hyperplane to the sublevel set {z | f(z) ≤
f(x)} at x.
This is the analog of inequality (3.2), for quasiconvex functions. We leave the proof
as an exercise (exercise 3.43).
The condition (3.20) has a simple geometric interpretation when ∇f(x)̸ = 0. It
states that ∇f(x) deﬁnes a supporting hyperplane to the sublevel set {y | f(y) ≤
f(x)}, at the point x, as illustrated in ﬁgure 3.12.
While the ﬁrst-order condition for convexity (3.2), and the ﬁrst-order condition
for quasiconvexity (3.20) are similar, there are some important diﬀerences. For
example, if f is convex and ∇f(x) = 0, then x is a global minimizer of f. But this
statement is false for quasiconvex functions: it is possible that ∇f(x) = 0, but x
is not a global minimizer of f.


## Page 35

3.4
Quasiconvex functions
101
Second-order conditions
Now suppose f is twice diﬀerentiable. If f is quasiconvex, then for all x ∈dom f,
and all y ∈Rn, we have
yT ∇f(x) = 0 =⇒yT ∇2f(x)y ≥0.
(3.21)
For a quasiconvex function on R, this reduces to the simple condition
f ′(x) = 0 =⇒f ′′(x) ≥0,
i.e., at any point with zero slope, the second derivative is nonnegative.
For a
quasiconvex function on Rn, the interpretation of the condition (3.21) is a bit
more complicated. As in the case n = 1, we conclude that whenever ∇f(x) = 0,
we must have ∇2f(x) ⪰0. When ∇f(x)̸ = 0, the condition (3.21) means that
∇2f(x) is positive semideﬁnite on the (n −1)-dimensional subspace ∇f(x)⊥. This
implies that ∇2f(x) can have at most one negative eigenvalue.
As a (partial) converse, if f satisﬁes
yT ∇f(x) = 0 =⇒yT ∇2f(x)y > 0
(3.22)
for all x ∈dom f and all y ∈Rn, y̸ = 0, then f is quasiconvex. This condition is
the same as requiring ∇2f(x) to be positive deﬁnite for any point with ∇f(x) = 0,
and for all other points, requiring ∇2f(x) to be positive deﬁnite on the (n −1)-
dimensional subspace ∇f(x)⊥.
Proof of second-order conditions for quasiconvexity
By restricting the function to an arbitrary line, it suﬃces to consider the case in
which f : R →R.
We ﬁrst show that if f : R →R is quasiconvex on an interval (a, b), then it
must satisfy (3.21), i.e., if f ′(c) = 0 with c ∈(a, b), then we must have f ′′(c) ≥0. If
f ′(c) = 0 with c ∈(a, b), f ′′(c) < 0, then for small positive ǫ we have f(c−ǫ) < f(c)
and f(c + ǫ) < f(c).
It follows that the sublevel set {x | f(x) ≤f(c) −ǫ} is
disconnected for small positive ǫ, and therefore not convex, which contradicts our
assumption that f is quasiconvex.
Now we show that if the condition (3.22) holds, then f is quasiconvex. Assume
that (3.22) holds, i.e., for each c ∈(a, b) with f ′(c) = 0, we have f ′′(c) > 0. This
means that whenever the function f ′ crosses the value 0, it is strictly increasing.
Therefore it can cross the value 0 at most once. If f ′ does not cross the value
0 at all, then f is either nonincreasing or nondecreasing on (a, b), and therefore
quasiconvex. Otherwise it must cross the value 0 exactly once, say at c ∈(a, b).
Since f ′′(c) > 0, it follows that f ′(t) ≤0 for a < t ≤c, and f ′(t) ≥0 for c ≤t < b.
This shows that f is quasiconvex.
3.4.4
Operations that preserve quasiconvexity
Nonnegative weighted maximum
A nonnegative weighted maximum of quasiconvex functions, i.e.,
f = max{w1f1, . . . , wmfm},


## Page 36

102
3
Convex functions
with wi ≥0 and fi quasiconvex, is quasiconvex.
The property extends to the
general pointwise supremum
f(x) = sup
y∈C
(w(y)g(x, y))
where w(y) ≥0 and g(x, y) is quasiconvex in x for each y. This fact can be easily
veriﬁed: f(x) ≤α if and only if
w(y)g(x, y) ≤α for all y ∈C,
i.e., the α-sublevel set of f is the intersection of the α-sublevel sets of the functions
w(y)g(x, y) in the variable x.
Example 3.37
Generalized eigenvalue. The maximum generalized eigenvalue of a
pair of symmetric matrices (X, Y ), with Y ≻0, is deﬁned as
λmax(X, Y ) = sup
u̸=0
uT Xu
uT Y u = sup{λ | det(λY −X) = 0}.
(See §A.5.3). This function is quasiconvex on dom f = Sn × Sn
++.
To see this we consider the expression
λmax(X, Y ) = sup
u̸=0
uT Xu
uT Y u .
For each u̸ = 0, the function uT Xu/uT Y u is linear-fractional in (X, Y ), hence a
quasiconvex function of (X, Y ). We conclude that λmax is quasiconvex, since it is the
supremum of a family of quasiconvex functions.
Composition
If g : Rn →R is quasiconvex and h : R →R is nondecreasing, then f = h ◦g is
quasiconvex.
The composition of a quasiconvex function with an aﬃne or linear-fractional
transformation yields a quasiconvex function. If f is quasiconvex, then g(x) =
f(Ax + b) is quasiconvex, and ˜g(x) = f((Ax + b)/(cT x + d)) is quasiconvex on the
set
{x | cT x + d > 0, (Ax + b)/(cT x + d) ∈dom f}.
Minimization
If f(x, y) is quasiconvex jointly in x and y and C is a convex set, then the function
g(x) = inf
y∈C f(x, y)
is quasiconvex.
To show this, we need to show that {x | g(x) ≤α} is convex, where α ∈R is
arbitrary. From the deﬁnition of g, g(x) ≤α if and only if for any ǫ > 0 there exists


## Page 37

3.4
Quasiconvex functions
103
a y ∈C with f(x, y) ≤α + ǫ. Now let x1 and x2 be two points in the α-sublevel
set of g. Then for any ǫ > 0, there exists y1, y2 ∈C with
f(x1, y1) ≤α + ǫ,
f(x2, y2) ≤α + ǫ,
and since f is quasiconvex in x and y, we also have
f(θx1 + (1 −θ)x2, θy1 + (1 −θ)y2) ≤α + ǫ,
for 0 ≤θ ≤1. Hence g(θx1 + (1 −θ)x2) ≤α, which proves that {x | g(x) ≤α} is
convex.
3.4.5
Representation via family of convex functions
In the sequel, it will be convenient to represent the sublevel sets of a quasiconvex
function f (which are convex) via inequalities of convex functions. We seek a family
of convex functions φt : Rn →R, indexed by t ∈R, with
f(x) ≤t ⇐⇒φt(x) ≤0,
(3.23)
i.e., the t-sublevel set of the quasiconvex function f is the 0-sublevel set of the
convex function φt. Evidently φt must satisfy the property that for all x ∈Rn,
φt(x) ≤0
=⇒
φs(x) ≤0 for s ≥t. This is satisﬁed if for each x, φt(x) is a
nonincreasing function of t, i.e., φs(x) ≤φt(x) whenever s ≥t.
To see that such a representation always exists, we can take
φt(x) =

0
f(x) ≤t
∞
otherwise,
i.e., φt is the indicator function of the t-sublevel of f. Obviously this representation
is not unique; for example if the sublevel sets of f are closed, we can take
φt(x) = dist (x, {z | f(z) ≤t}) .
We are usually interested in a family φt with nice properties, such as diﬀerentia-
bility.
Example 3.38 Convex over concave function. Suppose p is a convex function, q is a
concave function, with p(x) ≥0 and q(x) > 0 on a convex set C. Then the function
f deﬁned by f(x) = p(x)/q(x), on C, is quasiconvex.
Here we have
f(x) ≤t ⇐⇒p(x) −tq(x) ≤0,
so we can take φt(x) = p(x) −tq(x) for t ≥0. For each t, φt is convex and for each
x, φt(x) is decreasing in t.


## Page 38

104
3
Convex functions
3.5
Log-concave and log-convex functions
3.5.1
Deﬁnition
A function f : Rn →R is logarithmically concave or log-concave if f(x) > 0
for all x ∈dom f and log f is concave. It is said to be logarithmically convex
or log-convex if log f is convex. Thus f is log-convex if and only if 1/f is log-
concave. It is convenient to allow f to take on the value zero, in which case we
take log f(x) = −∞. In this case we say f is log-concave if the extended-value
function log f is concave.
We can express log-concavity directly, without logarithms: a function f : Rn →
R, with convex domain and f(x) > 0 for all x ∈dom f, is log-concave if and only
if for all x, y ∈dom f and 0 ≤θ ≤1, we have
f(θx + (1 −θ)y) ≥f(x)θf(y)1−θ.
In particular, the value of a log-concave function at the average of two points is at
least the geometric mean of the values at the two points.
From the composition rules we know that eh is convex if h is convex, so a log-
convex function is convex. Similarly, a nonnegative concave function is log-concave.
It is also clear that a log-convex function is quasiconvex and a log-concave function
is quasiconcave, since the logarithm is monotone increasing.
Example 3.39 Some simple examples of log-concave and log-convex functions.
• Aﬃne function. f(x) = aT x + b is log-concave on {x | aT x + b > 0}.
• Powers. f(x) = xa, on R++, is log-convex for a ≤0, and log-concave for a ≥0.
• Exponentials. f(x) = eax is log-convex and log-concave.
• The cumulative distribution function of a Gaussian density,
Φ(x) =
1
√
2π
Z x
−∞
e−u2/2 du,
is log-concave (see exercise 3.54).
• Gamma function. The Gamma function,
Γ(x) =
Z ∞
0
ux−1e−u du,
is log-convex for x ≥1 (see exercise 3.52).
• Determinant. det X is log concave on Sn
++.
• Determinant over trace. det X/ tr X is log concave on Sn
++ (see exercise 3.49).
Example 3.40
Log-concave density functions.
Many common probability density
functions are log-concave. Two examples are the multivariate normal distribution,
f(x) =
1
p
(2π)n det Σ
e−1
2 (x−¯x)T Σ−1(x−¯x)


## Page 39

3.5
Log-concave and log-convex functions
105
(where ¯x ∈Rn and Σ ∈Sn
++), and the exponential distribution on Rn
+,
f(x) =
 n
Y
i=1
λi
!
e−λT x
(where λ ≻0). Another example is the uniform distribution over a convex set C,
f(x) =

1/α
x ∈C
0
x̸ ∈C
where α = vol(C) is the volume (Lebesgue measure) of C. In this case log f takes
on the value −∞outside C, and −log α on C, hence is concave.
As a more exotic example consider the Wishart distribution, deﬁned as follows. Let
x1, . . . , xp ∈Rn be independent Gaussian random vectors with zero mean and co-
variance Σ ∈Sn, with p > n. The random matrix X = Pp
i=1 xixT
i has the Wishart
density
f(X) = a (det X)(p−n−1)/2 e−1
2 tr(Σ−1X),
with dom f = Sn
++, and a is a positive constant. The Wishart density is log-concave,
since
log f(X) = log a + p −n −1
2
log det X −1
2 tr(Σ−1X),
which is a concave function of X.
3.5.2
Properties
Twice diﬀerentiable log-convex/concave functions
Suppose f is twice diﬀerentiable, with dom f convex, so
∇2 log f(x) =
1
f(x)∇2f(x) −
1
f(x)2 ∇f(x)∇f(x)T .
We conclude that f is log-convex if and only if for all x ∈dom f,
f(x)∇2f(x) ⪰∇f(x)∇f(x)T ,
and log-concave if and only if for all x ∈dom f,
f(x)∇2f(x) ⪯∇f(x)∇f(x)T .
Multiplication, addition, and integration
Log-convexity and log-concavity are closed under multiplication and positive scal-
ing. For example, if f and g are log-concave, then so is the pointwise product
h(x) = f(x)g(x), since log h(x) = log f(x) + log g(x), and log f(x) and log g(x) are
concave functions of x.
Simple examples show that the sum of log-concave functions is not, in general,
log-concave. Log-convexity, however, is preserved under sums. Let f and g be log-
convex functions, i.e., F = log f and G = log g are convex. From the composition
rules for convex functions, it follows that
log (exp F + exp G) = log(f + g)


## Page 40

106
3
Convex functions
is convex. Therefore the sum of two log-convex functions is log-convex.
More generally, if f(x, y) is log-convex in x for each y ∈C then
g(x) =
Z
C
f(x, y) dy
is log-convex.
Example 3.41
Laplace transform of a nonnegative function and the moment and
cumulant generating functions. Suppose p : Rn →R satisﬁes p(x) ≥0 for all x. The
Laplace transform of p,
P(z) =
Z
p(x)e−zT x dx,
is log-convex on Rn. (Here dom P is, naturally, {z | P(z) < ∞}.)
Now suppose p is a density, i.e., satisﬁes R
p(x) dx = 1. The function M(z) = P(−z)
is called the moment generating function of the density. It gets its name from the fact
that the moments of the density can be found from the derivatives of the moment
generating function, evaluated at z = 0, e.g.,
∇M(0) = E v,
∇2M(0) = E vvT ,
where v is a random variable with density p.
The function log M(z), which is convex, is called the cumulant generating function
for p, since its derivatives give the cumulants of the density. For example, the ﬁrst
and second derivatives of the cumulant generating function, evaluated at zero, are
the mean and covariance of the associated random variable:
∇log M(0) = E v,
∇2 log M(0) = E(v −E v)(v −E v)T .
Integration of log-concave functions
In some special cases log-concavity is preserved by integration. If f : Rn×Rm →R
is log-concave, then
g(x) =
Z
f(x, y) dy
is a log-concave function of x (on Rn). (The integration here is over Rm.) A proof
of this result is not simple; see the references.
This result has many important consequences, some of which we describe in
the rest of this section. It implies, for example, that marginal distributions of log-
concave probability densities are log-concave. It also implies that log-concavity is
closed under convolution, i.e., if f and g are log-concave on Rn, then so is the
convolution
(f ∗g)(x) =
Z
f(x −y)g(y) dy.
(To see this, note that g(y) and f(x−y) are log-concave in (x, y), hence the product
f(x −y)g(y) is; then the integration result applies.)
