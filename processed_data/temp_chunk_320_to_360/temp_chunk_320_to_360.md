# temp_chunk_320_to_360



## Page 1

6.3
Regularized approximation
307
Smoothing regularization
The idea of regularization, i.e., adding to the objective a term that penalizes large
x, can be extended in several ways. In one useful extension we add a regularization
term of the form ∥Dx∥, in place of ∥x∥.
In many applications, the matrix D
represents an approximate diﬀerentiation or second-order diﬀerentiation operator,
so ∥Dx∥represents a measure of the variation or smoothness of x.
For example, suppose that the vector x ∈Rn represents the value of some
continuous physical parameter, say, temperature, along the interval [0, 1]: xi is
the temperature at the point i/n.
A simple approximation of the gradient or
ﬁrst derivative of the parameter near i/n is given by n(xi+1 −xi), and a simple
approximation of its second derivative is given by the second diﬀerence
n (n(xi+1 −xi) −n(xi −xi−1)) = n2(xi+1 −2xi + xi−1).
If ∆is the (tridiagonal, Toeplitz) matrix
∆= n2


1
−2
1
0
· · ·
0
0
0
0
0
1
−2
1
· · ·
0
0
0
0
0
0
1
−2
· · ·
0
0
0
0
...
...
...
...
...
...
...
...
0
0
0
0
· · ·
−2
1
0
0
0
0
0
0
· · ·
1
−2
1
0
0
0
0
0
· · ·
0
1
−2
1


∈R(n−2)×n,
then ∆x represents an approximation of the second derivative of the parameter, so
∥∆x∥2
2 represents a measure of the mean-square curvature of the parameter over
the interval [0, 1].
The Tikhonov regularized problem
minimize
∥Ax −b∥2
2 + δ∥∆x∥2
2
can be used to trade oﬀthe objective ∥Ax −b∥2, which might represent a measure
of ﬁt, or consistency with experimental data, and the objective ∥∆x∥2, which is
(approximately) the mean-square curvature of the underlying physical parameter.
The parameter δ is used to control the amount of regularization required, or to
plot the optimal trade-oﬀcurve of ﬁt versus smoothness.
We can also add several regularization terms. For example, we can add terms
associated with smoothness and size, as in
minimize
∥Ax −b∥2
2 + δ∥∆x∥2
2 + η∥x∥2
2.
Here, the parameter δ ≥0 is used to control the smoothness of the approximate
solution, and the parameter η ≥0 is used to control its size.
Example 6.3
Optimal input design. We consider a dynamical system with scalar
input sequence u(0), u(1), . . . , u(N), and scalar output sequence y(0), y(1), . . . , y(N),
related by convolution:
y(t) =
t
X
τ=0
h(τ)u(t −τ),
t = 0, 1, . . . , N.


## Page 2

308
6
Approximation and ﬁtting
The sequence h(0), h(1), . . . , h(N) is called the convolution kernel or impulse response
of the system.
Our goal is to choose the input sequence u to achieve several goals.
• Output tracking. The primary goal is that the output y should track, or follow,
a desired target or reference signal ydes. We measure output tracking error by
the quadratic function
Jtrack =
1
N + 1
N
X
t=0
(y(t) −ydes(t))2.
• Small input. The input should not be large. We measure the magnitude of the
input by the quadratic function
Jmag =
1
N + 1
N
X
t=0
u(t)2.
• Small input variations. The input should not vary rapidly. We measure the
magnitude of the input variations by the quadratic function
Jder = 1
N
N−1
X
t=0
(u(t + 1) −u(t))2.
By minimizing a weighted sum
Jtrack + δJder + ηJmag,
where δ > 0 and η > 0, we can trade oﬀthe three objectives.
Now we consider a speciﬁc example, with N = 200, and impulse response
h(t) = 1
9(0.9)t(1 −0.4 cos(2t)).
Figure 6.6 shows the optimal input, and corresponding output (along with the desired
trajectory ydes), for three values of the regularization parameters δ and η. The top
row shows the optimal input and corresponding output for δ = 0, η = 0.005. In this
case we have some regularization for the magnitude of the input, but no regularization
for its variation. While the tracking is good (i.e., we have Jtrack is small), the input
required is large, and rapidly varying. The second row corresponds to δ = 0, η = 0.05.
In this case we have more magnitude regularization, but still no regularization for
variation in u. The corresponding input is indeed smaller, at the cost of a larger
tracking error. The bottom row shows the results for δ = 0.3, η = 0.05. In this
case we have added some regularization for the variation.
The input variation is
substantially reduced, with not much increase in output tracking error.
ℓ1-norm regularization
Regularization with an ℓ1-norm can be used as a heuristic for ﬁnding a sparse
solution. For example, consider the problem
minimize
∥Ax −b∥2 + γ∥x∥1,
(6.11)


## Page 3

6.3
Regularized approximation
309
t
u(t)
0
50
100
150
200
−10
−5
0
5
t
y(t)
0
50
100
150
200
−1
−0.5
0
0.5
1
t
u(t)
0
50
100
150
200
−4
−2
0
2
4
t
y(t)
0
50
100
150
200
−1
−0.5
0
0.5
1
t
u(t)
0
50
100
150
200
−4
−2
0
2
4
t
y(t)
0
50
100
150
200
−1
−0.5
0
0.5
1
Figure 6.6 Optimal inputs (left) and resulting outputs (right) for three values
of the regularization parameters δ (which corresponds to input variation) and
η (which corresponds to input magnitude). The dashed line in the righthand
plots shows the desired output ydes. Top row: δ = 0, η = 0.005; middle row:
δ = 0, η = 0.05; bottom row: δ = 0.3, η = 0.05.


## Page 4

310
6
Approximation and ﬁtting
in which the residual is measured with the Euclidean norm and the regularization is
done with an ℓ1-norm. By varying the parameter γ we can sweep out the optimal
trade-oﬀcurve between ∥Ax −b∥2 and ∥x∥1, which serves as an approximation
of the optimal trade-oﬀcurve between ∥Ax −b∥2 and the sparsity or cardinality
card(x) of the vector x, i.e., the number of nonzero elements. The problem (6.11)
can be recast and solved as an SOCP.
Example 6.4
Regressor selection problem.
We are given a matrix A ∈Rm×n,
whose columns are potential regressors, and a vector b ∈Rm that is to be ﬁt by a
linear combination of k < n columns of A. The problem is to choose the subset of k
regressors to be used, and the associated coeﬃcients. We can express this problem
as
minimize
∥Ax −b∥2
subject to
card(x) ≤k.
In general, this is a hard combinatorial problem.
One straightforward approach is to check every possible sparsity pattern in x with k
nonzero entries. For a ﬁxed sparsity pattern, we can ﬁnd the optimal x by solving
a least-squares problem, i.e., minimizing ∥˜A˜x −b∥2, where ˜A denotes the submatrix
of A obtained by keeping the columns corresponding to the sparsity pattern, and
˜x is the subvector with the nonzero components of x. This is done for each of the
n!/(k!(n −k)!) sparsity patterns with k nonzeros.
A good heuristic approach is to solve the problem (6.11) for diﬀerent values of γ,
ﬁnding the smallest value of γ that results in a solution with card(x) = k. We then
ﬁx this sparsity pattern and ﬁnd the value of x that minimizes ∥Ax −b∥2.
Figure 6.7 illustrates a numerical example with A ∈R10×20, x ∈R20, b ∈R10. The
circles on the dashed curve are the (globally) Pareto optimal values for the trade-oﬀ
between card(x) (vertical axis) and the residual ∥Ax −b∥2 (horizontal axis). For
each k, the Pareto optimal point was obtained by enumerating all possible sparsity
patterns with k nonzero entries, as described above. The circles on the solid curve
were obtained with the heuristic approach, by using the sparsity patterns of the
solutions of problem (6.11) for diﬀerent values of γ. Note that for card(x) = 1, the
heuristic method actually ﬁnds the global optimum.
This idea will come up again in basis pursuit (§6.5.4).
6.3.3
Reconstruction, smoothing, and de-noising
In this section we describe an important special case of the bi-criterion approxi-
mation problem described above, and give some examples showing how diﬀerent
regularization methods perform. In reconstruction problems, we start with a signal
represented by a vector x ∈Rn. The coeﬃcients xi correspond to the value of
some function of time, evaluated (or sampled, in the language of signal processing)
at evenly spaced points. It is usually assumed that the signal does not vary too
rapidly, which means that usually, we have xi ≈xi+1. (In this section we consider
signals in one dimension, e.g., audio signals, but the same ideas can be applied to
signals in two or more dimensions, e.g., images or video.)


## Page 5

