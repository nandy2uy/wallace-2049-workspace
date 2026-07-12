# temp_chunk_120_to_160



## Page 1

3.5
Log-concave and log-convex functions
107
Suppose C ⊆Rn is a convex set and w is a random vector in Rn with log-
concave probability density p. Then the function
f(x) = prob(x + w ∈C)
is log-concave in x. To see this, express f as
f(x) =
Z
g(x + w)p(w) dw,
where g is deﬁned as
g(u) =

1
u ∈C
0
u̸ ∈C,
(which is log-concave) and apply the integration result.
Example 3.42 The cumulative distribution function of a probability density function
f : Rn →R is deﬁned as
F(x) = prob(w ⪯x) =
Z xn
−∞
· · ·
Z x1
−∞
f(z) dz1 · · · dzn,
where w is a random variable with density f.
If f is log-concave, then F is log-
concave. We have already encountered a special case: the cumulative distribution
function of a Gaussian random variable,
f(x) =
1
√
2π
Z x
−∞
e−t2/2 dt,
is log-concave. (See example 3.39 and exercise 3.54.)
Example 3.43 Yield function. Let x ∈Rn denote the nominal or target value of a
set of parameters of a product that is manufactured. Variation in the manufacturing
process causes the parameters of the product, when manufactured, to have the value
x + w, where w ∈Rn is a random vector that represents manufacturing variation,
and is usually assumed to have zero mean. The yield of the manufacturing process,
as a function of the nominal parameter values, is given by
Y (x) = prob(x + w ∈S),
where S ⊆Rn denotes the set of acceptable parameter values for the product, i.e.,
the product speciﬁcations.
If the density of the manufacturing error w is log-concave (for example, Gaussian) and
the set S of product speciﬁcations is convex, then the yield function Y is log-concave.
This implies that the α-yield region, deﬁned as the set of nominal parameters for
which the yield exceeds α, is convex. For example, the 95% yield region
{x | Y (x) ≥0.95} = {x | log Y (x) ≥log 0.95}
is convex, since it is a superlevel set of the concave function log Y .


## Page 2

108
3
Convex functions
Example 3.44 Volume of polyhedron. Let A ∈Rm×n. Deﬁne
Pu = {x ∈Rn | Ax ⪯u}.
Then its volume vol Pu is a log-concave function of u.
To prove this, note that the function
Ψ(x, u) =

1
Ax ⪯u
0
otherwise,
is log-concave. By the integration result, we conclude that
Z
Ψ(x, u) dx = vol Pu
is log-concave.
3.6
Convexity with respect to generalized inequalities
We now consider generalizations of the notions of monotonicity and convexity, using
generalized inequalities instead of the usual ordering on R.
3.6.1
Monotonicity with respect to a generalized inequality
Suppose K ⊆Rn is a proper cone with associated generalized inequality ⪯K. A
function f : Rn →R is called K-nondecreasing if
x ⪯K y =⇒f(x) ≤f(y),
and K-increasing if
x ⪯K y, x̸ = y =⇒f(x) < f(y).
We deﬁne K-nonincreasing and K-decreasing functions in a similar way.
Example 3.45 Monotone vector functions. A function f : Rn →R is nondecreasing
with respect to Rn
+ if and only if
x1 ≤y1, . . . , xn ≤yn =⇒f(x) ≤f(y)
for all x, y. This is the same as saying that f, when restricted to any component xi
(i.e., xi is considered the variable while xj for j̸ = i are ﬁxed), is nondecreasing.
Example 3.46
Matrix monotone functions. A function f : Sn →R is called ma-
trix monotone (increasing, decreasing) if it is monotone with respect to the posi-
tive semideﬁnite cone. Some examples of matrix monotone functions of the variable
X ∈Sn:


## Page 3

3.6
Convexity with respect to generalized inequalities
109
• tr(WX), where W ∈Sn, is matrix nondecreasing if W ⪰0, and matrix in-
creasing if W ≻0 (it is matrix nonincreasing if W ⪯0, and matrix decreasing
if W ≺0).
• tr(X−1) is matrix decreasing on Sn
++.
• det X is matrix increasing on Sn
++, and matrix nondecreasing on Sn
+.
Gradient conditions for monotonicity
Recall that a diﬀerentiable function f : R →R, with convex (i.e., interval) domain,
is nondecreasing if and only if f ′(x) ≥0 for all x ∈dom f, and increasing if
f ′(x) > 0 for all x ∈dom f (but the converse is not true).
These conditions
are readily extended to the case of monotonicity with respect to a generalized
inequality. A diﬀerentiable function f, with convex domain, is K-nondecreasing if
and only if
∇f(x) ⪰K∗0
(3.24)
for all x ∈dom f. Note the diﬀerence with the simple scalar case: the gradi-
ent must be nonnegative in the dual inequality. For the strict case, we have the
following: If
∇f(x) ≻K∗0
(3.25)
for all x ∈dom f, then f is K-increasing. As in the scalar case, the converse is
not true.
Let us prove these ﬁrst-order conditions for monotonicity. First, assume that
f satisﬁes (3.24) for all x, but is not K-nondecreasing, i.e., there exist x, y with
x ⪯K y and f(y) < f(x). By diﬀerentiability of f there exists a t ∈[0, 1] with
d
dtf(x + t(y −x)) = ∇f(x + t(y −x))T (y −x) < 0.
Since y −x ∈K this means
∇f(x + t(y −x))̸ ∈K∗,
which contradicts our assumption that (3.24) is satisﬁed everywhere. In a similar
way it can be shown that (3.25) implies f is K-increasing.
It is also straightforward to see that it is necessary that (3.24) hold everywhere.
Assume (3.24) does not hold for x = z. By the deﬁnition of dual cone this means
there exists a v ∈K with
∇f(z)T v < 0.
Now consider h(t) = f(z + tv) as a function of t. We have h′(0) = ∇f(z)T v < 0,
and therefore there exists t > 0 with h(t) = f(z + tv) < h(0) = f(z), which means
f is not K-nondecreasing.
3.6.2
Convexity with respect to a generalized inequality
Suppose K ⊆Rm is a proper cone with associated generalized inequality ⪯K. We
say f : Rn →Rm is K-convex if for all x, y, and 0 ≤θ ≤1,
f(θx + (1 −θ)y) ⪯K θf(x) + (1 −θ)f(y).


## Page 4

110
3
Convex functions
The function is strictly K-convex if
f(θx + (1 −θ)y) ≺K θf(x) + (1 −θ)f(y)
for all x̸ = y and 0 < θ < 1. These deﬁnitions reduce to ordinary convexity and
strict convexity when m = 1 (and K = R+).
Example 3.47
Convexity with respect to componentwise inequality. A function f :
Rn →Rm is convex with respect to componentwise inequality (i.e., the generalized
inequality induced by Rm
+ ) if and only if for all x, y and 0 ≤θ ≤1,
f(θx + (1 −θ)y) ⪯θf(x) + (1 −θ)f(y),
i.e., each component fi is a convex function. The function f is strictly convex with
respect to componentwise inequality if and only if each component fi is strictly con-
vex.
Example 3.48 Matrix convexity. Suppose f is a symmetric matrix valued function,
i.e., f : Rn →Sm. The function f is convex with respect to matrix inequality if
f(θx + (1 −θ)y) ⪯θf(x) + (1 −θ)f(y)
for any x and y, and for θ ∈[0, 1]. This is sometimes called matrix convexity. An
equivalent deﬁnition is that the scalar function zT f(x)z is convex for all vectors z.
(This is often a good way to prove matrix convexity). A matrix function is strictly
matrix convex if
f(θx + (1 −θ)y) ≺θf(x) + (1 −θ)f(y)
when x̸ = y and 0 < θ < 1, or, equivalently, if zT fz is strictly convex for every z̸ = 0.
Some examples:
• The function f(X) = XXT where X ∈Rn×m is matrix convex, since for
ﬁxed z the function zT XXT z = ∥XT z∥2
2 is a convex quadratic function of (the
components of) X. For the same reason, f(X) = X2 is matrix convex on Sn.
• The function Xp is matrix convex on Sn
++ for 1 ≤p ≤2 or −1 ≤p ≤0, and
matrix concave for 0 ≤p ≤1.
• The function f(X) = eX is not matrix convex on Sn, for n ≥2.
Many of the results for convex functions have extensions to K-convex functions.
As a simple example, a function is K-convex if and only if its restriction to any
line in its domain is K-convex. In the rest of this section we list a few results for
K-convexity that we will use later; more results are explored in the exercises.
Dual characterization of K-convexity
A function f is K-convex if and only if for every w ⪰K∗0, the (real-valued) function
wT f is convex (in the ordinary sense); f is strictly K-convex if and only if for every
nonzero w ⪰K∗0 the function wT f is strictly convex. (These follow directly from
the deﬁnitions and properties of dual inequality.)


## Page 5

3.6
Convexity with respect to generalized inequalities
111
Diﬀerentiable K-convex functions
A diﬀerentiable function f is K-convex if and only if its domain is convex, and for
all x, y ∈dom f,
f(y) ⪰K f(x) + Df(x)(y −x).
(Here Df(x) ∈Rm×n is the derivative or Jacobian matrix of f at x; see §A.4.1.)
The function f is strictly K-convex if and only if for all x, y ∈dom f with x̸ = y,
f(y) ≻K f(x) + Df(x)(y −x).
Composition theorem
Many of the results on composition can be generalized to K-convexity. For example,
if g : Rn →Rp is K-convex, h : Rp →R is convex, and ˜h (the extended-value
extension of h) is K-nondecreasing, then h ◦g is convex. This generalizes the fact
that a nondecreasing convex function of a convex function is convex. The condition
that ˜h be K-nondecreasing implies that dom h −K = dom h.
Example 3.49 The quadratic matrix function g : Rm×n →Sn deﬁned by
g(X) = XT AX + BT X + XT B + C,
where A ∈Sm, B ∈Rm×n, and C ∈Sn, is convex when A ⪰0.
The function h : Sn →R deﬁned by h(Y ) = −log det(−Y ) is convex and increasing
on dom h = −Sn
++.
By the composition theorem, we conclude that
f(X) = −log det(−(XT AX + BT X + XT B + C))
is convex on
dom f = {X ∈Rm×n | XT AX + BT X + XT B + C ≺0}.
This generalizes the fact that
−log(−(ax2 + bx + c))
is convex on
{x ∈R | ax2 + bx + c < 0},
provided a ≥0.


## Page 6

