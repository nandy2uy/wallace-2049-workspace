# temp_chunk_280_to_320



## Page 1

5.9
Generalized inequalities
267
Complementary slackness
Assume that the primal and dual optimal values are equal, and attained at the
optimal points x⋆, λ⋆, ν⋆. As in §5.5.2, the complementary slackness conditions
follow directly from the equality f0(x⋆) = g(λ⋆, ν⋆), along with the deﬁnition of g.
We have
f0(x⋆)
=
g(λ⋆, ν⋆)
≤
f0(x⋆) +
m
X
i=1
λ⋆
i
T fi(x⋆) +
p
X
i=1
ν⋆
i hi(x⋆)
≤
f0(x⋆),
and therefore we conclude that x⋆minimizes L(x, λ⋆, ν⋆), and also that the two
sums in the second line are zero. Since the second sum is zero (since x⋆satisﬁes
the equality constraints), we have Pm
i=1 λ⋆
i
T fi(x⋆) = 0. Since each term in this
sum is nonpositive, we conclude that
λ⋆
i
T fi(x⋆) = 0,
i = 1, . . . , m,
(5.94)
which generalizes the complementary slackness condition (5.48). From (5.94) we
can conclude that
λ⋆
i ≻K∗
i 0 =⇒fi(x⋆) = 0,
fi(x⋆) ≺Ki 0, =⇒λ⋆
i = 0.
However, in contrast to problems with scalar inequalities, it is possible to sat-
isfy (5.94) with λ⋆
i̸ = 0 and fi(x⋆)̸ = 0.
KKT conditions
Now we add the assumption that the functions fi, hi are diﬀerentiable, and gener-
alize the KKT conditions of §5.5.3 to problems with generalized inequalities. Since
x⋆minimizes L(x, λ⋆, ν⋆), its gradient with respect to x vanishes at x⋆:
∇f0(x⋆) +
m
X
i=1
Dfi(x⋆)T λ⋆
i +
p
X
i=1
ν⋆
i ∇hi(x⋆) = 0,
where Dfi(x⋆) ∈Rki×n is the derivative of fi evaluated at x⋆(see §A.4.1). Thus,
if strong duality holds, any primal optimal x⋆and any dual optimal (λ⋆, ν⋆) must
satisfy the optimality conditions (or KKT conditions)
fi(x⋆)
⪯Ki
0,
i = 1, . . . , m
hi(x⋆)
=
0,
i = 1, . . . , p
λ⋆
i
⪰K∗
i
0,
i = 1, . . . , m
λ⋆
i
T fi(x⋆)
=
0,
i = 1, . . . , m
∇f0(x⋆) + Pm
i=1 Dfi(x⋆)T λ⋆
i + Pp
i=1 ν⋆
i ∇hi(x⋆)
=
0.
(5.95)
If the primal problem is convex, the converse also holds, i.e., the conditions (5.95)
are suﬃcient conditions for optimality of x⋆, (λ⋆, ν⋆).


## Page 2

268
5
Duality
5.9.3
Perturbation and sensitivity analysis
The results of §5.6 can be extended to problems involving generalized inequalities.
We consider the associated perturbed version of the problem,
minimize
f0(x)
subject to
fi(x) ⪯Ki ui,
i = 1, . . . , m
hi(x) = vi,
i = 1, . . . , p,
where ui ∈Rki, and v ∈Rp.
We deﬁne p⋆(u, v) as the optimal value of the
perturbed problem. As in the case with scalar inequalities, p⋆is a convex function
when the original problem is convex.
Now let (λ⋆, ν⋆) be optimal for the dual of the original (unperturbed) problem,
which we assume has zero duality gap. Then for all u and v we have
p⋆(u, v) ≥p⋆−
m
X
i=1
λ⋆
i
T ui −ν⋆T v,
the analog of the global sensitivity inequality (5.57). The local sensitivity result
holds as well: If p⋆(u, v) is diﬀerentiable at u = 0, v = 0, then the optimal dual
variables λ⋆
i satisﬁes
λ⋆
i = −∇uip⋆(0, 0),
the analog of (5.58).
Example 5.13 Semideﬁnite program in inequality form. We consider a semideﬁnite
program in inequality form, as in example 5.11. The primal problem is
minimize
cT x
subject to
F(x) = x1F1 + · · · + xnFn + G ⪯0,
with variable x ∈Rn (and F1, . . . , Fn, G ∈Sk), and the dual problem is
maximize
tr(GZ)
subject to
tr(FiZ) + ci = 0,
i = 1, . . . , n
Z ⪰0,
with variable Z ∈Sk.
Suppose that x⋆and Z⋆are primal and dual optimal, respectively, with zero duality
gap. The complementary slackness condition is tr(F(x⋆)Z⋆) = 0. Since F(x⋆) ⪯0
and Z⋆⪰0, we can conclude that F(x⋆)Z⋆= 0. Thus, the complementary slackness
condition can be expressed as
R(F(x⋆)) ⊥R(Z⋆),
i.e., the ranges of the primal and dual matrices are orthogonal.
Let p⋆(U) denote the optimal value of the perturbed SDP
minimize
cT x
subject to
F(x) = x1F1 + · · · + xnFn + G ⪯U.


## Page 3

5.9
Generalized inequalities
269
Then we have, for all U, p⋆(U) ≥p⋆−tr(Z⋆U). If p⋆(U) is diﬀerentiable at U = 0,
then we have
∇p⋆(0) = −Z⋆.
This means that for U small, the optimal value of the perturbed SDP is very close
to (the lower bound) p⋆−tr(Z⋆U).
5.9.4
Theorems of alternatives
We can derive theorems of alternatives for systems of generalized inequalities and
equalities
fi(x) ⪯Ki 0,
i = 1, . . . , m,
hi(x) = 0,
i = 1, . . . , p,
(5.96)
where Ki ⊆Rki are proper cones. We will also consider systems with strict in-
equalities,
fi(x) ≺Ki 0,
i = 1, . . . , m,
hi(x) = 0,
i = 1, . . . , p.
(5.97)
We assume that D = Tm
i=0 dom fi ∩Tp
i=1 dom hi is nonempty.
Weak alternatives
We associate with the systems (5.96) and (5.97) the dual function
g(λ, ν) = inf
x∈D
 m
X
i=1
λT
i fi(x) +
p
X
i=1
νihi(x)
!
where λ = (λ1, . . . , λm) with λi ∈Rki and ν ∈Rp. In analogy with (5.76), we
claim that
λi ⪰K⋆
i 0,
i = 1, . . . , m,
g(λ, ν) > 0
(5.98)
is a weak alternative to the system (5.96). To verify this, suppose there exists an
x satisfying (5.96) and (λ, ν) satisfying (5.98). Then we have a contradiction:
0 < g(λ, ν) ≤λT
1 f1(x) + · · · + λT
mfm(x) + ν1h1(x) + · · · + νphp(x) ≤0.
Therefore at least one of the two systems (5.96) and (5.98) must be infeasible, i.e.,
the two systems are weak alternatives.
In a similar way, we can prove that (5.97) and the system
λi ⪰K∗
i 0,
i = 1, . . . , m,
λ̸ = 0,
g(λ, ν) ≥0.
form a pair of weak alternatives.
Strong alternatives
We now assume that the functions fi are Ki-convex, and the functions hi are aﬃne.
We ﬁrst consider a system with strict inequalities
fi(x) ≺Ki 0,
i = 1, . . . , m,
Ax = b,
(5.99)


## Page 4

270
5
Duality
and its alternative
λi ⪰K⋆
i 0,
i = 1, . . . , m,
λ̸ = 0,
g(λ, ν) ≥0.
(5.100)
We have already seen that (5.99) and (5.100) are weak alternatives. They are also
strong alternatives provided the following constraint qualiﬁcation holds: There
exists an ˜x ∈relint D with A˜x = b.
To prove this, we select a set of vectors
ei ≻Ki 0, and consider the problem
minimize
s
subject to
fi(x) ⪯Ki sei,
i = 1, . . . , m
Ax = b
(5.101)
with variables x and s ∈R. Slater’s condition holds since (˜x, ˜s) satisﬁes the strict
inequalities fi(˜x) ≺Ki ˜sei provided ˜s is large enough.
The dual of (5.101) is
maximize
g(λ, ν)
subject to
λi ⪰K∗
i 0,
i = 1, . . . , m
Pm
i=1 eT
i λi = 1
(5.102)
with variables λ = (λ1, . . . , λm) and ν.
Now suppose the system (5.99) is infeasible. Then the optimal value of (5.101)
is nonnegative. Since Slater’s condition is satisﬁed, we have strong duality and the
dual optimum is attained. Therefore there exist (˜λ, ˜ν) that satisfy the constraints
of (5.102) and g(˜λ, ˜ν) ≥0, i.e., the system (5.100) has a solution.
As we noted in the case of scalar inequalities, existence of an x ∈relint D with
Ax = b is not suﬃcient for the system of nonstrict inequalities
fi(x) ⪯Ki 0,
i = 1, . . . , m,
Ax = b
and its alternative
λi ⪰K⋆
i 0,
i = 1, . . . , m,
g(λ, ν) > 0
to be strong alternatives. An additional condition is required, e.g., that the optimal
value of (5.101) is attained.
Example 5.14
Feasibility of a linear matrix inequality. The following systems are
strong alternatives:
F(x) = x1F1 + · · · + xnFn + G ≺0,
where Fi, G ∈Sk, and
Z ⪰0,
Z̸ = 0,
tr(GZ) ≥0,
tr(FiZ) = 0,
i = 1, . . . , n,
where Z ∈Sk. This follows from the general result, if we take for K the positive
semideﬁnite cone Sk
+, and
g(Z) = inf
x (tr(F(x)Z)) =

tr(GZ)
tr(FiZ) = 0,
i = 1, . . . , n
−∞
otherwise.


## Page 5

5.9
Generalized inequalities
271
The nonstrict inequality case is slightly more involved, and we need an extra assump-
tion on the matrices Fi to have strong alternatives. One such condition is
n
X
i=1
viFi ⪰0 =⇒
n
X
i=1
viFi = 0.
If this condition holds, the following systems are strong alternatives:
F(x) = x1F1 + · · · + xnFn + G ⪯0
and
Z ⪰0,
tr(GZ) > 0,
tr(FiZ) = 0,
i = 1, . . . , n
(see exercise 5.44).