6.3
Regularized approximation
311
∥Ax −b∥2
card(x)
0
1
2
3
4
0
2
4
6
8
10
Figure 6.7 Sparse regressor selection with a matrix A ∈R10×20. The circles
on the dashed line are the Pareto optimal values for the trade-oﬀbetween
the residual ∥Ax −b∥2 and the number of nonzero elements card(x). The
points indicated by circles on the solid line are obtained via the ℓ1-norm
regularized heuristic.
The signal x is corrupted by an additive noise v:
xcor = x + v.
The noise can be modeled in many diﬀerent ways, but here we simply assume that
it is unknown, small, and, unlike the signal, rapidly varying. The goal is to form an
estimate ˆx of the original signal x, given the corrupted signal xcor. This process is
called signal reconstruction (since we are trying to reconstruct the original signal
from the corrupted version) or de-noising (since we are trying to remove the noise
from the corrupted signal). Most reconstruction methods end up performing some
sort of smoothing operation on xcor to produce ˆx, so the process is also called
smoothing.
One simple formulation of the reconstruction problem is the bi-criterion problem
minimize (w.r.t. R2
+)
(∥ˆx −xcor∥2, φ(ˆx)) ,
(6.12)
where ˆx is the variable and xcor is a problem parameter. The function φ : Rn →R
is convex, and is called the regularization function or smoothing objective. It is
meant to measure the roughness, or lack of smoothness, of the estimate ˆx. The
reconstruction problem (6.12) seeks signals that are close (in ℓ2-norm) to the cor-
rupted signal, and that are smooth, i.e., for which φ(ˆx) is small. The reconstruction
problem (6.12) is a convex bi-criterion problem. We can ﬁnd the Pareto optimal
points by scalarization, and solving a (scalar) convex optimization problem.


## Page 6

312
6
Approximation and ﬁtting
Quadratic smoothing
The simplest reconstruction method uses the quadratic smoothing function
φquad(x) =
n−1
X
i=1
(xi+1 −xi)2 = ∥Dx∥2
2,
where D ∈R(n−1)×n is the bidiagonal matrix
D =


−1
1
0
· · ·
0
0
0
0
−1
1
· · ·
0
0
0
...
...
...
...
...
...
0
0
0
· · ·
−1
1
0
0
0
0
· · ·
0
−1
1


.
We can obtain the optimal trade-oﬀbetween ∥ˆx−xcor∥2 and ∥Dˆx∥2 by minimizing
∥ˆx −xcor∥2
2 + δ∥Dˆx∥2
2,
where δ > 0 parametrizes the optimal trade-oﬀcurve. The solution of this quadratic
problem,
ˆx = (I + δDT D)−1xcor,
can be computed very eﬃciently since I + δDT D is tridiagonal; see appendix C.
Quadratic smoothing example
Figure 6.8 shows a signal x ∈R4000 (top) and the corrupted signal xcor (bottom).
The optimal trade-oﬀcurve between the objectives ∥ˆx−xcor∥2 and ∥Dˆx∥2 is shown
in ﬁgure 6.9. The extreme point on the left of the trade-oﬀcurve corresponds to
ˆx = xcor, and has objective value ∥Dxcor∥2 = 4.4. The extreme point on the right
corresponds to ˆx = 0, for which ∥ˆx −xcor∥2 = ∥xcor∥2 = 16.2. Note the clear knee
in the trade-oﬀcurve near ∥ˆx −xcor∥2 ≈3.
Figure 6.10 shows three smoothed signals on the optimal trade-oﬀcurve, cor-
responding to ∥ˆx −xcor∥2 = 8 (top), 3 (middle), and 1 (bottom). Comparing the
reconstructed signals with the original signal x, we see that the best reconstruction
is obtained for ∥ˆx −xcor∥2 = 3, which corresponds to the knee of the trade-oﬀ
curve. For higher values of ∥ˆx −xcor∥2, there is too much smoothing; for smaller
values there is too little smoothing.
Total variation reconstruction
Simple quadratic smoothing works well as a reconstruction method when the orig-
inal signal is very smooth, and the noise is rapidly varying. But any rapid varia-
tions in the original signal will, obviously, be attenuated or removed by quadratic
smoothing. In this section we describe a reconstruction method that can remove
much of the noise, while still preserving occasional rapid variations in the original
signal. The method is based on the smoothing function
φtv(ˆx) =
n−1
X
i=1
|ˆxi+1 −ˆxi| = ∥Dˆx∥1,


## Page 7

6.3
Regularized approximation
313
i
x
xcor
0
0
1000
1000
2000
2000
3000
3000
4000
4000
−0.5
−0.5
0
0
0.5
0.5
Figure 6.8 Top: the original signal x ∈R4000. Bottom: the corrupted signal
xcor.
∥ˆx −xcor∥2
∥Dˆx∥2
0
5
10
15
20
0
1
2
3
4
Figure 6.9 Optimal trade-oﬀcurve between ∥Dˆx∥2 and ∥ˆx −xcor∥2. The
curve has a clear knee near ∥ˆx −xcor∥≈3.


## Page 8

314
6
Approximation and ﬁtting
i
ˆx
ˆx
ˆx
0
0
0
1000
1000
1000
2000
2000
2000
3000
3000
3000
4000
4000
4000
−0.5
−0.5
−0.5
0
0
0
0.5
0.5
0.5
Figure 6.10 Three smoothed or reconstructed signals ˆx. The top one cor-
responds to ∥ˆx −xcor∥2 = 8, the middle one to ∥ˆx −xcor∥2 = 3, and the
bottom one to ∥ˆx −xcor∥2 = 1.
which is called the total variation of x ∈Rn.
Like the quadratic smoothness
measure φquad, the total variation function assigns large values to rapidly varying
ˆx. The total variation measure, however, assigns relatively less penalty to large
values of |xi+1 −xi|.
Total variation reconstruction example
Figure 6.11 shows a signal x ∈R2000 (in the top plot), and the signal corrupted
with noise xcor. The signal is mostly smooth, but has several rapid variations or
jumps in value; the noise is rapidly varying.
We ﬁrst use quadratic smoothing. Figure 6.12 shows three smoothed signals on
the optimal trade-oﬀcurve between ∥Dˆx∥2 and ∥ˆx−xcor∥2. In the ﬁrst two signals,
the rapid variations in the original signal are also smoothed. In the third signal
the steep edges in the signal are better preserved, but there is still a signiﬁcant
amount of noise left.
Now we demonstrate total variation reconstruction.
Figure 6.13 shows the
optimal trade-oﬀcurve between ∥Dˆx∥1 and ∥ˆx −xcor∥2. Figure 6.14 shows the re-
constructed signals on the optimal trade-oﬀcurve, for ∥Dˆx∥1 = 5 (top), ∥Dˆx∥1 = 8
(middle), and ∥Dˆx∥1 = 10 (bottom). We observe that, unlike quadratic smoothing,
total variation reconstruction preserves the sharp transitions in the signal.


## Page 9

6.3
Regularized approximation
315
i
x
xcor
0
0
500
500
1000
1000
1500
1500
2000
2000
−2
−2
−1
−1
0
0
1
1
2
2
Figure 6.11 A signal x ∈R2000, and the corrupted signal xcor ∈R2000. The
noise is rapidly varying, and the signal is mostly smooth, with a few rapid
variations.


## Page 10

316
6
Approximation and ﬁtting
i
ˆx
ˆx
ˆx
0
0
0
500
500
500
1000
1000
1000
1500
1500
1500
2000
2000
2000
−2
−2
−2
0
0
0
2
2
2
Figure 6.12 Three quadratically smoothed signals ˆx.
The top one corre-
sponds to ∥ˆx −xcor∥2 = 10, the middle one to ∥ˆx −xcor∥2 = 7, and the
bottom one to ∥ˆx −xcor∥2 = 4. The top one greatly reduces the noise, but
also excessively smooths out the rapid variations in the signal. The bottom
smoothed signal does not give enough noise reduction, and still smooths out
the rapid variations in the original signal. The middle smoothed signal gives
the best compromise, but still smooths out the rapid variations.
∥ˆx −xcor∥2
∥Dˆx∥1
0
10
20
30
40
50
0
50
100
150
200
250
Figure 6.13 Optimal trade-oﬀcurve between ∥Dˆx∥1 and ∥ˆx −xcor∥2.


## Page 11

6.3
Regularized approximation
317
i
ˆx
ˆx
ˆx
0
0
0
500
500
500
1000
1000
1000
1500
1500
1500
2000
2000
2000
−2
−2
−2
0
0
0
2
2
2
Figure 6.14 Three reconstructed signals ˆx, using total variation reconstruc-
tion. The top one corresponds to ∥Dˆx∥1 = 5, the middle one to ∥Dˆx∥1 = 8,
and the bottom one to ∥Dˆx∥1 = 10. The bottom one does not give quite
enough noise reduction, while the top one eliminates some of the slowly vary-
ing parts of the signal. Note that in total variation reconstruction, unlike
quadratic smoothing, the sharp changes in the signal are preserved.


## Page 12

318
6
Approximation and ﬁtting
6.4
Robust approximation
6.4.1
Stochastic robust approximation
We consider an approximation problem with basic objective ∥Ax−b∥, but also wish
to take into account some uncertainty or possible variation in the data matrix A.
(The same ideas can be extended to handle the case where there is uncertainty in
both A and b.) In this section we consider some statistical models for the variation
in A.
We assume that A is a random variable taking values in Rm×n, with mean ¯A,
so we can describe A as
A = ¯A + U,
where U is a random matrix with zero mean. Here, the constant matrix ¯A gives
the average value of A, and U describes its statistical variation.
It is natural to use the expected value of ∥Ax −b∥as the objective:
minimize
E ∥Ax −b∥.
(6.13)
We refer to this problem as the stochastic robust approximation problem.
It is
always a convex optimization problem, but usually not tractable since in most
cases it is very diﬃcult to evaluate the objective or its derivatives.
One simple case in which the stochastic robust approximation problem (6.13)
can be solved occurs when A assumes only a ﬁnite number of values, i.e.,
prob(A = Ai) = pi,
i = 1, . . . , k,
where Ai ∈Rm×n, 1T p = 1, p ⪰0. In this case the problem (6.13) has the form
minimize
p1∥A1x −b∥+ · · · + pk∥Akx −b∥,
which is often called a sum-of-norms problem. It can be expressed as
minimize
pT t
subject to
∥Aix −b∥≤ti,
i = 1, . . . , k,
where the variables are x ∈Rn and t ∈Rk. If the norm is the Euclidean norm,
this sum-of-norms problem is an SOCP. If the norm is the ℓ1- or ℓ∞-norm, the
sum-of-norms problem can be expressed as an LP; see exercise 6.8.
Some variations on the stochastic robust approximation problem (6.13) are
tractable. As an example, consider the stochastic robust least-squares problem
minimize
E ∥Ax −b∥2
2,
where the norm is the Euclidean norm. We can express the objective as
E ∥Ax −b∥2
2
=
E( ¯Ax −b + Ux)T ( ¯Ax −b + Ux)
=
( ¯Ax −b)T ( ¯Ax −b) + E xT U T Ux
=
∥¯Ax −b∥2
2 + xT Px,


