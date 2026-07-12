# temp_chunk_480_to_520



## Page 1

9.3
Gradient descent method
467
step length that minimizes ˜f. The righthand side is a simple quadratic, which
is minimized by t = 1/M, and has minimum value f(x) −(1/(2M))∥∇f(x)∥2
2.
Therefore we have
f(x+) = ˜f(texact) ≤f(x) −
1
2M ∥∇(f(x))∥2
2.
Subtracting p⋆from both sides, we get
f(x+) −p⋆≤f(x) −p⋆−
1
2M ∥∇f(x)∥2
2.
We combine this with ∥∇f(x)∥2
2 ≥2m(f(x) −p⋆) (which follows from (9.9)) to
conclude
f(x+) −p⋆≤(1 −m/M)(f(x) −p⋆).
Applying this inequality recursively, we ﬁnd that
f(x(k)) −p⋆≤ck(f(x(0)) −p⋆)
(9.18)
where c = 1 −m/M < 1, which shows that f(x(k)) converges to p⋆as k →∞. In
particular, we must have f(x(k)) −p⋆≤ǫ after at most
log((f(x(0)) −p⋆)/ǫ)
log(1/c)
(9.19)
iterations of the gradient method with exact line search.
This bound on the number of iterations required, even though crude, can give
some insight into the gradient method. The numerator,
log((f(x(0)) −p⋆)/ǫ)
can be interpreted as the log of the ratio of the initial suboptimality (i.e., gap
between f(x(0)) and p⋆), to the ﬁnal suboptimality (i.e., less than ǫ). This term
suggests that the number of iterations depends on how good the initial point is,
and what the ﬁnal required accuracy is.
The denominator appearing in the bound (9.19), log(1/c), is a function of M/m,
which we have seen is a bound on the condition number of ∇2f(x) over S, or the
condition number of the sublevel sets {z | f(z) ≤α}. For large condition number
bound M/m, we have
log(1/c) = −log(1 −m/M) ≈m/M,
so our bound on the number of iterations required increases approximately linearly
with increasing M/m.
We will see that the gradient method does in fact require a large number of
iterations when the Hessian of f, near x⋆, has a large condition number. Conversely,
when the sublevel sets of f are relatively isotropic, so that the condition number
bound M/m can be chosen to be relatively small, the bound (9.18) shows that
convergence is rapid, since c is small, or at least not too close to one.
The bound (9.18) shows that the error f(x(k)) −p⋆converges to zero at least
as fast as a geometric series. In the context of iterative numerical methods, this
is called linear convergence, since the error lies below a line on a log-linear plot of
error versus iteration number.


## Page 2

468
9
Unconstrained minimization
Analysis for backtracking line search
Now we consider the case where a backtracking line search is used in the gradient
descent method. We will show that the backtracking exit condition,
˜f(t) ≤f(x) −αt∥∇f(x)∥2
2,
is satisﬁed whenever 0 ≤t ≤1/M. First note that
0 ≤t ≤1/M =⇒
−t + Mt2
2
≤−t/2
(which follows from convexity of −t+Mt2/2). Using this result and the bound (9.17),
we have, for 0 ≤t ≤1/M,
˜f(t)
≤
f(x) −t∥∇f(x)∥2
2 + Mt2
2
∥∇(f(x))∥2
2
≤
f(x) −(t/2)∥∇f(x)∥2
2
≤
f(x) −αt∥∇f(x)∥2
2,
since α < 1/2. Therefore the backtracking line search terminates either with t = 1
or with a value t ≥β/M. This provides a lower bound on the decrease in the
objective function. In the ﬁrst case we have
f(x+) ≤f(x) −α∥∇f(x)∥2
2,
and in the second case we have
f(x+) ≤f(x) −(βα/M)∥∇f(x)∥2
2.
Putting these together, we always have
f(x+) ≤f(x) −min{α, βα/M}∥∇f(x)∥2
2.
Now we can proceed exactly as in the case of exact line search. We subtract p⋆
from both sides to get
f(x+) −p⋆≤f(x) −p⋆−min{α, βα/M}∥∇f(x)∥2
2,
and combine this with ∥∇f(x)∥2
2 ≥2m(f(x) −p⋆) to obtain
f(x+) −p⋆≤(1 −min{2mα, 2βαm/M})(f(x) −p⋆).
From this we conclude
f(x(k)) −p⋆≤ck(f(x(0)) −p⋆)
where
c = 1 −min{2mα, 2βαm/M} < 1.
In particular, f(x(k)) converges to p⋆at least as fast as a geometric series with an
exponent that depends (at least in part) on the condition number bound M/m. In
the terminology of iterative methods, the convergence is at least linear.


## Page 3

9.3
Gradient descent method
469
x1
x2
x(0)
x(1)
−10
0
10
−4
0
4
Figure 9.2 Some contour lines of the function f(x) = (1/2)(x2
1 + 10x2
2). The
condition number of the sublevel sets, which are ellipsoids, is exactly 10.
The ﬁgure shows the iterates of the gradient method with exact line search,
started at x(0) = (10, 1).
9.3.2
Examples
A quadratic problem in R2
Our ﬁrst example is very simple. We consider the quadratic objective function on
R2
f(x) = 1
2(x2
1 + γx2
2),
where γ > 0. Clearly, the optimal point is x⋆= 0, and the optimal value is 0. The
Hessian of f is constant, and has eigenvalues 1 and γ, so the condition numbers of
the sublevel sets of f are all exactly
max{1, γ}
min{1, γ} = max{γ, 1/γ}.
The tightest choices for the strong convexity constants m and M are
m = min{1, γ},
M = max{1, γ}.
We apply the gradient descent method with exact line search, starting at the
point x(0) = (γ, 1). In this case we can derive the following closed-form expressions
for the iterates x(k) and their function values (exercise 9.6):
x(k)
1
= γ
γ −1
γ + 1
k
,
x(k)
2
=

−γ −1
γ + 1
k
,
and
f(x(k)) = γ(γ + 1)
2
γ −1
γ + 1
2k
=
γ −1
γ + 1
2k
f(x(0)).
This is illustrated in ﬁgure 9.2, for γ = 10.
For this simple example, convergence is exactly linear, i.e., the error is exactly
a geometric series, reduced by the factor |(γ −1)/(γ + 1)|2 at each iteration. For


## Page 4

470
9
Unconstrained minimization
γ = 1, the exact solution is found in one iteration; for γ not far from one (say,
between 1/3 and 3) convergence is rapid. The convergence is very slow for γ ≫1
or γ ≪1.
We can compare the convergence with the bound derived above in §9.3.1. Using
the least conservative values m = min{1, γ} and M = max{1, γ}, the bound (9.18)
guarantees that the error in each iteration is reduced at least by the factor c =
(1 −m/M). We have seen that the error is in fact reduced exactly by the factor
1 −m/M
1 + m/M
2
in each iteration. For small m/M, which corresponds to large condition number,
the upper bound (9.19) implies that the number of iterations required to obtain
a given level of accuracy grows at most like M/m. For this example, the exact
number of iterations required grows approximately like (M/m)/4, i.e., one quarter
of the value of the bound. This shows that for this simple example, the bound on
the number of iterations derived in our simple analysis is only about a factor of four
conservative (using the least conservative values for m and M). In particular, the
convergence rate (as well as its upper bound) is very dependent on the condition
number of the sublevel sets.
A nonquadratic problem in R2
We now consider a nonquadratic example in R2, with
f(x1, x2) = ex1+3x2−0.1 + ex1−3x2−0.1 + e−x1−0.1.
(9.20)
We apply the gradient method with a backtracking line search, with α = 0.1,
β = 0.7. Figure 9.3 shows some level curves of f, and the iterates x(k) generated
by the gradient method (shown as small circles). The lines connecting successive
iterates show the scaled steps,
x(k+1) −x(k) = −t(k)∇f(x(k)).
Figure 9.4 shows the error f(x(k))−p⋆versus iteration k. The plot reveals that
the error converges to zero approximately as a geometric series, i.e., the convergence
is approximately linear. In this example, the error is reduced from about 10 to
about 10−7 in 20 iterations, so the error is reduced by a factor of approximately
10−8/20 ≈0.4 each iteration. This reasonably rapid convergence is predicted by
our convergence analysis, since the sublevel sets of f are not too badly conditioned,
which in turn means that M/m can be chosen as not too large.
To compare backtracking line search with an exact line search, we use the
gradient method with an exact line search, on the same problem, and with the
same starting point. The results are given in ﬁgures 9.5 and 9.4. Here too the
convergence is approximately linear, about twice as fast as the gradient method
with backtracking line search.
With exact line search, the error is reduced by
about 10−11 in 15 iterations, i.e., a reduction by a factor of about 10−11/15 ≈0.2
per iteration.


## Page 5

9.3
Gradient descent method
471
x(0)
x(1)
x(2)
Figure 9.3 Iterates of the gradient method with backtracking line search,
for the problem in R2 with objective f given in (9.20). The dashed curves
are level curves of f, and the small circles are the iterates of the gradient
method. The solid lines, which connect successive iterates, show the scaled
steps t(k)∆x(k).
k
f(x(k)) −p⋆
backtracking l.s.
exact l.s.
0
5
10
15
20
25
10−15
10−10
10−5
100
105
Figure 9.4 Error f(x(k)) −p⋆versus iteration k of the gradient method with
backtracking and exact line search, for the problem in R2 with objective f
given in (9.20). The plot shows nearly linear convergence, with the error
reduced approximately by the factor 0.4 in each iteration of the gradient
method with backtracking line search, and by the factor 0.2 in each iteration
of the gradient method with exact line search.