## Page 6

272
5
Duality
Bibliography
Lagrange duality is covered in detail by Luenberger [Lue69, chapter 8], Rockafellar [Roc70,
part VI], Whittle [Whi71], Hiriart-Urruty and Lemar´echal [HUL93], and Bertsekas, Nedi´c,
and Ozdaglar [Ber03]. The name is derived from Lagrange’s method of multipliers for
optimization problems with equality constraints; see Courant and Hilbert [CH53, chapter
IV].
The max-min result for matrix games in §5.2.5 predates linear programming duality.
It is proved via a theorem of alternatives by von Neuman and Morgenstern [vNM53,
page 153]. The strong duality result for linear programming on page 227 is due to von
Neumann [vN63] and Gale, Kuhn, and Tucker [GKT51]. Strong duality for the nonconvex
quadratic problem (5.32) is a fundamental result in the literature on trust region methods
for nonlinear optimization (Nocedal and Wright [NW99, page 78]). It is also related to the
S-procedure in control theory, discussed in appendix §B.1. For an extension of the proof
of strong duality of §5.3.2 to the reﬁned Slater condition (5.27), see Rockafellar [Roc70,
page 277].
Conditions that guarantee the saddle-point property (5.47) can be found in Rockafel-
lar [Roc70, part VII] and Bertsekas, Nedi´c, and Ozdaglar [Ber03, chapter 2]; see also
exercise 5.25.
The KKT conditions are named after Karush (whose unpublished 1939 Master’s thesis
is summarized in Kuhn [Kuh76]), Kuhn, and Tucker [KT51]. Related optimality condi-
tions were also derived by John [Joh85]. The water-ﬁlling algorithm in example 5.2 has
applications in information theory and communications (Cover and Thomas [CT91, page
252]).
Farkas’ lemma was published by Farkas [Far02].
It is the best known theorem of al-
ternatives for systems of linear inequalities and equalities, but many variants exist; see
Mangasarian [Man94, §2.4]. The application of Farkas’ lemma to asset pricing (exam-
ple 5.10) is discussed by Bertsimas and Tsitsiklis [BT97, page 167] and Ross [Ros99].
The extension of Lagrange duality to problems with generalized inequalities appears in
Isii [Isi64], Luenberger [Lue69, chapter 8], Berman [Ber73], and Rockafellar [Roc89, page
47].
It is discussed in the context of cone programming in Nesterov and Nemirovski
[NN94, §4.2] and Ben-Tal and Nemirovski [BTN01, lecture 2]. Theorems of alternatives
for generalized inequalities were studied by Ben-Israel [BI69], Berman and Ben-Israel
[BBI71], and Craven and Kohila [CK77]. Bellman and Fan [BF63], Wolkowicz [Wol81],
and Lasserre [Las95] give extensions of Farkas’ lemma to linear matrix inequalities.


## Page 7

Exercises
273
Exercises
Basic deﬁnitions
5.1 A simple example. Consider the optimization problem
minimize
x2 + 1
subject to
(x −2)(x −4) ≤0,
with variable x ∈R.
(a) Analysis of primal problem. Give the feasible set, the optimal value, and the optimal
solution.
(b) Lagrangian and dual function. Plot the objective x2 +1 versus x. On the same plot,
show the feasible set, optimal point and value, and plot the Lagrangian L(x, λ) versus
x for a few positive values of λ. Verify the lower bound property (p⋆≥infx L(x, λ)
for λ ≥0). Derive and sketch the Lagrange dual function g.
(c) Lagrange dual problem.
State the dual problem, and verify that it is a concave
maximization problem. Find the dual optimal value and dual optimal solution λ⋆.
Does strong duality hold?
(d) Sensitivity analysis. Let p⋆(u) denote the optimal value of the problem
minimize
x2 + 1
subject to
(x −2)(x −4) ≤u,
as a function of the parameter u. Plot p⋆(u). Verify that dp⋆(0)/du = −λ⋆.
5.2 Weak duality for unbounded and infeasible problems. The weak duality inequality, d⋆≤p⋆,
clearly holds when d⋆= −∞or p⋆= ∞. Show that it holds in the other two cases as
well: If p⋆= −∞, then we must have d⋆= −∞, and also, if d⋆= ∞, then we must have
p⋆= ∞.
5.3 Problems with one inequality constraint. Express the dual problem of
minimize
cT x
subject to
f(x) ≤0,
with c̸ = 0, in terms of the conjugate f ∗. Explain why the problem you give is convex.
We do not assume f is convex.
Examples and applications
5.4 Interpretation of LP dual via relaxed problems. Consider the inequality form LP
minimize
cT x
subject to
Ax ⪯b,
with A ∈Rm×n, b ∈Rm. In this exercise we develop a simple geometric interpretation
of the dual LP (5.22).
Let w ∈Rm
+ . If x is feasible for the LP, i.e., satisﬁes Ax ⪯b, then it also satisﬁes the
inequality
wT Ax ≤wT b.
Geometrically, for any w ⪰0, the halfspace Hw = {x | wT Ax ≤wT b} contains the feasible
set for the LP. Therefore if we minimize the objective cT x over the halfspace Hw we get
a lower bound on p⋆.


## Page 8

274
5
Duality
(a) Derive an expression for the minimum value of cT x over the halfspace Hw (which
will depend on the choice of w ⪰0).
(b) Formulate the problem of ﬁnding the best such bound, by maximizing the lower
bound over w ⪰0.
(c) Relate the results of (a) and (b) to the Lagrange dual of the LP, given by (5.22).
5.5 Dual of general LP. Find the dual function of the LP
minimize
cT x
subject to
Gx ⪯h
Ax = b.
Give the dual problem, and make the implicit equality constraints explicit.
5.6 Lower bounds in Chebyshev approximation from least-squares. Consider the Chebyshev
or ℓ∞-norm approximation problem
minimize
∥Ax −b∥∞,
(5.103)
where A ∈Rm×n and rank A = n. Let xch denote an optimal solution (there may be
multiple optimal solutions; xch denotes one of them).
The Chebyshev problem has no closed-form solution, but the corresponding least-squares
problem does. Deﬁne
xls = argmin ∥Ax −b∥2 = (AT A)−1AT b.
We address the following question. Suppose that for a particular A and b we have com-
puted the least-squares solution xls (but not xch). How suboptimal is xls for the Chebyshev
problem? In other words, how much larger is ∥Axls −b∥∞than ∥Axch −b∥∞?
(a) Prove the lower bound
∥Axls −b∥∞≤√m ∥Axch −b∥∞,
using the fact that for all z ∈Rm,
1
√m∥z∥2 ≤∥z∥∞≤∥z∥2.
(b) In example 5.6 (page 254) we derived a dual for the general norm approximation
problem. Applying the results to the ℓ∞-norm (and its dual norm, the ℓ1-norm), we
can state the following dual for the Chebyshev approximation problem:
maximize
bT ν
subject to
∥ν∥1 ≤1
AT ν = 0.
(5.104)
Any feasible ν corresponds to a lower bound bT ν on ∥Axch −b∥∞.
Denote the least-squares residual as rls = b −Axls. Assuming rls̸ = 0, show that
ˆν = −rls/∥rls∥1,
˜ν = rls/∥rls∥1,
are both feasible in (5.104). By duality bT ˆν and bT ˜ν are lower bounds on ∥Axch −
b∥∞. Which is the better bound? How do these bounds compare with the bound
derived in part (a)?
5.7 Piecewise-linear minimization.
We consider the convex piecewise-linear minimization
problem
minimize
maxi=1,...,m(aT
i x + bi)
(5.105)
with variable x ∈Rn.


## Page 9

Exercises
275
(a) Derive a dual problem, based on the Lagrange dual of the equivalent problem
minimize
maxi=1,...,m yi
subject to
aT
i x + bi = yi,
i = 1, . . . , m,
with variables x ∈Rn, y ∈Rm.
(b) Formulate the piecewise-linear minimization problem (5.105) as an LP, and form the
dual of the LP. Relate the LP dual to the dual obtained in part (a).
(c) Suppose we approximate the objective function in (5.105) by the smooth function
f0(x) = log
 m
X
i=1
exp(aT
i x + bi)
!
,
and solve the unconstrained geometric program
minimize
log  Pm
i=1 exp(aT
i x + bi)
.
(5.106)
A dual of this problem is given by (5.62). Let p⋆
pwl and p⋆
gp be the optimal values
of (5.105) and (5.106), respectively. Show that
0 ≤p⋆
gp −p⋆
pwl ≤log m.
(d) Derive similar bounds for the diﬀerence between p⋆
pwl and the optimal value of
minimize
(1/γ) log  Pm
i=1 exp(γ(aT
i x + bi))
,
where γ > 0 is a parameter. What happens as we increase γ?
5.8 Relate the two dual problems derived in example 5.9 on page 257.
5.9 Suboptimality of a simple covering ellipsoid. Recall the problem of determining the min-
imum volume ellipsoid, centered at the origin, that contains the points a1, . . . , am ∈Rn
(problem (5.14), page 222):
minimize
f0(X) = log det(X−1)
subject to
aT
i Xai ≤1,
i = 1, . . . , m,
with dom f0 = Sn
++. We assume that the vectors a1, . . . , am span Rn (which implies that
the problem is bounded below).
(a) Show that the matrix
Xsim =
 m
X
k=1
akaT
k
!−1
,
is feasible. Hint. Show that  Pm
k=1 akaT
k
ai
aT
i
1

⪰0,
and use Schur complements (§A.5.5) to prove that aT
i Xai ≤1 for i = 1, . . . , m.
(b) Now we establish a bound on how suboptimal the feasible point Xsim is, via the dual
problem,
maximize
log det  Pm
i=1 λiaiaT
i