## Page 13

6.4
Robust approximation
319
where P = E U T U. Therefore the stochastic robust approximation problem has
the form of a regularized least-squares problem
minimize
∥¯Ax −b∥2
2 + ∥P 1/2x∥2
2,
with solution
x = ( ¯AT ¯A + P)−1 ¯AT b.
This makes perfect sense: when the matrix A is subject to variation, the vector
Ax will have more variation the larger x is, and Jensen’s inequality tells us that
variation in Ax will increase the average value of ∥Ax−b∥2. So we need to balance
making ¯Ax −b small with the desire for a small x (to keep the variation in Ax
small), which is the essential idea of regularization.
This observation gives us another interpretation of the Tikhonov regularized
least-squares problem (6.10), as a robust least-squares problem, taking into account
possible variation in the matrix A. The solution of the Tikhonov regularized least-
squares problem (6.10) minimizes E ∥(A + U)x −b∥2, where Uij are zero mean,
uncorrelated random variables, with variance δ/m (and here, A is deterministic).
6.4.2
Worst-case robust approximation
It is also possible to model the variation in the matrix A using a set-based, worst-
case approach. We describe the uncertainty by a set of possible values for A:
A ∈A ⊆Rm×n,
which we assume is nonempty and bounded. We deﬁne the associated worst-case
error of a candidate approximate solution x ∈Rn as
ewc(x) = sup{∥Ax −b∥| A ∈A},
which is always a convex function of x. The (worst-case) robust approximation
problem is to minimize the worst-case error:
minimize
ewc(x) = sup{∥Ax −b∥| A ∈A},
(6.14)
where the variable is x, and the problem data are b and the set A. When A is the
singleton A = {A}, the robust approximation problem (6.14) reduces to the basic
norm approximation problem (6.1). The robust approximation problem is always
a convex optimization problem, but its tractability depends on the norm used and
the description of the uncertainty set A.
Example 6.5
Comparison of stochastic and worst-case robust approximation.
To
illustrate the diﬀerence between the stochastic and worst-case formulations of the
robust approximation problem, we consider the least-squares problem
minimize
∥A(u)x −b∥2
2,
where u ∈R is an uncertain parameter and A(u) = A0 + uA1.
We consider a
speciﬁc instance of the problem, with A(u) ∈R20×10, ∥A0∥= 10, ∥A1∥= 1, and u


## Page 14

320
6
Approximation and ﬁtting
u
r(u)
xnom
xstoch
xwc
−2
−1
0
1
2
0
2
4
6
8
10
12
Figure 6.15 The residual r(u) = ∥A(u)x −b∥2 as a function of the un-
certain parameter u for three approximate solutions x: (1) the nominal
least-squares solution xnom; (2) the solution of the stochastic robust approx-
imation problem xstoch (assuming u is uniformly distributed on [−1, 1]); and
(3) the solution of the worst-case robust approximation problem xwc, as-
suming the parameter u lies in the interval [−1, 1]. The nominal solution
achieves the smallest residual when u = 0, but gives much larger residuals
as u approaches −1 or 1. The worst-case solution has a larger residual when
u = 0, but its residuals do not rise much as the parameter u varies over the
interval [−1, 1].
in the interval [−1, 1]. (So, roughly speaking, the variation in the matrix A is around
±10%.)
We ﬁnd three approximate solutions:
• Nominal optimal. The optimal solution xnom is found, assuming A(u) has its
nominal value A0.
• Stochastic robust approximation. We ﬁnd xstoch, which minimizes E ∥A(u)x −
b∥2
2, assuming the parameter u is uniformly distributed on [−1, 1].
• Worst-case robust approximation. We ﬁnd xwc, which minimizes
sup
−1≤u≤1
∥A(u)x −b∥2 = max{∥(A0 −A1)x −b∥2, ∥(A0 + A1)x −b∥2}.
For each of these three values of x, we plot the residual r(u) = ∥A(u)x −b∥2 as a
function of the uncertain parameter u, in ﬁgure 6.15. These plots show how sensitive
an approximate solution can be to variation in the parameter u. The nominal solu-
tion achieves the smallest residual when u = 0, but is quite sensitive to parameter
variation: it gives much larger residuals as u deviates from 0, and approaches −1 or
1. The worst-case solution has a larger residual when u = 0, but its residuals do not
rise much as u varies over the interval [−1, 1]. The stochastic robust approximate
solution is in between.


## Page 15

6.4
Robust approximation
321
The robust approximation problem (6.14) arises in many contexts and applica-
tions. In an estimation setting, the set A gives our uncertainty in the linear relation
between the vector to be estimated and our measurement vector. Sometimes the
noise term v in the model y = Ax + v is called additive noise or additive error,
since it is added to the ‘ideal’ measurement Ax. In contrast, the variation in A is
called multiplicative error, since it multiplies the variable x.
In an optimal design setting, the variation can represent uncertainty (arising in
manufacture, say) of the linear equations that relate the design variables x to the
results vector Ax. The robust approximation problem (6.14) is then interpreted as
the robust design problem: ﬁnd design variables x that minimize the worst possible
mismatch between Ax and b, over all possible values of A.
Finite set
Here we have A = {A1, . . . , Ak}, and the robust approximation problem is
minimize
maxi=1,...,k ∥Aix −b∥.
This problem is equivalent to the robust approximation problem with the polyhe-
dral set A = conv{A1, . . . , Ak}:
minimize
sup {∥Ax −b∥| A ∈conv{A1, . . . , Ak}} .
We can cast the problem in epigraph form as
minimize
t
subject to
∥Aix −b∥≤t,
i = 1, . . . , k,
which can be solved in a variety of ways, depending on the norm used. If the norm
is the Euclidean norm, this is an SOCP. If the norm is the ℓ1- or ℓ∞-norm, we can
express it as an LP.
Norm bound error
Here the uncertainty set A is a norm ball, A = { ¯A + U | ∥U∥≤a}, where ∥· ∥is a
norm on Rm×n. In this case we have
ewc(x) = sup{∥¯Ax −b + Ux∥| ∥U∥≤a},
which must be carefully interpreted since the ﬁrst norm appearing is on Rm (and
is used to measure the size of the residual) and the second one appearing is on
Rm×n (used to deﬁne the norm ball A).
This expression for ewc(x) can be simpliﬁed in several cases. As an example,
let us take the Euclidean norm on Rn and the associated induced norm on Rm×n,
i.e., the maximum singular value. If ¯Ax −b̸ = 0 and x̸ = 0, the supremum in the
expression for ewc(x) is attained for U = auvT , with
u =
¯Ax −b
∥¯Ax −b∥2
,
v =
x
∥x∥2
,
and the resulting worst-case error is
ewc(x) = ∥¯Ax −b∥2 + a∥x∥2.


## Page 16

322
6
Approximation and ﬁtting
(It is easily veriﬁed that this expression is also valid if x or ¯Ax −b is zero.) The
robust approximation problem (6.14) then becomes
minimize
∥¯Ax −b∥2 + a∥x∥2,
which is a regularized norm problem, solvable as the SOCP
minimize
t1 + at2
subject to
∥¯Ax −b∥2 ≤t1,
∥x∥2 ≤t2.
Since the solution of this problem is the same as the solution of the regularized
least-squares problem
minimize
∥¯Ax −b∥2
2 + δ∥x∥2
2
for some value of the regularization parameter δ, we have another interpretation of
the regularized least-squares problem as a worst-case robust approximation prob-
lem.
Uncertainty ellipsoids
We can also describe the variation in A by giving an ellipsoid of possible values for
each row:
A = {[a1 · · · am]T | ai ∈Ei, i = 1, . . . , m},
where
Ei = {¯ai + Piu | ∥u∥2 ≤1}.
The matrix Pi ∈Rn×n describes the variation in ai. We allow Pi to have a nontriv-
ial nullspace, in order to model the situation when the variation in ai is restricted
to a subspace. As an extreme case, we take Pi = 0 if there is no uncertainty in ai.
With this ellipsoidal uncertainty description, we can give an explicit expression
for the worst-case magnitude of each residual:
sup
ai∈Ei
|aT
i x −bi|
=
sup{|¯aT
i x −bi + (Piu)T x| | ∥u∥2 ≤1}
=
|¯aT
i x −bi| + ∥P T
i x∥2.
Using this result we can solve several robust approximation problems.
For
example, the robust ℓ2-norm approximation problem
minimize
ewc(x) = sup{∥Ax −b∥2 | ai ∈Ei, i = 1, . . . , m}
can be reduced to an SOCP, as follows. An explicit expression for the worst-case
error is given by
ewc(x) =
 m