112
3
Convex functions
Bibliography
The standard reference on convex analysis is Rockafellar [Roc70]. Other books on convex
functions are Stoer and Witzgall [SW70], Roberts and Varberg [RV73], Van Tiel [vT84],
Hiriart-Urruty and Lemar´echal [HUL93], Ekeland and T´emam [ET99], Borwein and Lewis
[BL00], Florenzano and Le Van [FL01], Barvinok [Bar02], and Bertsekas, Nedi´c, and
Ozdaglar [Ber03]. Most nonlinear programming texts also include chapters on convex
functions (see, for example, Mangasarian [Man94], Bazaraa, Sherali, and Shetty [BSS93],
Bertsekas [Ber99], Polyak [Pol87], and Peressini, Sullivan, and Uhl [PSU88]).
Jensen’s inequality appears in [Jen06]. A general study of inequalities, in which Jensen’s
inequality plays a central role, is presented by Hardy, Littlewood, and P´olya [HLP52],
and Beckenbach and Bellman [BB65].
The term perspective function is from Hiriart-Urruty and Lemar´echal [HUL93, volume
1, page 100]. For the deﬁnitions in example 3.19 (relative entropy and Kullback-Leibler
divergence), and the related exercise 3.13, see Cover and Thomas [CT91].
Some important early references on quasiconvex functions (as well as other extensions of
convexity) are Nikaidˆo [Nik54], Mangasarian [Man94, chapter 9], Arrow and Enthoven
[AE61], Ponstein [Pon67], and Luenberger [Lue68]. For a more comprehensive reference
list, we refer to Bazaraa, Sherali, and Shetty [BSS93, page 126].
Pr´ekopa [Pr´e80] gives a survey of log-concave functions. Log-convexity of the Laplace
transform is mentioned in Barndorﬀ-Nielsen [BN78, §7]. For a proof of the integration
result of log-concave functions, see Pr´ekopa [Pr´e71, Pr´e73].
Generalized inequalities are used extensively in the recent literature on cone programming,
starting with Nesterov and Nemirovski [NN94, page 156]; see also Ben-Tal and Nemirovski
[BTN01] and the references at the end of chapter 4. Convexity with respect to generalized
inequalities also appears in the work of Luenberger [Lue69, §8.2] and Isii [Isi64]. Matrix
monotonicity and matrix convexity are attributed to L¨owner [L¨ow34], and are discussed
in detail by Davis [Dav63], Roberts and Varberg [RV73, page 216] and Marshall and
Olkin [MO79, §16E]. For the result on convexity and concavity of the function Xp in
example 3.48, see Bondar [Bon94, theorem 16.1]. For a simple example that demonstrates
that eX is not matrix convex, see Marshall and Olkin [MO79, page 474].


## Page 7

Exercises
113
Exercises
Deﬁnition of convexity
3.1 Suppose f : R →R is convex, and a, b ∈dom f with a < b.
(a) Show that
f(x) ≤b −x
b −a f(a) + x −a
b −a f(b)
for all x ∈[a, b].
(b) Show that
f(x) −f(a)
x −a
≤f(b) −f(a)
b −a
≤f(b) −f(x)
b −x
for all x ∈(a, b). Draw a sketch that illustrates this inequality.
(c) Suppose f is diﬀerentiable. Use the result in (b) to show that
f ′(a) ≤f(b) −f(a)
b −a
≤f ′(b).
Note that these inequalities also follow from (3.2):
f(b) ≥f(a) + f ′(a)(b −a),
f(a) ≥f(b) + f ′(b)(a −b).
(d) Suppose f is twice diﬀerentiable. Use the result in (c) to show that f ′′(a) ≥0 and
f ′′(b) ≥0.
3.2 Level sets of convex, concave, quasiconvex, and quasiconcave functions. Some level sets
of a function f are shown below. The curve labeled 1 shows {x | f(x) = 1}, etc.
1
2
3
Could f be convex (concave, quasiconvex, quasiconcave)? Explain your answer. Repeat
for the level curves shown below.
1 2
3
4
5
6


## Page 8

114
3
Convex functions
3.3 Inverse of an increasing convex function. Suppose f : R →R is increasing and convex
on its domain (a, b). Let g denote its inverse, i.e., the function with domain (f(a), f(b))
and g(f(x)) = x for a < x < b. What can you say about convexity or concavity of g?
3.4 [RV73, page 15] Show that a continuous function f : Rn →R is convex if and only if for
every line segment, its average value on the segment is less than or equal to the average
of its values at the endpoints of the segment: For every x, y ∈Rn,
Z 1
0
f(x + λ(y −x)) dλ ≤f(x) + f(y)
2
.
3.5 [RV73, page 22] Running average of a convex function. Suppose f : R →R is convex,
with R+ ⊆dom f. Show that its running average F, deﬁned as
F(x) = 1
x
Z x
0
f(t) dt,
dom F = R++,
is convex. Hint. For each s, f(sx) is convex in x, so R 1
0 f(sx) ds is convex.
3.6 Functions and epigraphs. When is the epigraph of a function a halfspace? When is the
epigraph of a function a convex cone? When is the epigraph of a function a polyhedron?
3.7 Suppose f : Rn →R is convex with dom f = Rn, and bounded above on Rn. Show that
f is constant.
3.8 Second-order condition for convexity. Prove that a twice diﬀerentiable function f is convex
if and only if its domain is convex and ∇2f(x) ⪰0 for all x ∈dom f. Hint. First consider
the case f : R →R. You can use the ﬁrst-order condition for convexity (which was proved
on page 70).
3.9 Second-order conditions for convexity on an aﬃne set. Let F ∈Rn×m, ˆx ∈Rn. The
restriction of f : Rn →R to the aﬃne set {Fz + ˆx | z ∈Rm} is deﬁned as the function
˜f : Rm →R with
˜f(z) = f(Fz + ˆx),
dom ˜f = {z | Fz + ˆx ∈dom f}.
Suppose f is twice diﬀerentiable with a convex domain.
(a) Show that ˜f is convex if and only if for all z ∈dom ˜f
F T ∇2f(Fz + ˆx)F ⪰0.
(b) Suppose A ∈Rp×n is a matrix whose nullspace is equal to the range of F, i.e.,
AF = 0 and rank A = n−rank F. Show that ˜f is convex if for all z ∈dom ˜f there
exists a λ ∈R such that
∇2f(Fz + ˆx) + λAT A ⪰0.
Hint. Use the following result: If B ∈Sn and A ∈Rp×n, then xT Bx ≥0 for all
x ∈N(A) if there exists a λ such that B + λAT A ⪰0.
3.10 An extension of Jensen’s inequality.
One interpretation of Jensen’s inequality is that
randomization or dithering hurts, i.e., raises the average value of a convex function: For
f convex and v a zero mean random variable, we have E f(x0 + v) ≥f(x0). This leads
to the following conjecture. If f is convex, then the larger the variance of v, the larger
E f(x0 + v).
(a) Give a counterexample that shows that this conjecture is false.
Find zero mean
random variables v and w, with var(v) > var(w), a convex function f, and a point
x0, such that E f(x0 + v) < E f(x0 + w).


## Page 9

Exercises
115
(b) The conjecture is true when v and w are scaled versions of each other. Show that
E f(x0 + tv) is monotone increasing in t ≥0, when f is convex and v is zero mean.
3.11 Monotone mappings. A function ψ : Rn →Rn is called monotone if for all x, y ∈dom ψ,
(ψ(x) −ψ(y))T (x −y) ≥0.
(Note that ‘monotone’ as deﬁned here is not the same as the deﬁnition given in §3.6.1.
Both deﬁnitions are widely used.) Suppose f : Rn →R is a diﬀerentiable convex function.
Show that its gradient ∇f is monotone. Is the converse true, i.e., is every monotone
mapping the gradient of a convex function?
3.12 Suppose f : Rn →R is convex, g : Rn →R is concave, dom f = dom g = Rn, and
for all x, g(x) ≤f(x). Show that there exists an aﬃne function h such that for all x,
g(x) ≤h(x) ≤f(x). In other words, if a concave function g is an underestimator of a
convex function f, then we can ﬁt an aﬃne function between f and g.
3.13 Kullback-Leibler divergence and the information inequality.
Let Dkl be the Kullback-
Leibler divergence, as deﬁned in (3.17). Prove the information inequality: Dkl(u, v) ≥0
for all u, v ∈Rn
++. Also show that Dkl(u, v) = 0 if and only if u = v.
Hint. The Kullback-Leibler divergence can be expressed as
Dkl(u, v) = f(u) −f(v) −∇f(v)T (u −v),
where f(v) = Pn
i=1 vi log vi is the negative entropy of v.
3.14 Convex-concave functions and saddle-points. We say the function f : Rn × Rm →R
is convex-concave if f(x, z) is a concave function of z, for each ﬁxed x, and a convex
function of x, for each ﬁxed z. We also require its domain to have the product form
dom f = A × B, where A ⊆Rn and B ⊆Rm are convex.
(a) Give a second-order condition for a twice diﬀerentiable function f : Rn × Rm →R
to be convex-concave, in terms of its Hessian ∇2f(x, z).
(b) Suppose that f : Rn×Rm →R is convex-concave and diﬀerentiable, with ∇f(˜x, ˜z) =
0. Show that the saddle-point property holds: for all x, z, we have
f(˜x, z) ≤f(˜x, ˜z) ≤f(x, ˜z).
Show that this implies that f satisﬁes the strong max-min property:
sup
z
inf
x
f(x, z) = inf
x
sup
z
f(x, z)
(and their common value is f(˜x, ˜z)).
(c) Now suppose that f : Rn × Rm →R is diﬀerentiable, but not necessarily convex-
concave, and the saddle-point property holds at ˜x, ˜z:
f(˜x, z) ≤f(˜x, ˜z) ≤f(x, ˜z)
for all x, z. Show that ∇f(˜x, ˜z) = 0.
Examples
3.15 A family of concave utility functions. For 0 < α ≤1 let
uα(x) = xα −1
α
,
with dom uα = R+. We also deﬁne u0(x) = log x (with dom u0 = R++).
(a) Show that for x > 0, u0(x) = limα→0 uα(x).


## Page 10

116
3
Convex functions
(b) Show that uα are concave, monotone increasing, and all satisfy uα(1) = 0.
These functions are often used in economics to model the beneﬁt or utility of some quantity
of goods or money. Concavity of uα means that the marginal utility (i.e., the increase
in utility obtained for a ﬁxed increase in the goods) decreases as the amount of goods
increases. In other words, concavity models the eﬀect of satiation.
3.16 For each of the following functions determine whether it is convex, concave, quasiconvex,
or quasiconcave.
(a) f(x) = ex −1 on R.
(b) f(x1, x2) = x1x2 on R2
++.
(c) f(x1, x2) = 1/(x1x2) on R2
++.
(d) f(x1, x2) = x1/x2 on R2
++.
(e) f(x1, x2) = x2
1/x2 on R × R++.
(f) f(x1, x2) = xα
1 x1−α
2
, where 0 ≤α ≤1, on R2
++.
3.17 Suppose p < 1, p̸ = 0. Show that the function
f(x) =
 