−1T λ + n
subject to
λ ⪰0,
with the implicit constraint Pm
i=1 λiaiaT
i ≻0. (This dual is derived on page 222.)
To derive a bound, we restrict our attention to dual variables of the form λ = t1,
where t > 0.
Find (analytically) the optimal value of t, and evaluate the dual
objective at this λ. Use this to prove that the volume of the ellipsoid {u | uT Xsimu ≤
1} is no more than a factor (m/n)n/2 more than the volume of the minimum volume
ellipsoid.


## Page 10

276
5
Duality
5.10 Optimal experiment design. The following problems arise in experiment design (see §7.5).
(a) D-optimal design.
minimize
log det  Pp
i=1 xivivT
i
−1
subject to
x ⪰0,
1T x = 1.
(b) A-optimal design.
minimize
tr  Pp
i=1 xivivT
i
−1
subject to
x ⪰0,
1T x = 1.
The domain of both problems is {x | Pp
i=1 xivivT
i
≻0}. The variable is x ∈Rp; the
vectors v1, . . . , vp ∈Rn are given.
Derive dual problems by ﬁrst introducing a new variable X ∈Sn and an equality con-
straint X = Pp
i=1 xivivT
i , and then applying Lagrange duality. Simplify the dual prob-
lems as much as you can.
5.11 Derive a dual problem for
minimize
PN
i=1 ∥Aix + bi∥2 + (1/2)∥x −x0∥2
2.
The problem data are Ai ∈Rmi×n, bi ∈Rmi, and x0 ∈Rn. First introduce new variables
yi ∈Rmi and equality constraints yi = Aix + bi.
5.12 Analytic centering. Derive a dual problem for
minimize
−Pm
i=1 log(bi −aT
i x)
with domain {x | aT
i x < bi, i = 1, . . . , m}. First introduce new variables yi and equality
constraints yi = bi −aT
i x.
(The solution of this problem is called the analytic center of the linear inequalities aT
i x ≤
bi, i = 1, . . . , m. Analytic centers have geometric applications (see §8.5.3), and play an
important role in barrier methods (see chapter 11).)
5.13 Lagrangian relaxation of Boolean LP. A Boolean linear program is an optimization prob-
lem of the form
minimize
cT x
subject to
Ax ⪯b
xi ∈{0, 1},
i = 1, . . . , n,
and is, in general, very diﬃcult to solve. In exercise 4.15 we studied the LP relaxation of
this problem,
minimize
cT x
subject to
Ax ⪯b
0 ≤xi ≤1,
i = 1, . . . , n,
(5.107)
which is far easier to solve, and gives a lower bound on the optimal value of the Boolean
LP. In this problem we derive another lower bound for the Boolean LP, and work out the
relation between the two lower bounds.
(a) Lagrangian relaxation. The Boolean LP can be reformulated as the problem
minimize
cT x
subject to
Ax ⪯b
xi(1 −xi) = 0,
i = 1, . . . , n,
which has quadratic equality constraints. Find the Lagrange dual of this problem.
The optimal value of the dual problem (which is convex) gives a lower bound on
the optimal value of the Boolean LP. This method of ﬁnding a lower bound on the
optimal value is called Lagrangian relaxation.


## Page 11

Exercises
277
(b) Show that the lower bound obtained via Lagrangian relaxation, and via the LP
relaxation (5.107), are the same. Hint. Derive the dual of the LP relaxation (5.107).
5.14 A penalty method for equality constraints. We consider the problem
minimize
f0(x)
subject to
Ax = b,
(5.108)
where f0 : Rn →R is convex and diﬀerentiable, and A ∈Rm×n with rank A = m.
In a quadratic penalty method, we form an auxiliary function
φ(x) = f0(x) + α∥Ax −b∥2
2,
where α > 0 is a parameter. This auxiliary function consists of the objective plus the
penalty term α∥Ax−b∥2
2. The idea is that a minimizer of the auxiliary function, ˜x, should
be an approximate solution of the original problem. Intuition suggests that the larger the
penalty weight α, the better the approximation ˜x to a solution of the original problem.
Suppose ˜x is a minimizer of φ. Show how to ﬁnd, from ˜x, a dual feasible point for (5.108).
Find the corresponding lower bound on the optimal value of (5.108).
5.15 Consider the problem
minimize
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m,
(5.109)
where the functions fi : Rn →R are diﬀerentiable and convex. Let h1, . . . , hm : R →R
be increasing diﬀerentiable convex functions. Show that
φ(x) = f0(x) +
m
X
i=1
hi(fi(x))
is convex. Suppose ˜x minimizes φ. Show how to ﬁnd from ˜x a feasible point for the dual
of (5.109). Find the corresponding lower bound on the optimal value of (5.109).
5.16 An exact penalty method for inequality constraints. Consider the problem
minimize
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m,
(5.110)
where the functions fi : Rn →R are diﬀerentiable and convex.
In an exact penalty
method, we solve the auxiliary problem
minimize
φ(x) = f0(x) + α maxi=1,...,m max{0, fi(x)},
(5.111)
where α > 0 is a parameter. The second term in φ penalizes deviations of x from feasibility.
The method is called an exact penalty method if for suﬃciently large α, solutions of the
auxiliary problem (5.111) also solve the original problem (5.110).
(a) Show that φ is convex.
(b) The auxiliary problem can be expressed as
minimize
f0(x) + αy
subject to
fi(x) ≤y,
i = 1, . . . , m
0 ≤y
where the variables are x and y ∈R. Find the Lagrange dual of this problem, and
express it in terms of the Lagrange dual function g of (5.110).


## Page 12

278
5
Duality
(c) Use the result in (b) to prove the following property.
Suppose λ⋆is an optimal
solution of the Lagrange dual of (5.110), and that strong duality holds.
If α >
1T λ⋆, then any solution of the auxiliary problem (5.111) is also an optimal solution
of (5.110).
5.17 Robust linear programming with polyhedral uncertainty. Consider the robust LP
minimize
cT x
subject to
supa∈Pi aT x ≤bi,
i = 1, . . . , m,
with variable x ∈Rn, where Pi = {a | Cia ⪯di}.
The problem data are c ∈Rn,
Ci ∈Rmi×n, di ∈Rmi, and b ∈Rm. We assume the polyhedra Pi are nonempty.
Show that this problem is equivalent to the LP
minimize
cT x
subject to
dT
i zi ≤bi,
i = 1, . . . , m
CT
i zi = x,
i = 1, . . . , m
zi ⪰0,
i = 1, . . . , m
with variables x ∈Rn and zi ∈Rmi, i = 1, . . . , m. Hint. Find the dual of the problem
of maximizing aT
i x over ai ∈Pi (with variable ai).
5.18 Separating hyperplane between two polyhedra. Formulate the following problem as an LP
or an LP feasibility problem. Find a separating hyperplane that strictly separates two
polyhedra
P1 = {x | Ax ⪯b},
P2 = {x | Cx ⪯d},
i.e., ﬁnd a vector a ∈Rn and a scalar γ such that
aT x > γ for x ∈P1,
aT x < γ for x ∈P2.
You can assume that P1 and P2 do not intersect.
Hint. The vector a and scalar γ must satisfy
inf
x∈P1 aT x > γ > sup
x∈P2
aT x.
Use LP duality to simplify the inﬁmum and supremum in these conditions.
5.19 The sum of the largest elements of a vector.
Deﬁne f : Rn →R as
f(x) =
r
X
i=1
x[i],
where r is an integer between 1 and n, and x[1] ≥x[2] ≥· · · ≥x[r] are the components of
x sorted in decreasing order. In other words, f(x) is the sum of the r largest elements of
x. In this problem we study the constraint
f(x) ≤α.
As we have seen in chapter 3, page 80, this is a convex constraint, and equivalent to a set
of n!/(r!(n −r)!) linear inequalities
xi1 + · · · + xir ≤α,
1 ≤i1 < i2 < · · · < ir ≤n.
The purpose of this problem is to derive a more compact representation.


## Page 13

Exercises
279
(a) Given a vector x ∈Rn, show that f(x) is equal to the optimal value of the LP
maximize
xT y
subject to
0 ⪯y ⪯1
1T y = r
with y ∈Rn as variable.
(b) Derive the dual of the LP in part (a). Show that it can be written as
minimize
rt + 1T u
subject to
t1 + u ⪰x
u ⪰0,
where the variables are t ∈R, u ∈Rn. By duality this LP has the same optimal
value as the LP in (a), i.e., f(x). We therefore have the following result: x satisﬁes
f(x) ≤α if and only if there exist t ∈R, u ∈Rn such that
rt + 1T u ≤α,
t1 + u ⪰x,
u ⪰0.
These conditions form a set of 2n+1 linear inequalities in the 2n+1 variables x, u, t.
(c) As an application, we consider an extension of the classical Markowitz portfolio
optimization problem
minimize
xT Σx
subject to
pT x ≥rmin
1T x = 1,
x ⪰0
discussed in chapter 4, page 155. The variable is the portfolio x ∈Rn; p and Σ are
the mean and covariance matrix of the price change vector p.
Suppose we add a diversiﬁcation constraint, requiring that no more than 80% of
the total budget can be invested in any 10% of the assets. This constraint can be
expressed as
⌊0.1n⌋
X
i=1
x[i] ≤0.8.
Formulate the portfolio optimization problem with diversiﬁcation constraint as a
QP.
5.20 Dual of channel capacity problem. Derive a dual for the problem
minimize
−cT x + Pm
i=1 yi log yi
subject to
Px = y
x ⪰0,
1T x = 1,
where P ∈Rm×n has nonnegative elements, and its columns add up to one (i.e., P T 1 =
1). The variables are x ∈Rn, y ∈Rm. (For cj = Pm
i=1 pij log pij, the optimal value is,
up to a factor log 2, the negative of the capacity of a discrete memoryless channel with
channel transition probability matrix P; see exercise 4.57.)
Simplify the dual problem as much as possible.


## Page 14