X
i=1

sup
ai∈Ei
|aT
i x −bi|
2!1/2
=
 m
X
i=1
(|¯aT
i x −bi| + ∥P T
i x∥2)2
!1/2
.
To minimize ewc(x) we can solve
minimize
∥t∥2
subject to
|¯aT
i x −bi| + ∥P T
i x∥2 ≤ti,
i = 1, . . . , m,


## Page 17

6.4
Robust approximation
323
where we introduced new variables t1, . . . , tm. This problem can be formulated as
minimize
∥t∥2
subject to
¯aT
i x −bi + ∥P T
i x∥2 ≤ti,
i = 1, . . . , m
−¯aT
i x + bi + ∥P T
i x∥2 ≤ti,
i = 1, . . . , m,
which becomes an SOCP when put in epigraph form.
Norm bounded error with linear structure
As a generalization of the norm bound description A = { ¯A + U | ∥U∥≤a}, we can
deﬁne A as the image of a norm ball under an aﬃne transformation:
A = { ¯A + u1A1 + u2A2 + · · · + upAp | ∥u∥≤1},
where ∥· ∥is a norm on Rp, and the p + 1 matrices ¯A, A1, . . . , Ap ∈Rm×n are
given. The worst-case error can be expressed as
ewc(x)
=
sup
∥u∥≤1
∥( ¯A + u1A1 + · · · + upAp)x −b∥
=
sup
∥u∥≤1
∥P(x)u + q(x)∥,
where P and q are deﬁned as
P(x) =
 A1x
A2x
· · ·
Apx 
∈Rm×p,
q(x) = ¯Ax −b ∈Rm.
As a ﬁrst example, we consider the robust Chebyshev approximation problem
minimize
ewc(x) = sup∥u∥∞≤1 ∥( ¯A + u1A1 + · · · + upAp)x −b∥∞.
In this case we can derive an explicit expression for the worst-case error. Let pi(x)T
denote the ith row of P(x). We have
ewc(x)
=
sup
∥u∥∞≤1
∥P(x)u + q(x)∥∞
=
max
i=1,...,m
sup
∥u∥∞≤1
|pi(x)T u + qi(x)|
=
max
i=1,...,m(∥pi(x)∥1 + |qi(x)|).
The robust Chebyshev approximation problem can therefore be cast as an LP
minimize
t
subject to
−y0 ⪯¯Ax −b ⪯y0
−yk ⪯Akx ⪯yk,
k = 1, . . . , p
y0 + Pp
k=1 yk ⪯t1,
with variables x ∈Rn, yk ∈Rm, t ∈R.
As another example, we consider the robust least-squares problem
minimize
ewc(x) = sup∥u∥2≤1 ∥( ¯A + u1A1 + · · · + upAp)x −b∥2.


## Page 18

324
6
Approximation and ﬁtting
Here we use Lagrange duality to evaluate ewc. The worst-case error ewc(x) is the
squareroot of the optimal value of the (nonconvex) quadratic optimization problem
maximize
∥P(x)u + q(x)∥2
2
subject to
uT u ≤1,
with u as variable. The Lagrange dual of this problem can be expressed as the
SDP
minimize
t + λ
subject to


I
P(x)
q(x)
P(x)T
λI
0
q(x)T
0
t

⪰0
(6.15)
with variables t, λ ∈R. Moreover, as mentioned in §5.2 and §B.1 (and proved
in §B.4), strong duality holds for this pair of primal and dual problems. In other
words, for ﬁxed x, we can compute ewc(x)2 by solving the SDP (6.15) with variables
t and λ. Optimizing jointly over t, λ, and x is equivalent to minimizing ewc(x)2.
We conclude that the robust least-squares problem is equivalent to the SDP (6.15)
with x, λ, t as variables.
Example 6.6
Comparison of worst-case robust, Tikhonov regularized, and nominal
least-squares solutions. We consider an instance of the robust approximation problem
minimize
sup∥u∥2≤1 ∥( ¯A + u1A1 + u2A2)x −b∥2,
(6.16)
with dimensions m = 50, n = 20. The matrix ¯A has norm 10, and the two matrices
A1 and A2 have norm 1, so the variation in the matrix A is, roughly speaking, around
10%. The uncertainty parameters u1 and u2 lie in the unit disk in R2.
We compute the optimal solution of the robust least-squares problem (6.16) xrls, as
well as the solution of the nominal least-squares problem xls (i.e., assuming u = 0),
and also the Tikhonov regularized solution xtik, with δ = 1.
To illustrate the sensitivity of each of these approximate solutions to the parameter
u, we generate 105 parameter vectors, uniformly distributed on the unit disk, and
evaluate the residual
∥(A0 + u1A1 + u2A2)x −b∥2
for each parameter value. The distributions of the residuals are shown in ﬁgure 6.16.
We can make several observations. First, the residuals of the nominal least-squares
solution are widely spread, from a smallest value around 0.52 to a largest value
around 4.9. In particular, the least-squares solution is very sensitive to parameter
variation. In contrast, both the robust least-squares and Tikhonov regularized so-
lutions exhibit far smaller variation in residual as the uncertainty parameter varies
over the unit disk. The robust least-squares solution, for example, achieves a residual
between 2.0 and 2.6 for all parameters in the unit disk.
6.5
Function ﬁtting and interpolation
In function ﬁtting problems, we select a member of a ﬁnite-dimensional subspace
of functions that best ﬁts some given data or requirements.
For simplicity we


## Page 19

6.5
Function ﬁtting and interpolation
325
∥(A0 + u1A1 + u2A2)x −b∥2
xls
xtik
xrls
frequency
0
1
2
3
4
5
0
0.05
0.1
0.15
0.2
0.25
Figure 6.16 Distribution of the residuals for the three solutions of a least-
squares problem (6.16): xls, the least-squares solution assuming u = 0; xtik,
the Tikhonov regularized solution with δ = 1; and xrls, the robust least-
squares solution. The histograms were obtained by generating 105 values of
the uncertain parameter vector u from a uniform distribution on the unit
disk in R2. The bins have width 0.1.


## Page 20

326
6
Approximation and ﬁtting
consider real-valued functions; the ideas are readily extended to handle vector-
valued functions as well.
6.5.1
Function families
We consider a family of functions f1, . . . , fn : Rk →R, with common domain
dom fi = D. With each x ∈Rn we associate the function f : Rk →R given by
f(u) = x1f1(u) + · · · + xnfn(u)
(6.17)
with dom f = D.
The family {f1, . . . , fn} is sometimes called the set of basis
functions (for the ﬁtting problem) even when the functions are not independent.
The vector x ∈Rn, which parametrizes the subspace of functions, is our optimiza-
tion variable, and is sometimes called the coeﬃcient vector. The basis functions
generate a subspace F of functions on D.
In many applications the basis functions are specially chosen, using prior knowl-
edge or experience, in order to reasonably model functions of interest with the
ﬁnite-dimensional subspace of functions.
In other cases, more generic function
families are used. We describe a few of these below.
Polynomials
One common subspace of functions on R consists of polynomials of degree less
than n. The simplest basis consists of the powers, i.e., fi(t) = ti−1, i = 1, . . . , n.
In many applications, the same subspace is described using a diﬀerent basis, for
example, a set of polynomials f1, . . . , fn, of degree less than n, that are orthonormal
with respect to some positive function (or measure) φ : Rn →R+, i.e.,
Z
fi(t)fj(t)φ(t) dt =

1
i = j
0
i̸ = j.
Another common basis for polynomials is the Lagrange basis f1, . . . , fn associated
with distinct points t1, . . . , tn, which satisfy
fi(tj) =

1
i = j
0
i̸ = j.
We can also consider polynomials on Rk, with a maximum total degree, or a
maximum degree for each variable.
As a related example, we have trigonometric polynomials of degree less than n,
with basis
sin kt,
k = 1, . . . , n −1,
cos kt,
k = 0, . . . , n −1.
Piecewise-linear functions
We start with a triangularization of the domain D, which means the following. We
have a set of mesh or grid points g1, . . . , gn ∈Rk, and a partition of D into a set
of simplexes:
D = S1 ∪· · · ∪Sm,
int(Si ∩Sj) = ∅for i̸ = j.


## Page 21

6.5
Function ﬁtting and interpolation
327
u1
0
1
0
1
0
1
u2
f(u1, u2)
Figure 6.17 A piecewise-linear function of two variables, on the unit square.
The triangulation consists of 98 simplexes, and a uniform grid of 64 points
in the unit square.
Each simplex is the convex hull of k + 1 grid points, and we require that each grid
point is a vertex of any simplex it lies in.
Given a triangularization, we can construct a piecewise-linear (or more precisely,
piecewise-aﬃne) function f by assigning function values f(gi) = xi to the grid
points, and then extending the function aﬃnely on each simplex. The function f
can be expressed as (6.17) where the basis functions fi are aﬃne on each simplex
and are deﬁned by the conditions
fi(gj) =
 1
i = j
0
i̸ = j.
By construction, such a function is continuous.
Figure 6.17 shows an example for k = 2.
Piecewise polynomials and splines
The idea of piecewise-aﬃne functions on a triangulated domain is readily extended
to piecewise polynomials and other functions.
Piecewise polynomials are deﬁned as polynomials (of some maximum degree)
on each simplex of the triangulation, which are continuous, i.e., the polynomials
agree at the boundaries between simplexes. By further restricting the piecewise
polynomials to have continuous derivatives up to a certain order, we can deﬁne
various classes of spline functions. Figure 6.18 shows an example of a cubic spline,
i.e., a piecewise polynomial of degree 3 on R, with continuous ﬁrst and second
derivatives.