## Page 6

472
9
Unconstrained minimization
x(0)
x(1)
Figure 9.5 Iterates of the gradient method with exact line search for the
problem in R2 with objective f given in (9.20).
A problem in R100
We next consider a larger example, of the form
f(x) = cT x −
m
X
i=1
log(bi −aT
i x),
(9.21)
with m = 500 terms and n = 100 variables.
The progress of the gradient method with backtracking line search, with pa-
rameters α = 0.1, β = 0.5, is shown in ﬁgure 9.6. In this example we see an initial
approximately linear and fairly rapid convergence for about 20 iterations, followed
by a slower linear convergence. Overall, the error is reduced by a factor of around
106 in around 175 iterations, which gives an average error reduction by a factor of
around 10−6/175 ≈0.92 per iteration. The initial convergence rate, for the ﬁrst 20
iterations, is around a factor of 0.8 per iteration; the slower ﬁnal convergence rate,
after the ﬁrst 20 iterations, is around a factor of 0.94 per iteration.
Figure 9.6 shows the convergence of the gradient method with exact line search.
The convergence is again approximately linear, with an overall error reduction by
approximately a factor 10−6/140 ≈0.91 per iteration. This is only a bit faster than
the gradient method with backtracking line search.
Finally, we examine the inﬂuence of the backtracking line search parameters α
and β on the convergence rate, by determining the number of iterations required
to obtain f(x(k)) −p⋆≤10−5. In the ﬁrst experiment, we ﬁx β = 0.5, and vary
α from 0.05 to 0.5. The number of iterations required varies from about 80, for
larger values of α, in the range 0.2–0.5, to about 170 for smaller values of α. This,
and other experiments, suggest that the gradient method works better with fairly
large α, in the range 0.2–0.5.
Similarly, we can study the eﬀect of the choice of β by ﬁxing α = 0.1 and
varying β from 0.05 to 0.95. Again the variation in the total number of iterations
is not large, ranging from around 80 (when β ≈0.5) to around 200 (for β small,
or near 1). This experiment, and others, suggest that β ≈0.5 is a good choice.


## Page 7

9.3
Gradient descent method
473
k
f(x(k)) −p⋆
exact l.s.
backtracking l.s.
0
50
100
150
200
10−4
10−2
100
102
104
Figure 9.6 Error f(x(k))−p⋆versus iteration k for the gradient method with
backtracking and exact line search, for a problem in R100.
These experiments suggest that the eﬀect of the backtracking parameters on the
convergence is not large, no more than a factor of two or so.
Gradient method and condition number
Our last experiment will illustrate the importance of the condition number of
∇2f(x) (or the sublevel sets) on the rate of convergence of the gradient method.
We start with the function given by (9.21), but replace the variable x by x = T ¯x,
where
T = diag((1, γ1/n, γ2/n, . . . , γ(n−1)/n)),
i.e., we minimize
¯f(¯x) = cT T ¯x −
m
X
i=1
log(bi −aT
i T ¯x).
(9.22)
This gives us a family of optimization problems, indexed by γ, which aﬀects the
problem condition number.
Figure 9.7 shows the number of iterations required to achieve ¯f(¯x(k))−¯p⋆< 10−5
as a function of γ, using a backtracking line search with α = 0.3 and β = 0.7. This
plot shows that for diagonal scaling as small as 10 : 1 (i.e., γ = 10), the number of
iterations grows to more than a thousand; for a diagonal scaling of 20 or more, the
gradient method slows to essentially useless.
The condition number of the Hessian ∇2 ¯f(¯x⋆) at the optimum is shown in
ﬁgure 9.8.
For large and small γ, the condition number increases roughly as
max{γ2, 1/γ2}, in a very similar way as the number of iterations depends on γ.
This shows again that the relation between conditioning and convergence speed is
a real phenomenon, and not just an artifact of our analysis.


## Page 8

474
9
Unconstrained minimization
γ
iterations
10−1
100
101
102
103
Figure 9.7 Number of iterations of the gradient method applied to prob-
lem (9.22).
The vertical axis shows the number of iterations required to
obtain ¯f(¯x(k)) −¯p⋆< 10−5. The horizontal axis shows γ, which is a param-
eter that controls the amount of diagonal scaling. We use a backtracking
line search with α = 0.3, β = 0.7.
γ
κ(∇2 ¯f(¯x⋆))
10−1
100
101
101
102
103
104
Figure 9.8 Condition number of the Hessian of the function at its minimum,
as a function of γ. By comparing this plot with the one in ﬁgure 9.7, we see
that the condition number has a very strong inﬂuence on convergence rate.


## Page 9

9.4
Steepest descent method
475
Conclusions
From the numerical examples shown, and others, we can make the conclusions
summarized below.
• The gradient method often exhibits approximately linear convergence, i.e.,
the error f(x(k)) −p⋆converges to zero approximately as a geometric series.
• The choice of backtracking parameters α, β has a noticeable but not dramatic
eﬀect on the convergence. An exact line search sometimes improves the con-
vergence of the gradient method, but the eﬀect is not large (and probably
not worth the trouble of implementing the exact line search).
• The convergence rate depends greatly on the condition number of the Hessian,
or the sublevel sets. Convergence can be very slow, even for problems that are
moderately well conditioned (say, with condition number in the 100s). When
the condition number is larger (say, 1000 or more) the gradient method is so
slow that it is useless in practice.
The main advantage of the gradient method is its simplicity. Its main disadvantage
is that its convergence rate depends so critically on the condition number of the
Hessian or sublevel sets.
9.4
Steepest descent method
The ﬁrst-order Taylor approximation of f(x + v) around x is
f(x + v) ≈bf(x + v) = f(x) + ∇f(x)T v.
The second term on the righthand side, ∇f(x)T v, is the directional derivative of
f at x in the direction v. It gives the approximate change in f for a small step v.
The step v is a descent direction if the directional derivative is negative.
We now address the question of how to choose v to make the directional deriva-
tive as negative as possible. Since the directional derivative ∇f(x)T v is linear in
v, it can be made as negative as we like by taking v large (provided v is a descent
direction, i.e., ∇f(x)T v < 0). To make the question sensible we have to limit the
size of v, or normalize by the length of v.
Let ∥· ∥be any norm on Rn. We deﬁne a normalized steepest descent direction
(with respect to the norm ∥· ∥) as
∆xnsd = argmin{∇f(x)T v | ∥v∥= 1}.
(9.23)
(We say ‘a’ steepest descent direction because there can be multiple minimizers.)
A normalized steepest descent direction ∆xnsd is a step of unit norm that gives the
largest decrease in the linear approximation of f.
A normalized steepest descent direction can be interpreted geometrically as
follows. We can just as well deﬁne ∆xnsd as
∆xnsd = argmin{∇f(x)T v | ∥v∥≤1},


## Page 10

476
9
Unconstrained minimization
i.e., as the direction in the unit ball of ∥· ∥that extends farthest in the direction
−∇f(x).
It is also convenient to consider a steepest descent step ∆xsd that is unnormal-
ized, by scaling the normalized steepest descent direction in a particular way:
∆xsd = ∥∇f(x)∥∗∆xnsd,
(9.24)
where ∥· ∥∗denotes the dual norm. Note that for the steepest descent step, we
have
∇f(x)T ∆xsd = ∥∇f(x)∥∗∇f(x)T ∆xnsd = −∥∇f(x)∥2
∗
(see exercise 9.7).
The steepest descent method uses the steepest descent direction as search direc-
tion.
Algorithm 9.4 Steepest descent method.
given a starting point x ∈dom f.
repeat
1. Compute steepest descent direction ∆xsd.
2. Line search. Choose t via backtracking or exact line search.
3. Update. x := x + t∆xsd.
until stopping criterion is satisﬁed.
When exact line search is used, scale factors in the descent direction have no eﬀect,
so the normalized or unnormalized direction can be used.
9.4.1
Steepest descent for Euclidean and quadratic norms
Steepest descent for Euclidean norm
If we take the norm ∥·∥to be the Euclidean norm we ﬁnd that the steepest descent
direction is simply the negative gradient, i.e., ∆xsd = −∇f(x).
The steepest
descent method for the Euclidean norm coincides with the gradient descent method.
Steepest descent for quadratic norm
We consider the quadratic norm
∥z∥P = (zT Pz)1/2 = ∥P 1/2z∥2,
where P ∈Sn
++. The normalized steepest descent direction is given by
∆xnsd = −
 ∇f(x)T P −1∇f(x)
−1/2 P −1∇f(x).
The dual norm is given by ∥z∥∗= ∥P −1/2z∥2, so the steepest descent step with
respect to ∥· ∥P is given by
∆xsd = −P −1∇f(x).
(9.25)
The normalized steepest descent direction for a quadratic norm is illustrated in
ﬁgure 9.9.


## Page 11