280
5
Duality
Strong duality and Slater’s condition
5.21 A convex problem in which strong duality fails. Consider the optimization problem
minimize
e−x
subject to
x2/y ≤0
with variables x and y, and domain D = {(x, y) | y > 0}.
(a) Verify that this is a convex optimization problem. Find the optimal value.
(b) Give the Lagrange dual problem, and ﬁnd the optimal solution λ⋆and optimal value
d⋆of the dual problem. What is the optimal duality gap?
(c) Does Slater’s condition hold for this problem?
(d) What is the optimal value p⋆(u) of the perturbed problem
minimize
e−x
subject to
x2/y ≤u
as a function of u? Verify that the global sensitivity inequality
p⋆(u) ≥p⋆(0) −λ⋆u
does not hold.
5.22 Geometric interpretation of duality.
For each of the following optimization problems,
draw a sketch of the sets
G
=
{(u, t) | ∃x ∈D, f0(x) = t, f1(x) = u},
A
=
{(u, t) | ∃x ∈D, f0(x) ≤t, f1(x) ≤u},
give the dual problem, and solve the primal and dual problems. Is the problem convex?
Is Slater’s condition satisﬁed? Does strong duality hold?
The domain of the problem is R unless otherwise stated.
(a) Minimize x subject to x2 ≤1.
(b) Minimize x subject to x2 ≤0.
(c) Minimize x subject to |x| ≤0.
(d) Minimize x subject to f1(x) ≤0 where
f1(x) =
( −x + 2
x ≥1
x
−1 ≤x ≤1
−x −2
x ≤−1.
(e) Minimize x3 subject to −x + 1 ≤0.
(f) Minimize x3 subject to −x + 1 ≤0 with domain D = R+.
5.23 Strong duality in linear programming. We prove that strong duality holds for the LP
minimize
cT x
subject to
Ax ⪯b
and its dual
maximize
−bT z
subject to
AT z + c = 0,
z ⪰0,
provided at least one of the problems is feasible. In other words, the only possible excep-
tion to strong duality occurs when p⋆= ∞and d⋆= −∞.


## Page 15

Exercises
281
(a) Suppose p⋆is ﬁnite and x⋆is an optimal solution. (If ﬁnite, the optimal value of an
LP is attained.) Let I ⊆{1, 2, . . . , m} be the set of active constraints at x⋆:
aT
i x⋆= bi,
i ∈I,
aT
i x⋆< bi,
i̸ ∈I.
Show that there exists a z ∈Rm that satisﬁes
zi ≥0,
i ∈I,
zi = 0,
i̸ ∈I,
X
i∈I
ziai + c = 0.
Show that z is dual optimal with objective value cT x⋆.
Hint.
Assume there exists no such z, i.e., −c̸ ∈{P
i∈I ziai | zi ≥0}.
Reduce
this to a contradiction by applying the strict separating hyperplane theorem of
example 2.20, page 49. Alternatively, you can use Farkas’ lemma (see §5.8.3).
(b) Suppose p⋆= ∞and the dual problem is feasible. Show that d⋆= ∞. Hint. Show
that there exists a nonzero v ∈Rm such that AT v = 0, v ⪰0, bT v < 0. If the dual
is feasible, it is unbounded in the direction v.
(c) Consider the example
minimize
x
subject to

0
1

x ⪯

−1
1

.
Formulate the dual LP, and solve the primal and dual problems. Show that p⋆= ∞
and d⋆= −∞.
5.24 Weak max-min inequality. Show that the weak max-min inequality
sup
z∈Z
inf
w∈W
f(w, z) ≤inf
w∈W
sup
z∈Z
f(w, z)
always holds, with no assumptions on f : Rn × Rm →R, W ⊆Rn, or Z ⊆Rm.
5.25 [BL00, page 95] Convex-concave functions and the saddle-point property. We derive con-
ditions under which the saddle-point property
sup
z∈Z
inf
w∈W
f(w, z) = inf
w∈W
sup
z∈Z
f(w, z)
(5.112)
holds, where f : Rn × Rm →R, W × Z ⊆dom f, and W and Z are nonempty. We will
assume that the function
gz(w) =

f(w, z)
w ∈W
∞
otherwise
is closed and convex for all z ∈Z, and the function
hw(z) =

−f(w, z)
z ∈Z
∞
otherwise
is closed and convex for all w ∈W.
(a) The righthand side of (5.112) can be expressed as p(0), where
p(u) = inf
w∈W
sup
z∈Z
(f(w, z) + uT z).
Show that p is a convex function.


## Page 16

282
5
Duality
(b) Show that the conjugate of p is given by
p∗(v) =

−infw∈W f(w, v)
v ∈Z
∞
otherwise.
(c) Show that the conjugate of p∗is given by
p∗∗(u) = sup
z∈Z
inf
w∈W
(f(w, z) + uT z).
Combining this with (a), we can express the max-min equality (5.112) as p∗∗(0) =
p(0).
(d) From exercises 3.28 and 3.39 (d), we know that p∗∗(0) = p(0) if 0 ∈int dom p.
Conclude that this is the case if W and Z are bounded.
(e) As another consequence of exercises 3.28 and 3.39, we have p∗∗(0) = p(0) if 0 ∈
dom p and p is closed. Show that p is closed if the sublevel sets of gz are bounded.
Optimality conditions
5.26 Consider the QCQP
minimize
x2
1 + x2
2
subject to
(x1 −1)2 + (x2 −1)2 ≤1
(x1 −1)2 + (x2 + 1)2 ≤1
with variable x ∈R2.
(a) Sketch the feasible set and level sets of the objective. Find the optimal point x⋆and
optimal value p⋆.
(b) Give the KKT conditions. Do there exist Lagrange multipliers λ⋆
1 and λ⋆
2 that prove
that x⋆is optimal?
(c) Derive and solve the Lagrange dual problem. Does strong duality hold?
5.27 Equality constrained least-squares. Consider the equality constrained least-squares prob-
lem
minimize
∥Ax −b∥2
2
subject to
Gx = h
where A ∈Rm×n with rank A = n, and G ∈Rp×n with rank G = p.
Give the KKT conditions, and derive expressions for the primal solution x⋆and the dual
solution ν⋆.
5.28 Prove (without using any linear programming code) that the optimal solution of the LP
minimize
47x1 + 93x2 + 17x3 −93x4
subject to


−1
−6
1
3
−1
−2
7
1
0
3
−10
−1
−6
−11
−2
12
1
6
−1
−3




x1
x2
x3
x4

⪯


−3
5
−8
−7
4


is unique, and given by x⋆= (1, 1, 1, 1).
5.29 The problem
minimize
−3x2
1 + x2
2 + 2x2
3 + 2(x1 + x2 + x3)
subject to
x2
1 + x2
2 + x2
3 = 1,
is a special case of (5.32), so strong duality holds even though the problem is not convex.
Derive the KKT conditions.
Find all solutions x, ν that satisfy the KKT conditions.
Which pair corresponds to the optimum?


## Page 17

Exercises
283
5.30 Derive the KKT conditions for the problem
minimize
tr X −log det X
subject to
Xs = y,
with variable X ∈Sn and domain Sn
++. y ∈Rn and s ∈Rn are given, with sT y = 1.
Verify that the optimal solution is given by
X⋆= I + yyT −
1
sT sssT .
5.31 Supporting hyperplane interpretation of KKT conditions. Consider a convex problem with
no equality constraints,
minimize
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m.
Assume that x⋆∈Rn and λ⋆∈Rm satisfy the KKT conditions
fi(x⋆)
≤
0,
i = 1, . . . , m
λ⋆
i
≥
0,
i = 1, . . . , m
λ⋆
i fi(x⋆)
=
0,
i = 1, . . . , m
∇f0(x⋆) + Pm
i=1 λ⋆
i ∇fi(x⋆)
=
0.
Show that
∇f0(x⋆)T (x −x⋆) ≥0
for all feasible x. In other words the KKT conditions imply the simple optimality criterion
of §4.2.3.
Perturbation and sensitivity analysis
5.32 Optimal value of perturbed problem. Let f0, f1, . . . , fm : Rn →R be convex. Show that
the function
p⋆(u, v) = inf{f0(x) | ∃x ∈D, fi(x) ≤ui, i = 1, . . . , m, Ax −b = v}
is convex. This function is the optimal cost of the perturbed problem, as a function of
the perturbations u and v (see §5.6.1).
5.33 Parametrized ℓ1-norm approximation. Consider the ℓ1-norm minimization problem
minimize
∥Ax + b + ǫd∥1
with variable x ∈R3, and
A =


−2
7
1
−5
−1
3
−7
3
−5
−1
4
−4
1
5
5
2
−5
−1


,
b =


−4
3
9
0
−11
5


,
d =


−10
−13
−27
−10
−7
14


.
We denote by p⋆(ǫ) the optimal value as a function of ǫ.
(a) Suppose ǫ = 0. Prove that x⋆= 1 is optimal. Are there any other optimal points?
(b) Show that p⋆(ǫ) is aﬃne on an interval that includes ǫ = 0.


## Page 18

284
5
Duality
5.34 Consider the pair of primal and dual LPs
minimize
(c + ǫd)T x
subject to
Ax ⪯b + ǫf
and
maximize
−(b + ǫf)T z
subject to
AT z + c + ǫd = 0
z ⪰0
where
A =


−4
12
−2
1
−17
12
7
11
1
0
−6
1
3
3
22
−1
−11
2
−1
−8

,
b =


8
13
−4
27
−18

,
f =


6
15
−13
48
8

,
c = (49, −34, −50, −5), d = (3, 8, 21, 25), and ǫ is a parameter.
(a) Prove that x⋆= (1, 1, 1, 1) is optimal when ǫ = 0, by constructing a dual optimal
point z⋆that has the same objective value as x⋆. Are there any other primal or dual
optimal solutions?
(b) Give an explicit expression for the optimal value p⋆(ǫ) as a function of ǫ on an
interval that contains ǫ = 0. Specify the interval on which your expression is valid.
Also give explicit expressions for the primal solution x⋆(ǫ) and the dual solution
z⋆(ǫ) as a function of ǫ, on the same interval.
Hint. First calculate x⋆(ǫ) and z⋆(ǫ), assuming that the primal and dual constraints
that are active at the optimum for ǫ = 0, remain active at the optimum for values
of ǫ around 0. Then verify that this assumption is correct.
5.35 Sensitivity analysis for GPs. Consider a GP
minimize
f0(x)
subject to
fi(x) ≤1,
i = 1, . . . , m
hi(x) = 1,
i = 1, . . . , p,
where f0, . . . , fm are posynomials, h1, . . . , hp are monomials, and the domain of the prob-
lem is Rn
++. We deﬁne the perturbed GP as
minimize
f0(x)
subject to
fi(x) ≤eui,
i = 1, . . . , m
hi(x) = evi,
i = 1, . . . , p,
and we denote the optimal value of the perturbed GP as p⋆(u, v). We can think of ui and
vi as relative, or fractional, perturbations of the constraints. For example, u1 = −0.01
corresponds to tightening the ﬁrst inequality constraint by (approximately) 1%.
Let λ⋆and ν⋆be optimal dual variables for the convex form GP
minimize
log f0(y)
subject to
log fi(y) ≤0,
i = 1, . . . , m
log hi(y) = 0,
i = 1, . . . , p,
with variables yi = log xi. Assuming that p⋆(u, v) is diﬀerentiable at u = 0, v = 0, relate
λ⋆and ν⋆to the derivatives of p⋆(u, v) at u = 0, v = 0. Justify the statement “Relaxing
the ith constraint by α percent will give an improvement in the objective of around αλ⋆
i
percent, for α small.”


## Page 19

Exercises
285
Theorems of alternatives
5.36 Alternatives for linear equalities. Consider the linear equations Ax = b, where A ∈Rm×n.
From linear algebra we know that this equation has a solution if and only b ∈R(A), which
occurs if and only if b ⊥N(AT ). In other words, Ax = b has a solution if and only if
there exists no y ∈Rm such that AT y = 0 and bT y̸ = 0.
Derive this result from the theorems of alternatives in §5.8.2.
5.37 [BT97] Existence of equilibrium distribution in ﬁnite state Markov chain. Let P ∈Rn×n
be a matrix that satisﬁes
pij ≥0,
i, j = 1, . . . , n,
P T 1 = 1,
i.e., the coeﬃcients are nonnegative and the columns sum to one. Use Farkas’ lemma to
prove there exists a y ∈Rn such that
Py = y,
y ⪰0,
1T y = 1.
(We can interpret y as an equilibrium distribution of the Markov chain with n states and
transition probability matrix P.)
5.38 [BT97] Option pricing.
We apply the results of example 5.10, page 263, to a simple
problem with three assets: a riskless asset with ﬁxed return r > 1 over the investment
period of interest (for example, a bond), a stock, and an option on the stock. The option
gives us the right to purchase the stock at the end of the period, for a predetermined
price K.
We consider two scenarios.
In the ﬁrst scenario, the price of the stock goes up from
S at the beginning of the period, to Su at the end of the period, where u > r. In this
scenario, we exercise the option only if Su > K, in which case we make a proﬁt of Su−K.
Otherwise, we do not exercise the option, and make zero proﬁt. The value of the option
at the end of the period, in the ﬁrst scenario, is therefore max{0, Su −K}.
In the second scenario, the price of the stock goes down from S to Sd, where d < 1. The
value at the end of the period is max{0, Sd −K}.
In the notation of example 5.10,
V =

r
uS
max{0, Su −K}
r
dS
max{0, Sd −K}

,
p1 = 1,
p2 = S,
p3 = C,
where C is the price of the option.
Show that for given r, S, K, u, d, the option price C is uniquely determined by the
no-arbitrage condition. In other words, the market for the option is complete.
Generalized inequalities
5.39 SDP relaxations of two-way partitioning problem. We consider the two-way partitioning
problem (5.7), described on page 219,
minimize
xT Wx
subject to
x2
i = 1,
i = 1, . . . , n,
(5.113)
with variable x ∈Rn. The Lagrange dual of this (nonconvex) problem is given by the
SDP
maximize
−1T ν
subject to
W + diag(ν) ⪰0
(5.114)
with variable ν ∈Rn. The optimal value of this SDP gives a lower bound on the optimal
value of the partitioning problem (5.113). In this exercise we derive another SDP that
gives a lower bound on the optimal value of the two-way partitioning problem, and explore
the connection between the two SDPs.


## Page 20

286
5
Duality
(a) Two-way partitioning problem in matrix form. Show that the two-way partitioning
problem can be cast as
minimize
tr(WX)
subject to
X ⪰0,
rank X = 1
Xii = 1,
i = 1, . . . , n,
with variable X ∈Sn.
Hint.
Show that if X is feasible, then it has the form
X = xxT , where x ∈Rn satisﬁes xi ∈{−1, 1} (and vice versa).
(b) SDP relaxation of two-way partitioning problem. Using the formulation in part (a),
we can form the relaxation
minimize
tr(WX)
subject to
X ⪰0
Xii = 1,
i = 1, . . . , n,
(5.115)
with variable X ∈Sn. This problem is an SDP, and therefore can be solved eﬃ-
ciently. Explain why its optimal value gives a lower bound on the optimal value of
the two-way partitioning problem (5.113). What can you say if an optimal point
X⋆for this SDP has rank one?
(c) We now have two SDPs that give a lower bound on the optimal value of the two-way
partitioning problem (5.113): the SDP relaxation (5.115) found in part (b), and the
Lagrange dual of the two-way partitioning problem, given in (5.114). What is the
relation between the two SDPs? What can you say about the lower bounds found
by them? Hint: Relate the two SDPs via duality.
5.40 E-optimal experiment design. A variation on the two optimal experiment design problems
of exercise 5.10 is the E-optimal design problem
minimize
λmax
 Pp
i=1 xivivT
i
−1
subject to
x ⪰0,
1T x = 1.
(See also §7.5.) Derive a dual for this problem, by ﬁrst reformulating it as
minimize
1/t
subject to
Pp
i=1 xivivT
i ⪰tI
x ⪰0,
1T x = 1,
with variables t ∈R, x ∈Rp and domain R++ × Rp, and applying Lagrange duality.
Simplify the dual problem as much as you can.
5.41 Dual of fastest mixing Markov chain problem. On page 174, we encountered the SDP
minimize
t
subject to
−tI ⪯P −(1/n)11T ⪯tI
P1 = 1
Pij ≥0,
i, j = 1, . . . , n
Pij = 0 for (i, j)̸ ∈E,
with variables t ∈R, P ∈Sn.
Show that the dual of this problem can be expressed as
maximize
1T z −(1/n)1T Y 1
subject to
∥Y ∥2∗≤1
(zi + zj) ≤Yij for (i, j) ∈E
with variables z ∈Rn and Y ∈Sn. The norm ∥· ∥2∗is the dual of the spectral norm
on Sn: ∥Y ∥2∗= Pn
i=1 |λi(Y )|, the sum of the absolute values of the eigenvalues of Y .
(See §A.1.6, page 637.)


## Page 21

Exercises
287
5.42 Lagrange dual of conic form problem in inequality form. Find the Lagrange dual problem
of the conic form problem in inequality form
minimize
cT x
subject to
Ax ⪯K b
where A ∈Rm×n, b ∈Rm, and K is a proper cone in Rm. Make any implicit equality
constraints explicit.
5.43 Dual of SOCP. Show that the dual of the SOCP
minimize
f T x
subject to
∥Aix + bi∥2 ≤cT
i x + di,
i = 1, . . . , m,
with variables x ∈Rn, can be expressed as
maximize
Pm
i=1(bT
i ui −divi)
subject to
Pm
i=1(AT
i ui −civi) + f = 0
∥ui∥2 ≤vi,
i = 1, . . . , m,
with variables ui ∈Rni, vi ∈R, i = 1, . . . , m. The problem data are f ∈Rn, Ai ∈Rni×n,
bi ∈Rni, ci ∈R and di ∈R, i = 1, . . . , m.
Derive the dual in the following two ways.
(a) Introduce new variables yi ∈Rni and ti ∈R and equalities yi = Aix + bi, ti =
cT
i x + di, and derive the Lagrange dual.
(b) Start from the conic formulation of the SOCP and use the conic dual. Use the fact
that the second-order cone is self-dual.
5.44 Strong alternatives for nonstrict LMIs.
In example 5.14, page 270, we mentioned that
the system
Z ⪰0,
tr(GZ) > 0,
tr(FiZ) = 0,
i = 1, . . . , n,
(5.116)
is a strong alternative for the nonstrict LMI
F(x) = x1F1 + · · · + xnFn + G ⪯0,
(5.117)
if the matrices Fi satisfy
n
X
i=1
viFi ⪰0 =⇒
n
X
i=1
viFi = 0.
(5.118)
In this exercise we prove this result, and give an example to illustrate that the systems
are not always strong alternatives.
(a) Suppose (5.118) holds, and that the optimal value of the auxiliary SDP
minimize
s
subject to
F(x) ⪯sI
is positive. Show that the optimal value is attained. If follows from the discussion
in §5.9.4 that the systems (5.117) and (5.116) are strong alternatives.
Hint. The proof simpliﬁes if you assume, without loss of generality, that the matrices
F1, . . . , Fn are independent, so (5.118) may be replaced by Pn
i=1 viFi ⪰0 ⇒v = 0.
(b) Take n = 1, and
G =

0
1
1
0

,
F1 =

0
0
0
1

.
Show that (5.117) and (5.116) are both infeasible.


## Page 22



## Page 23

Part II
Applications


## Page 24



## Page 25

Chapter 6
Approximation and ﬁtting
6.1
Norm approximation
6.1.1
Basic norm approximation problem
The simplest norm approximation problem is an unconstrained problem of the form
minimize
∥Ax −b∥
(6.1)
where A ∈Rm×n and b ∈Rm are problem data, x ∈Rn is the variable, and ∥·∥is
a norm on Rm. A solution of the norm approximation problem is sometimes called
an approximate solution of Ax ≈b, in the norm ∥· ∥. The vector
r = Ax −b
is called the residual for the problem; its components are sometimes called the
individual residuals associated with x.
The norm approximation problem (6.1) is a convex problem, and is solvable,
i.e., there is always at least one optimal solution.
Its optimal value is zero if
and only if b ∈R(A); the problem is more interesting and useful, however, when
b̸ ∈R(A). We can assume without loss of generality that the columns of A are
independent; in particular, that m ≥n. When m = n the optimal point is simply
A−1b, so we can assume that m > n.
Approximation interpretation
By expressing Ax as
Ax = x1a1 + · · · + xnan,
where a1, . . . , an ∈Rm are the columns of A, we see that the goal of the norm
approximation problem is to ﬁt or approximate the vector b by a linear combination
of the columns of A, as closely as possible, with deviation measured in the norm
∥· ∥.
The approximation problem is also called the regression problem. In this context
the vectors a1, . . . , an are called the regressors, and the vector x1a1 + · · · + xnan,


## Page 26

292
6
Approximation and ﬁtting
where x is an optimal solution of the problem, is called the regression of b (onto
the regressors).
Estimation interpretation
A closely related interpretation of the norm approximation problem arises in the
problem of estimating a parameter vector on the basis of an imperfect linear vector
measurement. We consider a linear measurement model
y = Ax + v,
where y ∈Rm is a vector measurement, x ∈Rn is a vector of parameters to be
estimated, and v ∈Rm is some measurement error that is unknown, but presumed
to be small (in the norm ∥· ∥). The estimation problem is to make a sensible guess
as to what x is, given y.
If we guess that x has the value ˆx, then we are implicitly making the guess that
v has the value y −Aˆx. Assuming that smaller values of v (measured by ∥· ∥) are
more plausible than larger values, the most plausible guess for x is
ˆx = argminz∥Az −y∥.
(These ideas can be expressed more formally in a statistical framework; see chap-
ter 7.)
Geometric interpretation
We consider the subspace A = R(A) ⊆Rm, and a point b ∈Rm. A projection of
the point b onto the subspace A, in the norm ∥· ∥, is any point in A that is closest
to b, i.e., any optimal point for the problem
minimize
∥u −b∥
subject to
u ∈A.
Parametrizing an arbitrary element of R(A) as u = Ax, we see that solving the
norm approximation problem (6.1) is equivalent to computing a projection of b
onto A.
Design interpretation
We can interpret the norm approximation problem (6.1) as a problem of optimal
design.
The n variables x1, . . . , xn are design variables whose values are to be
determined. The vector y = Ax gives a vector of m results, which we assume to
be linear functions of the design variables x. The vector b is a vector of target or
desired results. The goal is to choose a vector of design variables that achieves, as
closely as possible, the desired results, i.e., Ax ≈b. We can interpret the residual
vector r as the deviation between the actual results (i.e., Ax) and the desired
or target results (i.e., b). If we measure the quality of a design by the norm of
the deviation between the actual results and the desired results, then the norm
approximation problem (6.1) is the problem of ﬁnding the best design.


## Page 27

6.1
Norm approximation
293
Weighted norm approximation problems
An extension of the norm approximation problem is the weighted norm approxima-
tion problem
minimize
∥W(Ax −b)∥
where the problem data W ∈Rm×m is called the weighting matrix. The weight-
ing matrix is often diagonal, in which case it gives diﬀerent relative emphasis to
diﬀerent components of the residual vector r = Ax −b.
The weighted norm problem can be considered as a norm approximation prob-
lem with norm ∥·∥, and data ˜A = WA, ˜b = Wb, and therefore treated as a standard
norm approximation problem (6.1). Alternatively, the weighted norm approxima-
tion problem can be considered a norm approximation problem with data A and
b, and the W-weighted norm deﬁned by
∥z∥W = ∥Wz∥
(assuming here that W is nonsingular).
Least-squares approximation
The most common norm approximation problem involves the Euclidean or ℓ2-
norm. By squaring the objective, we obtain an equivalent problem which is called
the least-squares approximation problem,
minimize
∥Ax −b∥2
2 = r2
1 + r2
2 + · · · + r2
m,
where the objective is the sum of squares of the residuals. This problem can be
solved analytically by expressing the objective as the convex quadratic function
f(x) = xT AT Ax −2bT Ax + bT b.
A point x minimizes f if and only if
∇f(x) = 2AT Ax −2AT b = 0,
i.e., if and only if x satisﬁes the so-called normal equations
AT Ax = AT b,
which always have a solution. Since we assume the columns of A are independent,
the least-squares approximation problem has the unique solution x = (AT A)−1AT b.
Chebyshev or minimax approximation
When the ℓ∞-norm is used, the norm approximation problem
minimize
∥Ax −b∥∞= max{|r1|, . . . , |rm|}
is called the Chebyshev approximation problem, or minimax approximation problem,
since we are to minimize the maximum (absolute value) residual. The Chebyshev
approximation problem can be cast as an LP
minimize
t
subject to
−t1 ⪯Ax −b ⪯t1,
with variables x ∈Rn and t ∈R.


## Page 28

294
6
Approximation and ﬁtting
Sum of absolute residuals approximation
When the ℓ1-norm is used, the norm approximation problem
minimize
∥Ax −b∥1 = |r1| + · · · + |rm|
is called the sum of (absolute) residuals approximation problem, or, in the context
of estimation, a robust estimator (for reasons that will be clear soon). Like the
Chebyshev approximation problem, the ℓ1-norm approximation problem can be
cast as an LP
minimize
1T t
subject to
−t ⪯Ax −b ⪯t,
with variables x ∈Rn and t ∈Rm.
6.1.2
Penalty function approximation
In ℓp-norm approximation, for 1 ≤p < ∞, the objective is
(|r1|p + · · · + |rm|p)1/p .
As in least-squares problems, we can consider the equivalent problem with objective
|r1|p + · · · + |rm|p,
which is a separable and symmetric function of the residuals. In particular, the
objective depends only on the amplitude distribution of the residuals, i.e., the
residuals in sorted order.
We will consider a useful generalization of the ℓp-norm approximation problem,
in which the objective depends only on the amplitude distribution of the residuals.
The penalty function approximation problem has the form
minimize
φ(r1) + · · · + φ(rm)
subject to
r = Ax −b,
(6.2)
where φ : R →R is called the (residual) penalty function. We assume that φ is
convex, so the penalty function approximation problem is a convex optimization
problem. In many cases, the penalty function φ is symmetric, nonnegative, and
satisﬁes φ(0) = 0, but we will not use these properties in our analysis.
Interpretation
We can interpret the penalty function approximation problem (6.2) as follows. For
the choice x, we obtain the approximation Ax of b, which has the associated resid-
ual vector r. A penalty function assesses a cost or penalty for each component
of residual, given by φ(ri); the total penalty is the sum of the penalties for each
residual, i.e., φ(r1) + · · · + φ(rm). Diﬀerent choices of x lead to diﬀerent resulting
residuals, and therefore, diﬀerent total penalties. In the penalty function approxi-
mation problem, we minimize the total penalty incurred by the residuals.


## Page 29

6.1
Norm approximation
295
u
φ(u)
deadzone-linear
quadratic
log barrier
−1.5
−1
−0.5
0
0.5
1
1.5
0
0.5
1
1.5
2
Figure 6.1 Some common penalty functions: the quadratic penalty function
φ(u) = u2, the deadzone-linear penalty function with deadzone width a =
1/4, and the log barrier penalty function with limit a = 1.
Example 6.1 Some common penalty functions and associated approximation problems.
• By taking φ(u) = |u|p, where p ≥1, the penalty function approximation prob-
lem is equivalent to the ℓp-norm approximation problem.
In particular, the
quadratic penalty function φ(u) = u2 yields least-squares or Euclidean norm
approximation, and the absolute value penalty function φ(u) = |u| yields ℓ1-
norm approximation.
• The deadzone-linear penalty function (with deadzone width a > 0) is given by
φ(u) =

0
|u| ≤a
|u| −a
|u| > a.
The deadzone-linear function assesses no penalty for residuals smaller than a.
• The log barrier penalty function (with limit a > 0) has the form
φ(u) =

−a2 log(1 −(u/a)2)
|u| < a
∞
|u| ≥a.
The log barrier penalty function assesses an inﬁnite penalty for residuals larger
than a.
A deadzone-linear, log barrier, and quadratic penalty function are plotted in ﬁg-
ure 6.1. Note that the log barrier function is very close to the quadratic penalty for
|u/a| ≤0.25 (see exercise 6.1).
Scaling the penalty function by a positive number does not aﬀect the solution of
the penalty function approximation problem, since this merely scales the objective


## Page 30

296
6
Approximation and ﬁtting
function. But the shape of the penalty function has a large eﬀect on the solution of
the penalty function approximation problem. Roughly speaking, φ(u) is a measure
of our dislike of a residual of value u. If φ is very small (or even zero) for small
values of u, it means we care very little (or not at all) if residuals have these values.
If φ(u) grows rapidly as u becomes large, it means we have a strong dislike for
large residuals; if φ becomes inﬁnite outside some interval, it means that residuals
outside the interval are unacceptable. This simple interpretation gives insight into
the solution of a penalty function approximation problem, as well as guidelines for
choosing a penalty function.
As an example, let us compare ℓ1-norm and ℓ2-norm approximation, associ-
ated with the penalty functions φ1(u) = |u| and φ2(u) = u2, respectively. For
|u| = 1, the two penalty functions assign the same penalty. For small u we have
φ1(u) ≫φ2(u), so ℓ1-norm approximation puts relatively larger emphasis on small
residuals compared to ℓ2-norm approximation. For large u we have φ2(u) ≫φ1(u),
so ℓ1-norm approximation puts less weight on large residuals, compared to ℓ2-norm
approximation. This diﬀerence in relative weightings for small and large residuals
is reﬂected in the solutions of the associated approximation problems. The ampli-
tude distribution of the optimal residual for the ℓ1-norm approximation problem
will tend to have more zero and very small residuals, compared to the ℓ2-norm ap-
proximation solution. In contrast, the ℓ2-norm solution will tend to have relatively
fewer large residuals (since large residuals incur a much larger penalty in ℓ2-norm
approximation than in ℓ1-norm approximation).
Example
An example will illustrate these ideas. We take a matrix A ∈R100×30 and vector
b ∈R100 (chosen at random, but the results are typical), and compute the ℓ1-norm
and ℓ2-norm approximate solutions of Ax ≈b, as well as the penalty function
approximations with a deadzone-linear penalty (with a = 0.5) and log barrier
penalty (with a = 1).
Figure 6.2 shows the four associated penalty functions,
and the amplitude distributions of the optimal residuals for these four penalty
approximations. From the plots of the penalty functions we note that
• The ℓ1-norm penalty puts the most weight on small residuals and the least
weight on large residuals.
• The ℓ2-norm penalty puts very small weight on small residuals, but strong
weight on large residuals.
• The deadzone-linear penalty function puts no weight on residuals smaller
than 0.5, and relatively little weight on large residuals.
• The log barrier penalty puts weight very much like the ℓ2-norm penalty for
small residuals, but puts very strong weight on residuals larger than around
0.8, and inﬁnite weight on residuals larger than 1.
Several features are clear from the amplitude distributions:
• For the ℓ1-optimal solution, many residuals are either zero or very small. The
ℓ1-optimal solution also has relatively more large residuals.


## Page 31

6.1
Norm approximation
297
p = 1
p = 2
Deadzone
Log barrier
r
−2
−2
−2
−2
−1
−1
−1
−1
0
0
0
0
1
1
1
1
2
2
2
2
0
40
0
10
0
20
0
10
Figure 6.2 Histogram of residual amplitudes for four penalty functions, with
the (scaled) penalty functions also shown for reference. For the log barrier
plot, the quadratic penalty is also shown, in dashed curve.


## Page 32

298
6
Approximation and ﬁtting
u
φ(u)
−1.5
−1
−0.5
0
0.5
1
1.5
0
0.5
1
1.5
Figure 6.3 A (nonconvex) penalty function that assesses a ﬁxed penalty to
residuals larger than a threshold (which in this example is one): φ(u) = u2
if |u| ≤1 and φ(u) = 1 if |u| > 1. As a result, penalty approximation with
this function would be relatively insensitive to outliers.
• The ℓ2-norm approximation has many modest residuals, and relatively few
larger ones.
• For the deadzone-linear penalty, we see that many residuals have the value
±0.5, right at the edge of the ‘free’ zone, for which no penalty is assessed.
• For the log barrier penalty, we see that no residuals have a magnitude larger
than 1, but otherwise the residual distribution is similar to the residual dis-
tribution for ℓ2-norm approximation.
Sensitivity to outliers or large errors
In the estimation or regression context, an outlier is a measurement yi = aT
i x + vi
for which the noise vi is relatively large. This is often associated with faulty data
or a ﬂawed measurement. When outliers occur, any estimate of x will be associated
with a residual vector with some large components. Ideally we would like to guess
which measurements are outliers, and either remove them from the estimation
process or greatly lower their weight in forming the estimate. (We cannot, however,
assign zero penalty for very large residuals, because then the optimal point would
likely make all residuals large, which yields a total penalty of zero.) This could be
accomplished using penalty function approximation, with a penalty function such
as
φ(u) =

u2
|u| ≤M
M 2
|u| > M,
(6.3)
shown in ﬁgure 6.3. This penalty function agrees with least-squares for any residual
smaller than M, but puts a ﬁxed weight on any residual larger than M, no matter
how much larger it is. In other words, residuals larger than M are ignored; they
are assumed to be associated with outliers or bad data. Unfortunately, the penalty


## Page 33

6.1
Norm approximation
299
u
φhub(u)
−1.5
−1
−0.5
0
0.5
1
1.5
0
0.5
1
1.5
2
Figure 6.4 The solid line is the robust least-squares or Huber penalty func-
tion φhub, with M = 1. For |u| ≤M it is quadratic, and for |u| > M it
grows linearly.
function (6.3) is not convex, and the associated penalty function approximation
problem becomes a hard combinatorial optimization problem.
The sensitivity of a penalty function based estimation method to outliers de-
pends on the (relative) value of the penalty function for large residuals.
If we
restrict ourselves to convex penalty functions (which result in convex optimization
problems), the ones that are least sensitive are those for which φ(u) grows linearly,
i.e., like |u|, for large u. Penalty functions with this property are sometimes called
robust, since the associated penalty function approximation methods are much less
sensitive to outliers or large errors than, for example, least-squares.
One obvious example of a robust penalty function is φ(u) = |u|, corresponding
to ℓ1-norm approximation. Another example is the robust least-squares or Huber
penalty function, given by
φhub(u) =

u2
|u| ≤M
M(2|u| −M)
|u| > M,
(6.4)
shown in ﬁgure 6.4. This penalty function agrees with the least-squares penalty
function for residuals smaller than M, and then reverts to ℓ1-like linear growth for
larger residuals. The Huber penalty function can be considered a convex approx-
imation of the outlier penalty function (6.3), in the following sense: They agree
for |u| ≤M, and for |u| > M, the Huber penalty function is the convex function
closest to the outlier penalty function (6.3).
Example 6.2 Robust regression. Figure 6.5 shows 42 points (ti, yi) in a plane, with
two obvious outliers (one at the upper left, and one at lower right). The dashed line
shows the least-squares approximation of the points by a straight line f(t) = α + βt.
The coeﬃcients α and β are obtained by solving the least-squares problem
minimize
P42
i=1(yi −α −βti)2,


## Page 34

300
6
Approximation and ﬁtting
t
f(t)
−10
−5
0
5
10
−20
−10
0
10
20
Figure 6.5 The 42 circles show points that can be well approximated by
an aﬃne function, except for the two outliers at upper left and lower right.
The dashed line is the least-squares ﬁt of a straight line f(t) = α + βt
to the points, and is rotated away from the main locus of points, toward
the outliers. The solid line shows the robust least-squares ﬁt, obtained by
minimizing Huber’s penalty function with M = 1. This gives a far better ﬁt
to the non-outlier data.
with variables α and β. The least-squares approximation is clearly rotated away from
the main locus of the points, toward the two outliers.
The solid line shows the robust least-squares approximation, obtained by minimizing
the Huber penalty function
minimize
P42
i=1 φhub(yi −α −βti),
with M = 1. This approximation is far less aﬀected by the outliers.
Since ℓ1-norm approximation is among the (convex) penalty function approxi-
mation methods that are most robust to outliers, ℓ1-norm approximation is some-
times called robust estimation or robust regression. The robustness property of
ℓ1-norm estimation can also be understood in a statistical framework; see page 353.
Small residuals and ℓ1-norm approximation
We can also focus on small residuals. Least-squares approximation puts very small
weight on small residuals, since φ(u) = u2 is very small when u is small. Penalty
functions such as the deadzone-linear penalty function put zero weight on small
residuals. For penalty functions that are very small for small residuals, we expect
the optimal residuals to be small, but not very small. Roughly speaking, there is
little or no incentive to drive small residuals smaller.
In contrast, penalty functions that put relatively large weight on small residuals,
such as φ(u) = |u|, corresponding to ℓ1-norm approximation, tend to produce


## Page 35

6.1
Norm approximation
301
optimal residuals many of which are very small, or even exactly zero. This means
that in ℓ1-norm approximation, we typically ﬁnd that many of the equations are
satisﬁed exactly, i.e., we have aT
i x = bi for many i. This phenomenon can be seen
in ﬁgure 6.2.
6.1.3
Approximation with constraints
It is possible to add constraints to the basic norm approximation problem (6.1).
When these constraints are convex, the resulting problem is convex. Constraints
arise for a variety of reasons.
• In an approximation problem, constraints can be used to rule out certain un-
acceptable approximations of the vector b, or to ensure that the approximator
Ax satisﬁes certain properties.
• In an estimation problem, the constraints arise as prior knowledge of the
vector x to be estimated, or from prior knowledge of the estimation error v.
• Constraints arise in a geometric setting in determining the projection of a
point b on a set more complicated than a subspace, for example, a cone or
polyhedron.
Some examples will make these clear.
Nonnegativity constraints on variables
We can add the constraint x ⪰0 to the basic norm approximation problem:
minimize
∥Ax −b∥
subject to
x ⪰0.
In an estimation setting, nonnegativity constraints arise when we estimate a vector
x of parameters known to be nonnegative, e.g., powers, intensities, or rates. The
geometric interpretation is that we are determining the projection of a vector b onto
the cone generated by the columns of A. We can also interpret this problem as
approximating b using a nonnegative linear (i.e., conic) combination of the columns
of A.
Variable bounds
Here we add the constraint l ⪯x ⪯u, where l, u ∈Rn are problem parameters:
minimize
∥Ax −b∥
subject to
l ⪯x ⪯u.
In an estimation setting, variable bounds arise as prior knowledge of intervals in
which each variable lies. The geometric interpretation is that we are determining
the projection of a vector b onto the image of a box under the linear mapping
induced by A.


## Page 36

302
6
Approximation and ﬁtting
Probability distribution
We can impose the constraint that x satisfy x ⪰0, 1T x = 1:
minimize
∥Ax −b∥
subject to
x ⪰0,
1T x = 1.
This would arise in the estimation of proportions or relative frequencies, which are
nonnegative and sum to one. It can also be interpreted as approximating b by a
convex combination of the columns of A. (We will have much more to say about
estimating probabilities in §7.2.)
Norm ball constraint
We can add to the basic norm approximation problem the constraint that x lie in
a norm ball:
minimize
∥Ax −b∥
subject to
∥x −x0∥≤d,
where x0 and d are problem parameters. Such a constraint can be added for several
reasons.
• In an estimation setting, x0 is a prior guess of what the parameter x is, and d
is the maximum plausible deviation of our estimate from our prior guess. Our
estimate of the parameter x is the value ˆx which best matches the measured
data (i.e., minimizes ∥Az −b∥) among all plausible candidates (i.e., z that
satisfy ∥z −x0∥≤d).
• The constraint ∥x−x0∥≤d can denote a trust region. Here the linear relation
y = Ax is only an approximation of some nonlinear relation y = f(x) that is
valid when x is near some point x0, speciﬁcally ∥x −x0∥≤d. The problem
is to minimize ∥Ax −b∥but only over those x for which the model y = Ax is
trusted.
These ideas also come up in the context of regularization; see §6.3.2.
6.2
Least-norm problems
The basic least-norm problem has the form
minimize
∥x∥
subject to
Ax = b
(6.5)
where the data are A ∈Rm×n and b ∈Rm, the variable is x ∈Rn, and ∥· ∥is a
norm on Rn. A solution of the problem, which always exists if the linear equations
Ax = b have a solution, is called a least-norm solution of Ax = b. The least-norm
problem is, of course, a convex optimization problem.
We can assume without loss of generality that the rows of A are independent, so
m ≤n. When m = n, the only feasible point is x = A−1b; the least-norm problem
is interesting only when m < n, i.e., when the equation Ax = b is underdetermined.


## Page 37

6.2
Least-norm problems
303
Reformulation as norm approximation problem
The least-norm problem (6.5) can be formulated as a norm approximation problem
by eliminating the equality constraint. Let x0 be any solution of Ax = b, and let
Z ∈Rn×k be a matrix whose columns are a basis for the nullspace of A. The
general solution of Ax = b can then be expressed as x0 + Zu where u ∈Rk. The
least-norm problem (6.5) can be expressed as
minimize
∥x0 + Zu∥,
with variable u ∈Rk, which is a norm approximation problem.
In particular,
our analysis and discussion of norm approximation problems applies to least-norm
problems as well (when interpreted correctly).
Control or design interpretation
We can interpret the least-norm problem (6.5) as a problem of optimal design or
optimal control. The n variables x1, . . . , xn are design variables whose values are
to be determined. In a control setting, the variables x1, . . . , xn represent inputs,
whose values we are to choose. The vector y = Ax gives m attributes or results of
the design x, which we assume to be linear functions of the design variables x. The
m < n equations Ax = b represent m speciﬁcations or requirements on the design.
Since m < n, the design is underspeciﬁed; there are n −m degrees of freedom in
the design (assuming A is rank m).
Among all the designs that satisfy the speciﬁcations, the least-norm problem
chooses the smallest design, as measured by the norm ∥· ∥. This can be thought of
as the most eﬃcient design, in the sense that it achieves the speciﬁcations Ax = b,
with the smallest possible x.
Estimation interpretation
We assume that x is a vector of parameters to be estimated. We have m < n
perfect (noise free) linear measurements, given by Ax = b. Since we have fewer
measurements than parameters to estimate, our measurements do not completely
determine x. Any parameter vector x that satisﬁes Ax = b is consistent with our
measurements.
To make a good guess about what x is, without taking further measurements,
we must use prior information. Suppose our prior information, or assumption, is
that x is more likely to be small (as measured by ∥· ∥) than large. The least-norm
problem chooses as our estimate of the parameter vector x the one that is smallest
(hence, most plausible) among all parameter vectors that are consistent with the
measurements Ax = b. (For a statistical interpretation of the least-norm problem,
see page 359.)
Geometric interpretation
We can also give a simple geometric interpretation of the least-norm problem (6.5).
The feasible set {x | Ax = b} is aﬃne, and the objective is the distance (measured
by the norm ∥· ∥) between x and the point 0. The least-norm problem ﬁnds the


## Page 38

304
6
Approximation and ﬁtting
point in the aﬃne set with minimum distance to 0, i.e., it determines the projection
of the point 0 on the aﬃne set {x | Ax = b}.
Least-squares solution of linear equations
The most common least-norm problem involves the Euclidean or ℓ2-norm.
By
squaring the objective we obtain the equivalent problem
minimize
∥x∥2
2
subject to
Ax = b,
the unique solution of which is called the least-squares solution of the equations
Ax = b. Like the least-squares approximation problem, this problem can be solved
analytically. Introducing the dual variable ν ∈Rm, the optimality conditions are
2x⋆+ AT ν⋆= 0,
Ax⋆= b,
which is a pair of linear equations, and readily solved. From the ﬁrst equation
we obtain x⋆= −(1/2)AT ν⋆; substituting this into the second equation we obtain
−(1/2)AAT ν⋆= b, and conclude
ν⋆= −2(AAT )−1b,
x⋆= AT (AAT )−1b.
(Since rank A = m < n, the matrix AAT is invertible.)
Least-penalty problems
A useful variation on the least-norm problem (6.5) is the least-penalty problem
minimize
φ(x1) + · · · + φ(xn)
subject to
Ax = b,
(6.6)
where φ : R →R is convex, nonnegative, and satisﬁes φ(0) = 0. The penalty
function value φ(u) quantiﬁes our dislike of a component of x having value u;
the least-penalty problem then ﬁnds x that has least total penalty, subject to the
constraint Ax = b.
All of the discussion and interpretation of penalty functions in penalty function
approximation can be transposed to the least-penalty problem, by substituting
the amplitude distribution of x (in the least-penalty problem) for the amplitude
distribution of the residual r (in the penalty approximation problem).
Sparse solutions via least ℓ1-norm
Recall from the discussion on page 300 that ℓ1-norm approximation gives relatively
large weight to small residuals, and therefore results in many optimal residuals
small, or even zero. A similar eﬀect occurs in the least-norm context. The least
ℓ1-norm problem,
minimize
∥x∥1
subject to
Ax = b,
tends to produce a solution x with a large number of components equal to zero.
In other words, the least ℓ1-norm problem tends to produce sparse solutions of
Ax = b, often with m nonzero components.


## Page 39

6.3
Regularized approximation
305
It is easy to ﬁnd solutions of Ax = b that have only m nonzero components.
Choose any set of m indices (out of 1, . . . , n) which are to be the nonzero com-
ponents of x. The equation Ax = b reduces to ˜A˜x = b, where ˜A is the m × m
submatrix of A obtained by selecting only the chosen columns, and ˜x ∈Rm is the
subvector of x containing the m selected components. If ˜A is nonsingular, then
we can take ˜x = ˜A−1b, which gives a feasible solution x with m or less nonzero
components. If ˜A is singular and b̸ ∈R( ˜A), the equation ˜A˜x = b is unsolvable,
which means there is no feasible x with the chosen set of nonzero components. If
˜A is singular and b ∈R( ˜A), there is a feasible solution with fewer than m nonzero
components.
This approach can be used to ﬁnd the smallest x with m (or fewer) nonzero
entries, but in general requires examining and comparing all n!/(m!(n−m)!) choices
of m nonzero coeﬃcients of the n coeﬃcients in x.
Solving the least ℓ1-norm
problem, on the other hand, gives a good heuristic for ﬁnding a sparse, and small,
solution of Ax = b.
6.3
Regularized approximation
6.3.1
Bi-criterion formulation
In the basic form of regularized approximation, the goal is to ﬁnd a vector x that
is small (if possible), and also makes the residual Ax −b small. This is naturally
described as a (convex) vector optimization problem with two objectives, ∥Ax −b∥
and ∥x∥:
minimize (w.r.t. R2
+)
(∥Ax −b∥, ∥x∥) .
(6.7)
The two norms can be diﬀerent: the ﬁrst, used to measure the size of the residual,
is on Rm; the second, used to measure the size of x, is on Rn.
The optimal trade-oﬀbetween the two objectives can be found using several
methods. The optimal trade-oﬀcurve of ∥Ax −b∥versus ∥x∥, which shows how
large one of the objectives must be made to have the other one small, can then be
plotted. One endpoint of the optimal trade-oﬀcurve between ∥Ax −b∥and ∥x∥
is easy to describe. The minimum value of ∥x∥is zero, and is achieved only when
x = 0. For this value of x, the residual norm has the value ∥b∥.
The other endpoint of the trade-oﬀcurve is more complicated to describe. Let
C denote the set of minimizers of ∥Ax −b∥(with no constraint on ∥x∥). Then any
minimum norm point in C is Pareto optimal, corresponding to the other endpoint
of the trade-oﬀcurve. In other words, Pareto optimal points at this endpoint are
given by minimum norm minimizers of ∥Ax−b∥. If both norms are Euclidean, this
Pareto optimal point is unique, and given by x = A†b, where A† is the pseudo-
inverse of A. (See §4.7.6, page 184, and §A.5.4.)


## Page 40

306
6
Approximation and ﬁtting
6.3.2
Regularization
Regularization is a common scalarization method used to solve the bi-criterion
problem (6.7). One form of regularization is to minimize the weighted sum of the
objectives:
minimize
∥Ax −b∥+ γ∥x∥,
(6.8)
where γ > 0 is a problem parameter. As γ varies over (0, ∞), the solution of (6.8)
traces out the optimal trade-oﬀcurve.
Another common method of regularization, especially when the Euclidean norm
is used, is to minimize the weighted sum of squared norms, i.e.,
minimize
∥Ax −b∥2 + δ∥x∥2,
(6.9)
for a variety of values of δ > 0.
These regularized approximation problems each solve the bi-criterion problem
of making both ∥Ax −b∥and ∥x∥small, by adding an extra term or penalty
associated with the norm of x.
Interpretations
Regularization is used in several contexts. In an estimation setting, the extra term
penalizing large ∥x∥can be interpreted as our prior knowledge that ∥x∥is not too
large. In an optimal design setting, the extra term adds the cost of using large
values of the design variables to the cost of missing the target speciﬁcations.
The constraint that ∥x∥be small can also reﬂect a modeling issue. It might be,
for example, that y = Ax is only a good approximation of the true relationship
y = f(x) between x and y. In order to have f(x) ≈b, we want Ax ≈b, and also
need x small in order to ensure that f(x) ≈Ax.
We will see in §6.4.1 and §6.4.2 that regularization can be used to take into
account variation in the matrix A. Roughly speaking, a large x is one for which
variation in A causes large variation in Ax, and hence should be avoided.
Regularization is also used when the matrix A is square, and the goal is to
solve the linear equations Ax = b. In cases where A is poorly conditioned, or even
singular, regularization gives a compromise between solving the equations (i.e.,
making ∥Ax −b∥zero) and keeping x of reasonable size.
Regularization comes up in a statistical setting; see §7.1.2.
Tikhonov regularization
The most common form of regularization is based on (6.9), with Euclidean norms,
which results in a (convex) quadratic optimization problem:
minimize
∥Ax −b∥2
2 + δ∥x∥2
2 = xT (AT A + δI)x −2bT Ax + bT b.
(6.10)
This Tikhonov regularization problem has the analytical solution
x = (AT A + δI)−1AT b.
Since AT A + δI ≻0 for any δ > 0, the Tikhonov regularized least-squares solution
requires no rank (or dimension) assumptions on the matrix A.