## Page 22

328
6
Approximation and ﬁtting
u0
u1
u2
u3
f(u)
u
p1(u)
p2(u)
p3(u)
Figure 6.18 Cubic spline. A cubic spline is a piecewise polynomial, with
continuous ﬁrst and second derivatives. In this example, the cubic spline f
is formed from the three cubic polynomials p1 (on [u0, u1]), p2 (on [u1, u2]),
and p3 (on [u2, u3]). Adjacent polynomials have the same function value,
and equal ﬁrst and second derivatives, at the boundary points u1 and u2.
In this example, the dimension of the family of functions is n = 6, since
we have 12 polynomial coeﬃcients (4 per cubic polynomial), and 6 equality
constraints (3 each at u1 and u2).


## Page 23

6.5
Function ﬁtting and interpolation
329
6.5.2
Constraints
In this section we describe some constraints that can be imposed on the function
f, and therefore, on the variable x ∈Rn.
Function value interpolation and inequalities
Let v be a point in D. The value of f at v,
f(v) =
n
X
i=1
xifi(v),
is a linear function of x. Therefore interpolation conditions
f(vj) = zj,
j = 1, . . . , m,
which require the function f to have the values zj ∈R at speciﬁed points vj ∈D,
form a set of linear equalities in x. More generally, inequalities on the function
value at a given point, as in l ≤f(v) ≤u, are linear inequalities on the variable x.
There are many other interesting convex constraints on f (hence, x) that involve
the function values at a ﬁnite set of points v1, . . . , vN. For example, the Lipschitz
constraint
|f(vj) −f(vk)| ≤L∥vj −vk∥,
j, k = 1, . . . , m,
forms a set of linear inequalities in x.
We can also impose inequalities on the function values at an inﬁnite number of
points. As an example, consider the nonnegativity constraint
f(u) ≥0 for all u ∈D.
This is a convex constraint on x (since it is the intersection of an inﬁnite number
of halfspaces), but may not lead to a tractable problem except in special cases
that exploit the particular structure of the functions. One simple example occurs
when the functions are piecewise-linear. In this case, if the function values are
nonnegative at the grid points, the function is nonnegative everywhere, so we obtain
a simple (ﬁnite) set of linear inequalities.
As a less trivial example, consider the case when the functions are polynomials
on R, with even maximum degree 2k (i.e., n = 2k + 1), and D = R. As shown in
exercise 2.37, page 65, the nonnegativity constraint
p(u) = x1 + x2u + · · · + x2k+1u2k ≥0
for all u ∈R,
is equivalent to
xi =
X
m+n=i+1
Ymn,
i = 1, . . . , 2k + 1,
Y ⪰0,
where Y ∈Sk+1 is an auxiliary variable.


## Page 24

330
6
Approximation and ﬁtting
Derivative constraints
Suppose the basis functions fi are diﬀerentiable at a point v ∈D. The gradient
∇f(v) =
n
X
i=1
xi∇fi(v),
is a linear function of x, so interpolation conditions on the derivative of f at v
reduce to linear equality constraints on x. Requiring that the norm of the gradient
at v not exceed a given limit,
∥∇f(v)∥=

n
X
i=1
xi∇fi(v)
 ≤M,
is a convex constraint on x. The same idea extends to higher derivatives. For
example, if f is twice diﬀerentiable at v, the requirement that
lI ⪯∇2f(v) ⪯uI
is a linear matrix inequality in x, hence convex.
We can also impose constraints on the derivatives at an inﬁnite number of
points. For example, we can require that f is monotone:
f(u) ≥f(v) for all u, v ∈D, u ⪰v.
This is a convex constraint in x, but may not lead to a tractable problem except in
special cases. When f is piecewise aﬃne, for example, the monotonicity constraint
is equivalent to the condition ∇f(v) ⪰0 inside each of the simplexes. Since the
gradient is a linear function of the grid point values, this leads to a simple (ﬁnite)
set of linear inequalities.
As another example, we can require that the function be convex, i.e., satisfy
f((u + v)/2) ≤(f(u) + f(v))/2 for all u, v ∈D
(which is enough to ensure convexity when f is continuous). This is a convex con-
straint, which has a tractable representation in some cases. One obvious example
is when f is quadratic, in which case the convexity constraint reduces to the re-
quirement that the quadratic part of f be nonnegative, which is an LMI. Another
example in which a convexity constraint leads to a tractable problem is described
in more detail in §6.5.5.
Integral constraints
Any linear functional L on the subspace of functions can be expressed as a linear
function of x, i.e., we have L(f) = cT x. Evaluation of f (or a derivative) at a point
is just a special case. As another example, the linear functional
L(f) =
Z
D
φ(u)f(u) du,


## Page 25

6.5
Function ﬁtting and interpolation
331
where φ : Rk →R, can be expressed as L(f) = cT x, where
ci =
Z
D
φ(u)fi(u) du.
Thus, a constraint of the form L(f) = a is a linear equality constraint on x. One
example of such a constraint is the moment constraint
Z
D
tmf(t) dt = a
(where f : R →R).
6.5.3
Fitting and interpolation problems
Minimum norm function ﬁtting
In a ﬁtting problem, we are given data
(u1, y1),
. . . ,
(um, ym)
with ui ∈D and yi ∈R, and seek a function f ∈F that matches this data as
closely as possible. For example in least-squares ﬁtting we consider the problem
minimize
Pm
i=1(f(ui) −yi)2,
which is a simple least-squares problem in the variable x. We can add a variety of
constraints, for example linear inequalities that must be satisﬁed by f at various
points, constraints on the derivatives of f, monotonicity constraints, or moment
constraints.
Example 6.7 Polynomial ﬁtting. We are given data u1, . . . , um ∈R and v1, . . . , vm ∈
R, and hope to approximately ﬁt a polynomial of the form
p(u) = x1 + x2u + · · · + xnun−1
to the data. For each x we form the vector of errors,
e = (p(u1) −v1, . . . , p(um) −vm) .
To ﬁnd the polynomial that minimizes the norm of the error, we solve the norm
approximation problem
minimize
∥e∥= ∥Ax −v∥
with variable x ∈Rn, where Aij = uj−1
i
, i = 1, . . . , m, j = 1, . . . , n.
Figure 6.19 shows an example with m = 40 data points and n = 6 (i.e., polynomials
of maximum degree 5), for the ℓ2- and ℓ∞-norms.


## Page 26

332
6
Approximation and ﬁtting
u
p(u)
−1
−0.5
0
0.5
1
−0.1
0
0.1
0.2
Figure 6.19 Two polynomials of degree 5 that approximate the 40 data
points shown as circles. The polynomial shown as a solid line minimizes the
ℓ2-norm of the error; the polynomial shown as a dashed line minimizes the
ℓ∞-norm.
u
f(u)
−1
−0.5
0
0.5
1
−0.1
0
0.1
0.2
Figure 6.20 Two cubic splines that approximate the 40 data points shown as
circles (which are the same as the data in ﬁgure 6.19). The spline shown as
a solid line minimizes the ℓ2-norm of the error; the spline shown as a dashed
line minimizes the ℓ∞-norm. As in the polynomial approximation shown in
ﬁgure 6.19, the dimension of the subspace of ﬁtting functions is 6.


## Page 27

6.5
Function ﬁtting and interpolation
333
Example 6.8 Spline ﬁtting.
Figure 6.20 shows the same data as in example 6.7,
and two optimal ﬁts with cubic splines. The interval [−1, 1] is divided into three
equal intervals, and we consider piecewise polynomials, with maximum degree 3, with
continuous ﬁrst and second derivatives. The dimension of this subspace of functions
is 6, the same as the dimension of polynomials with maximum degree 5, considered
in example 6.7.
In the simplest forms of function ﬁtting, we have m ≫n, i.e., the number
of data points is much larger than the dimension of the subspace of functions.
Smoothing is accomplished automatically, since all members of the subspace are
smooth.
Least-norm interpolation
In another variation of function ﬁtting, we have fewer data points than the dimen-
sion of the subspace of functions. In the simplest case, we require that the function
we choose must satisfy the interpolation conditions
f(ui) = yi,
i = 1, . . . , m,
which are linear equality constraints on x. Among the functions that satisfy these
interpolation conditions, we might seek one that is smoothest, or smallest. These
lead to least-norm problems.
In the most general function ﬁtting problem, we can optimize an objective
(such as some measure of the error e), subject to a variety of convex constraints
that represent our prior knowledge of the underlying function.
Interpolation, extrapolation, and bounding
By evaluating the optimal function ﬁt ˆf at a point v not in the original data set,
we obtain a guess of what the value of the underlying function is, at the point v.
This is called interpolation when v is between or near the given data points (e.g.,
v ∈conv{v1, . . . , vm}), and extrapolation otherwise.
We can also produce an interval in which the value f(v) can lie, by maximizing
and minimizing (the linear function) f(v), subject to the constraints. We can use
the function ﬁt to help identify faulty data or outliers. Here we might use, for
example, an ℓ1-norm ﬁt, and look for data points with large errors.
6.5.4
Sparse descriptions and basis pursuit
In basis pursuit, there is a very large number of basis functions, and the goal is to
ﬁnd a good ﬁt of the given data as a linear combination of a small number of the
basis functions. (In this context the function family is linearly dependent, and is
sometimes referred to as an over-complete basis or dictionary.) This is called basis
pursuit since we are selecting a much smaller basis, from the given over-complete
basis, to model the data.