n
X
i=1
xp
i
!1/p
with dom f = Rn
++ is concave. This includes as special cases f(x) = (Pn
i=1 x1/2
i
)2 and
the harmonic mean f(x) = (Pn
i=1 1/xi)−1. Hint. Adapt the proofs for the log-sum-exp
function and the geometric mean in §3.1.5.
3.18 Adapt the proof of concavity of the log-determinant function in §3.1.5 to show the follow-
ing.
(a) f(X) = tr  X−1
is convex on dom f = Sn
++.
(b) f(X) = (det X)1/n is concave on dom f = Sn
++.
3.19 Nonnegative weighted sums and integrals.
(a) Show that f(x) = Pr
i=1 αix[i] is a convex function of x, where α1 ≥α2 ≥· · · ≥
αr ≥0, and x[i] denotes the ith largest component of x. (You can use the fact that
f(x) = Pk
i=1 x[i] is convex on Rn.)
(b) Let T(x, ω) denote the trigonometric polynomial
T(x, ω) = x1 + x2 cos ω + x3 cos 2ω + · · · + xn cos(n −1)ω.
Show that the function
f(x) = −
Z 2π
0
log T(x, ω) dω
is convex on {x ∈Rn | T(x, ω) > 0, 0 ≤ω ≤2π}.
3.20 Composition with an aﬃne function. Show that the following functions f : Rn →R are
convex.
(a) f(x) = ∥Ax −b∥, where A ∈Rm×n, b ∈Rm, and ∥· ∥is a norm on Rm.
(b) f(x) = −(det(A0 + x1A1 + · · · + xnAn))1/m, on {x | A0 + x1A1 + · · · + xnAn ≻0},
where Ai ∈Sm.
(c) f(X) = tr (A0 + x1A1 + · · · + xnAn)−1, on {x | A0 +x1A1 +· · ·+xnAn ≻0}, where
Ai ∈Sm. (Use the fact that tr(X−1) is convex on Sm
++; see exercise 3.18.)


## Page 11

Exercises
117
3.21 Pointwise maximum and supremum. Show that the following functions f : Rn →R are
convex.
(a) f(x) = maxi=1,...,k ∥A(i)x −b(i)∥, where A(i) ∈Rm×n, b(i) ∈Rm and ∥· ∥is a norm
on Rm.
(b) f(x) = Pr
i=1 |x|[i] on Rn, where |x| denotes the vector with |x|i = |xi| (i.e., |x| is
the absolute value of x, componentwise), and |x|[i] is the ith largest component of
|x|. In other words, |x|[1], |x|[2], . . . , |x|[n] are the absolute values of the components
of x, sorted in nonincreasing order.
3.22 Composition rules. Show that the following functions are convex.
(a) f(x) = −log(−log(Pm
i=1 eaT
i x+bi)) on dom f = {x | Pm
i=1 eaT
i x+bi < 1}. You can
use the fact that log(Pn
i=1 eyi) is convex.
(b) f(x, u, v) = −
√
uv −xT x on dom f = {(x, u, v) | uv > xT x, u, v > 0}. Use the
fact that xT x/u is convex in (x, u) for u > 0, and that −√x1x2 is convex on R2
++.
(c) f(x, u, v) = −log(uv −xT x) on dom f = {(x, u, v) | uv > xT x, u, v > 0}.
(d) f(x, t) = −(tp −∥x∥p
p)1/p where p > 1 and dom f = {(x, t) | t ≥∥x∥p}. You can use
the fact that ∥x∥p
p/up−1 is convex in (x, u) for u > 0 (see exercise 3.23), and that
−x1/py1−1/p is convex on R2
+ (see exercise 3.16).
(e) f(x, t) = −log(tp −∥x∥p
p) where p > 1 and dom f = {(x, t) | t > ∥x∥p}. You can
use the fact that ∥x∥p
p/up−1 is convex in (x, u) for u > 0 (see exercise 3.23).
3.23 Perspective of a function.
(a) Show that for p > 1,
f(x, t) = |x1|p + · · · + |xn|p
tp−1
= ∥x∥p
p
tp−1
is convex on {(x, t) | t > 0}.
(b) Show that
f(x) = ∥Ax + b∥2
2
cT x + d
is convex on {x | cT x + d > 0}, where A ∈Rm×n, b ∈Rm, c ∈Rn and d ∈R.
3.24 Some functions on the probability simplex. Let x be a real-valued random variable which
takes values in {a1, . . . , an} where a1 < a2 < · · · < an, with prob(x = ai) = pi,
i = 1, . . . , n. For each of the following functions of p (on the probability simplex {p ∈
Rn
+ | 1T p = 1}), determine if the function is convex, concave, quasiconvex, or quasicon-
cave.
(a) E x.
(b) prob(x ≥α).
(c) prob(α ≤x ≤β).
(d) Pn
i=1 pi log pi, the negative entropy of the distribution.
(e) var x = E(x −E x)2.
(f) quartile(x) = inf{β | prob(x ≤β) ≥0.25}.
(g) The cardinality of the smallest set A ⊆{a1, . . . , an} with probability ≥90%. (By
cardinality we mean the number of elements in A.)
(h) The minimum width interval that contains 90% of the probability, i.e.,
inf {β −α | prob(α ≤x ≤β) ≥0.9} .


## Page 12

118
3
Convex functions
3.25 Maximum probability distance between distributions. Let p, q ∈Rn represent two proba-
bility distributions on {1, . . . , n} (so p, q ⪰0, 1T p = 1T q = 1). We deﬁne the maximum
probability distance dmp(p, q) between p and q as the maximum diﬀerence in probability
assigned by p and q, over all events:
dmp(p, q) = max{| prob(p, C) −prob(q, C)| | C ⊆{1, . . . , n}}.
Here prob(p, C) is the probability of C, under the distribution p, i.e., prob(p, C) =
P
i∈C pi.
Find a simple expression for dmp, involving ∥p −q∥1 = Pn
i=1 |pi −qi|, and show that dmp
is a convex function on Rn × Rn. (Its domain is {(p, q) | p, q ⪰0, 1T p = 1T q = 1}, but
it has a natural extension to all of Rn × Rn.)
3.26 More functions of eigenvalues. Let λ1(X) ≥λ2(X) ≥· · · ≥λn(X) denote the eigenvalues
of a matrix X ∈Sn. We have already seen several functions of the eigenvalues that are
convex or concave functions of X.
• The maximum eigenvalue λ1(X) is convex (example 3.10). The minimum eigenvalue
λn(X) is concave.
• The sum of the eigenvalues (or trace), tr X = λ1(X) + · · · + λn(X), is linear.
• The sum of the inverses of the eigenvalues (or trace of the inverse), tr(X−1) =
Pn
i=1 1/λi(X), is convex on Sn
++ (exercise 3.18).
• The geometric mean of the eigenvalues, (det X)1/n = (Qn
i=1 λi(X))1/n, and the
logarithm of the product of the eigenvalues, log det X = Pn
i=1 log λi(X), are concave
on X ∈Sn
++ (exercise 3.18 and page 74).
In this problem we explore some more functions of eigenvalues, by exploiting variational
characterizations.
(a) Sum of k largest eigenvalues. Show that Pk
i=1 λi(X) is convex on Sn. Hint. [HJ85,
page 191] Use the variational characterization
k
X
i=1
λi(X) = sup{tr(V T XV ) | V ∈Rn×k, V T V = I}.
(b) Geometric mean of k smallest eigenvalues. Show that (Qn
i=n−k+1 λi(X))1/k is con-
cave on Sn
++. Hint. [MO79, page 513] For X ≻0, we have
 
n
Y
i=n−k+1
λi(X)
!1/k
= 1
k inf{tr(V T XV ) | V ∈Rn×k, det V T V = 1}.
(c) Log of product of k smallest eigenvalues. Show that Pn
i=n−k+1 log λi(X) is concave
on Sn
++. Hint. [MO79, page 513] For X ≻0,
n
Y
i=n−k+1
λi(X) = inf
(
k
Y
i=1
(V T XV )ii
 V ∈Rn×k, V T V = I
)
.
3.27 Diagonal elements of Cholesky factor. Each X ∈Sn
++ has a unique Cholesky factorization
X = LLT , where L is lower triangular, with Lii > 0. Show that Lii is a concave function
of X (with domain Sn
++).
Hint. Lii can be expressed as Lii = (w −zT Y −1z)1/2, where

Y
z
zT
w

is the leading i × i submatrix of X.


## Page 13

Exercises
119
Operations that preserve convexity
3.28 Expressing a convex function as the pointwise supremum of a family of aﬃne functions.
In this problem we extend the result proved on page 83 to the case where dom f̸ = Rn.
Let f : Rn →R be a convex function. Deﬁne ˜f : Rn →R as the pointwise supremum of
all aﬃne functions that are global underestimators of f:
˜f(x) = sup{g(x) | g aﬃne, g(z) ≤f(z) for all z}.
(a) Show that f(x) = ˜f(x) for x ∈int dom f.
(b) Show that f = ˜f if f is closed (i.e., epi f is a closed set; see §A.3.3).
3.29 Representation of piecewise-linear convex functions. A convex function f : Rn →R, with
dom f = Rn, is called piecewise-linear if there exists a partition of Rn as
Rn = X1 ∪X2 ∪· · · ∪XL,
where int Xi̸ = ∅and int Xi ∩int Xj = ∅for i̸ = j, and a family of aﬃne functions
aT
1 x + b1, . . . , aT
Lx + bL such that f(x) = aT
i x + bi for x ∈Xi.
Show that such a function has the form f(x) = max{aT
1 x + b1, . . . , aT
Lx + bL}.
3.30 Convex hull or envelope of a function. The convex hull or convex envelope of a function
f : Rn →R is deﬁned as
g(x) = inf{t | (x, t) ∈conv epi f}.
Geometrically, the epigraph of g is the convex hull of the epigraph of f.
Show that g is the largest convex underestimator of f. In other words, show that if h is
convex and satisﬁes h(x) ≤f(x) for all x, then h(x) ≤g(x) for all x.
3.31 [Roc70, page 35] Largest homogeneous underestimator. Let f be a convex function. Deﬁne
the function g as
g(x) = inf
α>0
f(αx)
α
.
(a) Show that g is homogeneous (g(tx) = tg(x) for all t ≥0).
(b) Show that g is the largest homogeneous underestimator of f: If h is homogeneous
and h(x) ≤f(x) for all x, then we have h(x) ≤g(x) for all x.
(c) Show that g is convex.
3.32 Products and ratios of convex functions. In general the product or ratio of two convex
functions is not convex. However, there are some results that apply to functions on R.
Prove the following.
(a) If f and g are convex, both nondecreasing (or nonincreasing), and positive functions
on an interval, then fg is convex.
(b) If f, g are concave, positive, with one nondecreasing and the other nonincreasing,
then fg is concave.
(c) If f is convex, nondecreasing, and positive, and g is concave, nonincreasing, and
positive, then f/g is convex.
3.33 Direct proof of perspective theorem. Give a direct proof that the perspective function g,
as deﬁned in §3.2.6, of a convex function f is convex: Show that dom g is a convex set,
and that for (x, t), (y, s) ∈dom g, and 0 ≤θ ≤1, we have
g(θx + (1 −θ)y, θt + (1 −θ)s) ≤θg(x, t) + (1 −θ)g(y, s).
3.34 The Minkowski function. The Minkowski function of a convex set C is deﬁned as
MC(x) = inf{t > 0 | t−1x ∈C}.


## Page 14

