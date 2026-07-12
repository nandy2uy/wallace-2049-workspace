# LSCOMO



## Page 1

Convex
Optimization
Large-Scale
ALGORITHMS & ANALYSES 
via MONOTONE OPERATORS
ERNEST K. RYU  
& WOTAO YIN


## Page 2

Large-Scale Convex Optimization
Algorithms and Analyses via Monotone Operators
Last Compiled: April 20, 2023


## Page 3



## Page 4

Large-Scale Convex Optimization
Algorithms and Analyses via Monotone Operators
Ernest K. Ryu
Department of Mathematical Sciences
Seoul National University
Wotao Yin
Department of Mathematics
University of California, Los Angeles
Decision Intelligence Lab, DAMO Academy
Alibaba Group
Cover art by Hyo Chung Lee


## Page 5



## Page 6

Dedicated to our wives
Bora and Rui


## Page 7



## Page 8

Contents
Preface
xi
1
Introduction and preliminaries
1
1.1
First-order methods in the modern era . . . . . . . . . . . . . . . . . . .
1
1.2
Limitations of monotone operator theory . . . . . . . . . . . . . . . . . .
2
1.3
Preliminaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
Bibliographical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
I
Monotone operator methods
23
2
Monotone operators and base splitting schemes
25
2.1
Set-valued operators
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
2.2
Monotone operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
2.3
Nonexpansive and averaged operators
. . . . . . . . . . . . . . . . . . .
32
2.4
Fixed-point iteration
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
2.5
Resolvents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
2.6
Proximal point method . . . . . . . . . . . . . . . . . . . . . . . . . . . .
44
2.7
Operator splitting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
45
2.8
Variable metric methods . . . . . . . . . . . . . . . . . . . . . . . . . . .
54
Bibliographical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
57
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
60
3
Primal-dual splitting methods
69
3.1
Infimal postcomposition technique
. . . . . . . . . . . . . . . . . . . . .
69
3.2
Dualization technique . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
72
3.3
Variable metric technique
. . . . . . . . . . . . . . . . . . . . . . . . . .
75
3.4
Gaussian elimination technique . . . . . . . . . . . . . . . . . . . . . . .
78
3.5
Linearization technique . . . . . . . . . . . . . . . . . . . . . . . . . . . .
82
Bibliographical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
89
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
91


## Page 9

viii
Contents
4
Parallel computing
99
4.1
Computational complexity via flop count . . . . . . . . . . . . . . . . . .
99
4.2
Parallel computing
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
Bibliographical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
5
Randomized coordinate update methods
113
5.1
Randomized coordinate fixed-point iteration . . . . . . . . . . . . . . . . 113
5.2
Coordinate and extended coordinate-friendly operators . . . . . . . . . . 117
5.3
Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
5.4
Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
Bibliographical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
6
Asynchronous coordinate update methods
131
6.1
Asynchronous fixed-point iteration . . . . . . . . . . . . . . . . . . . . . 133
6.2
Extended coordinate-friendly operators and exclusive memory access . . 142
6.3
Server-worker framework . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
6.4
Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
6.5
Exclusive memory access . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
Bibliographical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
II
Additional topics
159
7
Stochastic optimization
161
7.1
Stochastic forward-backward method . . . . . . . . . . . . . . . . . . . . 162
7.2
Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
Bibliographical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
8
ADMM-type methods
175
8.1
Function-linearized proximal ADMM . . . . . . . . . . . . . . . . . . . . 175
8.2
Derived ADMM-type methods . . . . . . . . . . . . . . . . . . . . . . . . 182
8.3
Bregman methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194
Bibliographical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 200
9
Duality in splitting methods
205
9.1
Fenchel duality
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205
9.2
Attouch–Théra duality
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
9.3
Duality in splitting methods . . . . . . . . . . . . . . . . . . . . . . . . . 207
Bibliographical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212


## Page 10

Contents
ix
10 Maximality and monotone operator theory
215
10.1 Maximality of subdifferential . . . . . . . . . . . . . . . . . . . . . . . . . 215
10.2 Fitzpatrick function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
10.3 Maximality and extension theorems . . . . . . . . . . . . . . . . . . . . . 220
Bibliographical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223
11 Distributed and decentralized optimization
227
11.1 Distributed optimization with centralized consensus
. . . . . . . . . . . 227
11.2 Decentralized optimization with graph consensus . . . . . . . . . . . . . 234
11.3 Decentralized optimization with mixing matrices
. . . . . . . . . . . . . 237
Bibliographical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247
12 Acceleration
255
12.1 Accelerated gradient method . . . . . . . . . . . . . . . . . . . . . . . . . 255
12.2 Accelerated proximal point and optimized Halpern method . . . . . . . . 258
12.3 When does an acceleration accelerate? . . . . . . . . . . . . . . . . . . . 260
Bibliographical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262
13 Scaled relative graphs
265
13.1 Basic definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265
13.2 Scaled relative graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268
13.3 Operator and SRG transformations . . . . . . . . . . . . . . . . . . . . . 275
13.4 Averagedness coefficients . . . . . . . . . . . . . . . . . . . . . . . . . . . 289
Bibliographical Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 292
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 294
Appendices
297
A Miscellaneous probability background
299
References
301
Index
329


## Page 11

x
Contents


## Page 12

Preface
We write this book to share an elegant perspective that provides powerful higher-
level insight into first-order convex optimization methods. The study of first-order
convex optimization methods, which are more effective at solving large-scale opti-
mization problems, started in the 1960s and 1970s, but the field at the time was
focused rather on second-order methods, which are more effective at solving smaller
problems. It was in the 2000s that increased computation power and the availability
of big data brought first-order optimization methods into the mainstream. During
this modern era, the authors entered the field of optimization and discovered (but
did not invent) the perspective mentioned above, and we wish to share it through
this book.
Our goal is to present a unified analysis of convex optimization algo-
rithms through the abstraction of monotone operators.
The widespread modern use of first-order methods makes this perspective more
relevant than ever for both researchers and users of optimization.
This book has a somewhat unconventional organization: the chapters are struc-
tured around the techniques for deriving and analyzing optimization methods,
rather than around optimization methods themselves. Through this organization,
we aim to provide structure to the theory and achieve intellectual economy in that
we present and analyze many optimization methods with a handful of mathemati-
cal concepts. The result is, we hope, a book that serves as a concise introduction
to the theory of convex optimization algorithms.
We should also explain what this book is not.
This book is not a text on
monotone operator theory. We use monotone operators as a means to the end of
developing and analyzing optimization algorithms, but we do not focus on the study
of monotone operators themselves. This book is not a comprehensive reference on
the best convex optimization methods or the strongest convergence analyses. We
utilize a handful of techniques to derive and analyze optimization methods, and we
only present methods and results that fit this approach.
Audience
This book is meant for both mathematicians and engineers. We appeal to mathe-
maticians by showing that the abstraction is elegant and, in some aspects, challeng-
ing (interesting). We appeal to engineers, users of optimization, with the simplicity
of the techniques and the diversity of the algorithms. In several instances, we have


## Page 13

xii
Preface
Chapter 1
Chapter 2
Chapter 3
Chapter 4
Chapter 5
Chapter 6
Chapter 7
Chapter 8
Chapter 9
Chapter 10
Chapter 11
Chapter 12
Chapter 13
Figure 1: Chapter dependencies.
Solid arrows denote hard dependence, while
dashed arrows denote soft dependence. For example, Chapter 11 can be read after
Chapter 4 but an understanding of the materials up to Chapter 6 is beneficial.
met engineers who know only gradient descent and ADMM, which, although pow-
erful, are not universally feasible or best choices. This book empowers the reader
to choose and even design the splitting methods best suited for any given problem.
The background required of the reader is a good knowledge of advanced calcu-
lus, linear algebra, basic probability, and basic notions of convex analysis on the
topics of convex sets, convex functions, convex optimization problems, and convex
duality at the level of Chapters 2 through 5 of Boyd and Vandenberghe’s Con-
vex Optimization. Background in (mathematical) analysis and measure-theoretic
probability theory is helpful but not necessary.
Informally, this book presupposes interest in convex optimization, and an ap-
preciation of it as a useful tool. To keep the discussion concise, we focus on opti-
mization algorithms without discussing the engineering and science origins of the
optimization problems that the algorithms solve. Boyd and Vandenberghe’s Convex
Optimization is an excellent reference on the applications.
Note to instructors
The material of this book can be taught in 15 weeks of a graduate or advanced
undergraduate course. We have taught this book in an undergraduate course at
SNU after covering the first five chapters of Boyd and Vandenberghe’s Convex
Optimization and in a graduate-level course at UCLA. The chapters of Part I
should be taught in a linear order, while the chapters of Part II can be selected
independently. Figure 1 illustrates the chapter dependencies. While the book does
not delve deeply into the analysis of any single method, it covers many methods,
as listed in Table 1. In our experience, many students appreciate the variety rather
than the depth of the coverage.


## Page 14

Preface
xiii
Chapters
Methods
Chapter 2
Gradient descent, dual ascent, proximal point method, method
of multipliers, proximal method of multipliers, forward-backward
splitting, Douglas–Rachford splitting, Davis–Yin splitting, proxi-
mal gradient method, iterative soft thresholding, consensus opti-
mization, forward-Douglas–Rachford, variable metric proximal
point, variable metric forward-backward splitting, backward-
backward method, averaged alternating modified reflections,
PPXA.
Chapter 3
ADMM, alternating minimization algorithm (Tseng), PDHG
(Chambolle–Pock), Condat–Vũ, proximal method of multipliers
with function linearization, PAPC/PDFP2O, linearized method
of multipliers, PD3O, proximal ADMM, linearized ADMM,
Chen–Teboulle, DYS 3-block ADMM, doubly linearized method
of multipliers.
Chapter 5
Coordinate gradient descent block-coordinate descent, coordi-
nate proximal-gradient descent, stochastic dual coordinate as-
cent, MISO/Finito, coordinate updates on conic programs.
Chapter 6
ARock, asynchronous coordinate gradient descent, asynchronous
ADMM.
Chapter 7
Stochastic forward-backward method, stochastic gradient de-
scent, stochastic proximal gradient method, stochastic proximal
simultaneous gradient method, stochastic Condat–Vũ.
Chapter 8
Function-linearized proximal ADMM, golden ratio ADMM, dou-
bly linearized ADMM, partial linearization, near-circulant split-
ting, Jacobi ADMM, 2-1-2 ADMM, Trip-ADMM, split Bregman
method, four-block 2-1-2-4-3-4 ADMM.
Chapter 11
Distributed ADMM, decentralized ADMM, distributed gradient
descent, method of diffusion, adapt-then-combine, PG-EXTRA,
NIDS.
Chapter 12
Nesterov accelerated gradient method, FISTA, accelerated prox-
imal point method.
Table 1: Optimization methods covered in each chapter.


## Page 15

xiv
Preface
This book contains almost no discussion of applications. Students without prior
exposure to applications may find lectures solely on algorithms dry, so an instructor
using this book may need to supplement the lectures with applications of interest to
the audience. For example, at SNU, we discussed engineering and machine learning
applications from Boyd and Vandenberghe’s Convex Optimization.
The textbook contains adequate homework exercises with varying levels of dif-
ficulties; some basic exercises complement the main exposition, while the difficult
ones are designed to challenge the mathematically gifted students. We have also
made public course material, including lecture slides and videos, on the website
https://large-scale-book.mathopt.com/
to help prospective instructors prepare for their lectures.
Acknowledgments
This book was greatly improved by the suggestions of Pontus Giselsson, Shuvomoy
Das Gupta, Howard Heaton, Jongmin Lee, Daniel McKenzie, Chanwoo Park, Jisun
Park, Ruoyu Sun, Jaewook Suh, Matthew Tam, and Taeho Yoon. We also thank
the students in our courses who provided us with valuable feedback.
We also acknowledge Stephen P. Boyd, the Ph.D. advisor of Ernest Ryu. Boyd
has a writing style of extreme clarity, and Ernest Ryu has strived to learn from
and emulate it. Those familiar with Boyd’s work may recognize his influence. In
particular, Chapter 2 has much overlap with the review paper “Primer on Monotone
Operator Methods,” written by Ernest Ryu and Stephen Boyd in 2016 [RB16].
Ernest K. Ryu
Seoul, Korea
Wotao Yin
Los Angeles, California, USA


## Page 16

Chapter 1
Introduction and preliminaries
Monotone operator theory is an elegant and powerful tool for analyzing first-order
convex optimization methods and, as such, plays a central role in convex analysis
and convex optimization theory. In this book, we use this tool to provide a unified
analysis of many classical and modern convex optimization methods.
This book is organized into two parts. Part I presents analysis of convex opti-
mization methods via monotone operators, the core content. The content of Part
I has sequential dependence, so the chapters should be read in a linear order. Part
II presents additional auxiliary topics. The chapters can be read independently of
each other. A diagram in the preface illustrates the dependency of the chapters.
1.1
First-order methods in the modern era
Many convex optimization methods can be classified into first or second-order
methods. First-order methods can be described and analyzed with gradients and
subgradients, while second-order methods use second-order derivatives or their ap-
proximations.
In the early days of convex optimization, the 1970s through the 1990s, re-
searchers focused primarily on second-order methods, as they were more effective
in solving the relatively smaller optimization problems of the era. Within the past
decade, however, the demand to solve ever-larger problems grew, and so did the
popularity of first-order methods.
Second-order methods require relatively fewer iterations to solve the optimiza-
tion problem to high accuracy, even up to machine precision. However, the com-
putational cost per iteration quickly becomes expensive as the problem size grows.
In contrast, first-order methods have a much lower computational cost per itera-
tion. For some large-scale optimization problems, running even a single iteration
of a second-order method is infeasible, while first-order methods can solve such
problems to acceptable accuracy.
Another advantage of first-order methods is that they are extremely simple; we
can usually describe the entire method with two or three lines of equations. This


## Page 17

2
1
Introduction and preliminaries
is a significant advantage in practice, as simpler methods are easy for practition-
ers to implement and try out quickly, and the simplicity tends to make efficient
parallelization easier.
The two classes of methods are usually not in competition.
When a high-
accuracy solution is needed, second-order methods should be used. In large-scale
problems, one should use first-order methods and tolerate inaccuracy. After all,
most engineering applications require only a few digits of accuracy in their solution.
If the problem size is small, one should use second-order methods since there is little
reason to forgo the high accuracy.
The total cost of a method is
(cost per iteration) × (number of iterations).
We can analyze the cost per iteration by examining the computational cost of the
individual components of the method. We can analyze the number of iterations
required for convergence by analyzing the rate of convergence.
In convex optimization, arguments advocating one method over another are
often based on the cost per iteration. In fact, we just made this very argument
in comparing first-order and second-order methods. However, it is important to
keep in mind that these arguments are incomplete since the cost per iteration is
only half of the equation, literally. A method with a low cost per iteration has the
potential, not a guarantee, to be efficient.
Nevertheless, primarily focusing on the cost per iteration of a method is still a
useful simplification, so we adopt it in this book. With the exception of §12 and
§13, this book almost entirely focuses on establishing convergence without paying
much attention to the rate of convergence. We do prove convergence rates, but the
rates are discussed infrequently.
1.2
Limitations of monotone operator theory
One of the main goals of this book is to provide streamlined and simple convergence
proofs, and we only discuss results that fit this approach. Such results are simple
but often not the strongest. The strongest results in convex optimization usually
involve arguments that go beyond monotone operator theory.
Proofs based on monotone operator theory use monotonicity, rather than con-
vexity, as the key property. This line of analysis does not lead to results involving
function values. For example, the gradient method xk+1 = xk−α∇f(xk) converges,
under suitable assumptions, with rate ∥∇f(xk)∥2 ≤O(1/k) and f(xk) −f(x⋆) ≤
O(1/k). We can prove the first result with properties of monotone operators, but
the second result requires properties of convex functions. Also, topics such as line
searching, Frank–Wolfe, and second-order methods are not explained very well with
monotone operator theory. Monotone operators do play a central role, but convex
optimization theory does go beyond monotone operators.


## Page 18

1.3
Preliminaries
3
1.3
Preliminaries
In this section, we quickly review preliminary topics. We simply state, without
proof, many of the results based on convex analysis and refer interested readers
to standard references such as [Roc70d, Roc74, HL93, HL01, BV04, Nes04, BL06,
NP06, Ber09, BV10, BC17a].
1.3.1
Sets
A set is empty when it contains no element. Let ∅denote the empty set. When a
set contains one element, we say it is a singleton.
A set S is convex if x, y ∈S implies θx + (1 −θ)y ∈S for all θ ∈[0, 1]. The
empty set, singletons, and Rn are also convex sets.
In this book, we overload the standard notation defined for points to sets. In
particular, when α ∈R, x ∈Rn, A, B ⊆Rn, and M ∈Rm×n, we write
αA = {αa | a ∈A}
x + A = {x + a | a ∈A}
MA = {Ma | a ∈A}
A + B = {a + b | a ∈A, b ∈B}.
These operations preserve convexity; if A and B are convex, all of these sets are
convex. The sum A + B is called the Minkowski sum.
1.3.2
Linear algebra
Write Rn for the n-dimensional Euclidean space. For any x, y ∈Rn, write
⟨x, y⟩= x⊺y =
n
X
i=1
xiyi
for the standard inner product.
Given a matrix A ∈Rm×n, write R(A) for the range of A and N(A) for the
nullspace of A. If A ∈Rn×n, we say A is a square matrix. If A⊺= A, which
implies A is square, we say A is symmetric. If A is symmetric, the eigenvalues of
A are real. Write λmax(A) and λmin(A) respectively for the largest and smallest
eigenvalues of A, when A is symmetric.
If all eigenvalues of a symmetric matrix A are nonnegative, we say A is symmet-
ric positive semidefinite and write A ⪰0. If all eigenvalues of a symmetric matrix
A are strictly positive, we say A is symmetric positive definite and write A ≻0.
We write A ⪰B and A ≻B if A −B ⪰0 and A −B ≻0, respectively.
Given M ⪰0, write M 1/2 for the matrix square root, the unique symmetric
positive semidefinite matrix that satisfies (M 1/2)2 = M. If M ≻0, then M 1/2 ≻0,
and we write M −1/2 = (M 1/2)−1.


## Page 19

4
1
Introduction and preliminaries
Consider a symmetric matrix X ∈R(m+n)×(m+n) partitioned as
X =
 A
B
B⊺
C

,
where A = A⊺∈Rm×m, B ∈Rm×n, and C = C⊺∈Rn×n. When A is invertible,
we call the matrix
S = C −B⊺A−1B
the Schur complement of A in X. Note that S ∈Rn×n is symmetric. Given A ≻0,
X is positive (semi)definite if and only if S is positive (semi)definite. Likewise,
when C is invertible,
T = A −BC−1B⊺
is the Schur complement of C in X. Given C ≻0, X is positive (semi)definite if
and only if T is positive (semi)definite. We use the Schur complement to assess
whether a symmetric matrix is positive (semi)definite.
The 2-norm or the Euclidean norm is
∥x∥= ∥x∥2 =
p
⟨x, x⟩.
In some cases, we will use the 1-norm and the ∞-norm respectively defined as
∥x∥1 =
n
X
i=1
|xi|,
∥x∥∞=
max
i=1,...,n |xi|.
Given A ≻0, define the A-norm as
∥x∥A =
√
x⊺Ax.
Given A ⪰0, define the A-seminorm as
∥x∥A =
√
x⊺Ax.
Since this is a seminorm, the triangle inequality ∥x + y∥A ≤∥x∥A + ∥y∥A and
absolute homogeneity ∥αx∥A = |α|∥x∥A hold, but ∥x∥A = 0 is possible when
x̸ = 0.
Given a matrix A ∈Rm×n, write
σmax(A) =
p
λmax(A⊺A) = max
x̸=0
∥Ax∥
∥x∥
for the maximum singular value of A and
σmin(A) =
p
λmin(A⊺A) = min
x̸=0
∥Ax∥
∥x∥
for the minimum singular value of A. While a real eigenvalue can be negative, all
singular values are nonnegative.
We say V ⊆Rn is a (linear) subspace if 0 ∈V , x, y ∈V implies x + y ∈V , and
x ∈V implies αx ∈V for any α ∈R. Under this definition, {0} and Rn are also
subspaces. For any A ∈Rm×n, R(A) and N(A) are subspaces.


## Page 20

1.3
Preliminaries
5
1.3.3
Analysis
For L > 0, we say that a mapping 핋: Rn →Rm is L-Lipschitz (continuous) if
∥핋(x) −핋(y)∥≤L∥x −y∥
∀x, y ∈Rn.
We say 핋is Lipschitz (continuous) if 핋is L-Lipschitz for some unspecified L ∈
(0, ∞). (One could say that a constant function is 0-Lipschitz, but we exclude this
degenerate case from our definition, since we will later encounter quantities like
2/L.)
If a mapping is Lipschitz, it is a continuous mapping. If 핋1 and 핋2 are respec-
tively L1- and L2-Lipschitz, then 핋1 ◦핋2 is L1L2-Lipschitz since
∥핋1(핋2(x)) −핋1(핋2(y))∥≤L1∥핋2(x) −핋2(y)∥≤L1L2∥x −y∥.
If 핋1 and 핋2 are respectively L1- and L2-Lipschitz, then α1핋1 + α2핋2 is (|α1|L1 +
|α2|L2)-Lipschitz.
A matrix A ∈Rm×n can be viewed as a mapping from x to Ax. Since
∥Ax∥≤σmax(A)∥x∥,
we can view A as a σmax(A)-Lipschitz mapping.
Write
B(x, r) = {y ∈Rn | ∥y −x∥≤r}
for the closed ball of radius r centered at x. Define the interior of a set C as
int C = {x ∈C | B(x, r) ⊆C for some r > 0}.
Denote the closure of a set C as cl C. Define the boundary of C as cl C\int C.
An affine set A can be expressed as
A = x0 + V,
where x0 ∈Rn and V ⊆Rn is a subspace. The affine hull of C is defined as
aff C = {θ1x1 + · · · + θkxk | x1, . . . , xk ∈C, θ1 + · · · + θk = 1, k ≥1}.
The affine hull is the smallest affine set containing C; if C ⊆A and A is affine,
then aff cl C ⊆A.
Define the relative interior of a set C as
ri C = {x ∈C | B(x, r) ∩aff C ⊆C for some r > 0}.
The relative interior of a nonempty convex set is nonempty. Under this definition,
the relative interior of a singleton is the singleton itself. Define the relative bound-
ary of C as cl C\ri C. When we are dealing with low-dimensional sets placed in
higher-dimensional spaces, the notion of relative interior is useful.
Example 1.1 Consider the line segment
S =

(x, y) ∈R2 | x ∈[0.5, 1], y = 4x −3
	
.
The relative interior is the line segment with the end points excluded.


## Page 21

6
1
Introduction and preliminaries
S =
ri S =
Define the distance of a point x ∈Rn to a nonempty set X ⊆Rn as
dist(x, X) = inf
z∈X ∥z −x∥.
When X is nonempty and closed, the infimum is attained and dist(x, X) = 0 if
and only if x ∈X. For notational convenience, write dist2(x, X) = (dist(x, X))2.
1.3.4
Functions
An extended real-valued function is a function that maps to the extended real line,
R ∪{±∞}. Unless otherwise specified, functions in this book are extended real-
valued. Write
dom f = {x ∈Rn | f(x) < ∞}
for the (effective) domain of f. We use ≤, <, ≥, and > for elements of the extended
real line in the obvious way; for any finite α, we have −∞< α < ∞. We allow
∞≤∞and −∞≤−∞, but not ∞< ∞or −∞< −∞.
A function f is convex if dom f is a convex set and
f(θx + (1 −θ)y) ≤θf(x) + (1 −θ)f(y),
∀x, y ∈dom f, θ ∈(0, 1).
(1.1)
A function f is strictly convex if the inequality (1.1) is strict when x̸ = y. We say
f is (strictly) concave if −f is (strictly) convex.
The epigraph of a function is defined as
epi f = {(x, α) ∈Rn × R | f(x) ≤α}.
A function f is convex if and only if epi f is convex. A function is proper if its
value is never −∞and is finite somewhere.
A proper function is closed if its
epigraph is a closed set in Rn+1.
A proper function is closed if and only if it
is lower semicontinuous. We say a function is CCP if it is closed, convex, and
proper.
As most convex functions of interest are closed and proper, we focus
exclusively on CCP functions in this book. A function is CCP if and only if its
epigraph is a nonempty closed convex set without a “vertical line,” a line of the
form {(x0, t) | t ∈R} for some x0 ∈Rn.


## Page 22

1.3
Preliminaries
7
Example 1.2 Whether a convex function f is closed is determined by f’s behavior on
the boundary of dom f.
Closed convex function
Convex but not closed
The dashed line denotes the function value of ∞.
Example 1.3 The epigraph of the CCP function −log is a nonempty closed convex
set.
epi (−log)
If f is a CCP function and α > 0, then αf is CCP. If f and g are CCP functions
and there is an x such that f(x) + g(x) < ∞, then f + g is CCP. If f is a CCP
function on Rn, A ∈Rn×m, and there is an x ∈Rm such that f(Ax) < ∞, then
g(x) = f(Ax) is CCP.
We say f : Rn →R∪{±∞} is differentiable if f : Rn →R (so f is not extended
real-valued), gradient ∇f(x) = [ ∂f
∂x1 (x), . . . , ∂f
∂xn (x)]⊺exists for all x ∈Rn, and
lim
h→0
f(x + h) −f(x) −⟨∇f(x), h⟩
∥h∥
= 0
for all x ∈Rn. A differentiable function f is convex if and only if
f(y) ≥f(x) + ⟨∇f(x), y −x⟩
∀x, y ∈Rn.
In other words, f is convex if its first-order Taylor expansion is a global lower
bound of f. A twice continuously differentiable function f is convex if and only if
∇2f(x) ⪰0 for all x ∈Rn. (By the classic Schwarz’s theorem, ∇2f(x) ∈Rn×n is
symmetric when f is twice continuously differentiable.) Intuitively speaking, ∇2f
measures curvature, and f is convex if f is flat or has upward curvature everywhere.
If f is a one-dimensional differentiable function, f is convex if and only if f ′(x) is
monotonically nondecreasing. See the bibliographical notes for further discussion.


## Page 23

8
1
Introduction and preliminaries
Write
argmin f =

x ∈Rn
 f(x) = inf
z∈Rn f(z)

for the set of minimizers of f. When f is CCP, argmin f is a closed convex set,
possibly empty. When f is strictly convex, argmin f has at most one point.
For S ⊆Rn, define the indicator function
δS(x) =
(
0
if x ∈S
∞
otherwise.
If S is convex, closed, and nonempty, then δS is CCP.
1.3.5
Convex optimization problems
An unconstrained optimization problem
minimize
x∈Rn
f(x)
is convex if f is a convex function. We call f the objective function. The constrained
optimization problem
minimize
x∈Rn
f(x)
subject to
x ∈C
is convex if f is a convex function and C is a convex set.
We call x ∈C the
constraint. When C is an affine set of the form {x | Ax = b}, we also write
minimize
x∈Rn
f(x)
subject to
Ax = b.
In these problems, x ∈Rn is the optimization variable. If a solution to an
optimization problem exists, write superscript ⋆to denote a solution. So if x is the
optimization variable, x⋆denotes a solution. If u is the optimization variable, u⋆
denotes a solution.
Indicator functions allow us to move the constraint into the objective function
and treat a constrained problem as an unconstrained problem:
minimize
x∈Rn
f(x) + δC(x).
This use of indicator functions and extended value functions greatly simplifies the
notation.
1.3.6
Subgradient
We say g ∈Rn is a subgradient of a convex function f at x if
f(y) ≥f(x) + ⟨g, y −x⟩
∀y ∈Rn.
(1.2)


## Page 24

1.3
Preliminaries
9
In other words, a subgradient provides a global affine lower bound of f. We call
(1.2) the subgradient inequality. The subdifferential of a convex function f at x is
∂f(x) = {g ∈Rn | f(y) ≥f(x) + ⟨g, y −x⟩, ∀y ∈Rn}.
In other words, ∂f(x) is the set of subgradients of f at x. It is straightforward
to see that ∂f(x) is a closed convex set, possibly empty. A convex function f is
differentiable at x if and only if ∂f(x) is a singleton.
By definition, x⋆∈argmin f if and only if 0 ∈∂f(x⋆). This fact, called Fermat’s
rule, illustrates why subgradients are central in convex optimization.
Example 1.4 The absolute value function is differentiable everywhere except at 0.
f(x) = |x|
∂f(x)
Example 1.5 At x1 the convex function f is differentiable and ∂f(x1) = {∇f(x1)}.
At x2, f is not differentiable and has many subgradients.
x1
x2
f(x1) + ⟨∇f(x1), x −x1⟩
f(x2) + ⟨g1, x −x2⟩,
g1 ∈∂f(x2)
f(x2) + ⟨g2, x −x2⟩,
g2 ∈∂f(x2)
Example 1.6 Let C ⊆Rn be a closed convex set. Then ∂δC(x) = ℕC(x), where
ℕC(x) =
 ∅
if x̸ ∈C
{y | ⟨y, z −x⟩≤0 ∀z ∈C}
if x ∈C
is the normal cone operator. For x ∈int C, ℕC(x) = {0}, and for x /∈C, ℕC(x) = ∅;
ℕC(x) is nontrivial only when x is on the boundary of C.


## Page 25

10
1
Introduction and preliminaries
C
x2
ℕC(x2)
x3
ℕC(x3)
x1
ℕC(x1)
In this book, we will not pay too much attention to the meaning of ℕC. Rather, we
use ℕC as notational shorthand for ∂δC.
We say a convex f is subdifferentiable at x if ∂f(x)̸ = ∅. When f is convex and
proper, ∂f(x) = ∅where f(x) = ∞. When f is convex and proper, ∂f(x)̸ = ∅for
any x ∈ri dom f. So a convex and proper function is not subdifferentiable outside
its domain, is subdifferentiable within the relative interior of its domain, and may
or may not be subdifferentiable on the relative boundary of its domain.
Example 1.7 The CCP function f defined as
f(x) =
 −√x
for x ≥0
∞
for x < 0
is not subdifferentiable at x = 0. The slope is −∞, but we do not allow infinite
gradients.
−√x
Several standard identities for gradients also hold for subdifferentials. Let f be
CCP and α > 0. Then
∂(αf)(x) = α∂f(x).
Let f be CCP and R(A) ∩ri dom f̸ = ∅. If g(x) = f(Ax), then
∂g(x) = A⊺∂f(Ax).
(1.3)
Let f and g be CCP and dom f ∩int dom g̸ = ∅. Then
∂(f + g)(x) = ∂f(x) + ∂g(x).
(1.4)
To clarify, ∂f(x)+∂g(x) is the Minkowski sum of the sets ∂f(x) and ∂g(x). Without
the regularity conditions involving interiors, we can say
∂g(x) ⊇A⊺∂f(Ax),
∂(f + g)(x) ⊇∂f(x) + ∂g(x).
Using the operator notation we define in §2, we can more concisely write
∂αf = α∂f,
∂g = A⊺∂fA,
∂(f + g) = ∂f + ∂g,
provided the regularity conditions involving interiors hold.


## Page 26

1.3
Preliminaries
11
1.3.7
Regularity conditions
Say we have a mathematical statement “If P then Q”. Then, if P “usually” holds,
then Q “usually” holds. In this case, we say P is a regularity condition, since P is
satisfied in the usual “regular” case. We just saw an example of this; if the regularity
condition dom f ∩int dom g̸ = ∅holds, then the identity ∂(f + g) = ∂f + ∂g holds.
Statements in this book involving interiors and relative interiors can be consid-
ered regularity conditions. We keep track of these conditions, as they are necessary
for a rigorous treatment of the subject. However, we do not focus on them.
1.3.8
Conjugate function, strong convexity, and smoothness
Define the conjugate function of f as
f ∗(y) = sup
x∈Rn {⟨y, x⟩−f(x)} ,
which is also known as the Fenchel conjugate or Legendre–Fenchel transform. When
f is CCP, f ∗is CCP and f ∗∗= f; i.e., the conjugate is CCP and the conjugate of
the conjugate function is the original function. We call f ∗∗the biconjugate of f.
Note that we use the symbol ∗for the notion of conjugate or dual, while we use
the symbol ⋆for the notion of optimality.
The conjugate function appears in optimization often because if f is CCP, then
∂f is an “inverse” of ∂f ∗in the sense we define in §2.1. When f and f ∗are both
differentiable, then (∇f)−1 = ∇f ∗as functions from Rn to Rn.
We say a CCP f is µ-strongly convex if any of the following equivalent conditions
are satisfied:
• f(x) −(µ/2)∥x∥2 is convex.
• ⟨∂f(x) −∂f(y), x −y⟩≥µ∥x −y∥2 for all x, y.
• ∇2f(x) ⪰µI for all x if f is twice continuously differentiable.
The second condition is written with set-valued notation; the left-hand side is a
subset of R, so the inequality means the subset lies in [µ∥x −y∥2, ∞). In the third
condition, I ∈Rn×n denotes the identity matrix.
Strongly convex CCP functions have unique minimizers.
If f is µ-strongly
convex and g is convex, then f + g is µ-strongly convex. Informally speaking, a
function is µ-strongly convex if it has upward curvature of at least µ, and we can
think of nondifferentiable points to be points with infinite curvature. To clarify,
strong convexity does not imply differentiability.
Example 1.8 Informally speaking, µ-strongly convex functions have upward curvature
of at least µ and L-smooth convex functions have upward curvature of no more than
L.


## Page 27

12
1
Introduction and preliminaries
Strongly convex but not smooth
Smooth but not strongly convex
We say a CCP f is L-smooth if any of the following equivalent conditions are
satisfied:
• f(x) −(L/2)∥x∥2 is concave.
• f is differentiable and ⟨∇f(x) −∇f(y), x −y⟩≥(1/L)∥∇f(x) −∇f(y)∥2 for
all x, y.
• f is differentiable and ∇f is L-Lipschitz.
• ∇2f(x) ⪯LI for all x if f is twice continuously differentiable.
(Remember, a function g is concave if −g is convex.) The terminology “L-smoothness”
is somewhat nonstandard; “smoothness” often means infinite differentiability in
other fields of mathematics. Under our definition, L-smooth functions only need
to be once-continuously differentiable.
Informally speaking, a convex function is L-strongly convex if it has upward
curvature of at most L. Since non-differentiable points of convex functions can
be thought of as points with infinite upward curvature, it is natural that smooth
functions are differentiable.
If f is µ-strongly convex and L-smooth, then µ ≤L. This follows from
µ∥x −y∥2 ≤⟨∇f(x) −∇f(y), x −y⟩≤∥∇f(x) −∇f(y)∥∥x −y∥≤L∥x −y∥2,
where we used the Cauchy–Schwartz inequality and the Lipschitz continuity of ∇f.
Strong convexity and smoothness are dual properties; a CCP f is µ-strongly convex
if and only if f ∗is (1/µ)-smooth. This follows from the fact that ∂f and ∂f ∗are
inverse operators, which we show in §2.1.
1.3.9
Convex duality
In many introductory texts of convex optimization, one starts with a primal opti-
mization problem and finds a corresponding dual problem. In this book, we take
a slightly different viewpoint. We view the primal and dual problems as the two
halves of a larger saddle point problem.
Let L: Rn × Rm →R ∪{±∞}. We say L(x, u) is convex-concave if L is convex
in x when u is fixed and concave in u when x is fixed. We say (x⋆, u⋆) is a saddle
point of L if
L(x⋆, u) ≤L(x⋆, u⋆) ≤L(x, u⋆)
∀x ∈Rn, u ∈Rm.


## Page 28

1.3
Preliminaries
13
We call
minimize
x∈Rn
supu∈Rm L(x, u)
the primal problem generated by L and write p⋆= infx supu L(x, u) for the primal
optimal value. We call
maximize
u∈Rm
infx∈Rn L(x, u)
the dual problem generated by L and write d⋆= supu infx L(x, u) for the dual opti-
mal value. In most engineering settings, one starts with an optimization problem,
not a convex-concave saddle function. With this view of duality, the trick is to find
a convex-concave saddle function that generates the primal problem of interest.
Example 1.9 Let f be a CCP function on Rn, A ∈Rm×n, and b ∈Rm. Consider the
Lagrangian
L(x, u) = f(x) + ⟨u, Ax −b⟩,
(1.5)
which generates the primal problem
minimize
x∈Rn
f(x)
subject to
Ax = b
(1.6)
and dual problem
maximize
u∈Rm
−f ∗(−A⊺u) −b⊺u.
(1.7)
The dual variable u is also called the Lagrange multipliers. If the constraint qualifi-
cation
{x | Ax = b} ∩int dom f̸ = ∅
holds, then d⋆= p⋆.
Example 1.10 Consider the Lagrangian
L(x, u) = f(x) + ⟨u, Ax⟩−g∗(u),
(1.8)
which generates the primal problem
minimize
x∈Rn
f(x) + g(Ax)
(1.9)
and dual problem
maximize
u∈Rm
−f ∗(−A⊺u) −g∗(u).
(1.10)
If the constraint qualification
Adom f ∩int dom g̸ = ∅
holds, then d⋆= p⋆. This primal-dual problem pair is sometimes called the Fenchel–
Rockafellar dual.


## Page 29

14
1
Introduction and preliminaries
Weak duality, which states d⋆≤p⋆, always holds. To prove this, note that for
any x, u we have
inf
x L(x, u) ≤L(x, u)
sup
u inf
x L(x, u) ≤sup
u L(x, u)
d⋆= sup
u inf
x L(x, u) ≤inf
x sup
u L(x, u) = p⋆.
Strong duality, which states d⋆= p⋆, holds often but not always in convex
optimization. Regularity conditions that ensure strong duality are sometimes called
constraint qualifications. The constraint qualifications for strong duality are similar
to the regularity conditions for subgradient identities. Again, interested readers can
refer to standard references such as [Roc74, Ber09, Boţ10] for a careful discussion
of this subject.
Total duality states that a primal solution exists, a dual solution exists, and
strong duality holds. Total duality holds if and only if L has a saddle point. Solving
the primal and dual optimization problems is equivalent to finding a saddle point
of the saddle function generating the primal and dual problems, provided that total
duality holds. We will see in §2 and §3 that total duality is the regularity condition
that ensures primal-dual methods converge.
Let us prove the equivalence. Assume L has a saddle point (x⋆, u⋆). Then
L(x⋆, u⋆) = inf
x L(x, u⋆)
≤sup
u inf
x L(x, u) = d⋆
≤inf
x sup
u L(x, u) = p⋆
≤sup
u L(x⋆, u) = L(x⋆, u⋆),
and equality holds throughout.
Since infx supu L(x, u) = supu L(x⋆, u), x⋆is a
primal solution. Since infx L(x, u⋆) = supu infx L(x, u), u⋆is a dual solution. Since
d⋆= supu infx L(x, u) = infx supu L(x, u) = p⋆, strong duality holds.
On the other hand, assume total duality holds and x⋆and u⋆are primal and
dual solutions. Then
inf
x L(x, u⋆) = sup
u inf
x L(x, u) = d⋆
= inf
x sup
u L(x, u) = p⋆
= sup
u L(x⋆, u).
Since
L(x⋆, u⋆) ≤sup
u L(x⋆, u) = inf
x L(x, u⋆) ≤L(x⋆, u⋆),
equality holds throughout and we conclude
sup
u L(x⋆, u) = L(x⋆, u⋆) = inf
x L(x, u⋆),


## Page 30

1.3
Preliminaries
15
i.e., (x⋆, u⋆) is a saddle point.
An augmented Lagrangian is a saddle function that has additional terms while
sharing the same saddle points as its unaugmented counterpart.
Example 1.11 Consider the Lagrangian
L(x, u) = f(x) + ⟨u, Ax −b⟩
with the associated primal problem
minimize
x∈Rn
f(x)
subject to
Ax = b.
We will often use the augmented Lagrangian
Lρ(x, u) = f(x) + ⟨u, Ax −b⟩+ ρ
2∥Ax −b∥2
(1.11)
with ρ > 0. It is straightforward to show that (x, u) is a saddle point of L if and only
if it is a saddle point of Lρ for any ρ > 0.
Certain augmented Lagrangians arise naturally in monotone operator theory. In
this book, we simply use these augmented Lagrangians without ascribing meaning
to them.
1.3.10
Slater’s constraint qualification
In the context of convex duality, regularity conditions that ensure strong duality
are sometimes called constraint qualifications.
The so-called Slater’s constraint
qualification is widely used, although not all constraint qualifications are due to
Slater.
Consider the primal problem
minimize
x∈Rn
f0(x)
subject to
fi(x) ≤0
for i = 1, . . . , m
Ax = b,
where f0, f1, . . . , fm are CCP functions, A ∈Rp×n, and b ∈Rp, generated by the
Lagrangian
L(x, λ, ν) = f0(x) +
m
X
i=1
λifi(x) + ⟨ν, Ax −b⟩−δRm
+ (λ),
where λ ∈Rm, ν ∈Rp, and Rm
+ = {(λ1, . . . , λm) | λi ≥0 for i = 1, . . . , m} is the
nonnegative orthant.
Slater’s constraint qualification states that if there exists an x such that
x ∈ri
m
\
i=0
dom fi,
fi(x) < 0
for i = 1, . . . , m,
Ax = b,
then strong duality holds (i.e., d⋆= p⋆), and if, furthermore, the optimal values
are finite (i.e., d⋆= p⋆> −∞), then a dual solution exists.


## Page 31

16
1
Introduction and preliminaries
1.3.11
Proximal operators
Let f be a CCP function on Rn. Let α > 0. We define the proximal operator with
respect to αf as
Proxαf(y) = argmin
x∈Rn

αf(x) + 1
2∥x −y∥2

.
When α = 1, we write Proxf. If f is CCP, then Proxαf is well defined, i.e., the
argmin uniquely exists.
Let us prove the well-definedness of Proxαf. Let x0 ∈ri dom f and g ∈∂f(x0).
(A CCP f has a nonempty domain, which is convex, the relative interior of a
nonempty convex set is nonempty, and a CCP function is subdifferentiable on the
relative interior of its domain.) Then, f(x) ≥f(x0) + ⟨g, x −x0⟩, and
αf(x) + 1
2∥x −y∥2
|
{z
}
= ˜
f(x)
≥αf(x0) + α⟨g, x −x0⟩+ 1
2∥x −y∥2
|
{z
}
=h(x)
.
Since lim∥x∥→∞h(x) = ∞and ˜f ≥h, we have lim∥x∥→∞˜f(x) = ∞. Therefore,
˜f(xk) →infx ˜f(x) implies x0, x1, . . . is bounded. For any convergent subsequence
xkj →¯x, lower semicontinuity of ˜f implies ˜f(¯x) ≤infx ˜f(x). Thus ˜f(¯x) = infx ˜f(x),
i.e., a solution exists. Finally, ˜f is strictly convex, so the minimizer is unique.
Example 1.12 The soft-thresholding operator S(x; κ) for x ∈Rn and κ ≥0 is defined
by
(S(x; κ))i =



xi −κ
for κ < xi
0
for −κ ≤xi ≤κ
xi + κ
for xi < −κ
for i = 1, . . . , n.
This is the proximal operator with respect to ℓ1 norm, that is,
S(x; κ) = Proxκ∥·∥1(x).
−κ
κ
S(x; κ)
Example 1.13 Let C be a nonempty closed convex set. Define the projection onto C
as
ΠC(y) = argmin
x∈C
∥x −y∥.
It is straightforward to check that ProxαδC = ProxδC = ΠC for any α > 0. In this
sense, proximal operators generalize projections.
In general, evaluating a proximal operator is an optimization problem itself. For
many interesting convex functions, however, the proximal operator has a closed-
form solution and, if so, is suitable to use as a subroutine. We loosely say a function


## Page 32

1.3
Preliminaries
17
is proximable if its proximal operator is computationally efficient to evaluate. Sev-
eral references such as [CP11b], [PB14b, Section 6], [BSS16, Section 3], and website
[CCCP] catalog a list of proximable functions.
The field of monotone operator and splitting methods revolve around the idea
of decomposing a given optimization problem (which is presumably not simple as a
whole) into smaller, simpler pieces and operating on them separately. These simple
pieces are functions for which we can easily evaluate the gradient or the proximal
operators.
1.3.12
Asymptotic notation
Write f(x1, . . . , xr) = O(g(x1, . . . , xr)) if
lim sup
x1,...,xr→∞

f(x1, . . . , xr)
g(x1, . . . , xr)
 < ∞.
We call this the O-notation (and read it as “big O notation”). For example,
6n2m + n3/2m = O(n2m).
Write f(x1, . . . , xr) = o(g(x1, . . . , xr)) if
lim sup
x1,...,xr→∞

f(x1, . . . , xr)
g(x1, . . . , xr)
 = 0.
We call this the o-notation (and read it as “little o notation”). For example,
1
k log k = o(1/k).
Write f(x1, . . . , xr) ∼g(x1, . . . , xr) if
lim sup
x1,...,xr→∞
f(x1, . . . , xr)
g(x1, . . . , xr) = 1
and say f and g are asymptotically equivalent. For example,
2n2m3 + 3nm3 ∼2n2m3.
These are examples of asymptotic notation. Asymptotic notation is useful for
identifying the limiting behavior of a function as the inputs tend toward a regime
of interest.
When discussing the convergence of methods, often the regime of
interest is k →∞, where k is the iteration count, as we wish to know how the
method eventually behaves. When discussing problem sizes, the regime of interest
is m, n →∞, where m and n describe the problem size, because a method is judged
by how well it can solve large (difficult) problems rather than small (easy) problems.
That is not to say that non-asymptotic information is irrelevant. Sometimes we
should ask at what iteration count or at what problem size the behavior described
by the asymptotic notation becomes visible. Nevertheless, the asymptotic notation
is a useful simplification.


## Page 33

18
1
Introduction and preliminaries
Bibliographical Notes
The 10-page lecture notes on subgradients by Boyd, Duchi, and Vandenberghe [BDV18] is
a great resource to learn more about subgradients. Chapter 23 of Rockafellar’s textbook
[Roc70d] is another great resource providing a careful convex analytical treatment of
subgradients.
The use of the conjugate function in convex analysis was pioneered by Fenchel in his
unpublished lecture notes that were later distributed in mimeographed form [Fen53]. In
particular, the result that f = f ∗∗when f is CCP is called the Fenchel–Moreau theorem
and was first presented in [Fen49] and [Fen53, Theorem 37].
In careful treatments of calculus and analysis, the existence of partial derivatives, differen-
tibility, and continuous differentiability are carefully distinguished. For convex functions,
however, these notions coincide. By [Roc70d, Theorem 25.2], if f is a convex function
and x ∈Rn is a point such that f(x) < ∞, then f is differentiable at x if and only if
∂f
∂xi (x) = lim
h→0
f(x + hei)
h
exists and is finite for all i = 1, . . . , n (where ei is the ith unit vector and the limit is
two-sided). By [Roc70d, Corollary 25.5.1], if f : R →R is convex and differentiable, then
f is necessarily continuously differentiable, i.e., when f is convex, existence of ∇f(x) for
all x ∈Rn implies ∇f(x) is continuous.
Showing that the equivalent definitions for strong convexity and smoothness are indeed
equivalent is a relatively straightforward exercise in vector calculus, when the function is
twice continuously differentiable. Proofs in the general case can be found in references such
as [Nes04]. The equivalence of the smoothness definitions is called the Baillon–Haddad
theorem [BH77, Corollaire 10] [BC10].
There are multiple related but distinct viewpoints of convex duality. The view that primal-
dual problem pairs are two halves of a larger saddle-point problem was developed in the
mid 1960s by Dantzig, Eisenberg, and Cottle [DEC65], Stoer [Sto63, Sto64], and Man-
gasarian and Ponstein [MP65]. The presentation of this book closely follows Rockafellar’s
1974 book [Roc74]. This 74-page book is still one of the best references on convex duality.
Regularity conditions that ensure strong duality in optimization is an area with a large
body of research. Slater’s constraint qualification, the most widely used such condition,
dates back to 1950 [Sla50]. Rockafellar’s book [Roc74] provides a thorough discussion on
this subject.
To expand on the discussion of §1.2, one can, in fact, establish an improved rate ∥∇f(xk)∥2 ≤
O(1/k2) for the gradient method using properties of convex functions [TB19, Theorem 3];
but this result cannot be established using only properties of monotone operators.


## Page 34

Exercises
19
Exercises
1.1 Assume 핋1 : Rn →Rm is L1-Lipschitz and 핋2 : Rn →Rm is L2-Lipschitz. Show that
α1핋1 + α2핋2 is (|α1|L1 + |α2|L2)-Lipschitz.
1.2 Let f be a convex function on Rn. Show that ∂f(x) is a closed convex set for all x ∈Rn.
Hint. Write ∂f(x) as an intersection of closed half-spaces.
Remark. Remember that ∂f(x) can be empty, but the empty set is a closed convex set.
1.3 Show that if f is a CCP function on Rm, A ∈Rm×n, and g(x) = f(Ax), then
∂g(x) ⊇A⊺∂f(Ax)
for all x ∈Rn. Also show that if f and g are CCP functions on Rn, then
∂(f + g)(x) ⊇∂f(x) + ∂g(x)
for all x ∈Rn.
1.4 Consider the function f : R2 →R ∪{±∞} defined as
f(x, y) =



x2/y
for y > 0,
0
for x = y = 0,
∞
otherwise.
Clearly f is proper, and it is possible to show that f is convex. Show that
(a) f is closed, and
(b) f|dom f : dom f →R is not continuous at (0, 0), i.e., show that f restricted to where
it is finite is not continuous at (0, 0).
Remark. This example demonstrates that a CCP function need not be continuous on its
domain. In convex optimization, lower semicontinuity, not continuity, is the regularity
condition of interest. However, a proper convex function is continuous on the relative
interior of its domain.
1.5 Existence of a minimizer with Slater. Let f be a CCP function on Rm, y ∈Rm, and
A ∈Rm×n. Assume R(A⊺) ∩ri dom f ∗̸ = ∅. Consider the optimization problem
minimize
µ∈Rm, ν∈Rn
f ∗(ν) −µ⊺y + 1
2∥µ∥2
subject to
A⊺µ −ν = 0
generated by the Lagrangian
L(µ, ν, x) = f ∗(ν) −µ⊺y + 1
2∥µ∥2 + ⟨x, A⊺µ −ν⟩.
Using Slater’s constraint qualification, show
argmin
x∈Rn

f(x) + (1/2)∥Ax −y∥2	̸
= ∅.
1.6 Saddle points of augmented Lagrangians. Let f be a CCP function on Rn, A ∈Rm×n,
and b ∈Rm. Show that the Lagrangian
L(x, u) = f(x) + ⟨u, Ax −b⟩
and the augmented Lagrangian
Lα(x, u) = f(x) + ⟨u, Ax −b⟩+ α
2 ∥Ax −b∥2,
where α > 0, share the same set of saddle points.


## Page 35

20
1
Introduction and preliminaries
1.7 Assume that a CCP function f : Rn →R ∪{±∞} is proximable. Define g : Rn × Rn →
R ∪{±∞} as
g(x1, x2) = f(x1 + x2).
Show that
Proxg(x1, x2) = 1
2
x1 −x2 + Prox2f(x1 + x2)
x2 −x1 + Prox2f(x1 + x2)

.
Likewise, show that if
h(x1, x2) = f(x1 −x2),
then
Proxh(x1, x2) = 1
2
x1 + x2 + Prox2f(x1 −x2)
x1 + x2 −Prox2f(x1 −x2)

.
Hint. Note that g = f ◦

I
I

and show that (y1, y2) = Proxg(x1, x2) if and only if there
exists a v ∈∂f(y1 + y2) such that
0 = v + (y1 −x1)
0 = v + (y2 −x2).
1.8 Assume a CCP function f : Rn →R ∪{±∞} is proximable. Assume a = (a1, . . . , am) ∈
Rm satisfies a̸ = 0. Define g : Rmn →R ∪{±∞} as
g(x1, . . . , xm) = f(a1x1 + · · · + amxm).
Show that
v =
1
∥a∥2
 a1x1 + · · · + amxm −Prox∥a∥2f(a1x1 + · · · + amxm)

Proxg(x1, . . . , xm) =


x1 −a1v
...
xm −amv

.
1.9 Basic normal cone example. Let Rn
+ = {(x1, . . . , xn) | xi ≥0 for i = 1, . . . , n} be the
nonnegative orthant.
(a) Characterize ℕRn
+, i.e., describe the set ℕRn
+(x) for all x ∈Rn.
(b) Let f : Rn →Rn be CCP and differentiable.
Directly show, without using the
subgradient identity ∂(f + g) = ∂f + ∂g, that x solves
minimize
x∈Rn
f(x)
subject to
x ≥0
if and only if −∇f(x) ∈ℕRn
+(x).
1.10 Linear programming duality. Consider the convex-concave saddle function
L(x, ν, µ) = ⟨c, x⟩+ ⟨Ax + b, ν⟩−⟨x, µ⟩−δRm
+ (ν) −δRn
+(µ),
convex in x ∈Rn and concave in (ν, µ) ∈Rm × Rn. Here, Rm
+ and Rn
+ denote the m and
n-dimensional nonnegative orthants. Remember that δC denotes the indicator function
with respect to the set C.


## Page 36

Exercises
21
Show that the saddle function L generates the primal problem
minimize
x∈Rn
c⊺x
subject to
Ax + b ≤0
x ≥0.
Here, the inequalities denote element-wise nonnegativity. Show that L generates a dual
problem that is equivalent to
maximize
ν∈Rm
b⊺ν
subject to
c + A⊺ν ≥0
ν ≥0.


## Page 37

22
1
Introduction and preliminaries


## Page 38

Part I
Monotone operator methods


## Page 39



## Page 40

Chapter 2
Monotone operators and base
splitting schemes
In this chapter, we present the basic notion of monotone operators and the base
splitting schemes. Throughout this book, we use this machinery to derive and ana-
lyze a wide variety of classical and modern algorithms in a unified and streamlined
manner. The approach is to first pose the problem at hand as a monotone inclu-
sion problem, then use one of the base splitting schemes to encode the solution as
a fixed point of a related operator, and finally find the solution with a fixed-point
iteration.
2.1
Set-valued operators
We say 핋is a (set-valued) operator, point-to-set mapping, set-valued mapping, multi-
valued function, or correspondence on Rn if 핋maps a point in Rn to a (possibly
empty) subset of Rn. We denote this as 핋: Rn ⇒Rn. So, 핋(x) ⊆Rn for all
x ∈Rn. For notational simplicity, we write 핋x = 핋(x).
If 핋x is a singleton or empty for all x, then 핋is a function or is single-valued
with domain {x | 핋(x)̸ = ∅}. In this case, we mix function and operator notation
and write 핋x = y (function notation) although 핋x = {y} (operator notation)
would be strictly correct.
We define the graph of an operator as
Gra 핋= {(x, u) | u ∈핋x} ⊆Rn × Rn.
An operator and its graph are mathematically equivalent. In other words, we can
view 핋: Rn ⇒Rn as a point-to-set mapping and as a subset of Rn × Rn. In this
book, we will often not distinguish the operator itself and its graph; we will often
write 핋when we really mean Gra 핋.
We extend many notions for functions to operators. For example, the domain


## Page 41

26
2
Monotone operators and base splitting schemes
and range of an operator 핋are defined as
dom 핋= {x | 핋x̸ = ∅},
range 핋= {y | y ∈핋x, x ∈Rn}.
If C ⊆Rn, we write 핋(C) = ∪c∈C핋(c) for the image of C under 핋. If 핋and 핊are
operators, we define the composition as
핋◦핊x = 핋핊x = 핋(핊(x))
and the sum as
(핋+ 핊)x = 핋(x) + 핊(x),
where 핋(x) + 핊(x) is the Minkowski sum. Alternate equivalent definitions that use
the graph are
핋핊= {(x, z) | ∃y (x, y) ∈핊, (y, z) ∈핋},
핋+ 핊= {(x, y + z) | (x, y) ∈핋, (x, z) ∈핊}.
We write 핀and 0 for the identity and zero operators
핀= {(x, x) | x ∈Rn},
0 = {(x, 0) | x ∈Rn}.
So, for any operator 핋, we have 핋+ 0 = 핋, 핋핀= 핋, and 핀핋= 핋.
For an L > 0, we say an operator 핋is L-Lipschitz if
∥u −v∥≤L∥x −y∥
∀(x, u), (y, v) ∈핋,
or, more concisely, if
∥핋x −핋y∥≤L∥x −y∥
∀x, y ∈dom 핋.
If 핋is L-Lipschitz, it is single-valued; if 핋x is not a singleton, then we have a
contradiction by setting y = x. (This generalizes the previous definition of §1, as
it allows dom 핋̸ = Rn.)
The inverse operator of 핋is defined as
핋−1 = {(y, x) | (x, y) ∈핋}.
Since 핋−1 can be multi-valued, it is always well defined. It is easy to see that
(핋−1)−1 = 핋and dom 핋−1 = range 핋. As a note of caution, the inverse operator
is not an inverse in the usual sense, as we can have 핋−1핋̸ = 핀. The zero operator
is such an example. However, we do have 핋−1핋x = x when 핋−1 is single-valued
and x ∈dom 핋. See Exercise 2.1.
Example 2.1 The inverse of an operator 핋always exists since we do not require it to
be single-valued.
Gra 핋
Gra 핋−1


## Page 42

2.2
Monotone operators
27
When 0 ∈핋(x), we say that x is a zero of 핋. We write the zero set of an
operator 핋as
Zer 핋= {x | 0 ∈핋x} = 핋−1(0).
We will see that many interesting problems can be posed as finding zeros of an
operator.
Subdifferential
Let f be a convex function on Rn. Then ∂f is a set-valued operator, and
argmin f = Zer ∂f,
i.e., 0 ∈∂f(x) if and only if x minimizes f. When f is known or assumed to be
differentiable, we write ∇f instead of ∂f. As an aside, dom ∂f ⊆dom f, and it is
possible to have dom ∂f̸ = dom f. Example 1.7 is one such example.
When f is CCP, we have the elegant formula
(∂f)−1 = ∂f ∗,
(2.1)
which is known as Fenchel’s identity. This follows from
u ∈∂f(x)
⇔
0 ∈∂f(x) −u
⇔
x ∈argmin
z
{f(z) −u⊺z}
⇔
−f(x) + u⊺x = f ∗(u)
⇔
f(x) + f ∗(u) = u⊺x
⇔
f ∗∗(x) + f ∗(u) = u⊺x
⇔
x ∈∂f ∗(u),
where the second-to-last step uses the fact that f ∗∗= f when f is CCP, as discussed
in §1.3.8, and the last step takes the whole argument backward.
Consider g(y) = f ∗(A⊺y), where f is CCP. If R(A⊺) ∩ri dom f ∗̸ = ∅, we have
u ∈∂g(y)
⇔
u ∈A∂f ∗(A⊺y)
⇔
u = Ax, x ∈∂f ∗(A⊺y)
⇔
u = Ax, ∂f(x) ∋A⊺y
(2.2)
⇔
u = Ax, 0 ∈∂f(x) −A⊺y
⇔
u = Ax, x ∈argmin
z
{f(z) −⟨y, Az⟩} .
This means we can find an element of ∂g by solving a minimization problem.
2.2
Monotone operators
An operator 핋on Rn is said to be monotone if
⟨u −v, x −y⟩≥0
∀(x, u), (y, v) ∈핋.


## Page 43

28
2
Monotone operators and base splitting schemes
Equivalently and more concisely, we can express monotonicity as
⟨핋x −핋y, x −y⟩≥0
∀x, y ∈Rn.
To clarify, ⟨핋x −핋y, x −y⟩is a subset of R and the inequality means the subset
is contained in [0, ∞). When x /∈dom 핋or y /∈dom 핋, then ⟨핋x −핋y, x −y⟩= ∅
and the inequality is vacuous.
An operator 핋is maximal monotone if there is no other monotone operator 핊
such that Gra 핋⊂Gra 핊properly. In other words, if the monotone operator 핋is
not maximal, then there exists (x, u) /∈핋such that 핋∪{(x, u)} is still monotone.
Maximality is a technical but fundamental detail.
Example 2.2 The Heaviside step function u: R →R defined as
u(x) =
 0
for x ≤0
1
for x > 0
is monotone but not maximal. The operator U : R ⇒R defined as
U(x) =



{0}
for x < 0
[0, 1]
for x = 0
{1}
for x > 0
is maximal monotone.
Gra u
Gra U
Subdifferential
If f is convex and proper, then ∂f is a monotone operator. If f is CCP, then ∂f
is maximal monotone. To prove monotonicity, add the inequalities
f(y) ≥f(x) + ⟨∂f(x), y −x⟩,
f(x) ≥f(y) + ⟨∂f(y), x −y⟩,
which hold by the definition of subdifferentials, to get
⟨∂f(x) −∂f(y), x −y⟩≥0.
We prove maximality later in §10. See Exercise 2.2 for an example where ∂f is not
maximal.
Not all maximal monotone operators are subdifferential operators. Subdifferen-
tial operators of CCP functions form a subclass of monotone operators that enjoy
certain nice properties that general maximal monotone operators do not.


## Page 44

2.2
Monotone operators
29
2.2.1
Stronger monotonicity properties
An operator 픸: Rn ⇒Rn is µ-strongly monotone or µ-coercive if µ > 0 and
⟨u −v, x −y⟩≥µ∥x −y∥2
∀(x, u), (y, v) ∈픸.
We say 픸is strongly monotone if it is µ-strongly monotone for some unspecified
µ ∈(0, ∞). An operator 픸is β-cocoercive or β-inverse strongly monotone if β > 0
and
⟨u −v, x −y⟩≥β∥u −v∥2
∀(x, u), (y, v) ∈픸.
We say 픸is cocoercive if it is β-cocoercive for some unspecified β ∈(0, ∞). Coco-
ercivity is the dual property of strong monotonicity; 픸is β-cocoercive if and only if
픸−1 is β-strongly monotone. Clearly, strongly monotone and cocoercive operators
are monotone.
We can more concisely express µ-strong monotonicity as
⟨픸x −픸y, x −y⟩≥µ∥x −y∥2
∀x, y ∈Rn,
and, when 픸is a priori known or assumed to be single-valued, express β-cocoercivity
as
⟨픸x −픸y, x −y⟩≥β∥픸x −픸y∥2
∀x, y ∈Rn.
When 픸is β-cocoercive, the Cauchy–Schwartz inequality tells us
(1/β)∥x −y∥≥∥픸x −픸y∥
∀x, y ∈Rn.
i.e., 픸is (1/β)-Lipschitz. Therefore, cocoercive operators are single-valued. The
converse is not true. The single-valued operator 픸: R2 →R2 defined as
픸(x1, x2) =

0
1
−1
0
 
x1
x2

=

x2
−x1

is an example of an operator that is maximal monotone and Lipschitz, but not
cocoercive since ⟨픸x −픸y, x −y⟩= 0, ∀x, y ∈Rn.
We say 픸is maximal µ-strongly monotone if there is no other µ-strongly mono-
tone operator 픹such that Gra 픸⊂Gra 픹properly.
We say 픸is maximal β-
cocoercive if there is no other β-cocoercive operator 픹such that Gra 픸⊂Gra 픹
properly. Maximal cocoercivity is the dual property of maximal strong monotonic-
ity; 픸is maximal β-cocoercive if and only if 픸−1 is maximal β-strongly monotone.
A β-cocoercive operator 픸is maximal if and only if dom 픸= Rn. (We show this
fact in §10.3 as Theorem 15.) Since a β-cocoercive operator is single-valued, the
statement “픸: Rn →Rn is β-cocoercive” is equivalent to “픸: Rn ⇒Rn is maxi-
mal β-cocoercive” since the notation 픸: Rn →Rn implicitly assumes dom 픸= Rn.
For further discussion, see §10 and Exercises 10.11 and 10.12.
Assume f is CCP. Then f is µ-strongly convex if and only if ∂f is µ-strongly
monotone, and f is L-smooth if and only if ∂f is (1/L)-cocoercive. Since ∂f is
µ-strongly monotone if and only if (∂f)−1 = ∂f ∗is µ-cocoercive, f is µ-strongly
convex if and only if f ∗is (1/µ)-smooth.
The notion of Lipschitz continuity and cocoercivity coincide for subdifferen-
tial operators of convex functions: ∂f is L-Lipschitz if and only if ∂f is (1/L)-
cocoercive. This result is known as the Baillon–Haddad theorem.


## Page 45

30
2
Monotone operators and base splitting schemes
Example 2.3 An operator on R is monotone if its graph is a nondecreasing curve in
R2. If it has vertical portions, the operator is multi-valued. If it is continuous with
no end points, then it is maximal. If its slope is at least µ everywhere, then it is
µ-strongly monotone. If its slope is never more than L, then it is L-Lipschitz. The
notion of Lipschitz continuity and cocoercivity coincide for operators on R.
Not monotone
Monotone but
not maximal
Maximal
monotone and
single-valued
Maximal
monotone and
multi-valued
Strongly
monotone but
not Lipschitz
Lipschitz but not
strongly
monotone
2.2.2
Operations preserving (maximal) monotonicity
If 핋is (maximal) monotone, then 핊(x) = y + α핋(x + z) for any α > 0 and y, z ∈
Rn is (maximal) monotone. If 핋is (maximal) monotone, then 핋−1 is (maximal)
monotone. If 핋and 핊are monotone, then 핋+ 핊is monotone. If 핋and 핊are
maximal monotone and if dom 핋∩int dom 핊̸ = ∅, then 핋+핊is maximal monotone.
If 핋: Rn ⇒Rn is monotone and M ∈Rn×m, then M ⊺핋M is a monotone operator
on Rm. If 핋is maximal and R(M) ∩int dom 핋̸ = ∅, then M ⊺핋M is maximal. See
§10 for proofs of maximality.
If ℝ: Rn ⇒Rn and 핊: Rm ⇒Rm, then the operator 핋: Rn+m ⇒Rn+m
defined by
핋(x, y) = {(u, v) | u ∈ℝx, v ∈핊y}
is (maximal) monotone if ℝand 핊are. We call 핋the concatenation of ℝand 핊
and use the notation
핋=

ℝ
핊

,
핋(x, y) =

ℝx
핊y

.
If 핋is µ-strongly monotone and 핊is monotone, then 핋+ 핊is µ-strongly mono-
tone and α핋is (αµ)-strongly monotone for α > 0. If 핋: Rn ⇒Rn is µ-strongly
monotone, and M ∈Rn×m has rank m (so n ≥m), then M ⊺핋M is (µσ2
min(M))-
strongly monotone. If 핋: Rn →Rn is L-Lipschitz and M ∈Rn×m, then M ⊺핋M
is (Lσ2
max(M))-Lipschitz.


## Page 46

2.2
Monotone operators
31
2.2.3
Examples
Affine operators
An affine operator 핋(x) = Ax + b is maximal monotone if and only if A + A⊺⪰0.
It is a subdifferential operator of a CCP function if and only if A = A⊺and A ⪰0.
It is λmin(A + A⊺)/2-strongly monotone and σmax(A)-Lipschitz.
Continuous operators
We say an operator 핋: Rn ⇒Rn is continuous if dom 핋= Rn, 핋is single-valued,
and 핋is continuous as a function. A continuous monotone operator 핋: Rn →Rn
is maximal. See Exercise 2.4 for a proof. Therefore maximality comes into question
only with discontinuous or set-valued operators.
Differentiable operators
We say an operator is differentiable if it is single-valued, continuous, and dif-
ferentiable.
A differentiable operator 핋: Rn →Rn is monotone if and only if
D핋(x) + D핋(x)⊺⪰0 for all x ∈Rn, where D핋(x) is the n × n Jacobian matrix
evaluated at x. It is µ-strongly monotone if and only if D핋(x) + D핋(x)⊺⪰2µI
for all x, and it is L-Lipschitz if and only if σmax(D핋(x)) ≤L for all x.
See
Exercises 2.7 and 2.8 for proofs.
If a monotone operator 핋is differentiable with continuous D핋, then 핋is a
subdifferential operator of a CCP function if and only if D핋(x) is symmetric for
all x ∈Rn. When n = 3, this condition is equivalent to the so-called curl-less (or
irrotational) condition discussed in the context of electromagnetic potentials.
Saddle subdifferential
Let L: Rn × Rm →R ∪{±∞} be a convex-concave saddle function, i.e., L(x, u)
is convex in x for fixed u and concave in u for fixed x. The saddle subdifferential
operator ∂L: Rn × Rm ⇒Rn × Rm is defined as
∂L(x, u) =

∂xL(x, u)
∂u(−L(x, u))

.
(2.3)
To clarify, ∂x and ∂u respectively denote the subgradients with respect to x and u.
To clarify, ∂L(x, u) is nonempty if both ∂xL(x, u) and ∂u(−L(x, u)) are nonempty.
Zer ∂L is the set of saddle points of L, i.e., 0 ∈∂L(x⋆, u⋆) if and only if (x⋆, u⋆) is
a saddle point of L.
For most well-behaved convex-concave saddle functions, their saddle subdiffer-
entials are maximal monotone. Specifically, “closed proper” convex-concave saddle
functions have maximal monotone saddle subdifferentials. (See the bibliographical
notes.) In this book, we avoid this notion, as it is usually straightforward to verify
the maximality of saddle subdifferentials on a case-by-case basis.
As a technical note, we adopt the convention +∞−∞= −∞+ ∞= −∞in
saddle functions. We do encounter +∞−∞in certain cases such as the Lagrangians
for DRS (2.17), PDHG (1.8), and Condat–Vũ (3.12). The specific value that we
ascribe to +∞−∞does not matter, but we define it for concreteness.


## Page 47

32
2
Monotone operators and base splitting schemes
KKT operator
Consider the problem
minimize
x
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m
hi(x) = 0,
i = 1, . . . , p,
where f0, . . . , fm are CCP and h1, . . . , hp are affine. The associated Lagrangian
L(x, λ, ν) = f0(x) +
m
X
i=1
λifi(x) +
p
X
i=1
νihi(x) −δRm
+ (λ),
where Rm
+ denotes the nonnegative orthant, is a convex-concave saddle function,
and we define the Karush–Kuhn–Tucker (KKT) operator as
핋(x, λ, ν) =


∂xL(x, λ, ν)
−픽(x) + ℕRm
+ (λ)
−ℍ(x)

=


∂xL(x, λ, ν)
∂λ(−L(x, λ, ν))
∂ν(−L(x, λ, ν))

,
where
픽(x) =


f1(x)
...
fm(x)

,
ℍ(x) =


h1(x)
...
hp(x)

.
핋is monotone, since it is a special case of the saddle subdifferential. Arguments
based on total duality tell us that 0 ∈핋(x⋆, λ⋆, ν⋆) if and only if x⋆solves the
primal problem, (λ⋆, ν⋆) solves the dual problem, and strong duality holds.
2.2.4
Monotone inclusion problem
Monotone inclusion problems are problems of the form
find
x∈Rn
0 ∈픸x,
where 픸is monotone. Many interesting problems can be formulated as monotone
inclusion problems. For example, minimizing a convex function f is equivalent to
finding a zero of ∂f.
2.3
Nonexpansive and averaged operators
Nonexpansive and contractive operators
We say an operator 핋is nonexpansive if
∥핋x −핋y∥≤∥x −y∥
∀x, y ∈dom 핋.


## Page 48

2.4
Fixed-point iteration
33
1
L
Contractive
⊂
θ
1
Averaged
⊂
1
Nonexpansive
Figure 2.1: Illustration of classes of contractive, averaged, and nonexpansive oper-
ators. The figure illustrates the relationship: contractive ⊂averaged ⊂nonexpan-
sive. The precise meaning of these figures will be defined in §13.
In other words, 핋is nonexpansive if it is 1-Lipschitz. We say 핋is a contraction
if it is L-Lipschitz with L < 1. Mapping a pair of points by a contraction reduces
the distance between them; mapping them by a nonexpansive operator does not
increase the distance between them.
If 핋and 핊are nonexpansive, then 핋핊is nonexpansive. If 핋or 핊is furthermore
contractive, then 핋핊is contractive. If 핋and 핊are nonexpansive, then θ핋+ (1 −
θ)핊with θ ∈[0, 1], a convex combination, is nonexpansive. If 핋is furthermore
contractive and θ ∈(0, 1], then θ핋+ (1 −θ)핊is contractive.
Averaged operators
For θ ∈(0, 1), we say an operator 핋is θ-averaged if 핋= (1 −θ)핀+ θ핊for some
nonexpansive operator 핊. We say an operator is averaged if it is θ-averaged for
some unspecified θ ∈(0, 1). In other words, taking a weighted average (convex
combination) of 핀and a nonexpansive operator gives an averaged operator. We say
an operator is firmly nonexpansive if it is (1/2)-averaged. See Figure 2.1. When
operators 핋and 핊are averaged, the composition 핋핊is averaged. We prove this as
Theorem 27 later in §13.
Averagedness is the central notion in establishing convergence for many splitting
methods. In fact, Theorems 1, 2, and 3, the main convergence theorems of Part I,
are based on the notion of averagedness.
2.4
Fixed-point iteration
We now discuss the first meta-algorithm of this book: the fixed-point iteration.
Using the fixed-point iteration involves two steps.
First, find a suitable opera-
tor whose fixed points are solutions to a monotone inclusion problem of interest.
Second, show that the iteration converges to a fixed point.


## Page 49

34
2
Monotone operators and base splitting schemes
2.4.1
Fixed points
We say x is a fixed point of a single-valued operator 핋if x = 핋x, and write
Fix 핋= {x | x = 핋x} = (핀−핋)−1(0)
for the set of fixed points of 핋. If 핋is nonexpansive and dom 핋= Rn, then its set
of fixed points is closed and convex. Certainly, Fix 핋can be empty (for example,
핋x = x + 1 on R) or contain many points (for example, 핋x = |x| on R).
Let us show Fix 핋is closed and convex when 핋: Rn →Rn is nonexpansive.
That Fix 핋is closed follows from the fact that 핋−핀is a continuous function. Now
suppose x, y ∈Fix 핋and θ ∈[0, 1]. We will show that z = θx + (1 −θ)y ∈Fix 핋.
Since 핋is nonexpansive, we have
∥핋z −x∥≤∥z −x∥= (1 −θ)∥y −x∥,
and similarly, we have
∥핋z −y∥≤θ∥y −x∥.
So, the triangle inequality
∥x −y∥≤∥핋z −x∥+ ∥핋z −y∥
holds with equality, which means the previous inequalities hold with equality and
핋z is on the line segment between x and y. From ∥핋z −y∥= θ∥y−x∥, we conclude
that 핋z = θx + (1 −θ)y = z. Thus z ∈Fix 핋.
2.4.2
Fixed-point iteration
The algorithm fixed-point iteration (FPI), also called the Picard iteration, is
xk+1 = 핋xk
for k = 0, 1, . . . , where x0 ∈Rn is some starting point and 핋: Rn →Rn is single-
valued. The FPI is used to find a fixed point of 핋. Clearly, the algorithm stays at
a fixed point if it starts at a fixed point. For the sake of brevity, we will usually
omit stating that x0 ∈Rn is some starting point and that k = 0, 1, . . . when we
write an FPI.
In general, an FPI need not converge, even if we assume 핋is nonexpansive.
For example, this is the case when 핋is a rotation about some line or a reflection
through a plane. We provide two conditions that guarantee convergence, although
these are not the only possible approaches.
Contractive operators
Suppose that 핋: Rn →Rn is a contraction with Lipschitz constant L < 1. In this
setting, FPI is also called the contraction mapping algorithm. For x⋆∈Fix 핋, we
have
∥xk −x⋆∥≤L∥xk−1 −x⋆∥≤· · · ≤Lk∥x0 −x⋆∥.


## Page 50

2.4
Fixed-point iteration
35
This is the basis of the classic Banach fixed-point theorem; see Exercise 2.14.
So, when 핋is a contraction, the convergence analysis is very simple. In many
optimization setups, however, a contraction is too much to ask for, and we need an
approach to establish convergence under weaker assumptions.
Averaged operators
Suppose 핋: Rn →Rn is averaged. In this setting, FPI is also called the averaged
or Krasnosel’skiĭ–Mann iteration, and it converges to a solution if one exists.
Theorem 1 Assume 핋: Rn →Rn is θ-averaged with θ ∈(0, 1) and Fix 핋̸ = ∅. Then
xk+1 = 핋xk with any starting point x0 ∈Rn converges to one fixed point, i.e.,
xk →x⋆
for some x⋆∈Fix 핋. The quantities dist(xk, Fix 핋), ∥xk+1 −xk∥, and ∥xk −x⋆∥
for any x⋆∈Fix 핋are monotonically nonincreasing with k. Finally, we have
dist(xk, Fix 핋) →0
and
∥xk+1 −xk∥2 ≤
θ
(k + 1)(1 −θ)dist2(x0, Fix 핋).
To find a fixed point of a nonexpansive operator 핋that is not necessarily aver-
aged, we can perform FPI on the averaged operator (1−θ)핀+θ핋with θ ∈(0, 1). 핋
and (1−θ)핀+θ핋share the same set of fixed points, i.e., Fix 핋= Fix ((1−θ)핀+θ핋).
This ensures the iteration converges, with essentially no additional computational
cost.
Example 2.4 Consider 핋: R2 →R2 defined as
핋x =
−0.5
0
0
1

x =
3
4
−1
0
0
1

+ 1
4
1
0
0
1

x.
This is a (3/4)-averaged operator with Fix 핋= {(0, z) | z ∈R}.
Fix 핋
x0
x1
x2
x3
We can see that FPI with respect to 핋converges to one of the fixed points and that
the limit depends on the starting point x0.


## Page 51

36
2
Monotone operators and base splitting schemes
Proof of Theorem 1. Before we begin the proof in earnest, we summarize the core
idea of the proof. Assume we have nonnegative scalar sequences V 0, V 1, . . . and
S0, S1, . . . . (To clarify, the superscripts denote iteration count, not exponents.)
Say we establish the inequality
V k+1 ≤V k −Sk
for k = 0, 1, 2, . . . . Such an inequality has two useful consequences. The first is
that V k is monotonically nonincreasing, although there is no guarantee that V k
decreases to 0. The second is that Sk →0. To see why, sum both sides from 0 to
k to get
k
X
i=0
Si ≤V 0 −V k+1 ≤V 0.
Taking k →∞gives us
∞
X
i=0
Si ≤V 0 < ∞,
and we say the sequence S0, S1, . . . is summable. Nonnegative summable sequences
converge to 0, so Sk →0. If, furthermore, we can show that S0, S1, . . . is nonin-
creasing, then
(k + 1)Sk ≤
k
X
i=0
Si ≤V 0,
and hence Sk ≤
1
k+1V 0. As an aside, we call V k the Lyapunov function and Sk
the summable term. The proof technique of showing that a Lyapunov function
produces a summable term, which converges to zero, is called the summability
argument.
Stage 1.
Note
∥(1 −θ)x + θy∥2 = (1 −θ)∥x∥2 + θ∥y∥2 −θ(1 −θ)∥x −y∥2,
for all θ ∈R, x, y ∈Rn. Verifying the identity is a matter of expanding both sides.
Write 핋= (1 −θ)핀+ θ핊, where 핊is nonexpansive. Write the FPI as
xk+1 = 핋xk = (1 −θ)xk + θ핊xk.
For any x⋆∈Fix 핋, we use the previous identity to get
∥xk+1 −x⋆∥2 = (1 −θ)∥xk −x⋆∥2 + θ∥핊(xk) −x⋆∥2 −θ(1 −θ)∥핊(xk) −xk∥2
≤(1 −θ)∥xk −x⋆∥2 + θ∥xk −x⋆∥2 −θ(1 −θ)∥핊(xk) −xk∥2
= ∥xk −x⋆∥2
|
{z
}
=V k
−θ(1 −θ)∥핊(xk) −xk∥2
|
{z
}
=Sk
,
(2.4)
where we used nonexpansiveness of 핊in the second line.
We now establish the monotonic decreases. The core inequality (2.4) tells us
∥xk+1 −x⋆∥≤∥xk −x⋆∥


## Page 52

2.4
Fixed-point iteration
37
for any x⋆∈Fix 핋, i.e., the distance of the iterates to any fixed point is mono-
tonically nonincreasing. Minimizing both sides with respect to x⋆∈Fix 핋gives
us
dist(xk+1, Fix 핋) ≤dist(xk, Fix 핋),
i.e., the distance of the iterates to the set of fixed points is monotonically non-
increasing. As another aside, an algorithm is said to be Fejér monotone if the
distance of the iterates to the solution set is monotonically nonincreasing.
We call 핋(xk) −xk = xk+1 −xk the fixed-point residual. If 핋(xk) −xk = 0, the
FPI is at a fixed point, and the iteration stops, so one can use ∥핋(xk) −xk∥as a
measure of progress of the FPI. Since 핋is nonexpansive, we have
∥xk+1 −xk∥= ∥핋xk −핋xk−1∥≤∥xk −xk−1∥,
i.e., the magnitude of the fixed-point residual is monotonically nonincreasing.
Using the monotonic decrease of ∥xk+1 −xk∥, we obtain a rate of convergence
for ∥xk+1 −xk∥→0. Summing the inequality (2.4) from 0 to k gives us
∥xk+1 −x⋆∥2 ≤∥x0 −x⋆∥2 −1 −θ
θ
k
X
j=0
∥핋xj −xj∥2.
Reorganizing, we get
k
X
j=0
∥핋xj −xj∥2 ≤
θ
1 −θ∥x0 −x⋆∥2 −
θ
1 −θ∥xk+1 −x⋆∥2.
With the monotonic decrease of ∥xk+1 −xk∥we get
(k + 1)∥xk+1 −xk∥2 ≤
k
X
j=0
∥xj+1 −xj∥2 ≤
θ
1 −θ∥x0 −x⋆∥2,
and we conclude that
∥xk+1 −xk∥2 ≤
θ
(k + 1)(1 −θ)∥x0 −x⋆∥2.
Minimizing the right-hand side with respect to x⋆∈Fix 핋, we get
∥xk+1 −xk∥2 ≤
θ
(k + 1)(1 −θ)dist2(x0, Fix 핋).
Stage 2.
We now show xk →x⋆for some x⋆∈Fix 핋. Consider any ˜x⋆∈Fix 핋.
Then (2.4) tells us that x0, x1, . . . lie within the compact set {x | ∥x −˜x⋆∥≤∥x0 −
˜x⋆∥}, and x0, x1, . . . has an accumulation point x⋆. Let xkj be a subsequence such
that xkj →x⋆. Then (핋−핀)(xk) →0 implies (핋−핀)(xkj) →0. Since 핋−핀is
continuous, xkj →x⋆and (핋−핀)(xkj) →0 implies (핋−핀)(x⋆) = 0. In other
words, x⋆∈Fix 핋. Finally, applying (2.4) to this accumulation point x⋆∈Fix 핋,
we conclude that ∥xk −x⋆∥monotonically decreases to 0, i.e., the entire sequence
converges to x⋆.


## Page 53

38
2
Monotone operators and base splitting schemes
Termination criterion
Although we avoid the discussion of termination criterion throughout this book
for the sake of simplicity, detecting when an iterate is a sufficiently accurate ap-
proximation of the solution is essential for a practical iterative method. We simply
point out that ∥xk+1 −xk∥< ε for some small ε > 0 can generally be used as
a termination criterion. Specific setups may have other termination criteria that
better capture the particular goals of the setup.
2.4.3
Methods
Gradient descent
Consider the problem
minimize
x∈Rn
f(x).
Assume f is CCP and differentiable. Then x is a solution if and only if
0 = ∇f(x)
⇔
x = (핀−α∇f)(x)
for any nonzero α ∈R. In other words, x is a solution if and only if it is a fixed
point of the operator 핀−α∇f.
The FPI for this setup is
xk+1 = xk −α∇f(xk).
This algorithm is called the gradient method or gradient descent, and α is called
the stepsize.
Now assume f is L-smooth. By the cocoercivity inequality,
∥(핀−(2/L)∇f)x −(핀−(2/L)∇f)y∥2
= ∥x −y∥2 −4
L

⟨x −y, ∇f(x) −∇f(y)⟩−1
L∥∇f(x) −∇f(y)∥2

≤∥x −y∥2.
Therefore, 핀−α∇f is averaged for α ∈(0, 2/L) since
핀−α∇f = (1 −θ)핀+ θ(핀−(2/L)∇f),
where θ = αL/2 < 1. Consequently, xk →x⋆for some solution x⋆, if one exists,
with rate
∥∇f(xk)∥2 = O(1/k),
for any
α ∈(0, 2/L).
(2.5)
If we furthermore assume f is strongly convex, we can show the iteration is a
contraction.


## Page 54

2.4
Fixed-point iteration
39
Forward step method
Consider the problem
find
x∈Rn
0 = 픽(x),
where 픽: Rn →Rn.
By the same argument as for gradient descent, x is a solution if and only if it
is a fixed point of 핀−α픽for any nonzero α ∈R. The FPI for this setup is
xk+1 = xk −α픽xk,
which we call the forward step method.
The forward step method converges if 픽is β-cocoercive and α ∈(0, 2β). The
forward step iteration is a contraction for small enough α > 0 if 픽is strongly
monotone and Lipschitz.
However, the method does not necessarily converge if 픽is merely monotone
and Lipschitz. The operator
픽(x, y) =
 0
1
−1
0
 x
y

is such an example, since the 2 × 2 matrix representing 핀−α픽has singular values
strictly greater than 1 for any α̸ = 0.
(This operator arises as, say, the KKT
operator of the problem of minimizing x subject to x = 0.) The scaled relative
graphs of §13 will provide the geometric intuition of this counterexample.
Dual ascent
Consider the primal-dual problem pair (1.6) and (1.7),
minimize
x∈Rn
f(x)
subject to
Ax = b,
maximize
u∈Rm
−f ∗(−A⊺u) −b⊺u,
generated by the Lagrangian (1.5)
L(x, u) = f(x) + ⟨u, Ax −b⟩.
Define g(u) = f ∗(−A⊺u) + b⊺u. By the discussion of §1.3.8, if f is µ-strongly
convex, then f ∗is differentiable and ∇f ∗is (1/µ)-Lipschitz. By the discussion of
§2.2.2,
∇g(u) = −A∇f ∗(−A⊺u) + b
is Lipschitz with parameters σ2
max(A)/µ.
Using (2.2), write the gradient method applied to g, the FPI on 핀−α∇g, as
xk+1 = argmin
x
L(x, uk)
uk+1 = uk + α(Axk+1 −b).
The first step is minimizing the Lagrangian, and the second is a multiplier update.
This method is called the Uzawa method or dual ascent. If f is µ-strongly convex,
total duality holds, and 0 < α < 2µ/σ2
max(A), then xk →x⋆and uk →u⋆. See
Exercise 2.17.


## Page 55

40
2
Monotone operators and base splitting schemes
2.5
Resolvents
The resolvent of an operator 픸is defined as
핁픸= (핀+ 픸)−1.
The reflected resolvent, also called the Cayley operator or the reflection operator,
of 픸is defined as
ℝ픸= 2핁픸−핀.
Often, we will use 핁α픸and ℝα픸with α > 0. If 픸is maximal monotone, ℝ픸is a
nonexpansive (single-valued) with dom ℝ픸= Rn, and 핁픸is a (1/2)-averaged with
dom 핁픸= Rn.
Let us prove nonexpansiveness. Assume we have (x, u), (y, v) ∈핁픸. By defini-
tion of resolvents, we have
x ∈u + 픸u,
y ∈v + 픸v.
By monotonicity of 픸,
⟨(x −u) −(y −v), u −v⟩≥0
and
∥(2u −x) −(2v −y)∥2 = ∥x −y∥2 −4⟨(x −u) −(y −v), u −v⟩
≤∥x −y∥2.
This proves ℝ픸is nonexpansive and therefore single-valued and 핁픸= (1/2)핀+
(1/2)ℝ픸is (1/2)-averaged.
The Minty surjectivity theorem states that dom 핁픸= Rn when 픸is maximal
monotone. This result is easy to intuitively see in 1D but is nontrivial in higher
dimensions. We prove this in §10.
Zero set of a maximal monotone operator
Using resolvents, we can quickly show Zer 픸is a closed convex set when 픸is
maximal monotone. Since
0 ∈픸x
⇔
x ∈x + 픸x
⇔
핁픸x = x,
we have Zer 픸= Fix 핁픸. Since 핁픸is nonexpansive, Fix 핁픸is a closed convex set.
Note that this proof relies on maximality through the condition dom 핁픸= Rn.
Example 2.5
When 픸is a monotone linear operator represented by a symmetric
matrix, it is easier to see why 핁픸and ℝ픸are nonexpansive.
In this case, 픸has
eigenvalues in [0, ∞) and 핁픸= (핀+ 픸)−1 has eigenvalues in (0, 1].
The reflected
resolvent,
ℝ픸= 2핁픸−핀= (핀−픸)(핀+ 픸)−1 = (핀+ 픸)−1(핀−픸),
also called the Cayley transform of 픸, has eigenvalues in (−1, 1].


## Page 56

2.5
Resolvents
41
Example 2.6
Let z ∈C be a complex number.
We can identify z with a linear
operator from C to C defined by multiplication, i.e., we can view z as the operator
that maps x 7→zx for any x ∈C. We equip the set of complex numbers with the
inner product ⟨x, y⟩= Re xy for any x, y ∈C, where y is the complex conjugate of y.
Then z ∈C is a monotone operator if and only if Re z ≥0.
{z | Re z ≥0}

(1 + z)−1 | Re z ≥0
	
1
So a monotone z is a complex number on the right half-plane, and its resolvent
(1 + z)−1 is a complex number within the disk with center 1/2 and radius 1/2 except
for the origin.
2.5.1
Examples
Subdifferential
When f is CCP and α > 0, we have
핁α∂f = Proxαf.
This follows from
z = (I + α∂f)−1(x)
⇔
z + α∂f(z) ∋x
⇔
0 ∈∂z

αf(z) + 1
2∥z −x∥2

⇔
z = argmin
z

αf(z) + 1
2∥z −x∥2

⇔
z = Proxαf(x).
Subdifferential of conjugate
Let g(u) = f ∗(A⊺u), and assume f is CCP and ri dom f ∗∩R(A⊺)̸ = ∅. Then
v = Proxαg(u)
⇔
x ∈argminx

f(x) −⟨u, Ax⟩+ α
2 ∥Ax∥2	
v = u −αAx.
(2.6)


## Page 57

42
2
Monotone operators and base splitting schemes
This follows from
v = (I + α∂g)−1(u)
⇔
v + αA∂f ∗(A⊺v) ∋u
⇔
v + αAx = u, x ∈∂f ∗(A⊺v)
⇔
v = u −αAx, ∂f(x) ∋A⊺v
⇔
v = u −αAx, ∂f(x) ∋A⊺(u −αAx)
⇔
v = u −αAx, x ∈argmin
x
n
f(x) −⟨u, Ax⟩+ α
2 ∥Ax∥2o
.
Projection
Let C ⊂Rn be a nonempty closed convex set.
Remember from §1 that δC is
the indicator function of C, ℕC is the normal cone operator of C, and ΠC is
the projection onto C.
These satisfy the following properties: δC = αδC and
ℕC = αℕC for any α > 0; ∂δC = ℕC; and 핁ℕC = ProxδC = ΠC.
KKT operator for linearly constrained problems
Consider the Lagrangian
L(x, u) = f(x) + ⟨u, Ax −b⟩,
which generates the primal problem
minimize
x∈Rn
f(x)
subject to
Ax = b.
We can compute its resolvent with
핁α∂L(x, u) = (y, v)
⇔
y = argminz

Lα(z, u) +
1
2α∥z −x∥2	
v = u + α(Ay −b),
(2.7)
where Lα = f(x)+⟨u, Ax−b⟩+ α
2 ∥Ax−b∥2 is the augmented Lagrangian of (1.11).
Let us show this. For any α > 0, we have
핁α∂L(x, u) = (y, v)
⇔

x
u

∈

y
v

+ α

∂f(y) + A⊺v
b −Ay

⇔
x
u

∈α
∂f(y)
b

+

I
αA⊺
−αA
I
 y
v

.
We left-multiply the invertible matrix
I
−αA⊺
0
I

to get
⇔

x −αA⊺u
u

∈α

∂f(y) −αA⊺b
b

+

I + α2A⊺A
0
−αA
I
 
y
v

.


## Page 58

2.5
Resolvents
43
We call this the Gaussian elimination technique and discuss it in more detail in
§3.4. Now that the first line of the inclusion is independent of v, we can compute
y first and then compute v. Reorganizing, we get
0 ∈∂f(y) + A⊺u + αA⊺(Ay −b) + (1/α)(y −x)
v = u + α(Ay −b),
and we have the formula
y = argmin
z

f(z) + ⟨u, Az −b⟩+ α
2 ∥Az −b∥2 + 1
2α∥z −x∥2

v = u + α(Ay −b).
2.5.2
Basic identities
Resolvent identities
If 픸is maximal monotone, α > 0, and 픹(x) = 픸(x) + t, then
핁α픹(u) = 핁α픸(u −αt).
(2.8)
This follows from
핁α픹u = v
⇔
u ∈v + α픹v
⇔
u −αt ∈v + α픸v
⇔
v = 핁α픸(u −αt).
With similar calculations, one can show that if 픸is maximal monotone, α > 0,
and 픹(x) = 픸(x −t), then
핁α픹(u) = 핁α픸(u −t) + t,
(2.9)
and if 픸is maximal monotone, α > 0, and 픹(x) = −픸(t −x), then
핁α픹(u) = t −핁α픸(t −u).
(2.10)
The inverse resolvent identity states
핁α−1픸(x) + α−1핁α픸−1(αx) = x,
(2.11)
for maximal monotone 픸and α > 0. This follows from
x −핁α−1픸x = y
⇔
x ∈x −y + α−1픸(x −y)
⇔
αy ∈픸(x −y)
⇔
픸−1(αy) ∋x −y
⇔
(핀+ α픸−1)(αy) ∋αx
⇔
y = (1/α)핁α픸−1(αx).


## Page 59

44
2
Monotone operators and base splitting schemes
When α = 1, we get the further elegant formula
핁픸+ 핁픸−1 = 핀.
The Moreau identity, a special case, states that for any CCP f,
Proxf + Proxf ∗= 핀,
or more generally,
Proxα−1f(x) + α−1Proxαf ∗(αx) = x.
(2.12)
An important practical consequence of the Moreau identity is that Proxαf and
Proxαf ∗require essentially the same computational cost. In other words, if you
can compute Proxαf, then you can compute Proxαf ∗, and vice versa.
Reflected resolvent identities
If 픸is maximal monotone and single-valued and α > 0, we have
ℝα픸= (핀−α픸)(핀+ α픸)−1.
This follows from
ℝα픸= 2(핀+ α픸)−1 −핀
= 2(핀+ α픸)−1 −(핀+ α픸)(핀+ α픸)−1
= (핀−α픸)(핀+ α픸)−1,
where we used the result of Exercise 2.1 in the second equality.
If 픸is maximal monotone (but not necessarily single-valued) and α > 0, we
have
ℝα픸(핀+ α픸) = 핀−α픸.
(2.13)
Let us prove this. Since (핀+ α픸)−1 is single-valued, for any x ∈dom 픸we have
ℝα픸(핀+ α픸)(x) = 2(핀+ α픸)−1(핀+ α픸)(x) −(핀+ α픸)(x)
= 2핀(x) −(핀+ α픸)(x)
= (핀−α픸)(x),
where we used the result of Exercise 2.1 in the second equality. For any x /∈dom 픸,
both sides are empty sets.
2.6
Proximal point method
Consider the problem
find
x∈Rn
0 ∈픸x,
where 픸is maximal monotone. This problem is equivalent to finding a fixed point
of 핁α픸, since Zer 픸= Fix 핁α픸for any α > 0. The FPI
xk+1 = 핁α픸(xk),
called the proximal point method (PPM) or proximal minimization, converges to a
solution if one exists, since 핁α픸is averaged.


## Page 60

2.7
Operator splitting
45
2.6.1
Methods of multipliers
Consider the primal-dual problem pair,
minimize
x∈Rn
f(x)
subject to
Ax = b,
maximize
u∈Rm
−f ∗(−A⊺u) −b⊺u,
of (1.6) and (1.7) generated by the Lagrangian L(x, u) = f(x) + ⟨u, Ax −b⟩. The
associated augmented Lagrangian discussed in Example 1.11 is
Lα(x, u) = f(x) + ⟨u, Ax −b⟩+ α
2 ∥Ax −b∥2.
Method of multipliers
Assume R(A⊺)∩ri dom f ∗̸ = ∅. Write g(u) = f ∗(−A⊺u)+b⊺u for the dual function.
Using (2.6) and (2.8), we can write the FPI uk+1 = 핁α∂g(uk) with α > 0 as
xk+1 ∈argmin
x
Lα(x, uk)
uk+1 = uk + α(Axk+1 −b),
which is called the method of multipliers, also known as the augmented Lagrangian
method or ALM. The first step is minimizing the augmented Lagrangian, and the
second is a multiplier update.
If a dual solution exists and α > 0, then uk →u⋆. If we further assume f is
strictly convex, we can show xk →x⋆. See Exercises 2.18 and 10.4.
Proximal method of multipliers
Using (2.7), we can write the FPI (xk+1, uk+1) = 핁α∂L(xk, uk) with α > 0 as
xk+1 = argmin
x

Lα(x, uk) + 1
2α∥x −xk∥2

uk+1 = uk + α(Axk+1 −b),
which is called the proximal method of multipliers, also the proximal augmented
Lagrangian method. The first step is minimizing the augmented Lagrangian with
an additional proximal term, and the second is a multiplier update. If total duality
holds and α > 0, then xk →x⋆and uk →u⋆.
The proximal method of multipliers becomes useful when it is combined with
the linearization technique. We discuss this in §3.5.
2.7
Operator splitting
Consider the monotone inclusion problems of finding an x ∈Zer (픸+ 픹) or x ∈
Zer (픸+ 픹+ ℂ), where 픸, 픹, and ℂare maximal monotone. In this section, we


## Page 61

46
2
Monotone operators and base splitting schemes
present a few base splitting schemes, which transform these monotone inclusion
problems into fixed-point equations with averaged operators constructed from 픸,
픹, ℂ, and their resolvents.
The key technique is to formulate a given optimization problem as a monotone
inclusion problem, apply one of the base splitting schemes, and use the fixed-
point iteration discussed in §2.4.2, or the randomized coordinate or asynchronous
variants of §5 and §6. The main message of Part I of this book is that a wide range
of methods can be derived and analyzed through this unified approach.
2.7.1
Base splitting schemes
Forward-backward and backward-forward splitting
Consider the problem
find
x∈Rn
0 ∈(픸+ 픹)x,
where 픸and 픹are maximal monotone and 픸is single-valued. Then for any α > 0,
we have
0 ∈(픸+ 픹)x
⇔
0 ∈(핀+ α픹)x −(핀−α픸)x
⇔
(핀+ α픹)x ∋(핀−α픸)x
⇔
x = 핁α픹(핀−α픸)x.
So, x is a solution if and only if it is a fixed point of 핁α픹(핀−α픸). This splitting
is called forward-backward splitting (FBS).
Assume 픸is β-cocoercive and α ∈(0, 2β). Then the forward step 핀−α픸and
the backward step (핀+ α픹)−1 are averaged. So, the composition 핁α픹(핀−α픸) is an
averaged operator.
The FPI with FBS
xk+1 = 핁α픹(xk −α픸xk)
converges if α ∈(0, 2β) and Zer (픸+ 픹)̸ = ∅.
We can also consider a similar splitting with a permuted order:
0 ∈(픸+ 픹)x
⇔
(핀+ α픹)x ∋(핀−α픸)x
⇔
z = (핀−α픸)x, z ∈(핀+ α픹)x
⇔
z = (핀−α픸)x, 핁α픹z = x
⇔
z = (핀−α픸)핁α픹z, 핁α픹z = x.
So, x is a solution if and only if there is a z ∈Fix (핀−α픸)핁α픹and x = 핁α픹z. This
splitting is called backward-forward splitting (BFS).
The FPI with BFS
xk+1 = 핁α픹zk
zk+1 = xk+1 −α픸xk+1
converges if α ∈(0, 2β) and Zer (픸+ 픹)̸ = ∅.


## Page 62

2.7
Operator splitting
47
Since BFS is FBS with the order permuted, BFS may seem like an unnecessary
complication. In fact, the FPIs with FBS and BFS have the same iterates if the
starting points x0 for FBS and z0 for BFS are matched in the sense that x0 = 핁α픹z0.
However, we will later see that BFS can be more natural to work with when using
the randomized or asynchronous coordinate fixed-point iterations of §5 and §6.
Peaceman–Rachford and Douglas–Rachford splitting
Consider the problem
find
x∈Rn
0 ∈(픸+ 픹)x,
where 픸and 픹are maximal monotone.
For any α > 0, we have
0 ∈(픸+ 픹)x
⇔
0 ∈(핀+ α픸)x −(핀−α픹)x
⇔
0 ∈(핀+ α픸)x −ℝα픹(핀+ α픹)x
⇔
0 ∈(핀+ α픸)x −ℝα픹z, z ∈(핀+ α픹)x
⇔
ℝα픹z ∈(핀+ α픸)핁α픹z, x = 핁α픹z
⇔
핁α픸ℝα픹z = 핁α픹z, x = 핁α픹z
⇔
ℝα픸ℝα픹z = z, x = 핁α픹z,
where we have used (2.13).
So, x is a solution if and only if there is a z ∈
Fix ℝα픸ℝα픹and x = 핁α픹z. This splitting is called Peaceman–Rachford splitting
(PRS).
Since the operator ℝα픸ℝα픹is merely nonexpansive, the FPI with PRS
zk+1 = ℝα픸ℝα픹(zk)
(2.14)
is not guaranteed to converge. See Exercise 2.27.
To ensure convergence, we average. For any α > 0, we have
0 ∈(픸+ 픹)x
⇔
1
2핀+ 1
2ℝα픸ℝα픹

(z) = z, x = 핁α픹(z).
This splitting is called Douglas–Rachford splitting (DRS).
The FPI with DRS
xk+1/2 = 핁α픹(zk)
xk+1 = 핁α픸(2xk+1/2 −zk)
zk+1 = zk + xk+1 −xk+1/2
converges for any α > 0 if Zer (픸+ 픹)̸ = ∅. See Exercise 2.26.
We can think of the xk+1/2- and xk+1-iterates as estimates of a solution with
different properties.
For example, if 핁α픹is a projection onto a constraint set,
xk+1/2-iterates satisfy these constraints exactly.


## Page 63

48
2
Monotone operators and base splitting schemes
Davis–Yin splitting
Consider the problem
find
x∈Rn
0 ∈(픸+ 픹+ ℂ)x,
where 픸, 픹, and ℂare maximal monotone, and ℂis single-valued.
Then for any α > 0, we have
0 ∈(픸+ 픹+ ℂ)x
⇔
0 ∈(핀+ α픸)x −(핀−α픹)x + αℂx
⇔
0 ∈(핀+ α픸)x −ℝα픹(핀+ α픹)x + αℂx
⇔
0 ∈(핀+ α픸)x −ℝα픹z + αℂx, z ∈(핀+ α픹)x
⇔
(ℝα픹−αℂ핁α픹)z ∈(핀+ α픸)핁α픹z, x = 핁α픹z
⇔
핁α픸(ℝα픹−αℂ핁α픹)z = 핁α픹z, x = 핁α픹z
⇔
(ℝα픸(ℝα픹−αℂ핁α픹) −αℂ핁α픹)z = z, x = 핁α픹z
⇔
((1/2)핀+ (1/2)핋)z = z, x = 핁α픹z,
핋= ℝα픸(ℝα픹−αℂ핁α픹) −αℂ핁α픹.
So x is a solution if and only if there is a z ∈Fix ((1/2)핀+ (1/2)핋) and x = 핁α픹z.
This splitting is called Davis–Yin splitting (DYS). We can also write
(1/2)핀+ (1/2)핋= 핀−핁α픹+ 핁α픸(ℝα픹−αℂ핁α픹).
Assume ℂis β-cocoercive and α ∈(0, 2β), then (1/2)핀+ (1/2)핋is averaged.
We prove this in §13 as Theorem 28. 핋itself may not be nonexpansive. The FPI
with DYS
xk+1/2 = 핁α픹(zk)
xk+1 = 핁α픸(2xk+1/2 −zk −αℂxk+1/2)
zk+1 = zk + xk+1 −xk+1/2
converges for α ∈(0, 2β) if Zer (픸+ 픹+ ℂ)̸ = ∅. Note that DYS reduces to BFS
when 픸= 0, to FBS when 픹= 0, and to DRS when ℂ= 0.
2.7.2
Splitting for convex optimization and total duality
In §3, we combine the base splittings with various techniques to derive a wide
range of methods. In this section, we directly apply the base splittings to convex
optimization problems as is.
Proximal gradient method
Consider the problem
minimize
x∈Rn
f(x) + g(x),
where f and g are CCP functions on Rn and f is differentiable. Then x is a solution
if and only if x ∈Zer (∇f + ∂g).


## Page 64

2.7
Operator splitting
49
The FPI with FBS is
xk+1 = Proxαg(xk −α∇f(xk)),
which is also called the proximal gradient method. Assume a primal solution exists,
f is L-smooth, and α ∈(0, 2/L). Then xk →x⋆.
We can write the proximal gradient method equivalently as
xk+1 = argmin
x

f(xk) + ⟨∇f(xk), x −xk⟩+ g(x) + 1
2α∥x −xk∥2
2

.
So, the proximal gradient method uses a first-order approximation of f about xk.
When g = δC for some nonempty convex set C, the proximal gradient method
reduces to the projected gradient method:
xk+1 = ΠC(xk −α∇f(xk)).
DRS for convex optimization and total duality
Consider the primal-dual problem pair
minimize
x∈Rn
f(x) + g(x)
(2.15)
and
maximize
u∈Rn
−f ∗(−u) −g∗(u)
(2.16)
generated by the Lagrangian
L(x, u) = f(x) + ⟨x, u⟩−g∗(u),
(2.17)
where f and g are CCP functions on Rn.
As we soon prove, the primal problem is equivalent to
find
x∈Rn
0 ∈(∂f + ∂g)x
when total duality holds. The FPI with DRS is
xk+1/2 = Proxαg(zk)
xk+1 = Proxαf(2xk+1/2 −zk)
(2.18)
zk+1 = zk + xk+1 −xk+1/2.
Assume total duality holds and α > 0.
Then xk →x⋆and xk+1/2 →x⋆.
In
§9, we furthermore show that fixed points are of the form z⋆= x⋆+ αu⋆. So,
zk →x⋆+ αu⋆.
The FPI with DRS requires f and g to be CCP, and the method converges for
all α > 0. In contrast, the proximal gradient method furthermore requires f to
be L-smooth, and the parameter α must lie within a specific range. DRS is useful
when evaluating Proxαf and Proxαg is easy but evaluating Proxα(f+g) is not. The


## Page 65

50
2
Monotone operators and base splitting schemes
proximal gradient method is useful when evaluating ∇f and Proxαg is easy. The
proximal point method is useful when evaluating Proxα(f+g) is easy.
Note that although the primal problem (2.15) is symmetric in f and g, the dual
problem (2.16) is not. Swapping the roles of f and g changes the sign of the dual
variable. The algorithm (2.18) is also not symmetric in f and g, and swapping the
roles of f and g changes the sign of the dual variable in zk →x⋆+ αu⋆.
DYS for convex optimization and total duality
Consider the primal-dual problem pair
minimize
x∈Rn
f(x) + g(x) + h(x)
and
maximize
u∈Rn
−(f + h)∗(−u) −g∗(u)
generated by the Lagrangian
L(x, u) = f(x) + h(x) + ⟨x, u⟩−g∗(u).
The FPI with DYS is
xk+1/2 = Proxαg(zk)
xk+1 = Proxαf(2xk+1/2 −zk −α∇h(xk+1/2))
zk+1 = zk + xk+1 −xk+1/2.
Assume total duality holds, h is L-smooth, and α ∈(0, 2/L).
Then xk →x⋆
and xk+1/2 →x⋆. In §9, we furthermore show that fixed points are of the form
z⋆= x⋆+ αu⋆. So, zk →x⋆+ αu⋆.
Necessity and sufficiency of total duality
The following equivalence summarizes the role of total duality in splitting methods:
argmin(f+g) = Zer (∂f+∂g)̸ = ∅
⇔
total duality holds between (2.15) and (2.16).
Therefore, we can write
minimize
x∈Rn
f(x) + g(x)
⇔
find
x∈Rn
0 ∈(∂f + ∂g)(x)
when total duality holds. This fact explains why total duality is required for the
convergence of so many operator splitting methods.
Let us see why. First, assume that total duality holds. Then x⋆∈argmin(f +g)
if and only if (x⋆, u⋆) is a saddle point of
L(x, u) = f(x) + ⟨x, u⟩−g∗(u)
for some u⋆∈Rn, and
(x⋆, u⋆) is a saddle point of L
⇔
0 ∈∂L(x⋆, u⋆)
⇔
0 ∈∂xL(x⋆, u⋆), 0 ∈∂u(−L)(x⋆, u⋆)
⇔
−u⋆∈∂f(x⋆), u⋆∈∂g(x⋆)
⇔
0 ∈(∂f + ∂g)(x⋆).


## Page 66

2.7
Operator splitting
51
We conclude that argmin(f + g) = Zer (∂f + ∂g)̸ = ∅.
Next, assume argmin(f +g) = Zer (∂f +∂g)̸ = ∅. Then any x⋆∈argmin(f +g)
satisfies 0 ∈(∂f + ∂g)(x⋆). By a similar chain of arguments, (x⋆, u⋆) is a saddle
point of L for some u⋆∈Rn, and we conclude that total duality holds.
2.7.3
Discussion
Fixed-point encoding
A fixed-point encoding establishes a correspondence between solutions of a mono-
tone inclusion problem and fixed points of a related operator. The splittings we
discussed are fixed-point encodings.
Upon reading §2.7.1, one may ask why there is no “forward-forward” splitting.
A “forward-forward splitting” of the form 핀−α(픸+픹) is an instance of the forward-
step method. A “forward-forward splitting” of the form (핀−α픸)(핀−β픹) would
not be a valid fixed-point encoding; i.e., we cannot recover a zero of A + B from a
fixed point of (핀−α픸)(핀−β픹). Likewise, a “backward-backward splitting” of the
form 핁α픸핁α픹is not a valid fixed-point encoding. See Exercise 2.28.
Why use the resolvent?
The splittings we discuss use resolvents or direct evaluations of single-valued op-
erators. Why do we not use other operators such as (핀−α픸)−1? One reason is
computational convenience. The resolvent is often easy to evaluate for many in-
teresting operators, while evaluating something like (핀−α∂f)−1 is often difficult.
Another reason is that only single-valued operators are, in a sense, algorithmi-
cally actionable. On a computer, we can compute and store a vector in Rn, but
we cannot store a subset of Rn in most cases. While multi-valued operators are a
useful mathematical concept, single-valued operators, such as resolvents, are more
algorithmically useful.
The role of maximality
An FPI xk+1 = 핋xk becomes undefined if its iterates ever escape the domain of 핋.
In §2.4.2, we implicitly assumed dom 핋= Rn through stating 핋: Rn →Rn. When
the operators are maximal monotone, FPIs defined with resolvents do not run into
this issue.
So, we assume maximality out of theoretical necessity, but in practice the non-
maximal monotone operators, such as the gradient operator of a nonconvex func-
tion, are usually ones we cannot efficiently compute the resolvent for anyway. In
other words, there is little need to consider resolvents of non-maximal monotone
operators, theoretically or practically.


## Page 67

52
2
Monotone operators and base splitting schemes
Computational efficiency
These base splitting methods are useful when the operators used in the splitting
are efficient to compute. For example, although the convergence of DRS iteration
zk+1 =
1
2핀+ 1
2ℝα픸ℝα픹

zk
does not depend on the value of α, it is most useful when ℝα픸and ℝα픹can be
computed efficiently.
For a given optimization problem, there is often more than one applicable
method. The trick is to find a method using computationally efficient split com-
ponents.
2.7.4
Methods
LASSO and ISTA
Consider the problem
minimize
x∈Rn
1
2∥Ax −b∥2 + λ∥x∥1,
for A ∈Rm×n, b ∈Rm, and λ > 0. This particular optimization problem is called
LASSO. Let S(x; κ) be the soft-thresholding operator of Example 1.12.
The FPI with DRS
xk+1/2 = (I + αA⊺A)−1(zk + αA⊺b)
xk+1 = S(2xk+1/2 −zk; αλ)
zk+1 = zk + xk+1 −xk+1/2
converges for any α > 0.
The FPI with FBS
xk+1 = S(xk −αA⊺(Axk −b); αλ)
converges for 0 < α < 2/λmax(A⊺A). This particular instance of the proximal
gradient method is called the Iterative Shrinkage-Thresholding Algorithm (ISTA).
Note that DRS uses the matrix inverse (I + αA⊺A)−1, while FBS does not.
When m and n are large, computing the matrix inverse can be prohibitively expen-
sive. Therefore, FBS is the more computationally effective splitting for large-scale
LASSO problems.
Consensus technique
Consider the problem
minimize
x∈Rn
m
X
i=1
gi(x),


## Page 68

2.7
Operator splitting
53
where g1, . . . , gm are CCP functions on Rn. This problem is equivalent to
minimize
x∈Rnm
m
X
i=1
gi(xi)
subject to
x ∈C,
where x = (x1, . . . , xm) and
C = {(x1, . . . , xm) ∈Rnm | x1 = · · · = xm}
(2.19)
is the consensus set. In turn, this problem is equivalent to
find
x∈Rnm
0 ∈


∂g1(x1)
...
∂gm(xm)

+ ℕC(x),
assuming Tm
i=1 int dom gi̸ = ∅.
The projection onto the consensus set is simple averaging:
ΠCx = x = (x, x, . . . , x),
x = 1
m
m
X
i=1
xi.
Define zk = ΠCzk. The FPI with DRS for this setup
xk+1
i
= Proxαgi(2zk −zk
i )
for i = 1, . . . , m,
zk+1 = zk + xk+1 −zk
converges for any α > 0, if Tm
i=1 int dom gi̸ = ∅and a solution exists. Since Proxαgi
for i = 1, . . . , m can be evaluated independently, this method is well-suited for
parallel and distributed computing, which we discuss in §4.2.1 and §11.1.
The use of the consensus set (2.19) is called the consensus technique and it can
more generally solve
find
x∈Rn
0 ∈
m
X
i=1
픸ix,
where 픸1, . . . , 픸m are maximal monotone. See Exercise 2.36.
Forward-Douglas–Rachford
Consider the problem
minimize
x∈Rn
m
X
i=1
(fi(x) + gi(x)),
where g1, . . . , gm are CCP and f1, . . . , fm are L-smooth. With the consensus tech-
nique, we can recast the problem into
minimize
x∈Rnm
m
X
i=1
fi(xi) +
m
X
i=1
gi(xi)
subject to
x ∈C,


## Page 69

54
2
Monotone operators and base splitting schemes
where we use the same notation as we did for consensus optimization.
The FPI with DYS for this setup
xk+1
i
= Proxαgi(2zk −zk
i −α∇fi(zk))
for i = 1, . . . , m,
zk+1 = zk + xk+1 −zk,
is called generalized forward-backward or forward-Douglas–Rachford. This method
converges if total duality holds, Tm
i=1 int dom gi̸ = ∅, and α ∈(0, 2/L).
2.8
Variable metric methods
In the theory we have developed so far, the Euclidean norm plays a special role.
In the definition of the proximal operator
Proxf(x) = argmin
z

f(z) + 1
2∥z −x∥2

,
the (1/2)∥z −x∥2 term, called the proximal term, is defined with the Euclidean
norm.
Theorem 1 is stated in terms of the Euclidean norm.
Variable metric
methods generalize many of the notions we have discussed so far with the M-norm.
One reason to consider this generalization is preconditioning. A good choice
of the norm ∥· ∥M can reduce the number of iterations needed for convergence.
Variable metric methods are also useful when an operator 픸has structure and a
well-chosen M cancels certain terms to make (M + 픸)−1 easy to evaluate. We
explore this technique thoroughly in §3.3.
Despite the name variable metric methods, the generalization works only with
M-norms since they are the norms induced by the inner product ⟨x, y⟩M = x⊺My.
The analysis of this section does not extend to other metrics, such as the ℓ1-norm.
Variable metric proximal point method
Let 픸be maximal monotone and M ≻0. Then M −1/2픸M −1/2 is maximal mono-
tone and the proximal point method
yk+1 = (핀+ M −1/2픸M −1/2)−1yk
converges.
With the change of variables xk = M −1/2yk, we get
(핀+ M −1/2픸M −1/2)yk+1 ∋yk
(핀+ M −1픸)xk+1 ∋xk.
This gives us
xk+1 = 핁M −1픸xk
= (M + 픸)−1Mxk.


## Page 70

2.8
Variable metric methods
55
We call this the variable metric PPM. The iterates xk inherit the convergence prop-
erties of yk. For example, the fact that ∥yk −y⋆∥is monotonically nonincreasing
translates to the fact that ∥xk −x⋆∥M is monotonically nonincreasing. Likewise,
∥xk+1 −xk∥M →0 monotonically at rate O(1/k).
When 픸= ∂f, then
핁M −1∂f(x) = argmin
z∈Rd

f(z) + 1
2∥z −x∥2
M

.
We can interpret the variable metric PPM as PPM performed with the norm ∥·∥M
instead of the Euclidean norm.
Variable metric forward-backward splitting
Let 픸and 픹be maximal monotone and let 픸be single-valued. Then with the
same reasoning, we can use a change of variables to write the FBS FPI with respect
to M −1/2픸M −1/2 and M −1/2픹M −1/2 as
xk+1 = (M + 픹)−1(M −픸)xk
= 핁M −1픹(핀−M −1픸)xk.
We call this splitting variable metric FBS. This method converges if 핀−M −1/2픸M −1/2
is averaged.
When 픸= ∇f and 픹= ∂g, then
핁M −1∂g(핀−M −1∇f)x = argmin
z∈Rd

g(z) + ⟨∇f(x), z⟩+ 1
2∥z −x∥2
M

.
We can interpret the variable metric FBS as the proximal gradient method per-
formed with the norm ∥· ∥M, instead of the Euclidean norm.
If 픸is β-cocoercive, then M −1/2픸M −1/2 is (β/∥M −1∥)-cocoercive. See Exer-
cise 2.9. Therefore, the FPI with variable metric FBS converges if ∥M −1∥< 2β.
Averagedness with respect to ∥· ∥M
Assume M ≻0. We say 핋is nonexpansive in ∥· ∥M if
∥핋x −핋y∥M ≤∥x −y∥M
∀x, y ∈dom 핋.
For θ ∈(0, 1), we say 핋is θ-averaged in ∥· ∥M if 핋= (1 −θ)핀+ θ핊for some 핊
that is nonexpansive in ∥· ∥M. We say 핋is averaged in ∥· ∥M if it is θ-averaged in
∥· ∥M for some unspecified θ ∈(0, 1).
The operator M −1/2핋M −1/2 is nonexpansive (in ∥· ∥) if and only if M −1핋is
nonexpansive in ∥· ∥M. This is easy to verify since
∥M −1/2핋M −1/2x −M −1/2핋M −1/2y∥2 ≤∥x −y∥2
is equivalent to
∥M −1핋˜x −M −1핋˜y∥2
M ≤∥˜x −˜y∥2
M
with the change of variables M −1/2x = ˜x and M −1/2y = ˜y.


## Page 71

56
2
Monotone operators and base splitting schemes
List of commonly used formulas
For later convenience, we list a few commonly used formulas derived in this section.
• If g(y) = f ∗(A⊺y), where f is CCP and R(A⊺) ∩ri dom f ∗̸ = ∅, then
u ∈∂g(y)
⇔
x ∈argminz {f(z) −⟨y, Az⟩}
u = Ax.
(2.2)
• If g(y) = f ∗(A⊺y), where f is CCP and R(A⊺) ∩ri dom f ∗̸ = ∅, then
v = Proxαg(u)
⇔
x ∈argminx

f(x) −⟨u, Ax⟩+ α
2 ∥Ax∥2	
v = u −αAx.
(2.6)
• Let L(x, u) = f(x) + ⟨u, Ax −b⟩and let Lα be the augmented Lagrangian of
(1.11). Then
핁α∂L(x, u) = (y, v)
⇔
y = argminz

Lα(z, u) +
1
2α∥z −x∥2	
v = u + α(Ay −b).
(2.7)
• If 픹(x) = 픸(x) + t, where 픸is maximal monotone and α > 0, then
핁α픹(u) = 핁α픸(u −αt).
(2.8)
• If 픹(x) = 픸(x −t), where 픸is maximal monotone and α > 0, then
핁α픹(u) = 핁α픸(u −t) + t.
(2.9)
• If 픹(x) = −픸(t −x), where 픸is maximal monotone and α > 0, then
핁α픹(u) = t −핁α픸(t −u).
(2.10)
• Inverse resolvent identity: If 픸is maximal monotone and α > 0, then
핁α−1픸(x) + α−1핁α픸−1(αx) = x.
(2.11)
• Moreau identity: If f is CCP and α > 0, then
Proxα−1f(x) + α−1Proxαf ∗(αx) = x.
(2.12)


## Page 72

Bibliographical Notes
57
Bibliographical Notes
There are many classical and recent review papers based on the core insight that monotone
operators serve as an elegant and unifying abstraction in the analysis of optimization
algorithms: Lemaire and Penot in 1989 [LP89], Iusem in 1999 [Ius99], Combettes in 2004
[Com04], Combettes and Wajs in 2005 [CW05], Combettes and Pesquet in 2011[CP11b],
Combettes, Condat, Pesquet, and Vũ in 2014 [CCPV14], Komodakis and Pesquet in 2015
[KP15], Clason and Valkonen in 2020 [CV20], and Condat, Kitahara, Contreras, and
Hirabayashi in 2020 [CKCH22]. This book is largely influenced by these prior treatments.
Early development: Basic notions.
The notion of monotonicity was first formal-
ized by Zarantonello in 1960 [Zar60]. The fact that derivatives of convex functions on
R are nondecreasing was established by Jensen in 1906 [Jen06], and this monotonicity
property was extended to gradients of convex functions on higher-dimensional spaces by
Kačurovskiĭ in 1960 [Kac60] and Minty in 1962 [Min62]. The notion of maximal mono-
tonicity was first established by Minty in 1962 [Min62]. Maximal monotonicity of subdif-
ferentials of CCP functions on Hilbert spaces (and thus on Rn) was established by Minty
in 1964 [Min64] and Moreau in 1965 [Mor65]. This maximality result was generalized to
convex functions on Banach spaces by Rockafellar [Roc66, Roc70b].
Fenchel’s identity (2.1) was first presented by Fenchel in 1951 in his lectures [Fen53,
Section 5]. The proximal operator was first introduced by Moreau in 1962 [Mor62, Mor65],
and the Moreau identity was introduced in 1965 [Mor65]. The proof of dom 핁픸= Rn
when 픸is maximal monotone, the Minty surjectivity theorem, was established by Minty
in 1962 [Min62]. The (1/2)-averagedness of resolvents was first discussed by Browder and
Petryshyn in 1967 [BP67].
The study of convex-concave saddle functions and their saddle subdifferentials was pio-
neered by Rockafellar. His work started in the 1960s [Roc64, Roc68], and the maximal
monotonicity of “closed proper” saddle subdifferentials was established in 1970 [Roc70a].
The augmented Lagrangian was used in [Hes69, Pow69] and later studied by Rockafellar
in the late 1970s [Roc76b, Roc78].
Early development: Methods.
Gradient descent dates back to Cauchy in 1847 [Cau47].
Fixed-point iterations date back to Picard, Lindelöf, and Banach in the late 1800s and
early 1900s [Pic90, Lin94, Ban22]. The proximal point method was first studied in the
1970s [Mar70, Mar72b, Roc76b, BL78], and its convergence rate in terms of function values
was later studied by Güler in 1991 [Gül91]. The method of multipliers was first presented
in 1969 by Hestenes and Powell [Hes69, Pow69] and was interpreted as an instance of PPM
by Rockafellar in 1973 [Roc73]. Dual ascent was first presented by Uzawa in 1972 [AHU58]
and was later further studied by Tseng, Bertsekas, and Tsitsiklis [TB87, Tse90a]. The
projected gradient method was first presented in the 1960s by Goldstein, Levitin, and
Polyak [Gol64, LP66]. The forward step method is due to Bruck in 1977 [Bru77] and
forward-backward splitting in its operator theoretic form was first presented in the 70s by
Bruck and Passty [Bru77, Pas79]. In modern literature, FBS applied to the sum of two
convex functions has been referred to as the proximal-gradient method [CW05].
Peaceman–Rachford and Douglas–Rachford splitting methods were first presented as split-
ting methods to solve the heat equation in 1955 and 1956 [PR55, DR56]. In 1979, Li-
ons and Mercier generalized the technique to a sum of two maximal monotone opera-
tors [LM79]. The effort of combining Douglas–Rachford and Forward–Backward splitting
schemes was initiated by Raguet, Fadili, and Peyré [RFP13, Rag19], extended by Briceño-
Arias [Bri15], and completed by Davis and Yin [DY17b] as they proved averagedness in the
general case with two maximal monotone operators and one cocoercive operator. This
splitting method, which we refer to as Davis–Yin splitting, is also called the Forward-


## Page 73

58
2
Monotone operators and base splitting schemes
Douglas–Rachford splitting.
As we explore further in §3, many of the splitting methods are intimately connected.
Since the DRS operator is firmly nonexpansive, it is a resolvent of a maximal monotone
operator, and this was first pointed out by Lawrence and Spingarn in 1987 [LS87] and
later by Eckstein and Bertsekas in 1992 [EB92]. That the gradient update can be viewed
as the proximal operator of the function’s first-order approximation, as discussed in §2.7.2,
was first identified by Polyak in 1987 [Pol87].
Fixed-point iteration.
The FPI analyzed in Theorem 1 is also called the Krasnosel’skiĭ–
Mann iteration. In 1953, Mann showed that the FPI converges when n = 1, C ⊂R is
a compact interval, and T : C →C is 1/2-averaged. In 1955, Krasnosel’skiĭ established
convergence when C ⊂Rn is compact and T : C →C is 1/2-averaged [Kra55]. In 1957,
Schaefer extended Krasnosel’skiĭ’s result to θ-averaged operators with θ ∈(0, 1) [Sch57].
The general convergence result of Theorem 1 (without any compactness assumption) is
due to Martinet’s 1972 work [Mar72a, Théorème 5.5.2]. A key component of our (and
Martinet’s) proof is the subsequence convergence argument of Stage 2, which is due to
Opial’s 1967 work [Opi67].
In fact, Theorem 1 of [Opi67] captures this subsequence
argument and is known as Opial’s lemma. The notion of averaged operators was first
formally defined in 1978 by Baillon, Bruck, and Reich [BBR78].
Infinite-dimensional analysis.
Although we focus on finite-dimensional spaces in this
book, much of the monotone operator theory is developed in the infinite-dimensional
setup, where a new set of interesting challenges arise.
For example, the convergence
xk →x⋆of Theorem 1 becomes weak when the underlying space is an infinite-dimensional
Hilbert space instead of Rn.
Bauschke and Combette’s textbook [BC17a] provides a
thorough treatment for operators on Hilbert spaces. Works on other setups include Reich
and Shoikhet’s [Rei79, RS98] work studying averaged operators in Banach spaces and
Goebel and Reich’s work [GR84, Rei85] studying averaged operators on the Hilbert ball
with the hyperbolic metric.
Forward and backward nomenclature and gradient-flow.
The operators 핀−α픸
and (핀+ α픸)−1 are respectively called forward and backward steps in analogy to the
forward and backward Euler discretizations of ˙x(t) = −픸x(t), a continuous-time differ-
ential equation defined for single-valued 픸. This interpretation is due to Lamaire and
Penot [LP89, Lem92] and Eckstein [Eck89, §3.2.2] in 1989. However, the gradient flow
˙x(t) = −∇f(x(t)) for functions f itself was studied earlier by Bruck in 1975 [Bru75a] and
Botsaris and Jacobson in 1976 [BJ76].
Consensus technique.
The first use of the consensus technique, also called the product
space trick, seems to be due to Pierra in 1984 [Pie84] and Spingarn in 1983 through the
“method of partial inverses” [Spi83, Spi85].
The use of the technique for distributed
optimization and machine learning was popularized through the works of Boyd, Parikh,
Chu, Peleato, and Eckstein [BPC+11, PB14b, PB14a].
Variable metric methods.
The variable metric proximal point method can be thought
of as a special case of the Bregman proximal point method, which was first presented by
Censor and Zenios for minimizing convex functions [CZ92] and Burachik and Iusem for
monotone inclusions [BI98]. Other early work includes that of Chen and Teboulle [CT93],
Bonnans, Gilbert, Lemaréchal, and Sagastizábal [BGLS95], Parente, Lotito, and Solodov
[PLS08], and He and Yuan [HY12b]. Variable metric forward backward splitting was first
formalized by Combettes and Vũ [CV14]. A block coordinate extension was given by
Chouzenoux, Pesquet, and Repetti [CPR16]. Liu and Yin [LY19] used variable metrics to
analyze the Davis–Yin splitting for smooth nonconvex problems. Vũ [Vũ13b] proposed


## Page 74

Bibliographical Notes
59
variable metric extensions of Tseng’s forward-backward-forward splitting. Briceño-Arias
and Davis [BD18] proposed variable metric extensions of their forward-backward-half
forward splitting. A different approach to apply variable metrics was introduced by Burke
and Qian [BQ99].
LASSO application.
LASSO (least absolute shrinkage and selection operator) first in-
troduced in geophysics literature in 1986 [SS86]. It was later independently rediscovered,
popularized, and named LASSO by the statistician Tibshirani in 1996 [Tib96]. LASSO is
one of the main models of compressed sensing [Don06, CT05, CT06] when the sensing is
corrupted by noise or the signal to sense is approximately sparse. Early work regarding
the computation of LASSO includes [EHJT04, FNW07, HYZ08, YOGD08]. The Nesterov
acceleration to the iterative soft thresholding algorithm was introduced in [BT09].


## Page 75

60
2
Monotone operators and base splitting schemes
Exercises
2.1 When 핋−1 is a left-inverse of 핋. Show that if x ∈dom 핋and 핋−1 is single-valued, then
핋−1핋x = x.
2.2 Non-maximal subdifferential. Consider the function f on R defined as
f(x) =



∞
for x < 0
1
for x = 0
0
for x > 0.
Show that f is convex and proper but not closed. Show that ∂f is not maximal.
2.3 Monotonicity of saddle subdifferential. Assume L: Rn × Rm →R and L(x, u) is convex-
concave. Recall ∂L is defined in (2.3). Show that ∂L is monotone.
Hint. Add the four subgradient inequalities that lower bound
• L(x2, u1) with a subgradient of L(·, u1) at x1
• −L(x1, u2) with a subgradient of −L(x1, ·) at u1
• L(x1, u2) with a subgradient of L(·, u2) at x2
• −L(x2, u1) with a subgradient of −L(x2, ·) at u2
to show
⟨∂xL(x1, u1) −∂xL(x2, u2), x1 −x2⟩+ ⟨∂u(−L(x1, u1)) −∂u(−L(x2, u2)), u1 −u2⟩≥0.
2.4 Maximality of continuous monotone operators. Show that if 핋: Rn →Rn is continuous
and monotone, then 핋is maximal.
Hint. Assume for contradiction that there is a pair (y, v) /∈핋such that
0 ≤⟨v −핋x, y −x⟩
for all x ∈Rn. Plug in x = y −δ and use continuity of 핋to argue
0 ≤⟨v −핋(y −δ), δ⟩= ⟨v −핋y, δ⟩+ o(∥δ∥)
as δ →0. Argue that v = 핋y and draw a contradiction.
2.5 Show that if f is a strictly convex CCP function, then (i) ∂f ∗is single-valued and (ii) f ∗
is differentiable on int dom f ∗.
Remark. Since f ∗is CCP, f ∗is subdifferentiable on int dom f ∗and ∂f ∗(u) is a singleton
if and only if f ∗is differentiable at u.
2.6 Recovering a primal solution from a dual solution. Let f be a strictly convex CCP function
on Rn, g a CCP function on Rm, and A ∈Rm×n. Consider the primal problem
minimize
x∈Rn
f(x) + g(Ax)
and dual problem
maximize
u∈Rm
−f ∗(−A⊺u) −g∗(u)
generated by the Lagrangian
L(x, u) = f(x) + ⟨Ax, u⟩−g∗(u).
Assume total duality holds. Show that ∇f ∗(−A⊺u⋆) is a primal solution.
Hint. Use Exercise 2.5.
Remark. Without the strict convexity, this statement is not true. The setting n = 1,
m = 1, f(x) = 0, A = 1, g(x) = δ{0}(x), and L(x, u) = xu is a counterexample: x⋆= 0
and u⋆= 0 are the unique primal and dual solutions, but ∂f ∗(−u⋆) = R.


## Page 76

Exercises
61
2.7 Differentiable monotone operators. Show that a differentiable operator 핋: Rn →Rn is
monotone if and only if D핋(x) + D핋(x)⊺⪰0 for all x.
Hint. Assume 핋is monotone, and use
D핋(x)v = lim
h→0
1
h(핋(x + hv) −핋(x))
to show v⊺D핋(x)v ≥0 for all v ∈Rn. For the other direction, assume D핋(x)+D핋(x)⊺⪰0
for all x, define g(t) = ⟨x −y, 핋(tx + (1 −t)y⟩, and use the mean value theorem to show
⟨x −y, 핋x −핋y⟩= g(1) −g(0) = g′(ξ)
for some ξ ∈[0, 1].
2.8 Differentiable Lipschitz operators. Show that a differentiable operator 핋: Rn →Rn is
L-Lipschitz if and only if σmax(D핋(x)) ≤L for all x.
Hint. Assume σmax(D핋(x)) ≤L, define g(t) = 핋(tx + (1 −t)y), and use the mean value
theorem and the Cauchy–Schwartz inequality to get
∥핋x −핋y∥2 = ⟨핋x −핋y, g(1) −g(0)⟩= ⟨핋x −핋y, g′(ξ)⟩≤∥핋x −핋y∥∥g′(ξ)∥.
For the other direction, assume 핋has Lipschitz parameter L and use
∥D핋(x)v∥= lim
h→0
1
h ∥핋(x + hv) −핋(x)∥.
2.9 Show that if 핋: Rn →Rn is β-cocoercive and M ∈Rn×n is symmetric positive definite,
then M −1/2핋M −1/2 is (β/∥M −1∥)-cocoercive.
2.10 Moreau envelope. Let f be a CCP function on Rn. For β > 0, define the Moreau envelope
of f of parameter β as
βf(x) = inf
z∈Rn

f(z) + 1
2β ∥z −x∥2

.
Show that
(a) βf(x) is convex and proper,
(b) ∇βf = β−1(핀−Proxβf),
(c) βf(x) is closed, and
(d) βf is 1/β-smooth.
Hint. For (a), establish closedness with βf(x) = f(Proxβf(x)) +
1
2β ∥Proxβf(x) −x∥2 and
the fact that Proxβf(x) is well-defined. For (b), note that
βf(x) = 1
2β ∥x∥2 −1
β sup
z∈Rn

⟨x, z⟩−βf(z) −1
2∥z∥2

,
and the supremum can be written as a conjugate. Take the gradient of both sides. For
(c), use the fact that βf is differentiable and therefore continuous. For (d), use the Moreau
identity to show β∇βf is a proximal operator of a convex function.
2.11 Moreau envelope as a smooth approximation. Let f be a CCP function on Rn and β > 0.
Show that limβ→0
βf(x) →f(x) for all x ∈Rn.
Hint. First show that u ∈∂f(x) if and only if f(x) + f ∗(u) = ⟨u, x⟩. Then argue that for
any x ∈Rn (possibly x /∈dom f)
f(x) = sup
u {−f ∗(u) + ⟨x, u⟩} =
sup
(y,u)∈∂f
{f(y) + ⟨u, x −y⟩}.


## Page 77

62
2
Monotone operators and base splitting schemes
So there exists a sequence (y0, u0), (y1, u1), . . . in ∂f such that
f(yk) + ⟨uk, x −yk⟩→f(x).
Remark. This result, along with the smoothness property of Exercise 2.10 allows us to
view βf as a smooth approximation of f. The interpretation of the Moreau envelope as a
smooth, regularized function is due to Attouch [Att77, Lemme 1], [Att84, Theorem 2.64].
However, the analogous notion for monotone operators, known as the Moreau–Yosida
approximation, was used earlier by Brezis [Bre71, Lemma 3], and the Moreau envelope
itself was presented earlier yet by Moreau [Mor65]. The result of this problem was first
presented by Friedlander, Goodwin, and Hoheisel [FGH21, Proposition 4].
2.12 PPM is GD. Show that argmin f = argmin βf for any β > 0. Also show that the PPM
with f is equivalent to gradient descent with respect to βf for some β > 0.
Hint. Use Exercise 2.10.
Remark. This problem illustrates that the Moreau envelope is also useful as a conceptual
tool for drawing connections.
2.13 Projection onto convex sets. Consider the convex feasibility problem
find
x∈Rn
x ∈C ∩D,
where C and D are nonempty closed convex sets. Assume C ∩D̸ = ∅.
(a) The convex feasibility problem is equivalent to the optimization problem
minimize
x∈Rn
1
2dist2(x, D)
subject to
x ∈C.
Show that the proximal gradient method with stepsize 1 applied to this problem is
xk+1 = ΠCΠDxk,
which is called the alternating projections method.
(b) The convex feasibility problem is also equivalent to the optimization problem
minimize
x∈Rn
θ
2dist2(x, C) + 1−θ
2 dist2(x, D),
where θ ∈(0, 1). Show that the gradient method with stepsize 1 applied to this
problem is
xk+1 = θΠCxk + (1 −θ)ΠDxk,
which is called the parallel projections method.
(c) Show that xk →x⋆∈C ∩D for both methods.
Hint. Note that 1
2dist2(x, C) is a Moreau envelope of δC.
Remark. See [BB96, BBL97, ER11] for an overview on convex feasibility problems.
2.14 Banach fixed-point theorem. Let 핋: Rn →Rn be contractive. Show that 핋has a unique
fixed point, i.e., show that a fixed point of 핋exists and is unique.
Hint. Consider an FPI and show that x0, x1, . . . is a Cauchy sequence.
Remark. This result is called the Banach fixed-point theorem [Ban22].
2.15 Strong monotonicity and unique zero. Show that if 픸: Rn ⇒Rn is maximal µ-strongly
monotone for some µ > 0, then 픸has exactly one zero.
Hint. Use the Banach fixed-point theorem.


## Page 78

Exercises
63
2.16 Contraction factor of gradient descent. Assume f is CCP, µ-strongly convex, L-smooth,
and twice continuously differentiable. Show that I −α∇f is max{|1 −αµ|, |1 −αL|}-
contractive for 0 < α < 2/L.
Hint. The fundamental theorem of calculus tells us
(I −α∇f)(x) −(I −α∇f)(y) =
Z 1
0
(I −α∇2f(tx + (1 −t)y))(x −y) dt.
Use the instance of Jensen’s inequality

Z 1
0
v(t) dt
 ≤
Z 1
0
∥v(t)∥dt,
where v(t) ∈Rn for t ∈[0, 1].
Remark. The result still holds when f is not continuously differentiable. See §13.
2.17 Convergence of dual ascent. Show that dual ascent converges in the sense of xk →x⋆and
uk →u⋆, where x⋆and u⋆are primal and dual solutions, under the stated conditions.
Hint. Use Theorem 1 to establish uk →u⋆and write xk as a continuous function of uk.
Remark. The stated conditions are f is CCP and µ-strongly convex, total duality holds,
and 0 < α < 2µ/σ2
max(A).
2.18 Method of multipliers primal solution convergence. Show that the method of multipliers
converges in the sense of xk →x⋆under the stated conditions and strict convexity. Use the
following fact: if h is a CCP function that is differentiable on D ⊆Rn, then ∇h: D →Rn
is a continuous function, i.e., differentiability and continuous differentiability coincide.
Remark. The stated conditions are f is CCP, R(A⊺) ∩ri dom f ∗̸ = ∅, a dual solution
exists, α > 0, and Lα(x, u) = f(x) + ⟨u, Ax −b⟩+ α
2 ∥Ax −b∥2.
Hint. Consider the primal problem
minimize
u∈Rm, v∈Rn
f ∗(v) + b⊺u
subject to
−v −A⊺u = 0
generated by the Lagrangian ˜L(v, u, x) = f ∗(v) + b⊺u −⟨x, v + A⊺u⟩, and use Slater’s
constraint qualification to show that R(A⊺) ∩ri dom f ∗̸ = ∅implies strong duality and
the existence of a primal solution for the primal-dual problem pair generated by L. Use
Exercise 2.5 to write xk = σ(uk), where σ: Rm →Rn is a continuous function.
Remark. The derivation of (2.6) or Exercise 1.5 establishes argminx Lα(x, uk)̸ = ∅, i.e.,
xk+1 ∈argminx Lα(x, uk) is well-defined for any uk ∈Rm.
2.19 Contraction factor of dual ascent. Consider dual ascent. Assume f is µ-strongly convex,
L-smooth, CCP, and 0 < α < 2µ/σ2
max(A). Using Exercise 2.16, show that dual ascent
converges with contraction factor
max{|1 −ασ2
max(A)/µ|, |1 −ασ2
min(A)/L|}.
2.20 Lyapunov analysis without summability. Let 핋: Rn →Rn be θ-averaged, and consider
the fixed-point iteration xk+1 = 핋xk. Consider the Lyapunov function
V k = k 1 −θ
θ
∥xk −xk−1∥2 + ∥xk −x⋆∥2.
Show that
V k+1 ≤V k
for k = 0, 1, . . . .
Use this inequality, instead of the summability argument, to prove
Theorem 1.


## Page 79

64
2
Monotone operators and base splitting schemes
2.21 When there is no fixed point. Assume 핋: Rn →Rn is averaged and Fix 핋= ∅. Prove that
the sequence xk+1 = 핋xk satisfies ∥xk∥→∞.
Hint. Assume for contradiction that ∥xk∥↛∞, which implies, by the Bolzano–Weierstrass
theorem, that there is a subsequence kj →∞such that xkj →¯x for some limit ¯x. Next,
show ∥xk+1 −xk∥→c for some c ≥0. Consider the cases c = 0 and c > 0 separately. In
the c > 0 case, show 핋k+1¯x −핋k¯x = 핋k¯x −핋k−1¯x and argue that ∥핋k¯x∥→∞, where
핋k = 핋◦· · · ◦핋
|
{z
}
k times
.
Remark. Interestingly, this result, first proved by Roehrig and Sine [RS81], does depend
on the finite-dimensionality of Rn. If 핋: H →H is an averaged operator on an infinite-
dimensional Hilbert space H, Browder and Petryshyn showed that lim supk→∞∥xk∥= ∞
[BP66], but Edelstein provided a counterexample for which lim infk→∞∥xk∥= 0 [Ede64,
BGMS21].
2.22 FPI with quasi-nonexpansive operators. We say 핊is quasi-nonexpansive if
∥핊x −x⋆∥2 ≤∥x −x⋆∥2
for all x⋆∈Fix 핊. We say 핋is θ-quasi-averaged if 핋= (1 −θ)핀+ θ핊for some quasi-
nonexpansive operator 핊. Assume 핋: Rn →Rn is continuous and θ-quasi-averaged with
θ ∈(0, 1). Assume Fix 핋̸ = ∅. Show that xk+1 = 핋xk with any starting point x0 ∈Rn
converges to one fixed point, i.e.,
xk →x⋆
for some x⋆∈Fix 핋.
2.23 Gradient descent with varying stepsize. Consider the problem of minimizing
minimize
x∈Rn
f(x),
where f is an L-smooth CCP function. Then
xk+1 = xk −αk∇f(xk),
where α0, α1, . . . ∈R, is called gradient descent with varying stepsize. Assume argmin f̸ =
∅and
0 <
inf
k=0,1,... αk ≤
sup
k=0,1,...
αk < 2/L.
Show
xk →x⋆∈argmin f.
Hint. Adapt the proof of Theorem 1 to fit the current setup.
2.24 Show (2.9) and (2.10).
2.25 Conic programs with DRS. Consider the problem of
minimize
x∈Rn
c⊺x
subject to
Ax = b
x ∈K,
where K ⊂Rn is a nonempty closed convex set. When K is a nonempty closed convex
cone, the problem is said to be a conic program. Assume A ∈Rm×n, where A has rank
m and b ∈Rm. Show that the FPI with DRS is
xk+1/2 = ΠK(zk)
xk+1 = D(2xk+1/2 −zk) + v
zk+1 = zk + xk+1 −xk+1/2,
where D = I −A⊺(AA⊺)−1A and v = A⊺(AA⊺)−1b −αDc.


## Page 80

Exercises
65
2.26 Convergence of DRS. Consider the FPI with DRS. Theorem 1 implies zk →z⋆for any
α > 0, provided that a fixed point exists. Show that this implies xk →x⋆, and xk+1/2 →
x⋆. Is ∥xk+3/2 −xk+1/2∥→0 and ∥xk+1 −xk∥→0 true?
2.27 When PRS does not converge. Consider the operators 픸= ℕ{0} and 픹= 0. Show that
although a fixed point of PRS does correspond to a solution, the FPI with PRS does not
converge. This example also demonstrates that the FPI with the reflected resolvent need
not converge.
2.28 Backward-backward is alternating minimization. Consider the monotone inclusion prob-
lem
find
x∈Rn
0 ∈(픸+ 픹)x.
The backward-backward method is
xk+1 = 핁α픸핁α픹xk,
where α > 0. Show that when 픸= ∂f and 픹= ∂g, where f and g are CCP functions,
we have
yk+1 = argmin
y∈Rn

f(xk) + g(y) + 1
2α∥xk −y∥2

xk+1 = argmin
x∈Rn

f(x) + g(yk+1) + 1
2α∥x −yk+1∥2

.
and that fixed points correspond to minimizers of
minimize
x,y∈Rn
f(x) + g(y) +
1
2α∥x −y∥2.
(2.20)
Finally, show that the backward-backward method converges.
Remark. This result was first published by Bauschke, Combettes, and Reich [BCR05].
2.29 Consensus + proximable is proximable.
Let r be a CCP function on Rn, C be the
consensus set as defined in (2.19), and
g(x1, . . . , xm) = δC(x1, . . . , xm) +
m
X
i=1
r(xi).
Show that we can evaluate Proxαg with
Proxαg(y1, . . . , ym) = (x, . . . , x),
x = Proxαr
 
1
m
m
X
i=1
yi
!
.
Also, what is the proximal operator of h(x1, . . . , xm) = δC(x1, . . . , xm) + r(x1)?
2.30 Let η ∈(0, 1) and consider the monotone inclusion problem
find
x∈Rn
0 ∈(2(1 −η)핀+ 픸+ 픹)x,
where 픸and 픹are maximal monotone, and assume 픸+ 픹is maximal. Show that the
solution can be found through the FPI zk+1 = 핋zk with
핋= 1
2핀+ 1
2(2η핁픸−핀)(2η핁픹−핀).
Hint. Show Zer (2(1 −η)핀+ 픸+ 픹) = 1
η Zer (픸(η) + 픹(η)), where 픸(η) = 픸◦1
η 핀+ 1−η
η 핀
and 픹(η) is defined likewise.
Remark. Since Zer (2(1 −η)핀+ 픸+ 픹) = 핁
1
2(1−η) (픸+픹)(0), a unique solution exists. This
method is called the averaged alternating modified reflections (AAMR) [AAC18, AAC19].


## Page 81

66
2
Monotone operators and base splitting schemes
2.31 Further properties of the proximal operator. Let f be a CCP function on Rn. Show:
(a) f(Proxαf(x)) is a nonincreasing function of α ∈(0, ∞) (for a fixed x ∈Rn).
(b) limα→∞f(Proxαf(x)) = infx f(x) (including the case infx f(x) = −∞).
(c) f(Proxαf(x)) ≤f(x) for any α > 0.
(d) limα→0+ f(Proxαf(x)) = f(x) for all x ∈dom f.
Hint. For (a), argue that
αf (Proxαf(x)) + 1
2 ∥Proxαf(x) −x∥2 ≤αf (Proxβf(x)) + 1
2 ∥Proxβf(x) −x∥2
βf (Proxβf(x)) + 1
2 ∥Proxβf(x) −x∥2 ≤βf (Proxαf(x)) + 1
2 ∥Proxαf(x) −x∥2
for α, β ∈R.
For (b), let ε > 0 and M > infx f(x). Let xM,ε be a point such that
f(xM,ε) < M + ε/2. Then
f(xM,ε) + 1
2α∥xM,ε −x∥2 < M + ε
for large enough α. For (d), show
αf(x) ≥αf(Proxαf(x)) + 1
2∥Proxαf(x) −x∥2
and let α →0.
Remark. The result of (d) is not necessarily true when x /∈dom f. For example, consider
f = δ{0} and x = 1.
Remark. In general, one can show limα→0+ Proxαf(x) = Πdom f(x) [FGH21, Proposi-
tion 5].
2.32 Proximable inequality constraints. Let f be a CCP function on Rn and informally assume
f is proximable. Through the following steps, show that δ{x∈Rn | f(x)≤0} is proximable.
Show:
(a) For maximal monotone 픸, α, β ∈(0, ∞),
핁α픸x = 핁β픸
β
αx +

1 −β
α

핁α픸x

∀x ∈Rn,
and
∥핁α픸x −핁β픸x∥≤
1 −β
α
 ∥핁α픸x −x∥
∀x ∈Rn.
(b) For a fixed x ∈Rn, f(Proxαf(x)) is a nonincreasing continuous function of α ∈
(0, ∞).
(c) Assume that dom f = Rn and that there exists an x ∈Rn such that f(x) < 0. Let
α⋆= inf{α > 0 | f(Proxαf(x)) ≤0}. Then
Π{x∈Rn | f(x)≤0}(x) =
 x
if f(x) ≤0
Proxα⋆f(x)
otherwise.
(d) Assume dom f = Rn and f(x) > 0. Also assume l0, u0 ∈R satisfy f(Proxl0f(x)) >
0 ≥f(Proxu0f(x)). The iteration
(lk+1, uk+1) =



(lk, lk+uk
2
)
if f

Prox lk+uk
2
f(x)

≤0
( lk+uk
2
, uk)
otherwise
converges in the sense that lk →α⋆and uk →α⋆.


## Page 82

Exercises
67
Hint. Show that (Proxα⋆f(x), α⋆) is a saddle point of
L(z, λ) = 1
2∥z −x∥2 + λf(z) −δR+(λ),
which implies that Proxα⋆f(x) is a solution to the primal problem generated by L.
Hint. Use Exercise 2.31.
Remark. The result of this problem was first presented by Friedlander, Goodwin, and
Hoheisel [FGH21, Corollary 13].
2.33 Consider the problem
minimize
x∈Rn
f0(x)
subject to
fi(x) ≤0,
i = 1, . . . , m,
where f0, . . . , fm are CCP. Assume all forms of total duality. Show that
xk+1/2 = Proxαf0
 
1
m
m
X
i=1
zk
i
!
xk+1
i
= Π{x∈Rn | fi(x)≤0}(2xk+1/2 −zk
i )
zk+1
i
= zk
i + xk+1
i
−xk+1/2
for i = 1, . . . , m
converges in the sense that xk+1/2 →x⋆and xk+1
i
→x⋆for i = 1, . . . , m.
Hint. Use Exercise 2.29.
2.34 Indicator function of a subspace. Let V ⊆Rn be a subspace and
V ⊥= {u ∈Rn | ⟨u, v⟩= 0 ∀v ∈V }
be its orthogonal complement. Show:
(a) (δV )∗= δV ⊥,
(b) ℕV (v) = V ⊥for all v ∈V , and
(c) ΠV + ΠV ⊥= 핀.
2.35 Indicator function of a convex cone. Let K ⊆Rn be a nonempty closed convex cone, i.e.,
K is a nonempty closed set satisfying
x1, x2 ∈K
⇒
θ1x1 + θ2x2 ∈K
for all θ1, θ2 ≥0. Let
K∗= {u ∈Rn | ⟨u, x⟩≥0 ∀x ∈K}
be the dual cone of K. Show:
(a) (δK)∗= δ−K∗,
(b) ℕK(x) = {u ∈−K∗| ⟨u, x⟩= 0} for all x ∈K, and
(c) ΠK + Π−K∗= 핀.
Remark. This problem subsumes Exercise 2.34.
2.36 Consensus technique for operators. Show that the problem
find
x∈Rn
0 ∈
m
X
i=1
픸ix,


## Page 83

68
2
Monotone operators and base splitting schemes
where 픸1, . . . , 픸m are (multi-valued) operators, is equivalent to
find
x1,...,xm∈Rn
0 ∈


픸1(x1)
...
픸m(xm)

+ ℕC(x1, . . . , xm),
where C = {(x1, . . . , xm) ∈Rnm | x1 = · · · = xm} is the consensus set.
Hint. Show C⊥= {(u1, . . . , um) ∈Rnm | u1 + · · · + um = 0} and use Exercise 2.34.
2.37 Variable metric DRS. Consider the problem
find
x∈Rn
0 ∈(픸+ 픹)x,
where 픸and 픹are maximal monotone. Assume Zer (픸+ 픹)̸ = ∅. Let M ∈Rn×n be a
symmetric positive definite matrix. Show that the FPI with variable metric DRS
xk+1/2 = 핁M−1픹(zk)
xk+1 = 핁M−1픸(2xk+1/2 −zk)
zk+1 = zk + xk+1 −xk+1/2
converges.
2.38 PPXA. Consider the problem
minimize
x∈Rn
m
X
i=1
gi(x),
where g1, . . . , gm are CCP functions on Rn. Let θ1, . . . , θm ∈R be such that θi > 0 for
i = 1, . . . , m and θ1 + · · · + θm = 1. Define the weighted average
zk
θ = θ1zk
1 + · · · + θmzk
m
and denote
zk
θ = (zk
θ, . . . , zk
θ) ∈Rmn.
The algorithm parallel proximal algorithm (PPXA) is
xk+1
i
= Prox(1/θi)gi(2zk
θ −zk
i )
for i = 1, . . . , m,
zk+1 = zk + xk+1 −zk
θ.
Assume Tm
i=1 int dom gi̸ = ∅and that a solution exists. Show that PPXA converges in
the sense that there exists a solution x⋆such that
(xk
1, . . . , xk
m) →(x⋆, . . . , x⋆).
Hint. Consider the variable metric DRS with
M =


θ1I
...
θmI

∈Rmn×mn,
where I ∈Rn×n is the identity matrix, and use
핁M−1∂f(x) = argmin
z∈Rd

f(z) + 1
2∥z −x∥2
M

.
Remark. PPXA was presented by Combettes and Pesquet [CP08, CP11b].


## Page 84

Chapter 3
Primal-dual splitting methods
This chapter presents techniques for deriving a collection of primal-dual methods,
methods that explicitly maintain and update both primal and dual variables. The
splitting methods of §2.7.2 are limited to optimization problems of the form of
minimizing f(x) + g(x) or f(x) + g(x) + h(x). The primal-dual methods of this
chapter can solve a wider range of problems and can exploit problem structures
with a high level of freedom.
With the techniques we present, we reduce a wide range of classical and modern
methods into instances of other methods for which we have established convergence.
Many of these connections are not at all obvious and were, in fact, discovered years
after the original publications of the methods. However, they are straightforward
to verify, and once a reduction is done, convergence analysis comes down to mere
bookkeeping.
For many methods, we present multiple derivations. For example, we derive
PDHG as a variable metric PPM, with the BCV technique, and as an instance of
linearized ADMM. The different derivations provide related but distinct interpre-
tations, and they show the intimate connection between the various primal-dual
methods.
3.1
Infimal postcomposition technique
The infimal postcomposition technique uses infimal postcomposition A ▷f, which
we define soon, to recast linearly constrained problems of the form
minimize
x∈Rp
f(x) + · · ·
subject to
Ax + · · ·
into an equivalent form without constraints
minimize
z∈Rn
(A ▷f)(z) + · · ·
and then applies a base splitting of §2.7.2.


## Page 85

70
3
Primal-dual splitting methods
Infimal postcomposition
Given a function f on Rn and matrix A ∈Rm×n, define the function A ▷f on Rm
with
(A ▷f)(z) =
inf
x∈{x | Ax=z} f(x).
This is called the infimal postcomposition of f by A or the image of f under A. If
f is CCP and R(A⊺) ∩ri dom f ∗̸ = ∅, then A ▷f is CCP.
The infimal postcomposition arises due to the formula
(A ▷f)∗(u) = f ∗(A⊺u),
(3.1)
which follows from
(A ▷f)∗(u) = sup
z∈Rm

⟨u, z⟩−inf
x∈Rn

f(x) + δ{x | Ax=z}(x)
	
= −inf
z∈Rm

−⟨u, z⟩+ inf
x∈Rn

f(x) + δ{x | Ax=z}(x)
	
= −
inf
x∈Rn,z∈Rm

f(x) + δ{x | Ax=z}(x) −⟨u, z⟩
	
= −inf
x∈Rn {f(x) −⟨u, Ax⟩}
= f ∗(A⊺u).
If R(A⊺) ∩ri dom f ∗̸ = ∅, then
x ∈argmin
x

f(x) + (1/2)∥Ax −y∥2	
z = Ax
⇔
z = ProxA▷f(y),
(3.2)
and the argmin of the left-hand side exists. (The argminx may not be unique, but
z = Ax is unique.) See Exercise 3.1 for a proof.
Alternating direction method of multipliers (ADMM)
Let f and g be CCP, A ∈Rn×p, B ∈Rn×q, and c ∈Rn. Consider the primal
minimize
x∈Rp, y∈Rq
f(x) + g(y)
subject to
Ax + By = c
(3.3)
and the dual problem
maximize
u∈Rn
−f ∗(−A⊺u) −g∗(−B⊺u) −c⊺u
(3.4)
generated by the Lagrangian
L(x, y, u) = f(x) + g(y) + ⟨u, Ax + By −c⟩.
(3.5)
Assume the regularity conditions
R(A⊺) ∩ri dom f ∗̸ = ∅
R(B⊺) ∩ri dom g∗̸ = ∅.
(3.6)


## Page 86

3.1
Infimal postcomposition technique
71
We will use the augmented Lagrangian:
Lρ(x, y, u) = f(x) + g(y) + ⟨u, Ax + By −c⟩+ ρ
2∥Ax + By −c∥2.
(3.7)
The primal problem (3.3) is equivalent to
minimize
z∈Rn
(A ▷f)(z)
|
{z
}
= ˜
f(z)
+ (B ▷g)(c −z)
|
{z
}
=˜g(z)
,
which is in the required form. We apply DRS to the equivalent primal problem.
The FPI with respect to 1
2핀+ 1
2ℝα−1∂˜
fℝα−1∂˜g is
zk+1/2 = Proxα−1˜g(ζk)
zk+1 = Proxα−1 ˜
f(2zk+1/2 −ζk)
ζk+1 = ζk + zk+1 −zk+1/2.
We introduce and substitute the variables xk, yk, and uk defined implicitly by
zk+1/2 = c −Byk+1, zk+1 = Axk+2, and ζk = α−1uk + Axk+1 and use (3.2) to get
yk+1 ∈argmin
y
n
g(y) + ⟨uk, Axk+1 + By −c⟩+ α
2 ∥Axk+1 + By −c∥2o
xk+2 ∈argmin
x
n
f(x) + ⟨uk+1, Ax + Byk+1 −c⟩+ α
2 ∥Ax + Byk+1 −c∥2o
uk+1 = uk + α(Axk+1 + Byk+1 −c).
Reordering the updates to get the dependency right, we get
xk+1 ∈argmin
x
n
f(x) + ⟨uk, Ax + Byk −c⟩+ α
2 ∥Ax + Byk −c∥2o
yk+1 ∈argmin
y
n
g(y) + ⟨uk, Axk+1 + By −c⟩+ α
2 ∥Axk+1 + By −c∥2o
uk+1 = uk + α(Axk+1 + Byk+1 −c).
Using the augmented Lagrangian (see Example 1.11), we can write the updates
more concisely as
xk+1 ∈argmin
x
Lα(x, yk, uk)
(3.8a)
yk+1 ∈argmin
y
Lα(xk+1, y, uk)
(3.8b)
uk+1 = uk + α(Axk+1 + Byk+1 −c).
(3.8c)
This method is called the alternating direction methods of multipliers (ADMM).
At this point, we have completed the core of the convergence analysis; we have
reduced ADMM to an instance of DRS applied to an equivalent transformation of
(3.3). What remains is the bookkeeping, where we check whether the necessary
conditions are met and translate the convergence of DRS into the convergence of
ADMM.


## Page 87

72
3
Primal-dual splitting methods
Convergence analysis.
When applying DRS to convex optimization, we require
total duality defined for a specific Lagrangian for convergence. In the current setup,
the Lagrangian for which we need total duality is not L.
DRS applied to the equivalent primal problem requires total duality between
minimize
z∈Rn
(A ▷f)(z)
|
{z
}
= ˜
f(z)
+ (B ▷g)(c −z)
|
{z
}
=˜g(z)
and
maximize
u∈Rn
−f ∗(−A⊺u) −g∗(−B⊺u) −c⊺u
generated by the Lagrangian
˜L(z, u) = (A ▷f)(z) + ⟨z, u⟩−g∗(−B⊺u) −c⊺u.
If the original primal and dual problems have solutions (x⋆, y⋆) and u⋆for which
strong duality holds, the equivalent primal and dual problems generated by ˜L(z, u)
have solutions Ax⋆and u⋆for which strong duality holds. In other words, total
duality of the original problems implies total duality of the equivalent problems.
Total duality implies that the FPI with DRS converges, and this translates to the
following convergence results.
If total duality between (3.3) and (3.4) holds, the regularity condition (3.6)
holds, and α > 0, then ADMM is well-defined, Axk →Ax⋆, and Byk →By⋆.
Regularity condition.
The assumed regularity condition (3.6) serves two pur-
poses: It ensures that A▷f and B ▷g are CCP functions, and that the minimizers
defining the iterations exist. (DRS applied to non-CCP (but convex) functions can
run into pathologies.) While (3.6) is a sufficient condition that ensures our analysis
is valid, it is not necessary. See the bibliographical notes, Exercise 3.1, and §8 for
further discussion.
3.2
Dualization technique
The dualization technique is to apply base splittings to the dual problems. Certain
primal problems with linear equality constraints have dual problems already of the
form of minimizing ˜f(u) + ˜g(u). We have seen this technique in the derivation of
the method of multipliers.
Alternating direction method of multipliers (ADMM)
With the dualization technique, we provide an alternate derivation and analysis of
ADMM. Again consider the problems (3.3) and (3.4) generated by the Lagrangian
(3.5). Apply DRS to the dual. Write ˜f(u) = f ∗(−A⊺u) and ˜g(u) = g∗(−B⊺u)+c⊺u,


## Page 88

3.2
Dualization technique
73
and the FPI with 1
2핀+ 1
2ℝα∂˜
fℝα∂˜g is
µk+1/2 = 핁α∂˜g(ψk)
µk+1 = 핁α∂˜
f(2µk+1/2 −ψk)
ψk+1 = ψk + µk+1 −µk+1/2.
Using (2.6) and (2.8), we write out the resolvent evaluations more explicitly as
˜yk+1 ∈argmin
y
n
g(y) + ⟨ψk −αc, By⟩+ α
2 ∥By∥2
2
o
µk+1/2 = ψk + α(B˜yk+1 −c)
˜xk+1 ∈argmin
x
n
f(x) + ⟨ψk + 2α(B˜yk+1 −c), Ax⟩+ α
2 ∥Ax∥2
2
o
µk+1 = ψk + αA˜xk+1 + 2α(B˜yk+1 −c)
ψk+1 = ψk + α(A˜xk+1 + B˜yk+1 −c).
Remove µk+1/2 and µk+1, as they no longer have any explicit dependence. Reor-
ganizing, we get
˜yk+1 ∈argmin
y
n
g(y) + ⟨ψk −αA˜xk, By⟩+ α
2 ∥A˜xk + By −c∥2
2
o
˜xk+1 ∈argmin
x
n
f(x) + ⟨ψk + α(B˜yk+1 −c), Ax⟩+ α
2 ∥Ax + B˜yk+1 −c∥2
2
o
ψk+1 = ψk + α(A˜xk+1 + B˜yk+1 −c).
Next, substitute uk = ψk −αA˜xk:
˜yk+1 ∈argmin
y
n
g(y) + ⟨uk, By⟩+ α
2 ∥A˜xk + By −c∥2
2
o
˜xk+1 ∈argmin
x
n
f(x) + ⟨uk+1, Ax⟩+ α
2 ∥Ax + B˜yk+1 −c∥2
2
o
uk+1 = uk + α(A˜xk + B˜yk+1 −c).
Finally, we swap the order of the uk+1 and ˜xk+1 update to get the correct depen-
dency and substitute xk+1 = ˜xk and yk = ˜yk to recover ADMM:
xk+1 ∈argmin
x
Lα(x, yk, uk)
yk+1 ∈argmin
y
Lα(xk+1, y, uk)
uk+1 = uk + α(Axk+1 + Byk+1 −c).
If total duality, (3.6), and α > 0 hold, then uk →u⋆, Axk →Ax⋆, and Byk →By⋆.
Convergence analysis.
The previous analysis of §3.1 established that Axk →Ax⋆
and Byk →By⋆. Since µk+1/2 →u⋆, this implies ψk →u⋆+ αAx⋆. Therefore, we
conclude uk →u⋆.


## Page 89

74
3
Primal-dual splitting methods
Alternating minimization algorithm (AMA)
Again consider the problems (3.3) and (3.4) generated by the Lagrangian (3.5).
Again, the dual problem (3.4) is
maximize
u∈Rn
−f ∗(−A⊺u)
|
{z
}
= ˜
f(u)
−(g∗(−B⊺u) + c⊺u)
|
{z
}
=˜g(u)
.
We furthermore assume f is µ-strongly convex. This implies f ∗(−A⊺u) is (λmax(A⊺A)/µ)-
smooth. Assume the regularity condition (3.6).
We apply FBS to the dual problem. The FPI with (핀+ α∂˜g)−1(핀−α∇˜f) is
uk+1/2 = uk −α∇˜f(uk)
uk+1 = (I + α∂˜g)−1(uk+1/2).
Using (2.2), (2.6), and (2.8) and assuming R(B) ∩ri dom g∗̸ = ∅, we write the
iteration as
xk+1 = argmin
x

f(x) + ⟨uk, Ax⟩
	
uk+1/2 = uk + αAxk+1
yk+1 ∈argmin
y
n
g(y) + ⟨uk+1/2 −αc, By⟩+ α
2 ∥By∥2o
uk+1 = uk+1/2 + αByk+1 −αc.
Eliminate uk+1/2 and use the Lagrangian (3.5) and augmented Lagrangian (3.7) to
write the iteration as
xk+1 = argmin
x
L(x, yk, uk)
yk+1 ∈argmin
y
Lα(xk+1, y, uk)
uk+1 = uk + α(Axk+1 + Byk+1 −c).
This method is called the alternating minimization algorithm (AMA) or dual prox-
imal gradient. If total duality, regularity conditions of (3.6), µ-strong convexity of
f, and α ∈(0, 2µ/λmax(A⊺A)) hold, then uk →u⋆, xk →x⋆, and Byk →By⋆.
Convergence analysis.
Under the stated assumptions, the convergence of FBS
tells us uk →u⋆. Since (x⋆, y⋆, u⋆) is a saddle point, we have x⋆= argminx L(x, y⋆, u⋆),
which implies 0 ∈∂f(x⋆) + A⊺u⋆, which in turn implies x⋆= ∇f ∗(−A⊺u⋆).
Since xk+1 = ∇f ∗(−A⊺uk), and since ∇f ∗is a continuous operator, uk →u⋆
implies xk →x⋆. Finally, uk →u⋆implies uk+1 −uk →0, which in turn implies
Axk+1 + Byk+1 −c →0. Combining this with xk →x⋆implies Byk →By⋆.


## Page 90

3.3
Variable metric technique
75
3.3
Variable metric technique
In §3.1 and §3.2, we transformed a given optimization problem into another equiva-
lent optimization problem and applied the splittings. In the following two sections,
we apply splittings to the saddle subdifferentials.
In this section, we present the variable metric technique. Its key insight is to
use variable metric PPM or variable metric FBS with a metric M carefully chosen
to cancel out certain terms and thereby simplify the update.
PDHG
Let f and g be CCP functions and A ∈Rm×n. Consider the problem pair (1.9)
and (1.10)
minimize
x∈Rn
f(x) + g(Ax),
maximize
u∈Rm
−f ∗(−A⊺u) −g∗(u)
generated by the Lagrangian (1.8),
L(x, u) = f(x) + ⟨u, Ax⟩−g∗(u).
We apply the variable metric PPM to the saddle subdifferential
∂L(x, u) =
 0
A⊺
−A
0
 x
u

+
 ∂f(x)
∂g∗(u)

.
The matrix
M =

(1/α)I
−A⊺
−A
(1/β)I

(3.9)
satisfies M ≻0 if α, β > 0 and αβλmax(A⊺A) < 1.
The FPI with (M + ∂L)−1M is
xk+1
uk+1

=
(1/α)I
0
−2A
(1/β)I

+
 ∂f
∂g∗
−1 (1/α)xk −A⊺uk
−Axk + (1/β)uk

,
which is equivalent to
(1/α)I
0
−2A
(1/β)I
 xk+1
uk+1

+
 ∂f(xk+1)
∂g∗(uk+1)

∋
(1/α)xk −A⊺uk
−Axk + (1/β)uk

.
Because the linear system of the resolvent is lower triangular, we can compute xk+1
from the upper inclusion and then, by substituting xk+1 into the lower inclusion,
compute uk+1:
xk+1 = Proxαf(xk −αA⊺uk)
uk+1 = Proxβg∗(uk + βA(2xk+1 −xk)).
This method is called the primal-dual hybrid gradient (PDHG) or Chambolle–Pock.
If total duality holds, α > 0, β > 0, and αβλmax(A⊺A) < 1, then xk →x⋆and
uk →u⋆.
There is another version PDHG that uses a similar but different M and obtains
uk+1 before xk+1. See Exercise 3.5.


## Page 91

76
3
Primal-dual splitting methods
Choice of metric.
Although PDHG is derived from PPM, which is technically not
an operator splitting, PDHG is a splitting since it deals with f and g separately.
Using the variable metric M to obtain a lower triangular system is crucial. For
example, although the FPI (xk+1, uk+1) = (핀+ ∂L)−1(xk, uk) would converge in
theory, it is not computationally useful; the off-diagonal terms A⊺and −A of ∂L
couple the xk+1 and uk+1-updates, so they must be computed simultaneously. With
no splitting, a single iteration is no easier than solving the whole problem itself.
Condat–Vũ
Consider the primal problem
minimize
x∈Rn
f(x) + h(x) + g(Ax)
(3.10)
and its dual problem
maximize
u∈Rm
−(f + h)∗(−A⊺u) −g∗(u),
(3.11)
where f, g, and h are CCP, h is differentiable, and A ∈Rm×n. The Lagrangian
that generates these problems is
L(x, u) = f(x) + h(x) + ⟨u, Ax⟩−g∗(u).
(3.12)
This generalizes the PDHG setup, as it allows the additional differentiable function
h.
We apply the variable metric FBS to the saddle subdifferential ∂L with the
metric M defined in (3.9). We split the saddle subdifferential into
∂L(x, u) =
∇h(x)
0

|
{z
}
=ℍ(x,u)
+
 0
A⊺
−A
0
 x
u

+
 ∂f(x)
∂g∗(u)

|
{z
}
=픽(x,u)
.
The FPI with (xk+1, uk+1) = (M + 픽)−1(M −ℍ)(xk, uk) is
xk+1
uk+1

=
(1/α)I
0
−2A
(1/β)I

+
 ∂f
∂g∗
−1 (1/α)xk −A⊺uk −∇h(xk)
−Axk + (1/β)uk

,
which we write as
xk+1 = Proxαf(xk −αA⊺uk −α∇h(xk))
uk+1 = Proxβg∗(uk + βA(2xk+1 −xk)).
This method is called Condat–Vũ. (See Exercise 3.5 for the other version of Condat–
Vũ.) If total duality holds, h is L-smooth, α > 0, β > 0, and
αL/2 + αβλmax(A⊺A) < 1,
(3.13)
then xk →x⋆and uk →u⋆.


## Page 92

3.3
Variable metric technique
77
Convergence analysis.
First, note that M ≻0 under the assumption α, β > 0
and (3.13). With basic computation, we get
M −1 =

α(I −αβA⊺A)−1
αβA⊺(I −αβAA⊺)−1
αβA(I −αβA⊺A)−1
β(I −αβAA⊺)−1

.
Let
θ = 2
L
 1
α −βλmax(A⊺A)

> 1.
Note that the condition θ > 1 equivalent to αL/2 + αβλmax(A⊺A) < 1. Then
θ
 1
αI −βA⊺A
−1
⪯θ
 1
α −βλmax(A⊺A)
−1
I = 2
LI.
If 핀−θM −1ℍis nonexpansive in ∥· ∥M, then 핀−M −1ℍis averaged in ∥·
∥M, and Condat–Vũ, a variable metric FBS, converges. (Nonexpansiveness and
averagedness in ∥· ∥M were discussed in §2.8.) Nonexpansiveness of 핀−θM −1ℍin
∥· ∥M follows from
∥(핀−θM −1ℍ)(x, u) −(핀−θM −1ℍ)(y, v)∥2
M
= ∥(x, u) −(y, v)∥2
M
−2θ⟨(x, u) −(y, v), ℍ(x, u) −ℍ(y, v)⟩+ θ2∥ℍ(x, u) −ℍ(y, v)∥2
M −1
= ∥(x, u) −(y, v)∥2
M
−2θ⟨x −y, ∇h(x) −∇h(y)⟩+ θ2∥∇h(x) −∇h(y)∥2
α(I−αβA⊺A)−1
≤∥(x, u) −(y, v)∥2
M
−(2θ/L)∥∇h(x) −∇h(y)∥2 + θ2∥∇h(x) −∇h(y)∥2
(α−1I−βA⊺A)−1
≤∥(x, u) −(y, v)∥2
M.
Example 3.1 In computational tomography (CT), the medical device measures the
Radon transform of a patient. The Radon transform is a linear operator R ∈Rm×n
and b ∈Rm is the measurement. It is often the case that m < n, i.e., there are more
unknowns than measurements, and b ≈Rxtrue, i.e., the measurement is corrupted
by small noise. Given the measurement b, the image is reconstructed by solving the
optimization problem
minimize
x∈Rn
1
2∥Rx −b∥2 + λ∥Dx∥1,
where the optimization variable x ∈Rn represents the 2D or 3D image to recover, D
is the 2D or 3D finite difference operator, and λ > 0. Although R and D are very
large matrices, the evaluation of matrix-vector products with R, D, R⊺, and D⊺are
efficient. To solve this problem, we can transform the given problem into
minimize
x∈Rn
0(x) + g(Ax),
where
A =

R
(β/α)D

,
0(x) = 0,
g(y, z) = 1
2∥y −b∥2 + (λα/β)∥z∥1,


## Page 93

78
3
Primal-dual splitting methods
for any α, β > 0, and apply PDHG to get
xk+1 = xk −(1/α)(αR⊺uk + βD⊺vk)
uk+1 =
1
1 + α(uk + αR(2xk+1 −xk) −αb)
vk+1 = Π[−λα/β,λα/β]

vk + βD(2xk+1 −xk)

,
where Π[−λα/β,λα/β] is applied elementwise. The computational bottleneck of this
algorithm is computing R⊺uk and R(2xk+1 −xk). (Computing D⊺vk and D(2xk+1 −
xk) costs much less.) In particular, this algorithm does not utilize any matrix inverses.
To further clarify, x ∈Rn is a 2D or 3D image reshaped into a length n vector.
Explicitly forming the matrices R and D is infeasible as they are too large, but there
are efficient algorithms for computing matrix-vector products with R, D, R⊺, and
D⊺. In particular, the application of R⊺is called backprojection.
3.4
Gaussian elimination technique
The Gaussian elimination technique reduces a system of inclusions into an upper
or lower triangular form through multiplying both sides by an invertible matrix.
The lower or upper triangular system is then solved sequentially, in a split manner.
Proximal method of multipliers with function linearization
Consider the constrained problem
minimize
x∈Rn
f(x) + h(x)
subject to
Ax = b,
(3.14)
where A ∈Rm×n, b ∈Rm, f and h are CCP, and h is differentiable.
The corresponding Lagrangian is
L(x, u) = f(x) + h(x) + ⟨u, Ax −b⟩.
We split the saddle subdifferential into
∂L(x, u) =
∇h(x)
b

|
{z
}
=ℍ(x,u)
+
 0
A⊺
−A
0
 x
u

+
∂f(x)
0

|
{z
}
=픾(x,u)
.
(3.15)
The FPI with (핀+ α픾)−1(핀−αℍ) is described by

I
αA⊺
−αA
I
 xk+1
uk+1

+

α∂f(xk+1)
0

∋
xk −α∇h(xk)
uk −αb

.
At first sight, this system may not seem useful, as the xk+1 and uk+1-updates are
seemingly coupled. However, left-multiply the system with the invertible matrix

I
−αA⊺
0
I

,


## Page 94

3.4
Gaussian elimination technique
79
which corresponds to Gaussian elimination, and get
I + α2A⊺A
0
−αA
I
 xk+1
uk+1

+

α∂f(xk+1)
0

∋

xk −α∇h(xk) −αA⊺(uk −αb)
uk −αb

,
a lower-triangular system. Now we compute xk+1 first and then compute uk+1:
xk+1 = argmin
x

f(x) + ⟨∇h(xk), x⟩+ ⟨uk, Ax −b⟩+ α
2 ∥Ax −b∥2 + 1
2α∥x −xk∥2

(3.16a)
uk+1 = uk + α(Axk+1 −b).
(3.16b)
This is called the proximal method of multipliers with function linearization. If
total duality holds, h is L-smooth, and α ∈(0, 2/L), then xk →x⋆and uk →u⋆.
Using Gaussian elimination with inclusions
It is important to keep in mind that row operations of Gaussian elimination can
only be performed using rows with single-valued operators. Given the system of
inclusions
픸z ∋b
픹z = c,
where 픹is single-valued, we can multiply M by the equation of the second row
and add it to the first row to obtain
픸z + M픹z ∋b + Mc
픹z = c.
This is equivalent to the original system of inclusions, as we can multiply −M by
the second row and add it to the first row to recover the original system.
Given the system of inclusions
픸z ∋b
픹z ∋c,
where 픹is not necessarily single-valued, we can multiply M by the inclusion of the
second row and add it to the first row to obtain
픸z + M픹z ∋b + Mc
픹z ∋c.
However, while this inclusion is a consequence of the original inclusion, it is not
equivalent; if we multiply −M by the second row and add it to the first row, we
get
픸z + M픹z −M픹z ∋b
픹z ∋c,
and this is not equivalent to the original system.


## Page 95

80
3
Primal-dual splitting methods
PAPC/PDFP2O
Consider the Lagrangian (3.12) in the special case of f = 0. This gives us the
problems
minimize
x∈Rn
h(x) + g(Ax)
maximize
u∈Rm
−h∗(−A⊺u) −g∗(u),
(3.17)
where h is differentiable, and the Lagrangian
L(x, u) = h(x) + ⟨u, Ax⟩−g∗(u).
We apply the variable metric FBS to the saddle subdifferential ∂L and use the
Gaussian elimination technique to evaluate the resolvent. (So we combine the two
techniques.) We split the saddle subdifferential into
∂L(x, u) =
∇h(x)
0

|
{z
}
=ℍ(x,u)
+
 0
A⊺
−A
0
 x
u

+

0
∂g∗(u)

|
{z
}
=픾(x,u)
.
The matrix
M =
(1/α)I
0
0
(1/β)I −αAA⊺

satisfies M ≻0 if αβλmax(A⊺A) < 1.
The FPI with (M + 픾)−1(M −ℍ) is described by
(1/α)I
A⊺
−A
(1/β)I −αAA⊺
 xk+1
uk+1

+

0
∂g∗(uk+1)

∋
 (1/α)xk −∇h(xk)
(1/β)uk −αAA⊺uk

.
Left-multiply the system by the invertible matrix
 I
0
αA
I

,
which corresponds to Gaussian elimination, and get
(1/α)I
A⊺
0
(1/β)I
 xk+1
uk+1

+

0
∂g∗(uk+1)

∋

(1/α)xk −∇h(xk)
Axk −αA∇h(xk) + (1/β)uk −αAA⊺uk

.
Now that the linear system of the resolvent is upper triangular, we can compute
uk+1 first and then compute xk+1:
uk+1 = Proxβg∗ uk + βA(xk −αA⊺uk −α∇h(xk))

xk+1 = xk −αA⊺uk+1 −α∇h(xk).
This method is called proximal alternating predictor corrector (PAPC) or primal-
dual fixed point algorithm based on proximity operator (PDFP2O). If total duality
holds, h is L-smooth, α > 0, β > 0, αβλmax(A⊺A) < 1, and α < 2/L, then xk →x⋆
and uk →u⋆.


## Page 96

3.4
Gaussian elimination technique
81
Example 3.2
In isotonic regression, entries of the regressor are constrained to be
nondecreasing. Isotonic regression with the Huber loss solves
minimize
x∈Rn
ℓ(Ax −b)
subject to
xi+1 −xi ≥0
for i = 1, . . . , n −1,
where A ∈Rm×n, b ∈Rm, and
ℓ(y) =
m
X
i=1
h(yi),
h(r) =
 r2
for |r| ≤1
2|r| −1
for |r| > 1.
For the sake of simplicity, assume n is even.
One solution method is to transform the problem into
minimize
x∈Rn
proximable
z
}|
{
X
i=1,3,...,n−1
δR+(xi+1 −xi) +
proximable
z
}|
{
X
i=2,4,...,n−2
δR+(xi+1 −xi) +
differentiable
z
}|
{
ℓ(Ax −b)
and use the FPI with DYS:
xk+1/2 = Πodd(zk)
xk+1 = Πeven(2xk+1/2 −zk −αA⊺∇ℓ(Axk+1/2 −b))
zk+1 = zk + xk+1 −xk+1/2,
where
Πodd = ProxP
i=1,3,...,n−1 δR+ ,
Πeven = ProxP
i=2,4,...,n−2 δR+
can be evaluated efficiently by Exercise 1.7.
Another solution method is to transform the problem into
minimize
x∈Rn
ℓ(Ax −b) + δR(n−1)
+
(Dx),
where R(n−1)
+
= {(u1, . . . , un−1) ∈R(n−1) | ui ≥0, i = 1, . . . , n−1} is the nonnegative
orthant and
D =


−1
1
0
· · ·
0
0
0
−1
1
· · ·
0
0
...
...
...
0
0
0
· · ·
−1
1

∈R(n−1)×n,
and use PAPC:
uk = Π(−∞,0](uk + βD(xk −αD⊺uk −αA⊺∇ℓ(Axk −b)))
xk = xk −αD⊺uk + αA⊺∇ℓ(Axk −b),
where Π(−∞,0] is applied elementwise. Note, (δR(n−1)
+
)∗= δ−R(n−1)
+
by Exercise 2.35.


## Page 97

82
3
Primal-dual splitting methods
3.5
Linearization technique
The linearization technique involves using a proximal term to cancel out a compu-
tationally inconvenient quadratic term. More specifically, consider the setup where
the method’s update is defined through
xk+1 = argmin
x∈Rn

f(x) + α
2 ∥Ax −b∥2 + 1
2∥x −xk∥2
M

.
If f is proximable and we have the freedom to choose M ≻0, we can choose
M = (1/β)I −αA⊺A with 1/β > αλmax(A⊺A) to get
f(x)+α
2 ∥Ax −b∥2 + 1
2∥x −xk∥2
M
= f(x) −α⟨Ax, b⟩−x⊺Mxk + α
2 x⊺A⊺Ax + 1
2x⊺Mx + constant
= f(x) + α⟨Axk −b, Ax⟩−1
β ⟨xk, x⟩+ 1
2β ∥x∥2 + constant
= f(x) + α⟨Axk −b, Ax⟩+ 1
2β ∥x −xk∥2 + constant
= f(x) + 1
2β
x −
 xk −αβA⊺(Axk −b)
2 + constant,
and we have
xk+1 = Proxβf
 xk −αβA⊺(Axk −b)

.
We call the ∥x −xk∥2
M term the “proximal term” and we choose M carefully to
cancel out the quadratic term x⊺A⊺Ax originating from ∥Ax −b∥2. The lineariza-
tion technique is named so because the result is as if we linearized the quadratic
term
α
2 ∥Ax −b∥2 ≈α⟨Ax, Axk −b⟩+ constant
and added (2β)−1∥x −xk∥2 to ensure convergence.
Linearized method of multipliers
Consider the primal problem (1.6):
minimize
x∈Rn
f(x)
subject to
Ax = b.
Let M ≻0 and K = α−1/2M −1/2. Re-parameterize the problem with x = Ky:
minimize
y∈Rn
f(Ky)
subject to
AKy = b.
The proximal method of multipliers of §2.6.1 applied to the re-parameterized
problem is
yk+1 = argmin
y

f(Ky) + ⟨uk, AKy⟩+ α
2 ∥AKy −b∥2 + 1
2α∥y −yk∥2

uk+1 = uk + α(AKyk+1 −b).


## Page 98

3.5
Linearization technique
83
Now we substitute back x = Ky and get
xk+1 = argmin
x

f(x) + ⟨uk, Ax⟩+ α
2 ∥Ax −b∥2 + 1
2∥x −xk∥2
M

uk+1 = uk + α(Axk+1 −b).
Let M = (1/β)I −αA⊺A, where αβλmax(A⊺A) < 1 so that M ≻0. Then, we get
xk+1 = argmin
x

f(x) + ⟨uk + α(Axk −b), Ax⟩+ 1
2β ∥x −xk∥2

uk+1 = uk + α(Axk+1 −b)
and we can write
xk+1 = Proxβf
 xk −βA⊺(uk + α(Axk −b))

uk+1 = uk + α(Axk+1 −b).
This method is called linearized method of multipliers. If total duality holds, α > 0,
β > 0, and αβλmax(A⊺A) < 1, then xk →x⋆and uk →u⋆.
When Proxβf is computationally easy to evaluate, but argminx{f(x)+ 1
2∥Ax−
b∥2} is not, the linearized method of multipliers can be much more effective than
the (original) method of multipliers.
3.5.1
BCV technique
When using the linearization technique, the proximal term (1/2)∥x −xk∥2
M must
come from somewhere. Sometimes we can use methods that already have a prox-
imal term, such as the proximal method of multipliers or the proximal ADMM of
Exercise 3.2. Alternatively, we can create proximal terms with the BCV technique,
named after Bertsekas, O’Connor, and Vandenberghe.
PDHG
Consider problem (1.9):
minimize
x∈Rn
f(x) + g(Ax).
This problem is equivalent to
minimize
x∈Rn, ˜x∈Rm
f(x) + δ{0}(˜x)
|
{z
}
= ˜
f(x,˜x)
+ g(Ax + M 1/2˜x)
|
{z
}
=˜g(x,˜x)
,
for any M ⪰0. This transformation is the BCV technique, and it will provide us
with a proximal term that we can use for the linearization.
Consider the FPI with DRS:
(zk+1, ˜zk+1) =
1
2핀+ 1
2ℝα∂˜gℝα∂˜
f

(zk, ˜zk).


## Page 99

84
3
Primal-dual splitting methods
Using (2.6), we have
Proxα˜g(x, ˜x) = (y, ˜y)
⇔
u ∈argmin
u
(
g∗(u) −

x
˜x

,
 A⊺
M 1/2

u

+ α
2

 A⊺
M 1/2

u

2)
y = x −αA⊺u
˜y = ˜x −αM 1/2u
under the regularity condition ri dom g ∩R([A M 1/2])̸ = ∅, and we write
xk+1/2 = argmin
x

f(x) + 1
2α∥x −zk∥2

˜xk+1/2 = 0
uk+1 = argmin
u
n
g∗(u) −⟨A(2xk+1/2 −zk) −M 1/2˜zk, u⟩+ α
2

∥A⊺u∥2 + ∥M 1/2u∥2o
xk+1 = 2xk+1/2 −zk −αA⊺uk+1
˜xk+1 = −˜zk −αM 1/2uk+1
zk+1 = xk+1/2 −αA⊺uk+1
˜zk+1 = −αM 1/2uk+1.
We simplify this further to get
xk+1/2 = argmin
x

f(x) + 1
2α∥x −(xk−1/2 −αA⊺uk)∥2

uk+1 = argmin
u
n
g∗(u) −⟨A(2xk+1/2 −xk−1/2), u⟩+ α
2 ∥u −uk∥2
(AA⊺+M)
o
.
We now perform linearization by setting M = (βα)−1I−AA⊺, where αβλmax(A⊺A) ≤
1 so that M ⪰0, and we get
xk+1/2 = Proxαf(xk−1/2 −αA⊺uk)
uk+1 = Proxβg∗(uk + βA(2xk+1/2 −xk−1/2)).
If total duality between (1.9) and (1.10), regularity condition ri dom g∩R([A M 1/2])̸ =
∅, α > 0, β > 0, and αβλmax(A⊺A) ≤1 hold, then xk+1/2 →x⋆.
Convergence analysis.
Note that the DRS in this derivation applies ℝα∂˜
f before
ℝα∂˜g, which is inconsistent with the usual ordering of §2.7.2, which applies Proxαg
before Proxαf. Keeping this reversed order in mind, note that the Lagrangian
˜L(x, ˜x, µ, ˜µ) = g(Ax + M −1/2˜x) + ⟨x, µ⟩+ ⟨˜x, ˜µ⟩−f ∗(µ),
the analog of (2.17), generates the stated equivalent primal problem and the dual
problem
maximize
µ∈Rn, ˜µ∈Rm
−
 A⊺
M 1/2

▷g∗

(−µ, −˜µ) −f ∗(µ).


## Page 100

3.5
Linearization technique
85
If (1.9) and (1.10) have solutions x⋆and u⋆for which strong duality holds, then the
equivalent primal-dual problem pair have solutions (x⋆, 0) and (−A⊺u⋆, −M 1/2u⋆)
for which strong duality holds. In other words, total duality of the original problems
imply total duality of the equivalent problems. So the FPI with DRS converges
under the stated assumptions and we conclude that xk+1/2 →x⋆.
PD3O
Consider the primal problem (3.10)
minimize
x∈Rn
f(x) + h(x) + g(Ax),
which was considered in Condat–Vũ. In particular, assume h is L-smooth. This
problem is equivalent to
minimize
x∈Rn, ˜x∈Rm
f(x) + δ{0}(˜x)
|
{z
}
= ˜
f(x,˜x)
+ g(Ax + M 1/2˜x)
|
{z
}
=˜g(x,˜x)
+ h(x)
|{z}
=˜h(x,˜x)
.
The DYS FPI is
(zk+1, ˜zk+1) = (핀−핁α∂˜
f + 핁α∂˜g(ℝα∂˜
f −α∇˜h핁α∂˜
f))(zk, ˜zk).
We let M = (βα)−1I −AA⊺and get
xk+1 = Proxαf
 xk −αA⊺uk −α∇h(xk)

uk+1 = Proxβg∗ uk + βA
 2xk+1 −xk + α∇h(xk) −α∇h(xk+1)

.
This method is called primal-dual three-operator splitting (PD3O). If total duality
holds, α > 0, β > 0, αβλmax(A⊺A) ≤1, and α < 2/L, then xk+1/2 →x⋆. See
Exercise 3.12.
Comparison with Condat–Vũ
Condat–Vũ and PD3O solve the same problem.
Condat–Vũ generalizes PDHG. PD3O generalizes PAPC and PDHG. The two
methods are very similar when compared side by side and have essentially identical
computational costs per iteration.
The convergence criteria of the two methods slightly differ.
Condat–Vũ re-
quires the stricter condition αβλmax(A⊺A) + αL/2 < 1, while PD3O requires
αβλmax(A⊺A) ≤1 and αL/2 < 1.
This difference allows PD3O to use step-
sizes that are, roughly speaking, twice as large. In some cases, this leads to PD3O
converging twice as fast compared to Condat–Vũ.
Proximal ADMM
Consider the primal problem (3.3):
minimize
x∈Rp, y∈Rq
f(x) + g(y)
subject to
Ax + By = c.


## Page 101

86
3
Primal-dual splitting methods
Let M ⪰0, N ⪰0, P = α−1/2M 1/2, and Q = α−1/2N 1/2.
This problem is
equivalent to
minimize
x∈Rp, y∈Rq
˜x∈Rq, ˜y∈Rp
f(x) + g(y)
subject to


A
0
P
0
0
I


x
˜x

+


B
0
0
I
Q
0


y
˜y

=


c
0
0

.
Applying ADMM to this problem gives us
xk+1 ∈argmin
x∈Rp
n
Lα(x, yk, uk) + ⟨˜uk
1, Px⟩+ α
2 ∥Px + ˜yk∥2o
˜xk+1 = argmin
˜x∈Rq
n
⟨˜uk
2, ˜x⟩+ α
2 ∥˜x + Qyk∥2o
= −Qyk −(1/α)˜uk
2
yk+1 ∈argmin
y∈Rq
n
Lα(xk+1, y, uk) + ⟨˜uk
2, Qy⟩+ α
2 ∥˜xk+1 + Qy∥2o
˜yk+1 = argmin
˜y∈Rp
n
⟨˜uk
1, ˜y⟩+ α
2 ∥Pxk+1 + ˜y∥2o
= −Pxk+1 −(1/α)˜uk
1
uk+1 = uk + α(Axk+1 + Byk+1 −c)
˜uk+1
1
= ˜uk
1 + α(Pxk+1 + ˜yk+1) = 0
˜uk+1
2
= ˜uk
2 + α(˜xk+1 + Qyk+1) = αQ(yk+1 −yk).
We simplify this to
xk+1 ∈argmin
x

Lα(x, yk, uk) + 1
2∥x −xk∥2
M

yk+1 ∈argmin
y

Lα(xk+1, y, uk) + 1
2∥y −yk∥2
N

uk+1 = uk + α(Axk+1 + Byk+1 −c).
This method is called the proximal alternating direction method of multipliers or
proximal ADMM. If total duality, M ⪰0, N ⪰0, (R(A⊺)+R(M))∩ri dom f ∗̸ = ∅,
(R(B⊺) + R(N)) ∩ri dom g∗̸ = ∅, and α > 0 hold, then uk →u⋆, Axk →Ax⋆,
Mxk →Mx⋆, Byk →By⋆, and Nyk →Ny⋆.
Convergence analysis.
The Lagrangian
L(x, y, u, ˜u1, ˜u2) = f(x) + g(y) + ⟨u, Ax + By −c⟩+ ⟨˜u1, Px + ˜y⟩+ ⟨˜u2, ˜x + Qy⟩
generates the equivalent primal problem. L generates the dual problem
maximize
u∈Rn
−f ∗(−A⊺u −P ˜u1) −δ{0}(−˜u2) −g∗(−B⊺u −Q˜u2) −δ{0}(−˜u1) −c⊺u


## Page 102

3.5
Linearization technique
87
If the original problems (3.3) and (3.4) have solutions (x⋆, y⋆) and u⋆for which
strong duality holds, then the equivalent problems have solutions (x⋆, y⋆) and
(u⋆, 0) for which strong duality holds. In other words, total duality of the original
problems implies total duality of the equivalent problems. So under the stated
assumptions, ADMM applied to the equivalent problem converges, and we get the
stated convergence results.
Finally, note that the equivalent dual problem resembles what we had when we
applied the BCV technique to PDHG. What we did is the BCV technique applied
to the dual.
Linearized ADMM
Consider the primal problem (3.3),
minimize
x∈Rp, y∈Rq
f(x) + g(y)
subject to
Ax + By = c.
Let M = (1/β)I −αA⊺A and N = (1/γ)I −αB⊺B. Proximal ADMM applied to
this setup is
xk+1 = argmin
x

f(x) + ⟨uk, Ax⟩+ α⟨Ax, Axk + Byk −c⟩+ 1
2β ∥x −xk∥2

yk+1 = argmin
y

g(y) + ⟨uk, By⟩+ α⟨By, Axk+1 + Byk −c⟩+ 1
2γ ∥y −yk∥2

uk+1 = uk + α(Axk+1 + Byk+1 −c),
which we can also write as
xk+1 = Proxβf
 xk −βA⊺(uk + α(Axk + Byk −c))

yk+1 = Proxγg
 yk −γB⊺(uk + α(Axk+1 + Byk −c))

uk+1 = uk + α(Axk+1 + Byk+1 −c).
This method is called linearized ADMM. If total duality holds, α > 0, β > 0, γ > 0,
αβλmax(A⊺A) ≤1, and αγλmax(B⊺B) ≤1, then xk →x⋆, yk →y⋆, and uk →u⋆.
Convergence analysis.
Under the stated assumptions, the convergence results for
proximal ADMM tell us uk →u⋆. We furthermore have Axk →Ax⋆, which implies
αAA⊺xk →αAA⊺x⋆, and x →Mx⋆. Since αA⊺A + M = β−1I, we add the two
convergence results to get xk →x⋆. We can show yk →y⋆with a similar argument.
PDHG
Consider the problem
minimize
y∈Rm, x∈Rn
g(y) + f(x)
subject to
−Iy + Ax = 0,
which is equivalent to (1.9), the primal problem for PDHG.


## Page 103

88
3
Primal-dual splitting methods
Linearized ADMM applied to this problem is
yk+1 = Proxβg
 yk + β(uk −α(yk −Axk))

xk+1 = Proxγf
 xk −γA⊺(uk −α(yk+1 −Axk))

uk+1 = uk −α(yk+1 −Axk+1).
Let β = 1/α and use the Moreau identity to get
yk+1 = (1/α)uk + Axk −(1/α) Proxαg∗ uk + αAxk
|
{z
}
=µk+1
xk+1 = Proxγf
 xk −γA⊺µk+1
uk+1 = µk+1 + αA(xk+1 −xk),
and we recover PDHG:
µk+1 = Proxαg∗ µk + αA(2xk −xk−1)

xk+1 = Proxγf
 xk −γA⊺µk+1
.
If total duality, α > 0, γ > 0, and αγλmax(A⊺A) ≤1 hold, then µk →u⋆and
xk →x⋆.
Discussion
In this section, we derived and established convergence of a wide range of splitting
methods through reducing them to another method for which we have already
established convergence. At a detailed level, the many techniques are not obvious,
and the execution often spans many lines of calculations. At a high level, however,
the approach is conceptually simple, as the theoretical basis of the convergence all
reduce to Theorem 1.
At this point, it is natural to ask how one should choose the appropriate opti-
mization method among the numerous ones that have been discussed. In practice, a
given problem usually has at most a few methods that apply conveniently. Among
the possible options, a good rule of thumb is to first consider methods with a low
per-iteration cost.


## Page 104

Bibliographical Notes
89
Bibliographical Notes
One key message of this chapter is that many operator splitting methods are closely
interconnected. This interconnectivity has been studied in prior works by Combettes,
Condat, Pesquet, and Vũ in 2014 [CCPV14], Yan and Yin in 2016 [YY16], Moursi and
Zinchenko in 2018 [MZ19], O’Connor and Vandenberghe in 2020 [OV20], and Condat,
Kitahara, Contreras, and Hirabayashi in 2020 [CKCH22].
Methods.
In 2011, Chambolle and Pock published PDHG (the form presented in this
chapter) [CP11a] and popularized the method. The method was not named in this work,
so many referred to it as the Chambolle–Pock method. However, similar methods were
proposed earlier by Pock, Cremers, Bischof, and Chambolle [PCBC09, Equation (21)] in
2009 and by Esser, Zhang, and Chan [EZC10, Equation (2.18) αk ≡1] in 2010. More
precisely, the algorithm we (along with Chambolle and Pock) consider corresponds to
the “PDHGMu” and “PDHGMp” of [EZC10]. The name “primal-dual hybrid gradient
(PDHG)” was first used by Zhu and Chan in their 2008 work [ZC08] to describe a similar
but different method. Nowadays, the method is more commonly referred to as PDHG
rather than Chambolle–Pock, even by Chambolle and Pock themselves [CP16a, Section
5.1].
PDHG and its variants were initially not presented as instances of the variable
metric PPM; this interpretation is due to He and Yuan in 2012 [HY12b]. Boţ, Csetnek,
Heinrich, and Hendrich’s 2015 work [BCHH15] and Chambolle and Pock’s 2016 work
provide further refined analyses of PDHG [CP16b].
PAPC/PDFP2O was independently proposed three different times: by Loris and Ver-
hoeven in 2011 for the case where h is quadratic [LV11], Chen, Huang, and Zhang in
2013 under the name PDFP2O [LV11], and by Drori, Sabach, and Teboulle in 2015 un-
der the name PAPC [DST15]. Combettes, Condat, Pesquet, and Vũ reinterpreted the
method as an instance of variable-metric FBS in 2014 [CCPV14]. Li and Yan [LY17] im-
proved the convergence analysis of PDFP2O/PAPC and relaxed the stepsize requirement
to αβλmax(A⊺A) ≤4/3.
The Condat–Vũ method was presented independently by Condat and Vũ in 2013 [Con13,
Vũ13a]. PD3O was presented by Yan in 2018 [Yan18a], and it was reinterpreted as an
instance of DYS by O’Connor and Vandenberghe in 2020 [OV20].
For the historical discussion of ADMM, see the bibliographical notes of §8.
Regularity conditions for ADMM.
For the ADMM iterations to be well defined, one
must either assume certain regularity conditions or directly assume the subproblems are
solvable. The influential review paper of Boyd et al. [BPC+11], which introduced ADMM
to the broad machine learning community, mistakenly claimed that the ADMM iterations
are well defined when f and g are CCP. This error was pointed out by Chen, Sun, and
Toh [CST17b].
Technique.
To the best of our knowledge, the first published instance of the infimal
postcomposition technique is due to Yan and Yin in 2016 [YY16], but the technique was
likely known earlier. In particular, the insight appears in a homework problem written
by Boyd in 2015 or earlier [BD15, Problem 7.1]. A thorough treatment of the infimal
postcomposition can be found in [Roc70d, Section 39] or [BC17a, §12.5]. The notion is also
referred to as the “image of a convex function.” The earliest instances of the dualization
technique are Rockafellar’s 1976 work showing that the augmented Lagrangian method
for a linearly constrained convex problem is PPM applied to its dual problem [Roc76b],
Gabay’s 1983 work showing ADMM is DRS applied to the dual [Gab83], and Tseng’s
1990 work deriving AMA as FBS applied to the dual [Tse90b, Tse91]. For the historical
discussion of the variable metric technique, see the bibliographical notes of §2. The origin
of the Gaussian elimination technique is unclear; to the best of our knowledge, this chapter


## Page 105

90
3
Primal-dual splitting methods
is the first instance where the Gaussian elimination technique is articulated, and the name
is due to us. However, the idea was likely known prior to the writing of this book. For
the historical discussion of the linearization technique, see the bibliographical notes of §8.
The BCV technique was independently presented in the 2016 edition of Bertsekas’s book
[Ber16, Chapter 7.4.2], where the technique is used to obtain a version of the proximal
ADMM from the regular ADMM, and by O’Connor and Vandenberghe’s 2020 paper
[OV20], where it is used to obtain PDHG from DRS. Although the two derivations seem
different at first sight, they are, loosely speaking, equivalent under duality.


## Page 106

Exercises
91
Exercises
3.1 Prox of infimal postcomposition. Let f be CCP. Show that if R(A⊺) ∩ri dom f ∗̸ = ∅, then
x ∈argmin
x

f(x) + (1/2)∥Ax −y∥2	
z = Ax
⇔
z = ProxA▷f(y),
and the argmin of the left-hand side exists.
Hint. Use Exercise 1.5 and show
argmin
z

inf
x∈{x | Ax=z} f(x) + 1
2∥Ax −y∥2

= ProxA▷f(y).
3.2 Proximal ADMM from KKT operator. Consider the primal-dual problem pair (3.3) and
(3.4) generated by the Lagrangian L of (3.5). Split the Lagrangian into
L(x, y, u) = f(x) + ⟨u, Ax⟩
|
{z
}
=L1(x,y,u)
+ g(y) + ⟨u, By −c⟩
|
{z
}
=L2(x,y,u)
.
Show that the FPI with DRS
(ξk+1, ζk+1, ωk+1) =
1
2I + 1
2Rα∂L1Rα∂L2

(ξk, ζk, ωk)
simplifies to
xk+1 = argmin
x

Lα(x, yk, uk) + 1
2α∥x −xk∥2
2

yk+1 = argmin
y

Lα(xk+1, y, uk) + 1
2α∥y −yk∥2
2

uk+1 = uk + α(Axk+1 + Byk+1 −c),
where Lα is the augmented Lagrangian of (3.7). Show that if total duality holds and
α > 0, then xk →x⋆, yk →y⋆, and uk →u⋆.
3.3 ADMM primal convergence. In the setup of ADMM, show that if g and f are strictly
convex in addition to the stated convergence conditions, then yk →y⋆and xk →x⋆,
where (x⋆, y⋆) is the primal solution. Use the following fact: if h is a CCP function that is
differentiable on D ⊆Rn, then ∇h: D →Rn is a continuous function, i.e., differentiability
and continuous differentiability coincide.
Remark. The stated conditions are f and g are CCP, R(A⊺) ∩ri dom f ∗̸ = ∅, R(B⊺) ∩
ri dom g∗̸ = ∅, L(x, y, u) = f(x) + g(y) + ⟨u, Ax + By −c⟩has a saddle point, and α > 0.
3.4 3-block extension of ADMM with DYS. Consider the problem
minimize
x,y,z
f(x) + g(y) + h(z)
subject to
Ax + By + Cz = d,
where x ∈Rp, y ∈Rq, z ∈Rr are the optimization variables and A ∈Rn×p, B ∈Rn×q,
C ∈Rn×r, and d ∈Rn. This is the primal problem generated by the Lagrangian
L(x, y, z, u) = f(x) + g(y) + h(z) + ⟨u, Ax + By + Cz −d⟩.


## Page 107

92
3
Primal-dual splitting methods
Assume f, g, and h are CCP, and furthermore assume h is µ-strongly convex. Show that
the dualization technique and DYS leads to the method
zk+1 = argmin
z
n
L(xk, yk, z, uk)
o
yk+1 ∈argmin
y
n
L(xk, y, zk+1, uk) + α
2 ∥Axk + By + Czk+1 −d∥2o
xk+1 ∈argmin
x
n
L(x, yk+1, zk+1, uk) + α
2 ∥Ax + Byk+1 + Czk+1 −d∥2o
uk+1 = uk + α(Axk+1 + Byk+1 + Czk+1 −d).
Under what conditions does this method converge?
3.5 Condat–Vũ, the other version. In the derivation of Condat–Vũ, show that if we instead
use
M =
(1/α)I
A⊺
A
(1/β)I

,
we get the method
uk+1 = Proxβg∗(uk + βAxk)
xk+1 = Proxαf(xk −αA⊺(2uk+1 −uk) −α∇h(xk)).
Also show that if total duality holds, h is L-smooth, α > 0, β > 0, and (3.13) holds, then
xk →x⋆and uk →u⋆.
Remark. Doing the same with h = 0 gives us the other version of PDHG:
uk+1 = Proxβg∗(uk + βAxk)
xk+1 = Proxαf(xk −αA⊺(2uk+1 −uk)).
3.6 PDHG generalizes DRS. PDHG with A = I and β = 1/α is
xk+1 = Proxαf(xk −αuk)
uk+1 = Prox(1/α)g∗(uk + (1/α)(2xk+1 −xk)).
DRS with Proxαf applied first is
xk+1/2 = Proxαf(zk)
xk+1 = Proxαg(2xk+1/2 −zk)
zk+1 = zk + xk+1 −xk+1/2.
Show that the two methods are equivalent in the sense that they generate an identical
sequence of iterates after a change of variables.
Hint. For PDHG, define ˜zk = xk −αuk.
Remark. The BCV technique establishes the converse, that DRS generalizes PDHG.
3.6-2 PD3O generalizes DYS. PD3O with A = I and β = 1/α is
xk+1 = Proxαf(xk −αuk −α∇h(xk))
uk+1 = Prox(1/α)g∗(uk + (1/α)(2xk+1 −xk) + ∇h(xk) −∇h(xk+1)).


## Page 108

Exercises
93
DYS with Proxαf applied first is
xk+1/2 = Proxαf(zk)
xk+1 = Proxαg(2xk+1/2 −zk −α∇h(xk+1/2))
zk+1 = zk + xk+1 −xk+1/2.
Show that the two methods are equivalent in the sense that they generate an identical
sequence of iterates after a change of variables.
Remark. The BCV technique establishes that DYS generalizes PD3O.
3.7 Preconditioned PDHG. Consider the problem
minimize
x∈Rn
f(x) + g(Ax),
where A ∈Rm×n and f and g are CCP, and show that
xk+1 = (N + ∂f)−1(Nxk −A⊺uk)
= argmin
x

f(x) + 1
2∥x −(xk −N −1A⊺uk)∥2
N

uk+1 = (M + ∂g∗)−1(Muk + A(2xk+1 −xk))
(3.18)
= argmin
u

g∗(u) + 1
2∥u −(uk + M −1A(2xk+1 −xk))∥2
M

,
where N ∈Rn×n and M ∈Rm×m are symmetric positive definite, converges when
 N
−A⊺
−A
M

≻0.
Remark. When N̸ = I or M̸ = I, (3.18) is called preconditioned PDHG. When N and
M are diagonal and N̸ = I or M̸ = I, (3.18) is called diagonally preconditioned PDHG.
Preconditioning is essential for PDHG to work well in practice [PC11].
3.8 Doubly linearized method of multipliers. Consider the primal problem
minimize
x∈Rn
f(x) + h(x)
subject to
Ax = b,
where A ∈Rm×n, b ∈Rm, f and h are CCP, and h is differentiable, generated by the
Lagrangian
L(x, u) = f(x) + h(x) + ⟨u, Ax −b⟩.
Show that the FPI with (M + 픾)−1(M −ℍ) with 픾and ℍdefined as in (3.15) and
M =
(1/α)I −βA⊺A
0
0
(1/β)I

gives us
xk+1 = Proxαf

xk −α∇h(xk) −αA⊺(uk + β(Axk −b))

uk+1 = uk + β(Axk+1 −b).
Under what conditions does this method converge? Note that Condat–Vũ and PD3O can
be used to solve this problem. How do the algorithms and their convergence conditions
compare?
Remark. This method is presented in [LY17, Section 3]. This method is useful when f is
proximable but f + h is not.


## Page 109

94
3
Primal-dual splitting methods
3.9 Constraint relaxation.
The constraint Ax = b is equivalent to the objective function
δ{0}(Ax −b). When we do not expect Ax = b to hold (due to errors or noise), we can
minimize its violation ℓ(Ax −b) with some loss function ℓ. Consider
minimize
x∈Rn
f(x) + h(x) + ℓ(Ax −b),
where f is CCP, h is CCP and L-smooth, and ℓis CCP and µ-strongly convex. The
primal problem is generated by the Lagrangian
L(x, u) = f(x) + h(x) + ⟨u, Ax −b⟩−ℓ∗(u).
Consider the decomposition
∂L(x, u) =

∇h(x)
∇ℓ∗(u) + b

|
{z
}
=ℍ(x,u)
+
 0
A⊺
−A
0
 x
u

+
∂f(x)
0

|
{z
}
=픾(x,u)
.
Show that the FPI with (M + 픾)−1(M −ℍ), where
M =
(1/α)I −βA⊺A
0
0
(1/β)I

gives us
xk+1 = Proxαf

xk −α∇h(xk) −αA⊺(uk + β(Axk −b −∇ℓ∗(uk)))

uk+1 = uk + β

Axk+1 −b −∇ℓ∗(uk)

.
Under what conditions does this method converge?
Remark. This method is presented in [LY17, Section 2]. When ℓ∗is not proximable, this
method is applicable, while Condat–Vũ and PD3O are not. This method generalizes the
method of Exercise 3.8 since ∇ℓ∗vanishes when ℓ= δ{0} and ℓ∗= 0.
3.10 Linearized method of multipliers with BCV. We used the linearization technique with
the proximal method of multipliers to prove convergence of the linearized method of
multipliers for αβλmax(A⊺A) < 1. By using the BCV technique, show that in fact uk →u⋆
for αβλmax(A⊺A) ≤1.
Hint. Apply ADMM to
minimize
x∈Rp, ˜y∈Rp
f(x)
subject to
A
P

x +
0
I

˜y =
b
0

.
3.11 PD3O generalizes PAPC/PDFP2O. PD3O with f = 0 is
xk+1 = xk −αA⊺uk −α∇h(xk)
uk+1 = Proxβg∗

uk + βA

2xk+1 −xk + α∇h(xk) −α∇h(xk+1)

.
PAPC/PDFP2O is
uk+1 = Proxβg∗

uk + βA(xk −αA⊺uk −α∇h(xk))

xk+1 = xk −αA⊺uk+1 −α∇h(xk).
Show that the two methods are equivalent in the sense that they generate an identical
sequence of iterates after a change of variables.


## Page 110

Exercises
95
3.12 PD3O. Show the omitted derivation of PD3O. Furthermore, show that uk →u⋆, i.e., show
that the dual variable converges to an optimal dual solution, under the stated conditions.
Remark. The stated conditions are f and h are CCP functions on Rn, h is L-smooth, g is
a CCP function on Rm, A ∈Rm×n, total duality holds, α > 0, β > 0, αβλmax(A⊺A) ≤1,
and α < 2/L.
3.13 Recast to LASSO. Let h be CCP and differentiable, A ∈Rn×p, and c ∈Rn. Consider the
problem
minimize
x∈Rp
µ∥x∥1 + h(Ax −b),
(3.19)
where µ > 0 is a penalty parameter.
Let us apply the infimal postcomposition technique to obtain the equivalent problem
minimize
z
(A ▷µ∥· ∥1)(z) + h(z −b).
The FPI with FBS is
zk+1 = ProxαA▷µ∥·∥1(zk −α∇h(zk −b)).
Show that this is equivalent to
ck = Axk −α∇h(Axk −b)
xk+1 ∈argmin
x

µ∥x∥1 + 1
2α∥Ax −ck∥2

.
Under what conditions does this method converge?
Remark. The subproblem for the xk+1-iterates is LASSO, which we discussed in §2.7.4.
(In fact, the problem at hand is LASSO if h = ∥· ∥2.)
Many sophisticated software
packages can effectively solve very large LASSO problems, and the presented method can
benefit from such packages.
3.14 Linearized method of multipliers and PDHG. Show the linearized method of multipliers
equivalent to a special case of PDHG with g = δ{b}.
Hint. Start with the linearized method of multipliers and define v0 = u0 + α(Ax0 −b)
and vk+1 = vk + α(A(2xk+1 −xk) −b) and eliminate uk.
3.15 Chen–Teboulle is variable metric PPM. Consider the primal problem
minimize
x∈Rn
f(x) + g(Ax),
where f is a CCP function on Rn, g is a CCP function on Rm, and A ∈Rm×n, generated
by the Lagrangian (convex with respect to (x, z) and concave with respect to u)
L(x, z, u) = f(x) + g(z) + ⟨u, Ax −z⟩.
Show that the Chen–Teboulle method
pk+1 = uk + α(Axk −zk)
xk+1 = Proxαf(xk −αA⊺pk+1)
zk+1 = Proxαg(zk + αpk+1)
uk+1 = uk + α(Axk+1 −zk+1)
is equivalent to an instance of the variable metric proximal point method on ∂L with
M =


α−1I
0
−A⊺
0
α−1I
I
−A
I
α−1I

.
Remark. The Chen–Teboulle method was published in 1994 [CT94], and this connection
was pointed out by Becker in 2019 [Bec19].


## Page 111

96
3
Primal-dual splitting methods
3.16 Chen–Teboulle is linearized method of multipliers. Consider the problem
minimize
x∈Rn, z∈Rm
f(x) + g(z)
subject to
Ax −z = 0,
where f is a CCP function on Rn, g is a CCP function on Rm, and A ∈Rm×n. Show that
the Chen–Teboulle method of Exercise 3.15 is equivalent to an instance of the linearized
method of multipliers.
Remark. The Chen–Teboulle method was published in 1994 [CT94], and this connection
was pointed out by Ma in 2020 [Ma20].
3.17 Unification of PAPC/PDFP2O and Condat–Vũ. Consider the primal-dual problem pair
minimize
x∈Rn
h(x) + g(Ax)
maximize
u∈Rm
−h∗(−A⊺u) −g∗(u),
where g is a CCP function on Rm, h is a differentiable CCP function on Rn, and A ∈
Rm×n, generated by the Lagrangian
L(x, u) = h(x) + ⟨u, Ax⟩−g∗(u).
The PAPC/PDFP2O method
uk+1 = Proxβg∗

uk + βA(xk −αA⊺uk −α∇h(xk))

xk+1 = xk −αA⊺uk+1 −α∇h(xk)
can be derived as the variable metric FBS with the metric matrix
M =
(1/α)I
0
0
(1/β)I −αAA⊺

.
The second version of Condat–Vũ (cf. Exercise 3.5),
uk+1 = Proxβg∗

uk + βAxk
xk+1 = xk −αA⊺(2uk+1 −uk) −α∇h(xk),
can be derived as the variable metric FBS with the metric matrix
M =
(1/α)I
A⊺
A
(1/β)I

.
Let B ∈Rm×n satisfy AB⊺= BA⊺. In this problem, use the metric matrix
M =
(1/α)I
B⊺
B
(1/β)I + α(BB⊺−AA⊺)

to derive
uk+1 = Proxβg∗

βAxk + (I + αβ(B −A)A⊺)uk + αβ(B −A)∇h(xk)

xk+1 = xk −αA⊺uk+1 −α∇h(xk) −αB⊺(uk+1 −uk)
as an instance of variable metric FBS. Note that when B = 0, we recover PAPC, and
when B = A, we recover Condat–Vũ. Show that the method converges if total duality
holds, h is L-smooth, α > 0, β > 0, α < 2
L, and
αβλmax(B⊺B) <
 2
αL −1

(1 −αβλmax(A⊺A)).


## Page 112

Exercises
97
You may use
M −1 =
αI + α2βB⊺(I −αβAA⊺)−1B
−αβB⊺(I −αβAA⊺)−1
−αβ(I −αβA⊺A)−1B
β(I −αβAA⊺)−1

without proof.
Hint. AB⊺= BA⊺implies BB⊺−AA⊺= (B −A)(A + B)⊺.
Remark. This unification was presented by Ko, Yu, and Won in 2019 [KYW19].
3.18 Variable metric DYS. Consider the 3-operator splitting problem
find
x∈Rd
0 ∈(픸+ 픹+ ℂ)x,
where 픸, 픹, and ℂare maximal monotone operators on Rd and Zer (픸+ 픹+ ℂ)̸ = ∅.
Show that if M ∈Rd×d is symmetric positive definite and M −1/2ℂM −1/2 is γ-cocoercive,
then
xk+1/2 = 핁αM−1픹

zk
xk+1 = 핁αM−1픸

2xk+1/2 −zk −αM −1ℂxk+1/2
zk+1 = zk + xk+1 −xk+1/2,
with α ∈(0, 2γ) converges.
3.19 PD3O via variable metric DYS. Consider the problem
minimize
x∈Rn
f(x) + h(x) + g(Ax),
where h : Rn →R is CCP and L-smooth, f is a CCP function on Rn, g is a CCP function
on Rm, and A ∈Rm×n. Assume
L(x, u) = f(x) + h(x) + ⟨u, Ax⟩−g∗(u)
has a saddle point. Consider the following decomposition of ∂L:
∂L(x, u) =

A⊺u
−Ax + ∂g∗(u)

|
{z
}
=픸(x,u)
+
∂f(x)
0

|
{z
}
=픹(x,u)
+
∇h(x)
0

|
{z
}
=ℂ(x,u)
.
Let α > 0 and β > 0 and consider the metric matrix
M =
I
0
0
α
β I −α2AA⊺

.
(a) Under what condition is M positive definite?
(b) Under what condition does the variable metric DYS
yk+1/2 = 핁αM−1픹

zk
yk+1 = 핁αM−1픸

2yk+1/2 −zk −αM −1ℂyk+1/2
zk+1 = zk + yk+1 −yk+1/2
with the given decomposition of ∂L converge?


## Page 113

98
3
Primal-dual splitting methods
(c) Show that the variable metric DYS in (b) is equivalent to PD3O:
xk+1 = Proxαf

xk −αA⊺uk −α∇h(xk)

uk+1 = Proxβg∗

uk + βA

2xk+1 −xk + α∇h(xk) −α∇h(xk+1)

.
Hint. For (c), use
zk =
pk
qk

,
yk+1/2 =
xk
wk

,
yk+1 =
rk
uk

.
Remark. In Exercise 3.12, we derived PD3O via the BCV technique and obtained the
stepsize requirement αβλmax(AA⊺) ≤1 and α < 2/L. Since the purpose of this problem
is to obtain an alternate derivation, you may not appeal to the prior analysis in your
answers for this problem.
Remark. This derivation of PD3O as variable metric DYS was first presented by Yan
[Yan18b] in his presentation slides and was later formally published by Salim, Condat,
Mishchenko, and Richtárik in 2020 [SCMR20].


## Page 114

Chapter 4
Parallel computing
In this chapter, we briefly discuss the basic notion of computational complexity
and parallel computing. The notion of computational complexity we consider is, in
a sense, incomplete as it accounts only for the cost of arithmetic operations, while
ignoring other costs such as the cost of coordination and communication between
computational agents. Nevertheless, this framework is a useful approximation for
analyzing the running time of algorithms.
4.1
Computational complexity via flop count
A floating-point operation or a flop is a single arithmetic operation carried out with
floating-point numbers. So a single operation of addition, subtraction, multiplica-
tion, and division count as a flop. For simplicity, we also count a single evaluation
of a non-elementary function such as exp(x), log(x), or √x as a single flop.
For example, we can evaluate
∥x∥=
q
x2
1 + · · · + x2n
for x ∈Rn with n multiplications, n−1 additions, and 1 square root. In total, ∥x∥
costs 2n = O (n) flops to compute.
The matrix-vector product Ax, where A ∈Rm×n and x ∈Rn, costs O (mn)
flops. The matrix-matrix product AB, where A ∈Rm×n and B ∈Rn×p, costs
O (mnp) flops. When computing the ABx, where A ∈Rm×n, B ∈Rn×p, and
x ∈Rp, it is better to use the formula A(Bx), which costs O (mn + np) flops,
instead of the formula (AB)x, which costs O (mnp) flops. Given a square matrix
A ∈Rn×n, the matrix inverse A−1 costs O
 n3
flops.
Modern CPUs operate at a clock speed of about 1 Ghz to 5 Ghz, and we can
expect them to compute roughly 109 flops or 1 gigaflop per second. This rough
estimate is quite useful in predicting the run time of an algorithm and analyzing
where the computational bottleneck of an algorithm will likely be. On the other
hand, it is a very rough estimate; expect a 10-fold or even a 100-fold inaccuracy.


## Page 115

100
4
Parallel computing
Algorithm vs. method
In this book, the words algorithm and method both refer to a specification of how
to compute a quantity of interest. However, they are different in that a method is
a higher-level description expressed in mathematical equations, while an algorithm
is a more literal step-by-step procedure unambiguously describing the steps the
computer takes. Although this distinction is not precise, it is useful. If an algorithm
carries out the idea described by a method, we say the algorithm implements the
method and call the algorithm an implementation of the method.
In a rigorous discussion, one should ascribe a flop count only to an algorithm,
not to a method. As an example, consider the method
xk+1 = xk −αA⊺(Axk −b),
where A ∈Rm×n and b ∈Rm.
The algorithm corresponding to the formula
A⊺(Axk −b) costs O (mn) flops per iteration, while the algorithm corresponding to
the formula (A⊺A)xk −A⊺b costs O
 n2
flops per iteration, provided that A⊺A ∈
Rn×n and A⊺b ∈Rm have been precomputed and stored. There is often more than
one way to implement a method written with mathematical equations. However,
when the implementation in consideration is clear from the context, we informally
ascribe the flop count to the method.
Flop-count operator
Define the flop-count operator
F [{x1, . . . , xn} 7→{y1, . . . , ym} | A]
as the number of flops the algorithm A processes to compute {y1, . . . , ym}, given
{x1, . . . , xn}. Again, it is the specific algorithm A, not a method, that determines
the flop count. When the algorithm is clear from context, we suppress the depen-
dency on A and write
F [{x1, . . . , xn} 7→{y1, . . . , ym}] .
When the input and/or output is a single quantity, we omit the curly braces and
write
F[x 7→y].
For example, we write
F[x 7→∥x∥] = 2n = O (n)
and
F[A 7→(I + αA⊺A)−1] = F[A 7→I + αA⊺A] + F[I + αA⊺A 7→(I + αA⊺A)−1]
= O
 mn2
+ O
 n3
= O
 (m + n)n2
.
As another example, consider
minimize
x∈Rn
1
2∥Ax −b∥2 + λ∥x∥1,


## Page 116

4.2
Parallel computing
101
where A ∈Rm×n, b ∈Rm, and λ > 0. As discussed in §2.7.4, the FPI with DRS is
xk+1/2 = (I + αA⊺A)−1(zk + αA⊺b)
xk+1 = S(2xk+1/2 −zk; αλ)
zk+1 = zk + xk+1 −xk+1/2,
where S is the soft-thresholding operator. A straightfoward and naive implemen-
tation costs
F

zk 7→zk+1
= F

A 7→(I + αA⊺A)−1
+ F
h
{zk, (I + αA⊺A)−1} 7→xk+1/2i
+ F
h
{xk+1/2, zk} 7→xk+1i
+ F
h
{zk, xk+1/2, xk+1} 7→zk+1i
= O
 (m + n)n2
+ O ((n + m)n) + O (n) + O (n)
= O
 (m + n)n2
flops per iteration.
It is possible to reduce this cost. When m ≥n, precompute (I +αA⊺A)−1 with
cost
F

A 7→(I + αA⊺A)−1
= O
 mn2
and αA⊺b with cost
F [{α, A, b} 7→αA⊺b] = O (mn).
In subsequent iterations, use precomputed quantities to reduce the cost to
F

{zk, (I + αA⊺A)−1, αA⊺b} 7→zk+1
= F
h
{zk, (I + αA⊺A)−1, αA⊺b} 7→xk+1/2i
+ F
h
{xk+1/2, zk} 7→xk+1i
+ F
h
{zk, xk+1/2, xk+1} 7→zk+1i
= O
 n2
+ O (n) + O (n)
= O
 n2
flops per iteration.
4.2
Parallel computing
In parallel computing, calculations are carried out simultaneously by multiple com-
puting units, such as multiple cores in a CPU, multiple cores in a GPU, or multiple
computers connected over the Internet. An (over)simplified view of parallel com-
puting is to think of a group of computational agents coordinating and working
together to complete a single task.
Assume we have p processors. If A, B ∈Rm×n and p ≤mn, then C = A + B
can be computed with O (mn/p) flops for each processor. To see why, consider the
following algorithm:


## Page 117

102
4
Parallel computing
parallel for i=1,...,m, j=1,...,n {
C[i,j] = A[i,j]+B[i,j]
}
The “parallel for” loop represents mn independent tasks. If p divides mn, then each
of the p processors can perform exactly mn/p out of the mn tasks. Otherwise,
partition the mn tasks into p groups of sizes roughly equal to mn/p and assign
them to the p processors.
We say a computational task is embarrassingly parallel if it takes little to no ef-
fort to divide it into parallel parts. (Embarrassingly parallel is good.) For example,
the computation of v = Ax is embarrassingly parallel:
parallel for i=1,...,m {
v[i] = 0;
for j=1,...,n
v[i] += A[i,j]*x[j]
}
Not all computational tasks benefit from parallel computing. Consider the FPI
with DRS as in (2.18):
xk+1/2 = Proxαf(zk)
xk+1 = Proxαg(2xk+1/2 −zk)
zk+1 = zk + xk+1 −xk+1/2.
Since the evaluation of Proxαg depends on the evaluation of Proxαf, it is in general
not possible to simultaneously compute Proxαg and Proxαf. When we have p ≤n
processors, the vector sum zk + xk+1 −xk+1/2 can be split up into p independent
parts, each costing O (n/p) flops. However, the computational bottleneck is usually
in evaluating Proxαg or Proxαf. It may not be possible to use parallel computing
to accelerate the evaluations of Proxαf and Proxαg, and, if not, this method does
not significantly benefit from parallel computing.
Parallel flop count operator
Let A be an algorithm that utilizes p parallel computing units. More specifically,
A can process up to p flops in parallel each step, provided that the p operations
are independent. In some steps, A may be unable to fully utilize the p computing
units and will process fewer than p flops. Define the parallel flop-count operator
Fp [{x1, . . . , xn} 7→{y1, . . . , ym} | A]
as the number of such steps A takes to compute {y1, . . . , ym}, given {x1, . . . , xn}.
As before, we omit the dependency on A if the algorithm is clear from context,
and we omit the curly braces when the input and/or output is a single quantity.
Parallelizable methods and operators
An algorithm is parallel if it utilizes multiple computing units and is serial oth-
erwise. Loosely speaking, a method is parallelizable if it has a parallel implemen-
tation that provides a significant speedup using many processors (p ≫1). We


## Page 118

4.2
Parallel computing
103
say a method is serial if it is not parallelizable. What constitutes a “significant”
speedup depends on the setup. We say an operator is parellelizable if there is a
parallelizable method for evaluating it.
Using the parallel flop count operator, we can express parallelizability of a
method for computing {y1, . . . , ym}, given {x1, . . . , xn} as
Fp [{x1, . . . , xn} 7→{y1, . . . , ym}] ≪F [{x1, . . . , xn} 7→{y1, . . . , ym}]
for large enough p. Again, what counts as ≪depends on context, but when
Fp [{x1, . . . , xn} 7→{y1, . . . , ym}] ∼C
p F [{x1, . . . , xn} 7→{y1, . . . , ym}]
for some C > 0 not too large, we safely say the method is parallelizable. Likewise,
an operator 핋is parallelizable if
Fp [x 7→핋x] ≪F [x 7→핋x] .
Parallel reduction
Reduction combines a set of numbers into one number with an associative binary
operator. A common instance of reduction is the sum
xsum =
m
X
i=1
xi,
where x1, . . . , xn ∈R. With p = 1 processor, reduction requires O (n) operations.
With p ≥⌊n/2⌋processors, reduction takes O (log n) steps. To see why, consider
the example of n = 8 and p = 4. The algorithm described by the following diagram
takes Fp [{x1, . . . , x8} 7→xsum] = 3 steps.
xsum
x1 + x2 + x3 + x4
x1 + x2
x1
x2
x3 + x4
x3
x4
x5 + x6 + x7 + x8
x5 + x6
x5
x6
x7 + x8
x7
x8
Step 1
Step 2
Step 3
+
+
+
+
+
+
+
The general strategy is to have the algorithm follow a binary tree with ⌊n/2⌋parallel
operations at the bottom and with a depth of log2 n.
With p < ⌊n/2⌋processors, reduction takes O (n/p + log p) steps. To see why,
consider the example of n = 40 and p = 4. The algorithm described by a following
diagram takes Fp [{x1, . . . , x40} 7→xsum] = 40/4 −1 + log2 4 = 11 steps.


## Page 119

104
4
Parallel computing
xsum
x1 + · · · + x20
x1 + · · · + x10
x1
x10
x11 + · · · + x20
x11
x20
x21 + · · · + x40
x21 + · · · + x30
x21
x30
x31 + · · · + x40
x31
x40
Steps 1–9
Step 10
Step 11
+
+
+
· · · + · · ·
· · · + · · ·
· · · + · · ·
· · · + · · ·
The general strategy is to partition the n numbers into p groups of sizes roughly
equal to n/p, take O (n/p) steps for the reduction on the p groups, and then reduce
the p numbers with an additional O (log p) steps.
To summarize,
Fp [{x1, . . . , xn} 7→xsum] =





O (n)
if p = 1
O (n/p + log p)
if 1 < p < ⌊n/2⌋
O (log n)
if p ≥⌊n/2⌋.
With a similar strategy, we can compute
• minimum and maximum of x1, . . . , xn ∈R,
• arithmetic mean, geometric mean, and product of x1, . . . , xn ∈R,
• ⟨x, y⟩for x, y ∈Rn, and
• ∥x∥1 and ∥x∥∞for x ∈Rn.
Parallel matrix-vector multiplication
Let A ∈Rm×n and x ∈Rn and consider the task of computing the matrix-vector
product b = Ax. Then
Fp [{A, x} 7→b] =







O (mn)
if p = 1
O (mn/p)
if p ≤m
O (mn/p + log(p/m))
m < p < mn/2
O (log n)
if mn/2 ≤p.
To see why, when p ≤m, we assign each processor with roughly m/p of the m
independent subtasks bi = Pn
j=1 Ai,jxj for i = 1, . . . , m, and when p > m, we
assign (p/m) processors to compute bi = Pn
j=1 Ai,jxj in O (n/(p/m) + log(p/m))
steps for i = 1, . . . , m, with the strategy used for computing parallel reduction.
The parallel flop count of reduction on m vectors in Rn follows from the same
reasoning: when x1, . . . , xm ∈Rn,
Fp [{x1, . . . , xn} 7→x1 + · · · + xn] =







O (mn)
if p = 1
O (mn/p)
if p ≤m
O (mn/p + log(p/m))
m < p < mn/2
O (log n)
if mn/2 ≤p.


## Page 120

4.2
Parallel computing
105
Other costs: coordination and communication
For parallel computing on a multicore CPU, counting floating-point operations to
analyze the computational cost of an algorithm is a useful approximation. However,
this may be inadequate for other parallel computing environments.
Parallel computing on a graphics processing unit (GPU) relies on thousands of
processors that are individually slower than a CPU’s processor but in aggregate
provide much more computing power.
On GPUs, the cost of coordination and
synchronization may be significant and thus should be taken into account.
In distributed and decentralized computing, which we discuss further in §11,
many computers operate in parallel and communicate over slow communication
channels such as the Internet. In this setup, the cost of communication may be
significant and thus should be taken into account.
4.2.1
Examples: finite-sum optimization
When a method relies on linear algebraic operations such as matrix-vector multi-
plication, it is possible to parallelize the linear algebra. In some cases, however,
a method itself is parallelizable at a higher level. We discuss several methods for
finite-sum minimization problems and to what extent they can be parallelized.
Sum of smooth functions
Consider the optimization problem
minimize
x∈Rn
f(x) + 1
m
m
X
i=1
hi(x),
where f is CCP and h1, . . . , hm are differentiable and CCP. The FPI with FBS,
the proximal gradient method, applied to this setup is
vk = −α
m
m
X
i=1
∇hi(xk)
xk+1 = Proxαf
 xk + vk
.
Assume computing Proxαf costs Cf flops and ∇hi costs Ch flops (or fewer) for
i = 1, . . . , m. Then, for p ≤min{m, n},
Fp

xk 7→xk+1
= Fp

xk 7→{∇hi(xk)}m
i=1

+ Fp

{∇hi(xk)}m
i=1 7→vk
+ Fp

{xk, vk} 7→xk+1
= O (mCh/p) + O (mn/p) + O (n/p + Cf)
= O ((Ch + n)m/p + Cf).
Therefore, the method is parallelizable if Cf = O ((Ch + n)m/p).


## Page 121

106
4
Parallel computing
Sum of proximable functions
Consider the problem
minimize
x∈Rn
f(x) + 1
m
m
X
i=1
gi(x).
where f, g1, . . . , gm are CCP and proximable. Using the consensus technique, which
we have seen in §2.7.4, we reformulate this problem into
minimize
x1,...,xm∈Rn
f(x1) + δC(x1, . . . , xm) + 1
m
m
X
i=1
gi(xi),
where C = {(x1, . . . , xm) | x1 = · · · = xm}. The FPI with DRS is
xk+1/2 = Proxαf
 
1
m
m
X
i=1
zk
i
!
xk+1
i
= Proxαgi(2xk+1/2 −zk
i )
zk+1
i
= zk
i + xk+1
i
−xk+1/2
for i = 1, . . . , m.
(See Exercise 2.29.) Assume computing Proxαf costs Cf flops and Proxαgi costs
Cg flops (or fewer) for i = 1, . . . , m. Write zk = (zk
1, . . . , zk
m). Then, for p ≤m,
Fp

zk 7→zk+1
= Fp
h
zk 7→xk+1/2i
+ Fp
h
{zk, xk+1/2} 7→zk+1i
= O (mn/p + Cf + Cgm/p).
Sum of proximable functions and a strongly convex function
Consider the primal problem
minimize
x∈Rn
f(x) +
m
X
i=1
gi(a⊺
i x −bi)
and the dual problem
maximize
u1,...,um∈R
−f ∗
 
−
m
X
i=1
uiai
!
−
m
X
i=1
(g∗
i (ui) + biui)
generated by the Lagrangian
L(x, u1, . . . , um) = f(x) +
m
X
i=1
⟨ui, a⊺
i x −bi⟩−
m
X
i=1
g∗
i (ui),
where a1, . . . , am ∈Rn, b1, . . . , bm ∈R, f is a strongly convex CCP function on
Rn, and g1, . . . , gm are proximable CCP functions on R. The FPI with FBS, the
proximal gradient method, applied to the dual is
xk = ∇f ∗
 
−
m
X
i=1
uk
i ai
!
uk+1
i
= Proxαg∗
i
 uk
i + α(a⊺
i xk −bi)

for i = 1, . . . , m.


## Page 122

4.2
Parallel computing
107
(Since f is strongly convex, f ∗is smooth.) Assume computing ∇f ∗costs Cf flops
and Proxαg∗
i costs Cg flops (or fewer) for i = 1, . . . , m. Then, for p ≤m and p ≤n,
Fp

{uk
1, . . . , uk
m} 7→{uk+1
1
, . . . , uk+1
m }

= O ((Cg + n)m/p + Cf).
Example 4.1 In the support-vector machine (SVM) setup, which is widely used in
machine learning for classification, we solve
minimize
x∈Rn
λ
2 ∥x∥2 +
m
X
i=1
max{1 −yia⊺
i x, 0},
where a1, . . . , am ∈Rn, y1, . . . , yn ∈{−1, 1}, and λ > 0. The FPI with FBS applied
to the dual is
xk = 1
2λ
 
−
m
X
i=1
uk
i yiai
!
uk+1
i
= Π[−1,0]

uk
i −α(1 −yia⊺
i xk)

for i = 1, . . . , m.
Then, this is parallelizable since
Fp
h
{uk
1, . . . , uk
m} 7→{uk+1
1
, . . . , uk+1
m
}
i
= O (nm/p)
for p ≤min{m, n}.
4.2.2
Amdahl’s law
Imagine that for a specific problem instance, the algorithm
xk+1/2 = xk −α∇f(xk)
xk+1 = Proxαg(xk+1/2)
takes 6 ms to evaluate xk+1/2 and 3 ms to evaluate xk+1. So the algorithm takes
9 ms per iteration. Imagine that we reduce the computation time of xk+1/2 from
6 ms to 0 ms. The speedup is
9
3 + 0 = 3.
This thought experiment provides an upper bound to the maximum speedup achiev-
able by reducing the computation time of xk+1/2; the speedup is at most 3.
Amdahl’s law formalizes this idea. Consider a task with a part that takes time
η ∈[0, 1], in proportion, to compute. If we speed up the computation time of this
part by s (through better math and parallel computing), then the total speedup is
S(s) =
1
1 −η + η/s.
We call this formula Amdahl’s law.


## Page 123

108
4
Parallel computing
As a corollary, we have
S(s) ≤
1
1 −η ,
i.e., 1/(1 −η) upper bounds the speedup we can achieve by accelerating the part.
This implies that a part of an algorithm is worth accelerating only if it occupies a
significant portion of the running time. Identifying the bottleneck should be the
first step of an effort to accelerate an algorithm.


## Page 124

Bibliographical Notes
109
Bibliographical Notes
Measuring the computational complexity of an algorithm by counting floating-point op-
erations is standard in applied mathematics. While our flop-count operator F is non-
standard, it does formalize the standard considerations of randomized and asynchronous
coordinate update algorithms that we discuss in §5 and §6. Our definitions of “method”
and “algorithm” are also nonstandard; the two words are often used interchangeably.
We point out that the stated complexity of O
 n3
for computing AB and A−1 when
A ∈Rn×n and B ∈Rn×n is not optimal. The Strassen algorithm [Str69] costs O
 n2.807
,
and the Coppersmith–Winograd algorithm [CW90] costs O
 n2.375
to compute AB and
A−1. The Strassen algorithm has found some practical applications, but not in convex
optimization. The Coppersmith–Winograd algorithm can only provide an advantage for
matrices of inordinate size and therefore has no practical use.
Amdahl’s law was formalized by Amdahl in 1967 [Amd67]. Support vector machine was
presented by Cortes and Vapnik in 1995 [CV95].


## Page 125

110
4
Parallel computing
Exercises
4.1 Matrix inversion lemma. The matrix inversion lemma or the Sherman–Woodbury–Morrison
formula states that
(E + BC)−1 = E−1 −E−1B(I + CE−1B)−1CE−1,
provided that E is invertible.
Let A ∈Rm×n and m ≤n. Show that with a given A and a precomputation O
 m2n

flops, each iteration
xk+1 = (I + αA⊺A)−1(xk + αb)
can be computed with O (mn) flops per iteration.
4.2 Parallel PDHG. Consider the problem
minimize
x∈Rn
ℓ
X
i=1
gi(Aix),
where A1, . . . , Aℓ∈Rm×n and g1, . . . , gℓare CCP. Assume computing Proxαgi costs
O (Cg) flops (or fewer) for i = 1, . . . , ℓ. Find a method that solves this problem using
O (ℓmn + ℓCg) flops per iteration. Can this algorithm benefit from parallel computing?
4.3 Parallel Condat–Vũ. Consider the problem
minimize
x∈Rn
f(x) + h(x) +
ℓ
X
i=1
gi(Aix −bi),
where A1, . . . , Aℓ∈Rm×n, g1, . . . , gℓare CCP, f is CCP, and h is differentiable and CCP.
Assume computing Proxαf and ∇h respectively costs Cf and Ch flops and computing
Proxαgi costs O (Cg) flops (or fewer) for i = 1, . . . , ℓ. Find a method that solves this
problem using O (ℓmn + ℓCg + Cf + Ch) flops per iteration. Can this algorithm benefit
from parallel computing?
4.4 Parallel PAPC/PDFP2O. Consider the problem
minimize
x∈Rn
h(x) + 1
m
ℓ
X
i=1
gi(Aix),
where A1, . . . , Aℓ∈Rm×n, g1, . . . , gℓare CCP, and h is differentiable and CCP. Assume
F[x 7→∇h] = Ch flops and computing F[y 7→Proxαgi(y)] ≤Cg for i = 1, . . . , ℓ. Find
a method that solves this problem using O (ℓmn + ℓCg + Ch) flops per iteration. Is this
method parallelizable?
4.5 Consensus technique and DYS. Consider the problem
minimize
x∈Rn
f(x) + 1
m
m
X
i=1
(gi(x) + hi(x)) ,
where f is CCP, g1, . . . , gm are CCP, h1, . . . , hm are differentiable and CCP. The consensus
technique yields the equivalent problem
minimize
x1,...,xm∈Rn
mf(x1) + δC(x1, . . . , xm) +
m
X
i=1
(gi(xi) + hi(xi)) .


## Page 126

Exercises
111
Show that the FPI with DYS is
xk+1/2 = Proxαf
 
1
m
m
X
i=1
zk
i
!
xk+1
i
= Proxαgi(2xk+1/2 −zk
i −α∇hi(xk+1/2))
zk+1
i
= zk
i + xk+1
i
−xk+1/2
for i = 1, . . . , m.
Assume computing Proxαf costs Cf flops, Proxαgi costs Cg flops, and ∇hi costs Ch flops
for i = 1, . . . , m. Assume the cost Cf cannot be further reduced through parallelization.
What is the parallel flop count Fp

{zk
1, . . . , zk
m} 7→{zk+1
1
, . . . , zk+1
m
}

for p ≤min{m, n}?
For simplicity, you may assume m/p and n/p are integers.
Hint. Use Exercise 2.29.
Remark. This method was first published by Raguet under the name generalized forward-
Douglas–Rachford [Rag19].


## Page 127

112
4
Parallel computing


## Page 128

Chapter 5
Randomized coordinate update
methods
In this chapter we present the randomized coordinate-update fixed-point iteration
(RC-FPI), a randomized method that updates a randomly chosen coordinate.
5.1
Randomized coordinate fixed-point iteration
Partition x ∈Rn into m non-overlapping blocks of sizes n1, . . . , nm, so n = n1 +
· · · + nm. Write x = (x1, . . . , xm), so xi ∈Rni for i = 1, . . . , m. Given an operator
핋: Rn →Rn, partition the output into m blocks and write
핋(x) =


(핋(x))1
...
(핋(x))m

,
so (핋(x))i ∈Rni for i = 1, . . . , m. For each i = 1, . . . , m, define 핋i : Rn →Rn as
핋i(x) =


x1
...
xi−1
(핋(x))i
xi+1
...
xm


,
i.e., 핋i is 핋on the ith block and is the identity map on the other blocks. When
ni = 1, the ith block corresponds to a single coordinate. Some authors use the
word “block” for a collection of more than one coordinate while reserving the
word “coordinate” for a single coordinate. In this book, we use these two words
interchangeably.


## Page 129

114
5
Randomized coordinate update methods
For 핋: Rn →Rn, consider the fixed-point problem
find
x∈Rn
x = 핋x.
The method coordinate-update fixed-point iteration (C-FPI) is
select i(k) ∈{1, . . . , m},
xk+1 = 핋i(k)(xk).
At the kth iteration, C-FPI selects an index i(k) and updates only the i(k)-th
block. Specifying the selection rule for i(k) fully specifies the method.
How to select i(k) is not a simple question. There are many block selection
rules with different advantages and disadvantages. Common selection rules include
the cyclic rule, which selects the blocks in a cyclic order; the essential cyclic rule,
which allows each coordinate to appear once or more in each “cycle”; the greedy
rule, which selects the block that leads to the most progress, measured in many
different ways; and the randomized rule, which selects blocks randomly.
In this chapter, we focus our study on the randomized rule with uniform prob-
ability, as its analysis is simplest. More specifically, we choose i(k) ∈{1, . . . , m}
independently uniformly at random.
Under this selection rule, C-FPI becomes
randomized coordinate-update fixed-point iteration (RC-FPI), which we write as
i(k) ∼IID Uniform{1, . . . , m}
xk+1 = 핋i(k)(xk).
The convergence property of RC-FPI is similar to the original FPI, and the proof
follows from analogous arguments. (For RC-FPI with non-uniform coordinate se-
lection probabilities, see Exercise 5.3.)
Theorem 2 Assume 핋: Rn →Rn is θ-averaged with θ ∈(0, 1) and Fix 핋̸ = ∅.
Assume the random indices i(0), i(1), . . . ∈{1, . . . , m} are independent and identi-
cally distributed with uniform probability. Then xk+1 = 핋i(k)xk with any starting
point x0 ∈Rn converges to one fixed point with probability 1, i.e.,
xk →x⋆
with probability 1 for some x⋆∈Fix 핋.
The quantities E dist2(xk, Fix 핋) and
E∥xk −x⋆∥2 for any x⋆∈Fix 핋are monotonically nonincreasing with k. Finally,
we have
dist(xk, Fix 핋) →0
with probability 1.


## Page 130

5.1
Randomized coordinate fixed-point iteration
115
Proof. Define 핊with 핋= 핀−θ핊and 핊i with 핋i = 핀−θ핊i. So we have
핊i(x) =


0
...
0
(핊(x))i
0
...
0


for i = 1, . . . , m. We can alternately express the iteration xk+1 = 핋i(k)xk as
xk+1 = xk −θ핊i(k)xk.
It is straightforward to verify that 핋is θ-averaged if and only if 핊is (1/2)-
cocoercive:
핋is θ-averaged
⇔
1
θ핋−
1
θ −1

핀is nonexpansive
⇔
핀−핊is nonexpansive
⇔
∥x −핊x −y + 핊y∥2 ≤∥x −y∥2
∀x, y ∈Rn
⇔
1
2∥핊x −핊y∥2 ≤⟨x −y, 핊x −핊y⟩
∀x, y ∈Rn
⇔
핊is (1/2)-cocoercive.
Clearly, x⋆= 핋x⋆if and only if 0 = 핊x⋆. So for any x⋆∈Fix 핋= Zer 핊and any
x ∈Rn, we have
1
2∥핊x∥2 ≤⟨핊x, x −x⋆⟩.
(5.1)
In Theorem 1 of §2, the sequence x0, x1, . . . was deterministic. In this theorem,
however, each xk+1 is a random variable that depends on i(k), i(k −1), . . . , i(0).
The initial point x0 is not random. Write E for the (full) expectation with respect
to all random variables random variables i(0), i(1), . . . . Write Ek for the conditional
expectation with respect to i(k) conditioned on the past random variables i(k −
1), i(k −2), . . . , i(0).
Then, E

Ek[X]

= E[X] by the law of total expectation.
Since the randomness of xk depends only on i(k −1), . . . , i(0), not i(k), we have
Ek[xk] = xk. Then,
Ek[핊i(k)xk] = 1
m핊xk,
(5.2)
Ek∥핊i(k)xk∥2 = 1
m∥핊xk∥2.
(5.3)
(Note that (5.3) does not follow from linearity of expectation but rather from the
fact that the squared norm ∥· ∥2 is separable across the indices.)


## Page 131

116
5
Randomized coordinate update methods
Stage 1.
For any x⋆∈Fix 핋, we have
∥xk+1 −x⋆∥2 = ∥xk −θ핊i(k)xk −x⋆∥2
= ∥xk −x⋆∥2 −2θ⟨핊i(k)xk, xk −x⋆⟩+ θ2∥핊i(k)xk∥2.
Taking conditional expectation Ek on both sides and using (5.2) and (5.3), we get
Ek∥xk+1 −x⋆∥2 = ∥xk −x⋆∥2 −2θ⟨Ek[핊i(k)xk], xk −x⋆⟩+ θ2Ek∥핊i(k)xk∥2
= ∥xk −x⋆∥2 −2θ
m ⟨핊xk, xk −x⋆⟩+ θ2
m ∥핊xk∥2
≤∥xk −x⋆∥2 −(1 −θ) θ
m∥핊xk∥2,
(5.4)
where the inequality follows from (5.1). Take the full expectation on both ends of
(5.4) to get
E∥xk+1 −x⋆∥2 ≤E∥xk −x⋆∥2 −(1 −θ) θ
mE∥핊xk∥2.
Therefore, E∥xk −x⋆∥2 is monotonically nonincreasing with k. By minimizing both
sides over x⋆∈Fix 핋, we obtain the monotonicity of E dist2(xk, Fix 핋).
Stage 2.
Next, we prove convergence of the iterates. Inequality (5.4) makes the
sequence (∥xk −x⋆∥2)k=0,1,... a nonnegative supermartingale. We apply the super-
martingale convergence theorem, which we state as Theorem 29 in the appendix,
to get
(i) P∞
k=0 ∥핊xk∥2 < ∞and
(ii) limk→∞∥xk −x⋆∥exists
with probability 1. Note that (i) implies ∥핊xk∥2 →0 and (ii) implies xk is bounded
with probability 1. (The limit limk→∞∥xk −x⋆∥is a random variable that depends
on x⋆and the random indices i(0), i(1), . . . .) For each x⋆, the convergence occurs
with probability 1. Next, we apply Proposition 1, which we state and prove in
what follows, to conclude with probability 1 that limk→∞∥xk −x⋆∥exists for all
x⋆∈Fix 핋. The convergence xk →x⋆with probability 1 now follows from the same
argument as that of Theorem 1 with the qualifier “with probability 1” appended
to each statement.
The necessity of Proposition 1 in Theorem 2 is subtle. Since we choose x⋆∈
Fix 핋first and then apply the supermartingale convergence theorem, the conclusion
that limk→∞∥xk −x⋆∥exists with probability 1 applies to one fixed point x⋆
at a time.
Without a formal argument, this does not immediately imply that
limk→∞∥xk −x⋆∥for all x⋆∈Fix 핋with probability 1 in the case where Fix 핋is
not a singleton and therefore has uncountably many fixed points.
Proposition 1 Let Y ⊆Rn and let x0, x1, . . . be a random sequence. Then statement
1 implies statement 2.
1. For all y ∈Y [with probability 1, limk→∞∥xk −y∥exists].


## Page 132

5.2
Coordinate and extended coordinate-friendly operators
117
2. With probability 1 [for all y ∈Y , limk→∞∥xk −y∥exists].
Proof of Proposition 1. This proof uses the separability of Rn, that is, Rn contains
a countable, dense subset.
In particular, Y ⊆Rn has a countable, dense subset {y1, y2, . . . }. By statement
1, given i ∈{1, 2, . . . }, there is a probability 1 event Ω(yi) such that limk→∞∥xk(ω)−
yi∥for all ω ∈Ω(yi). Therefore limk→∞∥xk(ω) −yi∥exists for all i ∈{1, 2, . . . }
for ω ∈∩i=1,2,...Ω(yi), and ∩i=1,2,...Ω(yi) is an event with probability 1 since it is
a countable intersection of probability 1 events.
(In other words: with probability 1 [for all i = 1, 2, . . . , limk→∞∥xk−yi∥exists].
The subtlety is that an uncountable intersection of probability 1 events may not
have probability 1.)
Now pick any y ∈Y . Statement 2 is proved if we can show ∥xk(ω)−y∥converges
for ω ∈∩i=1,2,...Ω(yi). To this end, pick any ε > 0. Since {y1, y2, . . . } ⊆Y is dense,
there exists yi ∈Y such that ∥yi −y∥≤ε. We get the following lower and upper
bounds with the triangle inequality:
∥xk(ω) −y∥≤∥xk(ω) −yi∥+ ∥yi −y∥≤∥xk(ω) −yi∥+ ε,
∥xk(ω) −y∥≥∥xk(ω) −yi∥−∥yi −y∥≥∥xk(ω) −yi∥−ε.
Since ω ∈Ω⊂Ω(yi),
lim sup
k→∞
∥xk(ω) −y∥≤lim
k→∞∥xk(ω) −yi∥+ ε,
lim inf
k
∥xk(ω) −y∥≥lim
k→∞∥xk(ω) −yi∥−ε,
and together we have
0 ≤lim sup
k
∥xk(ω) −y∥−lim inf
k
∥xk(ω) −y∥≤2ε.
As ε > 0 is arbitrary, we conclude
lim sup
k→∞
∥xk(ω) −y∥= lim inf
k→∞∥xk(ω) −y∥= lim
k→∞∥xk(ω) −y∥.
In mathematical terms, the key idea of Proposition 1 is that (i) Y has a count-
able dense subset, (ii) the sequence of functions {∥xk −·∥}k∈N has a limit on the
countable dense subset of Y , and (iii) if an equicontinuous sequence of functions
has a limit on the dense subset of a metric space, then the limit exists on the entire
metric space.
5.2
Coordinate and extended coordinate-friendly operators
While Theorem 2 is true regardless of the computational structure of 핋, the RC-FPI
is computationally effective when 핋is coordinate-friendly or extended coordinate-
friendly.


## Page 133

118
5
Randomized coordinate update methods
5.2.1
Coordinate-friendly operators
Let z = (z1, . . . , zm) ∈Rn and zi ∈Rni for i = 1, . . . , m. If
max
i=1,...,m F[x 7→zi] ≪F[x 7→z],
then we say the method is coordinate-friendly.
What counts as ≪depends on
context, but when
F[x 7→zi] ∼C
mF[x 7→{z1, . . . , zm}]
for i = 1, . . . , m,
for some C > 0 not too large, we safely say the method is coordinate-friendly.
Again, some authors use the terminology “block coordinate-friendly” and reserve
“coordinate-friendly” for when n1 = · · · = nm = 1, but we do not make this
distinction.
If a method for x 7→z is coordinate-friendly,
Fp[x 7→z] =
max
i=1,...,m F[x 7→zi] ≪F[x 7→z],
for p ≥m. So coordinate-friendly methods are parallelizable.
Finally, we say an operator 핋: Rn →Rn is coordinate-friendly if there is a
coordinate-friendly method for computing x 7→핋ix for i = 1, . . . , m.
Example 5.1
An affine operator 핋x = Ax + b, where A ∈Rn×n and b ∈Rn, is
coordinate-friendly if ni ≪n for i = 1, . . . , m, since
F[x 7→핋x] ∼2n2
F[x 7→핋ix] ∼2nni.
Example 5.2 We say 핋: Rn →Rn is a separable operator if
핋(x) = (핌1(x1), . . . , 핌m(xm)),
where 핌i : Rni →Rni for i = 1, . . . , m. Separable operators are coordinate-friendly
if maxi=1,...,m F[xi 7→핌i(xi)] ≪F[x 7→핋(x)]. Multiplication by a (block) diagonal
matrix is an example.
A function f : Rn →R is a separable function if it is of the form
f(x) =
m
X
i=1
fi(xi),
where fi : Rni →R for i = 1, . . . , m. If f is separable and differentiable, then ∇f is
separable. If f is separable and CCP, then Proxf is separable.
In optimization problems, a separable constraint is of the form
xi ∈Ci
for i = 1, . . . , m.
The projection onto a separable constraint is a separable operator. A common ex-
ample is the box constraint, which is of the form
ai ≤xi ≤bi
for i = 1, . . . , m,
where n1 = · · · = nm = 1, ai ∈[−∞, ∞), bi ∈(−∞, ∞], and ai ≤bi.


## Page 134

5.2
Coordinate and extended coordinate-friendly operators
119
5.2.2
Extended coordinate-friendly
An operator 핋: Rn →Rn is extended coordinate-friendly if there is an auxiliary
quantity y(x) such that
max
i=1,...,m F [{x, y(x)} 7→{핋ix, y(핋ix)}] ≪F [x 7→핋x] .
In other words, computing 핋i(x) is efficient so long as the auxiliary quantity y(x)
is maintained in memory.
More coordinate notation
We continue to use the notation x = (x1, . . . , xm) with xi ∈Rni for i = 1, . . . , m.
Given a matrix A ∈Rr×n, let
A:,i ∈Rr×ni
be the submatrix consisting of the columns of A corresponding to the ith block for
i = 1, . . . , m. So
A =

A:,1
· · ·
A:,m

.
Under this notation, we have
Ax = A:,1x1 + · · · + A:,mxm.
Write A⊺
:,i = (A:,i)⊺∈Rni×r for i = 1, . . . , m. When f is differentiable, we write
∇f(x) =


∇1f(x)
...
∇mf(x)

,
so (∇f(x))i = ∇if(x) for i = 1, . . . , m.
Example: Gradient descent on least squares
Consider the least-squares problem
minimize
x∈Rn
1
2∥Ax −b∥2,
where A ∈Rr×n and b ∈Rr. Consider the gradient descent operator
핋(x) = x −αA⊺(Ax −b).
When r ≪n, 핋is parallelizable and not coordinate-friendly, but extended coordinate-
friendly.
Without parallelization, evaluation of 핋costs
F[x 7→핋x] = O(rn).
핋is parallelizable assuming p ≤min{r, n} since
Fp[x 7→핋x] = Fp[{A, x} 7→Ax] + Fp[{A⊺, Ax} 7→A⊺(Ax)]
= O (rn/p).


## Page 135

120
5
Randomized coordinate update methods
핋is not coordinate-friendly since
F[x 7→핋ix] = F[x 7→Ax] + F[Ax 7→핋ix]
= O (rn) + O (rni)
= O (rn).
However, 핋is extended coordinate-friendly when we maintain the auxiliary quan-
tity Ax, since
F [{x, Ax} 7→{핋ix, A(핋ix)}] = O(rni)
if we use the formula
A(핋ix) = Ax + A:,i((핋x)i −xi).
Therefore, the C-FPI with 핋
xk+1
i(k) = xk
i(k) −αA⊺
:,i(k)(yk −b)
xk+1
j
= xk
j
for j̸ = i(k)
yk+1 = yk + A:,i(k)(xk+1
i(k) −xk
i(k))
costs O(rni(k)) flops per iteration. Note that the “step” xk+1
j
= xk
j for j̸ = i(k)
requires no flops. We initialize x0 = 0 and y = Ax0 = 0.
The other approach of precomputing A⊺A and A⊺b and using the formula
핋(x) = x−α((A⊺A)x−A⊺b) is not effective when, as before, r ≪n. Precomputing
F[{A, b} 7→{A⊺A, A⊺b}] = O
 rn2
can be prohibitively expensive, and
F[{xk, A⊺A, A⊺b} 7→xk+1
i(k) ] = O
 nni(k)

is larger than O
 rni(k)

.
5.3
Methods
In this section, we present several instances of the RC-FPI. When writing the
iterations, we only specify the updated block. It is implied that the selection rule
for i(k) is IID uniform and that the other blocks are not updated.
Coordinate gradient descent
Consider the problem
minimize
x∈Rn
f(x),


## Page 136

5.3
Methods
121
where f is differentiable. Then, the RC-FPI applied to 핀−α∇f is
xk+1
i(k) = xk
i(k) −α∇i(k)f(xk),
which is called the randomized/stochastic coordinate gradient descent/method. The
method converges if a minimizer exists, f is L-smooth, and α ∈(0, 2/L).
In general, 핀−α∇f need not be extended coordinate-friendly. However, one
setup from machine learning that does lead to an extended coordinate-friendly
operator is
f(x) =
r
X
j=1
ℓj(a⊺
j x −bj),
where a1, . . . , ar ∈Rn, b1, . . . , br ∈R, and ℓ1, . . . , ℓr are differentiable CCP func-
tions on R. When ℓj(x) = (1/2)x2 for j = 1, . . . , r, the problem reduces to the
familiar least-squares problem. Write
A =


— a⊺
1 —
...
— a⊺
r —

∈Rr×n,
ℓ(y) =
r
X
j=1
ℓj(yj).
Then
∇ℓ(x) = (ℓ′
1(x1), . . . , ℓ′
r(xr)).
Then, randomized coordinate gradient descent with yk = Axk
xk+1
i(k) = xk
i(k) −αA⊺
:,i(k)∇ℓ(yk −b)
yk+1 = yk + A:,i(k)(xk+1
i(k) −xk
i(k))
has cost per iteration of O
 rni(k)

, if maxj=1,...,r F[x 7→ℓ′
j(x)] = O(1).
Coordinate gradient descent with block-wise stepsize
Consider the problem
minimize
x∈Rn
f(x),
where f is L-smooth. For any diagonal matrix
D =


β1In1
β2In2
...
βmInm

,
where βi > 0 and Ini ∈Rni×ni is the ni × ni identity matrix for i = 1, . . . , m, the
stated problem is equivalent to
minimize
x∈Rn
f(Dx).


## Page 137

122
5
Randomized coordinate update methods
Randomized coordinate gradient method applied to the equivalent problem is
xk+1
i(k) = xk
i(k) −αi(k)∇i(k)f(xk),
where αi(k) = αβi(k). Using a non-uniform block-wise stepsize is usually necessary
for randomized coordinate gradient method to be faster than the (full deterministic)
gradient method in practice.
Coordinate proximal-gradient descent
Consider the problem
minimize
x∈Rn
f(x) +
m
X
i=1
gi(xi),
where f is CCP and differentiable and g1, . . . , gm are CCP. In other words, consider
the problem of minimizing the sum of a differentiable function and a separable
function. Write
g(x) =
m
X
i=1
gi(xi).
Since g is separable, so is Proxαg.
The RC-FPI with the FBS operator Proxαg(I −α∇f) is
xk+1
i(k) = Proxαgi(k)
 xk
i(k) −α∇i(k)f(xk)

,
which is called the coordinate proximal-gradient descent/method.
This method
converges if a minimizer exists, f is L-smooth, and α ∈(0, 2/L). With the same
block-wise stepsize argument, we can get
xk+1
i(k) = Proxαi(k)gi(k)
 xk
i(k) −αi(k)∇i(k)f(xk)

,
where α1, . . . , αm > 0. As before, it is important in practice to use non-uniform
block-wise stepsizes to achieve a speedup.
In general, when g is not separable, there is no way to implement the RC-FPI
with Proxαg(I −α∇f) efficiently. The evaluation of even a single coordinate of
Proxαg requires the full output of x −α∇f(x).
Stochastic dual coordinate ascent
Consider the problem
minimize
x∈Rr
g(x) +
n
X
i=1
ℓi(a⊺
i x −bi),
where g is a strongly convex CCP function on Rr (so g∗is smooth) and ℓi is a CCP
function on R for i = 1, . . . , n. Write
A =


— a⊺
1 —
...
— a⊺
n —

∈Rn×r,
b =


b1
...
bn

∈Rn.


## Page 138

5.3
Methods
123
This primal problem is generated by the Lagrangian
L(x, u) = g(x) + ⟨u, Ax −b⟩−
n
X
i=1
ℓ∗
i (ui).
The corresponding dual problem is
maximize
u∈Rn
−g∗(−A⊺u) −b⊺u −Pn
i=1 ℓ∗
i (ui).
The randomized coordinate proximal-gradient method applied to the dual prob-
lem is
uk+1
i(k) = Proxαi(k)ℓ∗
i(k)

uk
i(k) + αi(k)
 Ai(k),:∇g∗(yk) −bi(k)

yk+1 = yk −A⊺
i(k),:(uk+1
i(k) −uk
i(k)),
which is a variation of stochastic dual coordinate ascent (SDCA). Assume F[y 7→
∇g∗(y)] = O(r) and maxi=1,...,n F[u 7→Proxαiℓ∗
i (u)] = O(1). Then, the operator
is extended coordinate-friendly when we maintain yk = −A⊺uk, and we have a cost
of O
 rni(k)

per iteration. (One can recover the primal solution with ∇g∗(yk). See
Exercise 2.6.)
Note that each iteration of coordinate update to the dual accesses Ai(k),:, a
block of rows, while each iteration of coordinate update to the primal accesses
A:,i(k), a block of columns. In machine learning, a row of A is a training sample,
and it may be convenient to use it without splitting it into parts. In such cases,
the dual approach is preferred.
MISO/Finito
Consider the optimization problem
minimize
x∈Rn
r(x) + 1
m
m
X
i=1
fi(x),
where r, f1, . . . , fm are CCP and f1, . . . , fm are differentiable.
We use the consensus technique of §4.2.1 to get the equivalent problem
minimize
x∈Rnm
δC(x) +
m
X
i=1
 r(xi) + fi(xi)

,
where x = (x1, . . . , xm) and C is the consensus set (2.19). Write
f(x) =
m
X
i=1
fi(xi)
g(x) = δC(x) +
m
X
i=1
r(xi).


## Page 139

124
5
Randomized coordinate update methods
Using Exercise 2.29, we can evaluate Proxαg with
Proxαg(y1, . . . , ym) = (x, . . . , x),
x = Proxαr
 
1
m
m
X
i=1
yi
!
.
Both FBS and BFS operators are extended coordinate-friendly with the auxil-
iary quantity zk maintained. The RC-FPI with the BFS operator (핀−α∇f)Proxαg
is
xk = Proxαr

zk
zk+1
i(k) = xk −α∇fi(k)(xk)
zk+1 = zk + 1
m

zk+1
i(k) −zk
i(k)

.
The RC-FPI with the FBS operator Proxαg(핀−α∇f) is
xk+1
i(k) = Proxαr(zk)
zk+1 = zk + 1
m

xk+1
i(k) −xk
i(k) −α(∇fi(k)(xk+1
i(k) ) −∇fi(k)(xk
i(k)))

,
where zk =
1
m
Pm
i=1(xk
i −α∇fi(k)(xk
i )). These two methods are equivalent and
they are both called minimization by incremental surrogate optimization (MISO)
or Finito. They converge if a solution exists and α ∈(0, 2/L).
Of the two, the method from BFS has a minor and subtle advantage, as one
can initialize (z0
1, . . . , z0
m) = (0, . . . , 0) and z0 = 0 as the starting point. For the
method from FBS, the starting point (x0
1, . . . , x0
m) ∈Rnm can be arbitrary, but we
need to compute
z0 = 1
m
m
X
i=1
 x0
i −α∇fi(x0
i )

before starting the iterations.
Conic programs with many small cones
Consider the problem
minimize
x∈Rn
c⊺x
subject to
Ax = b
x ∈Q1 × · · · × Qm,
where Qi ⊆Rni is a nonempty closed convex set for i = 1, . . . , m, A ∈Rr×n has
rank r, and b ∈Rr. (The constraint is equivalent to xi ∈Qi for i = 1, . . . , m.)
When Q1, . . . , Qm are convex cones, this problem is called a conic program.
Consider the equivalent problem,
minimize
x∈Rn
c⊺x + δ{x | Ax=b}(x)
|
{z
}
=f(x)
+ δQ1×···×Qm(x).
|
{z
}
=g(x)


## Page 140

5.4
Discussion
125
A naive implementation of RC-FPI with DRS is
xk+1/2
i
= ΠQi(zk
i )
for i = 1, . . . , m
zk+1
i(k) = zk
i(k) + Di(k),:(2xk+1/2 −zk) + vi(k) −xk+1/2
i(k)
,
where D = I −A⊺(AA⊺)−1A and v = A⊺(AA⊺)−1b −αDc, as discussed in Ex-
ercise 2.25. Assume F[xi 7→ΠQixi] = Ci for i = 1, . . . , m. This method costs
O
 C1 + · · · + Cn + nni(k)

per iteration.
A better way is to utilize the extended coordinate-friendly structure with yk =
D2xk+1/2 −zk:
xk+1/2
i(k)
= ΠQi(k)(zk
i(k))
zk+1
i(k) = zk
i(k) + yk
i(k) + vi(k) −xk+1/2
i(k)
yk+1 = D:,i(k)

2ΠQi(k)(zk+1
i(k) ) −2xk+1/2
i(k)
−zk+1
i(k) + zk
i(k)

.
This implementation costs O
 Ci(k) + nni(k)

flops per iteration.
5.4
Discussion
In practice, RC-FPI may provide a greater speed than FPI when the operator is
extended coordinate-friendly and when RC-FPI uses coordinate-wise stepsizes that
are larger than the stepsize used by FPI.
When comparing RC-FPI and FPI, it is useful to compare one iteration of FPI
with m iterations of RC-FPI, which we call an epoch. In certain coordinate-friendly
setups, an epoch of RC-FPI and an iteration of FPI have similar computational
costs.
Theorems 1 and 2 guarantee a similar amount of reduction in fixed-point resid-
ual with one iteration of FPI and with one epoch of RC-FPI. However, this does not
necessarily mean one iteration of FPI and one epoch of RC-FPI actually make the
same amount of progress. In practice, RC-FPI and FPI often converge much faster
than what Theorems 1 and 2 guarantee. If so, the similarity in the guarantees does
not have much bearing on the similarity or difference of the actual performances.
When comparing optimization methods, the ability to use larger stepsizes often,
but not always, translates to a speedup. Loosely speaking, there are cases where
the stepsize limitation is the bottleneck of the algorithm, and alleviating it leads
to a speedup.
In some cases, there is theoretical support for this observation.
For example, an epoch of the randomized coordinate gradient method achieves
a greater reduction in function value than an iteration of the (deterministic full)
gradient method when different stepsizes are used for the different blocks. Such
analyses directly utilize the subgradient inequality (1.2) rather than the resulting
monotonicity inequality.
In general, RC-FPI may offer no speedup. There are empirical examples where
epochs of RC-FPI and iterations of FPI converge at the same rate. We are not


## Page 141

126
5
Randomized coordinate update methods
aware of any cases where epochs of RC-FPI make less progress than iterations of
FPI.
Nevertheless, studying RC-FPI without any guarantee of speedup is still useful,
since it serves as a precursor to the asynchronous FPI we discuss in §6. In parallel
computing, asynchrony can increase the number of iterations run per unit time.
Even if an epoch of asynchronous FPI makes the same amount of progress as an
iteration of FPI, asynchronous FPI can make more progress per unit time.


## Page 142

Bibliographical Notes
127
Bibliographical Notes
Coordinate update is a classical technique with a history almost as long as that of the field
of optimization itself. The technique has enjoyed increased popularity in recent years due
to the rising demand for large-scale optimization. As a complete survey of the subject
is beyond the scope of this section, we refer interested readers to the following recent
reviews. Lange, Chi, and Zhou’s 2014 paper [LCZ14] provides a review from a statistician’s
perspective; Wright’s 2015 paper [Wri15] gives an in-depth review of coordinate descent
methods; Shi, Tu, Xu, and Yin’s 2016 paper [STXY17] also provides thorough review on
coordinate descent methods; and Peng et al.’s 2016 paper [PWX+16] provides a thorough
review of coordinate update methods.
Coordinate descent and coordinate update methods.
Coordinate descent methods
date back to Hildreth’s 1957 work using the cyclic coordinate selection rule [Hil57]. By
coordinate “descent” methods, we refer to unconstrained optimization methods that re-
duce (descend) the function value by updating one coordinate at a time [D’E59, War63,
LT92, GS00, Tse01, BT13]. Variations of coordinate descent methods include proximal
coordinate descent methods [Aus92, GS00, RHL13, XY13], which update one coordinate
at a time in a proximal-point setup, and prox-linear coordinate descent methods [TY09,
YT11, YTT11, Nes12, BT13, XY13, SXB14, XY17, FR15, Xu15, ZXC+16, HWRL17],
which perform a forward-backward-type update, one coordinate at a time.
Verkama’s 1996 work using a randomized coordinate update for fixed-point iterations
is the first instance of coordinate update methods [Ver96]. We use the term coordinate
update for methods solving constrained optimization problems by updating one coordinate
at a time [PR15, ZX15, ZX17, PWX+16, GXZ19, XYLC19]. As such methods are usually
primal-dual, they do not monotonically “descend” in function value. A general framework
of RC-FPI was set up by Combettes and Pesquet in 2015 and 2018 [CP15, CP19], and,
in fact, the proof of Theorem 2 closely follows the presentation of [CP15].
The notion of coordinate-friendly operators was first articulated by Peng et al. in 2016
[PWX+16], although the notion had been implicitly used in many prior works. Stochastic
dual coordinate ascent was presented in [SZ13].
MISO/Finito was independently pre-
sented in [Mai13, DDC14], and further convergence analysis was presented in [QSMR19].
Coordinate selection rules.
For a thorough review of the vast literature on coordinate
selection rules, see the 2016 paper by Shi, Tu, Xu, and Yin [STXY17]. The various coor-
dinate selection rules considered in the literature include the cyclic selection rule [D’E59,
Zad70, LT92, GS00, TY09, Bon11, BT13, HWRL17, RHL13, ST13, XY17, SH15, SY21];
IID uniform random selection rule [ST09, ST11, Nes12, SZ13, RT14, FR15]; independent
and random but non-uniform selection rule (also referred to as “arbitrary sampling”)
[RT14, PN15, RT16, QR16a, QR16b]; independent and random but non-uniform selection
rules with probabilities inversely proportional to the coordinate-wise Lipschitz constants
(also referred to as “importance sampling”) [Zha04, LL10, Nes12, RT14, ZX15, ZX17];
random permutation selection rules that access the coordinates in a cyclic fashion but
with the order shuffled every epoch [LW19, NJN19, HS19, SY21, SLY20, WL20, RGP20];
and greedy selection rules [Tse90a, LT92, SK03, WL08, LO09, TY09, DRT11, CHLZ12,
PYY13, NSL+15, LUZ15].


## Page 143

128
5
Randomized coordinate update methods
Exercises
5.1 The RC-FPI can be generalized to the setup where p agents independently and randomly
select and update indices.
Define 핊i = 핀−핋i for i = 1, . . . , m. The method parallel RC-FPI is
i(k, w) ∼IID Uniform{1, . . . , m}
for w = 1, . . . , p
xk+1 = xk −
p
X
w=1
핊i(k,w)(xk).
The computation of 핊i(k,1)(xk), . . . , 핊i(k,p)(xk) can be parallelized by p computational
agents. We do not require i(k, 1), . . . , i(k, p) to be distinct. Prove convergence for parallel
RC-FPI.
5.2 Projection onto second-order cone. Consider the second-order cone
Q =

x ∈Rn 
q
x2
1 + · · · + x2
n−1 ≤xn

.
Write x1:(n−1) = (x1, . . . , xn−1). Show that ΠQ(x) = (ρ(x)x1:(n−1), σ(x)xn), where the
coefficients ρ(x), σ(x) are given by
(ρ(x), σ(x)) =







(0, 0)
if −∥x1:(n−1)∥≥xn
(1, 1)
if ∥x1:(n−1)∥≤xn
1
2(∥x1:(n−1)∥+ xn)

1
∥x1:(n−1)∥,
1
xn

otherwise.
5.3 Non-uniform selection rules. Assume i(k) is an IID random variable with Prob[i(k) =
j] = pj, where p1, . . . , pm > 0 and p1 + · · · + pm = 1. Assume T is θ-averaged, θ ∈(0, 1),
and Fix T̸ = ∅. Define Sj = I −Tj for j = 1, . . . , m. Modify the proof of Theorem 2 to
show that
xk+1 = xk −
α
pi(k)
Si(k)(xk)
converges. Provide a condition on α that ensures convergence.
5.4 Coordinate minimization can fail.
Generally speaking, the approach of updating one
coordinate at a time does not always work. Consider the problem
minimize
f(x1, . . . , xm),
where f is a CCP function. The method coordinate minimization can be described as
xk+1
i(k) ∈
argmin
zi(k)∈Rni(k)
f(xk
1, . . . , xk
i(k)−1, zi(k), xk
i(k)+1, . . . , xk
m),
where i(k) is chosen with some selection rule. Coordinate minimization converges under
very general assumptions, but such assumptions require f to be differentiable.
Consider the counterexample, g : R2 →R, defined as g(x, y) = |x + y| + 2|x −y|. First,
show that g is a CCP function with the unique minimizer (0, 0). Then, show that any
(β, β), where β ∈R, is a fixed point of the coordinate minimization method. Finally,
show that
∂g̸ =
∂xg
∂yg

,
where ∂x is the subdifferential with respect to x while y is fixed, and vice versa.


## Page 144

Exercises
129
5.5 Logistic regression with MISO/Finito. Consider the problem
minimize
x∈Rn
m
X
j=1
log(1 + exp(−yja⊺
jx)),
where a1, . . . , am ∈Rn and y1, . . . , ym ∈{−1, +1}. Describe gradient descent and MIS-
O/Finito applied to this problem. What are their flop counts per iteration?


## Page 145

130
5
Randomized coordinate update methods


## Page 146

Chapter 6
Asynchronous coordinate
update methods
Let 핋: Rn →Rn be a θ-averaged operator and define 핊: Rn →Rn with 핋= 핀−θ핊.
Partition x ∈Rn into m blocks (x1, . . . , xm) and define 핋1, . . . , 핋m as we did in
§5.1. Define 핊i : Rn →Rn with 핋i = 핀−θ핊i for i = 1, . . . , m. We can implement
xk+1 = xk −η핊xk,
where η > 0, with multiple computational agents simultaneously running the fol-
lowing code:
// p agents run the while loop simultaneously
// x and s are vectors in shared memory
WHILE (not converged) {
1. WHILE (not all indices processed) {
Select index i not yet processed
Read x
Write s[i] = eta*S[i](x)
}
2. Synchronize: wait for all agents
-------------------------------------------------------
3. WHILE (not all indices processed) {
Select index i not yet processed
Write x[i] = x[i] - s[i]
}
4. Synchronize: wait for all agents
-------------------------------------------------------
}
This algorithm (deterministically) computes the iteration xk+1 = xk −η핊xk. We
call Steps 2 and 4 synchronization barriers, and we say the algorithm is synchronous
parallel.
Step 1 reads from, but does not write to the variable x. Step 3 reads from
and writes to the variable x. Step 2 prevents agents finished with Step 1 from


## Page 147

132
6
Asynchronous coordinate update methods
proceeding to Step 3 and changing x while the other agents are still using x in Step
1. Similarly, Step 4 prevents agents finished with Step 3 from proceeding to Step 1
and reading x while other agents are still changing x. The synchronization barriers
of Steps 2 and 4 divide the outer while-loop into two parts; at a given time all
agents are in Steps 1–2 or all agents are in Steps 3–4.
Cost of synchrony
Synchronization barriers can be a significant computational overhead. When the
number of computing agents is large, it becomes difficult to ensure all parallel tasks
start and end at the same time. In distributed computing, agents are often not
equally powerful. In a modern multitasking system, agents may not be equally
available. When there are faster and slower agents, the faster ones will wait idly
for the slower ones. Furthermore, the synchronization barrier is itself an algorithm
with a cost.
Communication congestion is another cost of synchrony. In our chapter-opening
algorithm, multiple agents simultaneously write data in Steps 1 and 3. Writing
requires accessing memory and, in a distributed system, communication over a
network. Although modern systems allow multiple agents to share the bandwidths
of memory and network, simultaneous communication can cause congestion and
slowdown.
As the number of computing agents increases, the cost of synchrony quickly
becomes a significant factor in obtaining scalable parallel methods.
Asynchronous parallelism
We say an algorithm is asynchronous parallel if it avoids synchronization barriers.
Let us simply remove the synchronization barriers of the previous algorithm:
// p agents run the while loop asynchronously
// x and s are vectors in shared memory
WHILE (not converged) {
1. Select i from Uniform{1,2,...,m}
2. Read x
3. Compute s[i] = eta*S[i](x)
4. Write x[i] = x[i] - s[i] //Incorrect!
}
Now the agents run in a completely uncoordinated fashion, and the computational
cost and inefficiency of synchronization are eliminated. (The computations of the
agents are still related through the shared variable x.) Now, the number of updates
performed is determined by the aggregate computing power and bandwidths rather
than the slowest agent and the worst bottleneck.
However, does this algorithm work? In general, simply removing synchroniza-
tion barriers does not lead to a working asynchronous method. The asynchrony
must be carefully considered and designed around.
This algorithm implements neither the FPI xk+1 = (핀−η핊)xk nor the RC-FPI
xk+1 = (핀−η핊i(k))xk. By the time an agent is ready to perform Step 4, other agents
may have updated x, rendering the value of x used to compute Step 3 outdated.


## Page 148

6.1
Asynchronous fixed-point iteration
133
In this case, we say the information is stale.
We soon see that we can account for the impact of stale information in the
convergence analysis when we enforce exclusive access in Step 4. We say an agent
has exclusive access to a variable stored in shared memory if no other agent can
read from or write to it simultaneously.
6.1
Asynchronous fixed-point iteration
We first present the asynchronous coordinate-update fixed-point iteration (AC-FPI)
with an operational definition:
// p agents run the while loop asynchronously
// x and s are vectors in shared memory
WHILE (not converged) {
1. Select i from Uniform{1,2,...,m}
2. Read x
3. Compute s[i] = eta*S[i](x)
4. Exclusively read x[i] and write x[i] = x[i] - s[i]
}
While an agent is updating the block x[i] in Step 4, other agents cannot access
x[i]. Exclusive access can be implemented with standard parallel computing tech-
niques such as atomic operations, mutexes, or semaphores. If (핊x)i depends on only
some components of x, Step 2 needs to read only the necessary parts of x.
AC-FPI removes explicit synchronization barriers, although it still requires ex-
clusive access in writing to the individual blocks of xk. When there are many more
blocks than agents, i.e., p ≪m, it is rare for an agent to wait for the release of a
block’s exclusive access, and most, albeit not all, idle time is eliminated.
To mathematically analyze the AC-FPI, we need a mathematical definition.
For asynchronous algorithms, there is more than one valid approach to defining
the “iterates.” We present one here, and Exercise 6.5 presents another.
Define x0 to be the state of x before the start of the algorithm. Write xk =
(xk
1, . . . , xk
m) for the kth iterate and define the iteration count to increment by 1
when an agent completes an update of x in global memory, i.e., when an agent
completes Step 4. When the iteration counter is incremented to k, if no agent is
updating (i.e., writing to) x[j], then xk
j is the state of x[j] at that time; and
if an agent is updating x[j], then xk
j is what x[j] used to be right before the
agent currently writing to the block started the update. See Figure 6.1. If two
or more agents finish updating different blocks at the same time, we break the tie
arbitrarily. (The exclusive access of Step 4 prevents multiple agents from updating
the same block concurrently. However, different agents may concurrently update
different blocks.)
Write i(k) for the index of the kth update. As in §5, we consider the IID random
coordinate selection rule as it leads to the simplest theoretical analysis.
As we have discussed, the value of x read in Step 2 may become stale by the
time the agent performs Step 4. Write ˆxk for the stale value of x used for the


## Page 149

134
6
Asynchronous coordinate update methods
kth write completed
Block 5
Block 4
Block 3
Block 2
Block 1
x[5]
x[4]
x[3]
x[2]
x[1]
Agent 2 write
Agent 4 read
Agent 6 write
Agent 1 write
Agent 3 read
Agent 8 write
Agent 5 write
xk
1
Undefined
Undefined
xk
2
Undefined
xk
3
xk
4
Undefined
Undefined
xk
5
Iteration count
k −1
k
k + 1 k + 2
k + 3
Figure 6.1: The iterate xk is defined at the time when Agent 2 completes writing
to Block 1. Since Blocks 3 and 4 are not being updated at that time, xk
3 and xk
4 are
the state of x[3] and x[4] at the time. Since Blocks 2 and 5 are being updated at
the time, xk
2 and xk
5 are the state of x[2] and x[5] before the writes had begun.


## Page 150

6.1
Asynchronous fixed-point iteration
135
update of xk to xk+1. In other words, xk+1 = xk −η핊i(k)ˆxk. It is possible that
ˆxk̸ = xℓfor any ℓ= 0, . . . , k since other agents can update blocks while ˆxk is being
read block-by-block in Step 2. We discuss this issue further in §6.2 and illustrate
it in Figure 6.2. In Step 4, each block is accessed exclusively, but the entire x is
not. Therefore, we consider a coordinate-by-coordinate notion of staleness. Write
ˆxk =
 xk−d1(k)
1
, . . . , xk−dm(k)
m

,
to denote that the ith block of ˆxk is outdated by di(k) ≥0 iterations for i =
1, . . . , m. We call d1(k), . . . , dm(k) the block delays. We call
d(k) = (d1(k), . . . , dm(k)) ∈Nm
+
the vector delay and write ˆxk = xk−d(k).
Finally, we write the mathematical definition of the AC-FPI:
xk+1 = xk −η핊i(k)xk−d(k).
(6.1)
AC-FPI is a stochastic algorithm realized by the random variables i(0), i(1), . . . and
d(0), d(1), . . . . Randomness of the indices i(0), i(1), . . . is injected by design; they
come from the random selection of Step 1. Randomness of the delays d(0), d(1), . . .
comes from the randomness of i(0), i(1), . . . and the randomness of the agents’
computation time.
ARock and convergence of the AC-FPI
The AC-FPI is very general. The update xk+1 = xk −η핊i(k)xk−d(k) models many
asynchronous algorithms considered in the literature with consistent reads and
writes, which we discuss further in §6.2. We broadly refer to all such methods as
instances of the AC-FPI.
We analyze a particular instance of AC-FPI, which we call ARock. We call the
following assumptions the ARock assumptions:
• i(0), i(1), . . . are independently and identically distributed with uniform prob-
ability,
• i(k) and d(ℓ) are mutually independent for k = 0, 1, . . . and ℓ≤k, and
• d(0), d(1), . . . is a stochastic process with nonincreasing Q0, Q1, . . . ∈[0, 1]
such that for every k = 0, 1, . . . ,
Prob

max
i=1,...,m di(k) ≥ℓ
 d(k −1), . . . , d(0), i(k −1), . . . , i(0)

≤Qℓ,
∞
X
ℓ=1
ℓ(Qℓ)1/2 < ∞.
(6.2)
This summability assumption is very mild. See Exercise 6.2.


## Page 151

136
6
Asynchronous coordinate update methods
Theorem 3Assume 핊: Rn →Rn is (1/2)-cocoercive or, equivalently, that 핋= 핀−θ핊
is θ-averaged with θ ∈(0, 1). Assume Fix 핋̸ = ∅. Under the ARock assumptions,
the AC-FPI xk+1 = xk−η핊i(k)xk−d(k) with any starting point x0 ∈Rn and stepsize
η obeying
0 < η <
 
1 +
2
√m
∞
X
ℓ=1
Q1/2
ℓ
!−1
converges to one fixed point with probability 1, i.e.,
xk →x⋆
with probability 1 for some x⋆∈Fix 핋. Furthermore, with probability 1,
dist(xk, Fix 핋) →0.
Given a fixed distribution of delays, i.e., fixed values of Q0, Q1, . . . , larger m is
more favorable. The interpretation is that the staleness becomes less harmful as
the number of blocks grows. In fact, if we let m →∞with fixed Q0, Q1, . . . , the
stepsize requirement of Theorem 3 becomes the same as that of Theorem 2.
In practice, staleness may cause AC-FPI to make less progress per iteration,
although convergence is ensured by Theorem 3. Therefore, synchronous and asyn-
chronous parallel methods represent a trade-off between better and faster iterations.
6.1.1
Discussion of assumptions
Exclusive access
In the operational definition of the AC-FPI, Step 4 requires exclusive access. Oth-
erwise, we would not be able to use the notation
ˆxk = xk−d(k) = (xk−d1(k)
1
, . . . , xk−dm(k)
m
),
as an agent can read a block while another agent is halfway through writing to it.
Independence
We do not assume d(0), d(1), . . . is an independent sequence; it usually is a depen-
dent sequence. For example, it is likely that ˆxk and ˆxk+1 are read at close points
in time, and this makes d(k) and d(k + 1) highly correlated.
We do not assume i(k) and d(ℓ) are independent for k < ℓ; they usually are
dependent. For example, if i(k) = j, then dj(k + 1) > 0 is very likely.
We do assume that the sequence i(0), i(1), . . . is IID. When index i is sampled
in Step 1 of the AC-FPI, we do not yet know which iteration count k the index
will be associated with. If the blocks have non-uniform computational costs, the
choice of index affects the iteration count the update is assigned to and the IID


## Page 152

6.1
Asynchronous fixed-point iteration
137
assumption is violated. For example, if the jth block takes longer to compute,
then i(0) = j will have a lower probability than, say, i(1000) = j.
When the
computational cost of each block is equal, then the IID sampling of Step 1 makes
i(0), i(1), . . . an IID sequence.
We do assume i(k) and d(k) are independent for k = 0, 1, . . . . This is realistic
if the computational costs of the blocks are uniform. On the other hand, if, for
example, the jth block is much more expensive to compute than others and i(k) =
j, then it is likely that d(k) contains large delays.
Delays
A common assumption in the literature is that the delays are bounded:
max{d1(k), . . . , dm(k)} ≤D
for k = 0, 1, . . .
for some D < ∞. While this bounded-delay assumption would simplify Stage 2
of our proof of Theorem 3, it is not necessary. Therefore, we do not make this
assumption.
6.1.2
Proof of Theorem 3
Proof. Write E for the total expectation. Write Ei(k) for the expectation over i(k)
conditioned on d(k), . . . , d(0), i(k−1), . . . , i(0). Write Ed(k) for the expectation over
d(k) conditioned on d(k −1), . . . , d(0), i(k −1), . . . , i(0). Write Ei(k),d(k) for the
expectation over i(k) and d(k) conditioned on d(k −1), . . . , d(0), i(k −1), . . . , i(0).
Note that the random variables d(k −1), . . . , d(0), i(k −1), . . . , i(0) completely
determine xk, . . . , x1.
Stage 1.
We define the Lyapunov function
V k = ∥xk −x⋆∥2 + 1
m
∞
X
d=1
cd∥xk−d+1 −xk−d∥2,
where x⋆∈Fix 핋. We set x0 = x−1 = x−2 = · · · , which effectively truncates
the sum to be finite. The coefficients cd ≥0 for d = 0, 1, . . . will be determined
later. Clearly, V k ≥0. We have V k < ∞since the infinite sum has only finitely
many nonzero terms for a fixed k < ∞. As an aside, if one assumes the delays are
bounded, the infinite sum can be replaced with a finite sum. The first stage of the
proof is to show the key inequality
Ei(k),d(k)V k+1 ≤V k −η
m
 
1 −η
 
1 +
2
√m
∞
X
d=1
Q1/2
d
!!
Ed(k)∥핊xk−d(k)∥2. (6.3)
Using the mathematical definition of AC-FPI, we have
∥xk+1 −x⋆∥2 = ∥xk −η핊i(k)xk−d(k) −x⋆∥2
= ∥xk −x⋆∥2 −2η⟨핊i(k)xk−d(k), xk −x⋆⟩+ η2∥핊i(k)xk−d(k)∥2.


## Page 153

138
6
Asynchronous coordinate update methods
The independence between i(k) and d(k) gives us
Ei(k)핊i(k)xk−d(k) = 1
m핊xk−d(k),
Ei(k)∥핊i(k)xk−d(k)∥2 = 1
m∥핊xk−d(k)∥2.
Therefore,
Ei(k)∥xk+1 −x⋆∥2 = ∥xk −x⋆∥2 −2η
m ⟨핊xk−d(k), xk −x⋆⟩+ η2
m ∥핊xk−d(k)∥2. (6.4)
Using (1/2)-cocoercivity of 핊, bound the inner-product term as
−2⟨핊xk−d(k), xk −x⋆⟩= −2⟨핊xk−d(k), xk−d(k) −x⋆⟩−2⟨핊xk−d(k), xk −xk−d(k)⟩
≤−∥핊xk−d(k)∥2 −2⟨핊xk−d(k), xk −xk−d(k)⟩.
(6.5)
Since the blocks have different delays, we decompose the second term of (6.5) over
the blocks as
−2⟨핊xk−d(k), xk −xk−d(k)⟩= 2
m
X
i=1
⟨(−핊xk−d(k))i, xk
i −xk−di(k)
i
⟩
=
m
X
i=1
di(k)
X
d=1
2⟨(−핊xk−d(k))i, xk−d+1
i
−xk−d
i
⟩.
For each term in the summation, we apply Young’s inquality
−2⟨u, v⟩≤1
ε∥u∥2 + ε∥v∥2
∀ε > 0
to get
2⟨(−핊xk−d(k))i, xk−d+1
i
−xk−d
i
⟩≤η
εd
∥(핊xk−d(k))i∥2 + εd
η ∥xk−d+1
i
−xk−d
i
∥2,
where we choose εd > 0 later. Define τ(k) = maxi=1,...,m di(k). Using di(k) ≤τ(k)
and swapping the orders of sums, we get
−2⟨핊xk−d(k), xk −xk−d(k)⟩
≤
m
X
i=1
τ(k)
X
d=1
 η
εd
∥(핊xk−d(k))i∥2 + εd
η ∥xk−d+1
i
−xk−d
i
∥2

= η


τ(k)
X
d=1
ε−1
d

∥핊xk−d(k)∥2 + 1
η


τ(k)
X
d=1
εd∥xk−d+1 −xk−d∥2

.
(6.6)
Substituting (6.6) into (6.5) and substituting (6.5) into (6.4), we get
Ei(k)∥xk+1 −x⋆∥2 ≤∥xk −x⋆∥2 −η
m

1 −η −η
τ(k)
X
d=1
ε−1
d

∥핊xk−d(k)∥2
+ 1
m
τ(k)
X
d=1
εd∥xk−d+1 −xk−d∥2.
(6.7)


## Page 154

6.1
Asynchronous fixed-point iteration
139
By the definition of V k,
Ei(k)V k+1 = Ei(k)∥xk+1 −x⋆∥2 + 1
mEi(k)
∞
X
d=1
cd∥xk−d+2 −xk−d+1∥2
= Ei(k)∥xk+1 −x⋆∥2 + c1
mEi(k)∥xk+1 −xk∥2 + 1
m
∞
X
d=2
cd∥xk−d+2 −xk−d+1∥2.
We bound Ei(k)∥xk+1 −x⋆∥2 by (6.7), substitute
Ei(k)∥xk+1 −xk∥2 = Ei(k)∥η핊i(k)xk−d(k)∥2 = η2
m ∥핊xk−d(k)∥2,
and decrement the summation index to get
Ei(k)V k+1 ≤(RHS of (6.7)) + c1η2
m2 ∥핊xk−d(k)∥2 + 1
m
∞
X
d=1
cd+1∥xk−d+1 −xk−d∥2
= ∥xk −x⋆∥2 −η
m

1 −η −c1η
m −η
τ(k)
X
d=1
ε−1
d

∥핊xk−d(k)∥2
+ 1
m


τ(k)
X
d=1
εd∥xk−d+1 −xk−d∥2 +
∞
X
d=1
cd+1∥xk−d+1 −xk−d∥2

.
We now choose
εd = m1/2
Q1/2
d
and
cd =
∞
X
ℓ=d
εℓQℓ= m1/2
∞
X
ℓ=d
Qℓ
1/2,
d = 1, 2, . . . .
By the assumption (6.2), cd < ∞for all d. Since
Ed(k)
τ(k)
X
d=1
εd∥xk−d+1 −xk−d∥2 =
∞
X
ℓ=1
Prob[τ(k) = ℓ]
ℓ
X
d=1
εd∥xk−d+1 −xk−d∥2
=
∞
X
d=1
εdProb[τ(k) ≥d]∥xk−d+1 −xk−d∥2
≤
∞
X
d=1
εdQd∥xk−d+1 −xk−d∥2


## Page 155

140
6
Asynchronous coordinate update methods
and since cd = εdQd + cd+1, we obtain
Ei(k),d(k)V k+1 ≤∥xk −x⋆∥2 −η
mEd(k)



1 −η −c1η
m −η
τ(k)
X
d=1
ε−1
d

∥핊xk−d(k)∥2


+ 1
m
∞
X
d=1
cd∥xk−d+1 −xk−d∥2,
≤V k −η
m
 
1 −η −c1η
m −η
∞
X
d=1
ε−1
d
!
Ed(k)∥핊xk−d(k)∥2,
= V k −η
m
 
1 −η
 
1 +
2
√m
∞
X
d=1
Q1/2
d
!!
|
{z
}
>0 by assumption on η in Theorem 3.
Ed(k)∥핊xk−d(k)∥2,
which is (6.3).
As an aside, the coefficients cd and εd are carefully chosen to
construct the Lyapunov function, rather than being given by the algorithm or the
assumptions.
Stage 2.
To make the dependence on x⋆∈Fix 핋explicit, write
V k(x⋆) = ∥xk −x⋆∥2 + 1
m
∞
X
d=1
cd∥xk−d+1 −xk−d∥2.
We apply Theorem 29, the supermartingale convergence theorem, to (6.3), apply
the arguments of Proposition 1, and use ∥xk −x⋆∥2 ≤V k to get
(i) Ed(k)∥핊xk−d(k)∥2 →0,
(ii) V k(x⋆) →V ∞(x⋆) for all x⋆∈Fix 핋,
(iii) ∥xk∥< B for all k = 0, 1, . . . for some B < ∞,
with probability 1.
Write Fk for the σ-algebra generated by d(k), . . . , d(0), i(k), . . . , i(0). Let L > 0
be large enough such that 1 −QL > 0, which exists by assumption (6.2). This
implies
Prob

max
i=1,...,m di(k) < L
 Fk−1

≥1 −QL > 0
for all k = 0, 1, . . . . Let b(k) be an Fk−1-measurable random variable defined as
b(k) = argmax
b<L

Prob

d(k) = b
 Fk−1
	
,
where argmaxb<L is the maximizer over all b = (b1, . . . , bm) ∈Nm
+ satisfying
maxi=1,...,m bi < L. When the argmax is not unique, we break ties in some de-
terministic manner, say with the lexicographical ordering on Nm
+. Then
Prob

d(k) = b(k)
 Fk−1

≥1 −QL
Lm
> 0


## Page 156

6.1
Asynchronous fixed-point iteration
141
since the event maxi=1,...,m di(k) < L has probability at least 1 −QL with Lm
possible realizations of d(k), and b(k) is defined as the most likely among the real-
izations. By the second Borel–Cantelli lemma, version II [Dur10, Theorem 5.3.2],
for each D ∈N+, there exists a subsequence kj →∞such that d(kj +ℓ) = b(kj +ℓ)
for ℓ= 0, 1, . . . , D −1. Since xkj is bounded by (iii), there is a further subsequence
k′
j →∞such that xk′
j →¯x.
By (i), we have
Ed(k)∥핊xk−d(k)∥2
|
{z
}
→0
= E
h
∥핊xk−d(k)∥2  Fk−1
i
≥E
h
1{d(k)=b(k)}∥핊xk−b(k)∥2  Fk−1
i
≥1 −QL
Lm
∥핊xk−b(k)∥2 →0
as k →∞, so ∥핊xk−b(k)∥2 →0. Since
∥xk′
j+ℓ+1 −xk′
j+ℓ∥2 = η2∥핊i(k′
j+ℓ)xk′
j+ℓ−b(k′
j+ℓ)∥2 ≤η2∥핊xk′
j+ℓ−b(k′
j+ℓ)∥2 →0
for ℓ= 0, 1, . . . , D −1, we have
(xk′
j, xk′
j+1, . . . , xk′
j+D−1) →(¯x, ¯x, . . . , ¯x) ∈(Rn)D.
If D > L, then xk′
j+D−1−b(k′
j+D−1) →¯x, and 핊xk′
j+D−1−b(k′
j+D−1) →0 implies
핊¯x = 0 by continuity of 핊.
Stage 3.
Given D ∈N+ such that D > L, consider a subsequence kj →∞such
that
(xkj, xkj+1, . . . , xkj+(D−1)) →(¯xD, ¯xD, . . . , ¯xD) ∈(Rn)D.
We write ¯xD to make explicit the fact that the limit may depend on the choice of
D. Since
V kj(¯xD) →V ∞(¯xD)
by (ii), we have
V ∞(¯xD) = lim
kj→∞
1
m
∞
X
d=D
cd∥xkj−d+D+1 −xkj−d+D∥2 ≤2B2
m
∞
X
d=D
cd.
Therefore
lim sup
k→∞
∥xk −¯xD∥2 ≤lim
k→∞V k(¯xD) ≤2B2
m
∞
X
d=D
cd.
(6.8)
By (6.2), we have
∞
X
d=1
cd = m1/2
∞
X
d=1
∞
X
ℓ=d
Qℓ
1/2 = m1/2
∞
X
ℓ=1
ℓQℓ
1/2 < ∞.
Therefore,
∞
X
d=D
cd →0
as D →∞.
For any D ∈N+, (6.8) implies the accumulation points of xk reside in the closed
ball centered at ¯xD with a radius that goes to 0 as D →∞. The intersection of
these balls contains a single accumulation point x∞. (The intersection cannot be
empty, as the bounded sequence xk must have at least one accumulation point.)


## Page 157

142
6
Asynchronous coordinate update methods
6.2
Extended coordinate-friendly operators and exclusive
memory access
Let 핋: Rn →Rn be an extended coordinate-friendly operator with the auxiliary
quantity y(x). Throughout this section, consider the specific case y(x) = Ax. We
can compute xk+1 = 핋xk with the following parallel synchronous algorithm:
// multiple agents run the while loop simultaneously
// x, y, and s in shared memory
// S=(1/theta)*(I-T)
WHILE (not converged) {
1. WHILE (not all indices processed) {
Select index i not yet processed
Read x,y
Compute s[i] = eta*S[i](x) using y
}
2. Synchronize: wait for all agents to finish
-------------------------------------------------------
3. WHILE (not all indices processed) {
a. Select index i not yet processed
b. y = y - A[:,i]*s[i] (Sequential , any order)
c. x[i] = x[i] - s[i]
}
4. Synchronize: wait for all agents to finish
-------------------------------------------------------
}
We require Step 3b to be sequential so that two or more agents do not overwrite
each other’s updates. Step 3b can be parallelized by concurrently updating different
coordinates of y. As long as each component is sequentially updated, the algorithm
is correct.
Now consider removing the synchronization barrier:
// p agents run the while loop asynchronously
// x, y, and s in shared memory
WHILE (not converged) {
Select i from Uniform{1,2,...,m}
Read x,y
Compute s[i] = eta*S[i](x) using y
Read y and write y = y - A[:,i]*s[i] //Incorrect!
Exclusively read x[i] and write x[i] = x[i] - s[i]
}
This method is not an instance of ARock, due to race conditions. A race condition
is a negative behavior of a parallel method whose result depends on the order in
which the agents complete their tasks.
In particular, reads and writes on y can be inconsistent. If an agent reads a
block of memory while another agent writes to it, the read may retrieve partially
old, partially new data. This race condition is called an inconsistent read. See


## Page 158

6.2
Extended coordinate-friendly operators and exclusive memory access
143
y[4]
y[3]
y[2]
y[1]
0
0
0
0
0
0
0
1
0
0
1
1
0
1
1
1
1
1
1
1
Agent 2
Agent 1
write y[1]
write y[2]
write y[3]
write y[4]
1
1
1
1
read y[1]
read y[2]
read y[3]
read y[4]
1
1
0
1
Time
Figure 6.2: Example of an inconsistent read. Agent 2 reads y=[1,1,0,1], which
was never an actual state of y in memory. AC-FPI requires consistent reads within
a single block but does allow inconsistent reads on x across different blocks. (The
delay within a single block must be the same, but different blocks may have different
delays.)
Figure 6.2. When two agents write to the same block of memory, they may over-
write one another, resulting in data partially from one agent and partially from the
other. This race condition is called an inconsistent write. See Figure 6.3. We can
prevent inconsistent reads and writes by enforcing exclusive access of the block of
memory an agent is writing to. When multiple agents read from the same block
of memory but none are writing to it, there is no need for exclusive access. In this
algorithm, exclusive access on y can prevent inconsistent reads and writes.
Inconsistency between x and y is another possible race condition.
For this
method to be an instance of ARock, the x and y that an agent reads must be
related through the relationship y=A*x. This may fail to hold if x and y are updated
separately. We can prevent this by enforcing exclusive access for the whole (x,y)
pair:
// p agents run the while loop asynchronously
// x, y, and s in shared memory
WHILE (not converged) {
1. Select i from Uniform{1,2,...,m}
2. Read x,y
3. Compute s[i] = eta*S[i](x) using y
4. dy[i] = A[:,i]*s[i]
5. Acquire exclusive access to (x,y)
6. Read y and write y = y - dy[i]
Read x[i] and write x[i] = x[i] - s[i]
7. Release exclusive access to (x,y)


## Page 159

144
6
Asynchronous coordinate update methods
y[3]
y[2]
y[1]
0
0
0
0
0
1
0
0
2
0
2
2
2
1
2
1
1
2
Agent 2
Agent 1
Write y[1]
Write y[2]
Write y[3]
1
1
1
Write y[1]
Write y[2]
Write y[3]
2
2
2
Time
Figure 6.3: Example of an inconsistent write. The two writes of Agents 1 and 2
partially overwrite each other, and y=[2,1,1] is the resulting state. An inconsis-
tent write can occur when multiple agents attempt to concurrently write to the
same block. We enforce exclusive access to prevent inconsistent writes.
}
In some setups, exclusive access of Steps 5 through 7 can be a bottleneck. On
a case-by-case basis, it may be possible to perform a specialized analysis to allow
for inconsistency between x and y.
6.3
Server-worker framework
The discussion so far has been based on a shared memory system, where multiple
agents freely access variables stored in shared memory. A single computer with a
multicore CPU is modeled well by a shared memory system.
In the server-worker framework, a server, or parameter server, is a dedicated
agent that collects, updates, and distributes variables over a network connected to
workers, the computational agents working in parallel. The parameter server can
also perform minimal computation, so long as the server can keep up with the total
throughput of the workers. A cluster of multiple computers connected to a central
server node over a network is modeled well by the parameter server framework.
We can use one server and m workers to compute xk+1 = xk −η핊xk syn-
chronously: the server runs
// Server code
WHILE (not converged) {
Broadcast x to workers
WHILE (not all indices processed) {
Pick any arrived , unprocessed s_i


## Page 160

6.3
Server-worker framework
145
x[i] = x[i] - s_i
}
}
and the workers run
// Worker code, i = agent number
WHILE (not converged) {
x << receive from server (wait until receive)
s_i = eta*S[i](x)
s_i >> server
}
Each iteration starts with the server broadcasting x to all the workers. Then,
the server waits to receive s_i and updates x[i] upon the arrival of s_i. Once all
indices are processed, the server starts a new iteration.
This synchronous parallel algorithm has several potential sources of inefficien-
cies. Between a broadcast and the first arrival of s_i, the server is idle. Then,
workers upload the s_i’s around the same time, due to synchrony, and can cause
a computational and communication bottleneck. Also, a single straggler, a worker
taking significantly longer to process its work, can slow down the entire algorithm.
An asynchronous implementation in the server-worker framework can avoid the
inefficiencies of synchronization. The server broadcasts x at a certain interval, and
it runs
// Async server code
// Queue holds s_i's. Queue is first-in-first-out
WHILE (not converged) {
WHILE (before next broadcast schedule)
s_i =
Queue.pop() (if empty, wait until nonempty)
x[i] = x[i] - s_i
Broadcast(x)
}
The workers run
// Async worker code, i = agent number
// Buffer holds only most recent x received from server
WHILE (not converged) {
x << Buffer.read()
s_i = eta*S[i](x)
s_i >> server 's queue
}
The Queue stores the s_i from workers. Between the broadcasts, the server pro-
cesses the updates in the Queue on a first-in-first-out basis. Each worker has its
Buffer that holds the most recent copy of x received from the server, and uses
it to compute s_i. The server must process the received s_i sufficiently fast, as
otherwise the server cannot keep up with the workers and the Queue will overflow.
The broadcast should be sufficiently frequent so that the workers do not process


## Page 161

146
6
Asynchronous coordinate update methods
the same x too often. Inconsistent reads and writes do not arise in this setup, so
there is no need for exclusive memory access.
We can still model this asynchronous algorithm with AC-FPI (6.1). Specifically,
k increments whenever the server updates a block, and xk is the copy of x in the
server memory after the kth update.
If the arrival times of s_1,…,s_m are m
independent and identical Poisson processes, then i(0), i(1), . . . is an IID random
sequence. In this case, this algorithm is an instance of ARock and we can apply
Theorem 3. In general, i(0), i(1), . . . is not an IID random sequence, and Theorem 3
does not apply.
6.4
Methods
We now present instances of AC-FPI on shared memory systems and on the pa-
rameter server framework. The ARock assumptions are approximately, but not
fully, satisfied by these algorithms.
6.4.1
Asynchronous coordinate gradient descent
Consider the problem
minimize
x∈Rn
f
 m
X
i=1
A:,ixi −b
!
+
m
X
i=1
gi(xi),
where g1, . . . , gm are CCP functions on Rn1, . . . , Rnm, f is a CCP function on Rr,
b ∈Rr, and
A =
A:,1
A:,2
· · ·
A:,m

∈Rr×n.
Assume for simplicity that we have p = m agents. (If we have more blocks than
agents, we can consolidate the m blocks into p groups.) Assume the ith agent has
access to xk
i , Proxαgi, A:,i, ∇f for i = 1, . . . , m.
The RC-FPI with the FBS operator is
xk+1
i(k) = Proxαgi(k)

xk
i(k) −αA⊺
:,i(k)∇f(yk)

yk+1 = yk + A:,i(k)(xk+1
i(k) −xk
i(k)),
where we initialize y0 = Ax0 −b. The corresponding AC-FPI is
sk
i(k) = η

ˆxk
i(k) −Proxαgi(k)

ˆxk
i(k) −αA⊺
:,i(k)∇f(ˆyk)

xk+1
i(k) = xk
i(k) −sk
i(k)
yk+1 = yk −A:,i(k)sk
i(k),


## Page 162

6.4
Methods
147
where
ˆxk
i(k) = x
k−di(k)(k)
i(k)
,
ˆyk = A:,1xk−d1(k)
1
+ · · · + A:,mxk−dm(k)
m
.
In a shared memory system, we can implement AC-FPI with
// Shared memory code
// Initialize x=0, y=-b
// Pr_i = prox_{alpha*g_i}, G_f = gradient of f
WHILE (not converged) {
//i = agent number
Read y
s[i] = eta*(x[i] - Pr_i(x[i] - alpha*A[:,i]'*G_f(y)))
del[i] = -A[:,i]*s[i]
Acquire exclusive access to y
y = y + del[i]
Release exclusive access to y
x[i] = x[i] - s[i]
}
Although there is a momentary inconsistency between y and x[i] (after y is up-
dated but before x[i] is updated), this inconsistency makes no difference since
each x[i] is read and updated by agent i only, so to other agents, y and x[i] are
effectively updated simultaneously.
In a parameter server framework, we can implement AC-FPI with the server
running
// Server code
// Initialize y=-b
WHILE (not converged) {
WHILE (before next broadcast schedule)
y = y + Queue.pop() (if empty, wait until nonempty)
Broadcast(y)
}
and the m agents running
// Worker code
// Initialize x(1)=...=x(m)=0
// Pr_i = Prox_{alpha*g_i}, G_f = gradient of f
WHILE (not converged) {
//i = agent number
y << last received from server
s_i = eta*(x_i - Pr_i(x_i - alpha*A[:,i]'*G_f(y)))
(-A[:,i]*s_i) >> server's Queue
x_i = x_i - s_i
}
The value of y received from the parameter server may be inconsistent with x if
the parameter server has not yet processed the worker’s previous upload to the
buffer. To ensure consistency, the worker can wait until it is broadcast a y with


## Page 163

148
6
Asynchronous coordinate update methods
a timestamp certifying that the worker’s previous upload to the buffer has been
incorporated. See Exercise 6.3.
In computational models where each agent always updates the same block, the
independence assumption does not hold even if all agents are equally powerful and
the computational costs of all blocks are identical. See Exercise 6.1.
6.4.2
Asynchronous ADMM
Consider the optimization problem
minimize
x∈Rn
1
m
m
X
i=1
fi(x) + g(x).
We recast this problem into
minimize
x1,...,xm,y∈Rn
1
m
Pm
i=1 fi(xi) + g(y)
subject to


I
0
. . .
0
0
I
. . .
0
...
0
0
. . .
I


|
{z
}
=A


x1
x2
...
xm

−


I
I
...
I


|{z}
=B
y = 0.
(6.9)
Define f(x1, . . . , xm) = (1/m)(f1(x1) + · · · + fm(xm)). As we did in §3.2, consider
the dual problem
minimize
ν
˜f(ν) + ˜g(ν),
where ˜f(ν) = f ∗(−A⊺ν) and ˜g(ν) = g∗(−B⊺ν). The PRS operator (2.14) applied
to the dual problem is
wk+1 = (2Proxα ˜
f −핀)(2Proxα˜g −핀)wk.
The FPI with the PRS operator averaged by η ∈(0, 1) is
yk+1 = argmin
y∈Rn


g(y) −y⊺
m
X
j=1
wk
j + αm
2 ∥y∥2



xk+1
i
= argmin
x∈Rn
 1
mfi(x) + x⊺ wk
i −2αyk+1
+ α
2 ∥x∥2

for i = 1, . . . , m
wk+1
i
= wk
i + 2ηα(xk+1
i
−yk+1)
for i = 1, . . . , m.
With the change of variables wk = αuk and ρ = 1/(αm), we get
yk+1 = Proxρg

1
m
m
X
j=1
uk
j


xk+1
i
= Proxρfi
 2yk+1 −uk
i

for i = 1, . . . , m
uk+1
i
= uk
i + 2η(xk+1
i
−yk+1)
for i = 1, . . . , m.


## Page 164

6.5
Exclusive memory access
149
The corresponding AC-FPI is
yk+1 = Proxρg
 (1/m)ˆuk
sum

xk+1
i(k) = Proxρfi(k)

2yk+1 −ˆuk
i(k)

uk+1
i(k) = uk
i(k) + 2η(xk+1
i(k) −yk+1)
where
ˆuk
i(k) = u
k−di(k)(k)
i(k)
,
ˆuk
sum = uk−d1(k)
1
+ · · · + uk−dm(k)
m
.
Consider a parameter server framework. Assume for simplicity that we have
p = m workers. Assume the parameter server has access to Proxg/(αm). Assume
the ith agent has access to uk
i and Proxfi/α, for i = 1, . . . , m. We can implement
ARock with the server running
// Parameter server code
// Initialize u_sum=0
WHILE (not converged) {
WHILE (before next broadcast schedule)
s = Queue.pop() (if empty, wait until nonempty)
u_sum = u_sum + s
y = Prox_{rho*g}(u_sum/m)
Broadcast(y)
}
and the m agents running
// Worker code
// Initialize u[1]=...=u[m]=0
WHILE (not converged) {
//i = agent number
y << last received from server
x_i = Prox_{rho*f_i}(2*y-u_i)
2*eta*(x_i-y) >> server's Queue
u_i = u_i + 2*eta*(x_i - y)
}
6.5
Exclusive memory access
We now discuss how to implement exclusive memory access using atomic operations
and mutual exclusion locks.
We limit the discussion to a superficial level, just
enough to provide clarity on the behavior and the implementation of AC-FPI.
For a more thorough discussion on the lower-level considerations of concurrent
programming, we refer to readers to standard resources such as [Ray13].


## Page 165

150
6
Asynchronous coordinate update methods
6.5.1
Atomic operations
An operation of a computational agent is atomic if the whole operation is guaran-
teed to complete without interruption (or never start) in the presence of contention
from other agents; if an atomic operation consists of multiple steps, other agents
will not observe intermediate results. In most modern systems, reading and writing
a single number (represented as a 32- or 64-bit floating-point number) is an atomic
operation.
Consider the case where all blocks are single coordinates, i.e., m = n and
n1 = · · · = nm = 1. Then we can implement the AC-FPI as follows:
// p agents run the while loop asynchronously
WHILE (not converged) {
1. Select i from Uniform{1,2,...,m}
2. for j = 1,...,m
read x[j]
3. Compute s[i] = -eta*S[i](x)
4. x[i] += s[i] (atomic with compare -and-swap)
}
In Step 2, each coordinate x[j] is read consistently, although different coordinates
may have different delays.
Step 4 uses the increment operator +=, defined by a+=b being equivalent to
a=a+b. The increment operator reads from a and b, computes the sum, and writes
to a. Despite several erroneous claims in the asynchronous optimization literature,
+= is often not atomic in many CPUs and GPUs; when multiple agents simultane-
ously increment the same variable, one agent can overwrite another’s increment.
The atomic increment can be implemented via compare-and-swap:
// atomic a += b
do {
old <- a
} while ( !compare_and_swap(a, old, old+b) )
Most modern CPUs and GPUs support the compare-and-swap instruction as an
atomic operation. It corresponds to the following:
// atomic execution
// input num is passed by reference and is modifiable
function compare_and_swap(num, old, new) {
if num != old
return false
num <- new
return true
}
In other words, if num is equal to old, then write new to num and return true, but
otherwise do nothing and return false.
In the general case where the blocks represent more than one coordinate, this
approach is no longer valid. The reads of Step 2 are no longer guaranteed to be


## Page 166

6.5
Exclusive memory access
151
consistent, as it is possible for x[j] to be updated by another agent while it is being
read. Moreover, the atomic increment via compare-and-swap is no longer possible,
as compare-and-swap is usually supported only for data types of size 64-bits or
smaller.
6.5.2
Mutual exclusion lock
A mutual exclusion lock or mutex is a synchronization object for concurrent pro-
gramming with a lock and an unlock methods. A mutex is acquired by at most
one agent at any given time. An agent acquires a mutex with the lock() method.
If the mutex is available, lock() returns immediately and acquires the mutex.
Otherwise (if another agent has locked the mutex and has not yet unlocked it),
lock() waits until the mutex becomes available and then acquires the mutex. An
agent releases a mutex with the unlock() method. The unlock() method returns
immediately. If other agents are waiting to acquire the mutex, then one of the
waiting agents acquires the mutex upon the unlock. Mutexes can be implemented
using the compare-and-swap operation, although it is usually better to rely on
implementations provided by standard libraries.
An inefficient way to implement exclusive access in the AC-FPI is as follows:
// AC-FPI with one mutex. Inefficient!
WHILE (not converged) {
1. Select i from Uniform{1,2,...,m}
2. mutex.lock()
Read x
mutex.unlock()
3. Compute s[i] = eta*S[i](x)
4. mutex.lock()
x[i] = x[i] - s[i]
mutex.unlock()
}
With this locking mechanism, access to the shared variable x can be a significant
bottleneck, as at most one agent is allowed to access x at a time.
Rather, it is more efficient to use separate mutexes for all blocks:
// AC-FPI with mutex for each block
WHILE (not converged) {
1. Select i from Uniform{1,2,...,m}
2. for j = 1,...,m
mutex[j].lock()
read x[j]
mutex[j].unlock()
3. Compute s[i] = eta*S[i](x)
4. mutex[i].lock()
x[i] = x[i] - s[i]
mutex[i].unlock()
}


## Page 167

152
6
Asynchronous coordinate update methods
This mechanism ensures the reads and writes of all blocks are consistent, while
allowing multiple agents to concurrently operate on separate blocks.
However,
Step 2 is still inefficient, as it prevents multiple agents from concurrently reading
the same block.
6.5.3
Readers-writers lock
A readers-writers lock allows concurrent access for reads while enforcing exclusive
access for writes. The following class implements a readers-writers lock.
class rw_lock {
private:
int b
mutex MUTEX_b , MUTEX_W
public:
//constructor
rw_lock() {
b = 0
}
//member functions
function read_lock() {
MUTEX_b.lock()
b++
If b==1, MUTEX_W.lock()
MUTEX_b.unlock()
}
function read_unlock() {
MUTEX_b.lock()
b--
If b==0, MUTEX_W.unlock()
MUTEX_b.unlock()
}
function write_lock() {
MUTEX_W.lock()
}
function write_unlock() {
MUTEX_W.unlock()
}
}
Now we can implement the AC-FPI with readers-writers locks:
// AC-FPI with readers -writers locks
WHILE (not converged) {
1. Select i from Uniform{1,2,...,m}
2. for j = 1,...,m
rw_lock[j].read_lock()
read x[j]


## Page 168

6.5
Exclusive memory access
153
rw_lock[j].read_unlock()
3. Compute s[i] = eta*S[i](x)
4. rw_lock[i].write_lock()
x[i] = x[i] - s[i]
rw_lock[i].write_unlock()
}
This mechanism ensures that the reads and writes of all blocks are consistent, allows
multiple agents to concurrently operate on separate blocks, and allows multiple
agents to concurrently read from the same block.
This implementation of the readers-writers lock prioritizes readers: if there are
many readers, a writer must wait until there are no more readers, while if there
are many writers, a reader can acquire the lock while other writers are waiting.
To reduce the staleness as much as possible, one could use a readers-writers lock
prioritizing writers. However, such locks are more complex and allow for less con-
currency.


## Page 169

154
6
Asynchronous coordinate update methods
Bibliographical Notes
Stage 1 of the main proof relies on a construction of a Lyapunov function. The main
insight of this construction was first presented in the 2016 ARock paper by Peng, Xu,
Yan, and Yin in 2016 [PXYY16].
The specific construction follows the 2016 work of
Hannah and Yin [HY18]. The arguments of Stages 2 and 3 for establishing almost sure
convergence is new.
Classical asynchronous methods.
Asynchronous methods for solving linear systems
of equations were first proposed by Rosenfeld in 1969 [Ros69] and Chazan and Miranker in
1969 in [CM69]. In 1983, Bertsekas analyzed FPIs that are (almost surely) nonexpansive
for all choices of coordinates and delays [Ber83], and this line of analysis was generalized to
FPIs that are “pseudo-nonexpansive” by Tseng, Bertsekas, and Tsitsiklis in 1990 [TBT90].
However, this setup is comparatively much more restrictive, since the AC-FPI under
the ARock assumption is nonexpansive in expectation. Frommer and Szyld provides a
comprehensive review for classical asynchronous methods prior to 2000 [FS00].
Modern asynchronous optimization methods.
Arguably, the most influential mod-
ern work on asynchronous optimization is Recht, Re, Wright, and Niu’s 2011 paper
with the unusual title “Hogwild” [RRWN11].
The paper used asynchronous SGD to
obtain a practical speedup, analyzed the convergence theoretically, and popularized asyn-
chronous methods in machine learning. The theoretical convergence properties of asyn-
chronous SGD was further analyzed by Chaturapruek, Duchi, and Ré in 2015 [CDR15].
The study of many other asynchronous optimization methods followed Hogwild: asyn-
chronous ADMM was studied by Wei and Ozdaglar in 2013 [WO13] and Zhang and
Kwok in 2014 [ZK14a]; asynchronous coordinate descent was studied by Liu et al. in
2015 [LWR+14, LWR+15], Liu and Wright in 2015 [LW15], Lian, Huang, Li, and Liu in
2015 [LHLL15], and Hsieh, Yu, and Dhillon in 2015 [HYD15]; asynchronous SAGA was
studied by Leblond, Pedregosa, Lacoste-Julien in 2017 [LPL17, PLL17]; non-convex asyn-
chronous methods were studied by Cannelli, Scutari, Facchinei, and Kungurtsev in 2016
and 2017 [CSFK16, CFKS17a]; asynchronous proximal alternating linearized minimiza-
tion was studied by Davis in 2016 [Dav16]; and finally, asynchronous fixed-point iterations
and monotone operator methods were studied in the “ARock paper” by Peng, Xu, Yan,
and Yin in 2016 [PXYY16]. These works all rely on the bounded delay assumption.
ARock with unbounded delays was studied by Hannah and Yin in 2018 [HY18]. The
unbounded delay assumption is partially justified by Peng, Xu, Yan, and Yin’s 2019
work reporting that asynchronous delays empirically follow a Poisson distribution in some
setups [PXYY19]. Hannah and Yin showed in 2017 that, under the ARock assumptions
and a certain computational model, the AC-FPI theoretically provides a speedup by
executing more iterations individually providing improvements not much worse than that
of synchronous iterations [HY17]. Asynchronous optimization with unbounded delays was
also studied in the machine learning context by Zhou et al. in 2018 [ZMB+18].
Our analysis crucially relies on the independence assumption between i(k) and d(k) for
k = 0, 1, . . . ; but, as discussed in §6.1.1, this assumption is not always realistic. Several
past works relax this assumption, but they are only able to prove weaker results [SHY17,
CFKS17b, LPL17].
System-level discussions.
As discussed in §6.3 and §6.5, the analysis of the asyn-
chronous methods is inextricably linked to lower-level considerations of how the algo-
rithms are implemented and executed. The parameter server framework was introduced
in the machine learning community, and Smola and Narayanamurthy’s 2010 paper [SN10]
and Li et al.’s 2014 paper [LAP+14] are early references. We refer readers interested in
a thorough treatment of classical concurrent (asynchronous) programming to Raynal’s


## Page 170

Bibliographical Notes
155
book [Ray13]. In fact, the pseudocode of §6.5.3 was taken from [Ray13, p. 76].


## Page 171

156
6
Asynchronous coordinate update methods
Exercises
6.1 Violation of independence.
Consider the asynchronous coordinate gradient descent of
§6.4.1 implemented on a parameter server framework. In this setup, m agents or workers
are assigned to the m blocks, and there is no random selection of the blocks. Why are
i(k) and d(k) not independent? Why is i(0), i(1), . . . not an independent sequence?
6.2 Delay summability condition. Define τ(k) = maxi=1,...,m di(k). Let ε > 0. Assume
E

τ(k)5+ε
 d(k −1), . . . , d(0), i(k −1), . . . , i(0)

< C < ∞
∀k = 0, 1, . . . ,
where C is a constant independent of k.
Show there exists a nonincreasing sequence
Qℓ∈[0, 1] with ℓ= 0, 1, . . . satisfying (6.2).
6.3 Timestamp for consistency. Consider the asynchronous coordinate gradient descent of
§6.4.1 implemented on a parameter server framework. When can inconsistency between
y and x arise?
Assume the parameter server broadcasts, along with y, a timestamp that specifies the
time at which the server received the update that was last incorporated into y. How can
workers use this information to ensure consistency between y and x?
6.4 Non-uniform selection probabilities. Assume the ARock assumptions with the following
modification: i(0), i(1), . . . are independently and identically distributed with probability
Prob [i(k) = j] = pj
for j = 1, . . . , m, where p1, . . . , pm ≥0 and Pm
i=1 pi = 1. Show convergence of the AC-FPI
xk+1 = xk −
η
pi(k)
핊i(k)xk−d(k).
6.5 After-read labeling of iterates. We had defined the iteration count to increment when an
agent completes writing to the x variable. We call this definition of iterates the after-write
labeling. If the computational costs of the blocks are unequal, then i(k) and d(k) can be
dependent under the after-write labeling.
Consider the AC-FPI
// p agents run the while loop asynchronously
// x and s are vectors in shared memory
WHILE (not converged) {
1. Select i from Uniform{1,2,...,m}
2. Read x
3. Compute s[i] = eta*S[i](x)
4. Exclusively read x[i] and write x[i] = x[i] - s[i]
}
with the after-read labeling: starting from k = 0, the iteration count increments from k
to k + 1 when an agent completes Step 1, and let ˆxk be the copy x read just before this
increment. Starting from x0, sequentially define x1, x2, . . . via
xk+1 = xk −η핊i(k)ˆxk.
(a) The “iterates” x0, x1, . . . do not necessarily represent the state of x in shared memory
at some points in time, even if the agents do not concurrently perform Step 4.
Explain why.
(b) We can no longer define a delay vector d(k) with ˆxk = xk−d(k). Why?
Hint. Think of
xk = x0+
X
first k updates,
ˆxk = x0+
X
updates completed before the kth read.


## Page 172

Exercises
157
(c) By default, Step 2 reads the entire vector x. If S[i](x) does not depend on all of
x and we instead read only the components of x that are necessary for computing
S[i](x), then i(k) and ˆxk may no longer be conditionally independent. Explain
why.
Remark. This “after-read” labeling technique was introduced by Leblond, Pedregosa, and
Lacoste-Julien [LPL17].
6.6 Convergence analysis of after-read labeling.
Consider the after-read labeling of Exer-
cise 6.5. To analyze convergence of the AC-FPI mathematically described by the after-
read labeling under the ARock assumptions, how should we modify Stage 1 of the proof
of Theorem 3?
6.7 Extended coordinate-friendly operators with after-read labeling. Let 핋: Rn →Rn be an
extended coordinate-friendly operator with the auxiliary quantity y(x) = Ax. Consider
the after-write and after-read labeling of Exercise 6.5. Consider the following code, which
is almost the same as the code of §6.2 but different in how we enforce exclusive access.
// p agents run the while loop asynchronously
// x, y, and s in shared memory
WHILE (not converged) {
1. Select i from Uniform{1,2,...,m}
2. Read x,y
3. Compute s[i] = eta*S[i](x) using y
4. dy[i] = A[:,i]*s[i]
5. Acquire exclusive access to y
Read y and write y = y - dy[i]
Release exclusive access to y
6. Acquire exclusive access to x[i]
Read x[i] and write x[i] = x[i] - s[i]
Release exclusive access to x[i]
}
The “acquire” and “release” can be implemented by creating mutexes, one each for y,
x[1], . . . , x[m], and by locking and unlocking them.
(a) With after-write labeling, why are x and y inconsistent?
(b) With after-read labeling, why is the inconsistency resolved?


## Page 173

158
6
Asynchronous coordinate update methods


## Page 174

Part II
Additional topics


## Page 175



## Page 176

Chapter 7
Stochastic optimization
Consider the finite sum minimization problem
minimize
x∈Rn
1
N
N
X
i=1
fi(x),
where fi is a CCP function on Rn with dom fi = Rn for i = 1, . . . , N. When
f1, . . . , fN are differentiable, we can apply the celebrated stochastic gradient descent
(SGD),
xk+1 = xk −αk∇fi(k)(xk).
When f1, . . . , fN are not differentiable, we can apply the stochastic subgradient
method:
xk+1 ∈xk −αk∂fi(k)(xk).
For both methods, α0, α1, . . . ∈R are the stepsizes and i(k) ∈{1, . . . , N} is chosen
independently uniformly at random.
For the more general problem
minimize
x∈Rn
1
N
N
X
i=1
fi(x) + g(x),
where fi is a CCP function on Rn with dom fi = Rn for i = 1, . . . , N and g is a
CCP function on Rn, we can apply the stochastic proximal subgradient method:
xk+1 ∈Proxαkg(xk −αk∂fi(k)(xk)).
In particular, when g = δC for a nonempty closed convex set C, i.e., g represents
the constraint x ∈C, the method reduces to the stochastic projected subgradient
method:
xk+1 ∈ΠC
 xk −αk∂fi(k)(xk)

.


## Page 177

162
7
Stochastic optimization
These stochastic (sub)gradient methods are used widely for many large-scale
optimization problems, especially those arising in machine learning. In this section,
we study generalizations of these methods to the setup of monotone inclusions and
establish convergence.
7.1
Stochastic forward-backward method
Consider the problem
find
x∈Rn
0 ∈
 
1
N
N
X
i=1
픸i + 픹
!
x,
where 픸i : Rn ⇒Rn is maximal monotone with dom 픸i = Rn for i = 1, . . . , N
and 픹: Rn ⇒Rn is maximal monotone. Consider the stochastic forward-backward
method (SFB),
xk+1 ∈핁αk픹(핀−αk픸i(k))xk,
where αk > 0 and i(k) ∈{1, . . . , N} is chosen independently uniformly at random.
Since 픸i(k) may be multi-valued, the method is defined with an inclusion. One can
equivalently write
ak ∈픸i(k)(xk)
xk+1 = 핁αk픹(xk −αkak).
We do not make any assumptions on the selection ak ∈픸i(k)(xk); we can choose
ak deterministically or randomly to be any element within the set 픸i(k)(xk).
In this section, we analyze the convergence of SFB. In general, SFB may not
converge, so we establish convergence using demipositivity or averaging.
Basic assumptions
For notational simplicity, define
픸= 1
N
N
X
i=1
픸i.
Assume 픸i is maximal monotone and dom 픸i = Rn for i = 1, . . . , N. Assume
픹: Rn ⇒Rn is maximal monotone. Assume Zer (픸+픹)̸ = ∅. Assume the random
indices i(0), i(1), . . . ∈{1, . . . , N} are independent and identically distributed with
uniform probability. Assume there are nonnegative constants C1, C2 < ∞such
that
1
N
N
X
i=1
∥픸ix∥2 ≤C1
2 ∥x∥2 + C2
∀x ∈dom 픹.
(7.1)


## Page 178

7.1
Stochastic forward-backward method
163
Assume the positive sequence α0, α1, . . . satisfies
· · · ≤α1 ≤α0,
∞
X
k=0
αk = ∞,
∞
X
k=0
α2
k < ∞.
(7.2)
Examples of αk that satisfy the conditions in (7.2) include
αk =
C
(k + 1)p ,
k = 0, 1, . . . ,
for 1
2 < p ≤1.
Convergence with demipositivity
We say a maximal monotone operator 픸: Rn ⇒Rn is demipositive if there is an
x⋆∈Zer 픸such that
⟨픸x, x −x⋆⟩> 0
∀x /∈Zer 픸.
Strongly monotone, cocoercive, and subdifferential operators of CCP functions are
demipositive; for any x /∈Zer 픸and x⋆∈Zer 픸, if 픸is µ-strongly monotone, then
⟨픸x, x −x⋆⟩≥µ∥x −x⋆∥2 > 0;
if 픸is β-cocoercive, then
⟨픸x, x −x⋆⟩≥β∥픸x∥2 > 0;
and if 픸= ∂f for some CCP function f, then
⟨픸x, x −x⋆⟩≥f(x) −f(x⋆) > 0.
Also, if 픸is maximal monotone and int (Zer 픸)̸ = ∅, i.e., if Zer 픸has an interior,
then 픸is demipositive. See Exercise 7.5.
However, not all monotone operators are demipositive. The single-valued oper-
ator 픸: R2 →R2 defined as
픸(x, y) =
 0
1
−1
0
 x
y

is monotone but not demipositive. A quick computational experiment shows SFB
with this 픸and 픹= 0 does not converge; the iterates cycle around the zero 0
without converging to it.
Theorem 4 Assume the outlined “basic assumptions.” Assume 픸+ 픹is demiposi-
tive. Then xk+1 ∈핁αk픹(핀−αk픸i(k))(xk) with any starting point x0 converges to
a zero, i.e., xk →x⋆∈Zer 픸, with probability 1.


## Page 179

164
7
Stochastic optimization
Convergence with averaging
Consider the same SFB iteration
xk+1 ∈핁αk픹(핀−αk픸i(k))xk,
but we compute the averaged iterates:
¯xk =
Pk
j=0 αjxj
Pk
j=0 αj
.
(7.3)
This technique is also called Polyak–Ruppert averaging.
The averaged iterates
converge, i.e., ¯xk →x⋆∈Zer 픸, without demipositivity.
Theorem 5 Assume the outlined “basic assumptions.” Then the averaged iterates
¯xk of xk+1 ∈핁αk픹(핀−αk픸i(k))(xk), defined by (7.3), with any starting point x0
converges to a zero, i.e., ¯xk →x⋆∈Zer 픸, with probability 1.
In addition to being convergent without demipositivity, averaging has several
advantages. One is that averaging can provide a good rate of convergence in specific
setups. See Exercise 7.1. Another is that averaging makes the convergence rate
more robust to the choice of stepsizes. See Exercise 7.3. However, a drawback of
averaging is that it may slow down the algorithm when the (non-averaged) iterates
are converging to the solution quickly.
7.1.1
Convergence proofs
We first present the proof of Theorem 4, which relies on a summability argument
similar to what we have seen before.
Proof of Theorem 4. Define e픸i(k)xk ∈Rn with xk+1 = 핁αk픹(xk −αk e픸i(k)xk) and
e픹xk+1 = (1/αk)(xk−xk+1)−e픸i(k)xk. This implies e픸i(k)xk ∈픸i(k)xk and e픹xk+1 ∈
픹xk+1. Let e픸xk = Ei(k)[e픸i(k)xk] ∈픸xk for k = 0, 1, . . . . Let x⋆∈Zer (픸+ 픹)
for which the demipositivity property holds. Let e픸x⋆∈Rn be an element such
that e픸x⋆∈픸x⋆and −e픸x⋆∈픹x⋆. Let e픹x⋆= −e픸x⋆. Note that xk+1 = xk −
αk

e픸i(k)xk + e픹xk+1
.
Then we have
∥xk+1 −x⋆∥2 = ∥xk −x⋆∥2 + α2
k∥e픸i(k)xk −e픸x⋆∥2 −α2
k∥e픹xk+1 −e픹x⋆∥2
−2αk⟨e픸i(k)xk −e픸x⋆, xk −x⋆⟩−2αk⟨e픹xk+1 −e픹x⋆, xk+1 −x⋆⟩.
With assumption (7.1), we have
∥e픸i(k)xk −e픸x⋆∥2 ≤2∥e픸i(k)xk∥2 + 2∥e픸x⋆∥2
≤C1(∥xk∥2 + ∥x⋆∥2) + 4C2
≤C1(2∥xk −x⋆∥2 + 3∥x⋆∥2) + 4C2,


## Page 180

7.1
Stochastic forward-backward method
165
and we have
∥xk+1 −x⋆∥2 ≤(1 + 2C1α2
k)∥xk −x⋆∥2 + 3C1α2
k∥x⋆∥2 + 4C2α2
k
−2αk⟨e픸i(k)xk −e픸x⋆, xk −x⋆⟩−2αk⟨e픹xk+1 −e픹x⋆, xk+1 −x⋆⟩.
Define
V k = ∥xk −x⋆∥2 + 2αk⟨e픹xk −e픹x⋆, xk −x⋆⟩
for k = 0, 1, . . . . Then,
V k+1 = ∥xk+1 −x⋆∥2 + 2αk+1⟨e픹xk+1 −e픹x⋆, xk+1 −x⋆⟩
≤∥xk+1 −x⋆∥2 + 2αk⟨e픹xk+1 −e픹x⋆, xk+1 −x⋆⟩
≤(1 + 2C1α2
k)V k + 3C1α2
k∥x⋆∥2 + 4C2α2
k −2αk⟨e픸i(k)xk + e픹xk, xk −x⋆⟩.
Write Ek for the conditional expectation with respect to i(k) conditioned on i(k −
1), i(k −2), . . . , i(0). Then,
EkV k+1 ≤(1 + 2C1α2
k)V k + 3C1α2
k∥x⋆∥2 + 4C2α2
k −2αk⟨e픸xk + e픹xk, xk −x⋆⟩.
Now apply Theorem 30, the Robbins–Siegmund quasimartingale convergence
theorem, to get that for any x⋆∈Zer (픸+ 픹),
(i) P∞
k=0 αk⟨e픸xk + e픹xk, xk −x⋆⟩< ∞,
(ii) limk→∞V k exists
with probability 1. Since P
k αk = ∞and ⟨e픸xk + e픹xk, xk −x⋆⟩≥0, we conclude
from (i) that
lim inf
k
⟨e픸xk + e픹xk, xk −x⋆⟩= 0.
Since ∥xk −x⋆∥2 ≤V k and V k is bounded, we also conclude that xk is bounded
with probability 1. By (7.1), boundedness of xk implies e픸xk ∈픸xk is bounded.
By (7.1), boundedness of xk implies e픸i(k)xk is bounded, which implies e픹xk+1 is
bounded. Therefore, there exists a subsequence kj →∞such that
xkj →x∞,
e픸xkj →a∞,
e픹xkj →b∞,
⟨e픸xkj + e픹xkj, xkj −x⋆⟩→0.
Since 픸+ 픹is maximal monotone, its graph is closed (see Exercise 10.3), and
a∞+ b∞∈(픸+ 픹)x∞. Therefore
0 = ⟨a∞+ b∞, x∞−x⋆⟩
and
0 ∈⟨(픸+ 픹)x∞, x∞−x⋆⟩.
By demipositivity, we conclude x∞∈Zer (픸+ 픹).
Note that demipositivity was invoked only in the final step. By repeating the
application of Theorem 30 for all x⋆∈Zer (픸+ 픹), we can show (i) and (ii) for all


## Page 181

166
7
Stochastic optimization
x⋆∈Zer (픸+ 픹), not just the x⋆for which the demipositivity property holds. By
(i) and monotonicity of 픸and 픹, we have
αk⟨e픹xk −e픹x⋆, xk −x⋆⟩≤αk⟨e픸xk + e픹xk, xk −x⋆⟩→0.
Therefore, (ii) implies limk→∞∥xk −x⋆∥2 exists. We apply Proposition 1 to con-
clude limk→∞∥xk−y∥2 exists for all y ∈Zer (픸+픹), including y = x∞. Therefore,
∥xk −x∞∥→0, i.e., the entire sequence converges to x∞.
Next, we present the proof of Theorem 5, which is more elaborate and relies
on most of the steps performed for the proof of Theorem 4. We first present two
intermediate lemmas.
Lemma 1 Let 픸: Rn ⇒Rn be maximal monotone. If
inf
(x,u)∈픸⟨u, x −¯x⟩≥0,
then ¯x ∈Zer 픸.
Proof. The infimum can be rephrased as
⟨픸x −0, x −¯x⟩≥0
∀x ∈Rn.
Maximality of 픸implies 0 ∈픸¯x.
Lemma 2 Let α0, α1, . . . be a non-summable positive sequence and x0, x1, . . . be
vectors in Rn. Define ¯xk as in (7.3). Assume there is a nonempty closed convex
set Q such that (i) any convergent subsequence of ¯xk converges to a limit in Q; (ii)
limk→∞∥xk −q∥exists for all q ∈Q. Then ¯xk converges to a single limit in Q.
Proof. For any q1, q2 ∈Q,
xk −q1 + q2
2

2
= ∥xk −q1∥2 +

q1 −q2
2

2
+ ⟨xk −q1, q1 −q2⟩.
Then, ⟨xk −q1, q1 −q2⟩has a limit and
lim
k→∞⟨xk −q1, q1 −q2⟩= lim
k→∞⟨¯xk −q1, q1 −q2⟩,
since α0, α1, . . . is a non-summable positive sequence. Next, let σ1 and σ2 be two
accumulation points of ¯xk. Then,
⟨σ1 −q1, q1 −q2⟩= ⟨σ2 −q1, q1 −q2⟩,
and by letting q1 = σ1 and q2 = σ2, we get ∥σ1 −σ2∥2 = 0. Therefore, ¯xk has only
one limit.
Continuous-time illustration of the proof of Theorem 5. Before we prove The-
orem 5, we present a deterministic continuous-time analysis that motivates the
stochastic discrete-time analysis for Theorem 5. Analyzing convergence in continuous-
time (which is often easier) and then translating the analysis to the discrete-time
setup is a common technique for understanding and finding proofs.


## Page 182

7.1
Stochastic forward-backward method
167
Assume 픸is single-valued and 픹= 0. Consider the differential equation
˙x(t) = −픸x(t),
x(0) = x0.
Then, for any y ∈Rn, we have
d
dt
1
2∥x(t) −y∥2 = ⟨˙x(t), x(t) −y⟩= −⟨픸x(t), x(t) −y⟩
≤−⟨픸y, x(t) −y⟩.
When y = x⋆∈Zer 픸, we have d
dt
1
2∥x(t)−x⋆∥2 ≤0. So limt→∞∥x(t)−x⋆∥2 exists,
since ∥x(t) −x⋆∥2 is nonincreasing and nonnegative, for all x⋆∈Zer 픸and x(t) is
bounded.
Integrate
d
dt
1
2∥x(t) −y∥2 ≤−⟨픸y, x(t) −y⟩from t = 0 to t = T and divide by
T to get
1
T
1
2∥x(T) −y∥2 −1
2∥x(0) −y∥2

≤−⟨픸y, ¯x(T) −y⟩,
where ¯x(T) = 1
T
R T
0 x(t) dt. So
⟨픸y, ¯x(T) −y⟩≤−1
T
1
2∥x(T) −y∥2 −1
2∥x(0) −y∥2

and
lim sup
T →∞
⟨픸y, ¯x(T) −y⟩≤0.
By Lemma 1, all accumulation points of ¯x(t) are in Zer 픸. With a variation of
Lemma 2, we conclude that ¯x(t) converges to a single limit.
Proof of Theorem 5. We use the same notation as in the proof of Theorem 4. By
arguments of the proof of Theorem 4, with probability 1, limk→∞∥xk −x⋆∥exists
for all x⋆∈Zer (픸+ 픹). In particular, we know that xk, e픸xk, e픹xk are bounded
sequences with probability 1.
Define
ξk = e픸xk −e픸i(k)xk,
and consider the martingale Pk
j=0 αjξj. The martingale differences are summable
since
∞
X
k=0
α2
kEk

∥ξk∥2
=
∞
X
k=0
α2
kEk
h
∥e픸xk −e픸i(k)xk∥2i
≤
∞
X
k=0
2α2
kEk
h
∥e픸xk∥2 + ∥e픸i(k)xk∥2i
≤
∞
X
k=0
2α2
k
 C1∥xk∥2 + 2C2

< ∞,
where we used (7.1) and the fact that xk is bounded. By Theorem 31, a martingale
convergence theorem,
∞
X
k=1
αkξk


## Page 183

168
7
Stochastic optimization
exists with probability 1. Let K1 ∈N+. Define yK1 = xK1 and
yk+1 = yk −αk e픸xk −αk e픹xk+1
for k = K1, K1 + 1, . . . . Define
εK1 = sup
k≥K1
∥yk −xk∥= sup
k≥K1

k
X
j=K1
αjξj

.
Since P∞
k=1 αkξk exists, εK1 →0 as K1 →∞. (We use the yk-sequence because
the differences yk+1 −yk are defined with e픸xk rather than e픸i(k)xk, and because
the difference between xk and yk is small, bounded by εK1.)
Let K2 > K1. Define
¯x(K1,K2) =
PK2
k=K1 αkxk
PK2
k=K1 αk
,
i.e., ¯x(K1,K2) is the averaged iterate with the averaging starting from K1 and ending
at K2. Note that ¯xK2 = ¯x(0,K2), and that ¯x(K1+1,K2) and ¯xK2 share the same
accumulation points as K2 →∞.
Let x ∈Rn, e픸x ∈픸x, and e픹x ∈픹x be arbitrary. For k ≥K1, we have
∥yk+1 −x∥2 = ∥yk −x∥2 + α2
k∥e픸xk∥2 −α2
k∥e픹xk+1∥2
−2αk⟨e픸xk, yk −x⟩−2αk⟨e픹xk+1, yk+1 −x⟩
= ∥yk −x∥2 + α2
k∥e픸xk∥2 −α2
k∥e픹xk+1∥2
−2αk⟨e픸xk, xk −x⟩−2αk⟨e픹xk+1, xk+1 −x⟩
−2αk⟨e픸xk, yk −xk⟩−2αk⟨e픹xk+1, yk+1 −xk+1⟩
≤∥yk −x∥2 + α2
k∥e픸xk∥2 −α2
k∥e픹xk+1∥2
−2αk⟨e픸xk, xk −x⟩−2αk⟨e픹xk+1, xk+1 −x⟩
+ 2αkεK1∥e픸xk∥+ 2αkεK1∥e픹xk+1∥,
where we used the Cauchy–Schwartz inequality. Let M < ∞be a bound for
max
(
∥x∥, ∥xk∥, ∥e픸xk∥, ∥e픹xk∥,
∞
X
k=0
α2
k
)
≤M
∀k = 0, 1, . . . .
Then, we have
∥yk+1 −x∥2 ≤∥yk −x∥2 + α2
kM 2 + 4αkεK1M
−2αk⟨e픸xk, xk −x⟩−2αk⟨e픹xk+1, xk+1 −x⟩
≤∥yk −x∥2 + α2
kM 2 + 4αkεK1M
−2αk⟨e픸x, xk −x⟩−2αk⟨e픹x, xk+1 −x⟩,


## Page 184

7.2
Methods
169
where we used monotonicity of 픸and 픹. Sum over k = K1, . . . , K2 to get
2
K2
X
k=K1
αk⟨e픸x, xk −x⟩+ 2
K2+1
X
k=K1+1
αk⟨e픹x, xk −x⟩
≤∥xK1 −x∥2 + M 3 + 4εK1M
K2
X
k=K1
αk
−2
K2
X
k=K1
(αk −αk+1)⟨e픹x, xk+1 −x⟩.
Dividing by 2 PK2
k=K1+1 αk, we get
⟨e픸x + e픹x, ¯x(K1+1,K2) −x⟩≤O
 
1/
K2
X
k=K1+1
αk
!
+ 2εK1M
 
αK1
PK2
k=K1+1 αk
+ 1
!
+
M 2αK1
PK2
k=K1+1 αk
,
where we used −⟨e픹x, xk+1 −x⟩≤M 2 and the fact that PK2
k=K1(αk −αk+1) forms
a telescoping sum. Therefore,
lim sup
K2→∞
⟨e픸x + e픹x, ¯x(K1+1,K2) −x⟩≤4εK1M.
The right-hand side goes to 0 as K1 →∞. Since the sequences ¯x(K1+1,K2) and ¯xK2
share the same accumulation points as K2 →∞, we conclude
lim sup
k→∞
⟨e픸x + e픹x, ¯xk −x⟩≤0.
Since x ∈Rn, e픸x ∈픸x, and e픹x ∈픹x are arbitrary, Lemma 1 implies all accumu-
lation points of ¯xk are in Zer (픸+ 픹). Finally, Lemma 2 shows that ¯xk converges
to a single limit in Zer (픸+ 픹).
7.2
Methods
Subgradient methods
The problem
minimize
x∈Rn
f(x)
subject to
x ∈C,
where f is a CCP function on Rn and C ⊆Rn is a nonempty closed convex set,
can be solved with the (projected) subgradient method:
xk+1 ∈ΠC(xk −αk∂f(xk)).


## Page 185

170
7
Stochastic optimization
Likewise, the problem
minimize
x∈Rn
f(x) + g(x),
where f and g are CCP can be solved with the proximal subgradient method:
xk+1 ∈Proxαkg(xk −αk∂f(xk)).
Convergence of these subgradient methods are ensured by Theorem 5; if a
minimizer exists,
∥∂f(x)∥2 ≤C1
2 ∥x∥2 + C2
∀x ∈Rn
holds, and (7.2) holds, then xk →x⋆. Note that these methods have no stochas-
ticity.
Stochastic proximal subgradient method
For the stochastic proximal subgradient method
xk+1 ∈Proxαkg(xk −αk∂fi(k)(xk)),
we apply Theorem 4. If a minimizer exists,
1
N
N
X
i=1
∥∂fi(x)∥2 ≤C1
2 ∥x∥2 + C2
∀x ∈dom g
holds, and (7.2) holds, then xk →x⋆with probability 1.
Stochastic proximal simultaneous gradient method
Again, consider the problem of finding a saddle point of
L(x, u) = f(x) −g(u) + 1
N
N
X
i=1
Li(x, u),
where f is a CCP function on Rn, g is a CCP function on Rm, and Li : Rn+m →R
is convex-concave for i = 1, . . . , N. The SFB with ∂L,
xk+1 ∈Proxαkf
 xk −αk∂xLi(k)(xk, uk)

uk+1 ∈Proxαkg
 uk −αk∂u(−Li(k))(xk, uk)

,
is called the stochastic proximal simultaneous subgradient method. (The method
“simultaneously” updates the x and the u.)
Assume a saddle point exists, (7.1) holds, and (7.2) holds. The averaged iterates
defined as in (7.3) converge, i.e., ¯xk →x⋆and ¯uk →u⋆, with probability 1. If L is
furthermore strictly convex-concave, i.e., L(x, u) is strictly convex in x for fixed u
and strictly concave in u for fixed x, then xk →x⋆and uk →u⋆with probability
1.


## Page 186

7.2
Methods
171
Stochastic Condat–Vũ
Consider the problem
minimize
x∈Rn
f(x) + g(Ax) + 1
N
PN
i=1 hi(x),
where f, g, and h1, . . . , hN are CCP, h1, . . . , hN are differentiable, and A ∈Rm×n.
The Lagrangian generating this primal problem is
L(x, u) = f(x) + 1
N
N
X
i=1
hi(x) + ⟨u, Ax⟩−g∗(u).
We split ∂L into
∂L(x, u) = 1
N
N
X
i=1
∇hi(k)(x)
0

|
{z
}
=ℍi(k)(x,u)
+
 0
A⊺
−A
0
 x
u

+
 ∂f(x)
∂g∗(u)

|
{z
}
=픽(x,u)
.
The variable metric version of SFB with
M =
(1/α)I
−A⊺
−A
(1/β)I

and 픸i = 핀−(M −ℍi)(M + 픽)−1 for i = 1, . . . , N and 픹= 0 is
xk+1 = Proxβf(zk)
uk+1 = Proxγg∗(wk + 2βAxk+1)
zk+1 = zk −αk
 zk −xk+1 + β(A⊺uk+1 + ∇hi(k)(xk+1))

wk+1 = wk −αk(wk + γAxk+1).
If total duality holds, h1, . . . , hN are L-smooth, β > 0 and γ > 0 satisfy
βL/2 + βγλmax(A⊺A) < 1,
and (7.2) holds, then xk →x⋆and uk →u⋆with probability 1.


## Page 187

172
7
Stochastic optimization
Bibliographical Notes
The proof of Theorem 4 follows what is now considered a standard argument, which
was first presented in Bottou’s 1991 thesis in French [Bot91, Section 3.3.1.4] and later in
Bottou’s 1998 paper in English [Bot99]. The proof of Theorem 5 follows the techniques
presented in Andrieu, Moulines, and Priouret’s 2005 paper [AMP05] and Bianchi’s 2016
paper [Bia16]. Lemma 2 was first presented by Passty in 1979 [Pas79].
Stochastic approximation.
The stochastic gradient method, also referred to as stochas-
tic approximation in the classical literature, dates back to Robbins and Monro’s 1951 paper
[RM51]. Kushner and Yin’s 2003 textbook [KY03] provides a comprehensive treatment
of stochastic approximation. The technique of averaging was first proposed by Bruck in
1977 [Bru77] and Nemirovski and Yudin in 1978 [NY78] for the non-stochastic setup and
by Ruppert in 1988 [Rup88] and Polyak in 1990 [Pol90] for the stochastic setup. The
subgradient method for the non-stochastic setup was first proposed by Shor in the 1960s
[Sho62, Sho64, Sho85]. With the rise of machine learning, literature on the stochastic
subgradient method has exploded, as the method is used universally for training neural
networks.
The stochastic proximal gradient method has been studied extensively in machine learn-
ing. Stochastic forward-backward splitting for the operator setup was studied by Rosasco,
Villa, and Vũ in 2016 [RVV16]. Interestingly, the proximal subgradient method, stochastic
or otherwise, has not been studied much; Bello-Cruz’s 2017 paper seems to be the only
prior work [BC17b]. Recently, the stochastic forward-backward method has received in-
creased interest in machine learning due to minimax training of GANs [CGFL19, MLZ+19,
RYY19, GBV+19, MKS+20]. For the more general problem of the form
find
x∈Rn
0 ∈
 
1
N
N
X
i=1
(픸i + 픹i)
!
x,
where 픸i : Rn ⇒Rn is a maximal monotone operator on Rn with dom 픸i = Rn and
픹i : Rn ⇒Rn is a maximal monotone operator for i = 1, . . . , N. The method
xk+1 ∈핁αk픹i(k)(핀−αk픸i(k))xk,
where αk > 0 and i(k) ∈{1, . . . , N} is chosen independently uniformly at random, was
studied by Bianchi and Hachem in 2016 [Bia16, BH16].
Expectation of operators.
In this chapter, we focused on finite sums of operators to
avoid measure-theoretic discussions. The Aumann integral, first presented by Aumann
in 1965 [Aum65] and further studied by Rockafellar in 1969 [Roc69] and Bertsekas in
1973 [Ber73], generalizes the finite sum of multi-valued operators to general integrals and
expectations. Theorems 4 and 5 and their proofs remain valid with minimal modification
when the finite sum is replaced with the Aumann integral.
Demipositivity.
The demipositivity assumption was first formulated by Bruck [Bru75a].
The definition we use is equivalent to the definition formulated by Peypouquet and Sorin
[PS10]. See Exercise 7.4. Paramonotone operators, defined in the bibliographical notes
of §9, are also demipositive.


## Page 188

Exercises
173
Exercises
7.1 Convergence rate of the projected stochastic subgradient method. Consider the problem
minimize
x∈Rn
1
N
N
X
i=1
fi(x)
subject to
x ∈C,
where C is a nonempty closed convex set and fi is a CCP function on Rn such that
C ⊆dom ∂fi for i = 1, . . . , N. Assume ∥∂fi(x)∥≤G for any x ∈C for i = 1, . . . , N.
(This assumption is equivalent to assuming f1, . . . , fN are G-Lipschitz continuous on C.)
Consider the projected stochastic subgradient method:
xk+1 ∈ΠC

xk −αk∂fi(k)(xk)

.
Show that
f(¯xk) −f(x⋆) ≤∥x0 −x⋆∥2 + G2 Pk
i=0 α2
k
2 Pk
i=0 αk
,
where ¯xk is as defined in (7.3).
If αk = 1/(k + 1)p, for what value of p do we have
f(¯xk) −f(x⋆) →0?
Hint. Use the subgradient inequality to show
∥xi+1 −x⋆∥2 ≤∥xi −x⋆∥2 −2αi(f(xi) −f(x⋆)) + α2G2.
Then sum both sides from i = 0, . . . , k.
7.2 Convergence rate under strong monotonicity. In the setup for Theorem 4, furthermore
assume 픸+픹is µ-strongly monotone. Show that if αk = C/(k+1) for some large enough
C > 0, then
∥xk −x⋆∥2 ≤O(1/k).
Hint. Let U 0, U 1, . . . be a nonnegative sequence and let W 0, W 1, . . . be a nonnegative
summable sequence. Assume
U k+1 ≤

1 −σ
k + τ
k2

U k + W k −W k−1 + ρ
k2 ,
where σ > 0 and τ ≥0. Define
˜U k = kU k −
ρ
σ −1,
and show
˜U k+1 ≤

1 −σ −1
k
+ O
 1
k2

˜U k + O
 1
k2

+ (k + 1)(W k −W k+1).
Sum both sides to conclude
U k ≤
ρ
(σ −1)k + o
 1
k

.
7.3 Robust stochastic approximation. Consider the problem
minimize
x∈Rn
1
N
N
X
i=1
fi(x)
subject to
x ∈C,


## Page 189

174
7
Stochastic optimization
where fi are CCP functions on Rn with dom fi = Rn for i = 1, . . . , N, and C is a
nonempty convex set. For notational simplicity, define
f(x) = 1
N
N
X
i=1
fi(x).
Assume there is a G < ∞such that ∥∂fi(x)∥≤G for any x ∈C for i = 1, . . . , N.
Consider the projected stochastic subgradient method:
xk+1 ∈ΠC

xk −αk∂fi(k)(xk)

.
Use Exercise 7.1 to show that, with αk = γ/
√
k + 1 for any γ > 0, the averaged iterates
¯xk defined in (7.3) achieve the rate
f(¯xk) −f(x⋆) ≤O(1/
√
k).
Next, use Exercise 7.2 to show that, if f is µ-strongly convex and αk = γ/(k + 1) with
large enough γ > 0, the iterates achieve the rate
f(xk) −f(x⋆) ≤O(1/k).
Finally, consider the specific case n = N = 1, f1(x) = (µ/2)x2, and C = [−1, 1]. Show
that with x0 = 1, αk = γ/(k + 1), and γ < 1/µ,
f(xk) −f(x⋆) ≥O(1/kµγ).
Remark.
These results show that αk = γ/(k + 1) without averaging yields a rate of
convergence highly sensitive to the choice of γ, while αk = γ/
√
k + 1 with averaging more
robustly provides the rate of O(1/
√
k).
7.4 Equivalent definition of demipositivity. Peypouquet and Sorin [PS10] define a maximal
monotone operator 픸to be demipositive if there is an x⋆∈Zer 픸such that for every
sequence (xk, uk) ∈픸such that xk →x∞and uk is bounded:
⟨uk, xk −x⋆⟩→0
⇒
x∞∈Zer 픸.
Show that this definition of Peypouquet and Sorin is equivalent to our definition in §7.1.
7.5 Show that if 픸is maximal monotone and int (Zer 픸)̸ = ∅, then 픸is demipositive.
Hint. Let x⋆∈int (Zer 픸). Assume for contradiction that there is a x /∈Zer 픸such that
u ∈픸x and ⟨u, x −x⋆⟩= 0. Then x⋆+ εu ∈Zer 픸for small enough ε > 0.


## Page 190

Chapter 8
ADMM-type methods
In this chapter, we present the alternating direction method of multipliers (ADMM)
and its variants, which we loosely refer to as ADMM-type methods. We first present
FLiP-ADMM, a general and highly versatile variant, and establish its convergence
directly without relying on the machinery of monotone operators. We then derive
a wide range of ADMM-type methods from FLiP-ADMM.
8.1
Function-linearized proximal ADMM
Let f1 and f2 be CCP functions on Rp and g1 and g2 be CCP functions on Rq.
Let f2 and g2 be differentiable. For notational convenience, write
f = f1 + f2,
g = g1 + g2.
Let A ∈Rn×p, B ∈Rn×q, and c ∈Rn. Consider the primal problem
minimize
x∈Rp, y∈Rq
f1(x) + f2(x) + g1(y) + g2(y)
subject to
Ax + By = c,
(8.1)
generated by the Lagrangian
L(x, y, u) = f(x) + g(y) + ⟨u, Ax + By −c⟩.
The method function-linearized proximal alternating direction method of multipliers
(FLiP-ADMM) is
xk+1 ∈argmin
x∈Rp

f1(x) + ⟨∇f2(xk) + A⊺uk, x⟩+ ρ
2∥Ax + Byk −c∥2 + 1
2∥x −xk∥2
P

yk+1 ∈argmin
y∈Rq

g1(y) + ⟨∇g2(yk) + B⊺uk, y⟩+ ρ
2∥Axk+1 + By −c∥2 + 1
2∥y −yk∥2
Q

uk+1 = uk + ϕρ(Axk+1 + Byk+1 −c),
where ρ > 0, ϕ > 0, P ∈Rp×p, P ⪰0, Q ∈Rq×q, and Q ⪰0.


## Page 191

176
8
ADMM-type methods
Theorem 6 Consider FLiP-ADMM. Assume total duality. Assume the x- and y-
subproblems always have solutions. Assume f2 is Lf-smooth and g2 is Lg-smooth,
where Lf ≥0 and Lg ≥0. Assume there is an ε ∈(0, 2 −ϕ) such that
P ⪰LfI,
Q ⪰0,
ρ

1 −(1 −ϕ)2
2 −ϕ −ε

B⊺B + Q ⪰3LgI.
Then
f(xk) + g(yk) →f(x⋆) + g(y⋆),
Axk + Byk −c →0,
where (x⋆, y⋆) is a solution of the primal problem.
To clarify, when f2 = 0 or g2 = 0, we set Lf = 0 or Lg = 0, respectively.
8.1.1
Parameter choices
FLiP-ADMM has several algorithmic parameters, ϕ, ρ, P, Q, f2, and g2. Their
choices affect the number of iterations required to achieve a desired accuracy and
the computational cost per iteration.
The optimal choice for a given problem
balances the number of iterations and cost per iteration.
The condition
ρ

1 −(1 −ϕ)2
2 −ϕ −ε

B⊺B + Q ⪰3LgI
(8.2)
imposes constraints on ϕ and ρ. Note
1 −(1 −ϕ)2
2 −ϕ





> 0,
ϕ ∈(0,
√
5+1
2
)
= 0,
ϕ =
√
5+1
2
< 0,
ϕ ∈(
√
5+1
2
, 2).
For each ϕ ∈(0,
√
5+1
2
), there is a small enough ε > 0 such that
1 −(1 −ϕ)2
2 −ϕ −ε > 0,
so large ρ helps to satisfy (8.2). For each ϕ ∈[
√
5+1
2
, 2) and all ε ∈(0, 2 −ϕ),
1 −(1 −ϕ)2
2 −ϕ −ε < 0,
so small ρ helps to satisfy (8.2).
The dual extrapolation parameter ϕ
While the choice ϕ = 1 is most common, larger values for ϕ can provide a speedup.
When Q = 0 and Lg = 0, condition (8.2) is satisfied with ϕ ∈(0,
√
5+1
2
). This


## Page 192

8.1
Function-linearized proximal ADMM
177
is also the requirement for ϕ in the classical “golden ratio” ADMM setup, where
f2 = 0 (Lf = 0), g2 = 0 (Lg = 0), P = 0, and Q = 0.
In the classical ADMM setup, where f2 = 0, g2 = 0, P = 0, and Q = 0,
FLiP-ADMM reduces to
xk+1 ∈argmin
x∈Rp Lρ(x, yk, uk)
yk+1 ∈argmin
y∈Rq
Lρ(xk+1, y, uk)
uk+1 = uk + ϕρ(Axk+1 + Byk+1 −c),
where
Lρ(x, y, u) = f(x) + g(y) + ⟨u, Ax + By −c⟩+ ρ
2∥Ax + By −c∥2.
(8.3)
This is called the golden ratio ADMM, since the stepsize requirement is 0 < ϕ <
(1 +
√
5)/2, and (1 +
√
5)/2 ≈1.618 is the golden ratio.
Penalty parameter ρ
The parameter ρ controls the relative priority between primal and dual convergence.
The Lyapunov function used to prove convergence of FLiP-ADMM contains the
terms ρ∥B(yk −y⋆)∥2 (primal error) and
1
ϕρ∥uk −u⋆∥2 (dual error), and large ρ
prioritizes primal accuracy while small ρ prioritizes dual accuracy. When 0 < ϕ <
√
5+1
2
, we can use large ρ. When
√
5+1
2
≤ϕ < 2, we can use small ρ.
Proximal terms via P and Q
The letter “P” in FLiP-ADMM describes the presence of the proximal terms
1
2∥x −xk∥2
P ,
1
2∥y −yk∥2
Q.
Empirically, smaller P and Q lead to fewer required iterations. When f2 = 0 and
g2 = 0, the choice P = 0 and Q = 0 is often optimal in the number of required
iterations.
In the cases considered in §8.2.1 and §8.2.3, however, we can use a
nonzero P and Q to cancel out (linearize) unwieldy quadratic terms and thereby
reduce the cost per iteration.
Linearizing functions f2 and g2
When f2 = 0, the x-update of FLiP-ADMM is
xk+1 ∈argmin
x∈Rp

Lρ(x, yk, uk) + 1
2∥x −xk∥2
P

,
where Lρ is the augmented Lagrangian (8.3). When f2̸ = 0,
xk+1 ∈argmin
x∈Rp

f1(x) + f2(xk) + ⟨∇f2(xk), x −xk⟩+ g(yk)
+ ⟨uk, Ax + Byk −c⟩+ ρ
2∥Ax + Byk −c∥2 + 1
2∥x −xk∥2
P

,


## Page 193

178
8
ADMM-type methods
i.e., replace f2(x) with its first-order approximation f2(xk) + ⟨∇f2(xk), x −xk⟩in
Lρ(x, yk, uk) and minimize with respect to x. We call this linearizing the function
or function linearization. The same discussion holds for the y-update. The “FLi
(Function-Linearized)” in FLiP-ADMM describes this feature of accessing f2 and
g2 through their gradients.
FLiP-ADMM presents the choice of whether or not to use function-linearization.
Often, the choices f2 = 0 and g2 = 0 lead to fewer required iterations. In some
cases, however, nonzero choices of f2 and g2 reduces the cost per iteration of solving
the x- and y-subproblems.
8.1.2
Further discussion
Solvability of subproblems
We say the x- and y-subproblems are solvable if they have solutions (not necessarily
unique). Solvability of the subproblems is not automatic, even when total duality
holds and when f and g are CCP. In the derivation of ADMM in §3, solvability was
ensured by assuming the additional regularity condition (3.6). In this section, we
directly assume solvability instead. See the notes and references of §3 for further
discussion.
Notion of convergence
The notion of convergence in Theorem 6 is different from what we had previously
seen in Part I. The result establishes that the objective value converges to the
optimal value and that the constraint violation converges to 0 rather than showing
the iterates converge to a solution.
Relation to method of multipliers
The “AD (Alternating Direction)” in FLiP-ADMM describes the solving of the
two x- and y-subproblems in an alternating fashion. The “MM” in FLiP-ADMM
describes the method’s similarity to the method of multipliers, which has only one
primal subproblem.
When q = 0, the y-subproblem and B-matrix vanish, and the ADMM setup
reduces to the method of multipliers setup, and we obtain methods similar to what
we saw in Exercise 3.8. (Theorem 6 applies when q = 0.) In particular, when q = 0,
f2 = 0, g2 = 0, B = 0, P = 0, and Q = 0, FLiP-ADMM reduces to the classical
method of multipliers
xk+1 ∈argmin
x
n
f(x) + ⟨uk, Ax⟩+ ρ
2∥Ax −c∥2o
uk+1 = uk + ϕρ(Axk+1 −c),
which converges for ϕ ∈(0, 2).


## Page 194

8.1
Function-linearized proximal ADMM
179
8.1.3
Scaled form
With the substitution vk = (1/ρ)uk for k = 0, 1, . . . , FLiP-ADMM becomes
xk+1 ∈argmin
x∈Rp

f1(x) + ⟨∇f2(xk), x⟩+ ρ
2∥Ax + Byk −c + vk∥2 + 1
2∥x −xk∥2
P

yk+1 ∈argmin
y∈Rq

g1(y) + ⟨∇g2(yk), y⟩+ ρ
2∥Axk+1 + By −c + vk∥2 + 1
2∥y −yk∥2
Q

vk+1 = vk + ϕ(Axk+1 + Byk+1 −c).
We call this the scaled form of FLiP-ADMM. In some cases, the scaled forms of
ADMM-type methods are simpler than the original form and are therefore pre-
ferred. In this chapter, we use the unscaled form to make clear that the uk-iterates
represent (unscaled) dual variables.
8.1.4
Proof of Theorem 6
Proof. The assumption of total duality means L has a saddle point (x⋆, y⋆, u⋆).
Define
w⋆=


x⋆
y⋆
u⋆

,
wk =


xk
yk
uk


for k = 0, 1, . . . .
Define η = 2 −ϕ −ε. Define the symmetric positive semidefinite matrices
M0 = 1
2


P
0
0
0
ρB⊺B + Q
0
0
0
1
ϕρI

,
M1 = 1
2


0
0
0
0
Q + LgI
0
0
0
η
ϕ2ρI

,
M2 = 1
2


P −LfI
0
0
0
ρ

1 −(1−ϕ)2
η

B⊺B + Q −3LgI
0
0
0
2−ϕ−η
ϕ2ρ I

.
Define the Lyapunov function
V k = ∥wk −w⋆∥2
M0 + ∥wk −wk−1∥2
M1.
Proof outline.
In stage 1, we use the definition of xk+1 and yk+1 as minimizers to
obtain certain inequalities respectively relating xk+1 with x⋆and yk+1 with y⋆. In
stage 2, we use the definition of yk and yk+1 as minimizers to obtain an inequality
relating yk with yk+1. In stage 3, we use the inequalities of the previous stages to
establish the key inequality
V k+1 ≤V k −∥wk+1 −wk∥2
M2 −
 L(xk+1, yk+1, u⋆) −L(x⋆, y⋆, u⋆)

.
(8.4)
In stage 4, we use the summability argument to show convergence.


## Page 195

180
8
ADMM-type methods
Stage 1.
Generally, if z⋆∈argminz{h1(z) + h2(z)}, where h1 is convex and h2 is
differentiable convex, then z⋆∈argminz{h1(z) + ⟨∇h2(z⋆), z −z⋆⟩}. This fact can
be verified by considering the optimality conditions. In the x-subproblem defining
xk+1, we set h1 = f1 and h2 to the remaining terms and get
0 ≤f1(x) −f1(xk+1)
+

∇f2(xk) + A⊺(uk + ρ(Axk+1 + Byk −c)) + P(xk+1 −xk), x −xk+1
for any x ∈Rp. By convexity of f2 and Lf-smoothness of f2,
⟨∇f2(xk), x −xk+1⟩= ⟨∇f2(xk), x −xk⟩+ ⟨∇f2(xk), xk −xk+1⟩
≤f2(x) −f2(xk) + f2(xk) −f2(xk+1) + Lf
2 ∥xk+1 −xk∥2
= f2(x) −f2(xk+1) + Lf
2 ∥xk+1 −xk∥2.
Adding the two inequalities, we get
0 ≤f(x) −f(xk+1) + Lf
2 ∥xk+1 −xk∥2
+

A⊺(uk + ρ(Axk+1 + Byk −c)) + P(xk+1 −xk), x −xk+1
.
To simplify notation, define
ˆuk+1 = uk + ρ(Axk+1 + Byk+1 −c)
and rewrite the inequality as
f(xk+1) −f(x) +

ˆuk+1, A(xk+1 −x)

(8.5)
≤Lf
2 ∥xk+1 −xk∥2 + ρ

B(yk+1 −yk), A(xk+1 −x)

−

xk+1 −xk, xk+1 −x

P .
Repeating analogous steps with the y-update, we get
g(yk+1) −g(y) +

ˆuk+1, B(yk+1 −y)

≤Lg
2 ∥yk+1 −yk∥2 −

yk+1 −yk, yk+1 −y

Q
(8.6)
for any y ∈Rq.
Set x = x⋆in (8.5), set y = y⋆in (8.6), add the two inequalities, add the
identity
⟨u⋆−ˆuk+1, Axk+1 + Byk+1 −c⟩= 1
ρ⟨u⋆−ˆuk+1, ˆuk+1 −uk⟩,
and substitute
A(xk+1 −x⋆) = 1
ϕρ(uk+1 −uk) −B(yk+1 −y⋆)
u⋆−ˆuk+1 =

1 −1
ϕ

(uk+1 −uk) −(uk+1 −u⋆)
ˆuk+1 −uk = 1
ϕ
 uk+1 −uk


## Page 196

8.1
Function-linearized proximal ADMM
181
to get
L(xk+1, yk+1, u⋆) −L(x⋆, y⋆, u⋆)
≤Lf
2 ∥xk+1 −xk∥2 + Lg
2 ∥yk+1 −yk∥2 +

1 −1
ϕ
 1
ϕρ∥uk+1 −uk∥2
−2⟨wk+1 −wk, wk+1 −w⋆⟩M0 + 1
ϕ⟨uk+1 −uk, B(yk+1 −yk)⟩.
(8.7)
Stage 2.
Consider
g(yk+1) −g(yk) +

ˆuk+1, B(yk+1 −yk)

≤Lg
2 ∥yk+1 −yk∥2 −

yk+1 −yk, yk+1 −yk
Q ,
which follows from (8.6) with y = yk, and
g(yk) −g(yk+1) +

ˆuk, B(yk −yk+1)

≤Lg
2 ∥yk −yk−1∥2 −

yk −yk−1, yk −yk+1
Q ,
which follows from decrementing the indices (k + 1, k) to (k, k −1) in (8.6) and
using y = yk+1. We add the two inequalities and reorganize to get
1
ϕ⟨uk+1 −uk, B(yk+1 −yk)⟩
≤Lg
2 ∥yk+1 −yk∥2 + Lg
2 ∥yk −yk−1∥2 −∥yk+1 −yk∥2
Q
+ ⟨yk+1 −yk, yk −yk−1⟩Q −

1 −1
ϕ

⟨uk −uk−1, B(yk+1 −yk)⟩.
We apply Young’s inequality
⟨a, b⟩≤ζ
2∥a∥2 + 1
2ζ ∥b∥2,
∀a, b ∈Rn, ζ > 0
to the two inner products on the right-hand side and reorganize to get
1
ϕ⟨uk+1 −uk, B(yk+1 −yk)⟩
(8.8)
≤1
2∥yk+1 −yk∥2
LgI−Q+ (1−ϕ)2
η
ρB⊺B + 1
2∥yk −yk−1∥2
LgI+Q +
η
2ϕ2ρ∥uk −uk−1∥2
for any η > 0. The left-hand side of this inequality is the last term on the right-hand
side of (8.7).
Stage 3.
Using
∥wk+1 −w⋆∥2
M0 = ∥wk −w⋆∥2
M0 −∥wk+1 −wk∥2
M0 + 2⟨wk+1 −wk, wk+1 −w⋆⟩M0


## Page 197

182
8
ADMM-type methods
on the differences between V k+1 and V k, we get
V k+1 = V k −∥wk −wk−1∥2
M1 + ∥wk+1 −wk∥2
M1 −∥wk+1 −wk∥2
M0
+ 2⟨wk+1 −wk, wk+1 −w⋆⟩M0.
To this identity, we add the inequalities (8.8) and (8.7) to get
V k+1 ≤V k −1
2∥xk+1 −xk∥2
P −Lf I −1
2∥yk+1 −yk∥2
1−(1−ϕ)2
η

ρB⊺B+Q−3LgI
−2 −η −ϕ
2ϕ2ρ
∥uk+1 −uk∥2 −
 L(xk+1, yk+1, u⋆) −L(x⋆, y⋆, u⋆)

= V k −∥wk+1 −wk∥2
M2 −
 L(xk+1, yk+1, u⋆) −L(x⋆, y⋆, u⋆)

for any η > 0, which is the key inequality (8.4). Note that
L(xk+1, yk+1, u⋆) −L(x⋆, y⋆, u⋆) ≥0,
since (x⋆, y⋆, u⋆) is a saddle point of L.
Stage 4.
Applying the summability argument on (8.4) tells us ∥wk+1−wk∥2
M2 →0
and L(xk+1, yk+1, u⋆) −L(x⋆, y⋆, u⋆) →0. Note that ∥wk+1 −wk∥2
M2 →0 implies
uk+1 −uk →0 and thus Axk + Bxk −c →0. Since
L(xk+1, yk+1, u⋆) = f(xk+1) + g(yk+1) + ⟨u⋆, Axk+1 + Byk+1 −c⟩
|
{z
}
→0
→L(x⋆, y⋆, u⋆) = f(x⋆) + g(y⋆),
we conclude f(xk) + g(yk) →f(x⋆) + g(y⋆).
The inequalities we show in stages 1 and 2 are sometimes referred to as varia-
tional inequalities due to their connection to variational inequality problems. The
key technical difficulty of the proof is the construction of the Lyapunov function
V k, which comes from the insights accumulated over the many papers studying
various generalizations of ADMM.
8.2
Derived ADMM-type methods
8.2.1
Linearized methods
Consider the problem
minimize
x∈Rp, y∈Rq
f1(x) + g1(y)
subject to
Ax + By = c,
where f2 = 0 and g2 = 0. We use the linearization technique of §3.5 with FLiP-
ADMM. With P = (1/α)I −ρA⊺A and Q = (1/β)I −ρB⊺B, we get linearized


## Page 198

8.2
Derived ADMM-type methods
183
ADMM:
xk+1 = Proxαf
 xk −αA⊺(uk + ρ(Axk + Byk −c))

yk+1 = Proxβg
 yk −βB⊺(uk + ρ(Axk+1 + Byk −c))

uk+1 = uk + ϕρ(Axk+1 + Byk+1 −c).
The stepsize requirement is satisfied with 1 ≥αρλmax(A⊺A), 1 ≥βρλmax(B⊺B),
and 0 < ϕ < (1 +
√
5)/2. The linearized ADMM we had seen in §3.5 corresponds
to the case ϕ = 1.
“Linearization” in the context of ADMM-type methods is an ambiguous term
referring to more than one technique. While it most often refers to the technique
of canceling out inconvenient quadratic terms, there are other “linearizations” as
we will see in §8.2.2 and §8.2.6.
PDHG
Consider the problem
minimize
x∈Rp, y∈Rq
f1(x) + g1(y)
subject to
−Ix + By = 0.
As discussed in §3.5, PDHG is an instance of FLiP-ADMM. With ϕ = 1, P = 0,
and Q = (1/β)I −ρB⊺B, we recover PDHG
µk+1 = Proxρf ∗
1
 µk + ρB(2yk −yk−1)

yk+1 = Proxβg1
 yk −βB⊺µk+1
.
The stepsize requirement is 1 ≥βρλmax(B⊺B).
8.2.2
Function-linearized methods
FLiP-ADMM linearizes the functions f2 and g2, i.e., it accesses f2 and g2 through
their gradient evaluations rather than through minimization subproblems. This
feature provides great flexibility.
Condat–Vũ
Consider the problem
minimize
x∈Rp, y∈Rq
f1(x) + g1(y) + g2(y)
subject to
−Ix + By = 0.
FLiP-ADMM with ϕ = 1, P = 0, and Q = (1/β)I −ρB⊺B is
xk+1 = Prox(1/ρ)f1
 (1/ρ)uk + Byk
yk+1 = Proxβg1
 yk −β∇g2(yk) −βB⊺(uk −ρ(xk+1 −Byk))

uk+1 = uk −ρ(xk+1 −Byk+1).


## Page 199

184
8
ADMM-type methods
Use the Moreau identity (2.12) to get
xk+1 = (1/ρ)uk + Byk −(1/ρ) Proxρf ∗
1
 uk + ρByk
|
{z
}
=µk+1
yk+1 = Proxβg1
 yk −β∇g2(xk) −βB⊺µk+1
uk+1 = µk+1 + ρB(yk+1 −yk),
and we recover Condat–Vũ
µk+1 = Proxρf ∗
1
 µk + ρB(2yk −yk−1)

yk+1 = Proxβg1
 yk −β∇g2(yk) −βB⊺µk+1
.
Therefore, Condat–Vũ is a special case of FLiP-ADMM. The stepsize requirement
of FLiP-ADMM translates to the requirement 1 ≥βρλmax(B⊺B) + 3βLg, which is
worse than what we had seen in §3.3.
Doubly linearized ADMM
Consider the general problem
minimize
x∈Rp, y∈Rq
f1(x) + f2(x) + g1(y) + g2(y)
subject to
Ax + By = c.
FLiP-ADMM with P = (1/α)I −ρA⊺A and Q = (1/β)I −ρB⊺B is
xk+1 = Proxαf1
 xk −α
 ∇f2(xk) + A⊺uk + ρA⊺(Axk + Byk −c)

yk+1 = Proxβg1
 yk −β
 ∇g2(yk) + B⊺uk + ρB⊺(Axk+1 + Byk −c)

uk+1 = uk + ϕρ(Axk+1 + Byk+1 −c).
We call this method doubly linearized ADMM as it linearizes both the quadratic
terms and the functions f2 and g2.
The stepsize requirement is satisfied with
1 ≥αρλmax(A⊺A) + αLf, 1 ≥βρλmax(B⊺B) + 3βLg, and 0 < ϕ < (1 +
√
5)/2.
This method generalizes PDHG and Condat–Vũ.
Partial linearization
Consider the problem
minimize
x∈Rp, y∈Rq
f2(x) + g1(y) + g2(y)
subject to
Ax + By = c.
Assume γI + ρA⊺A is not easily invertible, but there is a C ≈ρA⊺A such that
γI + C is easily invertible, for γ > 0. Choose P = γI + C −ρA⊺A, where γ >
λmax(ρA⊺A −C). Since C ≈ρA⊺A is a close approximation, γ can be small.
In this case, the x-update of FLiP-ADMM is
xk+1 = xk −(γI + C)−1(∇f2(xk) + A⊺uk + ρA⊺(Axk + Byk −c)).


## Page 200

8.2
Derived ADMM-type methods
185
The x-update is easy to compute, and we say it has been partially linearized. In
contrast, the x-update of the doubly linearized ADMM is
xk+1 = xk −1
δ (∇f2(xk) + A⊺uk + ρA⊺(Axk + Byk −c))
for some δ > λmax(ρA⊺A). When C ≈ρA⊺A, partial linearization reduces the
number of required iterations compared to (full) linearization. This setup arises
when A⊺A is diagonally dominant in the regular basis or the discrete Fourier basis.
Example 8.1 CT imaging with total variation regularization. Consider the problem
minimize
x∈Rp
ℓ(Ax −b) + λ∥Dx∥1,
where x represents an unknown 2D or 3D image reshaped into a vector, A is the
discrete Radon transform operator, b represents the measurements, D is a finite
difference operator, and ℓis a CCP function. For simplicity, assume A⊺A is invertible.
The problem is equivalent to
minimize
x, y, z
1
2ℓ(y) + λ∥z∥1
subject to
A
D

x −
y
z

=
b
0

.
PDHG applied to the equivalent problem
uk+1 = Proxρℓ∗

uk + ρA(2xk −xk−1) −ρb

vk+1 = Π[−λ,λ]

vk+1 + ρD(2xk −xk−1)

xk+1 = xk −1
γ

A⊺uk+1 + Dvk+1
has a small cost per iteration, but sometimes requires too many iterations to converge.
Classic ADMM with ϕ = 1 applied to the equivalent problem
uk+1 = Proxρℓ∗

uk + ρA(2xk −xk−1) −ρb

vk+1 = Π[−λ,λ]

vk+1 + ρD(2xk −xk−1)

xk+1 = xk −(ρA⊺A + ρD⊺D)−1 
A⊺uk+1 + Dvk+1
cannot be implemented as (ρA⊺A + ρD⊺D)−1 is too expensive to compute. FLiP-
ADMM, where (i) we update the y- and z-variables first, the x-variable second, and
the dual variable last and (ii) we use the proximal term P = γI + C −ρA⊺A −ρD⊺D
for the x-update and ϕ = 1 for the dual update, simplifies to
uk+1 = Proxρℓ∗

uk + ρA(2xk −xk−1) −ρb

vk+1 = Π[−λ,λ]

vk+1 + ρD(2xk −xk−1)

xk+1 = xk −(γI + C)−1 
A⊺uk+1 + Dvk+1
.
See Exercise 8.2 for the derivation.


## Page 201

186
8
ADMM-type methods
This partially linearized method can provide a significant speedup over PDHG. We
can compute (γI + C)−1 efficiently with the fast Fourier transform; since A⊺A and
D⊺D are discretizations of shift-invariant continuous operators, they are closely ap-
proximated by circulant matrices, which are diagonalizable by the discrete Fourier
basis. A small γ > λmax(ρA⊺A + ρD⊺D −C) makes P small and thereby minimizes
the slowdown caused by the proximal term.
8.2.3
Block splitting
Partition x ∈Rp into m non-overlapping blocks of sizes p1, . . . , pm. Write x =
(x1, . . . , xm), so xi ∈Rpi for i = 1, . . . , m. Consider the problem
minimize
(x1,...,xm)∈Rp
m
X
i=1
fi(xi)
subject to
Ax = c,
(8.9)
where
A =
A:,1
A:,2
· · ·
A:,m

,
Ax = A:,1x1 + A:,2x2 + · · · + A:,mxm.
This problem is known as the multi-block ADMM problem or the extended monotropic
program.
The objective function splits across the blocks x1, . . . , xm.
However, the x-
updates of FLiP-ADMM couple the m blocks in general; FLiP-ADMM with no
function linearization and no y-block is
xk+1 ∈argmin
x∈Rp
( m
X
i=1
fi(xi) + ⟨A⊺uk, x⟩+ ρ
2∥Ax −c∥2 + 1
2∥x −xk∥2
P
)
uk+1 = uk + ρ(Ax −c),
and the blocks xk+1
1
, . . . , xk+1
m
cannot be computed independently. In this section,
we present techniques to obtain ADMM-type methods with split x-updates that
can be computed independently in parallel.
Orthogonal blocks
Consider problem (8.9). When the columns of A are block-wise orthogonal, i.e.,
A⊺
:,iA:,j = 0 for all i̸ = j, the x-updates of FLiP-ADMM with P = 0 split:
xk+1
i
∈argmin
xi∈Rpi
n
fi(xi) + ⟨uk −ρc, A:,ixi⟩+ ρ
2∥A:,ixi∥2o
for i = 1, . . . , m
uk+1 = uk + ϕρ(Ax −c).


## Page 202

8.2
Derived ADMM-type methods
187
Jacobi ADMM
Consider problem (8.9). Consider the matrix
P =


γI
−ρA⊺
:,1A:,2
· · ·
· · ·
−ρA⊺
:,1A:,m
−ρA⊺
:,2A:,1
γI
· · ·
· · ·
−ρA⊺
:,2A:,m
...
...
...
...
...
...
−ρA⊺
:,mA:,1
−ρA⊺
:,mA:,2
· · ·
−ρA⊺
:,mA:,(m−1)
γI


,
which is positive semidefinite for γ ≥ρλmax(A⊺A). Let
Lρ(x, u) =
m
X
i=1
fi(xi) + ⟨u, Ax −c⟩+ ρ
2∥Ax −c∥2.
Let xk̸
=i denote all components of xk excluding xk
i . Then FLiP-ADMM is
xk+1
i
= argmin
xi∈Rpi
n
Lρ(xi, xk̸
=i, uk) + γ
2 ∥xi −xk
i ∥2o
for i = 1, . . . , m
uk+1 = uk + ϕρ
 Axk+1 −c

.
This method is called Jacobi proximal ADMM in analogy to the Jacobi method
of numerical linear algebra; for i = 1, . . . , m, the update xk+1
i
is computed with
the other blocks fixed to the older copies xk
j for j̸ = i. The stepsize requirement is
satisfied with γ ≥ρλmax(A⊺A) and ϕ ∈(0, 2).
The off-diagonal blocks of P remove the interaction between the x-blocks and
thereby allow the x-update to split. Although we used γI for the diagonal blocks
of P, other choices are possible; they just need to be, loosely speaking, sufficiently
positive to ensure P is positive semidefinite.
In Exercise 8.3, we use different
diagonal blocks to perform linearizations with Jacobi ADMM.
Dummy variables
Consider the problem
minimize
(x1,...,xm)∈Rp
y∈Rn
m
X
i=1
fi(xi) + g(y)
subject to
Ax + y = c.
Introduce dummy variables z1, . . . , zm and eliminate y to get the equivalent problem
minimize
(x1,...,xm)∈Rp
z1,...,zm∈Rn
m
X
i=1
fi(xi) + g
 
c −
m
X
i=1
zi
!
subject to
A:,ixi −zi = 0
for i = 1, . . . , m.


## Page 203

188
8
ADMM-type methods
We apply FLiP-ADMM with P = 0, Q = 0, no function linearization, and initial
u-variables satisfying u0
1 = · · · = u0
m.
Then we can show uk
1 = · · · = uk
m for
k = 1, . . . , m, and the iteration simplifies to
xk+1
i
∈argmin
xi∈Rpi
n
fi(xi) +
D
uk + ρ
m(Axk −zk
sum), A:,ixi
E
+ ρ
2
A:,i(xi −xk
i )
2o
for i = 1, . . . , m
zk+1
sum = c −Prox m
ρ g

c −Axk+1 −m
ρ uk

uk+1 = uk + ϕρ
m
 Axk+1 −zk+1
sum

.
The stepsize requirement is ϕ ∈(0, (1 +
√
5)/2).
8.2.4
Consensus technique
Consider the problem
minimize
x∈Rp
n
X
i=1
fi(x).
Use the consensus technique to get the equivalent problem
minimize
x1,...,xn,z∈Rp
n
X
i=1
fi(xi)
subject to
xi = z,
for i = 1, . . . , n.
Here, xi ∈Rp is a copy of x ∈Rp. Apply FLiP-ADMM with P = 0, Q = 0, no
function linearization, and initial u-variables satisfying u0
1 + · · · + u0
n = 0 to get
xk+1
i
= argmin
x∈Rp
n
fi(xi) + ⟨uk
i , xi⟩+ ρ
2∥xi −zk∥2o
for i = 1, . . . , n
zk+1 = 1
n
n
X
i=1
xk+1
i
uk+1
i
= uk
i + ϕρ(xk+1
i
−zk+1)
for i = 1, . . . , n.
The stepsize requirement is ϕ ∈(0, (1 +
√
5)/2). To clarify, each xi represents a
copy of the entire x and therefore has the same dimension. This contrasts with the
block splitting of §8.2.3, where each xi represented a single block of x.
In this version of the consensus technique, we constrain x1, . . . , xn to equal a
single z. In general, one can have multiple z-variables related through a graph
structure. We explore this technique further in §11, in the context of decentralized
optimization.
8.2.5
2-1-2 ADMM
Consider the problem
minimize
x∈Rp, y∈Rq
f(x) + g(y)
subject to
Ax + By = c.


## Page 204

8.2
Derived ADMM-type methods
189
Assume g is a strongly convex quadratic function with affine constraints, i.e.,
g(y) = y⊺My + µ⊺y + δ{y∈Rq | Ny=ν}(y)
for some positive definite M ∈Rq×q, N ∈Rs×q, and ν ∈R(N). If there is no
affine constraint, we set s = 0. Define
Lρ(x, y, u) = f(x) + g(y) + ⟨u, Ax + By −c⟩+ ρ
2∥Ax + By −c∥2.
We call the method
yk+1/2 = argmin
y∈Rq
Lρ(xk, y, uk)
xk+1 ∈argmin
x∈Rp Lρ(x, yk+ 1
2 , uk)
yk+1 = argmin
y∈Rq
Lρ(xk+1, y, uk)
uk+1 = uk + ϕρ(Axk+1 + Byk+1 −c)
2-1-2 ADMM. As we soon show, 2-1-2 ADMM is an instance of FLiP-ADMM and
has the stepsize requirement of ϕ ∈(0, 2).
Derivation
As we show in Exercise 8.10, the y update can be expressed as
y(x) = argmin
y
Lρ(x, y, uk) = −TB⊺Ax + t(uk),
for a symmetric positive semidefinite T ∈Rq×q and a function t. Consider the
FLiP-ADMM
(xk+1, yk+1) ∈
argmin
x∈Rp, y∈Rq
n
Lρ(x, y, uk) + ρ
2∥x −xk∥2
P
o
uk+1 = uk + ϕρ(Axk+1 + Byk+1 −c),
(8.10)
with P = A⊺BTB⊺A. (In this instance of FLiP-ADMM, there is no second primal
block, so there is no alternating update.) The stepsize requirement is ϕ ∈(0, 2).
The optimality condition is
0 ∈∂f(xk+1) + A⊺ uk + ρ(Axk+1 + Byk+1 −c)

+ ρA⊺BTB⊺A(xk+1 −xk)
yk+1 = −TB⊺Axk+1 + t(uk).
On the other hand, the optimality condition of 2-1-2 ADMM is
yk+1/2 = −TB⊺Axk + t(uk)
0 ∈∂f(xk+1) + A⊺
uk + ρ(Axk+1 + Byk+1/2 −c)

yk+1 = −TB⊺Axk+1 + t(uk).
Eliminating yk+1/2 gives us the same optimality condition as that of (8.10). There-
fore, 2-1-2 ADMM and FLiP-ADMM (8.10) are equivalent in the sense that they
share the same set of iterates (xk, yk).


## Page 205

190
8
ADMM-type methods
8.2.6
Trip-ADMM
Consider the more general problem
minimize
x∈Rp, y∈Rq
f1(Cx) + f2(x) + g1(Dy) + g2(y)
subject to
Ax + By = c,
where C ∈Rr×p and D ∈Rs×q. We can solve this problem with







xk+1/2 = xk −σ
 C⊺vk + ∇f2(xk) + A⊺uk + ρA⊺(Axk + Byk −c)

vk+1 = Proxτf ∗
1

vk + τCxk+1/2
xk+1 = xk+1/2 −σC⊺ vk+1 −vk







yk+1/2 = yk −σ
 D⊺wk + ∇g2(yk) + B⊺uk + ρB⊺(Axk+1 + Byk −c)

wk+1 = Proxτg∗
1

wk + τDyk+1/2
yk+1 = yk+1/2 −σD⊺ wk+1 −wk
uk+1 = uk + ρ
 Axk+1 + Byk+1 −c

,
which we call Triple-linearized ADMM (Trip-ADMM). The stepsize requirement is
satisfied with ρ > 0, σ > 0, and τ > 0,
1 ≥σρλmax(A⊺A) + σLf,
1 ≥σρλmax(B⊺B) + 3σLg,
1 ≥στλmax(CC⊺),
1 ≥στλmax(DD⊺),
and under total duality, we have
f1(Cxk −σ ˜C⊺˜C(vk+1 −vk)) + f2(xk) + g1(Dyk −σ ˜D⊺˜D(wk+1 −wk)) + g2(yk)
→f1(Cx⋆) + f2(x⋆) + g1(Dy⋆) + g2(y⋆)
˜C⊺˜C(vk+1 −vk) →0,
˜D⊺˜D(wk+1 −wk) →0
Axk + Bxk −c →0.
Derivation
First, we show that for any CCP function h on Rn and A ∈Rm×n,

µ+
∈argmin
µ∈Rm
n
h∗(µ) −⟨z0, A⊺µ⟩+ α
2 ∥A⊺µ∥2
2
o
x+
= z0 −αA⊺µ+


(8.11)
⇒
x+ = argmin
x∈Rn

h(Ax) + 1
2α∥x −z0∥2
2

,


## Page 206

8.2
Derived ADMM-type methods
191
provided that an argmin µ+ exists. This follows from
x+ =z0 −αA⊺µ+, µ+ is an argmin
⇔
x+ = z0 −αA⊺µ+, ∂h∗(µ+) −Az0 + αAA⊺µ+ ∋0
⇔
x+ = z0 −αA⊺µ+, ∂h∗(µ+) ∋Ax+
⇔
A⊺µ+ + 1
α(x+ −z0) = 0, µ+ ∈∂h(Ax+)
⇔
A⊺∂h(Ax+) + 1
α(x+ −z0) ∋0
⇒
x+ is the argmin.
We now start the derivation. Consider the equivalent problem
minimize
x∈Rp, ˜x∈Rr
y∈Rq, ˜y∈Rs
f1(Cx + ˜C˜x) + f2(x) + g1(Dy + ˜D˜y) + g2(y)
subject to
Ax + By = c
1
√ρσ ˜x = 0
1
√ρσ ˜y = 0,
where ˜C ∈Rr×r and ˜D ∈Rs×s. FLiP-ADMM applied to this method is
(xk+1, ˜xk+1) ∈
argmin
x∈Rp, ˜x∈Rr

f1(Cx + ˜C˜x) + ⟨∇f2(xk) + A⊺uk, x⟩+
1
√ρσ ⟨˜uk
x, ˜x⟩
+ ρ
2∥Ax + Byk −c∥2 + 1
2σ ∥˜x∥2 + 1
2∥x −xk∥2
P + 1
2∥x −xk∥2
˜
P

(yk+1, ˜yk+1) ∈
argmin
y∈Rq, ˜y∈Rs

g1(Dy + ˜D˜y) + ⟨∇g2(yk) + B⊺uk, y⟩+
1
√ρσ ⟨˜uk
y, ˜y⟩
+ ρ
2∥Axk+1 + By −c∥2 + 1
2σ ∥˜y∥2 + 1
2∥y −yk∥2
Q + 1
2∥˜y −˜yk∥2
˜
Q

uk+1 = uk + ϕρ(Axk+1 + Byk+1 −c)
˜uk+1
x
= ˜uk
x + ϕ
p
ρ/σ˜xk+1
˜uk+1
y
= ˜uk
y + ϕ
p
ρ/σ˜yk+1.
Let
ϕ = 1,
P = 1
σ I −ρA⊺A,
˜P = 0,
Q = 1
σ I −ρB⊺B,
˜Q = 0.


## Page 207

192
8
ADMM-type methods
Then we have
(xk+1, ˜xk+1) ∈
argmin
x∈Rp, ˜x∈Rr

f1(Cx + ˜C˜x) + 1
2σ
˜x +
√σ
√ρ ˜uk
x

2
+ 1
2σ
x −xk + σ
 ∇f2(xk) + A⊺uk + ρA⊺(Axk + Byk −c)
2 
(yk+1, ˜yk+1) ∈
argmin
y∈Rq, ˜y∈Rs

g1(Dy + ˜D˜y) + 1
2σ
˜y +
√σ
√ρ ˜uk
y

2
+ 1
2σ
y −yk + σ
 ∇g2(yk) + B⊺uk + ρB⊺(Axk+1 + Byk −c)
2 
uk+1 = uk + ρ(Axk+1 + Byk+1 −c)
˜uk+1
x
= ˜uk
x +
p
ρ/σ˜xk+1
˜uk+1
y
= ˜uk
y +
p
ρ/σ˜yk+1.
Using (8.11), we get
vk+1 = argmin
v∈Rr

f ∗
1 (v) +
√σ
√ρ ˜uk
x, ˜C⊺v

+ σ
2

∥C⊺v∥2 + ∥˜C⊺v∥2
−

xk −σ
 ∇f2(xk) + A⊺uk + ρA⊺(Axk + Byk −c)

, C⊺v
 
xk+1 = xk −σ
 ∇f2(xk) + A⊺uk + ρA⊺(Axk + Byk −c)

−σC⊺vk+1
˜xk+1 = −
√σ
√ρ ˜uk
x −σ ˜C⊺vk+1
wk+1 = argmin
w∈Rs

g∗
1(w) +
√σ
√ρ ˜uk
y, ˜D⊺w

+ σ
2

∥D⊺w∥2 + ∥˜D⊺w∥2
−

yk −σ
 ∇g2(yk) + B⊺uk + ρB⊺(Axk+1 + Byk −c)

, D⊺w
 
yk+1 = yk −σ
 ∇g2(yk) + B⊺uk + ρB⊺(Axk+1 + Byk −c)

−σD⊺wk+1
˜yk+1 = −
√σ
√ρ ˜uk
y −σ ˜D⊺wk+1
uk+1 = uk + ρ(Axk+1 + Byk+1 −c)
˜uk+1
x
= ˜uk
x +
p
ρ/σ˜xk+1 = −√ρσ ˜C⊺vk+1
˜uk+1
y
= ˜uk
y +
p
ρ/σ˜yk+1 = −√ρσ ˜D⊺wk+1.


## Page 208

8.2
Derived ADMM-type methods
193
Eliminating some variables, we get
vk+1 = argmin
v∈Rr

f ∗
1 (v) −σ
D
vk, ˜C ˜C⊺v
E
+ σ
2

∥C⊺v∥2 + ∥˜C⊺v∥2
−

xk −σ
 ∇f2(xk) + A⊺uk + ρA⊺(Axk + Byk −c)

, C⊺v
 
xk+1 = xk −σ
 ∇f2(xk) + A⊺uk + ρA⊺(Axk + Byk −c) + C⊺vk+1
wk+1 = argmin
w∈Rs

g∗
1(w) −σ
D
wk, ˜D ˜D⊺w
E
+ σ
2

∥D⊺w∥2 + ∥˜D⊺w∥2
−

yk −σ
 ∇g2(yk) + B⊺uk + ρB⊺(Axk+1 + Byk −c)

, D⊺w
 
yk+1 = yk −σ
 ∇g2(yk) + B⊺uk + ρB⊺(Axk+1 + Byk −c) + D⊺wk+1
uk+1 = uk + ρ(Axk+1 + Byk+1 −c).
Next, we set
˜C ˜C⊺= 1
τσ I −CC⊺,
˜D ˜D⊺= 1
τσ I −DD⊺
to get
vk+1 = Proxτf ∗
1

vk + τC
 xk −σ
 ∇f2(xk) + A⊺uk + ρA⊺(Axk + Byk −c) + C⊺vk 
xk+1 = xk −σ
 ∇f2(xk) + A⊺uk + ρA⊺(Axk + Byk −c) + C⊺vk+1
wk+1 = Proxτg∗
1

wk + τD
 yk −σ
 ∇g2(yk) + B⊺uk + ρB⊺(Axk+1 + Byk −c) + D⊺wk 
yk+1 = yk −σ
 ∇g2(yk) + B⊺uk + ρB⊺(Axk+1 + Byk −c) + D⊺wk+1
uk+1 = uk + ρ
 Axk+1 + Byk+1 −c

.
The minimization subproblems are solvable since they are evaluations of proximal
operators of the CCP functions f1 and g1. We further simplify to get
xk+1/2 = xk −σ
 C⊺vk + ∇f2(xk) + A⊺uk + ρA⊺(Axk + Byk −c)

vk+1 = Proxτf ∗
1

vk + τCxk+1/2
xk+1 = xk+1/2 −σC⊺ vk+1 −vk
yk+1/2 = yk −σ
 D⊺wk + ∇g2(yk) + B⊺uk + ρB⊺(Axk+1 + Byk −c)

wk+1 = Proxτg∗
1

wk + τDyk+1/2
yk+1 = yk+1/2 −σD⊺ wk+1 −wk
uk+1 = uk + ρ
 Axk+1 + Byk+1 −c

.


## Page 209

194
8
ADMM-type methods
8.3
Bregman methods
A class of methods called the Bregman methods were developed and popularized
in the image processing community. Later, it was discovered that the Bregman
methods are related to the method of multipliers and ADMM. In this section, we
briefly describe the relationship.
Bregman distance.
Let f be a CCP function. When f is differentiable, we define
the f-induced Bregman distance or Bregman divergence as
Df(x, y) = f(x) −f(y) −⟨∇f(y), x −y⟩.
When f is not differentiable, we use
Dv
f(x, y) = f(x) −f(y) −⟨v, x −y⟩,
where v ∈∂f(y).
Df generalizes the squared Euclidean distance, since Df(x, y) = ∥x −y∥2 when
f(x) = ∥x∥2. Df(x, y) ≥0 follows from convexity of f. However, despite its name,
the Bregman “distance” is not a mathematical distance (metric). In particular,
Df(x, y) may not equal Df(y, x), and Df(x, y) = 0 may hold for x̸ = y.
Bregman method and method of multipliers.
Consider the problem
minimize
x∈Rn
f(x)
subject to
Ax = b,
(8.12)
where f is CCP, A ∈Rm×n, and b ∈Rm.
Let h(x) = ˆh(Ax −b), for some
differentiable CCP function ˆh such that ˆh(0) = 0 and ˆh(u) > 0 for u̸ = 0. When f
is differentiable, the Bregman method is
xk+1 = argmin
x∈Rn

Df(x, xk) + ρh(x)
	
,
where ρ is a scalar. When f is not differentiable, the Bregman method is
xk+1 = argmin
x∈Rn
n
Dvk
f (x, xk) + ρh(x)
o
vk+1 = vk −ρ∇h(xk+1),
where v0 ∈∂f(x0). The optimality condition of the first step ensures
vk+1 = vk −ρ∇h(xk+1) ∈∂f(xk+1).
Since the argmin depends on xk only through vk ∈∂f(xk), we can pick any v0 ∈
range (∂f) without explicitly specifying x0. The method converges under certain
mild conditions.
When h(x) = 1
2∥Ax −b∥2, the Bregman method with the change of variables
vk = −A⊺uk coincides with the method of multipliers
xk+1 ∈argmin
x∈Rn
n
f(x) + ⟨uk, Ax⟩+ ρ
2∥Ax −b∥2o
uk+1 = uk + ρ(Axk+1 −b).


## Page 210

8.3
Bregman methods
195
Split Bregman method and ADMM.
Consider the problem
minimize
x∈Rp, y∈Rq
f(x) + g(y)
subject to
Ax + y = c,
where f and g are CCP functions, A ∈Rq×p, and c ∈Rq. Let h(x) = 1
2∥Ax+y−c∥2
and apply the Bregman method to f(x) + g(y) to get
(xk+1, yk+1) ∈
argmin
x∈Rp, y∈Rq
n
Dvk
f (x, xk) + Duk
g (y, yk) + ρ
2∥Ax + y −b∥2o
vk+1 = vk −ρA⊺(Axk+1 + yk+1 −c)
uk+1 = uk −ρ(Axk+1 + yk+1 −c).
Using vk = A⊺uk, we eliminate vk to get
(xk+1, yk+1) ∈
argmin
x∈Rp, y∈Rq
n
f(x) + g(y) −⟨uk, Ax + y⟩+ ρ
2∥Ax + y −c∥2o
uk+1 = uk −ρ(Axk+1 + yk+1 −c).
The split Bregman method computes xk+1 and yk+1 approximately through alter-
nating updates. When only one pass of sequential minimization of x and then y is
performed, the split Bregman method coincides with ADMM.
Conclusion
In this section, we established the convergence of FLiP-ADMM and presented
techniques for applying the method to a wide range of problems. The exercises
further illustrate that the modular techniques can be combined to solve problems
with complicated structures.
The analysis of FLiP-ADMM differs from that of Part I, where we derived var-
ious methods, including ADMM-type methods, as instances of monotone operator
methods. There are two distinct approaches to analyze the classical ADMM. The
first is to derive ADMM from DRS, as we did in §3. This approach leads to a possi-
ble intermediate dual variable update, as we discuss in Exercise 8.1. The second is
to construct a Lyapunov function and analyze convergence directly. This approach
leads to a possible dual extrapolation parameter ϕ. To the best of our knowledge,
the fully general FLiP-ADMM cannot be reduced to a monotone operator splitting
method and therefore must be analyzed directly with a Lyapunov function.
ADMM-type methods are “splitting methods” in that they decompose the opti-
mization problem into smaller, simpler pieces and operate on them separately. They
are intimately related to monotone operator methods, although, strictly speaking,
they are not monotone operator methods themselves.


## Page 211

196
8
ADMM-type methods
Bibliographical Notes
FLiP-ADMM.
As individual components of ADMM-type methods, the dual extrapola-
tion parameter, function linerization, and proximal terms are known techniques; FLiP-
ADMM merely combines them. Among published ADMM-type methods, the randomized
primal-dual block coordinate update method (RPDBU) of Gao, Xu, and Zhang [GXZ19]
is most similar to FLiP-ADMM. RPDBU allows the x- and y-updates to be partially
updated in a randomized coordinate-update fashion but does not incorporate the dual
extrapolation parameter.
Early development.
ADMM dates back to the 1970s. When Glowinski and Marroco
was studying nonlinear Dirichlet problems in the form of
minimize
v∈V
f(Av) + g(v),
(8.13)
they reformulated it as
minimize
u∈AV, v∈V
f(u) + g(v)
subject to
u −Av = 0
(8.14)
and applied Hestenes and Powell’s augmented Lagrangian method (ALM) [Hes69, Pow69].
In [GM75b], Glowinski and Marroco proposed to solve the ALM subproblem by updating
u and v in an alternating manner while the Lagrange multipliers are fixed until a stopping
criterion is met. Their approach hinted at ADMM. ADMM for (8.14) was first presented
with a convergence proof by Gabay and Mercier [GM76, Algorithm 3.4]. They credited
[GM75a] for numerical experiments of their algorithm without proof. Gabay and Mercier’s
proof assumes g is linear and establishes subsequence-convergence of the dual iterates for
ϕ ∈(0, 2). When the objective functions are differentiable, they obtain convergence of the
dual iterates. Then Glowinski and Fortin [FG83] took a large step forward to studying
general convex f and g. They proved subsequence-convergence of the dual iterates for ϕ ∈
(0,
√
5+1
2
). Later using [Opi67], Glowinski and Le Tallec obtained convergence of the dual
iterates (weak convergence in infinite-dimensional Hilbert spaces) [GLT89]. Bertsekas and
Tsitsiklis also presented a proof in [BT89, §3.4].
Relationship with DRS.
In [Roc76b] Rockafellar showed that ALM for a linearly con-
strained convex problem is the proximal point method applied to its dual problem, i.e.,
“ALM = PPM to the dual.” Gabay [Gab83] extended this result to “ADMM = DRS
to the dual” and “PRS-ADMM = PRS to the dual.” (We discuss PRS-ADMM in Exer-
cise 8.1.) Following Gabay’s naming in [Gab83], many numerical analysts refer to ALM,
ADMM, and PRS-ADMM as ALG1, ALG2, and ALG3, repsectively. Using this charac-
terization, Eckstein generalized ADMM to allow the subproblems to be solved inexactly
[Eck89, Proposition 4.7].
Although ADMM is equivalent to DRS applied to the dual, one can still directly apply
ADMM to the dual. Eckstein [Eck89, Chapter 3.5] showed that ADMM is equivalent to
DRS applied to the primal problem when A = I, Eckstein and Fukushima [EF94] showed
the same for certain special problems, and Yan and Yin [YY16] extended their results to
general ADMM.
Update order.
Swapping the orders of the two subproblems of ADMM leads to different
iterates in general, and Bauschke and Moursi studied the dependence on the iterates on
this order [BM16]. Yan and Yin [YY16] showed that the two iterates generated by the
two orders are in fact equivalent if one of the functions is quadratic.
While either of
the two orders leads to convergence, repeatedly switching the orders causes divergence


## Page 212

Bibliographical Notes
197
as demonstrated by an example in [YY16]. Sun, Luo, and Ye [SLY20] showed that, for
solving linear systems of equations, ADMM under randomly permuted orders converges
in expectation.
Parameter selection.
The general question of how to optimally choose the scalar pa-
rameters ϕ and ρ is open. Ghadimi, Teixeira, Shames, and Johansson characterized the
optimal parameters for the specific problem of ℓ2 regularized and constrained quadratic
programming [GTSJ15]. There has been extensive work presenting adaptive methods for
tuning ρ in various settings [HYW00, Woh17, XFG17, XFY+17, XLLY17].
Dual extrapolation parameter.
The first appearance of ϕ ∈(0, (1+
√
5)/2), the golden
ratio range of the dual extrapolation parameter, is due to Fortin and Glowinski [FG83,
Glo84]. Xu showed that the same golden ratio range can be used for proximal ADMM
[Xu07]. Tao and Yuan showed that when both f and g are quadratics, the parameter
range extends to ϕ ∈(0, 2) [TY18].
Techniques.
Rockafellar presented the proximal method of multipliers [Roc76a]. Chen
and Teboulle presented the predictor corrector proximal multiplier method [CT94]. Shefi
and Teboulle [ST14] later identified Chen and Teboulle’s method to be an instance of
what we call the linearized method of multipliers. Eckstein presented proximal ADMM
and showed it is Douglas–Rachford splitting applied to the saddle subdifferential [Eck94].
He, Liao, Han, and Yang further generalized proximal ADMM [HLHY02].
However,
what we call the “linearization technique,” where one chooses the proximal term carefully
to cancel out and linearize quadratic terms, was likely unknown at the time of these
publications. The first explicit description of the linearization technique is due to the
concurrent work of Deng and Yin [DY16b] and Shefi and Teboulle [ST14].
Partial linearization in ADMM was first proposed by Deng and Yin [DY16b], and was
applied to CT and PET imaging by Ryu, Ko, and Won [RKW20]. In particular, the
method presented in Example 8.1 is the near-circulant splitting of [RKW20].
Function linearization in ADMM was first presented by Yang and Zhang [YZ11]; they
applied function linearization to one quadratic subproblem. Lin, Ma, and Zhang [LMZ17]
applied function linearization to general smooth convex functions in an ADMM-type
method. Banert, Boţ, and Csetnek [BBC21] applied function linearization to one function
with the ADMM with proximal terms and B = I. Gao, Xu, and Zhang applied function
linearization to both x- and y-subproblems [GXZ19].
Jacobi-ADMM was first presented in [DLPY17, GHY14, HHY15, Tao14, HXY16, BK19].
Similar but different methods are proposed and analyzed in [TY12, WS17, WHML15].
The 2-1-2 technique was first presented by Sun, Toh, Yang, and Li in [STY15, LST16].
They also showed that the technique can be applied twice and that it can be combined
with linearizations, as we do in Exercises 8.11 and 8.12. The 2-1-2 technique has also been
used as the basis for the symmetric Gauss–Seidel ADMM of Li, Sun, and Toh [LST19].
3- and multi-block ADMM.
Since the early 2010s, there have been attempts to gen-
eralize ADMM to three or more blocks of primal variables.
Chen, He, Ye, and Yuan
[CHYY16] showed that the direct extension of ADMM to three blocks with sequential
updates does not converge. On the other hand, the multi-block generalization does con-
verge with additional assumptions or modifications [HTY12, HY12a, CSY13, LMZ15b,
LST15, SLY20, LMZ16, HL17, CST17a, DY17b, HTY17, LST19, XXS19].
Using the reformulations of §8.2.3, the multi-block ADMM setup can be solved with
existing ADMM-type methods, but an open question is finding a method that converges
fast for the multi-block ADMM setup.
The 2019 work of P. Xiao, Z. Xiao, and Sun
[XXS19] provides excellent discussion on this subject and experimentally compares the


## Page 213

198
8
ADMM-type methods
three competitive methods: Gaussian back substitution ADMM by He, Tao, and Yuan
[HTY12, HTY17], symmetric Gauss–Seidel ADMM by Li, Sun, Toh, and Chen [CST17a,
LST19], and RP-ADMM by Sun, Luo, and Ye [SLY20].
Applications.
In image processing, Wang, Yang, Yin, and Zhang [WYYZ08] formulated
a total variation deblurring problem with (8.14) such that both subproblems have closed-
form solutions; however, their method is inexact ALM rather than ADMM. In compressed
sensing, Yang and Zhang [YZ11] applied ADMM to ℓ1-optimization. Wen, Goldfarb, and
Yin [WGY10] used ADMM to solve semidefinite and conic programs, and O’Donoghue,
Chu, Parikh, and Boyd [OCPB16] applied ADMM to the self-dual homogeneous embed-
ding reformulation of conic programs. Lin, Ma, Ye, and Zhang [LMYZ21] used ADMM
on a barrier formulation of linear programming. Yuan and Yang [YY13b, YY13a] used
ADMM to recover sparse and low-rank components of a matrix.
Yuan [Yua12] used
ADMM for covariance matrix selection. Ma, Xue, and Zou [MXZ13] used ADMM for
graphical model selection. Liu et al. [LMT+10] used ADMM for metric learning. Due to
its popularity, ADMM has numerous other applications.
Relationship with Bregman methods.
Bregman methods successively minimize a
sequence of Bregman distances instead of updating Lagrange multipliers. Osher et al.
[OBG+05] proposed the Bergman method in the context of image processing for finding
an member of {x | ∥Ax−b∥≤ε} for some small ε > 0 that serves as a good reconstruction
of the original image. This motivation is why the Bregman method looks like a method
for minimizing h, rather than minimizing f. Osher et al. shows h(xk) →argmin h mono-
tonically in [OBG+05]. Yin, Osher, Goldfard, and Darbon proved the Bregman method
converges to a solution of the optimization problem [YOGD08, Section 5.1,5.2] and ar-
gued that the method is equivalent to the method of multipliers, and more generally
the augmented Lagrangian method, under a change of variable [YOGD08, Section 3.4].
In [YOGD08, Section 5.3], they introduced linearized Bregman iteration. Both linearized
Bregman and linearized method of multipliers have simpler subproblems, but they are not
equivalent. Goldstein and Osher [GO09] introduced the Split Bregman method, equivalent
to the method of multipliers under change of variables, and reported great empirical per-
formance with a “single-pass,” which is equivalent to ADMM for (8.14). Zhang, Burger,
and Osher [ZBO11] linearized a split Bregman subproblem, obtaining a method that is
equivalent to linearized ADMM for (8.14). These works helped to popularize ADMM-type
methods in image processing. For other convergence results of the Bregman method, see
[OBG+05] for the general setting, [YOGD08, YO13] for ℓ1-norm and piece-wise linear
functions, and [JZZ09].
Other ADMM-type methods.
Wang and Banerjee [WB12] extended ADMM to the
online setting. Suzuki [Suz13] and Ouyang, He, Tran, and Gray [OHTG13] concurrently
extended ADMM to taking stochastic samples. Suzuki [Suz14], Zhong and Kwok [ZK14b],
and Zheng and Kwok [ZK16] presented accelerated stochastic ADMM using variance
reduction techniques.
Yi and Pavel [YP19] applied ADMM to computing generalized
Nash equilibrium. Chen, Chan, Ma, and Yang [CCMY15] and Boţ, Csetnek, and Hendrich
[BCH15] presented ADMM and DRS with with inertial acceleration.
Convergence rates.
Researchers have used different quantities to measure the rate of
ADMM convergence. He and Yuan [HY12b] established an O(1/k) rate that is applied
to the violation of a variational-inequality optimality condition of ADMM. Monterio and
Svaiter [MS13] showed another O(1/k) rate that is applied to the sizes of some approxi-
mate subgradients and their approximate levels. Shefi and Teboulle [ST14] analyzed the
convergence rates for the proximal and linearized ADMM. He and Yuan [HY15] showed
that fixed-point residuals decay at an O(1/k) rate. Davis and Yin [DY16a, DY17a] pre-
sented a comprehensive list of rates for function value and constraint violation correspond-


## Page 214

Bibliographical Notes
199
ing to different smoothness and strong convexity assumptions. They also improved the
O(1/k) rate of some setups to o(1/k) and establish tightness of the o(1/k) rate by extend-
ing examples from [BBCN+14]. Lin, Ma, and Zhang [LMZ15b] presented conditions for
this rate to hold for multi-block ADMM. Deng, Lai, Peng, and Yin established an o(1/k)
rate for Jacobi-ADMM [DLPY17].
With some additional assumptions, ADMM can be modified to achieve an accelerated
sublinear rate. Assuming strong convexity on f and g, Goldstein, O’Donoghue, Setzer,
and Baraniuk [GOSB14] used a modified ADMM to achieve an O(1/k2) rate. Ouyuang,
Chen, Lan, and Pasiliao [OCLPJ15] introduced an accelerated linearized ADMM that
also linearizes one objective function f. Assuming f is Lf Lipschitz differentiable, they
established a rate in the form of O(Lg/k2 + C/k), where C includes quantities indepen-
dent of Lg. Xu [Xu17] proposed a modified linearized ADMM that achieves a O(1/k2)
rate when either f or g1 + g2 is strongly convex. His method linearizes the Lipschitz
differentiable function g2.
Under different combinations of assumptions, ADMM converges linearly. Deng and Yin
[DY16b] proved linear convergence of ADMM for four combinations, and Davis and Yin
[DY17a, §6] discovered more combinations. Giselsson [GB15], Giselsson and Boyd [GB17],
Moursi and Vandenberghe [MV19], and Ryu, Taylor, Bergeling, and Giselsson [RTBG20]
obtained tight linear rates for certain combinations. Hong and Luo [HL17] established
linear convergence for multi-block ADMM under an “error-bound” condition. Lin, Ma,
and Zhang [LMZ15a] established linear convergence for multi-block ADMM under certain
strong convexity, smoothness, and rank conditions.
Linear convergence of ADMM has also been studied for specific classes of problems. Eck-
stein and Bertsekas [EB90] proved it for linear programming. Bauschke et al. [BBCN+14]
showed that, for finding an intersection point between two subspaces, the linear rate of
ADMM is the cosine of the Friedrichs angle between the subspaces. Boley [Bol13] analyzed
linear convergence of ADMM in different phases when applied to certain quadratic prob-
lems. Raghunathan and Di Cairano [RDC14] related the linear rate of ADMM applied
to quadratic programming with linear equality and bound constraints to the spectrum
of the Hessian and the Friedrichs angle. Aspelmeier, Charitha, and Luke [ACL16] estab-
lished eventual linear convergence based on metric subregularity. Liang, Fadili, and Peyré
[LFP17] studied local linear convergence and manifold identification.
Miscellaneous.
Eckstein showed that when total duality fails, ADMM diverges in the
sense that it generates unbounded iterates [Eck89, Proposition 4.8].
There has been
extensive work characterizing the manner in which the iterates diverge and using the
divergent iterates to identify pathological problems [RDC14, SBG+20, BGSB19, LRY19,
RLY19].
Given a Douglas–Rachford splitting operator TDRS, there generally is no function f such
that TDRS = Proxf [DY16a], but, when it exists, it is called the Douglas–Rachford en-
velope. Patrinos, Stella, Bemporad, and Themelis showed that the Douglas–Rachford
envelope exists under smoothness conditions and used it to accelerate DRS and ADMM
[PSB14, TP20]. Liu and Yin [LY19] gave the conditions for the Davis–Yin envelope to
exist.
Finally, the review papers by Boyd et al. [BPC+11], Eckstein [Eck12], and Glowin-
ski [Glo14] serve as excellent tutorials on ADMM.


## Page 215

200
8
ADMM-type methods
Exercises
8.1 Peaceman–Rachford ADMM. In §3, we derived ADMM as an instance of DRS. One may
wonder: what if we used the FPI with
(1 −θ)I + θRα∂˜
fRα∂˜g,
where ˜f and ˜g are as defined in §3.1 or 3.2, with θ ∈(0, 1)? Do we recover the golden
ratio ADMM? The answer is no. Show that we instead get
xk+1 = argmin
x
Lα(x, yk, uk)
uk+1/2 = uk + α(2θ −1)(Axk+1 + Byk −c)
yk+1 = argmin
y
Lα(xk+1, y, uk+1/2)
uk+1 = uk+1/2 + α(Axk+1 + Byk+1 −c).
When θ = 1, this method is called Peaceman–Rachford ADMM. Although Peaceman–
Rachford ADMM does not converge in general, it can be faster than regular ADMM under
additional assumptions [Gab83, HLWY14].
8.2 Provide the derivation of Example 8.1.
Hint. First, show that FLiP-ADMM can be written as
yk+1 = Prox 1
ρ ℓ

Axk −b + 1
ρξk

zk+1 = Prox λ
ρ ∥·∥1

Dyk + 1
ρζk

xk+1 = xk −(γI + C)−1 
A⊺(ξk + ρ(Axk −b) −ρyk+1) + D(ζk + ρDxk −ρzk+1)

ξk+1 = ξk + ρ(Axk+1 −b −yk+1)
ζk+1 = ζk + ρ(Dxk+1 −zk+1),
where ξk+1 and ζk+1 are the dual variables. Then apply the Moreau identity (2.12).
8.3 Jacobi doubly linearized ADMM. Consider the problem
minimize
x∈Rp
m
X
i=1
(fi(xi) + hi(xi))
subject to
Ax = c,
where (x1, . . . , xm) = x, f1, . . . , fm are proximable CCP functions, and h1, . . . , hm are
differentiable CCP functions. Find a method analogous to Jacobi ADMM with a split x-
update utilizing the proximal operators of f1, . . . , fm. What are the stepsize requirements?
8.4 Jacobi+1. Consider the problem
minimize
x∈Rp, y∈Rq
m
X
i=1
fi(xi) + g(y)
subject to
Ax + By = c.
Find a method analogous to Jacobi ADMM that performs a split x-update and then the
y-update. What are the stepsize requirements?


## Page 216

Exercises
201
8.5 More dummy variables. Consider the problem
minimize
x∈Rp, y∈Rq
m
X
i=1
fi(xi) +
ℓ
X
j=1
gj(yj)
subject to
Ax + By = c,
where x = (x1, . . . , xm) with xi ∈Rpi for i = 1, . . . , m and y = (y1, . . . , yℓ) with yj ∈Rqj
for j = 1, . . . , ℓ. Introduce dummy variables ξ1, . . . , ξm and ζ1, . . . , ζℓto get the equivalent
problem
minimize
(x1,...,xm)∈Rp
(y1,...,yℓ)∈Rq
ξ1,...,ξm,ζ1,...,ζℓ∈Rn
m
X
i=1
fi(xi) +
ℓ
X
j=1
gj(yj)
subject to
A:,ixi = ξi
for i = 1, . . . , m
B:,jyj = ζj
for j = 1, . . . , ℓ
m
X
i=1
ξj +
ℓ
X
j=1
ζj = c.
Find an ADMM-type method with split x- and y-updates. In particular, apply FLiP-
ADMM with the x- and ζ-variables updated first, y- and ξ-variables updated second, and
the dual variables updated last. What are the stepsize requirements?
8.6 The exchange problem. Consider the problem
minimize
x1,...,xm∈Rn
m
X
i=1
fi(xi)
subject to
x1 + · · · + xm = b,
x1, . . . , xm ≥0.
Assume fi is Lf-smooth and CCP and evaluating ∇fi is efficient, for i = 1, . . . , m.
Provide an ADMM-type method to efficiently solve this problem. What are the stepsize
requirements?
Remark. The economics interpretation of this problem is as follows. There are n goods
with a total amount of b1, . . . , bn.
There are m agents exchanging these goods while
preserving the total amount. Agents cannot have a negative amount of goods. The goal
is to find the optimal exchange that minimizes the global cost of all agents.
8.7 Canonical sharing problem. Consider the problem
minimize
x1,...,xm∈Rn
f
 m
X
i=1
xi
!
+
m
X
i=1
gi(xi).
Assume f, g1, . . . , gm are proximable CCP functions. Provide an ADMM-type method to
efficiently solve this problem. What are the stepsize requirements?
Remark. The economics interpretation of this problem is as follows. There are m agents
sharing n common resources.
The common shared cost is represented by f and the
individual costs by gi. For example, f may represent the shared cost of pollution, while gi
represents the individual cost (or negative gain) incurred by performing actions producing
pollutants. The goal is to minimize the sum of the global and all individual costs.
8.8 Model parallelism vs. data parallelism. Consider the problem
minimize
x∈Rp
f(x) + g(Ax −b),
where A ∈Rn×p and b ∈Rn. Partition x ∈Rp into m non-overlapping blocks of sizes
p1, . . . , pm, and write x = (x1, . . . , xm), so xi ∈Rpi for i = 1, . . . , m. Partition z ∈Rn


## Page 217

202
8
ADMM-type methods
into ℓnon-overlapping blocks of sizes n1, . . . , nℓ, and write z = (z1, . . . , zℓ), so zj ∈Rnj for
j = 1, . . . , ℓ. Assume f(x) = f1(x1) + · · · + fm(xm), where f1, . . . , fm are CCP functions.
Assume g(z) = g1(z1) + · · · + gℓ(zℓ), where g1, . . . , gℓare CCP functions.
The problem is equivalent to
minimize
(x1,...,xm)∈Rp
z∈Rn
Pm
i=1 fi(xi) + g(z −b)
subject to
Pm
i=1 A:,ixi = z,
where
A =

A:,1
A:,2
· · ·
A:,m

,
Ax = A:,1x1 + A:,2x2 + · · · + A:,mxm.
Provide an ADMM-type method that updates the blocks x1, . . . , xm in parallel.
The
update for xi should access the data A:,i for i = 1, . . . , m. What are the stepsize require-
ments?
Now, redefine x1, . . . , xℓand y as copies of x. The problem is also equivalent to
minimize
x1,...,xℓ,y∈Rp
Pℓ
j=1 gj(Aj,:xj −bj) + f(y)
subject to
xj = y,
j = 1, . . . , ℓ,
where
A =


A1,:
A2,:
...
Aℓ,:

,
Ax =


A1,:x
A2,:x
...
Aℓ,:x

.
Provide an ADMM-type method that updates the copies x1, . . . , xℓin parallel.
The
update for xj should access the data Aj,: and bj for j = 1, . . . , ℓ. What are the stepsize
requirements?
Remark.
In the context of machine learning, we say the first type of method utilizes
model parallelism and the second type data parallelism. We view (x1, . . . , xm) = x as a
decomposition of the machine learning model represented by x into m blocks, and we view
(A1,:, b1), . . . , (Aℓ,:, bℓ) as a decomposition of the data into ℓblocks. In model parallelism,
the ith parallel process updates the ith block using all data blocks (but only the data
relevant to the ith block of the model).
In data parallelism, the jth parallel process
updates the entire model using (Aj,:, bj), the jth block of data points.
8.9 Consolidating blocks with graph coloring. Consider the multi-block ADMM formulation
minimize
x∈Rp, y∈Rq
m
X
i=1
fi(xi)
subject to
Pm
i=1 A:,ixi = c.
As discussed in §8.2.3, we can solve this problem with several ADMM-type methods
utilizing block splitting. However, such methods can be slow; empirically, using proximal
terms or introducing dummy variables slows down the iteration. On the other hand, we
know that if the blocks are orthogonal, i.e., A⊺
:,iA:,j = 0 for all i̸ = j, then the classical
ADMM has split x-updates.
Consider the graph G = (V, E) with the vertex set V = {1, . . . , m} representing the blocks.
For the edge set E, we have {i, j} ∈E if and only if i̸ = j and A⊺
:,iA:,j̸ = 0.
Assume G has a 2-coloring, i.e., we can partition V into V1 and V2 such that for any
i, j ∈Vk, {i, j} /∈E for k = 1, 2. The problem is equivalent to
minimize
x∈Rp, y∈Rq
X
i∈V1
fi(xi) +
X
i∈V2
fi(xi)
subject to
P
i∈V1 A:,ixi + P
i∈V2 A:,ixi = c.


## Page 218

Exercises
203
Provide an ADMM-type method that updates the primal blocks in V1 and V2 in an
alternating manner. What are the stepsize requirements?
Next, assume G has a χ-coloring, i.e., we partition V into V1, . . . , Vχ such that for any
i, j ∈Vk, {i, j} /∈E for k = 1, . . . , χ. The problem is equivalent to
minimize
x∈Rp, y∈Rq
χ
X
k=1
X
i∈Vk
fi(xi)
subject to
Pχ
k=1
P
i∈Vk A:,ixi = c.
Provide an ADMM-type method analogous to Jacobi ADMM that updates the primal
blocks in V1, . . . , Vχ concurrently. What are the stepsize requirements?
8.10 Quadratic subproblem with affine constraints. Assume g1 is a strongly convex quadratic
function with affine constraints, i.e.,
g1(y) = 1
2y⊺Cy + ⟨d, y⟩+ δ{y | Ey=f}(y),
where C ∈Rq×q, C ≻0, d ∈Rq, E ∈Rs×q has linearly independent rows, and f ∈Rs.
When s = 0, the affine constraints vanish. Show that the solution to the subproblem
yk+1 = argmin
y∈Rq

g1(y) + ⟨∇g2(yk) + B⊺uk, y⟩+ ρ
2∥Axk + By −c∥2 + 1
2∥y −yk∥2
Q

is given by
yk+1 = −T
ρ
2B⊺Axk + ∇g2(yk) + B⊺uk −Qyk
−h
for some symmetric positive semidefinite matrix T ∈Rq×q and h = T(d −ρ
2B⊺c) +
M −1E⊺(EM −1E⊺)−1f with M = C + Q + ρB⊺B.
8.11 Four-block ADMM with 2-1-2-4-3-4 updates. Consider the problem
minimize
x1∈Rp1 , x2∈Rp2
x3∈Rp3 , x4∈Rp4
f1(x1) + f2(x2) + f3(x3) + f4(x4)
subject to
A:,1x1 + A:,2x2 + A:,3x3 + A:,4x4 = c,
where f2 and f4 are strongly convex quadratic functions with affine constraints as in
Exercise 8.10. Find an ADMM-type method that updates the primal blocks in the order
x2 →x1 →x2 →x4 →x3 →x4, analogous to the 2-1-2 ADMM of §8.2.5. What are the
stepsize requirements?
8.12 2-1-2 ADMM with FLiP. Consider the problem
minimize
x∈Rp, y∈Rq
f1(x) + g1(y)
subject to
Ax + By = c.
Assume g is is a strongly convex quadratic functions with affine constraints as in Exer-
cise 8.10. Consider the 2-1-2 ADMM method with function linearization and proximal
terms:
yk+1/2 = argmin
y∈Rq

g1(y) + ⟨∇g2(yk) + B⊺uk, y⟩+ ρ
2∥Axk + By −c∥2 + 1
2∥y −yk∥2
Q

xk+1 ∈argmin
x∈Rp

f1(x) + ⟨∇f2(xk) + A⊺uk, x⟩+ ρ
2∥Ax + Byk+1/2 −c∥2 + 1
2∥x −xk∥2
P

yk+1 = argmin
y∈Rq

g1(y) + ⟨∇g2(yk) + B⊺uk, y⟩+ ρ
2∥Axk+1 + By −c∥2 + 1
2∥y −yk∥2
Q

uk+1 = uk + ϕρ(Axk+1 + Byk+1 −c).


## Page 219

204
8
ADMM-type methods
To clarify, the function linearization and the proximal terms of the y-updates are centered
at yk for both the yk+1/2- and yk+1-updates.
Show that this method reduces to an
instance of FLiP-ADMM, analogous to the 2-1-2 ADMM of §8.2.5. What are the stepsize
requirements?
8.13 Alternate proof of Theorem 6. In this exercise, we perform an alternate analysis for Stages
2 and 3 of the proof of Theorem 6 to obtain a different stepsize requirement. Bound the
last term of (8.7) with
1
ϕ⟨uk+1 −uk, B(yk+1 −yk)⟩≤
η
2ϕ2ρ∥uk+1 −uk∥2 + 1
2∥yk+1 −yk∥2ρ
η B⊺B
to get
∥wk+1 −w⋆∥M0 ≤∥wk −w⋆∥M0 −∥wk+1 −wk∥M3 −

L(xk+1, yk+1, u⋆) −L(x⋆, y⋆, u⋆)

,
where
M3 = 1
2


P −LfI
0
0
0
ρ

1 −1
η

B⊺B + Q −LgI
0
0
0
2−ϕ−η
ϕ2ρ I

.
Show that FLiP-ADMM converges if
P ⪰LfI,
Q ⪰0,
and there exist ε ∈(0, 2 −ϕ) such that
ρ

1 −
1
2 −ϕ −ε

B⊺B + Q ⪰LgI.
Remark. This new condition is useful when Lg is large, as it does not have a factor 3.
8.14 Refinement of Theorem 6. Unify the proof of Theorem 6 and the analysis of Exercise 8.13.
For α ∈[0, 1], define
V k
α = ∥wk −w⋆∥2
M0 + α∥wk −wk−1∥2
M1.
Show the key inequality
V k+1
α
≤V k
α −∥wk+1 −wk∥2
αM2+(1−α)M3 −

L(xk+1, yk+1, u⋆) −L(x⋆, y⋆, u⋆)

,
where M3 is as defined in Exercise 8.13. Show that FLiP-ADMM converges if
P ⪰LfI,
Q ⪰0,
and there exist α ∈[0, 1] and ε ∈(0, 2 −ϕ) such that
ρ

1 −α(1 −ϕ)2 + 1 −α
2 −ϕ −ε

B⊺B + Q ⪰(2α + 1)LgI.
Remark. When ϕ = 1, the choice α = ε leads to the (sufficient) condition Q ≻LgI.


## Page 220

Chapter 9
Duality in splitting methods
In this chapter, we present Attouch–Théra duality, a duality framework for mono-
tone inclusion problems that is analogous to, but simpler than convex duality. Con-
vex duality has several distinct and complementary interpretations, and Attouch–
Théra duality takes one and generalizes it to operators.
We discuss the intimate connection of Attouch–Théra duality with the base
splitting methods of §2.7.1. This was a theoretical detail omitted in §2.7.2, and
the duality provides a more complete understanding. Furthermore, Attouch–Théra
duality has algorithmic utility, as dual solutions certify correctness of primal solu-
tions.
9.1
Fenchel duality
In Fenchel duality, the primal problem is
minimize
x∈Rn
f(x) + g(x),
(F-P)
where f and g are CCP functions, and the dual problem is
maximize
u∈Rn
−f ∗(−u) −g∗(u).
(F-D)
These primal-dual problem pairs are generated by the Lagrangian
L(x, u) = f(x) + ⟨x, u⟩−g∗(u).
As we discussed in §1.3.9, the question of when total duality holds in Fenchel
duality (and more generally in convex duality) is subtle.
We now discuss an interpretation of Fenchel duality that we later extend to
operators.
For simplicity, assume total duality holds and f, g, f ∗, and g∗are
differentiable. Under the assumptions, the primal problem is equivalent to
find
x∈Rn
0 = ∇f(x) + ∇g(x),


## Page 221

206
9
Duality in splitting methods
which we interpret as the problem of finding a point x such that the gradients of
f and g at x sum to 0. Remember from §2.1 that ∇f ∗= (∇f)−1. Under the
assumptions, the dual problem is equivalent to
find
u∈Rn
(∇f)−1(−u) = (∇g)−1(u),
which we interpret as the problem of finding the gradient u such that the point at
which ∇f produces −u and the point at which ∇g produces u agree. When f, g, f ∗,
and g∗are not differentiable, one can make a similar argument with subgradients.
This is one of the many viewpoints of convex duality; the primal viewpoint is
to find the variable x, while the dual viewpoint is to find the subgradient u.
9.2
Attouch–Théra duality
Consider the monotone inclusion problem
find
x∈Rn
0 ∈(픸+ 픹)x,
where 픸and 픹are maximal monotone. Define 픸−> = (−핀)픸−1(−핀), i.e., 픸−>(u) =
−픸−1(−u). The Attouch–Théra dual monotone inclusion problem is
find
u∈Rn
0 ∈(픸−> + 픹−1)u.
Attouch–Théra duality is, in a sense, easier than Fenchel duality since
Zer (픸+ 픹)̸ = ∅
⇔
Zer (픸−> + 픹−1)̸ = ∅.
This follows from
∃x [0 ∈(픸+ 픹)x]
⇔
∃x, u [−u ∈픸x, u ∈픹x]
⇔
∃x, u

−x ∈픸−>u, x ∈픹−1u

⇔
∃u

0 ∈(픸−> + 픹−1)u

.
In other words, a primal solution exists if and only if a dual solution exists. There
is no notion of strong duality, as there are no function values.
In a certain sense, Attouch–Théra duality generalizes Fenchel duality, as mono-
tone operators generalize subdifferential operators of convex functions. In a differ-
ent sense, Attouch–Théra duality does not generalize Fenchel duality, as Attouch–
Théra duality fails to capture and provide insight into the subtleties and difficulties
of convex duality. In Fenchel duality, strong duality may fail, a primal solution
may exist while a dual solution does not, or vice versa. There is no analog of such
pathologies in Attouch–Théra duality.


## Page 222

9.3
Duality in splitting methods
207
Dual solutions as certificates
When solving a monotone inclusion problem with multi-valued operators, a dual
solution certifies correctness of a primal solution.
Therefore, it is desirable for
a splitting method to produce solutions of both the primal and dual monotone
inclusion problems. Given (x⋆, u⋆), one can verify it is indeed a primal-dual solution
pair by checking −u⋆∈픸x⋆and u⋆∈픹x⋆. If only a primal solution is provided,
we must verify that 0 ∈픸x⋆+ 픹x⋆. This can be difficult if there is no effective
way to compute the Minkowski sum 픸x⋆+ 픹x⋆. (On a computer, how would we
represent the sets 픸x⋆and 픹x⋆and how would we compute the Minkowski sum?)
In practice, a method used to verify “correctness” of a primal-dual solution
must be able to deal with inaccuracies, since an output of an iterative algorithm
will be at most approximately correct. This issue relates how to design an effective
termination criterion for the iterative methods. We avoid this discussion for the
sake of simplicity.
9.3
Duality in splitting methods
We now present the intimate connection of the base splittings of §2.7.1 with
Attouch–Théra duality. We also show that the splittings are primal-dual in the
sense that they provide dual information.
9.3.1
FBS
The FPI with FBS
xk+1/2 = xk −α픸xk
xk+1 = 핁α픹xk+1/2
is often not considered a primal-dual method as there is no explicit reference to the
dual problem or a dual variable. However, we can make the method primal-dual
by writing
xk+1/2 = xk −α픸xk
uk+1/2 = −픸xk
xk+1 = 핁α픹xk+1/2
uk+1 = α−1(xk+1/2 −xk+1).
Note that uk+1 ∈픹xk+1. It is straightforward to verify that if xk →x⋆, then
uk+1/2 →u⋆,
uk+1 →u⋆,
u⋆∈Zer (픸−> + 픹−1).


## Page 223

208
9
Duality in splitting methods
9.3.2
DRS
Characterization of fixed points
Using the Attouch–Théra dual, we can now characterize the fixed points of the
PRS and DRS operators more concretely:
Fix (ℝα픸ℝα픹) ⊆Zer (픸+ 픹) + αZer (픸−> + 픹−1).
This follows from
z = ℝα픸ℝα픹z
⇔
z + 2핁α픸(2핁α픹−핀)z −2핁α픹z = z, x = 핁α픹z
⇔
핁α픸(x −αu) = x, z = x + αu, u ∈픹x
⇔
x −αu = x + αv, v ∈픸x, z = x + αu, u ∈픹x
⇔
v = −u, v ∈픸x, u ∈픹x, z = x + αu
⇔
−u ∈픸x, u ∈픹x, z = x + αu
⇔
−u ∈픸x, u ∈픹x, −x ∈픸−>u, x ∈픹−1u, z = x + αu
⇒
0 ∈(픸+ 픹)x, 0 ∈(픸−> + 픹−1)u, z = x + αu.
Because the last step is not an equivalence, the characterization is an inclusion,
not equality. See the notes and references section for further discussion.
DRS in primal-dual form
We can make the FPI with DRS more explicitly primal-dual by writing
xk+1/2 = 핁α픹(zk)
uk+1/2 = 1
α(zk −xk+1/2)
xk+1 = 핁α픸(2xk+1/2 −zk)
uk+1 = 1
α(xk+1 −xk+1/2 + αuk+1/2)
zk+1 = zk + xk+1 −xk+1/2.
Note that uk+1/2 ∈픹xk+1/2 and −uk+1 ∈픸xk+1. It is straightforward to verify
that if Zer (픸+ 픹)̸ = ∅, then
xk+1/2 →x⋆,
xk+1 →x⋆,
x⋆∈Zer (픸+ 픹)
uk+1/2 →u⋆,
uk+1 →u⋆,
u⋆∈Zer (픸−> + 픹−1)
zk →x⋆+ αu⋆.
Self-dual property of DRS
Interestingly, PRS and DRS are self-dual in the following sense:
ℝ픸ℝ픹= ℝ픸−>ℝ픹−1.


## Page 224

9.3
Duality in splitting methods
209
This follows from using 핁픸−> = 핀+ 핁픸(−핀) (see Exercise 9.1) and the inverse
resolvent identity 핁픹−1 = 핀−핁픹:
(2핁픸−> −핀)(2핁픹−1 −핀) = (2핁픸(−핀) + 핀)(핀−2핁픹)
= (2핁픸(−핀) + 핀)(−핀)(2핁픹−핀)
= (2핁픸−핀)(2핁픹−핀).
In fact, when α = 1, we can write the FPI with DRS as
xk+1/2 = 핁픹(zk)
uk+1/2 = 핁픹−1(zk) = zk −xk+1/2
xk+1 = 핁픸(2xk+1/2 −zk)
uk+1 = 핁픸−>(2uk+1/2 −zk) = xk+1 −xk+1/2 + uk+1/2
zk+1 = zk + xk+1 −xk+1/2 = zk + uk+1 −uk+1/2.
This form of the iteration nicely reveals the symmetry. (Algorithmically there is
no need to use both the x- and u-variables.) When α̸ = 1, we have a similar, but
slightly less elegant self-dual relationship.
As an aside, this self-dual property explains why the infimal postcomposition
technique of §3.1 and the dualization technique of §3.2 yield the same method
ADMM.
9.3.3
DYS
For the monotone inclusion problem
find
x∈Rn
0 ∈(픸+ 픹+ ℂ)x,
where 픸, 픹, and ℂare maximal monotone and ℂis single-valued, we consider the
Attouch–Théra dual
find
u∈Rn
0 ∈((픸+ ℂ)−> + 픹−1)u.
Consider the DYS operator
핀−핁α픹+ 핁α픸(ℝα픹−αℂ핁α픹).
With similar steps as before, we can characterize the fixed points with
Fix (핀−핁α픹+ 핁α픸(ℝα픹−αℂ핁α픹)) ⊆Zer (픸+ 픹+ ℂ) + αZer ((픸+ ℂ)−> + 픹−1).
We can make the FPI with DYS more explicitly primal-dual by writing
xk+1/2 = 핁α픹(zk)
uk+1/2 = 1
α(zk −xk+1/2)
xk+1 = 핁αA(2xk+1/2 −zk −αℂxk+1/2)
uk+1 = 1
α(xk+1 −xk+1/2 + αuk+1/2)
zk+1 = zk + xk+1 −xk+1/2.


## Page 225

210
9
Duality in splitting methods
Note that uk+1/2 ∈픹xk+1/2 and −uk+1 ∈픸xk+1 + ℂxk+1/2. It is straightforward
to verify that if zk →z⋆, then
xk+1/2 →x⋆,
xk+1 →x⋆,
x⋆∈Zer (픸+ 픹+ ℂ)
uk+1/2 →u⋆,
uk+1 →u⋆,
u⋆∈Zer ((픸+ ℂ)−> + 픹−1)
zk →x⋆+ αu⋆.
Finally, we note that DYS is not self-dual, as it uses an evaluation of ℂ, a primal
operation.


## Page 226

Bibliographical Notes
211
Bibliographical Notes
Fenchel duality was formalized by Fenchel in 1949 [Fen49].
Although Attouch–Théra
duality is named after Attouch and Théra’s 1996 paper [AT96], it was first formalized
by Mercier in 1980 [Mer80, p. 40]. The self-dual property of DRS was first presented by
Eckstein in 1989 [Eck89, Lemma 3.6 p. 133] and was further investigated in [BBHM12,
YY16, BLM17, BM17].
In general, Fix (ℝα픸ℝα픹)̸ = Zer (픸+ 픹) + αZer (픸−> + 픹−1). See Exercise 9.4 for a
counterexample and see Exercise 9.6 for a complete characterization, Fix (ℝα픸ℝα픹).
A monotone operator is said to be paramonotone if
u ∈픸x, v ∈픸y, ⟨u −v, x −y⟩= 0
⇒
v ∈픸x, u ∈픸y.
Bruck first presented the notion without naming the property [Bru75b]. Censor, Iusem,
and Zenios named the property paramonotonicity [CIZ98].
Bauschke, Boţ, Hare, and
Moursi [BBHM12] showed that if 픸and 픹are paramonotone, then we can characterize
the fixed points of PRS and DRS with equality:
Fix (ℝαAℝαB) = Zer (픸+ 픹) + αZer (픸−> + 픹−1).
(Subdifferential operators of CCP functions are paramonotone. Cf. Exercise 9.5.)


## Page 227

212
9
Duality in splitting methods
Exercises
9.1 Variation of the inverse resolvent identity. Prove 핁픸−> −핁픸(−핀) = 핀.
9.2 Show that the the fixed points of the DYS operator satisfy
Fix (핀−핁α픹+ 핁α픸(ℝα픹−αℂ핁α픹)) ⊆Zer (픸+ 픹+ ℂ) + αZer ((픸+ ℂ)−> + 픹−1).
9.3 Let
f(x) =
 −√x
for x ≥0
∞
otherwise,
g(x) = δ{0}(x),
where x ∈R. Show that while the primal problem
minimize
x∈R
f(x) + g(x)
has a solution, its Fenchel dual
maximize
u∈R
−f ∗(−u) −g∗(u)
does not. Also show that argmin(f + g)̸ = Zer (∂f + ∂g).
9.4 Consider the operators
픸= ℕR2
+,
픹=
0
−1
1
0

,
where R2
+ = {(x1, x2) ∈R2 | x1 ≥0, x2 ≥0}. Show
(a) Zer (픸+ 픹) = {(x1, 0) ∈R2 | x1 ≥0}
(b) Zer (픸−> + 픹−1) = {(0, u2) ∈R2 | u2 ≥0}
(c) Fix (ℝ픸ℝ픹) = {(z, z) ∈R2 | z ≥0}
and conclude that
Fix (ℝ픸ℝ픹)̸ = Zer (픸+ 픹) + Zer (픸−> + 픹−1).
Hint. Use
픹−1 = −픹,
핁픹= 1
2
 1
1
−1
1

,
ℝ픹= −픹
and
ℕR2
+(x) =
 {y ∈R2 | y1 ≤0, y2 ≤0, ⟨x, y⟩= 0}
if x ∈R2
+
∅
if x /∈R2
+.
Remark. This counterexample is due to Bauschke, Boţ, Hare, and Moursi [BBHM12].
9.5 Fixed points of DRS with Fenchel duality. Consider the Fenchel dual setup with primal
and dual problems
minimize
x∈Rn
f(x) + g(x),
maximize
u∈Rn
−f ∗(−u) −g∗(u),
where f and g are CCP functions on Rn, generated by
L(x, u) = f(x) + ⟨x, u⟩−g∗(u).
Assume total duality holds. Write X⋆and U ⋆for the sets of primal and dual solutions.
Show that
Fix (ℝα∂fℝα∂g) = X⋆+ αU ⋆.
Hint. Note that [x⋆∈X⋆and u⋆∈U ⋆] if and only if [(x⋆, u⋆) is a saddle point of L].


## Page 228

Exercises
213
9.6 Fixed points of DRS via primal-dual inclusion. Consider the Attouch–Théra dual setup
with primal and dual problems
find
x∈Rn
0 ∈(픸+ 픹)x,
find
u∈Rn
0 ∈(픸−> + 픹−1)u,
where 픸and 픹are maximal monotone operators on Rn. Write X⋆and U ⋆for the sets
of primal and dual solutions. Consider the primal-dual inclusion problem
find
x,u∈Rn
0 ∈
 픸
핀
−핀
픹−1
 x
u

=

픸x + u
−x + 픹−1u

and write Φ⋆⊆Rn × Rn for its solution set. Show
(a)

I
0

Φ⋆= X⋆,
(b)

0
I

Φ⋆= U ⋆, and
(c)

I
I

Φ⋆= Fix (ℝ픸ℝ픹),
where 0, I ∈Rn×n are the zero and identity matrices.
Clarification. For any A, B ∈Rn×n,

A
B

Φ⋆= {픸x⋆+ Bu⋆| (x⋆, u⋆) ∈Φ⋆}.
Hint. For (a), use the equivalences
0 ∈픸x⋆+ 픹x⋆
⇔
∃u⋆such that 0 ∈픸x⋆+ u⋆, u⋆∈픹x⋆
⇔
∃u⋆such that 0 ∈픸x⋆+ u⋆, 0 ∈−x⋆+ 픹−1u⋆.
Remark. This result was first established by Bauschke, Boţ, Hare, and Moursi [BBHM12,
Theorem 4.5]. The set Φ⋆is also referred to as the “extended solution set” and was first
studied by Eckstein and Svaiter [ES08].


## Page 229

214
9
Duality in splitting methods


## Page 230

Chapter 10
Maximality and monotone
operator theory
In this chapter, we digress and study monotone operator theory. Convex optimiza-
tion theory, the main subject of study in this book, focuses on the derivation and
analysis of convex optimization algorithms. In contrast, monotone operator theory
views monotone operators as interesting objects in their own right and focuses on
understanding them better.
One goal of this chapter is to provide theoretical completeness; we prove several
results that were simply asserted in §2. Another goal is to provide a gentle exposure
to the field of monotone operator theory. Readers who find this subject interesting
can continue their study through standard references such as [Phe93, Sho97, FP03,
BL06, BV10, Boţ10, BC17a].
Often, results in monotone operator theory are established in infinite-dimensional
Banach or Hilbert spaces, where a new set of interesting challenges arise. Here, we
limit our attention to finite-dimensional Euclidean spaces.
10.1
Maximality of subdifferential
We say ¯픸: Rn ⇒Rn is an extension of 픸: Rn ⇒Rn if Gra ¯픸⊇Gra 픸. We say ¯픸
is a proper extension of 픸if the containment Gra ¯픸⊃Gra 픸is strict.
Recall that a monotone operator is maximal if it has no proper monotone ex-
tension. As we have discussed in §2, and as we will soon prove, if 픸: Rn ⇒Rn is
maximal monotone, then dom 핁픸= Rn, which implies fixed-point iterations using
핁픸are well defined.
Theorem 7 If f : Rn →Rn ∪{∞} is CCP, then ∂f is maximal monotone.
Proof. We know ∂f is monotone.
Assume for contradiction that there exists a


## Page 231

216
10
Maximality and monotone operator theory
(˜x, ˜g) /∈∂f such that {(˜x, ˜g)} ∪∂f is monotone. Define (x, g) ∈∂f with
x = argmin
z

f(z) + 1
2∥z −(˜x + ˜g)∥2

= Proxf(˜x + ˜g),
0 = x −˜x + g −˜g.
We get g ∈∂f(x) from the 0 ∈x −˜x + ∂f(x) −˜g, the optimality condition of the
argmin. Since we assumed (˜x, ˜g) /∈∂f, either x̸ = ˜x or g̸ = ˜g (or both). Using
x −˜x = −g + ˜g, we have
⟨g −˜g, x −˜x⟩= −∥x −˜x∥2
2 = −∥g −˜g∥2
2 < 0,
which contradicts the assumption that {(˜x, ˜g)} ∪∂f is monotone.
The key idea of proof is that given v ∈Rn,
v 7→(Proxf(v)
|
{z
}
=x
, v −Proxf(v)
|
{z
}
=g
) ∈∂f
provides a unique decomposition v = x + g such that (x, g) ∈∂f.
10.2
Fitzpatrick function
For 픸: Rn ⇒Rn, define the Fitzpatrick function F픸: Rn × Rn →R ∪{∞} as
F픸(x, u) = ⟨x, u⟩−
inf
(y,v)∈픸⟨x −y, u −v⟩=
sup
(y,v)∈픸
{⟨y, u⟩+ ⟨x, v⟩−⟨y, v⟩} ,
which is useful when 픸is maximal monotone. The equivalent definition with sup
follows from expanding the inner product within the inf.
Lemma 3 Assume 픸: Rn ⇒Rn is maximal monotone. Then
• F픸is CCP,
• F픸(x, u) ≥⟨x, u⟩for all x, u ∈Rn, and
• F픸(x, u) = ⟨x, u⟩if and only if (x, u) ∈픸.
We say F픸is a representative function of 픸, since F픸is a convex extension
of ⟨x, u⟩from Gra 픸to Rn × Rn that furthermore satisfies F픸(x, u) ≥⟨x, u⟩.
The Fitzpatrick function is one of the several representative functions used in the
monotone operator theory literature.
A common technique in monotone operator theory is to analyze a representative
function to conclude results about the original operator. In our case specifically,
analyzing F픸, a CCP function, is easier than directly analyzing 픸, since we can
rely on results from convex analysis.


## Page 232

10.2
Fitzpatrick function
217
Proof. If (x, u) ∈픸, then ⟨x −y, u −v⟩≥0 for all (y, v) ∈픸by monotonicity, and
the infimum
inf
(y,v)∈픸⟨x −y, u −v⟩= 0
is attained at (x, u). So F픸(x, u) = ⟨x, u⟩.
Assume (x, u) /∈픸. Then by maximality there exists a (y, v) ∈픸such that
⟨x −y, u −v⟩< 0. Therefore
inf
(y,v)∈픸⟨x −y, u −v⟩< 0
and F픸(x, u) > ⟨x, u⟩.
Define
fy,v(x, u) = ⟨y, u⟩+ ⟨x, v⟩−⟨y, v⟩,
which is a closed convex function for all (y, v) ∈픸. Then
epi F픸=
\
(y,v)∈픸
epi fy,v
is a closed convex set as it is an intersection of closed convex sets.
Since F픸(x, u) ≥fy,v(x, u) > −∞for any (y, v) ∈픸, we have F픸> −∞
always. On the other hand,
F픸(x, u) = ⟨x, u⟩< ∞
for any (x, u) ∈픸. So F픸is proper.
Theorem 8, the Minty surjectivity theorem, is foundational to operator splitting
methods as it ensures that methods using resolvents are well defined. We say the
operator 핀+ 픸is surjective if range (핀+ 픸) = Rn, i.e., for any u ∈Rn there is an
x ∈Rn such that u ∈(핀+ 픸)x. If 핀+ 픸is surjective, then dom 핁픸= Rn.
Theorem 8(Minty surjectivity theorem) If 픸: Rn ⇒Rn is maximal monotone, then
range (핀+ 픸) = Rn.
Proof. We want to show that u ∈range (핀+ 픸) for any u ∈Rn and maximal
monotone 픸.
To do so, we first establish 0 ∈range (핀+ 픸) for any maximal
monotone 픸. Then the maximal monotone operator 픹(x) = 픸(x) −u satisfies
0 ∈range (핀+ 픹), which implies u ∈range (핀+ 픸) for any u ∈Rd.
We now complete the proof by showing 0 ∈range (핀+ 픸).
Define (y, v) ∈
Rn × Rn with
(y, v) =
argmin
(x,u)∈Rn×Rn

F픸(x, u) + 1
2∥x∥2 + 1
2∥u∥2

= ProxF픸(0, 0).
This implies

−y
−v

∈∂F픸(y, v).


## Page 233

218
10
Maximality and monotone operator theory
Since F픸is convex, the subgradient inequality tells us

−y
−v

,

x
u

−

y
v

≤F픸(x, u) −F픸(y, v)
∀(x, u) ∈Rn × Rn.
By Lemma 3,
F픸(x, u) −F픸(y, v) ≤⟨x, u⟩−⟨y, v⟩
∀(x, u) ∈픸.
Combining the two inequalities and reorganize to get
∥y + v∥2 ≤⟨x + v, u + y⟩
∀(x, u) ∈픸.
(10.1)
Since 0 ≤∥y + v∥2 and since 픸is maximal monotone, this implies (−v, −y) ∈픸.
By letting (x, u) = (−v, −y) in (10.1), we get v = −y. Thus (y, −y) ∈픸and we
have
0 ∈(픸+ 핀)(y).
The converse of Theorem 8 is true. As a consequence, we can show a monotone
operator 픸: Rn ⇒Rn is maximal if dom 핁픸= Rn.
Theorem 9 If 픸: Rn ⇒Rn is monotone and range (J + 픸) = Rn for a symmetric
positive definite J ∈Rn×n, then 픸is maximal monotone.
Proof. First consider the case J = 핀. Assume {(x, u)} ∪픸is monotone, i.e.,
0 ≤⟨x −z, u −w⟩
∀(z, w) ∈픸.
To establish maximality, it is enough to show (x, u) ∈픸. Since range (핀+픸) = Rn,
there is a y such that x + u ∈(핀+ 픸)y. Let
v = x + u −y ∈픸y.
Then
0 ≤⟨x −y, u −v⟩= −∥x −y∥2 = −∥u −v∥2.
So x = y and u = v, which implies (x, u) ∈픸.
When J̸ = 핀. Then J−1/2픸J−1/2 is monotone and, because J +픸is surjective,
range (핀+ J−1/2픸J−1/2) = Rn.
This implies J−1/2픸J−1/2 is maximal and so is 픸.
Theorem 10 Let 픸: Rn ⇒Rn be maximal monotone and f : Rn →R ∪{∞} be
CCP. If 0 ∈int (dom 픸−dom f), then 픸+ ∂f is maximal monotone.


## Page 234

10.2
Fitzpatrick function
219
Theorem 10 is useful, because Theorems 11 and 12 easily follow from it. The proof
of Theorem 10 is similar to the proof of Theorem 8 but somewhat more complicated.
See Exercise 10.9.
Theorem 11 Let 픸: Rn ⇒Rn and 픹: Rn ⇒Rn be maximal monotone. If dom 픸∩
int dom 픹̸ = ∅, then 픸+ 픹is maximal monotone.
Proof. Define
C = {(x, x) | x ∈Rn}.
Then
ℕC(x, x) = {(v, −v) | v ∈Rn}
for any x ∈Rn. (Remember that ℕC is the normal cone operator and ℕC = ∂δC,
where δC is the indicator function.)
Consider the operator 픽: Rd × Rd ⇒Rd × Rd defined as
픽(x, y) =
x
y

+
픸(x)
픹(y)

| {z }
=피(x,y)
+ℕC(x, y).
Pick any x0 ∈dom A ∩int dom B.
Then there is an ε > 0 such that for any
δ1, δ2 ∈Rn satisfying ∥δ1∥< ε and ∥δ2∥< ε, we have x0 + δ1 −δ2 ∈dom B. Then
(x0 −y, x0 + δ1 −δ2 −y) ∈dom 피−dom ℕC
for any ∥δ1∥< ε, ∥δ2∥< ε, and y ∈Rn. We let y = x0 −δ2 to get
(δ2, δ1) ∈dom 피−dom ℕC
for any ∥δ1∥< ε and ∥δ2∥< ε. So 0 ∈int (dom 피−dom ℕC), and Theorems 10
and 8 tell us range (픽) = Rn × Rn.
For any u ∈Rn, there is an x ∈Rn such that
u
0

∈
(픸+ 핀)x
(픹+ 핀)x

+
 v
−v

,
 v
−v

∈ℕC(x).
Left-multiplying by
핀
핀
gives us
u ∈(픸+ 픹+ 2핀)x.
So range (픸+ 픹+ 2핀) = Rn, and 픸+ 픹is maximal by Theorem 9.
Theorem 12 Let 픸: Rn ⇒Rn be maximal monotone and M ∈Rn×m.
If
int dom 픸∩R(M)̸ = ∅. then M ⊺픸M : Rm ⇒Rm is maximal monotone.
The proof is similar to the proof of Theorem 11. See Exercise 10.8.


## Page 235

220
10
Maximality and monotone operator theory
10.3
Maximality and extension theorems
Let P be a property of an operator such as monotonicity, θ-averagedness, or L-
Lipschitz continuity. We say an operator 픸: Rn ⇒Rn is “maximal P” if there
is no proper extension ¯픸with property P. To clarify, if 픸is already maximal
P, its maximal P “extension” ¯픸is not proper, i.e., 픸= ¯픸. In this section, we
characterize maximal extensions of certain operator classes.
Whether a given operator can be extended while preserving certain properties is
a classical question in analysis. Examples of classical extension results include the
Hahn–Banach theorem, which states that a linear operator on a subspace V ⊆Rn
has an extension to all of Rn with the same norm, and the Kirszbraun–Valentine
theorem, which states that an L-Lipschitz operator on a subset S ⊆Rn has an
L-Lipschitz extension to all of Rn.
Theorem 13 A monotone operator has a maximal monotone extension.
Proof. Let 픸: Rn ⇒Rn be monotone and let
P = {픹: Rn ⇒Rn | 픹is monotone and Gra 픸⊆Gra 픹},
which is nonempty. We impose the partial order on P with 픹1 ⪯픹2 if and only
if Gra 픹1 ⊆Gra 픹2 for all 픹1, 픹2 ∈P. Every chain C in P has the upper bound
¯픹∈P given by
Gra ¯픹=
[
픹∈C
Gra 픹.
By Zorn’s lemma, there is a maximal element ¯픸in P. This element ¯픸extends 픸
by the definition of P and cannot be properly extended as it is maximal in P.
Theorem 14 For µ > 0, a µ-strongly monotone operator has a maximal µ-strongly
monotone extension. Furthermore, if 픸: Rn ⇒Rn is µ-strongly monotone, then
픸is maximal µ-strongly monotone if and only if range (픸) = Rn.
Proof. Since µ-strong monotonicity of 픸is defined as
⟨픸x −픸y, x −y⟩≥µ∥x −y∥2
∀x, y ∈Rn,
픸is µ-strongly monotone if and only if 픹= 픸−µ핀is monotone.
Extending 픸and 픹are equivalent in the following sense. If ¯픸is a µ-strongly
monotone extension of 픸, then ¯픸−µ핀is a monotone extension of 픹. If ¯픹is a
monotone extension of 픹, then ¯픹+ µ핀is a µ-strongly monotone extension of 픸.
By Theorem 13, 픹has a maximal monotone extension ¯픹, and 픸has a maximal
µ-strongly monotone extension ¯픹+ µ핀.
Moreover, 픸is maximal µ-strongly monotone if and only if 픹is maximal mono-
tone. By Theorems 8 and 9, 픹is maximal monotone if and only if range (픸) =
range (픹+µ핀) = Rn. Finally, chaining the equivalences provides the second stated
result.


## Page 236

10.3
Maximality and extension theorems
221
Theorem 15 For β > 0, a β-cocoercive operator has a maximal β-cocoercive exten-
sion. Furthermore, if 픸: Rn ⇒Rn is β-cocoercive, then 픸is maximal β-cocoercive
if and only if dom 픸= Rn.
Proof. Note 픸is β-cocoercive if and only if 픸−1 is β-strongly monotone.
Extending 픸and 픸−1 are equivalent in the following sense.
If ¯픸is a β-
cocoercive extension of 픸, then ¯픸−1 is a β-strongly monotone extension of 픸−1. If
픸−1 is a β-strongly monotone extension of 픸−1, then (픸−1)−1 is a β-cocoercive ex-
tension of 픸. By Theorem 14, 픸−1 has a maximal β-strongly monotone extension
픸−1, and 픸has a maximal β-cocoercive extension (픸−1)−1.
Moreover, 픸is maximal β-cocoercive if and only if 픸−1 is maximal β-strongly
monotone. By Theorem 14, 픸−1 is maximal β-strongly monotone if and only if
range (픸−1) = Rn, which holds if and only if dom (픸) = Rn. Finally, chaining the
equivalences provides the second stated result.
Remember that a β-cocoercive operators must be single-valued.
By Theo-
rem 15, [픸: Rn ⇒Rn is maximal β-cocoercive] is equivalent to [픸: Rn →Rn
is β-cocoercive] since 픸: Rn →Rn implies dom 픸= Rn. For the sake of concise-
ness, we usually avoid the former expression.
Theorem 16 For L > 0, an L-Lipschitz operator has a maximal L-Lipschitz exten-
sion. Furthermore, if 픸: Rn ⇒Rn is L-Lipschitz, then 픸is maximal L-Lipschitz
if and only if dom 픸= Rn.
This result is known as the Kirszbraun–Valentine theorem. We defer the proof to
Exercise 10.10.


## Page 237

222
10
Maximality and monotone operator theory
Bibliographical Notes
Minty’s original proof of the surjectivity theorem [Min62] relied on the Kirszbraun–
Valentine theorem [Kir34, Val43, Val45] rather than the Fitzpatrick function.
We in-
stead prove the Minty surjectivity theorem with the Fitzpatrick function and obtain the
Kirszbraun–Valentine theorem as a consequence in Exercise 10.10.
Rockafellar first proved the sum of two maximal monotone operators is maximal under
regularity conditions, but the proof was quite complicated [Roc70c]. The presented proof
outlined in Exercise 10.9 is due to Simons, Zălinescu, and Borwein [SZ04, Zăl05, SZ05,
Bor06]. Maximality of M ⊺AM under the regularity condition stated in Theorem 12 was
first established by Robinson [Rob99].
The idea of representing maximal monotone operators with convex functions was first
explored by Krauss [Kra85]. Fitzpatrick soon provided a different construction, which
we now call the Fitzpatrick function [Fit88]. The usefulness of Fitzpatrick’s construction,
however, was discovered much later by Penot, Simons, and Zălinescu [Pen03, Pen04, SZ04,
Zăl05, SZ05].
There is a large body of work in monotone operator theory studying extension theorems
beyond the Hahn–Banach theorem or the Kirszbraun–Valentine theorem. The specific
extension theorems of §10.3 were presented by Ryu, Taylor, Bergeling, and Giselsson
[RTBG20], but the core ideas are present in prior work of Bauschke and Wang [BW10]
and Minty [Min62].
One may wonder whether F∂f with CCP f has a simple form. Bauschke, McLaren, and
Sendov characterizes F∂f in some special cases including
F∂∥·∥(x, u) =
 ∥x∥
if ∥u∥≤1
∞
otherwise.
F∂(1/2)∥·∥2(x, u) = 1
4∥x + u∥2
F∂δC(x, u) = δC(x) + δ∗
C(u),
where C is a nonempty closed convex set, but F∂f seems to be a complicated object in
general [BMS06].


## Page 238

Exercises
223
Exercises
10.1 Basic exercises on maximality. Let 픸: Rn ⇒Rn be maximal monotone. Show:
(a) 픸−1 is maximal monotone,
(b) M ⊺픸M is maximal monotone when M ∈Rn×n be invertible,
(c) [⟨u −v, x −y⟩≥0 for all (x, u) ∈픸] if and only if [(y, v) ∈픸],
(d) inf(x,u)∈픸⟨u, x −y⟩≤0 for all y ∈Rn, and inf(x,u)∈픸⟨u, x −y⟩= 0 if and only if
y ∈Zer 픸.
Remark. We already know that M ⊺핋M is maximal when R(M) ∩int dom 핋̸ = ∅, and
this immediately implies (b). However, provide a direct proof for (b) that does not rely
on this result. This problem does not require any of the new tools from this chapter.
10.2 Nonexpansiveness and monotonicity. Show that if 핋is maximal nonexpansive (i.e., non-
expansive and dom 핋= Rn per Theorem 16) then 픸=
  1
2핋+ 1
2핀
−1 −핀is maximal
monotone.
Remark. Conversely, if 픸is a maximal monotone operator, then 2핁픸−핀is maximal nonex-
pansive. Therefore, the transformation 픸7→2핁픸−핀and its inverse 핋7→
  1
2핋+ 1
2핀
−1 −핀
provide a one-to-one correspondence between maximal monotone operators and maximal
nonexpansive operators.
10.3 Closed graph theorem for maximal monotone operators. Let 픸: Rn ⇒Rn be maximal
monotone. Show 픸is upper hemicontinuituous, i.e., show that if xk →x∞, uk →u∞, and
uk ∈픸xk, then u∞∈픸x∞. (Upper hemicontinuity of 픸is equivalent to Gra 픸⊂Rn×Rn
being a closed set.)
Hint. The proof can be done in one line using F픸(x∞, u∞) ≤lim infk→∞F픸(xk, uk) and
Lemma 3.
10.4 Method of multipliers primal solution convergence without strict convexity. Consider the
method of multipliers under the stated conditions. Show that any accumulation point of
x0, x1, . . . is a primal solution.
Hint. Use Exercise 10.3 and note Exercise 2.18.
Remark. The stated conditions are f is CCP, R(A⊺) ∩ri dom f ∗̸ = ∅, a dual solution
exists, α > 0, and Lα(x, u) = f(x) + ⟨u, Ax −b⟩+ α
2 ∥Ax −b∥2.
10.5 Maximality by surjectivity. Consider
L(x, ν) = f(x) + ⟨ν, Ax −b⟩,
is the Lagrangian of (1.5). Assume f is CCP. Using Theorem 9, show that ∂L is maximal.
Hint. Use (2.7).
10.6 Partial inverse. Given an operator 픸: Rm+n ⇒Rm+n, the partial inverse of 픸is the
operator 픸1,−1 : Rm+n ⇒Rm+n defined with
Gra 픸1,−1 = {((x, v), (u, y)) ∈| (u, v) ∈A(x, y)}.
Note that 픸1,−1 = A if n = 0 and 픸1,−1 = 픸−1 is m = 0. Show that if 픸is maximal
monotone, then 픸1,−1 is maximal monotone.
10.7 Maximality of saddle subdifferential with partial inverse. Let L(x, ν) be a convex-concave
saddle function. Then
픽(x, y) = sup
v {L(x, ν) + ⟨y, v⟩}
is called the partial conjugate of L. Show that if 픽is CCP, then ∂L is maximal.
Hint. Show that ∂L is the partial inverse of ∂픽.
10.8 Prove Theorem 12.
Hint. Consider C = {(x, Mx) | x ∈Rn} and ℕC. Left-multiply by [I M ⊺].


## Page 239

224
10
Maximality and monotone operator theory
a(x)
f(x)
−g(x)
Figure 10.1: Illustration of the Hahn–Banach sandwich theorem.
10.9 Prove Theorem 10.
Hint. The Hahn–Banach sandwich theorem states that if f and g are convex and f ≥−g,
and 0 ∈int (dom f −dom g), then there is an affine function such that
f(x) ≥a(x) ≥−g(x).
See Figure 10.1 for an illustration. The Fenchel–Young inequality states that
⟨x, u⟩≤f(x) + f ∗(u)
for any x, u ∈Rn with equality if and only if (x, u) ∈∂f. Define f1(x) = f(x) + 1
2∥x∥2.
Show
F픸(x, u) ≥⟨x, u⟩≥−f1(x) −f ∗
1 (−u).
By the Hahn–Banach sandwich theorem, there is µ, ν ∈Rd such that
F픸(x, u) + f1(y) + f ∗
1 (−v) ≥⟨ν, x −y⟩+ ⟨µ, u −v⟩
for any x, u, y, v ∈Rn. This implies
⟨x −µ, u −ν⟩≥−(⟨y, v⟩+ f1(y) + f ∗
1 (−v)) + ⟨y −µ, v −ν⟩
(10.2)
for any (x, u) ∈픸and any y, v ∈Rn. The choice of (y, v) such that v = ν and −ν ∈
∂f1(y), possible by Theorems 7 and 8, shows
⟨x −µ, u −ν⟩≥0
for all (x, u) ∈픸. This tells us (µ, ν) ∈픸. Plugging x = µ and u = ν into (10.2), we get
0 ≥⟨y, −ν⟩−f1(y) + ⟨µ, −v⟩−f ∗
1 (−v) + ⟨µ, ν⟩
for all y, v ∈Rn. Maximizing over y and v gives us
0 ≥f ∗
1 (−ν) + f1(µ) + ⟨µ, ν⟩
This implies (µ, −ν) ∈∂f1. This implies that 0 ∈(핀+ 픸+ ∂f)(µ).
10.10 Maximal Lipschitz operators. Prove Theorem 16.
Hint. Use the fact that 픸is monotone if and only if 2핁픸−I is nonexpansive.


## Page 240

Exercises
225
10.11 Maximal and strong monotone ⇔maximal strong monotone. Let µ > 0. Show that an
operator is [(maximal monotone) and (µ-strongly monotone)] if and only if it is [maximal
(µ-strongly monotone)].
Hint.
The ⇒implication follows from the definitions (but you should explain why).
For the ⇐implication, the question is whether it is possible for a maximal µ-strongly
monotone operator 픸to have a proper extension ¯픸that is monotone but not µ-strongly
monotone.
Use the fact that 픸−1 : Rn →Rn is a continuous monotone operator by
Theorem 15.
Remark. Fortunately [maximal and strong monotone] and [maximal strong monotone]
mean the same thing, and there is no potential for confusion.
10.12 Maximal and cocoercive ⇔maximal cocoercive. Let β > 0. Show that an operator is
[(maximal monotone) and (β-cocoercive)] if and only if it is [maximal (β-cocoercive)].
Hint. Use Exercise 10.11.


## Page 241

226
10
Maximality and monotone operator theory


## Page 242

Chapter 11
Distributed and decentralized
optimization
In this chapter, we study distributed and decentralized methods that allow com-
putational agents communicating over a network to collaboratively solve an opti-
mization problem. Specifically, we solve
minimize
x∈Rp
r(x) + 1
n
n
X
i=1
(fi(x) + hi(x)),
(11.1)
where r, f1, . . . , fn are CCP (and proximable) and h1, . . . , hn are CCP and differ-
entiable, in a computational setup where a server performs computation with r,
agents i = 1, . . . , n each perform local computation with fi and hi, and the server
and agents communicate over a network to find the (shared) solution x⋆.
We
distinguish distributed and decentralized methods as follows: distributed methods
perform computation over a network (a broader class), while decentralized methods
do so without central coordination (a subclass).
One application of distributed optimization is solving extremely large opti-
mization problems that require the computing power of a cluster of computers
communicating over a network. Another application is controlling a fleet of au-
tonomous vehicles (such as drones) or a wireless sensor network, where individual
agents make real-time decisions based on data gathered by itself and other agents.
Decentralized methods are effective for these setups, as they reduce the high cost
and latency of communication.
11.1
Distributed optimization with centralized consensus
In this section, we study distributed optimization methods based on the consensus
technique of §2.7.4. We first present two base distributed methods and then present
the primal and dual decomposition techniques, which allow us to transform prob-
lems into forms eligible for the base distributed methods. The relatively simple,


## Page 243

228
11
Distributed and decentralized optimization
centralized communication structure of these methods allows us to analyze them
with the tools of §2.
Throughout this section, we write C = {(x1, . . . , xn) | x1 = · · · = xn ∈Rp} for
the consensus set, an unbound index i is assumed to range from i = 1, . . . , n, and we
write the mean over i = 1, . . . , n with a bar notation as in ¯xk = (1/n)(xk
1 +· · ·+xk
n)
and ¯gk = (1/n)(gk
1 + · · · + gk
n).
11.1.1
Base distributed methods
Distributed proximal gradient method.
Consider the problem
minimize
x∈Rp
r(x) + 1
n
n
X
i=1
hi(x),
where r is a CCP function and h1, . . . , hn are differentiable CCP functions. Using
the consensus technique, we obtain the equivalent problem
minimize
x1,...,xn∈Rp
r(x1) + 1
n
n
X
i=1
hi(xi)
subject to
(x1, . . . , xn) ∈C.
Apply FBS and use Exercise 2.29 to get
xk+1/2
i
= xk −α∇hi(xk)
xk+1 = Proxαr
 
1
n
n
X
i=1
xk+1/2
i
!
,
which is equivalent to
gk
i = ∇hi(xk)
xk+1 = Proxαr
 xk −α¯gk
.
We call this method the distributed proximal gradient method. Assume a solution
exists, h1, . . . , hn are L-smooth, and α ∈(0, 2/L). Then xk →x⋆.
This method is distributed, as it has a distributed implementation that alter-
nates between local computation and centralized communication in a setup with
n computational agents and a central node as in Figure 11.1: (i) each agent inde-
pendently computes gk
i = ∇hi(xk) and (ii) the agents send gk
i to the central agent,
the central agent computes their average and performs the proximal gradient step
involving Proxαr, and xk+1 is broadcast to all individual agents.
The central-
ized communication and computation of the average of gk
i in step (ii) is called a
reduction operation in the parallel computing literature.
Distributed (centralized) ADMM/DRS.
Consider the problem
minimize
x∈Rp
n
X
i=1
fi(x),


## Page 244

11.1
Distributed optimization with centralized consensus
229
Parameter server
Agent 1
Agent 2
· · ·
Agent n
Figure 11.1: Depiction of a parameter-server network model. This network struc-
ture allows efficient distributed centralized optimization.
where f1, . . . , fn are CCP functions. Using a variant of the consensus technique,
we obtain the equivalent problem
minimize
x1,...,xn∈Rp
y∈Rp
n
X
i=1
fi(xi)
subject to
xi = y.
Rewrite the constraints to fit ADMM’s form
minimize
x1,...,xn∈Rp
y∈Rp
n
X
i=1
fi(xi)
subject to


I
I
...
I




x1
x2
...
xn

+


−I
−I
...
−I

y = 0,
and apply ADMM to get
xk+1
i
= argmin
xi∈Rp
n
fi(xi) + ⟨uk
i , xi −yk⟩+ α
2 ∥xi −yk∥2o
yk+1 = argmin
y
( n
X
i=1
⟨uk
i , xk+1
i
−y⟩+ α
2 ∥xk+1
i
−y∥2
)
= 1
n
n
X
i=1

xk+1
i
+ 1
αuk
i

uk+1
i
= uk
i + α(xk+1
i
−yk+1).
Simplify the iteration by noting that uk
1, . . . , uk
n has mean 0 after the initial
iteration and eliminating yk:
xk+1
i
= Prox(1/α)fi
 ¯xk −(1/α)uk
i

uk+1
i
= uk
i + α(xk+1
i
−¯xk+1).
We call this method distributed (centralized) ADMM. Convergence follows from
the convergence of ADMM.
Distributed ADMM is also distributed, as it has a distributed implementation
that alternates local computation and centralized communication: (i) each agent


## Page 245

230
11
Distributed and decentralized optimization
independently performs the uk
i - and xk+1
i
-updates with local computation and (ii)
the agents coordinate to compute ¯xk+1 with a reduction.
Alternatively and equivalently, we can apply DRS to the problem obtained with
the consensus technique
minimize
x1,...,xn∈Rp
δC(x1, . . . , xn) +
n
X
i=1
fi(xi)
to get
xk+1/2
i
= Prox(1/α)fi(zi)
zk+1
i
= zk
i −¯zk + 2¯xk+1/2 −xk+1/2
i
.
This is equivalent to the previously stated distributed ADMM. See Exercise 11.7.
11.1.2
Primal decomposition technique
The primal decomposition technique obtains a master problem through minimizing
away local variables. This is a special case of the infimal postcomposition technique
of §3.1.
Consider the problem
minimize
xi∈Rpi
y∈Rq
r(y) + 1
n
n
X
i=1
fi(xi, y),
where r, f1, . . . , fn are CCP. For a fixed y ∈Rq, the minimization over x1, . . . , xn
decomposes into n embarrassingly parallel tasks. We call x1, . . . , xn local variables
and y the coupling variable. With
φi(y) =
inf
xi∈Rpi fi(xi, y),
we obtain the equivalent master problem
minimize
y∈Rq
r(y) + 1
n
n
X
i=1
φi(y),
which can be solved with methods chosen based on the properties of r, φ1, . . . , φn.
For example, when r is proximable and φ1, . . . , φn are smooth, we can apply
the proximal gradient method to solve the master problem:
yk+1 = Proxαr
 
yk −α 1
n
n
X
i=1
∇φi(yk)
!
.
Using Exercise 11.2, we express the method as
x⋆
i (yk) ∈argmax
xi∈Rpi fi(xi, yk)
(0, gk
i ) ∈∂fi(x⋆
i (yk), yk)
yk+1 = Proxαr
 yk −α¯gk
,


## Page 246

11.1
Distributed optimization with centralized consensus
231
provided that the argmins exist. This method has a distributed implementation,
as the subproblems for computing gk
i can be distributed.
When r is proximable but φ1, . . . , φn are not smooth, we can apply the proxi-
mal subgradient method of §7. See Exercises 11.9 and 11.10 for using distributed
ADMM/DRS.
Example 11.1 Common bound problem. Consider the setup where agents i = 1, . . . , n
each reduce its cost fi(xi) subject to the constraint gi(xi) ⪯y, where ⪯denotes
element-wise inequality, while paying a common cost r(y):
minimize
xi∈Rpi
y∈Rq
r(y) +
n
X
i=1
fi(xi)
subject to
gi(xi) ⪯y.
This problem is equivalent to the master problem
minimize
y∈Rq
r(y) + 1
n
n
X
i=1
φi(y),
where
φi(y) =
inf
xi∈Rpi

nfi(xi) + δ{(xi,y) | gi(xi)⪯y}(xi, y)
	
.
See Exercise 11.6 for evaluating the subdifferential ∂φi(y).
Example 11.2 Resource sharing problem. Consider the setup where agents i = 1, . . . , n
each reduces its cost fi(xi) subject to a total resource constraint Pn
i=1 gi(xi) ⪯y,
where ⪯denotes element-wise inequality, while paying a common cost r(y):
minimize
xi∈Rpi
y∈Rq
r(y) +
n
X
i=1
fi(xi)
subject to
n
X
i=1
gi(xi) ⪯y.
This problem is equivalent to the master problem
minimize
y1,...,yn∈Rq
r(y1 + · · · + yn) + 1
n
n
X
i=1
φi(yi),
where φi(yi) = infxi∈Rpi {nfi(xi)+δ{(xi,yi) | gi(xi)⪯yi}(xi, yi)}. The solutions y⋆
1, . . . , y⋆
n
specify the optimal allocation of resources among the agents. By Exercise 1.8, if r(y)
is proximable, then so is r(y1 + · · · + yn). See Exercise 11.6 for evaluating ∂φi(yi).
11.1.3
Dual decomposition technique
The dual decomposition technique obtains a master problem by taking the dual.
This is essentially the same as the dualization technique of §3.2, but the focus is
on obtaining a sum structure so that we can apply the base distributed methods.


## Page 247

232
11
Distributed and decentralized optimization
Dual decomposition with coupling variables.
Consider the problem
minimize
xi∈Rpi
y∈Rq
n
X
i=1
fi(xi, y),
where f1, . . . , fn are CCP. This is the same problem as in the primal decomposition
setup but with r = 0. The equivalent primal problem
minimize
x1,...,xn∈Rp
z1,...,zn∈Rq
y∈Rq
n
X
i=1
fi(xi, zi)
subject to
zi = y
is generated by the Lagrangian
L(x1, . . . , xn, y, z1, . . . , zn, v1, . . . , vn) =
n
X
i=1
(fi(xi, zi) −⟨vi, zi −y⟩) .
With
inf
y∈Rq
n
X
i=1
⟨vi, y⟩=
(
0,
if v1 + · · · + vn = 0
−∞,
otherwise
and
ψi(vi) = sup
xi∈Rp
zi∈Rq
{−fi(xi, zi) + ⟨vi, zi⟩} ,
we obtain the master dual problem
maximize
v1,...,vn∈Rq
−δC⊥(v1, . . . , vn) −
n
X
i=1
ψi(vi),
where C⊥= {(v1, . . . , vn) | v1 + · · · + vn = 0}. (See Exercise 11.8 for a discussion
of C⊥.) The master problem can be solved with methods chosen based on the
properties of ψ1, . . . , ψn.
For example, when ψ1, . . . , ψn are smooth, we can apply the projected gradient
method
gk
i = ∇ψi(vk
i )
vk+1
i
= vk
i −α(gk
i −¯gk)
provided that we initialize the iteration with (v0
1, . . . , v0
n) ∈C⊥.
Using Exer-
cise 11.3, we express the method as
(x⋆
i (vk
i ), gk
i ) ∈argmin
xi∈Rp
gi∈Rq

−fi(xi, gi) + ⟨vk
i , gi⟩
	
vk+1
i
= vk
i −α(gk
i −¯gk),
provided that the argmins exist and we initialize the iteration with (v0
1, . . . , v0
n) ∈
C⊥. This method has a distributed implementation, as the subproblems for com-
puting gk
i can be distributed.
When φ1, . . . , φn are not smooth, we can apply
the projected subgradient method of §7. See Exercises 11.9 and 11.10 for using
distributed ADMM/DRS.


## Page 248

11.1
Distributed optimization with centralized consensus
233
Dual decomposition with inequality constraints.
Consider the problem of Ex-
ample 11.2:
minimize
xi∈Rpi
y∈Rq
r(y) + 1
n
n
X
i=1
fi(xi)
subject to
n
X
i=1
gi(xi) ⪯y,
where r is a CCP function on Rq, f1, . . . , fn are respectively CCP functions on
Rp1, . . . , Rpn, and ⪯denotes element-wise inequality. Assume gi : Rpi →Rq has
the form gi = (gi,1, . . . , gi,q) with scalar-valued CCP functions gi,1, . . . , gi,q for
i = 1, . . . , n. Assume gi,j : Rpi →R (i.e., does not output ∞) for i = 1, . . . , n and
j = 1, . . . , q. This primal problem is generated by the Lagrangian
L(x1, . . . , xn, y, u) = r(y) −⟨u, y⟩+ 1
n
n
X
i=1
(fi(xi) + ⟨u, gi(xi)⟩) −δRn
+(u),
where Rq
+ denotes the nonnegative orthant. With
ψi(u) =
 supxi∈Rpi (⟨−u, gi(xi)⟩−fi(xi))
if u ⪰0
∞
otherwise,
we obtain the master dual problem
maximize
u∈Rq
−r∗(u) −δRq
+(u) −1
n
n
X
i=1
ψi(u).
The master problem can be solved with methods chosen based on the properties
of ψ1, . . . ψn.
For example, when r∗is proximable and ψ1, . . . ψn are smooth, we can apply
DYS and Exercise 11.3 to get
uk+1/2 = ΠRq
+
 ζk
xk+1
i
∈argmin
xi∈Rpi
n
fi(xi) + ⟨uk+1/2, gi(xi)⟩
o
uk+1 = Proxαr∗
 
2uk+1/2 −ζk + α
n
n
X
i=1
gi(xk+1
i
)
!
ζk+1 = ζk + uk+1 −uk+1/2.
When r = δ{b} and ψ1, . . . ψn are smooth, then r∗(u) = ⟨u, b⟩and we can apply
the proximal gradient method and Exercise 11.3 to get
xk+1
i
∈argmin
xi∈Rpi

fi(xi) + ⟨uk, gi(xi)⟩
	
uk+1 = ΠRq
+
 
uk + α
n
n
X
i=1
 gi(xk+1
i
) −b

!
.
When r = δ{b} but ψ1, . . . ψn are not smooth, we can apply the projected subgra-
dient method of §7.


## Page 249

234
11
Distributed and decentralized optimization
Recovering the primal solution.
The dual decomposition technique constructs
a master dual problem, which can be naturally solved with distributed methods.
Under certain strict convexity assumptions, the solution to the primal problem can
be recovered from the dual problem. See Exercise 2.6.
11.2
Decentralized optimization with graph consensus
Decentralized optimization solves an optimization problem defined on a network
without a central agent. In this section, we introduce the notion of graphs to rep-
resent the network and use them to derive and analyze decentralized optimization
methods.
Networks and graphs.
The word graph has two distinct meanings in mathemat-
ics. The first meaning, as in “we plot the graph sin(x) on a graphing calculator,”
concerns the relationship between the inputs and outputs of a function. The graph
of an operator, which we denote as Gra 픸, and the scaled relative graph of §13
use this first meaning. In this chapter, we consider the second meaning, the use in
discrete mathematics for representing networks.
A graph G = (V, E), where V is the set of nodes and E is the set of edges,
represents a network. Assume the network is finite and label the nodes 1 through
n, i.e., V = {1, . . . , n}. Assume the graph is undirected, i.e., an edge {i, j} ∈E is
an unordered pair of distinct nodes i and j. Assume the graph has no self-loops,
i.e., {i, i} /∈E for all i ∈V . Assume the graph is connected, i.e., for any i, j ∈V
such that i̸ = j, there is a sequence of edges
{i, v1}, {v1, v2}, . . . , {vk−1, vk}, {vk, j} ∈E
starting from i and ending at j. In this chapter, a node represents a computational
agent that stores data and performs computation, and an edge {i, j} represents a
direct connection between i and j through which agents i and j can communicate.
See Figure 11.2.
We use the words network, agent, and connection to refer to the physical infras-
tructure and graph, node, and edge to refer to their corresponding mathematical
abstractions. If {i, j} ∈E, then we say j is adjacent to i and that j is a neighbor
of i (and vice versa). Write
Ni = {j ∈V | {i, j} ∈E}
for the set of neighbors of i and |Ni| for the number of neighbors of i. Ni does not
include i itself.
In the decentralized setup, we assume r = 0 in (11.1). Using the notation of
graphs, we can recast problem (11.1) into
minimize
{xi}i∈V ⊂Rp
X
i∈V
fi(xi) + hi(xi)
subject to
xi = xj
∀{i, j} ∈E.
(11.2)


## Page 250

11.2
Decentralized optimization with graph consensus
235
Agent 1
Agent 2
Agent 3
Agent 4
Agent 5
Agent 6
Figure 11.2:
Depiction of a network without a central agent.
Decentral-
ized optimization is suitable for this network structure.
We represent this
network with the graph G = (V, E), where V
= {1, 2, 3, 4, 5, 6} and E =
{{1, 2}, {1, 4}, {2, 3}, {3, 4}, {4, 5}, {4, 6}}.
Throughout this chapter, we assume G = (V, E) is a finite, undirected, connected
graph without self-loops.
Because the network is connected, all agents can communicate with each other,
just as any computer can communicate with any other computer over the inter-
net. Any optimization method can be executed over the network by implementing
communication between arbitrary nodes; if they are not directly connected, the
communication is relayed over multiple edges. However, in distributed and decen-
tralized optimization, communication, rather than computation, tends to be the
bottleneck and relayed communication incurs a huge communication cost. There-
fore, methods with reduced communication costs are preferred, and we consider
algorithms that utilize communication across single edges, the most basic commu-
nication unit, without directly relying on long-range relayed communication.
11.2.1
Decentralized ADMM
Consider the setup (11.1) with r = h1 = · · · = hn = 0. For every edge e = {i, j},
introduce a variable ye ∈Rp and replace the constraint xi = xj of (11.2) with the
two constraints xi = ye and xj = ye to obtain the equivalent problem
minimize
{xi}i∈V
{ye}e∈E
X
i∈V
fi(xi)
subject to
(
xi −ye = 0
xj −ye = 0
∀e = {i, j} ∈E.
(11.3)


## Page 251

236
11
Distributed and decentralized optimization
For each e = {i, j} ∈E, introduce the dual variables ue,i for xi −ye = 0 and ue,j
for xj −ye = 0. The augmented Lagrangian is
Lα(x, y, u) =
X
i∈V
fi(xi) +
X
e={i,j}
(⟨ue,i, xi −ye⟩+ ⟨ue,j, xj −ye⟩)
+
X
e={i,j}
α
2
 ∥xi −ye∥2 + ∥xj −ye∥2
,
where P
e={i,j} is the summation over all edges e = {i, j} ∈E. Express ADMM
(3.8) applied to this setup as
xk+1
i
= argmin
xi∈Rp


fi(xi) +
X
j∈Ni

⟨uk
{i,j},i, xi −yk
{i,j}⟩+ α
2 ∥xi −yk
{i,j}∥2


∀i ∈V
yk+1
e
= argmin
ye∈Rp



X
t=i,j

⟨uk
e,t, xk+1
t
−ye⟩+ α
2 ∥xk+1
t
−ye∥2



∀e = {i, j} ∈E
uk+1
e,t
= uk
e,t + α(xk+1
t
−yk+1
e
)
∀e = {i, j} ∈E, t = i, j.
As is, this method can be implemented in a decentralized manner. However, we
simplify further. Using the closed-form solution yk+1
e
= 1
2
P
t=i,j(xk+1
t
+ 1
αuk
e,t),
eliminate yk+1
e
in the u-update to get
uk+1
e,i
= uk
e,i + α

xk+1
i
−1
2
X
t=i,j

xk+1
t
+ 1
αuk
e,t


= 1
2(uk
e,i −uk
e,j) + α
2 (xk+1
i
−xk+1
j
),
∀e = {i, j} ∈E.
Using uk
e,i + uk
e,j = 0 for all e = {i, j} and k = 1, 2, . . . , write yk
e = 1
2(xk
i + xk
j ),
uk+1
e,i
= uk
e,i + α
2 (xk+1
i
−xk+1
j
), and
xk+1
i
= argmin
xi∈Rp


fi(xi) + α
2
X
j∈Ni
xi −1
2(xk
i + xk
j ) + 1
αuk
{i,j},i

2



= argmin
xi∈Rp





fi(xi) + α|Ni|
2

xi −
1
|Ni|
X
j∈Ni
1
2(xk
i + xk
j ) −1
αuk
{i,j},i

2




for all i ∈V . By defining vk
i =
1
|Ni|
P
j∈Ni

1
2(xk
i + xk
j ) −1
αuk
{i,j},i

and ak
i =
1
|Ni|
P
j∈Ni xk
j , we obtain the simplified ADMM iteration:
xk+1
i
= Prox(α|Ni|)−1fi(vk
i )
i ∈V
(11.4a)
(
ak+1
i
=
1
|Ni|
P
j∈Ni xk+1
j
vk+1
i
= vk
i + ak+1
i
−1
2ak
i −1
2xk
i
i ∈V.
(11.4b)


## Page 252

11.3
Decentralized optimization with mixing matrices
237
We call this method decentralized ADMM. Convergence follows from the conver-
gence of ADMM. Step (11.4a) must be completed for all i ∈V before steps (11.4b)
start for any i. The two steps in (11.4b) must be sequential at each i but can be
out of sync across different i.
This method is decentralized, as it has a decentralized implementation that
alternates local computation and communication with neighbors in a decentralized
setup as in Figure 11.2: (i) each agent independently performs the vk- and xk+1-
updates with local computation and (ii) the agents send xk+1
i
to its neighbors and
each agent computes ak+1
i
by averaging the xk+1
j
’s received from its neighbors.
The decentralized communication and computation of step (ii) is referred to as a
reduction operation in the neighborhood or neighborhood reduction.
Decentralized FLiP-ADMM.
We can generalize decentralized ADMM to solve
minimize
{xi}i∈V
n
X
i=1
fi(x) + hi(x),
the general formulation of (11.1), using FLiP-ADMM of §8 with P = βI, Q = 0,
ϕ = 1, α > 0, and β > 0:
xk+1
i
= Prox(α|Ni|+β)−1fi
 (α|Ni| + β)−1  α|Ni|vk
i + βxk
i −∇hi(xk
i )

i ∈V
(
ak+1
i
=
1
|Ni|
P
j∈Ni xk+1
j
vk+1
i
= vk
i + ak+1
i
−1
2ak
i −1
2xk
i ,
i ∈V
with initial points v0
i =
1
2|Ni|
P
j∈Ni(x0
i + x0
j) and arbitrary x0
i , i ∈V . See Exer-
cise 11.11.
Decentralized methods and synchronization.
The decentralized methods of this
chapter are synchronous in the sense that all agents must complete their compu-
tation and communication for the iteration to proceed. In some real-world decen-
tralized networks, however, synchronization is a costly and unrealistic requirement.
For such systems, one can use asynchronous decentralized methods, which combine
the asynchrony studied in §6 with the decentralized methods of this chapter. See
the bibliographical notes.
11.3
Decentralized optimization with mixing matrices
In this section, we introduce the notion of mixing matrices and use them to describe
and analyze a broader class of decentralized optimization methods.


## Page 253

238
11
Distributed and decentralized optimization
Decentralized notation.
Define the stack operator and use boldface symbols to
denote stacked variables
x = stack(x1, . . . , xn) =


— x⊺
1 —
...
— x⊺
n —

∈Rn×p.
(11.5)
Write xk = stack(xk
1, . . . , xk
n) likewise to denote the iterates. Write both x⋆∈Rp
and x⋆= stack(x⋆, . . . , x⋆) ∈Rn×p to denote the solution of the optimization prob-
lem at hand. For any x = stack(x1, . . . , xn) ∈Rn×p and y = stack(y1, . . . , yn) ∈
Rn×p, define
⟨x, y⟩=
n
X
i=1
⟨xi, yi⟩.
For any symmetric positive semidefinite A ∈Rn×n, define
∥x∥2
A = ⟨x, Ax⟩
and specifically define ∥x∥2 = ∥x∥2
I = ⟨x, x⟩. Finally, define
f(x) =
n
X
i=1
fi(xi),
h(x) =
n
X
i=1
hi(xi)
Proxαf(x) = stack(Proxαf1(x1), . . . , Proxαfn(xn))
∇h(x) = stack(∇h1(x1), . . . , ∇hn(xn)).
We say x = stack(x1, . . . , xn) is in consensus if x1 = · · · = xn. A solution (or
any feasible point) of (11.2) is in consensus. The methods of this chapter produce
iterates that are in consensus in the limit.
11.3.1
Mixing matrices
We informally say W ∈Rn×n is a mixing matrix when an application of W, within
a distributed method, represents a round of communication and the aggregation
of the communicated information. Throughout this chapter, let λ1, . . . , λn denote
the eigenvalues of W.
We say W is a decentralized mixing matrix with respect to a graph G = (V, E)
if Wij = 0 when i̸ = j and {i, j} /∈E. (Wii may be nonzero.) Consider the setup
where agents 1, . . . , n each have access to the entries y1, . . . , yn of the vector y ∈Rn,
respectively, and we wish to evaluate the matrix-vector product Wy. When W is
a decentralized mixing matrix, we can do so in a decentralized manner: since
(Wy)i =
n
X
j=1
Wijyj =
X
j∈Ni∪{i}
Wijyj,
agent i needs to communicate only with its neighbors.


## Page 254

11.3
Decentralized optimization with mixing matrices
239
Example 11.3 Local averaging matrix. With the mixing matrix W ∈Rn×n defined
by
Wij =

1
|Ni|
if {i, j} ∈E
0
otherwise
for i, j ∈{1, . . . , n} and
˜f(x) =
n
X
i=1
1
|Ni|fi(xi),
we can express decentralized ADMM (11.4) as
xk+1 = Proxα ˜
f(vk)
ak+1 = Wxk+1
vk+1 = vk + ak+1 −1
2ak −1
2xk.
Decentralized averaging.
As a motivating example for mixing matrices, consider
decentralized averaging: each agent i ∈V has a vector xi ∈Rp, and the goal is to
compute the average ¯x = 1
n
Pn
i=1 xi in a decentralized manner. This problem is a
special case of (11.1) with fi(x) = 1
2∥x −xi∥2.
The method
xk+1 = Wxk
(11.6)
with the starting point x0 = stack(x1, . . . , xn) and a decentralized mixing matrix
W ∈Rn×n is called the decentralized averaging method. Let 1 denote the column
vector whose every entry is 1.
The method converges for all x0 if and only if
W1 = 1, 1⊺W = 1⊺, and 1 = |λ1| > |λ2| ≥· · · ≥|λn|. To clarify, |λi| denotes the
absolute value or modulus of the ith eigenvalue of W, sorted by absolute value.
We leave the proof to Exercise 11.14.
Condition W1 = 1 implies that the set of x-vectors in consensus (i.e., the
components of x satisfy x1 = · · · = xn) are fixed points of the iteration. Condition
1⊺W = 1⊺implies the mean is preserved throughout the iteration. Finally, the
eigenvalue condition implies the iteration converges.
Note that λ1 is real, i.e.,
1 = λ1, since W1 = 1 and 1⊺W = 1⊺imply that 1 is an eigenvalue of W.
Assumptions on mixing matrices.
A mixing matrix W ∈Rn×n used in decen-
tralized optimization often satisfies some or all of the following assumptions:
W = W ⊺
(11.7a)
N(I −W) = span(1)
(11.7b)
1 = λ1 > max {|λ2|, . . . , |λn|}.
(11.7c)
Although assumption (11.7a) was not assumed in decentralized ADMM or decen-
tralized averaging, it is common; methods with symmetric mixing matrices tend
to be easier to analyze. Assumption (11.7b) implies x is in consensus if and only
if x = Wx and is required for almost all decentralized optimization methods. For


## Page 255

240
11
Distributed and decentralized optimization
example, the mixing matrix of Example 11.3 satisfies assumption (11.7b) but not
(11.7a) or (11.7c). Finally, assumption (11.7c) is assumed to establish the conver-
gence of certain methods. Note that assumption (11.7a) implies the eigenvalues
are real (but not necessarily nonnegative), and assumption (11.7b) implies 1 = λ1.
Example 11.4 Laplacian-based mixing matrix. Consider the symmetric mixing matrix
W ∈Rn×n defined by
W = I −1
τ L,
where L is the graph Laplacian
Lij =



|Ni|
if i = j
−1
if {i, j} ∈E
0
otherwise
for i, j ∈{1, . . . , n} and τ is a constant satisfying τ >
1
2λmax(L). Using standard
arguments with the graph Laplacian, one can show that W1 = 1 and 1 = λ1 >
max {|λ2|, . . . , |λn|}.
Example 11.5 Metropolis mixing matrix. Consider the symmetric mixing matrix W ∈
Rn×n defined by
Wij =



1
max{|Ni|,|Nj|}+ε
if {i, j} ∈E
1 −P
j∈Ni Wij
if i = j
0
otherwise
for i, j ∈{1, . . . , n}, where ε > 0.
Using standard arguments with the Perron–
Frobenius theory (W is a stochastic matrix for an irreducible and aperiodic Markov
chain), one can show W1 = 1 and 1 = λ1 > max {|λ2|, . . . , |λn|}.
Relationship with stochastic matrices.
Mixing matrices and stochastic matrices
for Markov chains share some apparent similarities, but they do have some key dif-
ferences. Given a Markov chain with states 1, . . . , n, its stochastic matrix P ∈Rn×n
contains the transition probabilities as Pij being the probability of transitioning
from i to j, for all states i and j. Conversely, any matrix P ∈Rn×n satisfying
Pij ≥0 for all i, j and P1 = 1 can be interpreted as a stochastic matrix of a
Markov chain.
The first key difference between the two notions is that stochastic matrices
have nonnegative entries, while mixing matrices can have negative entries.
See
Exercise 11.16 for an example of a mixing matrix with negative entries. Another
difference is in their primary use as linear operators. With a stochastic matrix
P ∈Rn×n satisfying P1 = 1 (which means the total probability 1 is preserved),
the key operation is the vector-matrix product
(πk+1)⊺= (πk)⊺P,
and it represents the evolution of the state probabilities.
With mixing matrix
W ∈Rn×n satisfying W1 = 1 (which means a vector in consensus remains in
consensus), the key operation is the matrix-(stacked vector) product
xk+1 = Wxk.


## Page 256

11.3
Decentralized optimization with mixing matrices
241
When a mixing matrix is a stochastic matrix, one can utilize the classical
Markov chain theory based on the Perron–Frobenius theorem.
For example, if
W ∈Rn×n is a stochastic matrix for an irreducible Markov chain, then N(I−W) =
span(1) holds; if the Markov chain is irreducible and aperiodic, then 1 = λ1 >
max{|λ2|, . . . , |λn|} holds.
A Markov chain is irreducible if every state can be
reached from every other state. A state of a Markov chain is periodic if the chain
can return to the state only at multiples of some integer larger than 1. A Markov
chain is aperiodic if none of its states is periodic. See the bibliographical notes.
Dynamic mixing matrices.
For the sake of simplicity, we assumed the mixing
matrices do not depend on the iteration. However, when the connectivity of the
underlying graph is dynamic, one has to use a series of dynamic mixing matrices
instead of a fixed one.
11.3.2
Inexact decentralized methods
Consider the setup with r = f1 = · · · = fn = 0, and a symmetric mixing matrix
W = W ⊺∈Rn×n satisfying N(I −W) = span(1) and 1 = λ1 > max {λ2, . . . , λn}.
We write (11.1) equivalently as
minimize
x∈Rn×p
h(x)
subject to
(I −W)x = 0.
(11.8)
We now consider inexact decentralized methods that solve a penalty formulations
that approximate (11.8). When these inexact methods converge, they converge to
an approximation of the original solution.
Decentralized gradient descent (DGD).
Consider the penalty formulation
minimize
x∈Rn×p
h(x) + 1
2α∥x∥2
I−W .
(11.9)
Since the penalty term ∥x∥2
I−W equals 0 if and only if x is in consensus, we expect
this formulation to approximate (11.8) well when α > 0 is small. Gradient descent
with stepsize α applied to this penalty formulation is
xk+1 = xk −α

∇h(xk) + 1
α(I −W)xk

= Wxk −α∇h(xk).
We call this method decentralized gradient descent (DGD) or the combine-then-
adapt method. (The name combine-then-adapt is explained in the bibliographical
notes.) DGD is decentralized when W is a decentralized mixing matrix: computing
Wxk requires communication with neighbors, and all other operations require local
computation. Assume the penalty formulation has a solution, h1, . . . , hn are L-
smooth, and α ∈(0, (1 + λn(W))/L).
Then xk converges to a solution of the
penalty formulation. The stepsize bound of (1+λn(W))/L follows from the stepsize
requirement (stepsize) × (Lipschitz constant) < 2 of gradient descent.


## Page 257

242
11
Distributed and decentralized optimization
Diffusion.
Further assume min{λ2, . . . , λn} > 0, i.e., assume W is positive defi-
nite and therefore invertible, and consider the penalty formulation
minimize
x∈Rn×p
h(x) + 1
2α∥x∥2
W −1−I.
(11.10)
The forward-backward splitting FPI with (핀+ α픹)−1(핀−α픸), where 픸= ∇h,
픹= 1
α(W −1 −I), is
xk+1 = W(xk −α∇h(xk)).
Note that W −1 appears in the analysis and formulation of the algorithm, but not
within the iteration xk+1 = W(xk −α∇h(xk)).
This method is called the method of diffusion or the adapt-then-combine method.
(The name adapt-then-combine is explained in the bibliographical notes.) Diffu-
sion is also decentralized when W is a decentralized mixing matrix. Assume the
penalty formulation has a solution, h1, . . . , hn are Lh-smooth, and α ∈(0, 2/Lh).
Then xk converges to a solution of the penalty formulation.
Discussion.
The stepsize condition for diffusion α < 2/L is wider than the stepsize
condition for DGD α < (1 + λn(W))/L. Loosely speaking, use of a larger stepsize
often leads to faster convergence.
When min{λ2, . . . , λn} > 0 does not hold, we can still use diffusion using the
positive definite mixing matrix (1−θ)I +θW with θ ∈(0, 1/(1−min{λ2, . . . , λn})).
11.3.3
Exact decentralized methods
Consider the setup with r = 0 and a symmetric mixing matrix W = W ⊺∈Rn×n
satisfying N(I −W) = span(1) and 1 = λ1 > max {λ2, . . . , λn}. Since I −W is
symmetric positive semidefinite, there exists a symmetric U ∈Rn×n such that
U 2 = 1
2(I −W).
Note, N(U) = span(1).
The problem (11.1) is equivalent to
minimize
x∈Rn×p
f(x) + h(x) + δ{0}(Ux),
(11.11)
where the indicator function δ{0}(Ux) encodes the constraint Ux = 0.
In this
section, we present decentralized methods based on primal-dual splitting methods
that converge to an exact solution. The algorithms utilize W, while U is used only
in the analysis.
PG-EXTRA.
Apply Condat–Vũ of Exercise 3.5 to (11.11) with g = δ{0} (so
Proxβg∗= 핀) to get
uk+1 = uk + βUxk
xk+1 = Proxαf
 xk −α∇h(xk) −αU(2uk+1 −uk)

.


## Page 258

11.3
Decentralized optimization with mixing matrices
243
To eliminate U, define wk =
1
β Uuk = 1
2(I −W) Pk−1
j=0 xj. Choose β = α−1 for
simplicity and rearrange the terms to get
xk+1 = Proxαf(Wxk −α∇h(xk) −wk)
wk+1 = wk + 1
2(I −W)xk,
(11.12)
where we initialize w0 = 0, corresponding to u0 = 0 to avoid computing Uu0, and
set x0 arbitrarily.
This method is called PG-EXTRA. PG-EXTRA is decentralized when W is a
decentralized mixing matrix. Assume total duality holds, h1, . . . , hn are L-smooth,
and 0 < α < (1 + λmin(W))/L. Then, xk →x⋆. The stepsize bound follows from
the stepsize requirement (3.13) of Condat–Vũ and λmax(U 2) = 1/2 −1/2λmin(W).
The method EXTRA is the special case of PG-EXTRA with f = 0. See Exer-
cise 11.17 for generalizations of PG-EXTRA.
NIDS.
Apply PD3O on (11.11) to get
xk+1 = Proxαf(xk −αUuk −α∇h(xk))
uk+1 = uk + βU
 2xk+1 −xk + α
 ∇h(xk) −∇h(xk+1)

.
We initialize u0 = 0 but set x0 arbitrarily. To eliminate U, define zk = xk −
αUuk −α∇h(xk). Choose β = α−1 for simplicity and rearrange the terms to get
xk+1 = Proxαf(zk)
zk+1 = zk −xk+1 + 1
2(I + W)
 2xk+1 −xk + α
 ∇h(xk) −∇h(xk+1)

,
where we initialize z0 = x0 −α∇h(x0) but set x0 arbitrarily.
This method is called the Network InDependent Stepsize (NIDS) method. NIDS
is decentralized when W is a decentralized mixing matrix. Assume total duality
holds, h1, . . . , hn are L-smooth, and α ∈(0, 2/L). Then xk →x⋆. Note that the
choice of α ∈(0, 2/L) is independent of the mixing matrix and, thus, the network
topology.
Discussion of PG-EXTRA and NIDS.
The stepsize requirement of NIDS is more
favorable than that of PG-EXTRA. A drawback of PG-EXTRA is that the stepsize
α is affected by the eigenvalues of W, thus, also by the network structure. This
not only limits the size of α but also makes the choice of α more difficult when
the network is not fully known. In contrast, the stepsize α of NIDS can be chosen
independently of W.
On the other hand, PG-EXTRA can compute Wxk and ∇h(xk) simultaneously,
but NIDS must do its corresponding steps sequentially. Therefore, when those two
steps cost similar amounts of time, PG-EXTRA can be implemented to run nearly
twice as fast per iteration than NIDS.
When f = 0, we can simplify PG-EXTRA to one line. Apply Proxαf = 핀to
(11.12) and subtract xk from xk+1 to get
xk+1 −xk = W(xk −xk−1) −α
 ∇h(xk) −∇h(xk−1)

−(wk −wk−1).


## Page 259

244
11
Distributed and decentralized optimization
Then use wk −wk−1 = 1
2(I −W)xk−1 to eliminate wk −wk−1 and obtain the
one-line formula for xk+1 below. For comparison, also use f = 0 to simplify NIDS
to one line:
PG-EXTRA:
xk+1 = f
W(2xk −xk−1) + α(∇h(xk−1) −∇h(xk))
NIDS:
xk+1 = f
W
 2xk −xk−1 + α(∇h(xk−1) −∇h(xk))

,
where f
W = 1
2(W +I). PG-EXTRA resembles DGD while NIDS resembles diffusion.


## Page 260

Bibliographical Notes
245
Bibliographical Notes
Primal and dual decomposition.
Primal decomposition has its roots in the Dantzig–
Wolfe decomposition [DW60] and Benders’ decomposition [Ben62] for linear programming.
Primal decomposition in the form we present was first presented by Geoffrion [Geo70],
although the name “primal decomposition” was coined by Silverman [Sil72]. Dual decom-
position, which is also called Lagrangian relaxation, is used widely not only in optimization
with continuous variables [Eve63, SGJ11] but also in optimization with discrete variables
[Lem01, Fis04]. For other overviews on decomposition methods, see [PC06, CLCD07].
Decentralized ADMM.
There has been a large body of work studying decentralized
ADMM and its variants.
Bertsekas and Tsitsiklis [BT89], Mateos, Bazerque, and Gi-
annakis [MBG10], Schizas, Ribeiro, and Giannakis [SRG08], and Ling and Tian [LT10]
studied various decentralize ADMM methods and Shi et al. [SLY+14], Chang, Hong, and
Wang [CHW15], and Wei and Ozdaglar [WO13] further analyzed their convergence rates.
Mixing matrices and Markov chains.
Mixing matrices in decentralized optimization
and Markov chains are closely related, as discussed in §11.3.1. We refer readers to the work
of Boyd, Diaconis, and Xiao [XB04, BDX04] for further discussion on this connection, and
in particular, the discussion on the mixing matrices of Examples 11.4 and 11.5.
Inxact decentralized methods.
Cattivelli, Lopes, and Sayed introduced DGD [CLS07,
CS10]. We clarify that the original authors of DGD called it distributed gradient descent,
but we have decided to call it decentralized gradient descent per our definitions of dis-
tributed and decentralized methods. Yuan, Ling, and Yin [YLY16] showed that, with a
fixed stepsize α, DGD makes progress toward an O(α)-size neighborhood of the solution
to the original problem. Convergence to a solution (rather than a neighborhood) is possi-
ble with diminishing stepsizes as studied by Chen [Che12], Jakovetic, Xavier, and Moura
[JXM14], and Zeng and Yin [ZY18].
In the community of bio-inspired network signal processing, subtracting α∇h is called
adaptation, in analogy to organisms adapting to the environment, and applying W is
called combination. This is why DGD is also called combine-then-adapt, while diffusion
is called adapt-then-combine.
Exact decentralized methods.
Shi, Ling, Wu, and Yin presented EXTRA [SLWY15a]
as the first method to achieve “exact convergence,” i.e., the method converges to an
exact solution (unlike DGD), while using gradients ∇h and a fixed stepsize. The name
EXTRA is the abbreviation of EXact firsT-ordeR Algorithm. In a follow-up work, Shi,
Ling, Wu, and Yin presented PG-EXTRA [SLWY15b] as a generalization of EXTRA
that accommodates proximable functions. Li and Yan [LY17] show that PG-EXTRA,
in fact, converges with parameters that are chosen more aggressively, specifically with
α < ( 3
4(1 + λn(W)) + 1
2)/L and f
W = (W + I)/2. Li, Shi, and Yan presented NIDS
[LSY19] as an improvement upon PG-EXTRA that allows the stepsize α to be chosen
independent of the network topology.
Directed graph.
A graph is said to be a directional graph or digraph if its edges are
directed from one node to another. If agent i can send information directly to agent j but
not vice versa, we model this connection with a directed edge (i, j) and allow Wji̸ = 0 but
require Wij = 0 in the mixing matrix W. (So W is asymmetric.) Decentralized methods
for digraphs often use the “push-sum” technique [KDG03, NO15], and it does not seem
to be possible to obtain them via operator splitting.


## Page 261

246
11
Distributed and decentralized optimization
Other methods.
There is a large body of research on decentralized optimization meth-
ods not covered in this chapter. Terelius, Topcu, and Murray proposed a decentralized
method [TTM11] based on dual decomposition. Zhu and Marinez [ZM10] introduced gra-
dient tracking; see Exercises 11.18 and 11.19. The methods [NOSU17, XZSX15, LSY19,
QL18] allow stepsizes chosen using agents’ local information, similar to NIDS. Nedic,
Olshevsky, and Shi [NOS17] introduced the method DIGing and showed it has linear
convergence on certain time-varying graphs; see Exercise 11.19. Yuan, Ying, Zhao, and
Sayed [YYZS19b, YYZS19a] proposed methods similar to NIDS and that also support
left-stochastic matrices. Scaman et al. [SBB+17, SBB+18, SBB+19] established the lower
bounds of gradient and communication complexities. Accelerated decentralized methods
are another large body of work [QL20, SBB+18, LFYL20, SBB+17, ULGN21]. Lian et
al. [LZZ+17, LZZL18] introduced decentralized variants of stochastic gradient descent for
deep learning. Wu et al. [WYL+18] generalized PG-EXTRA to asynchronous communi-
cation with information delays.


## Page 262

Exercises
247
Exercises
11.1 Envelope theorem. Let f : X × Y →R and h(y) = infx∈X f(x, y). Assume X ⊆Rm is
nonempty, Y ⊆Rn is an open set, h(y) > −∞for all y ∈Y , f(x, y) differentiable in
y ∈Y for all fixed x ∈X, h is differentiable at y ∈Y , and x⋆(y) ∈argminx∈X f(x, y)
exists. Show that
∇yh(y) = (∇yf)(x⋆(y), y).
Hint. Note that
f(x, z) −h(z) ≥0
for all x ∈X and z ∈Y . For a given y ∈Y , show that
f(x⋆(y), z) −h(z),
as a function of z, is minimized at z = y.
Remark. When convexity is assumed, the differentiability assumptions can be dropped.
These setups are explored in Exercises 11.2 and 11.3.
Remark. By the same reasoning, if h(y) = supx∈X f(x, y), then
x⋆(y) ∈argmax
x∈X
f(x, y)
∇yh(y) = (∇yf)(x⋆(y), y).
11.2 Subgradients with partial minimization. Let f(x, y) with x ∈Rm and y ∈Rn be a convex
function. (f is jointly convex in x and y.) Let h(y) = infx∈Rm f(x, y). Show that
(a) h: Rn →R ∪{±∞} is convex and
(b) for all y ∈Rn, if x⋆(y) ∈argminx∈Rm f(x, y) exists, then (0, g) ∈∂f(x⋆(y), y) if and
only if g ∈∂h(y).
Remark. Even if f is CCP, h may not be proper.
11.3 Subgradients with partial maximization. Let f(v, y) with v ∈Rm and y ∈Rn be convex
in y for all fixed v. Let h(y) = supv∈Rm f(v, y). Show that
(a) h: Rn →R ∪{±∞} is convex and
(b) for all y ∈Rn, if v⋆(y) ∈argmaxv∈Rm f(v, y) exists, then g ∈(∂yf)(v⋆(y), y) implies
g ∈∂h(y). To clarify, g ∈(∂yf)(v⋆(y), y) means
f(v⋆(y), z) ≥f(v⋆(y), y) + ⟨g, z −y⟩
∀z ∈Rn.
11.4 Primal and dual decomposition duality. Let f(x, y) with a function of x ∈Rp and y ∈Rq.
Define
φ(y) = inf
x∈Rp f(x, y),
ψ(v) = sup
x∈Rp
y∈Rq
{−f(x, y) + ⟨v, y⟩} .
Show that ψ = φ∗.
11.5 Subgradients of indicator functions of linear constraints. Prove the following statements.
(a) Let A ∈Rm×n, b ∈Rm, and C = {x ∈Rn : Ax = b}. For x ∈C, ∂δC(x) = {A⊺u :
u ∈Rm}. In particular, for D = {(x, y) ∈Rn+m : Ax −y = b} and (x, y) ∈D,
∂δD(x, y) = {[A⊺u; −u] : u ∈Rm}.


## Page 263

248
11
Distributed and decentralized optimization
(b) Let A = [A1; A2] ∈R(m1+m2)×n, b = [b1; b2] ∈R(m1+m2), and C = {x ∈Rn : Ax ≤
b}. Suppose x ∈C satisfies A1x = b1 and A2x < b2. Then
∂δC(x) = {A⊺u : u = [u1; u2] ∈R(m1+m2), u1 ≥0, u2 = 0}
= {A⊺
1u1 : u1 ∈Rm1, u1 ≥0}.
(To clarify, u1 and u2 correspond to A1 and A2, respectively.) In particular, for
D = {(x, y) ∈Rn+m : Ax−y ≤b} and (x, y) ∈C such that A1x = b1 and A2x < b2,
∂δD(x, y) = {[A⊺u; −u] : u = [u1; u2] ∈Rm, u1 ≥0, u2 = 0}.
Vector u coincides with the Lagrange multipliers.
11.6 Subgradients of minimization objective subject to linear constraints. Consider
h(x, y) = δ{(x,y)∈Rp+q | Ax⪯y}(x, y) + f(x),
where A ∈Rq×p, f is CCP, and ⪯denotes element-wise inequality. Let φ(y) = infx∈Rp h(x, y),
whose value is equal to the optimal value of
minimize
x∈Rp
f(x)
subject to
Ax ⪯y.
Suppose (x⋆(y), u⋆(y)) is a primal-dual solution pair for which strong duality holds, i.e.,
(x⋆(y), u⋆(y)) is a saddle point of
L(x, µ) = f(x) + ⟨µ, Ax −y⟩.
Show that −u⋆(y) ∈∂φ(y).
11.7 Distributed ADMM = Distributed DRS. Show that distributed ADMM
xk+1
i
= Prox(1/α)fi

¯xk −(1/α)uk
i

uk+1
i
= uk
i + α(xk+1
i
−¯xk+1),
and distributed DRS
xk+1/2
i
= Prox(1/α)fi(zi)
zk+1
i
= zk
i −¯zk + 2¯xk+1/2 −xk+1/2
i
are equivalent in the sense that they generate an identical sequence of iterates after a
change of variables.
Hint. Note that uk
1, . . . , uk
n has mean 0 after the initial iteration.
11.8 Dual of consensus. Consider the consensus set
C = (x1, . . . , xn) ∈Rpn ∈{(x1, . . . , xn) | x1 = · · · = xn}.
Show that the orthogonal complement of C (as defined in, say, Exercise 2.34) is
C⊥= {(v1, . . . , vn) ∈Rpn | v1 + · · · + vn = 0}.


## Page 264

Exercises
249
11.9 DRS with primal decomposition. Consider the primal decomposition formulation
minimize
z∈Rq
n
X
i=1
φi(z),
with φi(z) = infx∈Rp fi(x, z). Show that DRS applied to the consensus formulation
minimize
z1,...,zn∈Rq
n
X
i=1
φi(zi) + δC(z1, . . . , zn)
is equivalent to distributed ADMM:
zk+1
i
= Prox(1/α)φi

¯zk −(1/α)uk
i

uk+1
i
= uk
i + α(zk+1
i
−¯zk+1),
for i = 1, . . . , n. For simplicity, assume all convex functions are CCP.
Remark. Note that Prox(1/α)φi(z0) can be computed by minimizing f(x, z) + α
2 ∥z −z0∥2
with respect to x, z and returning z.
11.10 DRS with dual decomposition. Consider the dual decomposition formulation
minimize
v1,...,vn∈Rq
n
X
i=1
ψi(vi) + δC⊥(v1, . . . , vn)
with ψi(vi) = supxi∈Rp
zi∈Rq {−fi(xi, zi) + ⟨vi, zi⟩} and
C⊥= {(v1, . . . , vn) ∈Rqn | v1 + · · · + vn = 0}.
Show that DRS applied to this formulation is equivalent to the method of Exercise 11.9.
For simplicity, assume all convex functions are CCP.
Hint. While it is possible to solve this problem by directly working out the application
of DRS and establishing the equivalence, this alternative approach is more insightful.
Use Exercises 11.8 and 2.34. Then use Exercise 11.4 and the self-dual property of DRS
discussed in §9.3.
11.11 FLiP-ADMM-based decentralized optimization. Consider
minimize
{xi}i∈V
{ye}e∈E
X
i∈V
fi(xi) + hi(xi)
subject to
(
xi −ye = 0
xj −ye = 0
∀e = {i, j} ∈E,
where fi is CCP and hi is CCP and L-smooth for i ∈V . Derive decentralized FLiP-
ADMM and use Theorem 6 to obtain convergence conditions.
11.12 Another ADMM-based decentralized method. Show that the formulation
minimize
{xi,yi}i∈V
X
i∈V
fi(xi)
subject to
xi = yi
∀i ∈V
 xi −yj = 0
xj −yi = 0
∀{i, j} ∈E


## Page 265

250
11
Distributed and decentralized optimization
is equivalent to (11.3). Apply ADMM to derive
xk+1
i
= Prox(α(|Ni|+1))−1fi


1
|Ni| + 1
X
j∈Ni∪{i}
yk
j −1
αvk
i


yk+1
i
=
1
|Ni| + 1
X
j∈Ni∪{i}
xk+1
j
vk+1
i
= vk
i + αxk+1
i
−
α
|Ni| + 1
X
j∈Ni∪{i}
yk+1
j
for all i ∈V . Also, explain why the method is decentralized.
11.13 Decentralized ADMM with a bipartite graph. We say a graph G = (V, E) is bipartite if
there exists a partitioning Vl and Vr of V (i.e., Vl ∪Vr = V and Vl ∩Vr = ∅) such that
there are no edges within Vl and Vr (i.e., for all {i, j} ∈E, [i ∈Vl and j ∈Vr] or [j ∈Vl
and i ∈Vr]). Assume G = (V, E) is a bipartite graph. Show that ADMM directly applied
to
minimize
{xi}i∈Vl , {yj}j∈Vr
X
i∈Vl
fi(xi) +
X
j∈Vr
fj(yj)
subject to
xi = yj
∀{i, j} ∈E
(without introducing any new variables) is
xk+1
i
= argmin
xi∈Rp


fi(xi) +
X
j∈Ni

⟨uk
{i,j}, xi −yk
j ⟩+ α
2 ∥xi −yk
j ∥2



∀i ∈V
yk+1
i
= argmin
yi∈Rp


fj(yj) +
X
i∈Nj

⟨uk
{i,j}, xk+1
i
−yj⟩+ α
2 ∥xk+1
i
−yj∥2



∀i ∈V
uk+1
e
= uk
e + α(xk+1
i
−yk+1
j
)
∀e = {i, j} ∈E.
Show that if fj = 0 for all j ∈Vr, then the method further simplifies to
xk+1
i
= Prox(α|Ni|)−1fi(vk
i )
ak+1
j
=
1
|Nj|
X
i∈Nj
xk+1
j
vk+1
i
= vk
i +
1
|Ni|
X
j∈Ni
(2ak+1
j
−ak
j ) −xk+1
i
for all i ∈V .
Remark. Since ADMM updates the two blocks separately, the absence of edges within the
partitions Vl and Vr leads to separable (in the sense of Example 5.2) ADMM subproblems.
In fact, the formulations of (11.3) and Exercise 11.12 can be understood as constructing
a bipartite graph and then applying ADMM: For each edge {i, j} ∈E, introduce a new
node k and replace {i, j} with {i, k} and {k, j} (this operation is called the subdivision
of an edge in graph theory) and place the original nodes in Vl and the new nodes (the
y-nodes) in Vr.
11.14 Let W ∈Rn×n. Consider the iteration
xk+1 = Wxk
for k = 0, 1, . . . . Then xk →x⋆holds for all starting points x0 = stack(x0
1, . . . , x0
n), where
x⋆= (1/n)(x0
1 + · · · + x0
n) and x⋆= stack(x⋆, . . . , x⋆), if and only if


## Page 266

Exercises
251
(i) W1 = 1,
(ii) 1⊺W = 1⊺,
(iii) 1 = λ1(W) > |λ2(W)| ≥· · · ≥|λn(W)|.
For the sake of simplicity, assume W is diagonalizable i.e, assume there exists a decom-
position W = V ΛV −1, where Λ ∈Cn×n is a diagonal matrix with diagonal components
λ1, . . . , λn and V ∈Cn×n is invertible. (The Jordan canonical form can be used to prove
the result without diagonalizability.)
Hint. If we let vi be the ith column of V and u⊺
i be the ith row of V −1, then vi is an
eigenvector of W corresponding to λi, ui is an eigenvector of W ⊺corresponding to λi,
and
W k =
n
X
i=1
λk
i viu⊺
i .
11.15 Equivalence of consensus conditions. Consider x = stack(x1, . . . , xn) ∈Rn×p as in (11.5)
and a mixing matrix satisfying W1 = 1 and N(I −W) = span(1). Write λ1, . . . , λn to
denote the eigenvalues of W. Show that the following conditions are equivalent:
(i) x1 = · · · = xn.
(ii) (I −W)x = 0.
(iii) ∥x∥I−W = 0, provided that W = W ⊺and 1 = λ1 > λ2 ≥· · · ≥λn.
(iv) (W −1 −I)x = 0, provided that W is invertible.
(v) ∥x∥W −1−I = 0, provided that W = W ⊺and 1 = λ1 > λ2 ≥· · · ≥λn > 0.
(vi) Ux = 0, provided that W = W ⊺, 1 = λ1 > λ2 ≥· · · ≥λn, and U = U ⊺, and
U 2 = I −W.
11.16 Mixing matrices with negative entries. Let W ∈Rn×n and consider the decentralized
averaging method
xk+1 = Wxk.
Since
∥xk −x⋆∥∼(ρ(W −11⊺/n))k ∥x0 −x⋆∥,
(11.13)
where 1 ∈Rn is the vector with all entries 1 and ρ denotes the spectral radius, we interpret
ρ(W −11⊺/n) as the asymptotic convergence rate. Next, consider a graph G = (V, E)
and assume W is decentralized with respect to G. Consider the problem of finding a
decentralized mixing matrix with the fastest asymptotic convergence rate:
minimize
W ∈Rn×n
ρ(W −11⊺/n)
subject to
1⊺W = 1⊺W, W1 = 1
Wij = 0, {i, j} /∈E, i̸ = j.
However, optimizing the spectral radius of asymmetric matrices is a difficult problem. So,
we further assume W is symmetric:
minimize
W ∈Rn×n
σmax(W −11⊺/n)
subject to
W = W ⊺, W1 = 1
Wij = 0, {i, j} /∈E, i̸ = j,
where σmax denotes the maximum singular value. This problem is equivalent to
minimize
s∈R, W ∈Rn×n
s
subject to
−sI ⪯W −11⊺/n ⪯sI
W = W ⊺, W1 = 1
Wij = 0, {i, j} /∈E, i̸ = j,
where ⪯denotes the partial order in the sense of positive semidefinite matrices.


## Page 267

252
11
Distributed and decentralized optimization
−0.1
0.2
−0.1
0.2
0.2
0.2
0.2
0.2
0.2
0.4
0.4
0.2
−0.1
0.2
0.2
0.2
0.2
0.2
0.2
0.2
0.2
0.2
0.2
0.2
0.2
Figure 11.3: A small graph with 8 nodes and 17 edges. Each edge and node is
labeled with the optimal symmetric weights, which give the minimum asymptotic
convergence factor.
(a) Show (11.13).
(b) Numerically solve the problem instance depicted in Figure 11.3 and establish that
the depicted solution is indeed optimal. (The solution is not unique.)
(c) The optimal mixing matrix of part (b) contains negative weights. Show that the
negative weights are necessary to obtain the optimal mixing matrix by solving the
optimization problem with the added constraint Wij ≥0 for all i, j ∈{1, . . . , n}.
Remark. For optimization problems with somewhat complicated constraints, such as this
one, it is often simpler to solve small problem instances with libraries such as CVX,
CVXPY, or YALMIP. For large problem instances, it becomes necessary to use efficient
splitting methods.
Remark.
The approach of formulating the problem of finding the optimal symmetric
mixing matrix and the particular example of Figure 11.3 was first presented by Xiao and
Boyd [XB04].
11.17 General form of PG-EXTRA. Consider two symmetric mixing matrices W, f
W ∈Rn×n
satisfying
W ⪯f
W ⪯1
2(W + I),
N(f
W −W) = N(I −W) = span(1).
The choice f
W = 1
2(W + I) is most common. Since f
W −W ⪰0, there exists a symmetric
U ∈Rn×n such that U 2 = f
W −W, and U satisfies N(U) = span(1).
(a) Show that
minimize
x∈Rn×p
f(x) + h(x) +
1
2α∥x∥2
I−f
W
subject to
Ux = 0.
is equivalent to problem (11.11) and that this primal problem is generated by the
Lagrangian L(x, u) = f(x) + h(x) +
1
2α∥x∥2
I−f
W + ⟨u, Ux⟩.


## Page 268

Exercises
253
(b) Let
M =
α−1I
−1
2U
−1
2U
αI

.
Find a decomposition ∂L = 픽+ ℍsuch the the FPI with (M + 픽)−1(M −ℍ) is
xk+1 = Proxαf
 f
Wxk −α∇h(xk) −αUuk
uk+1 = uk + α−1Uxk+1,
where w0 = 0.
(c) Show that the previous method with the initialization u0 = α−1Ux0 and arbitrary
x0 is equivalent to
xk+1 = Proxαf

Wxk −α∇h(xk) −wk
wk+1 = wk + (f
W −W)xk.
This method is called the general form of PG-EXTRA.
(Hint: substitute wk = Pk−1
j=0(f
W −W)xj and use U 2 = f
W −W.)
11.18 Consensus tracking in a network.
Consider a mixing matrix W ∈Rn×n satisfying
(11.7a)–(11.7c), and let y0, y1, . . . ∈Rn×p be a given sequence.
We call z0, z1, . . . a
consensus tracking sequence of y0, y1, . . . if z0 = y0 and
zk+1 = Wzk + yk+1 −yk
for k = 0, 1, . . . . Define yk = stack(yk
1, . . . , yk
n) and zk = stack(zk
1, . . . , zk
n). Show that
(a)
1
n
Pn
i=1 zk
i = 1
n
Pn
i=1 yk
i , and
(b) if limk→∞yk = stack(y⋆
1, . . . , y⋆
n), then limk→∞zk = stack(¯y⋆, . . . , ¯y⋆), where ¯y⋆=
1
n
Pn
i=1 y⋆
i .
Remark. The idea is that zk “tracks” the mean
1
n
P
j∈V yk
j and is in consensus in the
limit as k →∞. To clarify, limk→∞yk is not necessarily in consensus.
11.19 DIGing. Consider a mixing matrix W ∈Rn×n satisfying (11.7a)–(11.7c) and the problem
minimize
x∈Rn×p
h(x)
subject to
(I −W)x = 0,
where h is differentiable. The method
xk+1 = Wxk −αzk
zk+1 = Wzk + ∇h(xk+1) −∇h(xk),
where x0 is initialized to be in consensus and z0 = ∇h(x0), is called Distributed Inexact
Gradient method and a gradient tracking (DIGing). The xk+1 update is similar to that
of DGD but has α∇h(xk) replaced by zk. The zk iterates track the average gradient
1
n
Pn
i=1 ∇hi(xk
i ) in the sense of Exercise 11.18. Show that DIGing is a special case of
generalized PG-EXTRA of Exercise 11.17 with f = 0, W = 2W −I, and f
W = WW.
Remark. DIGing was introduced by Nedic, Olshevsky, and Shi [NOS17] for time-varying
graphs, i.e., W is not fixed but changes with k. In this problem, we derive DIGing with
a fixed W as an instance of PG-EXTRA.


## Page 269

254
11
Distributed and decentralized optimization
11.20 Local stepsizes of NIDS. Consider a symmetric mixing matrix W = W ⊺∈Rn×n satisfying
N(I −W) = span(1) and 1 = λ1 > max {λ2, . . . , λn}. Let U ∈Rn×n be a symmetric
matrix satisfying U 2 = 1
2(I −W). Consider
minimize
x∈Rn×p
f(x) + h(x) + δ{0}(Ux),
where the notation f(x) and h(x) is as defined for the NIDS setup. We assume f1, . . . , fn
and h1, . . . , hn are CCP, but each hi is Li-smooth for i = 1, . . . , n. Let us derive a variant
of NIDS that allows each agent i to utilize its individual stepsize αi < 2/Li.
Let γi =
p
2/Li for i = 1, . . . , n, and define
Γ = diag(γ1, . . . , γn) =


γ1
...
γn

.
Define ¯x ∈Rn×p with x = Γ¯x. Define ¯f(¯x) = f(Γ¯x), ¯h(¯x) = h(Γ¯x), and U = UΓ.
(a) Show that ¯h is 2-smooth.
(b) Show that applying PD3O to the equivalent formulation
minimize
¯x∈Rn×p
¯f(¯x) + ¯h(¯x) + δ{0}(U ¯x)
yields the iteration
xk+1 = ProxF (zk)
zk+1 = zk −xk+1 + M

2xk+1 −xk + diag(α1, . . . , αn)

∇h(xk) −∇h(xk+1)

,
where αi = αγ2
i for i = 1, . . . , n,
F(x) =
n
X
i=1
αifi(xi),
and M = I −β
2 diag(α1, . . . , αn)(I −W).
(c) Show that the iteration converges if αi ∈(0, 2/Li) for i = 1, . . . , n and α1, . . . , αn, β >
0 satisfy
λmax
β
2 diag(√α1, . . . , √αn)(I −W)diag(√α1, . . . , √αn)

≤1.
Remark. This version of NIDS was also presented in Li, Shi, and Yan’s original NIDS
paper [LSY19].


## Page 270

Chapter 12
Acceleration
Theorem 1 establishes an O(1/k) rate on the squared norm of the fixed-point
residual, and a similar O(1/k) rate can be established for the setups of Theorems 2,
3, and 6. It is natural to ask whether this rate can be improved. The answer is
yes, at least in the worst-case rate.
In optimization, an acceleration is a modification of a base method that im-
proves the convergence rate, and an improvement from O(1/k) to O(1/k2) is most
common for first-order algorithms. Acceleration is an active topic of research. In
this chapter, we keep the discussion minimal and discuss Nesterov’s AGM, which
is the most well known, and APPM/OHM, which is most relevant to this book’s
content.
12.1
Accelerated gradient method
Consider the problem
minimize
x∈Rn
f(x),
where f is convex and L-smooth. The method
xk+1 = yk −1
L∇f(yk)
yk+1 = xk+1 + k −1
k + 2(xk+1 −xk),
where x0 = y0, is called Nesterov’s accelerated gradient method (AGM).


## Page 271

256
12
Acceleration
Theorem 17 Assume the convex, L-smooth function f has a minimizer x⋆. Then
AGM converges with the rate
f(xk) −f(x⋆) ≤2L∥x0 −x⋆∥2
k2
for k = 1, 2, . . . .
We can equivalently write AGM as
xk+1 = yk −1
L∇f(yk)
zk+1 = zk −k + 1
2L ∇f(yk)
yk+1 =

1 −
2
k + 2

xk+1 +
2
k + 2zk+1,
where x0 = y0 = z0; the two forms are equivalent in the sense that the generated
xk- and yk-sequences are the same. See Exercise 12.1.
Proof of Theorem 17. We first make some preliminary observations. Define
θk = k + 1
2
for k = −1, 0, 1, . . . . It is straightforward to verify
θ2
k −θk ≤θ2
k−1
(12.1)
for k = 0, 1, . . . . We will use the inequalities
f(xk+1) −f(yk) + 1
2L∥∇f(yk)∥2 ≤0
(12.2)
f(yk) −f(xk) ≤⟨∇f(yk), yk −xk⟩
(12.3)
f(yk) −f(x⋆) ≤⟨∇f(yk), yk −x⋆⟩.
(12.4)
The first, (12.2), follows from L-smoothness, which implies f(x) −L
2 ∥x −yk∥2 is
concave as a function of x, which in turn implies
f(x) −L
2 ∥x −yk∥2 ≤f(yk) + ⟨∇f(yk), x −yk⟩.
We plug in x = xk+1 = yk −1
L∇f(yk) to get (12.2).
The second and third
inequalities, (12.3) and (12.4), follow from convexity of f.
Define
V k = θ2
k−1
 f(xk) −f(x⋆)

+ L
2 ∥zk −x⋆∥2,


## Page 272

12.1
Accelerated gradient method
257
where zk is as defined in the equivalent formulation of AGM. Then
V k+1 −V k
= θ2
k

f(xk+1) −f(x⋆) + 1
2L∥∇f(yk)∥2

−θ2
k−1(f(xk) −f(x⋆))
−θk⟨∇f(yk), zk −x⋆⟩
≤θ2
k
 f(yk) −f(x⋆)

−θ2
k−1(f(xk) −f(x⋆)) −θk⟨∇f(yk), zk −x⋆⟩
= (θ2
k −θk)(f(yk) −f(xk)) + θk(f(yk) −f(xk)) + (θ2
k −θ2
k−1)(f(xk) −f(x⋆))
−θk⟨∇f(yk), zk −x⋆⟩
≤(θ2
k −θk)(f(yk) −f(xk)) + θk(f(yk) −f(x⋆)) −θk⟨∇f(yk), zk −x⋆⟩
≤(θ2
k −θk)⟨∇f(yk), yk −xk⟩+ θk⟨∇f(yk), yk −x⋆⟩−θk⟨∇f(yk), zk −x⋆⟩
= θk⟨∇f(yk), (1 −θk)xk + θkyk −zk⟩= 0,
where the first equality follows from
L
2
zk −x⋆−θk
L ∇f(yk)

2
−L
2 ∥zk −x⋆∥2 = −θk⟨∇f(yk), zk −x⋆⟩+ θ2
k
2L∥∇f(yk)∥2,
the first inequality follows from (12.2), the second inequality follows from (12.1),
the third inequality follows from (12.3) and (12.4), and the final equality follows
from the definition of zk. This establishes V k ≤V k−1 ≤· · · ≤V 0, and V k ≤V 0
implies
f(xk) −f(x⋆) ≤
L
2θ2
k−1
∥z0 −x⋆∥2 = 2L
k2 ∥z0 −x⋆∥2.
Comparison with gradient descent.
Gradient descent (GD) with stepsize α =
1/L
xk+1 = xk −1
L∇f(xk)
converges in function value at the slower rate O(1/k). To see this, define
V k = k(f(xk) −f(x⋆)) + L
2 ∥xk −x⋆∥2
and note
V k+1 −V k
= (k + 1)(f(xk+1) −f(xk)) + f(xk) −f(x⋆) + L
2
 1
L2 ∥∇f(xk)∥2 −2
L⟨∇f(xk), xk −x⋆⟩

≤−k + 1
2L ∥∇f(xk)∥2 + ⟨∇f(xk), xk −x⋆⟩+ 1
2L∥∇f(xk)∥2 −⟨∇f(xk), xk −x⋆⟩
= −k
2L∥∇f(xk)∥2 ≤0,
where the inequality follows from analogues of (12.2) and (12.4). V k ≤V 0 implies
f(xk) −f(x⋆) ≤L
2k ∥x0 −x⋆∥2 −L
2k ∥xk −x⋆∥2 ≤L
2k ∥x0 −x⋆∥2.


## Page 273

258
12
Acceleration
Constructing the Lyapunov function.
The nonincreasing quantity V k in the proof
of AGM and GD (and later in APPM) is called a Lyapunov function, energy func-
tion, or potential function, and the style of proof relying on such quantities is called
a Lyapunov analysis. Not all convergence proofs in optimization use a Lyapunov
function, but the ones that do tend to be more concise. Constructing a Lyapunov
function is a highly nontrivial art, and we briefly outline the process for GD and
AGM.
Imagine analyzing GD, and we suspect the convergence rate is f(xk) −f(x⋆) =
O(1/k). We define W k = k(f(xk) −f(x⋆)) and, through some analysis, find
W k+1 −W k ≤L
2 ∥xk −x⋆∥2 −L
2 ∥xk+1 −x⋆∥2.
So we define V k = k(f(xk)−f(x⋆))+ L
2 ∥xk−x⋆∥2 and present a Lyapunov analysis.
Encouraged by this success, one may try to prove a faster rate for GD by
defining W k = t2
k(f(xk) −f(x⋆)) with a yet unspecified tk-sequence and analyzing
W k+1 −W k. If the tk-sequence has a growth rate on the order of k, perhaps we can
establish an O(1/k2) rate. However, such an effort does not lead to a rate faster
than O(1/k) for GD.
For AGM, we again define W k = t2
k−1(f(xk)−f(x⋆)) and analyze W k+1 −W k.
With an analysis similar to what we have seen, we get
W k+1 −W k ≤L
2 ∥zk −x⋆∥2 −L
2 ∥zk+1 −x⋆∥2.
for t2
k−tk ≤t2
k−1 and tk ≥0. An admissible sequence is tk = (k+1)/2. So we define
V k = t2
k(f(xk)−f(x⋆))+ L
2 ∥zk −x⋆∥2 and present a Lyapunov analysis. Instead of
k/2, we can let t0 = 1 and define t1, t2, . . . successively by t2
k+1 −tk+1 = t2
k, which
gives a slightly better rate (cf. see Exercise 12.3).
12.2
Accelerated proximal point and optimized Halpern method
Consider the problem
find
x∈Rn
0 ∈픸x,
where 픸is maximal monotone. The method
yk+1 = 핁픸xk
xk+1 = yk+1 +
k
k + 2(yk+1 −yk) −
k
k + 2(yk −xk−1),
where y0 = x0, is called the accelerated proximal point method (APPM).
Also consider the problem
find
x∈Rn
x = 핋x,


## Page 274

12.2
Accelerated proximal point and optimized Halpern method
259
where 핋: Rn →Rn is nonexpansive. We call
xk+1 =
1
k + 2x0 + k + 1
k + 2핋xk
the optimized Halpern method (OHM).
With 핋= ℝ픸, the two problems of finding elements of Zer 픸and Fix 핋are
equivalent (cf. Exercise 10.2), and the two methods APPM and OHM are equivalent
in the sense that the generated xk- sequences are the same. (See Exercise 12.2).
Theorem 18 Assume the maximal monotone operator 픸has a zero x⋆.
Then
APPM/OHM converges with the rate
∥xk−1 −핁픸xk−1∥2 ≤∥x0 −x⋆∥2
k2
for k = 1, 2, . . . .
Note that we can equivalently state this result as
∥핋xk−1 −xk−1∥2 ≤4∥x0 −x⋆∥2
k2
.
Proof. Define ˜픸yk = xk−1 −yk, which implies ˜픸yk ∈픸yk. Define
V k = k2∥˜픸yk∥2 + k⟨˜픸yk, yk −x0⟩+ 1
2∥x0 −x⋆∥2
= k2
2 ∥˜픸yk∥2 + k⟨˜픸yk, yk −x⋆⟩+ 1
2∥k ˜픸yk −(x0 −x⋆)∥2
for k = 0, 1, . . . . Note that ⟨˜픸yk, yk −x⋆⟩≥0 by monotonicity of 픸, so V k ≥0
for k = 0, 1, . . . . From the equivalent OHM form, we have
yk+1+ ˜픸yk+1 = xk =
1
k + 1x0+
k
k + 1(2핁픸−핀)xk−1 =
k
k + 1(2yk−(yk+ ˜픸yk))+
1
k + 1x0,
which we reorganized into
(k + 1) ˜픸yk+1 + (k + 1)(yk+1 −x0) + k ˜픸yk −k(yk −x0) = 0.
Then
V k+1 −V k
= (k + 1)2∥˜픸yk+1∥2 + (k + 1)⟨˜픸yk+1, yk+1 −x0⟩−k2∥˜픸yk∥2 −k⟨˜픸yk, yk −x0⟩
= ⟨(k + 1) ˜픸yk+1, (k + 1) ˜픸yk+1 + (yk+1 −x0)
|
{z
}
=−k(yk+1−x0)+k(yk−x0)−k ˜픸yk
⟩−⟨k ˜픸yk,
k ˜픸yk + (yk −x0)
|
{z
}
=(k+1)(yk−x0)−(k+1)(yk+1−x0)−(k+1)˜픸yk+1
⟩
= k(k + 1)⟨˜픸yk+1, yk −yk+1 −˜픸yk⟩−k(k + 1)⟨˜픸yk, yk −yk+1 −˜픸yk+1⟩
= −k(k + 1)⟨˜픸yk+1 −˜픸yk, yk+1 −yk⟩≤0,
where the final inequality follows from monotonicity of 픸. Finally, we conclude
that
k2
2 ∥˜픸yk∥2 ≤V k ≤V 0 = 1
2∥x0 −x⋆∥2.


## Page 275

260
12
Acceleration
12.3
When does an acceleration accelerate?
In optimization (and more generally in applied mathematics and computer science),
convergence rates are usually established in the worst case, and the convergence
observed in practice can be faster than this guarantee if the given problem instance
does not represent the worst case. If an unaccelerated method actually converges
at an O(1/k) rate, then an O(1/k2) acceleration will accelerate the convergence.
However, if the observed convergence is already faster than O(1/k2), the guarantee
of the accelerated method, then the acceleration does not guarantee a speedup and
may even slow down the convergence. See Exercise 12.9.
In practice, an acceleration is a technique that sometimes provides a speedup.
When an “accelerated” variant of a method is available, one should try it out with
the expectation that it may improve or worsen the convergence.


## Page 276

Bibliographical Notes
261
Bibliographical Notes
Nesterov’s accelerated gradient method was first presented in 1983 [Nes83]. Since then,
there has been a large body of work studying accelerated first-order methods in optimiza-
tion.
The accelerated O(1/k2) rate on the squared fixed-point residual for the problem of finding
fixed points of nonexpansive mappings was first established by Sabach and Shtern in 2017
[SS17]. The “accelerated proximal point method” of this chapter has a better constant for
the rate O(1/k2) and was independently discovered by Lieder [Lie21] and Kim [Kim21].
Specifically, the classical Halpern method [Hal67] has the form
xk+1 = λkx0 + (1 −λk)핋xk,
and Lieder showed that the specific choice of λk = 1/(k + 2) produces the stated O(1/k2)
rate.
Kim used the computer-assisted tool “performance estimation problem” [DT14,
KF16, THG17, RTBG20] to generate the accelerated proximal point method as the
method with the best theoretical guarantee among a certain class of methods.
Nesterov’s original 1983 paper used a Lyapunov analysis [Nes83], but this proof is some-
what forgotten as Nesterov used a different “estimate sequence” technique in his later work
[Nes88] for analyzing and constructing accelerated gradient methods. Tseng provided a
unified Lyapunov analysis for a variety of accelerated methods [Tse08]. The particular
Lyapunov analyses presented in this chapter were inspired by Bansal and Gupta [BG19]
and Taylor and Bach [TB19].
In this chapter, we cover Nesterov’s AGM, which is most well known, and APPM/OHM,
which is most relevant to the content of this book. However, there are many other acceler-
ations considered in the optimization literature: acceleration of the proximal point method
applied to functions by Güler [Gül92], Chambolle–Pock and Davis–Yin accelerations ap-
plied to PDHG and DYS [CP11a, DY17b], generalization of Nesterov’s acceleration to
problems involving a closed convex set or a proximable function by Nesterov [Nes04, §2.2.3
and 2.2.4] and [Nes13] and by Beck and Teboulle [BT09], a different type of acceleration by
Nesterov applied to structured convex-concave optimization problems [Nes05], Auslender
and Teboulle’s generalization of Nesterov’s acceleration to the setup of Bregman diver-
gences [AT06], Anderson acceleration applied to fixed-point iterations [And65, WN11],
geometric descent as an alternative to Nesterov’s acceleration by Bubeck, Lee, and Singh
[BLS15], optimized gradient method as an improvement upon Nesterov’s AGM by Drori,
Teboulle, Kim, and Fessler [DT14, KF16, KF17], triple momemtum method as an im-
provement upon Nesterov’s AGM in the strongly convex setup by Van Scoy, Freeman,
and Lynch [VSFL18], catalyst acceleration as a meta-algorithm for accelerating unac-
celerated methods by Lin, Mairal, and Harchaoui [LMH15, LMH18], and OGM-G for
accelerating the reduction of the gradient magnitude by Kim and Fessler [KF21]. For the
problem of minimizing smooth convex functions, one can establish a O(1/k4) rate on the
squared gradient magnitude [NGGD20, Remark 2.1], which is significantly faster than the
O(1/k2) rate of APPM/OHM.


## Page 277

262
12
Acceleration
Exercises
12.1 Show that the two forms of Nesterov AGM are equivalent.
12.2 Show that APPM and OHM are equivalent with 핋= 2핁픸−핀.
12.3 AGM with optimal parameters. Consider the problem
minimize
x∈Rn
f(x),
where f is a convex, L-smooth function with a minimizer. Show that the method
ϕk+1 = 1 +
p
1 + 4ϕ2
k
2
xk+1 = yk −1
L∇f(yk)
yk+1 = xk+1 + ϕk −1
ϕk+1 (xk+1 −xk),
where k = 0, 1, . . . , x0 = y0, and ϕ0 = 1, converges with the rate
f(xk) −f(x⋆) ≤L∥x0 −x⋆∥2
2ϕ2
k−1
,
where ϕk−1 ≥k+1
2 . This method is also called Nesterov’s accelerated gradient method.
Show that the rate of this variant is slightly better than the rate shown in §12.1.
Hint. Use
V k = ϕ2
k−1

f(xk) −f(x⋆)

+ L
2 ∥zk −x⋆∥2.
12.4 Backtracking linesearch. Suppose the smoothness constant L > 0 exists but is not known.
Consider the method
xk+1 = yk −
1
2iLk ∇f(xk),
try i = 0, 1, . . . until f(xk+1) −f(yk) +
1
2iLk ∥∇f(xk)∥2 ≤0
Lk+1 = 2 · 2iLk
yk+1 = xk+1 + k −1
k + 2(xk+1 −xk),
where x0 = y0 ∈Rn and L0 is an estimate of L. Show that if L0 ≤L, then
f(xk) −f(x⋆) ≤4L∥x0 −x⋆∥2
k2
.
Hint. The Lk = 2iLk−1 step represents a doubling of the estimate of L. This doubling
happens finitely many times.
12.5 Accelerated proximal gradient (FISTA). Consider the problem
minimize
x∈Rn
f(x) + g(x),
where f is convex and L-smooth and g is CCP. Assume f + g has a minimizer. Consider
the method
xk+1 = Prox 1
L g(yk −1
L∇f(yk))
yk+1 = xk+1 + k −1
k + 2(xk+1 −xk),


## Page 278

Exercises
263
where x0 = y0, is called the accelerated proximal gradient method and was proposed by
Nesterov in 2004 [Nes04, §2.2.3 and 2.2.4] and Beck and Teboulle in 2009 [BT09]. The
instance where g(x) = ∥x∥1 is more commonly known as the fast iterative shrinkage-
thresholding algorithm (FISTA).
Show
f(xk) + g(xk) −f(x⋆) −g(x⋆) ≤2∥x0 −x⋆∥2
α(k + 1)2 .
Hint. Use
V k = θ2
k−1

f(xk) + g(xk) −f(x⋆) −g(x⋆)

+ L
2 ∥zk −x⋆∥2.
12.6 Strongly-convex accelerated gradient method. Consider the problem
minimize
x∈Rn
f(x),
where f is µ-strongly convex and L-smooth. The method
xk+1 = yk −1
L∇f(yk)
yk+1 = xk+1 +
√κ −1
√κ + 1(xk+1 −xk),
where k = 0, 1, . . . , x0 = y0, and κ = L/µ, is called the strongly convex accelerated
gradient method (SC-AGM). Show
f(xk) −f(x⋆) ≤µ + L
2
∥x0 −x⋆∥2e−k/√κ.
Hint. Use
V k =

1 +
1
√κ −1
k 
f(xk) −f(x⋆) + µ
2 ∥zk −x⋆∥2
,
where zk = (1 + √κ)yk −√κxk.
Remark. The (unaccelerated) gradient method applied to this problem setup converges
with the slower rate O(e−k/κ). See Exercise 13.5.
12.7 Squared gradient norm of gradient descent. Consider the problem
minimize
x∈Rn
f(x),
where f is a convex, L-smooth function with a minimizer. Show that for GD
xk+1 = xk −1
L∇f(xk)
the quantity
V k = (2k + 1)L(f(xk) −f(x⋆)) + k(k + 2)∥∇f(xk)∥2 + L2∥xk −x⋆∥2
is nonincreasing for k = 0, 1, . . . .
Remark. This result implies the rate ∥∇f(xk)∥2 ≤
L
k(k+2)(L∥x0 −x⋆∥2 + f(x0) −f(x⋆)),
which is on the same order as APPM. So when the the goal is to reduce the magnitude of
the gradient of an L-smooth convex function, GD and APPM have the same rate. This
result is due to Taylor and Bach [TB19].


## Page 279

264
12
Acceleration
12.8 Gradient descent stepsize. Consider the problem
minimize
x∈Rn
f(x),
where f is a convex, L-smooth function with a minimizer. Show that gradient descent
with stepsize α
xk+1 = xk −α∇f(xk)
converges in function value at rate O(1/k) for α ∈(0, 2/L).
12.9 Acceleration can slow you down. Consider the specific problem instance
minimize
x∈R3
x2
1 + 2x2
2 + 3x2
3.
Apply gradient descent, AGM, and SC-AGM of Exercise 12.6. Experimentally, what are
the convergence rates on the objective value?
Also apply the proximal point method
and APPM. Experimentally, what are the convergence rates on the squared fixed-point
residual?
12.10 APPM/OHM for finding zeros of cocoercive operators. Consider the problem
find
x∈Rn
0 ∈픸x,
where 픸: Rn →Rn is β-cocoercive with β > 0. Show that method
xk+1 =
1
k + 2x0 + k + 1
k + 2(핀−2β픸)xk
converges with the rate
∥픸xk∥2 ≤∥x0 −x⋆∥2
β2(k + 1)2
for k = 0, 1, . . . . Also show that this method is equivalent to
yk+1 = (핀−β픸)xk
xk+1 = yk+1 +
k
k + 2(yk+1 −yk) −
k
k + 2(yk −xk−1),
for k = 0, 1, . . . .
Hint. Show that 핀−2β픸is nonexpansive and use Theorem 18.


## Page 280

Chapter 13
Scaled relative graphs
In this chapter, we present a new notion called the scaled relative graph (SRG).
The SRG provides a correspondence between algebraic operations on nonlinear op-
erators and geometric operations on subsets of the 2D plane. We can think of the
SRG as a signature of an operator analogous to how eigenvalues are a signature of
a matrix. Using this machinery and elementary Euclidean geometry, we establish
averagedness and contractiveness of certain operators and thereby establish conver-
gence of corresponding fixed-point iterations. The geometric arguments constitute
rigorous proofs and are not mere illustrations.
The geometric approach of this chapter contrasts with the analytical proofs
based on inequalities, which are more common in the splitting methods literature.
We make clear that the geometric proof techniques based on the SRG are meant
to supplement, rather than replace the analytical techniques.
13.1
Basic definitions
Operator classes.
We say A is a class of operators if A is a set of operators on
Rn for all n ∈N. Note that 픸1, 픸2 ∈A need not be defined on the same Euclidean
spaces, i.e., 픸1 : Rn ⇒Rn, 픸2 : Rm ⇒Rm, and n̸ = m is possible.
Given classes of operators A and B and α > 0, write
A + B = {픸+ 픹| 픸∈A, 픹∈B, 픸: Rn ⇒Rn, 픹: Rn ⇒Rn}
AB = {픸픹| 픸∈A, 픹∈B, 픸: Rn ⇒Rn, 픹: Rn ⇒Rn}
핁αA = {핁α픸| 픸∈A, 픸: Rn ⇒Rn}
ℝαA = 2핁αA −핀= {2핁−핀| 핁∈핁αA, 핁: Rn ⇒Rn, 핀: Rn ⇒Rn}
To clarify, these definitions require that 픸and 픹are operators on the same Eu-
clidean space Rn (so n is shared), as otherwise the operations would not make
sense. Also define
A−1 = {픸−1 | 픸∈A},
αA = {α픸| 픸∈A}.


## Page 281

266
13
Scaled relative graphs
For L ∈(0, ∞), define the class of L-Lipschitz operators as
LL =

픸: dom 픸→Rn | ∥픸x −픸y∥2 ≤L2∥x −y∥2, ∀x, y ∈dom 픸⊆Rn, n ∈N
	
.
For β ∈(0, ∞), define the class of β-cocoercive operators as
Cβ =

픸: dom 픸→Rn | ⟨픸x −픸y, x −y⟩≥β∥픸x −픸y∥2, ∀x, y ∈dom 픸⊆Rn, n ∈N
	
.
Define the class of monotone operators as
M =

픸: Rn ⇒Rn | ⟨픸x −픸y, x −y⟩≥0, ∀x, y ∈dom 픸, n ∈N
	
.
For µ ∈(0, ∞), define the class of µ-strongly monotone operators as
Mµ =

픸: Rn ⇒Rn | ⟨픸x −픸y, x −y⟩≥µ∥x −y∥2, ∀x, y ∈dom 픸, n ∈N}.
For θ ∈(0, 1), define the class of θ-averaged operators as
Nθ = (1 −θ)핀+ θL1.
In these definitions, we do not impose any requirements on the domain or maxi-
mality of the operators. We define these classes to include operators on Rn for all
n ∈N in order to avoid discussing issues specific to the cases n = 1 and n = 2.
Write Fµ,L, F0,L, Fµ,∞, and F0,∞for the sets of CCP functions on Rn for all
n ∈N that are respectively µ-strongly convex and L-smooth, convex and L-smooth,
µ-strongly convex, and convex, for 0 < µ < L < ∞. Write
∂Fµ,L = {∂f | f ∈Fµ,L},
where 0 ≤µ < L ≤∞.
Basic geometry.
For any a, b ∈Rn, let
∠(a, b) =
(
arccos

⟨a,b⟩
∥a∥∥b∥

if a̸ = 0, b̸ = 0
0
otherwise
denote the angle between them. The spherical triangle inequality states that any
nonzero a, b, c ∈Rn satisfies
|∠(a, b) −∠(b, c)| ≤∠(a, c) ≤∠(a, b) + ∠(b, c).
Figure 13.1 illustrates the inequality. We use the spherical triangle inequality in
Theorem 26 to argue that there is no need to consider a third dimension and that
we can continue the analysis in 2D.
The Stewart’s theorem states that for a triangle △ABC and Cevian CD to the
side AB,
A
B
C
D
the lengths of the line segments satisfy
AD · CB
2 + DB · AC
2 = AB · CD
2 + AD · DB
2 + AD
2 · DB.


## Page 282

13.1
Basic definitions
267
Figure 13.1: Spherical triangle inequality: |θ −ϕ| ≤ψ ≤θ + ϕ.
Extended complex plane and inversive geometry.
We use the extended complex
plane C = C ∪{∞} to represent the 2D plane and the point at infinity. Since
complex numbers compactly represent rotations and scaling, this choice simplifies
our notation compared to using R2 ∪{∞}. We avoid the operations ∞+ ∞, 0/0,
∞/∞, and 0 · ∞. Otherwise, we adopt the convention of z + ∞= ∞, z/∞= 0,
z/0 = ∞, and z · ∞= ∞.
We call z 7→¯z−1, a one-to-one map from C to C, the inversion map. To clarify,
¯z denotes the complex conjugate of z. In polar form, it is reiϕ 7→(1/r)eiϕ for
0 ≤r ≤∞, i.e., inversion preserves the angle and inverts the magnitude.
Generalized circles consist of (finite) circles and lines with {∞}. The interpreta-
tion is that a line is a circle with infinite radius. Inversion maps generalized circles
to generalized circles, and we can perform it with the following semi-geometric
procedure.
1. Draw a line L through the origin orthogonally intersecting the generalized
circle. This means L intersects the boundary perpendicularly, which implies
L goes through the circle’s center when the generalized circle is finite.
2. Let −∞< x < y ≤∞represent the signed distance of the intersecting points
from the origin along this line. If the generalized circle is a line, then y = ∞.
3. Draw a generalized circle orthogonally intersecting L at (1/x) and (1/y).
4. When inverting a region with a generalized circle as the boundary, pick a
point on L within the interior of the region to determine on which side of the
boundary the inverted interior lies.
Examples 13.1 and 13.2 illustrate these steps.
Example 13.1 Illustration of inverting a disk. In step 1, we choose L to be the x-axis
(although any line through the origin works). In steps 2 and 3, we identify x and y,
invert them to x−1 and y−1, and draw the generalized circle in the inverted plane
to be the new boundary. In step 4, we determine that the interior of the disk is


## Page 283

268
13
Scaled relative graphs
mapped to the exterior by noting that 1, a point invariant under the inversion map,
is excluded in the original region and therefore is excluded in the inverted region.
L
y
x
1
L
1
y−1
x−1
∪{∞}
Example 13.2 The three vertical pairs illustrate inversion. In step 1, we choose L
to be the x-axis. In step 4 we determine the interior by examining point 1: if 1 is
included in the original region, it is included in the inverted region, and vice versa.
x
y
1
x
1
∪{∞}
y = ∞
1
x
∪{∞}
y = ∞
x−1
y−1
1
y−1
x−1
1
y−1
1
∪{∞}
x−1 = ∞
13.2
Scaled relative graphs
In this section, we define the notion of scaled relative graphs (SRG). Loosely speak-
ing, SRG maps the action of an operator to a set on the extended complex plane.
13.2.1
SRG of operators
Consider an operator 픸: Rn ⇒Rn. Let x, y ∈Rn be a pair of inputs and let
u, v ∈Rn be their corresponding outputs, i.e., u ∈픸x, and v ∈픸y. The goal is to
understand the change in output relative to the change in input.
First, consider the case x̸ = y. Consider the complex conjugate pair
z = ∥u −v∥
∥x −y∥exp [±i∠(u −v, x −y)] .


## Page 284

13.2
Scaled relative graphs
269
The absolute value (magnitude) |z| =
∥u−v∥
∥x−y∥represents the size of the change
in outputs relative to the size of the change in inputs.
The argument (angle)
∠(u−v, x−y) represents how much the change in outputs is aligned with the change
in inputs. Equivalently, Re z and Im z respectively represent the components of
u −v aligned with and perpendicular to x −y:
Re z = sgn(⟨u −v, x −y⟩)∥Πspan{x−y}(u −v)∥
∥x −y∥
= ⟨u −v, x −y⟩
∥x −y∥2
Im z = ±∥Π{x−y}⊥(u −v)∥
∥x −y∥
,
(13.1)
where Πspan{x−y} is the projection onto the span of x −y and Π{x−y}⊥is the
projection onto the subspace orthogonal to x −y.
Define the SRG of an operator 픸: Rn ⇒Rn as
G(픸) =
∥u −v∥
∥x −y∥exp [±i∠(u −v, x −y)]
 u ∈픸x, v ∈픸y, x̸ = y


∪{∞} if 픸is multi-valued

.
We clarify several points: (i) G(픸) ⊆C. (ii) ∞∈G(픸) if and only if there is a point
x ∈Rn such that 픸x is multi-valued. (In this case, there exists (x, u), (y, v) ∈픸
such that x = y and u̸ = v, and the idea is that |z| = ∥u −v∥/0 = ∞, i.e., u −v
is infinitely larger than x −y = 0.) (iii) the ± makes G(픸) symmetric about the
real axis. (We include the ± because ∠(u −v, x −y) always returns a nonnegative
angle.)
Example 13.3 SRGs of the operators: ΠL : R2 →R2 is the projection onto an ar-
bitrary line L; 픸: R2 →R2 is defined as 픸(u, v) = (0, u); ∂∥· ∥is the subdiffer-
ential of the Euclidean norm on Rn with n ≥2; and 픹: R3 →R3 is defined as
픹(u, v, w) = (u, 2v, 3w). The shapes were obtained by plugging the operators into
the definition of the SRG and performing direct calculations.
G(ΠL) =
1
G(픸) =
i
G(∂∥· ∥) =
{z | Re z > 0} ∪{0, ∞}
∪{∞}
G(픹) =
1
2
3


## Page 285

270
13
Scaled relative graphs
The SRG G(픸) maps the action of the operator 픸to points in C.
In the
following sections, we will need to conversely take any point in C and find an
operator whose action maps to that point. Lemma 4 provides such constructions.
Lemma 4 Take any z = zr + zii ∈C. Define 픸z : R2 →R2 and 픸∞: R2 ⇒R2 as
픸z

ζ1
ζ2

=

zrζ1 −ziζ2
zrζ2 + ziζ1

픸∞(x) =

R2
if x = 0
∅
otherwise.
Then,
G(픸z) = {z, ¯z},
G(픸∞) = {∞}.
If we write ∼= to identify an element of R2 with an element in C in that

x
y

∼= x + yi,
then we can view 픸z as complex multiplication with z in the sense that
픸z

ζ1
ζ2

∼= z(ζ1 + ζ2i).
Proof. Again, we write ∼= to identify an element of R2 with an element in C. Write
z = rzeiθz. Consider any x, y ∈R2 where x̸ = y and define u = 픸zx and v = 픸zy.
Then we can write
x −y = rw
cos(θw)
sin(θw)

,
where rw > 0, and
u −v = 픸z(x −y) ∼= rzrwei(θz+θw).
This gives us
∥u −v∥
∥x −y∥= rz,
∠(u −v, x −y) = |θz|,
and
G(픸z) =

rzeiθz, rze−iθz	
.
Now consider A∞. By definition, ∞∈G(A∞). For any u ∈A∞x and v ∈A∞y,
we have x = y = 0, and therefore G(A∞) contains no finite z ∈C. We conclude
G(A∞) = {∞}.
13.2.2
SRG and eigenvalues
For linear operators, the SRG generalizes eigenvalues: specifically, if A ∈Rn×n and
n = 1 or n ≥3, then Λ(A) ⊆G(A), where Λ(A) denotes the set of eigenvalues of
A. It is also true (and not obvious to show) that G(A⊺) = G(A) for any A ∈Rn×n.
See Examples 13.4 and 13.5. See the bibliographical notes for further discussion.


## Page 286

13.2
Scaled relative graphs
271
Example 13.4 SRG of a 3 × 3 matrix. The three points denote the eigenvalues.
1/2 + i
1/2 −i
2
= G




1/2
2
0
−1/2
1/2
0
0
0
2




Example 13.5 For normal matrices, multiplicity of eigenvalues do not affect the SRG.
(Left) SRG of an n × n normal matrix with one distinct real eigenvalue and three
distinct complex conjugate eigenvalue pairs. (Right) SRG of an n × n symmetric
matrix with distinct eigenvalues λ1 < λ2 < · · · < λ6.
λ6
λ2
λ4
λ7
λ3
λ5
λ1
λ1
λ2
λ3
λ4 λ5
λ6
13.2.3
SRG of operator classes
Define the SRG of a collection of operators A as
G(A) =
[
픸∈A
G(픸).
We focus more on SRGs of operator classes, rather than individual operators,
because theorems are usually stated with operator classes. For example, one might
say “If 픸is 1/2-cocoercive, i.e., if 픸∈C1/2, then 핀−픸is nonexpansive.”


## Page 287

272
13
Scaled relative graphs
Theorem 19 Let µ, β, L ∈(0, ∞) and θ ∈(0, 1). Then
G(LL) =
L
−L

z ∈C
 |z|2 ≤L2	
G(Nθ) =
1
1 −2θ
θ

z ∈C
 |z|2 + (1 −2θ) ≤2(1 −θ) Re z
	
G(M) =
∪{∞}
{z ∈C | Re z ≥0} ∪{∞}
G(Mµ) =
∪{∞}
µ
{z ∈C | Re z ≥µ} ∪{∞}
G(Cβ) =
1/β

z ∈C
 Re z ≥β|z|2	
Proof. First, characterize G(LL). We have G(LL) ⊆

z ∈C
 |z|2 ≤L2	
since
픸∈LL
⇒
∥픸x −픸y∥
∥x −y∥
≤L, ∀x, y ∈Rn, x̸ = y
⇒
G(픸) ⊆

z ∈C
 |z|2 ≤L2	
.
Conversely, given any z ∈C such that |z| ≤L, the operator 픸z of Lemma 4 satisfies
∥픸zx −픸zy∥≤L∥x −y∥for any x, y ∈R2, i.e., 픸z ∈LL, and G(픸z) = {z, ¯z}.
Therefore G(LL) ⊇

z ∈C
 |z|2 ≤L2	
.
Next, characterize G(M). For any 픸∈M, monotonicity implies
⟨u −v, x −y⟩
∥x −y∥2
≥0,
∀u ∈픸x, v ∈픸y, x̸ = y.
Considering (13.1), we conclude G(픸)\{∞} ⊆{z | Re z ≥0}. On the other hand,
given any z ∈{z | Re z ≥0}, the operator 픸z of Lemma 4 satisfies ⟨픸zx−픸zy, x−
y⟩≥0 for any x, y ∈R2, i.e., 픸z ∈M, and G(픸z) = {z, ¯z}. Therefore, z ∈
G(픸z) ⊂G(M), and we conclude {z | Re z ≥0} ⊆G(M).
Finally, note that
∞∈G(M) is equivalent to saying that there exists a multi-valued operator in M.
The 픸∞of Lemma 4 is one such example.
We leave the characterization of G(Mµ), G(Cβ), and G(Nθ) to Exercise 13.12.
As the operator classes M, Mµ, Cβ, LL, and Nθ are defined to include operators
on Rn for all n ∈N, the use of Lemma 4 is sufficient, even though it only concerns
the case n = 2.


## Page 288

13.2
Scaled relative graphs
273
Theorem 20 Let 0 < µ < L < ∞. Then
G(∂F0,∞) =
∪{∞}
{z | Re z ≥0} ∪{∞}
G(∂Fµ,∞) =
∪{∞}
µ
{z | Re z ≥µ} ∪{∞}
G(∂F0,L) =
L
G(∂Fµ,L) =
L
µ
Proof. Since ∂F0,∞⊂M, we have G(∂F0,∞) ⊆G(M) = {z ∈C | Re z ≥0} ∪{∞}
by Theorem 19. We claim f : R2 →R defined by f(x, y) = |x| satisfies G(∂f) =
{z ∈C | Re z ≥0} ∪{∞}. This tells us {z ∈C | Re z ≥0} ∪{∞} ⊆G(∂F0,∞).
We prove the claim with basic computation. Let f(x, y) = |x|. The subgradient
has the form ∂f(x, y) = (h(x), 0) for h defined by
h(x) =



{−1}
for x < 0
{u | −1 ≤u ≤1}
for x = 0
{1}
for x > 0.
Since ∂f is multi-valued at (0, 0), we have ∞∈G(∂f). Since ∂f(1, 0) = ∂f(2, 0),
we have 0 ∈G(∂f). The input-output pairs (0, 0) ∈∂f(0, 0) and (h(R cos(θ)), 0) ∈
∂f(R cos(θ), R sin(θ)) map to the point R−1(| cos(θ)|, ± sin(θ)) ∈C. Clearly, the
image of this map over the range R ∈(0, ∞), θ ∈[0, 2π) is the right-hand plane
except the origin. Hence G(∂f) = {z ∈C | Re z ≥0} ∪{∞}.
We leave the characterization of G(∂Fµ,∞) and G(∂F0,L) to Exercise 13.13.
13.2.4
SRG-full classes
An operator defines its SRG. Conversely, can we examine the SRG and conclude
something about the operator? To perform this type of reasoning, we need further
conditions.
We say the class of operators A is SRG-full if
픸∈A
⇔
G(픸) ⊆G(A).
Since 픸∈A ⇒G(픸) ⊆G(A) already follows from the SRG’s definition, the
substance of this definition is G(픸) ⊆G(A) ⇒픸∈A.
Essentially, a class is
SRG-full if it can be fully characterized by its SRG; given an SRG-full class A and
an operator A, we can check membership 픸∈A by verifying (through geometric
arguments) the containment G(픸) ⊆G(A) in the 2D plane.
SRG-fullness assumes the desirable property G(픸) ⊆G(A) ⇒픸∈A. We now
discuss which classes possess this property.


## Page 289

274
13
Scaled relative graphs
Theorem 21 An operator class A is SRG-full if it is defined by
픸∈A
⇔
h
 ∥u −v∥2, ∥x −y∥2, ⟨u −v, x −y⟩

≤0,
∀u ∈픸x, v ∈픸y
for some nonnegative homogeneous function h: R3 →R.
To clarify, h is nonnegative homogeneous if θh(a, b, c) = h(θa, θb, θc) for all θ ≥0.
(We do not assume h is smooth.) When a class A is defined by h as in Theo-
rem 21, we say h represents A. For example, the µ-strongly monotone class Mµ is
represented by h(a, b, c) = µb −c, since
픸∈Mµ
⇔
µ∥x −y∥2 ≤⟨u −v, x −y⟩,
∀u ∈픸x, v ∈픸y.
As another example, firmly nonexpansive class N1/2 is represented by h(a, b, c) =
a −c, since
픸∈N1/2
⇔
∥u −v∥2 ≤⟨u −v, x −y⟩,
∀u ∈픸x, v ∈픸y.
By Theorem 21, the classes M, Mµ, Cβ, LL, and Nθ are all SRG-full. See Exer-
cise 13.14.
Proof. Since 픸∈A ⇒G(픸) ⊆G(A) always holds, we show G(픸) ⊆G(A) ⇒
픸∈A. Assume A is represented by h and an operator 픸: Rn ⇒Rn satisfies
G(픸) ⊆G(A). Let uA ∈픸xA and vA ∈픸yA represent distinct evaluations, i.e.,
xA̸ = yA or uA̸ = vA.
First, consider the case xA̸ = yA. Then,
z = (∥uA −vA∥/∥xA −yA∥) exp[i∠(uA −vA, xA −yA)]
satisfies z ∈G(픸) ⊆G(A). Since z ∈G(A), there is an operator 픹∈A such that
uB ∈픹xB and vB ∈픹yB with
∥uB −vB∥2
∥xB −yB∥2 = |z|2,
⟨uB −vB, xB −yB⟩
∥xB −yB∥2
= Re z.
Since h represents A, we have
0 ≥h
 ∥uB −vB∥2, ∥xB −yB∥2, ⟨uB −vB, xB −yB⟩

,
and homogeneity gives us
0 ≥h
∥uB −vB∥2
∥xB −yB∥2 , 1, ⟨uB −vB, xB −yB⟩
∥xB −yB∥2

= h
 |z|2, 1, Re z

= h
∥uA −vA∥2
∥xA −yA∥2 , 1, ⟨uA −vA, xA −yA⟩
∥xA −yA∥2

.
Finally, by homogeneity we have
h
 ∥uA −vA∥2, ∥xA −yA∥2, ⟨uA −vA, xA −yA⟩

≤0.


## Page 290

13.3
Operator and SRG transformations
275
Now consider the case xA = yA and uA̸ = vB. Then 픸is multi-valued and
∞∈G(픸) ⊆G(A). Since ∞∈G(A), there is a multi-valued operator 픹∈A such
that uB ∈픹xB and vB ∈픹xB with uB̸ = vB. This implies h(∥uB −vB∥2, 0, 0) ≤0.
Therefore, h(∥uA −vA∥2, 0, 0) ≤0.
In conclusion, (xA, uA) and (yA, vA), which represent arbitrary evaluations of
픸, satisfy the inequality defined by h, and we conclude 픸∈A.
Example 13.6 The classes ∂F0,∞, ∂Fµ,∞, ∂F0,L, and ∂Fµ,L are not SRG-full. For
example, the operator
픸(z1, z2) =
0
−1
1
0
 z2
z2

satisfies G(픸) = {−i, i} ⊆G(∂F0,∞).
However, 픸/∈∂F0,∞because there is no
convex function f for which ∇f = D픸.
For the sake of rigor and completeness, there is one degenerate case to keep in
mind. The SRG-full class of operators Anull represented by h(a, b, c) = a + b + |c|
has G(Anull) = ∅. However, the class Anull is not itself empty; it contains operators
whose graph contains zero or one pair, i.e., A ∈Anull if and only if we have either
(a) dom 픸= ∅or (b) dom 픸= x and 픸x = {y} for some x, y ∈Rn.
Role of maximality
The notion of maximality is mostly orthogonal to the notion of the SRG. In partic-
ular, non-maximal operators have well-defined SRGs, and SRG-full classes contain
non-maximal operators. By keeping the two notions separate, we avoid the geo-
metric analyses via SRGs being entangled with the subtleties of maximality.
13.3
Operator and SRG transformations
In this section, we show how transformations of operators map to changes in their
SRGs and analyze convergence of various fixed-point iterations.
13.3.1
Intersection
Theorem 22 If A and B are SRG-full classes, then A ∩B is SRG-full, and
G(A ∩B) = G(A) ∩G(B).
The substance of Theorem 22 is G(A ∩B) ⊇G(A) ∩G(B) since the containment
G(A ∩B) ⊆G(A) ∩G(B) holds by definition, regardless of SRG-fullness.


## Page 291

276
13
Scaled relative graphs
Proof. Since A and B are SRG-full,
G(ℂ) ⊆G(A ∩B) ⊆G(A) ∩G(B)
⇒
G(ℂ) ⊆G(A) and G(ℂ) ⊆G(B)
⇒
ℂ∈A and ℂ∈B
⇒
ℂ∈A ∩B,
for an operator ℂ, and we conclude A ∩B is SRG-full.
Assume z ∈C satisfies {z, ¯z} ⊆G(A) ∩G(B). Then, 픸z of Lemma 4 satisfies
G(픸z) = {z, ¯z} ⊆G(A) ∩G(B). Since A and B are SRG-full, 픸z ∈A, 픸z ∈B, and
{z, ¯z} = G(픸z) ⊆G(A ∩B). If ∞∈G(A) ∩G(B), then a similar argument using
픸∞of Lemma 4 proves ∞∈G(A ∩B). Therefore, G(A) ∩G(B) ⊆G(A ∩B). Since
the other containment, G(A ∩B) ⊆G(A) ∩G(B), holds by definition, we have the
equality.
Example 13.7 Theorem 22 does not apply when the operator classes are not SRG-full.
For example, although
∂Fµ,L = ∂Fµ,∞∩∂F0,L,
we have the strict containment:
L
µ
G(∂Fµ,L)
⊂
µ
G(∂Fµ,∞) ∩G(∂F0,L)
L
13.3.2
Scaling and translation
Theorem 23 Let α ∈R and α̸ = 0. If A is a class of operators, then
G(αA) = αG(A),
G(핀+ A) = 1 + G(A).
If A is furthermore SRG-full, then αA and 핀+ A are SRG-full.
Proof. G(α픸) = αG(픸) follows from the definition of the SRG, and G(핀+ 픸) =
1+G(픸) follows from (13.1). The scaling and translation operations are reversible,
and G((1/α)A) = (1/α)G(A) and G(A −핀) = G(A) −1. For any 픹: Rn ⇒Rn,
G(픹) ⊆G(αA)
⇒
G((1/α)픹) ⊆G(A)
⇒
(1/α)픹∈A
⇒
픹∈αA,
and we conclude αA is SRG-full. By a similar reasoning, 핀+ A is SRG-full.
Since a class of operators can consist of a single operator,
G(α픸) = αG(픸),
G(핀+ 픸) = 1 + G(픸)
holds for an individual operator 픸.


## Page 292

13.3
Operator and SRG transformations
277
Convergence analysis: Gradient descent
Consider the optimization problem
minimize
x∈Rn
f(x),
where f is µ-strongly convex and L-smooth with 0 < µ < L < ∞. Gradient descent
xk+1 = xk −α∇f(xk)
converges with rate
∥xk −x⋆∥≤(max{|1 −αµ|, |1 −αL|})k ∥x0 −x⋆∥
for α ∈(0, 2/L) by the following Proposition 2.
Proposition 2 Let 0 < µ < L < ∞and α ∈(0, ∞). If A = ∂Fµ,L, then 핀−αA ⊆LR
for
R = max{|1 −αµ|, |1 −αL|}.
This result is tight in the sense that 핀−αA ⊈LR for any smaller value of R.
Proof. By Theorems 20 and 23, we have the geometry
1 −αL
1 −αµ
G (핀−αA)
G (LR)
R = max{|1 −αµ|, |1 −αL|}
The containment of G(핀−αA) holds for R and fails for smaller R.
Since LR
is SRG-full by Theorem 21, the containment of the SRG in C equivalent to the
containment of the class.
Convergence analysis: Forward step method
Consider the monotone inclusion problem
find
x∈Rn
0 ∈픸x,
where 픸: Rn →Rn. Consider the forward step method
xk+1 = xk −α픸xk
under the following two setups.
Assume 픸is µ-strongly monotone and L-Lipschitz with 0 < µ < L < ∞. The
forward step method converges with rate
∥xk −x⋆∥≤
 1 −2αµ + α2L2k/2 ∥x0 −x⋆∥
for α ∈(0, 2µ/L2) by the following Proposition 3.


## Page 293

278
13
Scaled relative graphs
Proposition 3 Let 0 < µ < L < ∞and α ∈(0, ∞).
If A = Mµ ∩LL, then
핀−αA ⊆LR for
R =
p
1 −2αµ + α2L2.
This result is tight in the sense that 핀−αA ⊈LR for any smaller value of R.
Proof. First consider the case αµ > 1.
By Theorems 19 and 23, we have the
geometry
αµ
αL
G (αA)
−αµ
−αL
G (−αA)
1 −αµ
1 −αL
G (핀−αA)
1 −αµ
1 −αL
1
G (핀−αA)
G (LR)
R =
p
1 −2αµ + α2L2
A
B
C
C′
D
O
To clarify, O is the center of the circle with radius OC (lighter shade) and A is the
center of the circle with radius AC = AD defining the inner region (darker shade).
With two applications of the Pythagorean theorem, we get
OC
2 = CB
2 + BO
2 = AC
2 −BA
2 + BO
2
= (αL)2 −(αµ)2 + (1 −αµ)2 = 1 −2αµ + α2L2.
Since C′C is a chord of circle O, it is within the circle. Since two nonidentical
circles intersect at no more than two points, and since D is within circle O, arc
>
CDC′ is within circle O. Finally, the region bounded by C′C ∪>
CDC′ (darker
shade) is within circle O (lighter shade).
The previous diagram illustrates the case αµ > 1. When αµ = 1 and αµ < 1,
the geometries are slightly different, but the same arguments hold:


## Page 294

13.3
Operator and SRG transformations
279
A
C
C′
D
B = O
Case αµ = 1
A
B
C
C′
D
O
Case αµ < 1
The containment holds for R and fails for smaller R. Since LR is SRG-full by
Theorem 21, the containment of the SRG in C equivalent to the containment of
the class.
Assume 픸is µ-strongly monotone and β-cocoercive with 0 < µ < 1/β < ∞.
The forward step method converges with rate
∥xk −x⋆∥≤
 1 −2αµ + α2µ/β
k/2 ∥x0 −x⋆∥
for α ∈(0, 2β) by the following Proposition 4.
Proposition 4 Let 0 < µ < 1/β < ∞and α ∈(0, 2β). If A = Mµ ∩Cβ, then
핀−αA ⊆LR for
R =
p
1 −2αµ + α2µ/β.
This result is tight in the sense that 핀−αA ⊈LR for any smaller value of R.
Proof. First, consider the case µ < 1/(2β). By Theorems 19 and 23, we have the
geometry
1 −αµ
1 −α/β
1
G (핀−αA)
G (LR)
R =
p
1 −2αµ + α2µ/β
C
B
B′
D
A
1
O
To clarify, O is the center of the circle with radius OB (lighter shade) and C is the
center of the circle with radius AC = CB defining the inner region (darker shade).
With two applications of the Pythagorean theorem, we get
OB
2 = OD
2 + DB
2 = OD
2 + BC
2 −CD
2
= (1 −αµ)2 + (α/(2β))2 −(α/(2β) −αµ)2 = 1 −2αµ + α2µ/β.
Since B′B is a chord of circle O, it is within the circle. Since two nonidentical
circles intersect at at most two points, and since A is within circle O, arc >
BAB′


## Page 295

280
13
Scaled relative graphs
is within circle O. Finally, the region bounded by B′B ∪>
BAB′ (darker shade) is
within circle O (lighter shade).
When µ = 1/(2β) and µ > 1/(2β), the geometries are slightly different, but the
same arguments hold:
C = D
B
B′
A
1
O
Case µ = 1/(2β)
C
B
B′
D
A
1
O
Case µ > 1/(2β)
The containment holds for R and fails for smaller R. Since LR is SRG-full by
Theorem 21, the containment of the SRG in C is equivalent to the containment of
the class.
13.3.3
Inversion
In this subsection, we relate inversion of operators with inversion (reciprocal) of
complex numbers. This operation is intimately connected to inversive geometry.
Theorem 24 If A is a class of operators, then
G(A−1) = (G(A))−1 .
If A is furthermore SRG-full, then A−1 is SRG-full.
To clarify, (G(A))−1 = {z−1 | z ∈G(A)} ⊆C. Note that (G(A))−1 = (G(A))−1,
since G(A) is symmetric about the real axis, so we write the simpler (G(A))−1 even
though the inversion map we consider is z 7→¯z−1.
Proof. The equivalence of nonzero finite points, i.e.,
G(픸−1)\{0, ∞} = (G(픸)\ {0, ∞})−1,
follows from
G(픸)\{0, ∞} =
∥u −v∥
∥x −y∥exp [±i∠(u −v, x −y)]
 (x, u), (y, v) ∈픸, x̸ = y, u̸ = v



## Page 296

13.3
Operator and SRG transformations
281
and
G(픸−1)\{0, ∞}
=
∥x −y∥
∥u −v∥exp [±i∠(x −y, u −v)]
 (u, x), (v, y) ∈픸−1, x̸ = y, u̸ = v

=
∥x −y∥
∥u −v∥exp [±i∠(u −v, x −y)]
 (x, u), (y, v) ∈픸, x̸ = y, u̸ = v

= (G(픸)\{0, ∞})−1 ,
where we use the fact that ∠(a, b) = ∠(b, a).
The equivalence of the zero and infinite points follow from
∞∈G(픸)
⇔
∃(x, u), (x, v) ∈픸, u̸ = v
⇔
∃(u, x), (v, x) ∈픸−1, u̸ = v
⇔
0 ∈G(픸−1).
With the same argument, we have 0 ∈G(픸) ⇔∞∈G(픸−1).
The inversion operation is reversible. For any 픹: Rn ⇒Rn,
G(픹) ⊆G(A−1)
⇒
G(픹−1) ⊆G(A)
⇒
픹−1 ∈A
⇒
픹∈A−1,
and we conclude A−1 is SRG-full.
Convergence analysis: proximal point
Consider the monotone inclusion problem
find
x∈Rn
0 ∈픸x,
where 픸is maximal µ-strongly monotone. Consider the proximal point method
xk+1 = 핁α픸xk.
By the following Proposition 5, the proximal point method converges exponentially
with rate
∥xk −x⋆∥≤

1
1 + αµ
k
∥x0 −x⋆∥
for α > 0.
Proposition 5 Let µ ∈(0, ∞) and α ∈(0, ∞). If A = Mµ, then 핁αA ⊆LR for
R =
1
1 + αµ.
This result is tight in the sense that 핁αA ⊈LR for any smaller value of R.
Proof. By Theorems 19, 23, and 24, we have the geometry


## Page 297

282
13
Scaled relative graphs
1 + αµ
∪{∞}
1
G (핀+ αMµ)
¯z−1
−→
1
1
1+αµ
G (핁αA)
G (LR)
R =
1
1+αµ
The containment holds for R and fails for smaller R. Since LR is SRG-full by
Theorem 21, the containment of the SRG in C equivalent to the containment of
the class.
Convergence analysis: DRS
Consider the monotone inclusion problem
find
x∈Rn
0 ∈(픸+ 픹)x,
where 픸and 픹are maximal monotone. Assume 픸or 픹is µ-strongly monotone
and β-cocoercive with 0 < µ < 1/β < ∞. Consider DRS:
zk+1 =
  1
2핀+ 1
2ℝα픸ℝα픹

zk.
DRS converges exponentially with rate
∥zk −z⋆∥≤
 
1
2 + 1
2
s
1 −
4αµ
1 + 2αµ + α2µ/β
!k
∥z0 −z⋆∥
for α > 0 by the following Proposition 6 and the argument of Exercise 13.11.
Proposition 6 Let 0 < µ < 1/β < ∞and α ∈(0, ∞). If A = Mµ ∩Cβ, then
ℝαA ⊆LR for
R =
s
1 −
4αµ
1 + 2αµ + α2µ/β .
This result is tight in the sense that ℝαA ⊈LR for any smaller value of R.
Proof. By Theorems 19, 23, and 24, we have the geometry


## Page 298

13.3
Operator and SRG transformations
283
1+ α
β
1+αµ
1
G(핀+αA)
¯z−1
−→
1
1
1+αµ
1
1+α/β
G(핁αA)
2z−1
−→
G(2핁αA−핀)
1
1−αµ
1+αµ
β−α
β+α
A closer look gives us
1
−1
O
C
β
β+α
B
−αµ
1+αµ
A
R =
q
1 −
4αµ
1+2αµ+α2µ/β
A
A′
E
D
O
G (2JαA −I)
G (LR)
To clarify, B is the center of the circle with radius BA, and C is the center of the
circle with radius CA. By Stewart’s theorem, we have
OA
2 = OC · AB
2 + BO · CA
2 −BO · OC · BC
BC
=
β
α+β

1 −
αµ
1+αµ
2
+
αµ
1+αµ

1 −
β
α+β
2
−
β
α+β
αµ
1+αµ

β
α+β +
αµ
1+αµ

β
α+β +
αµ
1+αµ
= 1 −
4αµ
1 + 2αµ + α2µ/β .
Since two nonidentitcal circles intersect at at most two points, and since D is within
circle B, arc >
ADA′ is within circle O. By the same reasoning, arc >
A′EA is within


## Page 299

284
13
Scaled relative graphs
circle O. Finally, the region bounded by >
ADA′ ∪>
A′EA (darker shade) is within
circle O (lighter shade).
The containment holds for R and fails for smaller R. Since LR is SRG-full by
Theorem 21, the containment of the SRG in C is equivalent to the containment of
the class.
Consider the optimization problem
minimize
x∈Rn
f(x) + g(x),
where f and g are CCP. Assume f or g is µ-strongly convex and L-smooth with
0 < µ < L < ∞. Consider DRS:
xk+1/2 = Proxαg(zk)
xk+1 = Proxαf(2xk+1/2 −zk)
zk+1 = zk + xk+1 −xk+1/2.
DRS converges exponentially with rate
∥zk −z⋆∥≤
1
2 + 1
2 max

1 −αµ
1 + αµ
 ,

1 −αL
1 + αL

k
∥z0 −z⋆∥
by the following Proposition 7 and the argument of Exercise 13.11.
Proposition 7 Let 0 < µ < L < ∞and α ∈(0, ∞). If A = ∂Fµ,L, then ℝαA ⊆LR
for
R = max

1 −αµ
1 + αµ
 ,

1 −αL
1 + αL


.
This result is tight in the sense that ℝαA ⊈LR for any smaller value of R.
Proof. By Theorems 20, 23, and 24, we have the geometry


## Page 300

13.3
Operator and SRG transformations
285
G(핀+αA)
1
1+αL
1+αµ
¯z−1
−→
1
1+αµ
1
1+αL
G(핁αA)
1
2z−1
−→
G(2핁αA−핀)
R=max
n 1−αµ
1+αµ
,
 1−αL
1+αL

o
1−αµ
1+αµ
1−αL
1+αL
G(LR)
The containment holds for R and fails for smaller R. Since LR is SRG-full by
Theorem 21, the containment of the SRG in C is equivalent to the containment of
the class.
13.3.4
Sum of operators
Given z, w ∈C, define the line segment between z and w as
[z, w] = {θz + (1 −θ)w | θ ∈[0, 1]}.
We say an SRG-full class A satisfies the chord property if z ∈G(A)\{∞} implies
[z, ¯z] ⊆G(A). See Figure 13.2.
Theorem 25 Let A and B be SRG-full classes such that ∞/∈G(A) and ∞/∈G(B).
Then
G(A + B) ⊇G(A) + G(B).
If A or B furthermore satisfies the chord property, then
G(A + B) = G(A) + G(B).
Proof. We first show G(A + B) ⊇G(A) + G(B). Assume G(A)̸ = ∅and G(B)̸ = ∅as
otherwise there is nothing to show. Let z ∈G(A) and w ∈G(B) and let 픸z and 픸w
be their corresponding operators as defined in Lemma 4. Then it is straightforward


## Page 301

286
13
Scaled relative graphs
z
¯z
Figure 13.2: The chord property.
to see that 픸z +픸w corresponds to complex multiplication with respect to (z +w),
and z + w ∈G(픸z + 픸w) ⊆G(A + B).
Next, we show G(A + B) ⊆G(A) + G(B). Consider the case G(A)̸ = ∅and
G(B)̸ = ∅.
Without loss of generality, assume it is A that satisfies the chord
property.
Consider 픸+ 픹∈A + B such that 픸∈A and 픹∈B.
Consider
(x, uA + uB), (y, vA + vB) ∈픸+ 픹such that x̸ = y, (x, uA), (y, vA) ∈픸, and
(x, uB), (y, vB) ∈픹. Define
zA = ∥uA −vA∥
∥x −y∥
exp [i∠(uA −vA, x −y)] ∈G(픸)
zB = ∥uB −vB∥
∥x −y∥
exp [i∠(uB −vB, x −y)] ∈G(픹)
z = ∥uA + uB −vA −vB∥
∥x −y∥
exp [i∠(uA + uB −vA −vB, x −y)] ∈G(픸+ 픹).
(Note that Im zA, Im zB, Im z ≥0.) Since
Re zA = ⟨uA −vA, x −y⟩
∥x −y∥2
,
Re zB = ⟨uB −vB, x −y⟩
∥x −y∥2
,
Re z = ⟨(uA + uB) −(vA + vB), x −y⟩
∥x −y∥2
,
we have Re z = Re zA + Re zB. Using (13.1) and the triangle inequality, we have
Im z = ∥Π{x−y}⊥(uA + uB −vA −vB)∥
∥x −y∥
≤∥Π{x−y}⊥(uA −vA)∥+ ∥Π{x−y}⊥(uB −vB)∥
∥x −y∥
= Im zA + Im zB,
and using the reverse triangle inequality, we have Im z ≥−Im zA+Im zB. Together,
we conclude
−Im zA + Im zB ≤Im z ≤Im zA + Im zB
and
z ∈[zA, zA] + zB,
z ∈[zA, zA] + zB.
This shows
G(A + B) ⊆{wA + zB | wA ∈[zA, zA] , zA ∈G(A), zB ∈G(B)}
= {wA + zB | wA ∈G(A), zB ∈G(B)} = G(A) + G(B),


## Page 302

13.3
Operator and SRG transformations
287
z
¯z
Arc−(z, ¯z)
z
¯z
Arc+(z, ¯z)
Figure 13.3: Left- and right-arc properties.
where the equality follows from the chord property.
Now, consider the case G(A) = ∅or G(B) = ∅(or both). Assume G(A) = ∅
without loss of generality, and let 픸∈A and 픹∈B. Then, dom 픸is empty or a
singleton, and if {x} = dom 픸, then 픸x is a singleton. Therefore dom (픸+ 픹) ⊆
dom 픸is empty or a singleton, and if {x} = dom 픸, then (픸+ 픹)x is empty or
a singleton, since 픹is single-valued. Therefore, G(픸+ 픹) = ∅and we conclude
G(A + B) = ∅.
It is possible to generalize Theorem 25 to allow ∞by excluding the following
exception: if ∅= G(A) and ∞∈G(B), then {∞} = G(A + B).
13.3.5
Composition of operators
Given z ∈C, define the right-hand arc between z and ¯z as
Arc+(z, ¯z) =
n
rei(1−2θ)ϕ  z = reiϕ, ϕ ∈(−π, π], θ ∈[0, 1], r ≥0
o
and the left-hand arc as
Arc−(z, ¯z) = −Arc+(−z, −¯z).
We say an SRG-full class A respectively satisfies the left-arc property and right-
arc property if z ∈G(A)\{∞} implies Arc−(z, ¯z) ⊆G(A) and Arc+(z, ¯z) ⊆G(A),
respectively. We say A satisfies an arc property if the left- or right-arc property is
satisfied. See Figure 13.3.
Theorem 26 Let A and B be SRG-full classes such that ∞/∈G(A), ∅̸ = G(A),
∞/∈G(B), and ∅̸ = G(B). Then,
G(AB) ⊇G(A)G(B).
If A or B furthermore satisfies an arc property, then
G(AB) = G(BA) = G(A)G(B).


## Page 303

288
13
Scaled relative graphs
Proof. We first show G(AB) ⊇G(A)G(B). Assume G(A)̸ = ∅and G(B)̸ = ∅, as
otherwise there is nothing to show. Let z ∈G(A) and w ∈G(B) and let 픸z and 픸w
be their corresponding operators as defined in Lemma 4. Then, it is straightforward
to see that 픸z픸w corresponds to complex multiplication with respect to zw, and
zw ∈G(픸z픸w) ⊆G(AB).
Next, we show G(AB) ⊆G(A)G(B).
Let 픸∈A and 픹∈B.
Consider
(u, s), (v, t) ∈픸and (x, u), (y, v) ∈픹, where x̸ = y. This implies (x, s), (y, t) ∈픸픹.
Define
z = ∥s −t∥
∥x −y∥exp [i∠(s −t, x −y)] .
Consider the case u = v. Then 0 ∈G(B). Moreover, s = t, since 픸is single-valued
(by the assumption ∞/∈G(A)), and z = 0. Therefore, z = 0 ∈G(A)G(B).
Next, consider the case u̸ = v. Define
zA = ∥s −t∥
∥u −v∥eiϕA,
zB = ∥u −v∥
∥x −y∥eiϕB,
where ϕA = ∠(s −t, u −v) and ϕB = ∠(u −v, x −y). Consider the case where
A satisfies the right-arc property. Using the spherical triangle inequality (further
discussed in the appendix), we see that either ϕA ≥ϕB and
z ∈∥s −t∥
∥u −v∥
∥u −v∥
∥x −y∥exp [i[ϕA −ϕB, ϕA + ϕB]]
⊆∥s −t∥
∥u −v∥
∥u −v∥
∥x −y∥exp [i[ϕB −ϕA, ϕB + ϕA]]
= zBArc+ (zA, zA)
or ϕA < ϕB and
z ∈∥s −t∥
∥u −v∥
∥u −v∥
∥x −y∥exp [i[ϕB −ϕA, ϕB + ϕA]]
= zBArc+ (zA, zA) .
This gives us
z ∈
zB
|{z}
∈G(B)
Arc+ (zA, zA)
|
{z
}
⊆G(A)
⊆G(A)G(B).
That ¯z ∈G(A)G(B) follows from the same argument. That z, ¯z ∈G(A)G(B) when
instead B satisfies the right-arc property follows from the same argument.
Putting everything together, we conclude G(AB) = G(A)G(B) when A or B
satisfies the right-arc property. When A satisfies the left-arc property, −A satisfies
the right-arc property. So,
−G(AB) = G(−AB) = G(−A)G(B) −G(A)G(B)
by Theorem 23, and we conclude G(AB) = G(A)G(B). When B satisfies the left-arc
property, B ◦(−핀) satisfies the right-arc property. So
−G(AB) = G(AB ◦(−I)) = G(A)G(B ◦(−핀)) = −G(A)G(B)
by Theorem 23, and we conclude G(AB) = G(A)G(B).


## Page 304

13.4
Averagedness coefficients
289
It is possible to generalize Theorem 26 to allow ∅and ∞by excluding the
following exceptions: if ∅= G(A) and ∞∈G(B), then {∞} = G(AB); if 0 ∈G(A)
and ∞∈G(B), then ∞∈G(AB); if ∅= G(A) and 0 ∈G(B), then {0} = G(AB)
and ∅= G(BA).
13.4
Averagedness coefficients
In this section, we establish the averagedness coefficients for the composition of
averagedness operators and the DYS operator.
13.4.1
Composition of averaged operators
Theorem 27 Let 핋1 and 핋2 be θ1- and θ2-averaged operators on Rn with θ1, θ2 ∈
(0, 1). Then 핋1핋2 is θ-averaged with
θ = θ1 + θ2 −2θ1θ2
1 −θ1θ2
.
Proof. Note
z ∈G(Nθ)
⇔
|z −(1 −θ)|2 ≤θ2
⇔
|z|2 ≤1 −1 −θ
θ
|1 −z|2
by Theorem 19 and
θ2 −|z −(1 −θ)|2 = θ

1 −1 −θ
θ
|1 −z|2 −|z|2

.
Let z1 ∈G(Nθ1) and z2 ∈G(Nθ2). Then,
|z1z2|2 ≤|z2|2

1 −1 −θ1
θ1
|1 −z1|2

≤1 −1 −θ2
θ1
|1 −z2|2 −1 −θ1
θ1
|1 −z1|2|z2|2
= 1 −1 −θ
θ
|1 −z1z2|2 −
θ1θ2
θ1 + θ2 −2θ1θ2

1 −θ1
θ1
(1 −z1)z2 −1 −θ2
θ2
(1 −z2)

2
≤1 −1 −θ
θ
|1 −z1z2|2
and z1z2 ∈G(Nθ). In other words, we have shown G(Nθ1)G(Nθ2) ⊆G(N(Gθ)).
Since Nθ1 satisfies an arc property, G(Nθ1)G(Nθ2) = G(Nθ1Nθ2) by Theorem 26.
So,
G(Nθ1Nθ2) = G(Nθ1)G(Nθ2) ⊆G(Nθ)
implies Nθ1Nθ2 ⊆Nθ by SRG-fullness of Nθ.


## Page 305

290
13
Scaled relative graphs
1
θ1 = 2
3, θ2 = 1
4
1
θ1 = 1
4, θ2 = 3
4
1
θ1 = 2
3, θ2 = 3
4
1
θ1 = θ2 = 1
4
1
θ1 = θ2 = 1
2
1
θ1 = θ2 = 3
4
Figure 13.4: The shaded regions illustrate G(Nθ1Nθ2) and the dashed circles illus-
trate G(Nθ) given by Theorem 27.
13.4.2
Davis–Yin splitting
Theorem 28Assume 픸, 픹, and ℂare maximal monotone. Assume ℂis β-cocoercive
and α ∈(0, 2β). The DYS operator 핀−핁α픹+ 핁α픸(ℝα픹−αℂ핁α픹) is θ-averaged
with
θ =
2β
4β −α.
Lemma 5 For θ ∈(0, 1), 핋is θ-averaged if and only if
∥핋x −핋y∥2 ≤∥x −y∥2 −1 −θ
θ
∥핋x −x −핋y + y∥2
∀, x, y ∈Rn.
Proof. Note 핋is θ-averaged if and only if 1
θ핋−
  1
θ −1

핀is nonexpansive. The
claim follows from
0 ≥

1
θ핋x −
1
θ −1

x −1
θ핋y +
1
θ −1

y

2
−∥x −y∥2
= 1
θ

∥핋x −핋y∥2 + 1 −θ
θ
∥핋x −x −핋y + y∥2 −∥x −y∥2

.
Proof of Theorem 28. For any z0, ˆz0 ∈Rn, let


## Page 306

13.4
Averagedness coefficients
291
x1/2 = 핁α픹(z0)
x1 = 핁α픸(2x1/2 −zk −αℂx1/2)
z1 = z0 + x1 −x1/2
ˆx1/2 = 핁α픹(ˆz0)
ˆx1 = 핁α픸(2ˆx1/2 −ˆzk −αℂˆx1/2)
ˆz1 = ˆz0 + ˆx1 −ˆx1/2.
Define
˜픹x1/2 = 1
α(z0 −x1/2)
˜픸x1 = 1
α(2x1/2 −zk −αℂx1/2 −x1)
˜픹ˆx1/2 = 1
α(ˆz0 −ˆx1/2)
˜픸ˆx1 = 1
α(2ˆx1/2 −ˆzk −αℂˆx1/2 −ˆx1),
which implies
˜픹x1/2 ∈픹x1/2
˜픸x1 ∈픸x1
˜픹ˆx1/2 ∈픹ˆx1/2
˜픸ˆx1 ∈픸ˆx1.
Then,
∥z1 −ˆz1∥2 = ∥z0 −ˆz0∥2 −1 −θ
θ
∥z1 −z0 −ˆz1 + ˆz0∥2
−2α⟨˜픸x1 −˜픸ˆx1, x1 −ˆx1⟩−2α⟨˜픹x1/2 −˜픹ˆx1/2, x1/2 −ˆx1/2⟩
−2α

⟨ℂx1/2 −ℂˆx1/2, x1/2 −ˆx1/2⟩−β∥ℂx1/2 −ℂˆx1/2∥2
−α2
2β
 ˜픸x1 −˜픸ˆx1 + ˜픹x1/2 −˜픹ˆx1/2 −2β −α
α
(ℂx1/2 −ℂˆx1/2)

2
≤∥z0 −ˆz0∥2 −1 −θ
θ
∥z1 −z0 −ˆz1 + ˆz0∥2,
where the inequality follows from monotonicity of 픸and 픹and β-cocoercivity of
ℂ. Finally, the claim follows from Lemma 5.
This proof does not use SRGs. Whether there is a simpler proof of Theorem 28
that relies on the SRG machinery is an open problem.


## Page 307

292
13
Scaled relative graphs
Bibliographical Notes
Using circles or disks centered at the origin to illustrate contractive mappings is natu-
ral and likely common. Eckstein and Bertsekas’s illustration of firm-nonexpansiveness
via the disk with radius 1/2 centered at (1/2, 0) [Eck89, EB92] was, to the best of our
knowledge, the first geometric illustration of notions from fixed-point theory other than
nonexpansiveness and Lipschitz continuity. Since then, Giselsson and Boyd used similar
illustrations in earlier versions of the paper [GB17] (the arXiv versions 1 through 3 have
the geometric diagrams, but later versions do not) and more thoroughly in the lecture
slides [Gis15]. Banjac and Goulart also utilize similar illustrations [BG18].
In complex analysis, the inversion map is known as the Möbius transformation [AF03, p.
366]. In classical Euclidean geometry, inversive geometry considers generally the inversion
of the 2D plane about any circle [Ped70, p. 75]. Our inversion map z 7→¯z−1 is the inversion
about the unit circle.
Stewart’s theorem is due to [Ste46]. The proof of the spherical triangle inequality can be
found in [RHY21]. The proof SRG generalizing eigenvalues relies on topological arguments
and can be found in [RHY21]. To further understand Example 13.3, see [HRY20, HRY19]
for follow-up work on drawing the SRG of linear operators. Pates identified a connection
between the SRG of a linear operator and the numerical range of a related linear operator
[Pat21]. This connection allows one to utilize existing machinery for the numerical range
for drawing SRGs of linear operators. Furthermore, Pates used this connection and the
Toeplitz–Hausdorff theorem to show that G(A⊺) = G(A) for any A ∈Rn×n.
Finally,
Chaffey, Forni, and Sepulchre has explored applications of the SRG in control theory
[CFS21b, CFS21a].
Proposition 2 was first shown in [RHY21], Proposition 3 in [BC17a, Proposition 26.16],
Proposition 4 in [RHY21, Fact 7], Proposition 5 in [BC17a, Proposition 23.13], Proposi-
tion 6 in [GB15, Theorem 7.2], and Proposition 7 in [GB17, Theorem 1].
The definition of the SRG, when restricted to linear operators, has a form similar to
the pseudospectrum [TE05], but it is unclear if there is any meaningful connection. A
connection between the SRG and the numerical range (field of values) [HJ91] was identified
by Pates [Pat21].
In Example 13.3, the first, second, and third SRGs can be drawn by considering inputs of
the form [r cos(θ), r sin(θ)] for r > 0 and performing direct calculations. The fourth SRG
(the one with 픹) can be drawn with the results of [HRY19]. The SRG of Example 13.4
can be drawn with the ideas of [RHY21] and [HRY19]. The SRGs of Example 13.5 is
discussed in [HRY19].
The averagedness coefficient of Theorem 27 was established by Ogura, Yamada, and
Combettes [OY02, CY15]. Let
Tα,β = {핀−핁α픹+ 핁α픸(ℝα픹−αℂ핁α픹) | 픸, 픹∈M, ℂ∈Cβ}.
Theorem 28 states G(Tα,β) ⊆G

N
2β
4β−α

for α ∈(0, 2β), but the stronger result
G(Tα,β) = G

N
2β
4β−α

=
1
2β−α
4β−α
which implies tightness of the averagedness coefficient, was shown in [HRY20]. One may
ask whether the averagedness coefficients established in Theorems 27 and 28 are tight


## Page 308

Bibliographical Notes
293
(largest). In Figure 13.4, we can observe that the SRG touches the G(Nθ) at 1 and has
matching “curvature.” This observation has been formalized into a proof of tightness in
[HRY20].


## Page 309

294
13
Scaled relative graphs
Exercises
13.1 Contractive ⊂averaged ⊂nonexpansive. Let R < 1. Show
LR ⊂N 1+R
2
⊂L1.
13.2 Show 픸∈N1/2 ⇔픸∈C1 ⇔핀−픸∈N1/2 ⇔2픸−핀∈L1.
13.3 Show that 픸∈Nθ if and only if 핀−픸∈C1/(2θ).
Remark. We had proved this result in the proof of Theorem 2, but a proof using the SRG
provides geometric intuition.
13.4 Show that if θ ∈(0, 1/2), then Nθ ⊂M1−2θ, where the inclusion is strict.
13.5 Optimal stepsize for gradient descent. Let 0 < µ < L < ∞. We previously established
that 핀−α∂Fµ,L ⊆LR with
R = max{|1 −αµ|, |1 −αL|},
which provides an exponential rate of convergence for the gradient method
xk+1 = xk −α∇f(xk).
What is the optimal choice of α > 0 that minimizes the contraction factor? Describe
G(핀−α∂Fµ,L) with the optimal α.
13.6 Let L > 0. Consider
find
x∈Rn
0 = 픽(x),
where 픽: Rn →Rn is monotone and L-Lipschitz. Using G(핀−α(M ∩LL)), explain why
is it not possible to establish convergence of the forward step method
xk+1 = xk −α픽xk
without further assumptions.
13.7 Nonexpansive and inverse Lipschitz residual makes Krasnosel’skiĭ–Mann contractive. Show
that if 핋is nonexpansive and (핀−핋)−1 is γ-Lipschitz, with γ ≥1/2 and θ ∈(0, 1), then
(1 −θ)핀+ θ핋∈L
 s
1 −θ(1 −θ)
γ2
!
.
Remark. This result was first shown in [LFP16].
13.8 Proximal point with inverse Lipschitz operator. Let α, γ ∈(0, ∞). Show that if A =
L−1
γ
∩M, then JαA ⊆LR for
R =
γ
p
α2 + γ2 .
Also show that the result is tight in the sense that JαA ⊈LR for any smaller value of R.
Remark. This result was first shown analytically in [Roc76b].
13.9 Pseudononexpansive operators An operator 핋on Rn is said to be pseudononexpansive if
∥핋x −핋y∥2 ≤∥x −y∥2 + ∥(핀−핋)x −(핀−핋)y∥2
∀x, y ∈Rn.
Describe the SRG of the class of pseudononexpansive operators.
13.10 Closedness of {Cβ}β>0 under addition. Show that if β1, β2 ∈(0, ∞), then Cβ1 + Cβ2 =
C(β−1
1
+β−1
2
)−1.


## Page 310

Exercises
295
13.11 SRG of DRS. Let A be an SRG-full operator class such that G(A) ⊆G(LR) and R is
tight in the sense that there exists a z ∈G(A) such that |z| = R. Show that G(AL1) =
G(L1A) = G(LR). Also show that
G
1
2핀+ 1
2AL1

= G
1
2핀+ 1
2L1A

⊆G

L 1
2 + 1
2 R

.
Remark. Since the SRG-full classes are defined to contain operators on Rn for all n ≥1,
it is sufficient to consider the case n = 2 and appeal to Lemma 4.
13.12 Complete the proof of Theorem 19. Specifically, given G(M) = {z | Re z ≥0} ∪{∞} and
G(LL) = {z | |z| ≤L}, prove the characterizations of G(Nθ), G(Mµ), and G(Cβ) asserted
in Theorem 19.
Hint. Use Mµ = µI + M, (Mµ)−1 = Cµ, and (1 −θ)I + θL1 = Nθ.
13.13 Complete the proof of Theorem 20. Specifically, given G(F0,∞) = {z | Re z ≥0} ∪{∞},
prove the characterizations of G(∂Fµ,∞), G(∂F0,L), and G(∂Fµ,L) asserted in Theorem 20.
Hint. Use ∂Fµ,∞= µ핀+ ∂F0,∞, ∂F0,L =
 ∂F1/L,∞
−1, and ∂Fµ,L = µ핀+ ∂F0,L−µ.
13.14 Describe nonnegative homogeneous functions representing M, Cβ, LL, and Nθ.
13.15 SRG of union. Show that a result similar to Theorem 22 with a union, rather than an
intersection, holds.
13.16 Show that if h and g represent SRG-full classes A and B, then max{h, g} represents A∩B.
Also, which class does min{h, g} represent?
13.17 SRG-invariant transformations. Some operations do not change the SRG. Given 픸: Rn ⇒
Rn and w ∈Rn, define the inner and outer shifts 픸w : Rn ⇒Rn and w픸: Rn ⇒Rn as
픸w(x) = 픸(x −w),
w픸(x) = 픸(x) −w.
Let 픸: Rn ⇒Rn, w ∈Rn, and U ∈Rn×n be an orthogonal matrix. Show that
G(픸) = G(픸w) = G(w픸) = G(U픸U ⊺).
13.18 Composition without an arc property. Consider the SRG-full operator class A represented
by h(a, b, c) = |a −b| + |c|. Show:
(a) G(A) = {±i},
(b) linear operators on R3 representing 90 degrees rotations are in A, and
(c) G(AA) = {z ∈C | |z| = 1}.
Remark.
Since G(AA) = {z ∈C | |z| = 1} ⊃G(A)G(A) is a strict containment, the
analysis shows we cannot fully drop the arc property in Theorem 26.
13.19 Right-scalar multiplication. Define 픸α, the right-scalar multiplication with an operator
픸and scalar α, as
(픸α)(x) = 픸(αx).
Define Aα = {픸α | 픸∈A}. Show G(Aα) = αG(A) for α̸ = 0.
13.20 DRS with split strong monotonicity and cocoercivity is a contraction. Assume A = Mµ
and B = Cβ. Show:
(a) ℝB = N
1
1+β ,
(b) −ℝA = N
1
1+µ ,
(c) −ℝAℝB ⊆N
µ+β
µ+β+µβ ,
(d)
1
2핀+ 1
2ℝAℝB ⊆L
µ+β
µ+β+µβ , and
(e) ℝAℝB ⊈LR for any 0 ≤R < 1.


## Page 311

296
13
Scaled relative graphs
Hint. For part (c), use Theorem 27.
Remark. If −픸is θ-averaged, we say 픸is negatively averaged. Giselsson defined the notion
of negatively averaged operators and used it to prove fact (d) [GB15]. Ryu et al. used a
similar argument to establish a contraction for the “plug-and-play” image reconstruction
method in machine learning [RLW+19].


## Page 312

Appendices


## Page 313



## Page 314

Appendix A
Miscellaneous probability
background
Let F0 ⊆F1 ⊆· · · be a sequence of σ-algebras. Write E [X | Fk] for the conditional
expectation of a random variable X with respect to Fk.
In this book, Fk represents the information before iteration k, and the Lyapunov
function V k is Fk-measurable. Therefore, E

V k | Fk

= V k. To say this without
using measure theoretic language, E [· | Fk] represents the expectation conditioned
on the information before iteration k, and V k is determined by the randomness
of the iterations before k. For example, in Theorem 2 of §5.1, we (implicitly) use
the Lyapunov function V k = ∥xk −x⋆∥2. Since xk is determined by the (non-
random) starting point x0 and the random indices i(0), i(1), . . . , i(k −1), we have
E

V k | Fk

= V k, since there is no randomness in V k once we condition on the
information before iteration k.
Theorem 29 Supermartingale convergence theorem.
Let V k and Sk be Fk-
measurable random variables satisfying V k ≥0 and Sk ≥0 almost surely for
k = 0, 1, . . . . Assume
E

V k+1 | Fk

≤EkV k −Sk
holds for k = 0, 1, . . . . Then
1. V k →V ∞
2. P∞
k=0 Sk < ∞
almost surely. (Note that the limit V ∞is a random variable.)
This supermartingale convergence theorem is due to Doob [Doo53] and its proof
can be found in many standard textbooks on probability theory. (The standard
supermartingale convergence theorem is slightly more general.)


## Page 315

300
A
Miscellaneous probability background
Theorem 30 Let V k, Sk, and U k be Fk-measurable random variables satisfying
V k ≥0, Sk ≥0, and U k ≥0 almost surely for k = 0, 1, . . . . Let β0, β1, . . . be
nonnegative (non-random) scalars satisfying
∞
X
k=0
βk < ∞.
Assume
E

V k+1 | Fk

≤(1 + βk)V k −Sk + U k
and
∞
X
i=1
U i < ∞
almost surely. Then
1. V k →V ∞
2. P∞
k=0 Sk < ∞
almost surely. (Note that the limit V ∞is a random variable.)
This “almost supermartingale” convergence theorem is due to Robbins and Sieg-
mund [RS85].
Theorem 31 Let M k be a Fk-measurable random variable for k = 0, 1, . . . . Assume
E

M k+1 | Fk

= M k
almost surely,
E[∥Mk∥2] < ∞
∀k = 0, 1, . . . ,
and
∞
X
k=0
E

∥Mk+1 −Mk∥2 | Fk

< ∞
almost surely. Then
M k →M ∞
almost surely. (Note that the limit M ∞is a random variable.)
The proof of this result can be found as Theorem 5.3.33 of Dembo’s lecture notes
[Dem19].


## Page 316

References
[AAC18]
F. J. Aragón Artacho and R. Campoy. A new projection method for finding
the closest point in the intersection of convex sets. Computational Optimiza-
tion and Applications, 69(1):99–132, 2018.
[AAC19]
F. J. Aragón Artacho and R. Campoy.
Computing the resolvent of the
sum of maximally monotone operators with the averaged alternating modi-
fied reflections algorithm. Journal of Optimization Theory and Applications,
181(3):709–726, 2019.
[ACL16]
T. Aspelmeier, C. Charitha, and D. R. Luke. Local linear convergence of the
ADMM/Douglas–Rachford algorithms without strong convexity and applica-
tion to statistical imaging. SIAM Journal on Imaging Sciences, 9(2):842–868,
2016.
[AF03]
M. J. Ablowitz and A. S. Fokas. Complex Variables: Introduction and Ap-
plications. Cambridge Texts in Applied Mathematics. Cambridge University
Press, second ed., 2003.
[AHU58]
K. J. Arrow, L. Hurwicz, and H. Uzawa. Studies in Linear and Non-Linear
Programming. Stanford University Press, 1958.
[Amd67]
G. M. Amdahl. Validity of the single processor approach to achieving large-
scale computing capabilities. In AFIPS Conference Proceedings, 1967.
[AMP05]
C. Andrieu, É. Moulines, and P. Priouret. Stability of stochastic approxima-
tion under verifiable conditions. SIAM Journal on Control and Optimization,
44(1):283–312, 2005.
[And65]
D. G. Anderson. Iterative procedures for nonlinear integral equations. Jour-
nal of The ACM, 12(4):547–560, 1965.
[AT96]
H. Attouch and M. Théra. A general duality principle for the sum of two
operators. Journal of Convex Analysis, 3(1):1–24, 1996.
[AT06]
A. Auslender and M. Teboulle.
Interior gradient and proximal meth-
ods for convex and conic optimization.
SIAM Journal on Optimization,
16(3):697–725, 2006.
[Att77]
H. Attouch. Convergence of convex functions, subs-differentials and associ-
ated semi-groups. Comptes Rendus Hebdomadaires des Séances de l’Académie
des sciences, Série A, 284(10):539–542, 1977.
[Att84]
H. Attouch. Variational Convergence for Functions and Operators, volume 1
of Applicable Mathematics Series. Pitman Advanced Publishing Program,
1984.
[Aum65]
R. J. Aumann. Integrals of set-valued functions. Journal of Mathematical
Analysis and Applications, 12(1):1–12, 1965.
[Aus92]
A. Auslender.
Asymptotic properties of the Fenchel dual functional and
applications to decomposition problems.
Journal of Optimization Theory
and Applications, 73(3):427–449, 1992.


## Page 317

302
References
[Ban22]
S. Banach. Sur les opérations dans les ensembles abstraits et leur application
aux équations intégrales. Fundamenta Mathematicae, 3(1):133–181, 1922.
[BB96]
H. H. Bauschke and J. M. Borwein. On projection algorithms for solving
convex feasibility problems. SIAM Review, 38(3):367–426, 1996.
[BBC21]
S. Banert, R. I. Boţ, and E. R. Csetnek. Fixing and extending some recent
results on the ADMM algorithm. Numerical Algorithms, 86(3):1303–1325,
2021.
[BBCN+14] H. H. Bauschke, J. Y. Bello Cruz, T. T. A. Nghia, H. M. Phan, and X. Wang.
The rate of linear convergence of the Douglas–Rachford algorithm for sub-
spaces is the cosine of the Friedrichs angle. Journal of Approximation Theory,
185:63–79, 2014.
[BBHM12]
H. H. Bauschke, R. I. Boţ, W. L. Hare, and W. M. Moursi. Attouch–Théra
duality revisited: Paramonotonicity and operator splitting. Journal of Ap-
proximation Theory, 164(8):1065–1084, 2012.
[BBL97]
H. H. Bauschke, J. M. Borwein, and A. S. Lewis. The method of cyclic pro-
jections for closed convex sets in Hilbert space. Contemporary Mathematics,
204:1–38, 1997.
[BBR78]
J. B. Baillon, R. E. Bruck, and S. Reich. On the asymptotic behavior of
nonexpansive mappings and semigroups in Banach spaces. Houston Journal
of Mathematics, 4(1):1–9, 1978.
[BC10]
H. H. Bauschke and P. L. Combettes. The Baillon–Haddad theorem revisited.
Journal of Convex Analysis, 17(3–4):781–787, 2010.
[BC17a]
H. H. Bauschke and P. L. Combettes. Convex Analysis and Monotone Op-
erator Theory in Hilbert Spaces. Springer International Publishing, second
ed., 2017.
[BC17b]
J. Y. Bello Cruz. On proximal subgradient splitting method for minimizing
the sum of two nonsmooth convex functions.
Set-Valued and Variational
Analysis, 25(2):245–263, 2017.
[BCH15]
R. I. Boţ, E. R. Csetnek, and C. Hendrich. Inertial Douglas–Rachford split-
ting for monotone inclusion problems. Applied Mathematics and Computa-
tion, 256:472–487, 2015.
[BCHH15]
R. I. Boţ, E. R. Csetnek, A. Heinrich, and C. Hendrich. On the convergence
rate improvement of a primal-dual splitting algorithm for solving monotone
inclusion problems. Mathematical Programming, 150(2):251–279, 2015.
[BCR05]
H. H. Bauschke, P. L. Combettes, and S. Reich. The asymptotic behavior
of the composition of two resolvents. Nonlinear Analysis: Theory, Methods
and Applications, 60(2):283–301, 2005.
[BD15]
S. Boyd and J. Duchi. Exercises for EE364b. Homework Exercises EE364b,
Stanford University, 2015.
[BD18]
L. M. Briceũo-Arias and D. Davis.
Forward-backward-half forward algo-
rithm for solving monotone inclusions.
SIAM Journal on Optimization,
28(4):2839–2871, 2018.
[BDV18]
S. Boyd, J. Duchi, and L. Vandenberghe.
Subgradients.
Lecture Note
EE364b, Stanford University, 2018.
[BDX04]
S. Boyd, P. Diaconis, and L. Xiao. Fastest mixing Markov chain on a graph.
SIAM Review, 46(4):667–689, 2004.
[Bec19]
S. Becker. The Chen-Teboulle algorithm is the proximal point algorithm.
arXiv:1908.03633, 2019.
[Ben62]
J. F. Benders. Partitioning procedures for solving mixed-variables program-
ming problems. Numerische Mathematik, 4(1):238–252, 1962.


## Page 318

References
303
[Ber73]
D. P. Bertsekas.
Stochastic optimization problems with nondifferen-
tiable cost functionals. Journal of Optimization Theory and Applications,
12(2):218–231, 1973.
[Ber83]
D. P. Bertsekas.
Distributed asynchronous computation of fixed points.
Mathematical Programming, 27(1):107–120, 1983.
[Ber09]
D. P. Bertsekas. Convex Optimization Theory. Athena Scientific, 2009.
[Ber16]
D. P. Bertsekas. Nonlinear Programming. Athena Scientific, third ed., 2016.
[BG18]
G. Banjac and P. J. Goulart. Tight global linear convergence rate bounds
for operator splitting methods. IEEE Transactions on Automatic Control,
63(12):4126–4139, 2018.
[BG19]
N. Bansal and A. Gupta. Potential-function proofs for gradient methods.
Theory of Computing, 15(4):1–32, 2019.
[BGLS95]
J. F. Bonnans, J. C. Gilbert, C. Lemaréchal, and C. A. Sagastizábal. A
family of variable metric proximal methods.
Mathematical Programming,
68(1):15–47, 1995.
[BGMS21]
H. H. Bauschke, S. Gretchko, W. M. Moursi, and M. Saurette.
Edel-
stein’s astonishing affine isometry.
The American Mathematical Monthly,
128(9):796–809, 2021.
[BGSB19]
G. Banjac, P. Goulart, B. Stellato, and S. Boyd. Infeasibility detection in the
alternating direction method of multipliers for convex optimization. Journal
of Optimization Theory and Applications, 183(2):490–519, 2019.
[BH77]
J.-B. Baillon and G. Haddad.
Quelques propriétés des opérateurs angle-
bornés etn-cycliquement monotones.
Israel
Journal
of
Mathematics,
26(2):137–150, 1977.
[BH16]
P. Bianchi and W. Hachem.
Dynamical behavior of a stochastic For-
ward–Backward algorithm using random monotone operators.
Journal of
Optimization Theory and Applications, 171(1):90–120, 2016.
[BI98]
R. S. Burachik and A. N. Iusem. A generalized proximal point algorithm
for the variational inequality problem in a Hilbert space. SIAM Journal on
Optimization, 8(1):197–216, 1998.
[Bia16]
P. Bianchi. Ergodic convergence of a stochastic proximal point algorithm.
SIAM Journal on Optimization, 26(4):2235–2260, 2016.
[BJ76]
C. A. Botsaris and D. H. Jacobson.
A Newton-type curvilinear search
method for optimization. Journal of Mathematical Analysis and Applica-
tions, 54(1):217–229, 1976.
[BK19]
E. Börgens and C. Kanzow. Regularized Jacobi-type ADMM-methods for a
class of separable convex optimization problems in Hilbert spaces. Compu-
tational Optimization and Applications, 73(3):755–790, 2019.
[BL78]
H. Brezis and P. L. Lions. Produits infinis de resolvantes. Israel Journal of
Mathematics, 29(4):329–345, 1978.
[BL06]
J. Borwein and A. S. Lewis. Convex Analysis and Nonlinear Optimization.
Springer, second ed., 2006.
[BLM17]
H. H. Bauschke, B. Lukens, and W. M. Moursi. Affine nonexpansive op-
erators, Attouch–Théra duality and the Douglas–Rachford algorithm. Set-
Valued and Variational Analysis, 25(3):481–505, 2017.
[BLS15]
S. Bubeck, Y. T. Lee, and M. Singh. A geometric alternative to Nesterov’s
accelerated gradient descent. arXiv:1506.08187, 2015.
[BM16]
H. H. Bauschke and W. M. Moursi. On the order of the operators in the
Douglas–Rachford algorithm. Optimization Letters, 10(3):447–455, 2016.


## Page 319

304
References
[BM17]
H. H. Bauschke and W. M. Moursi. On the Douglas–Rachford algorithm.
Mathematical Programming, 164(1):263–284, 2017.
[BMS06]
H. H. Bauschke, D. A. McLaren, and H. S. Sendov. Fitzpatrick functions:
Inequalities, examples, and remarks on a problem by S. Fitzpatrick. Journal
of Convex Analysis, 13(3):499–523, 2006.
[Bol13]
D. Boley. Local linear convergence of the alternating direction method of
multipliers on quadratic or linear programs. SIAM Journal on Optimization,
23(4):2183–2207, 2013.
[Bon11]
S. Bonettini.
Inexact block coordinate descent methods with application
to non-negative matrix factorization. IMA Journal of Numerical Analysis,
31(4):1431–1452, 2011.
[Bor06]
J. M. Borwein. Maximal monotonicity via convex analysis. Journal of Convex
Analysis, 13(3–4):561–586, 2006.
[Bot91]
L. Bottou. Une Approche Théorique de l’Apprentissage Connexionniste: Ap-
plications à La Reconnaissance de La Parole.
PhD Thesis, Université de
Paris XI, Orsay, France, 1991.
[Bot99]
L. Bottou. On-line learning and stochastic approximations. In D. Saad, ed.,
On-Line Learning in Neural Networks, Publications of the Newton Institute,
pages 9–42. Cambridge University Press, 1999.
[Boţ10]
R. I. Boţ. Conjugate Duality in Convex Optimization, volume 637 of Lecture
Notes in Economics and Mathematical Systems. Springer-Verlag, 2010.
[BP66]
F. E. Browder and W. V. Petryshyn. The solution by iteration of nonlinear
functional equations in Banach spaces. Bulletin of the American Mathemat-
ical Society, 72(3):571–575, 1966.
[BP67]
F. E. Browder and W. V. Petryshyn. Construction of fixed points of non-
linear mappings in Hilbert space.
Journal of Mathematical Analysis and
Applications, 20(2):197–228, 1967.
[BPC+11]
S. Boyd, N. Parikh, E. Chu, B. Peleato, and J. Eckstein. Distributed op-
timization and statistical learning via the alternating direction method of
multipliers. Foundations and Trends in Machine Learning, 3(1):1–122, 2011.
[BQ99]
J. V. Burke and M. Qian.
A variable metric proximal point algorithm
for monotone operators.
SIAM Journal on Control and Optimization,
37(2):353–375, 1999.
[Bre71]
H. Brezis. On a problem of T. Kato. Communications on Pure and Applied
Mathematics, 24(1):1–6, 1971.
[Bri15]
L. M. Briceño-Arias.
Forward-Douglas–Rachford splitting and forward-
partial inverse method for solving monotone inclusions.
Optimization,
64(5):1239–1261, 2015.
[Bru75a]
R. E. Bruck. Asymptotic convergence of nonlinear contraction semigroups
in Hilbert space. Journal of Functional Analysis, 18(1):15–26, 1975.
[Bru75b]
R. E. Bruck.
An iterative solution of a variational inequality for certain
monotone operators in Hilbert space. Bulletin of the American Mathematical
Society, 81(5):890–892, 1975.
[Bru77]
R. E. Bruck. On the weak convergence of an ergodic iteration for the solution
of variational inequalities for monotone operators in Hilbert space. Journal
of Mathematical Analysis and Applications, 61(1):159–164, 1977.
[BSS16]
M. Burger, A. Sawatzky, and G. Steidl. First order algorithms in variational
image processing. In R. Glowinski, S. J. Osher, and W. Yin, eds., Splitting
Methods in Communication, Imaging, Science, and Engineering, Scientific
Computation, pages 345–407. Springer, 2016.


## Page 320

References
305
[BT89]
D. P. Bertsekas and J. N. Tsitsiklis. Parallel and Distributed Computation:
Numerical Methods. Prentice Hall, 1989.
[BT09]
A. Beck and M. Teboulle.
A fast iterative shrinkage-thresholding algo-
rithm for linear inverse problems.
SIAM Journal on Imaging Sciences,
2(1):183–202, 2009.
[BT13]
A. Beck and L. Tetruashvili. On the convergence of block coordinate descent
type methods. SIAM Journal on Optimization, 23(4):2037–2060, 2013.
[BV04]
S. Boyd and L. Vandenberghe. Convex Optimization. Cambridge University
Press, 2004.
[BV10]
J. M. Borwein and J. D. Vanderwerff. Convex Functions: Constructions,
Characterizations and Counterexamples. Encyclopedia of Mathematics and
Its Applications. Cambridge University Press, 2010.
[BW10]
H. H. Bauschke and X. Wang. Firmly nonexpansive and Kirszbraun–Valen-
tine extensions: A constructive approach via monotone operator theory. In
A. Leizarowitz, B. S. Mordukhovich, I. Shafrir, and A. J. Zaslavski, eds.,
Nonlinear Analysis and Optimization I: Nonlinear Analysis, pages 55–64.
American Mathematics Society, 2010.
[Cau47]
A.-L. Cauchy. Méthode générale pour la résolution des systémes d’équations
simultanées. Comptes Rendus Hebdomadaires des Séances de l’Académie des
Sciences, 25:536–538, 1847.
[CCCP]
G. Chierchia, E. Chouzenoux, P. L. Combettes, and J.-C. Pesquet.
The
proximity operator repository. User’s guide. http://proximity-operator.net/-
download/guide.pdf.
[CCMY15]
C. Chen, R. H. Chan, S. Ma, and J. Yang. Inertial proximal ADMM for lin-
early constrained separable convex optimization. SIAM Journal on Imaging
Sciences, 8(4):2239–2267, 2015.
[CCPV14]
P. L. Combettes, L. Condat, J.-C. Pesquet, and B. C. Vũ.
A forward-
backward view of some primal-dual optimization methods in image recovery.
In IEEE International Conference on Image Processing, 2014.
[CDR15]
S. Chaturapruek, J. C. Duchi, and C. Ré. Asynchronous stochastic convex
optimization: The noise is in the noise and SGD don’t care.
In Neural
Information Processing Systems, 2015.
[CFKS17a]
L. Cannelli, F. Facchinei, V. Kungurtsev, and G. Scutari.
Asynchronous
parallel nonconvex large-scale optimization. In International Conference on
Acoustics, Speech and Signal Processing, 2017.
[CFKS17b]
L. Cannelli, F. Facchinei, V. Kungurtsev, and G. Scutari.
Asynchronous
parallel algorithms for nonconvex big-data optimization. Part II: Complexity
and numerical results. arXiv:1701.04900, 2017.
[CFS21a]
T. Chaffey, F. Forni, and R. Sepulchre. Graphical nonlinear system analysis.
arXiv:2107.11272, 2021.
[CFS21b]
T. Chaffey, F. Forni, and R. Sepulchre. Scaled relative graphs for system
analysis. IEEE Conference on Decision and Control, 2021.
[CGFL19]
T. Chavdarova, G. Gidel, F. Fleuret, and S. Lacoste-Julien. Reducing noise
in GAN training with variance reduced extragradient. In Neural Information
Processing Systems, 2019.
[Che12]
A. I.-A. Chen.
Fast Distributed First-Order Methods.
PhD Thesis, Mas-
sachusetts Institute of Technology, Department of Electrical Engineering and
Computer Science, 2012.
[CHLZ12]
B. Chen, S. He, Z. Li, and S. Zhang. Maximum block improvement and poly-
nomial optimization. SIAM Journal on Optimization, 22(1):87–107, 2012.


## Page 321

306
References
[CHW15]
T.-H. Chang, M. Hong, and X. Wang. Multi-agent distributed optimization
via inexact consensus ADMM.
IEEE Transactions on Signal Processing,
63(2):482–497, 2015.
[CHYY16]
C. Chen, B. He, Y. Ye, and X. Yuan.
The direct extension of ADMM
for multi-block convex minimization problems is not necessarily convergent.
Mathematical Programming, 155(1):57–79, 2016.
[CIZ98]
Y. Censor, A. N. Iusem, and S. A. Zenios. An interior point method with
Bregman functions for the variational inequality problem with paramonotone
operators. Mathematical Programming, 81(3):373–400, 1998.
[CKCH22]
L. Condat, D. Kitahara, A. Contreras, and A. Hirabayashi. Proximal split-
ting algorithms for convex optimization: A tour of recent advances, with new
twists. SIAM Review, 2022.
[CLCD07]
M. Chiang, S. H. Low, A. R. Calderbank, and J. C. Doyle. Layering as op-
timization decomposition: A mathematical theory of network architectures.
Proceedings of the IEEE, 95(1):255–312, 2007.
[CLS07]
F. S. Cattivelli, C. G. Lopes, and A. H. Sayed. A diffusion rls scheme for
distributed estimation over adaptive networks. In Signal Processing Advances
in Wireless Communications, 2007.
[CM69]
D. Chazan and W. Miranker. Chaotic relaxation. Linear Algebra and Its
Applications, 2(2):199–222, 1969.
[Com04]
P. L. Combettes. Solving monotone inclusions via compositions of nonex-
pansive averaged operators. Optimization, 53(5–6):475–504, 2004.
[Con13]
L. Condat. A primal-dual splitting method for convex optimization involving
Lipschitzian, proximable and linear composite terms. Journal of Optimiza-
tion Theory and Applications, 158(2):460–479, 2013.
[CP08]
P. L. Combettes and J.-C. Pesquet. A proximal decomposition method for
solving convex variational inverse problems. Inverse Problems, 24(6):065014,
2008.
[CP11a]
A. Chambolle and T. Pock. A first-order primal-dual algorithm for convex
problems with applications to imaging. Journal of Mathematical Imaging
and Vision, 40(1):120–145, 2011.
[CP11b]
P. L. Combettes and J.-C. Pesquet. Proximal splitting methods in signal
processing. In H. H. Bauschke, R. S. Burachik, P. L. Combettes, V. Elser,
D. R. Luke, and H. Wolkowicz, eds., Fixed-Point Algorithms for Inverse
Problems in Science and Engineering, pages 185–212. Springer, 2011.
[CP15]
P. L. Combettes and J.-C. Pesquet. Stochastic quasi-Fejér block-coordinate
fixed point iterations with random sweeping. SIAM Journal on Optimization,
25(2):1221–1248, 2015.
[CP16a]
A. Chambolle and T. Pock. An introduction to continuous optimization for
imaging. Acta Numerica, 25:161–319, 2016.
[CP16b]
A. Chambolle and T. Pock. On the ergodic convergence rates of a first-order
primal-dual algorithm. Mathematical Programming, 159(1):253–287, 2016.
[CP19]
P. L. Combettes and J.-C. Pesquet. Stochastic quasi-Fejér block-coordinate
fixed point iterations with random sweeping II: Mean-square and linear con-
vergence. Mathematical Programming, 174(1–2):433–451, 2019.
[CPR16]
E. Chouzenoux, J.-C. Pesquet, and A. Repetti.
A block coordinate vari-
able metric forward–backward algorithm. Journal of Global Optimization,
66(3):457–485, 2016.
[CS10]
F. S. Cattivelli and A. H. Sayed. Diffusion LMS strategies for distributed
estimation. IEEE Transactions on Signal Processing, 58(3):1035–1048, 2010.


## Page 322

References
307
[CSFK16]
L. Cannelli, G. Scutari, F. Facchinei, and V. Kungurtsev.
Parallel asyn-
chronous lock-free algorithms for nonconvex big-data optimization. In Asilo-
mar Conference on Signals, Systems and Computers, 2016.
[CST17a]
L. Chen, D. Sun, and K.-C. Toh. An efficient inexact symmetric Gauss–Sei-
del based majorized ADMM for high-dimensional convex composite conic
programming. Mathematical Programming, 161(1):237–270, 2017.
[CST17b]
L. Chen, D. Sun, and K.-C. Toh.
A note on the convergence of ADMM
for linearly constrained convex optimization problems. Computational Opti-
mization and Applications, 66(2):327–343, 2017.
[CSY13]
C. Chen, Y. Shen, and Y. You. On the convergence analysis of the alternating
direction method of multipliers with three blocks.
Abstract and Applied
Analysis, 2013:183961, 2013.
[CT93]
G. Chen and M. Teboulle. Convergence analysis of a proximal-like minimiza-
tion algorithm using Bregman functions. SIAM Journal on Optimization,
3(3):538–543, 1993.
[CT94]
G. Chen and M. Teboulle.
A proximal-based decomposition method for
convex minimization problems. Mathematical Programming, 64(1):81–101,
1994.
[CT05]
E. J. Candes and T. Tao. Decoding by linear programming. IEEE Transac-
tions on Information Theory, 51(12):4203–4215, 2005.
[CT06]
E. J. Candes and T. Tao. Near-optimal signal recovery from random pro-
jections: Universal encoding strategies? IEEE Transactions on Information
Theory, 52(12):5406–5425, 2006.
[CV95]
C. Cortes and V. Vapnik.
Support-vector networks.
Machine Learning,
20(3):273–297, 1995.
[CV14]
P. L. Combettes and B. C. Vũ.
Variable metric forward–backward split-
ting with applications to monotone inclusions in duality.
Optimization,
63(9):1289–1318, 2014.
[CV20]
C. Clason and T. Valkonen. Introduction to Nonsmooth Analysis and Opti-
mization. arXiv:2001.00216, 2020.
[CW90]
D. Coppersmith and S. Winograd. Matrix multiplication via arithmetic pro-
gressions. Journal of Symbolic Computation, 9(3):251–280, 1990.
[CW05]
P. L. Combettes and V. R. Wajs.
Signal recovery by proximal forward-
backward splitting.
Multiscale Modeling and Simulation, 4(4):1168–1200,
2005.
[CY15]
P. L. Combettes and I. Yamada. Compositions and convex combinations
of averaged nonexpansive operators. Journal of Mathematical Analysis and
Applications, 425(1):55–70, 2015.
[CZ92]
Y. Censor and S. A. Zenios.
Proximal minimization algorithm with D-
functions. Journal of Optimization Theory and Applications, 73(3):451–464,
1992.
[Dav16]
D. Davis.
The asynchronous PALM algorithm for nonsmooth nonconvex
problems. arXiv:1604.00526, 2016.
[DDC14]
A. Defazio, J. Domke, and T. S. Caetano. Finito: A faster, permutable incre-
mental gradient method for big data problems. In International Conference
on Machine Learning, 2014.
[D’E59]
D. A. D’Esopo. A convex programming procedure. Naval Research Logistics
Quarterly, 6(1):33–42, 1959.
[DEC65]
G. B. Dantzig, E. Eisenberg, and R. W. Cottle. Symmetric dual nonlinear
programs. Pacific Journal of Mathematics, 15(3):809–812, 1965.


## Page 323

308
References
[Dem19]
A. Dembo.
Lecture notes on probability theory: Stanford statistics 310.
Lecture Note STAT310/MATH230, Department of Mathematics, Stanford
University, 2019.
[DLPY17]
W. Deng, M.-J. Lai, Z. Peng, and W. Yin. Parallel multi-block ADMM with
o(1/k) convergence. Journal of Scientific Computing, 71(2):712–736, 2017.
[Don06]
D. L. Donoho.
Compressed sensing.
IEEE Transactions on Information
Theory, 52(4):1289–1306, 2006.
[Doo53]
J. L. Doob. Stochastic Processes. Wiley, 1953.
[DR56]
J. Douglas and H. H. Rachford. On the numerical solution of heat conduction
problems in two and three space variables. Transactions of the American
Mathematical Society, 82(2):421–439, 1956.
[DRT11]
I. S. Dhillon, P. Ravikumar, and A. Tewari. Nearest neighbor based greedy
coordinate descent. In Neural Information Processing Systems, 2011.
[DST15]
Y. Drori, S. Sabach, and M. Teboulle. A simple algorithm for a class of non-
smooth convex–concave saddle-point problems. Operations Research Letters,
43(2):209–214, 2015.
[DT14]
Y. Drori and M. Teboulle. Performance of first-order methods for smooth
convex minimization:
A novel approach.
Mathematical Programming,
145(1):451–482, 2014.
[Dur10]
R. Durrett. Probability: Theory and Examples. Cambridge Series in Statisti-
cal and Probabilistic Mathematics. Cambridge University Press, fourth ed.,
2010.
[DW60]
G. B. Dantzig and P. Wolfe. Decomposition Principle for Linear Programs.
Operations Research, 8(1):101–111, 1960.
[DY16a]
D. Davis and W. Yin. Convergence rate analysis of several splitting schemes.
In R. Glowinski, S. J. Osher, and W. Yin, eds., Splitting Methods in Com-
munication, Imaging, Science and Engineering, Chapter 4, pages 115–163.
Springer, 2016.
[DY16b]
W. Deng and W. Yin. On the global and linear convergence of the generalized
alternating direction method of multipliers. Journal of Scientific Computing,
66(3):889–916, 2016.
[DY17a]
D. Davis and W. Yin.
Faster convergence rates of relaxed Peaceman–
Rachford and ADMM under regularity assumptions. Mathematics of Op-
erations Research, 42(3):783–805, 2017.
[DY17b]
D. Davis and W. Yin. A three-operator splitting scheme and its optimization
applications. Set-Valued and Variational Analysis, 25(4):829–858, 2017.
[EB90]
J. Eckstein and D. Bertsekas. An alternating direction method for linear
programming. LIDS Technical Reports LIDS-P 1967, Laboratory for Infor-
mation and Decision Systems, Massachusetts Institute of Technology, 1990.
[EB92]
J. Eckstein and D. P. Bertsekas. On the Douglas–Rachford splitting method
and the proximal point algorithm for maximal monotone operators. Mathe-
matical Programming, 55(1–3):293–318, 1992.
[Eck89]
J. Eckstein. Splitting Methods for Monotone Operators with Applications to
Parallel Optimization. PhD Thesis, Massachusetts Institute of Technology,
Department of Civil Engineering, 1989.
[Eck94]
J. Eckstein. Some saddle-function splitting methods for convex program-
ming. Optimization Methods and Software, 4(1):75–83, 1994.
[Eck12]
J. Eckstein. Augmented Lagrangian and alternating direction methods for
convex optimization: A tutorial and some illustrative computational results.
RUTCOR Research Report RRR RRR 32-2012, RUTCOR Rutgers Center
for Operations Research Rutgers University, 2012.


## Page 324

References
309
[Ede64]
M. Edelstein. On non-expansive mappings of Banach spaces. Mathematical
Proceedings of the Cambridge Philosophical Society, 60(3):439–447, 1964.
[EF94]
J. Eckstein and M. Fukushima. Some reformulations and applications of the
alternating direction method of multipliers. In W. W. Hager, D. W. Hearn,
and P. M. Pardalos, eds., Large Scale Optimization, pages 115–134. Springer,
1994.
[EHJT04]
B. Efron, T. Hastie, I. Johnstone, and R. Tibshirani. Least angle regression.
The Annals of Statistics, 32(2):407–499, 2004.
[ER11]
R. Escalante and M. Raydan. Alternating Projection Methods. Fundamentals
of Algorithms. Society for Industrial and Applied Mathematics, 2011.
[ES08]
J. Eckstein and B. F. Svaiter. A family of projective splitting methods for
the sum of two maximal monotone operators. Mathematical Programming,
111(1):173–199, 2008.
[Eve63]
H. Everett. Generalized Lagrange multiplier method for solving problems of
optimum allocation of resources. Operations Research, 11(3):399–417, 1963.
[EZC10]
E. Esser, X. Zhang, and T. F. Chan. A general framework for a class of first
order primal-dual algorithms for convex optimization in imaging science.
SIAM Journal on Imaging Sciences, 3(4):1015–1046, 2010.
[Fen49]
W. Fenchel. On conjugate convex functions. Canadian Journal of Mathe-
matics, 1(1):73–77, 1949.
[Fen53]
W. Fenchel. Convex Cones, Sets, and Functions. Lecture Note from notes by
D. W. Blackett of lectures, Princeton University Department of Mathematics,
1953.
[FG83]
M. Fortin and R. Glowinski. On decomposition-coordination methods using
an augmented Lagrangian. In M. Fortin and R. Glowinski, eds., Studies in
Mathematics and Its Applications, volume 15, pages 97–146. Elsevier, 1983.
[FGH21]
M. P. Friedlander, A. Goodwin, and T. Hoheisel. From perspective maps to
epigraphical projections. arXiv:2102.06809, 2021.
[Fis04]
M. L. Fisher. The Lagrangian relaxation method for solving integer pro-
gramming problems. Management Science, 50(12_supplement):1861–1871,
2004.
[Fit88]
S. Fitzpatrick. Representing monotone operators by convex functions. In
S. Fitzpatrick and J. Giles, eds., Workshop/Miniconference on Functional
Analysis and Optimization, pages 59–65. Centre for Mathematics and its
Applications, Mathematical Sciences Institute, The Australian National Uni-
versity, Canberra AUS, 1988.
[FNW07]
M. A. T. Figueiredo, R. D. Nowak, and S. J. Wright.
Gradient projec-
tion for sparse reconstruction: Application to compressed sensing and other
inverse problems.
IEEE Journal of Selected Topics in Signal Processing,
1(4):586–597, 2007.
[FP03]
F. Facchinei and J.-S. Pang. Finite-Dimensional Variational Inequalities and
Complementarity Problems. Springer-Verlag, 2003.
[FR15]
O. Fercoq and P. Richtárik. Accelerated, parallel, and proximal coordinate
descent. SIAM Journal on Optimization, 25(4):1997–2023, 2015.
[FS00]
A. Frommer and D. B. Szyld. On asynchronous iterations. Journal of Com-
putational and Applied Mathematics, 123(1–2):201–216, 2000.
[Gab83]
D. Gabay. Application of the methods of multipliers to variational inequali-
ties. In M. Fortin and R. Glowinski, eds., Augmented Lagrangians: Applica-
tion to the Numerical Solution of Boundary Value Problems, pages 299–331.
North-Holland, 1983.


## Page 325

310
References
[GB15]
P. Giselsson and S. Boyd. Metric selection in fast dual forward–backward
splitting. Automatica, 62:1–10, 2015.
[GB17]
P. Giselsson and S. Boyd.
Linear convergence and metric selection for
Douglas–Rachford splitting and ADMM. IEEE Transactions on Automatic
Control, 62(2):532–544, 2017.
[GBV+19]
G. Gidel, H. Berard, G. Vignoud, P. Vincent, and S. Lacoste-Julien.
A
variational inequality perspective on generative adversarial networks. In In-
ternational Conference on Learning Representation, 2019.
[Geo70]
A. M. Geoffrion. Primal resource-directive approaches for optimizing non-
linear decomposable systems. Operations Research, 18(3):375–403, 1970.
[GHY14]
G. Gu, B. He, and X. Yuan.
Customized proximal point algorithms for
linearly constrained convex minimization and saddle-point problems: A uni-
fied approach. Computational Optimization and Applications, 59(1):135–161,
2014.
[Gis15]
P. Giselsson. Lunds universitet, lecture notes: Large-scale convex optimiza-
tion. Lecture Note, Lunds Universitet, Department of Automatic Control,
2015.
[Glo84]
R. Glowinski.
Numerical Methods for Nonlinear Variational Problems.
Springer-Verlag, 1984.
[Glo14]
R. Glowinski. On alternating direction methods of multipliers: A histori-
cal perspective. In W. Fitzgibbon, Y. A. Kuznetsov, P. Neittaanmäki, and
O. Pironneau, eds., Modeling, Simulation and Optimization for Science and
Technology, volume 34, pages 59–82. Springer, 2014.
[GLT89]
R. Glowinski and P. Le Tallec. Augmented Lagrangian and Operator-Splitting
Methods in Nonlinear Mechanics. Society for Industrial and Applied Math-
ematics, 1989.
[GM75a]
R. Glowinski and A. Marrocco. Sur l’approximation, par éléments finis d’or-
dre un, et la résolution, par pénalisation-dualité d’une classe de problèmes
de Dirichlet non linéaires.
Revue Française d’Automatique, Informatique,
Recherche Opérationnelle. Analyse Numérique, 9(2):41–76, 1975.
[GM75b]
R. Glowinski and A. Marroco. Sur l’approximation, par éléments finis d’or-
dre un, et la résolution, par pénalisation-dualité d’une classe de problèmes
de Dirichlet non linéaires.
Revue Française d’Automatique, Informatique,
Recherche Opérationnelle. Analyse Numérique, 9(2):41–76, 1975.
[GM76]
D. Gabay and B. Mercier. A dual algorithm for the solution of nonlinear
variational problems via finite element approximation. Computers and Math-
ematics with Applications, 2(1):17–40, 1976.
[GO09]
T. Goldstein and S. Osher. The split Bregman method for L1-regularized
problems. SIAM Journal on Imaging Sciences, 2(2):323–343, 2009.
[Gol64]
A. A. Goldstein.
Convex programming in Hilbert space.
Bulletin of the
American Mathematical Society, 70(5):709–710, 1964.
[GOSB14]
T. Goldstein, B. O’Donoghue, S. Setzer, and R. Baraniuk. Fast alternat-
ing direction optimization methods.
SIAM Journal on Imaging Sciences,
7(3):1588–1623, 2014.
[GR84]
K. Goebel and S. Reich.
Uniform Convexity, Hyperbolic Geometry, and
Nonexpansive Mappings. Marcel Dekker, 1984.
[GS00]
L. Grippo and M. Sciandrone. On the convergence of the block nonlinear
Gauss–Seidel method under convex constraints. Operations Research Letters,
26(3):127–136, 2000.


## Page 326

References
311
[GTSJ15]
E. Ghadimi,
A. Teixeira,
I. Shames,
and M. Johansson.
Optimal
parameter selection for the alternating direction method of multipliers
(ADMM): Quadratic problems. IEEE Transactions on Automatic Control,
60(3):644–658, 2015.
[Gül91]
O. Güler. On the convergence of the proximal point algorithm for convex
minimization. SIAM Journal on Control and Optimization, 29(2):403–419,
1991.
[Gül92]
O. Güler. New proximal point algorithms for convex minimization. SIAM
Journal on Optimization, 2(4):649–664, 1992.
[GXZ19]
X. Gao, Y.-Y. Xu, and S.-Z. Zhang. Randomized primal-dual proximal block
coordinate updates. Journal of the Operations Research Society of China,
7(2):205–250, 2019.
[Hal67]
B. Halpern. Fixed points of nonexpanding maps. Bulletin of the American
Mathematical Society, 73(6):957–961, 1967.
[Hes69]
M. R. Hestenes. Multiplier and gradient methods. Journal of Optimization
Theory and Applications, 4(5):303–320, 1969.
[HHY15]
B. He, L. Hou, and X. Yuan. On full Jacobian decomposition of the aug-
mented lagrangian method for separable convex programming. SIAM Jour-
nal on Optimization, 25(4):2274–2312, 2015.
[Hil57]
C. Hildreth. A quadratic programming procedure. Naval Research Logistics
Quarterly, 4(1):79–85, 1957.
[HJ91]
R. A. Horn and C. R. Johnson.
Topics in Matrix Analysis.
Cambridge
University Press, 1991.
[HL93]
J.-B. Hiriart-Urruty and C. Lemaréchal. Convex Analysis and Minimization
Algorithms I, volume 2. Springer, 1993.
[HL01]
J.-B. Hiriart-Urruty and C. Lemaréchal. Fundamentals of Convex Analysis.
Springer-Verlag, 2001.
[HL17]
M. Hong and Z.-Q. Luo. On the linear convergence of the alternating di-
rection method of multipliers. Mathematical Programming, 162(1):165–199,
2017.
[HLHY02]
B. He, L.-Z. Liao, D. Han, and H. Yang. A new inexact alternating directions
method for monotone variational inequalities. Mathematical Programming,
92(1):103–118, 2002.
[HLWY14]
B. He, H. Liu, Z. Wang, and X. Yuan. A strictly contractive Peaceman–
Rachford splitting method for convex programming. SIAM Journal on Op-
timization, 24(3):1011–1040, 2014.
[HRY19]
X. Huang, E. K. Ryu, and W. Yin. Scaled relative graph of normal matrices.
arXiv:2001.02061, 2019.
[HRY20]
X. Huang, E. K. Ryu, and W. Yin. Tight coefficients of averaged operators
via scaled relative graph. Journal of Mathematical Analysis and Applications,
490(1):124211, 2020.
[HS19]
J. Haochen and S. Sra. Random shuffling beats SGD after finite epochs. In
International Conference on Machine Learning, 2019.
[HTY12]
B. He, M. Tao, and X. Yuan. Alternating direction method with gaussian
back substitution for separable convex programming. SIAM Journal on Op-
timization, 22(2):313–340, 2012.
[HTY17]
B. He, M. Tao, and X. Yuan. Convergence rate analysis for the alternating
direction method of multipliers with a substitution procedure for separable
convex programming. Mathematics of Operations Research, 42(3):662–691,
2017.


## Page 327

312
References
[HWRL17]
M. Hong, X. Wang, M. Razaviyayn, and Z.-Q. Luo. Iteration complexity
analysis of block coordinate descent methods. Mathematical Programming,
163(1):85–114, 2017.
[HXY16]
B. He, H.-K. Xu, and X. Yuan. On the proximal Jacobian decomposition
of ALM for multiple-block separable convex minimization problems and its
relationship to ADMM. Journal of Scientific Computing, 66(3):1204–1217,
2016.
[HY12a]
D. Han and X. Yuan. A note on the alternating direction method of mul-
tipliers. Journal of Optimization Theory and Applications, 155(1):227–238,
2012.
[HY12b]
B. He and X. Yuan. On the O(1/n) convergence rate of the Douglas–Rach-
ford alternating direction method. SIAM Journal on Numerical Analysis,
50(2):700–709, 2012.
[HY15]
B. He and X. Yuan.
On non-ergodic convergence rate of Douglas–Rach-
ford alternating direction method of multipliers. Numerische Mathematik,
130(3):567–577, 2015.
[HY17]
R. Hannah and W. Yin.
More iterations per second, same quality –
Why asynchronous algorithms may drastically outperform traditional ones.
arXiv:1708.05136, 2017.
[HY18]
R. Hannah and W. Yin. On unbounded delays in asynchronous parallel fixed-
point algorithms. Journal of Scientific Computing, 76(1):299–326, 2018.
[HYD15]
C.-J. Hsieh, H.-F. Yu, and I. S. Dhillon. PASSCoDe: Parallel ASynchronous
Stochastic dual Co-Ordinate Descent. In International Conference on Ma-
chine Learning, Lille, France, 2015.
[HYW00]
B. S. He, H. Yang, and S. L. Wang. Alternating direction method with self-
adaptive penalty parameters for monotone variational inequalities. Journal
of Optimization Theory and Applications, 106(2):337–356, 2000.
[HYZ08]
E. T. Hale, W. Yin, and Y. Zhang.
Fixed-point continuation for ℓ1-
minimization: Methodology and convergence. SIAM Journal on Optimiza-
tion, 19(3):1107–1130, 2008.
[Ius99]
A. N. Iusem. Augmented Lagrangian methods and proximal point methods
for convex optimization. Investigación Operativa, 8(1–3):11–49, 1999.
[Jen06]
J. L. W. V. Jensen.
Sur les fonctions convexes et les inégalités entre les
valeurs moyennes. Acta Mathematica, 30(1):175–193, 1906.
[JXM14]
D. Jakovetić, J. Xavier, and J. M. F. Moura.
Fast distributed gradient
methods. IEEE Transactions on Automatic Control, 59(5):1131–1146, 2014.
[JZZ09]
R.-Q. Jia, H. Zhao, and W. Zhao. Convergence analysis of the Bregman
method for the variational model of image denoising. Applied and Compu-
tational Harmonic Analysis, 27(3):367–379, 2009.
[Kac60]
R. I. Kachurovskii. Monotone operators and convex functionals. Uspekhi
Matematicheskikh Nauk, 15(4):213–215, 1960.
[KDG03]
D. Kempe, A. Dobra, and J. Gehrke. Gossip-based computation of aggregate
information. In IEEE Symposium on Foundations of Computer Science, 2003.
[KF16]
D. Kim and J. A. Fessler. Optimized first-order methods for smooth convex
minimization. Mathematical Programming, 159(1–2):81–107, 2016.
[KF17]
D. Kim and J. A. Fessler.
On the convergence analysis of the opti-
mized gradient method. Journal of Optimization Theory and Applications,
172(1):187–205, 2017.
[KF21]
D. Kim and J. A. Fessler. Optimizing the efficiency of first-order methods for
decreasing the gradient of smooth convex functions. Journal of Optimization
Theory and Applications, 188(1):192–219, 2021.


## Page 328

References
313
[Kim21]
D. Kim. Accelerated proximal point method for maximally monotone oper-
ators. Mathematical Programming, 190(1–2):57–87, 2021.
[Kir34]
M. D. Kirszbraun. Über die zusammenziehende und Lipschitzsche Transfor-
mationen. Fundamenta Mathematicae, 22(1):77–108, 1934.
[KP15]
N. Komodakis and J.-C. Pesquet.
Playing with duality: An overview of
recent primal-dual approaches for solving large-scale optimization problems.
IEEE Signal Processing Magazine, 32(6):31–54, 2015.
[Kra55]
M. A. Krasnosel’skii. Two remarks on the method of successive approxima-
tions. Uspekhi Matematicheskikh Nauk, 10(1):123–127, 1955.
[Kra85]
E. Krauss.
A representation of maximal monotone operators by sad-
dle functions.
Revue Roumaine de Mathématique Pures et Appliquées,
30(10):823–837, 1985.
[KY03]
H. J. Kushner and G. G. Yin.
Stochastic Approximation and Recursive
Algorithms and Applications. Springer, second ed., 2003.
[KYW19]
S. Ko, D. Yu, and J.-H. Won. Easily parallelizable and distributable class
of algorithms for structured sparsity, with optimal acceleration. Journal of
Computational and Graphical Statistics, 28(4):821–833, 2019.
[LAP+14]
M. Li, D. G. Andersen, J. W. Park, A. J. Smola, A. Ahmed, V. Josifovski,
J. Long, E. J. Shekita, and B.-Y. Su. Scaling distributed machine learning
with the parameter server. In USENIX Conference on Operating Systems
Design and Implementation, 2014.
[LCZ14]
K. Lange, E. C. Chi, and H. Zhou. A brief survey of modern optimization
for statisticians. International Statistical Review, 82(1):46–70, 2014.
[Lem92]
B. Lemaire. About the convergence of the proximal method. In W. Oettli
and D. Pallaschke, eds., Advances in Optimization, pages 39–51. Springer,
1992.
[Lem01]
C. Lemaréchal. Lagrangian relaxation. In M. Jünger and D. Naddef, eds.,
Computational Combinatorial Optimization:
Optimal or Provably Near-
Optimal Solutions, Lecture Notes in Computer Science, pages 112–156.
Springer, 2001.
[LFP16]
J. Liang, J. Fadili, and G. Peyré.
Convergence rates with inexact non-
expansive operators. Mathematical Programming, 159(1):403–434, 2016.
[LFP17]
J. Liang, J. Fadili, and G. Peyré.
Local convergence properties of Dou-
glas–Rachford and alternating direction method of multipliers. Journal of
Optimization Theory and Applications, 172(3):874–913, 2017.
[LFYL20]
H. Li, C. Fang, W. Yin, and Z. Lin.
Decentralized accelerated gradient
methods with increasing penalty parameters. IEEE Transactions on Signal
Processing, 68:4855–4870, 2020.
[LHLL15]
X. Lian, Y. Huang, Y. Li, and J. Liu. Asynchronous parallel stochastic gradi-
ent for nonconvex optimization. In Neural Information Processing Systems,
2015.
[Lie21]
F. Lieder. On the convergence rate of the Halpern-iteration. Optimization
Letters, 15(2):405–418, 2021.
[Lin94]
E. Lindelöf.
Sur l’applications de la méthode des approximations succes-
sives aux équations différentielles ordinaires du premier ordre. Comptes Ren-
dus Hebdomadaires des Séances de l’Académie des Sciences, 116(3):454–456,
1894.
[LL10]
D. Leventhal and A. S. Lewis. Randomized methods for linear constraints:
Convergence rates and conditioning. Mathematics of Operations Research,
35(3):641–654, 2010.


## Page 329

314
References
[LM79]
P. L. Lions and B. Mercier. Splitting algorithms for the sum of two nonlinear
operators. SIAM Journal on Numerical Analysis, 16(6):964–979, 1979.
[LMH15]
H. Lin, J. Mairal, and Z. Harchaoui.
A universal catalyst for first-order
optimization. In Neural Information Processing Systems, 2015.
[LMH18]
H. Lin, J. Mairal, and Z. Harchaoui. Catalyst acceleration for first-order
convex optimization: From theory to practice. Journal of Machine Learning
Research, 18(212):1–54, 2018.
[LMT+10]
W. Liu, S. Ma, D. Tao, J. Liu, and P. Liu. Semi-supervised sparse metric
learning using alternating linearization optimization. In SIGKDD Interna-
tional Conference on Knowledge Discovery and Data Mining, 2010.
[LMYZ21]
T. Lin, S. Ma, Y. Ye, and S. Zhang. An ADMM-based interior-point method
for large-scale linear programming.
Optimization Methods and Software,
36(2-3):389–424, 2021.
[LMZ15a]
T. Lin, S. Ma, and S. Zhang. On the global linear convergence of the ADMM
with multiblock variables. SIAM Journal on Optimization, 25(3):1478–1497,
2015.
[LMZ15b]
T.-Y. Lin, S.-Q. Ma, and S.-Z. Zhang. On the sublinear convergence rate of
multi-block ADMM. Journal of the Operations Research Society of China,
3(3):251–274, 2015.
[LMZ16]
T. Lin, S. Ma, and S. Zhang. Iteration complexity analysis of multi-block
ADMM for a family of convex minimization without strong convexity. Jour-
nal of Scientific Computing, 69(1):52–81, 2016.
[LMZ17]
T. Lin, S. Ma, and S. Zhang. An extragradient-based alternating direction
method for convex minimization. Foundations of Computational Mathemat-
ics, 17(1):35–59, 2017.
[LO09]
Y. Li and S. Osher. Coordinate descent optimization for ℓ1 minimization with
application to compressed sensing; a greedy algorithm. Inverse Problems and
Imaging, 3(3):487–503, 2009.
[LP66]
E. S. Levitin and B. T. Polyak. Constrained minimization methods. Zhurnal
Vychislitel’noi Matematiki i Matematicheskoi Fiziki, 6(5):787–823, 1966.
[LP89]
B. Lemaire and J.-P. Penot. The proximal algorithm. In New Methods in
Optimization and Their Industrial Uses, volume 87, pages 73–87. Birkhäuser,
1989.
[LPL17]
R. Leblond, F. Pedregosa, and S. Lacoste-Julien. ASAGA: Asynchronous
parallel SAGA. In International Conference on Artificial Intelligence and
Statistics, 2017.
[LRY19]
Y. Liu, E. K. Ryu, and W. Yin.
A new use of Douglas–Rachford split-
ting for identifying infeasible, unbounded, and pathological conic programs.
Mathematical Programming, 177(1):225–253, 2019.
[LS87]
J. Lawrence and J. E. Spingarn. On fixed points of non-expansive piecewise
isometric mappings. Proceedings of the London Mathematical Society, s3-
55(3):605–624, 1987.
[LST15]
M. Li, D. Sun, and K.-C. Toh. A convergent 3-block semi-proximal ADMM
for convex minimization problems with one strongly convex block.
Asia-
Pacific Journal of Operational Research, 32(04):1550024, 2015.
[LST16]
X. Li, D. Sun, and K.-C. Toh. A Schur complement based semi-proximal
ADMM for convex quadratic conic programming and extensions. Mathemat-
ical Programming, 155(1):333–373, 2016.
[LST19]
X. Li, D. Sun, and K.-C. Toh. A block symmetric Gauss–Seidel decomposi-
tion theorem for convex composite quadratic programming and its applica-
tions. Mathematical Programming, 175(1):395–418, 2019.


## Page 330

References
315
[LSY19]
Z. Li, W. Shi, and M. Yan.
A decentralized proximal-gradient method
with network independent step-sizes and separated convergence rates. IEEE
Transactions on Signal Processing, 67(17):4494–4506, 2019.
[LT92]
Z.-Q. Luo and P. Tseng.
On the convergence of the coordinate descent
method for convex differentiable minimization. Journal of Optimization The-
ory and Applications, 72(1):7–35, 1992.
[LT10]
Q. Ling and Z. Tian. Decentralized sparse signal recovery for compressive
sleeping wireless sensor networks. IEEE Transactions on Signal Processing,
58(7):3816–3827, 2010.
[LUZ15]
Z. Li, A. Uschmajew, and S. Zhang. On convergence of the maximum block
improvement method. SIAM Journal on Optimization, 25(1):210–233, 2015.
[LV11]
I. Loris and C. Verhoeven.
On a generalization of the iterative soft-
thresholding algorithm for the case of non-separable penalty. Inverse Prob-
lems, 27(12):125007, 2011.
[LW15]
J. Liu and S. J. Wright.
Asynchronous stochastic coordinate descent:
Parallelism and convergence properties.
SIAM Journal on Optimization,
25(1):351–376, 2015.
[LW19]
C.-P. Lee and S. J. Wright. Random permutations fix a worst case for cyclic
coordinate descent. IMA Journal of Numerical Analysis, 39(3):1246–1275,
2019.
[LWR+14]
J. Liu, S. Wright, C. Re, V. Bittorf, and S. Sridhar. An asynchronous par-
allel stochastic coordinate descent algorithm. International Conference on
Machine Learning, 2014.
[LWR+15]
J. Liu, S. J. Wright, C. Ré, V. Bittorf, and S. Sridhar. An asynchronous par-
allel stochastic coordinate descent algorithm. Journal of Machine Learning
Research, 16(1):285–322, 2015.
[LY17]
Z. Li and M. Yan. A primal-dual algorithm with optimal stepsizes and its
application in decentralized consensus optimization. arXiv:1711.06785, 2017.
[LY19]
Y. Liu and W. Yin.
An envelope for Davis–Yin splitting and strict sad-
dle point avoidance.
Journal of Optimization Theory and Applications,
181(2):567–587, 2019.
[LZZ+17]
X. Lian, C. Zhang, H. Zhang, C.-J. Hsieh, W. Zhang, and J. Liu.
Can
decentralized algorithms outperform centralized algorithms? A case study
for decentralized parallel stochastic gradient descent. In Neural Information
Processing Systems, 2017.
[LZZL18]
X. Lian, W. Zhang, C. Zhang, and J. Liu. Asynchronous decentralized par-
allel stochastic gradient descent. In International Conference on Machine
Learning, 2018.
[Ma20]
F. Ma. A revisit of Chen–Teboulle’s proximal-based decomposition method.
arXiv:2006.11255, 2020.
[Mai13]
J. Mairal. Optimization with first-order surrogate functions. In International
Conference on Machine Learning, 2013.
[Mar70]
B. Martinet. Régularisation d’inéquations variationnelles par approximations
successives. Revue Française d’Informatique et de Recherche Opérationnelle,
Série Rouge, 4(3):154–158, 1970.
[Mar72a]
B. Martinet. Algorithmes Pour La Résolution de Problèmes d’optimisation
et de Minimax. PhD Thesis, Université Scientifique et Médicale de Grenoble,
1972.
[Mar72b]
B. Martinet.
Determination approchée d’un point fixe d’une application
pseudo-contractante. Comptes Rendus de l’Académie des Sciences, Série A,
274(2):163–165, 1972.


## Page 331

316
References
[MBG10]
G. Mateos, J. A. Bazerque, and G. B. Giannakis. Distributed sparse linear
regression. IEEE Transactions on Signal Processing, 58(10):5262–5276, 2010.
[Mer80]
B. Mercier. Inéquations Variationnelles de La Mécanique. Publications Math-
ématiques d’Orsay. Université de Paris-Sud, Département de mathématique,
1980.
[Min62]
G. J. Minty. Monotone (nonlinear) operators in Hilbert space. Duke Math-
ematical Journal, 29(3):341–346, 1962.
[Min64]
G. J. Minty.
On the monotonicity of the gradient of a convex function.
Pacific Journal of Mathematics, 14(1):243–247, 1964.
[MKS+20]
K. Mishchenko, D. Kovalev, E. Shulgin, P. Richtarik, and Y. Malitsky. Re-
visiting stochastic extragradient. In International Conference on Artificial
Intelligence and Statistics, 2020.
[MLZ+19]
P. Mertikopoulos, B. Lecouat, H. Zenati, C.-S. Foo, V. Chandrasekhar, and
G. Piliouras. Optimistic mirror descent in saddle-point problems: Going the
extra (gradient) mile. In International Conference on Learning Representa-
tions, 2019.
[Mor62]
J. J. Moreau. Fonctions convexes duales et points proximaux dans un espace
hilbertien. Comptes rendus hebdomadaires des séances de l’Académie des
sciences, 255:2897–2899, 1962.
[Mor65]
J. J. Moreau. Proximité et dualité dans un espace hilbertien. Bulletin de la
Société Mathématique de France, 93:273–299, 1965.
[MP65]
O. L. Mangasarian and J. Ponstein. Minmax and duality in nonlinear pro-
gramming. Journal of Mathematical Analysis and Applications, 11:504–518,
1965.
[MS13]
R. D. C. Monteiro and B. F. Svaiter.
Iteration-complexity of block-
decomposition algorithms and the alternating direction method of multi-
pliers. SIAM Journal on Optimization, 23(1):475–507, 2013.
[MV19]
W. M. Moursi and L. Vandenberghe.
Douglas–Rachford splitting for the
sum of a Lipschitz continuous and a strongly monotone operator. Journal of
Optimization Theory and Applications, 183(1):179–198, 2019.
[MXZ13]
S. Ma, L. Xue, and H. Zou. Alternating direction methods for latent variable
Gaussian graphical model selection. Neural Computation, 25(8):2172–2198,
2013.
[MZ19]
W. M. Moursi and Y. Zinchenko. A note on the equivalence of operator
splitting methods.
In H. H. Bauschke, R. S. Burachik, and D. R. Luke,
eds., Splitting Algorithms, Modern Operator Theory, and Applications, pages
331–349. Springer, 2019.
[Nes83]
Y. Nesterov.
A method of solving a convex programming problem with
convergence rate O(1/k2). Doklady Akademii Nauk SSSR, 269(3):543–547,
1983.
[Nes88]
Y. Nesterov. On an approach to the construction of optimal methods of min-
imization of smooth convex functions. Ekonomika i Mateaticheskie Metody,
24(3):509–517, 1988.
[Nes04]
Y. Nesterov. Introductory Lectures on Convex Optimization: A Basic Course.
Springer, 2004.
[Nes05]
Y. Nesterov. Smooth minimization of non-smooth functions. Mathematical
Programming, 103(1):127–152, 2005.
[Nes12]
Y. Nesterov. Efficiency of coordinate descent methods on huge-scale opti-
mization problems. SIAM Journal on Optimization, 22(2):341–362, 2012.


## Page 332

References
317
[Nes13]
Y. Nesterov. Gradient methods for minimizing composite functions. Math-
ematical Programming, 140(1):125–161, 2013.
[NGGD20]
Y. Nesterov, A. Gasnikov, S. Guminov, and P. Dvurechensky. Primal-dual
accelerated gradient methods with small-dimensional relaxation oracle. Op-
timization Methods and Software, pages 1–38, 2020.
[NJN19]
D. Nagaraj, P. Jain, and P. Netrapalli. SGD without replacement: Sharper
rates for general smooth convex functions. In International Conference on
Machine Learning, 2019.
[NO15]
A. Nedic and A. Olshevsky. Distributed optimization over time-varying di-
rected graphs.
IEEE Transactions on Automatic Control, 60(3):601–615,
2015.
[NOS17]
A. Nedić, A. Olshevsky, and W. Shi. Achieving geometric convergence for
distributed optimization over time-varying graphs. SIAM Journal on Opti-
mization, 27(4):2597–2633, 2017.
[NOSU17]
A. Nedić, A. Olshevsky, W. Shi, and C. A. Uribe. Geometrically convergent
distributed optimization with uncoordinated step-sizes. In American Control
Conference, 2017.
[NP06]
C. P. Niculescu and L.-E. Persson. Convex Functions and Their Applications.
CMS Books in Mathematics. Springer, 2006.
[NSL+15]
J. Nutini, M. Schmidt, I. H. Laradji, M. Friedlander, and H. Koepke. Coor-
dinate descent converges faster with the gauss-southwell rule than random
selection. In International Conference on Machine Learning, 2015.
[NY78]
A. Nemirovski and D. B. Yudin. Cezari convergence of the gradient method of
approximating saddle point of convex-concave functions. Doklady Akademii
Nauk SSSR, 239(5):1056–1059, 1978.
[OBG+05]
S. Osher, M. Burger, D. Goldfarb, J. Xu, and W. Yin. An iterative reg-
ularization method for total variation-based image restoration. Multiscale
Modeling and Simulation, 4(2):460–489, 2005.
[OCLPJ15] Y. Ouyang, Y. Chen, G. Lan, and E. Pasiliao Jr. An accelerated linearized
alternating direction method of multipliers. SIAM Journal on Imaging Sci-
ences, 8(1):644–681, 2015.
[OCPB16]
B. O’Donoghue, E. Chu, N. Parikh, and S. Boyd. Conic optimization via
operator splitting and homogeneous self-dual embedding. Journal of Opti-
mization Theory and Applications, 169(3):1042–1068, 2016.
[OHTG13]
H. Ouyang, N. He, L. Q. Tran, and A. Gray. Stochastic alternating direction
method of multipliers. In International Conference on Machine Learning,
2013.
[Opi67]
Z. Opial. Weak convergence of the sequence of successive approximations
for nonexpansive mappings. Bulletin of the American Mathematical Society,
73(4):591–597, 1967.
[OV20]
D. O’Connor and L. Vandenberghe. On the equivalence of the primal-dual
hybrid gradient method and Douglas–Rachford splitting. Mathematical Pro-
gramming, 179(1–2):85–108, 2020.
[OY02]
N. Ogura and I. Yamada. Non-strictly convex minimization over the fixed
point set of an asymptotically shrinking nonexpansive mapping. Numerical
Functional Analysis and Optimization, 23(1–2):113–137, 2002.
[Pas79]
G. B. Passty. Ergodic convergence to a zero of the sum of monotone oper-
ators in Hilbert space. Journal of Mathematical Analysis and Applications,
72(2):383–390, 1979.
[Pat21]
R. Pates. The scaled relative graph of a linear operator. arXiv:2106.05650,
2021.


## Page 333

318
References
[PB14a]
N. Parikh and S. Boyd. Block splitting for distributed optimization. Math-
ematical Programming Computation, 6(1):77–102, 2014.
[PB14b]
N. Parikh and S. Boyd. Proximal algorithms. Foundations and Trends in
Optimization, 1(3):127–239, 2014.
[PC06]
D. P. Palomar and M. Chiang. A tutorial on decomposition methods for
network utility maximization. IEEE Journal on Selected Areas in Commu-
nications, 24(8):1439–1451, 2006.
[PC11]
T. Pock and A. Chambolle. Diagonal preconditioning for first order primal-
dual algorithms in convex optimization. In International Conference on Com-
puter Vision, 2011.
[PCBC09]
T. Pock, D. Cremers, H. Bischof, and A. Chambolle.
An algorithm for
minimizing the Mumford-Shah functional. In International Conference on
Computer Vision, 2009.
[Ped70]
D. Pedoe. A Course Geometry for Colleges and Universities. Cambridge
University Press, 1970.
[Pen03]
J.-P. Penot. Is convexity useful for the study of monotonicity?
In R. P.
Agarwal and D. O’Regan, eds., Nonlinear Analysis and Applications: To
V. Lakshmikantham on His 80th Birthday, pages 807–822. Kluwer Academic
Publishers, 2003.
[Pen04]
J.-P. Penot. The relevance of convex analysis for the study of monotonicity.
Nonlinear Analysis: Theory, Methods and Applications, 58(7):855–871, 2004.
[Phe93]
R. R. Phelps. Convex Functions, Monotone Operators and Differentiability.
Springer-Verlag, second ed., 1993.
[Pic90]
É. Picard. Mémoire sur la théorie des équations aux dérivées partielles et la
méthode des approximations successives. Journal de Mathématiques Pures
et Appliquées 4éme Série, 6(2):145–210, 1890.
[Pie84]
G. Pierra. Decomposition through formalization in a product space. Math-
ematical Programming, 28(1):96–115, 1984.
[PLL17]
F. Pedregosa, R. Leblond, and S. Lacoste-Julien. Breaking the nonsmooth
barrier: A scalable parallel method for composite optimization. In Neural
Information Processing Systems, 2017.
[PLS08]
L. A. Parente, P. A. Lotito, and M. V. Solodov. A class of inexact vari-
able metric proximal point algorithms.
SIAM Journal on Optimization,
19(1):240–260, 2008.
[PN15]
A. Patrascu and I. Necoara. Efficient random coordinate descent algorithms
for large-scale structured nonconvex optimization. Journal of Global Opti-
mization, 61(1):19–46, 2015.
[Pol87]
B. T. Polyak. Introduction to Optimization. Optimization Software, 1987.
[Pol90]
B. T. Polyak. New method of stochastic approximation type. Automat. i
Telemekh, 51(7):98–107, 1990.
[Pow69]
M. J. D. Powell. A method for nonlinear constraints in minimization prob-
lems.
In R. Fletcher, ed., Optimization:
Symposium of the Institute of
Mathematics and Its Applications, University of Keele, England, 1968, pages
283–298. Academic Press, 1969.
[PR55]
D. W. Peaceman and J. Rachford, H. H. The numerical solution of parabolic
and elliptic differential equations. Journal of the Society for Industrial and
Applied Mathematics, 3(1):28–41, 1955.
[PR15]
J.-C. Pesquet and A. Repetti. A class of randomized primal-dual algorithms
for distributed optimization.
Journal of Nonlinear and Convex Analysis,
16(12):2453–2490, 2015.


## Page 334

References
319
[PS10]
J. Peypouquet and S. Sorin.
Evolution equations for maximal monotone
operators: Asymptotic analysis in continuous and discrete time. Journal of
Convex Analysis, 17(3–4):1113–1163, 2010.
[PSB14]
P. Patrinos, L. Stella, and A. Bemporad. Douglas–Rachford splitting: Com-
plexity estimates and accelerated variants. In IEEE Conference on Decision
and Control, 2014.
[PWX+16]
Z. Peng, T. Wu, Y. Xu, M. Yan, and W. Yin. Coordinate-friendly struc-
tures, algorithms and applications. Annals of Mathematical Sciences and
Applications, 1(1):57–119, 2016.
[PXYY16]
Z. Peng, Y. Xu, M. Yan, and W. Yin. ARock: An algorithmic framework
for asynchronous parallel coordinate updates. SIAM Journal on Scientific
Computing, 38(5):A2851–A2879, 2016.
[PXYY19]
Z. Peng, Y. Xu, M. Yan, and W. Yin. On the convergence of asynchronous
parallel iteration with unbounded delays. Journal of the Operations Research
Society of China, 7(1):5–42, 2019.
[PYY13]
Z. Peng, M. Yan, and W. Yin. Parallel and distributed sparse optimization.
In Asilomar Conference on Signals, Systems and Computers. IEEE, 2013.
[QL18]
G. Qu and N. Li. Harnessing smoothness to accelerate distributed optimiza-
tion. IEEE Transactions on Control of Network Systems, 5(3):1245–1260,
2018.
[QL20]
G. Qu and N. Li. Accelerated distributed Nesterov gradient descent. IEEE
Transactions on Automatic Control, 65(6):2566–2581, 2020.
[QR16a]
Z. Qu and P. Richtárik. Coordinate descent with arbitrary sampling I: Algo-
rithms and complexity. Optimization Methods and Software, 31(5):829–857,
2016.
[QR16b]
Z. Qu and P. Richtárik.
Coordinate descent with arbitrary sampling II:
Expected separable overapproximation. Optimization Methods and Software,
31(5):858–884, 2016.
[QSMR19]
X. Qian, A. Sailanbayev, K. Mishchenko, and P. Richtárik. MISO is making
a comeback with better proofs and rates. arXiv:1906.01474, 2019.
[Rag19]
H. Raguet.
A note on the forward-Douglas–Rachford splitting for mono-
tone inclusion and convex optimization. Optimization Letters, 13(4):717–740,
2019.
[Ray13]
M. Raynal. Concurrent Programming: Algorithms, Principles, and Founda-
tions: Algorithms, Principles, and Foundations. Springer-Verlag, 2013.
[RB16]
E. K. Ryu and S. Boyd. Primer on monotone operator methods. Applied
and Computational Mathematics, 15(1):3–43, 2016.
[RDC14]
A. U. Raghunathan and S. Di Cairano. ADMM for convex quadratic pro-
grams: Q-linear convergence and infeasibility detection. arXiv:1411.7288,
2014.
[Rei79]
S. Reich. Weak convergence theorems for nonexpansive mappings in Banach
spaces. Journal of Mathematical Analysis and Applications, 67(2):274–276,
1979.
[Rei85]
S. Reich. Averaged mappings in the Hilbert ball. Journal of Mathematical
Analysis and Applications, 109(1):199–206, 1985.
[RFP13]
H. Raguet, J. Fadili, and G. Peyré. A generalized forward-backward splitting.
SIAM Journal on Imaging Sciences, 6(3):1199–1226, 2013.
[RGP20]
S. Rajput, A. Gupta, and D. Papailiopoulos. Closing the convergence gap of
SGD without replacement. In International Conference on Machine Learn-
ing, 2020.


## Page 335

320
References
[RHL13]
M. Razaviyayn, M. Hong, and Z.-Q. Luo. A unified convergence analysis of
block successive minimization methods for nonsmooth optimization. SIAM
Journal on Optimization, 23(2):1126–1153, 2013.
[RHY21]
E. K. Ryu, R. Hannah, and W. Yin. Scaled relative graphs: Nonexpansive
operators via 2D Euclidean geometry. Mathematical Programming, 2021.
[RKW20]
E. K. Ryu, S. Ko, and J.-H. Won. Splitting with near-circulant linear systems:
Applications to total variation CT and PET. SIAM Journal on Scientific
Computing, 42(1):B185–B206, 2020.
[RLW+19]
E. Ryu, J. Liu, S. Wang, X. Chen, Z. Wang, and W. Yin. Plug-and-play
methods provably converge with properly trained denoisers. In International
Conference on Machine Learning, 2019.
[RLY19]
E. K. Ryu, Y. Liu, and W. Yin. Douglas–Rachford splitting and ADMM for
pathological convex optimization. Computational Optimization and Applica-
tions, 74(3):747–778, 2019.
[RM51]
H. Robbins and S. Monro. A stochastic approximation method. The Annals
of Mathematical Statistics, 22(3):400–407, 1951.
[Rob99]
S. M. Robinson. Composition duality and maximal monotonicity. Mathe-
matical Programming, 85(1):1–13, 1999.
[Roc64]
R. T. Rockafellar. Minimax theorems and conjugate saddle-functions. Math-
ematica Scandinavica, 14(2):151–173, 1964.
[Roc66]
R. T. Rockafellar. Characterization of the subdifferentials of convex func-
tions. Pacific Journal of Mathematics, 17(3):497–510, 1966.
[Roc68]
R. T. Rockafellar. A general correspondence between dual minimax problems
and convex programs. Pacific Journal of Mathematics, 25(3):597–611, 1968.
[Roc69]
R. T. Rockafellar. Measurable dependence of convex sets and functions on
parameters. Journal of Mathematical Analysis and Applications, 28(1):4–25,
1969.
[Roc70a]
R. T. Rockafellar. Monotone operators associated with saddle-functions and
minimax problems. In F. E. Browder, ed., Nonlinear Functional Analysis,
Part 1, volume 18 of Proceedings of Symposia in Pure Mathematics, pages
241–250. American Mathematical Society, 1970.
[Roc70b]
R. T. Rockafellar. On the maximal monotonicity of subdifferential mappings.
Pacific Journal of Mathematics, 33(1):209–216, 1970.
[Roc70c]
R. T. Rockafellar. On the maximality of sums of nonlinear monotone op-
erators. Transactions of the American Mathematical Society, 149(1):75–88,
1970.
[Roc70d]
R. T. Rockafellar. Convex Analysis. Princeton University Press, 1970.
[Roc73]
R. T. Rockafellar. The multiplier method of Hestenes and Powell applied
to convex programming. Journal of Optimization Theory and Applications,
12(6):555–562, 1973.
[Roc74]
R. T. Rockafellar. Conjugate Duality and Optimization. CBMS-NSF Re-
gional Conference Series in Applied Mathematics. Society for Industrial and
Applied Mathematics, 1974.
[Roc76a]
R. T. Rockafellar. Augmented Lagrangians and applications of the prox-
imal point algorithm in convex programming. Mathematics of Operations
Research, 1(2):97–116, 1976.
[Roc76b]
R. T. Rockafellar. Monotone operators and the proximal point algorithm.
SIAM Journal on Control and Optimization, 14(5):877–898, 1976.
[Roc78]
R. T. Rockafellar. Monotone operators and augmented Lagrangian methods
in nonlinear programming. In O. L. Mangasarian, R. R. Meyer, and S. M.
Robinson, eds., Nonlinear Programming 3, pages 1–25. Academic Press, 1978.


## Page 336

References
321
[Ros69]
J. L. Rosenfeld. A case study in programming for parallel-processors. Com-
munications of The ACM, 12(12):645–655, 1969.
[RRWN11]
B. Recht, C. Re, S. Wright, and F. Niu. Hogwild!: A lock-free approach to
parallelizing stochastic gradient descent. In Neural Information Processing
Systems, 2011.
[RS81]
S. F. Roehrig and R. C. Sine. The structure of ω-limit sets of nonexpansive
maps.
Proceedings of the American Mathematical Society, 81(3):398–400,
1981.
[RS85]
H. Robbins and D. Siegmund. A convergence theorem for non negative almost
supermartingales and some applications. In T. L. Lai and D. Siegmund, eds.,
Herbert Robbins Selected Papers, pages 111–135. Springer, 1985.
[RS98]
S. Reich and D. Shoikhet.
Averages of holomorphic mappings and holo-
morphic retractions on convex hyperbolic domains.
Studia Mathematica,
130(3):231–244, 1998.
[RT14]
P. Richtárik and M. Takáč.
Iteration complexity of randomized block-
coordinate descent methods for minimizing a composite function. Mathe-
matical Programming, 144(1):1–38, 2014.
[RT16]
P. Richtárik and M. Takáč. On optimal probabilities in stochastic coordinate
descent methods. Optimization Letters, 10(6):1233–1243, 2016.
[RTBG20]
E. K. Ryu, A. B. Taylor, C. Bergeling, and P. Giselsson. Operator splitting
performance estimation: Tight contraction factors and optimal parameter
selection. SIAM Journal on Optimization, 30(3):2251–2271, 2020.
[Rup88]
D. Ruppert. Efficient estimations from a slowly convergent Robbins–Monro
process. ORIE Technical Reports 781, Cornell University Operations Re-
search and Industrial Engineering, 1988.
[RVV16]
L. Rosasco, S. Villa, and B. C. Vũ. Stochastic forward-backward splitting
for monotone inclusions. Journal of Optimization Theory and Applications,
169(2):388–406, 2016.
[RYY19]
E. K. Ryu, K. Yuan, and W. Yin.
ODE analysis of stochastic gradient
methods with optimism and anchoring for minimax problems and GANs.
arXiv:1905.10899, 2019.
[SBB+17]
K. Seaman, F. Bach, S. Bubeck, Y. T. Lee, and L. Massoulié. Optimal algo-
rithms for smooth and strongly convex distributed optimization in networks.
In International Conference on Machine Learning, 2017.
[SBB+18]
K. Scaman, F. Bach, S. Bubeck, L. Massoulié, and Y. T. Lee.
Optimal
algorithms for non-smooth distributed optimization in networks. In Neural
Information Processing Systems, 2018.
[SBB+19]
K. Scaman, F. Bach, S. Bubeck, Y. T. Lee, and L. Massoulié.
Optimal
convergence rates for convex distributed optimization in networks. Journal
of Machine Learning Research, 20(159):1–31, 2019.
[SBG+20]
B. Stellato, G. Banjac, P. Goulart, A. Bemporad, and S. Boyd. OSQP: An
operator splitting solver for quadratic programs. Mathematical Programming
Computation, 12(4):637–672, 2020.
[Sch57]
H. Schaefer. Über die methode sukzessiver approximationen. Jahresbericht
der Deutschen Mathematiker-Vereinigung, 59:131–140, 1957.
[SCMR20]
A. Salim, L. Condat, K. Mishchenko, and P. Richtárik. Dualize, split, ran-
domize: Fast nonsmooth optimization algorithms. NeurIPS 2020 Workshop
OPT2020: Optimization for Machine Learning, 2020.
[SGJ11]
D. Sontag, A. Globerson, and T. Jaakkola. Introduction to dual decomposi-
tion for inference. In S. Sra, S. Nowozin, and S. J. Wright, eds., Optimization
for Machine Learning, pages 219–254. The Massachusetts Institute of Tech-
nology Press, 2011.


## Page 337

322
References
[SH15]
R. Sun and M. Hong. Improved iteration complexity bounds of cyclic block
coordinate descent for convex problems. In Neural Information Processing
Systems, 2015.
[Sho62]
N. Z. Shor. An application of the method of gradient descent to the solu-
tion of the network transportation problem. Materialy Naucnovo Seminara
po Teoret i Priklad. Voprosam Kibernet. i Issted. Operacii, Nucnyi Sov. po
Kibernet, Akad. Nauk Ukrain. SSSR, vyp, 1:9–17, 1962.
[Sho64]
N. Z. Shor. On the Structure of Algorithms for Numerical Solution of Prob-
lems of Optimal Planning and Design. PhD Thesis, Institute of Mathematics
of National Academy of Sciences of Ukraine, 1964.
[Sho85]
N. Z. Shor.
Minimization Methods for Non-Differentiable Functions.
Springer-Verlag, 1985.
[Sho97]
R. E. Showalter. Montone Operators in Banach Space and Nonlinear Partial
Differential Equations. American Mathematical Society, 1997.
[SHY17]
T. Sun, R. Hannah, and W. Yin. Asynchronous coordinate descent under
more realistic assumptions. In Neural Information Processing Systems, 2017.
[Sil72]
G. J. Silverman.
Primal decomposition of mathematical programs by re-
source allocation: I. Basic theory and a direction-finding procedure. Opera-
tions Research, 20(1):58–74, 1972.
[SK03]
S. K. Shevade and S. S. Keerthi. A simple and efficient algorithm for gene
selection using sparse logistic regression. Bioinformatics, 19(17):2246–2253,
2003.
[Sla50]
M. Slater. Lagrange multipliers revisited: A contribution to non-linear pro-
gramming. Cowles Commision Discussion Papers Math 403, Cowles Foun-
dation for Research in Economics, 1950.
[SLWY15a] W. Shi, Q. Ling, G. Wu, and W. Yin. EXTRA: An exact first-order algorithm
for decentralized consensus optimization. SIAM Journal on Optimization,
25(2):944–966, 2015.
[SLWY15b] W. Shi, Q. Ling, G. Wu, and W. Yin. A proximal gradient algorithm for
decentralized composite optimization. IEEE Transactions on Signal Process-
ing, 63(22):6013–6023, 2015.
[SLY+14]
W. Shi, Q. Ling, K. Yuan, G. Wu, and W. Yin. On the linear convergence
of the ADMM in decentralized consensus optimization. IEEE Transactions
on Signal Processing, 62(7):1750–1761, 2014.
[SLY20]
R. Sun, Z.-Q. Luo, and Y. Ye. On the efficiency of random permutation
for ADMM and coordinate descent. Mathematics of Operations Research,
45(1):233–271, 2020.
[SN10]
A. Smola and S. Narayanamurthy. An architecture for parallel topic models.
Proceedings of the VLDB Endowment, 3(1–2):703–710, 2010.
[Spi83]
J. E. Spingarn. Partial inverse of a monotone operator. Applied Mathematics
and Optimization, 10(1):247–265, 1983.
[Spi85]
J. E. Spingarn.
Applications of the method of partial inverses to convex
programming: Decomposition. Mathematical Programming, 32(2):199–223,
1985.
[SRG08]
I. D. Schizas, A. Ribeiro, and G. B. Giannakis. Consensus in ad hoc WSNs
with noisy links – Part I: Distributed estimation of deterministic signals.
IEEE Transactions on Signal Processing, 56(1):350–364, 2008.
[SS86]
F. Santosa and W. W. Symes.
Linear inversion of band-limited reflec-
tion seismograms. SIAM Journal on Scientific and Statistical Computing,
7(4):1307–1330, 1986.


## Page 338

References
323
[SS17]
S. Sabach and S. Shtern. A first order method for solving convex bilevel
optimization problems. SIAM Journal on Optimization, 27(2):640–660, 2017.
[ST09]
S. Shalev-Shwartz and A. Tewari. Stochastic methods for ℓ1 regularized loss
minimization. In International Conference on Machine Learning, Montreal,
Quebec, Canada, 2009.
[ST11]
S. Shalev-Shwartz and A. Tewari. Stochastic methods for ℓ1 regularized loss
minimization. The Journal of Machine Learning Research, 12(52):1865–1892,
2011.
[ST13]
A. Saha and A. Tewari. On the nonasymptotic convergence of cyclic co-
ordinate descent methods. SIAM Journal on Optimization, 23(1):576–601,
2013.
[ST14]
R. Shefi and M. Teboulle. Rate of convergence analysis of decomposition
methods based on the proximal method of multipliers for convex minimiza-
tion. SIAM Journal on Optimization, 24(1):269–297, 2014.
[Ste46]
M. Stewart. Some General Theorems of Considerable Use in the Higher Parts
of Mathematics. W. Sands, A. Murray, and J. Cochran, 1746.
[Sto63]
J. Stoer. Duality in nonlinear programming and the minimax theorem. Nu-
merische Mathematik, 5(1):371–379, 1963.
[Sto64]
J. Stoer. Über einen Dualitätssatz der nichtlinearen programmierung. Nu-
merische Mathematik, 6(1):55–58, 1964.
[Str69]
V. Strassen. Gaussian elimination is not optimal. Numerische Mathematik,
13(4):354–356, 1969.
[STXY17]
H.-J. M. Shi, S. Tu, Y. Xu, and W. Yin. A primer on coordinate descent
algorithms. arXiv:1610.00040, 2017.
[STY15]
D. Sun, K.-C. Toh, and L. Yang. A convergent 3-block SemiProximal alter-
nating direction method of multipliers for conic programming with 4-Type
constraints. SIAM Journal on Optimization, 25(2):882–915, 2015.
[Suz13]
T. Suzuki. Dual averaging and proximal gradient descent for online alter-
nating direction multiplier method. In International Conference on Machine
Learning, 2013.
[Suz14]
T. Suzuki.
Stochastic dual coordinate ascent with alternating direction
method of multipliers. In International Conference on Machine Learning,
2014.
[SXB14]
J. V. Shi, Y. Xu, and R. G. Baraniuk. Sparse bilinear logistic regression.
UCLA CAM Reports 14-12, University of California, Los Angeles, 2014.
[SY21]
R. Sun and Y. Ye. Worst-case complexity of cyclic coordinate descent: O(n2)
gap with randomized version. Mathematical Programming, 185(1):487–520,
2021.
[SZ04]
S. Simons and C. Zălinescu. A new proof for Rockafellar’s characterization
of maximal monotone operators. Proceedings of the American Mathematical
Society, 132(10):2969–2972, 2004.
[SZ05]
S. Simons and C. Zălinescu. Fenchel duality, Fitzpatrick functions and max-
imal monotonicity. Journal of Nonlinear and Convex Analysis, 6(1):1–22,
2005.
[SZ13]
S. Shalev-Shwartz and T. Zhang. Stochastic dual coordinate ascent methods
for regularized loss. Journal of Machine Learning Research, 14(1):567–599,
2013.
[Tao14]
M. Tao.
Some parallel splitting methods for separable convex program-
ming with the o(1/t) convergence rate.
Pacific Journal on Optimization,
10(2):359–384, 2014.


## Page 339

324
References
[TB87]
P. Tseng and D. P. Bertsekas. Relaxation methods for problems with strictly
convex separable costs and linear constraints. Mathematical Programming,
38(3):303–321, 1987.
[TB19]
A. Taylor and F. Bach. Stochastic first-order methods: Non-asymptotic and
computer-aided analyses via potential functions. In Conference on Learning
Theory, 2019.
[TBT90]
P. Tseng, D. P. Bertsekas, and J. N. Tsitsiklis. Partially asynchronous, par-
allel algorithms for network flow and other problems.
SIAM Journal on
Control and Optimization, 28(3):678–710, 1990.
[TE05]
L. N. Trefethen and M. Embree. Spectra and Pseudospectra: The Behavior
of Nonnormal Matrices and Operators. Princeton University Press, 2005.
[THG17]
A. B. Taylor, J. M. Hendrickx, and F. Glineur. Smooth strongly convex in-
terpolation and exact worst-case performance of first-order methods. Math-
ematical Programming, 161(1):307–345, 2017.
[Tib96]
R. Tibshirani. Regression shrinkage and selection via the Lasso. Journal
of the Royal Statistical Society: Series B (Methodological), 58(1):267–288,
1996.
[TP20]
A. Themelis and P. Patrinos. Douglas–Rachford splitting and ADMM for
nonconvex optimization: Tight convergence results. SIAM Journal on Opti-
mization, 30(1):149–181, 2020.
[Tse90a]
P. Tseng. Dual ascent methods for problems with strictly convex costs and
linear constraints: A unified approach. SIAM Journal on Control and Opti-
mization, 28(1):214–242, 1990.
[Tse90b]
P. Tseng. Further applications of a splitting algorithm to decomposition in
variational inequalities and convex programming. Mathematical Program-
ming, 48(1):249–263, 1990.
[Tse91]
P. Tseng. Applications of a splitting algorithm to decomposition in convex
programming and variational inequalities. SIAM Journal on Control and
Optimization, 29(1):119–138, 1991.
[Tse01]
P. Tseng. Convergence of a block coordinate descent method for nondiffer-
entiable minimization.
Journal of Optimization Theory and Applications,
109(3):475–494, 2001.
[Tse08]
P. Tseng.
On accelerated proximal gradient methods for convex-concave
optimization. submitted to SIAM Journal on Optimization, 2008.
[TTM11]
H.
Terelius,
U.
Topcu,
and
R.
M.
Murray.
Decentralized
multi-
agent optimization via dual decomposition.
IFAC Proceedings Volumes,
44(1):11245–11251, 2011.
[TY09]
P. Tseng and S. Yun. A coordinate gradient descent method for nonsmooth
separable minimization.
Mathematical Programming, 117(1–2):387–423,
2009.
[TY12]
M. Tao and X. Yuan. An inexact parallel splitting augmented Lagrangian
method for monotone variational inequalities with separable structures.
Computational Optimization and Applications, 52(2):439–461, 2012.
[TY18]
M. Tao and X. Yuan. On Glowinski’s open question on the alternating direc-
tion method of multipliers. Journal of Optimization Theory and Applications,
179(1):163–196, 2018.
[ULGN21]
C. A. Uribe, S. Lee, A. Gasnikov, and A. Nedić. A dual approach for optimal
algorithms in distributed optimization over networks. Optimization Methods
and Software, 36(1), 2021.


## Page 340

References
325
[Val43]
F. A. Valentine.
On the extension of a vector function so as to preserve
a Lipschitz condition.
Bulletin of the American Mathematical Society,
49(2):100–108, 1943.
[Val45]
F. A. Valentine.
A Lipschitz condition preserving extension for a vector
function. American Journal of Mathematics, 67(1):83–93, 1945.
[Ver96]
M. Verkama. Random relaxation of fixed-point iteration. SIAM Journal on
Scientific Computing, 17(4):906–912, 1996.
[VSFL18]
B. Van Scoy, R. A. Freeman, and K. M. Lynch. The fastest known glob-
ally convergent first-order method for minimizing strongly convex functions.
IEEE Control Systems Letters, 2(1):49–54, 2018.
[Vũ13a]
B. C. Vũ. A splitting algorithm for dual monotone inclusions involving co-
coercive operators. Advances in Computational Mathematics, 38(3):667–681,
2013.
[Vũ13b]
B. C. Vũ.
A variable metric extension of the forward-backward-forward
algorithm for monotone operators. Numerical Functional Analysis and Op-
timization, 34(9):1050–1065, 2013.
[War63]
J. Warga. Minimizing certain convex functions. Journal of the Society for
Industrial and Applied Mathematics, 11(3):588–593, 1963.
[WB12]
H. Wang and A. Banerjee. Online alternating direction method. In Interna-
tional Conference on Machine Learning, 2012.
[WGY10]
Z. Wen, D. Goldfarb, and W. Yin.
Alternating direction augmented La-
grangian methods for semidefinite programming. Mathematical Programming
Computation, 2(3–4):203–230, 2010.
[WHML15] X. Wang, M. Hong, S. Ma, and Z.-Q. Luo. Solving multiple-block separable
convex minimization problems using two-block alternating direction method
of multipliers. Pacific Journal of Optimization, 11(4):645–667, 2015.
[WL08]
T. T. Wu and K. Lange. Coordinate descent algorithms for Lasso penalized
regression. The Annals of Applied Statistics, 2(1):224–244, 2008.
[WL20]
S. J. Wright and C.-P. Lee. Analyzing random permutations for cyclic coor-
dinate descent. Mathematics of Computation, 89(325):2217–2248, 2020.
[WN11]
H. F. Walker and P. Ni. Anderson acceleration for fixed-point iterations.
SIAM Journal on Numerical Analysis, 49(4):1715–1735, 2011.
[WO13]
E. Wei and A. Ozdaglar. On the O(1/k) convergence of asynchronous dis-
tributed alternating direction method of multipliers. In Global Conference
on Signal and Information Processing, 2013.
[Woh17]
B. Wohlberg.
ADMM penalty parameter selection by residual balancing.
arXiv:1704.06209, 2017.
[Wri15]
S. J. Wright. Coordinate descent algorithms. Mathematical Programming,
151(1):3–34, 2015.
[WS17]
J. J. Wang and W. Song. An algorithm twisted from generalized ADMM
for multi-block separable convex minimization models. Journal of Compu-
tational and Applied Mathematics, 309:342–358, 2017.
[WYL+18]
T. Wu, K. Yuan, Q. Ling, W. Yin, and A. H. Sayed. Decentralized consensus
optimization with asynchrony and delays. IEEE Transactions on Signal and
Information Processing over Networks, 4(2):293–307, 2018.
[WYYZ08]
Y. Wang, J. Yang, W. Yin, and Y. Zhang. A new alternating minimization
algorithm for total variation image reconstruction. SIAM Journal on Imaging
Sciences, 1(3):248–272, 2008.
[XB04]
L. Xiao and S. Boyd. Fast linear iterations for distributed averaging. Systems
and Control Letters, 53(1):65–78, 2004.


## Page 341

326
References
[XFG17]
Z. Xu, M. Figueiredo, and T. Goldstein. Adaptive ADMM with spectral
penalty parameter selection. In International Conference on Artificial Intel-
ligence and Statistics, 2017.
[XFY+17]
Z. Xu, M. A. T. Figueiredo, X. Yuan, C. Studer, and T. Goldstein. Adap-
tive relaxed ADMM: Convergence theory and practical implementation. In
Computer Vision and Pattern Recognition, 2017.
[XLLY17]
Y. Xu, M. Liu, Q. Lin, and T. Yang. ADMM without a fixed penalty pa-
rameter: Faster convergence with new adaptive penalization. In Neural In-
formation Processing Systems, 2017.
[Xu07]
M. H. Xu.
Proximal alternating directions method for structured vari-
ational inequalities.
Journal of Optimization Theory and Applications,
134(1):107–117, 2007.
[Xu15]
Y. Xu. Alternating proximal gradient method for sparse nonnegative Tucker
decomposition. Mathematical Programming Computation, 7(1):39–70, 2015.
[Xu17]
Y. Xu.
Accelerated first-order primal-dual proximal methods for linearly
constrained composite convex programming. SIAM Journal on Optimization,
27(3):1459–1484, 2017.
[XXS19]
P. Xiao, Z. Xiao, and R. Sun. Understanding limitation of two symmetrized
orders by worst-case complexity. arXiv:1910.04366, 2019.
[XY13]
Y. Xu and W. Yin. A block coordinate descent method for regularized mul-
ticonvex optimization with applications to nonnegative tensor factorization
and completion. SIAM Journal on Imaging Sciences, 6(3):1758–1789, 2013.
[XY17]
Y. Xu and W. Yin. A globally convergent algorithm for nonconvex opti-
mization based on block coordinate update. Journal of Scientific Computing,
72(2):700–734, 2017.
[XYLC19]
L. Xiao, A. W. Yu, Q. Lin, and W. Chen. DSCOVR: Randomized primal-
dual block coordinate algorithms for asynchronous distributed optimization.
Journal of Machine Learning Research, 20(43):1–58, 2019.
[XZSX15]
J. Xu, S. Zhu, Y. C. Soh, and L. Xie. Augmented distributed gradient meth-
ods for multi-agent optimization under uncoordinated constant stepsizes. In
IEEE Conference on Decision and Control, 2015.
[Yan18a]
M. Yan.
A new primal-dual algorithm for minimizing the sum of
three functions with a linear operator.
Journal of Scientific Computing,
76(3):1698–1717, 2018.
[Yan18b]
M. Yan.
Primal-dual algorithms for the sum of two and three functions.
Lecture Slides, https://mingyan08.github.io/Slides/PD3O.pdf, Michigan
State University, 2018.
[YLY16]
K. Yuan, Q. Ling, and W. Yin. On the convergence of decentralized gradient
descent. SIAM Journal on Optimization, 26(3):1835–1854, 2016.
[YO13]
W. Yin and S. Osher. Error forgetting of Bregman iteration. Journal of
Scientific Computing, 54(2–3):684–695, 2013.
[YOGD08]
W. Yin, S. Osher, D. Goldfarb, and J. Darbon. Bregman iterative algorithms
for ℓ1-minimization with applications to compressed sensing. SIAM Journal
on Imaging Sciences, 1(1):143–168, 2008.
[YP19]
P. Yi and L. Pavel. Distributed generalized Nash equilibria computation of
monotone games via double-layer preconditioned proximal-point algorithms.
IEEE Transactions on Control of Network Systems, 6(1):299–311, 2019.
[YT11]
S. Yun and K.-C. Toh.
A coordinate gradient descent method for ℓ1-
regularized convex minimization. Computational Optimization and Appli-
cations, 48(2):273–307, 2011.


## Page 342

References
327
[YTT11]
S. Yun, P. Tseng, and K.-C. Toh. A block coordinate gradient descent method
for regularized convex separable optimization and covariance selection. Math-
ematical Programming, 129(2):331–355, 2011.
[Yua12]
X. Yuan. Alternating direction method for covariance selection models. Jour-
nal of Scientific Computing, 51(2):261–273, 2012.
[YY13a]
J. Yang and X. Yuan. Linearized augmented Lagrangian and alternating
direction methods for nuclear norm minimization. Mathematics of Compu-
tation, 82(281):301–329, 2013.
[YY13b]
X. Yuan and J. Yang. Sparse and low-rank matrix decomposition via alter-
nating direction methods. Pacific Journal on Optimization, 9(1):167–180,
2013.
[YY16]
M. Yan and W. Yin. Self equivalence of the alternating direction method of
multipliers. In R. Glowinski, S. J. Osher, and W. Yin, eds., Splitting Meth-
ods in Communication, Imaging, Science and Engineering, pages 165–194.
Springer, 2016.
[YYZS19a]
K. Yuan, B. Ying, X. Zhao, and A. H. Sayed. Exact diffusion for distributed
optimization and learning — Part I: Algorithm development. IEEE Trans-
actions on Signal Processing, 67(3):708–723, 2019.
[YYZS19b]
K. Yuan, B. Ying, X. Zhao, and A. H. Sayed. Exact diffusion for distributed
optimization and learning — Part II: Convergence analysis. IEEE Transac-
tions on Signal Processing, 67(3):724–739, 2019.
[YZ11]
J. Yang and Y. Zhang. Alternating direction algorithms for ℓ1-problems in
compressive sensing. SIAM Journal on Scientific Computing, 33(1):250–278,
2011.
[Zad70]
N. Zadeh. Note – A note on the cyclic coordinate ascent method. Manage-
ment Science, 16(9):642–644, 1970.
[Zăl05]
C. Zălinescu. A new proof of the maximal monotonicity of the sum using
the Fitzpatrick function. In F. Giannessi and A. Maugeri, eds., Variational
Analysis and Applications, pages 1159–1172. Springer, 2005.
[Zar60]
E. H. Zarantonello. Solving functional equations by contractive averaging.
Technical Report 160, Mathematics Research Center, United States Army,
University of Wisconsin, 1960.
[ZBO11]
X. Zhang, M. Burger, and S. Osher.
A unified primal-dual algorithm
framework based on Bregman iteration. Journal of Scientific Computing,
46(1):20–46, 2011.
[ZC08]
M. Zhu and T. Chan. An efficient primal-dual hybrid gradient algorithm for
total variation image restoration. UCLA CAM Reports 08-34, University of
California, Los Angeles, 2008.
[Zha04]
T. Zhang. Solving large scale linear prediction problems using stochastic gra-
dient descent algorithms. In International Conference on Machine Learning,
2004.
[ZK14a]
R. Zhang and J. Kwok.
Asynchronous distributed ADMM for consensus
optimization. In International Conference on Machine Learning, 2014.
[ZK14b]
W. Zhong and J. T. Kwok. Fast stochastic alternating direction method of
multipliers. In International Conference on Machine Learning, 2014.
[ZK16]
S. Zheng and J. T. Kwok. Fast-and-light stochastic ADMM. In International
Joint Conference on Artificial Intelligence, 2016.
[ZM10]
M. Zhu and S. Martínez. Discrete-time dynamic average consensus. Auto-
matica, 46(2):322–329, 2010.


## Page 343

[ZMB+18]
Z. Zhou, P. Mertikopoulos, N. Bambos, P. Glynn, Y. Ye, L.-J. Li, and L. Fei-
Fei. Distributed asynchronous optimization with unbounded delays: How
slow can you go? In International Conference on Machine Learning, 2018.
[ZX15]
Y. Zhang and L. Xiao. Stochastic primal-dual coordinate method for regu-
larized empirical risk minimization. In International Conference on Machine
Learning, 2015.
[ZX17]
Y. Zhang and L. Xiao. Stochastic primal-dual coordinate method for regu-
larized empirical risk minimization. Journal of Machine Learning Research,
18(84):1–42, 2017.
[ZXC+16]
N. Zhou, Y. Xu, H. Cheng, J. Fang, and W. Pedrycz.
Global and local
structure preserving sparse subspace learning: An iterative approach to un-
supervised feature selection. Pattern Recognition, 53:87–101, 2016.
[ZY18]
J. Zeng and W. Yin. On nonconvex decentralized gradient descent. IEEE
Transactions on Signal Processing, 66(11):2834–2848, 2018.


## Page 344

Index
AAMR (averaged alternating modified re-
flections), 65
AC-FPI (asynchronous coordinate-update FPI),
133
mathematical definition, 135
operational definition, 133
acceleration, 255
adapt-then-combine, 242, 245
ADMM
2-1-2, 189, 197
2-1-2 with FLiP, 204
2-1-2-4-3-4 update, 203
3-block, 198
block splitting, 186
decentralized, 245
dual extrapolation parameter, 177
dummy variable, 201
four-block ADMM, 203
function-linearization, 178
golden ratio, 177, 197
graph coloring, 202
Jacobi doubly linearized, 200
Jacobi+1, 200
Peaceman–Rachford, 200
penalty parameter, 177
proximal term, 177
scaled form, 179
solvability of subproblems, 72, 89, 178
ADMM (alternating direction method of mul-
tipliers), 70, 72
ADMM-type, 175
after-read labeling, 156
AGM (Nesterov’s accelerated gradient method),
255, 261
algorithm, 100
ALM, 45
AMA (alternating minimization algorithm),
74
Amdahl’s law, 107
A-norm, 4
APPM (accelerated proximal point method),
258, 261
argmin, 8
ARock assumptions, 135
asymptotic equivalence, 17
asymptotic notation, 17
asynchronous ADMM, 148
asynchronous coordinate gradient descent,
146
asynchronous parallel, 132
atomic operation, 150
Attouch–Théra duality, 206
augmented Lagrangian, 15, 57
augmented Lagrangian method, 45, 196
Aumann integral, 172
averaged iteration, 35
backward-backward method, 65
Baillon–Haddad theorem, 12, 18, 29
ball, 5
Banach fixed-point theorem, 35, 62
base splitting scheme, 46
BCV (Bertsekas, O’Connor, and Vanden-
berghe) technique, 83, 90
BFS (backward-forward splitting), 46
biconjugate function, 11
big-O notation, 17
block, 113
block delay, 135
Bregman method, 58, 194, 198
C-FPI (coordinate-update fixed-point iter-
ation), 114
Cayley operator, 40
certificates, 207
Chambolle–Pock, 75, 89
Chen–Teboulle, 95
closed graph theorem, 223
cocoercivity, 29
combine-then-adapt, 241, 245
communication congestion, 132
compare-and-swap, 150
composition of averaged operators, 289
computational tomography, 77
Condat–Vũ, 76, 89, 92, 110, 184
conic program, 64, 124
conjugate function, 11, 27, 42
subdifferential, 42
consensus, 238
consensus set, 248
consensus technique, 53, 58, 65, 68, 106
consensus tracking, 253


## Page 345

330
Index
constraint qualification, 15
contraction mapping algorithm, 35
convex-concave, 12, 57, 60, 223
coordinate, 113
coordinate minimization, 128
coordinate proximal-gradient descent/method,
122
coordinate selection rule, 114, 127
coordinate-friendly method, 118
coordinate-friendly operator, 118
correspondence, 25
decentralized ADMM, 237
decentralized averaging, 239
decentralized FLiP-ADMM, 237
decentralized gradient descent, 245
decentralized methods, 227
delays, 137
demipositive, 163, 172, 174
DGD (decentralized gradient descent), 241
diffusion, 242
DIGing, 253
directed graph, 245
distance to a set, 6
distributed ADMM, 229
distributed DRS, 230
distributed methods, 227
distributed proximal gradient method, 228
doubly linearized ADMM, 184
doubly linearized method of multipliers, 93
DRS (Douglas–Rachford splitting), 47, 49,
57, 65, 208, 282
dual ascent, 39, 57, 63
dual decomposition, 231, 245, 247, 249
dual optimal value, 13
dual problem, 13
dual proximal gradient, 74
duality, 12
dualization technique, 72, 89
DYS (Davis–Yin splitting), 48, 50, 58, 111,
210, 290
edge, 234
eigenvalue, 3
embarrassingly parallel, 102
envelope theorem, 247
epigraph, 6
epoch, 125
Euclidean space, 3
exact decentralized methods, 242
exclusive access, 133, 136
exclusive memory access, 149
extended complex plane, 267
extended coordinate-friendly operator, 119,
142
extended real line, 6
extended solution set, 213
extension theorems, 220
EXTRA, 245
FBS (forward-backward splitting), 46, 207
Fejér monotonicity, 37
Fenchel conjugate, 11
Fenchel duality, 205
Fenchel’s identity, 27, 57
Fenchel–Moreau theorem, 11, 18
Fenchel–Rockafellar dual, 13
Fermat’s rule, 9
Finito, 123, 129
Fitzpatrick function, 216, 222
fixed point, 34
fixed-point encoding, 51
fixed-point residual, 37
FLiP-ADMM, 249
flop (floating-point operation), 99
flop-count operator, 100
forward step method, 39, 57, 277, 294
forward-Douglas–Rachford, 54, 58
FPI (fixed-point iteration), 34, 57
function
CCP (closed, convex, and proper), 6
closed, 6
concave, 6
convex, 6
differentiable, 7, 18
domain, 6
extended real-valued, 6
lower semicontinuous, 6
proper, 6
strictly concave, 6
strictly convex, 6
function-linearized proximal ADMM, 175
Gaussian elimination technique, 43, 78
generalized circles, 267
generalized forward-backward, 54
gradient descent, 38, 57, 62–64, 263, 277,
294
graph, 234
bipartite, 250
Hahn–Banach sandwich theorem, 224
Hogwild, 154
image of a convex function, 70
implementation on a method, 100
inconsistent read, 143
inconsistent write, 143
independence assumption on indices and de-
lays, 137
indicator function, 8
inexact decentralized methods, 241
infimal postcomposition, 70, 91
infimal postcomposition technique, 69, 89


## Page 346

Index
331
+∞−∞, 31
inner product, 3
inverse resolvent identity, 43
inversion map, 267
inversive geometry, 292
isotonic regression, 81
Iterative Shrinkage-Thresholding Algorithm
(ISTA), 52
iterative soft thresholding, 59
Jacobi ADMM, 187
Kirszbraun–Valentine theorem, 221, 222
KKT operator, 32, 42
Krasnosel’skiĭ–Mann iteration, 35
Lagrange multiplier, 13
LASSO (least absolute shrinkage and selec-
tion operator), 52, 59, 95
Legendre–Fenchel transform, 11
linearization technique, 82
linearized ADMM, 87, 183
linearized method of multipliers, 82, 94, 95
linesearch, 262
Lipschitz continuity, 5
little-o notation, 17
local averaging matrix, 239
logistic regression, 129
Lyapunov analysis, 36, 63, 137, 258, 261
Markov chain, 245
matrix
positive definite, 3
positive semidefinite, 3
square, 3
square root, 3
symmetric, 3
matrix inversion lemma, 110
maximal cocoercivity, 29
maximal monotone extension theorem, 220
maximal monotonicity, 28
maximal strongly monotonicity, 29
maximality, 51, 57
method, 100
method of multipliers, 45, 57, 63, 223
Minkowski sum, 3
Minty surjectivity theorem, 40, 57, 217, 222
MISO (minimization by incremental surro-
gate optimization), 123, 129
mixing matrix, 238, 245, 252
decentralized, 238
monotone inclusion problem, 32
monotonicity, 28
Moreau envelope, 61, 66
Moreau identity, 44
Moreau–Yosida approximation, 62
multi-valued function, 25
mutex (mutual exclusion lock), 151
near-circulant splitting, 197
NIDS (Network InDependent Stepsize), 243
node, 234
norm, 4
normal cone operator, 9
null space, 3
OHM (optimized Halpern method), 259, 261
operator
affine, 31
averaged, 33
cocoercive, 61
composition, 26
concatenation, 30
continuous, 31, 60
contractive, 33
differentiable, 31, 61
domain, 26
extension, 215
firmly nonexpansive, 33
graph, 25
identity, 26
image of a set, 26
inverse, 26, 60
Lipschitz, 26, 61
nonexpansive, 33
range, 26
set-valued, 25
single-valued, 25
sum, 26
zero, 26, 27
operator classes, 265
optimization problem
constrained, 8
constraint, 8
objective function, 8
optimization variable, 8
solution, 8
unconstrained, 8
PAPC (proximal alternating predictor cor-
rector), 80, 89, 94
parallel computing, 101
parallel flop-count operator, 102
parallel matrix-vector multiplication, 104
parallelizable method, 103
parallelizable operator, 103
parameter server, 144, 155
paramonotone, 172, 211
partial inverse, 223
partial linearization, 184
partial maximization, 247
partial minimization, 247
PD3O (primal-dual three-operator splitting),
85, 89, 93, 94


## Page 347

332
Index
PDFP2O (primal-dual fixed point algorithm
based on proximity operator), 80,
89, 94
PDHG (primal-dual hybrid gradient), 75,
83, 87, 89, 92, 95, 110, 183
PG-EXTRA, 243, 245, 253
point-to-set mapping, 25
Polyak–Ruppert averaging, 164
PPM (proximal point method), 44, 57, 62,
281, 294
preconditioned PDHG, 93
predictor corrector proximal multiplier method,
197
primal decomposition, 230, 245, 247, 249
primal optimal value, 13
primal problem, 13
primal-dual method, 69
product space trick, 58
projected gradient method, 49, 57
projected subgradient method, 170
projection, 16, 42
projection onto convex sets, 62
proximable, 17
proximal ADMM, 85, 91
proximal augmented Lagrangian method, 45
proximal gradient method, 49
proximal method of multipliers, 45
proximal method of multipliers with func-
tion linearization, 78
proximal minimization, 44
proximal operator, 16
proximal subgradient method, 170, 172
proximal term, 54, 82
proximal-gradient method, 57
PRS (Peaceman–Rachford splitting), 47, 57,
65
pseudononexpansive operators, 294
race condition, 142
Radon transform, 77
randomized coordinate gradient descent/method,
120
randomized primal-dual block coordinate up-
date method, 196
range, 3
RC-FPI (randomized coordinate-update fixed-
point iteration), 114
readers-writers lock, 152
reduction, 103, 228, 237
reflected resolvent, 40
regularity condition, 11
representation function of an operator class,
274
representative function, 216
resolvent, 40, 51
robust stochastic approximation, 174
saddle point, 13
saddle subdifferential, 31, 60
Schur complement, 4
SDCA (stochastic dual coordinate ascent),
122
second-order cone, 128
self-dual property of DRS, 209
seminorm, 4
separable constraint, 118
separable operator, 118
serial method, 103
server-worker framework, 144
set
affine, 5
affine hull, 5
boundary, 5
closure, 5
convex, 3
interior, 5
relative boundary, 5
relative interior, 5
set-valued mapping, 25
SFB (stochastic forward-backward method),
162
SGD (stochastic gradient descent), 161
shared memory system, 144
Sherman–Woodbury–Morrison formula, 110
singular value, 4
Slater’s constraint qualification, 15
smoothness, 12
soft-thresholding operator, 16
spherical triangle inequality, 266
split Bregman, 195
SRG
-full, 273
SRG (scaled relative graph), 268
of an operator, 268
composition, 287
intersection, 275
inversion, 280
of a matrix, 270
of an operator class, 271
product, 287
scaling, 276
sum, 285
translation, 276
stack operator, 238
staleness, 133
Stewart’s theorem, 266, 292
stochastic approximation, 172
stochastic Condat–Vũ, 171
stochastic coordinate gradient descent/method,
120
stochastic matrix, 240
stochastic projected subgradient method, 162


## Page 348

Index
333
stochastic proximal simultaneous gradient
method, 170
stochastic proximal subgradient method, 162,
170
stochastic subgradient method, 161, 173
strictly convex function, 60
strong convexity, 11
strong duality, 14
strong monotonicity, 29
strongly-convex accelerated gradient method,
263
subdifferentiability, 10
subdifferential, 9, 27, 41
maximality, 28
subdifferential of conjugate, 27
subgradient, 9
subgradient inequality, 9
subgradient method, 170
subspace, 4
summability argument, 36
supermartingale convergence theorem, 116
support-vector machine (SVM), 107
synchronization barrier, 131
synchronous parallel, 131
termination criterion, 38
total duality, 14, 50
trip-ADMM, 190
unbounded delay, 154
Uzawa method, 39
variable metric FBS, 55
variable metric methods, 54
variable metric PPM, 55, 58
variable metric technique, 75
variational inequality, 182
vector delay, 135
weak duality, 14