## Page 28

334
6
Approximation and ﬁtting
Thus we seek a function f ∈F that ﬁts the data well,
f(ui) ≈yi,
i = 1, . . . , m,
with a sparse coeﬃcient vector x, i.e., card(x) small. In this case we refer to
f = x1f1 + · · · + xnfn =
X
i∈B
xifi,
where B = {i | xi̸ = 0} is the set of indices of the chosen basis elements, as a sparse
description of the data. Mathematically, basis pursuit is the same as the regressor
selection problem (see §6.4), but the interpretation (and scale) of the optimization
problem are diﬀerent.
Sparse descriptions and basis pursuit have many uses. They can be used for
de-noising or smoothing, or data compression for eﬃcient transmission or storage
of a signal. In data compression, the sender and receiver both know the dictionary,
or basis elements. To send a signal to the receiver, the sender ﬁrst ﬁnds a sparse
representation of the signal, and then sends to the receiver only the nonzero coef-
ﬁcients (to some precision). Using these coeﬃcients, the receiver can reconstruct
(an approximation of) the original signal.
One common approach to basis pursuit is the same as the method for regressor
selection described in §6.4, and based on ℓ1-norm regularization as a heuristic for
ﬁnding sparse descriptions. We ﬁrst solve the convex problem
minimize
Pm
i=1(f(ui) −yi)2 + γ∥x∥1,
(6.18)
where γ > 0 is a parameter used to trade oﬀthe quality of the ﬁt to the data,
and the sparsity of the coeﬃcient vector. The solution of this problem can be used
directly, or followed by a reﬁnement step, in which the best ﬁt is found, using the
sparsity pattern of the solution of (6.18). In other words, we ﬁrst solve (6.18), to
obtain ˆx. We then set B = {i | ˆxi̸ = 0}, i.e., the set of indices corresponding to
nonzero coeﬃcients. Then we solve the least-squares problem
minimize
Pm
i=1(f(ui) −yi)2
with variables xi, i ∈B, and xi = 0 for i̸ ∈B.
In basis pursuit and sparse description applications it is not uncommon to have
a very large dictionary, with n on the order of 104 or much more. To be eﬀective,
algorithms for solving (6.18) must exploit problem structure, which derives from
the structure of the dictionary signals.
Time-frequency analysis via basis pursuit
In this section we illustrate basis pursuit and sparse representation with a simple
example. We consider functions (or signals) on R, with the range of interest [0, 1].
We think of the independent variable as time, so we use t (instead of u) to denote
it.
We ﬁrst describe the basis functions in the dictionary. Each basis function is a
Gaussian sinusoidal pulse, or Gabor function, with form
e−(t−τ)2/σ2 cos(ωt + φ),


## Page 29

6.5
Function ﬁtting and interpolation
335
t
f0.5,0,c
f0.5,75,c
f0.5,150,c
0
0
0
0.2
0.2
0.2
0.4
0.4
0.4
0.6
0.6
0.6
0.8
0.8
0.8
1
1
1
−1
0
1
−1
0
1
−1
0
1
Figure 6.21 Three of the basis elements in the dictionary, all with center time
τ = 0.5 and cosine phase. The top signal has frequency ω = 0, the middle
one has frequency ω = 75, and the bottom one has frequency ω = 150.
where σ > 0 gives the width of the pulse, τ is the time of (the center of) the pulse,
ω ≥0 is the frequency, and φ is the phase angle. All of the basis functions have
width σ = 0.05. The pulse times and frequencies are
τ = 0.002k,
k = 0, . . . , 500,
ω = 5k,
k = 0, . . . , 30.
For each time τ, there is one basis element with frequency zero (and phase φ = 0),
and 2 basis elements (cosine and sine, i.e., phase φ = 0 and φ = π/2) for each of 30
remaining frequencies, so all together there are 501 × 61 = 30561 basis elements.
The basis elements are naturally indexed by time, frequency, and phase (cosine or
sine), so we denote them as
fτ,ω,c,
τ = 0, 0.002, . . . , 1,
ω = 0, 5, . . . , 150,
fτ,ω,s,
τ = 0, 0.002, . . . , 1,
ω = 5, . . . , 150.
Three of these basis functions (all with time τ = 0.5) are shown in ﬁgure 6.21.
Basis pursuit with this dictionary can be thought of as a time-frequency analysis
of the data. If a basis element fτ,ω,c or fτ,ω,s appears in the sparse representation
of a signal (i.e., with a nonzero coeﬃcient), we can interpret this as meaning that
the data contains the frequency ω at time τ.
We will use basis pursuit to ﬁnd a sparse approximation of the signal
y(t) = a(t) sin θ(t)


## Page 30

336
6
Approximation and ﬁtting
t
t
ˆy(t), y(t)
y(t) −ˆy(t)
0
0
0.2
0.2
0.4
0.4
0.6
0.6
0.8
0.8
1
1
−1.5
−0.5
0.5
1.5
−0.05
0
0.05
Figure 6.22 Top. The original signal (solid line) and approximation ˆy ob-
tained by basis pursuit (dashed line) are almost indistinguishable. Bottom.
The approximation error y(t) −ˆy(t), with diﬀerent vertical scale.
where
a(t) = 1 + 0.5 sin(11t),
θ(t) = 30 sin(5t).
(This signal is chosen only because it is simple to describe, and exhibits noticeable
changes in its spectral content over time.)
We can interpret a(t) as the signal
amplitude, and θ(t) as its total phase. We can also interpret
ω(t) =

dθ
dt
 = 150| cos(5t)|
as the instantaneous frequency of the signal at time t. The data are given as 501
uniformly spaced samples over the interval [0, 1], i.e., we are given 501 pairs (tk, yk)
with
tk = 0.005k,
yk = y(tk),
k = 0, . . . , 500.
We ﬁrst solve the ℓ1-norm regularized least-squares problem (6.18), with γ =
1. The resulting optimal coeﬃcient vector is very sparse, with only 42 nonzero
coeﬃcients out of 30561. We then ﬁnd the least-squares ﬁt of the original signal
using these 42 basis vectors. The result ˆy is compared with the original signal
y in ﬁgure 6.22. The top ﬁgure shows the approximated signal (in dashed line)
and, almost indistinguishable, the original signal y(t) (in solid line). The bottom
ﬁgure shows the error y(t) −ˆy(t). As is clear from the ﬁgure, we have obtained an


## Page 31

6.5
Function ﬁtting and interpolation
337
y(t)
t
ω(t)
τ
0
0
0.2
0.2
0.4
0.4
0.6
0.6
0.8
0.8
1
1
−1.5
−0.5
0.5
1.5
0
50
100
150
Figure 6.23 Top: Original signal. Bottom: Time-frequency plot. The dashed
curve shows the instantaneous frequency ω(t) = 150| cos(5t)| of the original
signal. Each circle corresponds to a chosen basis element in the approxima-
tion obtained by basis pursuit. The horizontal axis shows the time index τ,
and the vertical axis shows the frequency index ω of the basis element.
approximation ˆy with a very good relative ﬁt. The relative error is
(1/501) P501
i=1(y(ti) −ˆy(ti))2
(1/501) P501
i=1 y(ti)2
= 2.6 · 10−4.
By plotting the pattern of nonzero coeﬃcients versus time and frequency, we
obtain a time-frequency analysis of the original data. Such a plot is shown in ﬁg-
ure 6.23, along with the instantaneous frequency. The plot shows that the nonzero
components closely track the instantaneous frequency.
6.5.5
Interpolation with convex functions
In some special cases we can solve interpolation problems involving an inﬁnite-
dimensional set of functions, using ﬁnite-dimensional convex optimization. In this
section we describe an example.
We start with the following question: When does there exist a convex function
f : Rk →R, with dom f = Rk, that satisﬁes the interpolation conditions
f(ui) = yi,
i = 1, . . . , m,


## Page 32

338
6
Approximation and ﬁtting
at given points ui ∈Rk? (Here we do not restrict f to lie in any ﬁnite-dimensional
subspace of functions.) The answer is: if and only if there exist g1, . . . , gm such
that
yj ≥yi + gT
i (uj −ui),
i, j = 1, . . . , m.
(6.19)
To see this, ﬁrst suppose that f is convex, dom f = Rk, and f(ui) = yi,
i = 1, . . . , m. At each ui we can ﬁnd a vector gi such that
f(z) ≥f(ui) + gT
i (z −ui)
(6.20)
for all z. If f is diﬀerentiable, we can take gi = ∇f(ui); in the more general case,
we can construct gi by ﬁnding a supporting hyperplane to epi f at (ui, yi). (The
vectors gi are called subgradients.) By applying (6.20) to z = uj, we obtain (6.19).
Conversely, suppose g1, . . . , gm satisfy (6.19). Deﬁne f as
f(z) =
max
i=1,...,m(yi + gT
i (z −ui))
for all z ∈Rk. Clearly, f is a (piecewise-linear) convex function. The inequali-
ties (6.19) imply that f(ui) = yi, for i = 1, . . . , m.
We can use this result to solve several problems involving interpolation, approx-
imation, or bounding, with convex functions.
Fitting a convex function to given data
Perhaps the simplest application is to compute the least-squares ﬁt of a convex
function to given data (ui, yi), i = 1, . . . , m:
minimize
Pm
i=1(yi −f(ui))2
subject to
f : Rk →R is convex,
dom f = Rk.
This is an inﬁnite-dimensional problem, since the variable is f, which is in the
space of continuous real-valued functions on Rk. Using the result above, we can
formulate this problem as
minimize
Pm
i=1(yi −ˆyi)2
subject to
ˆyj ≥ˆyi + gT
i (uj −ui),
i, j = 1, . . . , m,
which is a QP with variables ˆy ∈Rm and g1, . . . , gm ∈Rk. The optimal value of
this problem is zero if and only if the given data can be interpolated by a convex
function, i.e., if there is a convex function that satisﬁes f(ui) = yi. An example is
shown in ﬁgure 6.24.
Bounding values of an interpolating convex function
As another simple example, suppose that we are given data (ui, yi), i = 1, . . . , m,
which can be interpolated by a convex function. We would like to determine the
range of possible values of f(u0), where u0 is another point in Rk, and f is any
convex function that interpolates the given data.
To ﬁnd the smallest possible
value of f(u0) we solve the LP
minimize
y0
subject to
yj ≥yi + gT
i (uj −ui),
i, j = 0, . . . , m,