120
3
Convex functions
(a) Draw a picture giving a geometric interpretation of how to ﬁnd MC(x).
(b) Show that MC is homogeneous, i.e., MC(αx) = αMC(x) for α ≥0.
(c) What is dom MC?
(d) Show that MC is a convex function.
(e) Suppose C is also closed, bounded, symmetric (if x ∈C then −x ∈C), and has
nonempty interior. Show that MC is a norm. What is the corresponding unit ball?
3.35 Support function calculus. Recall that the support function of a set C ⊆Rn is deﬁned as
SC(y) = sup{yT x | x ∈C}. On page 81 we showed that SC is a convex function.
(a) Show that SB = Sconv B.
(b) Show that SA+B = SA + SB.
(c) Show that SA∪B = max{SA, SB}.
(d) Let B be closed and convex. Show that A ⊆B if and only if SA(y) ≤SB(y) for all
y.
Conjugate functions
3.36 Derive the conjugates of the following functions.
(a) Max function. f(x) = maxi=1,...,n xi on Rn.
(b) Sum of largest elements. f(x) = Pr
i=1 x[i] on Rn.
(c) Piecewise-linear function on R.
f(x) = maxi=1,...,m(aix + bi) on R.
You can
assume that the ai are sorted in increasing order, i.e., a1 ≤· · · ≤am, and that none
of the functions aix + bi is redundant, i.e., for each k there is at least one x with
f(x) = akx + bk.
(d) Power function. f(x) = xp on R++, where p > 1. Repeat for p < 0.
(e) Negative geometric mean. f(x) = −(Q
xi)1/n on Rn
++.
(f) Negative generalized logarithm for second-order cone. f(x, t) = −log(t2 −xT x) on
{(x, t) ∈Rn × R | ∥x∥2 < t}.
3.37 Show that the conjugate of f(X) = tr(X−1) with dom f = Sn
++ is given by
f ∗(Y ) = −2 tr(−Y )1/2,
dom f ∗= −Sn
+.
Hint. The gradient of f is ∇f(X) = −X−2.
3.38 Young’s inequality. Let f : R →R be an increasing function, with f(0) = 0, and let g be
its inverse. Deﬁne F and G as
F(x) =
Z x
0
f(a) da,
G(y) =
Z y
0
g(a) da.
Show that F and G are conjugates. Give a simple graphical interpretation of Young’s
inequality,
xy ≤F(x) + G(y).
3.39 Properties of conjugate functions.
(a) Conjugate of convex plus aﬃne function. Deﬁne g(x) = f(x) + cT x + d, where f is
convex. Express g∗in terms of f ∗(and c, d).
(b) Conjugate of perspective.
Express the conjugate of the perspective of a convex
function f in terms of f ∗.


## Page 15

Exercises
121
(c) Conjugate and minimization.
Let f(x, z) be convex in (x, z) and deﬁne g(x) =
infz f(x, z). Express the conjugate g∗in terms of f ∗.
As an application, express the conjugate of g(x) = infz{h(z) | Az + b = x}, where h
is convex, in terms of h∗, A, and b.
(d) Conjugate of conjugate. Show that the conjugate of the conjugate of a closed convex
function is itself: f = f ∗∗if f is closed and convex. (A function is closed if its
epigraph is closed; see §A.3.3.) Hint. Show that f ∗∗is the pointwise supremum of
all aﬃne global underestimators of f. Then apply the result of exercise 3.28.
3.40 Gradient and Hessian of conjugate function. Suppose f : Rn →R is convex and twice
continuously diﬀerentiable. Suppose ¯y and ¯x are related by ¯y = ∇f(¯x), and that ∇2f(¯x) ≻
0.
(a) Show that ∇f ∗(¯y) = ¯x.
(b) Show that ∇2f ∗(¯y) = ∇2f(¯x)−1.
3.41 Conjugate of negative normalized entropy. Show that the conjugate of the negative nor-
malized entropy
f(x) =
n
X
i=1
xi log(xi/1T x),
with dom f = Rn
++, is given by
f ∗(y) =

0
Pn
i=1 eyi ≤1
+∞
otherwise.
Quasiconvex functions
3.42 Approximation width. Let f0, . . . , fn : R →R be given continuous functions. We consider
the problem of approximating f0 as a linear combination of f1, . . . , fn. For x ∈Rn, we
say that f = x1f1 + · · · + xnfn approximates f0 with tolerance ǫ > 0 over the interval
[0, T] if |f(t) −f0(t)| ≤ǫ for 0 ≤t ≤T. Now we choose a ﬁxed tolerance ǫ > 0 and deﬁne
the approximation width as the largest T such that f approximates f0 over the interval
[0, T]:
W(x) = sup{T | |x1f1(t) + · · · + xnfn(t) −f0(t)| ≤ǫ for 0 ≤t ≤T}.
Show that W is quasiconcave.
3.43 First-order condition for quasiconvexity. Prove the ﬁrst-order condition for quasiconvexity
given in §3.4.3: A diﬀerentiable function f : Rn →R, with dom f convex, is quasiconvex
if and only if for all x, y ∈dom f,
f(y) ≤f(x) =⇒∇f(x)T (y −x) ≤0.
Hint. It suﬃces to prove the result for a function on R; the general result follows by
restriction to an arbitrary line.
3.44 Second-order conditions for quasiconvexity. In this problem we derive alternate repre-
sentations of the second-order conditions for quasiconvexity given in §3.4.3. Prove the
following.
(a) A point x ∈dom f satisﬁes (3.21) if there exists a σ such that
∇2f(x) + σ∇f(x)∇f(x)T ⪰0.
(3.26)
It satisﬁes (3.22) for all y̸ = 0 if and only if there exists a σ such
∇2f(x) + σ∇f(x)∇f(x)T ≻0.
(3.27)
Hint. We can assume without loss of generality that ∇2f(x) is diagonal.


## Page 16

122
3
Convex functions
(b) A point x ∈dom f satisﬁes (3.21) if and only if either ∇f(x) = 0 and ∇2f(x) ⪰0,
or ∇f(x)̸ = 0 and the matrix
H(x) =

∇2f(x)
∇f(x)
∇f(x)T
0

has exactly one negative eigenvalue. It satisﬁes (3.22) for all y̸ = 0 if and only if
H(x) has exactly one nonpositive eigenvalue.
Hint. You can use the result of part (a). The following result, which follows from
the eigenvalue interlacing theorem in linear algebra, may also be useful: If B ∈Sn
and a ∈Rn, then
λn

B
a
aT
0

≥λn(B).
3.45 Use the ﬁrst and second-order conditions for quasiconvexity given in §3.4.3 to verify
quasiconvexity of the function f(x) = −x1x2, with dom f = R2
++.
3.46 Quasilinear functions with domain Rn. A function on R that is quasilinear (i.e., qua-
siconvex and quasiconcave) is monotone, i.e., either nondecreasing or nonincreasing. In
this problem we consider a generalization of this result to functions on Rn.
Suppose the function f : Rn →R is quasilinear and continuous with dom f = Rn. Show
that it can be expressed as f(x) = g(aT x), where g : R →R is monotone and a ∈Rn.
In other words, a quasilinear function with domain Rn must be a monotone function of
a linear function. (The converse is also true.)
Log-concave and log-convex functions
3.47 Suppose f : Rn →R is diﬀerentiable, dom f is convex, and f(x) > 0 for all x ∈dom f.
Show that f is log-concave if and only if for all x, y ∈dom f,
f(y)
f(x) ≤exp

∇f(x)T (y −x)
f(x)

.
3.48 Show that if f : Rn →R is log-concave and a ≥0, then the function g = f −a is
log-concave, where dom g = {x ∈dom f | f(x) > a}.
3.49 Show that the following functions are log-concave.
(a) Logistic function: f(x) = ex/(1 + ex) with dom f = R.
(b) Harmonic mean:
f(x) =
1
1/x1 + · · · + 1/xn ,
dom f = Rn
++.
(c) Product over sum:
f(x) =
Qn
i=1 xi
Pn
i=1 xi
,
dom f = Rn
++.
(d) Determinant over trace:
f(X) = det X
tr X ,
dom f = Sn
++.


## Page 17

Exercises
123
3.50 Coeﬃcients of a polynomial as a function of the roots. Show that the coeﬃcients of a
polynomial with real negative roots are log-concave functions of the roots. In other words,
the functions ai : Rn →R, deﬁned by the identity
sn + a1(λ)sn−1 + · · · + an−1(λ)s + an(λ) = (s −λ1)(s −λ2) · · · (s −λn),
are log-concave on −Rn
++.
Hint. The function
Sk(x) =
X
1≤i1<i2<···<ik≤n
xi1xi2 · · · xik,
with dom Sk ∈Rn
+ and 1 ≤k ≤n, is called the kth elementary symmetric function on
Rn. It can be shown that S1/k
k
is concave (see [ML57]).
3.51 [BL00, page 41] Let p be a polynomial on R, with all its roots real.
Show that it is
log-concave on any interval on which it is positive.
3.52 [MO79, §3.E.2] Log-convexity of moment functions. Suppose f : R →R is nonnegative
with R+ ⊆dom f. For x ≥0 deﬁne
φ(x) =
Z ∞
0
uxf(u) du.
Show that φ is a log-convex function. (If x is a positive integer, and f is a probability
density function, then φ(x) is the xth moment of the distribution.)
Use this to show that the Gamma function,
Γ(x) =
Z ∞
0
ux−1e−u du,
is log-convex for x ≥1.
3.53 Suppose x and y are independent random vectors in Rn, with log-concave probability
density functions f and g, respectively. Show that the probability density function of the
sum z = x + y is log-concave.
3.54 Log-concavity of Gaussian cumulative distribution function. The cumulative distribution
function of a Gaussian random variable,
f(x) =
1
√
2π
Z x
−∞
e−t2/2 dt,
is log-concave. This follows from the general result that the convolution of two log-concave
functions is log-concave. In this problem we guide you through a simple self-contained
proof that f is log-concave. Recall that f is log-concave if and only if f ′′(x)f(x) ≤f ′(x)2
for all x.
(a) Verify that f ′′(x)f(x) ≤f ′(x)2 for x ≥0. That leaves us the hard part, which is to
show the inequality for x < 0.
(b) Verify that for any t and x we have t2/2 ≥−x2/2 + xt.
(c) Using part (b) show that e−t2/2 ≤ex2/2−xt. Conclude that, for x < 0,
Z x
−∞
e−t2/2 dt ≤ex2/2
Z x
−∞
e−xt dt.
(d) Use part (c) to verify that f ′′(x)f(x) ≤f ′(x)2 for x ≤0.


## Page 18

124
3
Convex functions
3.55 Log-concavity of the cumulative distribution function of a log-concave probability density.
In this problem we extend the result of exercise 3.54. Let g(t) = exp(−h(t)) be a diﬀer-
entiable log-concave probability density function, and let
f(x) =
Z x
−∞
g(t) dt =
Z x
−∞
e−h(t) dt
be its cumulative distribution.
We will show that f is log-concave, i.e., it satisﬁes
f ′′(x)f(x) ≤(f ′(x))2 for all x.
(a) Express the derivatives of f in terms of the function h. Verify that f ′′(x)f(x) ≤
(f ′(x))2 if h′(x) ≥0.
(b) Assume that h′(x) < 0. Use the inequality
h(t) ≥h(x) + h′(x)(t −x)
(which follows from convexity of h), to show that
Z x
−∞
e−h(t) dt ≤e−h(x)
−h′(x).
Use this inequality to verify that f ′′(x)f(x) ≤(f ′(x))2 if h′(x) < 0.
3.56 More log-concave densities. Show that the following densities are log-concave.
(a) [MO79, page 493] The gamma density, deﬁned by
f(x) =
αλ
Γ(λ)xλ−1e−αx,
with dom f = R+. The parameters λ and α satisfy λ ≥1, α > 0.
(b) [MO79, page 306] The Dirichlet density
f(x) =
Γ(1T λ)
Γ(λ1) · · · Γ(λn+1)xλ1−1
1
· · · xλn−1
n
 