9.4
Steepest descent method
477
−∇f(x)
∆xnsd
Figure 9.9 Normalized steepest descent direction for a quadratic norm. The
ellipsoid shown is the unit ball of the norm, translated to the point x. The
normalized steepest descent direction ∆xnsd at x extends as far as possible
in the direction −∇f(x) while staying in the ellipsoid. The gradient and
normalized steepest descent directions are shown.
Interpretation via change of coordinates
We can give an interesting alternative interpretation of the steepest descent direc-
tion ∆xsd as the gradient search direction after a change of coordinates is applied
to the problem. Deﬁne ¯u = P 1/2u, so we have ∥u∥P = ∥¯u∥2. Using this change
of coordinates, we can solve the original problem of minimizing f by solving the
equivalent problem of minimizing the function ¯f : Rn →R, given by
¯f(¯u) = f(P −1/2¯u) = f(u).
If we apply the gradient method to ¯f, the search direction at a point ¯x (which
corresponds to the point x = P −1/2¯x for the original problem) is
∆¯x = −∇¯f(¯x) = −P −1/2∇f(P −1/2¯x) = −P −1/2∇f(x).
This gradient search direction corresponds to the direction
∆x = P −1/2 
−P −1/2∇f(x)

= −P −1∇f(x)
for the original variable x. In other words, the steepest descent method in the
quadratic norm ∥· ∥P can be thought of as the gradient method applied to the
problem after the change of coordinates ¯x = P 1/2x.
9.4.2
Steepest descent for ℓ1-norm
As another example, we consider the steepest descent method for the ℓ1-norm. A
normalized steepest descent direction,
∆xnsd = argmin{∇f(x)T v | ∥v∥1 ≤1},


## Page 12

478
9
Unconstrained minimization
−∇f(x)
∆xnsd
Figure 9.10 Normalized steepest descent direction for the ℓ1-norm.
The
diamond is the unit ball of the ℓ1-norm, translated to the point x.
The
normalized steepest descent direction can always be chosen in the direction
of a standard basis vector; in this example we have ∆xnsd = e1.
is easily characterized. Let i be any index for which ∥∇f(x)∥∞= |(∇f(x))i|. Then
a normalized steepest descent direction ∆xnsd for the ℓ1-norm is given by
∆xnsd = −sign
∂f(x)
∂xi

ei,
where ei is the ith standard basis vector. An unnormalized steepest descent step
is then
∆xsd = ∆xnsd∥∇f(x)∥∞= −∂f(x)
∂xi
ei.
Thus, the normalized steepest descent step in ℓ1-norm can always be chosen to be a
standard basis vector (or a negative standard basis vector). It is the coordinate axis
direction along which the approximate decrease in f is greatest. This is illustrated
in ﬁgure 9.10.
The steepest descent algorithm in the ℓ1-norm has a very natural interpretation:
At each iteration we select a component of ∇f(x) with maximum absolute value,
and then decrease or increase the corresponding component of x, according to the
sign of (∇f(x))i. The algorithm is sometimes called a coordinate-descent algorithm,
since only one component of the variable x is updated at each iteration. This can
greatly simplify, or even trivialize, the line search.
Example 9.2
Frobenius norm scaling. In §4.5.4 we encountered the unconstrained
geometric program
minimize
Pn
i,j=1 M 2
ijd2
i /d2
j,
where M ∈Rn×n is given, and the variable is d ∈Rn. Using the change of variables
xi = 2 log di we can express this geometric program in convex form as
minimize
f(x) = log
Pn
i,j=1 M 2
ijexi−xj

.


## Page 13

9.4
Steepest descent method
479
It is easy to minimize f one component at a time. Keeping all components except
the kth ﬁxed, we can write f(x) = log(αk + βke−xk + γkexk), where
αk = M 2
kk +
X
i,j̸=k
M 2
ijexi−xj,
βk =
X
i̸=k
M 2
ikexi,
γk =
X
j̸=k
M 2
kje−xj.
The minimum of f(x), as a function of xk, is obtained for xk = log(βk/γk)/2. So
for this problem an exact line search can be carried out using a simple analytical
formula.
The ℓ1-steepest descent algorithm with exact line search consists of repeating the
following steps.
1. Compute the gradient
(∇f(x))i =
−βie−xi + γiexi
αi + βie−xi + γiexi ,
i = 1, . . . , n.
2. Select a largest (in absolute value) component of ∇f(x): |∇f(x)|k = ∥∇f(x)∥∞.
3. Minimize f over the scalar variable xk, by setting xk = log(βk/γk)/2.
9.4.3
Convergence analysis
In this section we extend the convergence analysis for the gradient method with
backtracking line search to the steepest descent method for an arbitrary norm. We
will use the fact that any norm can be bounded in terms of the Euclidean norm,
so there exists constants γ, ˜γ ∈(0, 1] such that
∥x∥≥γ∥x∥2,
∥x∥∗≥˜γ∥x∥2
(see §A.1.4).
Again we assume f is strongly convex on the initial sublevel set S. The upper
bound ∇2f(x) ⪯MI implies an upper bound on the function f(x + t∆xsd) as a
function of t:
f(x + t∆xsd)
≤
f(x) + t∇f(x)T ∆xsd + M∥∆xsd∥2
2
2
t2
≤
f(x) + t∇f(x)T ∆xsd + M∥∆xsd∥2
2γ2
t2
=
f(x) −t∥∇f(x)∥2
∗+ M
2γ2 t2∥∇f(x)∥2
∗.
(9.26)
The step size ˆt = γ2/M (which minimizes the quadratic upper bound (9.26))
satisﬁes the exit condition for the backtracking line search:
f(x + ˆt∆xsd) ≤f(x) −γ2
2M ∥∇f(x)∥2
∗≤f(x) + αγ2
M ∇f(x)T ∆xsd
(9.27)


## Page 14

480
9
Unconstrained minimization
since α < 1/2 and ∇f(x)T ∆xsd = −∥∇f(x)∥2
∗. The line search therefore returns a
step size t ≥min{1, βγ2/M}, and we have
f(x+) = f(x + t∆xsd)
≤
f(x) −α min{1, βγ2/M}∥∇f(x)∥2
∗
≤
f(x) −α˜γ2 min{1, βγ2/M}∥∇f(x)∥2
2.
Subtracting p⋆from both sides and using (9.9), we obtain
f(x+) −p⋆≤c(f(x) −p⋆),
where
c = 1 −2mα˜γ2 min{1, βγ2/M} < 1.
Therefore we have
f(x(k)) −p⋆≤ck(f(x(0)) −p⋆),
i.e., linear convergence exactly as in the gradient method.
9.4.4
Discussion and examples
Choice of norm for steepest descent
The choice of norm used to deﬁne the steepest descent direction can have a dra-
matic eﬀect on the convergence rate. For simplicity, we consider the case of steep-
est descent with quadratic P-norm. In §9.4.1, we showed that the steepest descent
method with quadratic P-norm is the same as the gradient method applied to the
problem after the change of coordinates ¯x = P 1/2x. We know that the gradient
method works well when the condition numbers of the sublevel sets (or the Hes-
sian near the optimal point) are moderate, and works poorly when the condition
numbers are large. It follows that when the sublevel sets, after the change of coor-
dinates ¯x = P 1/2x, are moderately conditioned, the steepest descent method will
work well.
This observation provides a prescription for choosing P: It should be chosen
so that the sublevel sets of f, transformed by P −1/2, are well conditioned. For
example if an approximation ˆH of the Hessian at the optimal point H(x⋆) were
known, a very good choice of P would be P = ˆH, since the Hessian of ˜f at the
optimum is then
ˆH−1/2∇2f(x⋆) ˆH−1/2 ≈I,
and so is likely to have a low condition number.
This same idea can be described without a change of coordinates. Saying that
a sublevel set has low condition number after the change of coordinates ¯x = P 1/2x
is the same as saying that the ellipsoid
E = {x | xT Px ≤1}
approximates the shape of the sublevel set. (In other words, it gives a good ap-
proximation after appropriate scaling and translation.)
This dependence of the convergence rate on the choice of P can be viewed from
two sides.
The optimist’s viewpoint is that for any problem, there is always a


## Page 15

9.4
Steepest descent method
481
x(0)
x(1)
x(2)
Figure 9.11 Steepest descent method with a quadratic norm ∥· ∥P1. The
ellipses are the boundaries of the norm balls {x | ∥x −x(k)∥P1 ≤1} at x(0)
and x(1).
choice of P for which the steepest descent method works very well. The challenge,
of course, is to ﬁnd such a P. The pessimist’s viewpoint is that for any problem,
there are a huge number of choices of P for which steepest descent works very
poorly. In summary, we can say that the steepest descent method works well in
cases where we can identify a matrix P for which the transformed problem has
moderate condition number.
Examples
In this section we illustrate some of these ideas using the nonquadratic problem in
R2 with objective function (9.20). We apply the steepest descent method to the
problem, using the two quadratic norms deﬁned by
P1 =

2
0
0
8

,
P2 =

8
0
0
2

.
In both cases we use a backtracking line search with α = 0.1 and β = 0.7.
Figures 9.11 and 9.12 show the iterates for steepest descent with norm ∥·∥P1 and
norm ∥· ∥P2.
Figure 9.13 shows the error versus iteration number for both norms.
Figure 9.13 shows that the choice of norm strongly inﬂuences the convergence.
With the norm ∥· ∥P1, convergence is a bit more rapid than the gradient method,
whereas with the norm ∥· ∥P2, convergence is far slower.
This can be explained by examining the problems after the changes of coor-
dinates ¯x = P 1/2
1
x and ¯x = P 1/2
2
x, respectively. Figures 9.14 and 9.15 show the
problems in the transformed coordinates. The change of variables associated with
P1 yields sublevel sets with modest condition number, so convergence is fast. The
change of variables associated with P2 yields sublevel sets that are more poorly
conditioned, which explains the slower convergence.


## Page 16