## Page 33

6.5
Function ﬁtting and interpolation
339
Figure 6.24 Least-squares ﬁt of a convex function to data, shown as circles.
The (piecewise-linear) function shown minimizes the sum of squared ﬁtting
error, over all convex functions.
which is an LP with variables y0 ∈R, g0, . . . , gm ∈Rk. By maximizing y0 (which
is also an LP) we ﬁnd the largest possible value of f(u0) for a convex function that
interpolates the given data.
Interpolation with monotone convex functions
As an extension of convex interpolation, we can consider interpolation with a convex
and monotone nondecreasing function. It can be shown that there exists a convex
function f : Rk →R, with dom f = Rk, that satisﬁes the interpolation conditions
f(ui) = yi,
i = 1, . . . , m,
and is monotone nondecreasing (i.e., f(u) ≥f(v) whenever u ⪰v), if and only if
there exist g1, . . . , gm ∈Rk, such that
gi ⪰0,
i = 1, . . . , m,
yj ≥yi + gT
i (uj −ui),
i, j = 1, . . . , m.
(6.21)
In other words, we add to the convex interpolation conditions (6.19), the condition
that the subgradients gi are all nonnegative. (See exercise 6.12.)
Bounding consumer preference
As an application, we consider a problem of predicting consumer preferences. We
consider diﬀerent baskets of goods, consisting of diﬀerent amounts of n consumer
goods. A goods basket is speciﬁed by a vector x ∈[0, 1]n where xi denotes the
amount of consumer good i.
We assume the amounts are normalized so that
0 ≤xi ≤1, i.e., xi = 0 is the minimum and xi = 1 is the maximum possible
amount of good i. Given two baskets of goods x and ˜x, a consumer can either
prefer x to ˜x, or prefer ˜x to x, or consider x and ˜x equally attractive. We consider
one model consumer, whose choices are repeatable.


## Page 34

340
6
Approximation and ﬁtting
We model consumer preference in the following way. We assume there is an
underlying utility function u : Rn →R, with domain [0, 1]n; u(x) gives a measure
of the utility derived by the consumer from the goods basket x. Given a choice
between two baskets of goods, the consumer chooses the one that has larger utility,
and will be ambivalent when the two baskets have equal utility. It is reasonable to
assume that u is monotone nondecreasing. This means that the consumer always
prefers to have more of any good, with the amounts of all other goods the same. It
is also reasonable to assume that u is concave. This models satiation, or decreasing
marginal utility as we increase the amount of goods.
Now suppose we are given some consumer preference data, but we do not know
the underlying utility function u.
Speciﬁcally, we have a set of goods baskets
a1, . . . , am ∈[0, 1]n, and some information about preferences among them:
u(ai) > u(aj) for (i, j) ∈P,
u(ai) ≥u(aj) for (i, j) ∈Pweak,
(6.22)
where P, Pweak ⊆{1, . . . , m}×{1, . . . , m} are given. Here P gives the set of known
preferences: (i, j) ∈P means that basket ai is known to be preferred to basket aj.
The set Pweak gives the set of known weak preferences: (i, j) ∈Pweak means that
basket ai is preferred to basket aj, or that the two baskets are equally attractive.
We ﬁrst consider the following question: How can we determine if the given data
are consistent, i.e., whether or not there exists a concave nondecreasing utility
function u for which (6.22) holds?
This is equivalent to solving the feasibility
problem
ﬁnd
u
subject to
u : Rn →R concave and nondecreasing
u(ai) > u(aj),
(i, j) ∈P
u(ai) ≥u(aj),
(i, j) ∈Pweak,
(6.23)
with the function u as the (inﬁnite-dimensional) optimization variable. Since the
constraints in (6.23) are all homogeneous, we can express the problem in the equiv-
alent form
ﬁnd
u
subject to
u : Rn →R concave and nondecreasing
u(ai) ≥u(aj) + 1,
(i, j) ∈P
u(ai) ≥u(aj),
(i, j) ∈Pweak,
(6.24)
which uses only nonstrict inequalities. (It is clear that if u satisﬁes (6.24), then
it must satisfy (6.23); conversely, if u satisﬁes (6.23), then it can be scaled to
satisfy (6.24).) This problem, in turn, can be cast as a (ﬁnite-dimensional) linear
programming feasibility problem, using the interpolation result on page 339:
ﬁnd
u1, . . . , um, g1, . . . , gm
subject to
gi ⪰0,
i = 1, . . . , m
uj ≤ui + gT
i (aj −ai),
i, j = 1, . . . , m
ui ≥uj + 1,
(i, j) ∈P
ui ≥uj,
(i, j) ∈Pweak.
(6.25)
By solving this linear programming feasibility problem, we can determine whether
there exists a concave, nondecreasing utility function that is consistent with the


## Page 35

6.5
Function ﬁtting and interpolation
341
given sets of strict and nonstrict preferences. If (6.25) is feasible, there is at least
one such utility function (and indeed, we can construct one that is piecewise-linear,
from a feasible u1, . . . , um, g1, . . . , gm). If (6.25) is not feasible, we can conclude
that there is no concave increasing utility function that is consistent with the given
sets of strict and nonstrict preferences.
As an example, suppose that P and Pweak are consumer preferences that are
known to be consistent with at least one concave increasing utility function. Con-
sider a pair (k, l) that is not in P or Pweak, i.e., consumer preference between
baskets k and l is not known. In some cases we can conclude that a preference
holds between basket k and l, even without knowing the underlying preference
function. To do this we augment the known preferences (6.22) with the inequality
u(ak) ≤u(al), which means that basket l is preferred to basket k, or they are
equally attractive. We then solve the feasibility linear program (6.25), including
the extra weak preference u(ak) ≤u(al). If the augmented set of preferences is in-
feasible, it means that any concave nondecreasing utility function that is consistent
with the original given consumer preference data must also satisfy u(ak) > u(al).
In other words, we can conclude that basket k is preferred to basket l, without
knowing the underlying utility function.
Example 6.9 Here we give a simple numerical example that illustrates the discussion
above. We consider baskets of two goods (so we can easily plot the goods baskets).
To generate the consumer preference data P, we compute 40 random points in [0, 1]2,
and then compare them using the utility function
u(x1, x2) = (1.1x1/2
1
+ 0.8x1/2
2
)/1.9.
These goods baskets, and a few level curves of the utility function u, are shown in
ﬁgure 6.25.
We now use the consumer preference data (but not, of course, the true utility function
u) to compare each of these 40 goods baskets to the basket a0 = (0.5, 0.5). For each
original basket ai, we solve the linear programming feasibility problem described
above, to see if we can conclude that basket a0 is preferred to basket ai. Similarly,
we check whether we can conclude that basket ai is preferred to basket a0. For each
basket ai, there are three possible outcomes: we can conclude that a0 is deﬁnitely
preferred to ai, that ai is deﬁnitely preferred to a0, or (if both LP feasibility problems
are feasible) that no conclusion is possible. (Here, deﬁnitely preferred means that the
preference holds for any concave nondecreasing utility function that is consistent with
the original given data.)
We ﬁnd that 21 of the baskets are deﬁnitely rejected in favor of (0.5, 0.5), and 14
of the baskets are deﬁnitely preferred. We cannot make any conclusion, from the
consumer preference data, about the remaining 5 baskets. These results are shown in
ﬁgure 6.26. Note that goods baskets below and to the left of (0.5, 0.5) will deﬁnitely
be rejected in favor of (0.5, 0.5), using only the monotonicity property of the utility
function, and similarly, those points that are above and to the right of (0.5, 0.5) must
be preferred. So for these 17 points, there is no need to solve the feasibility LP (6.25).
Classifying the 23 points in the other two quadrants, however, requires the concavity
assumption, and solving the feasibility LP (6.25).


## Page 36

342
6
Approximation and ﬁtting
x1
x2
0
0.5
1
0
0.5
1
Figure 6.25 Forty goods baskets a1, . . . , a40, shown as circles.
The
0.1, 0.2, . . . , 0.9 level curves of the true utility function u are shown as dashed
lines. This utility function is used to ﬁnd the consumer preference data P
among the 40 baskets.
x1
x2
0
0.5
1
0
0.5
1
Figure 6.26 Results of consumer preference analysis using the LP (6.25), for a
new goods basket a0 = (0.5, 0.5). The original baskets are displayed as open
circles if they are deﬁnitely rejected (u(ak) < u(a0)), as solid black circles
if they are deﬁnitely preferred (u(ak) > u(a0)), and as squares when no
conclusion can be made. The level curve of the underlying utility function,
that passes through (0.5, 0.5), is shown as a dashed curve. The vertical and
horizontal lines passing through (0.5, 0.5) divide [0, 1]2 into four quadrants.
Points in the upper right quadrant must be preferred to (0.5, 0.5), by the
monotonicity assumption on u. Similarly, (0.5, 0.5) must be preferred to the
points in the lower left quadrant. For the points in the other two quadrants,
the results are not obvious.