1 −
n
X
i=1
xi
!λn+1−1
with dom f = {x ∈Rn
++ | 1T x < 1}. The parameter λ satisﬁes λ ⪰1.
Convexity with respect to a generalized inequality
3.57 Show that the function f(X) = X−1 is matrix convex on Sn
++.
3.58 Schur complement. Suppose X ∈Sn partitioned as
X =

A
B
BT
C

,
where A ∈Sk. The Schur complement of X (with respect to A) is S = C −BT A−1B
(see §A.5.5). Show that the Schur complement, viewed as a function from Sn into Sn−k,
is matrix concave on Sn
++.
3.59 Second-order conditions for K-convexity. Let K ⊆Rm be a proper convex cone, with
associated generalized inequality ⪯K. Show that a twice diﬀerentiable function f : Rn →
Rm, with convex domain, is K-convex if and only if for all x ∈dom f and all y ∈Rn,
n
X
i,j=1
∂2f(x)
∂xi∂xj yiyj ⪰K 0,
i.e., the second derivative is a K-nonnegative bilinear form. (Here ∂2f/∂xi∂xj ∈Rm,
with components ∂2fk/∂xi∂xj, for k = 1, . . . , m; see §A.4.1.)


## Page 19

Exercises
125
3.60 Sublevel sets and epigraph of K-convex functions. Let K ⊆Rm be a proper convex cone
with associated generalized inequality ⪯K, and let f : Rn →Rm. For α ∈Rm, the
α-sublevel set of f (with respect to ⪯K) is deﬁned as
Cα = {x ∈Rn | f(x) ⪯K α}.
The epigraph of f, with respect to ⪯K, is deﬁned as the set
epiKf = {(x, t) ∈Rn+m | f(x) ⪯K t}.
Show the following:
(a) If f is K-convex, then its sublevel sets Cα are convex for all α.
(b) f is K-convex if and only if epiK f is a convex set.


## Page 20



## Page 21

Chapter 4
Convex optimization problems
4.1
Optimization problems
4.1.1
Basic terminology
We use the notation
minimize
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m
hi(x) = 0,
i = 1, . . . , p
(4.1)
to describe the problem of ﬁnding an x that minimizes f0(x) among all x that satisfy
the conditions fi(x) ≤0, i = 1, . . . , m, and hi(x) = 0, i = 1, . . . , p. We call x ∈Rn
the optimization variable and the function f0 : Rn →R the objective function or
cost function. The inequalities fi(x) ≤0 are called inequality constraints, and the
corresponding functions fi : Rn →R are called the inequality constraint functions.
The equations hi(x) = 0 are called the equality constraints, and the functions
hi : Rn →R are the equality constraint functions. If there are no constraints (i.e.,
m = p = 0) we say the problem (4.1) is unconstrained.
The set of points for which the objective and all constraint functions are deﬁned,
D =
m
\
i=0
dom fi ∩
p\
i=1
dom hi,
is called the domain of the optimization problem (4.1). A point x ∈D is feasible
if it satisﬁes the constraints fi(x) ≤0, i = 1, . . . , m, and hi(x) = 0, i = 1, . . . , p.
The problem (4.1) is said to be feasible if there exists at least one feasible point,
and infeasible otherwise. The set of all feasible points is called the feasible set or
the constraint set.
The optimal value p⋆of the problem (4.1) is deﬁned as
p⋆= inf {f0(x) | fi(x) ≤0, i = 1, . . . , m, hi(x) = 0, i = 1, . . . , p} .
We allow p⋆to take on the extended values ±∞. If the problem is infeasible, we
have p⋆= ∞(following the standard convention that the inﬁmum of the empty set


## Page 22

128
4
Convex optimization problems
is ∞). If there are feasible points xk with f0(xk) →−∞as k →∞, then p⋆= −∞,
and we say the problem (4.1) is unbounded below.
Optimal and locally optimal points
We say x⋆is an optimal point, or solves the problem (4.1), if x⋆is feasible and
f0(x⋆) = p⋆. The set of all optimal points is the optimal set, denoted
Xopt = {x | fi(x) ≤0, i = 1, . . . , m, hi(x) = 0, i = 1, . . . , p, f0(x) = p⋆}.
If there exists an optimal point for the problem (4.1), we say the optimal value
is attained or achieved, and the problem is solvable.
If Xopt is empty, we say
the optimal value is not attained or not achieved. (This always occurs when the
problem is unbounded below.)
A feasible point x with f0(x) ≤p⋆+ ǫ (where
ǫ > 0) is called ǫ-suboptimal, and the set of all ǫ-suboptimal points is called the
ǫ-suboptimal set for the problem (4.1).
We say a feasible point x is locally optimal if there is an R > 0 such that
f0(x) = inf{f0(z) | fi(z) ≤0, i = 1, . . . , m,
hi(z) = 0, i = 1, . . . , p, ∥z −x∥2 ≤R},
or, in other words, x solves the optimization problem
minimize
f0(z)
subject to
fi(z) ≤0,
i = 1, . . . , m
hi(z) = 0,
i = 1, . . . , p
∥z −x∥2 ≤R
with variable z. Roughly speaking, this means x minimizes f0 over nearby points
in the feasible set. The term ‘globally optimal’ is sometimes used for ‘optimal’
to distinguish between ‘locally optimal’ and ‘optimal’.
Throughout this book,
however, optimal will mean globally optimal.
If x is feasible and fi(x) = 0, we say the ith inequality constraint fi(x) ≤0 is
active at x. If fi(x) < 0, we say the constraint fi(x) ≤0 is inactive. (The equality
constraints are active at all feasible points.) We say that a constraint is redundant
if deleting it does not change the feasible set.
Example 4.1
We illustrate these deﬁnitions with a few simple unconstrained opti-
mization problems with variable x ∈R, and dom f0 = R++.
• f0(x) = 1/x: p⋆= 0, but the optimal value is not achieved.
• f0(x) = −log x: p⋆= −∞, so this problem is unbounded below.
• f0(x) = x log x: p⋆= −1/e, achieved at the (unique) optimal point x⋆= 1/e.
Feasibility problems
If the objective function is identically zero, the optimal value is either zero (if the
feasible set is nonempty) or ∞(if the feasible set is empty).
We call this the


## Page 23

4.1
Optimization problems
129
feasibility problem, and will sometimes write it as
ﬁnd
x
subject to
fi(x) ≤0,
i = 1, . . . , m
hi(x) = 0,
i = 1, . . . , p.
The feasibility problem is thus to determine whether the constraints are consistent,
and if so, ﬁnd a point that satisﬁes them.
4.1.2
Expressing problems in standard form
We refer to (4.1) as an optimization problem in standard form. In the standard
form problem we adopt the convention that the righthand side of the inequality
and equality constraints are zero. This can always be arranged by subtracting any
nonzero righthand side: we represent the equality constraint gi(x) = ˜gi(x), for
example, as hi(x) = 0, where hi(x) = gi(x) −˜gi(x). In a similar way we express
inequalities of the form fi(x) ≥0 as −fi(x) ≤0.
Example 4.2 Box constraints. Consider the optimization problem
minimize
f0(x)
subject to
li ≤xi ≤ui,
i = 1, . . . , n,
where x ∈Rn is the variable. The constraints are called variable bounds (since they
give lower and upper bounds for each xi) or box constraints (since the feasible set is
a box).
We can express this problem in standard form as
minimize
f0(x)
subject to
li −xi ≤0,
i = 1, . . . , n
xi −ui ≤0,
i = 1, . . . , n.
There are 2n inequality constraint functions:
fi(x) = li −xi,
i = 1, . . . , n,
and
fi(x) = xi−n −ui−n,
i = n + 1, . . . , 2n.
Maximization problems
We concentrate on the minimization problem by convention.
We can solve the
maximization problem
maximize
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m
hi(x) = 0,
i = 1, . . . , p
(4.2)


## Page 24

130
4
Convex optimization problems
by minimizing the function −f0 subject to the constraints. By this correspondence
we can deﬁne all the terms above for the maximization problem (4.2). For example
the optimal value of (4.2) is deﬁned as
p⋆= sup{f0(x) | fi(x) ≤0, i = 1, . . . , m, hi(x) = 0, i = 1, . . . , p},
and a feasible point x is ǫ-suboptimal if f0(x) ≥p⋆−ǫ. When the maximization
problem is considered, the objective is sometimes called the utility or satisfaction
level instead of the cost.
4.1.3
Equivalent problems
In this book we will use the notion of equivalence of optimization problems in an
informal way. We call two problems equivalent if from a solution of one, a solution
of the other is readily found, and vice versa. (It is possible, but complicated, to
give a formal deﬁnition of equivalence.)
As a simple example, consider the problem
minimize
˜f(x) = α0f0(x)
subject to
˜fi(x) = αifi(x) ≤0,
i = 1, . . . , m
˜hi(x) = βihi(x) = 0,
i = 1, . . . , p,
(4.3)
where αi > 0, i = 0, . . . , m, and βi̸ = 0, i = 1, . . . , p. This problem is obtained from
the standard form problem (4.1) by scaling the objective and inequality constraint
functions by positive constants, and scaling the equality constraint functions by
nonzero constants. As a result, the feasible sets of the problem (4.3) and the original
problem (4.1) are identical. A point x is optimal for the original problem (4.1) if
and only if it is optimal for the scaled problem (4.3), so we say the two problems are
equivalent. The two problems (4.1) and (4.3) are not, however, the same (unless
αi and βi are all equal to one), since the objective and constraint functions diﬀer.
We now describe some general transformations that yield equivalent problems.
Change of variables
Suppose φ : Rn →Rn is one-to-one, with image covering the problem domain D,
i.e., φ(dom φ) ⊇D. We deﬁne functions ˜fi and ˜hi as
˜fi(z) = fi(φ(z)),
i = 0, . . . , m,
˜hi(z) = hi(φ(z)),
i = 1, . . . , p.
Now consider the problem
minimize
˜f0(z)
subject to
˜fi(z) ≤0,
i = 1, . . . , m
˜hi(z) = 0,
i = 1, . . . , p,
(4.4)
with variable z. We say that the standard form problem (4.1) and the problem (4.4)
are related by the change of variable or substitution of variable x = φ(z).
The two problems are clearly equivalent: if x solves the problem (4.1), then
z = φ−1(x) solves the problem (4.4); if z solves the problem (4.4), then x = φ(z)
solves the problem (4.1).


## Page 25

