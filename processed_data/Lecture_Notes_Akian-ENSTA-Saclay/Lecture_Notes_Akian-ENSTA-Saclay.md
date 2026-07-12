# Lecture_Notes_Akian-ENSTA-Saclay



## Page 1

Markov decision processes: dynamic programming and
applications
ENSTA Course APM 5OD2A TA& M2 optimization
(Paris-Saclay University and Institut Polytechnique de Paris)
2025 Lecture notes
Marianne Akian
INRIA Saclay - ˆIle-de-France and
CMAP ´Ecole polytechnique CNRS IP Paris,
marianne.akian@inria.fr
http://www.cmap.polytechnique.fr/~akian/cours-ensta/


## Page 2



## Page 3

Abstract
The aim of this course is to introduce diﬀerent stochastic control models and to present dynamic
programming as a tool for solving them. Illustrations selected among stock management, portfolio
selection, Yield management, transportation or Web PageRank optimisation will be presented.
We shall consider essentially stochastic dynamical systems with discrete time and ﬁnite state
space, or ﬁnite Markov chains.
This framework already contains the essential diﬃculties (for
instance for long term problems), and allows one to give at the same time an insight of algorithms,
mathematical techniques and qualitative properties. We may however consider some examples with
inﬁnite state space or continuous time.
We shall present the diﬀerent types of stochastic control problems: complete and incomplete
observation problems, criteria with ﬁnite horizon, discounted inﬁnite horizon, stopping time, er-
godic criteria, risk-sensitive criteria, constrainted problems, armed bandit problems. For some of
these criteria, we shall state the corresponding dynamic programming equations, study their qual-
itative properties, and the algorithms for solving them (value iterations, policy iterations, linear
programming), and deduce in some cases the structure of optimal strategies.
Key Words:
Markov Decision processes, Stochastic control, Ergodic control, Risk-sensitive con-
trol, Dynamic programming, Max-plus algebra, Value iteration, Policy iteration.
i


## Page 4

ii


## Page 5

Contents
Motivations and Introduction
1
Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
Aim of the course . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2
1
Dynamic programming principle for deterministic optimal control
3
1.1
Dynamical systems (some recalls) . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
1.2
Deterministic optimal control problems with additive payoﬀand ﬁnite horizon
. . .
4
1.3
Dynamic programming equation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
1.4
Properties of Dynamic programming . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
1.4.1
Complexity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
1.4.2
Operator properties
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
1.5
Inﬁnite horizon problems
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
1.6
Max-plus or Tropical algebra
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
1.7
Solutions of Exercises
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
2
Markov chains and Kolmogorov equations
21
2.1
Introduction and Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
2.2
Markov property . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
2.3
Elementary Properties and representations . . . . . . . . . . . . . . . . . . . . . . . .
24
2.4
The digraph of a stationary Markov chain . . . . . . . . . . . . . . . . . . . . . . . .
26
2.5
Kolmogorov equation for ﬁnite horizon criteria
. . . . . . . . . . . . . . . . . . . . .
28
2.6
Kolmogorov Equations for inﬁnite horizon criteria
. . . . . . . . . . . . . . . . . . .
34
2.7
Kolmogorov Equations for stopping time criteria
. . . . . . . . . . . . . . . . . . . .
36
2.8
Further examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
2.9
Solutions of Exercises
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
3
Markov decision processes with ﬁnite horizon criteria
43
3.1
Markov decision processes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
43
3.2
Markov decision problems with additive ﬁnite horizon criteria . . . . . . . . . . . . .
47
3.3
Properties of Bellman operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
48
3.4
Proof of Theorem 3.13 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
3.5
Problems with multiplicative or discounted ﬁnite horizon payoﬀ. . . . . . . . . . . .
52
3.6
Problems with exit time in ﬁnite horizon . . . . . . . . . . . . . . . . . . . . . . . . .
56
3.7
The example of optimal stopping time problems with ﬁnite horizon . . . . . . . . . .
58
iii


## Page 6

3.8
Examples and Exercices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
60
3.9
Problem: Airline Revenue Management
. . . . . . . . . . . . . . . . . . . . . . . . .
62
4
Markov decision problems with inﬁnite horizon
65
4.1
Discounted inﬁnite horizon problems . . . . . . . . . . . . . . . . . . . . . . . . . . .
65
4.1.1
The stationary dynamic programming equation . . . . . . . . . . . . . . . . .
67
4.1.2
The Bellman operator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
67
4.1.3
Proof of the Stationary Dynamic programming equation . . . . . . . . . . . .
68
4.2
Algorithms
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
70
4.2.1
Value iteration algorithm
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
70
4.2.2
Policy iteration algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
71
4.2.3
Additional properties of Policy iterations for discounted problems . . . . . . .
73
4.3
Optimal stopping time problems with inﬁnite horizon
. . . . . . . . . . . . . . . . .
75
4.4
Problems with variably discounted inﬁnite horizon payoﬀ
. . . . . . . . . . . . . . .
78
4.5
Problems with exit time in inﬁnite horizon . . . . . . . . . . . . . . . . . . . . . . . .
79
4.6
Problem: Divorce of Birds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
81
5
Long run average payoﬀproblems
83
5.1
Motivation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
83
5.2
Long term behavior of Markov chains
. . . . . . . . . . . . . . . . . . . . . . . . . .
85
5.2.1
Ergodicity of Markov chains . . . . . . . . . . . . . . . . . . . . . . . . . . . .
85
5.2.2
Graph properties of a Markov matrix
. . . . . . . . . . . . . . . . . . . . . .
86
5.2.3
Perron-Frobenius theorem for irreducible matrices
. . . . . . . . . . . . . . .
88
5.2.4
Linear algebra techniques and the multichain case
. . . . . . . . . . . . . . .
90
5.2.5
The ergodic Kolmogorov equation
. . . . . . . . . . . . . . . . . . . . . . . .
93
5.3
The controlled case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
95
5.3.1
The ergodic dynamic programming equation
. . . . . . . . . . . . . . . . . .
95
5.3.2
Application to Pagerank optimization
. . . . . . . . . . . . . . . . . . . . . .
98
5.3.3
Vanishing discount approach
. . . . . . . . . . . . . . . . . . . . . . . . . . . 101
5.3.4
An existence result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
5.3.5
Policy iteration algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
5.4
Risk sensitive control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
5.4.1
Motivation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
5.4.2
Risk sensitive control in ﬁnite horizon . . . . . . . . . . . . . . . . . . . . . . 115
5.4.3
Risk sensitive control in inﬁnite horizon . . . . . . . . . . . . . . . . . . . . . 118
5.5
Problem: Machine replacement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
5.6
Problem: Portfolio selection with transaction cost . . . . . . . . . . . . . . . . . . . . 123
6
Markov decision problems with partial observation
125
6.1
Motivation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
6.2
Partially observable Markov decision processes
. . . . . . . . . . . . . . . . . . . . . 127
6.3
POMDP with additive criteria and ﬁnite horizon . . . . . . . . . . . . . . . . . . . . 130
6.4
A suﬃcient statistics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
6.5
The dynamics of the belief process . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
6.6
Inﬁnite horizon problems
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
6.7
Problem: Machine replacement with partial observation . . . . . . . . . . . . . . . . 139
iv


## Page 7

6.7.1
The corresponding POMDP . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
6.7.2
Solving the DP equation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
7
Constrained Markov decision processes and Linear programming formulation of
Dynamic programming
141
7.1
Motivation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
7.2
Constrained MDP with ﬁnite horizon . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
7.3
Constrained MDP with inﬁnite horizon
. . . . . . . . . . . . . . . . . . . . . . . . . 149
7.4
Constrained MDP with long run time average payoﬀ. . . . . . . . . . . . . . . . . . 151
7.5
Complexity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
v


## Page 8

vi


## Page 9

Motivations and Introduction
A Markov decision problem, or a deterministic or stochastic control problem consists in the maxi-
mization or minimization of some functional involving a (possibly random) dynamical system and
constructed dynamically. This means that we consider an optimization problem in which the vari-
ables are:
• A dynamical system (Xt)t≥0 over a state space E;
• A control process (Ut)t≥0 taking its values in a control or action space C, on which the states
depend;
• both may depend on a random process (Wt)t≥0.
In particular the simplest stochastic control problem satisﬁes
Xk+1 = fk(Xk, Uk, Wk),
k ∈N,
(0.1)
where (Wk)k≥0 is a sequence of independent random variables.
The criteria J to be optimized has a dynamical structure, which “separate” past and future of
the state, and thus allows to apply Dynamic Programming method (introduced by (Bellman, 53)).
For instance, it may be additive:
J(X; U) :=
T
X
k=0
gk(Xk, Uk)
(for a discrete time problem).
Applications
Several real life problems can be modelized as Markov decision processes (MDP) or Stochastic
Control Problems. Here are some examples:
• Airline Revenue management;
• Portfolio selection;
• Dam management;
• Stock management;
• Transportation or Web PageRank optimisation;
• Divorce of birds;
1


## Page 10

Aim of the course
• Modelize real life problems.
• Apply dynamic programming approach.
• Solve dynamic programming equations:
– with analytical tools (convexity,monotonicity,...)
– with numerical algorithms (value and policy iterations, linear programming)
One shall consider essentially deterministic or stochastic dynamical systems with discrete time
and ﬁnite state space, and go from simple to more sophisticated models/problems:
• from deterministic to stochastic problems;
• from uncontrolled to controlled problems;
• from complete to incomplete observation problems;
• additive criteria with ﬁnite horizon, discounted inﬁnite horizon, stopping time, ergodic crite-
ria, risk-sensitive criteria;
• from unconstrained to constrainted problems.
References
References [2, 3, 5, 7] contain material similar to the contains of this course. Background material
can be found in [4, 1, 6]. Additional references will be given during the lectures.
[1] Robert B. Ash. Basic probability theory. John Wiley & Sons, Inc., New York-London-Sydney,
1970.
[2] D. P. Bertsekas. Dynamic programming. Prentice Hall Inc., Englewood Cliﬀs, NJ, 1987.
[3] E.B. Dynkin and A.A. Yushkevich. Controlled Markov processes. Springer-Verlag, New York,
1979.
[4] William Feller. An introduction to probability theory and its applications. Vol. I. Third edition.
John Wiley & Sons, Inc., New York-London-Sydney, 1968.
[5] M. L. Puterman. Markov decision processes: discrete stochastic dynamic programming. John
Wiley & Sons Inc., New York, 1994.
[6] R. T. Rockafellar. Convex analysis. Princeton University Press Princeton, N.J., 1970.
[7] P. Whittle. Optimization over time. Vol. I and II. John Wiley & Sons Ltd., Chichester, 1982,
1983.
2


## Page 11

Chapter 1
Dynamic programming principle for
deterministic optimal control
1.1
Dynamical systems (some recalls)
Let us recall what is a general dynamical system.
Deﬁnition 1.1. A (deterministic) dynamical system consists in a function (or sequence) from a
set T of times to a set E of states, denoted (Xt)t∈T , such that, for each time t ∈T , the state Xt of
the system at time t is a (deterministic) function ft of the history of the states until time t, that is
(Xτ)τ<t.
There, the set of times T may be:
• Z or N and t = n: we speak about discrete time dynamical system.
• R or R+: we speak about continuous time dynamical system.
The state space E may be:
• a ﬁnite set: ﬁnite state space.
• a ﬁnite or countable set: discrete state space.
• Rn: (ﬁnite dimensional) continuous state space /system.
• a space of functions : inﬁnite dimensional continuous state space /system.
The system may satisfy:
• Xn = fn(Xn−1), n ≥0.
•
˙X = gt(X), t ≥0, with gt Lipschitz continuous: mechanical or physical systems.
•
∂X
∂t = −∆X. Heat equation.
• the discretization of a ODE or PDE.
In particular,
3


## Page 12

Deﬁnition 1.2. A (deterministic) dynamical system with discrete time and state space E is a
sequence (Xk)k∈Z or (Xk)k∈N with values in the set E, such that, for each k ∈N, the state Xk
at time (or stage) k is a (deterministic) function fk of the states at previous times, that is of
Xk−1, Xk−2, . . ..
The sequence (Xk)k≥0 is called the trajectory of the system starting from X0.
Examples of discrete time dynamical systems are as follows:
1. Xn+1 = fn(Xn), n ≥0, where fn : E →E.
2. Xn+1 = fn(Xn, Xn−1), n ≥1, with fn : E × E →E.
3. Xn+1 = fn(Xn, Xn−1, . . . , X0), n ≥0, with fn : En+1 →E.
4. Xn+1 = fn(Xn−τ(n)), n ≥0, where τ : N →N is a variable delay.
Fact 1.3. Any discrete time dynamical system can be reduced to a system of type 1.
Proof. If the time set is Z, then a dynamical system is such that Xn+1 = fn(Xn, Xn−1, . . .), with
fn : EN →E, for all n ∈Z.
Consider the new state X′
k = (Xk, Xk−1, . . .) belonging to the larger state space E′ = EN, then
X′
k has the dynamics X′
k+1 = f′
k(X′
k) with
f′
k((x0, x1, . . .)) = (fk(x0, x1, . . .), x0, x1, . . .) .
If the time set is N, a dynamical system is such that Xn+1 = fn(Xn, Xn−1, . . . , X0), with
fn : En+1 →E, for all n ≥0.
We can reduce the new state space to E′ = ∪k≥0Ek+1, which is countable if E is a ﬁnite set.
Indeed, the new state X′
k = (Xk, Xk−1, . . . , X0) belongs to E′ and has the dynamics X′
k = f′
k(X′
k−1),
where f′
k is only deﬁned on Ek by
f′
k((x0, . . . , xk−1)) = (fk(x0, . . . , xk−1), x0, x1, . . . , xk−1) ∈Ek+1 .
A drawback of the above construction is that even if E were a ﬁnite set, the new state space E′
may be inﬁnite noncountable, in particular, when the time set is Z. Also to initialize the sequence,
one need an initial state of the form X′
0 = (X0, X−1, . . .) to be given. However, when the time set
is N, and E is a ﬁnite set, then the state space E′ is countable.
The above construction is similar to the one used to transform a second order diﬀerential
equation to a ﬁrst order one for instance.
1.2
Deterministic optimal control problems with additive payoﬀ
and ﬁnite horizon
The simplest deterministic control problem is the following. Consider a discrete time dynamical
system (Xn)n≥0 with ﬁnite (or discrete) state space E and a dynamics of type 1:
Xn+1 = fn(Xn),
n ≥1 .
4


## Page 13

Assume now that we (or somebody) are able to change the behavior of this system, that is its
dynamics fn.
That is, the dynamics is supposed to depend not only on the state but also on a parameter,
called the action or the control:
Xn+1 = fn(Xn, Un),
n ≥1 .
An optimal control problem is the problem of choosing the actions U0, . . . , Uk, . . . in such a
way that they minimize (resp. maximize) a certain functional, called the total cost (resp. the total
payoﬀ) of the sequences X = (Xk)k≥0 and U = (Uk)k≥0.
We assume in this part that all the states are observable, which means in particular that the
initial state X0 is known. We speak about complete observation.
Let us consider or denote:
• a ﬁnite or discrete state space E;
• an action space C
• for all k ∈N and x ∈E, the subset Ck(x) ⊂C of all possible actions at time k, when the state
is equal to x;
• for all k ∈N, the set Ak := {(x, u) | x ∈E, u ∈Ck(x)} of all possibles couples (state, action)
at time k;
• for all k ≥0, the dynamics at time k, which is a map fk : Ak →E;
• for all k ∈N, the instantaneous/running reward/payoﬀat time k, which is a map rk : Ak →R;
• a ﬁnal reward, which is a map ϕ : E →R;
• an initial state x0 ∈E.
• for all sequences X = (Xk)k≥0 and U = (Uk)k≥0 in E and C respectively, the total additive
payoﬀwith ﬁnite horizon T ≥1:
J(X; U) :=
 T−1
X
k=0
rk(Xk, Uk)
!
+ ϕ(XT ) .
(1.1)
Moreover, we shall replace the words reward or payoﬀby cost, and the notation rk by ck, when the
criterion J is to be minimized, instead of maximized.
Deﬁnition 1.4. A deterministic control problem with discrete time, complete observation, and
the above data and additive criteria consists in the following optimization problem:
max
X,U J(X; U)
where the optimization holds over all sequences X = (Xk)k≥0 and U = (Uk)k≥0 in E and C
respectively, such that
Xk+1 = fk(Xk, Uk), X0 = x0, Uk ∈Ck(Xk), k ∈N .
The optimum of above criteria is called the value of the problem. A sequence U = (Uk)k≥0 of
an optimal solution (X, U) is called an optimal control (process). Moreover, maximization can be
replaced by minimization.
5


## Page 14

Deﬁnition 1.5. For all x0 ∈E, let v(x0) be the value of the problem of Deﬁnition 1.4 when the
initial state is x0. The map v : E →R, x0 7→v(x0) is called the value function.
Some small generalizations of the above problem can be done.
• One can also consider functions rk and ϕ taking their values in R∪{−∞} (for a maximization
problem).
• This allows one to restrict the state space at each time. Indeed, for all k ≥0, let Ek ⊂E, and
take rk(x, u) = −∞when x̸ ∈Sk and ϕ(x) = −∞when x̸ ∈ET , then the maximum of J is
attained only for a sequence X such that Xk ∈Ek for all k ≥0.
• In particular, if ϕ(x) = 0 when x = xT and ϕ(x) = −∞otherwise, then the ﬁnal state is
necessarily equal to xT .
• Conversely, one can replace the constraint X0 = x0 by the addition to J of an initial reward
ψ : E →R ∪{−∞}, as in
max
X,U ψ(X0) + J(X; U)
where the optimization holds over all sequences X = (Xk)k≥0 and U = (Uk)k≥0 in E and C
respectively, such that
Xk+1 = fk(Xk, Uk), Uk ∈Ck(Xk), k ∈N .
• If ψ(x) = 0 when x = x0 and ϕ(x) = −∞otherwise, we recover the previous problem.
• If vψ denotes the value of the problem, then
vψ = max
x0∈E(ψ(x0) + v(x0)) .
Example 1.6 (Shortest path problem). Consider a directed graph G = (N, A), where N is the
set of nodes, and A ⊂N 2 is the set of arcs. Let ℓbe a weight function representing the “lengths”
of arcs: ℓ: A →R+. One can think for instance to a network of towns: the nodes are the towns,
the arcs the direct roads between some of them (that is the ones containing no other town), and ℓ
can be either the true length (in km) of the road or the gas consumption necessary to travel on it.
The shortest path problem starting from node x0 and ending in xf consists in solving:
min
(N−1
X
k=0
ℓ(xk, xk+1) | N ∈N, (x0, . . . , xN) is a path of G, xN = xf
)
.
3
5
3
1
2
4
1
1
1
6
4
6


## Page 15

When we restrict the minimization to paths with length (that is number of arcs) less or equal
to N, we get:
min
(n−1
X
k=0
ℓ(xk, xk+1) | n ≤N, (x0, . . . , xn) is a path of G, xn = xf
)
.
This problem is an optimal control problem with ﬁnite horizon N with
• E = C = N.
• Ck(x) is the set of nodes y such that (x, y) ∈A, when x̸ = xf and Ck(xf) = {xf}.
• The dynamics is fk(x, u) = u.
• The instantaneous cost is : rk(x, u) = ℓ(x, u) if x̸ = xf and rk(xf, xf) = 0.
• The ﬁnal cost is ϕ(x) = 0 if x = xf and ϕ(x) = +∞otherwise.
• The initial state is x0.
Example 1.7 (Ressource allocation problem). An investor can invest M ∈N units (of money,
capacity, requets,...) in N ∈N ressources (stocks, ﬂats, planes, parallel processors,...).
• We assume that the reward obtained when he invests x units in the ith ressource is equal to
Ri(x).
• We also assume that the units that are not invested yield a zero reward.
• So the investor wants to maximize his total reward, that is equivalent to ﬁnd
max
( N
X
i=1
Ri(ui) | ui ∈N, i = 1, . . . , N,
N
X
i=1
ui ≤M
)
.
Consider the deterministic optimal control problem in which:
• The ressource number is considered as a stage/time;
• The state at each stage is equal to the number of units remaining to be invested.
• The state space is E = {0, . . . , M};
• The action spaces are C = E and Ck(x) = {0, . . . , x}.
• The dynamics at each time k is : fk(x, u) = x −u;
• for all k ∈N, the instantaneous reward is : rk(x, u) = Rk+1(u).
• The ﬁnal reward is ϕ(x) = 0.
• The initial state is x0 = M.
7


## Page 16

• The total additive payoﬀwith ﬁnite horizon T = N is then:
J(X; U) =
T−1
X
k=0
rk(Xk, Uk) =
N−1
X
k=0
Rk+1(Uk) .
Then the value of this problem coincides with the one of the ressource allocation problem : take
uk = Uk−1 and Xk equal to the number of units remaining to be invested, when the number of
units u1, . . . , uk, invested in ressources 1 to k have already been chosen (Xk = X0 −u1 −· · · −uk).
Example 1.8 (Knapsack problem). Given N items, each with a weight wi and a value mi,
i = 1, . . . , N, one need to determine the number ui of each item i to include in a knapsack so that
the total weight is less than or equal to W and the total value is as large as possible. This consists
in the optimization problem:
max
( N
X
i=1
miui | ui ∈N, i = 1, . . . , N,
N
X
i=1
wiui ≤W
)
.
Additionnaly, the numbers ui can be restricted to be in {0, 1} or to be in {0, . . . , c}.
If wi ∈N∗, for all i = 1, . . . , N, considering the ressource allocation problem in which the rewards
are linear with Ri(x) = mi
wi x, and adding constraints induced by non-divisibility of ressources, or
restricting the sets Ci(x) of the optimal control problem, we recover all types of knapsack problems.
For instance, for 0-1 knapsack problem, one can consider Ci−1(x) = {0, . . . , x} ∩{0, wi}. For the
unbounded knapsack problem, one can consider Ci−1(x) = {0, . . . , x} ∩wiN.
1.3
Dynamic programming equation
In the optimal control problem of Deﬁnition 1.4:
max
X,U J(X; U)
(1.2a)
Xk+1 = fk(Xk, Uk), X0 = x0, Uk ∈Ck(Xk), k ∈N
(1.2b)
the optimization is done over all sequences U = (Uk)k≥0 satisfying the above constraints.
One may wish to obtain an optimal control which yields a dynamical system, that is a system
which is causal in the sense that the state Xk+1 at time k + 1 only depends on the past states
X0, . . . , Xk. Moreover, one may wish to take a decision at time k using only the informations we
have in hand, that is the history of the trajectories of X and U before the decision. A strategy is
precisely a rule which tells how to take this decision.
Deﬁnition 1.9. The set Hk = A0 × · · · × Ak−1 × E is called the set of histories at time k.
A strategy for the (perfect information) optimal control problem of Deﬁnition 1.4 is a sequence
σ = (σ0, . . . , σT−1) such that, for all k = 0, . . . , T −1, σk is a map from Hk to C satisfying
σk(x0, u0, . . . , xk−1, uk−1, xk) ∈Ck(xk), for all (x0, u0, . . . , xk−1, uk−1, xk) ∈Hk .
We denote by Σ(T) the set of all strategies. A strategy gives rise to a dynamical system (Xk, Uk)k≥0
satisfying the dynamics: Xk+1 = fk(Xk, Uk) and Uk = σk(X0, U0, . . . , Xk−1, Uk−1, Xk). Such a
sequence (Xk, Uk)k≥0 is also called an admissible sequence of states and controls.
A strategy is optimal if the sequence (X, U) is optimal for the optimization problem (1.2)
restricted to admissible sequences of states and controls (that is to strategies).
8


## Page 17

Deﬁnition 1.10. A strategy σ is a feedback policy if each map σk depends only on the information
on the state at the current time, that is
σk(x0, u0, . . . , xk−1, uk−1, xk) = πk(xk) ,
where πk : E →C is such that πk(xk) ∈Ck(xk). We then denote by π = (π0, . . . , πT−1) such a
policy, and by Π(T) the set of all feedback policies.
Deﬁnition 1.11. An open-loop control is a strategy such that each map σk depends only on the
state x0 at the initial time, that is
σk(x0, u0, . . . , xk−1, uk−1, xk) = ωk(x0) .
We denote by O(T) the set of all open-loop controls.
The following result shows that the optimization of the total reward J over each of the above
types of strategies gives the same value. However, one can show that feedback policies are more
robust with respect to disturbances on the model, that is disturbances on the maps fk and rk.
Theorem 1.12 ((Bellman) Dynamic programming method for deterministic optimal control prob-
lems). Assume that the maps ϕ, rk, k ≥0 are bounded from above. Deﬁne the functions vt : E →R,
t = 0, . . . , T, by the backward recursion:
vT (x) = ϕ(x)
∀x ∈E ,
(1.3a)
vk(x) = sup{rk(x, u) + vk+1(fk(x, u)) | u ∈Ck(x)}
∀x ∈E, k ≤T −1.
(1.3b)
Then the value function v of the optimal control problem of Deﬁnition 1.4 coincides with v0.
Moreover, the value v coincides with the optimum of (1.2) (that is of J) restricted to admissible
controls (or strategies), or to feedback policies, or to open-loop controls.
Assume in addition that the maximum of (1.3b), is attained for an action u ∈Ck(x) and let
us denote by πk(x) this action, then the feedback policy π = (πk)0≤k≤T−1 is an optimal strategy
of the problem, and the dynamics Xk+1 = fk(Xk, πk(Xk)) with Uk = πk(Xk) furnishes an optimal
solution (X, U) of the optimal control problem.
Proof. The dynamic programming equation by moving suprema. The value v(x0) of the problem of
Deﬁnition 1.4 is by deﬁnition the optimum of
J(X; U) :=
 T−1
X
k=0
rk(Xk, Uk)
!
+ ϕ(XT )
over all sequences X = (Xk)k≥0 and U = (Uk)k≥0 of E and C satisfying the constraints (1.2b):
v(x0) = sup
( T−1
X
k=0
rk(Xk, Uk)
!
+ ϕ(XT ) | (X, U) satisﬁes (1.2b)
)
.
Note that these sequences are not necessarily admissible.
9


## Page 18

This can be rewritten as:
v(x0) =
sup
U0∈C0(x0), X1=f0(x0,U0)
 
· · ·
sup
UT −1∈CT −1(XT −1), XT =fT −1(XT −1,UT −1)
  T−2
X
k=0
rk(Xk, Uk)
!
+ rT−1(XT−1, UT−1) + ϕ(XT )
!
· · ·
!
,
Consider the maps vk, k ≥0, as in (1.3).
Since r0(X0, U0), . . . , rT−2(XT−2, UT−2) do not depend on UT−1 nor XT , but only on the ﬁrst
states and actions X0, . . . , XT−2 and U0, . . . , UT−2, we deduce that for X0 = x0, we have
v(x0) =
sup
U0∈C0(X0), X1=f0(X0,U0)
 
· · ·
sup
UT −2∈CT −2(XT −2), XT −1=fT −2(XT −2,UT −2)
  T−2
X
k=0
rk(Xk, Uk)
!
+
sup
UT −1∈CT −1(XT −1)
(rT−1(XT−1, UT−1) + vT (fT−1(XT−1, UT−1)))
!
· · ·
!
,
=
sup
U0∈C0(X0), X1=f0(X0,U0)
 
· · ·
sup
UT −2∈CT −2(XT −2), XT −1=fT −2(XT −2,UT −2)
  T−2
X
k=0
rk(Xk, Uk)
!
+ vT−1(XT−1)
!
· · ·
!
,
= · · · = v0(X0) .
which shows that the value function v of the problem of Deﬁnition 1.4 coincides with the function
v0 deﬁned recursively by (1.3).
Optimality and an alternative proof of dynamic programming equation Applying (1.3b) recur-
sively, it is easy to show that, for all sequences (X, U) of states and actions satisfying the dynamics
Xk+1 = fk(Xk, Uk), we have
v0(x0) ≥r0(x0, U0) + v1(X1) ≥· · · ≥J(X; U) .
Taking the supremum over all sequences, we deduce that v0(x0) ≥v(x0).
Now, if πk(x) is optimal in the criteria (1.3b), then taking the sequence (X, U) such that Uk =
πk(Xk) and Xk+1 = fk(Xk, Uk), we get v0(x0) = r0(X0, U0) + v1(X1) = · · · = J(X; U) ≤v(x0).
Hence, since v0(x0) ≥v(x0), we deduce the equality and that (X, U) is optimal.
Moreover, this action is a function of k and Xk, hence it comes from a (feedback) strategy,
which is in particular a strategy. This shows that the maximum v(x0) over all sequences is equal
to the maximum over all feedback strategies, or over all strategies.
Since the dynamics is deterministic, the constraints Uk = πk(Xk) together with (1.2b) allow
to write Uk as a function of X0 only, that is as an open-loop control, hence we also get that the
maximum v(x0) coincides with the optimum of J restricted to all open-loop controls.
10


## Page 19

When the action sets are inﬁnite, but the suprema are ﬁnite, which is the case when the maps
ϕ, rk, k ≥0, are bounded from above, one can prove the same result by considering actions πk(x)
that are ϵ-optimal for (1.3b), that is satisfying for all x ∈E, and k ≤T −1,
vk(x) ≤ϵ + rk(x, πk(x)) + vk+1(fk(x, πk(x))) .
Indeed, this gives a control sequence U = (πk(Xk))k≥0 which is (Tϵ)-optimal for the criteria J :
v0(x0) ≤ϵ + r0(x0, U0) + v1(X1) ≤· · · ≤Tϵ + J(X; U) ≤Tϵ + v(x0) .
Since this holds for all ϵ > 0, we obtain that v0(x0) ≤v(x0) and so the equality as in the above
case of ﬁnite action sets. Moreover, we obtain that v(x) ≤v0(x0) ≤Tϵ + J(X; U) and since the
sequence (X, U) comes from a feedback strategy, this shows that the supremum of J(X; U) over all
feedback strategies is equal to v(x0). The other assertions are shown as for the case of ﬁnite action
sets.
Remark 1.13. Let us consider the partial criteria:
Jn(X; U) :=
 T−1
X
k=n
rk(Xk, Uk)
!
+ ϕ(XT )
Then, the iterations (vn)0≤n≤T deﬁned in the dynamic programming equation have the following
interpretation:
vn(xn) = max
X,U Jn(X; U)
(1.4a)
where the optimization is done over all sequences X = (Xk)k≥n and U = (Uk)k≥n satisfying the
following constraints
Xk+1 = fk(Xk, Uk), Xn = xn, Uk ∈Ck(Xk), n ≤k ≤T −1
(1.4b)
Example 1.14 (Shortest path problem (continued)). Let us consider the shortest path prob-
lem described in Example 1.6. Using the optimal control interpretation of the value of the shortest
path from x0 to xf with paths with length (that is number of arcs) less or equal to N:
v(N)(x0) := min
(n−1
X
k=0
ℓ(xk, xk+1) | n ≤N, (x0, . . . , xn) is a path of G, xn = xf
)
,
we obtain the dynamic programming equation:
v(N)
N (x) = +∞
∀x ∈N \ {xf} ,
v(N)
N (xf) = 0 ,
v(N)
k
(x) = min{ℓ(x, y) + v(N)
k+1(y) | y, (x, y) ∈A}
∀x ∈N \ {xf}, k ≤N −1 ,
v(N)
k
(xf) = v(N)
k+1(xf) .
Morover, since ℓdoes not depend on time k, we can rewrite theses equation as a forward
recurrence for wk = v(k)
0 , such that v(N)
k
= wN−k:
w0(x) = +∞
∀x ∈N \ {xf} ,
w0(xf) = 0 ,
wk(x) = min{ℓ(x, y) + wk−1(y) | y, (x, y) ∈A}
∀x ∈N \ {xf}, k ≤N −1 ,
wk(xf) = wk−1(xf) .
11


## Page 20

Example 1.15 (Ressource allocation problem (continued)). Let us consider the ressource
allocation problem described in Example 1.7.
Using the deterministic optimal control problem
interpretation, the value of the ressource allocation problem coincides with v0(M), where vt, t =
0, . . . , N satisfy the dynamic programming equation:
vN(x) = 0
∀x ∈{0, . . . , M} ,
vk(x) = sup{Rk+1(u) + vk+1(x −u)) | 0 ≤u ≤x}
∀0 ≤x ≤M, k ≤N −1.
Example 1.16 (Knapsack problem (continued)). Let us consider Knapsack problem described
in Example 1.8:
max
( N
X
i=1
miui | ui ∈{0, 1}, i = 1, . . . , N,
N
X
i=1
wiui ≤W
)
.
As for the ressource allocation problem, the value of the problem is equal to v0(W) where vt,
t = 0, . . . , N satisfy the dynamic programming equation:
vN(x) = 0
∀x ∈{0, . . . , W} ,
vk(x) = sup{mk+1u + vk+1(x −wk+1u)) | u ∈{0, 1}, wk+1u ≤x}
∀0 ≤x ≤W, k ≤N −1.
So the recurrence equation reduces to:
vk(x) = max(vk+1(x), mk+1 + vk+1(x −wk+1))
(1.5)
if x ≥wk+1, and vk(x) = vk+1(x) otherwise. Moreover, one can use (1.5) for all x ≥0, by extending
the functions vk by vk(x) = −∞for all negative integers x.
Exercise 1.3.1. Solve the Knapsack problem
max {4u1 + 3u2 + 2u3 | ui ∈{0, 1}, i = 1, . . . , 3, 5u1 + 4u2 + 3u3 ≤10} ,
using dynamic programming equation.
1.4
Properties of Dynamic programming
1.4.1
Complexity
Corollary 1.17 (of Dynamic programming). Under the assumptions of Theorem 1.12, denote, for
x, y ∈E, and k ≥0:
Gk(x, y) = sup{rk(x, u) | u ∈Ck(x), fk(x, u) = y} ∈R ∪{−∞} .
Then, the dynamic programming equation of Theorem 1.12 can be rewritten as
vk(x) = sup{Gk(x, y) + vk+1(y) | y ∈E}
∀x ∈E, k ≤T −1.
Note also that an optimal feedback policy πk(x) can be obtained as the composition: πk(x) =
π′
k(x, π′′
k(x)) where
π′
k(x, y) ∈Argmax{rk(x, u) | u ∈Ck(x), fk(x, u) = y}
and
π′′
k(x) ∈Argmax{Gk(x, y) + vk+1(y) | y ∈E}
12


## Page 21

If the maps Gk do not depend on k, one can construct a weighted directed graph with set of
nodes E, an arc (x, y) if G(x, y)̸ = −∞, with the weight G(x, y). For instance for E = {1, 2, 3} and
the following table of values of G
G =


−1
2
−∞
10
−4
3
−∞
−∞
0

,
we obtain the (di)graph:
1
3
2
10
-4
0
2
-1
3
Then, the weight of a path is the sum of the weights of its arcs, and an optimal sequence of
states (Xk)k≥0 is a path in this graph which has a maximal weight among the paths with same
initial and ﬁnal nodes. When the weights are nonpositive, this is a “shortest path” (for the lengths
which are the opposite of G). In general, denote
• n = card(E), the number of states;
• mk = card({(x, y) ∈E × E | Gk(x, y)̸ = −∞}), the number of arcs in the graph.
Fact 1.18. Once an oracle is available to compute Gk, the computational complexity of Dynamic
programming equation is O(P
k mk) = O(Tn2). This has to be compared with O(nT ), if we solve
the optimization directly, that is we solve the combinatorial optimization problem consisting in
optimizing the criterion over all trajectories (x0, . . . , xT ) in ET+1.
The storage complexity is O(P
k mk) if Gk depends on k and is O(m + Tn) otherwise.
1.4.2
Operator properties
Deﬁnition 1.19. For k ≤T −1, let Bk : RE →RE be the map such that for all v ∈RE, and x ∈E,
we have
[Bk(v)](x) = sup{rk(x, u) + v(fk(x, u)) | u ∈Ck(x)}
= sup{Gk(x, y) + v(y) | y ∈E} .
The map Bk is called the Bellman operator at time k of the optimal control problem.
The dynamic programming equation can then be rewritten in functional form:
vT = ϕ,
vk = Bk(vk+1),
for T −1, . . . , 0.
Deﬁnition 1.20. Denotes by ≤the partial order on RE: v ≤w if v(x) ≤w(x) for all x ∈E.
We say that an operator B : RE →RE is monotone or order preserving if it preserves the partial
order of RE, that is if, for all v, w ∈RE, we have
v ≤w ⇒B(v) ≤B(w) .
13


## Page 22

Deﬁnition 1.21. Denote by 1 the element of RE which is the constant function (or vector) equal
to 1: 1(x) = 1 for all x ∈E.
We say that an operator B : RE →RE is additively homogeneous if it commutes with the
addition of a constant, that is, for all v ∈RE and λ ∈R, we have:
B(v + λ1) = B(v) + λ1 .
Proposition 1.22. The above Bellman operators are monotone and additively homogeneous.
Proposition 1.23. Any monotone additively homogeneous operator B : RE →RS is nonexpansif,
that is Liptschitz continuous with Lipschitz constant 1, for the sup-norm ( ∥v∥∞= sup{|v(x)| | x ∈
E}):
∥B(v) −B(w)∥∞≤∥v −w∥∞
∀v, w ∈RE .
Proof. For all v, w ∈RE, we have v(x)−w(x) ≤∥v −w∥∞, for all x ∈E, hence v −w ≤∥v −w∥∞1.
So v ≤∥v −w∥∞1 + w. Using monotonicity of B, and then additive homogeneity, we get
B(v) ≤B(∥v −w∥∞1 + w) ≤∥v −w∥∞1 + B(w) .
Hence B(v) −B(w) ≤∥v −w∥∞1, that is [B(v) −B(w)](x) ≤∥v −w∥∞, for all x ∈E.
By symmetry, we also get [B(w) −B(v)](x) ≤∥w −v∥∞, and deduce ∥B(v) −B(w)∥∞≤
∥v −w∥∞.
Remark 1.24. Another proof of the nonexpansivity of the operator B of a deterministic control
problem is as follows. Such an operator acts on RE and satisﬁes
[B(v)](x) = sup{r(x, u) + v(f(x, u)) | u ∈C(x)}
= sup{G(x, y) + v(y) | y ∈E} ,
for all v ∈RE and x ∈E, for some control sets C(x) and maps r, f and G. Given v, w ∈RE and
x ∈E, choose y ∈E which is optimal in the expression of [B(v)](x), that is such that [B(v)](x) =
G(x, y) + v(y). Since [B(w)](x) ≥G(x, y) + w(y), we obtain
[B(v)](x) −[B(w)](x) ≤v(y) −w(y) ≤∥v −w∥∞.
By symmetry, we also get [B(w)](x) −[B(v)](x) ≤∥v −w∥∞, and taking the maximum over x ∈E,
we deduce ∥B(v) −B(w)∥∞≤∥v −w∥∞.
1.5
Inﬁnite horizon problems
Assume now that the horizon T is inﬁnite, that is the functional J is replaced by:
J(X; U) :=
∞
X
k=0
rk(Xk, Uk)
(1.6)
and that the inﬁnite sum is well deﬁned in R∪{−∞} for all sequences Xk and Uk satisfying (1.2b).
Then, one may try to compute again the maximum (or supremum) v of J, as in ﬁnite horizon
problems.
This is the case when
14


## Page 23

(A1)
Ck and fk do not depend on k (then we omit k in the notations), rk(x, u) = αkr(x, u) for all
k ≥0, for some function r bounded from above and some constant α > 0;
and one of the following assumptions hold:
(A2)
α < 1;
(A3)
α = 1 and r(x, u) ≤0 for all x ∈E and u ∈C, and for all x0 ∈E, there exists a sequence
(Xk, Uk) satisfying (1.2b), such that r(Xk, Uk) = 0 for k large enough.
(A4)
α = 1, if G is constructed as in Section 1.4.1, then any circuit of the graph of G has a total
weight ≤0, and for all x0 ∈E, there exists an inﬁnite path x0, x1, . . . in the graph of G, such
that G(xk, xk+1) = 0 for k large enough.
Deﬁnition 1.25. The parameter α is called the discount factor. We say that the inﬁnite horizon
optimal control problem is discounted if α < 1, and that it is undiscounted when α = 1.
Deﬁnition 1.26. We deﬁne strategies, feedback policies and open-loop controls of an inﬁnite
horizon problem as for ﬁnite horizon problems, but with T = ∞.
We say that a feedback policy π∗= (πk)k≥0 of an inﬁnite horizon control problem is stationary
if πk = π0 for all k ≥0.
Moreover we will sometimes use the same notation for π∗and π0.
Theorem 1.27 (Stationnary deterministic dynamic programming). Assume that E is a ﬁnite set,
and that (A1) holds together with one of the assumptions (A2), (A3) or (A4). Then the value
function v of the problem
v(x0) = sup{J(X; U) | (X, U) satisﬁes (1.2b) }
(1.7)
with J as in (1.6), satisﬁes the equation:
v(x) = sup{r(x, u) + αv(f(x, u)) | u ∈C(x)}
∀x ∈E .
(1.8)
For all x0 ∈E, the value v(x0) coincides with the optimum of J over all strategies or over all
feedback policies, or over all open-loop controls. When α < 1, the solution of (1.8) is unique.
Moreover, assume that the maximum of (1.8) is attained for an action u ∈C(x) and let us
denote by π(x) this action, then the stationary feedback policy π∗= (πk)k≥0, with πk = π for
all k ≥0, is an optimal strategy of the problem, and the dynamics Xk+1 = f(Xk, π(Xk)) with
Uk = π(Xk) furnishes an optimal solution (X, U) of the inﬁnite horizon control problem.
To show this result, we shall use the Bellman operator.
Deﬁnition 1.28. Let Bα : RE →RE be the map such that for all v ∈RE, and x ∈E, we have
[Bα(v)](x) = sup{r(x, u) + αv(f(x, u)) | u ∈C(x)}
= sup{G(x, y) + αv(y) | y ∈E} ,
where
G(x, y) = sup{r(x, u) | u ∈C(x), f(x, u) = y} ∈R ∪{−∞} .
The map Bα is called the Bellman operator of the discounted inﬁnite horizon optimal control
problem.
15


## Page 24

Note that since r is bounded from above, G(x, y) exists in R ∪{−∞}. Then, if E a ﬁnite set,
we get that the values of G(x, y) which are ﬁnite (that is̸ = −∞) are bounded from below. Then,
one may have assumed from the begining that r is bounded from below and above.
The dynamic programming equation can be rewritten in functional form as the ﬁxed point
equation of the Bellman operator Bα:
v = Bα(v) .
Fact 1.29. The undiscounted Bellman operator B1 is monotone and additively homogenous.
Corollary 1.30. The discounted Bellman operator Bα is Lipschitz continuous for the sup-norm
with Lipschitz constant α, thus it is α-contracting when α < 1.
Proof. From Proposition 1.23, B1 is nonexpansive for the sup-norm. We have Bα(v) = B1(αv), so
∥Bα(v) −Bα(w)∥∞= ∥B1(αv) −B1(αw)∥∞≤∥αv −αw∥∞= α∥v −w∥∞.
Corollary 1.31. When E is ﬁnite and α < 1, the operator Bα admits a unique ﬁxed point v∗.
Moreover, for any initial point v0 ∈RE, the sequence vn+1 = Bα(vn) converges towards v∗:
∥vn −v∗∥∞≤αn∥v0 −v∗∥∞.
Proof. This follows from the ﬁxed point theorem since RE is a Banach space and Bα is contracting.
Proof of Theorem 1.27 when α < 1. Assume that E is a ﬁnite set and that α < 1. Let v∗be the
unique solution of the Bellman equation v = Bα(v), by Corollary 1.31.
Let v(N) be the value
function of the ﬁnite horizon problem:
v(N)(x) = max
X,U {J(N)(X; U) | (Xk, Yk) satisfying (1.2b)}
with
J(N)(X; U) :=
 N−1
X
k=0
αkr(Xk, Uk)
!
+ 0 .
From Theorem 1.12, v(N) = v(N)
0
with v(N)
k
solution of the dynamic programming equation:
v(N)
N (x) = 0
∀x ∈E ,
v(N)
k
(x) = sup{αkr(x, u) + v(N)
k+1(f(x, u)) | u ∈C(x)}
∀x ∈E, k ≤N −1.
This can be rewritten as v(N)
k
= αkBα(v(N)
k+1/αk+1). Hence, v(N) = BN
α (0) := Bα ◦· · · ◦Bα(0) (where
the composition is done N times). Therefore, limN→∞v(N) = v∗where the limit is uniform in E
(limit for the sup-norm of RE).
Let C be a bound of the ﬁnite values of |G(x, y)|, with G as in Deﬁnition 1.28. Then, for any
inﬁnite sequences X and U, we have
|J(N)(X; U) −J(X; U)| ≤
∞
X
k=N
αkC = αN
C
1 −α .
16


## Page 25

Using the deﬁnition of the value function v of the inﬁnite horizon problem and that of v(N), as the
supremum of J(X; U) and J(N)(X; U) respectively, we deduce
∥v −v(N)∥∞≤αN
C
1 −α ,
so limN→∞v(N) = v, which implies that v = v∗.
The proof of optimality is similar to the ﬁnite horizon case.
Proof of Theorem 1.27 when α = 1. Under Assumption (A3), we get that v ≤0 and v(x) ∈R for
all x ∈E. Moreover, v(x) ≤v(N)(x) ≤v(N−1)(x) for all x ∈E and N ≥1. This implies that v(N)
has a limit v∗which satisﬁes v ≤v∗. Since v(N) = B1(v(N−1)) for all N ≥1, and B1 is continuous,
we get that v∗= B1(v∗).
It remains to prove that v = v∗. We shall use the ﬁniteness of E. Let δ > 0 be a lower bound of
−G(x, y) over all (x, y) such that G(x, y) < 0 and let n be the cardinality of E. Let ε > 0 be such
that ε < δ, and N such that v(N)(x) ≤v∗(x) + ε/3. We get that v(N)(x) ≤v(N+n)(x) + ε/3 and if
(X, U) is ε/3-optimal for v(N+n), we deduce that PN−1
k=0 G(Xk, Xk+1) ≤v(N)(x) ≤v(N+n)(x)+ε/3 ≤
PN+n−1
k=0
G(Xk, Xk+1) + 2 × ε/3 so, for all k = N, . . . N + n −1, we have −G(Xk, Xk+1) ≤2 × ε/3.
This implies that all these (Xk, Xk+1) are such that G(Xk, Xk+1) = 0, and since the cardinality of
E is equal to n, two elements of the sequence (XN, . . . , XN+n) are equal, which means that there
is a cycle (Xℓ, . . . , Xℓ′ = Xℓ). Consider the inﬁnite sequence obtained by concatening (X0, . . . , Xℓ)
with an inﬁnite number of the cycle (Xℓ, . . . Xℓ′). We obtain that J(X; U) = Pℓ−1
k=0 G(Xk, Xk+1) =
PN+n−1
k=0
G(Xk, Xk+1) ≥v(N+n)(x) −ε/3 ≥v∗−ε/3.
Since v(x) ≥J(X; U) we deduce that
v(x) ≥v∗(x) −ε/3. Since this holds for all ε > 0 (with ε < δ), we get that v(x) ≥v∗(x), and so
the equality.
Deﬁnition 1.32. The algorithm constructing the sequence vn+1 = Bα(vn) is called value iterations.
In practice one uses rather a variant similar to Gauss-Seidel algorithm (wrt to Jacobi) for the
solution of linear systems, in order to avoid useless storage.
The resulting algorithm is called
Ford-Bellman algorithm. It depends on some ordering on E. When E = {1, . . . , N}, it is as follows:
vk,0 = vk,
for j = 1, . . . , N, vk,j(j) = [Bα(vk,j−1)](j),
vk,j(ℓ) = vk,j−1(ℓ) ∀ℓ̸ = j,
vk+1 = vk,N.
When α = 1, under suitable conditions, the value iterations converge in ﬁnite time ≤N =
card(E) to the solution. So with a computational time in O(mN), where m = card({(x, y) ∈E ×E |
G(x, y)̸ = −∞}).
When in addition (A3) holds (in particular r ≤0), the problem is equivalent to a shortest path
problem with weight G and no constraints in the length of paths.
The ﬁxed point equation can be solved using Dijkstra algorithm which is equivalent to one full
step of Ford-Bellman algorithm with an appropriate ordering of states. The computational time is
then in O(m + N log N) (with the implementation of Fredman and Tarjan).
Exercise 1.5.1 (Hierarchical shortest path problem). Alice and Bob are in holidays in Venezia with
the little Charlie (1 year). Venizia is composed of islets connected with bridges with several stairs,
which are thus diﬃcult to cross with the heavy stroller of Charlie.
17


## Page 26

Assume that the map of Venezia is approximated by a graph in which nodes correspond to
landmarks and arcs correspond to streets and bridges, and that we know the travel time and
number of stairs to cross between nodes. Alice et Bob want to ﬁnd the paths between two points
xi and xf of the graph which minimize ﬁrst the number of stairs and among all paths minimizing
the number of stairs, they want to choose the ones which minimize also the travel time. Modelize
this problem as a deterministic control problem.
1.6
Max-plus or Tropical algebra
The equations in (1.3b) can be seen as linear over the following semiﬁeld.
Consider the set R ∪{−∞} of real numbers extended by −∞, endowed with the maximization
as an addition and the usual addition as a multiplication: a ⊕b = max(a, b) and a ⊗b = a + b for
all a, b ∈R ∪{−∞}.
The addition is commutative, associative and has the zero element −∞, which is absorbing for
the multiplication, the multiplication is commutative, associative, has the unit (neutral) element
0, and it distributes over the addition ⊕.
The addition is idempotent, meaning that a ⊕a = a for all a. Therefore opposites to non zero
elements do not exist.
Inverses (for the multiplication) exist for all non zero elements. So we obtain a semiﬁeld called
the max-plus algebra or the tropical algebra, that is often denoted Rmax.
Then the dynamic programming equation of deterministic control with ﬁnite horizon (1.3b) can
be rewritten as
vk(x) =
M
u∈Ck(x)
rk(x, u) ⊗vk+1(fk(x, u))
∀x ∈E, and k = T −1, . . . , 0 ,
(1.9)
which is a linear equation over Rmax. In particular, denoting
M(k)
xy = sup{rk(x, u) | u ∈Ck(x), fk(x, u) = y}
for all x, y ∈E (this was Gk above), then (1.9) can be rewritten as
vk(x) =
M
y∈E
M(k)
xy ⊗vk+1(y)
∀x ∈E, and k = T −1, . . . , 0 ,
that is the vector vk is the product of the tropical matrix M(k) with entries M(k)
xy , x, y ∈E by the
vector vk+1. Hence, v0 is obtained by applying the product of the T matrices M(0), . . . , M(T−1) to
the vector vT = ϕ.
In this way, the Bellman equation can be seen as a Kolmogorov equation associated to a Markov
chain, as in Chapter 2.
In some situations, the analogy with usual numerical linear algebra may suggest some algo-
rithms. These algorithms are often called tropical numerical methods.
18


## Page 27

1.7
Solutions of Exercises
Exercise 1.3.1.
The example can be solved by applying (1.5) with N = 3, m1 = 4, m2 = 3, m3 =
2, w1 = 5, w2 = 4, w3 = 3. These equations reduce to:
v3(x) = 0
for x ∈{0, . . . , 10}
v2(x) = max(v3(x), 2 + v3(x −3))
v1(x) = max(v2(x), 3 + v2(x −4))
v0(x) = max(v1(x), 4 + v1(x −5))
with the extension of vk to −∞for x < 0. This gives the following table of values of the problem:
x
0
1
2
3
4
5
6
7
8
9
10
v3
0
0
0
0
0
0
0
0
0
0
0
v2
0
0
0
2
2
2
2
2
2
2
2
v1
0
0
0
2
3
3
3
5
5
5
5
v0
0
0
0
2
3
4
4
5
6
7
7
This table determines the optimal policy at each step k = 0, 1, 2: πk(x) = 0 if vk(x) = vk+1(x) and
πk(x) = 1 otherwise.
The value of the knapsack problem is equal to v0(10) = 7. It is obtained by starting with
X0 = 10 and taking the controls uk = Uk−1 = πk−1(Xk−1), and Xk = Xk−1 −wk−1Uk−1. In view
of the above table, we have v0(10)̸ = v1(10), so u1 = U0 = 1 and X1 = 10 −5 = 5. For X1 = 5, we
have v1(5) = 3̸ = v2(5), so u2 = U1 = 1 and X2 = 5−4 = 1. For X2 = 1, we have v2(1) = 0 = v3(1),
so u3 = U2 = 0 and X3 = 1.
Exercise 1.5.1.
19


## Page 28

20


## Page 29

Chapter 2
Markov chains and Kolmogorov
equations
2.1
Introduction and Notations
We shall consider here Markov chains over a ﬁnite (or countable) state space E. These are the
random version of the dynamical system Xn+1 = fn(Xn).
We shall also consider functionals similar to the ones optimized in the optimal control prob-
lems of Chapter 1. and prove a “linear version” of Bellman dynamic programming equation: the
Kolmogorov equation.
Bellow are some general notations used in all the course.
• The state space E is assumed to be ﬁnite or possibly countable, that is discrete. Let N =
card(E) ∈N ∪{∞}.
• The elements of E are (linearly) ordered, one can identify E with {1, . . . , N} (or N if N = ∞),
and any element of RE, that is any function E →R, to a column vector in RN.
• We shall use this identiﬁcation, without ﬁxing any order on E.
• More generally, we shall speak about matrices over E: an element M of RE×E is a matrix over
E, and its entries are denoted (Mxy)x,y∈E.
• E beeing at most countable, we shall endow E with the σ-algebra P(E) of all subsets of E.
• A probability law p over E will be identiﬁed to a row vector, although we will also write
p ∈RE, more precisely this is an element of the simplex:
∆E = {p ∈RE | px ≥0 ∀x ∈E, p1 =
X
x∈E
px = 1} .
• The Dirac measure over E in state x ∈E will be denoted δx: its entries are 1 in x and 0
elsewhere.
• A matrix M ∈RE×E is a Markov (or a stochastic) matrix if its entries are all nonnegative
(Mxy ≥0 for all x, y ∈E) and M1 = 1 (P
y∈E Mxy = 1 for all x ∈E).
21


## Page 30

• Given a probability space (Ω, A, P), a random variable taking its values in E is by deﬁnition
a measurable function from (Ω, A) to (E, P(E)).
• Given a ﬁltration (Fn)n∈N on (Ω, A), that is a nondecreasing sequence of σ-algebras Fn ⊂A,
we say that a sequence (Xn)n≥0 of random variables (also called a random process) taking
its values in E is adapted to the ﬁltration if for all n ≥0, Xn is measurable from (Ω, Fn) to
(E, P(E)).
2.2
Markov property
Deﬁnition 2.1. A sequence (Xn)n∈N of random variables over (Ω, A, P), taking its values in E, is
a Markov chain (or a discrete time Markov process) if it satisﬁes:
P(Xn+1 = xn+1 | X0 = x0, . . . , Xn = xn) = P(Xn+1 = xn+1 | Xn = xn)
(2.1)
for all n ≥1, x0, . . . , xn+1 ∈E.
The probability measure p(0) and the Markov matrices M(n) over E deﬁned by:
p(0)
x
= P(X0 = x)
M(n)
xy = P(Xn+1 = y | Xn = x)
for all x, y ∈E are respectively called the initial law and the transition matrix at time n of the
Markov chain (Xn)n∈N.
The Markov chain is stationary if the transition matrices M(n) do not depend on n. If p(0) = δx0,
we say that x0 is the initial state of the Markov chain.
Example 2.2 (Random walk). A particule or a drunk man is walking on a line: at each unit of
time, he is going forward with probability p ∈[0, 1], and backward with probability 1 −p. If he
stops at boundaries of E = {0, . . . , N}, then the position Xn at time n deﬁnes a Markov chain Xn
over E such that
P(Xn+1 = x + 1 | Xn = x) = 1 −P(Xn+1 = x −1 | Xn = x) = p,
when x̸ = 0, N.
The transition matrix is given by:
M =


1
0
0
0
· · ·
0
1 −p
0
p
0
· · ·
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
· · ·
0
1 −p
0
p
0
· · ·
0
0
0
1


Proposition 2.3. Let (Xn)n∈N be a sequence of random variables over (Ω, A, P), taking its values
in E, with initial law p(0). Then the following are equivalent:
1. (Xn)n∈N is a Markov chain with transition matrices M(n) at time n ∈N;
22


## Page 31

2. P(X0 = x0, . . . , Xn = xn) = p(0)
x0 M(0)
x0x1 · · · M(n−1)
xn−1xn, for all n ≥1, x0, . . . , xn ∈E;
3. P(Xn+1 = xn+1 | X0 = x0, . . . , Xn = xn) = M(n)
xnxn+1, for all n ≥0, x0, . . . , xn+1 ∈E;
Proof. Let (Xn)n∈N be a sequence of random variables over (Ω, A, P), taking its values in E, with
initial law p(0).
1. ⇒2. Assume (Xn)n∈N is a Markov chain with transition matrices M(n) at time n ∈N, then
it satisﬁes:
P(X0 = x0, . . . , Xn = xn)
=
P(X0 = x0, . . . , Xn−1 = xn−1)P(Xn = xn | X0 = x0, . . . , Xn−1 = xn−1)
=
P(X0 = x0, . . . , Xn−1 = xn−1)M(n−1)
xn−1xn ,
from which one deduce 2. by induction.
2. ⇒3. Assume that (Xn) satisﬁes 2. Then,
P(Xn+1 = xn+1 | X0 = x0, . . . , Xn = xn)
=
P(X0 = x0, . . . , Xn+1 = xn+1)
P(X0 = x0, . . . , Xn = xn)
=
p(0)
x0 M(0)
x0x1 · · · M(n)
xnxn+1
p(0)
x0 M(0)
x0x1 · · · M(n−1)
xn−1xn
=
M(n)
xnxn+1 ,
that is 3.
3. ⇒1. Assume now that (Xn) satisﬁes 3., or equivalently assume that P(Xn+1 = xn+1 |
X0 = x0, . . . , Xn = xn) does not depend on x0, . . . , xn−1. Let us deduce that it is also equal to
P(Xn+1 = xn+1 | Xn = xn), that is the Markov property. Indeed,
P(Xn = xn, Xn+1 = xn+1)
=
X
x0,...,xn−1∈E
P(X0 = x0, . . . , Xn = xn, Xn+1 = xn+1)
=
X
x0,...,xn−1∈E
(P(X0 = x0, . . . , Xn = xn)P(Xn+1 = xn+1 | X0 = x0, . . . , Xn = xn))
=


X
x0,...,xn−1∈E
P(X0 = x0, . . . , Xn = xn)

M(n)
xnxn+1
=
P(Xn = xn)P(Xn+1 = xn+1 | X0 = x0, . . . , Xn = xn) .
Corollary 2.4. Let (Xn)n∈N be a sequence of random variables over (Ω, A, P), taking its values in
E. If, for all n ≥0, x0, . . . , xn+1 ∈E, P(Xn+1 = xn+1 | X0 = x0, . . . , Xn = xn) does not depend
on x0, . . . , xn−1, that is is a function of n, xn, xn+1 only, then (Xn)n∈N is a Markov chain.
23


## Page 32

Theorem 2.5. Let p(0) be a probabilty over E and M(n) be Markov matrices over E, for all n ∈N.
Then, there exists a probability space (Ω, A, P) and a Markov chain (Xn)n∈N on (Ω, A, P) taking
its values in E, with initial law p(0) and transition matrices M(n).
Sketch of proof. We know that necessarily, the law of Xn is given by the formula in 2 of Propo-
sition 2.3. This allows to compute the probability of all the cylinders A0 × · · · × An × EN of EN.
Therefore, it is suﬃcient to consider the canonical probability space Ω= EN, with A the σ-algebra
generated by ﬁnite cylinders, and P the probability on (Ω, A) already given on cylinders. Such a
probability exists and is unique by Kolmogorov extension theorem.
2.3
Elementary Properties and representations
Proposition 2.6 (Fokker-Plank equation). Let (Xn)n∈N be a Markov chain over (Ω, A, P), taking
its values in E, with initial law p(0) and Markov transition matrices M(n) at time n ∈N. Then, the
law p(n) of the random variable Xn satisﬁes the Fokker-Plank recurrence equation:
p(n+1) = p(n)M(n) .
Proof. Using the deﬁnition of p(n), M(n) and of conditional probabilities, we get, for all xn+1 ∈E,
p(n+1)
xn+1
=
P(Xn+1 = xn+1)
=
X
xn∈E
P(Xn = xn, Xn+1 = xn+1)
=
X
xn∈E
P(Xn+1 = xn+1 | Xn = xn)P(Xn = xn)
=
X
xn∈E
M(n)
xnxn+1p(n)
xn = (p(n)M(n))xn+1 .
Remark 2.7. The proof of Fokker-Plank equation does not use the Markov property, but only the
value of P(Xn+1 = xn+1 | Xn = xn).
Proposition 2.8. Let (Xn)n∈N be a Markov chain over (Ω, A, P), taking its values in E, with initial
law p(0) and Markov transition matrices M(n) at time n ∈N. Then, the sequence (Xn+k)n∈N is a
Markov chain with initial law p(k) (given by Fokker-Plank equation) and Markov transition matrices
M(n+k) at time n ∈N.
Proof. By Proposition 2.3, the sequence (Xn)n∈N satisﬁes (2). Therefore, for k, n ∈N, we have
P(X0 = x0, . . . , Xn+k = xn+k) = p(0)
x0 M(0)
x0x1 · · · M(k−1)
xk−1xk · · · M(n+k)
xn+k−1xn+k .
Taking the sum for all x0, . . . , xk−1 ∈E, we get
P(Xk = xk, . . . , Xn+k = xn+k) =


X
x0,...,xk−1∈E
p(0)
x0 M(0)
x0x1 · · · M(k−1)
xk−1xk

M(k)
xkxk+1 · · · M(n+k)
xn+k−1xn+k .
(2.2)
24


## Page 33

For n = 0 this equation writes
P(Xk = xk) =
X
x0,...,xk−1∈E
p(0)
x0 M(0)
x0x1 · · · M(k−1)
xk−1xk .
Together with (2.2) for any n ∈N, this gives
P(Xk = xk, . . . , Xn+k = xn+k) = P(Xk = xk)M(k)
xkxk+1 · · · M(n+k)
xn+k−1xn+k
= p(k)
xk M(k)
xkxk+1 · · · M(n+k)
xn+k−1xn+k ,
where p(k) is the law of Xk. Therefore, using Proposition 2.3, we get that (Xn+k)n∈N is a Markov
chain with initial law p(k) and transition matrix M(n+k) at time n ∈N. Moreover, from Proposi-
tion 2.6, p(k) satisﬁes Fokker-Plank equation.
Proposition 2.9. Let (Xn)n∈N be a Markov chain over (Ω, A, P), taking its values in E, with
initial law p(0) and Markov transition matrices M(n) at time n ∈N. Then, for all x0, . . . , xT ∈E,
0 ≤k ≤T, we have
P(Xk+1 = xk+1, . . . , XT = xT | X0 = x0, . . . , Xk = xk) = M(k)
xkxk+1 · · · M(T−1)
xT −1xT .
Proposition 2.10. Let (Xn)n∈N be a Markov chain over (Ω, A, P), taking its values in E, with
initial law p(0) and Markov transition matrices M(n) at time n ∈N.
Then, for all k ≥1,
the sequence (Xnk)n∈N is a Markov chain with initial law p(0) and Markov transition matrices
M(nk) · · · M((n+1)k−1) at time n ∈N.
Proof. From Proposition 2.3, the sequence (Xn)n∈N satisﬁes (2). Then, for all k ≥1 and n ∈N,
we have
P(X0 = x0, . . . , Xnk = xnk) = p(0)
x0 M(0)
x0x1 · · · M(nk)
xnk−1xnk .
Taking the sum over all x1, . . . , xk−1, xk+1, . . . , x2k−1, . . . x(n−1)k+1, . . . , xnk−1 ∈E, we get:
P(X0 = x0, . . . , Xmk = xmk, . . . , Xnk = xnk)
=
X
x1,...,xk−1,xk+1,...,x2k−1,...x(n−1)k+1,...,xnk−1∈E
p(0)
x0 M(0)
x0x1 · · · M(nk)
xnk−1xnk .
Denoting M(k,n) := Mnk · · · M((n+1)k−1), we obtain
P(X0 = x0, . . . , Xmk = xmk, . . . , Xnk = xnk) = p(0)
x0 M(k,0)
x0xk · · · M(k,n)
x(n−1)kxnk ,
which with Proposition 2.3 shows the result.
Practical examples are often constructed in the following way.
Fact 2.11. Let (Ω, A, P) be a probability space. Let X0 be a random variable taking its values
in E, (Wn)n≥0 be a sequence of independent random variables taking its values in a ﬁnite set W,
and independent of X0, and for all n ∈N, let fn : E × W →E be a map. Then, the sequence Xn
deﬁned recursively by:
Xn+1 = fn(Xn, Wn),
n ∈N ,
is a Markov chain taking its values in E.
25


## Page 34

Proof. Indeed Xn is a deterministic function of X0, W0, . . . , Wn−1, so is independent of Wn. Hence,
P(Xn+1 = xn+1 | X0 = x0, . . . , Xn = xn) = P(fn(Xn, Wn) = xn+1 | X0 = x0, . . . , Xn =
xn) = P(fn(xn, Wn) = xn+1 | X0 = x0, . . . , Xn = xn) = P(fn(xn, Wn) = xn+1) only de-
pends on xn and xn+1.
From Proposition 2.3, Xn is a Markov chain with transition matrix
M(n)
xnxn+1 = P(fn(xn, Wn) = xn+1)
Proposition 2.12. Conversely, let p0) and M(n) be the initial law and transition Markov matrices
of a Markov chain taking its values in E. There exists a probability space (Ω, A, P), a set W, a
sequence (fn)n≥0 of maps fn : E × W →E, and, over (Ω, A, P), a random variable X0 taking
its values in E with law p(0), and a sequence (Wn)n≥0 of independent random variables, taking
their values in W, and independent of X0, such that the sequence (Xn)n≥0 deﬁned recursively by
Xn+1 = fn(Xn, Wn) is a Markov chain with transition Markov matrices M(n).
Proof. Assume to simplify that E is a ﬁnite set. Let W be the set of maps from E to itself. For
each n ≥0, denote by qn the probability law on W deﬁned, for all w ∈W (w : E →E, x 7→w(x)),
by qn(w) = Q
x∈E M(n)
xw(x). Let X0, W0, . . . , Wn, . . . be independent random variables with values in
E, W ,. . . , W, . . . , respectively with laws p(0), q0, . . . , qn, . . . , respectively. Such a sequence can
be constructed on Ω= E × WN, with A the set of cylinders. Then, taking fn(x, w) = w(x), we get
that Xn+1 = fn(Xn, Wn) deﬁnes a Markov chain with transition Markov matrices M(n).
Exercise 2.3.1. Let (Ω, A, P) be a probability space. Let X0 be a random variable taking its values
in a ﬁnite set E, let (Wn)n≥0 be a Markov chain taking its values in a ﬁnite set W, with initial
law q(0), transition matrix M(n) at time n ≥0, and independent of X0, and for all n ∈N, let
fn : E × W →E be a map. Consider the sequence Xn of random variables taking its values in E,
and deﬁned recursively by:
Xn+1 = fn(Xn, Wn),
n ∈N .
Show that ((Xn, Wn))n≥0 is a Markov chain and compute its transition matrix.
2.4
The digraph of a stationary Markov chain
Deﬁnition 2.13. Let M ∈RE×E be a matrix with nonnegative entries, in particular a Markov
matrix. We associate to M a digraph, denoted G(M), with set of nodes E and set of arcs A such
that (x, y) ∈E × E is in A if and only if Mxy > 0.
We associate also the weight map w : A →R, (x, y) 7→Mxy.
Then, the weight of a path p = (x0, . . . , xn) of G(M) (i.e.
such that x0, . . . , xn ∈E and
(x0, x1), . . . , (xn+1, xn) are arcs in G(M)), is deﬁned as w(p) = w((x0, x1)) × · · · × w((xn−1, xn)) =
Mx0x1 · · · Mxn−1xn.
If Xn is a stationary Markov chain with transition matrix M, we have
P(X1 = x1, . . . , Xn = xn | X0 = x0) =
(
w(x0, . . . , xn) if (x0, . . . , xn) is a path of G(M)
0
otherwise.
Moreover,
P(Xn+k = y | Xk = x) = (Mn)xy =
X
p path of length n
in G(M), from x to y
w(p),
26


## Page 35

where the length of a path is the number of its arcs. Indeed,
Mn
xy
=
X
(x1,...,xn−1)∈En−1
Mxx1 · · · Mxn−2xn−1Mxn−1y
=
X
(x1,...,xn−1)∈En−1
P(Xk+1 = x1, . . . Xk+n−1 = xn−1, Xk+n = y | Xk = x)
=
X
(x1,...,xn−1)∈En−1
Mxx1>0,...,Mxn−1y>0
w(x, x1, . . . , xn−1, y) .
Example 2.14. A Markov matrix and its associated digraph G(M) (with weights written on arcs):
M =


0.5
0.5
0
0.7
0.1
0.2
0
0
1


1
3
2
0.7
0.1
1
0.5
0.5
0.2
Example 2.15 (Random walks). The digraph associated to the random walk of Example 2.2 is as
follows:
Z
p
p
p
1 −p
1 −p
1 −p
n −2
n −1
n
n + 1
The digraph associated to a random walk on Z2 with probability p, q, r, s > 0 to go respectively to
right, up, left and down (with p + q + r + s = 1) is shown in
27


## Page 36

p
p
p
Z2
q
s
r
q
s
2.5
Kolmogorov equation for ﬁnite horizon criteria
The following equation is the dual of Fokker-Plank equation (seen in Proposition 2.6):
Proposition 2.16 (Kolmogorov equation without instantaneous reward). Let (Xn)n∈N be a Markov
chain over (Ω, A, P), taking its values in E, with Markov transition matrices M(n) at time n ∈N.
Let ϕ ∈RE and T ∈N, and denote:
vk(x) = E [ϕ(XT ) | Xk = x] .
Then, the value vk satisﬁes the following backward recurrence equation, called Kolmogorov equa-
tion :
vk = M(k)vk+1, 0 ≤k ≤T −1 ,
with ﬁnal condition:
vT = ϕ .
28


## Page 37

Proof. Let us use the formula already proved for the probabilities of the tuple (X0, . . . , Xn):
vk(x)
=
X
xk+1,...,xT ∈E
(P(Xk+1 = xk+1, . . . , XT = xT | Xk = x)ϕ(xT ))
=
X
xk+1,...,xT ∈E
P(Xk = x, Xk+1 = xk+1, . . . , XT = xT )
P(Xk = x)
ϕ(xT )

=
X
xk+1,...,xT ∈E

M(k)
xxk+1 · · · M(T−1)
xT −1xT ϕ(xT )

=
(M(k) · · · M(T−1)ϕ)x .
Then vk = M(k) · · · M(T−1)ϕ, which implies vk = M(k)vk+1 and vT = ϕ.
Another way to prove the above Kolmogorov equation is to use conditional expectations or
equivalently the notion of martingale. This is explained in Remark 2.20 below after some deﬁnitions
and elementary properties.
Deﬁnition 2.17. Given a Markov chain (Xn)n∈N over (Ω, A, P), we associate the ﬁltration (Fn)n∈N:
Fn := σa(X0, . . . , Xn),
∀n ∈N .
The ﬁltration associated to a Markov chain (Xn)n≥0 is the minimal ﬁltration such that (Xn)n≥0
is adapted to it.
Recall that for any real random variable Y (with respect to A), E [Y | F] denotes the orthogonal
projection of Y onto the subspace of real random variables that are measurable with respect to F.
Moreover, for any random variable X, we denote E [Y | X] := E [Y | σa(X)].
Lemma 2.18. Let (Xn)n∈N be a a Markov chain over (Ω, A, P) with values in E, and let (Fn)n∈N
be its associated ﬁltration. For any (measurable) function ϕ : E →R, and any 0 ≤n ≤T, we have
E [ϕ(XT ) | Fn] = E [ϕ(XT ) | Xn] .
Proof. Since Fn := σa(X0, . . . , Xn), and E is a ﬁnite (or discrete) set, E [ϕ(XT ) | Fn] is neces-
sarily of the form ψn(X0, . . . Xn), where ψn is the deterministic (measurable) function deﬁned
by: ψn(x0, . . . , xn) = E [ϕ(XT ) | X0 = x0, . . . , Xn = xn]. Also (by deﬁnition), E [ϕ(XT ) | Xn] =
E [ϕ(XT ) | F′
n], where F′
n = σa(Xn). Thus it is of the form ψ′
n(Xn), where ψ′
n is measurable and
given by ψ′
n(xn) = E [ϕ(XT ) | Xn = xn].
Since (Xn)n∈N is a Markov chain, we get that ψn(x0, . . . , xn) = E [ϕ(XT ) | Xn = xn] = ψ′
n(xn)
which depends only on xn. So E [ϕ(XT ) | Fn] = ψ′
n(Xn) = E [ϕ(XT ) | Xn].
Deﬁnition 2.19. A sequence (Yn)n∈N of real random variables over (Ω, A, P) is a Martingale with
respect to the ﬁltration (Fn)n≥0 if
E [Yn+1 | Fn] = Yn
∀n ≥0 .
Remark 2.20. Another way to prove Proposition 2.16 is to show that the sequence
Mn = vn(Xn),
n ≥0,
29


## Page 38

is a Martingale for the ﬁltration (Fn)n≥0 associated to the Markov chain (Xn)n≥0, that is
E [Mn+1 | Fn] = Mn .
Indeed, using the deﬁnition of vn, we get, for n ≥0,
Mn = E [ϕ(XT ) | Xn] .
Then, from Lemma 2.18, we obtain
Mn = E [ϕ(XT ) | Fn]
which is clearly a Martingale, by the property of compositions of conditional expectations and since
Fn ⊂Fn+1:
E [Mn+1 | Fn] = E [E [ϕ(XT ) | Fn+1] | Fn] = E [ϕ(XT ) | Fn] = Mn .
This implies that
vk(Xk) = Mk = E [Mk+1 | Fk] = E [vk+1(Xk+1) | Xk] .
So for all x ∈E, we have
vk(x) = E [vk+1(Xk+1) | Xk = x]
=
X
y∈E
P(Xk+1 = y | Xk = x)vk+1(y)
=
X
y∈E
M(k)
xy vk+1(y) = (M(k)vk+1)x ,
so vk = M(k)vk+1, which is the recurrence equation of Proposition 2.16.
The following more general result will be used in what follows in order to establish the Bellman
dynamic programming equation for Markov decision problems, which will be a nonlinear extension
of Kolmogorov equation.
Theorem 2.21 (Kolmogorov Equation for an additive functional). Let (Xn)n∈N be a Markov chain
over (Ω, A, P), taking its values in E, with Markov transition matrices M(n) at time n ∈N. Let
ϕ ∈RE, T ∈N, and rk ∈RE for 0 ≤k ≤T −1, and denote:
vk(x) = E
" T−1
X
ℓ=k
rℓ(Xℓ)
!
+ ϕ(XT ) | Xk = x
#
.
Then, vk satisﬁes the following backward recurrence equation, called Kolmogorov equation :
vk = rk + M(k)vk+1, 0 ≤k ≤T −1 ,
(2.3a)
with ﬁnal condition:
vT = ϕ .
(2.3b)
30


## Page 39

Proof. Use the second way of proof of previous Kolmogorov equation:
vk(x) = E
" T−1
X
ℓ=k
rℓ(Xℓ)
!
+ ϕ(XT ) | Xk = x
#
= E [rk(Xk) | Xk = x] + E
" T−1
X
ℓ=k+1
rℓ(Xℓ)
!
+ ϕ(XT ) | Xk = x
#
= rk(x) + E
"
E
" T−1
X
ℓ=k+1
rℓ(Xℓ)
!
+ ϕ(XT ) | Xk+1
#
| Xk = x
#
= rk(x) + E [vk+1(Xk+1) | Xk = x]
= rk(x) +
X
y∈E
P(Xk+1 = y | Xk = x)vk+1(y)
= rk(x) +
X
y∈E
M(k)
xy vk+1(y)
= (rk + M(k)vk+1)x ,
hence vk = rk + M(k)vk+1.
Remark 2.22. As in Remark 2.20, another way to prove Theorem 2.21 is to show that for all k ≥0,
the sequence
Mn =
 n−1
X
ℓ=k
rℓ(Xℓ)
!
+ vn(Xn),
n ≥k,
is a Martingale for the ﬁltration (Fn)n≥0 associated to the Markov chain (Xn)n≥k. Indeed, using
the deﬁnition of vn, we get, for n ≥k,
Mn =
 n−1
X
ℓ=k
rℓ(Xℓ)
!
+ E
" T−1
X
ℓ=n
rℓ(Xℓ)
!
+ ϕ(XT ) | Xn
#
and since Xk, . . . , Xn−1 are measurable with respect to Fn and Xn is a Markov chain, so the above
conditional expectation with respect to Xn is equivalent to the one with respect to Fn, we get
Mn = E
" n−1
X
ℓ=k
rℓ(Xℓ)
!
+
 T−1
X
ℓ=n
rℓ(Xℓ)
!
+ ϕ(XT ) | Fn
#
= E
" T−1
X
ℓ=k
rℓ(Xℓ)
!
+ ϕ(XT ) | Fn
#
which is clearly a Martingale. This implies that
vk(Xk) = Mk = E [Mk+1 | Fk] = rk(Xk) + E [vk+1(Xk+1) | Fk] = rk(Xk) + E [vk+1(Xk+1) | Xk] ,
which gives the recurrence equation of Theorem 2.21.
Remark 2.23. When rk = r and M(k) = M do not depend on k, (hence the Markov chain (Xn)n∈N
is stationary), the Kolmogorov equation writes vk = r + Mvk+1, so that one can consider the value
function as a function of the remaining time until the end:
v(t)(x) = E
" t−1
X
ℓ=0
rℓ(Xℓ)
!
+ ϕ(Xt) | X0 = x
#
,
31


## Page 40

which satisﬁes a forward Kolmogorov equation:
v(t+1) = r + Mv(t) .
Remark 2.24. Moreover, Kolmogorov equation can be rewritten as
vk −vk−1 + (M −I)vk + r = 0 .
which is analogue to the Kolmogorov equation of a Markov process (with continuous time):
dv
dt + (M −I)v + r = 0 .
Then, M −I is called the inﬁnitesimal generator of the Markov chain.
(A Markov process is
obtained when the holding times in each state are random independent with exponential law).
A similar Kolmogorov equation is obtained when (Xt)t≥0 is a Wiener process:
dv
dt + 1
2∆v + r = 0 .
Exercise 2.5.1. Compute
v := E
" T−1
X
ℓ=0
rℓ(Xℓ)
!
+ ϕ(XT )
#
,
for any initial law of the Markov chain (Xn)n≥0.
Exercise 2.5.2. Let Xn be a Markov chain with values in (a ﬁnite subset of) N, and consider the
sequence Yn = X0 + · · · + Xn. Compute
v(x) = E [ϕ(YT ) | X0 = x] .
Do the same for Yn = max(X0, . . . , Xn).
Exercise 2.5.3. Consider a Markov chain (Xn)n≥0 with values in E and transition matrix M ∈RE×E
(independent of time). Let f be a function from E to R, compute
vT (x) = P (∃n ∈{0, . . . , T}, f(Xn) ≥1 | X0 = x) .
Taking the exponential of an additive functional does not change optimization problems, but it
does change expectation.
Theorem 2.25 (Kolmogorov equation for a multiplicative functional). Let (Xn)n∈N be a Markov
chain over (Ω, A, P), taking its values in E, with Markov transition matrices M(n) at time n ∈N.
Let ϕ ∈RE, T ∈N, and αk ∈RE
+, for 0 ≤k ≤T −1, and denote:
vk(x) = E
" T−1
Y
ℓ=k
αℓ(Xℓ)
!
ϕ(XT ) | Xk = x
#
.
Let A(k) ∈RE×E be the matrix with nonnegative entries A(k)
xy = αk(x)M(k)
xy , for x, y ∈E. Then, vk
satisﬁes the following backward recurrence equation:
vk = A(k)vk+1, 0 ≤k ≤T −1 ,
(2.4a)
with ﬁnal condition:
vT = ϕ .
(2.4b)
32


## Page 41

Proof. We use again the same arguments as for the previous Kolmogorov equations:
vk(x) = E
" T−1
Y
ℓ=k
αℓ(Xℓ)
!
ϕ(XT ) | Xk = x
#
= αk(x)E
"
E
" T−1
Y
ℓ=k+1
αℓ(Xℓ)
!
ϕ(XT ) | Xk+1
#
| Xk = x
#
= αk(x)E [vk+1(Xk+1) | Xk = x]
= αk(x)

X
y∈E
P(Xk+1 = y | Xk = x)vk+1(y)


= αk(x)

X
y∈E
M(k)
xy vk+1(y)


=
X
y∈E
A(k)
xy vk+1(y) ,
which gives vk = A(k)vk+1.
Again, with the same arguments, one proves:
Theorem 2.26 (Kolmogorov equation for a mixed functional). Let (Xn)n∈N be a Markov chain
over (Ω, A, P), taking its values in E, with Markov transition matrices M(n) at time n ∈N. Let
ϕ ∈RE, T ∈N, rk ∈RE, and αk ∈RE
+, for 0 ≤k ≤T −1, and denote:
vk(x) = E
" T−1
X
ℓ=k
 ℓ−1
Y
m=k
αm(Xm)
!
rℓ(Xℓ)
!
+
 T−1
Y
m=k
αm(Xm)
!
ϕ(XT ) | Xk = x
#
.
Let A(k) ∈RE×E be the matrix with nonnegative entries A(k)
xy = αk(x)M(k)
xy , for x, y ∈E. Then, vk
satisﬁes the following backward recurrence equation:
vk = rk + A(k)vk+1, 0 ≤k ≤T −1 ,
(2.5a)
with ﬁnal condition:
vT = ϕ .
(2.5b)
When αk(x) ≡α < 1, α is the discount factor, as for determinitic control problems with inﬁnite
horizon.
More generally, when αk(x) ≤1 depends on x, we call it a variable discount factor.
In that case, the matrix A(k) satisﬁes A(k)1 ≤1. A matrix A with nonnegative entries and such
that A1 ≤1 is called a submarkovian matrix.
When the matrices A(k) are submarkovian, one can reduce the previous problem/functional to
a problem with additive criteria, by adding to the state space E a cemetery point. Indeed, let c
33


## Page 42

denote this cemetery point, assume that c̸ ∈E, and consider E′ = E ∪{c}. Let M′(k) ∈RE′×E′ be
the matrix such that
M′(k)
xy
= A(k)
xy ,
when x, y ∈E
M′(k)
cc
= 1,
M′(k)
cx
= 0,
∀x ∈E
M′(k)
xc
= 1 −αk(x),
∀x ∈E ,
and extend rk and ϕ to E′ in r′
k and ϕ′ respectively by mapping c to 0.
Proposition 2.27. The value function vk of Theorem 2.26 is the restriction to E of the value
function v′
k obtained in Theorem 2.21 for the matrices M′(k) and functions r′
k et ϕ′.
Note that v′
k satisﬁes necessarily v′
k(c) = v′
k+1(c) = · · · = ϕ′(c) = 0, so the boundary equation:
v′
k(c) = 0 .
2.6
Kolmogorov Equations for inﬁnite horizon criteria
Theorem 2.28 (Kolmogorov Equations for a discounted inﬁnite horizon functional). Let (Xn)n∈N
be a stationary Markov chain over (Ω, A, P), taking its values in E, with Markov transition matrix
M. Let r, α ∈RE, satisfying 0 ≤α(x) ≤¯α for all x ∈E, for some constant ¯α < 1. Assume that r
is bounded in sup-norm (or E is ﬁnite). Denote:
.v(x) = E
" ∞
X
ℓ=0
 ℓ−1
Y
m=0
α(Xm)
!
r(Xℓ)
!
| X0 = x
#
.
(2.6)
Let A ∈RE×E be the matrix with nonnegative entries Axy = α(x)Mxy, for x, y ∈E. Then, v is the
unique solution of the ﬁxed point linear equation:
v = r + Av ,
(2.7)
Before giving the proof let us state some properties of Markov matrices.
Recall that for any matrix M ∈RE×E, the matrix norm ∥M∥∞associated to the sup-norm of
vectors, deﬁned by:
∥M∥∞:=
sup
u∈RE\{0}
∥Mu∥∞
∥u∥∞
,
∥u∥∞=: sup
x∈E
|ux| ,
satisﬁes
∥M∥∞= sup
x∈E

X
y∈E
|Mxy|

,
and that spectral radius of M, denoted ρ(M), which is the maximum of the modulus of its
eigenvalues satisﬁes necessarily ρ(M) ≤∥M∥for any matrix norm.
Lemma 2.29. For any Markov matrix M ∈RE×E, we have
ρ(M) = ∥M∥∞= 1 .
34


## Page 43

Proof. Since a Markov matrix M has nonnegative entries, and the sum of each row is equal to 1,
we get ∥M∥∞= 1.
Since 1 is an eigenvalue of M associated to the eigenvector 1 (M1 = 1), we get ρ(M) ≥1.
Since 1 ≤ρ(M) ≤∥M∥∞= 1, we deduce the result.
Proof of Theorem 2.28. Assume that E is ﬁnite. Since α(Xm) ≤¯α < 1, for all m ≥0, and r is
bounded, the series inside the expectation in (2.6) is normally converging (for sup-norm), and its
sum is a.s. bounded by C/(1 −¯α), where C is a bound of r. Hence, the expectation v(x) exists,
for all x ∈E, which allows one to deﬁne the value function v : x 7→v(x).
By the same arguments as in previous proofs, one shows that v satisﬁes (2.7). So it remains to
prove that (2.7) has a unique solution. This holds if I −A is invertible, that is 1 is not an eigenvalue
of A. Using the formula of the sup-norm of a matrix, we get that ∥A∥∞≤¯α∥M∥∞= ¯α < 1, which
implies that ρ(A) ≤¯α < 1, and so I −A is invertible.
One can also show that the Kolmogorov operator: K : v 7→r + Av is monotone and contracting
for the sup-norm with factor ¯α < 1. Indeed
∥K(v) −K(w)∥∞= ∥A(v −w)∥∞≤∥A∥∞∥v −w∥∞≤¯α∥v −w∥∞.
So K has a unique ﬁxed point.
This property holds also when E is a countable set (discrete inﬁnite), by considering K as
an operator on the Banach space L∞(E) of bounded functions from E to R, endowed with the
sup-norm.
In sustainable development problems, on may wish to consider a functional which put more
weight on future rewards. This would mean that some of the discount factors α(x) are greater than
1, and so A is no more contracting for the sup-norm. However, the previous result remains if the
spectral radius of A remains lower than 1 as in the following result.
Theorem 2.30. Let (Xn)n∈N be a stationary Markov chain over (Ω, A, P), taking its values in a
ﬁnite set E, with Markov transition matrix M. Let r, α ∈RE, satisfying 0 ≤α(x) for all x ∈E. Let
A ∈RE×E be the matrix with nonnegative entries Axy = α(x)Mxy, for x, y ∈E. Assume that the
spectral radius ¯α := ρ(A) is < 1. Then, for all x ∈S, the value v(x) of (2.6) is well deﬁned and
the function v : E →R, x ∈E 7→v(x) is the unique solution of the ﬁxed point linear equation (2.7).
Proof. Since S is a ﬁnite set, r is bounded by some constant C. Hence
∞
X
ℓ=0

 ℓ−1
Y
m=0
α(Xm)
!
r(Xℓ)
 ≤CY
where Y is the nonnegative random variable deﬁned by
Y :=
∞
X
ℓ=0
 ℓ−1
Y
m=0
α(Xm)
!
.
Since Y is the sum of series with nonnegative coeﬀcients, its expectation exists and is equal to
E [Y | X0 = x] =
∞
X
ℓ=0
wk(x)
with
wk(x) := E
" k−1
Y
m=0
α(Xm) | X0 = x
#
.
35


## Page 44

Using Kolmogorov equation for multiplicative functionals, we obtain that wk satisﬁes wk = Awk−1
and w0 = 1, hence wk = Ak1. Therefore, E [Y | X0 = x] = P∞
ℓ=0(Ak1)x. Since ρ(A) < 1, the
previous series converges and is equal to ((I −A)−11)x. Then, Y has a ﬁnite expectation, which
implies (by dominated convergence theorem) that the random variable P∞
ℓ=0
Qℓ−1
m=0 α(Xm)

r(Xℓ)
is well deﬁned (exists almost surely) and has a ﬁnite expectation. Hence, the value v(x) in (2.6)
is well deﬁned. The rest of the result can be proved using the same arguments as for previous
theorem.
2.7
Kolmogorov Equations for stopping time criteria
Deﬁnition 2.31. Given a ﬁltration (Fn)n∈N on (Ω, A), a random variable τ with values in N∪{+∞}
is a stopping time with respect to (Fn)n∈N if {τ ≤n} ∈Fn, for all n ∈N. We then denote
Fτ := {A ∈A | {τ ≤t} ∩A ∈Ft, ∀t ≥0} .
Fact 2.32. τ is a stopping time if and only if {τ = n} ∈Fn, for all n ∈N.
Proof. If {τ = n} ∈Fn, for all n ∈N, then {τ ≤n} = ∪k=0,...,n{τ = k} ∈Fn, since Fk ⊂Fn, for
all k ≤n. Conversely, if {τ ≤n} ∈Fn, for all n ∈N, then {τ = n} = {τ ≤n} \ {τ ≤n −1} ∈Fn,
since Fn−1 ⊂Fn.
Deﬁnition 2.33. Given a Markov chain (Xn)n∈N over (Ω, A, P), we associate the ﬁltration (Fn)n∈N
as in Deﬁnition 2.17. Then, a random variable τ with values in N ∪{+∞} is a stopping time with
respect to the Markov chain (Xn)n∈N if it is a stopping time with respect to (Fn)n∈N.
Example 2.34. Let (Xn)n∈N be a Markov chain over (Ω, A, P), with values in E, and let B be a
subset of E. Then, for all k ∈N,
τ k
B := inf{n ≥k | Xn̸ ∈B}
is a stopping time with respect to the Markov chain (Xn)n≥k. Indeed, for t ≥0, {τ k
B > t} =
T
k≤ℓ≤t{Xℓ∈B} belongs to σa(Xk, . . . , Xt), so does its complementary {τ k
B ≤t}. The stopping
time τ k
B is called the exit time from B of the Markov chain starting at time k.
Theorem 2.35 (Strong Markov property). Let (Xn)n∈N be a Markov chain over (Ω, A, P), taking
its values in E. Let τ be a stopping time with respect to (Xn)n≥0. We have,
P(Xτ+1 = y1, . . . , Xτ+k = yk | X0 = x0, . . . , Xτ−1 = xτ−1, Xτ = y0 and τ < +∞)
= P(Xτ+1 = y1, . . . , Xτ+k = yk | Xτ = y0 and τ < +∞) .
for all k ∈N, sequences (xℓ)ℓ≥0, and y0, . . . , yk ∈E.
Moreover if the chain is stationary then
P(Xτ+1 = y1, . . . , Xτ+k = yk | Xτ = y0 and τ < +∞) = P(X1 = y1, . . . , Xk = yk | X0 = y0) .
Theorem 2.36 (Kolmogorov Equation for a ﬁnite horizon functional with stopping time). Let
(Xn)n∈N be a Markov chain over (Ω, A, P), taking its values in E, with Markov transition matrices
36


## Page 45

M(n) at time n ∈N. Let ϕ ∈RE, B ⊂E be nonempty, T ∈N, and rk ∈RB for 0 ≤k ≤T −1, and
denote, for all x ∈E:
vk(x) = E




T∧τ k
B−1
X
ℓ=k
rℓ(Xℓ)

+ ϕ(XT∧τ k
B) | Xk = x

.
Then, vk satisﬁes the following backward recurrence equation, called Kolmogorov equation :
vk(x) = rk(x) + (M(k)vk+1)(x), x ∈B, 0 ≤k ≤T −1 ,
(2.8a)
with boundary condition
vk(x) = ϕ(x), x̸ ∈B ,
(2.8b)
and ﬁnal condition
vT (x) = ϕ(x), x ∈B .
(2.8c)
Note that here, we used the same name ϕ for the function involved in the boundary condition
and in the ﬁnal condition. In general, and in particular when the state space is continuous, one
considers two maps ϕ ∈RB and ψ ∈RE\B, and deﬁne vk as the functional
vk(x) = E




T∧τ k
B−1
X
ℓ=k
rℓ(Xℓ)

+ ϕ(XT )1T<τ k
B + ψ(Xτ k
B)1T≥τ k
B | Xk = x

.
Proof of Theorem 2.36. Consider the sequence Yn = Xn∧τ k
B, for n ≥k. With the same arguments
as for the strong Markov property, we can show that this is a Markov chain starting at time n = k.
Indeed,
P(Yn = yn, · · · , Yk = yk) =
n−1
X
p=k
P(Yn = yn, · · · , Yk = yk, τ k
B = p)
+ P(Yn = yn, · · · , Yk = yk, τ k
B ≥n)
=
n−1
X
p=k
P(Xn∧p = yn, · · · , Xk = yk, τ k
B = p)
+ P(Xn = yn, · · · , Xk = yk, τ k
B ≥n)
=
n−1
X
p=k
P(Xp = yp, · · · , Xk = yk)1yk∈B · · · 1yp−1∈B1yp̸∈B1yp=yp+1=···=yn
+ P(Xn = yn, · · · , Xk = yk)1yk∈B · · · 1yn−1∈B
=



n=1
X
p=k
M(p−1)
yp−1yp · · · M(k)
ykyk+11yk∈B · · · 1yp−1∈B1yp̸∈B1yp=yp+1=···=yn
+M(n−1)
yn−1yn · · · M(k)
ykyk+11yk∈B · · · 1yn−1∈B
o
P(Yk = yk)
=M(B,n−1)
yn−1yn · · · M(B,k)
ykyk+1P(Yk = yk) ,
37


## Page 46

where, for n ≥k, M(B,n) is given by:
M(B,n)
xy
=





M(n)
xy
for x ∈B, y ∈E
1
for x = y̸ ∈B
0
otherwise.
Hence, by Proposition 2.3, (Yn)n≥k is a Markov chain with transition matrix M(B,n) at time n ≥k.
For all n ≥0, extend rn by 0 on E \ B. Then, for all x ∈E, vk coincides with:
vk(x) = E
" T−1
X
ℓ=k
rℓ(Yℓ)
!
+ ϕ(YT ) | Yk = x
#
.
From Theorem 2.21, we get the recurrence equation
vk = rk + M(B,k)vk+1, 0 ≤k ≤T −1 ,
with ﬁnal condition: vT = ϕ. This ﬁnal condition implies (2.8c). When x ∈B, the recurrence
equation gives (2.8a). When x̸ ∈B, the recurrence equation gives vk(x) = vk+1(x), which with the
ﬁnal condition implies vk(x) = ϕ(x), hence the boundary equation (2.8b).
Another way to prove Theorem 2.36 is to use Theorem 2.26 and the following result, which is
easy to check.
Fact 2.37. The value function vk of Theorem 2.36 can rewritten as the value function of the mixed
functional :
vk(x) = E
" T−1
X
ℓ=k
 ℓ−1
Y
m=k
αm(Xm)
!
r′
ℓ(Xℓ)
!
+
 T−1
Y
m=k
αm(Xm)
!
ϕ(XT ) | Xk = x
#
,
for the same Markov chain (Xn)n≥0, with the same ﬁnal reward ϕ, and the instantaneous rewards
r′
k and variable discount factors αk given by:
r′
k(x) = rk(x),
for x ∈B
r′
k(x) = ϕ(x),
for x̸ ∈B
αk(x) = 1,
for x ∈B
αk(x) = 0,
for x̸ ∈B .
We can derive similarly the solution of the discounted inﬁnite horizon problem with stopping
time.
Theorem 2.38 (Kolmogorov Equations for discounted inﬁnite horizon with stopping time). Let
(Xn)n∈N be a stationary Markov chain over (Ω, A, P), taking its values in E, with Markov transition
matrix M. Let B ⊂E be nonempty, r ∈RB, and α ∈(0, 1), Assume that r is bounded in sup-norm
(or E is ﬁnite). Denote, for all x ∈E,
v(x) = E
" τB−1
X
ℓ=0
αℓr(Xℓ)
!
+ ατBϕ(XτB) | X0 = x
#
.
(2.9)
Then, v is the unique solution of the ﬁxed point linear equation:
 v(x)
= r(x) + α(Mv)(x)
x ∈B ,
v(x)
= ϕ(x)
x̸ ∈B .
38


## Page 47

We can in some cases avoid the discount factor.
Theorem 2.39 (Kolmogorov Equations for undiscounted inﬁnite horizon with stopping time).
Let (Xn)n∈N be a stationary Markov chain over (Ω, A, P), taking its values in E, with Markov
transition matrix M. Let B ⊂E be nonempty, r ∈RB. Assume that r is bounded in sup-norm (or
E is ﬁnite), and that the matrix MBB ∈RB×B, which is the restriction of M to rows and columns
in B ((MBB)xy = Mxy for all x, y ∈B) has a spectral radius ρ < 1. Denote, for all x ∈E,
v(x) = E
" τB−1
X
ℓ=0
r(Xℓ)
!
+ ϕ(XτB) | X0 = x
#
.
(2.10)
Then, v is well deﬁned and it is the unique solution of the ﬁxed point linear equation:
 v(x)
= r(x) + (Mv)(x)
x ∈B ,
v(x)
= ϕ(x)
x̸ ∈B .
Proof. Same arguments as for the proof of Theorem 2.30.
Example 2.40. Consider a Markov chain with transition matrix
M =


1/2
1/2
0
1/2
1/2
0
0
1/2
1/2

.
If one consider B = {1, 2} ⊂E, then τB = +∞almost surely since B is a recurrence class. Then,
E
h
(PτB−1
k=0 r(Xk)) + ϕ(XτB) | X0 = x
i
= ∞if for instance r = (1 1 0)T .
Now if B = {2, 3}, then τB < +∞almost surely, and
MBB =
1/2
0
1/2
1/2

satisﬁes ρ(MBB) = 1/2. Then, v(x) = E
h
(PτB−1
k=0 r(Xk)) + ϕ(XτB) | X0 = x
i
exists and is solution
of
v(1) = ϕ(1)
v(2) = r(2) + 1
2v(1) + 1
2v(2)
v(3) = r(3) + 1
2v(2) + 1
2v(3) .
This gives
v(1) = ϕ(1)
v(2) = 2r(2) + ϕ(1)
v(3) = 2r(3) + 2r(2) + ϕ(1) .
39


## Page 48

2.8
Further examples
Example 2.41 (A rolling dice game). Consider a game in N steps. At each step, the player is
rolling a dice. If the dice falls on 6, the player is loosing all his previous gains positive or negative,
otherwise he receives the value of the dice minus 3 as an additional gain. Denoting by Wn the
value of the dice at the nth stage of the game, we get that (Wn)n≥0 is an i.i.d. sequence of random
variables with laws: P(Wn = i) = 1/6 for i ∈{1, . . . , 6}.
If the dice neither fall on 6, the total gain/payoﬀof the player at stage n would be equal to
W1 −3 + · · · + Wn −3. Since the player may loose everything, one need to consider a new sequence
Xn of states consisting in the (possible) total reward at time n. We starts with X0 = 0 and get
that
Xn+1 =
(
Xn + Wn+1 −3
if Wn+1̸ = 6
0
otherwise,
for all n = 0, . . . , N −1. Such a dynamics can be written Xn+1 = f(Xn, Wn+1), which implies that
the sequence (Xn)n≥0 is a Markov chain with values in Z. The expected total reward at the end of
the game is then equal to E [XT ], which has the form of the criterion considered in Proposition 2.16.
Then it can be computed by using the Kolmogorov equation. Using the dynamics f, instead of
transition probabilities, Kolmogorov equation can be written as follows
vk(x) = E [vk+1(f(x, Wk+1))] ,
vT (x) = x,
x ∈Z .
Then, E [XT ] = v0(0) (since X0 = 0). Using the above informations on f and the law of (Wn)n≥0,
we can rewrite the Kolmogorov equation as:
vk(x) = 1
6{vk+1(0) +
5
X
i=1
vk+1(x + i −3)}
x ∈Z .
Then, using that vT (x) = x, we can prove by backward induction on k that vk is linear in x:
vk(x) = zkx with zk = zk+1 5
6. This implies that the game has no expected gain.
2.9
Solutions of Exercises
Exercise 2.3.1.
Exercise 2.5.1.
Let
v := E
" T−1
X
ℓ=0
rℓ(Xℓ)
!
+ ϕ(XT )
#
.
Using the property that v = E
h
E
hPT−1
ℓ=0 rℓ(Xℓ)

+ ϕ(XT ) | X0
ii
, we get that v = p(0)v0, where
v0 is the solution of Kolmogorov equation.
Exercise 2.5.2.
Let Xn be a Markov chain with values in (a ﬁnite subset E of) N, and consider
the sequence Yn = X0 + · · · + Xn. Then, Yn satisﬁes the recurrence Yn+1 = Yn + Xn+1. Since Xn is
a Markov chain, then (Xn, Yn) is a Markov chain on E × N. Let ˜
M(n) be its transition probability
matrix. We have
˜
M(n)
(x,y)(x′,y′) = M(n)
xx′ 1(y+x′)y′ .
40


## Page 49

Moreover
v(x) = E [ϕ(YT ) | X0 = x] = E [ ˜ϕ(XT , YT ) | (X0, Y0) = (x, 0)] ,
with ˜ϕ(x, y) = ϕ(y). So v(x) = w0(x, 0) where wk satisﬁes Kolmogorov equation wk = ˜
M(k)wk+1,
that is
wk(x, y) =
X
x′∈E
M(k)
xx′wk+1(x′, y + x′) ,
with wT = ˜ϕ.
Exercise 2.5.3.
Consider a Markov chain (Xn)n≥0 with values in E and transition matrix
M ∈RE×E (independent of time). Let f be a function from E to R, compute
vT (x) = P (∃n ∈{0, . . . , T}, f(Xn) ≥1 | X0 = x) .
41


## Page 50

42


## Page 51

Chapter 3
Markov decision processes with ﬁnite
horizon criteria
We now consider a discrete time dynamical system (Xn)n≥0 with ﬁnite (or discrete) state space E
and a dynamics of the following type:
Xn+1 = fn(Xn),
n ≥1 ,
which can both be changed (by a company manager, an investor, a provider, a driver,...), by
applying an action or control Un at each time or stage n ≥0, and be subject to randomness. For
instance:
Xn+1 = fn(Xn, Un, Wn),
n ≥0 .
The aim is still to choose the sequence of actions U0, . . . , Uk, . . . in such a way that they minimize
(resp. maximize) a certain functional, called the total cost (resp. the total payoﬀ).
However, we assume that information on the sequences Xn and Wn arrive sequentially, so that
at time n, the “manager” only knows X0, . . . , Xn and W0, . . . , Wn. Then, the decision to choose Un
is taken at time n using this information. We are still in the context of complete observation since
we know all the past states, however we do not know the future states. This is the main diﬀerence
with deterministic control problems, in which, given the model, and the state at some time n, we
can infer all the state trajectory (Xk)k≥n.
Since we cannot observe the future realizations of the Markov chain (when the sequence of
actions is ﬁxed for instance), we shall optimize a functional which is the expectation of the total
payoﬀgiven the initial state, which is a criteria already considered in the chapter on Markov chains,
Chapter 2.
Another diﬃculty is that the choice of the actions (Un)n≥0 changes the random process (Xn)n≥0,
so we cannot start with a Markov chain on a given probability space as in previous chapter. We
can only deﬁne a model with all the parameters of the system, like the dynamics or the transition
probabilities, and the initial law. This is what is called a Markov decision process or a controlled
Markov chain.
3.1
Markov decision processes
Deﬁnition 3.1. A Markov Decision Process (MDP) or a controlled Markov chain consists in giving
the following parameters:
43


## Page 52

• a ﬁnite or discrete state space E;
• an action space C
• for all k ∈N and x ∈E, the subset Ck(x) ⊂C of all possible actions at time k, when the state
is equal to x;
• for all k ∈N, the set Ak := {(x, u) | x ∈E, u ∈Ck(x)} of all possibles couples (state, action)
at time k;
• an initial probability p(0) ∈∆E on E, or an initial state x0 ∈E, which is equivalent to the
case where p(0) is the Dirac measure at x0;
• for all k ∈N, x ∈E and u ∈Ck(x), a probability row vector M(k,u)
x
over E, the entries of
which will be denoted

M(k,u)
xy

y∈E.
The MDP is stationary if Ck(x) and M(k,u)
x
do not depend on time k. In this case, the index or
argument k is omitted. It is uncontrolled if the sets Ck(x) are singletons. In this case, the argument
u is omitted.
In the uncontrolled case, the above parameters allow one to construct a Markov chain (and a
probability space), by considering the transition probability matrices
M(k)
xy = P(Xk+1 = y | Xk = x) .
In the general case, one wish to construct (a probability space and) two discrete time processes
(Xk)k≥0 and (Uk)k≥0 taking their values in E and C respectively, with transition probabilities M(k,u)
xy
:
M(k,u)
xy
= P(Xk+1 = y | Xk = x, Uk = u) ,
(3.1a)
and such that (Xk) satisﬁes the following Markov property:
P(Xk+1 = xk+1 | Xk = xk, Uk = uk, Xk−1 = xk−1, Uk−1 = uk−1, . . . , X0 = x0, U0 = u0)
=
P(Xk+1 = xk+1 | Xk =k, Uk = uk) ,
∀xi ∈E, ui ∈Ci(xi), for i ≥0 .
(3.1b)
To deﬁne the underlying probability, one need to assume that the control process (Uk)k≥0 is ad-
missible, meaning that Uk depends only on the past of states and actions, or more precisely that
(Uk)k≥0 is obtained from a strategy, where we extend the notion of strategy as follows.
Deﬁnition 3.2. Given a MDP as above, the set Hk = A0 × · · · × Ak−1 × E is called the set of
histories at time k. A pure strategy is a sequence σ = (σk)k≥0 such that, for all k ≥0, σk, called
the strategy at time k, is a map from Hk to C satisfying
σk(x0, u0, . . . , xk−1, uk−1, xk) ∈Ck(xk), for all (x0, u0, . . . , xk−1, uk−1, xk) ∈Hk .
We denote by Σ the set of all pure strategies. A pure strategy gives rise to the stochastic process
(Xk, Uk)k≥0 with transition probabilities as in (3.1), satisfying in addition
Uk = σk(X0, U0, . . . , Xk−1, Uk−1, Xk) ,
that is there exists a probability space (Ω, A, P) and a stochastic process (Xk, Uk)k≥0 over this
space satisfying all the above properties. Such a sequence (Xk, Uk)k≥0 is also called an admissible
sequence of states and controls.
44


## Page 53

Deﬁnition 3.3. A random (or relaxed) strategy is a sequence σ = (σk)k≥0 such that, for all k ≥0,
σk is a map from Hk to the space of probabilities, denoted here CR, over a given probability space
(C, AC) such that the support of σk(x0, u0, . . . , xk−1, uk−1, xk) is included in Ck(xk), for all
(x0, u0, . . . , xk−1, uk−1, xk) ∈Hk. Such a strategy gives rise to a stochastic process (Xk, Uk)k≥0
satisfying, for all B ∈AC,
P(Uk ∈B | X0, U0, . . . , Xk−1, Uk−1, Xk) = [σk(X0, U0, . . . , Xk−1, Uk−1, Xk)](B) .
We denote by ΣR the set of all relaxed strategies.
Deﬁnition 3.4. A pure or random strategy is said Markovian if each map σk depends only on the
information on the state at the current time, that is
σk(x0, u0, . . . , xk−1, uk−1, xk) = πk(xk) ,
for some map πk from E to C or CR.
A pure Markovian strategy is also called a feedback strategy or feedback policy. We denote by
π = (πk)k≥0 such a policy and call πk the policy at time k.
We denote by Π and ΠR the sets of all feedback and Markov strategies respectively, and by Πk
and ΠR
k the sets of k-coordinates of elements of Π and ΠR respectively.
When Ck and M(k,u)
x
do not depend on k (for all x ∈E and u ∈C(x)), we say that a (pure or
relaxed) Markovian strategy is stationary if πk does not depend on k, in which case π also denotes
each of the πk.
Deﬁnition 3.5. A pure strategy is an open-loop strategy if σk depends only on the initial state,
that is
σk(x0, u0, . . . , xk−1, uk−1, xk) = ωk(x0) for all (x0, u0, . . . , xk−1, uk−1, xk) ∈Hk .
We denote by OL the set of all open-loop strategies.
Deﬁnition 3.6. Given a MDP as in Deﬁnition 3.1, and a feedback policy π = (πk)k≥0 ∈Π, we
associate the Markov transition matrices M(k,πk) at time k, where for all k ∈N, πk ∈Πk, the
matrix M(k,π) is deﬁned by
M(k,π)
xy
:= M(k,πk(x))
xy
, ∀x, y ∈E .
Fact 3.7. Given a MDP as in Deﬁnition 3.1, and a feedback policy π = (πk)k≥0 ∈Π, the associated
stochastic process (Xk, Uk)k≥0 as in Deﬁnition 3.2 is such that (Xk)k≥0 is a Markov chain with initial
law p(0) and transition probability matrices M(k,πk) at time k. Moreover, Uk = πk(Xk), and so
(Xk, Uk)k≥0 is also a Markov chain taking its values in E × C.
Another deﬁnition of a MDP is sometimes given, which can be shown to be equivalent to the
previous one at least in the case of ﬁnite state and action spaces, up to the choice of the probability
space.
Deﬁnition 3.8. A Markov Decision Process (MDP) or a controlled Markov chain consists in giving
the following parameters:
• a ﬁnite or discrete state space E;
45


## Page 54

• an action space C
• for all k ∈N and x ∈E, the subset Ck(x) ⊂C of all possible actions at time k, when the state
is equal to x;
• for all k ∈N, the set Ak := {(x, u) | x ∈E, u ∈Ck(x)} of all possibles couples (state, action)
at time k;
• an initial probability p(0) ∈∆E on E, or an initial state x0 ∈E, which is equivalent to the
case where p(0) is the Dirac measure at x0;
• a probability space (Ω, A, P), a random variable X0 with values in E and law p(0), and a
sequence of independent random variables (Wn)n≥0 with values in some discrete space W,
independent from X0;
• for all k ≥0, the dynamics at time k, which is a map fk : Ak × W →E.
The MDP is stationary if Ck(x) and fk do not depend on time k, and if the Wk are identically
distributed. In this case, the index or argument k is omitted. It is uncontrolled if the sets Ck(x)
are singletons. In this case, the argument u is omitted.
Given a MDP in the sense of Deﬁnition 3.8, and a strategy of one of the above form, one can
construct on a probability space (extending (Ω, A, P)), two discrete time processes (Xk)k≥0 and
(Uk)k≥0 taking their values in E and C respectively, satisfying:
Xn+1 = fn(Xn, Un, Wn),
n ≥0 .
(3.2)
Fact 3.9. Given a MDP in the sense of Deﬁnition 3.8, we can construct the following transition
probabilities which deﬁne a MDP in the sense of Deﬁnition 3.1, with same behavior as the initial
MDP:
M(k,u)
xy
= P(fk(x, u, Wk) = y) .
Proof. Indeed, given the probability space as in Deﬁnition 3.8, and the random variables X0 and
Wn, for all pure strategies σ, one can associate the random process (Xk, Uk)k≥0 satisfying both
(3.2) and
Uk = σk(X0, U0, . . . , Xk−1, Uk−1, Xk) .
In that case,
M(k,u)
xy
= P(Xk+1 = y | Xk = x, Uk = u)
= P(fk(x, u, Wk) = y) .
Moreover, if W is ﬁnite or discrete, then
P(fk(x, u, Wk) = y) =
X
w∈W, s.t. fk(x,u,w)=y
P(Wk = w) .
If one consider a relaxed strategy however, one need to increase the probability space in order to
handle all the possible probability laws σk(X0, U0, . . . , Xk−1, Uk−1, Xk).
46


## Page 55

Associated to a Markov decision process, we can consider a Markov decision problem or a discrete
time stochastic control problem which consists in maximizing (or minimizing) a criteria equal to the
expected value of a functional of the random processes (Xk)k≥0 and (Uk)k≥0 induced by the above
model among all (relaxed) strategies or among a restricted set of strategies. As for deterministic
control problems, the criteria can be of several types:
• Finite horizon (time) additive or multiplicative or mixed criteria.
• Inﬁnite horizon discounted (additive) criteria.
• Additive criteria with stopping time, which may be ﬁxed or to be optimized.
• Long run time average criteria.
3.2
Markov decision problems with additive ﬁnite horizon criteria
Let be given a Markov decision process as in Deﬁnition 3.1 or Deﬁnition 3.8, and consider or denote:
• for all k ∈N, the instantaneous/running reward/payoﬀat time k, which is a map rk : Ak →R;
• a ﬁnal reward, which is a map ϕ : E →R;
• for all strategies σ = (σk)k≥0 in Σ or ΣR (or Π and ΠR), the total additive payoﬀwith ﬁnite
horizon T ≥1:
J(T,σ) := JT (X; U) := E
" T−1
X
k=0
rk(Xk, Uk)
!
+ ϕ(XT )
#
,
(3.3)
where (X, U) := (Xk, Uk)k≥0 is the process induced by σ as in Deﬁnition 3.2 or Deﬁnition 3.3,
on a probability space (Ω, A, P).
• and for strategies associated to the MDP starting at time t, the additive payoﬀstarting at
time t:
J(T,σ)
t
(x) := JT
t,x(X; U) := E
" T−1
X
k=t
rk(Xk, Uk)
!
+ ϕ(XT ) | Xt = x
#
.
(3.4)
• for all k ≥0 and π ∈Πk (feedback policy at time k), the associated reward vector at time k
r(k,π) with r(k,π)
x
:= rk(x, π(x)), for x ∈E.
Deﬁnition 3.10. A Markov decision problem with complete observation, and the above data
consists in the following optimization problem:
max
σ
J(T,σ)
where the optimization holds over either all relaxed strategies σ ∈ΣR, or all pure strategies, or all
Markov strategies, or all feedback policies. The optimum of above criteria is called the value of the
problem. An optimal solution σ is called an optimal strategy, and the corresponding process Uk or
(Xk, Uk) an optimal control process. Moreover, maximization can be replaced by minimization.
47


## Page 56

Deﬁnition 3.11. For all x ∈E, and t ≤T, let vt(x) be the value of the Markov decision problem
with a criteria starting at time t:
max
σ
J(T,σ)
t
(x) .
The map v : {0, . . . , T} × E →R, (t, x 7→vt(x) is called the value function of the MDP.
Using Theorem 2.21 and Fact 3.7, we deduce the following result.
Lemma 3.12. When σ = π = (πk)k≥0 is a feedback policy, then vt := J(T,π)
t
satisﬁes the Kol-
mogorov equation:
vk = r(k,πk) + M(k,πk)vk+1, 0 ≤k ≤T −1 ,
with ﬁnal condition:
vT = ϕ .
In the controlled case, we obtain the nonlinear Bellman equation.
Theorem 3.13 (Dynamic programming equation for Markov decision problems with ﬁnite hori-
zon). Assume that the maps ϕ, rk, k ≥0 are bounded from above. Let vk be the value function of
the Markov decision problem:
vk(x) := max
σ
J(T,σ)
k
(x) ,
where the maximum is taken over all relaxed strategies starting at time k. Then, v satisﬁes the
following backward recurrence, called the Bellman dynamic programming equation:
vk(x) =
sup
u∈Ck(x)

rk(x, u) +
X
y∈E
M(k,u)
xy
vk+1(y)


∀x ∈E, 0 ≤k ≤T −1 .
(3.5)
with ﬁnal condition
vT = ϕ .
Moreover, the values v obtained by optimizing over the restricted sets of pure strategies, Markov
strategies, or feedback policies, coincide.
Assume in addition that the maximum of (3.5) is attained for an action u ∈Ck(x) and let us
denote by πk(x) this action, then the feedback policy π = (πk)0≤k≤T−1 is an optimal strategy of the
problem.
Note that we also have v = p(0)v0 for the value of the Markov decision problem with total
additive payoﬀ.
3.3
Properties of Bellman operators
We shall use similar operator notations as for deterministic control problems. For all k ∈N and
π ∈Πk, B(k,π) and B(k) denote the maps from RE to itself such that (assuming that the rk are
bounded from above)
B(k,π)(v) = r(k,π) + M(k,π)v
[B(k)(v)](x) =
sup
u∈Ck(x)

rk(x, u) +
X
y∈E
M(k,u)
xy
v(y)

.
(3.6)
48


## Page 57

The dynamic programming equation (3.5) can be rewritten as vk(x) = [B(k)(vk+1)](x) for all
x ∈E, or simply
vk = B(k)(vk+1).
(3.7)
Moreover, the supremum in (3.6) is ﬁnite as soon as E is ﬁnite, v ∈RE, and the functions rk
are bounded from above. Then, the operator B(k) is well deﬁned from RE to itself.
Remark 3.14. As for deterministic or uncontrolled problems, when the MDP is stationary, that is
Ck(x) and M(k,u)
x
do not depend on k, and the reward rk is independent of time k too, then B does
not depend on k, and one can consider the value function as a function of the remaining time until
the end:
v(t)(x) = max
σ
J(t,σ)
0
(x) .
Then, the backward Bellman equation for the value function is equivalent to the following forward
Bellman equation:
v(k+1)(x) = sup
u∈C(x)

r(x, u) +
X
y∈E
M(u)
xy v(k)(y)


∀x ∈E, 0 ≤k ≤T −1 ,
or equivalently to
v(k+1) = B(v(k)) ,
with initial condition v(0) = ϕ.
Deﬁnition 3.15. For all k ≤T −1, the map B(k) is called the Bellman operator at time k of the
Markov decision problem.
The maps B(k,π) are the Kolmogorov or Bellman operators at time k of the Markov decision
problem, when the policy is frozen.
Since
[B(k,π)(v)](x) = rk(x, π(x)) +
X
y∈E
M(k,π(x))
xy
v(y)
only depends on π(x), and not on all the other values of the map π, we get:
[B(k)(v)](x) = sup
π∈Πk
[B(k,π)(v)](x)
∀v ∈RE, ∀x ∈E.
and so
B(k)(v) = sup
π∈Πk
B(k,π)(v) ∀v ∈RE,
(3.8)
where the suppremum is taken for the partial order of RE.
Moreover, the existence of an optimum u in the dynamic programming equation (3.5) for all
x ∈E, is equivalent to the existence of π ∈Πk such that B(k)(vk+1) = B(k,π)(vk+1), that is to the
property that the supremum in (3.8) is a maximum when v = vk+1.
The operators B(k,π) : RE →RE are aﬃne operators that are the Kolmogorov operators asso-
ciated to the Markov chain of Fact 3.7. We already know that the operators B(k,π) are monotone
additively homogeneous (since a Markov matrix M has nonnegative entries and satisﬁes M1 = 1).
The Bellman operators as suprema of such operators satisfy the same property:
49


## Page 58

Lemma 3.16. The Bellman operators B(k) are monotone and additively homogeneous.
However, the Bellman operators B(k) are in general nonlinear both in usual algebra and tropical
algebra. They are however convex in the following sense, as suprema of aﬃne maps.
Deﬁnition 3.17. An operator B : RE →RE is convex if for all x ∈E, the function v ∈RE 7→
[B(v)](x) ∈R is convex, or equivalently, for all v, w ∈RE and t ∈[0, 1], B((1 −t)v + tw) ≤
(1 −t)B(v) + tB(w) for the partial order of RS.
Fact 3.18. The Bellman operators B(k) are convex.
3.4
Proof of Theorem 3.13
We shall show the results by using the previous notations and properties, although one may do
everything without using these properties explicitely.
Denote by (wk)0≤k≤T the sequence deﬁned (uniquely) by the ﬁnal condition wT = ϕ, and
the backward recurrence equations (3.5) or equivalently (3.7): wk = B(k)(wk+1). We denote also
w := p(0)w0. We need to show that wk = vk for all k ∈{0, . . . , T} and that w = v.
1. Proof of wk ≥vk and w ≥v (without any assumption).
Since for vk, we use strategies
starting at time k, the inequality wk ≥vk is of same type as w0 ≥v0. So we show w0 ≥v0 only.
Let σ ∈ΣR be ﬁxed, let (Xt, Ut)t≥0 be the process associated to the strategy σ, and let
Hk = (X0, U0, X1, U1, . . . , Xk), for all k ≥0, be the history process. For all 0 ≤k ≤T, and all
histories hk = (x0, u0, . . . , xk−1, uk−1, xk) ∈Hk, denote
z(σ)
k (hk) = E
" T−1
X
t=k
rt(Xt, Ut)
!
+ ϕ(XT ) | Hk = hk
#
.
Then, z(σ)
0 (x0) = J(T,σ)
0
(x0), and so J(T,σ) = E
h
z(σ)
0 (X0)
i
= p(0)z(σ)
0 .
The process Hk is a Markov chain taking its values in the variable state space Hk. Therefore,
z(σ)
k
satisﬁes the Kolmogorov equation for an additive functional (see Theorem 2.21)
z(σ)
n (hn) = E
h
rn(xn, Un) + z(σ)
n+1(hn, Un, Xn+1) | Hn = hn
i
(3.9)
if hn = (x0, u0, . . . , xn) ∈Hn, with the ﬁnal condition z(σ)
T (hT ) = ϕ(xT ).
wk satisﬁes (3.5), which can be rewritten as
wn(x) =
sup
u∈Cn(x)
(rn(x, u) + E [wn+1(Xn+1) | Xn = x, Un = u])
∀x ∈E .
(3.10)
Let us show that wk(xk) ≥z(σ)
k (hk) by backward induction on k, when hk = (x0, u0, . . . , xk) ∈Hk.
This is true for k = T since z(σ)
T (hT ) = ϕ(xT ) = wT (xT ). If the inequality is true for k + 1, then
from the above equations (3.9) and (3.10), we deduce
z(σ)
k (hk) ≤E [rk(xk, Uk) + wk+1(Xk+1) | Hk = hk] =
E [rk(xk, Uk) + E [wk+1(Xk+1) | Xk = xk, Uk] | Hk = hk] =
X
uk∈Ck(xk)
σk(hk)(uk) {rk(xk, uk) + E [wk+1(Xk+1) | Xk = xk, Uk = uk]} ,
50


## Page 59

where the last equality holds when σ(hk) is a probability with a countable support (in Ck(xk)).
Using (3.10), we deduce z(σ)
k (hk) ≤E [wk(xk) | Hk = hk] = wk(xk), which proves the induction.
In particular z(σ)
0 (x0) ≤w0(x0) for all x0 ∈E, and so J(T,σ) ≤p(0)w0. Since z(σ)
0 (x0) = J(T,σ)
0
(x0),
taking the maximum over all strategies, we deduce that v0(x0) ≤w0(x0). Since J(T,σ) = p(0)z(σ)
0
≤
p(0)w0, taking again the maximum over all strategies, we deduce v ≤w.
2. Proof of wk ≤vk and w ≤v when the supremum in (3.5) is attained.
Assume that the
maximum in
wk = sup
π∈Πk
B(k,π)(wk+1)
(3.11)
is attained for some policy π ∈Πk (for instance if the sets Ck(x) are ﬁnite). Denote π = (πk)k≥0.
Then,
wk = B(k,πk)(wk+1),
k = 0, . . . , T −1,
which means that (wk)n≥0 satisﬁes the same Kolmogorov equation as J(T,π)
k
, given in Lemma 3.12,
with same ﬁnal condition wT = ϕ = J(T,π)
T
. Hence, wk = J(T,π)
k
, for all k ≥0. So wk ≤vk, where
the value vk is obtained as the maximum over any set of strategies containing at least feedback
policies. Similarly, w = p(0)w0 = J(T,π) ≤v. Moreover, π is an optimal strategy which is a feedback
strategy.
3. Proof of wk ≤vk and w ≤v in general.
Assume now that the maximum in (3.11) is not
attained. We only assume that the maps rk are bounded from above, for all k ≤T −1. This
condition ensures in particular that the operators B(k) are well deﬁned as operators from RE to
itself. The supremum in (3.6) is ﬁnite, therefore for all ε > 0, k ≤T −1 and v ∈RE, there exists
π ∈Πk such that
[B(k,π)(v)](x) ≥[B(k)(v)](x) −ε
∀x ∈E ,
which can be rewritten as
B(k,π)(v) ≥B(k)(v) −ε1.
Let πk ∈Πk such that
B(k,πk)(wk+1) ≥B(k)(wk+1) −ε1.
We have
B(k,πk)(wk+1) ≥wk −ε1.
Denote zk = wk + (k −T)ε1. We have zT = wT = ϕ and
B(k,πk)(zk+1) = B(k,πk)(wk+1) + (k + 1 −T)ε1 ≥wk + (k −T)ε1 = zk
(3.12)
since B(k,πk) is additively homogeneous.
Then, the functions zk are sub-solutions of the Kolmogorov equation of Lemma 3.12. We shall
show the inequality zk ≤J(T,π)
k
by backward induction on k. Indeed the inequality is true for
k = T, since zT = ϕ = J(T,π)
T
. If it holds for k + 1, then
zk ≤B(k,πk)(zk+1) ≤B(k,πk)(J(T,π)
k+1 ) = J(T,π)
k
≤vk ,
51


## Page 60

where the ﬁrst inequality follows from (3.12), the second one from the induction assumption and
the monotonicity of B(k,πk), the third one from the Kolmogorov equation of Lemma 3.12 which is
satisﬁed by J(T,π)
k
, and the last one by deﬁnition of vk. This shows z0 ≤J(T,π)
0
≤v0, hence we get
p(0)z0 ≤p(0)J(T,π)
0
= E

J(T,π)
≤v.
Therefore,
wk = zk + (T −k)ε1 ≤vk + (T −k)ε1
for all k ∈{0, . . . , T}. Since we have shown this inequality for all ε > 0, we deduce that wk ≤vk
for all k ∈{0, . . . , T}. Similarly w = p(0)w0 = p(0)z0 + Tε ≤v + Tε, and since this holds for all
ε > 0, we get w ≤v.
Remark 3.19. In the present case of an additive functional, another way to prove that the values
v obtained by optimizing over either all relaxed strategies or all Markov strategies coincide is
to show that for all π ∈ΣR, there exists π′ ∈ΠR such that E

J(π)
= E
h
J(π′)i
. Indeed, let
(π′
k(x))(B) = P(Uk ∈B, Xk = x)/P(Xk = x), where P is the probability on the process (Xk, Uk)
induced by π as in Deﬁnition 3.3. Then, if (X′
k, U′
k) is the process induced by π′, we get that for
all k ≥0, the laws of the random variables (Xk, Uk) and (X′
k, U′
k) coincide (not the ones of the
processes). Therefore E

J(π)
= E
h
J(π′)i
, since they are both sums of expectations of functions of
the random variables (Xk, Uk) only and not of all the process (Xk, Uk)k≥0.
3.5
Problems with multiplicative or discounted ﬁnite horizon pay-
oﬀ
Let be given a Markov decision process as in Deﬁnition 3.1 or Deﬁnition 3.8, and consider or denote:
• for all k ∈N, the instantaneous/running reward/payoﬀat time k, which is a map rk : Ak →R;
• for all k ∈N, a variable discount factor at time k, which is a map αk : Ak →R+;
• a ﬁnal reward, which is a map ϕ : E →R;
• for all strategies σ = (σk)k≥0 in Σ or ΣR, the mixed payoﬀwith ﬁnite horizon T ≥1:
J(T,σ) := JT (X; U) :=E
" T−1
X
ℓ=0
 ℓ−1
Y
m=0
αm(Xm, Um)
!
rℓ(Xℓ, Uℓ)
!
+
 T−1
Y
m=0
αm(Xm, Um)
!
ϕ(XT )
#
,
(3.13)
where (X, U) := (Xk, Uk)k≥0 is the process induced by σ as in Deﬁnition 3.2 or Deﬁnition 3.3.
• and for strategies σ = (σk)k≥t associated to the MDP starting at time t, the mixed payoﬀ
starting at time t:
J(T,σ)
t
(x) := JT
t,x(X; U) :=E
" T−1
X
ℓ=t
 ℓ−1
Y
m=t
αm(Xm, Um)
!
rℓ(Xℓ, Uℓ)
!
+
 T−1
Y
m=t
αm(Xm, Um)
!
ϕ(XT ) | Xt = x
#
.
(3.14)
52


## Page 61

Theorem 3.20 (Dynamic programming equation for Markov decision problems with mixed func-
tional and ﬁnite horizon). Assume that the maps ϕ, rk, αk, k ≥0 are bounded from above. Let vk
be the value function of the Markov decision problem:
vk(x) := max
σ
J(T,σ)
k
(x) ,
where the maximum is taken over all relaxed strategies starting at time k. Then, v satisﬁes the
following backward recurrence, called the Bellman dynamic programming equation:
vk(x) =
sup
u∈Ck(x)

rk(x, u) + αk(x, u)
X
y∈E
M(k,u)
xy
vk+1(y)


∀x ∈E, 0 ≤k ≤T −1 .
(3.15)
with ﬁnal condition
vT = φ .
Moreover, the values v obtained by optimizing over the restricted sets of pure strategies, Markov
strategies, or feedback policies, coincide.
Assume in addition that the maximum of (3.15) is attained for an action u ∈Ck(x) and let us
denote by πk(x) this action, then the feedback policy π = (πk)0≤k≤T−1 is an optimal strategy of the
problem.
Remark 3.21. As above, when the MDP is stationary, that is Ck(x) and M(k,u)
x
do not depend on
k, and the reward rk and discount factor αk are independent of time k too, then B does not depend
on k, and one can consider the value function as a function of the remaining time until the end:
v(t)(x) = max
σ
J(t,σ)
0
(x) .
Then, the backward Bellman equation for the value function is equivalent to the following forward
Bellman equation:
v(k+1)(x) = sup
u∈C(x)

r(x, u) + α(x, u)
X
y∈E
M(u)
xy v(k)(y)


∀x ∈E, 0 ≤k ≤T −1 ,
or equivalently to
v(k+1) = B(v(k)) ,
with initial condition v(0) = ϕ.
For the proof of Theorem 3.20, we shall use the Kolmogorov operators B(k,π) from RE to itself
deﬁned, for k ∈N and v ∈RE, by:
B(k,π)(v) = r(π)
k
+ A(k,π)v
where A(k,π) is the matrix with nonnegative entries such that A(k,π)
xy
= αk(x, π(x))M(k,π)
xy
. We also
use the Bellman operators B(k) deﬁned by (3.8). We have:
[B(k)(v)](x) =
sup
u∈Ck(x)

rk(x, u) + αk(x, u)
X
y∈E
M(k,u)
xy
v(y)

.
(3.16)
53


## Page 62

Then, the dynamic programming equation (3.15) can be rewritten as in (3.7). As in the additive
case, the supremum in (3.16) is ﬁnite as soon as E is ﬁnite, v ∈RE, and the functions rk(x, ·) and
αk(x, ·) are bounded from above, which implies that B(k) is well deﬁned and is a map from RE
to itself, and that all the value functions vk take ﬁnite real values. Moreover, the existence of an
optimal control u in (3.15) for all x ∈E is equivalent to the existence of a policy π ∈Πk such
that B(k)(vk+1) = B(k,π)(vk+1). The operators B(k,π) : RE →RE are aﬃne, monotone, and thus
the operators B(k) are convex and monotone. However, they are no more additively homogeneous.
Nevertheless, when αk(x, u) ≤β, for all x ∈E and u ∈Ck(x), the operators B(k,π) and B are
β-subhomogeneous, where this property is deﬁned as follows.
Deﬁnition 3.22. Let β > 0. We say that an operator B : RE →RE is additively β-subhomogeneous
if it satisﬁes, for all v ∈RE and λ ∈R+,
B(v + λ1) ≤B(v) + βλ1 .
When β = 1, we say that B is additively subhomogeneous
Proof of Theorem 3.20. We follow the same arguments as in the proof of Theorem 3.13, where
Equation (3.15) is substituted to (3.5), and Kolmogorov equation of Theorem 2.26 is used instead
of the one of Theorem 2.21. Indeed, Points 1 and 2 of the proof of Theorem 3.13 only use the
monotonicity of the operators B(k,π) and B(k), Property (3.8) deﬁning B(k) as a supremum of the
B(k,π), and the Kolmogorov equation satisﬁed by the Markov chain Hk associated to any strategy,
or the Markov chain Xk associated to any feedback policy. They thus can be followed similarly for
the operators B(k,π) and B(k) of this section.
For Point 3, we use the property that the functions αk are bounded from above. Let β be
an upper bound. Then, from the above remarks, the operators B(k,π) and B(k) are additively β-
subhomogeneous. Choose πk as in Point 3 of the proof of Theorem 3.13, and zk = wk −εγk, where
the sequence γk is obtained by the backward induction γT = 0, and γk = 1 + βγk+1 (so γk = T −k
if β = 1, and γk = (βT−k −1)/(β −1) otherwise). We obtain in the same way as in the proof of
Theorem 3.13 that B(k,πk)(zk+1) ≥zk, and thus zk ≤v(π)
k , and p(0)z0 ≤v. Therefore
wk = zk + γkε ≤v(π)
k
+ γkε ≤vk + γkε
for all k ∈{0, . . . , T}. Since this holds for all ε > 0, we deduce that wk ≤vk for all k ∈{0, . . . , T}.
The rest of the proof remains.
Remark 3.23. Another way to prove Theorem 3.20 is to increase the state space by taking E′ :=
E × Z, with Z = R+, and considering the state sequence X′
k = (Xk, Zk), where Zk ∈Z satisﬁes
Zk+1 = αk(Xk, Uk)Zk starting at Z0 = 1. This corresponds to a MDP with transition probabilities
given by M′(k,u)
x′y′
= M(k,u)
xy
if x′ = (x, z) and y′ = (y, αk(x, u)z) and M(k,u)
x′y′
= 0 otherwise, and the
initial law p′(0) = p(0) ⊗pz, where pz is the Dirac probability at Point 1 on Z. The only diﬃculty is
that now the new state space is inﬁnite not countable. One can reduce however the problem to a
ﬁnite state space E′
k depending on time if we assume that the action spaces Ck(x) are ﬁnite. Consider
the reward functions deﬁned for x′ = (x, z) ∈E × Z, by r′
k(x′, u) = zrk(x, u), ϕ′(x′) = zϕ(x), we
get that JT
t,x(X; U) is equal to the additive functional JT
t,(x,1)(X′; U) deﬁned with the new MDP
and rewards. We can then apply Theorem 3.13. We deduce that v = (p(0) ⊗pz)(v′
0) where v′
T = ϕ′
54


## Page 63

and v′
k satisﬁes the dynamic programming equation
v′
k(x′) =
sup
u∈Ck(x)

r′
k(x′, u) +
X
y′∈E′
M(k,u)
x′y′ v′
k+1(y′)


∀x′ ∈E′ .
Replacing r′
k and ϕ′ with their values, we obtain that, for all k ≥0, v′
k(x′) = zvk(x) for some
function vk, and that vk satisﬁes (3.15). Similarly v = p(0)v0.
The previous remark shows that one can always reduce a MDP with mixed functional to a
MDP with additive functional by increasing the state space which may become inﬁnite. One can
also do the reverse operation, when the state has the form Xk = (X′
k, Zk), in which Zk is positively
homogeneous, that is satisﬁes that Zk is transformed into λZk when Z0 is transformed into λZ0,
if X′
k+1 does not depend on Zk. Indeed, in that case the state can be reduced to X′
k, then the
additive functional becomes a mixed functional.
When the discount factors αk are less than 1, we call the mixed functional a discounted func-
tional. Another reduction can be obtained in that case, by adding a cemetery point, as in Propo-
sition 2.27. This leads to the following result.
Proposition 3.24. The value function of a ﬁnite horizon discounted Markov Decision problem is
equal to the restriction to E of the value function of a ﬁnite horizon MDP with additive criteria on
the state space E ∪{c}, where c̸ ∈E is a cemetery point.
Proof. Consider a MDP with ﬁnite horizon mixed functional as above. Let c̸ ∈E, and consider
E′ = E ∪{c}. We construct a MDP with additive functional on E′ as follows. We keep the same
action spaces Ck(x) for x ∈E and we take for Ck(c) any singleton subset of C, The initial law p′(0)
is p′(0)
x
= p(0)
x
for x ∈E and p′(0)
c
= 0, and the transition probabilities are
M′(k,u)
xy
= αk(x, u)M(k,u)
xy
,
when x, y ∈E
M′(k,u)
xc
= 1 −αk(x, u),
∀x ∈E
M′(k,u)
cy
= 0,
∀y ∈E
M′(k,u)
cc
= 1 .
We extend rk and ϕ to E′ in r′
k and ϕ′ respectively by mapping (c, u) or c to 0. Let v′ be the value
function of this new MDP on E′ with additive functional (see (3.4)). By Theorem 3.13, we have
v′ = p′(0)v′
0 where v′
k ∈RE′ is solution of the backward recurrence dynamic programming equation
v′
k(x) =
sup
u∈Ck(x)

r′
k(x, u) +
X
y∈E′
M′(k,u)
xy
v′
k+1(y)


∀x ∈E′, 0 ≤k ≤T −1 ,
with ﬁnal condition v′
T = ϕ′. Since ϕ(c) = rk(c, u) = 0 and M′(k,u)
cc
= 1, for all u ∈Ck(c), we get
that v′
k(c) = v′
k+1(c) for all k ≥0, hence v′
k(c) = 0. Therefore, if vk is the restriction of v′
k to E, we
obtain that v′ = p(0)v0 and that vk satisﬁes the dynamic programming equation (3.15). Moreover,
v′ = v so the values of the two problems coincide.
55


## Page 64

3.6
Problems with exit time in ﬁnite horizon
Let be given a Markov decision process as in Deﬁnition 3.1 or Deﬁnition 3.8, and let B be a strict
subset of E. Then, any strategy σ = (σn)n≥0 in Σ or ΣR induces the process (Xn, Un)n≥0 and the
history process (Hn)n≥0. The later beeing a Markov chain, we can construct the ﬁltration (Fn)n≥0
generated by (Hn)n≥0, which is in that case Fn = σa(Hn) = σa(X0, U0, . . . , Un−1, Xn). Then, the
exit time of the sequence (Xn)n≥k from the set B:
τ k
B := inf{n ≥k | Xn̸ ∈B}
is a stopping time with respect to the ﬁltration (Fn)n≥k. When σ is a feedback policy, then (Xn)n≥0
is a Markov chain and τ k
B is also a stopping time with respect to the Markov chain (Xn)n≥k.
Consider or denote:
• for all k ∈N, the instantaneous/running reward/payoﬀat time k, which is a map rk : Ak →R;
• a ﬁnal reward, which is a map ϕ : E →R;
• for all k ∈N, an exit reward, which is a map ψk : E \ B →R, such that ψT is the restriction
of ϕ on E \ B;
• for all strategies σ = (σk)k≥0 in Σ or ΣR, the payoﬀwith exit stopping time and ﬁnite horizon
T ≥1:
J(T,B,σ) :=JT,B(X; U) := E




T∧τ 0
B−1
X
ℓ=0
rℓ(Xℓ, Uℓ)

+ ψT∧τ 0
B(XT∧τ 0
B)

,
(3.17)
where (X, U) := (Xk, Uk)k≥0 is the process induced by σ as in Deﬁnition 3.2 or Deﬁnition 3.3,
and τ 0
B is the exit time of the process (Xn)n≥0 from B.
• and for strategies associated to the MDP starting at time t, the payoﬀstarting at time t with
exit stopping time:
J(T,B,σ)
t
(x) := JT,B
t,x (X; U) := E




T∧τ t
B−1
X
ℓ=t
rℓ(Xℓ, Uℓ)

+ ψT∧τ t
B(XT∧τ t
B) | Xt = x

, (3.18)
where we extend ψT to B by taking ψT = ϕ.
Theorem 3.25 (Dynamic programming equation for Markov decision problems with exit time in
ﬁnite horizon). Assume that the maps ϕ, rk, k ≥0 are bounded from above. Let vk be the value
function of the Markov decision problem:
vk(x) := max
σ
J(T,B,σ)
k
(x) ,
where the maximum is taken over all relaxed strategies starting at time k. Then, v satisﬁes the
following backward recurrence, called the Bellman dynamic programming equation:
vk(x) =
sup
u∈Ck(x)

rk(x, u) +
X
y∈E
M(k,u)
xy
vk+1(y)


∀x ∈B, 0 ≤k ≤T −1 .
(3.19a)
56


## Page 65

with boundary condition
vk(x) = ψk(x),
∀x̸ ∈B, 0 ≤k ≤T ,
(3.19b)
and ﬁnal condition
vT (x) = ϕ(x) = ψT (x),
∀x ∈B .
(3.19c)
Moreover, the values v obtained by optimizing over the restricted sets of pure strategies, Markov
strategies, or feedback policies, coincide.
Assume in addition that the maximum of (3.19) is attained for an action u ∈Ck(x), for x ∈B,
and let us denote by πk(x) this action when x ∈B, and choose any action πk(x) for x̸ ∈B, then
the feedback policy π = (πk)0≤k≤T−1 is an optimal strategy of the problem.
Theorem 3.25 can be deduced easily from Theorem 3.20 using the following property which is
the same as Fact 2.37.
Fact 3.26. The functional J(T,B,σ)
t
of (3.18) can rewritten as the mixed functional:
J(T,B,σ)
t
(x) := JT,B
t,x (X; U) :=E
" T−1
X
ℓ=t
 ℓ−1
Y
m=t
αm(Xm, Um)
!
r′
ℓ(Xℓ, Uℓ)
!
+
 T−1
Y
m=t
αm(Xm, Um)
!
ϕ(XT ) | Xt = x
#
.
for the same Markov Decision process, with the same ﬁnal reward ϕ, and the instantaneous rewards
r′
k and variable discount factors αk given by:
r′
k(x, u) = rk(x, u),
for x ∈B, u ∈Ck(x)
r′
k(x, u) = ψk(x),
for x̸ ∈B, u ∈Ck(x)
αk(x, u) = 1,
for x ∈B, u ∈Ck(x)
αk(x, u) = 0,
for x̸ ∈B, u ∈Ck(x) .
The previous property shows that a Markov decision process with exit time in a ﬁnite horizon
functional can be seen as a problem with mixed functional with discount factors ≤1, for the
same MDP. By Proposition 3.24, such a problem can then be reduced to a problem with additive
functional by adding a cemetery point to the state space. Another way to prove Theorem 3.25 or
to reduce the exit time functional to an additive functional is to consider the process Xn∧τ k
B which
corresponds to a slightly diﬀerent MDP, in which the transition probabilities in E \ B are changed
(see the proof of Theorem 2.36). The advantage of Fact 3.26 is that we do not need to change the
MDP.
Example 3.27. Conversely, consider a Markov decision process with an additive criteria as (3.3)
including a cemetery point c ∈E, as in the reductions of previous section.
This means that
M(k,u)
cc
= 1, and rk(c, u) = 0 for all u ∈Ck(c). Then, one can rewrite the additive functional by
using the exit stopping time τB from the set B = E \ {c} of the process (Xk)k≥0 induced by any
strategy σ. Indeed, in that case rk(Xk, Uk) = 0 and Xk = Xk+1 = XτB for all k ≥τB, and so
J(T,σ) := JT (X; U) := E
" T−1
X
k=0
rk(Xk, Uk)
!
+ ϕ(XT )
#
= E
" T∧τB−1
X
k=0
rk(Xk, Uk)
!
+ ϕ(XT∧τB)
#
.
57


## Page 66

Again the advantage of this technique is that we do not need to change the MDP (the transition
probabilities).
3.7
The example of optimal stopping time problems with ﬁnite
horizon
Consider
• a (ﬁxed) Markov chain (Xn)n≥0 over a probability space (Ω, A, P) taking its values in a ﬁnite
state space E, with transition matrices M(n) at time n ∈N, and initial probability law p(0).
• instantaneous/running rewards/payoﬀs rk ∈RE (at any time k ≤T −1);
• ﬁnal rewards ϕk ∈RE (at any time k ≤T);
• for all stopping times τ with respect to the Markov chain (Xn)n≥0, the ﬁnite horizon payoﬀ
with stopping time τ:
J(T,τ) :=E
" τ∧T−1
X
ℓ=0
rℓ(Xℓ)
!
+ ϕτ∧T (Xτ∧T )
#
;
(3.20)
• and for all t ≤T, the ﬁnite horizon payoﬀwith stopping time τ ≥t, starting in x at time t:
J(T,τ)
t
(x) :=E
" τ∧T−1
X
ℓ=t
rℓ(Xℓ)
!
+ ϕτ∧T (Xτ∧T ) | Xt = x
#
.
(3.21)
Deﬁnition 3.28. An Optimal stopping time problem with complete observation and ﬁnite horizon
criteria consists in the following optimization problem:
max
τ
J(T,τ)
where the optimization holds over all stopping times τ with respect to the Markov chain (Xn)n≥0.
The optimum of above criteria is called the value of the problem.
An optimal solution τ is called an optimal stopping time.
Deﬁnition 3.29. For all x ∈E, and t ≤T, let vt(x) be the value of the optimal stopping time
problem with initial state x at time t:
max
τ
J(T,τ)
t
(x) .
The map v : {0, . . . , T} × E →R, (t, x) 7→vt(x) is called the value function of the stopping time
problem.
Theorem 3.30 (Dynamic programming equation for optimal stopping time problems with ﬁnite
horizon criteria). Assume that the maps ϕk, rk, k ≥0, are bounded from above (or E ﬁnite). Let
vk be the value function of the optimal stopping time problem with ﬁnite horizon:
vk(x) := max
τ
J(T,τ)
k
(x) ,
58


## Page 67

where the maximum is taken over all stopping times τ with respect to the Markov chain (Xn)n≥k.
Then, v satisﬁes the following backward recurrence, called the Bellman dynamic programming equa-
tion or variational inequality:
vk(x) = max

rk(x) +
X
y∈E
M(k)
xy vk+1(y), ϕk(x)

∀x ∈E, 0 ≤k ≤T −1 .
(3.22)
with ﬁnal condition
vT = ϕT .
For all 0 ≤k ≤T, let Bk be the set of states in which the maximum in (3.22) is attained in the
ﬁrst term, that is
Bk := {x ∈E | rk(x) +
X
y∈E
M(k)
xy vk+1(y) ≥ϕk(x)} ,
au deﬁne
τ = inf{k ≥0 | Xk̸ ∈Bk or k = N} .
Then τ is an optimal stopping time.
Proof. For the proof, we reduce this problem to a Markov decision problem with ﬁnite horizon
criteria.
Consider the MDP in which
• the state space is E′ = E ∪{c} where c̸ ∈E;
• the control space C = {0, 1} (0 for stop, and 1 for not stop);
• the control space C(x) is such that C(x) = C if x ∈E and C(x) = {0} if x = c.
• the states of the MDP, Yn, depend on the states of the Markov chain Xn and on the actions
as follows:
Yn+1 = g(Xn+1, Un)
where g(x, u) = x if u = 1 and g(x, u) = c otherwise.
• Then, for all xi ∈E′, ui ∈Ci(xi), i ≥0, we have
P(Yk+1 = xk+1 | Yk = xk, Uk = uk, Yk−1 = xk−1, . . . , Y0 = x0, U0 = u0)
= 1 if c = xk+1 and uk = 0
= 0 if xk+1 ∈E and uk = 0
= M(k)
xk,xk+1 if xk, xk+1 ∈E and uk = 1
• This implies that
P(Yk+1 = xk+1 | Yk = xk, Uk = uk, Yk−1 = xk−1, . . . , Y0 = x0, U0 = u0)
= P(Yk+1 = xk+1 | Yk = xk, Uk = uk) .
which is the Markov property.
59


## Page 68

• The transition probabilities of the MDP are: M(k,1)
xy
= M(k)
xy for all x, y ∈E, M(k,1)
xy
= 0 for
x ∈E and y = c, M(k,0)
xy
= 1 for x ∈E′ and y = c, and M(k,0)
xy
= 0 for x ∈E′ and y ∈E. Note
that M(k,1)
cy
, with y ∈E′, is useless.
• Take then the rewards: r′
k(x, 1) = rk(x), r′
k(x, 0) = ϕk(x) for x ∈E and r′
k(c, 0) = 0, and ﬁnal
reward ϕ(x) = ϕT (x) for x ∈E and ϕ(c) = 0.
Then, the value of the ﬁnite horizon Markov Decision problem coincides with the value of the
stopping time problem with ﬁnite horizon:
Given a pure strategy, the associated process Ut satisﬁes Ut ∈Ft = σa(X0, . . . , Xt), and so
τ = inf{t ≥0 | Ut = 0} is a stopping time. Conversely, given a stopping time τ, consider the process
such that Un = 1 for all n < τ and Un = 0 for n ≥τ, we get that {Ut = 1} ∈Ft = σa(X0, . . . , Xt),
so that Ut can be written as a measurable function σt of X0, . . . , Xt. Then, the process (Ut)t≥0 is
associated to the pure strategy (σt)t≥0.
The Bellman equation of the Markov decision problem is then:
vk(x) = max

rk(x) +
X
y∈E
M(k)
xy vk+1(y), ϕk(x) + vk+1(c)

∀x ∈E ,
vk(c) = vk+1(c) ,
with the ﬁnal condition vT (x) = ϕT (x) for x ∈E and vT (c) = 0.
Here the action u = 1 corresponds to the left term in the above maximum, and u = 0 corresponds
to the right term.
Therefore if πk : E →{0, 1} is an optimal policy given by the Bellman equation, we recover
again the optimal stopping time by taking:
τ = inf{t ≥0 | πt(Xt) = 0}
or by taking τ as in the theorem.
Remark 3.31. As seen in the above result, the variational inequality (3.22) allows one to construct
the set ∪k≥0{k}×Bk, for which the optimal stopping time is the exit time of the process (k, Xk)k≥0.
The complementary of this set plays the same role as a free boundary in the continuous time
and state setting.
Contrarilly to the case of control problems with an exit time considered in
Theorem 3.25, the above “boundary” is not known in advance, but is computed as the optimal
boundary for a certain criterion.
3.8
Examples and Exercices
Example 3.32 (A random ressource allocation problem). Let us consider the ressource allocation
problem described in Example 1.7 and Example 1.15, where we assume now that the reward ob-
tained when one invests x units in the ith ressource is random, and can be written as Ri(x, Zi),
where the Ri are deteministic maps and the Zi are independent random variables with values in
some set Z. Assume that the investor is choosing the numbers of units ui he is investing in each
ressource i in advance without knowing the values of the variables Zi.
What is the maximal expected total reward of the investor ?
60


## Page 69

Assume now that the investor is choosing the amounts to be invested in the ressources sequen-
tially, that is using some given order σ(i), i = 1, . . . , N, where σ is a permutation of {1, . . . , N},
and that when he decides to invest in ressource i, he is able to obtain the information on its reward,
that is on Zi. Assume also that the set Z is ﬁnite. The investor wants to maximize his expected
total reward. Write this problem as a Markov decision problem with state variable (x, z) with
x ∈{0, . . . , R} and z ∈Z.
Show that this problem can be solved via the recursive equation with ﬁnal value wN+1 = 0.
wn(x) = E

max
u∈N, 0≤u≤x[rσ(n)(u, Zσ(n)) + wn+1(x −u)]

, n = 1, . . . , N,
x ∈{0, . . . , R} ,
and that w1(R) gives the expected total reward of the investor. Show that if the maps ri are
concave with respect to the ﬁrst variable, then the maps wn are also concave (one can ﬁrst consider
the relaxed problem where x and the ui can take real values).
Show that the solution depends on the permutation σ.
61


## Page 70

3.9
Problem: Airline Revenue Management
Consider an airline revenue manager who decide at each time of arrival of a demand of seats on a
given ﬂight, if he accept or reject this demand.
We assume that the ﬂight contains n > 1 classes of seats (a class may contain an information
of level of the seat, of position in the plane, and of date of booking as well), numbered from 1 to
n. The price of a seat of class k ∈{1, . . . , n} will be denoted by pk, and we have p1 < · · · < pn.
We assume also that demands of seats of class k arrive before demands of seats of class k + 1, this
means that demands arrive in nonoverlapping intervals in the order of increasing prices (this is
called the early bird hypotheses). If Dk denotes the total amount of demands of seats of class k,
we also assume that the Dk are independent random variables.
We consider a Markov decision problem with ﬁnite horizon (n stages), starting at stage 1,
modelizing the sale of the seats of one ﬂight of a plane only. At each stage k = 1, . . . , n, all the
Dk demands of seats of class k arrive, and the manager decides to accept only a certain number
of them Uk ≤Dk. We add a ﬁnal stage n + 1, at which no demand of seats is done, so Dn+1 = 0.
Moreover, for each k = 1, . . . , n + 1, we denote by Xk the remaining capacity of the plane at stage
k, that is the number of available seats. Thus, X1 is the total number of seats of the plane, and
Xn+1 is the number of unsold seats at the end of the sale.
The Markov decision problem will involve a Markov decision process such that at each stage
k = 1, . . . , n + 1,
(Xk, Dk) : is the state of the MDP at stage k. Since the plane has a ﬁnite number of seats M, one
can consider that the set of states E is of the form E = [M] × N where [M] := {0, . . . , M},
or even E = [M] × [M].
Uk : is the action of the MDP at stage k. Again, since Uk ≤Dk, one can consider that the set
of actions C is [M], and that at stage k, Uk satisﬁes the constraint 0 ≤Uk ≤min(Xk, Dk),
so that Uk ∈C(Xk, Dk), with C(x, d) = [min(x, d)], for (x, d) ∈E.
Moreover, the dynamics of the MDP is such that:
Xk+1 = Xk −Uk,
k = 1, . . . , n ,
Dk are independent random variables with given laws qk(d) = P (Dk = d) , d ∈N .
The payoﬀ(criteria) of the MDP is the expected amount of money obtained after the end of the
sale, that the manager want to maximize. So the instantaneous reward at stage k, state (x, d) and
action u is given by
r(k; x, d; u) = pku ,
and the ﬁnal reward at state (x, d) is
φ(x, d) = 0 .
Q 9.1. We denote by v(k; x, d) the value function of the MDP, when the starting stage is k =
1, . . . , n + 1 with starting state (x, d) ∈E:
v(k; x, d) = sup E
" n
X
ℓ=k
r(ℓ; Xℓ, Dℓ; Uℓ) + φ(Xn+1, Dn+1) | Xk = x, Dk = d
#
,
where the supremum is taken over all (feedback) strategies (πk)k≥0 deﬁning the admissible process
(Uk)k≥1: Uk = πk(Xk, Dk). Write the dynamic programming equation satisﬁed by v.
62


## Page 71

Q 9.2. Denote wk(x) = E [v(k; x, Dk)]. Write a recurrence equation satisﬁed by wk.
Q 9.3. Show by induction on k, that wk : [M] →R is concave, and that for each d ∈N, x ∈[M] 7→
v(k; x, d) ∈R is concave.
Q 9.4. For k = 2, . . . , n + 1, choose
yk ∈Argmax
y∈[M]
{−pk−1y + wk(y)} .
Show that
πk(x, d) = max(min(x −yk+1, d), 0) = min(max(x −yk+1, 0), d)
is an optimal policy at time k for our problem.
Q 9.5. Explain the meaning of yk as a protection level for classes of levels ≥k.
Q 9.6. For all k = 2, . . . , n + 1, write yk as a function of the map ∆wk : [M] →R ∪{+∞}, where
∆wk(x) = wk(x) −wk(x −1) .
Q 9.7. To realize the previous policy, what should be the policy of acceptation of a single demand
of a seat of class k?
Q 9.8. Compute yn as a function of pn−1, pn and the law qn of Dn.
Q 9.9. Show that ∆wk+1(y) ≤∆wk(y) for all y ∈N and k ∈{1, . . . , n}.
Q 9.10. Show that y1 ≥· · · ≥yn.
Some references for this problem:
[RM1] K. Littlewood. Forecasting and control of passenger bookings. In Proc. 12th AGIFORS
Symposium. 1972. reprinted in Journal of Revenue and Pricing Management, Vol. 4 (2005).
[RM2] P.P. Belobaba. Air Travel Demand and Airline Seat Inventory Management. PhD thesis,
Flight Transportation Laboratory. Cambridge, MIT, 1987.
[RM3] S.L. Brumelle and J.I. McGill. Airline seat allocation with multiple nested fare classes.
Operations Research, (1):127–137, 1993.
[RM4] Kalyan T. Talluri and Garrett J. van Ryzin. The theory and practice of revenue management.
International Series in Operations Research & Management Science, 68. Kluwer Academic
Publishers, Boston, MA, 2004.
63


## Page 72

64


## Page 73

Chapter 4
Markov decision problems with
inﬁnite horizon
4.1
Discounted inﬁnite horizon problems
Assume given a stationary Markov decision process, that is
• a ﬁnite or discrete state space E;
• an action space C
• for all x ∈E, the subset C(x) ⊂C of all possible actions at any time k, when the state is equal
to x;
• the set A := {(x, u) | x ∈E, u ∈C(x)} of all possibles couples (state, action) at any time k;
• an initial probability p(0) ∈∆E on E, or an initial state x0 ∈E, which is equivalent to the
case where p(0) is the Dirac measure at x0;
with either
• for all x ∈E and u ∈C(x), a probability row vector M(u)
x
over E, the entries of which will be
denoted

M(u)
xy

y∈E, that are the transition probabilities;
or
• a probability space (Ω, A, P), a random variable X0 with values in E and law p(0), and a
sequence of independent and identically distributed random variables (Wn)n≥0 with values in
some discrete space W, independent from X0;
• with the dynamics at any time k, which is a map f : A × W →E.
Consider also the following (stationary) parameters:
• the instantaneous/running reward/payoﬀ(at any time k), which is a map r : A →R, where,
for all x ∈E and u ∈C(x), r(x, u) denotes the reward of the action u ∈C in state x ∈E;
• a (ﬁxed) discount factor α ∈[0, 1).
65


## Page 74

• for all strategies σ = (σk)k≥0 in Σ or ΣR, the discounted total additive payoﬀwith inﬁnite
horizon:
J(σ)
α
:= Jα(X; U) := E
" ∞
X
k=0
αkr(Xk, Uk)
#
,
(4.1)
where (X, U) := (Xk, Uk)k≥0 is the process induced by σ as in Deﬁnition 3.2 or Deﬁnition 3.3.
• and the discounted total additive payoﬀwith inﬁnite horizon starting at x at time 0:
J(σ)
α (x) := Jα,x(X; U) := E
" ∞
X
k=0
αkr(Xk, Uk) | X0 = x
#
;
(4.2)
Given the above parameters (in particular a stationary MDP, a stationary reward and a discount
factor), and a stationary feedback policy π ∈ΠS (the set of stationary feedback policies), we
associate the (stationary) Markov transition matrix: M(π) given by
M(π)
xy := M(π(x))
xy
, ∀x, y ∈E .
We also associate the (stationary) reward vector r(π) ∈RE with
r(π)
x
:= r(x, π(x)),
for x ∈E .
Fact 4.1. The associated stochastic process (Xk, Uk)k≥0 (that is satisfying Uk = π(Xk)) is such
that (Xk)k≥0 is a stationary Markov chain with initial law p(0) and transition probability matrix
M(π). Moreover, (Xk, Uk)k≥0 is also a Markov chain taking its values in E × C.
Using Kolmogorov equation for dicounted criteria (Theorem 2.28) and Fact 4.1, we deduce the
following result.
Lemma 4.2. When σ = π is a stationary feedback policy, then the value function v := J(π)
α
satisﬁes
the Kolmogorov equation:
v = r(π) + αM(π)v .
Deﬁnition 4.3. A Markov decision problem with complete observation and inﬁnite horizon dis-
counted criteria consists in the following optimization problem:
max
σ
J(σ)
α
where the optimization holds over either all relaxed strategies σ ∈ΣR, or all pure strategies, or all
Markov strategies, or all feedback policies, or all stationary feedback policies.
The optimum of above criteria is called the value of the problem.
An optimal solution σ is called an optimal strategy, and the corresponding process Uk or (Xk, Uk)
an optimal control process.
Moreover, maximization can be replaced by minimization.
66


## Page 75

4.1.1
The stationary dynamic programming equation
Deﬁnition 4.4. For all x ∈E, let vα(x) or simply v(x) be the value of the Markov decision problem
with an initial state x:
max
σ
J(σ)
α (x) .
The map vα : E →R, x 7→vα(x) is called the value function of the MDP.
Theorem 4.5 (Dynamic programming equation for Markov decision problems with discounted
inﬁnite horizon criteria). Assume that the map r is bounded from above. Let v be the value function
of the Markov decision problem:
v(x) := max
σ
J(σ)
α (x) ,
where the maximum is taken over all relaxed strategies (starting at time 0). Then, v is the unique
solution of the following ﬁxed point equation, called the stationary Bellman dynamic programming
equation:
v(x) = sup
u∈C(x)

r(x, u) + α
X
y∈E
M(u)
xy v(y)


∀x ∈E .
(4.3)
Moreover, the values v obtained by optimizing over the restricted sets of pure strategies, Markov
strategies, feedback policies, or stationary feedback policies coincide.
Assume in addition that the maximum of (4.3) is attained for an action u ∈C(x) and let us
denote by π(x) this action, then the stationary feedback policy π (that is (πk)k≥0 with πk = π) is
an optimal strategy of the problem.
We also have w = p(0)v for the value w of the Markov decision problem with inﬁnite horizon
discounted criteria.
The right hand side of the Bellman equation (4.3):
v(x) = sup
u∈C(x)

r(x, u) + α
X
y∈E
M(u)
xy v(y)


∀x ∈E
can also be written as:
sup
u∈C(x)

r(x, u) + αE [v(X1) | X0 = x, U0 = u]

.
Moreover, in the case of the deﬁnition of a MDP using a i.i.d. random sequence (Wn) and a
dynamics f such that Xn+1 = f(Xn, Un, Wn), the right hand side of the Bellman equation writes:
sup
u∈C(x)

r(x, u) + αE [v(f(x, u, W0))]

.
4.1.2
The Bellman operator
Deﬁnition 4.6. Let Bα : RE →RE be the map such that for all v ∈RE, and x ∈E, we have
[Bα(v)](x) = sup
u∈C(x)

r(x, u) + α
X
y∈E
M(u)
xy v(y)

.
67


## Page 76

The map Bα is called the Bellman operator of the discounted inﬁnite horizon Markov decision
problem.
The dynamic programming equation can be rewritten in functional form as the ﬁxed point
equation of the Bellman operator Bα:
v = Bα(v) .
Fact 4.7. The undiscounted Bellman operator B1 is monotone and additively homogenous.
Recall the proof given in the ﬁnite horizon case:
Bα is the supremum of Kolmogorov operators
B(π)
α
: v 7→r(π) + αM(π)v .
The operators B(π)
1
are monotone and additively homogeneous, so is B1. One can also do the proof
by “hand” on:
B1(v)(x) = sup
u∈C(x)

r(x, u) + E [v(f(x, u, W0))]

.
Expectation is monotone and it is additively homogenous because E [1] = 1.
So is the previous expression as a function of v.
Corollary 4.8. The discounted Bellman operator Bα is Lipschitz continuous for the sup-norm with
Lipschitz constant α, thus it is α-contracting when α < 1.
Corollary 4.9. When E is ﬁnite and α < 1, the operator Bα admits a unique ﬁxed point v∗.
Moreover, for any initial point v0 ∈RE, the sequence vn+1 = Bα(vn) converges towards v∗:
∥vn −v∗∥∞≤αn∥v0 −v∗∥∞.
Deﬁnition 4.10. The algorithm constructing the sequence vn+1 = Bα(vn) is called value iterations.
4.1.3
Proof of the Stationary Dynamic programming equation
1. v is solution of the Bellman equation.
Assume that α < 1. Let v∗be the unique solution
of the Bellman equation v = Bα(v), (by Fact 4.9).
Let v(N) be the value function of the ﬁnite horizon problem:
v(N)(x) = max
σ
J(N,σ)
0
(x) ,
with
J(N,σ)
0
(x) := JN
0,x(X; U) := E
" N−1
X
k=0
αkr(Xk, Uk)
!
+ 0 | X0 = x
#
.
From Theorem 3.13, v(N) = v(N)
0
with v(N)
k
solution of the dynamic programming equation:
v(N)
N (x) = 0
∀x ∈E ,
v(N)
k
(x) = sup{αkr(x, u) +
X
y∈E
M(u)
xy v(N)
k+1(y) | u ∈C(x)}
∀x ∈E, k ≤N −1.
68


## Page 77

This can be rewritten as
v(N)
k
= αkBα(v(N)
k+1/αk+1) .
Hence, v(N) = BN
α (0) := Bα ◦· · · ◦Bα(0) (where the composition is done N times). Therefore,
limN→∞v(N) = v∗where the limit is uniform in E (limit for the sup-norm of RE).
Let C be a bound of r. Then, for all strategies σ, the sum P∞
k=0 αkr(Xk, Uk) exists a.s. since
|αkr(Xk, Uk)| ≤Cαk (the series is absolutely convergent). Hence the expectation J(σ)
α (x) also exists
and is bounded. Therefore
v(x) := sup
σ J(σ)
α (x) = sup
σ E
" ∞
X
k=0
αkr(Xk, Uk) | X0 = x
#
∈R
exists and satisﬁes
∥v −v(N)∥∞≤
∞
X
k=N
αkC = αN
C
1 −α ,
so limN→∞v(N) = v, which implies that v = v∗.
2. Optimality.
Note that the bound ∥v −v(N)∥∞≤αN
C
1−α holds for the maximization over all
nonstationary types of strategies: relaxed strategies, pure strategies, Markov strategies, or feedback
policies. Since the value v(N) is the same if we maximize over all these types of strategies, the same
property holds for v. To get the equality with stationary feedback strategies, and the optimality of
the feedback policy given by Bellman equation, one proceed as for the proof of the ﬁnite horizon
case.
If π is the stationary policy obtained as in the theorem, that is if u = π(x) is optimal in (4.3),
then v satisﬁes the Kolmogorov equation associated to π, and so (by Theorem 2.28), v(x) = J(π)
α (x)
which shows that π is optimal. If u = π(x) is only ε-optimal for (4.3), that is
v(x) −ε ≤

r(x, u) + α
X
y∈E
M(u)
xy v(y)


Then, v −ε1 ≤B(π)
α (v). Iterating this inequality and using that B(π)
1
is monotone and additively
homogenous, which, with B(π)
α (v) = B(π)
1 (αv), implies that B(π)
α
is monotone and satisﬁes B(π)
α (λ1+
v) = αλ1 + B(π)
α (v), we get
v ≤ε + B(π)
α (v) ≤ε(1 + α) + [B(π)
α ]2(v) ≤· · · ≤ε1 −αn+1
1 −α
+ [B(π)
α )]n+1(v) .
Using that B(π)
α
is contracting, we get that the limit of [B(π)
α )]n+1(v) is equal to the solution of
the stationary Kolmogorov equation, and is thus equal to J(π)
α . Passing to the limit when n →∞,
in the previous inequality, we deduce:
v ≤
ε
1 −α + J(π)
α
.
This shows that π is then ε/(1 −α)-optimal for the Markov decision problem.
Since this holds for all ε > 0 (with a diﬀerent π), we obtain that v is less or equal to the
supremum of J(π)
α
over all stationary feedback policies. Since v is the supremum of J(σ)
α
over all
strategies, and is thus greater or equal to the one over all stationary feedback policies, we deduce
that both suprema are equal.
69


## Page 78

4.2
Algorithms
4.2.1
Value iteration algorithm
Recall that the value iteration is the algorithm constructing
vn+1 = Bα(vn) .
that is the ﬁxed point iterations associated to the α-contracting operator Bα.
• It satisﬁes
∥vn −v∥∞≤αn∥v0 −v∥∞.
• Denote rmax a bound on r (on both sides). Using the deﬁnition of v (as a maximum of the
criterion (4.2), we found
∥v∥∞≤rmax
1 −α .
This can also be obtained from (4.3).
• To ﬁnd a ε-solution, starting from 0, one need n iterations with αn rmax
1−α ≤ε, so the complexity
is in
O
log((1−α)ε
rmax )
log(α)

nm ,
where m = card(A) and n = card(E) (O(nm) is the maximal complexity of the computation
of Bα(v) for some v).
• If α = 1−η with η = p/q a small rational, then the length (number of bit) of α is in the order
of log(q), whereas −1/ log(α) is in the order of q so is exponential in the length of α, so in the
length of the input.
• Hence value iteration is only pseudo-polynomial.
• If α is ﬁxed, and we consider that the entries ε, r(x, u) and M(u)
xy are rational numbers, we
obtain that the complexity of value iteration is polynomial in the total length (number of bit)
of the entries, so is a polynomial algorithm. Since the number of iterations depends on rmax,
value iteration algorithm is not strongly polynomial.
• In practice one uses rather a variant similar to Gauss-Seidel algorithm (wrt to Jacobi) for the
solution of linear systems, in order to avoid useless storage. The resulting algorithm is called
Ford-Bellman algorithm. It depends on some ordering on E.
It has a similar convergence rate and complexity.
• When α < 1, or when α = 1 and the MDP is not deterministic, none of them converge in
ﬁnite time.
• This is already the case with no control: C = {1}.
70


## Page 79

• For α < 1, take E = {1}, r = rmax, and v0 = 0, then vn ∈R satisﬁes
vn+1 = rmax + αvn =⇒vn = rmax
1 −αn
1 −α
In this case, the number of iterations is equal to
log( (1−α)ε
rmax )
log(α)
. So the upper bound was tight.
• For α = 1, take E = {1, 2}, M =
1/2
1/2
0
1

and r =
1
0

. Then vn ∈R2 satisﬁes
vn+1(1) = 1 + vn(1)/2 + vn(2)/2,
vn+1(2) = vn(2).
• If v0(2) = 0, we get vn(1) = 2(1 −2−n), and so the number of iterations is equal to log(ε/2)
log(1/2).
4.2.2
Policy iteration algorithm
Recall that we want to solve
v(x) = sup
u∈C(x)

r(x, u) + α
X
y∈E
M(u)
xy v(y)


∀x ∈E .
and ﬁnd an optimal strategy of the Markov decision problem.
Assume that the action space C are ﬁnite, then for all v ∈RE, and x ∈E, the maximum in
sup
u∈C(x)

r(x, u) + α
X
y∈E
M(u)
xy v(y)


(4.4)
is attained by some action π(x) ∈C(x).
Theorem 4.5 shows that computing π with respect to the solution of the Bellman equation
yields a feedback policy which is optimal among all strategies.
The following algorithm has been introduced by Howard (1960) and is thus also called Howard
algorithm.
Deﬁnition 4.11. The policy iteration algorithm applied to the Bellman equation v = Bα(v) consists
in the following successive steps k ≥0, starting from a policy π0 ∈Π:
1. wk is the unique solution of the Kolmogorov equation associated to the policy πk:
v(x) = r(x, πk(x)) + α
X
y∈E
M(πk(x))
xy
v(y)
∀x ∈E .
2. πk+1 is an optimal policy for wk, that is an element π such that
π(x) ∈Argmax
u∈C(x)

r(x, u) + α
X
y∈E
M(u)
xy wk(y)


∀x ∈E .
71


## Page 80

The Bellman equation can be put in the form:
v = Bα(v) ,
where Bα is the supremum of the Kolmogorov operators:
B(π)
α
: v 7→r(π) + αM(π)v .
If π is optimal for v in (4.4), then
Bα(v) = B(π)
α (v)
which means that
Bα(v) = max
π∈Π B(π)
α (v) .
Fact 4.12. The policy iteration algorithm applied to the Bellman equation v = Bα(v) consists in
the following successive steps, starting from a policy π0 ∈Π: for k ≥0, do
1. wk is the value of problem when the policy is freezed to πk that is the solution of the equation
w = B(πk)
α
(w).
2. πk+1 is an optimal policy for wk, that is an element π of Π such that B(π)
α (wk) = Bα(wk).
Theorem 4.13. Assume that the optimization problems in Bellman equations can be solved, that
is, for all v ∈RE, there exists π ∈Π such that B(π)
α (v) = Bα(v). Denote by v the value function of
the MDP with discounted criteria, that is the solution of v = Bα(v).
Then, for all k ≥0, we have
wk ≤wk+1 ≤· · · ≤v ,
and
lim
k→∞wk = v .
Moreover,
wk ≤Bα(wk) ≤wk+1 ,
which means that the policy iteration algorithm converges faster than the value iteration algorithm,
and we have
∥wk+1 −v∥∞≤α∥wk −v∥∞.
The proofs of Policy iteration properties use the following properties that are of independent
interest.
Proposition 4.14 (Sub or supersolutions). Let B be a monotone operator from RE to itself, which
is contracting for the sup-norm. Let v be the unique ﬁxed point of B. Then
w ≤B(w) =⇒w ≤v
(4.5)
w ≥B(w) =⇒w ≥v .
(4.6)
Proof. From w ≤B(w) and monotonicity of B, we get, for all n ≥1, w ≤· · · ≤Bn(w).
Since B is contracting, Bn(w) converges towards v, which implies w ≤v.
72


## Page 81

Deﬁnition 4.15. A solution of w ≤B(w) is called a subsolution of Bellman equation.
A solution of w ≥B(w) is called a supersolution of Bellman equation.
Proof of Theorem 4.13. We have
wk = B(πk)
α
(wk)
(4.7)
Bα(wk) = B(πk+1)
α
(wk)
(4.8)
wk+1 = B(πk+1)
α
(wk+1) .
(4.9)
Using the ﬁrst and second equation together with the deﬁnition of Bα, we get
wk = B(πk)
α
(wk) ≤Bα(wk) = B(πk+1)
α
(wk) .
Hence wk is a subsolution of the Kolmogorov equation w = B(πk+1)
α
(w). From (4.5) applied to the
operator B(πk+1)
α
, and (4.9), we deduce that wk ≤wk+1.
Since we also have wk ≤Bα(wk), wk is a subsolution of the Bellman equation w = Bα(w).
Applying (4.5) to Bα, we deduce that wk ≤v, for all k ≥0.
From the above inequalities, we also get that wk ≤Bα(wk) = B(πk+1)
α
(wk), and so B(πk+1)
α
(wk) ≤
(B(πk+1)
α
)2(wk) ≤· · · ≤wk+1. This shows that wk ≤Bα(wk) ≤wk+1 ≤v, which is the second
assertion. With this we get that
0 ≤v −wk+1 ≤v −Bα(wk)
hence
∥v −wk+1∥∞≤∥v −Bα(wk)∥∞= ∥Bα(v) −Bα(wk)∥∞≤α∥v −wk∥∞.
This shows that the sequence wk converges towards v and that the convergence is faster than the
one of value iterations.
Theorem 4.16. Assume that the action spaces C(x) are all ﬁnite.
Then, the policy iteration
algorithm converges in a ﬁnite number of steps.
Proof. Since the sets C(x) are ﬁnite, the set of feedback policies, Π is ﬁnite. Therefore, there exists
k < ℓsuch that πk = πℓ. From the uniqueness of the solution w to the equation B(πk)
α
(w) = w, we
get that wk = wℓ. Since the sequence wk is nondecreasing, wk ≤wk+1 ≤· · · ≤wℓ, and satisﬁes
wk = wℓ, we get the equality wk = wk+1.
Then, using the deﬁnition of wk+1 and πk+1, and
wk = wk+1, we deduce wk = wk+1 = B(πk+1)
α
(wk+1) = B(πk+1)
α
(wk) = Bα(wk). Hence, wk is a ﬁxed
point solution of Bα and since Bα is contracting, the ﬁxed point is unique, so wk = v. Moreover,
since πk+1 satisﬁes Bα(v) = B(π)
α (v), then it is optimal, and wℓ= v for all ℓ≥1.
4.2.3
Additional properties of Policy iterations for discounted problems
In Theorem 4.18 below, we prove that the policy iterations coincide with Newton algorithm applied
to the system of equations v −Bα(v) = 0.
Let us ﬁrst remark that if the map Bα is regular, then the latter Newton algorithm consists in
the iterations (wk)k≥0 in which wk+1 is the solution of the tangent equation in point wk, that is
Dwk(I −Bα)(wk+1 −wk) + (I −Bα)(wk) = 0
73


## Page 82

which can be rewritten as:
wk+1 = Bα(wk) + Dwk(Bα)(wk+1 −wk) .
Moreover, one can weaken Newton algorithm by replacing the above diﬀerential by a subdif-
ferential of Bα. Therefore, using the following result, one can see that policy iteration algorithm
belongs to the class of generalized Newton algorithms, since then the above equation is equivalent
to
wk+1 = rπwk
+ αM(πwk)wk+1 = Bπwk
α
(wk+1) .
Lemma 4.17. For all x ∈E, the map ψ : v ∈RE 7→[Bα(v)](x) ∈R is convex, and for all v ∈RE,
and u ∈Argmaxu∈C(x){r(x, u) + αM(u)
x v}, the row vector αM(u)
x
is in the subdiﬀerential of ψ at
point v.
Proof. For all x ∈E, the map ψ : v ∈RE 7→[Bα(v)](x) ∈R is convex as a supremum of aﬃne
maps: ψ(x) = [Bα(v)](x) = supu∈C(x) r(x, u) + αM(u)
x v. If u ∈Argmaxu∈C(x){r(x, u) + αM(u)
x v},
we get that
ψ(w)−ψ(v) = [Bα(w)](x)−[Bα(v)](x) ≥(r(x, u)+αM(u)
x w)−(r(x, u)+αM(u)
x v) = αM(u)
x (w−v) .
This shows that the row vector αM(u)
x
is in the subdiﬀerential of ψ at point v.
Theorem 4.18. Assume that E is ﬁnite, that the sets C(x) are compact spaces, that there exists a
continuous map v ∈RE 7→πv ∈Π such that, for all v ∈RE, πv is the unique element of Π such
that B(πv)
α
(v) = Bα(v), and that the map u ∈C(x) 7→M(u)
xy is continuous for all x, y ∈E. Then,
Bα is of class C1, the policy iteration algorithm coincides with Newton algorithm associated to the
ﬁxed point equation v = Bα(v), and its convergence is superlinear:
lim
k→∞
∥wk+1 −v∥∞
∥wk −v∥∞
= 0 .
Proof. Assume that a continuous map v ∈RE 7→πv ∈Π exists with the property that πv is the
unique element of Π such that B(πv)
α
(v) = Bα(v). This means that, for all v ∈RE, x ∈E, u = πv(x)
is the unique element of Argmaxu∈C(x){r(x, u) + αM(u)
x v}. Then, by Lemma 4.17, αM(u)
x
is in the
subdiﬀerential of ψ : v ∈RE 7→[Bα(v)](x) ∈R at point v. Similarly, for all w ∈RE, αM(πw(x))
x
is
in the subdiﬀerential of ψ at w. Let p be any element of the subdiﬀerential of ψ at v, which means
that for all w ∈RE, we have
ψ(w) −ψ(v) ≥p(w −v) .
Then, we also have
ψ(w) −ψ(v) ≤αM(πw(x))
x
(w −v) ,
since αM(πw(x))
x
is in the subdiﬀerential of ψ at w. Therefore
p(w −v) ≤αM(πw(x))
x
(w −v) .
Consider the sequence wn = v + 1
nz, we deduce
pz ≤αM(πwn(x))
x
z .
74


## Page 83

Using that wn converges towards v, and that the maps w 7→πw(x) ∈C(x) and u ∈C(x) 7→M(u)
xy
are continuous, we deduce that αM(πwn(x))
x
converges towards αM(πv(x))
x
. This implies that pz ≤
αM(πv(x))
x
z. Since this holds for all z ∈RE, we deduce that p = αM(πv(x))
x
. We have shown that the
subdiﬀerential of ψ is reduced to a singleton. Then, the map is diﬀerentiable [6] and αM(πv(x))
x
is the
diﬀerential of v 7→[Bα(v)](x). Applying this property for all x ∈E, we get that Bα si diﬀerentiable
at v with diﬀerential equal to αM(πv). Since this diﬀerential is continuous with respect to v, this
shows also that Bα is of class C1. Then, the above comments show that policy iteration algorithm
coincides with Newton algorithm.
Now let v be the value function. We have
(I −αM(πwk))(wk+1 −v) = rπwk
+ αM(πwk)v −v
(4.10)
= Bα(wk) −Bα(v) −αM(πwk)(wk −v) .
(4.11)
We can show
∥wk+1 −v∥∞≤
1
1 −α∥Bα(wk) −Bα(v) −αM(πwk)(wk −v)∥∞.
Since we already proved that Bα is of class C1 and that its diﬀerential at v is equal to αM(πv), we
get that the right hand side of the above inequality is in o(∥wk −v∥∞), which gives the superlinear
convergenve of Policy Iterations.
Another proof is using directly the above subdiﬀerential properties to show from (4.10):
α(M(πv) −M(πwk))(wk −v) ≤(I −αM(πwk))(wk+1 −v) ≤0 .
Then, we obtain
∥wk+1 −v∥∞≤
α
1 −α∥(M(πwk)−M(πv))(wk −v)∥∞,
and since the map v 7→M(πv) is continuous, the right hand side of the above inequality is in
o(∥wk −v∥∞), which gives the superlinear convergenve of Policy Iterations.
Note that contrarilly to the general situation of the Newton algorithm, the policy iterations
always converge towards the solution of the ﬁxed point equation. This comes from the convexity
of the maps v 7→[B(v)](x), which implies the monotonicity of the sequence of value functions wk.
4.3
Optimal stopping time problems with inﬁnite horizon
Consider
• a (ﬁxed) stationary Markov chain (Xn)n≥0 over a probability space (Ω, A, P) with values in
a ﬁnite state space E and transition matrix M and initial probability law p(0).
• an instantaneous/running reward/payoﬀ(at any time k), which is a map r : A →R;
• a (ﬁxed) discount factor α ∈[0, 1).
75


## Page 84

• for all stopping times τ with respect to the Markov chain (Xn)n≥0, the discounted inﬁnite
horizon payoﬀwith stopping time τ:
J(τ)
α
:=E
" τ−1
X
ℓ=0
αℓr(Xℓ)
!
+ ατϕ(Xτ)
#
;
(4.12)
• and the discounted inﬁnite horizon payoﬀwith stopping time τ, starting in x at time 0:
J(τ)
α
:=E
" τ−1
X
ℓ=0
αℓr(Xℓ)
!
+ ατϕ(Xτ) | X0 = x
#
.
(4.13)
Deﬁnition 4.19. An Optimal stopping time problem with complete observation and inﬁnite horizon
discounted criteria consists in the following optimization problem:
max
τ
J(τ)
α
where the optimization holds over all stopping times τ with respect to the Markov chain (Xn)n≥0.
The optimum of above criteria is called the value of the problem.
An optimal solution τ is called an optimal stopping time.
Deﬁnition 4.20. For all x ∈E, let vα(x) or simply v(x) be the value of the optimal stopping time
problem with an initial state x:
max
τ
J(τ)
α (x) .
The map vα : E →R, x 7→vα(x) is called the value function of the stopping time problem.
Theorem 4.21 (Dynamic programming equation for optimal stopping time problems with dis-
counted inﬁnite horizon criteria). Assume that the map r is bounded from above. Let v be the value
function of the optimal stopping time problem:
v(x) := max
τ
J(τ)
α (x) ,
where the maximum is taken over all stopping times τ with respect to the Markov chain (Xn)n≥0.
Then, v is the unique solution of the following ﬁxed point equation, called stationary Bellman
equation or variational inequality:
v(x) = max

r(x) + α
X
y∈E
Mxyv(y), ϕ(x)

∀x ∈E .
(4.14)
Let B be the set of states in which the maximum in (4.14) is attained in the ﬁrst term, that is
B := {x ∈E | r(x) + α
X
y∈E
Mxyv(y) ≥ϕ(x)} .
Then an optimal stopping time τ is obtained by choosing for τ the exit time τB from B of the
Markov chain.
Proof. Consider the MDP in which
76


## Page 85

• the state space is E′ = E ∪{c} where c̸ ∈E;
• the control space C = {0, 1} (0 for stop, and 1 for not stop);
• the control space C(x) is such that C(x) = C if x ∈E and C(x) = {0} if x = c.
• the states of the MDP, Yn, depend on the states of the Markov chain Xn and on the actions
as follows:
Yn+1 = g(Xn+1, Un)
where g(x, u) = x if u = 1 and g(x, u) = c otherwise.
Then, for all xi ∈E′, ui ∈Ci(xi), i ≥0, we have
P(Yk+1 = xk+1 | Yk = xk, Uk = uk, Yk−1 = xk−1, . . . , Y0 = x0, U0 = u0)
= 1 if c = xk+1 and uk = 0
= 0 if xk+1 ∈E and uk = 0
= Mxk,xk+1 if xk, xk+1 ∈E and uk = 1
This implies that
P(Yk+1 = xk+1 | Yk = xk, Uk = uk, Yk−1 = xk−1, . . . , Y0 = x0, U0 = u0)
= P(Yk+1 = xk+1 | Yk =k, Uk = uk) .
which is the Markov property. The transition vectors of the MDP are: M(1)
xy = Mxy for all x, y ∈E,
M(1)
xy = 0 for all y = c, and M(0)
xy = 1 for y = c and 0 for y ∈E.
Let us take the rewards: r′(x, 1) = r(x), r′(x, 0) = φ(x) for x ∈E and r′(c, 0) = 0.
Then, the value of the discounted inﬁnite horizon problem coincides with the value of the
stopping time problem. Indeed, take τ = inf{t ≥0 | Ut = 0}, and conversely take Un = 1 for all
n < τ and Un = 0 for n ≥τ. Then, τ is a stopping time if and only if Un is given by a strategy.
The Bellman equation of the Markov decision problem is then:
v(x) = max

r(x) + α
X
y∈E
Mxyv(y), ϕ(x) + v(c)

∀x ∈E ,
v(c) = 0 .
Here the action u = 1 corresponds to the left term in the above maximum, and u = 0 corresponds
to the right term. Therefore if π : E →{0, 1} is an optimal policy given by the Bellman equation,
we recover again the optimal stopping time by taking:
τ = inf{t ≥0 | π(Xt) = 0}
or by taking τ = τB where B = {x ∈E | π(x) = 1}.
77


## Page 86

4.4
Problems with variably discounted inﬁnite horizon payoﬀ
Assume given a stationary Markov decision process, and the following stationary parameters:
• the instantaneous/running reward/payoﬀ(at any time k), which is a map r : A →R;
• a variable discount factor (at any time k), which is a map α : A →R+;
• for all strategies σ = (σk)k≥0 in Σ or ΣR, the variably discounted total additive payoﬀwith
inﬁnite horizon:
J(σ) :=J(X; U) := E
" ∞
X
ℓ=0
 ℓ−1
Y
m=0
α(Xm, Um)
!
r(Xℓ, Uℓ)
#
,
(4.15)
where (X, U) := (Xk, Uk)k≥0 is the process induced by σ as in Deﬁnition 3.2 or Deﬁnition 3.3.
• and the variably discounted total additive payoﬀwith inﬁnite horizon, starting x at time 0:
J(σ)(x) := Jx(X; U) := E
" ∞
X
ℓ=0
 ℓ−1
Y
m=0
α(Xm, Um)
!
r(Xℓ, Uℓ) | Xk = x
#
,
(4.16)
Theorem 4.22 (Dynamic programming equation for Markov decision problems with variably dis-
counted inﬁnite horizon criteria). Assume that the map r is bounded from above and that α(x, u) ≤¯α
for all (x, u) ∈A, for some constant ¯α < 1. Let v be the value function of the Markov decision
problem associated to the above parameters:
v(x) := max
σ
J(σ)(x) ,
where the maximum is taken over all relaxed strategies (starting at time 0). Then, v is the unique
solution of the following ﬁxed point equation, called the stationary Bellman dynamic programming
equation:
v(x) = sup
u∈C(x)

r(x, u) + α(x, u)
X
y∈E
M(k,u)
xy
v(y)


∀x ∈E .
(4.17)
Moreover, the values v obtained by optimizing over the restricted sets of pure strategies, Markov
strategies, or feedback policies, or stationary feedback policies coincide.
Assume in addition that the maximum of (4.17) is attained for an action u ∈C(x) and let us
denote by π(x) this action, then the stationary feedback policy π (that is (πk)k≥0 with πk = π) is
an optimal strategy of the problem. problem.
The arguments of the proof are the same as when α is constant. Let us consider the Bellman
operator of the variably discounted problem which is the map B : RE →RE such that, for all
v ∈RE, and x ∈E, we have
[B(v)](x) = sup
u∈C(x)

r(x, u) + α(x, u)
X
y∈E
M(u)
xy v(y)

.
The map B satisﬁes the following properties
78


## Page 87

Lemma 4.23. Under the assumptions of Theorem 4.22, B is monotone and ¯α-additively subho-
mogenous (Deﬁnition 3.22), meaning that for all v ∈RE and λ ≥0, we have
B(v + λ1) ≤B(v) + ¯αλ1 .
Therefore, it is Lipschitz continuous for the sup-norm with Lipschitz constant ¯α < 1, thus it is
¯α-contracting.
Proof. The ﬁrst assertion can be proved elementarily. Let us prove the second one using the ﬁrst
one. Let v, v′ ∈RE. Denote λ = ∥v−v′∥∞. We have v(x) ≤λ+v′(x) for all x ∈E, that is v ≤v′+λ1.
Since B is monotone, we get B(v) ≤B(v′ +λ1). Since B is additively subhomogenous with constant
¯α, we deduce B(v′ + λ1) ≤B(v′) + ¯αλ. Then, B(v) ≤B(v′) + ¯αλ1, hence maxx∈E[B(v)](x) −
[B(v′)](x) ≤¯αλ. Exchanging v and v′ we get the other inequality: maxx∈E[B(v′)](x) −[B(v)](x) ≤
¯αλ. Hence ∥B(v′) −B(v)∥∞= maxx∈E max([B(v′)](x) −[B(v)](x), [B(v)](x) −[B(v′)](x)) ≤¯αλ =
¯α∥v′ −v∥∞. This shows the Lipschitz continuity.
Proof of Theorem 4.22. We use the same technique as for the constant discount factor case: ﬁrst
use of Bellman equation for ﬁnite horizon problems with mixed criterias, then take the limit us-
ing contraction, then use of the stationary Kolmogorov equation for inﬁnite horizon criteria with
variable discount factor.
Exercise 4.4.1. Show that one can reduce the above problem to an inﬁnite horizon problem with
constant discount factor equal to ¯α, by adding a cemetery point to the state space E.
Corollary 4.24. Under the assumptions of Theorem 4.22, the sequence v(T) of value functions
of ﬁnite horizon problems with mixed criteria (given in Remark 3.21) converges when T goes to
inﬁnity to the unique solution of the stationary Bellman dynamic programming equation (4.17).
4.5
Problems with exit time in inﬁnite horizon
Assume given a stationary Markov decision process, and the following stationary parameters:
• a strict subset B of E;
• a ﬁnal reward, which is a map ϕ : E →R;
• a (ﬁxed) discount factor α ∈[0, 1);
• the instantaneous/running reward/payoﬀ(at any time k), which is a map r : A →R;
• for all strategies σ = (σk)k≥0 in Σ or ΣR, the payoﬀwith exit time in inﬁnite horizon:
J(B,σ) :=JB(X; U) := E
"τB−1
X
ℓ=0
αℓr(Xℓ, Uℓ) + ατBϕ(XτB)1τB<+∞
#
,
(4.18)
where (X, U) := (Xk, Uk)k≥0 is the process induced by σ as in Deﬁnition 3.2 or Deﬁnition 3.3,
and τB is the exit time of the process (Xn)n≥0 from B.
79


## Page 88

• and the payoﬀwith exit time and inﬁnite horizon, starting in x at time 0:
J(B,σ)(x) := JB
x (X; U) := E
"τB−1
X
ℓ=0
αℓr(Xℓ, Uℓ) + ατBϕ(XτB)1τB<+∞| X0 = x
#
.
(4.19)
Theorem 4.25 (Dynamic programming equation for Markov decision problems with exit time in
discounted inﬁnite horizon). Assume that the maps ϕ, r are bounded from above. Let v be the value
function of the Markov decision problem:
v(x) := max
σ
J(B,σ)(x) ,
where the maximum is taken over all relaxed strategies (starting at time 0). Then, v is the unique
solution of the following ﬁxed point equation, called the stationary Bellman dynamic programming
equation:
v(x) = sup
u∈C(x)

r(x, u) + α
X
y∈E
M(k,u)
xy
v(y)


∀x ∈B .
(4.20a)
with boundary condition
v(x) = ϕ(x),
∀x̸ ∈B .
(4.20b)
Moreover, the values v obtained by optimizing over the restricted sets of pure strategies, Markov
strategies, or feedback policies, coincide.
Assume in addition that the maximum of (4.20) is attained for an action u ∈C(x), for x ∈B,
and let us denote by π(x) this action when x ∈B, and choose any action π(x) for x̸ ∈B, then the
stationary feedback policy π (that is (πk)k≥0 with πk = π) is an optimal strategy of the problem.
As for ﬁnite horizon problems, Theorem 4.25 can be deduced easily from Theorem 4.22 using
the following property which is the same as Fact 2.37 and Fact 3.26.
Fact 4.26. The functional J(B,σ) of (4.19) can rewritten as the inﬁnite horizon mixed functional:
J(B,σ)(x) := JB
x (X; U) :=E
" ∞
X
ℓ=0
 ℓ−1
Y
m=0
α(Xm, Um)
!
r′(Xℓ, Uℓ)
#
,
for the same Markov Decision process, with the instantaneous rewards r′ and variable discount
factors α given by:
r′(x, u) = r(x, u),
for x ∈B, u ∈C(x)
r′(x, u) = ϕ(x),
for x̸ ∈B, u ∈C(x)
α(x, u) = α,
for x ∈B, u ∈C(x)
α(x, u) = 0,
for x̸ ∈B, u ∈C(x) .
80


## Page 89

4.6
Problem: Divorce of Birds
This problem is taken from the (ENSTA+M2) exam of 2016/2017.
We consider the modelization of the decision of divorce of birds as a MDP. We assume that at
each breeding (reproduction) season, the bird female has a mate, and that at the end of the season,
she is taking the decision on whether to divorce her mate. Then, winter arrives and the female and
the male may die. If the female has no mate after winter (she divorced, or the male died, or it is
the ﬁrst breeding season of the female), then she is choosing a mate among a “pool” of available
males. The decision of the female is based on the qualities of the male and female, and also on the
information on whether it is the ﬁrst breeding season of the female, or the female divorced, or the
male died during winter.
We consider the following notations, parameters and assumptions:
• We consider one female during her life, and denote by Yk ∈Y ⊂R her quality at the begining
of the breeding season of year k (one can start to number years after the female is able to
breed). We shall assume that Y = [¯y] := {0, . . . , ¯y}, where y = 0 means that the female is
dead. We denote by Y∗= Y \ {0}.
• We denote by Xk ∈X ⊂R the quality of the male choosen by the female at the begining of
the breeding season of year k. Again, one may assume that X = [¯x].
• We denote by Zk ∈Z = {0, 1, M} the information on whether it is the ﬁrst breeding season
of the female or the female divorced (in which case Zk = 0), or the male died during winter
(in which case Zk = M), or the female mated with the same male the previous year (in which
case Zk = 1).
• We denote by Uk ∈C = {0, 1} the decision of the female to divorce: Uk = 1 if she decides to
divorce and 0 otherwise.
• r(x, y, z) is the reproductive success, that is the expected number of children, during one
season, when the qualities of the male and female are x and y and the information on whether
it is the ﬁrst breeding season of the female or the female divorced or the male died during
winter is z.
• We assume that the pools of males in which the female is choosing a partner each year when
needed are independent and that f(x) is the probability of ﬁnding a male with quality x in
a pool.
• sf and sm are respectively the survival probabilities of a female and a male after winter. They
are independent of age, constant and < 1.
• We assume that the quality of males and females do not vary with time until their death.
Q 6.1. Show that the sequence Yk is a Markov chain and compute its transition probability.
Q 6.2. Show that the sequences Xk, Yk, Zk, Uk deﬁne a MDP, precise what is the state and what
is the control, and compute the transition probabilities.
Q 6.3. We assume that the aim of the female is to maximize her reproductive success, that is the
expected total number of her children, during all her life. Write this as an inﬁnite horizon criterion
for the MDP.
81


## Page 90

Q 6.4. Let v(x, y, z) be the value of the previous problem when the initial qualities of male and
female are x ∈X and y ∈Y∗and the information on what happened before and during previous
winter is z ∈Z. What is the equation satisﬁed by the function v? How to ﬁnd an optimal policy?
Q 6.5. Show that the equation of v is of the form v(x, y, z) = [F(v)](x, y, z) where F is an operator
on the set of functions from X × Y∗× Z to R of the form:
[F(v)](x, y, z) = r(x, y, z) + sf max

[M(1)v](y), [M(0)v](x, y)

where v is identiﬁed to a vector, for u = 0, 1, M(u) is a Markov matrix, and [M(0)v]x,y,z does not
depend on z and [M(1)v]x,y,z does not depend on x and z.
Q 6.6. Deduce that the operator F is contracting for the sup-norm ∥v∥= maxx,y,z |v(x, y, z)|.
Q 6.7. Show that the ﬁxed point v of F is unique.
Q 6.8. Show that if r is nondecreasing with respect to x, then so does v.
Q 6.9. Show in that case that there exists x∗(y) such that the optimal policy of the female y is to
divorce from the male x if and only if x < x∗(y).
Some references for this problem:
[BI1] John M. McNamara and Par Forslund. Divorce rates in birds: Predictions from an optimiza-
tion model. The American Naturalist, 147(4):609–640, 1996.
82


## Page 91

Chapter 5
Long run average payoﬀproblems
5.1
Motivation
Consider a stationary Markov Decision Process (Xk)k≥0, that is a MDP with a dynamics (transition
probabilities) independent of time. This means that the following parameters (independent of time)
are given:
• a state space E, which is a ﬁnite or countable set;
• a set of actions C, and possibly for each state x ∈E, a nonempty subset C(x) of C, which is
the set of possible actions when the state is equal to x;
• an initial probability p(0) on E, or an initial state x0, which is equivalent to the case where
p(0) is the Dirac measure at x0;
• for all x ∈E and u ∈C(x), a probability vector M(u)
x
over E, the entries of which will be
denoted

M(u)
xy

y∈E.
Recall, that given the above parameters, and a pure strategy σ = (σk)k≥0, there exists two
discrete time processes (Xk)k≥0 and (Uk)k≥0 taking their values in E and C respectively, with
transition probabilities M(u)
xy :
M(u)
xy = P(Xk+1 = y | Xk = x, Uk = u)
satisfying
Uk = σk(X0, U0, . . . , Xk−1, Uk−1, Xk) ,
and the Markov property:
P(Xk+1 = y | Xk = x, Uk = u, Xk−1 = xk−1, Uk−1 = uk−1, . . . , X0 = x0, U0 = u0)
=
P(Xk+1 = y | Xk = x, Uk = u) ,
∀x, y, xi ∈E, u ∈C(x), ui ∈C(xi), for i ≥0 .
Moreover, the same holds for a relaxed strategy, in which case:
P(Uk ∈B | X0, U0, . . . , Xk−1, Uk−1, Xk) = [σk(X0, U0, . . . , Xk−1, Uk−1, Xk)](B) .
83


## Page 92

We are interested here in the optimization of inﬁnite horizon undiscounted criteria or in long
run average criteria, for which we look for optimal strategies (among all strategies) that would be
stationary and in feedback form (Markov).
We assume given the stationary instantaneous/running reward/payoﬀ(at any time k), which is
a map r : A →R.
For all strategies σ = (σk)k≥0 in Σ or ΣR, the undiscounted total additive payoﬀwith inﬁnite
horizon (when it exists) is:
J(∞,σ) := J∞(X; U) := E
" ∞
X
k=0
r(Xk, Uk)
#
,
(5.1)
where (X, U) := (Xk, Uk)k≥0 is the process induced by σ as in Deﬁnition 3.2 or Deﬁnition 3.3.
This criteria is ﬁnite when for instance there exist a cemetery point c in which the state process
arrives almost surely in a ﬁnite expected time and the reward there is zero. In that case, one can
often transform the problem in a discounted control problem, in which the discount factor α is
such that the probability to arrive in one step to the cemetery point is at least 1 −α. So we can
generally apply the methods of the ﬁrst part of the course. In particular, the value function
v∞(x) := max J(∞,σ)
when X0 = x ,
is equal to the limit of the value function vT of the problem with ﬁnite horizon and (undiscounted)
additive criteria:
vT (x) = max J(T,σ)(x) ,
(5.2)
with
J(T,σ)(x) = E
" T
X
k=0
r(Xk, Uk) | X0 = x
#
.
(5.3)
The second type of criteria is the mean-payoﬀor long run time average payoﬀ/reward, which is
one of the following ones, for all strategies σ = (σk)k≥0 in Σ or ΣR
J(+,σ) := J+(X; U) := lim sup
T→∞
(
1
T E
" T
X
k=0
r(Xk, Uk)
#)
,
(5.4a)
J(−,σ) := J−(X; U) := lim inf
T→∞
(
1
T E
" T
X
k=0
r(Xk, Uk)
#)
,
(5.4b)
where (X, U) := (Xk, Uk)k≥0 is the process induced by σ as in Deﬁnition 3.2 or Deﬁnition 3.3.
The corresponding value functions will be denoted:
ζ±(x) = max J(±,σ)
when X0 = x .
One may try to understand in which situations both criteria are equal and independent of the
initial law of the MDP, and to compare the limit of (1 −α)Jσ
α when α goes to 1 from below.
Moreover, we shall compare the optimum of the limit with the limit of the optimum.
We also look for an optimal strategy which is a feedback stationary policy.
We ﬁrst study the uncontrolled case.
84


## Page 93

5.2
Long term behavior of Markov chains
5.2.1
Ergodicity of Markov chains
In this section, we shall study the uncontrolled case.
We assume that (Xk)k≥0 is a stationary Markov chain on the ﬁnite state space E (for instance
E = [n]) and we denote by M its transition probability matrix. Then, if X0 = x, we have
E
" T
X
k=0
r(Xk)
#
=
T
X
k=0
[Mkr]x ,
and when X0 is random with law p(0), we have
E
" T
X
k=0
r(Xk)
#
=
T
X
k=0
p(0)Mkr .
Hence, the value functions ζ± deﬁned in the previous section reduce to
ζϵ(x) = Jϵ((Xk)k≥0) :=



lim supT→∞
n
1
T
PT
k=0[Mkr]x
o
if ϵ = +
lim infT→∞
n
1
T
PT
k=0[Mkr]x
o
if ϵ = −.
(5.5)
Moreover, if we consider the case of a Markov chain (Xk) with initial law p(0) (not necessarily equal
to the Dirac measure in some state x0), then we are looking for
ζϵ(p(0)) = Jϵ((Xk)k≥0) :=



lim supT→∞
n
1
T
PT
k=0(p(0)Mkr)
o
if ϵ = +
lim infT→∞
n
1
T
PT
k=0(p(0)Mkr)
o
if ϵ = −.
(5.6)
Example 5.1. If (Xn)n≥0 is a sequence of independent random variables with values in E, then
it is in particular a Markov chain with transition matrix M such that all rows are equal to the
probability vector of X0, that is p(0). Then, (r(Xn))n≥0 is a sequence of i.i.d. random variables
with expectation equal to p(0)r and the law of large numbers shows that
1
T
T
X
k=0
r(Xk) −→
T→∞p(0)r
a.s.
Taking the expectation, we get that ζ±(p(0)) = p(0)r.
In order to generalize the law of large numbers, or at least the easier expectation version above,
to a Markov chain, one need the following notion.
Deﬁnition 5.2. We say that m ∈∆E is an invariant probability measure of the Markov chain
(Xn)n≥0 on E with transition matrix M, or simply of the matrix M, if m satisﬁes mM = m.
As an example, if Xn are i.i.d with laws p, then Xn is a Markov chain with invariant probability
measure p.
Fact 5.3. If the initial law of a Markov chain is an invariant probability measure, p(0) = m, then
the law of Xn is equal to m for all n ≥0.
85


## Page 94

In this case, it is easy to see that ζ±(p(0)) = mr. This motivates the following deﬁnition.
Deﬁnition 5.4. We say that the Markov chain with Markov transition matrix M is ergodic if M
has a unique invariant probability measure m.
To check the ergodicity of the chain or to ﬁnd more generally the limit ζ±(p(0)), we need to
study the spectral properties of the Markov matrix M. To do this, we can use general linear algebra
techniques in particular Jordan normal form and/or the Perron-Frobenius theorem which is the tool
for studying matrices with nonnegative entries. The latter result uses the properties of the graph
associated to M, deﬁned in the following section.
5.2.2
Graph properties of a Markov matrix
Recall (see Deﬁnition 2.13) that to a nonnegative matrix M over E, we associate a digraph denoted
G(M), with set of nodes equal to E and set of arcs A the set of (x, y) ∈E × E such that Mxy > 0.
Deﬁnition 5.5. Given a directed graph G, with set of nodes E, we deﬁne the relations on E such
that for x, y ∈E,
• x →y if there exists a path from x to y of any length ≥0 in G (where a path of length 0
means that x = y).
• x ∼y if x →y and y →x.
Proposition 5.6. For any digraph G with set of nodes E, ∼is an equivalence relation and →a
preorder on E. This deﬁnes a partition of E into equivalence classes for ∼, that are called strongly
connected components of the graph G. If G = G(M), where M is a Markov matrix, they are also
called communication classes of M. Moreover, the relation →becomes a partial order on the set
E/ ∼of strongly connected components of G.
Proof. →is reﬂexive, x →x ∀x ∈E, because paths of length 0 are allowed. It is transitive :
(x →y and y →z ⇒x →z) ∀x, y, z ∈E, by concatenation of paths. So it is a preorder.
Therefore ∼is also reﬂexive and transitive. Moreover, it is symmetric by deﬁnition: (x ∼y ⇔
y ∼x) ∀x, y ∈E.
Recall that the equivalence class of x for ∼is deﬁned as ¯x = {y ∈E, x ∼y}, and that we have
¯x = ¯y if x ∼y and ¯x ∩¯y = ∅otherwise, so that equivalence classes deﬁne a partition of E.
Since x ∼y if x →y and y →x, we get that →can be deﬁned on the quotient set E/ ∼, that
is the set of equivalence classes for ∼, and that on this quotient set, we have (¯x →¯y and ¯y →¯x) if
and only if ¯x = ¯y, so that →becomes a (partial) order.
Deﬁnition 5.7.
• A subset F of E is closed if (x ∈F and x →y) ⇒y ∈F.
• A closed set with a unique element is absorbant.
• A maximal element for →in E/ ∼is called a ﬁnal class. This is a stongly connected component
of G which is also a closed set.
• A transient state is an element of E which is not in a ﬁnal class.
• The graph G is strongly connected if it has a unique strongly connected component, or equiv-
alently if E is the only closed set.
86


## Page 95

• The matrix M is irreducible if G(M) is strongly connected.
• The Markov chain (Xn)n≥0 is irreducible if its transition matrix is irreducible.
In a ﬁnite set E, ﬁnal classes are equivalent to recurrence classes.
Example 5.8. The digraph G(M) of the following matrix M is shown on the right:
M =








0
0
0
0
0
1
1
2
0
0
0
1
2
0
0
0
1
0
0
0
1
0
0
0
0
0
0
3
4
1
4
0
0
0
0
0
0
1
0
0








1
2
3
4
5
6
.
6
2
1
1
1
1/2
3/4
1/4
1
1
4
3
5
1/2
We see 3 strongly connected components: {1, 4, 6}, {3} and {2, 5}. The state 3 is absorbant.
The closed sets are E, {3}, {1, 4, 6} and {1, 3, 4, 6}. The ﬁnal classes are {3} and {1, 4, 6}.
Example 5.9 (Simple random walk). Given a directed graph G with set of nodes N and arcs
A, and at least one arc from each node, a simple random walk is a Markov chain with transition
probabilities: Mxy = 1/Nx if (x, y) is an arc and Nx ≥1 is the number of arcs starting from x,
and Mxy = 0 otherwise. This means that the random walker is going with uniform probability in
outgoing arcs. The graph of M coincides with G.
Example 5.10 (PageRank). Denote by E the set of Web pages. The graph of the Web is composed
of E as set of nodes, and contains an arc (x, y) if there is a hyperlink from page x to page y.
Assume that there is at least one hyperlink starting from any page. Otherwise, if a page x has
no successor, then one add an arc from x to any page.
Let P ∈RE×E be the Markov transition matrix of a simple random walk on the Web graph:
Pxy = 1/Nx if there is a hyperlink from x to y where Nx ≥1 is the number of hyperlinks from x,
and Pxy = 0 otherwise. This matrix may not be irreducible.
Google constructs the following Markov matrix:
M = γP + (1 −γ)1z
where
• 0 < γ < 1 is the damping factor: 1−γ is the probability that a Web surfer is stopping clicking
on following pages and is returning to the Google site (or any search engine) for instance or
is going to any page randomly;
• z ∈∆E is a row probability vector with positive entries (zx > 0 for all x ∈E, and z1 = 1)
giving the probability for the Web surfer of going to any page when he is stopping clicking
on following pages. This is the preference vector.
The PageRank computed by Google [EC1] is the invariant measure pM of M: that is a row
probability vector (pM ∈∆E) satisfying pM = pMM. Hence, the PageRank of a Web page x, P M
x ,
87


## Page 96

corresponds to the expected frequency of visit of this page by the state of the Markov chain. Then
the order on Web pages is deﬁned as follows: a page x is better than page y if pM
x ≥pM
y .
In this context, a Website means a subset W of E. To “optimize” his Website, the owner of W
would like to maximize a certain positive linear combination of the PageRank of W:
max
P∈P
X
x∈W
g(x)pM
x
,
(5.7)
where g ∈RW
+ , and P is a set of possible Markov matrices. To solve this problem, we shall interpret
X
x∈W
g(x)pM
x
as the value of a mean-payoﬀcriteria, and in some particular cases the optimization as a Markov
decision problem with mean-payoﬀcriteria.
5.2.3
Perron-Frobenius theorem for irreducible matrices
The elements of this section can be found in [EC4].
Recall that we denote by ≤the partial order on RE deﬁned by entrywise inequalities: v ≤w if
vx ≤wx for all x ∈E; that 1 is the column vector of RE with all its entries equal to 1: 1x = 1 for all
x ∈E; and that we denote by ∥· ∥∞the sup-norm on vectors and the associated norm on matrices.
Then, any Markov Matrix M over a ﬁnite set E satisﬁes ρ(M) = ∥M∥∞= 1 (see Lemma 2.29).
We also denote by < the relation on RE deﬁned by entrywise strict inequalities: v < w if
vx < wx for all x ∈E.
Theorem 5.11 (Perron-Frobenius theorem). Let M be a matrix over E with nonnegative entries.
Assume that M is irreducible. The following hold
1. ρ(M) is an eigenvalue associated to an eigenvector v0 ∈RE with positive entries (v0 > 0).
2. The eigenvalue ρ(M) is (geomerically) simple, meaning that if Mv = ρ(M)v, with v ∈CE,
then v = µv0 for some scalar µ ∈C.
3. Any eigenvector v ≥0 is necessarily associated to the eigenvalue ρ(M), and thus proportional
to v0.
4. If Mv ≤µv and v > 0, then µ ≥ρ(M). (Collatz-Wielandt property)
5. If µv ≤Mv with µ ≥0, v ≥0 and v̸ = 0, then µ ≤ρ(M).
6. If Mv ≤ρ(M)v with v ∈RE (or Mv ≥ρ(M)v), then Mv = ρ(M)v.
Then, any eigenvector v0 > 0 associated to the eigenvalue ρ(M) is called a Perron vector.
Before giving the proof of Perron-Frobenius theorem, let us give some remark. Denote
ρ+(M) = inf{µ > 0 | ∃v > 0, Mv ≤µv} = inf
v>0 max
x∈E
P
y∈E Mxyvy
vx
.
(5.8)
Note that this scalar is ﬁnite < +∞by the second equivalent formula. Point 4 of Perron-Frobenius
theorem 5.11 says that ρ+(M) ≥ρ(M).
Moreover, together with Point 1, it implies that the
minimum is attained in the formula of ρ+(M) and that ρ(M) = ρ+(M).
88


## Page 97

Proof of Perron-Frobenius theorem. The proof consists in several steps that are not necessarily in
the same order as the points in the theorem.
Let n be the cardinality of E and assume that
E = {1, . . . , n}.
(1) If Mv ≤µv, with v ≥0 and v̸ = 0, then v > 0 and µ > 0.
Indeed, since M ≥0 is irreducible, then (I + M)n has positive entries. If Mv ≤µv, with v ≥0 and
v̸ = 0, then µ ≥0 (applying 0 ≤[Mv]x ≤µvx to x such that vx̸ = 0), and so (I +M)nv ≤(1+µ)nv
(by using the monotonicity of M). Therefore, v > 0 and so µ > 0.
(2) Point 4 or equivalently ρ+(M) ≥ρ(M).
Indeed, let v > 0 such that Mv ≤µv. Considering the diagonal matrix D such that Dxx = vx for
all x ∈E, we get that D1 = v, so MD1 ≤µD1. Since v > 0, D is invertible and nonnegative, so
D−1MD1 ≤µ1. This implies that ∥D−1MD∥∞≤µ, by the above formula for the sup-norm, and
so ρ(M) = ρ(D−1MD) ≤µ, which shows Point 4.
(3) The inﬁnum in (5.8) is a minimum.
By deﬁnition of ρ+(M), there exists µn > ρ+(M) and vn > 0 such that limn→∞µn = ρ+(M) and
µnvn ≥Mvn. One can choose vn such that vn · 1 = 1. Then, the sequence vn is bounded and thus
admits a converging subsequence, that we also denote vn. Let v be the limit of this sequence. We
have v ≥0 and v̸ = 0 and Mv ≤ρ+(M)v. By Property (1) above, this implies that v > 0 and so
ρ+(M) is a minimum.
(4) If v is such that Mv ≤ρ+(M)v and v ≥0 then Mv = ρ+(M)v.
Denote w = ρ+(M)v −Mv.
We have w ≥0.
Assume by contradiction that w̸ = 0.
Then,
applying (I + M)n to w, we get that (I + M)nw > 0 and that (I + M)nw = ρ+(M)z −Mz, with
z = (I + M)nv > 0. Then, Mz < ρ+(M)z and so there exists µ < ρ+(M) such that Mz ≤µz,
which contradicts the deﬁnition of ρ+(M).
(5) Point 1.
By (3), there exists v > 0 such that Mv ≤ρ+(M)v. By (4), this implies that Mv = ρ+(M)v.
Hence, ρ+(M) ≤ρ(M) and since the reverse inequality holds by (2), we get that ρ+(M) = ρ(M)
and that there exists v > 0 such that Mv = ρ(M)v, which shows Point 1.
(6) Point 6.
Let v ∈RE such that Mv ≤ρ(M)v. Considering v0 as in Point 1. There exists µ ∈R such that
v ≥µv0. Take µ as large as possible so that z = v −µv0 ≥0 and there exists an entry of z equal to
zero. We have Mz ≤ρ(M)z and z ≥0 so by (1), if z̸ = 0, this implies that z > 0 a contradiction.
So z = 0, then v = µv0 and Mv = ρ(M)v.
(7) Point 2.
Let v ∈CE \ {0} be such that Mv = ρ(M)v. Taking the absolute value of the entries, we get that
ρ(M)|v| = |Mv| ≤M|v|. Then, using Point 6, we deduce that ρ(M)|v| = M|v| and so |v| = µv0
for some constant µ ≥0. We also have (1 + ρ(M))nv = (I + M)nv and so (1 + ρ(M))n|v| =
|(I + M)nv| ≤(I + M)n|v| = (1 + ρ(M))n|v|. Hence, |(I + M)nv| = (I + M)n|v|, in particular
denoting αx = (I + M)n
1x, we get | Pn
x=1 αxvx| = Pn
x=1 αx|vx|. Since all the αx are > 0, this shows
that there exists β ∈C, such that vx = β|vx|. So v = βµv0.
(8) Point 5.
Let v ≥0 such that µv ≤Mv and v̸ = 0. Then, by the monotonicity of M, we have µnv ≤Mnv.
Taking the sup-norm, we obtain that µ ≤∥Mn∥1/n
∞
for all n ≥1. Taking the limit when n goes to
inﬁnity, we deduce that µ ≤ρ(M).
(9) Point 3.
If v ≥0, v̸ = 0 is such that Mv = µv, then µ > 0 and v > 0, by (1). So by Points 4 and 5, we get
89


## Page 98

that µ = ρ(M). Point 2 or 6 implies that v is proportional to v0.
Corollary 5.12. Let M be an irreducible Markov matrix. Then 1 is the unique eigenvector as-
sociated to the eigenvalue 1, up to a scalar factor, and there exists a unique invariant probability
measure, that is a row vector m over E such that m ≥0, m1 = 1.
Proof. Since ρ(M) = 1, M1 = 1, and 1 > 0, Point 2 or 3 of Perron-Frobenius theorem 5.11 implies
that 1 is a Perron vector and any eigenvector associated to the eigenvalue 1 is proportional to 1.
Since the transpose matrix of M, denoted MT , is also nonnegative and ρ(MT ) = ρ(M), then by
Point 1 of Perron-Frobenius theorem 5.11, there exists a column vector w > 0 such that MT w = w.
Choosing w such that w · 1 = 1, we get that m = wT is an invariant probability measure of M:
m1 = 1 and mM = m. Moreover, by Point 2 or 3 of Perron-Frobenius theorem 5.11, if m and m′ are
both invariant probability measures, then since m⊤and (m′)⊤are eigenvectors of MT associated
to the eigenvalue 1, they are proportional. Then using the condition m1 = m′1 = 1, we get that
they m = m′. So the invariant probability measure of M is unique.
Deﬁnition 5.13. We say that a Markov matrix M is primitive or acyclic if there exists k ≥1 such
that Mk is positive, meaning that all its entries are positive.
Proposition 5.14. Let M be a primitive Markov matrix over E. Then 1 is the unique eigenvalue
with modulus 1.
Proof. Let λ be an eigenvalue with modulus 1 and v be an eigenvector associated to the eigenvalue
λ. For any vector w in RE, we denote by |w| the vector with entries |wx|, x ∈E. Then, |v| =
|λv| = |Mv| ≤M|v|. By Point 6 of Theorem 5.11, this implies that |v| is proportional to the
vector 1 and that |λv| = M|v|. Hence, |Mkv| = |λkv| = Mk|v| for all k ≥0. Let k be such
that Mk is positive, and let x ∈E. Then, taking the equality |Mkv| = Mk|v| at x, we get that
| P
y∈E[Mk]xyvy| = P
y∈E[Mk]xy|vy|. This implies that all the entries vy have same “sign”, that v
is proportional to |v| and so to 1. Hence, λ = 1.
5.2.4
Linear algebra techniques and the multichain case
Proposition 5.15. Let M be a Markov matrix M over the state space E. Then all its eigenvalues
of modulus 1 are semi-simple, meaning that they have no nilpotent.
Proof. Let M = QJQ−1 be the Jordan decomposition of M. Since ∥M∥∞= 1, and Jn = Q−1MnQ,
we deduce that ∥Jn∥∞≤C = ∥Q−1∥∞∥Q∥∞. If J′ is a block of J of size k corresponding to an
eigenvalue λ of modulus 1, then J′ = λI + N where I is the identity matrix, and N is the nilpotent
matrix of order k (Nk = 0) of the form N =
" 0
1
0
···
0 ... ...
···
0
1
···
0
0
#
. Then, (J′)n = Pk−1
i=0
 n
i

λn−iNi (with
N0 = I) and ∥Jn∥∞≥∥(J′)n∥∞≥
  n
k−1

−Pk−2
i=0
 n
i

. If k > 1, we get that ∥Jn∥∞tends to +∞
when n goes to inﬁnity, a contradiction. So k = 1 and the eigenvalue λ of M has no nilpotent.
Corollary 5.16. Let M be an irreducible Markov matrix. Then the eigenvalue 1 is algebraically
simple.
Proof. By Corollary 5.12, there is a unique eigenvector associated to the eigenvalue 1, so 1 is
geometrically simple. From Proposition 5.15, 1 has no nilpotent, so 1 is algebraically simple.
90


## Page 99

Proposition 5.17. Given a Markov matrix M over the state space E, and a Markov chain (Xn)n≥0
with transition matrix M and initial state X0 = x, we have
ζ±(x) = [Pr]x,
(5.9)
where P is the spectral projector of M for the eigenvalue 1, that is P is the unique matrix such that
P = P 2,
Im P = ker(I −M),
ker P = Im(I −M),
and
P = PM = MP .
This implies in particular, in the uncontrolled case, that vT
T converges towards ζ±.
Proof. Recall that ζ±(x) is the limsup or liminf of
1
T
PT
k=0[Mkr]x when T goes to inﬁnity. Let
M = QJQ−1 be the Jordan decomposition of M. Then, 1
T
PT
k=0 Mk = Q

1
T
PT
k=0 Jk
Q−1. Let
J′ be a block of J corresponding to an eigenvalue λ. If |λ| < 1, then (J′)T tends to 0 when T goes
to inﬁnity, so does the Ces`aro mean 1
T
PT
k=0 Jk. If |λ| = 1, then by Proposition 5.15, J′ is a block
of size 1 with entry λ. So
1
T
PT
k=0 Jk is a block of size 1 and entry
1
T
PT
k=0 λk. If λ̸ = 1, then
this entry is equal to (1 −λT+1)/(1 −λ)/T which tends to 0 when T goes to inﬁnity. Otherwise,
the entry is equal to 1 + 1/T which tends to 1 when T goes to inﬁnity. All together, we get that
1
T
PT
k=0 Jk tends to the diagonal matrix D with ones at the places corresponding to the blocks
of J associated to the eigenvalue 1 and 0 elsewhere. This diagonal matrix is exactly the spectral
projector of J for the eigenvalue 1. Then,
1
T
PT
k=0 Mk tends to QDQ−1, which is the spectral
projector P of M for the eigenvalue 1. Since 1 has no nilpotent, then P satisﬁes Im P = ker(I −M)
and ker P = Im(I −M).
Corollary 5.18. Let M be an irreducible Markov matrix over the state space E, let m be its unique
invariant probability measure and let (Xn)n≥0 be a Markov chain with transition matrix M and
initial state X0 = x. We have
ζ±(x) = mr,
∀x ∈E .
(5.10)
Proof. Let M = QJQ−1 be the Jordan decomposition of M. Since the eigenvalue 1 of M is simple,
the spectral projector P of M for the eigenvalue 1 is equal to QDQ−1, where D is the diagonal
matrix with 1 in some position x and 0 elsewhere. So P is the product of the column x of Q and of
the row x of Q−1, which are respectively equal to a column and row eigenvector of M with respect
to the eigenvalue 1. These vectors are equal respectively to λ1 and µm, for some λ, µ ∈C \ {0}.
Since Q−1Q = I, and m1 = 1, we get that λµ = 1. So P = 1m and the result follows.
Theorem 5.19 (Decomposition of the spectral projector using ﬁnal classes). Let M be a Markov
matrix over the state space E. For each ﬁnal class F ⊂E, there exists a unique invariant probability
measure m(F) of M with support equal to F, and a unique ﬁxed point v(F) of M (that si satisfying
Mv(F) = v(F)) such that [v(F)]x = 1 for x ∈F and [v(F)]x = 0 for x ∈F ′ and F ′ a ﬁnal class̸ = F.
Moreover, the spectral projector of M for the eigenvalue 1 is equal to:
P =
X
F ﬁnal class
v(F)m(F) .
Therefore, all invariant probability measures of M are convex combinations of the m(F), and all
ﬁxed points of M are linear combinations of the v(F). Given a Markov chain (Xn)n≥0 with transition
91


## Page 100

matrix M and initial state X0 = x, we have
ζ±(x) =
X
F ﬁnal class
(m(F)r)[v(F)]x .
(5.11)
In particular
ζ±(x) = m(F)r
∀x ∈F .
Proof. Let T be the set of transient states of M, that is the complementary of the union of ﬁnal
classes. Ordering the elements of E as x1, . . . , xn such that xi →xj for i < j, we get that the
matrix M can be written in the following block form, where F1, . . . , Fm are the ﬁnal classes:
M =


MTT
MTF1
· · ·
MTFm
0
MF1F1
0
0
0
0
...
0
0
0
0
MFmFm

.
For each ﬁnal class F ∈{F1, . . . , Fm}, MFF is an irreducible Markov matrix on the set of states F,
so that it has a unique invariant probability measure mF on F. For each ﬁnal class, consider the
row vector m(F) =

0
· · ·
0
mF
0
· · ·
0

, where mF corresponds to the restriction of m(F)
to the states in F. It is easy to see that m(F) is an invariant probability measure of M with support
equal to F. Conversely, if m is an invariant probability measure of M with support in F, then its
restriction to F is an invariant probability measure of MFF so it is equal to mF and m = m(F).
The set T is equal to the union of the classes Ti, i = 1, . . . , k, of M that are transient (that is not
ﬁnal). Then, the eigenvalues of MTT are obtained by taking all the eigenvalues of the blocks MTiTi
of MTT corresponding to the classes Ti. Since Ti is a transient class of M, we have that MTiTi1 ≤1
and MTiTi1̸ = 1.
Using the irreducibility of MTiTi and applying Point 6 of Perron-Frobenius
Theorem 5.11, we deduce that ρ(MTiTi) < 1. Then, ρ(MTT ) = maxi=1,...,k ρ(MTiTi) < 1.
Consider now the vector vF on T c = F1 ∪· · · ∪Fm with entries [vF ]x equal to 1 for x ∈F
and to 0 otherwise. Then, vF is a ﬁxed point of the restriction MT cT c of M to T c. Consider
v(F) =
(ITT −MTT )−1MTF vF
vF

, which exists and has nonnegative entries, since ρ(MTT ) < 1. We
have that Mv(F) = v(F) and that the entries [v(F)]x are equal to 1 for x ∈F and to 0 for x ∈F ′
with F ′ a ﬁnal class̸ = F. Conversely, if v satisﬁes these properties, then v = v(F). This ﬁnish the
proof of the ﬁrst assertion of the theorem.
In view of the block representation of M and of the properties that ρ(MTT ) < 1 and that
the matrices MFjFj are irreducible and Markov, we get that 1 is an eigenvalue of (geometric and
algebraic) multiplicity m of M. We have already found m left eigenvectors of M, m(Fj), j = 1, . . . , m
and m right eigenvectors of M, v(Fj), j = 1, . . . , m. Moreover, m(Fj)v(Fk) = δjk, so that one can
construct a Jordan decomposition of M, M = QJQ−1, such that the m ﬁrst diagonal entries of J
are ones, the m ﬁrst columns of Q are the eigenvectors v(Fj), j = 1, . . . , m, and the m ﬁrst rows
of Q−1 are the invariant probability measures m(Fj), j = 1, . . . , m. Then, the spectral projector is
equal to P = QDQ−1, where D contains the Jordan blocks corresponding to the eigenvalue 1 of
M, so is the diagonal matrix with its ﬁrst m diagonal entries equal to 1 and remaining ones equal
to 0. This leads to P = P
j=1,...,m v(Fj)m(Fj), that is the formula of P in the theorem. The last
assertions follow from this formula.
92


## Page 101

The following result gives a characterization of ergodicity of a Markov chain.
Corollary 5.20. Let M be a Markov matrix over the state space E. Then, M has a unique ﬁnal
class F ⊂E if and only if there exists a unique invariant probability measure m of M (that is
the associated Markov chain is ergodic). In that case, F is the support of m and 1 is the unique
ﬁxed point of M. Moreover the spectral projector of M for the eigenvalue 1 is equal to P = 1m.
Therefore, given a Markov chain (Xn)n≥0 with transition matrix M and initial state X0 = x, we
have
ζ±(x) = mr
∀x ∈E .
The previous results show that Ces`aro means of Mn converge. Using Proposition 5.14, one
shows that, in the primitive case, the following stronger property holds.
Proposition 5.21. Let M be a primitive Markov matrix, and let ρ2 be the maximum of the modulus
of the eigenvalues̸ = 1, and let k be the maximal size of the Jordan block of such an eigenvalue. We
have
Mn = 1m + O(ρn
2nk−1) .
The previous results, in particular Corollary 5.20 can be seen as a weak version of the ergodic
theorem, stating a convergence in law. The following “strong” ergodic theorem states almost sure
convergence. It can be proved using probabilistic techniques, and in particular using the law of
large numbers, whereas it generalizes the law of large numbers. We state it without proof.
Theorem 5.22 (See []). Let M and m be as in Corollary 5.20. Given a Markov chain (Xn)n≥0
with transition matrix M, and any initial law p(0), we have
lim
T→∞
(
1
T
T
X
k=0
r(Xk)
)
= mr,
almost surely.
(5.12)
5.2.5
The ergodic Kolmogorov equation
Consider ﬁrst the case where M has a unique ﬁnal (or recurrence) class. By Corollary 5.20, M has
a unique invariant probability m, the support of m is the ﬁnal class of M, and any right eigenvector
of M associated to the eigenvalue 1 is a constant vector (Mv = v =⇒v = λ1 for some λ ∈C).
This implies that ζ±(x) is independent of the initial state x ∈E, and equal to mr = P
x∈E mxr(x).
We can also characterize the value function ζ± as follows.
Proposition 5.23 (The ergodic Kolmogorov equation). Let E be a ﬁnite set, M be a Markov
transition matrix on E and r ∈RE. The following assertions hold:
1. Assume that there exists ρ ∈R and v ∈RE such that
ρ1 + v = r + Mv .
(5.13)
Then, ζ±(x) = ρ for all x ∈E.
2. Assume that M has a unique ﬁnal class, then there exists ρ ∈R and v ∈RE satisfying (5.13).
Moreover, ρ ∈R satisfying (5.13) is unique equal to mr, where m is the unique invariant
probability measure of M and v satisfying (5.13) is unique up to an additive constant, meaning
that if v, v′ satisfy (5.13), then v −v′ is a constant vector.
93


## Page 102

Proof. 1) We already know that ζ±(x) = [Pr]x, where P is the spectral projector of M for the
eigenvalue 1. Then, applying P to (5.13), we get that ρP1 + Pv = Pr + PMv and since P = PM
and P1 = 1 (1 is a right eigenvector of M), we obtain ρ1 = Pr, so ζ±(x) = ρ for all x ∈E.
2) If M has a unique ﬁnal class, then P = 1m, where m is the unique invariant probability
measure of M, and so ζ±(x) = [Pr]x = mr, for all x ∈E. Let ρ = mr, we get that m(r −ρ1) = 0
so r −ρ1 ∈ker m = ker P = Im(I −M). Hence, there exists v ∈RE such that r −ρ1 = v −Mv that
is ρ and v satisfy (5.13). Conversely, if ρ and v satisfy (5.13), then by applying m to the equation,
we get that ρ = mr so ρ is unique. Also if v, v′ satisfy (5.13), then (I −M)(v −v′) = 0 so v −v′ is
a constant vector.
Example 5.24 (Pagerank (continued)). Let us come back to Example 5.10. Recall that to “opti-
mize” his Website, the owner of W would like to maximize the criteria (5.7).
Since M is irreducible (it has positive entries, since z > 0), we get that pM is unique pM > 0,
and
X
x∈W
g(x)pM
x = pMg = ρ
where g is extended by zero on W c, ρ = ζ±(x) for all x ∈E with:
ζϵ(x) =



lim supT→∞
n
1
T E
hPT
k=0 g(Xk) | X0 = x
io
if ϵ = +
lim infT→∞
n
1
T E
hPT
k=0 g(Xk) | X0 = x
io
if ϵ = −.
and there exists v ∈RE satisfying the ergodic Kolmogorov equation:
ρ1 + v = g + Mv .
Moreover since M = γP + (1 −γ)1z, we have v = g + γPv and ρ = (1 −γ)zv.
Proposition 5.23 can be generalized as follows. The word “multichain” refers to the case of
Markov chains with multiple ﬁnal/recurrence classes.
Proposition 5.25 (The multichain Kolmogorov equation). Let E be a ﬁnite set, M be a Markov
transition matrix on E and r ∈RE, and let ζ = ζ± ∈RE be deﬁned as in (5.5) or (5.9). Then,
there exists v ∈RE such that (ζ, v) is solution to the following equations:
ζ + v = r + Mv
(5.14a)
ζ = Mζ
(5.14b)
The solution ζ of (5.14) is unique and thus equal to Pr, and v is unique up to the addition of any
element of ker(I −M) = ker(I −P). In particular, there exists a unique (ζ, v) satisfying (5.14)
together with the following condition:
mv = 0
for all invariant probability measures m of M.
(5.15)
Note that (5.15) is equivalent to the condition that Pv = 0.
94


## Page 103

5.3
The controlled case
Let us consider now the controlled problem. Our ﬁrst aim is to show a result similar to Proposi-
tion 5.23.
We assume given a stationary Markov decision process and a stationary instantaneous/running
reward/payoﬀ(at any time k), which is a map r : A →R. For all strategies σ = (σk)k≥0 in Σ or
ΣR, and initial state x ∈E, we consider the mean-payoﬀor long run time average payoﬀ/reward :
J(+,σ)(x) := J+
x (X; U) := lim sup
T→∞
(
1
T E
" T
X
k=0
r(Xk, Uk) | X0 = x
#)
,
(5.16a)
J(−,σ)(x) := J−
x (X; U) := lim inf
T→∞
(
1
T E
" T
X
k=0
r(Xk, Uk) | X0 = x
#)
,
(5.16b)
where (X, U) := (Xk, Uk)k≥0 is the process induced by σ as in Deﬁnition 3.2 or Deﬁnition 3.3.
Let B : RE →RE be the Bellman dynamic programming operator associated to undiscounted
Markov decision problem:
[B(v)](x) = sup
u∈C(x)

r(x, u) +
X
y∈E
M(u)
xy v(y)

,
for v ∈RE, and x ∈E.
For any feedback policy π ∈Π := {π : E →C | π(x) ∈C(x), ∀x ∈E}, we denote by r(π), M(π)
and B(π) the reward vector, Markov transition matrix and Kolmogorov operator of the Markov
decision problem with ﬁxed policy π:
r(π)
x
= r(x, π(x)) ,
M(π) = (M(π(x))
xy
)x,y∈E ,
B(π)(v) = r(π) + M(π)v .
5.3.1
The ergodic dynamic programming equation
Let us ﬁrst assume
(A5)
There exists ρ ∈R and v ∈RE satisfying the ergodic dynamic programming equation equa-
tion:
ρ1 + v = B(v) .
(5.17)
Theorem 5.26 (The ergodic dynamic programming equation). Under (A5), the value function of
the mean-payoﬀ(long run time average payoﬀ) Markov decision problem :
ζ±(x) := max
σ
J(±,σ)(x) ,
where the maximum is taken over either all relaxed strategies (starting at time 0), or over the
restricted sets of pure strategies, Markov strategies, feedback policies, or stationary feedback policies,
satisﬁes
ζ±(x) = ρ
∀x ∈E .
95


## Page 104

Moreover, if, for all x ∈E,
π(x) ∈Argmax
u∈C(x)

r(x, u) +
X
y∈E
M(u)
xy v(y)

,
then π is an optimal stationary policy for the MDP with mean-payoﬀ.
For the proof, we shall use the following result which computes the limit of the supremum instead
of the supremum of the limit. Let vT be the value of a ﬁnite horizon problem. From dynamic
programming equation for MDP with ﬁnite horizon (Theorem 3.13) and the stationarity of the
MDP and instantaneous reward, this is equivalent to compute recursively (forward): vT = B(vT−1)
with v0 = ϕ ∈RE.
Proposition 5.27. Assume that there exists ρ ∈R and v ∈RE satisfying the ergodic Bellman
equation (5.17). We have:
1. limT→∞1
T vT = ρ1
2. vT −ρT1 is bounded (w.r.t. T > 0).
Proof. Let ρ and v satisfy ρ1 + v = B(v), and vT satisfy vT = B(vT−1) with v0 = ϕ. Consider
also the ﬁnite horizon value wT starting from w0 = v. Since B is additively homogeneous, and
B(v) = ρ1 + v, we obtain
wT = BT (v) = Tρ1 + v .
Since B is Lipschitz continuous with constant 1 (one also says nonexpansive), we deduce:
∥wT −vT ∥∞≤∥w0 −v0∥∞= ∥v −ϕ∥∞.
So
∥vT −ρT1∥∞≤∥vT −wT ∥∞+ ∥v∥∞≤∥v −ϕ∥∞+ ∥v∥∞.
This shows Point 2, which in turn implies Point 1.
Proof of Theorem 5.26. Proof of ζ+ ≤ρ1.
Let σ be any strategy. For all ﬁnite horizon T, denote
J(T,σ)(x) = E
" T
X
k=0
r(Xk, Uk) | X0 = x
#
.
Then,
J(+,σ)(x) = lim sup
T→∞
 1
T J(T,σ)(x)

.
Let vT be the value of the MDP with ﬁnite horizon and ﬁnal reward ϕ = 0. Then,
J(T,σ)(x) ≤vT+1(x) .
Using Proposition 5.27, we get
J(+,σ)(x) = lim sup
T→∞
 1
T J(T,σ)(x)

≤lim
T→∞
 1
T vT+1(x)

= ρ .
Since this holds for all strategies, we get ζ+(x) ≤ρ, where the supremum is taken over all relaxed
strategies.
96


## Page 105

Proof of ζ−≥ρ1.
Assume ﬁrst that the maximum in the ergodic dynamic programming equation
is attained by some policy π ∈Π. Then ρ and v satisfy the ergodic Kolmogorov equation
ρ1 + v = r(π) + M(π)v = B(π)(v) .
Using Proposition 5.23, we deduce that
ρ = J(±,π)(x)
∀x ∈E .
Hence ζ−(x) ≥J(−,π)(x) = ρ for all x ∈E.
Assume now more generally that there exists π ∈Π which is ε-optimal in the r.h.s of the ergodic
dynamic programming equation. Then,
−ε1 + ρ1 + v = −ε1 + B(v) ≤r(π) + M(π)v .
Using the same technique as in the proof of Proposition 5.23, that is multiplying by the spectral
projector P (π) of M(π), we obtain:
(ρ −ε)1 + P (π)v ≤P (π)r(π) + P (π)M(π)v
then
(ρ −ε)1 ≤P (π)r(π) .
Since
[P (π)r(π)]x = lim
T→∞
(
1
T E
" T
X
k=0
r(Xk, Uk) | X0 = x
#)
= J(−,π)(x) ≤ζ−(x)
we obtain
ρ −ε ≤ζ−(x)
∀x ∈E .
Since this holds for all ε > 0, we obtain ζ−≥ρ1.
Proposition 5.27 suggests the following algorithm.
Deﬁnition 5.28. Relative value iterations consists in computing the sequence vT −vT (x0)1 for
some ﬁxed state x0.
Example 5.29. In general, vT −vT (x0)1 or vT −ρT1 does not converge when T goes to inﬁnity.
Let us show an example in the uncontrolled deterministic case. Consider the Bellman operator:
B(v) =
 1
−1

+
0
1
1
0

v
The Markov chain is a deterministic process: 1 →2 and 2 →1, and the reward satisﬁes r(1) = 1
and r(2) = −1. The invariant measure is [1/2 1/2] and so ρ = 0. Starting from v0 = ϕ = 0, we
obtain
v1 = B(v0) =
 1
−1

,
v2 = B(v1) = 0 = v0 .
So vT −ρT1 does not converge, nor vT −vT (1)1:
vT −vT (1)1 =
0
2

for T odd,
= 0 for T even.
97


## Page 106

Remark 5.30. One way to improve the method is to apply relative value iteration combined with
Krasnoselskii-Mann iterations with respect to B, that is compute wT −wT (x0)1, where
wT+1 = 1
2wT + 1
2B(wT ) .
Note that (ρ, v) satisﬁes ergodic equation if and only if
1
2ρ1 + v = BKM(v) := 1
2v + 1
2B(v) .
Moreover, if M is irreducible, then (I + M)/2 is primitive and so ((I + M)/2)n converges, see
Proposition 5.21.
5.3.2
Application to Pagerank optimization
Let us come back to Examples 5.10 and 5.24. The owner of a Web site W can choose any hyperlink
starting from any page belonging to W according to his own rules, but cannot change the hyperkinks
starting from the other Web pages.
Assume that the rules are such that any page in W can be changed independently from the other
pages, so that the set P of possible Markov matrices P is of the form:
P = {P ∈RE×E
+
| Px· ∈C(x)}
where Px· denotes the row x of P, C(x) is a subset of C := ∆E, and C(x) is a singleton when x̸ ∈W.
Considering the Markov decision process with state space E, action spaces C(x), x ∈E, and
transition probabilities:
M(u)
xy = γuy + (1 −γ)zy ,
we obtain that if π ∈Π is the policy such that π(x) = Px·, then
M(π)
xy = M(π(x))
xy
= γ[π(x)]y + (1 −γ)zy = γPxy + (1 −γ)zy = Mxy .
Conversely, if P is the matrix such that Px· = π(x), then M = M(π).
The optimization rewrites as the mean-payoﬀMarkov decision problem:
max
π∈Π J(±,π)(x′) ,
for any x′ ∈E, with
J(+,π)(x) := J+
x (X; U) := lim sup
T→∞
(
1
T E
" T
X
k=0
g(Xk) | X0 = x
#)
,
J(−,π)(x) := J−
x (X; U) := lim inf
T→∞
(
1
T E
" T
X
k=0
g(Xk) | X0 = x
#)
.
where g is extended by 0 on E \ W, Uk = π(Xk) and P(Xk+1 = y | Xx = x, Uk = u) = M(u)
xy .
An optimal stationary feedback policy for the MDP corresponds to an optimal matrix P for the
optimization problem.
98


## Page 107

Consider the associated ergodic dynamic programming equation:
ρ1 + v = B(v)
with
[B(v)]x = max
u∈C(x)


g(x) +
X
y∈E
M(u)
xy v(y)



= max
u∈C(x)


g(x) +
X
y∈E
(γuy + (1 −γ)zy)v(y)



= g(x) + γ max
u∈C(x)



X
y∈E
uyv(y)


+ (1 −γ)



X
y∈E
zyv(y)



It can be rewritten in the form:
ρ + v(x) = g(x) + γ max
u∈C(x)(u · v) + (1 −γ)z · v .
Note that since z · v is a constant, then one can solve ﬁrst:
v(x) = g(x) + γ max
u∈C(x)(u · v) ;
(5.18)
and then take
ρ = (1 −γ)z · v .
(5.18) is the dynamic programming equation of a discounted inﬁnite horizon Markov decision prob-
lem with discount factor γ, so it has a unique solution.
This yields a solution to the ergodic
equation. (5.18) can be solved, either by value iterations or by policy iterations.
Here are some examples or characteristics of the sets C(x):
• The owner of W cannot act on the pages not in W, so for x ∈E \ W, C(x) is a singleton of
∆E.
• Without any constraint on the Web pages, except that P is the transition probability matrix
of a simple random walk, C(x) is the set of uniform probabilities on nonempty subsets of E.
Note that the cardinality of C(x) is 2N where N is the cardinality of E, which lead to an
exponential complexity of the solution of the problem. To avoid this exponential complexity,
or to modelize some inequalities in hyperlinks due for instance to the order of the hyperlinks
in the web page, or to the text size and font of the hyperlinks, one may choose to relax the
problem by considering C(x) = ∆E.
• Let F be a set of forbidden pages, M a set of mandatory pages, and R the complement. Then,
C(x) is the set of uniform probabilities on subsets A of E such that M ⊂A ⊂E \ F. This
can be relaxed by considering C(x) as the set of p ∈∆E such that py ≥py0 for y ∈M and
py = 0 for y ∈F, where py0 is the uniform probability on E \ F.
• Skeleton constraints: one can consider the set of p such that py ≥(1 −µ)qy where q ∈∆E.
99


## Page 108

• Conditionnal probability constraints P(Xk+1 ∈Jx | Xk = x) ≤b is equivalent to
C(x) = {p ∈∆E |
X
j∈Jx
pj ≤b} .
• Frequency constraints P(Xk+1 ∈J | Xk ∈I) ≤b cannot be put into a local constraint of the
form C(x).
The problem can be solved analytically in the following particular examples.
• Assume that there is no hyperlink from Web pages outside W to Web pages inside W. Since
g(x) = 0 for x̸ ∈W, the solution of (5.18) satisﬁes
v(x) = γ max
u∈C(x)(u · v),
∀x ∈W c ,
where u ∈C(x) has a support in W c. This equation depends only on v|W c, and it is a ﬁxed
point equation of a contracting map. Since it has 0 has a solution, we get v|W c = 0.
The remaining equations reduce to equations for W states only:
v(x) = g(x) + γ max
u∈C(x)(
X
y∈W
uyv(y))
∀x ∈W .
• If g(x) > 0 on W, and W = {x0} is a single page, this reduces to
v(x0) = g(x0) + γ max
u∈C(x0)(ux0v(x0)) .
So v(x0) > 0 and the optimal u need to maximize ux0, that is the self hyperlink among the
possible constraints.
• If g(x) > 0 on W and C(x) = ∆E, then
v(x) = g(x) + γ max
u∈∆E
X
y∈W
(uyv(y)) .
so v = g + µ1 on W for some µ ∈R. Moreover, the maximum in u is satisﬁed for u such
that there exists λ ∈R and λy ≥0 (the Lagrange multipliers for the constraints u1 = 1 and
uy ≥0 respectively) with v(y) = λ −λy and λyuy = 0 (complementary slackness). If g takes
only diﬀerent values on W, then, u = δx0 for x0 ∈Argmax g(x).
The initial optimization problem can also be generalized as follows. Consider the optimization
problem
max
P∈P
X
x∈W
g(x, Px·)pM
x
,
where now the criteria depends also on the rows of P. For instance if g(x, u) is linear with respect
to γu + (1 −γ)z, we obtain:
max
P∈P
X
x,y∈E
gxyMxypM
x
,
100


## Page 109

and MxypM
x represents the probability to move from Web page x to Web page y, when the invariant
probability measure is applied, so in the long run.
This optimization problem rewrites as a mean-payoﬀMarkov decision problem, with instanta-
neous reward g depending on u. It can be solved by computing ρ and v solutions of the ergodic
equation:
ρ1 + v = B(v)
with
[B(v)]x = max
u∈C(x)


g(x, u) +
X
y∈E
M(u)
xy v(y)



= max
u∈C(x)


g(x, u) + γ
X
y∈E
uyv(y)


+ (1 −γ)



X
y∈E
zyv(y)


,
which can be rewritten in the form:
ρ + v(x) = max
u∈C(x)(g(x, u) + γu · v) + (1 −γ)z · v .
As above, one can solve ﬁrst:
v(x) = max
u∈C(x)(g(x, u) + γu · v) ;
(5.19)
and then take
ρ = (1 −γ)z · v .
(5.19) is the dynamic programming equation of a discounted inﬁnite horizon Markov decision prob-
lem with discount factor γ, so it has a unique solution.
This yields a solution to the ergodic
equation. Moreover, (5.19) can be solved, either by value iterations or by policy iterations.
5.3.3
Vanishing discount approach
Another way to improve relative value iterations is to replace the uniform mean in time by a
discounted mean in time.
Let us ﬁrst consider the uncontrolled case, that is consider a stationary Markov chain (Xk)k≥0
on the ﬁnite state space E, and denote by M its transition probability matrix, and by r ∈RE a
running reward vector.
The following criteria are similar to the mean-payoﬀcriteria:
ζ+(x) := J+((Xk)k≥0) = lim sup
α→1−
(
(1 −α)E
" ∞
X
k=0
αkr(Xk) | X0 = x
#)
,
ζ−(x) := J−((Xk)k≥0) = lim inf
α→1−
(
(1 −α)E
" ∞
X
k=0
αkr(Xk) | X0 = x
#)
,
which can be rewritten as
ζϵ(x) =
(
lim supα→1−

(1 −α) P∞
k=0[(αM)kr]x
	
if ϵ = +
lim infα→1−

(1 −α) P∞
k=0[(αM)kr]x
	
if ϵ = −.
(5.20)
101


## Page 110

Proposition 5.31. Given a Markov matrix M over the state space E, and a Markov chain (Xn)n≥0
with transition matrix M and initial state X0 = x, the criteria in (5.20) satisfy
ζ±(x) = [Pr]x,
where P is the spectral projector of M for the eigenvalue 1, that is P is the unique matrix such that
P = P 2,
Im P = ker(I −M),
ker P = Im(I −M),
and
P = PM = MP .
Proof. Same proof as for Proposition 5.17 for the time average criteria.
Since ζ±(x) = limα→1−(1−α)(I−αM)−1, which is related to the resolvent matrix of M, one can
even obtain the following more precise result, which implies that the map α 7→(1 −α)(I −αM)−1
is analytic around α = 1, a property which will be used later.
Theorem 5.32. Given a Markov matrix M over the state space E. We have the following asymp-
totic expansion around α = 1:
(I −αM)−1 =
1
1 −αP −
∞
X
k=0
(1 −α)k(α−1S)k+1 ,
(5.21)
where P is the spectral projector of M for the eigenvalue 1, that is P is the unique matrix such that
P = P 2,
Im P = ker(I −M),
ker P = Im(I −M),
and
P = PM = MP ,
and S satisﬁes S(M −I) = (M −I)S = I −P.
Proof. See [EC3].
Let us consider now the controlled case.
Denote by vα the value of the discounted inﬁnite
horizon problem. From dynamic programming equation for MDP with inﬁnite horizon discounted
criteria, Theorem 4.5, vα is the unique solution of the stationary equation vα = B(αvα).
Proposition 5.33. Under (A5), we have
1. limα→1−(1 −α)vα = ρ1.
2. vα −
ρ
1−α1 is bounded (w.r.t. α ∈[0, 1)).
3. For any converging subsequence of vα−
ρ
1−α1 when α goes to 1, the limit v satisﬁes the ergodic
Bellman equation (5.17).
Proof. Proof of Point 2. Denote wα = vα −
ρ
1−α1. Since vα = B(αvα), we obtain, using the
additive homogeneity of B:
wα = B(αvα) −
ρ
1 −α1
= B(αwα + α
ρ
1 −α1) −
ρ
1 −α1
= B(αwα) + α
ρ
1 −α1 −
ρ
1 −α1
= B(αwα) −ρ1 .
102


## Page 111

Substracting ergodic equation v = B(v) −ρ1, we obtain
wα −v = B(αwα) −B(v) .
Using the nonexpansivity (1-Lipschitz continuity) of B, we deduce:
∥wα −v∥∞= ∥B(αwα) −B(v)∥∞
≤∥αwα −v∥∞
≤∥αwα −αv∥∞+ ∥αv −v∥∞
≤α∥wα −v∥∞+ (1 −α)∥v∥∞.
Then,
∥wα −v∥∞≤∥v∥∞
and so
∥wα∥∞≤2∥v∥∞,
which shows Point 2.
Point 2. implies Point 1.
Proof of Point 3.
Since closed bounded sets of RE are compact, any sequence wαn with αn →1−
has a converging subsequence. Let us denote also by wαn such a converging sequence, and let w be
its limit. We have
wαn = B(αnwαn) −ρ1 .
Passing to the limit when n goes to ∞in this equation, and using the continuity of B, we obtain
w = B(w) −ρ1 ,
that is w is solution of the ergodic equation.
In the uncontrolled case, the ergodicity of the Markov chain, which is equivalent to the property
that its matrix has a unique ﬁnal class, implied a stronger property than (A5), which can be
generalized as follows in the controlled case:
(A6)
There exists ρ ∈R and v ∈RE satisfying the ergodic Bellman equation (5.17). Moreover,
ρ ∈R is unique and v is unique up to an additive constant, meaning that if v, v′ satisfy (5.17),
then v −v′ is a constant vector.
Corollary 5.34. If (A6) holds, then vα −vα(x0)1 has a limit v when α →1−and v satisﬁes (with
ρ) the ergodic Bellman equation (5.17).
Deﬁnition 5.35. A solution v of the ergodic Bellman equation (5.17) is called a bias or a relative
value function of the MDP with mean-payoﬀcriteria.
Proof of Corollary 5.34. By Proposition 5.33, wα = vα −
ρ
1−α1 is bounded w.r.t. α ∈[0, 1), and
any limit point of wα when α →1−is solution of the ergodic Bellman equation (5.17). Hence, the
diﬀerence between two values of the vector wα is also bounded, so vα −vα(x0)1 = wα −wα(x0)1
is bounded.
Moreover any limit point of a sequence vαn −vαn(x0)1, with αn →1−, is equal
103


## Page 112

to v −v(x0)1 for some solution v of the ergodic Bellman equation (5.17). Since B is additively
homogeneous, w = v −v(x0)1 is also a solution of the ergodic Bellman equation (5.17). Moreover
w satisﬁes w(x0) = 0. By (A6), such a solution w is unique, since if w, w′ satisfy (5.17) and the
condition w(x0) = 0 = w′(x0), then w −w′ is a constant vector and satisﬁes (w −w′)(x0) = 0, so
w = w′. So all limit points of vαn −vαn(x0)1 are equal to this unique solution w. This implies that
vα −vα(x0)1 converges towards w when α →1−.
However, Assumption (A6) is not needed in the case of ﬁnite action spaces.
Proposition 5.36. Under (A5), if the sets C(x) are ﬁnite, then vα −
ρ
1−α1 has a limit v when
α →1−and v satisﬁes (with ρ) the ergodic Bellman equation (5.17). Moreover, the same property
holds for vα −vα(x0)1.
Proof. Let wα = vα −
ρ
1−α1, we have wα = B(αwα)−ρ1. By the continuity of B and the uniqueness
of the solution of the previous equation, the map α ∈[0, 1) 7→wα is continuous.
Indeed, for
instance for all 0 ≤α, α′ < 1, we have ∥wα −wα′∥= ∥B(αwα) −B(αwα′)∥≤∥αwα −α′wα′∥≤
|α −α′|∥wα∥+ α′∥wα −wα′∥. So ∥wα −wα′∥≤|α−α′|
1−α′ ∥wα∥.
Since the sets C(x) are ﬁnite, for any α < 1, there exist π ∈Π such that B(αwα) = B(π)(αwα).
Therefore, wα is solution of wα = r(π) + αM(π)wα −ρ1, and is thus given by:
wα = wπ
α := (I −αM(π))−1(r(π) −ρ1) .
The map α ∈[0, 1) 7→wπ
α is rational and thus meromorphic (see Theorem 5.32). So, for any two
feedback policies π and π′, and any x ∈E, the set of zeros of the map α ∈[0, 1) 7→wπ
α(x) −wπ′
α (x)
has no accumulation point, or the map is identically zero.
Hence, there exists α0 < 1 such that for all x ∈E, and any two feedback policies π and π′,
either wπ
α(x)̸ = wπ′
α (x), for all α ∈[α0, 1), or wπ
α(x) = wπ′
α (x), for all α ∈[α0, 1).
For all α ∈[α0, 1), there exists π ∈Π such that wα = wπ
α. Moreover, wα(x) ≥wπ
α(x) for all
α ∈[0, 1), x ∈E and π ∈Π. Pick one π such that wα0 = wπ
α0. If there exists α1 ∈(α0, 1) such
that wα1̸ = wπ
α1, then there exist π′ ∈Π and x ∈E such that wα1 = wπ′
α1 and wα1(x)̸ = wπ
α1(x).
Hence wπ′
α (x)̸ = wπ
α(x), for all α ∈[α0, 1) by the previous property. Since wα(x) ≥wπ
α for all
π ∈Π, we deduce that wπ′
α (x) −wπ
α(x) is > 0 for α = α1 and ≤0 for α = α0. By the continuity of
α 7→wπ′
α (x) −wπ
α(x), this implies that there is a zero, a contradiction. Therefore, wα = wπ
α for all
α ∈[α0, 1).
The asymptotics expansion of wπ
α has the form:
wπ
α =
1
1 −αv−1 + v + O(1 −α)
for some v−1, v ∈RE. Since wπ
α = wα which is bounded, we get that the ﬁrst term is zero, and so
wα converges towards v. Passing to the limit in the equation wα = B(αwα) −ρ1, we get that v is
solution of the ergodic equation.
Since vα −vα(x0)1 = wα −wα(x0)1, we get that vα −vα(x0)1 converges towards v −v(x0)1
which is also solution of the ergodic equation.
104


## Page 113

5.3.4
An existence result
Deﬁnition 5.37 (Blackwell 62). We say that a policy π is Blackwell optimal for the MDP, if there
exists α0 < 1 such that for all α ∈[α0, 1), π is optimal for the MDP with discounted inﬁnite horizon
criteria with discount factor α, that is if vα = B(αvα) then vα = B(π)(αvα).
In the proof of Proposition 5.36, we have indeed shown the following result.
Theorem 5.38. If the sets C(x) are ﬁnite, then there exists a Blackwell optimal policy for the
MDP.
Deﬁnition 5.39. Consider a MDP with state space E, action spaces C(x) and transition probabil-
ities Mu
xy. We deﬁne the digraph of the MDP as the set of nodes E with an arc from x ∈E to y ∈E
if there exists u ∈C(x) such that Mu
xy > 0.
Theorem 5.40 (Bather, 73). Assume the graph of the MDP is strongly connected. Then, for all
reward functions r, there exists a solution (ρ, v) to the ergodic Bellman equation (5.17).
One proof relies on metric techniques: a solution is a ﬁxed point to an operator on a projective
space. We shall give another one which relies on Blackwell strategies and works when the sets C(x)
are ﬁnite.
Proof of Bather theorem, Theorem 5.40. Assume that Blackwell strategies exist. Let α0 ∈[0, 1)
and π ∈Π be such that for all α ∈[α0, 1), the value function vα solution of vα = B(αvα) satisﬁes
vα = B(π)(αvα). Therefore, vα = r(π) + αM(π)vα, and is thus given by:
vα = vπ
α := (I −αM(π))−1r(π) .
By Theorem 5.32, we have
vα =
1
1 −αv−1 + v0 + O(1 −α) ,
for some vectors v−1, v0 ∈RE.
Since the graph of the MDP is strongly connected, one can construct a Markov strategy (that is
a relaxed policy) with an irreducible associated transition matrix. Indeed, for any arc (x, y) of the
graph of the MDP, there exist u ∈C(x) such that M(u)
xy > 0. Denote by Gx a ﬁnite subset of C(x)
composed of the actions u associated to the arcs (x, y) of the MDP. Considering a policy ˜π ∈ΠR
such that ˜π(x) is the uniform probability on Gx, we get that the transition matrix of the Markov
chain Xn induced by this policy satisﬁes M(˜π)
xy =
1
card(Gx)
P
u∈Gx M(u)
xy > 0 for all arcs (x, y) of the
MDP. Then, the graph of M(˜π) coincides with the graph of the MDP, and thus M(˜π) is irreducible.
We have vα = B(αvα) ≥B(˜π)(αvα). Using the asymptotic expansion of vα, we get:
1
1 −αv−1 + v0 + O(1 −α) ≥r(˜π) + αM(˜π)(
1
1 −αv−1 + v0 + O(1 −α)) .
Taking the dominant terms, we obtain:
v−1 ≥M(˜π)v−1
105


## Page 114

which by Perron-Frobenius theorem applied to the irreducible Markov matrix M(˜π) implies that
v−1 is of the form ρ1 for some ρ ∈R (since 1 is the Perron vector of M(˜π)). Then, the asymptotic
expansion of vα has the form:
vα =
ρ
1 −α1 + v0 + O(1 −α) .
Puting this in the equation vα = B(αvα), and using that B is additively homogeneous, we get
ρ1 + v0 + O(1 −α) = B(αv0 + O(1 −α)) .
Since B is Lipschitz continuous, we deduce that ρ1+v0 = B(v0)+O(1−α) and so ρ1+v0 = B(v0),
so v0 is solution of the ergodic equation.
5.3.5
Policy iteration algorithm
Recall that the value vα of the discounted inﬁnite horizon problem is the unique solution of the
stationary dynamic programming equation vα = B(αvα) and that the policy iteration (or Howard)
algorithm to solve this equation consists in the following successive steps k ≥0, starting from a
policy π0 ∈Π (see Deﬁnition 4.11):
1. wk is the unique solution of the Kolmogorov equation associated to the policy πk:
v(x) = r(x, πk(x)) + α
X
y∈E
M(πk(x))
xy
v(y)
∀x ∈E .
2. πk+1 is an optimal policy for wk, that is an element π such that
π(x) ∈Argmax
u∈C(x)

r(x, u) + α
X
y∈E
M(u)
xy wk(y)


∀x ∈E .
which can also be rewritten in functional form :
1. wk is the solution of the equation w = B(πk)(αw).
2. πk+1 is an element π of Π such that B(π)(αwk) = B(αwk).
One may thus ask what is the limit of the algorithm when α →1−. Let us ﬁrst study the
behavior of the algorithm under the following assumption.
(A7)
Assume that all the matrices M(π), with π ∈Π, are ergodic (have a unique ﬁnal class).
In that case, we have
• for all π ∈Π, the ergodic equation
ρ1 + v = B(π)(v)
has a solution (ρπ, vπ) with ρπ ∈R and vπ ∈RE. Moreover, one may force vπ to be unique
by imposing vπ(x0) = 0, for some ﬁxed state x0 ∈E.
106


## Page 115

• Then the solution wπ
α of w = B(π)(αw) satisﬁes:
wπ
α =
1
1 −αρπ1 + µ1 + vπ + O(1 −α) ,
for some constant µ ∈R.
• With the same arguments as in the proof of Proposition 5.36, for all π the exists π′ such that
B(αwπ
α) = B(π′)(αwπ
α) for all α close to 1.
• Therefore for α close to 1, the sequence πk of PI algorithm is independent of α, and we have
wk =
1
1 −αρk1 + µk1 + vk + O(1 −α) ,
where
ρk1 + vk = B(πk)(vk),
vk(x0) = 0 .
• Since B and B(π) are additively homogeneous, we have: πk+1 is optimal for vk in B(vk).
Let us consider ﬁrst the stronger assumption:
(A8)
Assume that all the matrices M(π), with π ∈Π, are irreducible.
Deﬁnition 5.41 (Policy Iteration alogirithm (PI) for irreducible matrices). Assume (A8) holds,
and that the optimization problems in Bellman equations can be solved, that is, for all v ∈RE,
there exists π ∈Π such that B(π)(v) = B(v). The policy iteration algorithm applied to the ergodic
Bellman equation ρ1 + v = B(v) consists in the following successive steps k ≥0, starting from a
policy π0 ∈Π:
1. (ρk, vk) ∈R×RE is the unique solution of the ergodic Kolmogorov equation associated to the
policy πk:
ρ + v(x) = r(x, πk(x)) +
X
y∈E
M(πk(x))
xy
v(y)
∀x ∈E ,
satistying in addition the condition v(x0) = 0 for some ﬁxed point x0 ∈E.
2. πk+1 is an optimal policy for vk, that is an element π such that
π(x) ∈Argmax
u∈C(x)

r(x, u) +
X
y∈E
M(u)
xy vk(y)


∀x ∈E .
Fact 5.42. The policy iteration algorithm applied to the ergodic Bellman equation ρ1 + v = B(v)
consists in the following successive steps, starting from a policy π0 ∈Π: for k ≥0, do
1. ρk is the value and vk is the biais of problem when the policy is frozen to πk that is the
solution of the equation ρ1 + v = B(πk)(v) (with v(x0) = 0).
2. πk+1 is an optimal policy for vk, that is an element π of Π such that B(π)(vk) = B(vk).
107


## Page 116

Remark 5.43. Recall that for the PI for discounted problems, we proved that the sequence of values
satisﬁes
wk ≤wk+1 ≤· · · ≤v ,
and
lim
k→∞wk = v .
Since wk =
1
1−αρk1 + µk1 + vk + O(1 −α), we obtain:
ρk ≤ρk+1 · · · ≤ρ ,
and if ρk = ρk+1 then
µk1 + vk ≤µk+11 + vk+1 .
Theorem 5.44. Assume (A8) holds, and that the optimization problems in Bellman equations can
be solved, that is, for all v ∈RE, B(v) is ﬁnite and there exists π ∈Π such that B(π)(v) = B(v).
Let ρk, vk, πk be the sequence generated by PI algorithm. We have, for all k ≥0,
ρk ≤ρk+1 .
Moreover, there exists a solution (ρ, v) ∈R × RE to the ergodic equation: ρ1 + v = B(v), and we
have, for all k ≥0,
ρk ≤ρk+1 ≤· · · ≤ρ .
Proposition 5.45 (Sub or supersolutions). Let B be a monotone additively homogeneous operator
from RE to itself, beeing the Bellman operator of a undiscounted MDP. Assume that there exists
(ρ, v) ∈R × RE solution of the ergodic equation ρ1 + v = B(v). Then, for (ζ, w) ∈R × RE, we have
ζ1 + w ≤B(w) =⇒ζ ≤ρ
(5.22)
ζ1 + w ≥B(w) =⇒ζ ≥ρ .
(5.23)
Proof. From ζ1+w ≤B(w) and the monotonicity and additive homogeneity, we get that Tζ1+w ≤
BT (w) for all t ≥1.
Since BT (w) is the value function of the ﬁnite horizon problem, we obtain (from Proposi-
tion 5.27) that limT→∞1
T BT (w) = ρ.
Passing to the limit into the previous inequality, we deduce that ζ ≤ρ.
The same holds for the reverse inequality.
Proof of Theorem 5.44. Since all the M(π) are irreducible, the associated ergodic equations have a
solution. We have
ρk1 + vk = B(πk)(vk)
(5.24)
B(vk) = B(πk+1)(vk)
(5.25)
ρk+11 + vk+1 = B(πk+1)(vk+1) .
(5.26)
Using the ﬁrst and second equations together with the deﬁnition of B, we get
ρk1 + vk = B(πk)(vk) ≤B(vk) = B(πk+1)(vk) .
108


## Page 117

Hence (ρk, vk) is a subsolution of the ergodic Kolmogorov equation ρ1 + v = B(πk+1)(v).
From (5.26), (ρk+1, vk+1) is a solution of this ergodic equation.
From (5.22), we deduce that ρk ≤ρk+1.
We also have ρk1 + vk ≤B(vk), so (ρk, vk) is a subsolution of the ergodic Bellman equation.
Since the graph of the MDP contains the one of any matrix M9π), it is strongly connected. Then,
by Bather theorem, there exists a solution (ρ, v) ∈R × RE to the ergodic equation: ρ1 + v = B(v).
Moreover, applying (5.22) to B, we deduce that ρk ≤ρ, for all k ≥0.
Theorem 5.46. If in the PI algorithm for irreducible matrices, we have ρk = ρk+1, then
vk = vk+1 .
Proof. Assume that in the PI algorithm, we have ρk = ρk+1. Recall that we proved during the
proof of the ﬁrst properties:
ρk1 + vk = B(πk)(vk) ≤B(vk) = B(πk+1)(vk) .
Since ρk+11 + vk+1 = B(πk+1)(vk+1), taking the diﬀerence, we obtain
vk −vk+1 ≤M(πk+1)(vk −vk+1) .
By Perron-Frobenius theorem applied to the irreducible matrix M(πk+1), we obtain that vk−vk+1
is a constant vector.
Since in addition (vk −vk+1)(x0) = 0, we obtain vk = vk+1.
Corollary 5.47. If the sets C(x) are ﬁnite, then the PI algorithm for irreducible matrices converges
after a ﬁnite number of iterations.
Proof. If the sets C(x) are ﬁnite, the set of feedback policies, Π is ﬁnite.
Therefore, there exists k < ℓsuch that πk = πℓ.
From the uniqueness of the solution (ρ, v) to the equation B(πk)(w) = w+ρ1, with the additional
condition w(x0) = 0, we get that ρk = ρℓand vk = vℓ.
Since the sequence ρk is nondecreasing, ρk ≤ρk+1 ≤· · · ≤ρℓ, and satisﬁes ρk = ρℓ, we get the
equality ρk = ρk+1 = · · · = ρℓ.
This implies vk = vk+1 by Theorem 5.46.
Since πk+1 is optimal for vk = vk+1, and (ρk+1, vk+1) is a solution of the ergodic equation
associated to πk+1, we obtain
ρk+11 + vk+1 = B(πk+1)(vk+1) = B(πk+1)(vk) = B(vk) = B(vk+1)
and so (ρk+1, vk+1) is a solution to the ergodic Bellman equation.
Hence ρk+1 = ρ and πk+1 is optimal.
Deﬁnition 5.48 (Policy Iteration algorithm (PI) for ergodic matrices). Assume (A7) holds. The
policy iteration algorithm applied to the ergodic Bellman equation ρ1 + v = B(v) consists in the
following successive steps k ≥0, starting from a policy π0 ∈Π:
109


## Page 118

1. (ρk, vk) ∈R×RE is the unique solution of the ergodic Kolmogorov equation associated to the
policy πk:
ρ + v(x) = r(x, πk(x)) +
X
y∈E
M(πk(x))
xy
v(y)
∀x ∈E ,
satistying in addition the condition
mv = 0where m is the unique invariant probability measure of M(πk).
2. πk+1 is an optimal policy for vk, that is an element π such that
π(x) ∈Argmax
u∈C(x)

r(x, u) +
X
y∈E
M(u)
xy vk(y)


∀x ∈E ,
such that π(x) = πk(x) whenever possible (conservative policy improvement).
Theorem 5.49. Assume (A7) holds, and that the optimization problems in Bellman equations can
be solved, that is, for all v ∈RE, B(v) is ﬁnite and there exists π ∈Π such that B(π)(v) = B(v).
Let ρk, vk, πk be the sequence generated by PI algorithm. We have, for all k ≥0,
ρk ≤ρk+1 .
Moreover, if there exists a solution (ρ, v) ∈R × RE to the ergodic equation: ρ1 + v = B(v), we also
have, for all k ≥0,
ρk ≤ρk+1 ≤· · · ≤ρ .
Theorem 5.50. If in the PI algorithm for ergodic matrices, we have ρk = ρk+1, then
vk ≤vk+1 .
Corollary 5.51. If the sets C(x) are ﬁnite, then the PI algorithm for ergodic matrices converges
after a ﬁnite number of iterations.
Proof. If the sets C(x) are ﬁnite, the set of feedback policies, Π is ﬁnite.
Therefore, there exists k < ℓsuch that πk = πℓ.
From the uniqueness of the solution (ρ, v) to the equation B(πk)(w) = w+ρ1, with the additional
condition mw = 0, we get that ρk = ρℓand vk = vℓ.
Since the sequence ρk is nondecreasing, ρk ≤ρk+1 ≤· · · ≤ρℓ, and satisﬁes ρk = ρℓ, we get the
equality ρk = ρk+1 = · · · = ρℓ.
This implies vk ≤vk+1 ≤· · · vℓby Theorem 5.50 and so the equality vk = vk+1 = · · · = vℓ.
Since πk+1 is optimal for vk = vk+1, and (ρk+1, vk+1) is a solution of the ergodic equation
associated to πk+1, we obtain
ρk+11 + vk+1 = B(πk+1)(vk+1) = B(πk+1)(vk) = B(vk) = B(vk+1)
and so (ρk+1, vk+1) is a solution to the ergodic Bellman equation and πk+1 is optimal for vk+1.
Since the improvement is conservative, we get that πk+2 = πk+1.
The proof of Theorem 5.50 is based on the following lemma.
110


## Page 119

Lemma 5.52. Let M be an ergodic Markov matrix with unique ﬁnal class denoted F. Assume
v ≤Mv. Then, we have:
1. v = Mv and v = λ1 on F, for some real λ, that is v(x) = [Mv](x) and v(x) = λ for all
x ∈F.
2. If v = 0 on F, that is v(x) = 0 for all x ∈F, then v ≤0.
Proof. Denote vA and MAB the restriction of v to the set A ⊂E and of M to the rows in A and
columns in B respectively.
Proof of Point 1.
Since MFF c = 0, v ≤Mv implies vF ≤MFF vF . Applying Perron-Frobenius
theorem to the irreducible Markov matrix MFF , we deduce vF = MFF vF and vF = λ1F for some
scalar λ ∈R. So vF = MFF cvF c + MFF vF = [Mv]F .
Proof of Point 2.
If vF = 0, then vF c ≤MF cF cvF c. By the nonnegativity of MF cF c, we deduce
that vF c ≤(MF cF c)nvF c, for all n ≥1.
Since F is the unique ﬁnal class of M, then F c contains only transient states. So ρ(MF cF c) < 1
and limn→∞(MF cF c)n = 0.
Passing to the limit in vF c ≤(MF cF c)nvF c, we get vF c ≤0, and since vF = 0, we have v ≤0.
Proof of Theorem 5.50. Assume that in the PI algorithm, we have ρk = ρk+1.
Recall that we
proved during the proof of the ﬁrst properties:
ρk1 + vk = B(πk)(vk) ≤B(vk) = B(πk+1)(vk) .
Since ρk+11 + vk+1 = B(πk+1)(vk+1), taking the diﬀerence, we obtain
vk −vk+1 ≤M(πk+1)(vk −vk+1) .
Let F be the unique ﬁnal class of the ergodic matrix M(πk+1). By Point 1 of Lemma 5.52, we
obtain [vk −vk+1](x) = [M(πk+1)(vk −vk+1)](x) and (vk −vk+1)(x) = λ for all x ∈F, for some
λ ∈R.
This implies in particular that on F, we have B(vk) = B(πk+1)(vk) = B(πk+1)(vk+1) + λ1F =
ρk+11 + vk+1 + λ1F = ρk1 + vk = B(πk)(vk).
So, for all x ∈F, πk(x) was already optimal for vk, and since policy improvement is conservative,
we have πk(x) = πk+1(x).
Then, the restriction to rows in F of M(πk) and M(πk+1) are the same and since F is a ﬁnal
class of M(πk+1), it is also a ﬁnal class of M(πk).
Since the invariant measure of an ergodic matrix has a support equal to the ﬁnal class, we get
that the invariant measures of M(πk) and M(πk+1) coincide. Let us denote it by m.
Then, the constraint “mv = 0” implies that mvk = 0 and mvk+1 = 0. Since (vk −vk+1)(x) = λ
for all x ∈F, we deduce that vk −vk+1 = 0 on F.
By Point 2 of Lemma 5.52, we obtain that vk −vk+1 ≤0.
Aplying PI algorithm, we deduce:
Corollary 5.53. If (A7) holds and the sets C(x) are ﬁnite, then there exists a solution to the
ergodic Bellman equation.
111


## Page 120

This includes the case of Kolmogorov equations, but also some cases in which the graph of the
MDP is not strongly connected.
Corollary 5.54. The same holds if the sets C(x) are ﬁnite, and if instead of assuming (A7), we
assume that there exists a sequence of the PI algorithm for ergodic matrices which only meet ergodic
matrices.
Example 5.55 (A simple non strongly connected example). Consider
ρ + v(1) = max(1 + 1
2v(1) + 1
2v(2), v(2))
ρ + v(2) = 2 + v(3)
ρ + v(3) = max(v(2), v(3))
This is the ergodic dynamic programming equation of a MDP with 3 states, E = {1, 2, 3}, a
maximum of 2 actions: C(1) = C(3) = {1, 2}, C(2) = {1}, and the following transition probabilities:
M(1)
1·
=
1
2
1
2
0

M(2)
1·
=

0
1
0

M(1)
2·
=

0
0
1

M(1)
3·
=

0
1
0

M(2)
3·
=

0
0
1

Example 5.56 (An example in which conservative improvement is essential).
ρ + v(1) = v(2) + 1
ρ + v(2) = v(3) −1
ρ + v(3) = max(v(1), v(3))
This is the ergodic dynamic programming equation of a MDP with 3 states, E = {1, 2, 3}, a
maximum of 2 actions: C(1) = C(2) = {1}, C(3) = {1, 2} = C, and the following transition
probabilities:
M(1)
1·
=

0
1
0

M(1)
2·
=

0
0
1

M(1)
3·
=

1
0
0

M(2)
3·
=

0
0
1

So there exist only 2 policies π1 and π2. Indeed, these are applications from E to C such that
πi(1) = πi(2) = 1, for i = 1, 2, and π1(3) = 1 and π2(3) = 2. They thus satisfy:
M(π1) =


0
1
0
0
0
1
1
0
0

,
M(π2) =


0
1
0
0
0
1
0
0
1

,
r(π1) = r(π1) =


1
−1
0

.
112


## Page 121

Their invariant measures are
m(π1) =
1
3
1
3
1
3

,
m(π2) =

0
0
1

.
Consider policy iterations in which the condition mv = 0 is applied in value computation step,
but policy improvement may not be conservative in policy step. Starting from π0 = π1, we get
necessarily ρ0 = m(π0)r(π0) = 0 and thus v0 must satisfy v(1) = v(2) + 1, v(2) = v(3) −1,
v(3) = v(1), and m(π1)v = (v(1) + v(2) + v(3))/3 = 0, which leads to v0 =

1/3
−2/3
1/3
T .
Then, π1 and π2 are both optimal. If we choose π1 in a conservative way, then one must choose
π1 = π1, and the algorithm stops, since π1 = π0, ρ1 = ρ0 and v1 = v0. However, if we choose
π1 = π2, then ρ1 = ρ0 = 0, but v1 must satisfy v(1) = v(2) + 1, v(2) = v(3) −1, v(3) = v(3),
and m(π2)v = v(3) = 0, which leads to v1 =

0
−1
0
T = v0 −1
31, and so to the same choice of
policies for π2. If we alternate this choice at each step of the algorithm, then the algorithm never
converge.
Example 5.57 (Blackmailer). Consider a blackmailer who is blackmailing a victim each day, by
asking her a certain amount of money Ut depending on time t ∈N. At each time t ∈N, the
victim may be willing or not, but if she is not willing at some time, then she will neither be willing
anymore. We shall denote by
Xt : the state of the victim at time t, where Xt = 1 if she is willing, and Xt = 0 otherwise;
Ut : the amount of money asked by the blackmailer at time t, where we assume that Ut ≤1.
We then consider a MDP in which
• the state space is E = {0, 1}.
• the action spaces is C = [0, 1] = C(x) (note that C is inﬁnite but compact).
• the dynamics satisﬁes
M(u)
01 = P (Xt+1 = 1 | Xt = 0, Ut = u) = 0,
M(u)
00 = P (Xt+1 = 0 | Xt = 0, Ut = u) = 1 .
We shall assume that
M(u)
10 = P (Xt+1 = 0 | Xt = 1, Ut = u) = u2,
M(u)
11 = P (Xt+1 = 1 | Xt = 1, Ut = u) = 1−u2 ,
• the reward of the blackmailer at time t is equal to
r(x; u) = xu .
Consider ﬁrst the discounted inﬁnite horizon criteria with discount factor 0 < α < 1, so that the
expected payoﬀof the blackmailer that he want to maximize is
E
" ∞
X
t=0
αtr(Xt, Ut)
#
.
113


## Page 122

Let vα(x) be the value function at state x ∈E of the above MDP. Then, the Dynamic programming
equation satisﬁed by vα is:
vα(0) = αvα(0)
vα(1) = max
u∈[0,1]{u + α(u2vα(0) + (1 −u2)vα(1))} .
Hence, vα(0) = 0 and wα := vα(1) satisﬁes:
wα = max
u∈[0,1]{u + α(1 −u2)wα} = αwα +
1
4αwα
.
Therefore, the optimal control among all u > 0 is uα = 1/(2αwα) which is ≤1 if wα ≥1/(2α). In
that case
wα =
1
2
p
α(1 −α)
.
So these formula hold when α ≥1/2, and in that case an optimal stationary policy πα(1) to be
applied at each time in which the state Xt is equal to 1 is given by
πα(1) = uα =
r
1 −α
α
Therefore limα→1−wα = +∞and limα→1−((1−α)wα) = 0. This implies that the ergodic equa-
tion has no solution (otherwise, ρ = 0 and wα would have been bounded). Moreover, limα→1−πα(1) =
0, and so the optimal stationary policy in the long run would be to ask nothing.
Similarly, if we consider the maximization of the mean-payoﬀcriteria:
lim
T→∞
1
T E
"T−1
X
t=0
r(Xt; Ut) | X0 = x
#
,
then the limit of the optimal policy (at time 0) is 0.
Note that the Markov matrix associated to the policy π(1) = 0 has two ﬁnal classes, so that
the policy iteration cannot be applied apriori.
Exercise 5.3.1. Consider the blackmailer in which we restrict the action space C to be C = [ε, 1].
Show that the matrices associated to all policies are ergodic ({0} is the unique ﬁnal class), and
that policy iteration stops after a ﬁnite number of steps, although the action space is inﬁnite.
5.4
Risk sensitive control
5.4.1
Motivation
In mathematical ﬁnance, one is interested in the optimization of the total wealth or rather of the
return factor or return rate of a “portfolio”, that is
WT
W0
or
log WT
W0
.
where Wk is the total wealth at time k.
114


## Page 123

The return in one time unit can generally be written in the form:
Wk+1
Wk
= R(Xk, Uk, Dk+1)
where
Xk+1 = f(Xk, Uk, Dk+1),
for some maps R, f, where Xk is the “state” of the portfolio, for instance the proportion in each
asset (stock) or any ﬁnancial product, Uk is the action of the investor, like purchasing orders, and
Dk is the random disturbances in the parameters of the portfolio, like return rates.
When the Dk are either independent random variables or a Markov chain, the process (Yk, Uk)
with Yk = (Xk, Dk) can be seen as a Markov Decision Process.
It is stationary if (Dk)k≥0 is stationary.
Then, one may wish to maximize the expectation of any increasing function ϕ of the random
return rate in T time units:
E

ϕ(log WT
W0
)

(5.27)
and to its limit when T goes to inﬁnity.
The choice of ϕ will depend on the risk one wish to take. Examples are:
• ϕ(x) = 1
γ exp(γx), where 1 −γ ∈R is called the risk aversion parameter.
• When γ = 0, the optimization is the same as for ϕ(x) = x.
• One can replace (5.27) by considering ρ(log WT
W0 ), where ρ is a risk measure, that is a real
valued map on random variables, which is monotone and additively homogeneous (ρ(X +λ) =
ρ(X) + λ)), like expectation.
We will consider the case where ϕ(x) = 1
γ exp(γx), with γ ≥0 only, which reduces either to a
multiplicative payoﬀ(γ > 0) or an additive payoﬀ(γ = 0).
5.4.2
Risk sensitive control in ﬁnite horizon
Consider a stationary Markov chain (Dk)k≥0 with transition matrix M on the space D, and a MDP
on E × D with action spaces C(x) ⊂C and transitions given by
Xk+1 = f(Xk, Uk, Dk+1), whereYk = (Xk, Dk), ∀k ≥0 .
Consider a nonnegative map R : E × C × D →R+ and, for all strategies σ = (σk)k≥0 in Σ or ΣR,
the multiplicative payoﬀwith ﬁnite horizon T ≥1:
J(T,σ)(y) :=JT (Y ; U) := E
" T−1
Y
m=0
R(Xm, Um, Dm+1)
!
ϕ(XT ) | Y0 = y
#
,
(5.28)
where (Y, U) := (Yk, Uk)k≥0 is the process induced by σ.
Theorem 5.58. Assume that the map r is bounded from above. Let vT be the value function of
the Markov decision problem:
vT (y) := max
σ
J(T,σ)(y) , ∀y ∈E × D ,
115


## Page 124

where the maximum is taken over all relaxed strategies starting at time 0. Then, v satisﬁes the
following forward recurrence:
vT (x, d) = sup
u∈C(x)
 X
z∈D
MdzR(x, u, z)vT−1(f(x, u, z), z)
!
∀(x, d) ∈E × D .
(5.29)
with ﬁnal condition vT (x, d) = ϕ(x), for all (x, d) ∈E × D.
Assume in addition that the maximum of (5.29) is attained for an action u ∈C(x) and let us
denote by πT (x, d) this action, then the feedback policy π = (πT−k)0≤k≤T−1 is an optimal strategy
of the problem.
Sketch of proof. The proof is similar to the one of Theorem 3.20, the diﬀerences beeing:
• In Theorem 3.20, there was an additive part which is 0 here.
• In Theorem 3.20, the multiplicative reward R (which was denoted αk) depends only on the
current state Yk and not on the following state Yk+1, so it was outside the expectation. Thus,
one need to adapt the proof.
• Here the process and reward are stationary, so we replaced the backward equation by a
forward one, by considering the value as a function of the time remaining until the end.
Remark 5.59. When the Dk are independent with law p, then vT does not depend on d, and we
get:
vT (x) = sup
u∈C(x)
 X
z∈D
pzR(x, u, z)vT−1(f(x, u, z))
!
∀x ∈E .
One can rewrite (5.29) as
vT (x, d) = sup
u∈C(x)

eR(x, d, u)
X
(x′,z)∈E×D
Mu
(x,d),(x′,z)vT−1(x′, z)


∀(x, d) ∈E × D ,
with
eR(x, d, u) = E [R(x, u, Dk+1) | Dk = d] =
X
z∈D
(MdzR(x, u, z)) ,
and
Mu
(x,d),(x′,z) := MdzR(x, u, z)δx′=f(x,u,z)/ eR(x, u, d) .
Hence, the above ﬁnite horizon problem with multiplicative payoﬀis equivalent to a ﬁnite
horizon problem with (usual) multiplicative payoﬀfor a MDP on the same state space, and control
space but with transition probabilities Mu
(x,d),(x′,z) and multiplicative reward eR.
We have more.
116


## Page 125

Theorem 5.60. The above ﬁnite horizon problem with multiplicative payoﬀis equivalent to the
ﬁnite horizon problem deﬁned for a MDP on the same state space, the control space eC(x) = C(x) ×
∆E×D, and with transition probabilities M(u,θ)
yy′
= θy′ and the following additive payoﬀcriteria
eJ(T,σ)(y) :=JT (Y ; U, Θ) := E
" T−1
X
m=0
˜r(Xm, Dm, Um, θm)
!
+ eϕ(XT ) | Y0 = y
#
,
(5.30)
where σ = (σk)k≥0 is any strategy in Σ or ΣR, (Y, U, Θ) := (Yk, Uk, θk)k≥0 is the process induced
by σ, the ﬁnal reward is eϕ = log(ϕ), and
˜r(x, d, u, θ) = log eR(x, d, u) −KL(θ, M (u)
(x,d),·)
(5.31)
¿ where KL is the Kullback-Leibler distance (or entropy):
KL(θ, θ′) =
X
(x,d)∈E×D
θx,d log
 
θx,d
θ′
x,d
!
.
Proof. Take the logarithm of the dynamic programming equation rewritten with eR, and denote
˜vT (x, d) = log vT (x, d). Then, ˜vT satisﬁes the forward equation (for (x, d) ∈E × D)
˜vT (x, d) = sup
u∈C(x)

log( eR(x, d, u)) + log


X
(x′,z)∈E×D
Mu
(x,d),(x′,z)e˜vT −1(x′,z)



.
We compare this equation with the dynamic programming equation of the value wT of the
additive criteria problem, which is (for (x, d) ∈E × D)
wT (x, d) =
sup
u∈C(x),θ∈∆S×D

˜r(x, d, u, θ) +
X
(x′,z)∈E×D
Mu,θ
(x,d),(x′,z)wT−1(x′, z)

.
Both equations have the same initial condition ˜v0 = log ϕ = ˜ϕ = w0.
So one only need to show, that for all (x, d) ∈E × D and u ∈C(x), we have
log( eR(x, d, u)) + log


X
(x′,z)∈E×D
Mu
(x,d),(x′,z)e˜vT −1(x′,z)


=
sup
θ∈∆E×D

˜r(x, d, u, θ) +
X
(x′,z)∈E×D
Mu,θ
(x,d),(x′,z)wT−1(x′, z)


when ˜vT−1 = wT−1.
This follows from the following lemma.
Lemma 5.61. For any ﬁnite set E, vector v ∈RE, and probability ν ∈∆E, we have
log
 X
x′∈E
νx′ev(x′)
!
= sup
θ∈∆S
 
−KL(θ, ν) +
X
x′∈E
θx′v(x′)
!
117


## Page 126

Proof. The map ψ : v 7→log
P
x′∈E νx′ev(x′)
is convex. This follows from H¨older inequality for
the “integral” with respect to ν.
So
ψ(v) = sup
θ∈RE θ · v −ψ∗(θ)
where
ψ∗(θ) = sup
v∈RE θ · v −ψ(v)
is the Legendre-Fenchel transform of ψ. Computing ψ∗(by diﬀerentiating), we obtain that ψ∗(θ) =
KL(θ, ν) when θ ∈∆E and +∞otherwise.
Corollary 5.62. Consider the dynamic programming equation of the Kullback-Leibler additive
criteria:
wT (x, d) =
sup
u∈C(x),θ∈∆S×D

˜r(x, d, u, θ) +
X
(x′,z)∈E×D
Mu,θ
(x,d),(x′,z)wT−1(x′, z)

,
with initial condition w0 = eϕ. Then, if, for all (x, d) ∈E × D and k ≥0, there exists
πT (x, d) ∈
Argmax
u∈C(x),θ∈∆S×D

˜r(x, d, u, θ) +
X
(x′,z)∈E×D
Mu,θ
(x,d),(x′,z)wT−1(x′, z)

,
and if we denote by πT
1 (x, d) the u-coordinate of πT (x, d). Then, πT
1 is an optimal policy for the
initial MDP.
5.4.3
Risk sensitive control in inﬁnite horizon
Consider now, for the same MDP and for all strategies σ = (σk)k≥0 in Σ or ΣR, the long run time
average multiplicative payoﬀs:
J(+,σ)(y) :=J+(Y ; U) := lim sup
T→∞
 
1
T log E
"T−1
Y
m=0
R(Xm, Um, Dm+1) | Y0 = y
#!
,
(5.32)
J(−,σ)(y) :=J−(Y ; U) := lim inf
T→∞
 
1
T log E
"T−1
Y
m=0
R(Xm, Um, Dm+1) | Y0 = y
#!
,
(5.33)
where (Y, U) := (Yk, Uk)k≥0 is the process induced by σ.
Consider the Bellman operator associated to the Kullback-Leibler rewards (given in (5.31)).
118


## Page 127

This is the operator BKL on RE×D given, for all (x, d) ∈E × D, by
BKL(w)](x, d) :=
sup
u∈C(x),θ∈∆S×D

˜r(x, d, u, θ) +
X
(x′,z)∈E×D
Mu,θ
(x,d),(x′,z)wT−1(x′, z)


=
sup
u∈C(x),θ∈∆S×D

log eR(x, d, u) −KL(θ, M (u)
(x,d),·) +
X
(x′,z)∈E×D
θ(x′,z)w(x′, z)


= sup
u∈C(x)
log

eR(x, d, u)
X
(x′,z)∈E×D
M(u)
(x,d),(x′,d)ew(x′,z)


= sup
u∈C(x)
 X
z∈D
MdzR(x, u, z)ew(f(x,u,z),z)
!
.
Theorem 5.63 (The ergodic risk-sensitive dynamic programming equation). Assume that there
exists ρ ∈R and w ∈RE satisfying the ergodic risk-sensitive dynamic programming equation:
ρ1 + w = BKL(w) ,
(5.34)
with BKL as above. Then, the value function of the long run time average multiplicative Markov
decision problem :
ζ±(x) := max
σ
J(±,σ)(x) ,
where the maximum is taken over either all relaxed strategies (starting at time 0), or over the
restricted sets of pure strategies, Markov strategies, feedback policies, or stationary feedback policies,
satisﬁes
ζ±(x) = ρ
∀x ∈E .
Moreover, if, for all (x, d) ∈E × D, there exists
π(x, d) ∈
Argmax
u∈C(x),θ∈∆S×D

˜r(x, d, u, θ) +
X
(x′,z)∈E×D
θ(x′,z)w(x′, z)

,
and if we denote by π1(x, d) the u-coordinate of π(x, d). Then, π1 is an optimal policy for the long
run time average multiplicative MDP.
Note that (5.34) is equivalent to the following equation for v = ew:
eρv = sup
u∈C(x)
 X
z∈D
MdzR(x, u, z)v(f(x, u, z), z)
!
,
and that π1 can be ﬁnd directly by using:
π1(x, d) ∈Argmax
u∈C(x)
 X
z∈D
MdzR(x, u, z)v(f(x, u, z), z)
!
.
119


## Page 128

Consider now the same MDP as above and for all strategies σ = (σk)k≥0 in Σ or ΣR, the long
run risk sentive payoﬀs for 0 < γ ≤1:
J(+,γ,σ)(y) :=J+,γ(Y ; U) := lim sup
T→∞
 
1
γT log E
"T−1
Y
m=0
Rγ(Xm, Um, Dm+1) | Y0 = y
#!
,
(5.35)
J(−,γ,σ)(y) :=J−,γ(Y ; U) := lim inf
T→∞
 
1
γT log E
"T−1
Y
m=0
Rγ(Xm, Um, Dm+1) | Y0 = y
#!
,
(5.36)
where (Y, U) := (Yk, Uk)k≥0 is the process induced by σ.
The associated Bellman operator is given, for all (x, d) ∈E × D, by
Bγ(w)](x, d) :=
sup
u∈C(x),θ∈∆S×D

log eRγ(x, d, u) −1
γ KL(θ, M (γ,u)
(x,d),·) +
X
(x′,z)∈E×D
θ(x′,z)w(x′, z)


=1
γ log sup
u∈C(x)
 X
z∈D
MdzRγ(x, u, z)eγw(f(x,u,z),z)
!
.
where
eRγ(x, d, u) = (E [Rγ(x, u, Dk+1) | Dk = d])1/γ =
 X
z∈D
MdzR(x, u, z)
! 1
γ
,
and
Mγ,u
(x,d),(x′,z) := MdzRγ(x, u, z)δx′=f(x,u,z)/( eRγ(x, u, d))γ .
Corollary 5.64. Assume that there exists ργ ∈R and wγ ∈RE satisfying the ergodic risk-sensitive
dynamic programming equation:
ργ1 + wγ = Bγ(wγ) ,
(5.37)
with Bγ as above. Then, the value function of the long run risk sentive Markov decision problem :
ζ±,γ(x) := max
σ
J(±,γ,σ)(x) ,
where the maximum is taken over either all relaxed strategies (starting at time 0), or over the
restricted sets of pure strategies, Markov strategies, feedback policies, or stationary feedback policies,
satisﬁes
ζ±,γ(x) = ργ
∀x ∈E .
Moreover, if, for all (x, d) ∈E × D, there exists
π1(x, d) ∈Argmax
u∈C(x)
 X
z∈D
MdzRγ(x, u, z)eγwγ(f(x,u,z),z)
!
,
then, π1 is an optimal policy for the long run risk sentive MDP.
120


## Page 129

5.5
Problem: Machine replacement
Consider a machine which has several levels of performance depending on its use and that can
eventually be repaired/replaced. Let E = {1, . . . , n} be the set of its possible states, where i is a
better state than i + 1, meaning in particular that 1 corresponds to a machine in perfect state. For
any given state i ∈S, we denote by gi the reward obtained from the use of the machine during an
interval of time of one unit (second, minute,...), when it is in state i at the begining of this interval
of time and it is not being repaired. We assume that g1 > · · · > gn. We denote by R the cost to
repair the machine and assume that after reparation during one unit interval of time, the machine
is in state 1 at the begining of the next interval. We also assume that, when the machine is in state
i < n and is not repaired, then, after one unit of time, it stays in state i with probability 1 −pi
and becomes in state i + 1 with probability pi. Moreover, if i = n then the machine stays in state
n as long as it is not repared. Here, p1, . . . , pn are elements of the real interval (0, 1). We would
like to optimize the productivity of the machine in the long run.
To solve this problem, we consider a MDP with mean-payoﬀcriterion with for each time t ∈N,
Xt : as the state of the machine at the begining of the time interval [t, t + 1), where Xt ∈E the
state space;
Ut : as the action of the MDP at stage t, equal to 1 if we decide to repare the machine during the
time interval [t, t + 1), or 0 otherwise, so that the set of actions is C = {0, 1}, and we can take
also C(i) = C for all i (the set of actions is the same for all states of the machine).
The dynamics of the MDP is:
P(Xt+1 = j | Xt = i, Ut = u) = M(u)
i,j
with
M(1)
i,1 = 1
∀i ∈E
M(0)
i,i = 1 −pi, M(0)
i,i+1 = pi,
∀i ∈{1, . . . , n −1}
M(0)
n,n = 1
M(u)
i,j = 0
for all other cases.
The reward (gain) at any time t, given the state x ∈E and action u ∈C is
g(x; u) = gx(1 −u) −Ru .
The payoﬀof the MDP is the limit when the horizon tends to inﬁnity of the expected productivity
in one unit of time, that we try to maximize. Then, the value of the problem is
ζ(i) = sup lim sup
T→∞
1
T E
"T−1
X
t=0
g(Xt; Ut) | X0 = i
#
,
where the supremum is taken among all the feedback strategies deﬁning the process (Ut)t≥0: Ut =
πt(Xt).
Q 5.1. Write the ergodic dynamic programming equation associated to this problem.
121


## Page 130

Q 5.2. Compute the graph associated to this problem and show that the previous equation has a
solution.
Q 5.3. Can we use policy iterations to solve this equation?
Q 5.4. Let v be a bias solution of the ergodic equation, and let π be a stationary feedback control
associated to v. Show that πt = π, t = 0, . . . , T −1 is an optimal strategy for the ﬁnite horizon
problem with reward g and ﬁnal reward v. What is the interpretation of v and π?
Q 5.5. Consider the ﬁnite horizon problem with reward g, ﬁnal reward φ = 0 and horizon T = 10
and assume that 9(g1−gn) < R+gn. Show that the optimal strategy is to never repair the machine.
Explain the diﬀerence with the strategy obtained in the previous case.
Q 5.6. Show that there exists a bias v solution of the ergodic equation, such that v is nonincreasing
(that is satisfying v(x) ≥v(x + 1) for x ∈{1, . . . , n −1}).
Q 5.7. For u ∈C, denote by F (u) the Kolmogorov operator associated to the constant policy
π(i) = u, for all i ∈E:
F (0)(v)x =
(
gx + (1 −px)v(x) + pxv(x + 1)
if x < n
gn + v(n)
if x = n
F (1)(v)x = −R + v(1) .
Given any nonincreasing bias vector v, show that the optimal policy is to repare the machine when
i > i∗only, where
i∗= max{i ∈E | F (0)(v)i ≥F (1)(v)i} .
Q 5.8. Let ρ, v be a solution of the ergodic equation such that v(1) = R + ρ. Show that v(i) = 0
for i > i∗and
v(i) =R + ρ +
i−1
X
j=1
ρ −gj
pj
for i ≤min(n, i∗+ 1) .
Deduce that the bias is unique up to an additive constant.
Q 5.9. Using the nonincreasing property of v, show that ρ ≤gi∗and that gi∗+1 < ρ, when i∗< n.
Q 5.10. Let
w(i) = −gi +
i−1
X
j=1
gj −gi
pj
.
Show that w is nondecreasing.
Q 5.11. Show that w(i∗) ≤R and that R < w(i∗+ 1), when i∗< n. Conclude.
122


## Page 131

5.6
Problem: Portfolio selection with transaction cost
An investor has the choice to invest in a bank account with a ﬁxed proportional return equal to
r for each unit of time, or a risky asset (stocks) with a random proportional return equal to αk+1
between time k and time k + 1. The αk take their values in a ﬁnite subset A of (0, +∞), and are
independent and identically distributed. Transactions on the risky asset induce a proportional cost
(commission), which is the same when buying or selling and is denoted by c ∈(0, 1).
Q 6.1. Denote by wb
k the amount of money in the bank account and by wr
k the value in money
corresponding to what is already invested in the risky asset at the begining of the period of time
[k, k + 1]. Denote also by wk = wb
k + wr
k the total wealth, and by xk = wr
k
wk the proportion of wealth
already invested in the risky asset. At the begining of the period [k, k +1], the investor chooses the
(new) amount of money wr
k+ to be invested in the risky asset. Let us denote by uk ≥0 the ratio
between this amount and wk, that is uk =
wr
k+
wk . Show that the resulting amount of money in the
bank account, denoted wb
k+, satisﬁes:
wb
k+
wk
= 1 −uk −c|uk −xk| .
Give the conditions on uk so that wr
k+ and wb
k+ remain nonnegative and write these conditions in
the form uk ∈C(xk), for some subsets C(x) of R to be deﬁned.
Q 6.2. Show that, when uk ∈C(xk),
wk+1
wk
= R(xk, uk, αk+1)
and
xk+1 = f(xk, uk, αk+1),
for some maps R, f : [0, 1] × [0, 1] × R+. Deduce that (xk)k≥0 can be seen as a MDP with values in
the state space E := [0, 1], controlled by the sequence of actions (uk)k≥0 with values in the action
space C := [0, 1], and such that C(x) ⊂C is the possible action space when the state equals x.
Q 6.3. The aim of the investor is to maximize the expected return of the portfolio in the long
run. One possible measure of this return is to take the limit when T goes to inﬁnity of 1
T log

wT
w0

.
Write this problem as an ergodic control problem.
Q 6.4. Write formally the ergodic dynamic programming equation associated to this problem,
although the state space is inﬁnite (note that when the sets C(x) are replaced by ﬁnite subsets of
C(x), and x0 takes its values in a ﬁnite subset E0 of E, the random (ﬁnite) sequence (xk)0≤k≤T
remains in a ﬁnite subset ET , so that the equation can be shown using the same techniques as in
the ﬁnite state space case).
Q 6.5. Solve the equation, in the case with no transaction costs, c = 0.
Q 6.6. Assume now that the aim of the investor is to maximize the expectation of

wT
w0
γ
during a
ﬁxed period of time T, where 0 < γ ≤1 is a parameter. Write formally the dynamic programming
equation satisﬁed by the value vT
γ of the resulting MDP with ﬁnite horizon.
Q 6.7. Write the equation satisﬁed by wT = 1
γ log vT
γ . Show that wT is the value function of a new
MDP with ﬁnite horizon and enlarged action space. Which equation computes limT→∞wT /T?
Q 6.8. Solve the equation, in the case with no transaction costs, c = 0.
123


## Page 132

Additional references for this chapter
[EC1] Serguey Brin and Larry Page. The anatomy of a large-scale hypertextual web search engine.
Computer Networks and ISDN Systems, 30(1-7):107–117, 1998. Proc. 17th International
World Wide Web Conference.
[EC2] E. V. Denardo and B. L. Fox. Multichain Markov renewal programs. SIAM J. Appl. Math.,
16:468–487, 1968.
[EC3] Tosio Kato. Perturbation theory for linear operators. Classics in Mathematics. Springer-
Verlag, Berlin, 1995. Reprint of the 1980 edition.
[EC4] E. Seneta. Nonnegative matrices and Markov chains. Springer Series in Statistics. Springer-
Verlag, New York, second edition, 1981.
124


## Page 133

Chapter 6
Markov decision problems with
partial observation
6.1
Motivation
Until now, we assumed that at each time k, we (the person who decide) know the history of states
and actions until this time: Hk = (X0, U0 . . . , Xk−1, Uk−1, Xk). Then, at each time a decision is
taken using the knowledge at that time. This decision consists in choosing an action Uk which is
either a deterministic function of the history, Uk = σk(Hk) ∈Ck(Xk), or a random function of the
history, in which case Uk is a random variable with values in Ck(Xk), and σk(Hk) is its law. A
strategy is then a rule which tells the decision to take at each time, that is a sequence (σk)k≥0. The
aim is to optimize the expectation of some criteria, or its conditional expectation given the current
knowledge, and this optimization is done over all possible strategies.
Now we shall assume that we only know (that is observe or measure) at time k some of the
parameters Yk of the state Xk: Yk may be (seen as) a projection of the state Xk ∈E and possibly the
control Uk−1 ∈Ck−1 on a subset Y of E or E×C, moreover, this projection may be perturbed by noise.
We speak of partially observable Markov decision processes (POMDP), or incomplete information
1-players games. The information Ik available at time k, is now the history of observations and
actions, that is Ik = (Y0, U0 . . . , Yk−1, Uk−1, Yk).
A strategy adapted to the observations now
only depend on Ik at time k.
For instance a decision associated to a pure strategy satisﬁes:
Uk = σk(Ik) ∈Ck. Since we do not know Xk, we cannot restrict the set of actions by the condition
Uk ∈Ck(Xk).
One may however consider restrictions of the form Uk ∈Ck(Yk), or extend the
instantaneous rewards by −∞, when Uk̸ ∈Ck(Yk).
For instance, for the MDP:
Xn+1 = fn(Xn, Un, Wn+1),
n ≥0
where Xn ∈E, Un ∈Cn(Xn) and Wn ∈W, n ≥1, are independent random variables, one may only
observe:
Yn+1 = on(Xn+1, Xn, Un, W ′
n+1) ∈Y ,
where W ′
n ∈W′, n ≥1, are independent random variables, independent of the Wk, k ≥1.
The sequence (W ′
n)n≥1 is the noise on observations.
Then, one may ﬁrst ask if we can recover after some time the sequence of states X0, . . . , Xn
using an appropriate sequence of controls (Uk)k≥0. At least, we would like to compute and optimize,
125


## Page 134

given the information at time k, the expectation of
 T
X
n=k
r(Xn, Un)
!
+ ϕ(XT ) .
Example 6.1. Consider E = Z ∩[−a, a], C = {−1, 0, 1}, Y = {−1, 0, 1} and the dynamics
Xn+1 = max(min(Xn + Un, a), −a)
Yn = sgn(Xn)
with sgn(0) = 0 .
Applying the actions:
Un = −Yn
we obtain
X0 = τ := inf{n ≥0, Yn = 0}
and X0, . . . , Xn are recovered, but this does not allow one to optimize any criteria of the form:
 T
X
n=0
r(Xn, Un)
!
+ ϕ(XT ) .
Assume now that the dynamics of Yn is perturbed as in
Xn+1 = max(min(Xn + Un, a), −a)
Yn = sgn(Xn + W ′
n)
with sgn(0) = 0 ,
with W ′
n ∈W′ = {−1, 0, 1} a sequence of independent random variables. Then,
X0 = τ + 0, 1, or −1, where τ := inf{n ≥0, Yn = 0 or YnYn+1 = −1}
and X0 is only recovered up to the addition of 0, 1 or −1.
Example 6.2. Consider E = E1 × E2, with Ei ⊂R, C = R+, Y = E1 and Xn is the couple
(position,speed) of a car on a line at time n, Un is the acceleration assumed to be constant on the
interval of time [n, n + 1), and Yn is only the position at time n. Then
Xn+1 = f(Xn, Un)
Yn = [Xn]1 ,
with f((x1, x2), u) = (u/2+x2 +x1, u+x2)T . This is obtained by integration over the time interval
[n, n + 1) of the time continuous system:
˙x1 = x2
˙x2 = u
y = x1 .
126


## Page 135

Example 6.3. Consider a MDP for which one does not know the model, that is the transition
probabilities M(u)
xy , nor the instantaneous rewards r(x, u) are not known. However, one can observe
the sequence of states Xn ∈E. Assuming that transition probabilities functions (x, y, u) 7→M(u)
xy
and the reward functions r, belong to a ﬁnite set Z, one can consider the enlarged MDP with state
space E × Z and state (Xn, Zn) at time n with Zn = z, for all n ≥0, in which z is the parameter
deﬁning the transition probabilities functions θ(z) and rewards η(z), and Xn is the state process of
the MDP with transition probabilities M(u)
xy = θ(z)(x, y, u). In that case, one need at the same time
to optimize the criterion and learn the model. This is what is done in Q-learning or reinforcement
learning.
Example 6.4. Assume that E = {1, 2, . . . , N} is the set of states of a machine in which larger
means worst (N corresponds to breakdown). Also, C = {0, 1, 2} is the set of possible actions: u = 0
means that one does not test the machine and thus does not repair it, u = 1 means that one test
it but does not repair it, and u = 2 that one test it and repair it. The set of observations is
Y = {0, 1, . . . , N}, where y = 0 means that one does not test the machine and so does not know its
state, and y̸ = 0 is the state of the machine when we test it. Then one can consider the following
dynamics:
Xn+1 =
(
1
if Un = 2,
Xn + Wn
if Un ≤1
Yn =
(
min(max(Xn + W ′
n, 0), N)
if Un ≥1,
0
otherwise,
where Wn are independent random variables, taking the values 0 and 1, and W ′
n are independent
random variables, independent of the Wk, taking the values −1, 0, 1.
6.2
Partially observable Markov decision processes
Deﬁnition 6.5. A Partially Observable Markov Decision Process (POMDP) consists in the fol-
lowing parameters:
• a ﬁnite or discrete state space E;
• a ﬁnite or discrete observation space Y;
• an action space C
• for all k ∈N, the subset Ck ⊂C of all possible actions at time k;
• an initial probability p(0) ∈∆E×Y on E × Y;
• for all k ∈N, x ∈E and u ∈Ck, a probability row vector M(k,u)
x
over E × Y, the entries of
which will be denoted

M(k,u,y′)
xx′

(x′,y′)∈E×Y.
The POMDP is stationary if Ck and M(k,u)
x
do not depend on time k. In this case, the index or
argument k is omitted. It is uncontrolled if the sets Ck are singletons. In this case, the argument u
is omitted.
127


## Page 136

Formally, a POMDP allows one to construct discrete time processes (Xk)k≥0, (Yk)k≥0 and
(Uk)k≥0 taking their values in E, Y and C respectively, with transition probabilities M(k,u,y′)
xx′
:
M(k,u,y′)
xx′
= P(Xk+1 = x′, Yk+1 = y′ | Xk = x, Uk = u) ,
(6.1a)
and such that (Xk, Yk) satisﬁes the following Markov property:
P (Xk+1 = xk+1, Yk+1 = yk+1 | Xk = xk, Yk = yk, Uk = uk,
Xk−1 = xk−1, . . . , X0 = x0, Y0 = y0, U0 = u0)
= P(Xk+1 = xk+1, Yk+1 = yk+1 | Xk = xk, Uk = uk) ,
∀xi ∈E, yi ∈Y, ui ∈Ci, with i ≥0 .
(6.1b)
We thus can see (Xn, Yn)n≥0 as the process of a MDP but with the additional property that
P(Xk+1 = x′, Yk+1 = y′ | Xk = x, Yk = y, Uk = u) does not depend on y.
Deﬁnition 6.6. Given a POMDP as above, denote Ik = A0 × · · · × Ak−1 × Y, where (this time)
Ak := Y × Ck. This is the set of informations at time k.
A pure strategy for the POMDP is a sequence σ = (σk)k≥0 such that, for all k ≥0, σk, called
the strategy at time k, is a map from Ik to C satisfying
σk(ik) ∈Ck, for all ik ∈Ik .
We denote by Σ the set of all pure strategies. A pure strategy gives rise to the stochastic process
(Xk, Yk, Uk, Ik)k≥0 with transition probabilities as in (6.1), satisfying in addition
Uk = σk(Ik),
and Ik = (Y0, U0, . . . , Yk−1, Uk−1, Yk) ∈Ik ,
that is there exists a probability space (Ω, A, P) and a stochastic process (Xk, Yk, Uk, Ik)k≥0 over
this space satisfying all the above properties.
Such a sequence (Xk, Yk, Uk)k≥0 is also called an admissible sequence of states, observations,
and controls.
Deﬁnition 6.7. A random (or relaxed) strategy is a sequence σ = (σk)k≥0 such that, for all k ≥0,
σk is a map from Ik to the space of probabilities, denoted here CR, over a given probability space
(C, AC) such that the support of σk(ik) is included in Ck, for all k ≥0 and ik ∈Ik.
Such a strategy gives rise to a stochastic process (Xk, Yk, Uk, Ik)k≥0 satisfying, for all B ∈AC,
P(Uk ∈B | Ik) = [σk(Ik)](B),
and Ik = (Y0, U0, . . . , Yk−1, Uk−1, Yk) ∈Ik .
We denote by ΣR the set of all relaxed strategies.
We can also deﬁne the notions of Markovian strategies and feedback strategies.
However, since Y0, . . . , Yk may all be useful to get some information on Xk, the maximum of
any criteria over all strategies will not coincide in general with the maximum over all Markovian
strategies.
128


## Page 137

Fact 6.8. Given a POMDP as in Deﬁnition 6.5, and a pure strategy σ = (σk)k≥0 ∈Σ, the associated
stochastic process (Xk, Yk, Uk, Ik)k≥0 as in Deﬁnition 6.6 is such that (Ik)k≥0 is a Markov chain
with initial law p(Y,0):
p(Y,0)
y
=
X
x∈E
p(0)
xy .
Indeed, since the information Ik is contained in Ik+1, and the transition probabilities are:
P(Ik+1 = ik+1 | Ik = ik) = M(k,σk(ik))
ik,ik+1
where, for u ∈Ck,
M(k,u)
ik,ik+1 =
(
P(Yk+1 = yk+1 | Ik = ik, Uk = u)
if ik+1 = (ik, u, yk+1)
0
otherwise.
So (Ik, Uk) is the state-control process of a MDP with state space Ik, control space Ck at time k,
and transition probabilities M(k,u)
ik,ik+1. Similarly, when σ is only a random strategy, then (Ik, Uk)k≥0
is a Markov chain.
As for MDP, one can consider the following model of POMDP, with a given probability space.
Deﬁnition 6.9. A Partially Observable Markov Decision Process (POMDP) consists in the fol-
lowing parameters:
• a ﬁnite or discrete state space E;
• a ﬁnite or discrete observation space Y;
• an action space C;
• for all k ∈N, the subset Ck ⊂C of all possible actions at time k;
• an initial probability p(0) ∈∆E×Y on E × Y;
• a probability space (Ω, A, P), a random variable (X0, Y0) with values in E × Y and law p(0),
and two sequences of independent random variables (Wn)n≥0, (W ′
n)n≥0 with values in some
discrete spaces W and W′, independent from each other and independent from (X0, Y0);
• for all k ≥0, the dynamics of the state at time k, which is a map fk : E × Ck × W →E, and
the dynamics of the observation, which is a map ok : E × E × Ck × W′ →Y.
The POMDP is stationary if Ck, fk and ok do not depend on time k, and if the Wk and W ′
k are
identically distributed. In this case, the index or argument k is omitted. It is uncontrolled if the
sets Ck are singletons. In this case, the argument u is omitted.
Given a POMDP in the sense of Deﬁnition 6.9, and a strategy of one of the above forms, one
can construct on a probability space (extending (Ω, A)), discrete time processes (Xk)k≥0, (Yk)k≥0
and (Uk)k≥0 taking their values in E, Y and C respectively, satisfying, for all n ≥0:
Xn+1 = fn(Xn, Un, Wn+1),
Yn+1 = on(Xn+1, Xn, Un, W ′
n+1).
Moreover, one can keep the probability space (Ω, A) when the strategy is pure.
129


## Page 138

Fact 6.10. Given a POMDP in the sense of Deﬁnition 6.9, we can construct the following transition
probabilities which deﬁne a POMDP in the sense of Deﬁnition 6.5, with same behavior as the initial
POMDP:
M(k,u,y′)
xx′
= P(fk(x, u, Wk+1) = x′, ok(x′, x, u, W ′
k+1) = y′) .
Associated to a Partially Observable Markov decision process, we can consider an optimization
problem which consists in maximizing (or minimizing) a criteria equal to the expected value of a
functional of the random processes (Xk)k≥0 and (Uk)k≥0 induced by the above model among all
(relaxed) strategies depending on the information. As for fully observable processes, the criteria
can be of several types:
• Finite horizon (time) additive or multiplicative or mixed criteria.
• Inﬁnite horizon discounted (additive) criteria.
• Additive criteria with stopping time, which may be ﬁxed or to be optimized.
• Long run time average criteria.
We shall only discuss here the ﬁnite horizon additive criteria.
6.3
POMDP with additive criteria and ﬁnite horizon
Let be given a POMDP as in Deﬁnition 6.5 or Deﬁnition 6.9, and consider or denote:
• for all k ∈N, the instantaneous/running reward/payoﬀat time k, which is a map rk : E×Ck →
R;
• a ﬁnal reward, which is a map ϕ : E →R;
• for all strategies σ = (σk)k≥0 in Σ or ΣR associated to the POMDP, the total additive payoﬀ
with ﬁnite horizon T ≥1:
J(T,σ) := JT (X; U) := E
" T−1
X
k=0
rk(Xk, Uk)
!
+ ϕ(XT )
#
,
(6.2)
where (X, U) := (Xk, Uk)k≥0 is the process induced by σ as in Deﬁnition 6.6 or Deﬁnition 6.7.
• and the additive payoﬀstarting at time t with information it ∈It:
J(T,σ)
t
(it) := JT
t,it(X; U) := E
" T−1
X
k=t
rk(Xk, Uk)
!
+ ϕ(XT ) | It = it
#
.
(6.3)
Deﬁnition 6.11. A Partially Observable Markov decision problem with the above data consists
in the following optimization problem:
max
σ
J(T,σ)
where the optimization holds over either all relaxed strategies σ ∈ΣR, or all pure strategies
associated to the POMDP, that is strategies depending on the information only.
130


## Page 139

The optimum of above criteria is called the value of the problem.
An optimal solution σ is called an optimal strategy, and the corresponding process Uk an optimal
control process.
To compute the optimal strategy, we can rewrite the previous criteria as an additive criteria for
the process (In, Un)n≥0.
Denote (for any strategy σ)
˜rk(i, u) = E [rk(Xk, Uk) | Ik = i, Uk = u]
∀i ∈Ik, u ∈Ck
˜ϕ(i) = E [ϕ(XT ) | IT = i]
∀i ∈IT .
Then,
E [˜rk(Ik, Uk)] = E [rk(Xk, Uk)]
E [ ˜ϕ(IT )] = E [ϕ(XT )] .
Similarly if we consider the ﬁltration Fℓ= σa(Iℓ, Uℓ), then for all ℓ≤k ≤T, we have
E [˜rk(Ik, Uk) | Fℓ] = E [rk(Xk, Uk) | Fℓ]
E [ ˜ϕ(IT ) | Fℓ] = E [ϕ(XT ) | Fℓ] .
Fact 6.12. For all strategies σ = (σk)k≥0 in Σ or ΣR associated to the POMDP, the functionals
J(T,σ) and J(T,σ)
t
(i) correspond to the additive payoﬀof the MDP (In, Un)n≥0, with instanteneous
reward ˜rk at time k, and ﬁnal reward ˜ϕ.
Theorem 6.13 (Dynamic programming equation for POMDP with ﬁnite horizon as a function
of information). Assume that the maps ϕ, rk, k ≥0 are bounded from above. Let vk be the value
function of the information of the POMDP:
vk(ik) := max
σ
J(T,σ)
k
(ik),
∀ik ∈Ik ,
where the maximum is taken over all relaxed strategies starting at time k. Then, v satisﬁes the
following backward recurrence, called the Bellman dynamic programming equation:
vk(ik) = sup
u∈Ck

˜rk(ik, u) +
X
ik+1∈Ik+1
M(k,u)
ik,ik+1vk+1(ik+1)


∀ik ∈Ik .
(6.4)
with ﬁnal condition
vT = ˜ϕ .
Moreover, the values v obtained by optimizing over the restricted set of pure strategies coincide with
the one over the set of relaxed strategies.
Assume in addition that the maximum of (6.4) is attained for an action u ∈Ck and let us
denote by σk(ik) this action, then the pure strategy σ = (σk)0≤k≤T−1 is an optimal strategy of the
problem.
131


## Page 140

The diﬃculty with this result is that Ik evolves with time k, and that the transition probabilities
M(k,u)
ik,ik+1 and the rewards ˜rk and ˜ϕ are not so easy to compute.
For instance, if ik = (y0, u0, . . . , yk−1, uk−1, yk), and ik+1 = (ik, u, yk+1), then
M(k,u)
ik,ik+1 = P(Yk+1 = yk+1 | Ik = ik, Uk = u)
= P(Ik = ik, Uk = u, Yk+1 = yk+1)
P(Ik = ik, Uk = u)
with for ik = (y0, u0, . . . , yk−1, uk−1, yk),
P(Ik = ik, Uk = uk, Yk+1 = yk+1)
= P(Y0 = y0, U0 = u0, . . . , Uk = uk, Yk+1 = yk+1)
=
X
x0,...,xk+1
P(Y0 = y0, X0 = x0, U0 = u0, . . . , Uk = uk, Yk+1 = yk+1, Xk+1 = xk+1)
=
X
x0,...,xk+1
p(0)
x0,y0P(U0 = u0 | I0 = i0)M(0,u0,y1)
x0,x1
· · · P(Uk = uk | Ik = ik)M(k,uk,yk+1)
xk,xk+1
6.4
A suﬃcient statistics
Consider the belief process Bk ∈∆E deﬁned by
Bk(x) = P(Xk = x | Ik)
∀x ∈E .
By deﬁnition of Bk, it is a measurable function of Ik. Indeed Bk(x) = E [1Xk=x | Ik] and
Bk = bk(Ik)
with [bk(ik)](x) = P(Xk = x | Ik = ik) = E [Bk(x) | Ik = ik] ∀ik ∈Ik .
Therefore, the set of (pure or random) strategies σk which depend only on Bk is smaller than the
set of all (pure or random) strategies (which depend on Ik).
We shall show that the optimum of the criteria are the same, or equivalently that the belief pro-
cess is suﬃcient to compute the optimal strategy. This is done by proving the following properties
for Bk.
Theorem 6.14 (Dynamic programming equation for a suﬃcient statistics of the POMDP). Let
ck be (measurable) maps from Ik to some set eE. Given a strategy σ ∈ΣR, we consider the process
Ck = ck(Ik). Assume that for all k ≥0, ik ∈Ik and uk ∈Ck, P(Ck+1 = c′ | Ik = ik, Uk = uk)
depends only on ck(ik) and uk, and let us denote by f
M(k,uk)
ck(ik),c′ its value. Assume in addition that
˜rk(ik, uk) depends only on ck(ik) and uk, ˜rk(ik, uk) = eRk(ck(ik), uk), and ˜ϕT (iT ) depends only on
cT (iT ), ˜ϕ(iT ) = eΦ(cT (iT )).
Then, the process (Ck, Uk) deﬁnes a MDP with state space eE and action spaces Ck and
J(T,σ) = E
" T−1
X
k=0
eRk(Ck, Uk)
!
+ eΦ(CT )
#
.
Moreover, assume that the maps ϕ, rk, k ≥0 are bounded from above.
Then, the value of
the POMDP, that is the supremum of the previous functional over all (relaxed) strategies σ of the
132


## Page 141

POMDP, is equal to the supremum over all strategies of the form σk = σ′
k ◦ck, that is depending
on Ck only. More precisely, let wk ∈ReE satisﬁes, for all c ∈eE,
wk(c) = sup
u∈Ck

˜Rk(c, u) +
X
c′∈eE
f
M(k,u)
c,c′ wk+1(c′)

.
(6.5)
with ﬁnal condition
wT = eΦ .
Then, wk is the value function of the MDP (Ck, Uk) with the above criteria, that is, for all c ∈eE,
wk(c) = max
σ
eJ(T,σ)
k
(c) ,
where, for all 0 ≤t ≤T,
eJ(T,σ)
t
(c) := E
" T−1
X
k=t
eRk(Ck, Uk)
!
+ eΦ(CT ) | Ct = c
#
and the maximum is taken over all (relaxed) strategies for the process (Ck, Uk), starting at time k.
If vk is as in Theorem 6.13, then
vk(ik) = wk(ck(ik))
∀ik ∈Ik .
In particular v = E [v0(I0)] = E [w0(C0)] and the values v obtained by optimizing over the set of
pure or relaxed strategies for the POMDP and the restricted set of pure strategies depending only
on the Ck coincide.
If, in addition, the maximum in (6.5) is attained for an action u ∈Ck and if we denote by
σ′
k(c) this action, then the pure strategy σ = (σ′
k ◦ck)0≤k≤T−1, depending on the Ck, is an optimal
strategy of the problem.
When Ck is as above, we say that the process (Ck)k≥0 is a suﬃcient statistics of the information
process (Ik)k≥0.
Proof. Since the functionals to be maximized for the POMDP and the MDP (Ck, Uk) are the same,
it is suﬃcient to prove that the value functions obtained from the dynamic programming equations
are the same, that is to show that vk(ik) = wk(ck(ik)) for all ik ∈Ik.
Let us show this by backward induction. We have vT (iT ) = ˜ϕ(iT ) = eΦ(cT (iT )) = wT (cT (iT )).
133


## Page 142

Assume now that vk+1(ik+1) = wk+1(ck+1(ik+1)) for all ik+1 ∈Ik+1. Then, for all ik ∈Ik, we have
vk(ik) = sup
u∈Ck

˜rk(ik, u) +
X
ik+1∈Ik+1
M(k,u)
ik,ik+1vk+1(ik+1)


= sup
u∈Ck

eRk(ck(ik), u) + E [wk+1(ck+1(Ik+1)) | Ik = ik, Uk = u]

= sup
u∈Ck

eRk(ck(ik), u) +
X
c′∈eE
wk+1(c′)P(ck+1(Ik+1) = c′ | Ik = ik, Uk = u)


= sup
u∈Ck

eRk(ck(ik), u) +
X
c′∈eE
f
M(k,u)
ck(ik),c′wk+1(c′)


= wk(ck(ik))
This shows the induction and ﬁnishes the proof.
The following result shows that Bk satisﬁes at least the properties relative to the criteria in
Theorem 6.14.
Lemma 6.15. Let σ ∈Σ or ΣR be a strategy for the POMDP, and let (Xn, Yn, Un, In)n≥0 be the
process induced by σ. Let Bn be the belief process
Bn(x) = P(Xn = x | In)
∀x ∈E .
We have
˜rk(Ik, Uk) =
X
x∈E
Bk(x)rk(x, Uk) = Rk(Bk, Uk)
with Rk(b, u) = b · rk(·, u)
˜ϕ(IT ) =
X
x∈E
BT (x)ϕ(x) = Φ(BT )
with Φ(b) = b · ϕ .
Therefore
J(T,σ) = E
" T−1
X
k=0
Rk(Bk, Uk)
!
+ Φ(BT )
#
.
Proof. We have for all i ∈Ik and u ∈Ck,
˜rk(i, u) = E [rk(Xk, u) | Ik = i, Uk = u]
=
X
xk∈E
rk(xk, u)P(Xk = xk | Ik = i, Uk = u)
Then, using that Uk = σk(Ik) or has a law equal to σk(Ik) and is independent of Xk, we get
˜rk(Ik, Uk) =
X
xk∈E
rk(xk, Uk)P(Xk = xk | Ik)
=
X
xk∈E
rk(xk, Uk)Bk(xk) = Rk(Bk, Uk) .
134


## Page 143

Similarly
˜ϕ(IT ) =
X
x∈E
BT (x)ϕ(x) .
To prove that (Bk)k≥0 is a suﬃcient statistics, and thus use the DP equation of wk, it remains
to show that P(Bk+1 = b′ | Ik = ik, Uk = uk) depends only on bk(ik) and uk, and thus can be
written as f
M(k,uk)
bk(ik),b′.
6.5
The dynamics of the belief process
We ﬁrst show a formula for the transition probabilities of the information process using the belief
process.
Lemma 6.16. Let σ ∈Σ or ΣR be a strategy for the POMDP, and let (Xn, Yn, Un, In)n≥0 be
the process induced by σ. Then, the belief process (Bn)n≥0 satisﬁes Bk = bk(Ik) with bk(ik) =
E [Bk | Ik = ik] ∈∆E, for all k ≥0, so it is adapted to the ﬁltration (Fn = σa(In))n≥0. Moreover,
for all k ≥0, ik = (y0, u0, . . . , yk−1, uk−1, yk), and ik+1 = (ik, uk, yk+1), we have
M(k,uk)
ik,ik+1 =
X
xk,xk+1∈E

[bk(ik)](xk)M(k,uk,yk+1)
xk,xk+1

= bk(ik)M(k,uk,yk+1)1 .
Proof. Let k ≥0, ik = (y0, u0, . . . , yk−1, uk−1, yk), and ik+1 = (ik, uk, yk+1). We have
M(k,uk)
ik,ik+1 = P(Yk+1 = yk+1 | Ik = ik, Uk = uk)
= P(Ik = ik, Uk = uk, Yk+1 = yk+1)
P(Ik = ik, Uk = uk)
with
P(Ik = ik, Uk = uk, Yk+1 = yk+1)
=
X
xk,xk+1
P(Ik = ik, Uk = uk, Xk = xk, Yk+1 = yk+1, Xk+1 = xk+1)
=
X
xk,xk+1
P(Ik = ik, Xk = xk)P(Uk = uk | Ik = ik)M(k,uk,yk+1)
xk,xk+1
=
X
xk,xk+1
P(Ik = ik)P(Xk = xk | Ik = ik)P(Uk = uk | Ik = ik)M(k,uk,yk+1)
xk,xk+1
=
X
xk,xk+1
P(Ik = ik, Uk = uk)P(Xk = xk | Ik = ik)M(k,uk,yk+1)
xk,xk+1
Hence
M(k,u)
ik,ik+1 =
X
xk,xk+1∈E
P(Xk = xk | Ik = ik)M(k,uk,yk+1)
xk,xk+1
,
and since P(Xk = xk | Ik = ik) = E [Bk(xk) | Ik = ik] = [bk(ik)](xk), we get the result.
135


## Page 144

Corollary 6.17. We have, for all ik ∈Ik, uk ∈Ck, and b′ ∈∆E,
P(Bk+1 = b′ | Ik = ik, Uk = uk) =
X
yk+1∈Y,bk+1(ik,uk,yk+1)=b′
bk(ik)M(k,uk,yk+1)1 .
Proof. Use
P(Bk+1 = b′ | Ik = ik, Uk = uk) = P(bk+1(Ik+1) = b′ | Ik = ik, Uk = uk)
=
X
ik+1∈Ik+1, bk+1(ik+1)=b′
M(k,uk)
ik,ik+1 .
In view of previous formula, it is now suﬃcient to show that bk+1(ik, uk, yk+1) only depends on
bk(ik).
Let us ﬁrst show the property in the case with no control. In this case, M(k,y′) is the matrix
with entries M(k,y′)
xx′
, x, x′ ∈E. We shall use the notation
N(b) = 1
b1b ∈∆E,
∀b ∈RE
+ .
This is a normalization: N(λb) = N(b), for all λ ∈R+.
Proposition 6.18. If Ik = (Y0, . . . , Yk), ik = (y0, . . . , yk) and [bk(ik)](x) = P(Xk = x | Ik = ik),
then
bk+1(ik, yk+1) = N(bk(ik)M(k,yk+1))
and
b0(i0) = N(p(0)
·,i0) .
Proof. Let us ﬁx ik and denote q(k)
x
= P(Xk = x, Ik = ik), and similarly for ik+1 and q(k+1). Since
[bk(ik)](x) = P(Xk = x | Ik = ik), we get bk(ik) = N(q(k)).
We have
q(k+1)
x
=P(Xk+1 = x, Yk+1 = yk+1, Ik = ik)
=
X
x′∈E
P(Xk+1 = x, Yk+1 = yk+1, Xk = x′, Ik = ik)
=
X
x′∈E
P(Xk+1 = x, Yk+1 = yk+1 | Xk = x′)P(Xk = x′, Ik = ik)
=
X
x′∈E
M(k,yk+1)
x′x
q(k)
x′ = [q(k)M(k,yk+1)]x
Therefore q(k+1) = q(k)M(k,yk+1), hence
bk+1(ik+1) = N(q(k+1)) = N(q(k)M(k,yk+1)) ,
and since bk(ik) = N(q(k)) is proportional to q(k), we deduce bk+1(ik+1) = N(bk(ik)M(k,yk+1)).
Generalizing the previous result to the controlled case, we obtain:
Corollary 6.19. Given a strategy σ ∈Σ, with σk : Ik →Ck, for all k ≥0, we have for all k ≥0,
uk ∈Ck, y0, yk+1 ∈Y and ik ∈Ik
bk+1(ik, uk, yk+1) = N(bk(ik)M(k,uk,yk+1))
and
b0(y0) = N(p(0)
·,y0) .
Therefore the dynamics of the belief process is given by:
Bk+1 = N(BkM(k,Uk,Yk+1)) .
136


## Page 145

Note ﬁrst that the above dynamics is linear up to a normalization.
Moreover, the future
observation Yk+1 plays the role of a random perturbation of the dynamics of the state process Bk.
Corollary 6.20. For all b′ ∈∆E, we have that
P(Bk+1 = b′ | Ik = ik, Uk = uk) =
X
yk+1∈Y,N(bk(ik)M(k,uk,yk+1))=b′
bk(ik)M(k,uk,yk+1)1
depends only on bk(ik) and uk, and thus can be written as f
M(k,uk)
bk(ik),b′ with
f
M(k,u)
b,b′
=
X
y′∈Y,N(bM(k,u,y′))=b′

bM(k,u,y′)1

This shows that the belief process Bk is a suﬃcient statistics for the information process Ik.
The Dynamic programming equation associated to the belief process Bk is
wk(b) = sup
u∈Ck

Rk(b, u) +
X
b′∈∆E
f
M(k,u)
b,b′ wk+1(b′)


with ﬁnal condition
wT = Φ ,
in which
Rk(b, u) = b · rk(·, u)
Φ(b) = b · ϕ
f
M(k,u)
b,b′
=
X
y′∈Y,N(bM(k,u,y′))=b′

bM(k,u,y′)1

.
It can then be rewritten as:
wk(b) = sup
u∈Ck

b · rk(·, u) +
X
y′∈Y

(bM(k,u,y′)1)wk+1(N(bM(k,u,y′)))


.
(6.6)
So the sequence (Yk)k≥0 is like a sequence of independent random variables, such that the law of
Yk+1 depends on Bk.
Theorem 6.21 (Dynamic programming equation for the POMDP as a function of belief). Assume
that the maps ϕ, rk, k ≥0 are bounded from above. Then, the value of the POMDP is equal to the
value of the MDP for the belief process:
Bk+1 = N(BkM(k,Uk,Yk+1)) ,
starting at B0 = N(p(0)
·,Y0). If wk is solution of (6.6) with the ﬁnal condition wT (b) = b · ϕ, then
v = E [w0(B0)].
Assume in addition that the maximum in (6.6) is attained for an action u ∈Ck and let us
denote by σk(b) this action, then the pure strategy σ = (σk)0≤k≤T−1, depending on the Bk, is an
optimal strategy of the problem.
137


## Page 146

• If E, Y and Ck are ﬁnite, then the sets Ik are ﬁnite and so the set of possible values of Bk in
∆E is also ﬁnite. To be in the case of a MDP with ﬁnite state space, we still need to consider
a variable state space: take Pk be the set of possible values of Bk.
• One can show that wk is a convex function of b ∈∆E.
• One can show that wk is Lipschitz continuous with a constant less than PT−1
ℓ=k ∥rℓ∥∞+∥ϕ∥∞.
6.6
Inﬁnite horizon problems
One can generalize the above results to discounted inﬁnite horizon criteria. In that case, the belief
MDP belongs to an inﬁnite state space. However, the set of possible values of Bk can still be
restricted to a countable set, by taking the reachable set from B0.
138


## Page 147

6.7
Problem: Machine replacement with partial observation
Consider a machine which has two levels of performance: working (1) or breakdown (0). When it
is working, it can return R euros by time unit. When it is broken, it returns nothing. We do not
have access to the state of the machine, however we can choose to do some test which gives its
state. The test costs Ct euros and repairing the machine (if it is broken) costs Cr euros. We denote
Xk : the state of the machine at time k (at the begining of the time period [k, k + 1)), Xk = 0 if
the machine is broken, and Xk = 1 if it works;
Uk : the action taken at time k, Uk = 1 means that we test the machine and we repair it it is
broken. and Uk = 0 means that we do not test it;
Yk : the information we have on the state of the machine at time k −1 in case we have tested it:
Yk = Xk−1 if Uk−1 = 1 and Yk = −1 otherwise.
We assume that if the machine is working at time k, it will still work at time k +1 with probability
p, and it will be broken at time k + 1 with probability 1 −p.
6.7.1
The corresponding POMDP
Q 7.1. Construct a MDP satisfying the above properties for Xk with Uk equal to the decision to
repair or not: give the transition probabilities.
Q 7.2. Construct a POMDP satisfying the above properties, with Yk as the observation, and Uk
as the action. Show that (Xk, Yk) is the sequence of states of a MDP, the transition probabilities
of which do not depend on past of observations Yk. Determine the transition probabilities:
M(u,y′)
xx′
:= P(Xk+1 = x′, Yk+1 = y′|Xk = x, Yk = y, Uk = u) .
Q 7.3. The aim is to maximize the sum of the rewards during a period of T time units. Write this
problem as a POMDP with ﬁnite horizon. Precise the parameters of the problem.
Q 7.4. Write the dynamic programming equation satisﬁed by the value function vT
k for the criteria
with ﬁnite horizon starting at time k, as a function of the law q = (q0, q1) ∈∆E of Xk given the
past information.
Q 7.5. Show that vT
k = vT−k
0
, and that vT
0 (q) = zT (q1), for some map zT : [0, 1] →R which satisﬁes
the recurrence:
zT+1 = B(zT )
with initial condition z0 = 0, where B : R[0,1] →R[0,1] satisﬁes:
[B(z)](q) = max([B(0)(z)](q), [B(1)(z)](q))
with
[B(0)(z)](q) = Rq + z(qp)
[B(1)(z)](q) = −(Ct + Cr) + (R + Cr)q + (1 −q)z(1) + qz(p) .
Gives the optimal policy πT (q) by using this equation.
139


## Page 148

6.7.2
Solving the DP equation
Q 7.6. Show that B(0), B(1) and thus B preserve the set C of convex function that are piecewise
aﬃne. Deduce that zk ∈C for all k ≥0.
Q 7.7. Show that z1 ≥z0 and deduce that zk+1 ≥zk.
Q 7.8. Let a = max(R + Cr, R/(1 −p)). Show that B preserves the set of functions v that are
piecewise diﬀerentiable with a derivative in [0, a]. Deduce that zk is a nondecreasing function, for
all k ≥0.
Q 7.9. denote ϕk+1 = B(0)(zk) −B(1)(zk). Show that ϕk+1(1) > 0 and that
ϕk+1(0) ≤max(ϕk(0), 0) .
Q 7.10. Let k∗:= min{k ≥0 | ϕk(0) ≤0}. Show that for all k ≥k∗, there exist 0 ≤sk < 1 such
that ϕk(x) > 0 ⇔x > sk. Deduce that an optimal policy can be obtained such that πk(x) = 0 for
x ≥sk and πk(x) = 1 for x < sk.
Q 7.11. Show by induction that for all k < k∗, zk and ϕk+1 are aﬃnes, and that ϕk+1 is positive
on all [0, 1]. Deduce that the threshold sk = 0 is possible for k ≤k∗.
140


## Page 149

Chapter 7
Constrained Markov decision
processes and Linear programming
formulation of Dynamic programming
7.1
Motivation
Example 7.1 (Dam optimization). Consider the management of a hydroelectric dam subject to a
tourist constraint: one optimizes the revenue of the electrical production with the constraint that
the dam has a minimal level with a given tolerance level in probability. Such a problem is often
called a chance constrained control/optimization problem.
For instance, let b ∈(0, 1) be the probability level, T be a subset of {0, 1, . . . , T −1} representing
the tourist season, and ψ(x) be the dam level. The dam optimization can be as follows:
max E
" T−1
X
k=0
r(Xk, Uk)
!
+ ϕ(XT )
#
under the constraint P(ψ(Xk) ≥a, ∀k ∈T ) ≥b
and Xk+1 = fk(Xk, Uk, Wk) .
with (Wk)k≥0 a sequence of independent random variables.
Since P(X ≥a) = E [1X≥a], we can rewrite the constraint as a constraint on a functional of
the same type as the one to be optimized (although it contains only a ﬁnal reward):
P(ψ(Xk) ≥a, ∀k ∈T ) = E [ZT ]
where Z0 = 1 and for all k ≥0,
Zk+1 =
(
Zk
if ψ(Xk) ≥a or k̸ ∈T
0
otherwise.
Then, taking (Xk, Zk) as the new state at time k, we obtain a constrained MDP with ﬁnite horizon
additive crirerion and constraints.
141


## Page 150

Example 7.2 (Pagerank Optimization). Consider the pagerank optimization:
max
P∈P
X
x∈W
g(x)pM
x
,
in which
• E is the set of Web pages;
• W ⊂E is the web site to be optimized;
• P is a set of possible E ×E Markov matrices, like Markov transition matrices of simple random
walks on the possible Web graphs;
• M = γP + (1 −γ)1z, where 0 < γ < 1 is the damping factor;
• g ∈RW
+ is a vector of weights.
When P is local, meaning that
P = {P ∈RE×E
+
| Px· ∈C(x)} ,
we can reduce this problem to a long run time average payoﬀproblem for a MDP, see Section 5.3.2.
However, frequency constraints such as
P(Xk+1 ∈J | Xk ∈I) ≤b
(7.1)
with b ∈(0, 1) cannot be put into a local constraint of the form C(x).
We have
P(Xk+1 ∈J | Xk ∈I) =
P
x∈I, y∈J P(Xk = x, Xk+1 = y)
P
x∈I, y∈E P(Xk = x, Xk+1 = y) =
P
x∈I, y∈J pM
x Mxy
P
x∈I, y∈E pM
x Mxy
.
The frequency constraint (7.1) is then equivalent to
X
x∈I, y∈J
pM
x Mxy ≤b
X
x∈I, y∈E
pM
x Mxy .
and so can be put in the form:
X
x∈E, y∈E
h(x, y)pM
x Mxy ≤0
with
h(x, y) =





1 −b
if x ∈I, y ∈J
−b
if x ∈I, y ∈E \ J
0
otherwise (x ∈E \ I).
Since M = γP + (1 −γ)1z, and the row x of P, Px·, is the action π(x) choosen in state x, we
can consider
˜h(x, u) =
X
y∈E
(h(x, y)(γuy + (1 −γ)zy)) .
142


## Page 151

Then, the constraint is equivalent to the following constraint on the policy π:
X
x∈E

˜h(x, π(x))p(π)
x

≤0
which is equivalent to
G(±,π)(x) := lim
T→∞
(
1
T E
" T
X
k=0
h(Xk, Uk) | X0 = x
#)
≤0.
We then obtain a constrained MDP with long run time average payoﬀand constraints.
7.2
Constrained MDP with ﬁnite horizon
Let be given a Markov decision process as in Deﬁnition 3.1, that is the following parameters:
• a ﬁnite or discrete state space E;
• an action space C
• for all k ∈N and x ∈E, the subset Ck(x) ⊂C of all possible actions at time k, when the state
is equal to x;
• for all k ∈N, the set Ak := {(x, u) | x ∈E, u ∈Ck(x)} of all possibles couples (state, action)
at time k;
• an initial probability p(0) ∈∆E on E, or an initial state x0 ∈E, which is equivalent to the
case where p(0) is the Dirac measure at x0;
• for all k ∈N, x ∈E and u ∈Ck(x), a probability row vector M(k,u)
x
over E, the entries of
which will be denoted

M(k,u)
xy

y∈E.
One can alternatively consider a MDP in the sense of Deﬁnition 3.8. Consider several instantaneous
and ﬁnal rewards: some will be used in the functional to be optimized, the other ones will be used
in the constraint functionals:
• for all k ∈N, the instantaneous rewards at time k, are maps rk and gℓ
k, 1 ≤ℓ≤L, Ak →R;
• the ﬁnal rewards are maps ϕ, and ψℓ, 1 ≤ℓ≤L, E →R;
For all strategies σ = (σk)k≥0 in Σ or ΣR (or Π or ΠR), consider the total additive payoﬀs with
ﬁnite horizon T ≥1:
J(T,σ) := JT (X; U) := E
" T−1
X
k=0
rk(Xk, Uk)
!
+ ϕ(XT )
#
(7.2a)
G(ℓ,T,σ) := Jℓ,T (X; U) := E
" T−1
X
k=0
gℓ
k(Xk, Uk)
!
+ ψℓ(XT )
#
,
(7.2b)
where (X, U) := (Xk, Uk)k≥0 is the process induced by σ (as in Deﬁnition 3.2 or Deﬁnition 3.3).
143


## Page 152

Deﬁnition 7.3. A constrained Markov decision problem with complete observation, and ﬁnite
horizon consists in the following optimization problem:
max
σ
J(T,σ) under the constraints G(ℓ,T,σ) ≤hℓ
∀1 ≤ℓ≤L ,
where the optimization holds over either all relaxed strategies σ ∈ΣR, or all pure strategies, or all
Markov strategies, or all feedback policies, and where hl ∈R, 1 ≤ℓ≤L, are some given thresholds.
The optimum of above criteria is called the value of the problem. An optimal solution σ is
called an optimal strategy, and the corresponding process Uk or (Xk, Uk) an optimal control process.
Contrarily to the unconstrained case we have
Fact 7.4. For a constrained MDP, the value over the set of random strategies may be diﬀerent
from the value over the set of pure strategies.
Example 7.5 (A counter-example). Consider the simplest case: T = 1, E = {1}, C = {0, 1},
ℓ= 1 (one constraint). Since T = 1, we only need one reward function r0, strategies coincide with
Markovian strategies and consist in one policy at time 0, so we shall ommit the index 0 in r0 and
g0 and denote the policy at time 0 by π. Since E = {1}, we omit the parameter x, and policies are
probabilities on C, or equivalently probability row vectors π = (π0, π1). Pure strategies correspond
to the Dirac probabilities in 0 or 1. Then
ΣR = {(π0, π1) ∈R2 | π0 + π1 = 1, π0 ∈[0, 1]},
Σ = {(0, 1), (1, 0)}.
Denote by h = h1 the threshold of the constraint, and by v(h) the value over the set of pure
strategies and vR(h) the value over the set of random strategies.
We have
vR(h) = max{r(0)π0 + r(1)π1 + ϕ | π ∈ΣR, g(0)π0 + g(1)π1 + ψ ≤h}
and
v(h) = max{r(0)π0 + r(1)π1 + ϕ | π ∈Σ, g(0)π0 + g(1)π1 + ψ ≤h} .
The ﬁrst problem is the maximization of an aﬃne function over the convex subset of ΣR satis-
fying the linear inequality constraint. The optimum is attained on extremal points of this subset.
With no constraints, the set of extremal points is Σ. In general it is not.
Choose
r(0) = 1, r(1) = 0, g(0) = 1, g(1) = 0, ϕ = ψ = 0 .
Then
vR(h) = max{π0 | π0 ∈[0, 1], π0 ≤h}
and
v(h) = max{π0 | π0 ∈{0, 1}, π0 ≤h} .
We then obtain
vR(h) =





−∞
if h < 0
no solution
h
if 0 ≤h < 1
π0 = h
1
if h ≥1
π0 = 1 .
144


## Page 153

and
v(h) =





−∞
if h < 0
no solution
0
if 0 ≤h < 1
π0 = 0
1
if h ≥1
π0 = 1 .
Hence
v(h) < vR(h)
for h ∈(0, 1) .
We already saw in this simple example that the optimization over random strategies is a Linear
Program, that is the optimization of an aﬃne functional over a subset K of vectors satisfying linear
inequality constraints. Moreover, the optimization over pure strategies corresponds to the same
criteria but on a subset of K. Then, the optimization over random strategies consists in a relaxation
or convexiﬁcation of the optimization over pure strategies.
Some attempts (see works of Chen and Blankenship [CS2]) have been done to solve a constrained
MDP over the set of pure feedback strategies, by using a dynamic programming approach, but this
is to the prize of increasing the state space with the threshold parameters hℓ, and the control space
with set of functions.
To solve a constrained MDP, over the set of random feedback or Markovian strategies, we shall
rewrite the optimization as a Linear Program on an appropriate set of vectors. Instead of a random
policy π ∈ΠR, which gives for all k and x, the probability law of Uk given Xk = x, we shall consider
the occupation measure which is the induced probability law of (Xk, Uk).
Let π = (πk)k≥0 ∈ΠR be a random Markovian strategy, and denote πk(· | x) the probability
measure πk(x). For all k ≥0, the associated Markov matrix and reward vectors at time k will be
denoted M(k,π), r(k,π), g(k,ℓ,π), for 1 ≤ℓ≤L, and are given, for x ∈E, by
r(k,π)
x
:=
Z
C
rk(x, u)πk(du | x)
g(k,ℓ,π)
x
:=
Z
C
gℓ
k(x, u)πk(du | x)
M(k,π)
xy
:=
Z
C
M(k,u)
xy
πk(du | x) .
If (X, U) := (Xk, Uk)k≥0 is the process induced by π, we get
r(k,π)
x
= E [rk(Xk, Uk) | Xk = x]
g(k,ℓ,π)
x
= E
h
gℓ
k(Xk, Uk) | Xk = x
i
M(k,π)
xy
= P(Xk+1 = y | Xk = x) .
The ﬁnal rewards ϕ(π) and ψ(ℓ,π) are deﬁned similarly. In the sequel, we shall assume that the sets
C(x) are ﬁnite, so that the above integrals are replaced by sums.
Deﬁnition 7.6. Let σ = (σk)k≥0 ∈ΣR be any random strategy, and (X, U) := (Xk, Uk)k≥0 be the
process induced by σ. The probability law of (Xk, Uk) on E × C is the occupation measure of the
process at time k. When the sets C(x) are ﬁnite, it is simply written as a map f(k,σ) on E × C, such
that
f(k,σ)(x, u) = P(Xk = x, Uk = u),
x ∈E, u ∈U .
145


## Page 154

The occupation measure fk at time k associated to a Markovian strategy π satisﬁes, for all
x ∈E, u ∈C,
f(k,π)(x, u) = πk(u | x)P(Xk = x) .
(7.3)
Then, in that case, we can recover the law of the process Xk and the strategy πk at time k from
fk by:
P(Xk = x) = p(k)(x) :=
X
u∈C
f(k,π)(x, u)
(7.4a)
πk(u | x) = f(k,π)(x, u)
p(k)(x)
.
(7.4b)
Proposition 7.7. For all policies π ∈ΠR, the occupation measure satisﬁes the constraints:
X
u′∈C
f(k+1,π)(y, u′) =
X
x∈E
X
u∈C
M(k,u)
xy
f(k,π)(x, u),
∀y ∈E, k ≥0 .
Moreover, it satisﬁes the recurrence:
f(k+1,π)(y, u′) =
X
x∈E
X
u∈C

πk+1(u′ | y)M(k,u)
xy
f(k,π)(x, u)

,
∀y ∈E, u′ ∈C ,
(7.5a)
with the constraint on the initial condition
f(0,π)(x, u′) = π0(u′ | x)
X
u∈C
f(0,π)(x, u) .
(7.5b)
Proof. Given π ∈ΠR, Xk is a Markov chain with transition probability matrix M(k,π) at time k.
So the law of Xk can be computed using Fokker-Plank equation:
P(Xk+1 = y) =
X
x∈E
P(Xk = x)M(k,π)
xy
=
X
x∈E
P(Xk = x)
 X
u∈C
M(k,u)
xy
πk(u | x)
!
Then, using (7.4a) and (7.3), we obtain
X
u∈C
f(k+1,π)(y, u) = P(Xk+1 = y) =
X
x∈E
X
u∈C
M(k,u)
xy
f(k,π)(x, u) .
We also obtain:
f(k+1,π)(y, u′) =
X
x∈E
X
u∈C

πk+1(u′ | y)M(k,u)
xy
f(k,π)(x, u)

,
which can also be obtained as the Fokker-Plank equation for the Markov chain (Xk, Uk)k≥0, since
πk+1(u′ | y)M(k,u)
xy
= P(Uk+1 = u′, Xk+1 = y | Uk = u, Xk = x) .
146


## Page 155

Proposition 7.8. Let f(k) : E × C →R+ be functions satisfying the constraints in Proposition 7.7,
that is:
X
u′∈C
f(k+1)(y, u′) =
X
x∈E
X
u∈C
M(k,u)
xy
f(k)(x, u),
∀y ∈E ,
(7.6)
together with the constraints
X
u′∈C
f(0)(x, u′) = p(0)(x),
and f(k)(x, u) = 0
∀u̸ ∈Ck(x) .
(7.7)
Let πk be deﬁned as in (7.4), that is:
πk(u | x) = f(k)(x, u)
q(k)(x) ,
with q(k)(x) :=
X
u∈C
f(k)(x, u) .
Then, π = (πk)k≥0 ∈ΠR and the process (Xk, Uk)k≥0 associated to the policy π, and the initial law
p(0), satisﬁes
f(k)(x, u) = P(Xk = x, Uk = u) .
Proof. By deﬁnition, πk(· | x) is a probability on C. Moreover, by the constraints on f(k), the
support of πk(· | x) is included in Ck(x).
Let (Xk, Uk)k≥0 be the process associated to the policy π, and f(k,π) be deﬁned as above that
is f(k,π)(x, u) = P(Xk = x, Uk = u). We need to prove that f(k) = f(k,π).
Using the constraints on the functions f(k), we deduce that they satisfy the recurrence:
f(k+1)(y, u′) =
X
x∈E
X
u∈C

πk+1(u′ | y)M(k,u)
xy
f(k)(x, u)

,
∀y ∈E, u′ ∈C ,
which is the same as the one of f(k,π), see (7.5).
Moreover f(0)(x, u) = q(0)(x)π0(u | x), and by the constraints on f(0), we get that q(0) = p(0).
Hence f(0) = f(0,π), and by induction f(k) = f(k,π), for all k ≥0.
Remark 7.9. In Proposition 7.8, we did not add the constraint that f(k) are probabilities, since this
is deduced from the constraints and the properties of p(0) and M.
Corollary 7.10. Let f(k) : E × C →R+, and πk be as in Proposition 7.8. We have
J(T,π) = eJ(T)(f),
and G(ℓ,T,π) = eG(ℓ,T)(f)
with
eJ(T)(f) :=


T−1
X
k=0
X
x∈E,u∈C
rk(x, u)f(k)(x, u)

+
X
x∈E,u∈C
ϕ(x)f(T)(x, u)
(7.8a)
eG(ℓ,T)(f) :=


T−1
X
k=0
X
x∈E,u∈C
gℓ
k(x, u)f(k)(x, u)

+
X
x∈E,u∈C
ψℓ(x)f(T)(x, u) .
(7.8b)
147


## Page 156

Theorem 7.11. The value of the constrained Markov decision problem with ﬁnite horizon over
the set of Markovian strategies is equal to the value of the following Linear Program:
max
f
eJ(T)(f) under the constraints eG(ℓ,T)(f) ≤hℓ
∀1 ≤ℓ≤L ,
where the maximization is done over the set of sequences f = (f(k))k≥0 of functions f(k) : E × C →
R+ satisfying the linear constraints (7.6) and (7.7), and eJ(T) and eG(ℓ,T) are as in (7.8).
Proof. Let ˜v be the value of the Linear Program and v be the value of the constrained Markov
decision problem with ﬁnite horizon over the set of random feedback strategies.
For any π ∈ΠR, the sequence f = (f(k,π))k≥0 of occupation measures satisﬁes all the properties
of an argument f of the Linear Program, that is the linear constraints (7.6) and (7.7), and since
eJ(T)(f) = J(T,π) and eG(ℓ,T)(f) = G(ℓ,T,π), we get that v ≤˜v.
Conversely, for any f satisfying the constraints (7.6) and (7.7), Proposition 7.8 constructs
π ∈ΠR such that f(k) = f(k,π), for all k ≥0. Then, ˜v ≤v.
Theorem 7.12. The value of the constrained Markov decision problem with ﬁnite horizon over
the set of all random strategies is equal to the value of the same problem over random Markov
strategies and thus to the value of the Linear Program:
max
f
eJ(T)(f) under the constraints eG(ℓ,T)(f) ≤hℓ
∀1 ≤ℓ≤L ,
where the maximization is done over the set of sequences f = (f(k))k≥0 of functions f(k) : E × C →
R+ satisfying the linear constraints (7.6) and (7.7), and eJ(T) and eG(ℓ,T) are as in (7.8).
This result follows from the following one.
Proposition 7.13. For all strategies σ ∈ΣR, the occupation measure f(k) = f(k,σ) satisﬁes the
linear constraints (7.6) and (7.7), and
J(T,σ) = eJ(T)(f),
and G(ℓ,T,σ) = eG(ℓ,T)(f) .
Hence, there exists π ∈ΠR such that
J(T,σ) = J(T,π),
and G(ℓ,T,σ) = G(ℓ,T,π) .
Proof. The proof in Proposition 7.7 was based on Fokker-Plank equation for Xk, but the constraint
may be derived from the Fokker-Plank equation for (Xk, Uk), as follows. Moreover, Fokker-Plank
equation holds even if (Xk, Uk) is not a Markov chain, so for the process (Xk, Uk) induced by a
general random strategy σ ∈ΣR.
Denote f(k) = f(k,σ). The Fokker-Plank equation writes
f(k+1)(y, u′) =
X
x∈E
X
u∈C
P(Uk+1 = u′, Xk+1 = y | Uk = u, Xk = x)f(k)(x, u) .
Taking the sum over u′, we obtain
X
u′∈C
f(k+1)(y, u′) =
X
x∈E
X
u∈C
P(Xk+1 = y | Uk = u, Xk = x)f(k)(x, u) ,
and since P(Xk+1 = y | Uk = u, Xk = x) = M(k,u)
xy
, we get (7.6).
The ﬁrst constraint in (7.7) follows from the fact that f(0)(x, y) = P(X0 = x, U0 = u) and the
second constraint in (7.7) is by deﬁnition of the supports of strategies.
148


## Page 157

7.3
Constrained MDP with inﬁnite horizon
Assume given a stationary Markov decision process as in Deﬁnition 3.1, that is the following
parameters:
• a ﬁnite or discrete state space E;
• an action space C;
• for all x ∈E, the subset C(x) ⊂C of all possible actions at any time k, when the state is equal
to x;
• the set A := {(x, u) | x ∈E, u ∈C(x)} of all possibles couples (state, action) (at any time k);
• an initial probability p(0) ∈∆E on E, or an initial state x0 ∈E;
• for all x ∈E and u ∈C(x), a probability row vector M(u)
x
over E, the entries of which will be
denoted (M(u)
xy )y∈E.
Consider the following (stationary) parameters:
• the instantaneous rewards (at any time k), are maps r and gℓ, 1 ≤ℓ≤L, A →R;
• a (ﬁxed) discount factor α ∈[0, 1).
For all strategies σ = (σk)k≥0 in ΣR, consider the discounted total additive payoﬀs with inﬁnite
horizon:
J(σ)
α
:= Jα(X; U) := E
" ∞
X
k=0
αkr(Xk, Uk)
#
(7.9a)
G(ℓ,σ)
α
:= Jℓ
α(X; U) := E
" ∞
X
k=0
αkgℓ(Xk, Uk)
#
,
(7.9b)
where (X, U) := (Xk, Uk)k≥0 is the process induced by σ (as in Deﬁnition 3.2 or Deﬁnition 3.3).
Proposition 7.14. For all strategies σ ∈ΣR, and all α ∈[0, 1), denote, for x ∈E and u ∈C(x),
f(σ)(x, u) =
∞
X
k=0
αkf(k,σ) .
This function satisﬁes the constraints:
X
u′∈C
f(σ)(y, u′) = p(0)(y) + α
X
x∈E
X
u∈C
M(u)
xy f(σ)(x, u),
∀y ∈E .
Moreover, if σ = π is a stationary Markovian strategy, we have:
f(π)(y, u′) = π(u′ | y)
 X
u∈C
f(π)(y, u)
!
,
∀y ∈E, u′ ∈C .
(7.10)
149


## Page 158

Proof. Multiplying the constraint in Proposition 7.7 (which is also true for any strategy σ ∈ΣR)
by αk+1, and summing all the equations for k ≥0, we obtain
X
u′∈C
(f(σ)(y, u′) −f(0,σ)(y, u′)) = α
X
x∈E
X
u∈C
M(k,u)
xy
f(π)(x, u),
∀y ∈E, k ≥0 .
Using (7.4a), we deduce the constraint of the proposition. The last equation is also obtained by
summing all the equations in (7.3) after multiplication by αk.
Proposition 7.15. Let f : E × C →R+ satisﬁes the constraint of Proposition 7.14, that is
X
u′∈C
f(y, u′) = p(0)(y) + α
X
x∈E
X
u∈C
M(u)
xy f(x, u),
∀y ∈E ,
(7.11)
together with the constraints
f(x, u) = 0
∀u̸ ∈C(x) .
(7.12)
Let π be deﬁned by:
π(u | x) = f(x, u)
q(x) ,
with q(x) :=
X
u∈C
f(x, u) .
Then, π is a stationary Markovian strategy and the process (Xk, Uk)k≥0 associated to the policy π
and the initial law p(0) satisﬁes
f(x, u) =
∞
X
k=0
αkP(Xk = x, Uk = u) .
Corollary 7.16. Let f : E × C →R+ and π be as in Proposition 7.15. We have
J(π)
α
= eJ(f),
and
G(ℓ,π)
α
= eG(ℓ)(f)
with
eJ(f) :=
X
x∈E,u∈C
(r(x, u)f(x, u))
(7.13a)
eG(ℓ)(f) :=
X
x∈E,u∈C

gℓ(x, u)f(x, u)

.
(7.13b)
Theorem 7.17. The value of the constrained Markov decision problem with discounted inﬁnite
horizon criteria over the set of all random strategies is equal to the value of the same problem over
random stationary Markov strategies and to the value of the Linear Program:
max
f
eJ(f) under the constraints eG(ℓ)(f) ≤hℓ
∀1 ≤ℓ≤L ,
where the maximization is done over the set of functions f : E × C →R+ satisfying the linear
constraints (7.11) and (7.12), and eJ and eG(ℓ) are as in (7.13).
150


## Page 159

7.4
Constrained MDP with long run time average payoﬀ
Similarly, passing to the limit when α →1−, we can obtain, assuming some ergodicity:
Theorem 7.18. The value of the constrained Markov decision problem with long run time average
payoﬀover the set of all random strategies is equal to the value of the same problem over random
stationary Markov strategies and to the value of the Linear Program:
max
f
eJ(f) under the constraints eG(ℓ)(f) ≤hℓ
∀1 ≤ℓ≤L ,
where the maximization is done over the set of functions f : E × C →R+ satisfying the linear
constraints (7.12) and
X
u′∈C
f(y, u′) =
X
x∈E
X
u∈C
M(u)
xy f(x, u),
∀y ∈E ,
(7.14)
and eJ and eG(ℓ) are as in (7.13).
(7.14) means that f is an invariant occupation measure.
7.5
Complexity
For solving an unconstrainted discounted inﬁnite horizon MDP with ﬁnite state and action spaces,
with m = maxk card(Ak) and n = card(E), the complexity of value iterations was:
O
log((1 −α)ε/Rmax)
log(α)

nm ,
where Rmax is a bound on the rewards. It is only pseudo-polynomial because log(α) is exponential
in the number of bit of α. If α is ﬁxed, it is polynomial but not strongly polynomial, since it
depends on the number of bit of the rewards.
For a constrained inﬁnite horizon MDP, the size of the variable f of the corresponding Linear
Program is in O(m) with L linear inquality constraints and n linear equality constraints.
One can use the simplex or interior point algorithms.
Ye [CS3] proved that simplex for unconstrained MDP is strongly polynomial when α is ﬁxed.
Interior point is polynomial but not strongly polynomial.
Additional references for this chapter
[CS1] Eitan Altman
Constrained Markov Decision Processes.
CRC Press, 1999. See also
https://www-sop.inria.fr/members/Eitan.Altman/TEMP/h.pdf
[CS2] Richard C. Chen and Gilmer L. Blankenship. Dynamic programming equations for discounted
constrained stochastic control. IEEE Trans. Autom. Control, 49(5):699–709, 2004.
[CS3] Y. Ye. The simplex and policy-iteration methods are strongly polynomial for the Markov
decision problem with a ﬁxed discount rate. Math. Oper. Res., 36(4):593–603, 2011.
151