## Page 37

Bibliography
343
Bibliography
The robustness properties of approximations with diﬀerent penalty functions were an-
alyzed by Huber [Hub64, Hub81], who also proposed the penalty function (6.4).
The
log-barrier penalty function arises in control theory, where it is applied to the system
closed-loop frequency response, and has several names, e.g., central H∞, or risk-averse
control; see Boyd and Barratt [BB91] and the references therein.
Regularized approximation is covered in many books, including Tikhonov and Arsenin
[TA77] and Hansen [Han98]. Tikhonov regularization is sometimes called ridge regression
(Golub and Van Loan [GL89, page 564]).
Least-squares approximation with ℓ1-norm
regularization is also known under the name lasso (Tibshirani [Tib96]).
Other least-
squares regularization and regressor selection techniques are discussed and compared in
Hastie, Tibshirani, and Friedman [HTF01, §3.4].
Total variation denoising was introduced for image reconstruction by Rudin, Osher, and
Fatemi [ROF92].
The robust least-squares problem with norm bounded uncertainty (page 321) was in-
troduced by El Ghaoui and Lebret [EL97], and Chandrasekaran, Golub, Gu, and Sayed
[CGGS98]. El Ghaoui and Lebret also give the SDP formulation of the robust least-squares
problem with structured uncertainty (page 323).
Chen, Donoho, and Saunders [CDS01] discuss basis pursuit via linear programming. They
refer to the ℓ1-norm regularized problem (6.18) as basis pursuit denoising. Meyer and
Pratt [MP68] is an early paper on the problem of bounding utility functions.


## Page 38

344
6
Approximation and ﬁtting
Exercises
Norm approximation and least-norm problems
6.1 Quadratic bounds for log barrier penalty.
Let φ : R →R be the log barrier penalty
function with limit a > 0:
φ(u) =

−a2 log(1 −(u/a)2)
|u| < a
∞
otherwise.
Show that if u ∈Rm satisﬁes ∥u∥∞< a, then
∥u∥2
2 ≤
m
X
i=1
φ(ui) ≤φ(∥u∥∞)
∥u∥2∞
∥u∥2
2.
This means that Pm
i=1 φ(ui) is well approximated by ∥u∥2
2 if ∥u∥∞is small compared to
a. For example, if ∥u∥∞/a = 0.25, then
∥u∥2
2 ≤
m
X
i=1
φ(ui) ≤1.033 · ∥u∥2
2.
6.2 ℓ1-, ℓ2-, and ℓ∞-norm approximation by a constant vector. What is the solution of the
norm approximation problem with one scalar variable x ∈R,
minimize
∥x1 −b∥,
for the ℓ1-, ℓ2-, and ℓ∞-norms?
6.3 Formulate the following approximation problems as LPs, QPs, SOCPs, or SDPs. The
problem data are A ∈Rm×n and b ∈Rm. The rows of A are denoted aT
i .
(a) Deadzone-linear penalty approximation: minimize Pm
i=1 φ(aT
i x −bi), where
φ(u) =

0
|u| ≤a
|u| −a
|u| > a,
where a > 0.
(b) Log-barrier penalty approximation: minimize Pm
i=1 φ(aT
i x −bi), where
φ(u) =

−a2 log(1 −(u/a)2)
|u| < a
∞
|u| ≥a,
with a > 0.
(c) Huber penalty approximation: minimize Pm
i=1 φ(aT
i x −bi), where
φ(u) =

u2
|u| ≤M
M(2|u| −M)
|u| > M,
with M > 0.
(d) Log-Chebyshev approximation: minimize maxi=1,...,m | log(aT
i x)−log bi|. We assume
b ≻0. An equivalent convex form is
minimize
t
subject to
1/t ≤aT
i x/bi ≤t,
i = 1, . . . , m,
with variables x ∈Rn and t ∈R, and domain Rn × R++.


## Page 39

Exercises
345
(e) Minimizing the sum of the largest k residuals:
minimize
Pk
i=1 |r|[i]
subject to
r = Ax −b,
where |r|[1] ≥|r|[2] ≥· · · ≥|r|[m] are the numbers |r1|, |r2|, . . . , |rm| sorted in
decreasing order. (For k = 1, this reduces to ℓ∞-norm approximation; for k = m, it
reduces to ℓ1-norm approximation.) Hint. See exercise 5.19.
6.4 A diﬀerentiable approximation of ℓ1-norm approximation. The function φ(u) = (u2+ǫ)1/2,
with parameter ǫ > 0, is sometimes used as a diﬀerentiable approximation of the absolute
value function |u|. To approximately solve the ℓ1-norm approximation problem
minimize
∥Ax −b∥1,
(6.26)
where A ∈Rm×n, we solve instead the problem
minimize
Pm
i=1 φ(aT
i x −bi),
(6.27)
where aT
i is the ith row of A. We assume rank A = n.
Let p⋆denote the optimal value of the ℓ1-norm approximation problem (6.26). Let ˆx
denote the optimal solution of the approximate problem (6.27), and let ˆr denote the
associated residual, ˆr = Aˆx −b.
(a) Show that p⋆≥Pm
i=1 ˆr2
i /(ˆr2
i + ǫ)1/2.
(b) Show that
∥Aˆx −b∥1 ≤p⋆+
m
X
i=1
|ˆri|

1 −
|ˆri|
(ˆr2
i + ǫ)1/2

.
(By evaluating the righthand side after computing ˆx, we obtain a bound on how subop-
timal ˆx is for the ℓ1-norm approximation problem.)
6.5 Minimum length approximation. Consider the problem
minimize
length(x)
subject to
∥Ax −b∥≤ǫ,
where length(x) = min{k | xi = 0 for i > k}.
The problem variable is x ∈Rn; the
problem parameters are A ∈Rm×n, b ∈Rm, and ǫ > 0. In a regression context, we are
asked to ﬁnd the minimum number of columns of A, taken in order, that can approximate
the vector b within ǫ.
Show that this is a quasiconvex optimization problem.
6.6 Duals of some penalty function approximation problems. Derive a Lagrange dual for the
problem
minimize
Pm
i=1 φ(ri)
subject to
r = Ax −b,
for the following penalty functions φ : R →R. The variables are x ∈Rn, r ∈Rm.
(a) Deadzone-linear penalty (with deadzone width a = 1),
φ(u) =

0
|u| ≤1
|u| −1
|u| > 1.
(b) Huber penalty (with M = 1),
φ(u) =

u2
|u| ≤1
2|u| −1
|u| > 1.


## Page 40

346
6
Approximation and ﬁtting
(c) Log-barrier (with limit a = 1),
φ(u) = −log(1 −u2),
dom φ = (−1, 1).
(d) Relative deviation from one,
φ(u) = max{u, 1/u} =

u
u ≥1
1/u
u ≤1,
with dom φ = R++.
Regularization and robust approximation
6.7 Bi-criterion optimization with Euclidean norms. We consider the bi-criterion optimization
problem
minimize (w.r.t. R2
+)
(∥Ax −b∥2
2, ∥x∥2
2),
where A ∈Rm×n has rank r, and b ∈Rm. Show how to ﬁnd the solution of each of the
following problems from the singular value decomposition of A,
A = U diag(σ)V T =
r
X
i=1
σiuivT
i
(see §A.5.4).
(a) Tikhonov regularization: minimize ∥Ax −b∥2
2 + δ∥x∥2
2.
(b) Minimize ∥Ax −b∥2
2 subject to ∥x∥2
2 = γ.
(c) Maximize ∥Ax −b∥2
2 subject to ∥x∥2
2 = γ.
Here δ and γ are positive parameters.
Your results provide eﬃcient methods for computing the optimal trade-oﬀcurve and the
set of achievable values of the bi-criterion problem.
6.8 Formulate the following robust approximation problems as LPs, QPs, SOCPs, or SDPs.
For each subproblem, consider the ℓ1-, ℓ2-, and the ℓ∞-norms.
(a) Stochastic robust approximation with a ﬁnite set of parameter values, i.e., the sum-
of-norms problem
minimize
Pk
i=1 pi∥Aix −b∥
where p ⪰0 and 1T p = 1. (See §6.4.1.)
(b) Worst-case robust approximation with coeﬃcient bounds:
minimize
supA∈A ∥Ax −b∥
where
A = {A ∈Rm×n | lij ≤aij ≤uij, i = 1, . . . , m, j = 1, . . . , n}.
Here the uncertainty set is described by giving upper and lower bounds for the
components of A. We assume lij < uij.
(c) Worst-case robust approximation with polyhedral uncertainty:
minimize
supA∈A ∥Ax −b∥
where
A = {[a1 · · · am]T | Ciai ⪯di, i = 1, . . . , m}.
The uncertainty is described by giving a polyhedron Pi = {ai | Ciai ⪯di} of possible
values for each row. The parameters Ci ∈Rpi×n, di ∈Rpi, i = 1, . . . , m, are given.
We assume that the polyhedra Pi are nonempty and bounded.