482
9
Unconstrained minimization
x(0)
x(1)
x(2)
Figure 9.12 Steepest descent method, with quadratic norm ∥· ∥P2.
k
P1
P2
f(x(k)) −p⋆
0
10
20
30
40
10−15
10−10
10−5
100
105
Figure 9.13 Error f(x(k)) −p⋆versus iteration k, for the steepest descent
method with the quadratic norm ∥· ∥P1 and the quadratic norm ∥· ∥P2.
Convergence is rapid for the norm ∥· ∥P1 and very slow for ∥· ∥P2.


## Page 17

9.4
Steepest descent method
483
¯x(0)
¯x(1)
Figure 9.14 The iterates of steepest descent with norm ∥· ∥P1, after the
change of coordinates.
This change of coordinates reduces the condition
number of the sublevel sets, and so speeds up convergence.
¯x(0)
¯x(1)
Figure 9.15 The iterates of steepest descent with norm ∥· ∥P2, after the
change of coordinates. This change of coordinates increases the condition
number of the sublevel sets, and so slows down convergence.


## Page 18

484
9
Unconstrained minimization
f
bf
(x, f(x))
(x + ∆xnt, f(x + ∆xnt))
Figure 9.16 The function f (shown solid) and its second-order approximation
bf at x (dashed). The Newton step ∆xnt is what must be added to x to give
the minimizer of bf.
9.5
Newton’s method
9.5.1
The Newton step
For x ∈dom f, the vector
∆xnt = −∇2f(x)−1∇f(x)
is called the Newton step (for f, at x). Positive deﬁniteness of ∇2f(x) implies that
∇f(x)T ∆xnt = −∇f(x)T ∇2f(x)−1∇f(x) < 0
unless ∇f(x) = 0, so the Newton step is a descent direction (unless x is optimal).
The Newton step can be interpreted and motivated in several ways.
Minimizer of second-order approximation
The second-order Taylor approximation (or model) bf of f at x is
bf(x + v) = f(x) + ∇f(x)T v + 1
2vT ∇2f(x)v,
(9.28)
which is a convex quadratic function of v, and is minimized when v = ∆xnt. Thus,
the Newton step ∆xnt is what should be added to the point x to minimize the
second-order approximation of f at x. This is illustrated in ﬁgure 9.16.
This interpretation gives us some insight into the Newton step. If the function
f is quadratic, then x + ∆xnt is the exact minimizer of f. If the function f is
nearly quadratic, intuition suggests that x + ∆xnt should be a very good estimate
of the minimizer of f, i.e., x⋆. Since f is twice diﬀerentiable, the quadratic model
of f will be very accurate when x is near x⋆. It follows that when x is near x⋆,
the point x + ∆xnt should be a very good estimate of x⋆. We will see that this
intuition is correct.


## Page 19

9.5
Newton’s method
485
x
x + ∆xnt
x + ∆xnsd
Figure 9.17 The dashed lines are level curves of a convex function.
The
ellipsoid shown (with solid line) is {x + v | vT ∇2f(x)v ≤1}. The arrow
shows −∇f(x), the gradient descent direction. The Newton step ∆xnt is
the steepest descent direction in the norm ∥· ∥∇2f(x). The ﬁgure also shows
∆xnsd, the normalized steepest descent direction for the same norm.
Steepest descent direction in Hessian norm
The Newton step is also the steepest descent direction at x, for the quadratic norm
deﬁned by the Hessian ∇2f(x), i.e.,
∥u∥∇2f(x) = (uT ∇2f(x)u)1/2.
This gives another insight into why the Newton step should be a good search
direction, and a very good search direction when x is near x⋆.
Recall from our discussion above that steepest descent, with quadratic norm
∥· ∥P , converges very rapidly when the Hessian, after the associated change of
coordinates, has small condition number. In particular, near x⋆, a very good choice
is P = ∇2f(x⋆). When x is near x⋆, we have ∇2f(x) ≈∇2f(x⋆), which explains
why the Newton step is a very good choice of search direction. This is illustrated
in ﬁgure 9.17.
Solution of linearized optimality condition
If we linearize the optimality condition ∇f(x⋆) = 0 near x we obtain
∇f(x + v) ≈∇f(x) + ∇2f(x)v = 0,
which is a linear equation in v, with solution v = ∆xnt. So the Newton step ∆xnt is
what must be added to x so that the linearized optimality condition holds. Again,
this suggests that when x is near x⋆(so the optimality conditions almost hold),
the update x + ∆xnt should be a very good approximation of x⋆.
When n = 1, i.e., f : R →R, this interpretation is particularly simple. The
solution x⋆of the minimization problem is characterized by f ′(x⋆) = 0, i.e., it is


## Page 20

486
9
Unconstrained minimization
f ′
bf ′
(x, f ′(x))
(x + ∆xnt, f ′(x + ∆xnt))
Figure 9.18 The solid curve is the derivative f ′ of the function f shown in
ﬁgure 9.16. bf ′ is the linear approximation of f ′ at x. The Newton step ∆xnt
is the diﬀerence between the root of bf ′ and the point x.
the zero-crossing of the derivative f ′, which is monotonically increasing since f is
convex. Given our current approximation x of the solution, we form a ﬁrst-order
Taylor approximation of f ′ at x. The zero-crossing of this aﬃne approximation is
then x + ∆xnt. This interpretation is illustrated in ﬁgure 9.18.
Aﬃne invariance of the Newton step
An important feature of the Newton step is that it is independent of linear (or
aﬃne) changes of coordinates.
Suppose T ∈Rn×n is nonsingular, and deﬁne
¯f(y) = f(Ty). Then we have
∇¯f(y) = T T ∇f(x),
∇2 ¯f(y) = T T ∇2f(x)T,
where x = Ty. The Newton step for ¯f at y is therefore
∆ynt
=
−
 T T ∇2f(x)T
−1  T T ∇f(x)

=
−T −1∇2f(x)−1∇f(x)
=
T −1∆xnt,
where ∆xnt is the Newton step for f at x. Hence the Newton steps of f and ¯f are
related by the same linear transformation, and
x + ∆xnt = T(y + ∆ynt).
The Newton decrement
The quantity
λ(x) =
 ∇f(x)T ∇2f(x)−1∇f(x)
1/2
is called the Newton decrement at x.
We will see that the Newton decrement
plays an important role in the analysis of Newton’s method, and is also useful


## Page 21

9.5
Newton’s method
487
as a stopping criterion.
We can relate the Newton decrement to the quantity
f(x) −infy bf(y), where bf is the second-order approximation of f at x:
f(x) −inf
y
bf(y) = f(x) −bf(x + ∆xnt) = 1
2λ(x)2.
Thus, λ2/2 is an estimate of f(x) −p⋆, based on the quadratic approximation of f
at x.
We can also express the Newton decrement as
λ(x) =
 ∆xT
nt∇2f(x)∆xnt
1/2 .
(9.29)
This shows that λ is the norm of the Newton step, in the quadratic norm deﬁned
by the Hessian, i.e., the norm
∥u∥∇2f(x) =
 uT ∇2f(x)u
1/2 .
The Newton decrement comes up in backtracking line search as well, since we have
∇f(x)T ∆xnt = −λ(x)2.
(9.30)
This is the constant used in a backtracking line search, and can be interpreted as
the directional derivative of f at x in the direction of the Newton step:
−λ(x)2 = ∇f(x)T ∆xnt = d
dtf(x + ∆xntt)

t=0
.
Finally, we note that the Newton decrement is, like the Newton step, aﬃne in-
variant. In other words, the Newton decrement of ¯f(y) = f(Ty) at y, where T is
nonsingular, is the same as the Newton decrement of f at x = Ty.
9.5.2
Newton’s method
Newton’s method, as outlined below, is sometimes called the damped Newton
method or guarded Newton method, to distinguish it from the pure Newton method,
which uses a ﬁxed step size t = 1.
Algorithm 9.5 Newton’s method.
given a starting point x ∈dom f, tolerance ǫ > 0.
repeat
1. Compute the Newton step and decrement.
∆xnt := −∇2f(x)−1∇f(x);
λ2 := ∇f(x)T ∇2f(x)−1∇f(x).
2. Stopping criterion. quit if λ2/2 ≤ǫ.
3. Line search. Choose step size t by backtracking line search.
4. Update. x := x + t∆xnt.
This is essentially the general descent method described in §9.2, using the New-
ton step as search direction. The only diﬀerence (which is very minor) is that the
stopping criterion is checked after computing the search direction, rather than after
the update.


## Page 22

488
9
Unconstrained minimization
9.5.3
Convergence analysis
We assume, as before, that f is twice continuously diﬀerentiable, and strongly
convex with constant m, i.e., ∇2f(x) ⪰mI for x ∈S. We have seen that this also
implies that there exists an M > 0 such that ∇2f(x) ⪯MI for all x ∈S.
In addition, we assume that the Hessian of f is Lipschitz continuous on S with
constant L, i.e.,
∥∇2f(x) −∇2f(y)∥2 ≤L∥x −y∥2
(9.31)
for all x, y ∈S. The coeﬃcient L, which can be interpreted as a bound on the
third derivative of f, can be taken to be zero for a quadratic function.
More
generally L measures how well f can be approximated by a quadratic model, so
we can expect the Lipschitz constant L to play a critical role in the performance
of Newton’s method. Intuition suggests that Newton’s method will work very well
for a function whose quadratic model varies slowly (i.e., has small L).
Idea and outline of convergence proof
We ﬁrst give the idea and outline of the convergence proof, and the main conclusion,
and then the details of the proof. We will show there are numbers η and γ with
0 < η ≤m2/L and γ > 0 such that the following hold.
• If ∥∇f(x(k))∥2 ≥η, then
f(x(k+1)) −f(x(k)) ≤−γ.
(9.32)
• If ∥∇f(x(k))∥2 < η, then the backtracking line search selects t(k) = 1 and
L
2m2 ∥∇f(x(k+1))∥2 ≤
 L