4.1
Optimization problems
131
Transformation of objective and constraint functions
Suppose that ψ0 : R →R is monotone increasing, ψ1, . . . , ψm : R →R satisfy
ψi(u) ≤0 if and only if u ≤0, and ψm+1, . . . , ψm+p : R →R satisfy ψi(u) = 0 if
and only if u = 0. We deﬁne functions ˜fi and ˜hi as the compositions
˜fi(x) = ψi(fi(x)),
i = 0, . . . , m,
˜hi(x) = ψm+i(hi(x)),
i = 1, . . . , p.
Evidently the associated problem
minimize
˜f0(x)
subject to
˜fi(x) ≤0,
i = 1, . . . , m
˜hi(x) = 0,
i = 1, . . . , p
and the standard form problem (4.1) are equivalent; indeed, the feasible sets are
identical, and the optimal points are identical. (The example (4.3) above, in which
the objective and constraint functions are scaled by appropriate constants, is the
special case when all ψi are linear.)
Example 4.3
Least-norm and least-norm-squared problems.
As a simple example
consider the unconstrained Euclidean norm minimization problem
minimize
∥Ax −b∥2,
(4.5)
with variable x ∈Rn. Since the norm is always nonnegative, we can just as well solve
the problem
minimize
∥Ax −b∥2
2 = (Ax −b)T (Ax −b),
(4.6)
in which we minimize the square of the Euclidean norm. The problems (4.5) and (4.6)
are clearly equivalent; the optimal points are the same. The two problems are not
the same, however. For example, the objective in (4.5) is not diﬀerentiable at any
x with Ax −b = 0, whereas the objective in (4.6) is diﬀerentiable for all x (in fact,
quadratic).
Slack variables
One simple transformation is based on the observation that fi(x) ≤0 if and only if
there is an si ≥0 that satisﬁes fi(x) + si = 0. Using this transformation we obtain
the problem
minimize
f0(x)
subject to
si ≥0,
i = 1, . . . , m
fi(x) + si = 0,
i = 1, . . . , m
hi(x) = 0,
i = 1, . . . , p,
(4.7)
where the variables are x ∈Rn and s ∈Rm. This problem has n + m variables,
m inequality constraints (the nonnegativity constraints on si), and m + p equality
constraints. The new variable si is called the slack variable associated with the
original inequality constraint fi(x) ≤0. Introducing slack variables replaces each
inequality constraint with an equality constraint, and a nonnegativity constraint.
The problem (4.7) is equivalent to the original standard form problem (4.1).
Indeed, if (x, s) is feasible for the problem (4.7), then x is feasible for the original


## Page 26

132
4
Convex optimization problems
problem, since si = −fi(x) ≥0. Conversely, if x is feasible for the original problem,
then (x, s) is feasible for the problem (4.7), where we take si = −fi(x). Similarly,
x is optimal for the original problem (4.1) if and only if (x, s) is optimal for the
problem (4.7), where si = −fi(x).
Eliminating equality constraints
If we can explicitly parametrize all solutions of the equality constraints
hi(x) = 0,
i = 1, . . . , p,
(4.8)
using some parameter z ∈Rk, then we can eliminate the equality constraints
from the problem, as follows. Suppose the function φ : Rk →Rn is such that
x satisﬁes (4.8) if and only if there is some z ∈Rk such that x = φ(z).
The
optimization problem
minimize
˜f0(z) = f0(φ(z))
subject to
˜fi(z) = fi(φ(z)) ≤0,
i = 1, . . . , m
is then equivalent to the original problem (4.1). This transformed problem has
variable z ∈Rk, m inequality constraints, and no equality constraints.
If z is
optimal for the transformed problem, then x = φ(z) is optimal for the original
problem.
Conversely, if x is optimal for the original problem, then (since x is
feasible) there is at least one z such that x = φ(z). Any such z is optimal for the
transformed problem.
Eliminating linear equality constraints
The process of eliminating variables can be described more explicitly, and easily
carried out numerically, when the equality constraints are all linear, i.e., have the
form Ax = b. If Ax = b is inconsistent, i.e., b̸ ∈R(A), then the original problem is
infeasible. Assuming this is not the case, let x0 denote any solution of the equality
constraints. Let F ∈Rn×k be any matrix with R(F) = N(A), so the general
solution of the linear equations Ax = b is given by Fz + x0, where z ∈Rk. (We
can choose F to be full rank, in which case we have k = n −rank A.)
Substituting x = Fz + x0 into the original problem yields the problem
minimize
f0(Fz + x0)
subject to
fi(Fz + x0) ≤0,
i = 1, . . . , m,
with variable z, which is equivalent to the original problem, has no equality con-
straints, and rank A fewer variables.
Introducing equality constraints
We can also introduce equality constraints and new variables into a problem. In-
stead of describing the general case, which is complicated and not very illuminating,
we give a typical example that will be useful later. Consider the problem
minimize
f0(A0x + b0)
subject to
fi(Aix + bi) ≤0,
i = 1, . . . , m
hi(x) = 0,
i = 1, . . . , p,


## Page 27

4.1
Optimization problems
133
where x ∈Rn, Ai ∈Rki×n, and fi : Rki →R. In this problem the objective
and constraint functions are given as compositions of the functions fi with aﬃne
transformations deﬁned by Aix + bi.
We introduce new variables yi ∈Rki, as well as new equality constraints yi =
Aix + bi, for i = 0, . . . , m, and form the equivalent problem
minimize
f0(y0)
subject to
fi(yi) ≤0,
i = 1, . . . , m
yi = Aix + bi,
i = 0, . . . , m
hi(x) = 0,
i = 1, . . . , p.
This problem has k0 + · · · + km new variables,
y0 ∈Rk0,
. . . ,
ym ∈Rkm,
and k0 + · · · + km new equality constraints,
y0 = A0x + b0,
. . . ,
ym = Amx + bm.
The objective and inequality constraints in this problem are independent, i.e., in-
volve diﬀerent optimization variables.
Optimizing over some variables
We always have
inf
x,y f(x, y) = inf
x
˜f(x)
where ˜f(x) = infy f(x, y). In other words, we can always minimize a function by
ﬁrst minimizing over some of the variables, and then minimizing over the remaining
ones. This simple and general principle can be used to transform problems into
equivalent forms. The general case is cumbersome to describe and not illuminating,
so we describe instead an example.
Suppose the variable x ∈Rn is partitioned as x = (x1, x2), with x1 ∈Rn1,
x2 ∈Rn2, and n1 + n2 = n. We consider the problem
minimize
f0(x1, x2)
subject to
fi(x1) ≤0,
i = 1, . . . , m1
˜fi(x2) ≤0,
i = 1, . . . , m2,
(4.9)
in which the constraints are independent, in the sense that each constraint function
depends on x1 or x2. We ﬁrst minimize over x2. Deﬁne the function ˜f0 of x1 by
˜f0(x1) = inf{f0(x1, z) | ˜fi(z) ≤0, i = 1, . . . , m2}.
The problem (4.9) is then equivalent to
minimize
˜f0(x1)
subject to
fi(x1) ≤0,
i = 1, . . . , m1.
(4.10)


## Page 28

134
4
Convex optimization problems
Example 4.4
Minimizing a quadratic function with constraints on some variables.
Consider a problem with strictly convex quadratic objective, with some of the vari-
ables unconstrained:
minimize
xT
1 P11x1 + 2xT
1 P12x2 + xT
2 P22x2
subject to
fi(x1) ≤0,
i = 1, . . . , m,
where P11 and P22 are symmetric. Here we can analytically minimize over x2:
inf
x2
 xT
1 P11x1 + 2xT
1 P12x2 + xT
2 P22x2

= xT
1
 P11 −P12P −1
22 P T
12

x1
(see §A.5.5). Therefore the original problem is equivalent to
minimize
xT
1
 P11 −P12P −1
22 P T
12

x1
subject to
fi(x1) ≤0,
i = 1, . . . , m.
Epigraph problem form
The epigraph form of the standard problem (4.1) is the problem
minimize
t
subject to
f0(x) −t ≤0
fi(x) ≤0,
i = 1, . . . , m
hi(x) = 0,
i = 1, . . . , p,
(4.11)
with variables x ∈Rn and t ∈R. We can easily see that it is equivalent to the
original problem: (x, t) is optimal for (4.11) if and only if x is optimal for (4.1)
and t = f0(x). Note that the objective function of the epigraph form problem is a
linear function of the variables x, t.
The epigraph form problem (4.11) can be interpreted geometrically as an op-
timization problem in the ‘graph space’ (x, t): we minimize t over the epigraph of
f0, subject to the constraints on x. This is illustrated in ﬁgure 4.1.
Implicit and explicit constraints
By a simple trick already mentioned in §3.1.2, we can include any of the constraints
implicitly in the objective function, by redeﬁning its domain. As an extreme ex-
ample, the standard form problem can be expressed as the unconstrained problem
minimize
F(x),
(4.12)
where we deﬁne the function F as f0, but with domain restricted to the feasible
set:
dom F = {x ∈dom f0 | fi(x) ≤0, i = 1, . . . , m, hi(x) = 0, i = 1, . . . , p},
and F(x) = f0(x) for x ∈dom F. (Equivalently, we can deﬁne F(x) to have value
∞for x not feasible.) The problems (4.1) and (4.12) are clearly equivalent: they
have the same feasible set, optimal points, and optimal value.
Of course this transformation is nothing more than a notational trick. Making
the constraints implicit has not made the problem any easier to analyze or solve,


## Page 29

4.1
Optimization problems
135
t
x
epi f0
(x⋆, t⋆)
Figure 4.1 Geometric interpretation of epigraph form problem, for a prob-
lem with no constraints. The problem is to ﬁnd the point in the epigraph
(shown shaded) that minimizes t, i.e., the ‘lowest’ point in the epigraph.
The optimal point is (x⋆, t⋆).
even though the problem (4.12) is, at least nominally, unconstrained. In some ways
the transformation makes the problem more diﬃcult. Suppose, for example, that
the objective f0 in the original problem is diﬀerentiable, so in particular its domain
is open. The restricted objective function F is probably not diﬀerentiable, since
its domain is likely not to be open.
Conversely, we will encounter problems with implicit constraints, which we can
then make explicit. As a simple example, consider the unconstrained problem
minimize
f(x)
(4.13)
where the function f is given by
f(x) =

xT x
Ax = b
∞
otherwise.
Thus, the objective function is equal to the quadratic form xT x on the aﬃne set
deﬁned by Ax = b, and ∞oﬀthe aﬃne set. Since we can clearly restrict our
attention to points that satisfy Ax = b, we say that the problem (4.13) has an
implicit equality constraint Ax = b hidden in the objective.
We can make the
implicit equality constraint explicit, by forming the equivalent problem
minimize
xT x
subject to
Ax = b.
(4.14)
While the problems (4.13) and (4.14) are clearly equivalent, they are not the same.
The problem (4.13) is unconstrained, but its objective function is not diﬀerentiable.
The problem (4.14), however, has an equality constraint, but its objective and
constraint functions are diﬀerentiable.


## Page 30

136
4
Convex optimization problems
4.1.4
Parameter and oracle problem descriptions
For a problem in the standard form (4.1), there is still the question of how the
objective and constraint functions are speciﬁed.
In many cases these functions
have some analytical or closed form, i.e., are given by a formula or expression that
involves the variable x as well as some parameters.
Suppose, for example, the
objective is quadratic, so it has the form f0(x) = (1/2)xT Px + qT x + r. To specify
the objective function we give the coeﬃcients (also called problem parameters or
problem data) P ∈Sn, q ∈Rn, and r ∈R. We call this a parameter problem
description, since the speciﬁc problem to be solved (i.e., the problem instance) is
speciﬁed by giving the values of the parameters that appear in the expressions for
the objective and constraint functions.
In other cases the objective and constraint functions are described by oracle
models (which are also called black box or subroutine models). In an oracle model,
we do not know f explicitly, but can evaluate f(x) (and usually also some deriva-
tives) at any x ∈dom f. This is referred to as querying the oracle, and is usually
associated with some cost, such as time. We are also given some prior information
about the function, such as convexity and a bound on its values. As a concrete
example of an oracle model, consider an unconstrained problem, in which we are
to minimize the function f. The function value f(x) and its gradient ∇f(x) are
evaluated in a subroutine. We can call the subroutine at any x ∈dom f, but do
not have access to its source code. Calling the subroutine with argument x yields
(when the subroutine returns) f(x) and ∇f(x). Note that in the oracle model,
we never really know the function; we only know the function value (and some
derivatives) at the points where we have queried the oracle. (We also know some
given prior information about the function, such as diﬀerentiability and convexity.)
In practice the distinction between a parameter and oracle problem description
is not so sharp. If we are given a parameter problem description, we can construct
an oracle for it, which simply evaluates the required functions and derivatives when
queried. Most of the algorithms we study in part III work with an oracle model, but
can be made more eﬃcient when they are restricted to solve a speciﬁc parametrized
family of problems.
4.2
Convex optimization
4.2.1
Convex optimization problems in standard form
A convex optimization problem is one of the form
minimize
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m
aT
i x = bi,
i = 1, . . . , p,
(4.15)
where f0, . . . , fm are convex functions. Comparing (4.15) with the general standard
form problem (4.1), the convex problem has three additional requirements:


## Page 31

4.2
Convex optimization
137
• the objective function must be convex,
• the inequality constraint functions must be convex,
• the equality constraint functions hi(x) = aT
i x −bi must be aﬃne.
We immediately note an important property: The feasible set of a convex optimiza-
tion problem is convex, since it is the intersection of the domain of the problem
D =
m
\
i=0
dom fi,
which is a convex set, with m (convex) sublevel sets {x | fi(x) ≤0} and p hyper-
planes {x | aT
i x = bi}. (We can assume without loss of generality that ai̸ = 0: if
ai = 0 and bi = 0 for some i, then the ith equality constraint can be deleted; if
ai = 0 and bi̸ = 0, the ith equality constraint is inconsistent, and the problem is in-
feasible.) Thus, in a convex optimization problem, we minimize a convex objective
function over a convex set.
If f0 is quasiconvex instead of convex, we say the problem (4.15) is a (standard
form) quasiconvex optimization problem.
Since the sublevel sets of a convex or
quasiconvex function are convex, we conclude that for a convex or quasiconvex
optimization problem the ǫ-suboptimal sets are convex. In particular, the optimal
set is convex. If the objective is strictly convex, then the optimal set contains at
most one point.
Concave maximization problems
With a slight abuse of notation, we will also refer to
maximize
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m
aT
i x = bi,
i = 1, . . . , p,
(4.16)
as a convex optimization problem if the objective function f0 is concave, and the
inequality constraint functions f1, . . . , fm are convex. This concave maximization
problem is readily solved by minimizing the convex objective function −f0. All
of the results, conclusions, and algorithms that we describe for the minimization
problem are easily transposed to the maximization case.
In a similar way the
maximization problem (4.16) is called quasiconvex if f0 is quasiconcave.
Abstract form convex optimization problem
It is important to note a subtlety in our deﬁnition of convex optimization problem.
Consider the example with x ∈R2,
minimize
f0(x) = x2
1 + x2
2
subject to
f1(x) = x1/(1 + x2
2) ≤0
h1(x) = (x1 + x2)2 = 0,
(4.17)
which is in the standard form (4.1). This problem is not a convex optimization
problem in standard form since the equality constraint function h1 is not aﬃne, and


## Page 32

138
4
Convex optimization problems
the inequality constraint function f1 is not convex. Nevertheless the feasible set,
which is {x | x1 ≤0, x1 + x2 = 0}, is convex. So although in this problem we are
minimizing a convex function f0 over a convex set, it is not a convex optimization
problem by our deﬁnition.
Of course, the problem is readily reformulated as
minimize
f0(x) = x2
1 + x2
2
subject to
˜f1(x) = x1 ≤0
˜h1(x) = x1 + x2 = 0,
(4.18)
which is in standard convex optimization form, since f0 and ˜f1 are convex, and ˜h1
is aﬃne.
Some authors use the term abstract convex optimization problem to describe the
(abstract) problem of minimizing a convex function over a convex set. Using this
terminology, the problem (4.17) is an abstract convex optimization problem. We
will not use this terminology in this book. For us, a convex optimization problem is
not just one of minimizing a convex function over a convex set; it is also required
that the feasible set be described speciﬁcally by a set of inequalities involving
convex functions, and a set of linear equality constraints. The problem (4.17) is
not a convex optimization problem, but the problem (4.18) is a convex optimization
problem. (The two problems are, however, equivalent.)
Our adoption of the stricter deﬁnition of convex optimization problem does not
matter much in practice. To solve the abstract problem of minimizing a convex
function over a convex set, we need to ﬁnd a description of the set in terms of
convex inequalities and linear equality constraints. As the example above suggests,
this is usually straightforward.
4.2.2
Local and global optima
A fundamental property of convex optimization problems is that any locally optimal
point is also (globally) optimal. To see this, suppose that x is locally optimal for
a convex optimization problem, i.e., x is feasible and
f0(x) = inf{f0(z) | z feasible, ∥z −x∥2 ≤R},
(4.19)
for some R > 0. Now suppose that x is not globally optimal, i.e., there is a feasible
y such that f0(y) < f0(x). Evidently ∥y −x∥2 > R, since otherwise f0(x) ≤f0(y).
Consider the point z given by
z = (1 −θ)x + θy,
θ =
R
2∥y −x∥2
.
Then we have ∥z −x∥2 = R/2 < R, and by convexity of the feasible set, z is
feasible. By convexity of f0 we have
f0(z) ≤(1 −θ)f0(x) + θf0(y) < f0(x),
which contradicts (4.19). Hence there exists no feasible y with f0(y) < f0(x), i.e.,
x is globally optimal.


## Page 33

4.2
Convex optimization
139
−∇f0(x)
X
x
Figure 4.2 Geometric interpretation of the optimality condition (4.21). The
feasible set X is shown shaded. Some level curves of f0 are shown as dashed
lines.
The point x is optimal: −∇f0(x) deﬁnes a supporting hyperplane
(shown as a solid line) to X at x.
It is not true that locally optimal points of quasiconvex optimization problems
are globally optimal; see §4.2.5.
4.2.3
An optimality criterion for diﬀerentiable f0
Suppose that the objective f0 in a convex optimization problem is diﬀerentiable,
so that for all x, y ∈dom f0,
f0(y) ≥f0(x) + ∇f0(x)T (y −x)
(4.20)
(see §3.1.3). Let X denote the feasible set, i.e.,
X = {x | fi(x) ≤0, i = 1, . . . , m, hi(x) = 0, i = 1, . . . , p}.
Then x is optimal if and only if x ∈X and
∇f0(x)T (y −x) ≥0 for all y ∈X.
(4.21)
This optimality criterion can be understood geometrically: If ∇f0(x)̸ = 0, it means
that −∇f0(x) deﬁnes a supporting hyperplane to the feasible set at x (see ﬁg-
ure 4.2).
Proof of optimality condition
First suppose x ∈X and satisﬁes (4.21).
Then if y ∈X we have, by (4.20),
f0(y) ≥f0(x). This shows x is an optimal point for (4.1).
Conversely, suppose x is optimal, but the condition (4.21) does not hold, i.e.,
for some y ∈X we have
∇f0(x)T (y −x) < 0.


## Page 34

140
4
Convex optimization problems
Consider the point z(t) = ty +(1−t)x, where t ∈[0, 1] is a parameter. Since z(t) is
on the line segment between x and y, and the feasible set is convex, z(t) is feasible.
We claim that for small positive t we have f0(z(t)) < f0(x), which will prove that
x is not optimal. To show this, note that
d
dtf0(z(t))

t=0
= ∇f0(x)T (y −x) < 0,
so for small positive t, we have f0(z(t)) < f0(x).
We will pursue the topic of optimality conditions in much more depth in chap-
ter 5, but here we examine a few simple examples.
Unconstrained problems
For an unconstrained problem (i.e., m = p = 0), the condition (4.21) reduces to
the well known necessary and suﬃcient condition
∇f0(x) = 0
(4.22)
for x to be optimal. While we have already seen this optimality condition, it is
useful to see how it follows from (4.21). Suppose x is optimal, which means here
that x ∈dom f0, and for all feasible y we have ∇f0(x)T (y −x) ≥0. Since f0 is
diﬀerentiable, its domain is (by deﬁnition) open, so all y suﬃciently close to x are
feasible. Let us take y = x −t∇f0(x), where t ∈R is a parameter. For t small and
positive, y is feasible, and so
∇f0(x)T (y −x) = −t∥∇f0(x)∥2
2 ≥0,
from which we conclude ∇f0(x) = 0.
There are several possible situations, depending on the number of solutions
of (4.22). If there are no solutions of (4.22), then there are no optimal points; the
optimal value of the problem is not attained. Here we can distinguish between
two cases: the problem is unbounded below, or the optimal value is ﬁnite, but not
attained. On the other hand we can have multiple solutions of the equation (4.22),
in which case each such solution is a minimizer of f0.
Example 4.5 Unconstrained quadratic optimization. Consider the problem of mini-
mizing the quadratic function
f0(x) = (1/2)xT Px + qT x + r,
where P ∈Sn
+ (which makes f0 convex). The necessary and suﬃcient condition for
x to be a minimizer of f0 is
∇f0(x) = Px + q = 0.
Several cases can occur, depending on whether this (linear) equation has no solutions,
one solution, or many solutions.
• If q̸ ∈R(P), then there is no solution. In this case f0 is unbounded below.
• If P ≻0 (which is the condition for f0 to be strictly convex), then there is a
unique minimizer, x⋆= −P −1q.


## Page 35

4.2
Convex optimization
141
• If P is singular, but q ∈R(P), then the set of optimal points is the (aﬃne) set
Xopt = −P †q + N(P), where P † denotes the pseudo-inverse of P (see §A.5.4).
Example 4.6 Analytic centering. Consider the (unconstrained) problem of minimiz-
ing the (convex) function f0 : Rn →R, deﬁned as
f0(x) = −
m
X
i=1
log(bi −aT
i x),
dom f0 = {x | Ax ≺b},
where aT
1 , . . . , aT
m are the rows of A. The function f0 is diﬀerentiable, so the necessary
and suﬃcient conditions for x to be optimal are
Ax ≺b,
∇f0(x) =
m
X
i=1
1
bi −aT
i xai = 0.
(4.23)
(The condition Ax ≺b is just x ∈dom f0.) If Ax ≺b is infeasible, then the domain
of f0 is empty. Assuming Ax ≺b is feasible, there are still several possible cases (see
exercise 4.2):
• There are no solutions of (4.23), and hence no optimal points for the problem.
This occurs if and only if f0 is unbounded below.
• There are many solutions of (4.23).
In this case it can be shown that the
solutions form an aﬃne set.
• There is a unique solution of (4.23), i.e., a unique minimizer of f0. This occurs
if and only if the open polyhedron {x | Ax ≺b} is nonempty and bounded.
Problems with equality constraints only
Consider the case where there are equality constraints but no inequality constraints,
i.e.,
minimize
f0(x)
subject to
Ax = b.
Here the feasible set is aﬃne.
We assume that it is nonempty; otherwise the
problem is infeasible. The optimality condition for a feasible x is that
∇f0(x)T (y −x) ≥0
must hold for all y satisfying Ay = b. Since x is feasible, every feasible y has the
form y = x + v for some v ∈N(A). The optimality condition can therefore be
expressed as:
∇f0(x)T v ≥0 for all v ∈N(A).
If a linear function is nonnegative on a subspace, then it must be zero on the
subspace, so it follows that ∇f0(x)T v = 0 for all v ∈N(A). In other words,
∇f0(x) ⊥N(A).