2m2 ∥∇f(x(k))∥2
2
.
(9.33)
Let us analyze the implications of the second condition.
Suppose that it
is satisﬁed for iteration k, i.e., ∥∇f(x(k))∥2 < η.
Since η ≤m2/L, we have
∥∇f(x(k+1))∥2 < η, i.e., the second condition is also satisﬁed at iteration k + 1.
Continuing recursively, we conclude that once the second condition holds, it will
hold for all future iterates, i.e., for all l ≥k, we have ∥∇f(x(l))∥2 < η. Therefore
for all l ≥k, the algorithm takes a full Newton step t = 1, and
L
2m2 ∥∇f(x(l+1))∥2 ≤
 L
2m2 ∥∇f(x(l))∥2
2
.
(9.34)
Applying this inequality recursively, we ﬁnd that for l ≥k,
L
2m2 ∥∇f(x(l))∥2 ≤
 L
2m2 ∥∇f(x(k))∥2
2l−k
≤
1
2
2l−k
,
and hence
f(x(l)) −p⋆≤
1
2m∥∇f(x(l))∥2
2 ≤2m3
L2
1
2
2l−k+1
.
(9.35)


## Page 23

9.5
Newton’s method
489
This last inequality shows that convergence is extremely rapid once the second
condition is satisﬁed. This phenomenon is called quadratic convergence. Roughly
speaking, the inequality (9.35) means that, after a suﬃciently large number of
iterations, the number of correct digits doubles at each iteration.
The iterations in Newton’s method naturally fall into two stages. The second
stage, which occurs once the condition ∥∇f(x)∥2 ≤η holds, is called the quadrat-
ically convergent stage. We refer to the ﬁrst stage as the damped Newton phase,
because the algorithm can choose a step size t < 1. The quadratically convergent
stage is also called the pure Newton phase, since in these iterations a step size t = 1
is always chosen.
Now we can estimate the total complexity. First we derive an upper bound on
the number of iterations in the damped Newton phase. Since f decreases by at
least γ at each iteration, the number of damped Newton steps cannot exceed
f(x(0)) −p⋆
γ
,
since if it did, f would be less than p⋆, which is impossible.
We can bound the number of iterations in the quadratically convergent phase
using the inequality (9.35). It implies that we must have f(x) −p⋆≤ǫ after no
more than
log2 log2(ǫ0/ǫ)
iterations in the quadratically convergent phase, where ǫ0 = 2m3/L2.
Overall, then, the number of iterations until f(x) −p⋆≤ǫ is bounded above by
f(x(0)) −p⋆
γ
+ log2 log2(ǫ0/ǫ).
(9.36)
The term log2 log2(ǫ0/ǫ), which bounds the number of iterations in the quadrati-
cally convergent phase, grows extremely slowly with required accuracy ǫ, and can
be considered a constant for practical purposes, say ﬁve or six. (Six iterations of
the quadratically convergent stage gives an accuracy of about ǫ ≈5 · 10−20ǫ0.)
Not quite accurately, then, we can say that the number of Newton iterations
required to minimize f is bounded above by
f(x(0)) −p⋆
γ
+ 6.
(9.37)
A more precise statement is that (9.37) is a bound on the number of iterations to
compute an extremely good approximation of the solution.
Damped Newton phase
We now establish the inequality (9.32). Assume ∥∇f(x)∥2 ≥η. We ﬁrst derive a
lower bound on the step size selected by the line search. Strong convexity implies
that ∇2f(x) ⪯MI on S, and therefore
f(x + t∆xnt)
≤
f(x) + t∇f(x)T ∆xnt + M∥∆xnt∥2
2
2
t2
≤
f(x) −tλ(x)2 + M
2mt2λ(x)2,


## Page 24

490
9
Unconstrained minimization
where we use (9.30) and
λ(x)2 = ∆xT
nt∇2f(x)∆xnt ≥m∥∆xnt∥2
2.
The step size ˆt = m/M satisﬁes the exit condition of the line search, since
f(x + ˆt∆xnt) ≤f(x) −m
2M λ(x)2 ≤f(x) −αˆtλ(x)2.
Therefore the line search returns a step size t ≥βm/M, resulting in a decrease of
the objective function
f(x+) −f(x)
≤
−αtλ(x)2
≤
−αβ m
M λ(x)2
≤
−αβ m
M 2 ∥∇f(x)∥2
2
≤
−αβη2 m
M 2 ,
where we use
λ(x)2 = ∇f(x)T ∇2f(x)−1∇f(x) ≥(1/M)∥∇f(x)∥2
2.
Therefore, (9.32) is satisﬁed with
γ = αβη2 m
M 2 .
(9.38)
Quadratically convergent phase
We now establish the inequality (9.33). Assume ∥∇f(x)∥2 < η. We ﬁrst show that
the backtracking line search selects unit steps, provided
η ≤3(1 −2α)m2
L .
By the Lipschitz condition (9.31), we have, for t ≥0,
∥∇2f(x + t∆xnt) −∇2f(x)∥2 ≤tL∥∆xnt∥2,
and therefore
∆xT
nt
 ∇2f(x + t∆xnt) −∇2f(x)

∆xnt
 ≤tL∥∆xnt∥3
2.
With ˜f(t) = f(x + t∆xnt), we have ˜f ′′(t) = ∆xT
nt∇2f(x + t∆xnt)∆xnt, so the
inequality above is
| ˜f ′′(t) −˜f ′′(0)| ≤tL∥∆xnt∥3
2.
We will use this inequality to determine an upper bound on ˜f(t). We start with
˜f ′′(t) ≤˜f ′′(0) + tL∥∆xnt∥3
2 ≤λ(x)2 + t
L
m3/2 λ(x)3,


## Page 25

9.5
Newton’s method
491
where we use ˜f ′′(0) = λ(x)2 and λ(x)2 ≥m∥∆xnt∥2
2. We integrate the inequality
to get
˜f ′(t)
≤
˜f ′(0) + tλ(x)2 + t2
L
2m3/2 λ(x)3
=
−λ(x)2 + tλ(x)2 + t2
L
2m3/2 λ(x)3,
using ˜f ′(0) = −λ(x)2. We integrate once more to get
˜f(t) ≤˜f(0) −tλ(x)2 + t2 1
2λ(x)2 + t3
L
6m3/2 λ(x)3.
Finally, we take t = 1 to obtain
f(x + ∆xnt) ≤f(x) −1
2λ(x)2 +
L
6m3/2 λ(x)3.
(9.39)
Now suppose ∥∇f(x)∥2 ≤η ≤3(1 −2α)m2/L. By strong convexity, we have
λ(x) ≤3(1 −2α)m3/2/L,
and by (9.39) we have
f(x + ∆xnt)
≤
f(x) −λ(x)2
1
2 −Lλ(x)
6m3/2

≤
f(x) −αλ(x)2
=
f(x) + α∇f(x)T ∆xnt,
which shows that the unit step t = 1 is accepted by the backtracking line search.
Let us now examine the rate of convergence. Applying the Lipschitz condition,
we have
∥∇f(x+)∥2
=
∥∇f(x + ∆xnt) −∇f(x) −∇2f(x)∆xnt∥2
=

Z 1
0
 ∇2f(x + t∆xnt) −∇2f(x)

∆xnt dt

2
≤
L
2 ∥∆xnt∥2
2
=
L
2 ∥∇2f(x)−1∇f(x)∥2
2
≤
L
2m2 ∥∇f(x)∥2
2,
i.e., the inequality (9.33).
In conclusion, the algorithm selects unit steps and satisﬁes the condition (9.33)
if ∥∇f(x(k))∥2 < η, where
η = min {1, 3(1 −2α)} m2
L .
Substituting this bound and (9.38) into (9.37), we ﬁnd that the number of iterations
is bounded above by
6 +
M 2L2/m5
αβ min{1, 9(1 −2α)2}(f(x(0)) −p⋆).
(9.40)


## Page 26

492
9
Unconstrained minimization
x(0)
x(1)
Figure 9.19 Newton’s method for the problem in R2, with objective f given
in (9.20), and backtracking line search parameters α = 0.1, β = 0.7. Also
shown are the ellipsoids {x | ∥x−x(k)∥∇2f(x(k)) ≤1} at the ﬁrst two iterates.
9.5.4
Examples
Example in R2
We ﬁrst apply Newton’s method with backtracking line search on the test func-
tion (9.20), with line search parameters α = 0.1, β = 0.7. Figure 9.19 shows the
Newton iterates, and also the ellipsoids
{x | ∥x −x(k)∥∇2f(x(k)) ≤1}
for the ﬁrst two iterates k = 0, 1. The method works well because these ellipsoids
give good approximations of the shape of the sublevel sets.
Figure 9.20 shows the error versus iteration number for the same example.
This plot shows that convergence to a very high accuracy is achieved in only ﬁve
iterations. Quadratic convergence is clearly apparent: The last step reduces the
error from about 10−5 to 10−10.
Example in R100
Figure 9.21 shows the convergence of Newton’s method with backtracking and exact
line search for a problem in R100. The objective function has the form (9.21), with
the same problem data and the same starting point as was used in ﬁgure 9.6. The
plot for the backtracking line search shows that a very high accuracy is attained in
eight iterations. Like the example in R2, quadratic convergence is clearly evident
after about the third iteration.
The number of iterations in Newton’s method
with exact line search is only one smaller than with a backtracking line search.
This is also typical. An exact line search usually gives a very small improvement in
convergence of Newton’s method. Figure 9.22 shows the step sizes for this example.
After two damped steps, the steps taken by the backtracking line search are all full,
i.e., t = 1.
Experiments with the values of the backtracking parameters α and β reveal that
they have little eﬀect on the performance of Newton’s method, for this example