## Page 36

142
4
Convex optimization problems
Using the fact that N(A)⊥= R(AT ), this optimality condition can be expressed
as ∇f0(x) ∈R(AT ), i.e., there exists a ν ∈Rp such that
∇f0(x) + AT ν = 0.
Together with the requirement Ax = b (i.e., that x is feasible), this is the classical
Lagrange multiplier optimality condition, which we will study in greater detail in
chapter 5.
Minimization over the nonnegative orthant
As another example we consider the problem
minimize
f0(x)
subject to
x ⪰0,
where the only inequality constraints are nonnegativity constraints on the variables.
The optimality condition (4.21) is then
x ⪰0,
∇f0(x)T (y −x) ≥0 for all y ⪰0.
The term ∇f0(x)T y, which is a linear function of y, is unbounded below on y ⪰0,
unless we have ∇f0(x) ⪰0. The condition then reduces to −∇f0(x)T x ≥0. But
x ⪰0 and ∇f0(x) ⪰0, so we must have ∇f0(x)T x = 0, i.e.,
n
X
i=1
(∇f0(x))ixi = 0.
Now each of the terms in this sum is the product of two nonnegative numbers, so
we conclude that each term must be zero, i.e., (∇f0(x))i xi = 0 for i = 1, . . . , n.
The optimality condition can therefore be expressed as
x ⪰0,
∇f0(x) ⪰0,
xi (∇f0(x))i = 0,
i = 1, . . . , n.
The last condition is called complementarity, since it means that the sparsity pat-
terns (i.e., the set of indices corresponding to nonzero components) of the vectors x
and ∇f0(x) are complementary (i.e., have empty intersection). We will encounter
complementarity conditions again in chapter 5.
4.2.4
Equivalent convex problems
It is useful to see which of the transformations described in §4.1.3 preserve convex-
ity.
Eliminating equality constraints
For a convex problem the equality constraints must be linear, i.e., of the form
Ax = b. In this case they can be eliminated by ﬁnding a particular solution x0 of


## Page 37

4.2
Convex optimization
143
Ax = b, and a matrix F whose range is the nullspace of A, which results in the
problem
minimize
f0(Fz + x0)
subject to
fi(Fz + x0) ≤0,
i = 1, . . . , m,
with variable z. Since the composition of a convex function with an aﬃne func-
tion is convex, eliminating equality constraints preserves convexity of a problem.
Moreover, the process of eliminating equality constraints (and reconstructing the
solution of the original problem from the solution of the transformed problem)
involves standard linear algebra operations.
At least in principle, this means we can restrict our attention to convex opti-
mization problems which have no equality constraints. In many cases, however, it
is better to retain the equality constraints, since eliminating them can make the
problem harder to understand and analyze, or ruin the eﬃciency of an algorithm
that solves it. This is true, for example, when the variable x has very large dimen-
sion, and eliminating the equality constraints would destroy sparsity or some other
useful structure of the problem.
Introducing equality constraints
We can introduce new variables and equality constraints into a convex optimization
problem, provided the equality constraints are linear, and the resulting problem
will also be convex. For example, if an objective or constraint function has the form
fi(Aix + bi), where Ai ∈Rki×n, we can introduce a new variable yi ∈Rki, replace
fi(Aix + bi) with fi(yi), and add the linear equality constraint yi = Aix + bi.
Slack variables
By introducing slack variables we have the new constraints fi(x) + si = 0. Since
equality constraint functions must be aﬃne in a convex problem, we must have fi
aﬃne. In other words: introducing slack variables for linear inequalities preserves
convexity of a problem.
Epigraph problem form
The epigraph form of the convex optimization problem (4.15) is
minimize
t
subject to
f0(x) −t ≤0
fi(x) ≤0,
i = 1, . . . , m
aT
i x = bi,
i = 1, . . . , p.
The objective is linear (hence convex) and the new constraint function f0(x) −t is
also convex in (x, t), so the epigraph form problem is convex as well.
It is sometimes said that a linear objective is universal for convex optimization,
since any convex optimization problem is readily transformed to one with linear
objective. The epigraph form of a convex problem has several practical uses. By
assuming the objective of a convex optimization problem is linear, we can simplify
theoretical analysis.
It can also simplify algorithm development, since an algo-
rithm that solves convex optimization problems with linear objective can, using


## Page 38

144
4
Convex optimization problems
the transformation above, solve any convex optimization problem (provided it can
handle the constraint f0(x) −t ≤0).
Minimizing over some variables
Minimizing a convex function over some variables preserves convexity. Therefore,
if f0 in (4.9) is jointly convex in x1 and x2, and fi, i = 1, . . . , m1, and ˜fi, i =
1, . . . , m2, are convex, then the equivalent problem (4.10) is convex.
4.2.5
Quasiconvex optimization
Recall that a quasiconvex optimization problem has the standard form
minimize
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m
Ax = b,
(4.24)
where the inequality constraint functions f1, . . . , fm are convex, and the objective
f0 is quasiconvex (instead of convex, as in a convex optimization problem). (Qua-
siconvex constraint functions can be replaced with equivalent convex constraint
functions, i.e., constraint functions that are convex and have the same 0-sublevel
set, as in §3.4.5.)
In this section we point out some basic diﬀerences between convex and quasicon-
vex optimization problems, and also show how solving a quasiconvex optimization
problem can be reduced to solving a sequence of convex optimization problems.
Locally optimal solutions and optimality conditions
The most important diﬀerence between convex and quasiconvex optimization is
that a quasiconvex optimization problem can have locally optimal solutions that
are not (globally) optimal. This phenomenon can be seen even in the simple case
of unconstrained minimization of a quasiconvex function on R, such as the one
shown in ﬁgure 4.3.
Nevertheless, a variation of the optimality condition (4.21) given in §4.2.3 does
hold for quasiconvex optimization problems with diﬀerentiable objective function.
Let X denote the feasible set for the quasiconvex optimization problem (4.24). It
follows from the ﬁrst-order condition for quasiconvexity (3.20) that x is optimal if
x ∈X,
∇f0(x)T (y −x) > 0 for all y ∈X \ {x}.
(4.25)
There are two important diﬀerences between this criterion and the analogous
one (4.21) for convex optimization:
• The condition (4.25) is only suﬃcient for optimality; simple examples show
that it need not hold for an optimal point. In contrast, the condition (4.21)
is necessary and suﬃcient for x to solve the convex problem.
• The condition (4.25) requires the gradient of f0 to be nonzero, whereas the
condition (4.21) does not. Indeed, when ∇f0(x) = 0 in the convex case, the
condition (4.21) is satisﬁed, and x is optimal.


## Page 39

4.2
Convex optimization
145
(x, f(x))
Figure 4.3 A quasiconvex function f on R, with a locally optimal point x
that is not globally optimal. This example shows that the simple optimality
condition f ′(x) = 0, valid for convex functions, does not hold for quasiconvex
functions.
Quasiconvex optimization via convex feasibility problems
One general approach to quasiconvex optimization relies on the representation of
the sublevel sets of a quasiconvex function via a family of convex inequalities, as
described in §3.4.5. Let φt : Rn →R, t ∈R, be a family of convex functions that
satisfy
f0(x) ≤t ⇐⇒φt(x) ≤0,
and also, for each x, φt(x) is a nonincreasing function of t, i.e., φs(x) ≤φt(x)
whenever s ≥t.
Let p⋆denote the optimal value of the quasiconvex optimization problem (4.24).
If the feasibility problem
ﬁnd
x
subject to
φt(x) ≤0
fi(x) ≤0,
i = 1, . . . , m
Ax = b,
(4.26)
is feasible, then we have p⋆≤t. Conversely, if the problem (4.26) is infeasible, then
we can conclude p⋆≥t. The problem (4.26) is a convex feasibility problem, since
the inequality constraint functions are all convex, and the equality constraints
are linear.
Thus, we can check whether the optimal value p⋆of a quasiconvex
optimization problem is less than or more than a given value t by solving the
convex feasibility problem (4.26). If the convex feasibility problem is feasible then
we have p⋆≤t, and any feasible point x is feasible for the quasiconvex problem
and satisﬁes f0(x) ≤t. If the convex feasibility problem is infeasible, then we know
that p⋆≥t.
This observation can be used as the basis of a simple algorithm for solving the
quasiconvex optimization problem (4.24) using bisection, solving a convex feasi-
bility problem at each step. We assume that the problem is feasible, and start
with an interval [l, u] known to contain the optimal value p⋆. We then solve the
convex feasibility problem at its midpoint t = (l + u)/2, to determine whether the


## Page 40

146
4
Convex optimization problems
optimal value is in the lower or upper half of the interval, and update the interval
accordingly. This produces a new interval, which also contains the optimal value,
but has half the width of the initial interval. This is repeated until the width of
the interval is small enough:
Algorithm 4.1 Bisection method for quasiconvex optimization.
given l ≤p⋆, u ≥p⋆, tolerance ǫ > 0.
repeat
1. t := (l + u)/2.
2. Solve the convex feasibility problem (4.26).
3. if (4.26) is feasible, u := t;
else l := t.
until u −l ≤ǫ.
The interval [l, u] is guaranteed to contain p⋆, i.e., we have l ≤p⋆≤u at
each step. In each iteration the interval is divided in two, i.e., bisected, so the
length of the interval after k iterations is 2−k(u −l), where u −l is the length of
the initial interval. It follows that exactly ⌈log2((u −l)/ǫ)⌉iterations are required
before the algorithm terminates. Each step involves solving the convex feasibility
problem (4.26).
4.3
Linear optimization problems
When the objective and constraint functions are all aﬃne, the problem is called a
linear program (LP). A general linear program has the form
minimize
cT x + d
subject to
Gx ⪯h
Ax = b,
(4.27)
where G ∈Rm×n and A ∈Rp×n. Linear programs are, of course, convex opti-
mization problems.
It is common to omit the constant d in the objective function, since it does not
aﬀect the optimal (or feasible) set. Since we can maximize an aﬃne objective cT x+
d, by minimizing −cT x −d (which is still convex), we also refer to a maximization
problem with aﬃne objective and constraint functions as an LP.
The geometric interpretation of an LP is illustrated in ﬁgure 4.4. The feasible
set of the LP (4.27) is a polyhedron P; the problem is to minimize the aﬃne
function cT x + d (or, equivalently, the linear function cT x) over P.
Standard and inequality form linear programs
Two special cases of the LP (4.27) are so widely encountered that they have been
given separate names. In a standard form LP the only inequalities are componen-