## Page 27

9.5
Newton’s method
493
k
f(x(k)) −p⋆
0
1
2
3
4
5
10−15
10−10
10−5
100
105
Figure 9.20 Error versus iteration k of Newton’s method for the problem
in R2. Convergence to a very high accuracy is achieved in ﬁve iterations.
k
f(x(k)) −p⋆
exact l.s.
backtracking l.s.
0
2
4
6
8
10
10−15
10−10
10−5
100
105
Figure 9.21 Error versus iteration for Newton’s method for the problem in
R100. The backtracking line search parameters are α = 0.01, β = 0.5. Here
too convergence is extremely rapid: a very high accuracy is attained in only
seven or eight iterations. The convergence of Newton’s method with exact
line search is only one iteration faster than with backtracking line search.


## Page 28

494
9
Unconstrained minimization
k
step size t(k)
exact l.s.
backtracking l.s.
0
2
4
6
8
0
0.5
1
1.5
2
Figure 9.22 The step size t versus iteration for Newton’s method with back-
tracking and exact line search, applied to the problem in R100. The back-
tracking line search takes one backtracking step in the ﬁrst two iterations.
After the ﬁrst two iterations it always selects t = 1.
(and others). With α ﬁxed at 0.01, and values of β varying between 0.2 and 1,
the number of iterations required varies between 8 and 12. With β ﬁxed at 0.5,
the number of iterations is 8, for all values of α between 0.005 and 0.5. For these
reasons, most practical implementations use a backtracking line search with a small
value of α, such as 0.01, and a larger value of β, such as 0.5.
Example in R10000
In this last example we consider a larger problem, of the form
minimize −
n
X
i=1
log(1 −x2
i ) −
m
X
i=1
log(bi −aT
i x)
with m = 100000 and n = 10000. The problem data ai are randomly generated
sparse vectors. Figure 9.23 shows the convergence of Newton’s method with back-
tracking line search, with parameters α = 0.01, β = 0.5. The performance is very
similar to the previous convergence plots. A linearly convergent initial phase of
about 13 iterations is followed by a quadratically convergent phase, that achieves
a very high accuracy in 4 or 5 more iterations.
Aﬃne invariance of Newton’s method
A very important feature of Newton’s method is that it is independent of linear
(or aﬃne) changes of coordinates. Let x(k) be the kth iterate of Newton’s method,
applied to f : Rn →R. Suppose T ∈Rn×n is nonsingular, and deﬁne ¯f(y) =
f(Ty). If we use Newton’s method (with the same backtracking parameters) to


## Page 29

9.5
Newton’s method
495
k
f(x(k)) −p⋆
0
5
10
15
20
10−5
100
105
Figure 9.23 Error versus iteration of Newton’s method, for a problem
in R10000. A backtracking line search with parameters α = 0.01, β = 0.5 is
used. Even for this large scale problem, Newton’s method requires only 18
iterations to achieve very high accuracy.
minimize ¯f, starting from y(0) = T −1x(0), then we have
Ty(k) = x(k)
for all k. In other words, Newton’s method is the same: The iterates are related
by the same change of coordinates. Even the stopping criterion is the same, since
the Newton decrement for ¯f at y(k) is the same as the Newton decrement for f at
x(k). This is in stark contrast to the gradient (or steepest descent) method, which
is strongly aﬀected by changes of coordinates.
As an example, consider the family of problems given in (9.22), indexed by the
parameter γ, which aﬀects the condition number of the sublevel sets. We observed
(in ﬁgures 9.7 and 9.8) that the gradient method slows to useless for values of γ
smaller than 0.05 or larger than 20. In contrast, Newton’s method (with α = 0.01,
β = 0.5) solves this problem (in fact, to a far higher accuracy) in nine iterations,
for all values of γ between 10−10 and 1010.
In a real implementation, with ﬁnite precision arithmetic, Newton’s method is
not exactly independent of aﬃne changes of coordinates, or the condition number
of the sublevel sets. But we can say that condition numbers ranging up to very
large values such as 1010 do not adversely aﬀect a real implementation of Newton’s
method. For the gradient method, a far smaller range of condition numbers can
be tolerated. While choice of coordinates (or condition number of sublevel sets) is
a ﬁrst-order issue for gradient and steepest descent methods, it is a second-order
issue for Newton’s method; its only eﬀect is in the numerical linear algebra required
to compute the Newton step.


## Page 30

496
9
Unconstrained minimization
Summary
Newton’s method has several very strong advantages over gradient and steepest
descent methods:
• Convergence of Newton’s method is rapid in general, and quadratic near x⋆.
Once the quadratic convergence phase is reached, at most six or so iterations
are required to produce a solution of very high accuracy.
• Newton’s method is aﬃne invariant. It is insensitive to the choice of coordi-
nates, or the condition number of the sublevel sets of the objective.
• Newton’s method scales well with problem size. Its performance on problems
in R10000 is similar to its performance on problems in R10, with only a modest
increase in the number of steps required.
• The good performance of Newton’s method is not dependent on the choice
of algorithm parameters. In contrast, the choice of norm for steepest descent
plays a critical role in its performance.
The main disadvantage of Newton’s method is the cost of forming and storing
the Hessian, and the cost of computing the Newton step, which requires solving
a set of linear equations. We will see in §9.7 that in many cases it is possible to
exploit problem structure to substantially reduce the cost of computing the Newton
step.
Another alternative is provided by a family of algorithms for unconstrained op-
timization called quasi-Newton methods. These methods require less computational
eﬀort to form the search direction, but they share some of the strong advantages
of Newton methods, such as rapid convergence near x⋆. Since quasi-Newton meth-
ods are described in many books, and tangential to our main theme, we will not
consider them in this book.
9.6
Self-concordance
There are two major shortcomings of the classical convergence analysis of Newton’s
method given in §9.5.3.
The ﬁrst is a practical one: The resulting complexity
estimates involve the three constants m, M, and L, which are almost never known
in practice. As a result, the bound (9.40) on the number of Newton steps required
is almost never known speciﬁcally, since it depends on three constants that are, in
general, not known. Of course the convergence analysis and complexity estimate
are still conceptually useful.
The second shortcoming is that while Newton’s method is aﬃnely invariant, the
classical analysis of Newton’s method is very much dependent on the coordinate
system used. If we change coordinates the constants m, M, and L all change. If
for no reason other than aesthetic, we should seek an analysis of Newton’s method
that is, like the method itself, independent of aﬃne changes of coordinates. In


## Page 31

9.6
Self-concordance
497
other words, we seek an alternative to the assumptions
mI ⪯∇2f(x) ⪯MI,
∥∇2f(x) −∇2f(y)∥2 ≤L∥x −y∥2,
that is independent of aﬃne changes of coordinates, and also allows us to analyze
Newton’s method.
A simple and elegant assumption that achieves this goal was discovered by
Nesterov and Nemirovski, who gave the name self-concordance to their condition.
Self-concordant functions are important for several reasons.
• They include many of the logarithmic barrier functions that play an impor-
tant role in interior-point methods for solving convex optimization problems.
• The analysis of Newton’s method for self-concordant functions does not de-
pend on any unknown constants.
• Self-concordance is an aﬃne-invariant property, i.e., if we apply a linear
transformation of variables to a self-concordant function, we obtain a self-
concordant function. Therefore the complexity estimate that we obtain for
Newton’s method applied to a self-concordant function is independent of
aﬃne changes of coordinates.
9.6.1
Deﬁnition and examples
Self-concordant functions on R
We start by considering functions on R. A convex function f : R →R is self-
concordant if
|f ′′′(x)| ≤2f ′′(x)3/2
(9.41)
for all x ∈dom f. Since linear and (convex) quadratic functions have zero third
derivative, they are evidently self-concordant. Some more interesting examples are
given below.
Example 9.3 Logarithm and entropy.
• Negative logarithm.
The function f(x) = −log x is self-concordant.
Using
f ′′(x) = 1/x2, f ′′′(x) = −2/x3, we ﬁnd that
|f ′′′(x)|
2f ′′(x)3/2 =
2/x3
2(1/x2)3/2 = 1,
so the deﬁning inequality (9.41) holds with equality.
• Negative entropy plus negative logarithm. The function f(x) = x log x −log x is
self-concordant. To verify this, we use
f ′′(x) = x + 1
x2
,
f ′′′(x) = −x + 2
x3
to obtain
|f ′′′(x)|
2f ′′(x)3/2 =
x + 2
2(x + 1)3/2 .


## Page 32

498
9
Unconstrained minimization
The function on the righthand side is maximized on R+ by x = 0, where its
value is 1.
The negative entropy function by itself is not self-concordant; see exercise 11.13.
We should make two important remarks about the self-concordance deﬁni-
tion (9.41).
The ﬁrst concerns the mysterious constant 2 that appears in the
deﬁnition. In fact, this constant is chosen for convenience, in order to simplify the
formulas later on; any other positive constant could be used instead. Suppose, for
example, that the convex function f : R →R satisﬁes
|f ′′′(x)| ≤kf ′′(x)3/2
(9.42)
where k is some positive constant. Then the function ˜f(x) = (k2/4)f(x) satisﬁes
| ˜f ′′′(x)|
=
(k2/4)|f ′′′(x)|
≤
(k3/4)f ′′(x)3/2
=
(k3/4)

(4/k2) ˜f ′′(x)
3/2
=
2 ˜f ′′(x)3/2
and therefore is self-concordant. This shows that a function that satisﬁes (9.42)
for some positive k can be scaled to satisfy the standard self-concordance inequal-
ity (9.41).
So what is important is that the third derivative of the function is
bounded by some multiple of the 3/2-power of its second derivative. By appropri-
ately scaling the function, we can change the multiple to the constant 2.
The second comment is a simple calculation that shows why self-concordance
is so important: it is aﬃne invariant. Suppose we deﬁne the function ˜f by ˜f(y) =
f(ay + b), where a̸ = 0. Then ˜f is self-concordant if and only if f is. To see this,
we substitute
˜f ′′(y) = a2f ′′(x),
˜f ′′′(y) = a3f ′′′(x),
where x = ay + b, into the self-concordance inequality for ˜f, i.e., | ˜f ′′′(y)| ≤
2 ˜f ′′(y)3/2, to obtain
|a3f ′′′(x)| ≤2(a2f ′′(x))3/2,
which (after dividing by a3) is the self-concordance inequality for f.
Roughly
speaking, the self-concordance condition (9.41) is a way to limit the third derivative
of a function, in a way that is independent of aﬃne coordinate changes.
Self-concordant functions on Rn
We now consider functions on Rn with n > 1. We say a function f : Rn →R
is self-concordant if it is self-concordant along every line in its domain, i.e., if the
function ˜f(t) = f(x + tv) is a self-concordant function of t for all x ∈dom f and
for all v.


## Page 33

9.6
Self-concordance
499
9.6.2
Self-concordant calculus
Scaling and sum
Self-concordance is preserved by scaling by a factor exceeding one: If f is self-
concordant and a ≥1, then af is self-concordant. Self-concordance is also preserved
by addition: If f1, f2 are self-concordant, then f1 + f2 is self-concordant. To show
this, it is suﬃcient to consider functions f1, f2 : R →R. We have
|f ′′′
1 (x) + f ′′′
2 (x)|
≤
|f ′′′
1 (x)| + |f ′′′
2 (x)|
≤
2(f ′′
1 (x)3/2 + f ′′
2 (x)3/2)
≤
2(f ′′
1 (x) + f ′′
2 (x))3/2.
In the last step we use the inequality
(u3/2 + v3/2)2/3 ≤u + v,
which holds for u, v ≥0.
Composition with aﬃne function
If f : Rn →R is self-concordant, and A ∈Rn×m, b ∈Rn, then f(Ax + b) is
self-concordant.
Example 9.4 Log barrier for linear inequalities. The function
f(x) = −
m
X
i=1
log(bi −aT
i x),
with dom f = {x | aT
i x < bi, i = 1, . . . , m}, is self-concordant. Each term −log(bi −
aT
i x) is the composition of −log y with the aﬃne transformation y = bi −aT
i x, and
hence self-concordant. Therefore the sum is also self-concordant.
Example 9.5 Log-determinant. The function f(X) = −log det X is self-concordant
on dom f = Sn
++. To show this, we consider the function ˜f(t) = f(X + tV ), where
X ≻0 and V ∈Sn. It can be expressed as
˜f(t)
=
−log det(X1/2(I + tX−1/2V X−1/2)X1/2)
=
−log det X −log det(I + tX−1/2V X−1/2)
=
−log det X −
n
X
i=1
log(1 + tλi)
where λi are the eigenvalues of X−1/2V X−1/2. Each term −log(1 + tλi) is a self-
concordant function of t, so the sum, ˜f, is self-concordant.
It follows that f is
self-concordant.
Example 9.6 Log of concave quadratic. The function
f(x) = −log(xT Px + qT x + r),


## Page 34

500
9
Unconstrained minimization
where P ∈−Sn
+, is self-concordant on
dom f = {x | xT Px + qT x + r > 0}.
To show this, it suﬃces to consider the case n = 1 (since by restricting f to a line,
the general case reduces to the n = 1 case). We can then express f as
f(x) = −log(px2 + qx + r) = −log (−p(x −a)(b −x))
where dom f = (a, b) (i.e., a and b are the roots of px2+qx+r). Using this expression
we have
f(x) = −log(−p) −log(x −a) −log(b −x),
which establishes self-concordance.
Composition with logarithm
Let g : R →R be a convex function with dom g = R++, and
|g′′′(x)| ≤3g′′(x)
x
(9.43)
for all x. Then
f(x) = −log(−g(x)) −log x
is self-concordant on {x | x > 0, g(x) < 0}. (For a proof, see exercise 9.14.)
The condition (9.43) is homogeneous and preserved under addition. It is sat-
isﬁed by all (convex) quadratic functions, i.e., functions of the form ax2 + bx + c,
where a ≥0. Therefore if (9.43) holds for a function g, then it holds for the function
g(x) + ax2 + bx + c, where a ≥0.
Example 9.7 The following functions g satisfy the condition (9.43).
• g(x) = −xp for 0 < p ≤1.
• g(x) = −log x.
• g(x) = x log x.
• g(x) = xp for −1 ≤p ≤0.
• g(x) = (ax + b)2/x.
It follows that in each case, the function f(x) = −log(−g(x))−log x is self-concordant.
More generally, the function f(x) = −log(−g(x) −ax2 −bx −c) −log x is self-
concordant on its domain,
{x | x > 0, g(x) + ax2 + bx + c < 0},
provided a ≥0.
Example 9.8 The composition with logarithm rule allows us to show self-concordance
of the following functions.
• f(x, y) = −log(y2 −xT x) on {(x, y) | ∥x∥2 < y}.
• f(x, y) = −2 log y −log(y2/p −x2), with p ≥1, on {(x, y) ∈R2 | |x|p < y}.
• f(x, y) = −log y −log(log y −x) on {(x, y) | ex < y}.
We leave the details as an exercise (exercise 9.15).


## Page 35

9.6
Self-concordance
501
9.6.3
Properties of self-concordant functions
In §9.1.2 we used strong convexity to derive bounds on the suboptimality of a point
x in terms of the norm of the gradient at x. For strictly convex self-concordant
functions, we can obtain similar bounds in terms of the Newton decrement
λ(x) =
 ∇f(x)T ∇2f(x)−1∇f(x)
1/2 .
(It can be shown that the Hessian of a strictly convex self-concordant function is
positive deﬁnite everywhere; see exercise 9.17.) Unlike the bounds based on the
norm of the gradient, the bounds based on the Newton decrement are not aﬀected
by an aﬃne change of coordinates.
For future reference we note that the Newton decrement can also be expressed
as
λ(x) = sup
v̸=0
−vT ∇f(x)
(vT ∇2f(x)v)1/2
(see exercise 9.9). In other words, we have
−vT ∇f(x)
(vT ∇2f(x)v)1/2 ≤λ(x)
(9.44)
for any nonzero v, with equality for v = ∆xnt.
Upper and lower bounds on second derivatives
Suppose f : R →R is a strictly convex self-concordant function. We can write the
self-concordance inequality (9.41) as

d
dt

f ′′(t)−1/2 ≤1
(9.45)
for all t ∈dom f (see exercise 9.16). Assuming t ≥0 and the interval between 0
and t is in dom f, we can integrate (9.45) between 0 and t to obtain
−t ≤
Z t
0
d
dτ

f ′′(τ)−1/2
dτ ≤t,
i.e., −t ≤f ′′(t)−1/2 −f ′′(0)−1/2 ≤t. From this we obtain lower and upper bounds
on f ′′(t):
f ′′(0)
 1 + tf ′′(0)1/22 ≤f ′′(t) ≤
f ′′(0)
 1 −tf ′′(0)1/22 .
(9.46)
The lower bound is valid for all nonnegative t ∈dom f; the upper bound is valid
if t ∈dom f and 0 ≤t < f ′′(0)−1/2.
Bound on suboptimality
Let f : Rn →R be a strictly convex self-concordant function, and let v be a
descent direction (i.e., any direction satisfying vT ∇f(x) < 0, not necessarily the


## Page 36

502
9
Unconstrained minimization
Newton direction). Deﬁne ˜f : R →R as ˜f(t) = f(x + tv). By deﬁnition, the
function ˜f is self-concordant.
Integrating the lower bound in (9.46) yields a lower bound on ˜f ′(t):
˜f ′(t) ≥˜f ′(0) + ˜f ′′(0)1/2 −
˜f ′′(0)1/2
1 + t ˜f ′′(0)1/2 .
(9.47)
Integrating again yields a lower bound on ˜f(t):
˜f(t) ≥˜f(0) + t ˜f ′(0) + t ˜f ′′(0)1/2 −log(1 + t ˜f ′′(0)1/2).
(9.48)
The righthand side reaches its minimum at
¯t =
−˜f ′(0)
˜f ′′(0) + ˜f ′′(0)1/2 ˜f ′(0)
,
and evaluating at ¯t provides a lower bound on ˜f:
inf
t≥0
˜f(t)
≥
˜f(0) + ¯t ˜f ′(0) + ¯t ˜f ′′(0)1/2 −log(1 + ¯t ˜f ′′(0)1/2)
=
˜f(0) −˜f ′(0) ˜f ′′(0)−1/2 + log(1 + ˜f ′(0) ˜f ′′(0)−1/2).
The inequality (9.44) can be expressed as
λ(x) ≥−˜f ′(0) ˜f ′′(0)−1/2
(with equality when v = ∆xnt), since we have
˜f ′(0) = vT ∇f(x),
˜f ′′(0) = vT ∇2f(x)v.
Now using the fact that u + log(1 −u) is a monotonically decreasing function of u,
and the inequality above, we get
inf
t≥0
˜f(t) ≥˜f(0) + λ(x) + log(1 −λ(x)).
This inequality holds for any descent direction v. Therefore
p⋆≥f(x) + λ(x) + log(1 −λ(x))
(9.49)
provided λ(x) < 1. The function −(λ + log(1 −λ)) is plotted in ﬁgure 9.24. It
satisﬁes
−(λ + log(1 −λ)) ≈λ2/2,
for small λ, and the bound
−(λ + log(1 −λ)) ≤λ2
for λ ≤0.68. Thus, we have the bound on suboptimality
p⋆≥f(x) −λ(x)2,
(9.50)
valid for λ(x) ≤0.68.
Recall that λ(x)2/2 is the estimate of f(x) −p⋆, based on the quadratic model
at x; the inequality (9.50) shows that for self-concordant functions, doubling this
estimate gives us a provable bound. In particular, it shows that for self-concordant
functions, we can use the stopping criterion
λ(x)2 ≤ǫ,
(where ǫ < 0.682), and guarantee that on exit f(x) −p⋆≤ǫ.


## Page 37

9.6
Self-concordance
503
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
Figure 9.24 The solid line is the function −(λ+log(1−λ)), which for small λ
is approximately λ2/2. The dashed line shows λ2, which is an upper bound
in the interval 0 ≤λ ≤0.68.
9.6.4
Analysis of Newton’s method for self-concordant functions
We now analyze Newton’s method with backtracking line search, when applied to
a strictly convex self-concordant function f. As before, we assume that a starting
point x(0) is known, and that the sublevel set S = {x | f(x) ≤f(x(0))} is closed.
We also assume that f is bounded below. (This implies that f has a minimizer x⋆;
see exercise 9.19.)
The analysis is very similar to the classical analysis given in §9.5.2, except that
we use self-concordance as the basic assumption instead of strong convexity and
the Lipschitz condition on the Hessian, and the Newton decrement will play the
role of the norm of the gradient. We will show that there are numbers η and γ > 0,
with 0 < η ≤1/4, that depend only on the line search parameters α and β, such
that the following hold:
• If λ(x(k)) > η, then
f(x(k+1)) −f(x(k)) ≤−γ.
(9.51)
• If λ(x(k)) ≤η, then the backtracking line search selects t = 1 and
2λ(x(k+1)) ≤

2λ(x(k))
2
.
(9.52)
These are the analogs of (9.32) and (9.33). As in §9.5.3, the second condition can
be applied recursively, so we can conclude that for all l ≥k, we have λ(x(l)) ≤η,
and
2λ(x(l)) ≤

2λ(x(k))
2l−k
≤(2η)2l−k ≤
1
2
2l−k
.
As a consequence, for all l ≥k,
f(x(l)) −p⋆≤λ(x(l))2 ≤1
4
1
2
2l−k+1
≤
1
2
2l−k+1
,


## Page 38

504
9
Unconstrained minimization
and hence f(x(l)) −p⋆≤ǫ if l −k ≥log2 log2(1/ǫ).
The ﬁrst inequality implies that the damped phase cannot require more than
(f(x(0)) −p⋆)/γ steps. Thus the total number of iterations required to obtain an
accuracy f(x) −p⋆≤ǫ, starting at a point x(0), is bounded by
f(x(0)) −p⋆
γ
+ log2 log2(1/ǫ).
(9.53)
This is the analog of the bound (9.36) in the classical analysis of Newton’s method.
Damped Newton phase
Let ˜f(t) = f(x + t∆xnt), so we have
˜f ′(0) = −λ(x)2,
˜f ′′(0) = λ(x)2.
If we integrate the upper bound in (9.46) twice, we obtain an upper bound for ˜f(t):
˜f(t)
≤
˜f(0) + t ˜f ′(0) −t ˜f ′′(0)1/2 −log

1 −t ˜f ′′(0)1/2
=
˜f(0) −tλ(x)2 −tλ(x) −log(1 −tλ(x)),
(9.54)
valid for 0 ≤t < 1/λ(x).
We can use this bound to show the backtracking line search always results in a
step size t ≥β/(1 + λ(x)). To prove this we note that the point ˆt = 1/(1 + λ(x))
satisﬁes the exit condition of the line search:
˜f(ˆt)
≤
˜f(0) −ˆtλ(x)2 −ˆtλ(x) −log(1 −ˆtλ(x))
=
˜f(0) −λ(x) + log(1 + λ(x))
≤
˜f(0) −α λ(x)2
1 + λ(x)
=
˜f(0) −αλ(x)2ˆt.
The second inequality follows from the fact that
−x + log(1 + x) +
x2
2(1 + x) ≤0
for x ≥0. Since t ≥β/(1 + λ(x)), we have
˜f(t) −˜f(0) ≤−αβ
λ(x)2
1 + λ(x),
so (9.51) holds with
γ = αβ
η2
1 + η .


## Page 39

9.6
Self-concordance
505
Quadratically convergent phase
We will show that we can take
η = (1 −2α)/4,
(which satisﬁes 0 < η < 1/4, since 0 < α < 1/2), i.e., if λ(x(k)) ≤(1 −2α)/4, then
the backtracking line search accepts the unit step and (9.52) holds.
We ﬁrst note that the upper bound (9.54) implies that a unit step t = 1 yields a
point in dom f if λ(x) < 1. Moreover, if λ(x) ≤(1 −2α)/2, we have, using (9.54),
˜f(1)
≤
˜f(0) −λ(x)2 −λ(x) −log(1 −λ(x))
≤
˜f(0) −1
2λ(x)2 + λ(x)3
≤
˜f(0) −αλ(x)2,
so the unit step satisﬁes the condition of suﬃcient decrease.
(The second line
follows from the fact that −x −log(1 −x) ≤1
2x2 + x3 for 0 ≤x ≤0.81.)
The inequality (9.52) follows from the following fact, proved in exercise 9.18. If
λ(x) < 1, and x+ = x −∇2f(x)−1∇f(x), then
λ(x+) ≤
λ(x)2
(1 −λ(x))2 .
(9.55)
In particular, if λ(x) ≤1/4,
λ(x+) ≤2λ(x)2,
which proves that (9.52) holds when λ(x(k)) ≤η.
The ﬁnal complexity bound
Putting it all together, the bound (9.53) on the number of Newton iterations be-
comes
f(x(0)) −p⋆
γ
+log2 log2(1/ǫ) =
20 −8α
αβ(1 −2α)2 (f(x(0))−p⋆)+log2 log2(1/ǫ). (9.56)
This expression depends only on the line search parameters α and β, and the ﬁnal
accuracy ǫ. Moreover the term involving ǫ can be safely replaced by the constant
six, so the bound really depends only on α and β. For typical values of α and β, the
constant that scales f(x(0)) −p⋆is on the order of several hundred. For example,
with α = 0.1, β = 0.8, the scaling factor is 375. With tolerance ǫ = 10−10, we
obtain the bound
375(f(x(0)) −p⋆) + 6.
(9.57)
We will see that this bound is fairly conservative, but does capture what appears
to be the general form of the worst-case number of Newton steps required. A more
reﬁned analysis, such as the one originally given by Nesterov and Nemirovski, gives
a similar bound, with a substantially smaller constant scaling f(x(0)) −p⋆.


## Page 40

506
9
Unconstrained minimization
f(x(0)) −p⋆
iterations
0
5
10
15
20
25
30
35
0
5
10
15
20
25
Figure 9.25 Number of Newton iterations required to minimize self-
concordant functions versus f(x(0)) −p⋆.
The function f has the form
f(x) = −Pm
i=1 log(bi −aT
i x), where the problem data ai and b are ran-
domly generated. The circles show problems with m = 100, n = 50; the
squares show problems with m = 1000, n = 500; and the diamonds show
problems with m = 1000, n = 50. Fifty instances of each are shown.
9.6.5
Discussion and numerical examples
A family of self-concordant functions
It is interesting to compare the upper bound (9.57) with the actual number of
iterations required to minimize a self-concordant function. We consider a family of
problems of the form
f(x) = −
m
X
i=1
log(bi −aT
i x).
The problem data ai and b were generated as follows. For each problem instance,
the coeﬃcients of ai were generated from independent normal distributions with
mean zero and unit variance, and the coeﬃcients b were generated from a uniform
distribution on [0, 1]. Problem instances which were unbounded below were dis-
carded. For each problem we ﬁrst compute x⋆. We then generate a starting point
by choosing a random direction v, and taking x(0) = x⋆+ sv, where s is chosen so
that f(x(0)) −p⋆has a prescribed value between 0 and 35. (We should point out
that starting points with values f(x(0)) −p⋆= 10 or higher are actually very close
to the boundary of the polyhedron.) We then minimize the function using New-
ton’s method with a backtracking line search with parameters α = 0.1, β = 0.8,
and tolerance ǫ = 10−10.
Figure 9.25 shows the number of Newton iterations required versus f(x(0))−p⋆
for 150 problem instances. The circles show 50 problems with m = 100, n = 50;
the squares show 50 problems with m = 1000, n = 500; and the diamonds show 50
problems with m = 1000, n = 50.
