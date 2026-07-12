# Introduction+to+Stochastic+Programming+by+Birge



## Page 1



## Page 2



## Page 3



## Page 4

519.7    dc21
                        97-6931


## Page 5



## Page 6

To Pierrette and Marie


## Page 7

Preface
According to a French saying “G´erer, c’est pr´evoir,” which we may trans-
late as “(The art of) Managing is (in) foreseeing.” Now, probability and
statistics have long since taught us that the future cannot be perfectly
forecast but instead should be considered random or uncertain. The aim of
stochastic programming is precisely to ﬁnd an optimal decision in problems
involving uncertain data. In this terminology, stochastic is opposed to de-
terministic and means that some data are random, whereas programming
refers to the fact that various parts of the problem can be modeled as linear
or nonlinear mathematical programs. The ﬁeld, also known as optimization
under uncertainty, is developing rapidly with contributions from many dis-
ciplines such as operations research, economics, mathematics, probability,
and statistics. The objective of this book is to provide a wide overview of
stochastic programming, without requiring more than a basic background
in these various disciplines.
Introduction to Stochastic Programming is intended as a ﬁrst course for
beginning graduate students or advanced undergraduate students in such
ﬁelds as operations research, industrial engineering, business administra-
tion (in particular, ﬁnance or management science), and mathematics. Stu-
dents should have some basic knowledge of linear programming, elementary
analysis, and probability as given, for example, in an introductory book on
operations research or management science or in a combination of an in-
troduction to linear programming (optimization) and an introduction to
probability theory.
Instructors may need to add some material on convex analysis depending
on the choice of sections covered. We chose not to include such introductory


## Page 8

viii
Preface
material because students’ backgrounds may vary widely and other texts
include these concepts in detail. We did, however, include an introduction
to random variables while modeling stochastic programs in Section 2.1 and
short reviews of linear programming, duality, and nonlinear programming
at the end of Chapter 2. This material is given as an indication of the pre-
requisites in the book to help instructors provide any missing background.
In the Subject Index, the ﬁrst reference to a concept is where it is deﬁned
or, for concepts speciﬁc to a single section, where a source is provided.
In our view, the objective of a ﬁrst course based on this book is to help
students build an intuition on how to model uncertainty into mathemati-
cal programs, which changes uncertainty brings into the decision process,
what diﬃculties uncertainty may bring, and what problems are solvable. To
begin this development, the ﬁrst section in Chapter 1 provides a worked
example of modeling a stochastic program. It introduces the basic con-
cepts, without using any new or speciﬁc techniques. This ﬁrst example can
be complemented by any one of the other proposed cases of Chapter 1,
in ﬁnance, in multistage capacity expansion, and in manufacturing. Based
again on examples, Chapter 2 describes how a stochastic model is formally
built. It also stresses the fact that several diﬀerent models can be built,
depending on the type of uncertainty and the time when decisions must
be taken. This chapter links the various concepts to alternative ﬁelds of
planning under uncertainty.
Any course should begin with the study of those two chapters. The sequel
would then depend on the students’ interests and backgrounds. A typical
course would consist of elements of Chapter 3, Sections 4.1 to 4.5, Sections
5.1 to 5.3 and 5.7, and one or two more advanced sections of the instructor’s
choice. The ﬁnal case study may serve as a conclusion. A class emphasizing
modeling might focus on basic approximations in Chapter 9 and sampling
in Chapter 10. A computational class would stress methods from Chapters
6 to 8. A more theoretical class might concentrate more deeply on Chapter
3 and the results from Chapters 9 to 11.
The book can also be used as an introduction for graduate students
interested in stochastic programming as a research area. They will ﬁnd
a broad coverage of mathematical properties, models, and solution algo-
rithms. Broad coverage cannot mean an in-depth study of all existing re-
search. The reader will thus be referred to the original papers for details.
Advanced sections may require multivariate calculus, probability measure
theory, or an introduction to nonlinear or integer programming. Here again,
the stress is clearly in building knowledge and intuition in the ﬁeld. Math-
ematical results are given so long as they are either basic properties or
helpful in developing eﬃcient solution procedures. The importance of the
various sections clearly reﬂects our own interests, which focus on results
that may lead to practical applications of stochastic programming.


## Page 9

Preface
ix
To conclude, we may use the following little story. An elderly person,
celebrating her one hundredth birthday, was asked how she succeeded in
reaching that age. She answered, “It’s very simple. You just have to wait.”
In comparison, stochastic programming may well look like a ﬁeld of young
impatient people who not only do not want to wait and see but who con-
sider waiting to be suboptimal. We realize how much patience was needed
from our friends and colleagues who encouraged us to write this book, which
took us much longer than expected. To all of them, we are extremely thank-
ful for their support. The authors also wish to thank the Fonds National
de la Recherche Scientiﬁque and the National Science Foundation for their
ﬁnancial support. Both authors are deeply grateful to the people who in-
troduced us to the ﬁeld, George Dantzig, Roger Wets, Jacques Dr`eze, and
Guy de Ghellinck. Our special thanks go to our wives, Pierrette and Marie,
to whom we dedicate this book.
Ann Arbor, Michigan
John R. Birge
Namur, Belgium
Fran¸cois Louveaux


## Page 10



## Page 11

Contents
Preface
vii
Notation
xv
I
Models
1
1
Introduction and Examples
3
1.1
A Farming Example and the News Vendor Problem . . . .
4
1.2
Financial Planning and Control
. . . . . . . . . . . . . . .
20
1.3
Capacity Expansion . . . . . . . . . . . . . . . . . . . . . .
28
1.4
Design for Manufacturing Quality . . . . . . . . . . . . . .
37
1.5
Other Applications . . . . . . . . . . . . . . . . . . . . . . .
42
2
Uncertainty and Modeling Issues
49
2.1
Probability Spaces and Random Variables . . . . . . . . .
49
2.2
Deterministic Linear Programs . . . . . . . . . . . . . . . .
51
2.3
Decisions and Stages . . . . . . . . . . . . . . . . . . . . . .
52
2.4
Two-Stage Program with Fixed Recourse . . . . . . . . . .
54
2.5
Random Variables and Risk Aversion . . . . . . . . . . . .
61
2.6
Implicit Representation of the Second Stage . . . . . . . .
63
2.7
Probabilistic Programming . . . . . . . . . . . . . . . . . .
64
2.8
Relationship to Other Decision-Making Models
. . . . . .
67
2.9
Short Reviews
. . . . . . . . . . . . . . . . . . . . . . . . .
73


## Page 12

xii
Contents
II
Basic Properties
81
3
Basic Properties and Theory
83
3.1
Two-Stage Stochastic Linear Programs with Fixed
Recourse . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
84
3.2
Probabilistic or Chance Constraints . . . . . . . . . . . . .
103
3.3
Stochastic Integer Programs
. . . . . . . . . . . . . . . . .
109
3.4
Two-Stage Stochastic Nonlinear Programs with Recourse .
122
3.5
Multistage Stochastic Programs with Recourse
. . . . . .
128
4
The Value of Information and the Stochastic Solution
137
4.1
The Expected Value of Perfect Information
. . . . . . . .
137
4.2
The Value of the Stochastic Solution
. . . . . . . . . . . .
139
4.3
Basic Inequalities . . . . . . . . . . . . . . . . . . . . . . . .
140
4.4
The Relationship between EVPI and VSS
. . . . . . . . .
141
4.5
Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . .
144
4.6
Bounds on EVPI and VSS
. . . . . . . . . . . . . . . . . .
145
III
Solution Methods
153
5
Two-Stage Linear Recourse Problems
155
5.1
The L-Shaped Method . . . . . . . . . . . . . . . . . . . . .
156
5.2
Feasibility . . . . . . . . . . . . . . . . . . . . . . . . . . . .
163
5.3
The Multicut Version . . . . . . . . . . . . . . . . . . . . .
166
5.4
Bunching and Other Eﬃciencies . . . . . . . . . . . . . . .
169
5.5
Inner Linearization Methods . . . . . . . . . . . . . . . . .
174
5.6
Basis Factorization Methods . . . . . . . . . . . . . . . . .
179
5.7
Special Cases—Simple Recourse and Network Problems .
192
6
Nonlinear Programming Approaches to Two-Stage Recourse
Problems
199
6.1
Regularized Decomposition . . . . . . . . . . . . . . . . . .
199
6.2
The Piecewise Quadratic Form of the L-Shaped Method .
206
6.3
Methods Based on the Stochastic Program Lagrangian . .
215
6.4
Nonlinear Programming in Simple Recourse Problems . .
225
6.5
Other Nonlinear Programming–Based Methods . . . . . .
231
7
Multistage Stochastic Programs
233
7.1
Nested Decomposition Procedures . . . . . . . . . . . . . .
234
7.2
Quadratic Nested Decomposition
. . . . . . . . . . . . . .
244
7.3
Other Approaches to Multiple Stages . . . . . . . . . . . .
251
8
Stochastic Integer Programs
253
8.1
Integer L-Shaped Method . . . . . . . . . . . . . . . . . . .
253
8.2
Simple Integer Recourse . . . . . . . . . . . . . . . . . . . .
262


## Page 13

Contents
xiii
8.3
Binary First-Stage Variables . . . . . . . . . . . . . . . . .
268
8.4
Other Approaches . . . . . . . . . . . . . . . . . . . . . . .
276
IV
Approximation and Sampling Methods
283
9
Evaluating and Approximating Expectations
285
9.1
Direct Solutions with Multiple Integration . . . . . . . . .
286
9.2
Discrete Bounding Approximations . . . . . . . . . . . . .
288
9.3
Using Bounds in Algorithms . . . . . . . . . . . . . . . . .
296
9.4
Bounds in Chance-Constrained Problems . . . . . . . . . .
301
9.5
Generalized Bounds . . . . . . . . . . . . . . . . . . . . . .
305
9.6
General Convergence Properties . . . . . . . . . . . . . . .
323
10 Monte Carlo Methods
331
10.1
General Results for Sampled Problems . . . . . . . . . . .
332
10.2
Using Sampling in the L-Shaped Method . . . . . . . . . .
335
10.3
Stochastic Quasi-Gradient Methods . . . . . . . . . . . . .
343
10.4
Sampling Extensions: Uses with Analytical and Empirical
Observations . . . . . . . . . . . . . . . . . . . . . . . . . .
349
11 Multistage Approximations
353
11.1
Bounds Based on the Jensen and Edmundson-Madansky
Inequalities . . . . . . . . . . . . . . . . . . . . . . . . . . .
354
11.2
Bounds Based on Aggregation . . . . . . . . . . . . . . . .
359
11.3
Bounds Based on Separable Responses . . . . . . . . . . .
362
11.4
Bounds for Speciﬁc Problem Structures . . . . . . . . . . .
366
V
A Case Study
373
12 Capacity Expansion
375
12.1
Model Development . . . . . . . . . . . . . . . . . . . . . .
376
12.2
Demand Distribution Modeling
. . . . . . . . . . . . . . .
382
12.3
Computational Comparisons . . . . . . . . . . . . . . . . .
383
12.4
Results and Extensions . . . . . . . . . . . . . . . . . . . .
383
A Sample Distribution Functions
385
A.1
Discrete Random Variables . . . . . . . . . . . . . . . . . .
385
A.2
Continuous Random Variables . . . . . . . . . . . . . . . .
386
References
387
Author Index
411
Subject Index
415


## Page 14



## Page 15

Notation
The following describes the major symbols and notations used in the text.
To the greatest extent possible, we have attempted to keep unique meanings
for each item. In those cases where an item has additional uses, they should
be clear from context. We include here only notation used in more than one
section. Additional notation may be needed within speciﬁc sections and is
explained when used.
In general, vectors are assumed to be columns with transposes to indicate
row vectors. This yields cT x to denote the inner product of two n-vectors,
c and x. We reserve prime (′) for ﬁrst derivatives with respect to time (e.g.,
f ′ = df/dt).
Vectors in primal programs are represented by lowercase Latin letters
while matrices are uppercase. Dual variables and certain scalars are gen-
erally Greek letters. Superscripts indicate a stage while subscripts indi-
cate components followed by realization index. Boldface indicates a ran-
dom quantity. Expectations of random variables are indicated by a bar
(¯ξ), µ, or (E(ξ)). We also use the bar notation to denote sample means in
Chapter 10.
Equations are numbered consecutively in the text by section and number
within the section (e.g., (1.2) for Section 1, Equation 2). For references to
chapters other than the current one, we use three indices: chapter, section,
and equation, (e.g., (3.1.2) for Chapter 3, Section 1, Equation 2). Exercises
are given at the end of each section and are referenced in the same manner
as equations. All other items (ﬁgures, tables, declarations, examples) are
labeled consecutively through the entire chapter with a single reference
(e.g., Figure 1) if within the current chapter and chapter and number if in
a diﬀerent chapter (e.g., Figure 3.1 for Chapter 3, Figure 1).


## Page 16

xvi
Notation
Symbol
Deﬁnition
+
Superscript indicates the positive part of a real
(i.e., a+ = max(a, 0)) or unrestricted variable (e.g.,
y = y+ −y−, y+ ≥0, y−≥0) and its objective
coeﬃcients (e.g., q+), subscript as non-negative
values in a set (e.g., ℜ+) or the
right-limit (F +(t) = lims↓t F(s))
−
Superscript indicates the negative part of a real
(i.e., a−= max(−a, 0)) or unrestricted variable
(e.g., y = y+ −y−, y+ ≥0, y−≥0) and its
objective coeﬃcients (e.g., q−) or the left-limit
(F −(t) = lims↑t F(s))
∗
Indicates an optimal value or solution (e.g., x∗)
0ˆ′˜
Indicate given nonoptimal values or
solutions (e.g., x0,ˆx, x′, ˜x)
a
Ancestor scenario, real value or vector
A
First-stage matrix (e.g., Ax = b), also used
to indicate a subset, A ∈A ⊂Ω
A
Collection of subsets
b
First-stage right-hand side (e.g., Ax = b)
B
Matrix, basis submatrix, Borel sets,
or index set of a basis
B
Collection of subsets (notably Borel sets)
c
First-stage objective (cT x), t-th stage objective
((ct(ω))T xt) or real vectors
C
Matrix or index set of continuous variables
d
Right-hand side of a feasibility cut in the L-shaped
method, a demand, or real vector
D
Left-hand side vector of a feasibility cut in the
L-shaped method, a matrix, a set, or an index set
of discrete variables
D
Set of descendant scenarios
e
Exponential, right-hand side of an optimality cut
in the L-shaped method, an extreme point,
or the unit vector (eT = (1, . . . , 1))
E
Mathematical expectation operator or left-hand
side vector of an optimality cut in the
L-shaped method
f
Function (usually in an objective (f(x) or fi(x))
or a density
F
Cumulative probability distribution
g
Function (usually in constraints (g(x) or gj(x)))
h
Right-hand side in second-stage (Wy = h −Tx),
also ht(ω) in multistage problems


## Page 17

Notation
xvii
Symbol
Deﬁnition
H
Number of stages (horizon) in multistage problems
i
Subscript index of functions (fi)
or vector elements (xi, xij)
I
Identity matrix or index set (i ∈I)
j
Subscript index of functions (gj)
or vector elements (yj, yij)
J
Matrix or index set
k
Index of a realization of a random
vector (k = 1, . . . , K)
K
Feasibility sets (K1, K2) or total number of
realizations of a discrete random vector
l
Index or a lower bound on a variable
L
The L-shaped method, objective value lower
bound, or real value
m
Number of constraints (m1, m2) or
number of elements (i = 1, . . . , m)
n
Number of variables (n1, n2) or
number of elements (i = 1, . . . , n)
N
Set, normal cone, normal distribution,
or number of random elements
O
Zero matrix
p
Probability of a random element (e.g., pk
= P(ξ = ξk)) or matrix of probabilities
P
Probability of events (e.g., P(ξ ≤0))
q
Second-stage objective vector (qT y)
Q
Second-stage (multistage) value function
with random argument (Q(x,ξ) or Qt(xt, ξt))
Q
Second-stage (multistage) expected value
value (recourse) function (Q(x) or Qt(xt))
r
Revenue or return in examples, real vector,
or index
R
Matrix or set
ℜ
Real numbers
s
Scenario or index
S
Set or matrix
t
Superscript stage or period index for multistage
programs (t = 1, . . . , H), a real-valued parameter,
or an index
T
Technology matrix (Wy = h −Tx or
T t−1(ω)(x)); as a superscript, the transpose of
a matrix or vector
u
General vector, upper-bound vector, or
expected shortage
U
Objective value upper bound


## Page 18

xviii
Notation
Symbol
Deﬁnition
v
Variable vector or expected surplus
V
Set, matrix or an operator
w
Second-stage decision vector in some examples
W
Recourse matrix (Wy = h −Tx)
x
First-stage decision vector or multistage
decision vector (xt)
X
First-stage feasible set (x ∈X) or
tth stage feasible set (Xt)
y
Second-stage decision vector
Y
Second-stage feasible set (y ∈Y )
z
Objective value (min z = cT x + · · ·)
Z
Integers
α
Real value, vector, or probability level with
probabilistic constraints
β
Real value or vector
γ
Real value or function
δ
Real value or function
ǫ
Real value
ζ
Random variable
η
Real value or random variable
θ
Lower bound on Q(x) in the
L-shaped method
κ
Index
λ
Dual multiplier, parameter in a convex
combination, or measure
µ
Expectation (used mostly in examples of densities)
or a parameter for non-negative multiples
ν
Algorithm iteration index
ξ
Random vector (often indexed by time,
ξt) with realizations as ξ (without boldface)
Ξ
Support of the random vector ξ
π
Dual multiplier
Π
Product or projection operator
ρ
Dual multiplier or discount factor
σ
Dual multiplier, standard deviation, or
σ-ﬁeld
Σ
Summation
τ
Possible right-hand side in bundles
or index of time
φ
Function in computing the value of
the stochastic solution or a measure
Φ
Function, cumulative distribution of standard
normal


## Page 19

Notation
xix
Symbol
Deﬁnition
∅
Empty set
χ
Tender or oﬀer from ﬁrst to second
period (χ = Tx)
ψ
Second stage value function deﬁned on tenders
and with random argument, ψ(χ, ξ(ω)))
Ψ
Expected second stage value function
deﬁned on tenders, Ψ(χ))
ω
Random event (ω ∈Ω)
Ω
Set of all random events


## Page 20

Part I
Models
1


## Page 21



## Page 22

1
Introduction and Examples
This chapter presents stochastic programming examples from a variety of
areas with wide application in stochastic programming. These examples are
intended to help the reader build intuition on how to model uncertainty.
They also reﬂect diﬀerent structural aspects of the problems. In particular,
we show the variety of stochastic programming models in terms of the
objectives of the decision process, the constraints on those decisions, and
their relationships to the random elements.
In each example, we investigate the value of the stochastic programming
model over a similar deterministic problem. We show that even simple
models can lead to signiﬁcant savings. These results provide the motiva-
tion to lead us into the following chapters on stochastic programs, solution
properties, and techniques.
In the ﬁrst section, we consider a farmer who must decide on the amounts
of various crops to plant. The yields of the crops vary according to the
weather. From this example, we illustrate the basic foundation of stochas-
tic programming and the advantage of the stochastic programming solu-
tion over deterministic approaches. We also introduce the classical news
vendor (or newsboy) problem and give the fundamental properties of these
problems’ general class, called two-stage stochastic linear programs with
recourse.
The second section contains an example in planning ﬁnances for a child’s
education. This example ﬁts the situation in many discrete time control
problems. Decisions occur at diﬀerent points in time so that the problem
can be viewed as having multiple stages of observations and actions.


## Page 23

4
1. Introduction and Examples
The third section considers power system capacity expansion. Here, de-
cisions are taken dynamically about additional capacity and about the
allocation of capacity to meet demand. The resulting problem has multiple
decision stages and a valuable property known as block separable recourse
that allows eﬃcient solution. The problem also provides a natural example
of constraints on reliability within the area called probabilistic or chance-
constrained programming.
The fourth example concerns the design of a simple axle. It includes
market reaction to the design and performance characteristics of products
made by a manufacturing system with variable performance. The essen-
tial characteristics of the maximum performance of the product illustrate
a problem with fundamental nonlinearities incorporated directly into the
stochastic program.
The ﬁnal section of this chapter brieﬂy describes several other major
application areas of stochastic programs. The exercises at the end of the
chapter develop modeling techniques. This chapter illustrates some of the
range of stochastic programming applications but is not meant to be ex-
haustive. Applications in routing and location, for example, are discussed
in Chapter 2.
1.1
A Farming Example and the News Vendor
Problem
a. The farmer’s problem
Consider a European farmer who specializes in raising grain, corn, and
sugar beets on his 500 acres of land. During the winter, he wants to decide
how much land to devote to each crop. (We refer to the farmer as “he”
for convenience and not to imply anything about the gender of European
farmers.)
The farmer knows that at least 200 tons (T) of wheat and 240 T of corn
are needed for cattle feed. These amounts can be raised on the farm or
bought from a wholesaler. Any production in excess of the feeding require-
ment would be sold. Selling prices are $170 and $150 per ton of wheat and
corn, respectively. The purchase prices are 40% more than this due to the
wholesaler’s margin and transportation costs.
Another proﬁtable crop is sugar beet, which sells at $36/T; however,
the European Commission imposes a quota on sugar beet production. Any
amount in excess of the quota can be sold only at $10/T. The farmer’s
quota for next year is 6000 T.
Based on past experience, the farmer knows that the mean yield on his
land is roughly 2.5 T, 3 T, and 20 T per acre for wheat, corn, and sugar


## Page 24

1.1 A Farming Example and the News Vendor Problem
5
TABLE 1. Data for farmer’s problem.
Wheat
Corn
Sugar Beets
Yield (T/acre)
2.5
3
20
Planting cost ($/acre)
150
230
260
Selling price ($/T)
170
150
36 under 6000 T
10 above 6000 T
Purchase price ($/T)
238
210
–
Minimum require-
200
240
–
ment (T)
Total available land: 500 acres
beets, respectively. Table 1 summarizes these data and the planting costs
for these crops.
To help the farmer make up his mind, we can set up the following model.
Let
x1 = acres of land devoted to wheat,
x2 = acres of land devoted to corn,
x3 = acres of land devoted to sugar beets,
w1 = tons of wheat sold,
y1 = tons of wheat purchased,
w2 = tons of corn sold,
y2 = tons of corn purchased,
w3 = tons of sugar beets sold at the favorable price,
w4 = tons of sugar beets sold at the lower price.
The problem reads as follows:
min
150x1 + 230x2 + 260x3 + 238y1 −170w1
+210y2 −150w2−36w3 −10w4
(1.1)
s.t. x1 + x2 + x3 ≤500, 2.5 x1 + y1 −w1 ≥200,
3 x2 + y2 −w2 ≥240,w3 + w4 ≤20x3, w3 ≤6000,
x1, x2, x3,y1, y2, w1, w2, w3, w4 ≥0.
After solving (1.1) with his favorite linear program solver, the farmer ob-
tains an optimal solution, as in Table 2.
This optimal solution is easy to understand. The farmer devotes enough
land to sugar beets to reach the quota of 6000 T. He then devotes enough
land to wheat and corn production to meet the feeding requirement. The
rest of the land is devoted to wheat production. Some wheat can be sold.
To an extent, the optimal solution follows a very simple heuristic rule:
to allocate land in order of decreasing proﬁt per acre. In this example, the
order is sugar beets at a favorable price, wheat, corn, and sugar beets at
the lower price. This simple heuristic would, however, no longer be valid


## Page 25

6
1. Introduction and Examples
TABLE 2. Optimal solution based on expected yields.
Culture
Wheat
Corn
Sugar Beets
Surface (acres)
120
80
300
Yield (T)
300
240
6000
Sales (T)
100
–
6000
Purchase (T)
–
–
–
Overall proﬁt: $118,600
if other constraints, such as labor requirements or crop rotation, would be
included.
After thinking about this solution, the farmer becomes worried. He has
indeed experienced quite diﬀerent yields for the same crop over diﬀerent
years mainly because of changing weather conditions. Most crops need rain
during the few weeks after seeding or planting, then sunshine is welcome
for the rest of the growing period. Sunshine should, however, not turn
into drought, which causes severe yield reductions. Dry weather is again
beneﬁcial during harvest. From all these factors, yields varying 20 to 25%
above or below the mean yield are not unusual.
In the next sections, we study two possible representations of these vari-
able yields. One approach using discrete, correlated random variables is
described in Sections 1.1b and 1.1c. Another, using continuous uncorre-
lated random variables, is described in Section 1.1d.
b. A scenario representation
A ﬁrst possibility is to assume some correlation among the yields of the
diﬀerent crops. A very simpliﬁed representation of this would be to as-
sume, e.g., that years are good, fair, or bad for all crops, resulting in above
average, average, or below average yields for all crops. To ﬁx these ideas,
“above” and “below” average indicate a yield 20% above or below the mean
yield given in Table 1. For simplicity, we assume that weather conditions
and yields for the farmer do not have a signiﬁcant impact on prices.
The farmer wishes to know whether the optimal solution is sensitive to
variations in yields. He decides to run two more optimizations based on
above average and below average yields. Tables 3 and 4 give the optimal
solutions he obtains in these cases.
Again, the solutions in Tables 3 and 4 seem quite natural. When yields
are high, smaller surfaces are needed to raise the minimum requirements in
wheat and corn and the sugar beet quota. The remaining land is devoted to
wheat, whose extra production is sold. When yields are low, larger surfaces
are needed to raise the minimum requirements and the sugar beet quota. In


## Page 26

1.1 A Farming Example and the News Vendor Problem
7
TABLE 3. Optimal solution based on above average yields (+ 20%).
Culture
Wheat
Corn
Sugar Beets
Surface (acres)
183.33
66.67
250
Yield (T)
550
240
6000
Sales (T)
350
–
6000
Purchase (T)
–
–
–
Overall proﬁt: $167,667
TABLE 4. Optimal solution based on below average yields (−20%).
Culture
Wheat
Corn
Sugar Beets
Surface (acres)
100
25
375
Yield (T)
200
60
6000
Sales (T)
–
–
6000
Purchase (T)
–
180
–
Overall proﬁt: $59,950
fact, corn requirements cannot be satisﬁed with the production, and some
corn must be bought.
The optimal solution is very sensitive to changes in yields. The optimal
surfaces devoted to wheat range from 100 acres to 183.33 acres. Those
devoted to corn range from 25 acres to 80 acres and those devoted to sugar
beets from 250 acres to 375 acres. The overall proﬁt ranges from $59,950
to $167,667.
Long-term weather forecasts would be very helpful here. Unfortunately,
as even meteorologists agree, weather conditions cannot be accurately pre-
dicted six months ahead. The farmer must make up his mind without per-
fect information on yields.
The main issue here is clearly on sugar beet production. Planting large
surfaces would make it certain to produce and sell the quota, but would also
make it likely to sell some sugar beets at the unfavorable price. Planting
small surfaces would make it likely to miss the opportunity to sell the full
quota at the favorable price.
The farmer now realizes that he is unable to make a perfect decision
that would be best in all circumstances. He would, therefore, want to as-
sess the beneﬁts and losses of each decision in each situation. Decisions
on land assignment (x1, x2, x3) have to be taken now, but sales and pur-
chases (wi, i = 1, . . . , 4, yj, j = 1, 2) depend on the yields. It is use-
ful to index those decisions by a scenario index s = 1, 2, 3 corresponding
to above average, average, or below average yields, respectively. This cre-


## Page 27

8
1. Introduction and Examples
ates a new set of variables of the form wis, i = 1, 2, 3, 4, s = 1, 2, 3 and
yjs, j = 1, 2, s = 1, 2, 3. As an example, w32 represents the amount of
sugar beets sold at the favorable price if yields are average.
Assuming the farmer wants to maximize long-run proﬁt, it is reasonable
for him to seek a solution that maximizes his expected proﬁt. (This as-
sumption means that the farmer is neutral about risk. For a discussion of
risk aversion and alternative utilities, see Chapter 2.) If the three scenarios
have an equal probability of 1/3, the farmer’s problem reads as follows:
min
150x1 + 230x2 + 260x3−1
3(170w11 −238y11 + 150w21
−210y21 + 36w31 + 10w41)
−1
3(170w12 −238y12 + 150w22
−210y22 + 36w32 + 10w42)
−1
3(170w13 −238y13 + 150w23
−210y23 + 36w33 + 10w43)
s.t.
x1 + x2 + x3 ≤500, 3x1 + y11−w11 ≥200, 3.6x2 + y21 −w21 ≥240,
w31 + w41 ≤24x3, w31≤6000, 2.5x1 + y12 −w12 ≥200,
3x2 + y22 −w22 ≥240, w32+w42 ≤20x3, w32 ≤6000,
2x1 + y13 −w13 ≥200, 2.4x2+y23 −w23 ≥240, w33 + w43 ≤16x3,
w33 ≤6000, x, y, w ≥0.
(1.2)
Such a model of a stochastic decision program is known as the extensive
form of the stochastic program because it explicitly describes the second-
stage decision variables for all scenarios. The optimal solution of (1.2) is
given in Table 5. The top line gives the planting areas, which must be
determined before realizing the weather and crop yields. This decision is
called the ﬁrst stage. The other lines describe the yields, sales, and pur-
chases in the three scenarios. They are called the second stage. The bottom
line shows the overall expected proﬁt.
The optimal solution can be understood as follows. The most proﬁtable
decision for sugar beet land allocation is the one that always avoids sales
at the unfavorable price even if this implies that some portion of the quota
is unused when yields are average or below average.
The area devoted to corn is such that it meets the feeding requirement
when yields are average. This implies sales are possible when yields are
above average and purchases are needed when yields are below average.
Finally, the rest of the land is devoted to wheat. This area is large enough
to cover the minimum requirement. Sales then always occur.
This solution illustrates that it is impossible, under uncertainty, to ﬁnd
a solution that is ideal under all circumstances. Selling some sugar beets at
the unfavorable price or having some unused quota is a decision that would
never take place with a perfect forecast. Such decisions can appear in a


## Page 28

1.1 A Farming Example and the News Vendor Problem
9
TABLE 5. Optimal solution based on the stochastic model (1.2).
Wheat
Corn
Sugar Beets
First
Area (acres)
170
80
250
Stage
s = 1
Yield (T)
510
288
6000
Above
Sales (T)
310
48
6000
(favor. price)
Purchase (T)
–
–
–
s = 2
Yield (T)
425
240
5000
AverageSales (T)
225
–
5000
(favor. price)
Purchase (T)
–
–
–
s = 3
Yield (T)
340
192
4000
Below
Sales (T)
140
–
4000
(favor. price)
Purchase (T)
–
48
–
Overall proﬁt: $108,390
stochastic model because decisions have to be balanced or hedged against
the various scenarios.
The hedging eﬀect has an important impact on the expected optimal
proﬁt. Suppose yields vary over years but are cyclical. A year with above
average yields is always followed by a year with average yields and then
a year with below average yields. The farmer would then take optimal
solutions as given in Table 3, then Table 2, then Table 4, respectively. This
would leave him with a proﬁt of $167,667 the ﬁrst year, $118,600 the second
year, and $59,950 the third year. The mean proﬁt over the three years (and
in the long run) would be the mean of the three ﬁgures, namely $115,406
per year.
Now, assume again that yields vary over years, but on a random basis. If
the farmer gets the information on the yields before planting, he will again
choose the areas on the basis of the solution in Table 2, 3, or 4, depending
on the information received. In the long run, if each yield is realized one
third of the years, the farmer will get again an expected proﬁt of $115,406
per year. This is the situation under perfect information.
As we know, the farmer unfortunately does not get prior information on
the yields. So, the best he can do in the long run is to take the solution as
given by Table 5. This leaves the farmer with an expected proﬁt of $108,390.
The diﬀerence between this ﬁgure and the value, $115,406, in the case of
perfect information, namely $7016, represents what is called the expected
value of perfect information (EVPI). This concept, along with others, will


## Page 29

10
1. Introduction and Examples
be studied in Chapter 4. At this introductory level, we may just say that
it represents the loss of proﬁt due to the presence of uncertainty.
Another approach the farmer may have is to assume expected yields and
always to allocate the optimal planting surface according to these yields,
as in Table 2. This approach represents the expected value solution. It is
common in optimization but can have unfavorable consequences. Here, as
shown in Exercise 1, using the expected value solution every year results
in a long run annual proﬁt of $107,240. The loss by not considering the
random variations is the diﬀerence between this and the stochastic model
proﬁt from Table 5. This value, $108,390−107,240=$1,150, is the value of
the stochastic solution (VSS), the possible gain from solving the stochastic
model. Note that it is not equal to the expected value of perfect information,
and, as we shall see in later models, may in fact be larger than the EVPI.
These two quantities give the motivation for stochastic programming in
general and remain a key focus throughout this book. EVPI measures the
value of knowing the future with certainty while VSS assesses the value of
knowing and using distributions on future outcomes. Our emphasis will be
on problems where no further information about the future is available so
the VSS becomes more practically relevant. In some situations, however,
more information might be available through more extensive forecasting,
sampling, or exploration. In these cases, EVPI would be useful for deciding
whether to undertake additional eﬀorts.
c. General model formulation
We may also use this example to illustrate the general formulation of a
stochastic problem. We have a set of decisions to be taken without full
information on some random events. These decisions are called ﬁrst-stage
decisions and are usually represented by a vector x. In the farmer example,
they are the decisions on how many acres to devote to each crop. Later, full
information is received on the realization of some random vector ξ. Then,
second-stage or corrective actions y are taken. We use boldface notation
here and throughout the book to denote that these vectors are random
and to diﬀerentiate them from their realizations. We also sometimes use a
functional form, such as ξ(ω) or y(s), to show explicit dependence on an
underlying element, ω or s.
In the farmer example, the random vector is the set of yields and the
corrective actions are purchases and sales of products. In mathematical
programming terms, this deﬁnes the so-called two-stage stochastic program
with recourse of the form
min
cT x + EξQ(x,ξ)
(1.3)
s.t.
Ax = b,
x ≥0,


## Page 30

1.1 A Farming Example and the News Vendor Problem
11
where Q(x,ξ) = min{qT y|Wy = h −Tx, y ≥0}, ξ is the vector formed by
the components of qT , hT , and T, and Eξ denote mathematical expectation
with respect to ξ. We assume here that W is ﬁxed (ﬁxed recourse). Reasons
for this restriction are explained in Section 3.1.
In the farmer example, the random vector is a discrete variable with
only three diﬀerent values. Only the T matrix is random. A second-stage
problem for one particular scenario s can thus be written as
Q(x, s) = min{238y1 −170w1+210y2 −150w2 −36w3 −10w4}
(1.4)
s.t. t1(s)x1+y1 −w1 ≥200,
t2(s)x2+y2 −w2 ≥240,
w3+w4 ≤t3(s)x3,
w3≤6000,
y1, w1≥0,
where ti(s) represents the yield of crop i under scenario s (or state of na-
ture s). To illustrate the link between the general formulation (1.3) and the
example (1.4), observe that in (1.4) we may say that the random vector
ξ = (t1, t2, t3) is formed by the three yields and that ξ can take on three dif-
ferent values, say ξ1, ξ2, and ξ3, which represent (t1(1), t2(1), t3(1)), (t1(2),
t2(2), t3(2)), and (t1(3), t2(3), t3(3)), respectively.
An alternative interpretation would be to say that the random vector ξ(s)
in fact depends on the scenario s, which takes on three diﬀerent values1.
In this section, we have illustrated two possible representations of a
stochastic program. The form (1.2) given earlier for the farmer’s example
is known as the extensive form. It is obtained by associating one decision
vector in the second-stage to each possible realization of the random vector.
The second form (1.3) or (1.4) is called the implicit representation of the
stochastic program. A more condensed implicit representation is obtained
by deﬁning Q(x) = EξQ(x,ξ) as the value function or recourse function so
that (1.3) can be written as
min
cT x + Q(x)
(1.5)
s.t.
Ax = b,
x ≥0.
d. Continuous random variables
Contrary to the assumption made in Section 1.2, we may also assume that
yields for the diﬀerent crops are independent. In that case, we may as well
consider a continuous random vector for the yields. To illustrate this, let us
1Note that the decisions y1, y2, w1, w2, w3, and w4 also depend on the scenario.
This dependence is not always made explicit. It appears explicitly in (1.7) but
not in (1.4).


## Page 31

12
1. Introduction and Examples
assume that the yield for each crop i can be appropriately described by a
uniform random variable, inside some range [li, ui] (see Appendix A.2). For
the sake of comparison, we may take li to be 80% of the mean yield and ui
to be 120% of the mean yield so that the expectations for the yields will
be the same as in Section 1.b. Again, the decisions on land allocation are
ﬁrst-stage decisions because they are taken before knowledge of the yields.
Second-stage decisions are purchases and sales after the growing period.
The second-stage formulation can again be described as Q(x) = EξQ(x,ξ),
where Q(x,ξ) is the value of the second stage for a given realization of the
random vector.
Now, in this particular example, the computation of Q(x,ξ) can be sep-
arated among the three crops due to independence of the random vector.
(Note that this separability property also holds in the discrete representa-
tion of Section 1.b.) We can then write:
EξQ(x,ξ) =
3

i=1
EξQi(xi,ξ) =
3

i=1
Qi(xi),
(1.6)
where Qi(xi,ξ) is the optimal second-stage value of purchases and sales of
crop i.
We are in fact in position to give an exact analytical expression for the
second-stage value functions Qi(xi), i = 1, . . . , 3. We ﬁrst consider sugar
beet sales. For a given value t3(ξ) of the sugar beet yield, one obtains the
following second-stage problem:
Q3(x3,ξ) = min −36w3(ξ)−10w4(ξ)
(1.7)
s.t. w3(ξ) + w4(ξ)≤t3(ξ)x3,
w3(ξ)≤6000,
w3(ξ), w4(ξ)≥0.
The optimal decisions for this problem are clearly to sell as many sugar
beets as possible at the favorable price, and to sell the possible remaining
production at the unfavorable price, namely
w3(ξ)= min[6000, t3(ξ)x3],
(1.8)
w4(ξ)= max[t3(ξ)x3 −6000, 0].
This results in a second-stage value of
Q3(x3,ξ) = −36 min[6000, t3(ξ)x3] −10 max[t3(ξ)x3 −6000, 0].
We ﬁrst assume that the surface x3 devoted to sugar beets will not be so
large that quota would be exceeded for any possible yield or so small that
production would always be less than the quota for any possible yield. In
other words, we assume that the following relation holds:
l3x3 ≤6000 ≤u3x3,
(1.9)


## Page 32

1.1 A Farming Example and the News Vendor Problem
13
where, as already deﬁned, l3 and u3 are the bounds on the possible values
of t3(ξ). Under this assumption, the expected value of the second stage for
sugar beet sales is
Q3(x3) = EξQ3(x3,ξ3)
= −
 6000/x3
l3
36tx3f(t)dt
−
 u3
6000/x3
(216000 + 10tx3 −60000)f(t)dt,
where f(t) denotes the density of the random yield t3(ξ). Given the as-
sumption that this density is uniform over the interval [l3, u3], one obtains,
after some computation, the following analytical expression
Q3(x3) = −18(u2
3 −l2
3)x3
u3 −l3
+ 13(u3x3 −6000)2
x3(u3 −l3)
,
which can also be expressed as
Q3(x3) = −36¯t3x3 + 13(u3x3 −6000)2
x3(u3 −l3)
,
(1.10)
where ¯t3 denotes the expected yield for sugar beet production, which is
u3+l3
2
for a uniform density.
Note that assumption (1.9) is not really limiting. We can still compute
the analytical expression of Q3(x3) for the other situations.
For example, if the surface x3 is such that the production exceeds the
quota for any possible yield (l3x3 > 6000), then the optimal second-stage
decisions are simply
w3(ξ) = 6000,
w4(ξ) = t3(ξ)x3 −6000, for all ξ.
The second-stage value for a given ξ is now
Q3(x3, ξ) = −216000 −10(t3(ξ)x3 −6000) = −156000 −10t3(ξ)x3,
and the expected value is simply
Q3(x3) = −156000 −10¯t3x3.
(1.11)
Similarly, if the surface devoted to sugar beets is so small that for any yield
the production is lower than the quota, the second-stage value function is
Q3(x3) = −36¯t3x3.
(1.12)


## Page 33

14
1. Introduction and Examples
FIGURE 1. The expected recourse value for sugar beets as a function of acres
planted.
We may therefore draw the graph of the function Q3(x3) for all possible
values of x3 as in Figure 1. Note that with our assumption of ¯t3 = 20, we
would then have the limits on x3 in (1.9) as 250 ≤x3 ≤375.
We immediately see that the function has three diﬀerent pieces. Two of
these pieces are linear and one is nonlinear, but the function Q3(x3) is
continuous and convex. This property will be proved when we consider
the generalization of this problem, known as the news vendor, newsboy,
or Christmas tree problem. In fact, this property holds for a large class of
second-stage problems, as will be seen in Chapter 3.
Similar computations can be done for the other two crops. For wheat,
we obtain
Q1(x1) =









47600 −595x1
for x1 ≤200/3,
119 (200−2x1)2
x1
−85 (200−3x1)2
x1
for 200
3 ≤x1 ≤100,
34000 −425x1
for x1 ≥100,
and, for corn, we obtain
Q2(x2) =









50400 −630x2
for x2 ≤200/3,
87.5 (240−2.4x2)2
x2
−62.5 (240−3.6x2)2
x2
for 200/3 ≤x2 ≤100,
36000 −450x2
for x2 ≥100.


## Page 34

1.1 A Farming Example and the News Vendor Problem
15
The global problem is therefore
min 150x1 + 230x2 + 260x3 + Q1(x1) + Q2(x2) + Q3(x3)
s.t. x1 + x2 + x3 ≤500,
x1, x2, x3 ≥0.
Given that the three functions Qi(xi) are convex, continuous, and diﬀer-
entiable functions and the ﬁrst-stage objective is linear, this problem is
a convex program for which Karush-Kuhn-Tucker (K-K-T) conditions are
necessary and suﬃcient for a global optimum. (This result is from nonlinear
programming. For more on this result about optimality, see Section 2.9.)
Denoting by λ the multiplier of the surface constraint and as before by ci
the ﬁrst-stage objective coeﬃcient of crop i, the K-K-T conditions require
xi

ci + ∂Qi(xi)
∂xi
+ λ

= 0, ci + ∂Qi(xi)
∂xi
+ λ ≥0, xi ≥0,
i = 1, 2, 3;
λ[x1 + x2 + x3 −500] = 0, x1 + x2 + x3 ≤500,
λ ≥0.
Assume the optimal solution is such that 100 ≤x1, 200
3
≤x2 ≤100, and
250 ≤x3 ≤375 with λ̸ = 0. Then the conditions read

















−275 + λ = 0,
−76 −1.44 106
x2
2
+ λ = 0,
476 −5.85 107
x2
3
+ λ = 0,
x1 + x2 + x3 = 500.
Solving this system of equations gives λ = 275.00, x1 = 135.83, x2 =
85.07, x3 = 279.10, which satisﬁes all the required conditions and is there-
fore optimal. We observe that this solution is similar to the one obtained
by using the scenario approach, although more surface is devoted to sugar
beet and less to wheat than before. This similarity represents a charac-
teristic robustness of a well-formed stochastic programming formulation.
We shall consider it in more detail in our discussion of approximations in
Chapter 9.
e. The news vendor problem
The previous section illustrates an example of a famous and basic problem
in stochastic optimization, the news vendor problem. In this problem, a
news vendor goes to the publisher every morning and buys x newspapers
at a price of c per paper. This number is usually bounded above by some
limit u, representing either the news vendor’s purchase power or a limit set
by the publisher to each vendor. The vendor then walks along the streets


## Page 35

16
1. Introduction and Examples
to sell as many newspapers as possible at the selling price q. Any unsold
newspaper can be returned to the publisher at a return price r, with r < c.
We are asked to help the news vendor decide how many newspapers
to buy every morning. Demand for newspapers varies over days and is
described by a random variable ξ.
It is assumed here that the news vendor cannot return to the publisher
during the day to buy more newspapers. Other news vendors would have
taken the remaining newspapers. Readers also only want the last edition.
To describe the news vendor’s proﬁt, we deﬁne y as the eﬀective sales
and w as the number of newspapers returned to the publisher at the end
of the day. We may then formulate the problem as
min cx + Q(x)
0 ≤x ≤u,
where
Q(x) = EξQ(x,ξ)
and
Q(x,ξ) = min −qy(ξ) −rw(ξ)
s.t.
y(ξ) ≤ξ,
y(ξ) + w(ξ) ≤x,
y(ξ), w(ξ) ≥0,
where again Eξ denotes the mathematical expectation with respect to ξ.
In this notation, −Q(x) is the expected proﬁt on sales and returns, while
−Q(x,ξ) is the proﬁt on sales and returns if the demand is at level ξ.
The model illustrates the two-stage aspect of the news vendor problem.
The buying decision has to be taken before any information is given on
the demand. When demand is known in the so-called second stage, which
represents the end of the sales period of a given edition, the proﬁt can be
computed. This is done using the following simple rule:
y∗(ξ) = min(ξ, x),
w∗(ξ) = max(x −ξ, 0).
Sales can never exceed the number of available newspapers or the demand.
Returns occur only when demand is less than the number of newspapers
available. The second-stage expected value function is simply
Q(x) = Eξ[−q min(ξ, x) −r max(x −ξ, 0)].
As we will learn later, this function is convex and continuous. It is also dif-
ferentiable when ξ is a continuous random vector. In that case, the optimal


## Page 36

1.1 A Farming Example and the News Vendor Problem
17
solution of the news vendor’s problem is simply:
x = 0 if c + Q′(0) > 0,
x = u if c + Q′(u) < 0,
a solution of c + Q′(x) = 0
otherwise,
where Q′(x) denotes the ﬁrst order derivative of Q(x) evaluated at x.
By construction, Q(x) can be computed as
Q(x) =
 x
−∞
(−qξ −r(x −ξ))dF(ξ) +
 ∞
x
−qx dF(ξ)
= −(q −r)
 x
−∞
ξ dF(ξ) −rx F(x) −qx(1 −F(x)),
where F(ξ) represents the cumulative probability distribution of ξ (see
Section 2.1).
Integrating by parts, we observe that
 x
−∞
ξ dF(ξ) = xF(x) −
 x
−∞
F(ξ)dξ
under mild conditions on the distribution function F(ξ). It follows that
Q(x) = −qx + (q −r)
 x
−∞
F(ξ)dξ.
We may thus conclude that
Q′(x) = −q + (q −r)F(x).
and therefore that the optimal solution is





x∗= 0 if
q−c
q−r < F(0),
x∗= u if
q−c
q−r > F(u),
x∗= F −1( q−c
q−r)
otherwise,
where F −1(α) is the α-quantile of F (see Section 2.1). If F is continuous,
x = F −1(α) means α = F(x). Any reasonable representation of the demand
would imply F(0) = 0 so that the solution is never x∗= 0.
As we shall see in Chapter 3, this problem is an example of a basic type
of stochastic program called the stochastic program with simple recourse.
The ideas of this section can be generalized to larger problems in this class
of examples. Also observe that, as such, we only come to a partial answer,
under the form of an expression for x∗. The vendor may still need to consult
a statistician, who would provide an accurate cumulative distribution F(·).
Only then will a precise ﬁgure be available for x∗.


## Page 37

18
1. Introduction and Examples
Exercises
1. Value of the stochastic solution
Assume the farmer allocates his land according to the solution of
Table 2, i.e., 120 acres for wheat, 80 acres for corn, and 300 acres
for sugar beets. Show that if yields are random (20% below average,
average, and 20% above average for all crops with equal probability
one third), his expected annual proﬁt is $107,240. To do this observe
that planting costs are certain but sales and purchases depend on
the yield. In other words, ﬁll in a table such as Table 5 but with the
ﬁrst-stage decisions given here.
2. Price eﬀect
When yields are good for the farmer, they are usually also good for
many other farmers. The supply is thus increasing, which will lower
the prices. As an example, we may consider prices going down by
10% for corn and wheat when yields are above average and going up
by 10% when yields are below average. Formulate the model where
these changes in prices aﬀect both sales and purchases of corn and
wheat. Assume sugar beet prices are not aﬀected by yields.
3. Binary ﬁrst stage
Consider the case where the farmer possesses four ﬁelds of sizes 185,
145, 105, and 65 acres, respectively. Observe that the total of 500 acres
is unchanged. Now, the ﬁelds are unfortunately located in diﬀerent
parts of the village. For reasons of eﬃciency the farmer wants to
raise only one type of crop on each ﬁeld. Formulate this model as a
two-stage stochastic program with a ﬁrst-stage program with binary
variables.
4. Integer second stage
Consider the case where sales and purchases of corn and wheat can
only be obtained through contracts involving multiples of hundred
tons. Formulate the model as a stochastic program with a mixed-
integer second stage.
5. Consider any one of Exercises 2 to 4. Using standard mixed integer
programming software, obtain an optimal solution of the extensive
form of the stochastic program. Compute the expected value of per-
fect information and the value of the stochastic solution.
6. Multistage program
It is typical in farming to implement crop rotation in order to main-
tain good soil quality. Sugar beets would, for example, appear in
triennial crop rotation, which means they are planted on a given ﬁeld
only one out of three years. Formulate a multistage program to de-
scribe this situation. To keep things simple, describe the case when


## Page 38

1.1 A Farming Example and the News Vendor Problem
19
sugar beets cannot be planted two successive years on the same ﬁeld,
and assume no such rule applies for wheat and corn.
(On a two-year basis, this exercise consists purely of formulation:
with the basic data of the example, the solution is clearly to repeat
the optimal solution in Table 5, i.e., to plant 170 acres of wheat, 80
acres of corn, and 250 acres of sugar beets. The problem becomes
more relevant on a three-year basis. It is also relevant on a two-year
basis with ﬁelds of given sizes as in Exercise 2.
In terms of formulation, it is suﬃcient to consider a three-stage
model. The ﬁrst stage consists of ﬁrst-year planting. The second stage
consists of ﬁrst-year purchases and sales and second-year planting.
The third-stage consists of second-year purchases and sales. Alterna-
tively, a four-stage model can be built, separating ﬁrst-year purchases
and sales from second-year planting. Also discuss the question of dis-
counting the revenues and expenses of the various stages.)
7. Risk aversion
Economic theory tells us that, like many other people, the farmer
would normally act as a risk-averse person. There are various ways
to model risk aversion. One simple way is to plan for the worst case.
More precisely, it consists of maximizing the proﬁt under the worst
situation. Note that for some models, it is not known in advance which
scenario will turn out to induce the lowest proﬁt. In our example,
the worst situation corresponds to Scenario 3 (below average yields).
Planning for the worst case implies the solution of Table 4 is optimal.
(a) Compute the loss in expected proﬁt if that solution is taken.
(b) A median situation would be to require a reasonable proﬁt under
the worst case. Find the solution that maximizes the expected
proﬁt under the constraint that in the worst case the proﬁt does
not fall below $58,000. What is now the loss in expected proﬁt?
(c) Repeat part (b) with other values of minimal proﬁt: $56,000,
$54,000, $52,000, $50,000, and $48,000. Graph the curve of ex-
pected proﬁt loss. Also compare the associated optimal deci-
sions.
8. If prices are also random variables, the problem becomes more com-
plicated. However, if prices and demands are independent random
variables, show that the solution of the news vendor’s problem is the
one obtained before, where q and r are replaced by their expected
values. Indicate under which conditions the same proposition is true
for the farmer’s problem.
9. In the news vendor’s problem, we have assumed for simplicity that
the random variable takes value from −∞to +∞. Show that the


## Page 39

20
1. Introduction and Examples
optimal decisions are insensitive to this assumption, so that if the
random variables have a nonzero density on a limited interval then
the optimal solutions are obtained by the same analytical expression.
10. Suppose c = 10, q = 25, r = 5, and demand is uniform on [50, 150].
Find the optimal solution of the news vendor problem. Also, ﬁnd the
optimal solution of the deterministic model obtained by assuming a
demand of 100. What is the value of the stochastic solution?
1.2
Financial Planning and Control
Financial decision-making problems can often be modeled as stochastic
programs. In fact, the essence of ﬁnancial planning is the incorporation
of risk into investment decisions. The area represents one of the largest
application areas of stochastic programming. Many references can be found
in, for example, Mulvey and Vladimirou [1989, 1991b, 1992], Ziemba and
Vickson [1975], and Zenios [1992].
We consider a simple example that illustrates additional stochastic pro-
gramming properties. As in the farming example of Section 1, this example
involves randomness in the constraint matrix instead of the right-hand side
elements. These random variables reﬂect uncertain investment yields.
This section’s example also has the characteristic that decisions are
highly dependent on past outcomes. In the following capacity expansion
problem of Section 3, this is not the case. In Chapter 3, we deﬁne this
diﬀerence by a block separable recourse property that is present in some
capacity expansion and similar problems.
For the current problem, suppose we wish to provide for a child’s college
education Y years from now. We currently have $b to invest in any of I in-
vestments. After Y years, we will have a wealth that we would like to have
exceed a tuition goal of $G. We suppose that we can change investments
every υ years, so we have H = Y/υ investment periods. For our purposes
here, we ignore transaction costs and taxes on income although these con-
siderations would be important in reality. We also assume that all ﬁgures
are in constant dollars.
In formulating the problem, we must ﬁrst describe our objective in math-
ematical terms. We suppose that exceeding $G after Y years would be
equivalent to our having an income of q% of the excess while not meeting
the goal would lead to borrowing for a cost r% of the amount short. This
gives us the concave utility function in Figure 2. Many other forms of non-
linear utility functions are, of course, possible. See Kallberg and Ziemba
[1983] for a description of their relevance in ﬁnancial planning.
The major uncertainty in this model is the return on each investment i
within each period t. We describe this random variable as ξ(i, t) = ξ(i, t, ω)
where ω is some underlying random element. The decisions on investments


## Page 40

1.2 Financial Planning and Control
21
FIGURE 2. Utility function of wealth at year Y for a goal G.
will also be random. We describe these decisions as x(i, t) = x(i, t, ω). From
the randomness of the returns and investment decisions, our ﬁnal wealth
will also be a random variable.
A key point about this investment model is that we cannot completely
observe the random element ω when we make all our decisions x(i, t, ω). We
can only observe the returns that have already taken place. In stochastic
programming, we say that we cannot anticipate every possible outcome so
our decisions are nonanticipative of future outcomes. Before the ﬁrst period,
this restriction corresponds to saying that we must make ﬁxed investments,
x(i, 1), for all ω ∈Ω, the space of all random elements or, more speciﬁcally,
returns that could possibly occur.
To illustrate the eﬀects of including stochastic outcomes as well as mod-
eling eﬀects from choosing the time horizon Y and the coarseness of the
period approximations H, we use a simple example with two possible in-
vestment types, stocks (i = 1) and government securities (bonds) (i = 2).
We begin by setting Y at 15 years and allow investment changes every ﬁve
years so that H = 3.
We assume that, over the three decision periods, eight possible scenarios
may occur. The scenarios correspond to independent and equal likelihoods
of having (inﬂation-adjusted) returns of 1.25 for stocks and 1.14 for bonds
or 1.06 for stocks and 1.12 for bonds over the ﬁve-year period. We indicate
the scenarios by an index s = 1, . . . , 8, which represents a collection of
the outcomes ω that have common characteristics (such as returns) in a
speciﬁc model. When we wish to allow more general interpretations of the
outcomes, we use the base element ω. With the scenarios deﬁned here, we
assign probabilities for each s, p(s) = 0.125. The returns are ξ(1, t, s) =
1.25, ξ(2, t, s) = 1.14 for t = 1, s = 1, . . . , 4, for t = 2, s = 1, 2, 5, 6, and for
t = 3, s = 1, 3, 5, 7. In the other cases, ξ(1, t, s) = 1.06, ξ(2, t, s) = 1.12.
The eight scenarios are represented by the tree in Figure 3. The scenario
tree divides into branches corresponding to diﬀerent realizations of the
random returns. Because Scenarios 1 to 4, for example, have the same


## Page 41

22
1. Introduction and Examples
FIGURE 3. Tree of scenarios for three periods.


## Page 42

1.2 Financial Planning and Control
23
return for t = 1, they all follow the same ﬁrst branch. Scenarios 1 and
2 then have the same second branch and ﬁnally divide completely in the
last period. To show this more explicitly, we may refer to each scenario by
the history of returns indexed by st for periods t = 1, 2, 3 as indicated on
the tree in Figure 3. In this way, Scenario 1 may also be represented as
(s1, s2, s3) = (1, 1, 1).
With the tree representation, we need only have a decision vector for
each node of the tree. The decisions at t = 1 are just x(1, 1) and x(2, 1)
for the amounts invested in stocks (1) and bonds (2) at the outset. For
t = 2, we would have x(i, 2, s1) where i = 1, 2 for the type of investment
and s1 = 1, 2 for the ﬁrst-period return outcome. Similarly, the decisions
at t = 3 are x(i, 3, s1, s2).
With these decision variables deﬁned, we can formulate a mathematical
program to maximize expected utility. Because the concave utility function
in Figure 1 is piecewise linear, we just need to deﬁne deﬁcit or shortage and
excess or surplus variables, w(i1, i2, i3) and y(i1, i2, i3), and we can maintain
a linear model. The objective is simply a probability- and penalty-weighted
sum of these terms, which, in general, becomes:

sH
. . .

s1
p(s1, . . . , sH)(−rw(s1, . . . , sH) + qy(s1, . . . , sH)).
The ﬁrst-period constraint is simply to invest the initial wealth:

i
x(i, 1) = b.
The constraints for periods t = 2, . . . , H −1 are, for each s1, . . . , st−1:

i
−ξ(i, t −1, s1, . . . , st−1)x(i, t −1, s1, . . . , st−2)
+

i
x(i, t, s1, . . . , st−1) = 0,
while the constraints for period H are:

i
−ξ(i, H, s1, . . . , sH)x(i, H, s1, . . . , sH−1) −y(s1, . . . , sH)
+ w(s1, . . . , sH) = G.
Other constraints restrict the variables to be non-negative.
To specify the model in this example, we use initial wealth, b = 55, 000;
target value, G = 80, 000; surplus reward, q = 1; and shortage penalty,
r = 4. The result is a stochastic program in the following form where the


## Page 43

24
1. Introduction and Examples
units are thousands of dollars:
max z = 	2
s1=1
	2
s2=1
	2
s3=1 0.125(y(s1, s2, s3) −4w(s1, s2, s3))
s. t.
x(1, 1) + x(2, 1)
= 55,
−1.25x(1, 1) −1.14x(2, 1) + x(1, 2, 1) + x(2, 2, 1)
= 0,
−1.06x(1, 1) −1.12x(2, 1) + x(1, 2, 2) + x(2, 2, 2)
= 0,
−1.25x(1, 2, 1) −1.14x(2, 2, 1) + x(1, 3, 1, 1) + x(2, 3, 1, 1) = 0,
−1.06x(1, 2, 1) −1.12x(2, 2, 1) + x(1, 3, 1, 2) + x(2, 3, 1, 2) = 0,
−1.25x(1, 2, 2) −1.14x(2, 2, 2) + x(1, 3, 2, 1) + x(2, 3, 2, 1) = 0,
−1.06x(1, 2, 2) −1.12x(2, 2, 2) + x(1, 3, 2, 2) + x(2, 3, 2, 2) = 0,
1.25x(1, 3, 1, 1) + 1.14x(2, 3, 1, 1) −y(1, 1, 1) + w(1, 1, 1) = 80,
1.06x(1, 3, 1, 1) + 1.12x(2, 3, 1, 1) −y(1, 1, 2) + w(1, 1, 2) = 80,
1.25x(1, 3, 1, 2) + 1.14x(2, 3, 1, 2) −y(1, 2, 1) + w(1, 2, 1) = 80,
1.06x(1, 3, 1, 2) + 1.12x(2, 3, 1, 2) −y(1, 2, 2) + w(1, 2, 2) = 80,
1.25x(1, 3, 2, 1) + 1.14x(2, 3, 2, 1) −y(2, 1, 1) + w(2, 1, 1) = 80,
1.06x(1, 3, 2, 1) + 1.12x(2, 3, 2, 1) −y(2, 1, 2) + w(2, 1, 2) = 80,
1.25x(1, 3, 2, 2) + 1.14x(2, 3, 2, 2) −y(2, 2, 1) + w(2, 2, 1) = 80,
1.06x(1, 3, 2, 2) + 1.12x(2, 3, 2, 2) −y(2, 2, 2) + w(2, 2, 2) = 80,
x(i, t, s1, . . . , st−1) ≥0, y(s1, s2, s3) ≥0, w(s1, s2, s3)
≥0,
for all i, t, s1, s2, s3.
(2.1)
Solving the problem in (2.1) yields an optimal expected utility value of
−1.52. We call this value, RP, for the expected recourse problem solution
value. The optimal solution (in thousands of dollars) appears in Table 6.
In this solution, the initial investment is heavily in stock ($41,500) with
only $13,500 in bonds. Notice the reaction to ﬁrst-period outcomes, how-
ever. In the case of Scenarios 1 to 4, stocks are even more prominent, while
Scenarios 5 to 8 reﬂect a more conservative government security portfo-
lio. In the last period, notice how the investments are either completely in
stocks or completely in bonds. This is a general trait of one-period deci-
sions. It occurs here because in Scenarios 1 and 2, there is no risk of missing
the target. In Scenarios 3 to 6, stock investments may cause one to miss the
target, so they are avoided. In Scenarios 7 and 8, the only hope of reaching
the target is through stocks.
We compare the results in Table 6 to a deterministic model in which all
random returns are replaced by their expectation. For that model, because
the expected return on stock is 1.155 in each period, while the expected
return on bonds is only 1.13 in each period, the optimal investment plan
places all funds in stocks in each period. If we implement this policy each
period, but instead observed the random returns, we would have an ex-
pected utility called the expected value solution, or EV. In this case, we
would realize an expected utility of EV = −3.79, while the stochastic pro-
gram value is again RP = −1.52. The diﬀerence between these quantities
is the value of the stochastic solution:
V SS = RP −EV = −1.52 −(−3.79) = 2.27.


## Page 44

1.2 Financial Planning and Control
25
TABLE 6. Optimal solution with three-period stochastic program.
Period, Scenario
Stock
Bonds
1,1-8
41.5
13.50
2,1-4
65.1
2.17
2,5-8
36.7
22.40
3,1-2
83.0
0.00
3,3-4
0.0
71.40
3,5-6
0.0
71.40
3,7-8
64.0
0.00
Scenario
Above G
Below G
1
24.80
0.0
2
8.87
0.0
3
1.42
0.0
4
0.00
0.0
5
1.42
0.0
6
0.00
0.0
7
0.00
0.0
8
0.00
12.2
This comparison gives us a measure of the utility value in using a deci-
sion from a stochastic program compared to a decision from a determin-
istic program. Another comparison of models is in terms of the probabil-
ity of reaching the goal. Models with these types of objectives are called
chance-constrained programs or programs with probabilistic constraints (see
Charnes and Cooper [1959] and Pr´ekopa [1973]). Notice that the stochastic
program solution reaches the goal 87.5% of the time. The expected value
deterministic model solution only reaches the goal 50% of the time. In this
case, the value of the stochastic solution may be even more signiﬁcant.
The formulation we gave in (2.1) can become quite cumbersome as the
time horizon, H, increases and the decision tree of Figure 3 grows quite
bushy. Another modeling approach to this type of multistage problem is
to consider the full horizon scenarios, s, directly, without specifying the
history of the process. We then substitute a scenario set S for the random
elements Ω. Probabilities, p(s), returns, ξ(i, t, s), and investments, x(i, t, s),
become functions of the H-period scenarios and not just the history until
period t.
The diﬃculty is that, when we have split up the scenarios, we may
have lost nonanticipativity of the decisions because they would now in-
clude knowledge of the outcomes up to the end of the horizon. To enforce
nonanticipativity, we add constraints explicitly in the formulation. First,
the scenarios that correspond to the same set of past outcomes at each
period form groups, St
s1,...,st−1, for scenarios at time t. Now, all actions up


## Page 45

26
1. Introduction and Examples
to time t must be the same within a group. We do this through an explicit
constraint. The new general formulation of (2.1) becomes:
max z =

s
p(s)(qy(s) −rw(s))
s. t.
I

i=1
x(i, 1, s)= b, ∀s ∈S,
I

i=1
ξ(i, t, s)x(i, t −1, s) −
I

i=1
x(i, t, s)= 0, ∀s ∈S,
t = 2, . . . , H,
I

i=1
ξ(i, H, s)x(i, H, s) −y(s) + w(s)= G,
(

s′∈St
J(s,t)
p(s′)x(i, t, s′))−(

s′∈St
J(s,t)
p(s′))x(i, t, s) = 0,
∀1 ≤i ≤I, ∀1 ≤t ≤H, ∀s ∈S,
x(i, t, s) ≥0, y(s) ≥0,w(s) ≥0,
∀1 ≤i ≤I,∀1 ≤t ≤H, ∀s ∈S,
(2.2)
where J(s, t) = {s1, . . . , st−1} such that s ∈St
s1,...,st−1. Note that the last
equality constraint indeed forces all decisions within the same group at
time t to be the same. Formulation 2.2 has a special advantage for the
problem here because these nonanticipativity constraints are the only con-
straints linking the separate scenarios. Without them, the problem would
decompose into a separate problem for each s, maintaining the structure
of that problem.
In modeling terms, this simple additional constraint makes it relatively
easy to move from a deterministic model to a stochastic model of the same
problem. This ease of conversion can be especially useful in modeling lan-
guages. For example, Figure 4 gives a complete AMPL (Fourer, Gay, and
Kernighan [1993]) model of the problem in (2.2). In this language, set,
param, and var are keywords for sets, parameters, and variables. The ad-
dition of the scenario indicators and nonanticipativity constraints (nonan-
ticip) are the only additions to a deterministic model.
Given the ease of this modeling eﬀort, standard optimization procedures
can be simply applied to this problem. However, as we noted earlier, the
number of scenarios can become extremely large. Standard methods may
not be able to solve the problem in any reasonable amount of time, necessi-
tating other techniques. The remaining chapters in this book focus on these
other methods and on procedures for creating models that are amenable
to those specialized techniques.
In ﬁnancial problems, it is particularly worthwhile to try to exploit the
underlying structure of the problem without the nonanticipativity con-
straints. This relaxed problem is in fact a generalized network that allows


## Page 46

1.2 Financial Planning and Control
27
# This problem describes a simple financial planning problem
# for financing college education
set investments; # different investment options
param initwealth; # initial holdings
param scenarios; # number of scenarios (total S)
# The following 0-1 array shows which scenarios are combined at period T
param scen links{1..scenarios,1..scenarios,1..T};
param target; # target value G at time T
param H; # number of periods
param invest; # value of investing beyond target value
param penalty; # penalty for not meeting target
param return {investments,1..scenarios,1..T}; # return on each inv
param prob {1..scenarios}; # probability of each scenario
# variables
var amtinvest{investments,1..scenarios,1..T} ¿= 0; #actual amounts inv’d
var above target{1..scenarios}¿= 0; # amt above final target
var below target{1..scenarios} ¿= 0; # amt below final target
# objective
maximize exp value : sum{i in 1..scenarios} prob[i]*(invest*above target[i]
- penalty*below target[i]);
# constraints
subject to budget{i in 1..scenarios} :
sum{k in investments}(amtinvest[k,i,1]) = initwealth;#invest initial wealth
subject to nonanticip{k in investments,j in 1..scenarios,H in 1..T}:
(sum{i in 1..scenarios}scen links[j,i,H]*prob[i]*amtinvest[k,i,H]) -
(sum{i in 1..scenarios}scen links[j,i,H]*prob[i])*
amtinvest[k,j,H] = 0; # makes all investments nonanticipative
subject to balance{j in 1..scenarios, t in 1..T-1}:
(sum{k in investments}return[k,j,H]*amtinvest[k,j,H]) - sum{k in
investments} amtinvest[k,j,H+1] = 0; # reinvest each time period
subject to scenario value{j in 1..scenarios}: (sum{k in
investments}return[k,j,H]*amtinvest[k,j,H]) - above target[j] +
below target[j] = target; # amounts not meeting target
FIGURE 4. AMPL format of ﬁnancial planning model.


## Page 47

28
1. Introduction and Examples
the use of eﬃcient network optimization methods that cannot apply to the
full problem in (2.2). We discuss this option more thoroughly in Chapters
5 and 7.
With either formulation (2.1) or (2.2), in completing the model, some
decisions must be made about the possible set of outcomes or scenarios and
the coarseness of the period structure, i.e., the number of periods H allowed
for investments. We must also ﬁnd probabilities to attach to outcomes
within each of these periods. These probabilities are often approximations
that can, as we shall see in Chapter 9, provide bounds on true values
or on uncertain outcomes with incompletely known distributions. A key
observation is that the important step is to include stochastic elements
at least approximately and that deterministic solutions most often give
misleading results.
In closing this section, note that the mathematical form of this prob-
lem actually represents a broad class of control problems (see, for example,
Varaiya and Wets [1989]). In fact, it is basically equivalent to any control
problem governed by a linear system of diﬀerential equations. We have
merely taken a discrete time approach to this problem. This approach can
be applied to the control of a wide variety of electrical, mechanical, chemi-
cal, and economic systems. We merely redeﬁne state variables (now, wealth)
in each time period and controls (investment levels). The random gain or
loss is reﬂected in the return coeﬃcients. Typically, these types of control
problems would have nonlinear (e.g., quadratic) costs associated with the
control in each time period. This presents no complication for our purposes,
so we may include any of these problems as potential applications. In the
last section, we will look at a fundamentally nonlinear problem in more
detail.
Exercises
1. Suppose you consider just a ﬁve-year planning horizon. Choose an
appropriate target and solve over this horizon with a single ﬁrst-
period decision.
2. Suppose that goal G is also a random parameter and could be $75,000
or $85,000 with equal probabilities. Formulate and solve this problem.
Compare this solution to the solution for the problem with a known
target.
1.3
Capacity Expansion
Capacity expansion models optimal choices of the timing and levels of in-
vestments to meet future demands of a given product. This problem has
many applications. Here we illustrate the case of power plant expansion


## Page 48

1.3 Capacity Expansion
29
for electricity generation: we want to ﬁnd optimal levels of investment in
various types of power plants to meet future electricity demand.
We ﬁrst present a static deterministic analysis of the electricity genera-
tion problem. Static means that decisions are taken only once. Determin-
istic means that the future is supposed to be fully and perfectly known.
Three properties of a given power plant i can be singled out in a static
analysis: the investment cost ri, the operating cost qi, and the availability
factor ai, which indicates the percent of time the power plant can eﬀectively
be operated. Demand for electricity can be considered a single product,
but the level of demand varies over time. Analysts usually represent the
demand in terms of a so-called load duration curve that describes the de-
mand over time in decreasing order of demand level (Figure 5). The curve
gives the time, τ, that each demand level, D, is reached. Because here we
are concerned with investments over the long run, the load duration curve
we consider is taken over the life cycle of the plants.
The load duration curve can be approximated by a piecewise constant
curve (Figure 6) with m segments. Let d1 = D1, dj = Dj −Dj−1, j =
2, . . . , m represent the additional power demanded in the so-called mode j
for a duration τj. To obtain a good approximation of the load curve, it is
necessary to consider large values of m. In the static situation, the problem
consists of ﬁnding the optimal investment for each mode j, i.e., to ﬁnd the
particular type of power plant i, i = 1, . . . , n, that minimizes the total cost
of eﬀectively producing 1 MW of electricity during the time τj. It is given
by
i(j) = arg
min
i=1,...,n

ri + qi τj
ai

,
(3.1)
where n is the number of available technologies and arg min represents the
index i for which the minimum is achieved.
The static model (3.1) captures one essential feature of the problem,
namely, that base load demand (associated with large values of τj, i.e.,
small indices j) is covered by equipment with low operating costs (scaled by
availability factor), while peak-load demand (associated with small values
of τj, i.e., large indices j) is covered by equipment with low investment
costs (also scaled by their availability factor). For the sake of completeness,
peak-load equipment should also oﬀer operational ﬂexibility.
At least four elements justify considering a dynamic or multistage model
for the electricity generation investment problem:
• the long-term evolution of equipment costs;
• the long-term evolution of the load curve;
• the appearance of new technologies;
• the obsolescence of currently available equipment.


## Page 49

30
1. Introduction and Examples
FIGURE 5. The load duration curve.
FIGURE 6. A piecewise constant approximation of the load duration curve.


## Page 50

1.3 Capacity Expansion
31
The equipment costs are inﬂuenced by technological progress but also (and,
for some, drastically) by the evolution of fuel costs.
Of signiﬁcant importance in the evolution of demand is both the total
energy demanded (the area under the load curve) and the peak-level Dm,
which determines the total capacity that should be available to cover de-
mand. The evolution of the load curve is determined by several factors,
including the level of activity in industry, energy savings in general, and
the electricity producers’ rate policy.
The appearance of new technologies depends on the technical and com-
mercial success of research and development while obsolescence of available
equipment depends on past decisions and the technical lifetime of equip-
ment. All the elements together imply that it is no longer optimal to invest
only in view of the short-term ordering of equipment given by (3.1) but
that a long-term optimal policy should be found.
The following multistage model can be proposed. Let
• t = 1, . . . , H index the periods or stages;
• i = 1, . . . , n index the available technologies;
• j = 1, . . . , m index the operating modes in the load duration curve.
Also deﬁne the following:
• ai = availability factor of i;
• Li = lifetime of i;
• gt
i = existing capacity of i at time t, decided before t = 1;
• rt
i = unit investment cost for i at time t (assuming a ﬁxed plant life
cycle for each type i of plant);
• qt
i = unit production cost for i at time t;
• dt
j = maximal power demanded in mode j at time t;
• τ t
j = duration of mode j at time t.
Consider, ﬁnally, the set of decisions
• xt
i = new capacity made available for technology i at time t;
• wt
i = total capacity of i available at time t;
• yt
ij = capacity of i eﬀectively used at time t in mode j.
The electricity generation H-stage problem can be deﬁned as
min
x,y,w
H

t=1


n

i=1
rt
i · wt
i +
n

i=1
m

j=1
qt
i · τ t
j · yt
ij


(3.2)


## Page 51

32
1. Introduction and Examples
subject to wt
i = wt−1
i
+ xt
i −xt−Li
i
, i = 1, . . . , n,
t = 1, . . . , H,
(3.3)
n

i=1
yt
ij = dt
j, j = 1, . . . , m,
t = 1, . . . , H,
(3.4)
m

j=1
yt
ij ≤ai(gt
i + wt
i), i = 1, . . . , n,
t = 1, . . . , H,
(3.5)
x, y, w ≥0.
Decisions in each period t involve new capacities xt
i made available in each
technology and capacities yt
ij operated in each mode for each technology.
Newly decided capacities increase the total capacity wt
i made available,
as given by (3.3), where the equipment’s becoming obsolete after its lifetime
is also considered. We assume xt
i = 0 if t ≤0, so equation (3.3) only involves
newly decided capacities.
By (3.4), the optimal operation of equipment must be chosen to meet
demand in all modes using available capacities, which by (3.5) depend on
capacities gt
i decided before t = 1, newly decided capacities xt
i, and the
availability factor.
The objective function (3.2) is the sum of the investment plus main-
tenance costs and operating costs. Compared to (3.1), availability factors
enter constraints (3.5) and do not need to appear in the objective function.
The operating costs are exactly the same and are based on operating deci-
sions yt
ij, while the investment annuities and maintenance costs rt
i apply on
the cumulative capacity wt
i. Placing annuities on the cumulative capacity,
instead of charging the full investment cost to the decision xt
i, simpliﬁes
the treatment of end of horizon eﬀects and is currently used in many power
generation models. It is a special case of the salvage value approach and
other period aggregations discussed in Section 11.2.
The same reasons that plead for the use of a multistage model motivate
resorting to a stochastic model. The evolution of equipment costs, partic-
ularly fuel costs, the evolution of total demand, the date of appearance of
new technologies, even the lifetime of existing equipment, can all be con-
sidered truly random. The main diﬀerence between the stochastic model
and its deterministic counterpart is in the deﬁnition of the variables xt
i and
wt
i. In particular, xt
i now represents the new capacity of i decided at time t,
which becomes available at time xt+∆i
i
, where ∆i is the construction delay
for equipment i. In other words, to have extra capacity available at time
t, it is necessary to decide at t −∆i, when less information is available on
the evolution of demand and equipment costs. This is especially important
because it would be preferable to be able to wait until the last moment to
take decisions that would have immediate impact.
Assume that each decision is now a random variable. Instead of writing
an explicit dependence on the random element, ω, we use boldface notation
to denote random variables. We then have:
• xt
i = new capacity decided at time t for equipment i, i = 1, . . . , n;


## Page 52

1.3 Capacity Expansion
33
• wt
i = total capacity of i available and in order at time t;
• ξ = the vector of random parameters at time t;
and all other variables as before. The stochastic model is then
min Eξ
H

t=1


n

i=1
rt
iwt
i +
n

i=1
m

j=1
qt
i τ t
j yt
ij


(3.6)
s. t. wt
i = wt−1
i
+ xt
i −xt−Li
i
, i = 1, . . . , n, t = 1, . . . , H,
(3.7)
n

i=1
yt
ij = dt
j, j = 1, . . . , m, t = 1, . . . , H,
(3.8)
m

j=1
yt
ij ≤ai(gt
i + wt−∆i
i
), i = 1, . . . , n, t = 1, . . . , H,
(3.9)
w, x, y ≥0,
where the expectation is taken with respect to the random vector ξ =
(ξ2, . . . ,ξH). Here, the elements forming ξt are the demands, (dt
1, . . . , dt
k),
and the cost vectors, (rt, qt). In some cases, ξt can also contain the lifetimes
Li, the delay factors ∆i, and the availability factors ai, depending on the
elements deemed uncertain in the future.
Formulation (3.6)–(3.9) is a convenient representation of the stochastic
program. At some point, however, this representation might seem a little
confusing. For example, it seems that the expectation is taken only on the
objective function, while the constraints contain random coeﬃcients (such
as dt
j in the right-hand side of (3.8)).
Another important aspect is the fact that decisions taken at time t,
(wt, yt), are dependent on the particular realization of the random vector,
ξt, but cannot depend on future realizations of the random vector. This is
clearly a desirable feature for a truly stochastic decision process. If demands
in several periods are high, one would expect investors to increase capacity
much more than if, for example, demands remain low.
Formally, if the decision variables (wt, yt) were not dependent on ξt, the
objective function in (3.6) could be replaced by

t

i

Eξrt
i wt
i +

j
Eξ qt
i τ t
i yt
ij


=

t

i

¯rt
i · wt
i +

j
(qiτj)yt
ij

,


## Page 53

34
1. Introduction and Examples
where ¯rt
i = Eξrt
i and qiτj = Eξ(qt
i τ t
j), making problem (3.6) to (3.9)
deterministic. In the next section, we will make the dependence of the
decision variables on the random vector explicit.
The formulation given earlier is convenient in its allowing for both con-
tinuous and discrete random variables. Theoretical properties such as con-
tinuity and convexity can be derived for both types of variables. Solution
procedures, on the other hand, strongly diﬀer.
Problem (3.6) to (3.9) is a multistage stochastic linear program with
several random variables that actually has an additional property, called
block separable recourse. This property stems from a separation that can be
made between the aggregate-level decisions, (xt, wt), and the detailed-level
decisions, yt.
We will formally deﬁne block separability in Chapter 3, but we can make
an observation about its eﬀect here. Suppose future demands are always
independent of the past. In this case, the decision on capacity to install
in the future at some t only depends on available capacity and does not
depend on the outcomes up to time t. The same xt must then be optimal
for any realization of ξ. The only remaining stochastic decision is in the
operation-level vector, yt, which now depends separately on each period’s
capacity. The overall result is that a multiperiod problem now becomes a
much less complex two-period problem.
As a simple example, consider the following problem that appears in
Louveaux and Smeers [1988]. In this case, the resulting two period model
has three operating modes, n = 4 technologies, ∆i = 1 period of construc-
tion delay, full availabilities, a ≡1, and no existing equipment, g ≡0.
The only random variable is d1 = ξ. The other demands are d2 = 3 and
d3 = 2. The investment costs are r1 = (10, 7, 16, 6)T with production costs
q2 = (4, 4.5, 3.2, 5.5)T and load durations τ 2 = (10, 6, 1)T . We also add
a budget constraint to keep all investment below 120. The resulting two-
period stochastic program is:
min 10x1
1 + 7x1
2 + 16x1
3 + 6x1
4+Eξ[
3

j=1
τ 2
j (4y2
1j + 4.5y2
2j
+3.2y2
3j + 5.5y2
4j)]
s. t. 10x1
1 + 7x1
2 + 16x1
3 + 6x1
4≤120,
−x1
i +
3

j=1
y2
ij≤0, i = 1, . . . , 4,
y

i=1
y2
i1= ξ,
y

i=1
y2
ij= d2
j, j = 2, 3,
x1
1 ≥0, x1
2 ≥0, x1
3 ≥0, x1
4 ≥0, y2
ij ≥0, i = 1, . . . , 4, j = 1, 2, 3.
(3.10)


## Page 54

1.3 Capacity Expansion
35
Assuming that ξ takes on the values 3, 5, and 7 with probabilities 0.3, 0.4,
and 0.3, respectively, an optimal stochastic programming solution to (3.10)
includes x1∗= (2.67, 4.00, 3.33, 2.00)T with an optimal objective value of
381.85. We can again consider the expected value solution, which would
substitute ξ ≡5 in (3.10). An optimal solution here (again not unique)
is ¯x1 = (0.00, 3.00, 5.00, 2.00)T . The objective value, if this single event
occurs, is 365. However, if we use this solution in the stochastic problem,
then with probability 0.3, demand cannot be met. This would yield an
inﬁnite value of the stochastic solution.
Inﬁnite values probably do not make sense in practice because an action
can be taken somehow to avoid total system collapse. The power com-
pany could buy from neighboring utilities, for example, but the cost would
be much higher than any company operating cost. An alternative tech-
nology (internal or external to the company) that is always available at
high cost is called a backstop technology. If we assume, for example, in
problem (3.10) that some other technology is always available, without any
required investment costs at a unit operating cost of 100, then the expected
value solution would be feasible and have an expected stochastic program
value of 427.82. In this case, the value of the stochastic solution becomes
427.82 −381.85 = 45.97.
In many power problems, focus is on the reliability of the system or
the system’s ability to meet demand. This reliability is often described
as expressing a minimum probability for meeting demand using the non-
backstop technologies. If these technologies are 1, . . . , n −1, then the relia-
bility restriction (in the two-period situation where capacity decisions need
not be random) is:
P[
n−1

i=1
ai(gt
i + wt
i) ≥
m

j=1
dt
j] ≥α, ∀t,
(3.11)
where 0 < α ≤1. Inequality (3.11) is called a chance or probabilistic
constraint in stochastic programming. In production problems, these con-
straints are often called ﬁll rate or service rate constraints. They place
restrictions on decisions so that constraint violations are not too frequent.
Hence, we would often have α quite close to 1.
If the only probabilistic constraints are of the form in (3.11), then we
simply want the cumulative available capacity at time t to be at least the
α quantile of the cumulative demand in all modes at time t. We then obtain
a deterministic equivalent constraint to (3.11) of the following form:
n−1

i=1
ai(gt
i + wt
i) ≥(F t)−1(α), ∀t,
(3.12)
where F t is the (assumed continuous) distribution function of 	m
j=1 dt
j and
F −1(α) is the α-quantile of F. Constraints of the form in (3.12) can then


## Page 55

36
1. Introduction and Examples
be added to (3.6) to (3.9) or, indeed, to the deterministic problem in (3.2)
to (3.5), where expected values replace the random variables.
By adding these chance constraint equivalents, many of the problems of
deterministic formulations can be avoided. For example, if we choose α =
0.7 for the problem in (3.10), then adding a constraint of the form in (3.12)
would not change the deterministic expected value solution. However, we
would get a diﬀerent result if we set α = 1.0. In this case, constraint (3.12)
for the given data becomes simply:
4

i=1
w1
i ≥12.
(3.13)
Adding (3.13) to the expected value problem results in an optimal solu-
tion with w1∗= (0.833, 3.00, 4.17, 4.00)T . The expected value of using this
solution in the stochastic program is 383.99, or only 2.14 more than the
optimal value in (3.10).
In general, probabilistic constraints are represented by deterministic
equivalents and are often included in stochastic programs. We discuss some
of the theory of these constraints in Chapter 3. Our emphasis in this book
is, however, on optimizing the expected value of continuous utility func-
tions, such as the costs in this capacity expansion problem. We, therefore,
concentrate on recourse problems and assume that probabilistic constraints
are represented by deterministic equivalents within our formulations.
This problem illustrates a multistage decision problem and the addition
of probabilistic constraints. The structure of the problem, however, allows
for a two-stage equivalent problem. In this way, the capacity expansion
problem provides a bridge between the two-stage example of Section 1 and
the multistage problem of Section 2.
This problem also has a natural interpretation with discrete decision
variables. For most producing units, only a limited number of possible
sizes exists. Typical sizes for high-temperature nuclear reactors would be
1000 MW and 1300 MW, so that capacity decisions could only be taken as
integer multiples of these values.
Exercises
1. The detailed-level decisions can be found quite easily according to an
order of merit rule. In this case, one begins with mode 1 and uses the
least expensive equipment until its capacity is exhausted or demand
is satisﬁed. One continues to exhaust capacity or satisfy demand in
order of increasing unit operating cost and mode. Show that this
procedure is indeed optimal for determining the yt
ij values.
2. Prove that, in the case of no serial correlation (ξt and ξt+1 stochas-
tically independent), an optimal solution has the same value for wt


## Page 56

1.4 Design for Manufacturing Quality
37
and xt for all ξ. Give an example where this does not occur with
serial correlation.
3. For the example in (3.10), suppose we add a reliability constraint
of the form in (3.13) to the expected value problem, but we use a
right-hand side of 11 instead of 12. What is the stochastic program
expected value of this solution?
1.4
Design for Manufacturing Quality
This section illustrates a common engineering problem that we model as
a stochastic program. The problem demonstrates nonlinear functions in
stochastic programming and provides further evidence of the importance
of the stochastic solution.
Consider a designer deciding various product speciﬁcations to achieve
some measure of product cost and performance. The speciﬁcations may
not, however, completely determine the characteristics of each manufac-
tured product. Key characteristics of the product are often random. For
example, every item includes variations due to machining or other process-
ing. Each consumer also does not use the product in the same way. Cost
and performance characteristics thus become random variables.
Deterministic methods may yield costly results that are only discovered
after production has begun. From this experience, designing for quality and
consideration of variable outcomes has become an increasingly important
aspect of modern manufacturing (see, for example, Taguchi et al. [1989]). In
industry, the methods of Taguchi have been widely used (see also Taguchi
[1986]). Taguchi methods can, in fact, be seen as examples of stochastic
programming, although they are often not described this way.
In this section, we wish to give a small example of the uses of stochas-
tic programming in manufacturing design and to show how the general
stochastic programming approach can be applied. We note that we base
our analysis on actual performance measures, whereas the Taguchi meth-
ods generally attach surrogate costs to deviations from nominal parameter
values.
We consider the design of a simple axle assembly for a bicycle cart. The
axle has the general appearance in Figure 7.
The designer must determine the speciﬁed length w and design diame-
ter ξ of the axle. We use inches to measure these quantities and assume
that other dimensions are ﬁxed. Together, these quantities determine the
performance characteristics of the product. The goal is to determine a com-
bination that gives the greatest expected proﬁt.
The initial costs are for manufacturing the components. We assume that
a single process is used for the two components. No alternative technologies
are available, although, in practice, several processes might be available.


## Page 57

38
1. Introduction and Examples
FIGURE 7. An axle of length w and diameter ξ with a central load L.
When the axle is produced, the actual dimensions are not exactly those
that are speciﬁed. For this example, we suppose that the length w can
be produced exactly but that the diameter ξ is a random variable, ξ(x),
that depends on a speciﬁed mean value, x, that represents, for example,
the setting on a machine. We assume a triangular distribution for ξ(x) on
[0.9x, 1.1x]. This distribution has a density,
fx(ξ) =
 (100/x2)(ξ −0.9x)
if 0.9x ≤ξ < x,
(100/x2)(1.1x −ξ)
if x ≤ξ ≤1.1x,
0
otherwise.
(4.1)
The decision is then to determine w and x, subject to certain limits, w ≤
wmax and x ≤xmax, in order to maximize expected proﬁts. For revenues, we
assume that if the product is proﬁtable, we sell as many as we can produce.
This amount is ﬁxed by labor and equipment regardless of the size of the
axle. We, therefore, only wish to determine the maximum selling price that
generates enough demand for all production. From marketing studies, we
determine that this maximum selling price depends on the length and is
expressed as
r(1 −e−0.1w),
(4.2)
where r is the maximum possible for any such product.
Our production costs for labor and equipment are assumed ﬁxed, so
only material cost is variable. This cost is proportional to the mean values
of the speciﬁed dimensions because material is acquired before the actual
machining process. Suppose c is the cost of a single axle material unit. The
total manufacturing cost for an item is then
c(wπx2
4
).
(4.3)
In this simpliﬁed model, we assume that no quantity discounts apply in the
production process.
Other costs are incurred after the product is made due to warranty claims
and potential future sales losses from product defects. These costs are of-
ten called quality losses. In stochastic programming terms, these are the
recourse costs. Here, the product may perform poorly if the axle becomes


## Page 58

1.4 Design for Manufacturing Quality
39
bent or broken due to excess stress or deﬂection. The stress limit, assuming
a steel axle and 100-pound maximum central load, is
w
ξ3 ≤39.27.
(4.4)
For deﬂection, we use a maximum 2000-rpm speed (equivalent to a speed
of 60 km/hour for a typical 15-centimeter wheel) to obtain:
w3
ξ4 ≤63, 169.
(4.5)
When either of these constraints is violated, the axle deforms. The expected
cost for not meeting these constraints is assumed proportional to the square
of the violation. We express it as
Q(w, x, ξ) = min
y {qy2 s. t. w
ξ3 −y ≤39.27, w3
ξ4 −300y ≤63, 169},
(4.6)
where y is, therefore, the maximum of stress violation and (to maintain
similar units)
1
300 of the deﬂection violation.
The expected cost, given w and x, is
Q(w, x) =

ξ
Q(w, x, ξ)fx(ξ)dξ,
(4.7)
which can be written as:
Q(w, x) = q
 1.1x
.9x
(100/x2) min{ξ −.9x, 1.1x −ξ}
[max{0, ( w
ξ3 ) −39.27, ( w3
300ξ4 ) −210.56}]2dξ.
(4.8)
The overall problem is to ﬁnd:
max (total revenue per item −manufacturing cost per item
−expected future cost per item).
(4.9)
Mathematically, we write this as:
max z(w, x) = r(1 −e−0.1w)−c(wπx2
4
) −Q(w, x)
s. t. 0 ≤w ≤wmax, 0 ≤x ≤xmax.
(4.10)
In stochastic programming terms, this formulation gives the determinis-
tic equivalent problem to the stochastic program for minimizing the cur-
rent value for the design decision plus future reactions to deviations in
the axle diameter. Standard optimization procedures can be used to solve


## Page 59

40
1. Introduction and Examples
this problem. Assuming maximum values of wmax = 36, xmax = 1.25, a
maximum sales price of $10 (r = 10), a material cost of $0.025 per cubic
inch (c = .025), and a unit penalty q = 1, an optimal solution is found
at w∗= 33.6, x∗= 1.038, and z∗= z(w∗, x∗) = 8.94. The graphs of z as
a function of w for x = x∗and as a function of x for w = w∗appear in
Figures 8 and 9. In this solution, the stress constraint is only violated when
.9x = 0.934 ≤ξ ≤0.949 = (w/39.27)1/3.
FIGURE 8. The expected unit proﬁt as a function of length with a diameter of
1.038 inches.
FIGURE 9. The expected unit proﬁt as a function of diameter with a length of
33.6 inches.
We again consider the expected value problem where random variables
are replaced with their means to obtain a deterministic problem. For this


## Page 60

1.4 Design for Manufacturing Quality
41
problem, we would obtain:
max z(w, x, ¯ξ) =r(1 −e−0.1w) −c(wπx2
4
)
−[max{0, ( w
x3 ) −39.27, ( w3
300x4 ) −210.56}]2
s. t. 0 ≤w ≤wmax, 0 ≤x ≤xmax.
(4.11)
Using the same data as earlier, an optimal solution to (4.11) is ¯w(¯ξ) =
35.0719, ¯x(¯ξ) = 0.963, and z( ¯w, ¯x, ¯ξ) = 9.07.
At ﬁrst glance, it appears that this solution obtains a better expected
proﬁt than the stochastic problem solution. However, as we shall see in
Chapter 9 on approximations, this deterministic problem paints an overly
optimistic picture of the actual situation. The deterministic objective is
(in the case of concave maximization) always an overestimate of the actual
expected proﬁt. In this case, the true expected value of the determinis-
tic solution is z( ¯w, ¯x) = −26.79. This problem then has a value of the
stochastic solution equal to the diﬀerence between the expected value of
the stochastic solution and the expected value of the deterministic solution,
z∗−z( ¯w, ¯x) = 35.73. In other words, solving the stochastic program yields
an expected proﬁt increase over solving the deterministic problem.
This problem is another example of how stochastic programming can be
used. The problem has nonlinear functions and a simple recourse structure.
We will discuss further computational methods for problems of this type
in Chapter 6. In other problems, decisions may also be taken after the
observation of the outcome. For example, we could inspect and then decide
whether to sell the product (Exercise 3). This often leads to tolerance
settings and is the focus of much of quality control.
The general stochastic program provides a framework for uniting design
and quality control. Many loss functions can be used to measure perfor-
mance degradation to help improve designs in their initial stages. These
functions may include the stress and performance penalties described ear-
lier, the Taguchi-type quadratic loss, or methods based on reliability char-
acterizations.
Most traditional approaches assume some form for the distribution as we
have done here. This situation rarely matches practice, however. Approxi-
mations can nevertheless be used that obtain bounds on the actual solution
value so that robust decisions may be made without complete distributional
information. This topic will be discussed further in Chapter 9.
Exercises
1. For the example given, what is the probability of exceeding the stress
constraint for an axle designed according to the stochastic program
optimal speciﬁcations?


## Page 61

42
1. Introduction and Examples
2. Again, for the example given, what is the probability of exceeding the
stress constraint for an axle designed according to the deterministic
program’s (4.11) optimal speciﬁcations?
3. Suppose that every axle can be tested before being shipped at a
cost of s per test. The test completely determines the dimensions
of the product and thus informs the producer of the risk of failure.
Formulate the new problem with testing.
1.5
Other Applications
In this chapter, we discussed a few examples of stochastic programming ap-
plications. The examples were chosen because of their frequency in stochas-
tic programming application as well as to illustrate various aspects of
stochastic programming models in terms of number of stages, continuous
or discrete variables, separable or nonseparable recourse, probabilistic con-
straints, and linear or nonlinear constraint and objective functions.
Several other application areas deserve some recognition but were not
discussed yet. A particular example is in airline planning. One of the ﬁrst
applications of stochastic programming was a decision on the allocation
of aircraft to routes (ﬂeet assignment) by Ferguson and Dantzig [1956].
In this problem, penalties were incurred for lost passengers. The problem
becomes a simple recourse problem in stochastic programming terms that
they solved using a variant of the standard transportation simplex method.
Production planning is another major area that was not in our examples.
This area also has been the subject of stochastic programming models
for many years. The original chance-constrained stochastic programming
model of Charnes, Cooper, and Symonds [1958], for example, considered
the production of heating oil with constraints on meeting sales and not
exceeding capacity. More recent examples include the study by Escudero
et al. [1993] for IBM procurement policies.
Water resource modeling has also received widespread application. A
good example of this area is the paper by Pr´ekopa and Sz´antai [1976],
where they discuss regulation of Lake Balaton’s water level and show how
stochastic programming could have avoided ﬂoods that occurred before
such planning methods were available. Approaches to pollution and the
environmental area of water resource planning are also common. An exam-
ple discussion appears in Somly´ody and Wets [1988].
Energy planning has been the focus of many stochastic programming
studies. We note in particular Manne’s [1974] analysis of the U.S. decision
on whether to invest in breeder reactors. The more recent work of Manne
and Richels [1992] on buying insurance against the greenhouse eﬀect is also
an excellent example of how stochastic programming can model uncertain
future situations so that informed public policy decisions may be made.


## Page 62

1.5 Other Applications
43
Stochastic programming has been applied in many other areas. Of par-
ticular note is the forestry planning model in Gassmann ([1989]) and the
hospital staﬃng problem in Kao and Queyranne ([1985]). We also include
two exercises in stochastic programming in sports. Many other references
appear in King’s survey (King [1988b]) in the volume by Ermoliev and
Wets [1988]. Many more applications are open to stochastic programming,
especially with the powerful techniques now available. In the remainder of
this book, we will explore those methods, their properties, and the general
classes of problems they solve.
Exercises
These exercises all contain a stochastic programming problem that can be
solved using standard linear, nonlinear and integer programming software.
For each problem, you should develop the model, solve the stochastic pro-
gram, solve the expected value problem, and ﬁnd the value of the stochastic
solution.
1. Northam Airlines is trying to decide how to partition a new plane
for its Chicago–Detroit route. The plane can seat 200 economy class
passengers. A section can be partitioned oﬀfor ﬁrst class seats but
each of these seats takes the space of 2 economy class seats. A busi-
ness class section can also be included, but each of these seats takes
as much space as 1.5 economy class seats. The proﬁt on a ﬁrst class
ticket is, however, three times the proﬁt of an economy ticket. A busi-
ness class ticket has a proﬁt of two times an economy ticket’s proﬁt.
Once the plane is partitioned into these seating classes, it cannot be
changed. Northam knows, however, that the plane will not always be
full in each section. They have decided that three scenarios will occur
with about the same frequency: (1) weekday morning and evening
traﬃc, (2) weekend traﬃc, and (3) weekday midday traﬃc. Under
Scenario 1, they think they can sell as many as 20 ﬁrst class tickets,
50 business class tickets, and 200 economy tickets. Under Scenario 2,
these ﬁgures are 10, 25, and 175. Under Scenario 3, they are 5, 10,
and 150. You can assume they cannot sell more tickets than seats in
each of the sections. (In reality, the company may allow overbooking,
but then it faces the problem of passengers with reservations who
do not appear for the ﬂight (no-shows). The problem of determining
how many passengers to accept is part of the ﬁeld called yield man-
agement. For one approach to this problem, see Brumelle and McGill
[1993]. This subject is explored further in Exercise 1 of Section 2.7.)
2. Tomatoes Inc. (TI) produces tomato paste, ketchup, and salsa from
four resources: labor, tomatoes, sugar, and spices. Each box of the
tomato paste requires 0.5 labor hours, 1.0 crate of tomatoes, no sugar,


## Page 63

44
1. Introduction and Examples
and 0.25 can of spice. A ketchup box requires 0.8 labor hours, 0.5
crate of tomatoes, 0.5 sacks of sugar, and 1.0 can of spice. A salsa
box requires 1.0 labor hour, 0.5 crate of tomatoes, 1.0 sack of sugar,
and 3.0 cans of spice.
The company is deciding production for the next three periods. It
is restricted to using 200 hours of labor, 250 crates of tomatoes, 300
sacks of sugar, and 100 cans of spices in each period at regular rates.
The company can, however, pay for additional resources at a cost of
2.0 per labor hour, 0.5 per tomato crate, 1.0 per sugar sack, and 1.0
per spice can. The regular production costs for each product are 1.0
for tomato paste, 1.5 for ketchup, and 2.5 for salsa.
Demand is not known with certainty until after the products are
made in each period. TI forecasts that in each period two possibilities
are equally likely, corresponding to a good or bad economy. In the
good case, 200 boxes of tomato paste, 40 boxes of ketchup, and 20
boxes of salsa can be sold. In the bad case, these values are reduced to
100, 30, and 5, respectively. Any surplus production is stored at costs
of 0.5, 0.25, and 0.2 per box for tomato paste, ketchup, and salsa,
respectively. TI also considers unmet demand important and assigns
costs of 2.0, 3.0, and 6.0 per box for tomato paste, ketchup, and salsa,
respectively, for any demand that is not met in each period.
3. The Clear Lake Dam controls the water level in Clear Lake, a well-
known resort in Dreamland. The Dam Commission is trying to decide
how much water to release in each of the next four months. The Lake
is currently 150 mm below ﬂood stage. The dam is capable of lowering
the water level 200 mm each month, but additional precipitation and
evaporation aﬀect the dam. The weather near Clear Lake is highly
variable. The Dam Commission has divided the months into two two-
month blocks of similar weather. The months within each block have
the same probabilities for weather, which are assumed independent
of one another. In each month of the ﬁrst block, they assign a proba-
bility of 1/2 to having a natural 100-mm increase in water levels and
probabilities of 1/4 to having a 50-mm decrease or a 250-mm increase
in water levels. All these ﬁgures correspond to natural changes in wa-
ter level without dam releases. In each month of the second block,
they assign a probability of 1/2 to having a natural 150-mm increase
in water levels and probabilities of 1/4 to having a 50-mm increase or
a 350-mm increase in water levels. If a ﬂood occurs, then damage is
assessed at $10,000 per mm above ﬂood level. A water level too low
leads to costly importation of water. These costs are $5000 per mm
less than 250 mm below ﬂood stage. The commission ﬁrst considers
an overall goal of minimizing expected costs. They also consider mini-
mizing the probability of violating the maximum and minimum water


## Page 64

1.5 Other Applications
45
levels. (This makes the problem a special form of chance-constrained
model.) Consider both objectives.
4. The Energy Ministry of a medium-size country is trying to decide
on expenditures for new resources that can be used to meet energy
demand in the next decade. There are currently two major resources
to meet energy demand. These resources are, however, exhaustible.
Resource 1 has a cost of 5 per unit of demand met and a total current
availability equal to 25 cumulative units of demand. Resource 2 has
a cost of 10 per unit of demand met and a total current availability
of 10 demand units. An additional resource from outside the country
is always available at a cost of 16.7 per unit of demand met.
Some investment is considered in each of Resources 1 and 2 to dis-
cover new supplies and build capital. Resource 1 is, however, elusive.
A unit of investment in new sources of Resource 1 yields only 0.1
demand unit of Resource 1 with probability 0.5 and yields 1 demand
unit with probability 0.5. For Resource 2, investment is well known.
Each unit of investment yields a demand unit equivalent of Resource
2. Cumulative demand in the current decade is projected to be 10,
while demand in the next decade will be 25.
The ministry wants to minimize expected costs of meeting de-
mands in the current and following decade assuming that the results
of Resource 1 investment will only be known when the current decade
ends. Next-decade costs are discounted to 60% of their future real val-
ues (which should not change).
5. Paciﬁc Pulp and Paper is deciding how to manage their main forest.
They have trees at a variety of ages, which we will break into Classes 1
to 4. Currently, they have 8000 acres in Class 1, 10,000 acres in Class
2, 20,000 in Class 3, and 60,000 in Class 4. Each class corresponds
to about 25 years of growth. The company would like to determine
how to harvest in each of the next four 25-year periods to maximize
expected revenue from the forest. They also foresee the company’s
continuing after a century, so they place a constraint of having 40,000
acres in Class 4 at the end of the planning horizon.
Each class of timber has a diﬀerent yield. Class 1 has no yield, Class
2 yields 250 cubic feet per acre, Class 3 yields 510 cubic feet per acre,
and Class 4 yields 700 cubic feet per acre. Without ﬁres, the number
of acres in Class i (for i = 2, 3) in one period is equal to the amount
in Class i −1 from the previous period minus the amount harvested
from Class i −1 in the previous period. Class 1 at period t consists
of the total amount harvested in the previous period t −1, while
Class 4 includes all remaining Class 4 land plus the increment from
Class 3.


## Page 65

46
1. Introduction and Examples
While weather eﬀects do not vary greatly over 25-year periods, ﬁre
damage can be quite variable. Assume that in each 25-year block, the
probability is 1/3 that 15% of all timber stands are destroyed and that
the probability is 2/3 that 5% is lost. Suppose that discount rates are
completely overcome by increasing timber value so that all harvests
in the 100-year period have the same current value. Revenue is then
proportional to the total wood yield.
6. A hospital emergency room is trying to plan holiday weekend staﬃng
for a Saturday, Sunday, and Monday. Regular-time nurses can work
any two days of the weekend at a rate of $300 per day. In general,
a nurse can handle 10 patients during a shift. The demand is not
known, however. If more patients arrive than the capacity of the
regular-time nurses, they must work overtime at an average cost of
$50 per patient overload. The Saturday demand also gives a good
indicator of Sunday–Monday demand. More nurses can be called in
for Sunday–Monday duty after Saturday demand is observed. The
cost is $400 per day, however, in this case. The hospital would like to
minimize the expected cost of meeting demand.
Suppose that the following scenarios of 3 day demand are all
equally likely: (100, 90, 20), (100, 110, 120), (100, 100, 110), (90,
100, 110), (90, 80, 110), (90, 90,100), (80, 90, 100), (80, 70, 100), (80,
80, 90).
7. After winning the pole at Monza, you are trying to determine the
quickest way to get through the ﬁrst right-hand turn, which begins
200 meters from the start and is 30 meters wide. You are through
the turn at 100 meters past the beginning of the next stretch (see
Figure 10). As in the ﬁgure, you will attempt to stay 10 meters inside
the barrier on the starting stretch and accelerate as fast as possible
until point d1. At this distance, you will start braking as hard as
possible and take the turn at the current velocity reached at some
point d2. (Assume a circular turn with radius equal to the square of
velocity divided by maximum lateral acceleration.) Obviously, you do
not want to go oﬀthe course.
The problem is that you can never be exactly sure of the car and
track speed until you start braking at point d1. At that point, you
can tell whether the track is fast, medium, or slow, and you can then
determine the point d2 where you enter the turn. You suppose that
the three kinds of track/car combinations are equally likely. If fast,
you accelerate at 27 m/sec2, decelerate at 45 m/sec2, and have a
maximum lateral acceleration of 1.8 g (= 17.5 m/sec2). For medium,
these values are 24, 42, and 16; for slow, the values are 20, 35, and 14.
You want to minimize the expected time through this section. You
also assume that if you follow an optimal strategy, other competitors


## Page 66

1.5 Other Applications
47
FIGURE 10. Opening straight and turn for Problem 7.
will not throw you out of the race (although you may not be sure of
that).
8. In training for the Olympic decathlon, you are trying to choose your
takeoﬀpoint for the long jump to maximize your expected oﬃcial
jump. Unfortunately, when you aim at a certain spot, you have a
50/50 chance of actually taking oﬀ10 cm beyond that point. If that
violates the oﬃcial takeoﬀline, you foul and lose that jump opportu-
nity. Assume that you have three chances and that your longest jump
counts as your oﬃcial ﬁnish.
You then want to determine your aiming strategy for each jump.
Assume that your actual takeoﬀis independent from jump to jump.
Initially you are equally likely to hit a 7.4- or 7.6-meter jump from
your actual takeoﬀpoint. If you hit a long ﬁrst jump, then you have
a 2/3 chance of another 7.6-meter jump and 1/3 chance of jumping
7.4 meters. The probabilities are reversed if you jumped 7.4 meters
the ﬁrst time. You always seem to hit the third jump the same as the
second.
First, ﬁnd a strategy to maximize the expected oﬃcial jump. Then,
maximize decathlon points from the following Table 7.


## Page 67

48
1. Introduction and Examples
TABLE 7. Decathlon Points for Problem 8.
Distance
Points
Distance
Points
7.30
886
7.46
925
7.31
888
7.47
927
7.32
891
7.48
930
7.33
893
7.49
932
7.34
896
7.50
935
7.35
898
7.51
937
7.36
900
7.52
940
7.37
903
7.53
942
7.38
905
7.54
945
7.39
908
7.55
947
7.40
910
7.56
950
7.41
913
7.57
952
7.42
915
7.58
955
7.43
918
7.59
957
7.44
920
7.60
960
7.45
922
7.61
962


## Page 68

2
Uncertainty and Modeling Issues
In the previous chapter, we gave several examples of stochastic program-
ming models. These formulations ﬁt into diﬀerent categories of stochastic
programs in terms of the characteristics of the model. This chapter presents
those basic characteristics by describing the fundamentals of any modeling
eﬀort and some of the standard forms detailed in later chapters.
Before beginning general model descriptions, however, we ﬁrst describe
the probability concepts that we will assume in the rest of the book. Fa-
miliarity with these concepts is essential in understanding the structure of
a stochastic program. This presentation is made simple enough to be un-
derstood by readers unfamiliar with the ﬁeld and, thus, leaves aside some
questions related to measure theory. Sections 2 through 7 build on these
fundamentals and give the general forms in various categories. Section 8
gives some background on the relationship of stochastic programming to
other areas of decision making under uncertainty. Section 9 brieﬂy reviews
the main optimization concepts used in the book.
2.1
Probability Spaces and Random Variables
Several parameters of a problem can be considered uncertain and are thus
represented as random variables. Production and distribution costs typi-
cally depend on fuel costs, which are random. Future demands depend on
uncertain market conditions. Crop returns depend on uncertain weather
conditions.


## Page 69

50
2. Uncertainty and Modeling Issues
Uncertainty is represented in terms of random experiments with out-
comes denoted by ω. The set of all outcomes is represented by Ω. In a
transport and distribution problem, the outcomes range from political con-
ditions in the Middle East to general trade situations, while the random
variable of interest may be the fuel cost. The relevant set of outcomes is
clearly problem-dependent. Also, it is usually not very important to be able
to deﬁne those outcomes accurately because the focus is mainly on their
impact on some (random) variables.
The outcomes may be combined into subsets of Ωcalled events. We
denote by A a collection of random events. As an example, if Ωcontains
the six possible results of the throw of a dice, A also contains combined
outcomes such as an odd number, a result smaller than or equal to four, etc.
If Ωcontains weather conditions for a single day, A also contains combined
events such as “a day without rain,” which might be the union of a sunny
day, a partly cloudy day, a cloudy day without showers, etc.
Finally, to each event A ∈A is associated a value P(A), called a prob-
ability, such that 0 ≤P(A) ≤1, P(∅) = 0, P(Ω) = 1 and P(A1 ∪A2) =
P(A1) + P(A2) if A1 ∩A2 = ∅.
The triplet (Ω, A, P) is called a probability space that must satisfy a
number of conditions (see, e.g., Chung [1974]). It is possible to deﬁne several
random variables associated with a probability space, namely, all variables
that are inﬂuenced by the random events in A. If one takes as elements of Ω
events ranging from the political situation in the Middle East to the general
trade situations, they allow us to describe random variables such as the fuel
costs and the interest rates and inﬂation rates in some Western countries.
If the elements of Ωare the weather conditions from April to September,
they inﬂuence random variables such as the production of corn, the sales
of umbrellas and ice cream, or even the exam results of undergraduate
students.
In terms of stochastic programming, there exists one situation where
the description of random variables is closely related to Ω: in some cases
indeed, the elements ω ∈Ωare used to describe a few states of the world or
scenarios. All random elements then jointly depend on these ﬁnitely many
scenarios. Such a situation frequently occurs in strategic models where
the knowledge of the possible outcomes in the future is obtained through
experts’ judgments and only a few scenarios are considered in detail. In
many situations, however, it is extremely diﬃcult and pointless to construct
Ωand A; the knowledge of the random variables is suﬃcient.
For a particular random variable ξ, we deﬁne its cumulative distribution
Fξ(x) = P(ξ ≤x), or more precisely Fξ(x) = P({ω|ξ ≤x}). Two major
cases are then considered. A discrete random variable takes a ﬁnite or
countable number of diﬀerent values. It is best described by its probability
distribution, which is the list of possible values, ξk, k ∈K, with associated


## Page 70

2.2 Deterministic Linear Programs
51
probabilities,
f(ξk) = P(ξ = ξk) s.t.

k∈K
f(ξk) = 1.
Continuous random variables can often be described through a so-called
density function f(ξ). The probability of ξ being in an interval [a, b] is
obtained as
P(a ≤ξ ≤b) =
 b
a
f(ξ)dξ,
or equivalently
P(a ≤ξ ≤b) =
 b
a
dF(ξ),
where F(.) is the cumulative distribution as earlier. Contrary to the dis-
crete case, the probability of a single value P(ξ = a) is always zero for
a continuous random variable. The distribution F(.) must be such that
 ∞
−∞dF(ξ) = 1.
The expectation of a random variable is computed as µ = 	
k∈K ξkf(ξk)
or µ =
 ∞
−∞ξdF(ξ) in the discrete and continuous cases, respectively. The
variance of a random variable is E[(ξ −µ)2]. The expectation of ξr is called
the rth moment of ξ and is denoted ¯ξ(r) = E[ξr]. A point η is called the
α-quantile of ξ if and only if for 0 < α < 1, η = min{x|F(x) ≥α}.
The appendix lists the distributions used in the textbook and their ex-
pectations and variances. The concepts of probability distribution, density,
and expectation easily extend to the case of multiple random variables.
Some of the sections in the book use probability measure theory which
generalizes these concepts. These sections contain a warning to readers
unfamiliar with this ﬁeld.
2.2
Deterministic Linear Programs
A deterministic linear program consists of ﬁnding a solution to
min z =cT x
s.t. Ax = b,
x ≥0,
where x is an (n × 1) vector of decisions and c, A, and b are known data
of sizes (n × 1), (m × n), and (m × 1), respectively. The value z = cT x
corresponds to the objective function, while {x|Ax = b, x ≥0} deﬁnes
the set of feasible solutions. An optimum x∗is a feasible solution such
that cT x ≥cT x∗for any feasible x. Linear programs typically search for
a minimal-cost solution under some requirements (demand) to be met or
for a maximum proﬁt solution under limited resources. There exists a wide


## Page 71

52
2. Uncertainty and Modeling Issues
variety of applications, routinely solved in the industry. As introductory
references, we cite Chv´atal [1980], Dantzig [1963], and Murty [1983]. We
assume the reader is familiar with linear programming and has some knowl-
edge of basic duality theory as in these textbooks. A short review is given
in Section 2.9.
2.3
Decisions and Stages
Stochastic linear programs are linear programs in which some problem data
may be considered uncertain. Recourse programs are those in which some
decisions or recourse actions can be taken after uncertainty is disclosed. To
be more precise, data uncertainty means that some of the problem data can
be represented as random variables. An accurate probabilistic description of
the random variables is assumed available, under the form of the probability
distributions, densities or, more generally, probability measures. As usual,
the particular values the various random variables will take are only known
after the random experiment, i.e., the vector ξ = ξ(ω) is only known after
the experiment.
The set of decisions is then divided into two groups:
• A number of decisions have to be taken before the experiment. All
these decisions are called ﬁrst-stage decisions and the period when
these decisions are taken is called the ﬁrst stage.
• A number of decisions can be taken after the experiment. They are
called second-stage decisions. The corresponding period is called the
second stage.
First-stage decisions are represented by the vector x, while second-stage de-
cisions are represented by the vector y or y(ω) or even y(ω, x) if one wishes
to stress that second-stage decisions diﬀer as functions of the outcome of
the random experiment and of the ﬁrst-stage decision. The sequence of
events and decisions is thus summarized as
x →ξ(ω) →y(ω, x).
Observe here that the deﬁnitions of ﬁrst and second stages are only re-
lated to before and after the random experiment and may in fact contain
sequences of decisions and events. In the farming example of Section 1.1,
the ﬁrst stage corresponds to planting and occurs during the whole spring.
Second-stage decisions consist of sales and purchases. Selling extra corn
would probably occur very soon after the crop while buying missing corn
will take place as late as possible.
A more extreme example is the following. A traveling salesperson receives
one item every day. She visits clients hoping to sell that item. She returns


## Page 72

2.3 Decisions and Stages
53
home when a buyer is found or when all clients are visited. Clients buy
or do not buy in a random fashion. The decision is not inﬂuenced by the
previous days’ decisions. The salesperson wishes to determine the order in
which to visit clients, in such a way as to be at home as early as possible
(seems reasonable, does it not?). Time spent involves the traveling time
plus some service time at each visited client.
To make things simple, once the sequence of clients to be visited is ﬁxed,
it is not changed. Clearly the ﬁrst stage consists of ﬁxing the sequence
and traveling to the ﬁrst client. The second stage is of variable duration
depending on the successive clients buying the item or not. Now, consider
the following example. There are two clients with probability of buying 0.3
and 0.8, respectively and traveling times (including service) as in the graph
of Figure 1.
FIGURE 1. Traveling salesperson example.
Assume the day starts at 8 A.M. If the sequence is (1,2), the ﬁrst stage
goes from 8 to 9:30. The second stage starts at 9:30 and ﬁnishes either at
11 A.M. if 1 buys or 4:30 P.M. otherwise. If the sequence is (2,1), the ﬁrst
stage goes from 8 to 12:00, the second stage starts at 12:00 and ﬁnishes
either at 4:00 P.M. or at 4:30 P.M. Thus, the ﬁrst stage if sequence (2,1) is
chosen may sometimes end after the second stage is ﬁnished when (1,2) is
chosen if Client 1 buys the item.


## Page 73

54
2. Uncertainty and Modeling Issues
2.4
Two-Stage Program with Fixed Recourse
The classical two-stage stochastic linear program with ﬁxed recourse (orig-
inated by Dantzig [1955] and Beale [1955]) is the problem of ﬁnding
min z =cT x + Eξ[min q(ω)T y(ω)]
(4.1)
s.t. Ax = b,
(4.2)
T(ω)x + Wy(ω) = h(ω),
(4.3)
x ≥0 , y(ω) ≥0.
(4.4)
As in the previous section, a distinction is made between the ﬁrst stage and
the second stage. The ﬁrst-stage decisions are represented by the n1 × 1
vector x. Corresponding to x are the ﬁrst-stage vectors and matrices c, b,
and A, of sizes n1×1, m1×1, and m1×n1, respectively. In the second stage,
a number of random events ω ∈Ωmay realize. For a given realization ω,
the second-stage problem data q(ω), h(ω) and T(ω) become known, where
q(ω) is n2 × 1, h(ω) is m2 × 1, and T(ω) is m2 × n1.
Each component of q, T, and h is thus a possible random vari-
able. Let Ti·(ω) be the ith row of T(ω). Piecing together the stochas-
tic components of the second-stage data, we obtain a vector ξT (ω) =
(q(ω)T , h(ω)T , T1·(ω), · · · , Tm2·(ω)), with potentially up to N = n2 + m2 +
(m2 × n1) components. As indicated before, a single random event ω (or
state of the world) inﬂuences several random variables, here, all components
of ξ.
Let also Ξ ⊂ℜN be the support of ξ, that is, the smallest closed subset in
ℜN such that P(Ξ) = 1. As just said, when the random event ω is realized,
the second-stage problem data, q, h, and T, become known. Then, the
second-stage decision y(ω) or (y(ω, x)) must be taken. The dependence
of y on ω is of a completely diﬀerent nature from the dependence of q
or other parameters on ω. It is not functional but simply indicates that
the decisions y are typically not the same under diﬀerent realizations of
ω. They are chosen so that the constraints (4.3) and (4.4) hold almost
surely (denoted a.s.), i.e., for all ω ∈Ωexcept perhaps for sets with zero
probability. We assume random constraints to hold in this way throughout
this book unless a speciﬁc probability is given for satisfying constraints.
The objective function of (4.1) contains a deterministic term cT x and the
expectation of the second-stage objective q(ω)T y(ω) taken over all realiza-
tions of the random event ω. This second-stage term is the more diﬃcult
one because, for each ω, the value y(ω) is the solution of a linear pro-
gram. To stress this fact, one sometimes uses the notion of a deterministic
equivalent program. For a given realization ω, let
Q(x, ξ(ω)) = min
y {q(ω)T y|Wy = h(ω) −T(ω)x, y ≥0}
(4.5)


## Page 74

2.4 Two-Stage Program with Fixed Recourse
55
be the second-stage value function. Then, deﬁne the expected second-stage
value function
Q(x) = EξQ(x, ξ(ω))
(4.6)
and the deterministic equivalent program (DEP)
min z =cT x + Q(x)
(4.7)
s.t. Ax = b,
(4.8)
x ≥0.
This representation of a stochastic program clearly illustrates that the ma-
jor diﬀerence from a deterministic formulation is in the second-stage value
function. If that function is given, then a stochastic program is just an
ordinary nonlinear program.
Formulation (4.1)–(4.4) is the simplest form of a stochastic two-stage pro-
gram. Extensions are easily modeled. For example, if ﬁrst-stage or second-
stage decisions are to be integers, constraint (4.4) can be replaced by a
more general form:
x ∈X, y(w) ∈Y,
where X = Zn1
+ and Y = Zn2
+ . Similarly, nonlinear ﬁrst-stage and second-
stage objectives or constraints can easily be incorporated.
Examples of recourse formulation and interpretations
The deﬁnition of ﬁrst stage versus second stage is not only problem de-
pendent but also context dependent. We illustrate diﬀerent examples of
recourse formulations for one class of problems: the location problem.
Let i = 1, · · · , m index clients having demand di for a given commodity.
The ﬁrm can open a facility (such as a plant or a warehouse) in potential
sites j = 1, . . . , n. Each client can be supplied from an open facility where
the commodity is made available (i.e., produced or stored). The problem of
the ﬁrm is to choose the number of facilities to open, their locations, and
market areas to maximize proﬁt or minimize costs.
Let us ﬁrst present the deterministic version of the so-called simple plant
location or uncapacitated facility location problem. Let xj be a binary
variable equal to one if facility j is open and zero otherwise. Let cj be the
ﬁxed cost for opening and operating facility j and let vj be the variable
operating cost of facility j. Let yij be the fraction of the demand of client
i served from facility j and tij be the unit transportation cost from j to i.
All costs and proﬁts should be taken in conformable units, typically on a
yearly equivalent basis. Let ri denote the unit price charged to client i and
qij = (ri −vj −tij)di be the total revenue obtained when all of client i’s
demand is satisﬁed from facility j. Then the simple plant location problem


## Page 75

56
2. Uncertainty and Modeling Issues
or uncapacitated facility location problem (UFLP) reads as follows:
UFLP: max
x,y
z(x, y) =−
n

j=1
cjxj +
m

i=1
n

j=1
qijyij
(4.9)
s.t.
n

j=1
yij ≤1, i = 1, · · · , m,
(4.10)
0 ≤yij ≤xj, i = 1, . . . , m, j = 1, . . . , n,
(4.11)
xj ∈{0, 1}, j = 1, . . . , n.
(4.12)
Constraints (4.10) ensure that the sum of fractions of clients i’s demand
served cannot exceed one. Constraints (4.11) ensure that clients are served
only through open plants.
It is customary to present the uncapacitated facility location in a diﬀerent
canonical form that minimizes the sum of the ﬁxed costs of opening facilities
and of the transportation costs plus possibly the variable operating costs.
(There are several ways to arrive at this canonical representation. One is to
assume that unit prices are much larger than unit costs in such a way that
demand is always fully satisﬁed.) This presentation more clearly stresses
the link between the deterministic and stochastic cases.
In the UFLP, a trade-oﬀis sought between opening more plants, which
results in higher ﬁxed costs and lower transportation costs and opening
fewer plants with the opposite eﬀect. Whenever the optimal solution is
known, the size of an open facility is computed as the sum of demands
it serves. (In the deterministic case, it is always optimal to have each yij
equal to either zero or one.) The market areas of each facility are then
well-deﬁned.
The notation xj for the location variables and yij for the distribution
variables is common in location theory and is thus not meant here as ﬁrst
stage and second stage, respectively, although in some of the models it is
indeed the case.
Several parameters of the problem may be uncertain and may thus have
to be represented by random variables. Production and distribution costs
may vary over time. Future demands for the product may be uncertain.
As indicated in the introduction of the section, we will now discuss var-
ious situations of recourse. It is customary to consider that the location
decisions xj are ﬁrst-stage decisions because it takes some time to imple-
ment decisions such as moving or building a plant or warehouse. The main
modeling issue is on the distribution decisions. The ﬁrm may have full con-
trol on the distribution, for example, when the clients are shops owned by
the ﬁrm. It may then choose the distribution pattern after conducting some
random experiments. In other cases, the ﬁrm may have contracts that ﬁx
which plants serve which clients, or the ﬁrm may wish ﬁxed distribution
patterns in view of improved eﬃciency because drivers would have better
knowledge of the regions traveled.


## Page 76

2.4 Two-Stage Program with Fixed Recourse
57
a. Fixed distribution pattern, ﬁxed demand, ri, vj, tij stochastic
Assume the only uncertainties are in production and distribution costs
and prices charged to the client. Assume also that the distribution pattern
is ﬁxed in advance, i.e., is considered ﬁrst stage. The second stage then
just serves as a measure of the cost of distribution. We now show that
the problem is in fact a deterministic problem in which the total revenue
qij = (ri −vj −tij)di can be replaced by its expectation. To do this, we
formally introduce extra second-stage variables wij, with the constraint
wij(ω) = yij for all ω. We obtain
max
−
n

j=1
cjxj + Eξ
m

i=1
n

j=1
qij(ω)wij(ω)
s.t. (4.10), (4.11), (4.12), and
wij(ω) = yij,
i = 1, . . . , m , j = 1, . . . , n
for all ω.
(4.13)
By (4.13), the second-stage objective function can be replaced by
Eξ
m

i=1
n

j=1
qij(ω)yij
or
n

i=1
n

j=1
Eξqij(ω)yij,
because yij is ﬁxed and summations and expectation can be interchanged.
The problem is thus the deterministic problem
max
−
n

j=1
cjxj +
m

i=1
n

j=1
(Eξqij(ω))yij
s.t. (4.10), (4.11), (4.12).
Although there exists uncertainty about the distribution costs and rev-
enues, the only possible action is to plan in view of the expected costs.
b. Fixed distribution pattern, uncertain demand
Assume now that demand is uncertain, but, for some of the reasons cited
earlier, the distribution pattern is ﬁxed in the ﬁrst stage. Depending on the
context, the distribution costs and revenues (vj, tij, ri) may or may not be
uncertain.
We deﬁne yij = quantity transported from j to i, a quantity no longer
deﬁned as a function of the demand di, because demand is now stochastic.
For simplicity, we assume that a penalty q+
i is paid per unit of demand di


## Page 77

58
2. Uncertainty and Modeling Issues
which cannot be satisﬁed from all quantities transported to i (they might
have to be obtained from other sources) and a penalty q−
i is paid per unit
on the products delivered to i in excess of di (the cost of inventory, for
example). We thus introduce second-stage variables: w−
i (ω) = amount of
extra products delivered to i in state ω; w+
i (ω) = amount of unsatisﬁed
demand to i in state ω.
The formulation becomes
max
−
n

j=1
cjxj+
m

i=1
n

j=1
(Eξ(−vj −tij))yij + Eξ[−
m

i=1
q+
i w+
i (ω) (4.14)
−
m

i=1
q−
i w−
i (ω)] + Eξ
m

i=1
ridi
s.t.
m

i=1
yij ≤Mxj, j = 1, . . . , n,
(4.15)
w+
i (ω) −w−
i (ω) = di(ω) −
n

j=1
yij, i = 1, . . . , m, (4.16)
xj ∈{0, 1}, 0 ≤yij,w+
i (ω) ≥0, w−
i (ω) ≥0, i = 1, . . . , m; j = 1, . . . , n.(4.17)
This model is a location extension of the transportation model of Williams
[1963]. The objective function contains the investment costs for opening
plants, the expected production and distribution costs, the expected penal-
ties for extra or insuﬃcient demands, and the expected revenue. This last
term is constant because it is assumed that all demands must be satis-
ﬁed by either direct delivery or some other means reﬂected in the penalty
for unmet demand. The problem only makes sense if q+
i
is large enough,
for example, larger than Eξ(vj + tij) for all j, although weaker conditions
may sometimes suﬃce. Constraint (4.15) guarantees that distribution only
occurs from open plants, i.e., plants such that xj = 1. The constant M
represents the maximum possible size of a plant.
Observe that here the variables yij are ﬁrst-stage variables. Also observe
that in the second stage, the constraints (4.16,4.17) have a very simple
form, as w+
i (ω) = di −	n
j=1 yij if this quantity is non-negative and
w−
i (ω) = 	n
j=1 yij −di otherwise. This is an example of a second stage
with simple recourse.
Also note that in Cases a and b, the size or capacity of plant j is simply
obtained as the sum of the quantity transported from j, namely, 	m
i=1 diyij
in Case a and 	m
i=1 yij in Case b.
c. Uncertain demand, variable distribution pattern
We now consider the case where the distribution pattern can be adjusted
to the realization of the random event. This might be the case when un-
certainty corresponds to long-term scenarios, of which only one is realized.


## Page 78

2.4 Two-Stage Program with Fixed Recourse
59
Then the distribution pattern can be adapted to this particular realization.
This also implies that the sizes of the plants cannot be deﬁned as the sum
of the quantity distributed, because those quantities depend on the random
event. We thus deﬁne as before:
xj =
 1
if plant j is open,
0
otherwise.
We now let yij depend on ω with yij(ω) = fraction of demand di(ω) served
from j and deﬁne new variables wj = size (capacity) of plant j, with unit
investment cost gj.
The model now reads
max
−
n

j=1
cjxj−
n

j=1
gjwj + Eξ max
m

i=1
n

j=1
qij(ω)yij(ω)
(4.18)
s.t. xj ∈{0, 1}, wj ≥0, j = 1, . . . , n,
(4.19)
n

j=1
yij(ω) ≤1, i = 1, . . . , m,
(4.20)
m

i=1
di(ω)yij(ω) ≤wj, j = 1, . . . , n,
(4.21)
0 ≤yij(ω) ≤xj, i = 1, . . . , m, j = 1, . . . , n,
(4.22)
where qij(ω) = (ri −vj −tij)di(ω) now includes the demand di(ω).
Constraint (4.20) indicates that no more than 100% of i’s demand can
be served, but that the possibility exists that not all demand is served.
Constraint (4.21) imposes that the quantity distributed from plant j does
not exceed the capacity wj decided in the ﬁrst stage. For the sake of clarity,
one could impose a constraint wj ≤Mxj, but this is implied by (4.21)
and (4.22). For a discussion of algorithmic solutions of this problem, see
Louveaux and Peeters [1992].
d. Stages versus periods; Two-stage versus multistage
In this section, we highlight again the diﬀerence in a stochastic program
between stages and periods of times. Consider the case of a distribution
ﬁrm that makes its plans for the next 36 months. It may formulate a model
such as (4.18)–(4.22). The location of warehouses would be ﬁrst-stage deci-
sions, while the distribution problem would be second-stage decisions. The
duration of the ﬁrst stage would be something like six months (depending
on the type of warehouse) and the second stage would run over the 30 re-
maining months. Although we may think of a problem over 36 periods, a
two-stage model is totally relevant. In this case, the only moment where the
number of periods is important is when the precise values of the objective
coeﬃcients are computed.
In this example, a multistage model becomes necessary if the distribution
ﬁrm foresees additional periods where it is ready to change the location of


## Page 79

60
2. Uncertainty and Modeling Issues
the warehouses. In this example, suppose the ﬁrm decides that the opening
of new warehouses can be decided after one year. A three-stage model can
be constructed. The ﬁrst stage would consist of decisions on warehouses to
be built now. The second stage would consist of the distribution patterns
between months 7 and 18 as well and new openings decided in month 12.
The third stage would consist of distribution patterns between months 19
and 36.
FIGURE 2. Three-stage model decisions and times.
Let x1 and x2(ω2) be the binary vectors representing opening warehouses
in stages 1 and 2, respectively. Let y2(ω2) and y3(ω3) be the vectors rep-
resenting the distribution decisions in stages 2 and 3, respectively, where
ω2 and ω3 are the states of the world in stages 2 and 3. Assuming each
warehouse can only have a ﬁxed size M, the following model can be built:
max
−
n

j=1
cjx1
j + Eξ2 max{
m

i=1
n

j=1
q2
ij(ω2)y2
ij(ω2) −
n

j=1
c2
j(ω2)x2
j(ω2)
+ Eξ3|ξ2 max[
m

i=1
n

j=1
q3
ij(ω3)y3
ij(ω3)]}
s.t.
n

j=1
y2
ij(ω2) ≤1, i = 1, . . . , m,
m

i=1
di(ω2)y2
ij(ω2) ≤Mx1
j, j = 1, . . . , n,
n

j=1
y3
ij(ω3) ≤1, i = 1, . . . , m,
m

i=1
di(ω3)y3
ij(ω3) ≤M(x1
j + x2
j(ω2)), j = 1, . . . , n,
x1
j + x2
j(ω2) ≤1, j = 1, . . . , n,
x1
j,x2
j(ω2) ∈{0, 1}, j = 1, . . . , n,
y2
ij(ω2), y3
ij(ω3) ≥0, i = 1, . . . , m, j = 1, . . . , n.


## Page 80

2.5 Random Variables and Risk Aversion
61
Multistage programs will be further studied in Section 3.5.
2.5
Random Variables and Risk Aversion
In our view, one can often classify random events and random variables
in two major categories. In the ﬁrst category, we would place uncertain-
ties that recur frequently on a short-term basis. As an example, uncertainty
may correspond to daily or weekly demands. This normally leads to a model
similar to the one in Section 4, Case b (4.b), where allocation cannot be
adjusted every time period. It follows that the expectation in the second
stage somehow represents a mean over possible values of the random vari-
ables, of which many will occur. Thus, the expectation takes into account
realizations that might not occur and many realizations that will occur.
To ﬁx ideas here, if in Model 4.b the units in the objective function are in
a yearly basis and the randomness involves daily or weekly demands, one
may expect that the value of the objective of stochastic model will closely
match the realized total yearly revenue.
As one interesting example of a real-world application of a location model
of this ﬁrst category, we may recommend the paper by Psaraftis, Tharakan,
and Ceder [1986]. It deals with the optimal location and size of equipment
to ﬁght oil spills. Occurrence and sizes of spills are random. The sizes of
the spills are represented by a discrete random variable taking three possi-
ble values, corresponding to small, medium, or large spills. Sadly enough,
spills are suﬃciently frequent that the expectation may be considered close
enough to the mean cost, as just described. Occurrence of spills at a given
site is also random. It is described by a Poisson process. By making the
assumption of nonconcomitant occurrence of spills, all equipment is made
available for each spill, which simpliﬁes the second-stage descriptions com-
pared to (4.14)–(4.17).
In the second category, we would place uncertainties that can be rep-
resented as scenarios, of which basically only one or a small number are
realized. This would be the case in long-term models where scenarios rep-
resent the general trend of the variables. As already indicated, this is the
spirit in which Model c is built. In the second stage, among all scenarios
over which expectation is taken, only one is realized. The objective func-
tion may then be considered a poor representation of risk aversion, which
is typically assumed in decision making (if we exclude gambling).
Starting from the Von Neumann and Morgenstern [1944] theory of utility,
this ﬁeld of modeling preferences has been developed by economics. Models
such as the mean-variance approach of Markowitz [1959] have been widely
used. Other methods have been proposed based on mixes of mean-variance
and other approaches (see, e.g, Ben-Tal and Teboulle [1986]). From a the-
oretical point of view, considering a nonlinear utility function transforms


## Page 81

62
2. Uncertainty and Modeling Issues
the problems into stochastic nonlinear programs. This topic is covered in
Chapter 6. In practice, however, it seems diﬃcult to solve large-scale non-
linear stochastic programs, so that the choice has very often been either
to include risk aversion in a somewhat small second-stage description or
to maintain a linear utility function with a more detailed second-stage
description.
One interesting alternative to nonlinear utility models is to include risk
aversion in a linear utility model under the form of a linear constraint,
called downside risk (Eppen, Martin, and Schrage [1989]). The problem
there is to determine the type and level of production capacity at each of
several locations. Plants produce various types of cars and may be open,
closed, or retooled. The demand for each type of car in the medium term
is random. The decisions about the locations and conﬁgurations of plants
have to be made before the actual demands are known.
Scenarios are based on pessimistic, neutral, or optimistic realizations of
demands. A scenario consists of a sequence of realizations for the next
ﬁve years. The stochastic model maximizes the present value of expected
discounted cash ﬂows. The linear constraint on risk is as follows: the down-
side risk of a given scenario is the amount by which proﬁt falls below some
given target value. It is thus zero for larger proﬁts. The expected downside
risk is simply the expectation of the downside risk over all scenarios. The
constraint is thus that the expected downside risk must fall below some
level.
To give an idea of how this works, consider a two-stage model similar to
(4.1)–(4.4) but in terms of proﬁt maximization, by
max z = cT x + Eξ[max qT (ω)y(ω)]
s.t. (4.2)–(4.4).
Then deﬁne the target level g on proﬁt. The downside risk u(ξ) is thus
deﬁned by two constraints:
u(ξ(ω))≥g −qT (ω)y(ω)
(5.1)
u(ξ(ω))≥0.
(5.2)
The constraint on expected downside risk is
Eξu(ξ) ≤l,
(5.3)
where l is some given level. For a problem with a discrete random vector ξ,
constraint (5.3) is linear. Observe that (5.3) is in fact a ﬁrst-stage constraint
as it runs over all scenarios. It can be used directly in the extensive form.
It can also be used indirectly in a sequential manner, by imposing such
a constraint only when needed. This can be done in a way similar to the
induced constraints for feasibility that we will study in Chapter 5.


## Page 82

2.6 Implicit Representation of the Second Stage
63
2.6
Implicit Representation of the Second Stage
This book is mainly concerned with stochastic programs of the form (4.1)–
(4.4), assuming that an adequate and computationally tractable represen-
tation of the recourse problem exists. This is not always the case. Two
possibilities then exist that still permit some treatment of the problem:
• A closed form expression is available for the expected value function
Q(x).
• For a given ﬁrst-stage decision x, the expected value function Q(x)
is computable.
These possibilities are described in the following sections.
a. A closed form expression is available for Q(x)
We may illustrate this case by the Stochastic Queue Median model (SQM)
ﬁrst proposed by Berman, Larson, and Chiu [1985] from which we take
the following in a simpliﬁed form. The problem consists of locating an
emergency unit (such as an ambulance). When a call arrives, there is a
certain probability that the ambulance is already busy handling an earlier
demand for ambulance service. In that event, the new service demand is
either referred to a backup ambulance service or entered into a queue of
other waiting “customers.” Here, the ﬁrst-stage decision consists of ﬁnding
a location for the ambulance. The second stage consists of the day-to-day
response of the system to the random demands. Assuming a ﬁrst-in, ﬁrst-
out decision rule, decisions in the second stage are somehow automatic. On
the other hand, the quality of response, measured, e.g., by the expected
service time, depends on the ﬁrst-stage decision. Indeed, when responding
to a call, an ambulance typically goes to the scene and returns to the home
location before responding to the next call. The time when it is unavailable
for another call is clearly a function of the home location.
Let λ be the total demand rate, λ ≥0. Let pi be the probability that a
demand originates from demand region i, with 	m
i=1 pi = 1. Let also t(i, x)
denote the travel time between location x and call i. On-scene service time
is omitted for simplicity. Given facility location x, the expected response
time is the sum of the mean-in-queue delay w(x) and the expected travel
time ¯t(x),
Q(x) = w(x) + ¯t(x),
(6.1)
where
w(x) =

λ¯t(2)(x)
2(1−λ¯t(x))
if λ¯t(x) < 1,
0
otherwise,
(6.2)
¯t(x) =
m

i=1
pit(i, x),
(6.3)


## Page 83

64
2. Uncertainty and Modeling Issues
and
¯t(2)(x) =
m

i=1
pit2(i, x) .
(6.4)
The global problem is then of the form:
min
x∈X Q(x),
(6.5)
where the ﬁrst-stage objective function is usually taken equal to zero and
X represents the set of possible locations, which typically consists of a
network.
It should be clear that no possibility exists to adequately describe the
exact sequence of decisions and events in the so-called second stage and
that the expected recourse Q(x) represents the result of a computation
assuming the system is in steady state.
b. For a given x, Q(x) is computable
The deterministic traveling salesperson problem (TSP) consists of ﬁnding
a Hamiltonian tour of least cost or distance. Following a Hamiltonian tour
means that the traveling salesperson starts from her home location, visits
all customers, (say i = 1, · · · , m) exactly, and returns to the home location.
Now, assume each customer has a probability pi of being present. A full
optimization that would allow the salesperson to decide the next customer
to visit at each step would be a diﬃcult multistage stochastic program.
A simpler two-stage model, known as a priori optimization is as follows:
in the ﬁrst-stage, an a priori Hamiltonian tour is designed. In the second
stage, the a priori tour is followed by skipping the absent customers. The
problem is to ﬁnd the tour with minimal expected cost (Jaillet [1988]).
The exact representation of such a second-stage recourse problem as a
mathematical program with binary decision variables might be possible in
theory but would be so cumbersome that it would be of no practical value.
On the other hand, the expected length of the tour (and thus Q(x)) is
easily computed when the tour (x) is given. Other examples of a priori
optimization can be found in Bertsimas, Jaillet, and Odoni [1990].
2.7
Probabilistic Programming
In probabilistic programming, some of the constraints or the objective are
expressed in terms of probabilistic statements about ﬁrst-stage decisions.
The description of second-stage or recourse actions is thus avoided. This is
particularly useful when the cost and beneﬁts of second-stage decisions are
diﬃcult to assess.


## Page 84

2.7 Probabilistic Programming
65
Consider the following covering location problem. Let j = 1, · · · , n be the
potential locations with, as usual, xj = 1 if site j is open and 0 otherwise,
and cj the investment cost. Let i = 1, · · · , m be the clients. Client i is served
if there exists an open site within distance ti. The distance between i and
j is tij. Deﬁne Ni = {j|tij < ti} as the set of eligible sites for client i. The
deterministic covering problem is
min
n

j=1
cjxj
(7.1)
s.t.

j∈Ni
xj ≥1, i = 1, · · · , m,
(7.2)
xj ∈{0, 1}, j = 1, · · · , n.
(7.3)
Taking again the case of an ambulance service, one site may be covering
more than one region or demand area. When a call is placed, the emergency
units may be busy serving another call. Let q be the probability that no
emergency unit is available at site j. For simplicity, assume this probability
is the same for every site (see Toregas et al. [1971]). Then, the deterministic
covering constraint (7.2) may be replaced by the requirement that P (at
least one emergency unit from an open eligible site is available) ≥α where
α is some conﬁdence level, typically 90 or 95%. Here, the probability that
none of the eligible sites has an available emergency unit is q to the power
	
j∈Ni xj, so that the probabilistic constraint is
1 −q

j∈Ni xj ≥α , i = 1, · · · , m
(7.4)
or
q

j∈Ni xj ≤1 −α.
Taking the logarithm on both sides, one obtains

j∈Ni
xj ≥b
(7.5)
with
b = ⌈ln(1 −α)
ln q
⌉,
(7.6)
where ⌈a⌉denotes the smallest integer greater than or equal to a. Thus,
the probabilistic constraint (7.4) has a linear deterministic equivalent (7.5).
This is the desired situation with probabilistic constraints. Very often, the
deterministic equivalents correspond to nonlinear constraints and the ques-
tion is whether they deﬁne a convex feasible region. This will be studied in
Section 3.2.


## Page 85

66
2. Uncertainty and Modeling Issues
Exercises
1. Consider Exercise 1 of Section 1.5.
(a) Show that this is a two-stage stochastic program with ﬁrst-stage
integer decision variables. Observe that for a random variable
with integer realizations, the second-stage variables can be as-
sumed continuous, because the optimal second-stage decisions
are automatically integer.
Assume that Northam revises its seating policy every year.
Is a multistage program needed?
(b) Assume that the data in Exercise 1 correspond to the demand for
seat reservations. Assume that there is a 50% probability that
all clients with a reservation eﬀectively show up and that 10 or
20% no-shows occur with equal probability. Model this situation
as a three-stage program, with ﬁrst-stage decisions as before,
second-stage decisions corresponding to the number of accepted
reservations, and third-stage decisions corresponding to eﬀective
seat occupation. Show that the third stage is a simple recourse
program with a reward for each occupied seat and a penalty for
each denied reservation.
(c) Consider now the situation where the number of seats has been
ﬁxed to 12, 24, and 140 for the ﬁrst class, business class, and
economy class, respectively. Assume the top management esti-
mates the reward of an occupied seat to be 4, 2, and 1 in the
ﬁrst class, business class, and economy class, respectively, and
the penalty for a denied reservation is 1.5 times the reward.
Model the corresponding problem as a recourse program. Find
the optimal acceptance policy with the data of Exercise 1 in
Section 1.5 and no-shows as in (b) of the current exercise. To
simplify, assume that passengers with a denied reservation are
not seated in a higher class even if a seat is available there.
2. Let x represent the ﬁrst-stage production of a given good. Let ξ be the
demand for the same good. A typical second stage would consist of
selling as much as possible, namely, min(ξ, x). Obtain a closed form
expression for the recourse function Eξ[min(ξ, x)] in the following
cases of ξ:
(a) Poisson distribution,
(b) A normal distribution.
3. Consider an airplane with x seats. Assume passengers with reserva-
tions show up with probability 0.90, independently of each other.


## Page 86

2.8 Relationship to Other Decision-Making Models
67
(a) Let x = 40. If 42 passengers receive a reservation, what is the
probability that at least one is denied seat.
(b) Let x = 50. How many reservations can be accepted under the
constraint that the probability of seating all passengers who ar-
rive for the ﬂight is greater than 90% ?
2.8
Relationship to Other Decision-Making
Models
The stochastic programming models considered in this section illustrate
the general form of a stochastic program. While this form can apply to
virtually all decision-making problems with unknown parameters, certain
characteristics typify stochastic programs and form the major emphasis
of this book. In general, stochastic programs are generalizations of deter-
ministic mathematical programs in which some uncontrollable data are
not known with certainty. The key features are typically many decision
variables with many potential values, discrete time periods for decisions,
the use of expectation functionals for objectives, and known (or partially
known) distributions. The relative importance of these features contrasts
with similar areas, such as statistical decision theory, decision analysis,
dynamic programming, Markov decision processes, and stochastic control.
In the following subsections, we consider these other areas of study and
highlight the diﬀerent emphases.
a. Statistical decision theory and decision analysis
Wald [1950] developed much of the foundation of optimal statistical deci-
sion theory (see also DeGroot [1970] and Berger [1985]). The basic motiva-
tion was to determine best levels of variables that aﬀect the outcome of an
experiment. With variables x in some set X, random outcomes, ω ∈Ω, an
associated distribution, F(ω), and a reward or loss associated with the ex-
periment under outcome ω of r(x, ω), the basic problem is to ﬁnd x ∈X to
max Eω[r(x, ω)|F] = max

ω
r(x, ω)dF(ω).
(8.1)
The problem in (8.1) is also the fundamental form of stochastic program-
ming. The major diﬀerences in emphases between the ﬁelds stem from
underlying assumptions about the relative importance of diﬀerent aspects
of the problem.
In stochastic programming, one generally assumes that diﬃculties in
ﬁnding the form of the function r and changes in the distribution F as
a function of actions are small in comparison to ﬁnding the expectations


## Page 87

68
2. Uncertainty and Modeling Issues
with known distributions and an optimal value x with all other informa-
tion known. The emphasis is on ﬁnding a solution after a suitable problem
statement in the form (8.1) has been found. For example, in the simple
farming example in Section 1.1, the number of possible planting conﬁg-
urations (even allowing only whole-acre lots) is enormous. Enumerating
the possibilities would be hopeless. Stochastic programming avoids such
ineﬃciencies through an optimization process.
We might suppose that the ﬁelds or crop varieties are new and that the
farmer has little direct information about yields. In this case, the yield
distribution would probably start as some prior belief but would be modi-
ﬁed as time went on. This modiﬁcation and possible eﬀects of varying crop
rotations to obtain information are the emphases from statistical decision
theory. If we assumed that only limited variation in planting size (such as
50-acre blocks) was possible, then the combinatorial nature of the prob-
lem would look less severe. Enumeration might then be possible without
any particular optimization process. If enumeration were not possible, the
farmer might still update the distributions and objectives and use stochas-
tic programming procedures to determine next year’s crops based on the
updated information.
In terms of (8.1), statistical decision theory places a heavy emphasis on
changes in F to some updated distribution ˆFx that depends on a partial
choice of x and some observations of ω. The implied assumption is that
this part of the analysis dominates any solution procedure, as when X is a
small ﬁnite set that can be enumerated easily.
Decision analysis (see, e.g., Raiﬀa [1968]) can be viewed as a particular
part of optimal statistical decision theory. The key emphases are often on
acquiring information about possible outcomes, on evaluating the utility
associated with various outcomes, and on deﬁning a limited set of possible
actions (usually in the form of a decision tree). For example, consider the
capacity expansion problem in Section 1.3. We considered a wide number
of alternative technology levels and production decisions. In that model,
we assumed that demand in each period was independent of the demand in
the previous period. This characteristic gave the block separability property
that can allow eﬃcient solutions for large problems.
A decision analytic model might apply to the situation where an electric
utility’s demand depends greatly on whether a given industry locates in the
region. The decision problem might then be broken into separate stochastic
programs depending on whether the new industry demand materializes
and whether the utility starts on new plants before knowing the industry
decision. In this framework, the utility ﬁrst decides whether to start its own
projects. The utility then observes whether the new industry expands into
the region and faces the stochastic program form from Section 1.4 with four
possible input scenarios about the available capacity when the industry’s
location decision is known (see Figure 3).


## Page 88

2.8 Relationship to Other Decision-Making Models
69
FIGURE 3. Decision tree for utility with stochastic programs on leaves.
The two stochastic programs given each initial decision allow for the
evaluation of expected utility given the two possible outcomes and two
possible initial decisions. The actual initial decision taken on current ca-
pacity expansion would then be made by taking expectations over these
two outcomes.
Separation into distinct possible outcomes and decisions and the real-
ization of diﬀerent distributions depending on the industry decision give
this model a decision analysis framework. In general, a decision analytic
approach would probably also consider multiple attributes of the capacity
decisions (for example, social costs for a given location) and would concen-
trate on the value of risk in the objective. It would probably also entail
consideration of methods for obtaining information about the industry’s
decision and contingent decisions based on the outcomes of these investi-
gations. Of course, these considerations can all be included in a stochastic
program, but they are not typically the major components of a stochastic
programming analysis.
b. Dynamic programming and Markov decision processes
Much of the literature on stochastic optimization considers dynamic pro-
gramming and Markov decision processes (see, e.g., Heyman and Sobel
[1984], Bellman [1957], Ross [1983], and Kall and Wallace [1994] for a dis-
cussion relating to stochastic programming). In these models, one searches


## Page 89

70
2. Uncertainty and Modeling Issues
for optimal actions to take at generally discrete points in time. The actions
are inﬂuenced by random outcomes and carry one from some state at some
stage t to another state at stage t + 1. The emphasis in these models is
typically in identifying ﬁnite (or, at least, low-dimensional) state and ac-
tion spaces and in assuming some Markovian structure (so that actions and
outcomes only depend on the current state).
With this characterization, the typical approach is to form a backward
recursion resulting in an optimal decision associated with each state at
each stage. With large state spaces, this approach becomes quite compu-
tationally cumbersome although it does form the basis of many stochastic
programming computation schemes as given in Chapter 7. Another ap-
proach is to consider an inﬁnite horizon and use discounting to establish
a stationary policy (see Howard [1960] and Blackwell [1965]) so that one
need only ﬁnd an optimal decision associated with a state for any stage.
A typical example of this is in investment. Suppose that instead of saving
for a speciﬁc time period in the example of Section 1.2, you wish to max-
imize a discounted expected utility of wealth in all future periods. In this
case, the state of the system is the amount of wealth. The decision or action
is to determine what amount of the wealth to invest in stock and bonds.
We could discretize to varying wealth levels and then form a problem as
follows:
max
∞

t=1
ρtE[qy(t) −rw(t)]
(8.2)
s. t. x(1, 1) + x(2, 1) = b,
ξ(1, t)x(1, t) + ξ(2, t)x(2, t) −y(t) + w(t) = G,
ξ(1, t)x(1, t) + ξ(2, t)x(2, t) = x(1, t + 1) + x(2, t + 1),
x(i, t), y(t), w(t) ≥0, x ∈N,
where N is the space of nonanticipative decisions and ρ is some discount
factor. This approach could lead to ﬁnding a stationary solution to
z(b) =
max
x(1)+x(2)=b{E[−q(G −ξ(1)x(1) −ξ(2)x(2))−
−r(G −ξ(1)x(1) −ξ(2)x(2))+ + ρE[z(ξ(1)x(1) + ξ(2)x(2))]}.
(8.3)
Again, problem (8.2) ﬁts the general stochastic programming form, but par-
ticular solutions as in (8.3) are more typical of Markov decision processes.
These are not excluded in stochastic programs, but stochastic programs
generally do not include the Markovian assumptions necessary to derive
(8.3).
c. Comparison to optimal stochastic control
Stochastic control models are often similar to stochastic programming mod-
els. The diﬀerences are mainly due to problem dimension (stochastic pro-


## Page 90

2.8 Relationship to Other Decision-Making Models
71
grams would generally have higher dimension), emphases on control rules in
stochastic control, and more restrictive constraint assumptions in stochas-
tic control. In many cases, the distinction is, however, not at all clear.
As an example, suppose a more general formulation of the ﬁnancial model
in Section 1.2. There, we considered a speciﬁc form of the objective func-
tion, but we could also use other forms. For example, suppose the objective
was generally stated as minimizing some cost rt(x(t), u(t)) in each time pe-
riod t, where u(t) are the controls u((i, j), t, s) that correspond to actual
transactions of exchanging asset i into asset j in period t under scenario s.
In this case, problem (1.2.2) becomes:
min z =

s
p(s)(
H

t=1
rt(x(t, s),u(t, s), s))
s. t. x(0, s)= b,
x(t, s) + ξ(s)T u(t, s)= x(t + 1, s), t = 0, . . . , H,
x(s), u(s) nonanticipative,
(8.4)
where ξ(s)T represents returns on investments minus transaction costs. Ad-
ditional constraints may be incorporated into the objective of (8.4) through
penalty terms.
Problem (8.4) is fairly typical of a discrete time control problem gov-
erned by a linear system. The general emphasis in control approaches to
such problems is for linear, quadratic, Gaussian (LQG) models (see, for ex-
ample, Kushner [1971], Fleming and Rishel [1975], and Dempster [1980]),
where we have a linear system as earlier, but where the randomness is
Gaussian in each period (for example, ξ is known but the state equation for
x(t + 1, s) includes a Gaussian term), and rt is quadratic. In these models,
one may also have diﬃculty observing x so that an additional observation
variable y(t) may be present.
The LQG problem leads to Kalman ﬁltering solutions (see, for exam-
ple, Kalman [1969]). Various extensions of this approach are also possible,
but the major emphasis remains on developing controls with speciﬁc de-
cision rules to link observations directly into estimations of the state and
controls. In stochastic programming models, general constraints (such as
non-negative state variables) are emphasized. In this case, most simple de-
cision rules forms (such as when u is a linear function of state) fail to obtain
satisfactory solutions (see, for example, Gartska and Wets [1974]). For this
reason, stochastic programming procedures tend to search for more general
solution characteristics.
Stochastic control procedures may, of course, apply but stochastic pro-
gramming tends to consider more general forms of interperiod relationships
and state space constraints. Other types of control formulations, such as
robust control, may also be considered speciﬁc forms of a stochastic pro-
gram that are amenable to speciﬁc techniques to ﬁnd control policies with
given characteristics.


## Page 91

72
2. Uncertainty and Modeling Issues
Continuous time stochastic models (see, e.g., Harrison [1985]) are also
possible but generally require more simpliﬁed models than those consid-
ered in stochastic programming. Again, continuous time formulations are
consistent with stochastic programs but have not been the main emphasis
of research or the examples in this book. In certain examples again, they
may be quite relevant (see, for example, Harrison and Wein [1990] for an
excellent application in manufacturing) in deﬁning fundamental solution
characteristics, such as the optimality of control limit policies.
In all these control problems, the main emphasis is on characterizing solu-
tions of some form of the dynamic programming Bellman-Hamilton-Jacobi
equation or application of Pontryagin’s maximum principle. Stochastic pro-
grams tend to view all decisions from beginning to end as part of the pro-
cedure. The dependence of the current decision on future outcomes and the
transient nature of solutions are key elements. Section 3.5 provides some
further explanation by describing these characteristics in terms of general
optimality conditions.
c. Summary
Stochastic programming is simply another name for the study of optimal
decision making under uncertainty. The term stochastic programming em-
phasizes a link to mathematical programming and algorithmic optimization
procedures. These considerations dominate work in stochastic program-
ming and distinguish stochastic programming from other ﬁelds of study.
In this book, we follow this paradigm of concentrating on representation
and characterizations of optimal decisions and on developing procedures
to follow in determining optimal or approximately optimal decisions. This
development begins in the next chapter with basic properties of stochastic
program solution sets and optimal values.
Exercises
1. Consider the design problem in Section 1.4. Suppose the design de-
cision does not completely specify x in (1.4.1), but the designer only
knows that if a value ˆx is speciﬁed then x ∈[.99ˆx, 1.01ˆx]. Suppose a
uniform distribution for x is assumed initially on this interval. How
would the formulation in Section 1.4 be modiﬁed to account for in-
formation as new parts are produced?
2. From the example in Section 1.2, suppose that a goal in each period
is to realize a 16% return with penalties q = 1 and r = 4 as before.
Formulate the problem as in (8.2).


## Page 92

2.9 Short Reviews
73
2.9
Short Reviews
a. Linear Programming
Consider a linear program (L.P.) of the form
max{cT x|Ax = b, x ≥0},
(9.1)
where A is an m × n matrix, x and c are n × 1 vectors, and b is an m × 1
vector. If needed, any inequality constraint can be transformed into an
equality by the addition of slack variables:
ai·x ≤bibecomes ai·x + si = bi,
where si is the slack variable of row i and ai· is the ith row of matrix A.
A solution to (9.1) is a vector x that satisﬁes Ax = b. A feasible solution
is a solution x with x ≥0. An optimal solution x∗is a feasible solution such
that cT x∗≥cT x for all feasible solutions x. A basis is a choice of n linearly
independent columns of A. Associated to a basis is a submatrix B of the
corresponding columns, so that, after a suitable rearrangement, A can be
partitioned into A = [B, N]. Associated with a basis is a basic solution,
xB = B−1b, xN = 0, and z = cT
BB−1b, where [xB, xN] and [cB, cN] are
partitions of x and c following the basic and nonbasic columns. We use
B−1 to denote the inverse of B, which is known to exist because B has
linearly independent columns and is square.
In geometric terms, basic solutions correspond to extreme points of the
polyhedron, {x|Ax = b, x ≥0}. A basis is feasible (optimal) if its associated
basic solution is feasible (optimal). The conditions for feasibility are B−1b ≥
0. The conditions for optimality are that in addition to feasibility, the
inequalities, cT
N −cT
BB−1N ≤0, hold.
Linear programs are routinely solved by widely distributed, easy-to-use
linear program solvers. Access to such a solver would be useful for some
exercises in this book. For a better understanding, some examples and
exercises also use manual solutions of linear programs.
Finding an optimal solution is equivalent to ﬁnding an optimal dictio-
nary, a deﬁnition of individual variables in terms of the other variables.
In the simplex algorithm, starting from a feasible dictionary, the next one
is obtained by selecting an entering variable (any nonbasic variable whose
increase leads to an increase in the objective value), then ﬁnding a leaving
variable (the ﬁrst to become negative as the entering variable increases),
then realizing a pivot substituting the entering for the leaving variable in
the dictionary. An optimal solution is reached when no entering variable
can be found.
A linear program is unbounded if an entering variable exists for which no
leaving variable can be found. In some cases, a feasible initial dictionary
is not available at once. Then, phase one of the simplex method consists


## Page 93

74
2. Uncertainty and Modeling Issues
of ﬁnding such an initial dictionary. A number of artiﬁcial variables are
introduced to make the dictionary feasible. The phase one procedure min-
imizes the sum of artiﬁcials using the simplex method. If a solution with a
sum of artiﬁcials equal to zero exists, then the original problem is feasible
and phase two continues with the true objective function. If the optimal
solution of the phase one problem is nonzero, then the original problem is
infeasible.
As an example, consider the following linear program:
max
−x1
+3x2
s. t.
2x1
+x2
≥5,
x1
+x2
≤3,
x1,
x2
≥0.
Adding slack variables s1 and s2, the two constraints read
2x1
+x2
−s1
= 5,
x1
+x2
+s2
= 3.
The natural choice for the initial basis is (s1, s2). This basis is infeasible as
s1 would obtain the value −5. An artiﬁcial variable (a1) is added to row
one to form:
2x1 + x2 −s1 + a1 = 5.
The phase one problem consists of minimizing a1, i.e., ﬁnding −max −a1.
Let z = −a1 be the phase one objective, which after substituting for a1
gives the initial dictionary in phase one:
z
= −5
+2x1
+x2
−s1,
a1
= 5
−2x1
−x2
+s1,
s2
= 3
−x1
−x2,
corresponding to the initial basis (a1, s2). Entering candidates are x1 and x2
as they both increase the objective value. Choosing x1, the leaving variable
is a1 (because it becomes zero for x1 = 2.5 while s2 becomes zero only for
x1 = 3). Substituting x1 for a1, the second dictionary becomes:
z
=
−a1,
x1
= 2.5
−0.5x2
+0.5s1
−0.5a1,
s2
= 0.5
−0.5x2
−0.5s1
+0.5a1.
This dictionary is an optimal dictionary for phase one. (No nonbasic vari-
able would possibly increase x.) This means the original problem is feasible.
(In fact, the basis (x1, s2) is feasible with solution x1 = 2.5, x2 = 0.0).)
We now turn to phase two. We replace the phase one objective with the
original objective:
z = −x1 + 3x2 = −2.5 + 3.5x2 −0.5s1.


## Page 94

2.9 Short Reviews
75
By removing the artiﬁcial variable a1 (as it is not needed anymore), we
obtain the following ﬁrst dictionary in phase two:
z
= −2.5
+3.5x2
−0.5s1,
x1
= 2.5
−0.5x2
+0.5s1,
s2
= 0.5
−0.5x2
−0.5s1.
The next entering variable is x2 with leaving variable s2. After substitution,
we obtain the ﬁnal dictionary:
z
= 1
−4s1
−7s2,
x1
= 2
+s1
+s2,
x2
= 1
−s1
−2s2,
which is optimal because no nonbasic variable is a valid entering variable.
The optimal solution is x∗= (2, 1)T with z∗= 1.
b. Duality for linear programs
The dual of the so-called primal problem (9.1) is:
min{πT b|πT A ≥cT , π unrestricted}.
(9.2)
Variables π are called dual variables. One such variable is associated with
each constraint of the primal. When the primal constraint is an equality,
the dual variable is free (unrestricted in sign). Dual variables are sometimes
called shadow prices or multipliers (as in nonlinear programming). The dual
variable πi may sometimes be interpreted as the marginal value associated
with resource bi.
If the dual is unbounded, then the primal is infeasible. Similarly, if the
primal is unbounded, then the dual is infeasible. Both problems can also
be simultaneously infeasible.
If x is primal feasible and π is dual feasible, then cT x ≤πT b. The primal
has an optimal solution x∗if and only if the dual has an optimal solution
π∗. In that case, cT x∗= (π∗)T b and the primal and dual solutions satisfy
the complementary slackness conditions:
(ai·)x∗= bi or π∗
i = 0 or both, for any i = 1, . . . , m,
(π∗)T a·j = cj or x∗
j = 0 or both, for any j = 1, . . . , n,
where a·j is the jth column of A and, as before, ai· is the ith row of A.
An alternative presentation is to say that s∗
i π∗
i = 0, where si is the slack
variable of the ith constraint, i.e., either the slack or the dual variable
associated with a constraint is zero, and similarly for the second condition.
Thus, the optimal solution of the dual can be recovered from the optimal
solution for the primal, and vice versa.


## Page 95

76
2. Uncertainty and Modeling Issues
The optimality conditions can also be interpreted to say that either there
exists some improving direction, w, from a current feasible solution, ˆx, so
that cT w > 0, wj ≥0 for all j ∈N, N = {j|ˆxj = 0}, and ai·w ≤0
for all i ∈I , I = {i|ai·ˆx = bi} or there exists some π ≥0 such that
	
i∈I πiaij ≤cj for all j ∈N, 	
i∈I πiaij = cj for all j̸ ∈N, but both
cannot occur. This result is equivalent to the Farkas lemma, which gives
alternative systems with or without solutions.
The dual simplex method replicates on the primal solution what the it-
erations of the simplex method would be on the dual problem: it ﬁrst ﬁnds
the leaving variable (one that is strictly negative) then the entering vari-
able (the ﬁrst one that would become positive in the objective line). The
dual simplex is particularly useful when a solution is already available to
the original primal problem and some extra constraint or bound is added
to the problem. The reader is referred to Chv´atal [1980, pp. 152–157] for a
detailed presentation.
Other material not covered in this section is meant to be restrictive to
a given topic area. The next section discusses more of the mathematical
properties of solutions and functions.
c. Nonlinear programming and convex analysis
When objectives and constraints may contain nonlinear functions, the op-
timization problem becomes a nonlinear program. The nonlinear program
analogous to (9.1) has the form
min{f(x)|g(x) ≤0, h(x) = 0},
(9.3)
where x ∈ℜn, f : ℜn →ℜ, g : ℜn →ℜm, and h : ℜn →ℜl. We may also
assume that the range of f may include ∞to allow the objective to include
constraints directly through an indicator function:
δ(x|X) =

0
if g(x) ≤0, h(x) = 0,
+∞
otherwise,
where X is the set of x satisfying the constraints in (9.3), i.e., the feasible
region.
In this book, the feasible region is usually a convex set so that X contains
any convex combination,
s

i=1
λixi,
s

i=1
λi = 1, λi ≥0, i = 1, . . . , s,
of points, xi, i = 1, . . . , s, that are in the feasible region. Extreme points of
the region are points that cannot be expressed as a convex combination of
two distinct points also in the region. The set of all convex combinations
of a given set of points is its convex hull.


## Page 96

2.9 Short Reviews
77
The feasible region is also most generally closed so that it contains all
limits of inﬁnite sequences of points in the region. The region is also gener-
ally connected, so that, for any x1 and x2 in the region, there exists some
path of points in the feasible region connecting x1 to x2 by a function,
η : [0, 1] →ℜn that is continuous with η(0) = x1 and η(1) = x2. For
certain results, we may also assume the region is bounded so that a ball of
radius M, {x|∥x∥≤M}, contains the entire set of feasible points. Other-
wise, the region is unbounded. Note that a region may be unbounded while
the optimal value in (9.1) or (9.3) is still bounded. In this case, the region
often contains a cone, i.e., a set S such that if x ∈S, then λx ∈S for all
λ ≥0. When the region is both closed and bounded, then it is compact.
The set of equality constraints, h(x) = 0, is often aﬃne, i.e., they can be
expressed as linear combinations of the components of x and some constant.
In this case, each constraint, hi(x) = 0, is a hyperplane, ai·x −bi = 0, as
in the linear program constraints. In this case, h(x) = 0, deﬁnes an aﬃne
space, a translation of the parallel subspace, Ax = 0. The aﬃne space
dimension is the same as its parallel subspace, i.e., the maximum number
of linearly independent vectors in the subspace.
With nonlinear constraints and inequalities, the region may not be an
aﬃne space, but we often consider the lowest-dimension aﬃne space con-
taining them, i.e., the aﬃne hull of the region. The aﬃne hull is useful in
optimality conditions because it distinguishes interior points that can be
the center of a ball entirely within the region from the relative interior (ri),
which can be the center of a ball whose intersection with the aﬃne hull
is entirely within the region. When a point is not in a feasible region, we
often take its projection into the region using an operator, Π. If the region
is X, then the projection of x onto X is Π(x) = argmin{∥w −x∥|w ∈X}.
In this book, we generally assume that the objective function f is a
convex function, i.e., such that
f(λx1 + (1 −λ)x2) ≤λf(x1) + (1 −λ)f(x2),
0 ≤λ ≤1. If f also is never −∞and is not +∞everywhere, then f is a
proper convex function. The region where f is ﬁnite is called the eﬀective
domain of f (domf). We can also deﬁne convex functions in terms of the
epigraph of f, epi(f) = {(x, β)|β ≥f(x)}. In this case, f is convex if and
only if its epigraph is convex. If −f is convex, then f is concave.
Often, we assume that f has directional derivatives, f ′(x; w), that are
deﬁned as:
f ′(x; w) = lim
λ↓0
f(x + λw) −f(x)
λ
.
When these limits exist and do not vary in all directions, then f is diﬀer-
entiable, i.e., there exists a gradient, ∇f, such that
∇f T w = f ′(x; w)


## Page 97

78
2. Uncertainty and Modeling Issues
for all directions w ∈ℜn. We sometimes distinguish this standard form of
diﬀerentiability from stricter forms as Gˆateaux or G-diﬀerentiability. The
stricter forms impose more conditions on the directional derivative such as
uniform convergence over compact sets (Hadamard derivatives).
We also consider Lipschitz continuous or Lipschitzian functions such that
|f(x) −f(w)| ≤M∥x −w∥for any x and w and some M < ∞. If this
property holds for all x and w in a set X, then f is Lipschitizian relative
to X. When this property only holds locally, i.e., for ∥w −x∥≤ǫ for some
ǫ > 0, then f is locally Lipschitz at x.
Among diﬀerentiable functions, we often use quadratic functions that
have a Hessian matrix of second derivatives, D, and can be written as
f(x) = cT x + 1
2xT Dx.
Many functions are not, however, diﬀerentiable. In this case, we express
optimality in terms of subgradients at a point x, or vectors, η, such that
f(w) ≥f(x) + ηT (w −x)
for all w. In this case, {(x, β)|β = f(x) + ηT (w −x)} is a supporting hyper-
plane of f at x. The set of subgradients at a point x is the subdiﬀerential
of f at x, written ∂f(x).
Other useful properties include that f is piecewise linear, i.e., such that
f(x) is linear over regions deﬁned by linear inequalities. When f is sep-
arable so that f(x) = 	n
i=1 fi(xi), then other advantages are possible in
computation.
Given f convex and a convex feasible region in (9.3), we can deﬁne con-
ditions that an optimal solution x∗and associated multipliers (π∗, ρ∗) must
satisfy. In general, these conditions require some form of regularity condi-
tion. A common form is that there exists some ˆx such that g(ˆx) < 0 and h
is aﬃne. This is generally called the Slater condition.
Given a regularity condition of this type, if the constraints in (9.3) deﬁne
a feasible region, then x∗is optimal if and only if the Karush-Kuhn-Tucker
conditions hold so that x∗∈X and there exists π∗≥0, ρ∗such that
∇f(x∗) + (π∗)T ∇g(x∗) + (ρ∗)T ∇h(x∗) = 0, ∇g(x∗)T π∗= 0.
(9.4)
Optimality can also be expressed in terms of the Lagrangian:
L(x, π, ρ) = f(x) + πT g(x) + ρT h(x),
so that sequentially minimizing over x and maximizing over π (in both
orders) produces the result in (9.4). This occurs through a Lagrangian dual
problem to (9.3) as
max
π≥0,ρ inf
x f(x) + πT g(x) + ρT h(x),
(9.5)


## Page 98

2.9 Short Reviews
79
which is always a lower bound on the objective in (9.3) (weak duality), and,
under the regularity conditions, yields equal optimal values in (9.3) and
(9.4) (strong duality). In many cases, the Lagrangian can also be interpreted
with the conjugate function of f, deﬁned as
f ∗(π) = sup
x {πT x −f(x)},
which is also a convex function if f is convex.
Our algorithms often apply to the Lagrangian to obtain convergence, i.e.,
a sequence of solutions, xν →x∗. In some cases, we also approximate the
function so that f ν →f in some way. If this convergence is pointwise, then
f ν(x) →f(x) for each x individually. If the convergence is uniform on a
set X, then, for any ǫ > 0, there exists N(ǫ) such that for all ν ≥N(ǫ) and
all x ∈X, |f ν(x) −f(x)| < ǫ.


## Page 99



## Page 100

Part II
Basic Properties
81


## Page 101



## Page 102

3
Basic Properties and Theory
This chapter considers the basic properties and theory of stochastic pro-
gramming. As throughout this book, the emphasis is on results that have di-
rect application in the solution of stochastic programs. Proofs are included
for those results we consider most central to the overall development.
The main properties we consider are formulations of deterministic equiv-
alent programs to a stochastic program, the forms of the feasible region
and objective function, and conditions for optimality and solution stabil-
ity. Our focus is on stochastic programs with recourse, and, in particular,
for stochastic linear programs. The ﬁrst section describes two-stage ver-
sions of these problems in detail. It assumes some knowledge of convex sets
and functions.
Sections 2 to 5 add extensions to the results in Section 1 by allowing
additional forms of constraints, objectives, and decision variables. Section 2
considers problems with probabilistic or chance constraints that occur with
some ﬁxed probability. Section 3 considers problems with integer variables,
while Section 4 extends results to include nonlinear functions. Section 5
concludes the chapter with multiple-stage problems.


## Page 103

84
3. Basic Properties and Theory
3.1
Two-Stage Stochastic Linear Programs with
Fixed Recourse
a. Formulation
As in Chapter 2, we ﬁrst form the basic two-stage stochastic linear program
with ﬁxed recourse. It is repeated here for clarity.
min z =cT x + Eξ[min q(ω)T y(ω)]
(1.1)
s.t. Ax = b,
T(ω)x + Wy(ω) = h(ω),
x ≥0, y(ω) ≥0,
where c is a known vector in ℜn1, b a known vector in ℜm1, A and W
are known matrices of size m1 × n1 and m2 × n2, respectively, and W is
called the recourse matrix, which we assume here is ﬁxed. This allows us to
characterize the feasibility region in a convenient manner for computation.
If W is not ﬁxed, we may have diﬃculties, as shown next.
For each ω, T(ω) is m2 × n1, q(ω) ∈ℜn2 and h(ω) ∈ℜm2. Piecing
together the stochastic components of the problem, we obtain a vector
ξT (ω) = (q(ω)T , h(ω)T , T1·(ω), . . . , Tm2·(ω)) with N = n2 +m2 +(m2 ×n1)
components, where Ti·(ω) is the ith row of the technology matrix T(ω). As
before, Eξ represents the mathematical expectation with respect to ξ. Let
also Ξ ⊆ℜN be the support of ξ, i.e., the smallest closed subset in ℜN such
that P{ξ ∈Ξ} = 1. As said in Section 2.4, the constraints are assumed to
hold almost surely.
Problem (1.1) is equivalent to the so-called deterministic equivalent pro-
gram (D.E.P.):
min z =cT x + Q(x)
(1.2)
s.t. Ax = b,
x ≥0,
where
Q(x) = EξQ(x, ξ(ω))
(1.3)
and
Q(x, ξ(ω)) = min
y {q(ω)T y|Wy = h(ω) −T(ω)x, y ≥0}.
(1.4)
Examples of formulations (1.1) and (1.2-4) have been given in Chapter 1.
In the farmer’s problem, x represents the surfaces devoted to each crop, ξ
represents the yields so that only the technology matrix T(ω) is stochas-
tic (because prices q and requirements h are ﬁxed), and y represents the
sales and purchases of the various crops. Formulations (1.1) and (1.2)–(1.4)
apply for both discrete and continuous random variables. Examples with
continuous random yields have also been given for the farmer’s problem.


## Page 104

3.1 Two-Stage Stochastic Linear Programs with Fixed Recourse
85
This representation clearly illustrates the sequence of events in the re-
course problem. First-stage decisions x are taken in the presence of uncer-
tainty about future realizations of ξ. In the second stage, the actual value
of ξ becomes known and some corrective actions or recourse decisions y
can be taken. First-stage decisions are, however, chosen by taking their
future eﬀects into account. These future eﬀects are measured by the value
function or recourse function, Q(x), which computes the expected value of
taking decision x.
When T is nonstochastic, the original formulation (1.2)–(1.4) can be
replaced by
min z =cT x + Ψ(χ)
(1.5)
s.t. Ax = b,
Tx −χ = 0,
x ≥0,
where Ψ(χ) = Eξψ(χ, ξ(ω)) and ψ(χ, ξ(ω)) = min{q(ω)T y|Wy = h(ω) −
χ, y ≥0}. This formulation stresses the fact that choosing x corresponds
to generating an m2-dimensional tender χ = Tx to be bid against the
outcomes h(ω) of the random events.
The diﬃculty inherent in stochastic programming clearly lies in the com-
putational burden of computing Q(x) for all x in (1.2)–(1.4), or Ψ(χ) for
all χ in (1.5). It is no surprise therefore that the properties of the deter-
ministic equivalent program in general and of the functions Q(x) or Ψ(χ)
have been extensively studied. The next sections present some of the known
properties. Section 5.1 presents a general algorithm for solving (1.2)–(1.4)
when ξ is a discrete random variable.
b. Feasibility sets
Although in the rest of the book we restrict ourselves to the ﬁxed recourse
case deﬁned in the previous section, here we study the situation where the
recourse matrix W can be random. This is because the main issues about
deﬁnitions of second-stage feasibility sets depend on whether W is ﬁxed.
For ﬁxed x and ξ, the value Q(x,ξ) of the second-stage program is given
by
Q(x,ξ) = min
y {q(ω)T y|W(ω)y = h(ω) −T(ω)x, y ≥0}.
(1.6)
When the mathematical program (1.6) is unbounded below or infeasible,
the value of the second-stage program is deﬁned to be −∞or +∞, respec-
tively.
The expected second-stage value function is, as given in (1.3),
Q(x) = EξQ(x,ξ).


## Page 105

86
3. Basic Properties and Theory
Let us ﬁrst consider the situation when ξ is a ﬁnite discrete random variable,
namely, ξ ∈Ξ with Ξ a ﬁnite or countable set.
The second-stage value function is then the weighted sum of the Q(x,ξ)
values for the various possible realizations of ξ. To make the deﬁnition
complete, we make the additional convention +∞+ (−∞) = +∞. This
corresponds to a conservative attitude, rejecting any ﬁrst-stage decision
that could lead to an undeﬁned recourse action even if there is some real-
ization of the random vector inducing an inﬁnitely low-cost function. Let
K1 = {x|Ax = b, x ≥0} be the set determined by the ﬁxed constraints,
namely, those that do not depend on the particular realization of the ran-
dom vector, and let K2 = {x|Q(x) < ∞} be the second-stage feasibility
set. We may now redeﬁne the deterministic equivalent program as follows
min z(x) = cT x + Q(x)
s.t. x ∈K1 ∩K2.
From a practical point of view, it is not absolutely necessary to have a
complete description of the region of ﬁniteness of Q(x). On the other hand,
it is desirable to be able to check if a particular ﬁrst-stage decision x leads
to a ﬁnite second-stage value without having to compute that value. The
deﬁnition of K2 is not useful in that respect. We therefore consider an
alternative deﬁnition. Let
K2(ξ) = {x|Q(x, ξ) < +∞}
be the elementary feasibility sets and
KP
2 = {x| for all ξ ∈Ξ,
y ≥0 exists s.t. Wy = h −T · x}
= ∩ξ∈ΞK2(ξ).
The set KP
2 is said to deﬁne the possibility interpretation of second-stage
feasibility sets. A decision x belongs to the set KP
2 if, for all “possible”
values of the random vector ξ, a feasible second-stage decision y can be
taken. Note that the decision y can be diﬀerent from one value ξ to another,
although this is not stressed in the notation.
Theorem 1.
a. For each ξ, the elementary feasibility set is a closed convex polyhedron,
hence the set KP
2 is closed and convex.
b. When Ξ is ﬁnite, then KP
2 is also polyhedral and coincides with K2.
Proof:
For each ξ, K2(ξ) is deﬁned by a set of linear constraints, which
suﬃces to prove a. A particular x belongs to K2 if Q(x) is bounded above.
Because Q(x) is a positively weighted sum of ﬁnitely many Q(x, ξ) values
and, due to our convention, +∞+(−∞), Q(x) is bounded above only if each


## Page 106

3.1 Two-Stage Stochastic Linear Programs with Fixed Recourse
87
Q(x, ξ) is bounded above, which implies x belongs to K2(ξ) for all ξ, which
in turn implies x belongs to KP
2 . Similarly, if x belongs to KP
2 , Q(x, ξ) is
bounded above for all values, which implies Q(x) is bounded above and x
belongs to K2.
The case where ξ is a continuous random variable may lead to some
diﬃculties. To illustrate this, consider an example where the second stage
is deﬁned by
Q(x, ξ) = min
y {y|ξy = 1 −x, y ≥0}
where ξ has a triangular distribution on [0, 1], namely, P(ξ ≤u) = u2. Note
that here W reduces to a 1 × 1 matrix and is the only random element.
For all ξ in (0, 1], the optimal y is 1−x
ξ
, so that
K2(ξ) = {x|x ≤1}
and
Q(x, ξ) = 1 −x
ξ
, for x ≤1.
When ξ = 0, no y exists such that 0 · y = 1 −x, unless x = 1, so that
K2(0) = {x|x = 1}.
Now, for x̸ = 1, Q(x, 0) should normally be +∞. However, because the
probability that ξ = 0 is zero, the convention is to take Q(x, 0) = 0. This
corresponds to deﬁning 0 · ∞= 0. A more detailed justiﬁcation can be
found in Walkup and Wets [1967].
Hence,
KP
2 = {x|x = 1} ∩{x|x ≤1} = {x|x = 1}
while
Q(x) =
 1
0
1 −x
ξ
· 2ξdξ = 2(1 −x)
for all x ≤1,
so that K2 = {x|x ≤1} and KP
2 is strictly contained in K2. The diﬀerence
between the two sets relates to the fact that a point is not in KP
2 as soon
as it is infeasible for some ξ value, regardless of the distribution of ξ, while
K2 does not consider infeasibilities occurring with zero probability.
Fortunately, this kind of diﬃculty rarely occurs for programs with a
ﬁxed W matrix. It never occurs when the random vector satisﬁes some
conditions.
Another diﬃculty that could arise and would cause the sets KP
2 and K2
to be diﬀerent, would be to have Q(x, ξ) bounded above with probability
one and yet to have Q(x), the expectation of Q(x, ξ), unbounded.
Proposition 2. If ξ has ﬁnite second moments, then
P(ω|Q(x,ξ) < ∞) = 1
implies Q(x) < ∞.


## Page 107

88
3. Basic Properties and Theory
To illustrate why this might be true, consider particular x and ξ values.
The second-stage program is the linear program
Q(x,ξ) = min{q(ω)T y|Wy = h(ω) −T(ω)x, y ≥0}.
Solving this linear program for given x and ξ amounts to ﬁnding some
square submatrix B of W, called a basis (see Section 2.9), such that yB =
B−1(h(ω) −T(ω)x), yN = 0, and qB(ω)T B−1W ≤q(ω)T , where yB is the
subvector associated with the columns of B and yN includes the remaining
components of y.
It follows that
Q(x,ξ) = qB(ω)T B−1(h(ω) −T(ω)x).
Now, assume Q(x,ξ) is bounded above with probability one and imagine
for a while that the same basis B would be optimal for all x and all ξ.
Then, ξ having ﬁnite second moments is a suﬃcient condition for Q(x) to
be bounded because it implies Eξ(qT
BB−1h) and Eξ(qT
BB−1T · x) are both
bounded above. In general the optimal basis B is diﬀerent for diﬀerent x and
ξ values so that a more general proof taking care of diﬀerent submatrices
of W is needed. This is done in detail in Walkup and Wets [1967].
In the next two theorems, we use the deﬁnition of pos W = {t|Wy =
t, y ≥0} as the positive hull of W. We observe that pos W is a closed set.
Theorem 3. For a stochastic program with ﬁxed recourse where ξ has
ﬁnite second moments, the sets K2 and KP
2 coincide.
Proof:
(Note: This proof uses some concepts from measure theory.) First
consider x ∈KP
2 . This implies Q(x,ξ) < ∞with probability one, so that,
by the proposition, Q(x) is bounded above and x ∈K2.
Now, consider x ∈K2 . It follows that {ξ|Q(x,ξ) < ∞} is a set of measure
one. Observe that Q(x, ξ) < ∞is equivalent to h(ω)−T(ω)x ∈pos W and
that h(ω) −T(ω)x is a linear function of ξ, and {ξ ∈	 |Q(x,ξ) < ∞}
is a closed subset of 	 of measure one, for any set 	 of measure one. In
particular, {ξ ∈Ξ|Q(x,ξ) < ∞} is a closed subset of Ξ having measure one.
By deﬁnition of Ξ, this set can only be Ξ itself, so that {ξ|Q(x, ξ) < ∞} ⊆Ξ
and therefore x ∈KP
2 .
Note however that W being ﬁxed and ξ having ﬁnite moments are just
suﬃcient conditions for K2 and KP
2 to coincide. Other, more general, suf-
ﬁcient conditions can be found in Walkup and Wets [1967].
Note also that a third deﬁnition of the second-stage feasibility set could
be given as {x|Q(x,ξ) < ∞with probability one}. For problems with ﬁxed
recourse where ξ has ﬁnite second moments, this set also coincides with K2
and KP
2 . In the sequel, we simply speak of K2, the second-stage feasibility
set.
Theorem 4. When W is ﬁxed and ξ has ﬁnite second moments:


## Page 108

3.1 Two-Stage Stochastic Linear Programs with Fixed Recourse
89
(a) K2 is closed and convex.
(b) If T is ﬁxed, K2 is polyhedral.
(c) Let ΞT be the support of the distribution of T. If h(ξ) and T(ξ)
are independent and ΞT is polyhedral, then K2 is polyhedral.
Proof:
The proof of (a) is elementary under the possibility representation
of K2. If T is ﬁxed, x ∈K2 if and only if h(ξ)−Tx ∈pos W for all ξ ∈Ξh,
where Ξh is the support of the distribution of h(ξ).
Consider some x and ξ s.t. h(ξ) −Tx̸ ∈pos W. Then there must exist
some hyperplane, say {x|σT x = 0} that separates h(ξ) −Tx from pos
W. This hyperplane must satisfy σT t ≤0 for t ∈pos W and σT (h(ξ) −
Tx) > 0. Because W is ﬁxed, there can only be ﬁnitely many diﬀerent
such hyperplanes, so that h(ξ) −Tx ∈pos W is equivalent to W ∗(h(ξ) −
Tx) ≤0 for some matrix W ∗. This matrix, called the polar matrix of W,
is obtained by choosing some minimal set of separating hyperplanes. The
set is minimal if removing any hyperplane would no longer guarantee the
equivalence between h(ξ) −Tx ∈pos W and W ∗(h(ξ) −Tx) ≤0 for all x
and ξ in Ξh. It follows that x ∈K2 if and only if W ∗(h(ξ) −Tx) ≤0 for
all ξ in Ξ. This can still be an inﬁnite system of linear inequalities due to
h(ξ). We may, however, replace this system by
(W ∗T)i·x ≥u∗
i =
sup
h(ξ)∈Ξh
W ∗
i·h(ξ), i = 1, . . . , l,
(1.7)
where W ∗
i· is the ith row of W ∗and l is the ﬁnite number of rows of W ∗.
If for some i, u∗
i is unbounded, then the problem is infeasible and the
result in (b) is trivially satisﬁed. If, for all i, u∗
i < ∞, then the system
(1.7) constitutes a ﬁnite system of linear inequalities deﬁning the polyhe-
dron K2 = {x|W ∗Tx ≥u∗} where u∗is the vector whose ith component
is u∗
i . This proves (b). When T is stochastic, a relation similar to (1.7)
holds, which, unless ΞT is ﬁnite, deﬁnes an inﬁnite system of inequalities.
Whenever ΞT is polyhedral, (c) can be proved by working on the extremal
elements of ΞT . This is done in Wets [1974, Corollary 4.13].
c. Second-stage value function
We ﬁrst start by properties of Q(x, ξ), assuming it is not −∞.
Theorem 5. For a stochastic program with ﬁxed recourse, Q(x, ξ) is
(a) a piecewise linear convex function in (h, T);
(b) a piecewise linear concave function in q;
(c) a piecewise linear convex function in x for all x in K = K1∩K2.


## Page 109

90
3. Basic Properties and Theory
Proof: To prove convexity in (a) and (c), we just need to prove that f(b) =
min{qT y|Wy = b} is a convex function in b. We consider two diﬀerent
vectors, say b1 and b2, and some convex combination bλ = λb1 + (1 −
λ)b2,
λ ∈(0, 1).
Let y∗
1 and y∗
2 be some optimal solution of min{qT y|Wy = b} for b = b1
and b = b2, respectively. Then, λy∗
1 + (1 −λ)y∗
2 is a feasible solution of
min{qT y|Wy = bλ}. Now, let y∗
λ be an optimal solution of this last problem.
We thus have
f(bλ) = qT y∗
λ ≤qT (λy∗
1 + (1 −λ)y∗
2)
= λqT y∗
1 + (1 −λ)qT y∗
2 = λf(b1) + (1 −λ)f(b2),
which proves the required proposition. A similar proof can be given to
show concavity in q. Piecewise linearity follows from the existence of ﬁnitely
many diﬀerent optimal bases for the second-stage program. A detailed proof
is given in Walkup and Wets [1969]. This fact will be illustrated and used
in the L-shaped algorithm of Section 5.1.
Another property is evident from parametric solutions of linear programs
when q and T are ﬁxed. Notice that
Q(x, q, λ(h′) + Tx, T) = λQ(x, q, h′ + Tx, T)
(1.8)
for any λ ≥0 because a dual optimal solution for h = h′ + Tx is also
dual feasible for h = λ(h′) + Tx and complementary with y∗optimal for
h = h′ +Tx. Because λy∗is also feasible for h = λ(h′)+Tx, λy∗is optimal
for h = λ(h′)+Tx, demonstrating (1.8). This says that Q(x, q, h′+Tx, T) is
a positively homogeneous function of h′. From the convexity of Q(x, q, h′ +
Tx, T) in h = h′ + Tx, this function is also sublinear (see Theorem 4.7
of Rockafellar [1969]) in h′. This property is central to some bounding
procedures described in Chapter 9.
Complete descriptions of Q(x, ξ) are also often useful. Finding the dis-
tribution induced on Q(x, ξ) is often the goal of these descriptions. This
information can then be used to ﬁnd Q or to address other risk criteria that
may not be given by the expectation functional (e.g., the probability of los-
ing some percentage of one’s wealth). The description of the distribution of
Q(x, ξ) is called the distribution problem. Its solution is quite diﬃcult al-
though some methods exist (see Wets [1980b] and Bereanu [1980]). Approx-
imations are generally required as in Dempster and Papagaki-Papoulias
[1980]; because these results are not central to our solution development,
we will not go into further detail. We concentrate on properties of the
expectation functional Q(x) as follows.
Theorem 6. For a stochastic program with ﬁxed recourse where ξ has
ﬁnite second moments,
(a) Q(x) is a Lipschitzian convex function and is ﬁnite on K2.


## Page 110

3.1 Two-Stage Stochastic Linear Programs with Fixed Recourse
91
(b) When ξ is ﬁnite, Q(x) is piecewise linear.
(c) If F(ξ) is an absolutely continuous distribution, Q(x) is diﬀer-
entiable on K2.
Proof:
Convexity and ﬁniteness in (a) are immediate. Part (b) follows
directly. A proof of the Lipschitz condition can be found in Wets [1972] or
Kall [1976], who also give conditions for Q(x) to be diﬀerentiable.
Although many of the proofs of these results become intricate in general,
the outcomes are relatively easy to apply.
When the random variables are appropriately described by a ﬁnite dis-
tribution, the constraint set K2 is best deﬁned by the possibility inter-
pretation and is easily seen to be polyhedral. The second-stage recourse
function Q(x) is piecewise linear and convex on K2. The decomposition
techniques of Chapter 5 then apply. This is a category of programs for
which computational methods can be made eﬃcient, as we shall see.
When the random variables cannot be described by a ﬁnite distribu-
tion, they can usually be associated with some probability density. Many
common probability densities are absolutely continuous and have ﬁnite
second moment, so the constraints set deﬁnitions K2 and KP
2 coincide and
the second-stage value function Q(x) is diﬀerentiable and convex. Clas-
sical nonlinear programming techniques could then be applied. A typical
example was given in the farmer’s problem in Chapter 1. There, a convex
diﬀerentiable function Q(x) was constructed analytically. It is easily under-
stood that analytical expressions can reasonably be found only for small
second-stage problems or problems with a very speciﬁc structure such as
separability.
In general, one can only compute Q(x) by numerical integration of
Q(x, ξ), for a given value of x. Most nonlinear techniques would also require
the gradients of Q(x), which in turn require numerical integration. An in-
troduction to numerical integration appears in Chapter 9. From there, we
come to the conclusion that numerical integration, as of today, produces an
eﬀective computational method only when the random vector is of small
dimensionality. As a consequence, the practical solution of stochastic pro-
grams having continuous random variables is, in general, a diﬃcult problem.
One line of approach is to approximate the random variable by a discrete
one and let the discretization be ﬁner and ﬁner, hoping that the solutions
of the successive problems with discrete random variables will converge to
the optimal solution of the problem with a continuous random variable.
This is also discussed in Chapter 9. It is suﬃcient at this point to observe
that approximation is a second reason for constructing eﬃcient methods
for stochastic programs with ﬁnite random variables.


## Page 111

92
3. Basic Properties and Theory
d. Special cases: relatively complete, complete, and simple
recourse
The previous sections presented properties for general problems. In par-
ticular instances, the feasible regions and objective values have special
properties that are particularly useful in computation. One advantage can
be obtained if every solution x that satisﬁes the ﬁrst-period constraints,
Ax = b, also has a feasible completion in the second stage. In other words,
K1 ⊂K2. In this case, we say that the stochastic program has relatively
complete recourse. If, for the example with stochastic W in Section 1.b,
we had the ﬁrst-period constraints x ≤1, then this problem would have
relatively complete recourse.
Although relatively complete recourse is very useful in practice and in
many of the theoretical results that follow, it may be diﬃcult to identify
because it requires some knowledge of the sets K1 and K2. A special type
of relatively complete recourse may, however, often be identiﬁed from the
structure of the W. This form, called complete recourse, holds when there
exists y ≥0 such that Wy = t for all t ∈ℜm2.
Complete recourse is also represented by pos W = ℜm2 (the positive cone
spanned by the columns of W includes ℜm2), and says that W contains a
positive linear basis of ℜm2. Complete recourse is often added to a model to
ensure that no outcome can produce infeasible results. With most practical
problems, this should be the case. In some instances, complete recourse
may not be apparent. An algorithm in Wets and Witzgall [1967] can be
used in this situation to determine whether W contains a positive linear
basis.
A special type of complete recourse oﬀers additional computational ad-
vantages to stochastic programming solutions. This case is the generaliza-
tion of the news vendor problem introduced in Section 1.1. It is called
simple recourse. For a simple recourse problem, W = [I, −I], y is divided
correspondingly as (y+, y−), and q = (q+, q−). Note that, in this case,
the optimal values of y+
i (ω), y−
i (ω) are determined purely by the sign of
hi(ω) −Ti·(ω)x provided that q+
i + q−
i
≥0 with probability one. This
ﬁniteness result is in the following theorem.
Theorem 7. Suppose the two-stage stochastic program in (1.1) is feasible
and has simple recourse and that ξ has ﬁnite second moments. Then Q(x)
is ﬁnite if and only if q+
i + q−
i ≥0 with probability one.
Proof:
If q+
i (ω) + q−
i (ω) < 0 for ω ∈Ω1 where P(Ω1) > 0, then, for
any feasible x in (1.1), for all ω ∈Ω1 where hi(ω) −Ti·(ω)x > 0, let
y+
i (ω) = hi(ω)−Ti·(ω)x+u, y−
i (ω) = u. By letting u →∞, Q(x, ω) →−∞.
A similar argument applies if hi(ω) −Ti·(ω)x ≤0, so Q(x) is not ﬁnite.
If q+
i +q−
i ≥0 with probability one, then Q(x, ω) = 	m2
i=1(q+
i (ω)(hi(ω)−
Ti·(ω)x)+ + q−
i (ω)(−hi(ω) + Ti·(ω)x)+), which is ﬁnite for all ω. Using
Proposition 2, we obtain the result.


## Page 112

3.1 Two-Stage Stochastic Linear Programs with Fixed Recourse
93
We, therefore, assume that q+
i + q−
i ≥0 with probability one and can
write Q(x) as 	m2
i=1 Qi(x), where Qi(x) = Eω[Qi(x, ξ(ω))], and Qi(x, ξ(ω))
= q+
i (ω)(hi(ω) −Ti·(ω)x)+ + q−
i (ω)(−h(ω) + Ti·(ω)x))+. When q and T
are ﬁxed, this characterization of Q allows its expression as a separable
function in the remaining random components hi. Often, in this case, Ti·x
is substituted with χi and Ψ is substituted for Q so that Q(x) = Ψ(χ).
We then obtain Ψ(χ) = 	m2
i=1 Ψi(χi) where Ψi(χ) = Ehi[ψi(χi, hi)] and
ψi(χi, hi) = q+
i (hi −χi)+ + q−
i (−hi + χi)+. We, however, continue to use
Q(x) to maintain consistency with our previous results.
We can deﬁne the objective function even further. In this case, let hi have
an associated distribution function Fi, mean value ¯hi, and let qi = q+
i +q−
i .
We can then write Qi(x) as
Qi(x) = q+
i ¯hi −(q+
i −qiFi(Ti·x))Ti·x −qi

hi≤Ti·x
hidFi(hi).
(1.9)
Of particular importance in optimization is the subdiﬀerential of this func-
tion, which has the following simple form:
∂Qi(x) = {π(Ti·)T | −q+
i + qiFi(Ti·x) ≤π ≤−q+
i + qiF +
i (Ti·x)},
(1.10)
where F +
i (h) = limt↓h Fi(t). These results can be used to obtain speciﬁc
optimality conditions. These general conditions are the subject of the next
part of this section.
e. Optimality conditions
In this subsection, we consider optimality conditions for stochastic pro-
grams. Our goal in describing these conditions is to show the special con-
ditions that can apply to stochastic programs and to show how stochastic
programs may diﬀer from other mathematical programs. In particular, we
give the additional assumptions that guarantee necessary and suﬃcient
conditions for two-stage stochastic linear programs. The following sections
contain generalizations.
The deterministic equivalent problem in (1.2) provides the framework for
optimality conditions, but several questions arise.
1. When is a solution to (1.2) attainable?
2. What form do the optimality conditions take and how can they be
simpliﬁed?
3. How stable is an optimal solution to (1.2) to changes in the parame-
ters and distributions?
4. What types of dual problems can be formulated to accompany (1.2)
and do they obtain bounds on optimal values?


## Page 113

94
3. Basic Properties and Theory
This subsection brieﬂy describes answers to these questions. Further details
are contained in Kall [1976], Wets [1974, 1990], and Dempster [1980]. Our
aim is to give only the basic results that may be useful in formulating,
solving, and analyzing practical stochastic programs.
From the previous section, supposing that ξ has ﬁnite second moments,
we know that Q is Lipschitzian. We can then apply a direct subgradient
result. A question is, however, whether the solution of (1.2) can indeed be
obtained, i.e., whether the optimal objective value is ﬁnite and attained by
some value of x.
To see that this question is indeed relevant, consider the following exam-
ple. Find
inf{Eξ[y+(ξ)]|y+(ξ), y−(ξ) ≥0, x + y+(ξ) −y−(ξ) = ξ, a.s.},
(1.11)
where ξ is, for example, negative exponentially distributed on [0, ∞). For
any ﬁnite value of x, (1.11) has a positive value, but the inﬁmum is zero.
The following theorem gives some suﬃcient conditions to guarantee that
a solution to (1.2) exists. In the following, we use rc to denote the recession
cone, {v|u + λv ∈S, for all λ ≥0 and u ∈S} when applied to a set, S, and
the recession value, supx∈domf(f(x + v) −f(x)) when applied to a proper
convex function, f.
Theorem 8. Suppose that the random elements ξ have ﬁnite second mo-
ments and one of the following:
(a) the feasible region K is bounded; or
(b) the recourse function Q is eventually linear in all recession di-
rections of K, i.e., Q(x + λv) = Q(x + ¯λv) + (λ −¯λ)rcQ(v) for
some ¯λ ≥0 (dependent on x), all λ ≥¯λ, and some constant
recession value, rcQ(v), for all v such that x + λv ∈K for all
x ∈K and λ ≥0.
Then, if problem (1.2) has a ﬁnite optimal value, it is attained for some
x ∈ℜn.
Proof: The proof given (a) follows immediately by noting that the objective
is convex and ﬁnite on K, which is by the assumption compact. The only
possibility for not attaining an optimum is, therefore, when the optimal
value is only attained asymptotically. By (b), along any recession direction
v, we must have rcQ(v) ≥0 for a ﬁnite value of Q(x + λv). Hence, the
optimal value must be attained.
As shown in Wets [1974], if T is ﬁxed and Ξ is compact, the condition
in (b) is obtained. In the exercises, we will show that (b) may not hold if
either of these conditions is relaxed.


## Page 114

3.1 Two-Stage Stochastic Linear Programs with Fixed Recourse
95
We now assume that an optimal solution can be attained as we would
expect in most practical situations. For optimization, we would like to de-
scribe the characteristics of such points. The general deterministic equiv-
alent form gives us the following result in terms of Karush-Kuhn-Tucker
conditions.
Theorem 9. Suppose (1.2) has a ﬁnite optimal value. A solution x∗∈K1,
is optimal in (1.2) if and only if there exists some λ∗∈ℜm1, µ∗∈ℜn1
+ ,
µ∗T x∗= 0, such that,
−c + AT λ∗+ µ∗∈∂Q(x∗).
(1.12)
Proof:
From the optimization of a convex function over a convex region
(see, for example, Bazaraa and Shetty [1979, Theorem 3.4.3]), we have
that cT x + Q(x) has a subgradient η at x∗such that ηT (x −x∗) ≥0 for
all x ∈K1 if and only if x∗minimizes cT x + Q(x) over K1. We can write
the set, {η|ηT (x −x∗) ≥0 for all x ∈K1}, as {η|η = AT λ + µ, for some
µ ≥0, µT x∗= 0}. Hence, the general optimality condition states that a
nonempty intersection of {η|η = AT λ + µ, for some µ ≥0, µT x∗= 0} and
∂(cT x∗+Q(x∗)) = c+∂Q(x∗) is necessary and suﬃcient for the optimality
of x∗.
This result can be combined with our previous results on simple recourse
functions to obtain speciﬁc conditions for that problem as in the following.
Corollary 10. Suppose (1.1) has simple recourse and a ﬁnite optimal
value. Then x∗∈K1 is optimal in (1.2) corresponding to this problem
if and only if there exists some λ∗∈ℜm1, µ∗∈ℜn1
+ , µ∗T x∗= 0, π∗
i such
that −(q+
i −qiFi(Ti·x∗)) ≤π∗
i ≤−(q+
i −qiF +
i (Ti·x∗)) and
−c + AT λ∗+ µ∗−(π∗)T T = 0.
(1.13)
Proof:
This is a direct application of (1.10) and Theorem 9.
Inclusion (1.12) suggests that a subgradient method or other nondiﬀer-
entiable optimization procedure may be used to solve (1.2). While this is
true, we note that ﬁnite realizations of the random vector lead to equiva-
lent linear programs (although of large scale), while absolutely continuous
distributions lead to a diﬀerentiable recourse function Q.
Obviously if Q is diﬀerentiable, we can replace ∂Q(x∗) with ∇Q(x∗) to
obtain:
c + ∇Q(x∗) = AT λ∗+ µ∗
(1.14)
in place of (1.12). Possible algorithms based on convex minimization sub-
ject to linear constraints are then admissible as in MINOS (Murtagh and
Saunders [1983]).


## Page 115

96
3. Basic Properties and Theory
The main practical possibilities for solutions of (1.2) then appear as
examples of either large-scale linear programming or smooth nonlinear op-
timization. The main diﬃculty is, however, in characterizing ∂Q because
even evaluating this function is diﬃcult. This evaluation is, however, de-
composable into subgradients of the recourse for each realization of ξ.
Theorem 11. If x ∈K, then
∂Q(x) = Eω∂Q(x, ξ(ω)) + N(K2, x),
(1.15)
where N(K2, x) = {v|vT y ≤0, ∀y such that x + y ∈K2}, the normal cone
to K2 at x.
Proof: From the theory of subdiﬀerentials of random convex functions with
ﬁnite expectations (see, for example, Wets [1990, Proposition 2.11]),
∂Q(x) = Eω∂Q(x, ξ(ω)) + rc[∂Q(x)],
(1.16)
where again rc denotes the recession cone, {v|u+λv ∈∂Q(x), for all λ ≥0
and u ∈∂Q(x)}. This set is equivalently {v|yT (u + λv) + Q(x) ≤Q(x + y)
for all λ ≥0 and y}. Hence, v ∈rc[∂Q(x)] if and only if yT v ≤0 for
all y such that Q(x + y) < ∞. Because K2 = {x|Q(x) < ∞}, the result
follows.
This theorem indeed provides the basis for the results on the diﬀeren-
tiability of Q. In the exercises, we illustrate more of the characteristics of
optimal solutions. Also note that if the problem has relatively complete re-
course, then, for any y such that x+y ∈K1, we must also have x+y ∈K2.
Hence, N(K2, x) ⊂N(K1, x) = {v|v = AT λ + µ, µT x = 0, µ ≥0}. This
yields the following corollary to Theorems 9 and 11.
Corollary 12. If (1.2) has relatively complete recourse, a solution x∗is
optimal in (1.2) if and only if there exists some λ∗∈ℜm1, µ∗∈ℜn1
+ ,
µ∗T x∗= 0, such that
−c + AT λ∗+ µ∗∈Eω∂Q(x, ξ(ω)).
(1.17)
f. Stability and nonanticipativity
Another practical concern is whether the optimal solution set is also sta-
ble, i.e., whether it changes continuously in some sense when parameters of
the problem change continuously. Although this may be of concern when
considering changing problem conditions, we do not develop this theory
in detail. The main results are that stability is achieved (i.e., some opti-
mal solution of an original problem is close to some optimal solution of
a perturbed problem) if problem (1.2) has complete recourse and the set
of recourse problem dual solutions, {π|πT W ≤q(ω)T }, is nonempty with


## Page 116

3.1 Two-Stage Stochastic Linear Programs with Fixed Recourse
97
probability one. For further details, we refer to Robinson and Wets [1987]
and R¨omisch and Schultz [1991b].
Another approach to optimality conditions is to consider problem (1.2),
in which y(ω) again becomes an explicit part of the problem and the nonan-
ticipativity constraints also become explicit. The advantage in this repre-
sentation is that we may obtain information on the value of future infor-
mation. It also leads naturally to algorithms based on relaxing nonantici-
pativity.
We discuss the main results in this characterization brieﬂy. The follow-
ing development assumes some knowledge of measure theory and can be
skipped by those unfamiliar with these concepts.
In general, for this approach, we wish to have a diﬀerent x, y pair for
every realization of the random outcomes. We then wish to restrict the x
decisions to be the same for almost all outcomes. This says that the deci-
sion, (x(ω), y(ω)), is a function (with suitable properties) on Ω. We restrict
this to some space, X, of measurable functions on Ω, for example, the p-
integrable functions, Lp(Ω, B, µ; ℜn), for some 1 ≤p ≤∞. (For background
on these concepts, see, for example, Royden [1968].) The general version of
(1.2) (with certain restrictions) then becomes:
inf
(x(ω),y(ω))∈X

Ω
(cT x(ω) + q(ω)T y(ω))µ(dω)
s. t. Ax(ω)= b, a.s.,
EΩ(x(ω)) −x(ω)= 0, a.s.,
T(ω)x(ω) + Wy(ω)= h(ω), a.s.,
x(ω), y(ω)≥0, a.s.
(1.18)
Problem (1.18) is equivalent to (1.2) if, for example, X is the space of
essentially bounded functions on Ωand K is bounded for (1.2). The two
formulations are not necessarily the same, however, as in the problem given
in Exercise 10.
The condition that the x decision is taken before realizing the random
outcomes is reﬂected in the second set of constraints in (1.18). These con-
straints are called nonanticipativity constraints. They imply that almost all
x(ω) values are the same.
The only diﬀerence in optimality conditions from (1.12) is that we include
explicit multipliers for the nonanticipativity constraints. For continuous
distributions, these multipliers may, however, have a diﬃcult representation
unless (1.18) has relatively complete recourse. The diﬃculty is that we
cannot guarantee boundedness of the multipliers and may not be able to
obtain an integrable function to represent them. This diﬃculty is caused
when future constraints restrict the set of feasible solutions at the ﬁrst
stage.
For ﬁnite distributions, (1.18) is, however, an implementable problem
structure that is used in several algorithms discussed here. In this case,
with K possible realizations of ξ with probabilities pk, k = 1, . . . , K, the


## Page 117

98
3. Basic Properties and Theory
problem becomes:
inf
(xk,yk),k=1,...,K
K

k=1
pk(cT xk + (qk)T yk)
s. t. Axk= b, k = 1, . . . , K,
(

j̸=k
pjxj) + (pk −1)xk= 0, k = 1, . . . , K,
T kxk + Wyk= hk, k = 1, . . . , K,
xk, yk≥0, k = 1, . . . , K.
(1.19)
Notice that (1.19) almost completely decomposes into K separate problems
for the K realizations. The only links are in the second set of constraints
that impose nonanticipativity. An aim of computation is to take advantage
of this structure.
Consider the optimality conditions for (1.19). We wish to illustrate the
diﬃculties that may occur when continuous distributions are allowed. A
solution (xk∗, yk∗), k = 1, . . . , K, is optimal for (1.19) if and only if there
exist (λk∗, ρk∗, πk∗) such that
pk(cj −λk∗T a·j −

l̸=k
plρl∗
j −(−1 + pk)ρk∗
j −π∗T T k
·j) ≥0, k = 1, . . . , K,
j = 1, . . . , n1,
(1.20)
(cj −λk∗T a·j −

l̸=k
pkρk∗
j pk −(−1 + pk)ρk∗
j −π∗T T k
·j)xk∗
j
= 0, k = 1, . . . , K,
j = 1, . . . , n1,
(1.21)
pk(qk
j −π∗T W·j) ≥0, k = 1, . . . , K, j = 1, . . . , n2,
(1.22)
pk(qk
j −π∗T W·j)yk∗
j
= 0, k = 1, . . . , K, j = 1, . . . , n2,
(1.23)
where we have eﬀectively multiplied the constraints in (1.19) by pk to obtain
the form in (1.20)–(1.23). We may also add the condition,

k=1,...,K
pkρk∗= 0,
(1.24)
without changing the feasibility of (1.20)–(1.23). This is true because, if
	
k=1,...,K pkρk∗= κ for some κ̸ = 0 is part of a feasible solution to (1.20)–
(1.23), then so is ρk′ = ρk∗−κ. A problem arises if more realizations are
included in the formulation (i.e., K increases) and ρk′ becomes unbounded.
For example, consider the following example (see also Rockafellar and
Wets [1976a]). We wish to ﬁnd minx{x|x ≥0, x −y = ξ, a.s., y ≥0},
where ξ is uniformly distributed on k/K for k = 0, . . . , K −1. In this case,


## Page 118

3.1 Two-Stage Stochastic Linear Programs with Fixed Recourse
99
the optimal solution is x∗=
K−1
K
and yk∗=
K−1−k
K
for k = 0, . . . , K.
The multipliers satisfying (1.20)–(1.24) are ρk∗= 1, πk∗= 0 for k =
0, . . . , K −2, and ρK−1∗= −(K −1) and πK−1∗= K + 2. Note that as K
increases, ρ∗approaches a distribution with a singular value at one. The
diﬃculty is that ρK−1∗is unbounded so that bounded convergence cannot
apply. If relatively complete recourse is assumed, however, then all elements
of ρ∗are bounded (see Exercise 11). No singular values are necessary.
In this example, the continuous distribution would tend toward a singular
multiplier for some value of ω (i.e., a multiplier with mass one at a single
point). If this is the case, we must have that the solution to the dual of
the recourse problem is unbounded, or the recourse problem is infeasible
for x∗feasible in the ﬁrst stage. This possibility is eliminated by imposing
the relatively complete recourse assumption.
With relatively complete recourse, we can state the following optimality
conditions for a solution (x∗(ω), y∗(ω)) to (1.19). The theorem appears in
other ways in Hiriart-Urruty [1978], Rockafellar and Wets [1976a, 1976b],
Birge and Qi [1993], and elsewhere. We only note that regularity conditions
(other than relatively complete recourse) follow from the linearity of the
constraints.
Theorem 13. Assuming that (1.18) with X = L∞(Ω, B, µ; ℜn1+n2) is
feasible, has a bounded optimal value, and satisﬁes relatively complete re-
course, a solution (x∗(ω), y∗(ω)) is optimal in (1.18) if and only if there
exist integrable functions on Ω, (λ∗(ω), ρ∗(ω), π∗(ω)), such that
cj −λ∗(ω)A·j −ρ∗(ω) −π∗T (ω)T·j(ω) ≥0, a.s., j = 1, . . . , n1,
(1.25)
(cj−λ∗(ω)A·j−ρ∗(ω)−π∗T (ω)T·j(ω))x∗
j(ω) = 0, a.s., j = 1, . . . , n1, (1.26)
qj(ω) −π∗T (ω)W·j ≥0, a.s., j = 1, . . . , n2,
(1.27)
(qj(ω) −π∗T (ω)W·j)y∗
j (ω) = 0, a.s., j = 1, . . . , n2,
(1.28)
and
Eω[ρ∗(ω)] = 0.
(1.29)
Proof:
We ﬁrst show the suﬃciency of these conditions directly. If (1.25)–
(1.29) are satisﬁed, then for any (x(ω), y(ω)) (with expected value (x, y))
such that (x∗(ω)+x(ω), y∗(ω)+y(ω)) is feasible in (1.18), then integrating
over ω, summing over j in (1.26), and using (1.27), we obtain that cT x −
Eω[π∗T (ω)T(ω)]x ≥0. We also have that q(ω)T y(ω) ≥π∗T (ω)Wy(ω) =
−π∗T (ω)T(ω)x. Hence, cT x + Eω[q(ω)T y(ω)] ≥0, giving the optimality of
(x∗(ω), y∗(ω)).
For necessity, we use the equivalence of (1.18) and (1.2), and Corollary 12.
In this case, let λ∗from (1.12) replace λ∗(ω) in (1.25). Let π∗(ω) be the op-
timal dual value in the recourse problem in (1.4). Thus, Eω[∂Q(x∗, ξ(ω))] =


## Page 119

100
3. Basic Properties and Theory
Eω[−π∗T (ω)T(ω)]. Now, if we let ρ∗(ω) = Eω[−π∗T (ω)T] −π∗T (ω)T(ω),
we obtain all the conditions in (1.25)–(1.29).
The results in this section give conditions that can be useful in algorithms
and in checking the optimality of stochastic programming solutions. Dual
problems can also be formulated based on these conditions either to obtain
bounds on optimal solutions by ﬁnding corresponding feasible dual solu-
tions or to give an alternative solution procedure that can be used directly
or in some combined primal-dual approach (see, for example, Bazaraa and
Shetty [1979]). The dual problem directly obtained from (1.25)–(1.29) is to
ﬁnd (λ(ω), ρ(ω), π(ω)) on the dual space to X to maximize
Eω[λT (ω)b + πT (ω)h(ω)] subject to
(1.30)
cj −λ(ω)A·j −ρ(ω) −πT (ω)T·j(ω) ≥0, a.s., j = 1, . . . , n1,
(1.31)
qj(ω) −πT (ω)W·j ≥0, a.s., j = 1, . . . , n2,
(1.32)
and
Eω[ρ(ω)] = 0.
(1.33)
This ﬁts the general duality framework used by Klein Haneveld [1985] where
further details on the properties of these dual problems may be found.
Rockafellar and Wets [1976a, 1976b] also discuss this alternative viewpoint
with an analysis based on perturbations of both primal and dual forms.
Discussion of alternative dual spaces appears in Eisner and Olsen [1975].
In general, Problem (1.18) attains its minimum with a bounded region, and
the supremum in (1.30)–(1.33) gives the same value. Relatively complete
recourse, or a similar requirement, is necessary to obtain that the dual
optimum is also attained. With unbounded regions or without relatively
complete recourse, as we have seen, we may have that an optimal solution
is not attained for either (1.19) or (1.30)–(1.33). In this case, it is possible
that the corresponding dual problem does not have the same optimal value
and the two problems exhibit a duality gap. The exercises explore this
possibility further.


## Page 120

3.1 Two-Stage Stochastic Linear Programs with Fixed Recourse
101
Exercises
1. Let a second-stage program be deﬁned as
min 2y1 + y2
s.t. y1 + 2y2 ≥ξ1 −x1,
y1 + y2 ≥ξ2 −x1 −x2,
0 ≤y1 ≤1, 0 ≤y2 ≤1.
(a) Find K2(ξ) for all ξ. (Hint: Use the bounds on y1 and y2 to
bound the left-hand side.)
(b) Let ξ1 and ξ2 be two independent continuous random variables.
Assume they both have uniform density over [2, 4].
i. What is KP
2 ?
ii. What is K2?
iii. Let u∗
i be deﬁned as in (1.7). What are u∗
1 and u∗
2 in this
example?
2. Let the second stage of a stochastic program be
min 2y1 + y2
s.t. y1 −y2 ≤2 −ξx1,
y2 ≤x2,
0 ≤y1, y2.
Find K2(ξ) and K2 for:
(a) ξ ∼U[0, 1].
(b) ξ ∼Poisson(λ), λ > 0.
What properties do you expect for K2?
3. Consider the following second-stage program:
Q(x, ξ) = min{y|y ≥ξ, y ≥x} .
For simplicity, assume x ≥0.
Let ξ have density
f(ξ) = 2
ξ3 , ξ ≥1.
Show that KP
2̸
=
K2. Compare this with the statement of
Theorem 3.


## Page 121

102
3. Basic Properties and Theory
4. Let a second-stage program be deﬁned as
min 2y1 + y2
s. t. y1 + y2 ≥1 −x1,
y1 ≥ξ −x1 −x2,
y1, y2 ≥0.
(a) Show that this program has complete recourse if ξ has ﬁnite
expectation.
(b) Assuming 0 ≤x1 ≤1, 0 ≤x2 ≤1, show that the following are
optimal second-stage solutions:
If ξ ≥x1 + x2 ⇒y∗
1 = ξ −x1 −x2 : y∗
2 = (1 −ξ + x2)+ where
(a)+ = max(a; 0).
If ξ ≤x1 + x2 ⇒y∗
1 = 0; y∗
2 = 1 −x1.
It follows that
Q(x, ξ) =



1 −x1
for 0 ≤ξ < x1 + x2,
ξ + 1 −2x1 −x2
for x1 + x2 ≤ξ ≤1 + x2,
2(ξ −x1 −x2)
for 1 + x2 ≤ξ.
Check that Q(x, ξ) has properties (a) and (c) in Theorem 5.
(c) Assume ξ ∼U[0, 2]. After a tedious integration that proba-
bly only the authors of this book will go through, one obtains
Q(x) = 1
4(x2
1 + 2x2
2 + 2x1x2 −8x1 −6x2 + 9). Check that the
relevant properties of Theorem 6 are satisﬁed.
5. Let a second-stage program be deﬁned as
min ξy1 + y2
s. t. y1 + y2 ≥1 −x1,
y1 ≥1 −x1 −x2,
y1, y2 ≥0 .
Assume 0 ≤x1, x2 ≤1. Obtain Q(x, ξ) and observe that it is concave
in ξ.
6. Prove the positive homogeneity property in (1.8).
7. Derive the simple recourse results in (1.9) and (1.10).
8. Show that the news vendor problem is a special case of a simple
recourse problem.


## Page 122

3.2 Probabilistic or Chance Constraints
103
9. Consider the following example:
min −x + E(t(ω),h(ω))[y+(ω) + y−(ω)]
s. t. t(ω)x + y+(ω) −y−(ω) = h(ω), a.s.,
x, y+(ω), y−(ω) ≥0, a.s.,
where h, t are uniformly distributed on the unit circle, h2 + t2 ≤1.
Find Q(x) and show that it is not eventually linear for x →∞(Wets
[1974]).
10. Suppose you wish to solve (1.11) in the form of (1.18) over
(x(ω), y(ω)) ∈L∞(Ω, B, µ : ℜn1+n2). What is the optimal value?
How does this diﬀer using (1.2)?
11. This exercise uses approximation results to give an alternative proof
of Theorem 13. As shown in Chapter 9, if a discrete distribution
approaches a continuous distribution (in distribution) and problem
(1.2) has a bounded optimal solution and the bounded second mo-
ment property, then a limiting optimal solution for the discrete distri-
butions is an optimal solution using the continuous distribution. This
also implies that recourse solutions, y∗, converge and that the opti-
mality conditions in (1.25)–(1.29) are obtained as long as the ρk∗in
the discrete approximations are uniformly bounded. Show that rela-
tively complete recourse implies uniform boundedness of some ρk∗for
any discrete approximation approaching a continuous distribution in
(1.18). (Hint: Construct a system of equations that must be violated
for some iteration ν of the discretization and for any bound M on
the largest value of ρk∗if the ρk∗are not uniformly bounded. Then
show that the complementary system implies no relatively complete
recourse.)
3.2
Probabilistic or Chance Constraints
As mentioned in Chapter 2, in some models, constraints need not hold
almost surely as we have assumed to this point. They can instead hold
with some probability or reliability level. These probabilistic, or chance,
constraints take the form:
P{Ai(ω)x ≥hi(ω)} ≥αi,
(2.1)
where 0 < αi < 1 and i = 1, . . . , I is an index of the constraints that
must hold jointly. We can, of course, model these constraints in a gen-
eral expectational form Eω(f i(ω, x(ω)) ≥αi where f i is an indicator of
{ω|Ai(ω)x ≥hi(ω)} but we would then have to deal with a discontinuous
function.


## Page 123

104
3. Basic Properties and Theory
In chance-constrained programming (see, e.g., Charnes and Cooper
[1963]), the objective is often an expectational functional as we used earlier
(the E-model), or it may be the variance of some result (theV-model) or
the probability of some occurrence (such as satisfying the constraints) (the
P-model). Another variation includes an objective that is a quantile of a
random function (see, e.g., Kibzun and Kurbakovskiy [1991] and Kibzun
and Kan [1996]).
The main results with probabilistic constraints refer to forms of deter-
ministic equivalents for constraints of the form in (2.1). Provided the de-
terministic equivalents of these constraints and objectives have the desired
convexity properties, these functions can be added to the recourse prob-
lems given earlier (or used as objectives). In this way, all our previous
results apply to chance-constrained programming with suitable function
characteristics.
The main goal in problems with probabilistic constraints is, therefore,
to determine deterministic equivalents and their properties. To maintain
consistency with the recourse problem results, we let
Ki
1(αi) = {x|P(Ai(ω)x ≥hi(ω)) ≥αi},
(2.2)
where 0 < αi ≤1 and ∩iKi
1(1) = K1 as in Section 1. Unfortunately,
Ki
1(αi) need not be convex or even connected. Suppose, for example that
Ω= {ω1, ω2}, P[ω1] = P[ω2] = 1
2,
Ai(ω1) = Ai(ω2)=

1
−1

hi(ω1)=

0
−1

hi(ω2)=

2
−3

.
(2.3)
For 0 < αi ≤1
2, Ki
1(αi) = [0, 1] ∪[2, 3].
When each i corresponds to a distinct linear constraint and Ai is a
ﬁxed row vector, then obtaining a deterministic equivalent of (2.2) is fairly
straightforward. In this case, P(Aix ≥hi(ω)) = F i(Aix), where F i is the
distribution function of hi. Hence, Ki
1(αi) = {x|F i(Aix) ≥αi}, which im-
mediately yields a deterministic equivalent form. In general, however, the
constraints must hold jointly so that the set I is a singleton. This situa-
tion corresponds to requiring an α-conﬁdence interval that x is feasible.
We assume this in the remainder of this section and drop the superscript i
indicating the set of joint constraints.
The results to determine the deterministic equivalent often involve ma-
nipulations of probability distributions that use measure theory. The re-
mainder of this section is intended for readers familiar with this area. One
of the main results in probabilistic constraints is that, in the joint con-
straint case, a large class of probability measures on h(ω) (for A ﬁxed)


## Page 124

3.2 Probabilistic or Chance Constraints
105
leads to convex and closed K1(α). A probability measure P is in this class
of quasi-concave measures if for any convex measurable sets U and V and
any 0 ≤λ ≤1,
P((1 −λ)U + λV ) ≥min{P(U), P(V )}.
(2.4)
The use of this and a special form, called logarithmically concave mea-
sures, began with Pr´ekopa [1971, 1973]. General discussions also appear
in Pr´ekopa [1980, 1995], Kallberg and Ziemba [1983] concerning related
utility functions, and the surveys of Wets [1983b, 1990] which include the
following theorem.
Theorem 14. Suppose A is ﬁxed and h has an associated quasi-concave
probability measure P. Then K1(α) is a closed convex set for 0 ≤α ≤1.
Proof:
Let H(x) = {h|Ax ≥h}. Suppose x(λ) = λx1 + (1 −λ)x2 where
x1, x2 ∈K1(α). Suppose h1 ∈H(x1) and h2 ∈H(x2). Then λh1 + (1 −
λ)h2 ≤Ax(λ), so H(x(λ)) ⊃λH(x1) + (1 −λ)H(x2). Hence, P({Ax(λ) ≥
h}) = P(H(x(λ)) ≥P(λH(x1)+(1−λ)H(x2)) ≥α. Thus, K1(α) is convex.
For closure, suppose that xν
→
¯x, where xν
∈K1(α). Consider
H(xν). If h ≤Axνi for some subsequence {νi} of {ν}, then h ≤
A¯x. Hence lim supν H(xν) ⊂H(¯x), so P(H(¯x)) ≥P(lim supν H(xν))
≥lim supν P(H(xν)) ≥α.
The relevance of this result stems from the large class of probability mea-
sures which ﬁt these conditions. Some extent of this class is given in the
following result of Borell [1975], which we state without proof.
Theorem 15. If f is the density of a continuous probability distribution
in ℜm and f −( 1
m ) is convex on ℜm, then the probability measure
P(B) =

B
f(x)dx,
deﬁned for all Borel sets B in ℜm is quasi-concave.
In particular, this result states that any density of the form f(x) = e−l(x)
for some convex function l yields a quasi-concave probability measure.
These measures include the multivariate normal, beta, and Dirichlet dis-
tributions and are logarithmically concave (because, for 0 ≤λ ≤1,
P((1−λ)U +λV ) ≥P(U)λP(V )1−λ for all Borel sets U and V ) as studied
by Pr´ekopa. These distributions lead to computable deterministic equiva-
lents as, for example, in the following theorem.
Theorem 16. Suppose A is ﬁxed and the components hi, i = 1, . . . , m1, of
h are stochastically independent random variables with logarithmically con-
cave probability measures, Pi, and distribution functions, Fi, then K1(α) =
{x| 	m1
i=1 ln(Fi(Ai·x)) ≥lnα} and is convex.


## Page 125

106
3. Basic Properties and Theory
Proof:
From the independence assumption, P[Ax ≥h] = Πm1
i=1Pi[Ai·x ≥
hi] = Πm1
i=1Fi(Ai·x). So, K1(α) = {x|Πm1
i=1Fi(Ai·x) ≥α}. Taking loga-
rithms (which is a monotonically increasing function), we obtain K1(α) =
{x| 	m1
i=1 ln(Fi(Ai·x)) ≥lnα}. Because
Fi(Ai·(λx1 + (1 −λ)x2)) = Pi(hi ≤Ai·(λx1 + (1 −λ)x2))
≥Pi(λ{hi ≤Ai·x1} + (1 −λ){hi ≤Ai·x2)})
≥(Pi({hi ≤Ai·x1})λ(Pi({hi ≤Ai·x2})1−λ
= (Fi(Ai·x1)λ)(Fi(Ai·x2)1−λ),
the logarithm of Fi(Ai·x) is a concave function, and K1(α) is convex.
Logarithmically concave distribution functions include the increasing
failure rate functions (see Miller and Wagner [1965] and Parikh [1968]) that
are common in reliability studies. Other types of quasi-concave measures
include the multivariate t and F distributions. Because these distributions
include those most commonly used in multivariate analysis, it appears that,
with continuous distributions and ﬁxed A, the convexity of the solution set
is generally assured.
When A is also random, the convexity of the solution set is, however, not
as clear. The following theorem from Pr´ekopa [1974], given without proof,
shows this result for normal distributions with ﬁxed covariance structure
across columns of A and h.
Theorem 17. If A1·, . . . , An1·, h have a joint normal distribution with a
common covariance structure, a matrix C, such that E[(Ai·−E(Ai·))(Aj·−
E(Aj·))T ] = rijC for i, j in 1, . . . , n1, and
E[(Ai· −E(Ai·))(h −E(h))] = siC
for i = 1, . . . , n1, where rij and si are constants for all i and j, then K1(α)
is convex for α ≥1
2.
Stronger results than Theorem 17 are diﬃcult to obtain. In general, one
must rely on approximations to the deterministic equivalent that maintain
convexity although the original solution set may not be convex. We will
consider some of these approximations in Chapter 9.
Some other speciﬁc examples where A may be random include single con-
straints (see Exercise 5). In the case of h ≡0 and normally distributed A,
the deterministic equivalent is again readily obtainable as in the following
from Parikh [1968].
Theorem 18. Suppose that m1 = 1, h1 = 0, and A1· has mean ¯A1· and
covariance matrix C1, then K1(α) = {x| ¯A1·x −Φ−1(α)

xT C1x ≥0},
where Φ is the standard normal distribution function.
Proof:
Observe that A1·x is normally distributed with mean, ¯A1·x, and
variance, xT C1x. If xT C1x = 0, then the result is immediate. If not, then


## Page 126

3.2 Probabilistic or Chance Constraints
107
A1·x−¯
A1·x
√
xT C1x
is a standard normal random variable with cumulative Φ, and
P(A1·x ≥0) = P(A1·x −¯A1·x

xT C1x
≥
−¯A1·x

xT C1x
)
= P(A1·x −¯A1·x

xT C1x
≤
¯A1·x

xT C1x
)
= Φ(
¯A1·x

xT C1x
).
Substitution in the deﬁnition of K1(α) yields the result.
Finally in this chapter, we would like to show some of the similarities
between models with probabilistic constraints and problems with recourse.
As stated in Chapter 2, models with probabilistic constraints and models
with recourse can often lead to the same optimal solutions. Some other
aspects of the modeling process may favor one over the other (see, e.g.,
Hogan, Morris, and Thompson [1981, 1984], Charnes and Cooper [1983]),
but, these diﬀerences generally just represent decision makers’ diﬀerent
attitudes toward risk.
We use an example from Parikh [1968] to relate simple recourse and
chance-constrained problems. Consider the following problem with proba-
bilistic constraints:
min cT x
s. t. Ax= b,
Pi[Ti·x ≥hi]≥αi, i = 1, . . . , m2,
x≥0,
(2.5)
where Pi is the probability measure of hi and Fi is the distribution function
for hi. For the deterministic equivalent to (2.5), we just let Fi(h∗
i ) = αi, to
obtain:
min cT x
s. t. Ax= b,
Ti·x≥h∗
i , i = 1, . . . , m2,
x≥0.
(2.6)
Suppose we solve (2.6) and obtain an optimal x∗and optimal dual solution
{λ∗, π∗}, where cT x∗= bT λ∗+ h∗T π∗. If π∗
i = 0, let q+
i = 0 and, if π∗
i > 0,
let q+
i =
π∗
i
1−αi . An equivalent stochastic program with simple recourse to
(2.5) is then:
min cT x+Eh[q+y+]
s. t. Ax= b,
Ti·x + y+
i −y−
i = hi, i = 1, . . . , m2,


## Page 127

108
3. Basic Properties and Theory
x, y+, y−≥0.
(2.7)
For problems (2.5) and (2.7) to be equivalent, we mean that any x∗opti-
mal in (2.5) corresponds to some (x∗, y∗+) optimal in (2.7) for a suitable
deﬁnition of q+ and that any (x∗, y∗+) optimal in (2.7) corresponds to x∗
optimal in (2.5) for a suitable deﬁnition of αi. We show the ﬁrst part of
this equivalence in the following theorem.
Theorem 19. For the q+
i deﬁned as a function of some optimal π∗for the
dual to (2.5), if x∗is optimal in (2.5), there exists y∗+ ≥0 a.s. such that
(x∗, y∗+) is optimal in (2.7).
Proof:
First, let x∗be optimal in (2.5). It must also be optimal in (2.6)
with dual variables, {λ∗, π∗}. We must have π∗≥0,
cT −λ∗T A −π∗T T≥0,
Tx∗−h∗≥0,
(cT −λ∗T A −π∗T T)x∗= 0, and
π∗T (Tx∗−h∗)= 0.
(2.8)
Now, for x∗to be optimal in (2.7), consider the optimality conditions (1.13)
from Corollary 10. These conditions state that if there exists λ∗such that
cT −λ∗T A −
m2

i=1
Ti·(q+
i −qiFi(Ti·x∗))≥0,
(cT −λ∗T A −
m2

i=1
Ti·(q+
i −qiFi(Ti·x∗))x∗= 0.
(2.9)
Substituting for π∗
i = q+
i (1 −αi) in (2.8) and noting from the complemen-
tarity condition that αi = Fi(h∗
i ) = Fi(Ti·x∗) if π∗
i > 0, we obtain
cT −λ∗T A −π∗T T= cT −λ∗T A −
m2

i=1
Ti·(q+
i (1 −Fi(Ti·x∗))
= cT −λ∗T A −
m2

i=1
Ti·(q+
i −qiFi(Ti·x∗))
(2.10)
from the deﬁnitions and noting that π∗
i > 0 if and only if q+
i > 0. From
(2.10), we can verify the conditions in (2.9) and obtain the optimality of
x∗in (2.7).
If we assume x∗is optimal in (2.7), we can reverse the argument to
show that x∗is also optimal in (2.5) for some value of αi. This result
(from Symonds [1968]) is Exercise 7. Further equivalences are discussed in
Gartska [1980]. We note that all of these equivalences are somewhat weak
because they require a priori knowledge of the optimal solution to one of
the problems (see also the discussion in Gartska and Wets [1974]).


## Page 128

3.3 Stochastic Integer Programs
109
Exercises
1. Suppose a single probabilistic constraint with ﬁxed A and that h
has an exponential distribution with mean λ. What is the resulting
deterministic equivalent constraint for K1(α)?
2. For the example in (2.3), what happens for 1
2 < αi ≤1 ?
3. Can you construct an example with continuous random variables
where K1(α) is not connected? (Hint: Try a multimodal distribu-
tion such as a random choice of one of two bivariate normal random
variables.)
4. Extend Theorem 14 to allow any set of convex constraints, gi(x, ξ(ω))
≤0, i = 1, . . . , m.
5. Suppose a single linear constraint in K1(α) where the components of
A and h have a joint normal distribution. Show that K1(α) is also
convex in this case for α ≥1
2. (Hint: The random variable, A1·x−h1,
is also normally distributed.)
6. Show that

xT C1x is a convex function of x.
7. Prove the converse of Theorem 19 by ﬁnding an appropriate αi so
that x∗optimal in (2.7) is also optimal in (2.5).
3.3
Stochastic Integer Programs
a. Recourse problems
The general formulation of a two-stage integer program resembles that of
the general linear case presented in Section 1. It simply requires that some
variables, in either the ﬁrst stage or the second stage, are integer. As we
have seen in the examples in Chapter 1, in many practical situations the
restrictions are, in fact, that the variables must be binary, i.e., they can
only take the value zero or one. Formally, we may write
min
x∈X z =cT x + Eξ min{q(ω)T y|Wy = h(ω) −T(ω)x, y ∈Y }
s.t. Ax = b,
where the deﬁnitions of c, b,ξ, A, W, T, and h are as before. However, X
and/or Y contains some integrality or binary restrictions on x and/or y.
With this deﬁnition, we may again deﬁne a deterministic equivalent pro-
gram of the form
min
x∈X z =cT x + Q(x)
s.t. Ax = b


## Page 129

110
3. Basic Properties and Theory
with Q(x) the expected value of the second stage deﬁned as in Section 1.2.
In this section, we are interested in the properties of Q(x) and K2 =
{x|Q(x) < ∞}. Clearly, if the only integrality restrictions are in X, the
properties of Q(x) and K2 are the same as in the continuous case. The main
interesting cases are those in which some integrality restrictions are present
in the second stage. The properties of Q(x, ξ) for given ξ are those of the
value function of an integer program in terms of its right-hand side. This
problem has received much attention in the ﬁeld of integer programming
(see, e.g., Blair and Jeroslow [1982] or Nemhauser and Wolsey [1988]). In
addition to being subadditive, the value function of an integer program can
be obtained by starting from a linear function and ﬁnitely often repeating
the operations of sums, maxima, and non-negative multiples of functions
already obtained and rounding up to the nearest integer. Functions so ob-
tained are known as Gomory functions (see again Blair and Jeroslow [1982]
or Nemhauser and Wolsey [1988]). Clearly, the maximum and rounding up
operations imply undesirable properties for Q(x, ξ), Q(x), and K2, as we
now illustrate.
Proposition 20. The expected recourse function Q(x) of an integer pro-
gram is in general nonconvex and discontinuous.
Example 1
We illustrate the proposition in the following simple example where the
ﬁrst stage contains a single decision variable x ≥0 and the second-stage
recourse function is deﬁned as:
Q(x,ξ) = min{2y1 + y2|y1 ≥x −ξ, y2 ≥ξ −x, y ≥0, integer}.
(3.1)
Assume ξ can take on the values one and two with equal probability 1/2.
Let ⌈a⌉denote the smallest integer greater than or equal to a (the round-
ing up operation) and ⌊a⌋the truncation or rounding down operation
(⌊a⌋= −⌈−a⌉). Consider ξ = 1. For x ≤1, the optimal second-stage
solution is y1 = 0, y2 = ⌈1 −x⌉. For x ≥1, it is y1 = ⌈x −1⌉, y2 = 0.
Hence, Q(x, 1) = max{2(⌈x −1⌉), ⌈1 −x⌉}, a typical Gomory function. It
is discontinuous at x = 1. Nonconvexity can be illustrated by Q(0.5, 1) >
0.5Q(0, 1)| + 0.5Q(1, 1). Similarly, Q(x, 2) = max{2(⌈x −2⌉), ⌈2 −x⌉}. The
three functions, Q(x, 1), Q(x, 2), and Q(x) are represented in Figure 1.
The recourse function, Q(x), is clearly discontinuous in all positive in-
tegers. Nonconvexity can be illustrated by Q(1.5) = 1.5 > 0.5Q(1) +
0.5Q(2) = .75. Thus Q(x) has none of the properties that one may wish for
to design an algorithmic procedure. Note, however, that a convexity-related
property exists in the case of simple integer recourse (Proposition 8.4) and
that it applies to this example.


## Page 130

3.3 Stochastic Integer Programs
111
FIGURE 1. Example of discontinuity.


## Page 131

112
3. Basic Properties and Theory
Continuity of the recourse function can be regained when the random vari-
able is absolutely continuous (Stougie [1987]).
Proposition 21. The expected recourse function Q(x) of an integer pro-
gram with an absolutely continuous random variable is continuous.
Note, however, that despite Proposition 21, the recourse function Q(x)
remains, in general, nonconvex.
Example 2
Consider Example 1 but with the (continuous) random variable deﬁned by
its cumulative distribution,
F(t) = P(ξ ≤t) = 2 −2/t, 1 ≤t ≤2.
Consider 1 < x < 2. For 1 ≤ξ < x, we have 0 < x −ξ < 1, hence
y1 = 1, y2 = 0, while for x < ξ ≤2, we have 0 < ξ −x ≤1, hence
y1 = 0, y2 = 1.
It follows that
Q(x) =
 x
1
2dF(t) +
 2
x
1dF(t) = 2F(x) + 1 −F(x)
= F(x) + 1 = 3 −2/x,
which is easily seen to be nonconvex.
Properties are just as poor in terms of feasibility sets. As in the continu-
ous case, we may deﬁne the second-stage feasibility set for a ﬁxed value of
ξ as K2(ξ(ω)) = {x| there exists y s.t. Wy = h(ω) −T(ω)x, y ∈Y } where
ξ(ω) is formed by the stochastic components of h(ω) and T(ω).
Proposition 22. The second-stage feasibility set K2(ξ) is in general
nonconvex.
Proof:
Because K2(ξ) = {x|Q(x, ξ) < ∞}, nonconvexity of K2(ξ) imme-
diately follows from nonconvexity of Q(x, ξ).
A simple example suﬃces to illustrate this possibility.
Example 3
Let the second stage of a stochastic program be deﬁned as
−y1 + y2≤ξ −x1,
(3.2)
y1 + y2≤2 −x2,
(3.3)
y1, y2≥0 and integer.
(3.4)
Assume ξ takes on the values 1 and 2 with equal probability 1/2. We then
construct K2(1).


## Page 132

3.3 Stochastic Integer Programs
113
By (3.3), x2 ≤2 is a necessary condition for second-stage feasibility. For
1 < x2 ≤2, the only feasible integer satisfying (3.3) is y1 = y2 = 0. This
point is also feasible for (3.2) if ξ −x1 ≥0, i.e., if x1 ≤1.
FIGURE 2. Feasibility set for Example 3.
For 0 < x2 ≤1, the integer points y satisfying (3.3) are (0, 0), (0, 1), (1, 0).
The one yielding the smallest left-hand side (and thus the most likely to
yield points in K2(1)) is (1, 0). It requires ξ −x1 ≥−1, i.e., x1 ≤2. Hence
K2(1) is as in Figure 2 and is clearly nonconvex. It may be represented as
K2(1) = {x| min{x1 −1, x2 −1} ≤0, 0 ≤x1 ≤2, 0 ≤x2 ≤2} and is again
a typical Gomory function due to the minimum operation.
We may then deﬁne the second-stage feasibility set K2 as the intersection
of K2(ξ) over all possible ξ values. This deﬁnition poses no diﬃculty when
ξ has a discrete distribution. In Example 3, K2 = K2(1) and is thus also
nonconvex.
Computationally, it might be very useful to have the constraint matrix
of the extensive form totally unimodular. (Recall that a matrix is totally
unimodular if the determinants of all square submatrices are 0, 1, or −1.)
This would imply that any solution of the associated stochastic continuous
program would be integer when right-hand sides of all constraints are also
integer. A widely used suﬃcient condition for total unimodularity is as
follows: all coeﬃcients are 0, 1, or −1; every variable has at most two
nonzero coeﬃcients and constraints can be separated in two groups such
that, if a variable has two nonzero coeﬃcients and if they are of the same
sign, the two associated rows belong to diﬀerent sets and if they are of
opposite signs they belong to the same set.
To help understand the suﬃciency condition, consider the following
matrix


1
0
1
−1
0
1
1
0
−1
1
0
1


as an example. For this matrix, one set consists of Rows 1 and 3, and the
second set contains just Row 2. The constraint matrix of the extensive form


## Page 133

114
3. Basic Properties and Theory
of a nontrivial stochastic program cannot satisfy this suﬃcient condition.
For simplicity, consider the case of a ﬁxed T matrix. Assume that any
variable that has a nonzero coeﬃcient in T also has a nonzero coeﬃcient
in A. Then, if |Ξ| ≥2, the constraint matrix of the extensive form contains
a submatrix


A
T
T


that has at least three nonzero coeﬃcients. Thus, only very special cases
(a random T matrix with every column having a nonzero element in only
one realization, for example) could lead to totally unimodular matrices.
Last but not least, it should be clear that just ﬁnding Q(x) for a given x
becomes an extremely diﬃcult task for a general integer second stage. This
is especially true because there is no hope to use sensitivity analysis or some
sort of bunching procedure (see Section 5.4) to ﬁnd Q(x,ξ) for neighboring
values of ξ. Cases where Q(x) can be computed or even approximated in a
reasonable amount of time should thus be considered exceptions. One such
exception is provided in the next section.
b. Simple integer recourse
Let ξ be a random vector with support Ξ in ℜm, expectation µ, and cumu-
lative distribution F with F(t) = P{ξ ≤t}, t ∈Rm. A two-stage stochastic
program with simple integer recourse is as follows:
SIR
min z= cT x + Eξ{min(q+)T y+ + (q−)T y−|
y+ ≥ξ −Tx, y−≥Tx −ξ,
y+ ∈Zm
+ , y−∈Zm
+ }
s.t. Ax= b, x ∈X,
(3.5)
where X typically deﬁnes either non-negative continuous or non-negative
integer decision variables and where we use ξ = h because both T and q
are known and ﬁxed. As in the continuous case, we may replace the second-
stage value function Q(x) by a separable sum over the various coordinates.
Let χ = Tx be a tender to be bid against future outcomes. Then Q(x) is
separable in the components χi.
Q(x) =
m

i=1
ψi(χi),
(3.6)
with
ψi(χi) = Eξiψi(χi,ξi)
(3.7)
and
ψi(χi, ξi)= min{q+
i y+
i + q−
i y−
i |y+
i ≥ξi −χi,


## Page 134

3.3 Stochastic Integer Programs
115
y−
i ≥χi −ξi, y+
i , y−
i ∈Z+}.
(3.8)
As in the continuous case, any error made in bidding χi versus ξi must be
compensated for in the second stage, but this compensation must now be
an integer.
Now deﬁne the expected shortage as
ui(χi) = E⌈ξi −χi⌉+
and the expected surplus as
vi(χi) = E⌈χi −ξi⌉+,
where ⌈x⌉+ = max{⌈x⌉, 0}. It follows that ψi(χi) is simply
ψi(χi) = q+
i ui(χi) + q−
i vi(χi).
As is reasonable from the deﬁnition of SIR, we assume q+
i ≥0, q−
i ≥0.
Studying SIR is thus simply studying the expected shortage and surplus.
Unless necessary, we drop the indices in the sequel. Let ξ be some random
variable and x ∈ℜ. The expected shortage is
u(x) = E⌈ξ −x⌉+
(3.9)
and the expected surplus is
v(x) = E⌈x −ξ⌉+.
(3.10)
For easy reference, we also deﬁne their continuous counterparts. Let the
continuous expected shortage be
ˆu(x) = E(ξ −x)+
(3.11)
and the continuous expected surplus be
ˆv(x) = E(x −ξ)+.
(3.12)
First observe that Example 1 (and 2) is a case of a stochastic program with
simple recourse, from which we know that u(x) + v(x) is in general non-
convex and discontinuous unless ξ has an absolutely continuous probability
distribution function. We thus limit our ambitions to study ﬁniteness and
computational tractability for u(.) and v(.). The following results appear
in Louveaux and van der Vlerk [1993].
Proposition 23. The expected shortage function is a non-negative non-
decreasing extended real-valued function. It is ﬁnite for all x ∈ℜif and
only if µ+ = E max{ξ, 0} is ﬁnite.


## Page 135

116
3. Basic Properties and Theory
Proof:
We only give the proof for ﬁniteness because the other results are
immediate. First, observe that for all t in ℜ,
(t −x)+ ≤⌈t −x⌉+ ≤(t −x + 1)+ ≤(t −x)+ + 1.
Taking expectation yields
ˆu(x) ≤u(x) ≤ˆu(x −1) ≤ˆu(x) + 1.
(3.13)
The result follows as ˆu(x) is ﬁnite if and only if µ+ is ﬁnite.
We now provide a computational formula for u(x).
Theorem 24. Let ξ be a random variable with cumulative distribution
function F. Then
u(x) =
∞

k=0
(1 −F(x + k)).
(3.14)
Proof:
Following the previous deﬁnitions, we have:
∞

k=0
(1 −F(x + k)) =
∞

k=0
P{ξ −x > k}
=
∞

k=0
∞

j=k+1
P{⌈ξ −x⌉+ = j}
=
∞

j=1
j−1

k=0
P{⌈ξ −x⌉+ = j}
=
∞

j=1
jP{⌈ξ −x⌉+ = j} = E⌈ξ −x⌉+ = u(x),
which completes the proof.
Similar results hold for v(x).
Theorem 25. Let ξ be a random variable with ˆF(t) = P{ξ < t} and
µ−= Eξ−. Then v is a non-negative nondecreasing extended real-valued
function, which is ﬁnite for all x ∈ℜif and only if µ−is ﬁnite. Moreover,
v(x) =
∞

k=0
ˆF(x −k).
(3.15)
Theorems 24 and 25 provide workable formulas for a number of cases.
Case a. Clearly, if ξ has a ﬁnite range, then (3.14) and (3.15) reduce to
a ﬁnite computation.


## Page 136

3.3 Stochastic Integer Programs
117
Example 4
Let ξ have a uniform density on [0, a]. Consider 0 ≤x ≤a. Then
u(x) =
∞

k=0
(1 −F(x + k)) =
⌈a−x⌉+−1

k=0
(1 −F(x + k))
=
⌈a−x⌉+−1

k=0

1 −x + k
a

= ⌈a −x⌉+ 
1 −x
a

−⌈a −x⌉+(⌈a −x⌉+ −1)
2a
.
Observe that ⌈a−x⌉+ is piecewise constant. Hence, u(x) is piecewise linear
and convex.
Similarly, one computes
v(x) = x(⌊x⌋+ 1)
a
−⌊x⌋(⌊x⌋+ 1)
2a
.
Again, v(x) is piecewise linear and convex. It follows that a simple inte-
ger recourse program with uniform densities is a piecewise linear convex
program whose second-stage recourse function is easily computable.
Case b. For some continuous random variables, we may obtain analytical
expressions for u(x) and v(x).
Example 5
Let ξ follow an exponential distribution with parameter λ > 0. Then, for
x ≥0,
u(x) =
∞

k=0
(1 −F(x + k)) =
∞

k=0
e−λ(x+k) =
e−λx
1 −e−λ ,
while
v(x) =
∞

k=0
F(x −k) = ⌊x⌋+ 1 −e−λ(x−⌊x⌋) ·
⌊x⌋

k=0
e−λk
= ⌊x⌋+ 1 −
e−λ(x−⌊x⌋) −e−λ(x+1)
1 −e−λ

.
Observe that v(x) is nonconvex (as it would be u(x) for x ≤0).
Case c. Finite computation can also be obtained when Ξ ∈Z. From
Theorems 24 and 25, we derive the following corollary.


## Page 137

118
3. Basic Properties and Theory
Corollary 26. For all n ∈Z+, we have
u(x + n) = u(x) −
n−1

k=0
(1 −F(x + k))
(3.16)
and
v(x + n) = v(x) +
n

k=1
ˆF(x + k)).
(3.17)
Corollary 27. Let ξ be a discrete random variable with support Ξ ∈Z.
Then
u(x) =

µ+ −⌊x⌋−	−1
k=⌊x⌋F(k)
if x < 0,
µ+ −⌊x⌋+ 	⌊x⌋−1
k=0
F(k)
if x ≥0.
Proof:
Because Ξ ∈Z, F(t) = F(⌊t⌋), for all t ∈ℜ. Hence, u(x) = u(⌊x⌋)
for all x ∈R. Now, u(0) = µ+. Then apply (3.16) to obtain the result.
Corollary 28. Let ξ be a discrete random variable with support Ξ ∈Z.
Then
v(x) =

µ−−	−1
k=⌈x⌉F(k)
if x < 0,
µ−+ 	⌈x⌉−1
k=0
F(k)
if x ≥0.
Thus, here the ﬁnite computation comes from the ﬁniteness of ⌈x⌉.
Case d. Finally, we may have a random variable that does not fall in any
of the given categories. We may then resort to approximations.
Theorem 29. Let ξ be a random variable with cumulative distribution
function, F. Then
ˆu(x) ≤u(x) ≤ˆu(x) + 1 −F(x).
(3.18)
Proof:
The ﬁrst inequality was given in (3.13). Because 1 −F(t) is nonin-
creasing, we have for any x ∈ℜand any k ∈{1, 2, · · ·} that
1 −F(x + k) ≤1 −F(t), t ∈[x + k −1, x + k).
Hence,
∞

k=1
(1 −F(x + k)) ≤
 ∞
x
(1 −F(t))dt.
Adding 1 −F(x) to both sides gives the desired result.


## Page 138

3.3 Stochastic Integer Programs
119
Theorem 30. Let ξ be a random variable with cumulative distribution
function F. Let n be some integer, n ≥1. Deﬁne
un(x) =
n−1

k=0
(1 −F(x + k)) + ˆu(x + n).
(3.19)
Then
un(x) ≤u(x) ≤un(x) + 1 −F(x + n).
(3.20)
Proof:
The proof follows directly from Theorem 29 and formula (3.16).
To approximate u(x) within an accuracy ε, we have to compute the ﬁrst
n terms in u(x), where n is chosen so that F(x + n) ≥1 −ε and ˆu(x + n),
which involves computing one integral.
Example 6
Let ξ follow a normal distribution with mean µ and variance σ2, i.e.,
N(µ, σ2), with cumulative distribution function
F and probability den-
sity function f. Integrating by parts, one obtains:
un(x) =
n−1

k=0
(1 −F(x + k)) +
 ∞
x+n
(1 −F(t))dt
=
n−1

k=0
(1 −F(x + k)) −(x + n)(1 −F(x + n)) +
 ∞
x+n
tf(t)dt.
Using tf(t) = µf(t) −σ2f ′(t), it follows that
un(x) =
n−1

k=0
(1 −F(x + k)) + (µ −x −n)(1 −F(x + n)) + σ2f(x + n).
Similar results apply for v(x).
Theorem 31. Let ξ be a random variable with cumulative distribution
function ˆF(t) = P {ξ < t}. Then
ˆv(x) ≤v(x) ≤ˆv(x) + ˆF(x).
(3.21)
Let n be some integer, n ≥1. Deﬁne
vn(x) =
n−1

k=0
ˆF(x −k) + ˆv(x −n).
(3.22)
Then
vn(x) ≤v(x) ≤vn(x) + ˆF(x −n).
(3.23)


## Page 139

120
3. Basic Properties and Theory
Example 6 (continued)
Let ξ follow an N(µ, σ2) distribution, with cumulative distribution function
F and probability density function f. Then
vn(x) =
n−1

k=0
F(x −k) + (x −n −µ)F(x −n) + σ2f(x −n).
As a conclusion, expected shortage, expected surplus, and thus simple in-
teger recourse functions can be computed in ﬁnitely many steps either in
an exact manner or within a prespeciﬁed tolerance ε. Deeper studies of
continuity and diﬀerentiability properties of the recourse function can be
found in Stougie [1987], Louveaux and van der Vlerk [1993], and Schultz
[1993].
c. Probabilistic constraints
Probabilistic constraints involving integer decision variables may generally
be treated in exactly the same manner as if they involved continuous de-
cision variables. One need only take the intersection of their deterministic
equivalents with the integrality requirements. The question is then how to
obtain a polyhedral representation of this intersection. This problem some-
times has quite nice solutions. Here we provide an example of probabilistic
constraints in routing problems.
Let V = {v1, v2, · · · , vn} be a set of vertices, typically representing cus-
tomers. Let v0 represent the depot and let V0 = V ∪{v0}. A route is an
ordered sequence L = {i0 = 0, i1, i2, · · · , ik, ik+1 = 0}, with k ≤n, starting
and ending at the depot and visiting each customer at most once. Clearly,
if k < n, more than one vehicle is needed to visit all customers. Assume
a vehicle of given capacity C follows each route, collecting customers’ de-
mands di. If demands di are random, it may turn out that at some point of
a given route, the vehicle cannot load a customer’s demand. This is clearly
an undesirable feature, which is usually referred to as a failure of the route.
A probabilistic constraint for the capacitated routing requires that only
routes with a small probability of failure are considered feasible:
P(failure on any route) ≤α.
(3.24)
We now show, as in Laporte, Louveaux, and Mercure [1989], that any route
that violates (3.24) can be eliminated by a linear inequality. For any route
L, let S = {i1, i2, · · · , ik} be the index set of visited customers. Violation
of (3.24) occurs if
P (

i∈S
di > C) > α.
(3.25)
Let Vα(S) denote the smallest number of vehicles required to serve S so
that the probability of failure in S does not exceed α, i.e., Vα(S) is the


## Page 140

3.3 Stochastic Integer Programs
121
smallest integer such that
P (

i∈S
di > C · Vα(S)) ≤α.
(3.26)
Now, let ¯S denote the complement of S versus V0, i.e., ¯S = V0\S. Then the
following subtour elimination constraint imposes, in a linear fashion, that
at least Vα(S) vehicles are needed to cover demand in S:

i∈S,j∈¯S or i∈¯S,j∈S
xij ≥2Vα(S),
(3.27)
where, as usual, xij = 1 when arc ij is traveled in the solution and xij = 0
otherwise. It follows that routes that violate (3.24) can be eliminated when
needed by the linear constraint (3.27). Observe that this result is obtained
without any assumption on the random variables. Also observe that (3.27)
is not the deterministic equivalent of (3.24). This should be clear from the
fact that an analytical expression for (3.24) is diﬃcult to write. Finally,
observe that in practice, as for many random variables, the probability
distribution of

i∈S
di is easily obtained. The computation of Vα(S) in (3.26)
poses no diﬃculty. Additional results appear in the survey on stochastic
vehicle routing by Gendreau, Laporte, and S´eguin [1996].
Exercises
1. Consider the following second-stage integer program:
Q(x, ξ) = max{4y1 + y2|y1 + y2 ≤ξx, y1 ≤2, y2 ≤1, y integer}.
(a) Obtain y∗
1, y∗
2, and Q(x, ξ) as Gomory functions.
(b) Consider ξ = 1. Observe that Q(x, 1) is piecewise constant on
four pieces (x < 1, 1 ≤x < 2, 2 ≤x < 3, 3 ≤x).
(c) Now assume ξ is uniformly distributed over [0, 2]. Obtain Q(x)
on four pieces (x < 0.5, 0.5 ≤x < 1, 1 ≤x < 1.5, 1.5 ≤x).
Check the nonconcavity of Q(x). Observe that Q(x) is concave
on each piece separately, but that Q(x) is not (compare, e.g.,
Q(1) to 1/2Q(3/4) + 1/2Q(5/4).
2. Consider ξ uniformly distributed over [0, 1] and 0 ≤x ≤1. Show that
u(x) + v(x) = 1.
3. Consider ξ uniformly distributed over [0, 2].
(a) Compute u(x) directly from deﬁnition (3.9) and check with the
result in Example 4. Observe that u(x) is piecewise linear, con-
vex, and continuous.


## Page 141

122
3. Basic Properties and Theory
(b) Compute ˆu(x).
(c) Show that u(x) −ˆu(x) is decreasing in x.
4. Consider ξ that is Poisson distributed with parameter three. Compute
u(3).
5.
(a) Let ξ be normally distributed with mean zero and variance one.
What is the accuracy level of u3(0) versus u(0).
(b) Let ξ be normally distributed with mean µ and variance σ2.
Show that u(µ) is independent of µ. Is the accuracy of un(µ), n
given, increasing or decreasing with σ2?
3.4
Two-Stage Stochastic Nonlinear Programs
with Recourse
In this section, we generalize the results from the previous sections to prob-
lems with nonlinear functions. The results extend directly so the treatment
here will be brief. The basic types of results we would like to obtain concern
the structure of the feasible region, the optimal value function, and opti-
mality conditions. As a note of caution, some of the results in this chapter
refer to concepts from measure theory.
We begin with a deﬁnition of the two-stage stochastic nonlinear program
with (additive) recourse. The additive form of the recourse is used to obtain
separation of ﬁrst- and second-period problems as in (1.2). This problem
has the form:
inf z = f 1(x) + Q(x)
s. t. g1
i (x) ≤0,i = 1, . . . , ¯m1,
g1
i (x) = 0,i = ¯m1 + 1, . . . , m1,
(4.1)
where Q(x) = Eω[Q(x, ω)] and
Q(x, ω) = inf f 2(y(ω), ω)
s. t. t2
i (x, ω) + g2
i (y(ω), ω)≤0, i = 1, . . . , ¯m2,
t2
i (x, ω) + g2
i (y(ω), ω)= 0, i = ¯m2 + 1, . . . , m2,
(4.2)
where all functions f 2(·, ω), t2
i (·, ω), and g2
i (·, ω) are continuous for any ﬁxed
ω and measurable in ω for any ﬁxed ﬁrst argument. Given this assumption,
Q(x, ω) is measurable (Exercise 1) and hence Q(x) is well-deﬁned.
We make the following deﬁnitions consistent with Section 1.
K1 ≡{x|g1
i (x) ≤0, i = 1, . . . , ¯m1; g1
i (x) = 0, i = ¯m1 + 1, . . . , m1},
K2(ω) = {x|∃y(ω)|t2
i (x, ω) + g2
i (y(ω), ω) ≤0, i = 1, . . . , ¯m2;


## Page 142

3.4 Two-Stage Stochastic Nonlinear Programs with Recourse
123
t2
i (x, ω) + g2
i (y(ω), ω) = 0, i = ¯m2 + 1, . . . , m2},
and
K2 = {x|Q(x) < ∞}.
We have not forced ﬁxed recourse in Problem 4.1 because the second-period
constraint functions may depend on ω and on y(ω). For linear programs,
we assumed ﬁxed recourse so we could describe the feasible region in terms
of intersections of feasible regions for each random outcome. We could also
follow this approach here but the conditions for this result depend directly
on the form of the objective and constraint functions. We explore these
possibilities in Exercise 1 but we continue here with the more general case.
We also only allow the ﬁrst-period decision x to act separately in the
constraints of the recourse problem. We make this restriction so we can
develop optimality conditions that are separable between the ﬁrst- and
second-period variables. Other formulations might allow for nonseparable
constraints and dependence of the objective on x. In this way, we could
model distributional changes through a transformation determined by x.
We make some other assumptions, however, to allow results along the
lines of the previous section. These conditions ensure regularity for the
application of necessary and suﬃcient optimality conditions.
1. Convexity. The function f 1 is convex on ℜn1, g1
i is convex on ℜn1
for i = 1, . . . , ¯m1, g1
i is aﬃne on ℜn1 for i = ¯m1 + 1, . . . , m1, f 2(·, ω)
is convex on ℜn2 for all ω ∈Ω, g2
i (·, ω) is convex on ℜn2 for all
i = 1, . . . , ¯m2 and for all ω ∈Ω, g2
i (·, ω) is aﬃne on ℜn2 for i =
¯m2 + 1, . . . , m2 and for all ω ∈Ω, and t2
i (·, ω) is convex on ℜn1 for
all i = 1, . . . , ¯m2 and for all ω ∈Ω, and t2
i (·, ω) is aﬃne on ℜn1 for
i = ¯m2 + 1, . . . , m2.
2. Slater condition. If Q(x) < ∞, for almost all ω ∈Ω, there exists
some y(ω) such that t2
i (x, ω) + g2
i (ω, y(ω)) < 0 for i = 1, . . . , ¯m2 and
t2
i (x, ω) + g2
i (ω, y(ω)) = 0 for i = ¯m2 + 1, . . . , m2.
The main purpose of these assumptions is to ensure that the resulting
deterministic equivalent nonlinear program is also convex. The following
theorem gives conditions for convexity of the recourse function. It follows
directly from the deﬁnitions.
Theorem 32. Under Assumptions 1 and 2, the recourse function Q(x, ω)
is a convex function of x for all ω ∈Ω.
Proof:
Let y1 solve the optimization problem in (4.2) for x1 and let y2
solve the corresponding problem for x2. Consider x = λx1 + (1 −λ)x2. In
this case, t2
i (λx1 +(1−λ)x2, ω)+g2
i (λy1 +(1−λ)y2, ω) ≤λt2
i (x1, ω)+(1−
λ)t2
i (x2, ω) + λg2
i (y1, ω) + (1 −λ)g2
i (y2, ω) ≤0 for each i = 1, . . . , ¯m2. We
also have that t2
i (λx1 +(1−λ)x2, ω)+g2
i (λy1 +(1−λ)y2, ω) = λt2
i (x1, ω)+


## Page 143

124
3. Basic Properties and Theory
(1−λ)t2
i (x, ω)+λg2
i (y1, ω)+(1−λ)g2
i (y2, ω) = 0 for each i = ¯m2+1, . . . , m2.
So, Q(λx1 + (1 −λ)x2, ω) ≤f 2(λy1 + (1 −λ)y2, ω) ≤λf 2(x1, ω) + (1 −
λ)f 2(x2, ω) = λQ(x1, ω) + (1 −λ)Q(x2, ω), giving the result.
We can also obtain continuity of the recourse function if we assume the
recourse feasible region is bounded.
Theorem 33. If the recourse feasible region is bounded for any x ∈ℜn1,
then the function Q(x, ω) is lower semicontinuous in x for all ω ∈Ω(i.e.,
Q(x, ω) is a closed convex function).
Proof:
Proving lower semicontinuity is equivalent (see, e.g., Rockafellar
[1969]) to showing that
lim inf
x→¯x Q(x, ω) ≥Q(¯x, ω)
for any ¯x ∈ℜn1, x →¯x, and ω ∈Ω. Suppose a sequence xν →¯x. We can
assume that Q(xν, ω) < ∞for all ν because there is either a subsequence
of {xν} that is ﬁnite valued in Q or the result holds trivially.
We therefore have t2
i (xν, ω) + g2
i (yν(ω), ω) ≤0 for i = 1, . . . , ¯m2
and t2
i (xν, ω) + g2
i (yν(ω), ω) = 0 for i = ¯m2 + 1, . . . , m2 and for some
yν(ω). Hence, by continuity of each of these functions and the bound-
edness assumption, the {yν(ω)} sequence must have some limit point,
e.g., ¯y(ω). Thus, t2
i (¯x, ω) + g2
i (¯y(ω), ω) ≤0 for i = 1, . . . , ¯m2 and
t2
i (¯x, ω) + g2
i (¯y(ω), ω) = 0 for i = ¯m2 + 1, . . . , m2. So, ¯x is feasible and
Q(¯x, ω) ≤f 2(¯x, ω) = limν f 2(xν, ω) = limν Q(xν, ω).
Because integration is a linear operation on the convex function Q, we
obtain the following corollaries.
Corollary 34. The expected recourse function Q(x) is a convex function
in x.
Corollary 35. The feasibility set K2 = {x|Q(x) < ∞} is closed and
convex.
Corollary 36. Under the conditions in Theorem 33, Q is a lower semi-
continuous function on x.
This corollary then leads directly to the following attainability result.
Theorem 37. Suppose the conditions in Theorem 33, K1 is bounded, f 1
continuous, g1
i and g2
i continuous for each i, and K1 ∩K2̸ = ∅. Then (4.1)
has a ﬁnite optimal solution and the inﬁmum is attained.
Proof:
From Corollary 34, Q is continuous on its eﬀective domain. The
continuity of g1
i also implies that K1 is closed so the optimization is


## Page 144

3.4 Two-Stage Stochastic Nonlinear Programs with Recourse
125
for a continuous, convex function over the nonempty, compact region
K1 ∩K2.
Other results may follow for speciﬁc cases from Fenchel’s duality theorem
(see Rockafellar [1969]). In some cases, it may be diﬃcult to decompose the
feasibility set K2 into ∩ωK2(ω). It is possible if f 2 is always dominated by
some integrable function in ω for any y(ω) feasible in the recourse problem
for all x. This might be veriﬁable if, for example, the feasible recourse region
is bounded for all x ∈K1. Another possibility is for special functions such
as the quadratic function in Exercise 2.
We can now proceed to state optimality conditions for (4.1) as in The-
orem 9. As a reminder from Section 2.9, in the following, we use ri to
indicate relative interior.
Theorem 38. If there exists x such that x ∈ri(dom(f 1(x)) and x ∈
ri(dom(Q(x))) and g1
i (x) < 0 for all i = 1, . . . , ¯m1 and g1
i (x) = 0 for all
i = ¯m1 + 1, . . . , m1, then x∗is optimal in (4.1) if and only if x∗∈K1
and there exists λ∗
i ≥0, i = 1, . . . , ¯m1, λ∗
i , i = ¯m1 + 1, . . . , m1, such that
λ∗
i g1
i (x∗) = 0, i = 1, . . . , ¯m1, and
0 ∈∂f 1(x∗) + ∂Q(x∗) +
m1

i=1
λ∗
i ∂g1
i (x∗).
(4.3)
Proof: This result is a direct extension of the general optimality conditions
in nonlinear programming (see, e.g., Rockafellar [1969, Theorem 28.3]).
For most practical purposes, we need to obtain some decomposition of
∂Q(x) into subgradients of the Q(x, ω). The same argument as in Theorem
11 applies here so that
∂Q(x) = Eω[∂Q(x, ω)] + N(K2, x)
(4.4)
for all x ∈K. Moreover, if we have relatively complete recourse, we can
remove the normal cone term in (4.4).
We can also develop optimality conditions that apply to the problem
with explicit constraints on nonanticipativity as in Section 1. In this case,
Problem 4.1 becomes
inf
(x(ω),y(ω))∈X

Ω
(f 1(x(ω)) + f 2(y(ω), ω))µ(dω)
s. t. g1
i (x(ω))≤0, a.s.,
i = 1, . . . , ¯m1,
g1
i (x(ω))= 0, a.s.,
i = ¯m1 + 1, . . . , m1,
EΩ(x(ω)) −x(ω)= 0, a.s.,
t2
i (x(ω), ω) + g2
i (y(ω), ω)≤0, a.s.,


## Page 145

126
3. Basic Properties and Theory
i = 1, . . . , ¯m2,
t2
i (x(ω), ω) + g2
i (y(ω), ω)= 0, a.s.,
i = ¯m2 + 1, . . . , m2,
x(ω), y(ω)≥0, a.s.
(4.5)
The optimality results appear in the following theorem.
Theorem 39. Assume that (4.5) with X = L∞(Ω, B, µ; ℜn1+n2) is fea-
sible, has a bounded optimal value, satisﬁes relatively complete recourse,
and that a feasible solution (x∗(ω), y∗(ω)) is at a point satisfying the lin-
ear independence condition that any vector in ∂f 2(y∗(ω), ω) cannot be
written as a combination of some strict subset of representative vectors
from ∂g2
i (y∗(ω), ω) for i such that t2
i (x∗(ω), ω) + g2
i (y∗(ω), ω) = 0. Then
(x∗(ω), y∗(ω)) is optimal in (4.5) if and only if there exist integrable func-
tions on Ω, (λ∗(ω), ρ∗(ω), π∗(ω)), such that, for almost all ω,
ρ∗(ω) ∈∂f 1(x∗(ω))+
m1

i=1
λ∗
i (ω)∂g1
i (x∗(ω))+
m2

i=1
π∗
i (ω)∂t2
i (x∗(ω), ω), (4.6)
λ∗
i (ω) ≥0, λ∗
i (ω)g1
i (x∗(ω)) = 0, i = 1, . . . , ¯m1,
(4.7)
0 ∈∂f 2(y∗(ω), ω) +
m2

i=1
π∗
i (ω)∂g2
i (y∗(ω), ω),
(4.8)
π∗
i (ω) ≥0, π∗
i (ω)g2
i (y∗(ω), ω) = 0, i = 1, . . . , ¯m2,
(4.9)
and
Eω[ρ∗(ω)] = 0.
(4.10)
Proof:
The proof of Theorem 39 is similar to the proof of Theorem 13.
We ﬁrst observe that the conditions are suﬃcient (Exercise 4) and then
develop the necessary conditions using (4.5). In this case, we just need
to ﬁnd ∂Q(x, ω). By the regularity assumption (see again, e.g., Bazaraa
and Shetty [1979, Theorem 6.2.4]), Q(x, ω) = sup{π(ω):πi(ω)≥0,i=1,..., ¯m2}
infy(ω){f 2(ω, y(ω)) + 	m2
i=1 πi(ω)(g2
i (ω, y(ω)) + t2
i (x(ω), ω))}. For the inﬁ-
mum problem, we have through the regularity condition that if y∗(ω) is
a minimizer given x∗(ω) and π∗(ω) with π∗
i (ω) ≥0, i = 1, . . . , ¯m2, then
0 ∈∂f 2(y∗(ω), ω) + 	m2
i=1 π∗
i (ω)∂g2
i (y∗(ω), ω).


## Page 146

3.4 Two-Stage Stochastic Nonlinear Programs with Recourse
127
Because any vector ηi ∈∂t2
i (x∗(ω), ω) satisﬁes ηT
i (x−x∗) ≤t2
i (x(ω), ω)−
t2
i (x∗(ω), ω) by assumption,
m2

i=1
π∗
i (ω)ηT
i (x −x∗)
≤f 2(y∗(ω), ω) +
m2

i=1
π∗
i (ω)(g2
i (y∗(ω), ω) + t2
i (x(ω), ω))
−f 2(y∗(ω), ω) −
m2

i=1
π∗
i (ω)(g2
i (y∗(ω), ω) + t2
i (x∗(ω), ω))
≤Q(x, ω) −Q(x∗, ω).
Next, suppose there exists some η such that η ∈∂Q(x∗, ω) but η̸ =
	
i π∗
i ηi for any ηi ∈∂t2
i (x∗(ω), ω) then, by the Farkas lemma, there ex-
ists some z such zT η > 0 and π∗
i zT ηi ≤0 for all i and π∗
i such that
0 ∈∂f 2(y∗(ω), ω) + 	m2
i=1 π∗
i (ω)∂g2
i (y∗(ω), ω). However, zT η > 0 im-
plies that Q(x∗+ z, ω) > Q(x∗, ω) while π∗
i zT ηi ≤0, which then im-
plies that −t2
i (x + z, ω) + t2
i (x, ω) ≤0 and, for any constraint i with
some positive π∗
i , the directional derivative of t2
i at x∗in the direction z is
t2′
i (x∗; z) = supηi∈∂t2
i (x∗){zT ηi} ≤0. Hence for all t2
i (x∗, ω)+g2
i (y∗(ω), ω) =
0, t2
i (x∗+z, ω) ≤t2
i (x∗, ω) for some nonzero z. Thus, the y∗(ω) is still feasi-
ble in the recourse problem with x(ω) = x∗+z and Q(x∗+z, ω) ≤Q(x∗, ω).
So, we must have that {	m2
i=1 π∗
i (ω)ηT
i (x −x∗)|ηi ∈∂t2
i (x∗(ω), ω)} and
0 ∈∂f 2(y∗(ω), ω) + 	m2
i=1 π∗
i (ω)∂g2
i (y∗(ω), ω) = ∂Q(x∗, ω). Now, we can
deﬁne ρ∗(ω) as −Eω[	m2
i=1 π∗
i (ω)ηi] + 	m2
i=1 π∗
i (ω)ηi to obtain the result as
in Theorem 12.
Again the ρ functions represent the value of information in each of the
scenarios under ω. These results can also be generalized to allow for non-
separability between the ﬁrst and second stage but for our computational
descriptions, this is generally not necessary.
Exercises
1. Show that the assumptions made when deﬁning (4.1) and (4.2) imply
that Q(x, ω) is a measurable function of ω for all x. (Hint: Find
{ω|Q(x, ω) ≤α} for any α using a countable covering of ℜn2.)
2. Suppose f 2 is a convex, quadratic function on ℜn2 for each ω ∈Ω
and the constraints g2
i and h2
j are aﬃne on ℜn2 for all i = 1, . . . , ¯m2
and j = 1, . . . , m2 −¯m2. What conditions on ξ(ω) can guarantee that
K2 = ∩ωK2(ω)?
3. Construct an example in which the recourse function Q(x, ω) is not
lower semicontinuous. (Hint: Try to make the only feasible recourse


## Page 147

128
3. Basic Properties and Theory
action tend to ∞while the ﬁrst-period action tends to some ﬁnite
value.)
4. Show that conditions in (4.6)–(4.10) are suﬃcient to obtain optimal-
ity in (4.5).
3.5
Multistage Stochastic Programs with
Recourse
The previous sections in this chapter concerned stochastic programs with
two stages. Most practical decision problems, however, involve a sequence
of decisions that react to outcomes that evolve over time. In this section,
we will consider the stochastic programming approach to these multistage
problems.
We present the same basic results as in previous chapters. We describe
the basic structure of feasible solutions, objective values, and conditions
for optimality. We begin again with the linear, ﬁxed recourse, ﬁnite horizon
framework because this model has been the most widely implemented. We
then continue with more general approaches.
We start with implicit nonanticipativity constraints as in the previous
sections. The multistage stochastic linear program with ﬁxed recourse then
takes the following form.
min z = c1x1 + Eξ2[min c2(ω)x2(ω2) + · · · +EξH[min cH(ω)xH(ωH)] · · ·]
s. t. W 1x1= h1,
T 1(ω)x1 + W 2x2(ω2)= h2(ω),
· · ·...
T H−1(ω)xH−1(ωH−1) + W HxH(ωH)= hH(ω),
x1 ≥0; xt(ωt) ≥0, t = 2, . . . , H;
(5.1)
where c1 is a known vector in ℜn1, h1 is a known vector in ℜm1, ξt(ω)T =
(ct(ω)T , ht(ω)T , T t−1
1·
(ω), . . . , T t−1
mt· ) is a random Nt-vector deﬁned on (Ω,
Σt, P) (where Σt ⊂Σt+1) for all t = 2, . . . , H, and each W t is a known
mt × nt matrix. The decisions x depend on the history up to time t, which
we indicate by ωt. We also suppose that Ξt is the support of ξt.
We ﬁrst describe the deterministic equivalent form of this problem in
terms of a dynamic program. If the stages are 1 to H, we can deﬁne states
as xt(ωt). Noting that the only interaction between periods is through this
realization, we can deﬁne a dynamic programming type of recursion. For
terminal conditions, we have
QH(xH−1, ξH(ω)) = min cH(ω)xH(ω)
s. t. W HxH(ω)= hH(ω) −T H−1(ω)xH−1,
xH(ω)≥0.
(5.2)


## Page 148

3.5 Multistage Stochastic Programs with Recourse
129
Letting Qt+1(xt) = Eξt+1[Qt+1(xt, ξt+1(ω))] for all t, we obtain the recur-
sion for t = 2, . . . , H −1,
Qt(xt−1, ξt(ω)) = min ct(ω)xt(ω) + Qt+1(xt)
s. t. W txt(ω)= ht(ω) −T t−1(ω)xt−1,
xt(ω)≥0,
(5.3)
where we use xt to indicate the state of the system. Other state information
in terms of the realizations of the random parameters up to time t should be
included if the distribution of ξt is not independent of the past outcomes.
The value we seek is:
min z = c1x1 + Q(x1)
s. t. W 1x1= h1,
x1≥0,
(5.4)
which has the same form as the two-stage deterministic equivalent pro-
gram. Examples of this formulation appeared in Chapter 1 in terms of the
capacity expansion and ﬁnance problems. The recourse represented reac-
tions to actual demand for power in the ﬁrst case and yield realizations in
the second case.
We would again like to obtain properties of the problems in (5.2)–(5.4)
that allow uses of mathematical programming procedures such as decompo-
sition. We concentrate ﬁrst on the form of the feasible regions for problems
of the form (5.3). Let these be
Kt = {xt|Qt+1(xt) < ∞}.
We have the following result which helps in the development of several
algorithms for multistage stochastic programs.
Theorem 40. The sets Kt and functions Qt+1(xt) are convex for t =
1, . . . , H −1 and, if Ξt is ﬁnite for t = 1, . . . , H, then Kt and Qt+1(xt) are
polyhedral.
Proof:
Proceed by induction. Because QH(xH−1, ξH(ω)) is convex for all
ξH(ω), so is QH(xH−1). We can then carry this back to each t < T −1.
The same applies for the polyhedrality property because ﬁnite numbers of
realizations lead to each Qt+1(xt)’s being the sum of a ﬁnite number of
polyhedral functions, which is then polyhedral.
We note that we may also describe the feasibility sets Kt in terms of
intersections of feasibility sets for each outcome if we have ﬁnite second
moments for ξt in each period. This result is also true when we have a
ﬁnite number of possible realizations of the future outcomes. In this case,
the set of possible future sequences of outcomes are called scenarios.
The description of scenarios is often made on a tree such as that in
Figure 3. Here, there are eight scenarios that are evident in the last stage


## Page 149

130
3. Basic Properties and Theory
(H = 4). In previous stages (t < 4), we have a more limited number of
possible realizations, which we call the stage t scenarios. Each of these
period t scenarios is said to have a single ancestor scenario in stage (t −1)
and perhaps several descendant scenarios in stage (t + 1). We note that
diﬀerent scenarios at stage t may correspond to the same ξt realizations
and are only distinguished by diﬀerences in their ancestors.
FIGURE 3. A tree of seven scenarios over four periods.
The deterministic equivalent program to (5.1) with a ﬁnite number of
scenarios is still a linear program. It has the structural form indicated in
Figure 4, where we use an additional superscript to index distinct values
of W t and T t. This is often called arborescent form and can be exploited
in large-scale optimization approaches as in Kallio and Porteus [1977]. A
diﬃculty is still, however, that these problems become extremely large as
the number of stages increases, even if only a few realizations are allowed
in each stage.
In some problems, however, we can avoid much of this diﬃculty if the in-
teractions between consecutive stages are suﬃciently weak. This is the case
in the capacity expansion problem described in Chapter 1. Here, capacity
carried over from one stage to the next is not aﬀected by the demand in that
stage. Decisions about the amount of capacity to install can be made at the
beginning and then the future only involves reactions to these outcomes.
Problems with this form are called block separable.
Formally, we have the following deﬁnition for block separability (see Lou-
veaux [1986]).


## Page 150

3.5 Multistage Stochastic Programs with Recourse
131
FIGURE 4. The deterministic equivalent matrix for a problem with seven sce-
narios in four periods.
Deﬁnition 41. A multistage stochastic linear program (5.1) has block
separable recourse if for all periods t = 1, . . . , H and all ω, the decision
vectors, xt(ω), can be written as xt(ω) = (wt(ω), yt(ω)) where wt represents
aggregate level decisions and yt represents detailed level decisions. The
constraints also follow these partitions:
1. The stage t objective contribution is ctxt(ω) = rtwt(ω) + qtyt(ω).
2. The constraint matrix W t is block diagonal:
W t =

At
0
0
Bt

.
(5.5)
3. The other components of the constraints are random but we assume
that for each realization of ω, T t(ω) and ht(ω) can be written:
T t(ω) =

Rt(ω)
0
St(ω)
0

and ht(ω) =

bt(ω)
dt(ω)

,
(5.6)
where the zero components of T t correspond to the detailed level variables.
Notice that (3) in the deﬁnition implies that detailed level variables have
no direct eﬀect on future constraints. This is the fundamental advantage
of block separability.
With block separable recourse, we may rewrite Qt(xt−1, ξt(ω)) as the
sum of two quantities, Qt
w(wt−1, ξt(ω)) + Qt
y(wt−1, ξt(ω)), where we need


## Page 151

132
3. Basic Properties and Theory
not include the yt−1 terms in xt−1,
Qt
w(wt−1, ξt(ω)) = min rt(ω)wt(ω) + Qt+1(xt)
s. t. Atwt(ω)= bt(ω) −Rt−1(ω)wt−1,
wt(ω)≥0,
(5.7)
and
Qt
y(wt−1, ξt(ω)) = min qt(ω)yt(ω)
s. t. Btyt(ω)= dt(ω) −St−1(ω)wt−1,
yt(ω)≥0.
(5.8)
The great advantage of block separability is that we need not consider
nesting among the detailed level decisions. In this way, the w variables can
all be pulled together into a ﬁrst stage of aggregate level decisions. The
second stage is then composed of the detailed level decisions. Note that if
the bt and Rt are known, then the block separable problem is equivalent
to a similarly sized two-stage stochastic linear program.
Separability is indeed a very useful property for stochastic programs.
Computational methods should try to exploit it whenever it is inherent
in the problem because it may reduce work by orders of magnitude. We
will also see in Chapter 11 that separability can be added to a problem
(with some error that can be bounded). This approach opens many possible
applications with large numbers of random variables.
Another modeling approach that may have some computational advan-
tage appears in Grinold [1976]. This approach extends from analyses of
stochastic programs as examples of Markov decision process. He assumes
that ωt belongs to some ﬁnite set 1, . . . , kt, that the probabilities are deter-
mined by pij = P{ωt+1 = j|ωt = i} for all t, and that T t = T t(ωt, ωt+1).
In this framework, he can obtain an approximation that again obtains a
form of separability of future decisions from previous outcomes. We discuss
more approximation approaches in Chapter 11.
We now consider generalizations into nonlinear functions and inﬁnite
horizons. The general results of the previous section can be extended
here directly. We concentrate on some areas where diﬀerences may oc-
cur and, for notational convenience, concentrate just on the description
of problems in the form with explicit nonanticipativity constraints. More
detailed descriptions of these problems appear in the papers by Rockafel-
lar and Wets [1976a,1976b], Dempster [1988], Fl˚am [1985], and Birge and
Dempster [1992].
For our basic model, we assume that within each period t, there is a
convex random extended-value function of xt and xt+1 that includes the
original objective and any constraints linking the decisions in periods t and
t + 1. The constraints are, therefore, implicitly contained in the objective
function.


## Page 152

3.5 Multistage Stochastic Programs with Recourse
133
The only explicit constraints are to maintain nonanticipativity. The re-
maining development again supposes some familiarity with concepts from
measure theory. Proofs are omitted because we are most interested in the
results for computational considerations. In this model, the random param-
eter is a data process, ω := {ωt : t = 0, . . .}. The decisions are a process
x := {xt : t = 0, . . .} such that x is a measurable function x : ω →x(ω).
The space of the decision processes is again the space of essentially bounded
functions, Ln
∞:= L∞(Ω×N, Σ×P(N), µ×#; ℜn), where P is the power set
and # is the counting measure. In distinguishing information from period
to period, we associate a ﬁltration with the data process. F := {Σt}∞
t=1,
where Σt := σ(¯ωt) is the σ-ﬁeld of the history process ¯ωt := {ω0, . . . , ωt},
and the Σt satisfy {0, Ω} ⊂Σ0 ⊂· · · ⊂Σ.
Nonanticipativity of the decision process at time t implies that decisions
must only depend on the data up to time t, i.e., xt must be Σt–measurable.
An alternative characterization of this nonanticipative property is that xt =
E{xt|Σt} a.s., t = 0, . . ., where E{·|Σt} is conditional expectation with
respect to the σ-ﬁeld Σt. Using the projection operator Πt : z →Πtz :=
E{z|Σt}, t = 0, . . ., this is equivalent to
(I −Πt)xt = 0, t = 0, . . . .
(5.9)
We then let N denote the closed linear subspace of nonanticipative pro-
cesses in Ln
∞.
The general multistage stochastic programming model is to ﬁnd
infx∈N E
H

t=0
f t(ω, xt(ω), xt+1(ω)),
(5.10)
where “E” is expectation with respect to Σ. Using our random variable
boldface notation, expression (5.10) then becomes
infx∈N E
H

t=0
f t(xt, xt+1),
(5.11)
with objective z(x) := E 	H
t=0 ft(xt, xt+1).
We develop optimality conditions that allow H →∞. The conditions
are basically the same as in previous sections (in terms of some assumption
about relatively complete recourse and some regularity condition), but we
need some additional assumptions to control multipliers at H = ∞. We
assume in (5.11) that the objective components f t are proper convex normal
integrands (in this case, proper, lower semicontinuous convex functions for
each t, see Rockafellar [1976b]) .
Without additional restrictions, the objective in (5.11) may be inﬁnite.
We can avoid this diﬃculty by deﬁning a policy x∗:= {x0, x1∗, . . .} as


## Page 153

134
3. Basic Properties and Theory
optimal (weakly) as in McKenzie [1976] if it is not overtaken by any other
policy, i.e., if there does not exist x′ such that
lim sup
τ→∞E
τ

t=0
(f t(x′,t, x′,t+1) −f t(x∗t, x∗t+1)) ≤−ǫ,
(5.12)
where ǫ > 0. This type of optimality has some advantages over other inﬁ-
nite horizon optimality conditions (such as average optimality). If we also
make some assumptions about the growth of values so that we can always
subtract some value from a weakly optimal solution to obtain a solution
with zero value, then we can assume that (5.11) has ﬁnite optimal value.
The following theorem states the basic necessary conditions for an op-
timal solution to (5.11). We do not give the proof that appears in Birge
and Dempster [1992]. Note that relatively complete recourse is replaced
here with nonanticipative feasibility as in Fl˚am [1986]. Dempster [1981] ob-
tains similar results using relatively complete recourse. In general, the two
conditions are similar but not identical (see Exercises 4 and 5).
Theorem 42. Suppose x∗is optimal in (5.11) with ﬁnite inﬁmum and the
following.
(a) (nonanticipative feasibility) For any x ∈dom z (i.e., such that
E 	∞
t=0 f t(xt, xt+1) < ∞), the projection of x into N, Πx, is
such that E 	∞
t=0 f t(Πxt, Πxt+1) < ∞.
(b) (strict feasibility) For some x ∈N, such that E 	∞
t=0 f t(xt, xt+1)
< ∞, there exists δ > 0 such that for all ∥y −x∥< δ, y ∈Ln
∞,
E 	∞
t=0 f t(yt, yt+1) < ∞.
(c) (ﬁnite horizon continuation approximation) For any x
∈
dom z, there exists x′ such that for all Hk in some sequence
{H1, H2, ...}, (xHk, x′,Hk+1, x′,Hk+2, . . .) is also feasible, and
the transition cost to x′ is such that |E[f Hk−1(xHk−1, xHk) +
f Hk(xHk, x′,Hk+1)]| →0 as k →∞and |E[f Hk−1(xHk−1, xHk)+
f Hk(xHk, x′,Hk+1)]| ≥|E[f Hk−1(xHk−1, xHk)+f Hk(xHk, xHk+1)]|
for k = 1, . . . .
Then x∗is optimal with given initial conditions x0 if and only if there exist
pt ∈Ln
1(Σ), t = 0, . . . such that
i. pt is nonanticipative, i.e. pt = E{pt|Σt} a.s. for t = 0, . . . .
ii. E0(f 0(x0, x1) −p0x0 + p1x1) is a.s. minimized by x∗1 = x1
over x1 = E{x1 | Σ1}, and, for t > 0, E(f t(xt, xt+1)−ptxt+
pt+1xt+1) is a.s. minimized by (x∗t, x∗t+1) = (xt, xt+1)
over xt = E{xt | Σt} and xt+1 = E{xt+1 | Σt+1}, and
iii. E ptk(xtk −x∗tk) →0 as tk →∞, for all x ∈dom z.


## Page 154

3.5 Multistage Stochastic Programs with Recourse
135
Proof: The proof is given in Birge and Dempster [1992] and follows Fl˚am
[1985, 1986]. The result establishes a price system, pt, on the value of
information.
This basic result can be extended to results with constraints in the same
way as necessary conditions in the previous sections. The only require-
ment is to describe the subdiﬀerentials of f t in terms of an objective and
constraint functions (see Exercise 6). The signiﬁcance of the result is that
we may again decompose the multistage problem into individual period t
problems. In this way, optimization may be applied at each period pro-
vided suitable multipliers are available. This property is the basis for the
Lagrangian and progressive hedging algorithms described in Chapter 6.
Exercises
1. Show why the capacity expansion example in Section 1.3 is block
separable.
2. State the optimality conditions of Theorem 42 for the ﬁnancial plan-
ning model in Section 1.2.
3. A policy is average optimal if it minimizes limH→∞
H
t=1 f(xt,xt+1)
H
.
Give an example where an average optimal policy is not weakly op-
timal. (Example: Suppose you can produce up to two items in any
period with a cost of one per item. You must meet demand of one in
each period. Can you produce more than one in each period and still
be average optimal?)
4. Suppose a multistage problem with constraints,
xt(1, ω) + xt+1(1, ω) + xt+1(2, ω) ≥ξt+1(ω),
where ξt ∈[0, 1]. If xt+1(i, ω) ≥0 a.s. with no other restrictions, this
problem would have relatively complete recourse. Suppose

Σt+1
ξt+1(ω)P(dω) < 1.
Show that this problem does not satisfy nonanticipative feasibility.
5. Suppose in the previous example that ξt+1(ω) ≡1+t. Show that this
problem satisﬁes nonanticipative feasibility but not relatively com-
plete recourse.
6. Suppose that constraints are explicitly represented by gt(xt, xt+1) in
(5.7) instead of being incorporated into f t. Use Theorem 42 to ﬁnd a
subdiﬀerential form of the necessary conditions similar to the result
in Theorem 39.


## Page 155



## Page 156

4
The Value of Information and the
Stochastic Solution
Stochastic programs have the reputation of being computationally diﬃcult
to solve. Many people faced with real-world problems are naturally inclined
to solve simpler versions. Frequently used simpler versions are, for example,
to solve the deterministic program obtained by replacing all random vari-
ables by their expected values or to solve several deterministic programs,
each corresponding to one particular scenario, and then to combine these
diﬀerent solutions by some heuristic rule.
A natural question is whether these approaches can sometimes be nearly
optimal or whether they are totally inaccurate. The theoretical answer to
this is given by two concepts: the expected value of perfect information
and the value of the stochastic solution. The object of this chapter is to
study these two concepts. Section 1 introduces the expected value of perfect
information. Section 2 gives the value of the stochastic solution. Some basic
inequalities and the relationships between these quantities are given in
Sections 3 and 4, respectively. Section 5 provides some examples of these
quantities. Section 6 presents additional bounds.
4.1
The Expected Value of Perfect Information
The expected value of perfect information (EVPI) measures the maximum
amount a decision maker would be ready to pay in return for complete
(and accurate) information about the future. In the farmer’s problem of
Chapter 1, we saw that the farmer would greatly beneﬁt from perfect in-


## Page 157

138
4. The Value of Information and the Stochastic Solution
formation about future weather conditions, so that he could allocate his
land optimally to the various crops.
The concept of EVPI was ﬁrst developed in the context of decision anal-
ysis and can be found in a classical reference such as Raiﬀa and Schlaifer
[1961]. In the stochastic programming setting, we may deﬁne it as follows.
Suppose uncertainty can be modeled through a number of scenarios. Let ξ
be the random variable whose realizations correspond to the various sce-
narios. Deﬁne
min z(x, ξ)= cT x + min{qT y | Wy = h −Tx, y ≥0}
(1.1)
s.t. Ax= b, x ≥0,
as the optimization problem associated with one particular scenario ξ,
where, as before, ξ(ω)T = (q(ω)T , h(ω)T , T1·(ω), . . . , Tm2·(ω)). To make
the deﬁnition complete, we repeat the notation, K1 = {x|Ax = b, x ≥0}
and K2(ξ) = {x|∃y ≥0 s.t. Wy = h −Tx}. We deﬁne z(x, ξ) = +∞if x̸ ∈
K1 ∩K2(ξ) and z(x, ξ) = −∞if (1.1) is unbounded below. We again use
the convention +∞+ (−∞) = +∞.
We may also reasonably assume that for all ξ ∈Ξ, there exists at least
one x ∈ℜn1 such that z(x, ξ) < ∞. (Otherwise, there would exist one
scenario for which no feasible solution exists at all. No reasonable stochastic
model could be constructed in such a situation.) This assumption implies
that, for all ξ ∈Ξ, there exists at least one feasible solution, which in turn
implies the existence of at least one optimal solution. Let ¯x(ξ) denote some
optimal solution to (1.1). As in a scenario approach, we might be interested
in ﬁnding all solutions ¯x(ξ) of problem (1.1) for all scenarios and the related
optimal objective values z(¯x(ξ), ξ).
This search is known as the distribution problem (as we mentioned in
Section 3.1c) because it looks for the distribution of ¯x(ξ) and of z(¯x(ξ), ξ)
in terms of ξ. The distribution problem can be seen as a generalization of
sensitivity analysis or parametric analysis in linear programming.
Here, we assume we somehow have the ability to ﬁnd these decisions ¯x(ξ)
and their objective values z(¯x(ξ), ξ) so that we are in a position to compute
the expected value of the optimal solution, known in the literature as the
wait-and-see solution (WS, see Madansky [1960]) where
WS= Eξ

min
x z(x,ξ)

= Eξz(¯x(ξ),ξ).
(1.2)
We may now compare the wait-and-see solution to the so-called here-and-
now solution corresponding to the recourse problem (RP) deﬁned earlier in
Chapter 3 as (1.1), and we may now write that as
RP = min
x Eξz(x,ξ),
(1.3)
with an optimal solution, x∗.


## Page 158

4.2 The Value of the Stochastic Solution
139
The expected value of perfect information is, by deﬁnition, the diﬀerence
between the wait-and-see and the here-and-now solution, namely,
EV PI= RP −WS.
(1.4)
An example was given in Chapter 1 in the farmer’s problem. The wait-
and-see solution value was −$115, 406 (when converted to a minimization
problem), while the recourse solution value was −$108, 390. The expected
value of perfect information for the farmer was then $7016.
This is how much the farmer would be ready to pay each year to ob-
tain perfect information on next summer’s weather. A meteorologist could
reasonably ask him to pay part of this amount to support meteorological
research.
4.2
The Value of the Stochastic Solution
For practical purposes, many people would believe that ﬁnding the wait-
and-see solution or equivalently solving the distribution problem is still too
much work (or impossible if perfect information is just not available at any
price). This is especially diﬃcult because the wait-and-see approach delivers
a set of solutions instead of one solution that would be implementable.
A natural temptation is to solve a much simpler problem: the one ob-
tained by replacing all random variables by their expected values. This is
called the expected value problem or mean value problem, which is simply
EV = min
x z(x, ¯ξ),
(2.1)
where ¯ξ = E(ξ) denotes the expectation of ξ. Let us denote by ¯x(¯ξ) an
optimal solution to (2.1), called the expected value solution. Anyone aware
of some stochastic programming or realizing that uncertainty is a fact of
life would feel at least a little insecure about advising to take decision ¯x(¯ξ).
Indeed, unless ¯x(ξ) is somehow independent of ξ, there is no reason to
believe that ¯x(¯ξ) is in any way near the solution of the recourse problem
(1.3).
The value of the stochastic solution (ﬁrst introduced in Chapter 1) is the
concept that precisely measures how good or, more frequently, how bad a
decision ¯x(¯ξ) is in terms of (1.3). We ﬁrst deﬁne the expected result of using
the EV solution to be
EEV = Eξ(z(¯x(¯ξ),ξ)).
(2.2)
The quantity, EEV, measures how ¯x(¯ξ) performs, allowing second-stage
decisions to be chosen optimally as functions of ¯x(¯ξ) and ξ. The value of
the stochastic solution is then deﬁned as
V SS= EEV −RP.
(2.3)


## Page 159

140
4. The Value of Information and the Stochastic Solution
Recall, for example, that in Section 1.1 this value was found using EEV =
−$107, 240 and RP = −$108, 390, for V SS = $1150. This quantity is the
cost of ignoring uncertainty in choosing a decision.
4.3
Basic Inequalities
The following relations between the deﬁned values have been established
by Madansky [1960]. Generalizations to nonlinear functions can be found
in Mangasarian and Rosen [1964].
Proposition 1.
WS ≤RP ≤EEV.
(3.1)
Proof:
For every realization, ξ, we have the relation
z(¯x(ξ), ξ) ≤z(x∗, ξ),
where, as said before, x∗denotes an optimal solution to the recourse prob-
lem (1.3). Taking the expectation of both sides yields the ﬁrst inequality.
x∗being an optimal solution to the recourse problem (1.3) while ¯x(¯ξ) is
just one solution to (1.3) yields the second inequality.
Proposition 2. For stochastic programs with ﬁxed objective coeﬃcients,
ﬁxed T, and ﬁxed W,
EV ≤WS.
(3.2)
Proof: Jensen’s inequality (Jensen [1906]) states that for any convex func-
tion f(ξ) of ξ, Ef(ξ) ≥f(Eξ). To apply this result, we need to show that
f(ξ) = minx z(x, ξ) is a convex function of ξ = (h). Convexity follows by
noting that minx z(x, ξ) = maxσ,π{σT b+πT h|σT A+πT T ≤cT , πT W ≤q}.
Since the constraints of the dual problem are unchanged for all ξ = (h), the
epigraph of f(ξ) is the intersection of the epigraphs of the linear functions
σT b + πT h for all feasible (σT , πT ). Hence, f(ξ) is convex because it has a
convex epigraph.
Proposition 2 does not hold for general stochastic programs. Indeed, if
we consider q only to be stochastic, by Theorem 3.5 the function z(x, ξ) is
a concave function of ξ and Jensen’s inequality does not apply. An example
of a program where EV > WS is given in Exercise 3.
Other bounds can be obtained. We give two more examples of such
bounds here.


## Page 160

4.4 The Relationship between EVPI and VSS
141
Proposition 3. Let x∗represent an optimal solution to the recourse prob-
lem (1.3) and let ¯x(¯ξ) be a solution to the expected value problem (1.5).
Then
RP ≥EEV +(x∗−¯x(¯ξ))T η,
(3.3)
where η ∈∂Eξz(¯x(¯ξ),ξ), the subdiﬀerential set of Eξz(x,ξ) at ¯x(¯ξ).
Proof:
By convexity of Eξz(x,ξ), the subgradient inequality applied at
point x1 implies that for any x2 the relation Eξz(x2,ξ) ≥Eξz(x1,ξ) +
(x2 −x1)T η holds. The proposition follows by application of this relation
for x1 = ¯x(¯ξ) and x2 = x∗, by noting that RP = Eξz(x∗,ξ) and EEV =
Eξz(¯x(¯ξ),ξ).
The last bound is obtained by considering a slightly diﬀerent version of
the recourse problem, deﬁned as follows:
min zu(x,ξ)= cT x + min{qT y | Wy ≥h(ξ) −Tx, y ≥0}
(3.4)
s. t. Ax = b,
x ≥0.
Problem (3.4) diﬀers from problem (1.1) because in (3.4) only the right-
hand side is stochastic and the second-stage constraints are inequalities. It
is not diﬃcult to observe that all deﬁnitions and relations also apply to
zu. If we further assume that h(ξ) is bounded above, then an additional
inequality results.
Proposition 4. Consider problem (3.4) and the related deﬁnition
RP = min
x Eξzu(x,ξ).
Assume further that h(ξ) is bounded above by a ﬁxed quantity hmax. Let
xmax be an optimal solution to zu(x, hmax). Then
RP≤zu(xmax, hmax).
(3.5)
Proof:
For any ξ in Ξ and any x ∈K1, a feasible solution to Wy ≥
hmax −Tx, y ≥0, is also a feasible solution to Wy ≥h(ξ) −Tx, y ≥0.
Hence zu(x, hmax) ≥zu(x, h(ξ)). Thus zu(x, hmax) ≥Eξzu(x, h(ξ)), hence
zu(x, hmax) ≥minx Eξzu(x, h(ξ)) = RP.
4.4
The Relationship between EVPI and VSS
The quantities, EVPI and VSS, are often diﬀerent, as our examples have
shown. This section describes the relationships that exist between the two
measures of uncertainty eﬀects.


## Page 161

142
4. The Value of Information and the Stochastic Solution
From the inequalities in the previous section, the following proposition
holds.
Proposition 5.
a. For any stochastic program,
0≤EV PI,
(4.1)
0≤V SS.
(4.2)
b. For stochastic programs with ﬁxed recourse matrix and ﬁxed objective
coeﬃcients,
EV PI≤EEV −EV,
(4.3)
V SS≤EEV −EV.
(4.4)
The proposition indicates that the EVPI and the VSS are (both) nonnega-
tive (anyone would be surprised if this was not true) and are both bounded
above by the same quantity EEV −EV , which is easily computable. It fol-
lows that when EV = EEV , both the EVPI and VSS vanish. A suﬃcient
condition for this to happen is to have ¯x(ξ) independent of ξ. This means
that optimal solutions are insensitive to the value of the random elements.
In such situations, ﬁnding the optimal solution for one particular ξ (or for
¯ξ) would yield the same result, and it is unnecessary to solve a recourse
problem. Such extreme situations rarely occur.
From these observations, three lines of research have been addressed. The
ﬁrst one studies relationships between EVPI and VSS. It is illustrated in
the sequel of this paragraph by showing an example where EVPI is zero
and VSS is not and an example of the reverse. The second one studies
classes of problems for which one can observe or theorize that the EVPI is
low. Examples and counterexamples are given in Section 5. The third one
studies reﬁned bounds on EVPI and VSS. Results about reﬁned upper and
lower bounds on EVPI and VSS appear in Section 6.
We thus end this section by showing examples taken from Birge [1982]
that illustrate cases in which one of the two concepts (EVPI and VSS) is
null and the other is positive.
a. EV PI = O and V SS̸ = O
Consider the following problem
z(x,ξ) =x1 + 4x2 + min{y1 + 10y+
2 + 10y−
2 | y1 + y+
2 −y−
2 = ξ + x1−
2x2, y1 ≤2, y ≥0}
s. t. x1 + x2 = 1,
x ≥0,
(4.5)


## Page 162

4.4 The Relationship between EVPI and VSS
143
where the random variable ξ follows a uniform density over [1,3]. For a
given x and ξ, we may conclude that
y∗(x, ξ) =



y1 = ξ + x1 −2x2, y2 = 0
if 0 ≤ξ + x1 −2x2 ≤2,
y1 = 2, y+
2 = ξ + x1 −2x2 −2
if
ξ + x1 −2x2 > 2,
y−
2 = 2x2 −ξ −x1
if
ξ + x1 −2x2 < 0,
so that
z(x, ξ) =
 2x1 + 2x2 + ξ
if 0 ≤ξ + x1 −2x2 ≤2,
−18 + 11x1 −16x2 + 10ξ
if
ξ + x1 −2x2 > 2,
−9x1 + 24x2 −10ξ
if
ξ + x1 −2x2 < 0.
Given the ﬁrst-stage constraint x1 + x2 = 1, one has z(x, ξ) = 2 + ξ in
the ﬁrst of these three regions. Now, using the ﬁrst-stage constraint and
the deﬁnition of the regions, one can easily check that z(x, ξ) ≥2 + ξ in
the other two regions. Hence, any ˆx ∈{(x1, x2)|x1 + x2 = 1, x ≥0} is an
optimal solution of (4.5) for −x1 + 2x2 ≤ξ ≤2 −x1 + 2x2, or equivalently
for 2 −3x1 ≤ξ ≤4 −3x1.
In particular,
 1
3, 2
3

is optimal for all ξ, (0, 1) is optimal for all ξ ∈[2, 3],
and (1, 0) is optimal for ξ = {1}.
Taking ¯x(ξ) =
 1
3, 2
3

for all ξ leads to the conclusion that ¯x(ξ) is identical
for all ξ, hence WS = RP = 4, so that EVPI = 0. On the other hand, solving
z(x, ¯ξ = 2) may yield a diﬀerent solution, for example, ¯x(2) = (0, 1), with
EV = 4 .
In that case,
EEV = Eξ≤2(24 −10ξ) + Eξ≥2(2 + ξ) = 27
4 ,
so that VSS = 11/4.
Because linear programs often include multiple optimal solutions, this
type of situation is far from exceptional.
b. V SS = O and EV PI̸ = O
We consider the same function z(x, ξ) with ξ ∈

0, 3
2, 3

, with each event
occurring with probability 1/3.
For ξ = 0, ¯x(0) =

x|x1 + x2 = 1, 2
3 ≤x1 ≤1

.
For ξ = 3/2, ¯x(3/2) = {x|x1 + x2 = 1, 1/6 ≤x1 ≤5/6}.
For ξ = 3, ¯x(3) = {x|x1 + x2 = 1, 0 ≤x1 ≤1/3}.
Let us take ¯x(3/2) = (2/3, 1/3). Then EV = z(¯x, 3/2) = 2 + 3/2 = 7/2,
and EEV = 2 + 1
3

0 + 3
2 + 12

= 2 + 13
2 = 13/2.
No single decision is optimal for the three cases, so we expect EVPI to
be nonzero. In the wait-and-see solution, it is possible for all three cases to
take a diﬀerent optimal solution, such as ¯x(0) = (1, 0), ¯x(3/2) = (1/2, 1/2),


## Page 163

144
4. The Value of Information and the Stochastic Solution
and ¯x(3) = (0, 1), yielding
WS = 1
3(1 + 1) + 1
3
5
2 + 1

+ 1
3(4 + 1)
= 2
3 + 7
6 + 5
3 = 21
6 = 7
2.
The recourse solution is obtained by solving the stochastic program
min Eξ(z(x,ξ)), which yields x∗= (2/3, 1/3) with the RP value equal to
the EEV value. Hence,
EV = WS = 7/2 ≤RP = 13/2 = EEV,
which means EV PI = 3 while V SS = 0.
4.5
Examples
There has always been a strong interest in trying to have a better under-
standing of when the EVPI and VSS take large values and when they take
low values. A deﬁnite answer to this question would greatly simplify the
practice of stochastic programming. Only those programs with large EVPI
or VSS would require the solution of a stochastic program. Interested read-
ers may ﬁnd detailed examples in the ﬁeld of energy policy and exhaustible
resources. Manne [1974] provides an example where EVPI is low, while H.P.
Chao [1981] elaborates general conditions for EVPI to be low on a resource
exhaustion model. By introducing other types of uncertainty, Louveaux
and Smeers [1997] and Birge [1988a] show related examples where EVPI
and/or VSS is large.
In this section, we provide simple examples to show that no general
answer is available. It is usually felt that using stochastic programming is
more relevant when there is more randomness in the problem. To translate
this feeling in a more precise statement, we would, for example, expect that
for a given problem, EVPI and VSS would increase when the variances of
the random variables increase. In the following example, we show that this
may or may not be the case.
Example 1
Let ξ be a single random variable taking the two values ξ1 and ξ2, with
probability p1 and p2, respectively, where p2 = 1 −p1. Let ¯ξ = E[ξ] = 1/2.
Let x be a single decision variable. Consider the recourse problem:
min 6x + 10Eξ|x −ξ|
s. t. x ≥0 .


## Page 164

4.6 Bounds on EVPI and VSS
145
(a) Let ξ1 = 1/3, ξ2 = 2/3, p1 = p2 = 1/2 serve as reference. We
compute EVPI =2/3 and VSS=1. We also observe that the vari-
ance, Var (ξ) = 1/36.
(b) Consider the case ξ1 = 0, ξ2 = 1 again with equal probability
1/2 (and unchanged expectation). The variance Var (ξ) is now
1/4, 9 times higher. We now obtain EVPI = 2 and VSS = 3,
showing an example where both values clearly increase with the
variance of ξ.
(c) Consider the case ξ1 = 0, ξ2 = 5/8 with probability p1 = 0.2
and p2 = 0.8, respectively. Again, ¯ξ = 0.5. Now, Var (ξ) = 1/16,
larger than in (a). We obtain EV PI = 2, larger than in (a) but
V SS = 0. Knowing this result in advance would mean that the
solution of the deterministic problem with ¯ξ = Eξ delivers the
optimal solution (although EVPI is three times larger than in
(a)).
(d) Consider the case ξ1 = 0.4, ξ2 = 0.8 with p1 = 0.75 and p2 =
0.25, always with ¯ξ = 0.5. Now, Var (ξ) = 0.03, slightly larger
than in (a). We now observe EV PI = 0.4 and V SS = 1.1,
namely the opposite behavior from (c), a decrease in EVPI and
an increase in VSS.
(e) It is also felt that a more “diﬃcult” stochastic program would
induce higher EVPI and VSS. One such case would be to have
integer decision variables instead of continuous ones. Exercise 3
of Section 1.1, shows that, with ﬁrst-stage integer variables, the
farming problem sees that VSS remains almost unchanged while
EVPI even decreases. On the other hand, Exercise 4 of that sec-
tion shows that with second-stage integer variables, both EVPI
and VSS strongly increase. It would probably not be diﬃcult to
reach diﬀerent conclusions by suitably changing the data.
We may conclude from these simple examples that a general rule is unlikely
to be found. One alternative to such a rule is to consider bounds on the
information and solution value quantities that require less than complete
solutions. We discuss these bounds in the next section.
4.6
Bounds on EVPI and VSS
Bounds on EVPI and VSS rely on constructing intervals for the expected
value of solutions of linear programs representing WS, RP, and EEV. The
simplest bounds stem from the inequalities in Proposition 5. The EVPI
bound was suggested in Avriel and Williams [1970] while the VSS form ap-
pears in Birge [1982]. Many other bounds are possible with diﬀerent limits


## Page 165

146
4. The Value of Information and the Stochastic Solution
on the deﬁning quantities. In the remainder of this section, we consider re-
ﬁned bounds that particularly address the value of the stochastic solution.
More general approaches to bound expectations of value functions appear
in Chapter 9.
The VSS bounds were developed in Birge [1982]. To ﬁnd them, we con-
sider a simpliﬁed version of the stochastic program, where only the right-
hand side is stochastic (ξ = h(ω)) and Ξ is ﬁnite. Let ξ1, ξ2, . . . , ξK index
the possible realizations of ξ, and pk, k = 1, . . . , K be their probabilities. It
is customary to refer to each realization ξk of ξ as a scenario k.
To reﬁne the bounds on VSS, we consider a reference scenario, say ξr.
Two classical reference scenarios are ¯ξ, the expected value of ξ, or the
worst-case scenario (for example, the one with the highest demand level for
problems when costs have to be minimized under the restriction that de-
mand must be satisﬁed). Note that in both situations the reference scenario
may not correspond to any of the possible scenarios in Ξ. This is obvious
for ¯ξ. The worst-case scenario is, however, a possible scenario when, for ex-
ample, ξ is formed by components that are independent random variables.
If the random variables are not independent, then a meaningful worst-case
scenario may be more diﬃcult to construct. Let pr = P(ξ = ξr) be the
reference scenario’s probability.
The PAIRS subproblem of ξr and ξk is deﬁned as
min zP (x, ξr, ξk) = cT x + prqT y(ξr) + (1 −pr)qT y(ξk)
s.t. Ax = b,
Wy(ξr) = ξr −Tx,
Wy(ξk) = ξk −Tx,
x, y ≥0.
Let (¯xk, ¯yk, y(ξk)) denote an optimal solution to the PAIRS subproblem
and zk the optimal objective value zP (¯xk, ¯yk, y(ξk)). We may see the PAIRS
subproblem as a stochastic programming problem with two possible real-
izations ξr and ξk, with probability pr and 1 −pr, respectively.
Two particular cases of the pairs subproblem are of interest. First, ob-
serve that zP (x, ξr, ξr) is well-deﬁned and is in fact z(x, ξr), the deter-
ministic problem for which the only scenario is the reference scenario.
Next, observe that if the reference scenario is not a possible scenario,
pr = P(ξ = ξr) = 0, then zP (x, ξr, ξk) becomes simply z(x, ξk).
We now show the relations between the pairs subproblems and the re-
course problem. To do this, we deﬁne the sum of pairs expected values,
denoted by SPEV, to be
SPEV =
1
1 −pr
K

k=1
pk min zP (x, ξr, ξk).


## Page 166

4.6 Bounds on EVPI and VSS
147
Again, observe that this deﬁnition still makes sense when scenario r is not
possible. In that case, however, it is not really a new concept.
Proposition 6. When the reference scenario is not in Ξ, then SPEV =
WS.
Proof:
As we observed before, when pr = 0, the pairs subproblems
zP (x, ξr, ξk) coincide with z(x, ξk). Hence, SPEV =
K

k=1
k̸=r
pk min z(x, ξk),
which by deﬁnition (1.2) is WS.
In general, the SPEV is related to WS and RP as follows.
Proposition 7. WS ≤SPEV ≤RP.
Proof:
Let us ﬁrst prove the ﬁrst inequality. By deﬁnition,
SPEV =
K

k=1
k̸=r
pk (cT ¯xk + prqT ¯yk + (1 −pr)qT y(ξk))
1 −pr
,
where (¯xk, ¯yk, y(ξk)) is a solution to the pairs subproblem of ξr and ξk. By
the constraint deﬁnition in the pairs subproblem, the solution (¯xk, ¯yk) is
feasible for the problem z(x, ξr) so that
cT ¯xk + qT ¯yk ≥min z(x, ξr) = z∗
r.
Weighting cT xk with a pr and a (1 −pr) term, we obtain:
SPEV =
K

k=1
k̸=r
pk[pr(cT ¯xk + qT ¯yk) + (1 −pr)(cT ¯xk + qT y(ξk))]
1 −pr
,
which, by the property just given, is bounded by
SPEV ≥

k̸=r
pk · pr · z∗
r
1 −pr
+

k̸=r
pk(cT ¯xk + qT y(ξk)).
Now, we simplify the ﬁrst term and bound cT ¯xk + qT y(ξk) by z∗
k in the
second term, because (¯x, y(ξk)) is feasible for min z(x, ξk) = z∗
k. Thus,
SPEV ≥prz∗
r +

k̸=r
pkzk∗= WS.
For the second inequality, let x∗, y∗(ξk), k = 1, . . . , K, be an optimal solu-
tion to the recourse problem. For simplicity, we assume here that r ∈Ξ.


## Page 167

148
4. The Value of Information and the Stochastic Solution
By the constraint deﬁnitions, (x∗, y∗(ξr), y∗(ξk)) is feasible for the PAIRS
subproblem of ξr and ξk. This implies
cT ¯xk + prqT ¯yk + (1 −pr)qT y(ξk) ≤cT x∗+ prqT y∗(ξr) + (1 −pr)qT y∗(ξk).
If we take the weighted sums of these inequalities for all k̸ = r, with pk
as the weight of the kth inequality, the weighted sum of the left-hand side
elements is, by deﬁnition, equal to (1 −pr) · SPEV and the weighted sum
of the right-hand side elements is
K

k=1
k̸=r
pk(cT x∗+ prqT y∗(ξr) + (1 −pr)qT y∗(ξk))
= (1 −pr)

cT x∗+ prqT y∗(ξr) +

k̸=r
pkqT y∗(ξk)


= (1 −pr)
"
cT x∗+
K

k=1
pkqT y∗(ξk)
#
= (1 −pr)RP,
which proves the desired inequality.
To obtain upper bounds on RP that relate to the pairs subproblem,
we generalize the VSS deﬁnition. Let z(x, ξr) be the deterministic problem
associated with scenario ξr (remember ξr need not necessarily be a possible
scenario) and ¯xr an optimal solution to minx z(x, ξr). We may then deﬁne
the expected value of the reference scenario,
EV RS = Eξz(¯xr,ξ),
and the value of a stochastic solution to be
V SS = EV RS −RP.
Note that V SS is still nonnegative, because ¯xr is either a feasible solution
to the recourse problem and EV RS ≥RP or an infeasible solution so that
EV RS = +∞.
Now, as before, let (¯xk, ¯yk, y(ξk)) be optimal solutions to the pairs sub-
problem of ξr and ξk, k = 1, . . . , K. Deﬁne the expectations of pairs ex-
pected value to be
EPEV =
min
k=1,...,K∪{r} Eξz(¯xk,ξ).
Proposition 8. RP ≤EPEV ≤EV RS.
Proof:
The three values are the optimal value of the recourse function
minx Eξz(x,ξ) over smaller and smaller feasibility sets: the ﬁrst one over


## Page 168

4.6 Bounds on EVPI and VSS
149
all feasible x in K1 ∩K2, the second one over x ∈K1 ∩K2 ∩{¯xk, k =
1, . . . , K ∪{r}}, and the third one over ¯xr ∩K1 ∩K2.
Putting these two propositions together, one obtains the following theo-
rem.
Theorem 9. 0 ≤EV RS −EPEV ≤V SS ≤EV RS −SPEV ≤EV RS −
WS.
We apply these concepts in the following example.
Example 2
Consider the problem to ﬁnd:
min 3x1 + 2x2 + Eξ min(−15y1 −12y2)
s.t. 3y1 + 2y2 ≤x1,
2y1 + 5y2 ≤x2,
.8ξ1 ≤y1 ≤ξ1,
.8ξ2 ≤y2 ≤ξ2,
x, y ≥0,
where ξ1 = 4 or 6 and ξ2 = 4 or 8, independently of each other, with
probability 1/2 each.
This example can be seen as an investment decision in two resources x1
and x2, which are needed in the second-stage problem to cover at least
80% of the demand. In this situation, the EEV and WS answers are totally
inconclusive.
Table 1 gives the various solutions under the four scenarios, the optimal
objective values under these scenarios and the WS value. It also describes
the EV value under the expected value scenario ¯ξ = (5, 6)T . Note that
this scenario is not one of those possible. The optimal solution ¯x(¯ξ) =
(24.6, 34)T is infeasible for the stochastic problem so that EEV is set to be
+∞.
It follows from Table 1 that EV = WS = 9.2 ≤RP ≤EEV = +∞.
This relation is of no help: we can only conclude from it that EVPI is
somewhere between 0 and +∞, and so is VSS. These statements could
have been made without any computation.
It is in such situations that the pairs subproblems are of great interest.
Because the problem under consideration is an investment problem with
demand satisfaction constraints, the most logical reference scenario corre-
sponds to the largest demand, ξr = (6, 8)T , and not to the mean demand
¯ξ.
This will force the ﬁrst-stage decisions to take demand satisfaction under
the maximal demand into consideration, so that decisions taken under the


## Page 169

150
4. The Value of Information and the Stochastic Solution
TABLE 1. Solutions and optimal values under the four scenarios and the expected
value scenario.
Scenario
First-Stage Second-Stage
Optimal Value
Solution
Solution
z(¯x(ξ), ξ)
1. (4,4)
(18.4, 24)
(4, 3.2)
4.8
2. (6,4)
(24.4, 28)
(6, 3.2)
0.8
3. (4,8)
(24.8, 40)
(4, 6.4)
17.6
4. (6,8)
(30.8, 44)
(6, 6.4)
13.6
WS = 9.2
¯ξ = (5, 6)
(24.6, 34)
(5, 4.8)
EV = 9.2
EEV = +∞
pairs subproblem are feasible for the recourse problem. Due to indepen-
dence, ξr is one of the possible realizations of ξ, with pr = 1/4.
The PAIRS subproblems of ξr and ξk are
min 3x1 + 2x2 −1
4(15yr
1 + 12yr
2) −3
4(15y1 + 12y2)
s.t.
x1 ≥27.2,
3yr
1 + 2yr
2 ≤x1,
3y1 + 2y2 ≤x1,
x2 ≥41.6,
2yr
1 + 5yr
2 ≤x2,
2y1 + 5y2 ≤x2,
4.8 ≤yr
1 ≤6,
.8ξk
1 ≤y1 ≤ξk
1,
6.4 ≤yr
2 ≤8,
.8ξk
2 ≤y2 ≤ξk
2,
y ≥0.
The bounds on x1 and x2 are induced by the feasibility for the reference
scenarios.
Table 2 gives the solutions of the pairs subproblems for the three sce-
narios (other than the reference scenario), the SPEV, the EVRS and the
EPEV values.
This time, the relations one can derive from this table are strongly
conclusive:
WS = 9.2 ≤SPEV = 30.94 ≤RP ≤EPEV = 30.94 ≤EV RS = 40.6
implies RP = 30.94 and (27.2, 41.6)T is an optimal solution.
Exercises
1. Show that Proposition 1 still holds if some of the x and/or y must be
integer.


## Page 170

4.6 Bounds on EVPI and VSS
151
TABLE 2. Pairs subproblems solutions.
Pairs
First-Stage Second-Stage
Second-Stage
Objective
Subproblem
Solution
under
under
Value zP
Reference Sc.
ξk
1. (4,4), r
(27.2, 41.6)
(4.8, 6.4)
(4,4)
46.6
2. (6,4), r
(27.2, 41.6)
(4.8, 6.4)
(6,4)
24.1
3. (4,8), r
(27.2, 41.6)
(4.8, 6.4)
(4, 6.72)
22.12
SPEV = 30.94
EPEV = mink Eξz(¯x(ξk),ξ) = Eξz(27.2, 41.6,ξ)
= 30.94
EVRS = Eξz((30.8, 44), ξ) = 40.6
2. Consider Example 3.1 with a single ﬁrst-stage decision x and
Q(x,ξ) = min{2y1 + y2|y1 ≥x −ξ, y2 ≥ξ −x, y ≥0, integer }
with ξ = 1 or 2 with probability of 1/2 each. Show:
(a) If x must be integer, then EV > WS for any value of c ≥0.
(b) If x is continuous, then EV = WS for 0 ≤c ≤1 and EV > WS
for c > 1. Beware that y is always integer, the discussion is on
x being integer or not.
3. Consider the following stochastic program
min
x≥0 2x + Eξ{ξ · y | y ≥1 −x, y ≥0},
and ξ takes on values 1 and 3 with probability 3/4 and 1/4, respec-
tively. Show that in this case EV > WS.
4. Consider the following two-stage program:
min 2x1 + x2 + Eξ(−3y1 −4y2|y1 + 2y2 ≥ξ1, y1 ≤x1 ,
y2 ≤x2, y2 ≤ξ2, y ≥0)
s.t. x1 + x2 ≤7, x1, x2 ≥0,
where ξ can take the values
 3
2

,
 5
3

,
 7
3

with probability 1/3 each.
(a) Choose the scenario
 7
3

as the reference scenario. Deﬁne the
problem z(x,ξ) for this reference scenario. Its optimal solution
gives the optimal ﬁrst-stage decision x1 = 4, x2 = 3. Compute
the EVRS value.
(b) State the pairs subproblem for
 3
2

and the reference scenario.


## Page 171

152
4. The Value of Information and the Stochastic Solution
(c) The solution of the pairs subproblem for
 3
2

and the reference
scenario has ﬁrst-stage optimal solutions x1 = 5, x2 = 2; the so-
lution of the pairs subproblem for
 5
3

and the reference scenario
has ﬁrst-stage optimal solutions x1 = 4, x2 = 3. Compute the
values of the two pairs subproblems. Compute the SPEV value.
What relation holds for the recourse problem value?
5. Adapt the proofs in Proposition 7 for the case where r̸ ∈Ξ.


## Page 172

Part III
Solution Methods
153


## Page 173



## Page 174

5
Two-Stage Linear Recourse
Problems
Computation in stochastic programs with recourse has focused on two-stage
problems with ﬁnite numbers of realizations. This problem was introduced
in the farming example of Chapter 1. As we saw in the capacity expan-
sion model, this problem can also represent multiple stages of decisions
with block separable recourse and it provides a foundation for multistage
methods. The two-stage problem is, therefore, our primary model for com-
putation.
The general model is to choose some initial decision that minimizes cur-
rent costs plus the expected value of future recourse actions. With a ﬁnite
number of second-stage realizations and all linear functions, we can always
form the full deterministic equivalent linear program or extensive form.
With many realizations, this form of the problem becomes quite large.
Methods that ignore the special structure of stochastic linear programs be-
come quite ineﬃcient (as some of the results in Section 3 show). Taking
advantage of structure is especially beneﬁcial in stochastic programs and
is the focus of much of the algorithmic work in this area.
The method used most frequently is based on building an outer lineariza-
tion of the recourse cost function and a solution of the ﬁrst-stage problem
plus this linearization. This cutting plane technique is called the L-shaped
method in stochastic programming. Section 1 describes the basic L-shaped
method in some detail, while Sections 2 to 4 continue this development
with a discussion of enhancements of the L-shaped method in terms of
feasibility, multicuts, and bunching of realizations.
Several variants and extensions of the L-shaped method have been de-
signed. Variants adding nonlinear regularized terms will be studied in Chap-


## Page 175

156
5. Two-Stage Linear Recourse Problems
ter 6. Bounding techniques will be considered in Chapter 9. The use of
sampling will be studied in Chapter 10.
The remainder of this chapter discusses alternative algorithms. In Section
5, we will discuss alternative decomposition procedures. The ﬁrst method
is an inner linearization, or Dantzig-Wolfe decomposition approach, that
solves the dual of the L-shaped method problem. The other approach is a
primal form of inner linearization based on generalized programming.
Section 6 will consider direct approaches to the extensive form through
eﬃcient extreme point and interior point methods. We discuss basis fac-
torization and its relationship to decomposition methods. We also present
interior point approaches and the use of a special stochastic programming
structure for these algorithms.
Additional problem structures can be of further beneﬁt for solving two-
stage stochastic linear programs. These structures are generally based on
the form of the recourse function. Section 7 will discuss methods for the
generalizations of the news vendor problem called simple recourse problems
and problems involving networks.
5.1
The L-Shaped Method
Consider the general formulation in (3.1.2) or (3.1.5). The basic idea of the
L-shaped method is to approximate the nonlinear term in the objective of
these problems. A general principle behind this approach is that, because
the nonlinear objective term (the recourse function) involves a solution of
all second-stage recourse linear programs, we want to avoid numerous func-
tion evaluations for it. We therefore use that term to build a master problem
in x, but we only evaluate the recourse function exactly as a subproblem.
To make this approach possible, we assume that the random vector ξ
has ﬁnite support. Let k = 1, . . . , K index its possible realizations and
let pk be their probabilities. Under this assumption, we may now write
the deterministic equivalent program in the extensive form. This form is
created by associating one set of second-stage decisions, say, yk, to each
realization ξ, i.e., to each realization of qk, hk, and Tk. It is a large-scale
linear problem that we can deﬁne as the extensive form (EF):
(EF)
min cT x +
K

k=1
pkqT
k yk
(1.1)
s.t. Ax = b,
Tkx + Wyk = hk,
k = 1, . . . , K;
x ≥0,
yk ≥0,
k = 1, . . . , K.
An example of an extensive form has been given for the farmer’s problem
in Chapter 1 (model (1.1.2)).
The block structure of the extensive form appears in Figure 1.


## Page 176

5.1 The L-Shaped Method
157
FIGURE 1. Block structure of the two-stage extensive form.
This picture has given rise to the name, L-shaped method for the following
algorithm. Taking the dual of the extensive form, one obtains a dual block-
angular structure, as in Figure 2. Therefore it seems natural to exploit
this dual structure by performing a Dantzig-Wolfe [1960] decomposition
(inner linearization) of the dual or a Benders [1962] decomposition (outer
linearization) of the primal. This method has been extended in stochastic
programming to take care of feasibility questions and is known as Van Slyke
and Wets’s [1969] L-shaped method. It proceeds as follows.
FIGURE 2. Block angular structure of the two-stage dual.
L-Shaped Algorithm
Step 0. Set r = s = ν = 0.
Step 1. Set ν = ν + 1. Solve the linear program (1.2)–(1.4).
min z = cT x + θ
(1.2)
s.t. Ax = b,
Dℓx ≥dℓ,
ℓ= 1, . . . , r,
(1.3)
Eℓx + θ ≥eℓ,
ℓ= 1, . . . , s,
(1.4)
x ≥0,
θ ∈ℜ.


## Page 177

158
5. Two-Stage Linear Recourse Problems
Let (xν, θν) be an optimal solution. If no constraint (1.4) is present, θν is
set equal to −∞and is not considered in the computation of xν.
Step 2. For k = 1, . . . , K solve the linear program
min w′ = eT v+ + eT v−
(1.5)
s.t. Wy + Iv+ −Iv−= hk −Tkxν,
(1.6)
y ≥0,
v+ ≥0,
v−≥0,
where eT = (1, . . . , 1), until, for some k, the optimal value w′ > 0. In this
case, let σν be the associated simplex multipliers and deﬁne
Dr+1 = (σν)T Tk
(1.7)
and
dr+1 = (σν)T hk
(1.8)
to generate a constraint (called a feasibility cut) of type (1.3). Set r = r+1,
add to the constraint set (1.3), and return to Step 1. If for all k, w′ = 0,
go to Step 3.
Step 3. For k = 1, . . . , K solve the linear program
min w = qT
k y
(1.9)
s.t. Wy = hk −Tkxν,
y ≥0.
Let πν
k be the simplex multipliers associated with the optimal solution of
Problem k of type (1.9). Deﬁne
Es+1 =
K

k=1
pk · (πν
k)T Tk
(1.10)
and
es+1 =
K

k=1
pk · (πν
k)T hk.
(1.11)
Let wν = es+1 −Es+1xν. If θν ≥wν, stop; xν is an optimal solution.
Otherwise, set s = s+1, add to the constraint set (1.4), and return to Step
1.
The method consists of solving an approximation of (3.1.2) by using an
outer linearization of Q. Two types of constraints are sequentially added: (i)
feasibility cuts (1.3) determining {x|Q(x) < +∞} and (ii) optimality cuts
(1.4), which are linear approximations to Q on its domain of ﬁniteness. We
ﬁrst illustrate the optimality cuts.


## Page 178

5.1 The L-Shaped Method
159
Example 1
Let
Q(x, ξ) =

ξ −x
if x ≤ξ,
x −ξ
if x ≥ξ,
and let ξ take on the values 1, 2, and 4, each with probability 1/3. Assume
also c = 0 and 0 ≤x ≤10.
Figure 3 represents the functions Q(x, 1), Q(x, 2), Q(x, 4) and Q(x). As
indicated in Theorem 3.5, each of these functions is polyhedral. Because
the ﬁrst-stage objective cT x is zero, Q(x) is also the function z(x) to be
minimized. Assume the starting point is x1 = 0. The sequence of iterations
for the L-shaped method is as follows.
Iteration 1:
x1 is not optimal; send the cut
θ ≥7/3 −x.
Iteration 2:
x2 = 10, θ2 = −23/3 is not optimal; send the cut
θ ≥x −7/3.
Iteration 3:
x3 = 7/3, θ3 = 0 is not optimal; send the cut
θ ≥x + 1
3
.
Iteration 4:
x4 = 1.5, θ4 = 2.5/3 is not optimal; send the cut
θ ≥5 −x
3
.
Iteration 5:
x5 = 2, θ5 = 1, which is the optimal solution.
We now constructively prove that constraints of the type (1.4) deﬁned in
Step 3 are supporting hyperplanes of Q(x) and that the algorithm will
converge to an optimal solution, provided the constraints (1.3) adequately
deﬁne feasible points of K2. (This last provision will be taken care of later
in this section.)
First, observe that solving (3.1.2), namely,
min cT x + Q(x)
(1.12)


## Page 179

160
5. Two-Stage Linear Recourse Problems
FIGURE 3. Recourse functions for Example 1.


## Page 180

5.1 The L-Shaped Method
161
s. t. x ∈K1 ∩K2,
is equivalent to solving
min cT x + θ
(1.13)
Q(x) ≤θ,
s. t. x ∈K1 ∩K2,
where, in both problems, Q(x) is deﬁned as in (3.1.3),
Q(x) = EωQ(x, ξ(ω))
and
Q(x, ξ(ω)) = min
y {q(ω)T y|Wy = h(ω) −T(ω)x, y ≥0}
as in (3.1.4).
We are thus looking for a ﬁnitely convergent algorithm for solving (1.12)
or (1.13).
In Step 3 of the algorithm, problem (1.9) is solved repeatedly for each
k = 1, . . . , K, yielding optimal simplex multipliers πν
k, k = 1, . . . , K. It
follows from duality in linear programming that, for each k,
Q(xν, ξk) = (πν
k)T (hk −Tkxν).
Moreover, by convexity of Q(x, ξk), it follows from the subgradient inequal-
ity that
Q(x, ξk) ≥(πν
k)T hk −(πν
k)T Tkx.
We may now take the expectation of these two relations to obtain
Q(xν) = E(πν)T (h −Txν) =
K

k=1
pk · (πν
k)T (hk −Tkxν)
and
Q(x) ≥E(πν)T (h −Tx) =
K

k=1
pk(πν
k)T hk −
$ K

k=1
pk(πν
k)T Tk
%
x,
respectively. By θ ≥Q(x), it follows that a pair (x, θ) is feasible for (1.13)
only if θ ≥E(πν)T (h −Tx), which corresponds to (1.4) where Eℓand eℓ
are deﬁned in (1.10) and (1.11).
On the other hand, if (xν, θν) is optimal for (1.13), it follows that
Q(xν) = θν, because θ is unrestricted in (1.13) except for θ ≥Q(x). This
happens when θν = E(πν)T (h −Txν), which justiﬁes the termination cri-
terion in Step 3.
This means that at each iteration either θν ≥Q(xν) implying termina-
tion or θν < Q(xν). In the latter case, none of the already deﬁned opti-
mality cuts (1.4) adequately imposes θ ≥Q(x), so a new set of multipliers


## Page 181

162
5. Two-Stage Linear Recourse Problems
πν
k will be deﬁned at xν to generate an appropriate constraint (1.4). The
ﬁnite convergence of the algorithm follows from the fact that there is only
a ﬁnite number of diﬀerent combinations of the K multipliers πk, because
each corresponds to one of the ﬁnitely many diﬀerent bases of (1.9).
An alternative proof of convergence could be obtained by showing that
Step 3 coincides with an iteration of the subproblems in the Dantzig-Wolfe
decomposition of the dual of (1.12) while Step 1 coincides with the master
problem. We will consider this approach in Section 5.
We now have to prove that at most a ﬁnite number of constraints (1.3)
is needed to guarantee x ∈K2. Constraints (1.3) are generated in Step 2
of the algorithm.
By deﬁnition, x ∈K2 is equivalent to
x ∈{x| for k = 1, . . . , K, ∃y ≥0 s.t. Wy = hk −Tkx}.
Referring to a previously introduced notation, this means
hk −Tkx ∈pos W, for k = 1, . . . , K.
In Step 2, a subproblem (1.5) is solved that tests whether hk −Tkxν
belongs to pos W for k = 1, . . . , K. If not, this means that for some
k = 1, . . . , K, hk −Tkxν̸ ∈pos W. Then, there must be a hyperplane
separating hk −Tkxν and pos W. This hyperplane must satisfy σT t ≤0 for
all t ∈pos W and σT (hk−Tkxν) > 0. In Step 2, this hyperplane is obtained
by taking σ for the value σν of the simplex multipliers of the subproblem
(1.5) solved in Step 2.
By duality, w′ being strictly positive is the same as (σν)T (hk−Tkxν) > 0.
Also, (σν)T W ≤0 is satisﬁed because σν is an optimal simplex multiplier
and, at the optimum, the reduced costs associated with y must be non-
negative.
Therefore, σν has the desired property. A necessary condition for x be-
longing to K2 is that (σν)T (hk −Tkx) ≤0. There is at most a ﬁnite number
of such constraints (1.3) because there are only a ﬁnite number of optimal
bases to the problem (1.5) solved in Step 2. This is no surprise because we
already know from Theorem 3.5 that K2 is polyhedral when ξ is a ﬁnite
random variable. We thus have proved the following theorem.
Theorem 1. When ξ is a ﬁnite random variable, the L-shaped algorithm
ﬁnitely converges to an optimal solution when it exists or proves the infea-
sibility of problem (1.12).


## Page 182

5.2 Feasibility
163
To illustrate the feasibility cuts, consider Example 4.2:
min
3x1 + 2x2 =Eξ(15y1 + 12y2)
s.t. 3y1 + 2y2 ≤x1,
2y1 + 5y2 ≤x2,
.8ξ1 ≤y1 ≤ξ1,
.8ξ2 ≤y2 ≤ξ2,
x, y ≥0,
with ξ1 = 4 or 6 and ξ2 = 4 or 8, independently, with probability 1/2 each
and ξ = (ξ1,ξ2)T .
To keep the discussion short, assume the ﬁrst considered realization of
ξ is (6, 8)T . If not, many cuts would be needed. Starting from an initial
solution x0 = (0, 0)T , a ﬁrst feasibility cut 3x1 + x2 ≥123.2 is generated.
The ﬁrst-stage solution is then x1 = (41.067, 0)T . A second feasibility cut
is x2 ≥22.4. The ﬁrst-stage solution becomes x2 = (33.6, 22.4)T . A third
feasibility cut x2 ≥41.6 is generated. The ﬁrst-stage solution is
x3 = (27.2, 41.6)T ,
which yields feasible second-stage decisions.
This example also illustrates that generating feasibility cuts by a mere
application of Step 2 of the L-shaped method may not be eﬃcient. Indeed,
a simple look at the problem reveals that, for feasibility when ξ1 = 6 and
ξ2 = 8, it is at least necessary to have y1 ≥4.8 and y2 ≥6.4, which in
turn implies x1 ≥27.2 and x2 ≥41.6. We may then consider the following
program as a reasonable initial problem:
min 3x1 + 2x2 + Q(x)
s.t. x1 ≥27.2,
x2 ≥41.6,
which immediately appears to be feasible. Such situations frequently occur
in practice. More is said about these circumstances in the next section.
5.2
Feasibility
As indicated in the previous section, Step 2 of the L-shaped method consists
of determining whether a ﬁrst-stage decision x ∈K1 is also second-stage
feasible, i.e., x ∈K2. This step may be extremely time-consuming. It may
require the solution of up to K phase-one problems of the form (1.5)–(1.6).
The process may have to be repeated several times for successive candidate
ﬁrst-stage solutions.


## Page 183

164
5. Two-Stage Linear Recourse Problems
In some cases, Step 2 can be simpliﬁed. A ﬁrst case is when the sec-
ond stage is always feasible. The stochastic program is then said to have
complete recourse. Let, as in (1.1), the second-stage constraint be:
Wy = h −Tx, y ≥0.
We repeat here the deﬁnition given in Section 3.1d for complete recourse
for convenience.
Deﬁnition. A stochastic program is said to have complete recourse when
pos W = ℜm2. It is said to have relatively complete recourse when K2 ⊇K1,
i.e., x ∈K1 implies h −Tx ∈pos W for any h, T realization of h, T.
If we consider the farmer’s problem in Section 1.1, program (1.1.2) has
complete recourse. The second stage just serves as a measure of the cost to
the farmer of the decisions taken. Any lack of production can be covered
by a purchase. Any production in excess can be sold. If we consider the
power generation model (1.3.6), it has complete recourse if there exists at
least one technology with zero lead time (∆i = 0). If the demand in a
given period t exceeds what can be delivered by the available equipment,
an investment is made in this (usually expensive) technology to cover the
needed demand.
A second case is when it is possible to derive some constraints that have
to be satisﬁed to guarantee second-stage feasibility. These constraints are
sometimes called induced constraints. They can be obtained from a good
understanding of the model. A simple look at the second-stage program in
the example of the previous section reveals the conditions for feasibility.
Constraints x1 ≥27.2 and x2 ≥41.6 are examples of induced constraints.
In the power generation model (1.3.6) of Section 1.3, the total possible
demand in a given stage t is obtained from (1.3.8) as
m

j=1
dt
j. The maximal
possible demand in stage t is thus Dt = max
ξ∈Ξ
m

j=1
dt
j. Stage t feasibility will
thus require enough investments in the various technologies to cover the
maximal demand, i.e.,
n

i=1
ai(wt−∆i
i
+ gi) ≥Dt .
Again, with the introduction of these induced constraints, Step 2 of the
L-shaped algorithm can be dropped.
A third case is when Step 2 is not required for all k = 1, · · · , K, but for
one single hk. Assume T is deterministic. Also assume we can transform W
so that for all t ≥0, t ∈pos W. This poses no diﬃculty for inequalities, as
it is just a matter of taking the slack variables with a positive coeﬃcient.
In the example of the previous section, the following representation of W


## Page 184

5.2 Feasibility
165
satisﬁes the desired requirement:
3y1 + 2y2 + w1
= x1,
2y1 + 5y2
+ w2
= x2,
y1
+ w3
= d1,
−y1
+ w4
= −.8d1,
y2
+ w5
= d2,
−y2
+ w6 = −0.8d2.
For any t ≥0, it suﬃces to take w = t to have a second-stage feasible
solution. Assume ﬁrst some lower bound,
b(x) ≤hk −Tkx , k = 1, · · · , K,
exists. Then a suﬃcient condition for x to be feasible is that the linear
system Wy = b(x), y ≥0 is feasible. Indeed, if Wy = b(x), y ≥0 is feasible,
then Wy = b′(x), y ≥0 is feasible for any b′(x) ≥b(x) by construction of
W.
Theorem 2. Assume that W is such that t ∈pos W for all t ≥0. Deﬁne
ai =
min
k=1,···K{hik} to be the componentwise minimum of h. Also assume
there exists one realization hℓ, ℓ∈{1, · · · , K} s.t. a = hℓ. Then, x ∈K2 if
and only if Wy = a −Tx, y ≥0 is feasible.
Proof: This is easily checked,as the condition was just seen to be suﬃcient.
It is also necessary because x ∈K2 only if Wy = a−Tx, y ≥0 is feasible.
Again taking the example of the previous section, we observe that, with
an appropriate choice of W, the vector h = (0, 0, ξ1, −.8ξ1, ξ2, −.8ξ2)T . The
componentwise minimum is a = (0, 0, 4, −4.8, 4, −6.4)T . Unfortunately, no
h coincides with a. The system {y|Wy = a −Tx, y ≥0} is infeasible.
On the other hand, the system is feasible only if 3y1 + 2y2 ≤x1, 2y1 +
5y2 ≤x2, y1 ≥0.8ξ1, y2 ≥0.8ξ2 is feasible (we just drop the upper bounds
on y). This reduced system is feasible if and only if
3y1 + 2y2 ≤x1, 2y1 + 5y2 ≤x2, y1 ≥4.8, y2 ≥6.4,
i.e., if and only if x1 ≥27.2 and x2 ≥41.6, which (as already seen in-
tuitively) is a necessary condition for feasibility. Thus, even if in practice
there does not always exist a realization hℓsuch that a = hℓ, the condition
of Theorem 2 may still be helpful.
Exercises
1. Obtain the feasibility cuts for Example 4.1.
2. Feasibility cuts in Benders decomposition have an equivalent in
Dantzig-Wolfe decomposition. What is it?


## Page 185

166
5. Two-Stage Linear Recourse Problems
5.3
The Multicut Version
In Step 3 of the L-shaped method, all K realizations of the second-stage
program are optimized to obtain their optimal simplex multipliers. These
multipliers are then aggregated in (1.10) and (1.11) to generate one cut
(1.4). The structure of stochastic programs clearly allows placing several
cuts instead of one. In the multicut version, one cut per realization in the
second stage is placed. For those familiar with Dantzig-Wolfe decomposition
(explored more deeply in Section 6), adding multiple cuts at each iteration
corresponds to including several columns in the master program of an inner
linearization algorithm (see, e.g., Lasdon [1970] for a general presentation
and Birge [1985b] for an analysis of the stochastic case).
We ﬁrst give
a presentation of the multicut algorithm, taken from Birge and Louveaux
[1988].
The Multicut L-Shaped Algorithm
Step 0. Set r = ν = 0 and sk = 0 for all k = 1, · · · , K.
Step 1. Set ν = ν + 1. Solve the linear program (3.1)–(3.4)
min z = cT x +
K

k=1
θk
(3.1)
s.t. Ax= b ,
(3.2)
Dℓx≥dℓ, ℓ= 1, · · · , r ,
(3.3)
Eℓ(k)x + θk≥eℓ(k) , ℓ(k) = 1, · · · , s(k),
(3.4)
k = 1, · · · , K ,
x ≥0 ,
Let (xν, θν
1, . . . , θν
K) be an optimal solution of (3.1)–(3.4). If no constraint
(3.4) is present for some k, θν
k is set equal to −∞and is not considered in
the computation of xν.
Step 2. As before.
Step 3. For k = 1, · · · , K solve the linear program (1.9). Let πν
k be the
simplex multipliers associated with the optimal solution of problem k. If
θν
k < pk(πν
k)T (hk −Tkxν),
(3.5)
deﬁne
Es(k)+1 = pk(πν
k)T Tk,
(3.6)
es(k)+1 = pk(πν
k)T hk,
(3.7)
and set s(k) = s(k) + 1. If (3.5) does not hold for any k = 1, · · · , K, stop;
xν is an optimal solution. Otherwise, return to Step 1.


## Page 186

5.3 The Multicut Version
167
We illustrate the multicut L-shaped on Example 1. Starting from x1 = 0,
the sequence of iterations is as follows:
Iteration 1:
x1 is not optimal, send the cuts
θ1 ≥1 −x
3
; θ2 ≥2 −x
3
; θ3 ≥4 −x
3
.
Iteration 2:
x2 = 10, θ2
1 = −3, θ2
2 = −8/3, θ2
3 = −2 is not optimal; send the cuts
θ1 ≥x −1
3
; θ2 ≥x −2
3
; θ3 ≥x −4
3
.
Iteration 3:
x3 = 2, θ3
1 = 1/3, θ3
2 = 0, θ3
3 = 2/3 is the optimal solution.
Let us deﬁne a major iteration to consist of the operations performed be-
tween returns to Step 1 in both algorithms. By sending multiple cuts, a
solution is found in two major iterations instead of four with the single-cut
L-shaped method.
A few observations are necessary. By sending disaggregate cuts, more
detailed information is given to the ﬁrst stage. The number of major iter-
ations is expected then to be less than in the single cut method. Because
the two methods do not necessarily follow the same path, by chance, the
L-shaped method can conceivably do better than the multicut approach.
Exercise 1 provides such an example.
In general, however, as numerical experiments reveal, the number of ma-
jor iterations is reduced. This is done at the expense of a larger ﬁrst-stage
program, because many more cuts are added. The balance between less
major iterations but larger ﬁrst-stage programs is problem-dependent. The
results of numerical experiments are available in Birge and Louveaux [1988]
and Gassmann [1990]. As a rule of thumb, the multicut approach is ex-
pected to be more eﬀective when the number of realizations K is not sig-
niﬁcantly larger than the number of ﬁrst-stage constraints m1.
Finally, some hybrid approach may be worthwhile, where subsets of the
realizations are grouped to form a smaller number of combination cuts.
Exercise 2 provides such an example.
Exercises
1. Assume n1 = 1, m1 = 0, m2 = 3, n2 = 6,
W =


1
−1
−1
−1
0
0
0
1
0
0
1
0
0
0
1
0
0
1

,


## Page 187

168
5. Two-Stage Linear Recourse Problems
and K = 2 realizations of ξ with equal probability 1/2. These
realizations are ξ1 = (q1, h1, T 1)T and ξ2 = (q2, h2, T 2)T , where
q1 = (1, 0, 0, 0, 0, 0)T , q2 = (3/2, 0, 2/7, 1, 0, 0)T , h1 = (−1, 2, 7)T ,
h2 = (0, 2, 7)T , and T 1 = T 2 = (1, 0, 0)T . For the ﬁrst value of
ξ, Q(x, ξ) has two pieces, such that
Q1(x) =

−x −1
if x ≤−1,
0
if x ≥−1.
For the second value of ξ, Q(x, ξ) has four pieces such that
Q2(x) =





−1.5x
if x ≤0,
0
if 0 ≤x ≤2,
2/7(x −2)
if 2 ≤x ≤9,
x −7
if x ≥9.
Assume also that x is bounded by −20 ≤x ≤20 and c = 0. Starting
from any initial point x1 ≤−1, show that one obtains the following
sequence of iterate points and cuts for the L-shaped method.
Iteration 1:
x1 = −2, θ1 is omitted; new cut θ ≥−0.5 −1.25x.
Iteration 2:
x2 = +20, θ2 = −25.5; new cut θ ≥0.5x −3.5.
Iteration 3:
x3 = 12/7, θ3 = −37/14; new cut θ ≥0.
Iteration 4:
x4 ∈[−2/5, 7], θ4 = 0. If x4 is chosen to be any value in [0,2], then
the algorithm terminates at Iteration 4. The multicut approach would
generate the following sequence.
Iteration 1:
x1 = −2, θ1
1 and θ1
2 omitted; new cuts θ1 ≥−0.5x −0.5, θ2 ≥−3/4x.
Iteration 2:
x2 = 20, θ2
1 = −10.5, θ2
2 = −15; new cuts θ1 ≥0, θ2 ≥0.5x −3.5.
Iteration 3:
x3 = 2.8, θ3
1 = 0, θ3
1 = −2.1; new cut θ2 ≥1/7(x −2).


## Page 188

5.4 Bunching and Other Eﬃciencies
169
Iteration 4:
x4 = 0.32, θ4
1 = 0, θ4
2 = −0.24; new cut θ2 ≥0.
Iteration 5:
x5 = 0, θ5
1 = θ5
2 = 0, stop.
2. Consider Example 1, now with ξ taking values:
0.5, 1.0, 1.5 with probability 1/9 each,
2 with probability 1/3,
3, 4, 5 with probability 1/9 each.
As can be seen, the expectation of ξ is still 2, and new uncertainty is
added around 1 and 4.
(a) Show that the L-shaped method follows exactly the same path
as before (x1 = 0, x2 = 10, x3 = 7/3, x4 = 1.5, x5 = 2) provided
that in Iteration 4, the support is chosen to describe the region
[1.5, 2]. If it is chosen to describe the region [1, 1.5], one more
iteration is needed.
(b) Show the multicut version also follows the same path as before
(x1 = 0, x2 = 10, x3 = 2).
(c) Now consider an intermediate situation, where Q(x) is approxi-
mated by 1
3[Q1(x)+Q2(x)+Q3(x)], where Q1(x) is the expecta-
tion over the three realizations 0.5, 1.0, and 1.5 (conditional on
ξ being in the group {0.5, 1.0, 1.5}), Q2(x) = Q(x, ξ = 2), and
Q3(x) is the (similarly conditional) expectation over the realiza-
tions 3, 4, and 5. Thus, the objective becomes 1
3(θ1 + θ2 + θ3).
Show that in Iteration 1, the cuts at x1 = 0 are θ1 ≥1 −x, θ2 ≥
2 −x, and θ3 ≥4 −x. In Iteration 2, x2 = 10, and the cuts
become θ1 ≥x −1, θ2 ≥x −2, and θ3 ≥x −4. Show, without
computations, that only two major iterations are needed. What
conclusions can you draw from this example?
5.4
Bunching and Other Eﬃciencies
One big issue in the eﬃcient implementation of the L-shaped method is
in Step 3. The second-stage program (1.9) has to be solved K times to
obtain the optimal multipliers, πν
k. For a given xν and a given realiza-
tion k, let B be the optimal basis of the second stage. It is well-known


## Page 189

170
5. Two-Stage Linear Recourse Problems
from linear programming that B is a square submatrix of W such that
(πν
k)T = qT
k,BB−1, qT
k −(πν
k)T W ≥0, B−1(hk −Tkxν) ≥0, where qk,B
denotes the restriction of qk to the selection of columns that deﬁne B. Im-
portant savings can be obtained in Step 3 when the same basis B is optimal
for several realizations of k. This is especially the case when q is determin-
istic. Then, two diﬀerent realizations that share the same basis also share
the same multipliers πν
k. We present the rest of the section, assuming q is
deterministic.
To be more precise, deﬁne
τ = {t|t = hk −Tkxν for some k = 1, · · · , K}
(4.1)
as the set of possible right-hand sides in the second stage. Let B be a square
submatrix and πT = qT
BB−1. Assume B satisﬁes the optimality criterion
qT −πT W ≥0. Then deﬁne a bunch as
Bu = {t ∈τ|B−1t ≥0},
(4.2)
the set of possible right-hand sides that satisfy the feasibility condition.
Thus, π is an optimal dual multiplier for all t ∈Bu. Note also that, by
virtue of Step 2 of the L-shaped method, only feasible ﬁrst-stage xν ∈K2
are considered. This observation means that, by construction,
τ ⊆pos W = {t|t = Wy, y ≥0}.
We now provide an introduction to possible implementations that use these
ideas. For more details, the reader is referred to Gassmann [1990], Wets
[1988], or Wets [1983b].
a. Full decomposability
One ﬁrst possibility is to work out a full decomposition of pos W into
component bases. This can only be done for small problems or problems
with a well-deﬁned structure. As an example, consider the farming example
of Section 1.1. The second-stage representation (1.1.4) is repeated here
under the notation of the current chapter:
Q(x, ξ) = min
−210y1 + 140y2 −150y3 + 100y4 −36y5 + y6
s.t. y1 −y2 −w1 = 200 −ξ1x1,
y3 −y4 −w2 = 240 −ξ2x2,
y5 + y6 + w3 = ξ3x3,
y5 + w4 = 6000,
y, w ≥0,


## Page 190

5.4 Bunching and Other Eﬃciencies
171
where w1 to w4 are slack variables. This second stage has complete recourse,
so pos W = ℜ4.
The matrix W =



1
−1
0
0
0
0
−1
0
0
0
0
0
1
0
0
0
0
−1
0
0
0
0
0
−1
1
1
0
0
1
0
0
0
0
0
1
0
0
0
0
1



has 4 rows and 10 columns, so that theoretically
 10
4

= 210 bases could be
found. However, in practice w1, w2, and w3 are never in the basis, as they
are always dominated by y2, y4, and y6, respectively. The matrix where the
columns w1, w2, and w3 are removed is sometimes called the support of
W (see Wallace and Wets [1992]). Also, y5 is always in the basis (a fact
of worldwide importance as it is one of the reasons that created tension
between United States and Europe within the GATT negotiations). More-
over y1 or y2 and y3 or y4 are always basic. In this case, not only is a full
decomposition of pos W available, but an immediate analytical expression
for the multipliers is also obtained. Thus,
π1(ξ) =

210
if ξ1x1 < 200,
−140
otherwise;
π2(ξ) =

150
if ξ2x2 < 240,
−100
otherwise;
π3(ξ) =

−36
if ξ3x3 < 6000,
0
otherwise;
π4(ξ) =
 10
if ξ3x3 > 6000,
0
otherwise.
The dual multipliers are easily obtained because the problem is small and
enjoys some form of separability. The decomposition is thus (1, 3, 5, 6), (1, 3,
5, 10), (1, 4, 5, 6), (1, 4, 5, 10), (2, 3, 5, 6), (2, 3, 5, 10), (2, 4, 5, 6), (2, 4, 5, 10),
where the four variables in a basis are described by their indices (where
the index is 6 + j for the jth slack variable). Another example is given in
Exercise 1 and Wallace [1986a].
When applicable, full decomposability has proven very eﬃcient. In gen-
eral, however, it is expected to be applicable only for small problems.
b. Bunching
A relatively simple bunching procedure is as follows. Again let τ = {t|t =
hk −Tkxν for some k = 1, · · · , K} be the set of possible right-hand sides
in the second stage. Consider some k. Denote tk = hk −Tkxν. It might
arbitrarily be k = 1, or, if available, a value of k such that hk −Tkxν = ¯t,
the expectation of all tk ∈τ. Let B1 be the corresponding optimal basis


## Page 191

172
5. Two-Stage Linear Recourse Problems
and π(1) the corresponding vector of simplex multipliers. Then, Bu(1) =
{t ∈τ|B−1
1 t ≥0}. Let τ1 = τ\Bu(1).
We can now repeat the same operations. Some element of τ1 is chosen.
The corresponding optimal basis B2 and its associated vector of multipliers
π(2) are formed . Then, Bu(2) = {t ∈τ1|B−1
2 t ≥0} and τ2 = τ1\Bu(2).
The process is repeated until all tk ∈τ are in one of b total bunches. Then,
(1.10) and (1.11) are replaced by
Es+1 =
b

ℓ=1
π(ℓ)T

tk∈Bu(ℓ)
pkTk
(4.3)
and
es+1 =
b

ℓ=1
π(ℓ)T

tk∈Bu(ℓ)
pkhk .
(4.4)
This procedure still has some drawbacks. One is that the same tk ∈τ may
be checked many times against diﬀerent bases. The second is that a new
optimization is restarted every time a new bunch is considered. It is obvious
here that some savings can be obtained in organizing the work in such a
way that the optimal basis in the next bunch is obtained by performing
only one (or a few) dual simplex iterations from the previous one. As an
example, consider the following second stage:
max 6y1 +5y2 +4y3 +3y4
s. t. 2y1 +y2
+y3
≤ξ1,
y2
+y3
+y4 ≤ξ2,
y1
+y3
≤x1,
2y2
+y4 ≤x2,
y ≥0.
Let ξ1 ∈{4, 5, 6, 7, 8} with equal probability 0.2 each and ξ2 ∈{2, 3, 4, 5, 6}
with equal probability 0.2 each. There are theoretically
 8
4

= 70 diﬀerent
possible bases. In view of the possible realizations of ξ, at most 25 diﬀerent
bases can be optimal.
Let t1 to t25 denote the possible right-hand sides with
t1 =



4
2
x1
x2


, t2 =



4
3
x1
x2


, · · · , t25 =



8
6
x1
x2


.
Consider the case where x1 = 3.1 and x2 = 4.1. Let us start from ξ =
¯ξ = (6, 4)T . Represent a basis again by the variable indices with 4 + j
the index of the jth slack. The optimal basis is B1 = {1, 4, 7, 8} with
y1 = 3, y4 = 4, w3 = 0.1, w4 = 0.1, the values of the basic variables.


## Page 192

5.4 Bunching and Other Eﬃciencies
173
The optimal dictionary associated with B1 is
z = 3ξ1 + 3ξ2 −y2 −2y3 −3w1 −3w2,
y1 = 1/2ξ1 −1/2y2 −1/2y3 −1/2w1,
y4 = ξ2 −y2 −y3 −w2,
w3 = 3.1 −1/2ξ1 + 1/2y2 −1/2y3 + 1/2w1,
w4 = 4.1 −ξ2 −y2 + y3 + w2.
This basis is optimal and feasible as long as ξ1/2 ≤3.1 and ξ2 ≤4.1,
which in view of the possible values of ξ amounts to ξ1 ≤6 and ξ2 ≤4,
so that Bu(1) = {t1, t2, t3, t6, t7, t8, t11, t12, t13}. Neighboring bases can be
obtained by considering either ξ1 ≥7 or ξ2 ≥5. Let us start with ξ2 ≥5.
This means that w4 becomes negative and a dual simplex pivot is required
in Row 4. This means that w4 leaves the basis, and, according to the usual
dual simplex rule, y3 enters the basis.
The new basis is B2 = {1, 3, 4, 7} with an optimal dictionary
z = 3ξ1 + ξ2 + 8.2 −3y2 −3w1 −w2 −2w4,
y1 = ξ1
2 −ξ2
2 + 2.05 −y2 −w1
2 + w2
2 −w4
2 ,
y3 = ξ2 −4.1 + y2 −w2 + w4,
y4 = 4.1 −2y2 −w4,
w3 = 5.15 −ξ1
2 −ξ2
2 + w1
2 + w2
2 −w4
2 .
The condition ξ1 −ξ2 + 4.1 ≥0 always holds. This basis is optimal as long
as ξ2 ≥5 and ξ1 + ξ2 ≤10, so that Bu(2) = {t4, t5, t9}.
Neighboring bases are B1 when ξ2 ≤4 and B3 obtained when w3 < 0,
i.e., ξ1 + ξ2 ≥11. This basis corresponds to w3 leaving the basis and w2
entering the basis. To keep a long story short, we just summarize the various
steps in the following list:
B1 = {1, 4, 7, 8}
Bu(1) = {t1, t2, t3, t6, t7, t8, t11, t12, t13}
B2 = {1, 3, 4, 7}
Bu(2) = {t4, t5, t9}
B3 = {1, 3, 4, 6}
Bu(3) = {t10, t14, t15}
B4 = {1, 4, 5, 6}
Bu(4) = {t19, t20, t24, t25}
B5 = {1, 2, 4, 5}
Bu(5) = {t18, t22, t23}
B6 = {1, 2, 4, 8}
Bu(6) = {t16, t17, t21}
B7 = {1, 2, 5, 8}
Bu(7) = ∅.


## Page 193

174
5. Two-Stage Linear Recourse Problems
Several paths are possible, as one may have chosen B6 instead of B2 as
a second basis. Also, the graph may take the form of a tree, and more
elaborate techniques for constructing the graph and recovering the bases
can be used, see Gassmann [1988] and Wets [1983b].
Research has also been done to ﬁnd an appropriate root of the tree
(Haugland and Wallace [1988]) and to develop preprocessing techniques
(Wallace and Wets [1992]). Other attempts include the sifting procedure,
a sort of parametric analysis proposed by Gartska and Rutenberg [1973].
Finally, it is reasonable to expect that parallel processing may be helpful
in the search of the optimal multipliers in the second stage. As an example,
Ariyawansa and Hudson [1991] have designed a parallel implementation of
the L-shaped algorithm, in which the computation of the dual simplex mul-
tipliers in Step 3 is parallelized. They report an average speed-up factor of
5.5 on a seven-processor Sequent/Balance, for problems where the number
K of realizations in the second stage is large (up to 10, 000).
Exercise
1. Consider the capacity expansion example. Order the equipment in
increasing order of utilization cost q1 ≤q2 ≤. . .. Observe that it is
always optimal to use the equipment in that order. Then obtain a full
decomposition of pos W.
5.5
Inner Linearization Methods
As mentioned earlier, the most direct alternative to an outer linearization,
or cut generation, approach is an inner linearization or column generation
approach (see Geoﬀrion [1970] for other basic approaches to large-scale
problems). In fact, this was the ﬁrst suggestion of Dantzig and Madansky
[1961] for solving stochastic linear programs. They observed that the struc-
ture of the dual in Figure 2 ﬁts the prototype for Dantzig-Wolfe decompo-
sition. In fact, we can derive this approach from the L-shaped method by
taking duals.
Consider the following dual linear program to (1.2)–(1.4).
max ζ = ρT b +
r

ℓ=1
σℓdℓ+
s

ℓ=1
πℓeℓ
(5.1)
s.t. ρT A +
r

ℓ=1
σℓDℓ+
s

ℓ=1
πℓEℓ≤cT ,
(5.2)
s

ℓ=1
πℓ= 1, σℓ≥0, ℓ= 1, . . . , r, πℓ≥0, ℓ= 1, . . . , s.
(5.3)


## Page 194

5.5 Inner Linearization Methods
175
The linear program in (5.1)–(5.3) includes multipliers σℓon extreme rays, or
directions of recession, that cannot be produced with positive combinations
of distinct other recession directions, of the duals of the subproblems and
multipliers πℓon the expectations of extreme points of the duals of the
subproblems. To see this, suppose that (5.1)–(5.3) is solved to obtain a
multiplier xν on constraint (5.2). Now, consider the following dual to (1.9):
max
w = πT (hk −Tkxν) s.t. πT W ≤qT .
(5.4)
If (5.4) is unbounded for any k, we then must have some σν such that
σνT W ≤0 and σνT (hk −Tkxν) > 0, or (1.5)–(1.6) has a feasible dual
solution (hence optimal primal solution) with a positive value. So, Step 2 of
the L-shaped method is equivalent to checking whether (5.4) is unbounded
for any k. In this case, we form Dr+1 and dr+1 as in (1.7) and (1.8) of the
L-shaped method and add them to (5.1)–(5.3).
Next, note, that if (5.4) is infeasible, the stochastic program is not well-
formulated (see Exercise 1). Consider when (5.4) has a ﬁnite optimal value
for all k. In the L-shaped method, if (1.9) was solvable for all k, then we
formed Es+1 and es+1 and added them to (1.2)–(1.4). In this case in the
inner linearization procedure, we again use (1.10) and (1.11) to form Es+1
and es+1 and add them to (5.1)–(5.3).
Solving the duals in Steps 1 to 3 of the L-shaped algorithm then consists
of solving (5.1)–(5.3) as a master problem and problems (5.4) as subprob-
lems. Formally, this method is the following inner linearization method.
Inner Linearization Algorithm
Step 0. Set r = s = ν = 0.
Step 1. Set ν = ν + 1 and solve the linear program in (5.1)–(5.3). Let the
solution be (ρν, σν, πν) with a dual solution, (xν, θν).
Step 2. For k = 1, . . . , K, solve (5.4). If any infeasible problem (5.4) is found,
stop and evaluate the formulation. If an unbounded solution with extreme
ray σν is found for any k, then form new columns (dr+1 = (σν)T hk, Dr+1 =
(σν)T Tk), set r = r + 1, and return to Step 1.
If all problems (5.4) are solvable, then form new columns, Es+1 and es+1,
as in (1.10) and (1.11). If es+1 −Es+1xν −θν ≤0, then stop; (ρν, σν, πν)
and (xν, θν) are optimal in the original problem (5.1.2).
If es+1 −Es+1xν −θν > 0, set s = s + 1, and return to Step 1.
Clearly, the inner linearization method follows the same steps as the L-
shaped method, except that we solve the duals of the problems instead of
the primals. Hence, convergence follows directly from the L-shaped method.
We could also view this approach directly as in Dantzig-Wolfe decomposi-
tion by stating that (5.1)–(5.3) is an inner linearization of the dual of the
basic L-shaped problem in (5.1.2) and that the subproblems (5.4) generate


## Page 195

176
5. Two-Stage Linear Recourse Problems
new extreme points and rays to add to this inner linearization (see Exercise
2).
If, as in many problems, n1 >> m1, the primal version has smaller
basis matrices, at most of order m1 + m2, than the n1 × n1 bases for
the dual. Hence, the L-shaped implementation is usually preferred. Inner
linearization can, however, be applied directly to the primal by assuming
T is ﬁxed using the form in (3.1.5), which we repeat here:
min z =cT x + Ψ(χ)
(5.5)
s.t. Ax = b,
Tx −χ = 0,
x ≥0,
where Ψ(χ) = Eωψ(χ, ξ(ω)) and ψ(χ, ξ(ω)) = min{q(ω)T y|Wy = h(ω) −
χ, y ≥0}. Note that, in this form, we assume that T is ﬁxed but q and h
may still be functions of ω. For this reason, we revert to the use of Ψ for
the recourse function.
In this case, we wish to build an inner linearization of the function Ψ(χ)
using the generalized programming approach as in Dantzig [1963, Chapter
24]. The basic idea is to replace Ψ(χ) by the convex hull of points Ψ(χℓ)
chosen in each iteration of the algorithm. Each iteration generates a new ex-
treme point of a region of linearity for Ψ, which is polyhedral as we showed
in Theorem 3.6. Thus, ﬁnite convergence is assured with ﬁnite numbers of
realizations.
The algorithm follows.
Generalized Programming Method for Two-Stage Stochastic
Linear Programs
Step 0. Set s = t = ν = 0.
Step 1. Set ν = ν + 1 and solve the linear program master problem:
min zν = cT x +
r

i=1
µiΨ+
0 (ζi) +
s

i=1
λiΨ(χi)
(5.6)
s.t. Ax = b,
(5.7)
Tx −
r

i=1
µiζi −
s

i=1
λiχi = 0,
(5.8)
r

i=1
λi = 1,
(5.9)
x, µi ≥0, i = 1, . . . , r, λi ≥0, i = 1, . . . , s.
If (5.6)–(5.9) is infeasible or unbounded, stop. Otherwise, let the solution
be (xν, µν, λν) with associated dual variables, (σν, πν, ρν).


## Page 196

5.5 Inner Linearization Methods
177
Step 2. Solve the subproblem:
min
χ Ψ(χ) + (πν)T χ −ρν,
(5.10)
which we assume has value less than ∞.
If (5.10) is unbounded, a recession direction ζr+1 is obtained, such that
for some χ, Ψ(χ + αζr+1) + (πν)T (χ + αζr+1) →−∞as α →∞. In this
case, let Ψ+
0 (ζr+1) = limα→∞
Ψ(χ+αζr+1)−Ψ(χ)
α
, r = r + 1, and return to
Step 1.
If (5.10) is solvable, let the solution be χs+1. If Ψ(χ) + (πν)T χ −ρν ≥0,
then stop; (xν, µν, λν) corresponds to an optimal solution to (5.5). Other-
wise, set s = s + 1 and return to Step 1.
This algorithm generates columns in (5.6)–(5.9) corresponding to new
proposals from the subproblem in (5.10). In the two-stage stochastic linear
program form, (5.10) can be recast as:
min
K

k=1
pkqT
k yk + (πν)T χ −ρν
(5.11)
s.t. Wyk + χ = hk, k = 1, . . . , K,
yk ≥0, k = 1, . . . , K.
This problem is not generally separable into diﬀerent subproblems for each
k. Hence, for general problems, the L-shaped method has an advantage. In
some cases (notably simple recourse), Ψ(χ) is separable into components for
each k, and (5.11) can again be divided into K independent subproblems.
We discuss this possibility further in Section 7.
To show that the generalized programming method also converges
ﬁnitely, we wish to show that an extreme solution in (5.11) is an extreme
value of linear regions of Ψ(χ). We do this for extreme points in the fol-
lowing proposition.
Proposition 3. Every optimal extreme point, (¯y1, . . . , ¯yK, ¯χ), of the fea-
sible region in (5.11) corresponds to an extreme point ¯χ of {χ|Ψ(χ) =
¯πT χ + θ}, where ¯π = 	K
k=1 ¯πk, and each ¯πk is an extreme point of
{πk|πT
k W ≤qT
k }.
Proof:
Suppose (¯y1, . . . , ¯yK, ¯χ) is an optimal extreme point in (5.11). In
this case, we must have qT
i ¯yi ≤qT
i yi for all Wyi = ξi −¯χ. We must also
have that ¯yi is an extreme point of {yi|Wyi = ξi −¯χ, yi ≥0} because,
otherwise, we could take ¯yi = (1/2)(y1
i +y2
i ) for distinct feasible y1
i and y2
i .
So, ¯yk has a complementary dual solution, ¯πk, that is an extreme point of
{πk|πT
k W ≤qT
k } and such that (qT
k −¯πT
k W)¯yk = 0.
Now, suppose ¯χ is not an extreme point of the linearity region where
Ψ(χ) = ¯πT χ + θ for θ = Ψ(¯χ) −¯πT χ with ¯π = 	K
k=1 ¯πk. In this case,


## Page 197

178
5. Two-Stage Linear Recourse Problems
there exists χ1 and χ2 such that ¯χ = λχ1 + (1 −λ)χ2 where 0 < λ < 1,
for Ψ(χ1) = ¯πT χ1 + θ and Ψ(χ2) = ¯πT χ2 + θ. We also have that Ψ(χj) =
	K
k=1 qT
k yj
k, where qT
k yj
k = ¯πT
k (hk −χj) for j = 1, 2, because, by ¯πT
k feasible
in the kth recourse problem, the only other possibility is qT
k yj
k > ¯πT
k (ξ−χj),
which would imply Ψ(χj) > ¯πT χj + θ. This also implies that
(¯πT
k W −qT
k )(λy1
k + (1 −λ)y2
k) = 0,
(5.12)
which implies that λy1
k + (1 −λ)y2
k = ¯yk because ¯yk is an extreme point of
the feasible region in recourse problem k. In this case, (¯y1, . . . , ¯yK, ¯χ) =
λ(y1
1, . . . , ¯y1
K, χ1) + (1 −λ)(y2
1, . . . , ¯y2
K, χ2), with both terms feasible in
(5.11). This contradicts that (¯y1, . . . , ¯yK, ¯χ) is an extreme point.
A similar argument shows that any extreme ray found in solving (5.11)
is an extreme ray of a region of linearity of Ψ(χ) (Exercise 3). Now, we can
state the generalized programming ﬁnite convergence result.
Theorem 4. The generalized programming applied to problem (5.5) with
subproblem (5.11) solves (5.5) in a ﬁnite number of steps.
Proof: At each solution of (5.11), a new linear region extreme value is gen-
erated. First for a new extreme ray, we must have Ψ+
0 (ζr+1)+(πν)T (ζr+1) <
0, while, for 1 ≤i ≤s, Ψ+
0 (ζi) ≥−(πν)T ζi. For an extreme point, we only
add that point if Ψ(χs+1) + (πν)T χs+1 −ρν < 0, while, for 1 ≤i ≤s,
Ψ(χs) + (πν)T χs −ρν ≥0. Because the number of such regions is ﬁnite
and each has a ﬁnite number of extreme points and rays, the algorithm
converges ﬁnitely.
The solution found solves (5.5) because if we reach the termination con-
dition, then
(σν)T b + ρν≤(σν)T b + Ψ(χ) + (πν)T χ
≤(σνT A + (πν)T T)x + Ψ(χ), (x, χ) feasible in (5.5),
≤cT x + Ψ(χ),
(5.13)
for all (x, χ) feasible in (5.5).
As with the L-shaped method, we can also modify the generalized linear
programming approach to consider only active columns so that s and t
can be bounded again by m2. Of course, this approach’s greatest potential
is in simple recourse problems as we mentioned earlier. It may also be
advantageous if an algorithm can take advantage of the special matrix
structure in (5.11). The most direct approach in this case is to construct
a working basis and to try to perform most linear transformations with
submatrices chosen from W. In this case, the procedure becomes quite
similar to the procedures for directly attacking (3.1.2) that are given in the
next section.
The generalized programming approach is also useful in considering the
stochastic program as a procedure for combining tenders χi (see Nazareth


## Page 198

5.6 Basis Factorization Methods
179
and Wets [1986]) bid from the subproblems. In this case, the method may
converge most quickly if the initial set of tenders is chosen well. A method
for choosing such an initial set of tenders appears in Birge and Wets [1984].
Exercises
1. Suppose Problem (5.4) is infeasible for some k. What can be said
about the original two-stage stochastic linear program? Find exam-
ples for these possible situations.
2. Prove directly that the inner linearization method converges to an
optimal solution to the two-stage stochastic linear program (3.1.2).
3. Show that any extreme descending ray in (5.11) corresponds to an
extreme ray of a linear piece of Ψ(χ).
5.6
Basis Factorization Methods
As observed earlier in this chapter, the matrices in (1.1) and its dual have a
special structure that may allow eﬃcient speciﬁc basis factorizations. In this
way, the extensive form of the problem may be more eﬃciently solved by
either extreme point or interior point methods. There are similarities with
the previous decomposition approaches. We discuss relative advantages and
disadvantages at the end of this section.
Basis factorization for extreme point methods has generally been consid-
ered the dual structure, although the same ideas apply to either the dual or
primal problems. For more details on this approach, we refer to Kall [1979]
and Strazicky [1980]. We consider the primal approach because, generally,
the number of columns (n1 + Kn2) is larger than the number of rows
(m1 + Km2) in the original constraint matrix. In this case, we can write
a basic solution as (xI0, xI1, . . . , xIK, yJ1, . . . , yJk), where Ij, j = 0, . . . , K,
and Jl, l = 1, . . . , K, are index sets that may be altered at each iteration.
The constraints are also partitioned according to these index sets so that
a basis is:
B =




AI0
AI1
. . .
AIK
T1,I0
T1,I1
. . .
T1,IK
WJ1
...
...
...
...
WJk
TK,I0
TK,I1
. . .
TK,IK
WJK



.
(6.1)
The main observation in basis factorization is that we may permute the
rows of B to achieve an eﬃcient form. This is the result of the following
proposition.


## Page 199

180
5. Two-Stage Linear Recourse Problems
Proposition 5. A basis matrix, B, for problem (1.1) is equivalent after a
row permutation P to
B′ = PB =

D
C
F
L

,
(6.2)
where D is square invertible and at most n1 × n1 and L is an invertible
matrix of K invertible blocks of sizes at most m2 × m2 each.
Proof:
We can perform the required permutation on B in (6.1). First,
note that the number of columns in AI0, . . . , AIK is at most n1 for B to
be nonsingular. We must also be able to form a nonsingular submatrix
from these columns if B is invertible. Suppose this matrix is composed of
AI0, . . . , AIK and rows Tku,Ij from each subproblem j = 1, . . . , K. In this
case, we have constructed
D =




AI0
AI1
. . .
AIK
T1u,I0
T1u,I1
. . .
T1u,IK
...
...
...
...
TKu,I0
TKu,I1
. . .
TKu,IK



.
Hence,
C =










0
0
· · ·
0
0
W1u,J1
0
· · ·
0
0
0
...
0
· · ·
0
...
0
Wku,Jk
0
...
0
· · ·
0
...
0
0
0
· · ·
0
WKu,JK










.
Next, assume that the remaining rows of Tk,Ij are Tkl,Ij. We then obtain:
F =



T1l,I0
T1l,I1
. . .
T1l,IK
...
...
...
...
TKl,I0
TKl,I1
. . .
TKl,IK



and
L =


W1l,J1
0
0
0
· · · Wkl,Jk · · ·
0
0
0
WKl,JK

.
Because D has rank at least m1, each Wkl,Jk in L has rank at most m2.
This gives the result.
To show how this result is used, consider the forward transformation to
ﬁnd the basic values of (xI0, xI1, . . . , xIK, yJ1, . . . , yJk), which we write as
(xB, yB), that solve:
DxB + CyB = b′; FxB + LyB = h′,
(6.3)


## Page 200

5.6 Basis Factorization Methods
181
where b′ =

b
hu

, h′ = hl, hu corresponds to the components of the right-
hand side for rows of T in D, and hl corresponds to the components with
rows in F.
Note that L is invertible, so
yB = L−1(h′ −FxB).
(6.4)
Substituting in the ﬁrst system of equations yields
(D −CL−1F)xB = b′ −CL−1h′.
(6.5)
Hence, we use L to solve for the columns of L−1F and L−1h′, then form
the working basis, (D −CL−1F), to solve for xB, and multiply xB again
by L−1F and subtract from L−1h′ to obtain yB. Because most of the work
involves just the square block matrices in L and the working basis, substan-
tial eﬀort can be saved in the decomposition procedure (see Exercise 1).
The backward transformation can also be performed by taking advantage
of this structure (see Exercise 2). The other forward transformation in the
simplex method to ﬁnd the leaving column is, of course, the same as the
operations used in (6.4) and (6.5). The entire simplex method then has the
following form.
Basic Factorization Simplex Method
Step 0. Suppose that (x0
B0, y0
B0′) = (x0
I0
0 , . . . , x0
I0
K, y0
J0
0 , . . . , y0
J0
K) is an initial
basic feasible solution for (1.1), with initial indices partitioned according
to B0 = {β0
1, . . . , β0
l0} = {I0
i , i = 0, . . . , K} and B0′ = {β0,′
1,1, . . . , β0,′
1,l′
1, . . . ,
β0,′
K,1, . . . , β0,′
K,l′
K} = J0
j , j = 1, . . . , K. Let the initial permutation matrix be
P 0, and set ν = 0.
Step 1. Solve (ρT , πT )

D
C
F
L

= (cT
B0, ˆqT
β0), where ˆqk,i = pkqk,i.
Step 2. Find ¯cs = minj{cj −(ρT |πT )P ν(AT
·j|T T
1,·j| · · · |T T
K,·j)T } and ¯qk′,s′ =
minj,k{pkqk,j −(ρT |πT )P ν(0 · · · Wk,·j · · · 0)}. If ¯cs ≥0 and ¯qk′,s′ ≥0, then
stop; the current solution is optimal. Otherwise, if ¯cs < ¯qk′,s′, go to Step
4. If ¯cs ≥¯qk′,s′, go to Step 3.
Step 3. Solve for the entering column,

D
C
F
L

¯Wk′,·s′ = P ν(0 · · · W T
k′,·s′
· · · 0)T . Let
θ = xν
Bν(r)/ ¯Wk′,rs′ =
min
¯
Wk′,is′>0,1≤i≤lν{xν
Bν(i)/ ¯Wk′,is′}
(6.6)
and
θ′ = yν
Bν′(r′)/ ¯Wk′,r′s′ =
min
¯
Wk′,is′>0,lν+1≤i≤m1+Km2
{yν
Bν′(i)/ ¯Wk′,is′}.
(6.7)


## Page 201

182
5. Two-Stage Linear Recourse Problems
If no minimum exists in either (6.6) or (6.7), then stop; the problem is
unbounded. Otherwise, if θ < θ′, go to Step 5. If θ ≥θ′, go to Step 6.
Step 4. Solve for the entering column,

D
C
F
L

¯A·s′ = P ν(AT
·s|T T
1,·s| · · ·
|T T
K,·s)T . Let
θ = xν
Bν(r)/ ¯Ars =
min
¯
Ais>0,1≤i≤lν{xν
Bν(i)/ ¯Ais′}
(6.8)
and
θ′ = yν
Bν′(r′)/ ¯Ar′s =
min
¯
Ais′>0,lν+1≤i≤m1+Km2
{yν
Bν′(i)/ ¯Ais}.
(6.9)
If no minimum exists in either (6.8) or (6.9), then stop; the problem is
unbounded. Otherwise, if θ < θ′, go to Step 5. If θ ≥θ′, go to Step 6.
Step 5. Let Bν+1 = Bν, Bν+1′ = Bν′, Iν+1
i
= Iν
i , and Jν+1 = Jν. Suppose
Bν(r) = Iν
j,w = t. If xs is entering, then let Bν+1(r) = Iν+1(j, w) = s. If
yk′s′ is entering, then let Bν+1(i) = Bν(i + 1), i ≥r, Iν+1
j,i
= Iν
j,i+1, i ≥w,
Jν+1
k′,l′
k′+1 = s′, and l′
k′ = l′
k′ + 1. Update P ν to P ν+1, the factorization
correspondingly, let ν = ν + 1, and go to Step 1.
Step 6. Let Bν+1 = Bν, Bν+1′ = Bν′, Iν+1
i
= Iν
i , and Jν+1 = Jν. Suppose
Bν′(r′) = Jν
k,w = t. If xs is entering, then let Bν+1(	k
j=1 lj) = Iν+1(k, lk +
1) = s, Bν+1(i) = Bν(i −1), i > 	k
j=1 lj, lk = lk+1, Jν+1
k,i
= Jν
k,i+1, i ≥w.
If yk′s′ is entering, then let Bν+1(i) = Bν(i+1), i ≥r, Iν+1
j,i
= Iν
j,i+1, i ≥w,
Jν+1
k′,l′
k′+1 = s′, Jν+1
k,i
= Jν+1
k,i+1, i ≥w, l′
k = l′
k −1, and l′
k′ = l′
k′ + 1. Update
P ν to P ν+1, the factorization correspondingly, let ν = ν + 1, and go to
Step 1.
For updating a factorization of the basis as used in (6.4) and (6.5), several
cases need to be considered according to the possibilities in Steps 5 and 6
(see Exercise 3). If the entering and leaving variables are both in x, then
only D changes. Substantial eﬀort can again be saved. In other cases, only
one block of L is altered by any iteration so we can again achieve some
savings by only updating the corresponding parts of L−1F and L−1h.
As mentioned earlier, this procedure can also apply to the dual of (1.1)
and the primal. In this case, the procedure can mimic decomposition pro-
cedures and entails essentially the same work per iteration as the L-shaped
method (see Birge [1988b]) or the inner linearization method applied to the
dual. If choices of entering columns are restricted in a special variant of a
decomposition procedure, then factorization and decomposition follow the
same path.
In general, decomposition methods have been favored for this class of
problems because they oﬀer other paths of solutions, require less overhead,


## Page 202

5.6 Basis Factorization Methods
183
and, by maintaining separate subproblems, allow for parallel computation.
The extensive form oﬀers little hope for eﬃcient solution, so it is not sur-
prising that even sophisticated factorizations would not prove beneﬁcial.
Because most commercial methods already have substantial capabilities
for exploiting general matrix structure, it is diﬃcult to see how substan-
tial gains could be obtained from basis factorization alone for a direct
extreme point approach. Combinations of decomposition and factorization
approaches may, however, be beneﬁcial, as observed in Birge [1985b].
Factorization schemes also oﬀer substantial promise for interior point
methods, where there is much speculation that the solution eﬀort grows
linearly in the size of the problem. This observation is supported by the re-
sults we present here. For this discussion, we assume that the interior point
method follows a standard form version of Karmarkar’s projective algo-
rithm as in Anstreicher [1989, 1990], Gay [1987], and Ye [1987]. We choose
the standard form because we believe it is more practical for computation
than various canonical forms. We also assume an unknown optimal objec-
tive value and use Todd and Burrell’s [1986] method for updating a lower
bound on the optimal objective value. We use an initial lower bound, as
is often available in practice. An alternative is Anstreicher’s [1989] method
to obtain an initial lower bound.
Other interior point methods based on aﬃne scaling (Barnes [1986], Van-
derbei, Meketon, and Freedman [1986], Dikin [1967]) also follow the same
basic steps with some simpliﬁcation. They are, however, not provably poly-
nomial methods. We present this polynomial version as a more general case.
We ﬁrst describe the algorithm for a standard linear program:
min cT x
s. t. Ax= b,
x≥0,
(6.10)
where x ∈ℜn, c ∈Zn (i.e., an n-vector of rationals), b ∈Zm, A ∈Zm×n
with optimal value cT x∗= z∗. In referring to the parameters in (6.10), we
use (ext) as a modiﬁer, e.g., c(ext), when necessary to distinguish these
parameters in our standard stochastic program form in (1.1).
Suppose we have a strictly interior feasible point x0 of (6.10), i.e.,
Ax0 = b, x0 > 0,
(6.11)
a lower bound β0 on z∗, and the set of optimal solutions in (6.10) is
bounded. Note that if we do not have a feasible solution, we can solve
a phase-one problem as in Karmarkar [1984].
The standard form variant of Karmarkar’s projective scaling algorithm
creates a sequence of points x0, x1, ..., xk by the following steps.
Standard Form Projective Scaling Method
Step 0. Set ν = 0 and lower bound β0 ≤z∗.


## Page 203

184
5. Two-Stage Linear Recourse Problems
Step 1. If cT xν −βν is small enough, i.e., less than a given positive number
ǫ, then stop. Otherwise, go to Step 2.
Step 2. Let D = diag{xν
1, . . . , xν
n}, ˆA := [AD, −b], and let Π ˆ
A be the
projection onto the null space of ˆA. Find
u = Π ˆ
A

Dc
0

, v = Π ˆ
A

0
1

,
(6.12)
and let µ(βν) = min{ui −βνvi : i = 1, . . . , n + 1}. If µ(βν) ≤0, let
βν+1 = βν. Otherwise, let βν+1 = min{ui/vi : vi > 0, i = 1, . . . , n + 1}. Go
to Step 3.
Step 3. Let cp = u−βν+1v−(cT xν−βν+1)e/(n+1), where e = (1, . . . , 1)T ∈
ℜn+1. Let
g′ =
1
n + 1e −α
cp
∥cp∥2
.
Let g ∈ℜn consist of the ﬁrst n components of g′. Then xν+1 = Dg/g′
n+1,
ν = ν + 1, go to Step 1.
For the purpose of obtaining a worst-case bound, the step length α in the
deﬁnition of g′ may be set equal to
1
3(n+1), as in Gay [1987]. In practice,
much better performance is obtained by choosing α using a line search of
the “potential functions” (see Anstreicher [1990] and Gay [1987]). We con-
sider the number of arithmetic operations in our complexity analyses. The
main computational eﬀort in each iteration of the algorithm is to compute
the projections in (6.12), which requires O(m2n) arithmetic operations.
The algorithm is shown to obtain a solution that can be resolved to an
optimal basic feasible solution in O(nL) iterations in Ye and Kojima [1987]
and Anstreicher [1989], who also shows how a slightly revised version ob-
tains a complexity of O(√nL) iterations (Anstreicher [1993]). The overall
arithmetic complexity for the basic method is O(m2n2L). Karmarkar [1984]
uses a rank–one updating scheme to reduce the complexity to O(n3.5L).
In our case, if we consider (1.1) as in the form of (6.10), then n =
n0 + Kn1, m = m0 + Km1, x((ext)) =




x
y1
...
yK



, c((ext)) =




c
p1q1
...
pKqK



,


## Page 204

5.6 Basis Factorization Methods
185
b((ext)) =




b
h1
...
hK



, and
A((ext)) =




A
0
· · ·
0
T1
W
· · ·
0
...
0
...
0
TK
0
· · ·
W



.
(6.13)
The main computational work at each step of Karmarkar’s algorithm is to
compute the projections in (6.12). The projection can be written as
Π ˆ
A = (I −ˆAT ( ˆA ˆAT )−1 ˆA),
where ( ˆA ˆAT ) = AD2AT + bbT := M + bbT . In this case, the work is
dominated by computing M −1. The key eﬀort is in solving systems with
AD2AT for the general A in the formulation in (6.10). Using the speciﬁc
A(ext) in the stochastic programming matrix as given by (6.13) and letting
D0 = diag(xν), Dk = diag(yν
k), k = 1, . . . , K, we would have
M =




AD2
0AT
AD2
0T T
1
· · ·
AD2
0T T
K
T1D2
0AT
T1D2
0T T
1 + WD2
1W T
· · ·
T1D2
0T T
K
...
...
...
...
TKD2
0AT
T1D2
0T T
K
· · ·
TKD2
0T T
K + WD2
KW T



,
(6.14)
which is clearly much denser than the original constraint matrix in (1.1).
In this case, a straightforward implementation of an interior point method
that solves systems with M is quite ineﬃcient.
Note, however, that M in (6.14) has a great deal of structure that can
be exploited in any solution scheme. This is the object of the factorization
scheme given by Birge and Qi [1988]. The following proposition gives the
essential characterization of that factorization.
Proposition 6. Let S0 = I2 ∈ℜm1×m1, Sl = WlD2
l W T
l , l = 1, . . . , K,
S = diag{S0, . . . , SK}. Then S−1 = diag{S0, S−1
1 , . . . , S−1
N }. Let I1 and I2
be identity matrices of dimensions n1 and m1, respectively. Let
G1 = (D0)−2 + AT S−1
0 A +
K

l=1
T T
l S−1
l
Tl, G2 = −AG−1
1 AT ,
(6.15)
U =




A
I2
T1
0
...
...
TK
0



, V =




A
−I2
T1
0
...
...
TK
0



.


## Page 205

186
5. Two-Stage Linear Recourse Problems
If A, Wk, k = 1, . . . , K have full row rank, then G2 and M are invertible
and
M −1= S−1 −S−1U

I1
G−1
1 AT
0
I2
 
I1
0
0
G−1
2


I1
0
A
I2
 
G−1
1
0
0
−I2

V T S−1.
(6.16)
Proof:
Follows Birge and Qi [1988]. See also Birge and Holmes [1992].
Following the assumptions and using Karmarkar’s complexity result, the
number of arithmetic operations using this factorization can be reduced
from O((n1+Kn2)4) as in the general projective scaling method. Birge and
Qi show that the eﬀort is, in fact, dominated by O(K(n3
2+n2
2n1+n2n2
1)). It
is also possible to reduce this bound further as Karmarkar does with a par-
tial rank-one updating scheme. In this case, for n = n1+Kn2, the complex-
ity using the factorization in (6.16) becomes O((n0.5n2
2 + n max{n1, n2} +
n3
1)nL) for the entire algorithm, where L represents the size of the data,
or, if K ∼n1 ∼n2, the full arithmetic complexity is O(n2.5L), compared
to Karmarkar’s general result of O(n3.5L). Thus, the factorization in (6.16)
provides an order of magnitude improvement over a general solution scheme
if the number of realizations K approaches the number of variables in the
ﬁrst and second stage.
In practice, we would not compute M −1 explicitly. The work in (6.16) is
dominated by the eﬀort to solve systems of the form
Mv = u
(6.17)
using
v = p −r,
(6.18)
where
Sp= u,
Gq= V T p,
Sr= Uq,
(6.19)
where G is the inverse of the matrix between U and V T in (6.16). The
systems in (6.19) require solving systems with Sl, computation of G1 and
G2, and solving systems with G1 and G2. In practice, we ﬁnd a Cholesky
factorization of each Sl, use them to ﬁnd G1 and G2, and ﬁnd Cholesky
factorizations of G1 and G2.
Before we describe results using the factorization in (6.16), we consider
some other options for interior point methods. These possibilities are
1. Schur complement updates;
2. Column splitting;


## Page 206

5.6 Basis Factorization Methods
187
3. Solution of the dual.
The Schur complement approach is used in many interior point method
implementations (see, e.g., Choi, Monma, and Shanno [1990]). The basic
idea is to write M as the sum of a matrix with sparse columns, AsD2
sAT
s ,
and a matrix with dense columns, AdD2
dAT
d . Using a Cholesky factorization
of the sparse matrix, LLT = AsD2
sAT
s , the method involves solving Mu = v
by:

LLT
−AdDd
DdAT
d
I
 
v
w

=

u
0

,
(6.20)
which requires solving [I+DdAT
d (LLT )−1AdDd]w = −DdAT
d (LLT )−1b and
LLT v = b+AdDdw, where I+DdAT
d (LLT )−1AdDd is a Schur complement.
The Schur complement is thus quite similar to the factorization method
given earlier. If every column of x is considered a dense column, then the
remaining matrix is quite sparse but rank deﬁcient. The factorization in
(6.16) is a method for maintaining an invertible matrix when AsD2
sAT
s is
singular. It can thus be viewed as an extension of the Schur complement to
the stochastic linear program. Because of the possible rank deﬁciency and
the size of the Schur complement, the straightforward Schur complement
approach in (6.20) is quick but leads to numerical instabilities as Carpenter,
Lustig, and Mulvey [1991] report.
Carpenter et al. also propose the column splitting technique. The basic
idea is to rewrite problem (1.1) with explicit constraints on nonanticipa-
tivity. The formulation then becomes:
min
K

k=1
pk(cT xk + qT
k yk)
(6.21)
s.t. Axk = b,
(6.22)
Tkxk + Wyk = hk,
k = 1, . . . , K,
(6.23)
xk −xk+1 = 0, k = 1, . . . , K −1,
(6.24)
xk ≥0,
yk ≥0,
k = 1, . . . , K.
(6.25)
The diﬀerence now is that the constraints in (6.22) and (6.23) separate into
separate subproblems k and constraints (6.24) link the problems together.
Alternating constraints, (6.22), (6.23) and (6.24) for each k in sequence,


## Page 207

188
5. Two-Stage Linear Recourse Problems
the full constraint matrix has the form:
¯A =
















A
0
0
0
0
0
0
0
T1
W
0
0
0
0
0
0
I
0
−I
0
0
0
0
0
0
0
A
0
0
0
0
0
0
0
T2
W
0
0
0
0
0
0
I
0
−I
0
0
0
...
...
0
...
...
...
0
...
0
0
0
0
I
0
−I
0
0
0
0
0
0
0
A
0
0
0
0
0
0
0
Tk
W
















.
(6.26)
If we form ¯A ¯AT , then we obtain ¯A ¯AT =





















AAT
AT T
1
A
0
0
0
0
0
T1AT
T1T T
1 + WW T
T1
0
0
0
0
0
AT
T T
1
2I
−AT
0
0
0
0
0
0
−A
AAT
AT T
2
A
0
0
0
0
T2AT
T2T T
2
T2
0
0
0
+WW T
0
0
0
T T
2
2I
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
...
0
0
0
AT
T T
K−1
2I
−AT
0
0
0
0
0
0
−A
AAT
AT T
K
0
0
0
0
0
0
TKAT
TKT T
K
+WW T





















,
(6.27)
which is clearly much sparser than the original matrix in (6.14). It is,
however, larger than the matrix in (6.14) (see Exercise 5) so there is some
tradeoﬀfor the reduced density.
The third additional approach is to form the dual of (1.1) and to solve
that problem using the same basic interior point method we gave earlier.
The dual problem is:
max bT ρ +
K

k=1
pkπT
k hk
(6.28)
s.t. AT ρ +
K

k=1
pkT T
k πk ≤c, k = 1, . . . , K,
(6.29)
W T πk ≤q, k = 1, . . . , K,
(6.30)
where the variables are not restricted in sign. For this problem, we can
achieve a standard form as in (6.10) by splitting the variables πk and ρ
into diﬀerences of non-negative variables and by adding slack variables to


## Page 208

5.6 Basis Factorization Methods
189
constraints (6.29) and (6.30)1. In this way the constraint matrix for (6.29)
and (6.30) becomes:









AT
−AT
T T
1
−T T
1
0
T T
2
−T T
2
· · ·
T T
K
−T T
K
0
I
0
0
W T
−W T
I
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
0
W T
−W T
I
0
0
0
0
...
...
...
...
...
0
...
...
...
0
0
...
0
0
0
0
0
0
0
0
W T
−W T
I
0









.
(6.31)
The matrix in (6.31) may again be much larger than the matrix in the
original, but the gain comes in considering A′A′T which is now:






2(AT A + K
k=1 T T
k Tk) + I
2T T
1 W
2T T
2 W
· · ·
2T T
k W
2W T T1
2W T W + I
0
0
0
2W T T2
0
2W T W + I
0
0
...
0
0
...
0
2W T Tk
0
0
0
2W T W






,
(6.32)
with an inherent sparsity of which an interior point method can take ad-
vantage. In fact, it is not necessary to take the dual to use this alterna-
tive factorization form, although we do so in the following computations.
As shown in Birge, Freund, and Vanderbei [1992], the Sherman-Morrison-
Woodbury formula can be applied to the original problem in (6.10) so that
computations with the structure of A(ext)A(ext)T are replaced by compu-
tations with A(ext)T A(ext). In this way, the matrix in (6.32) replaces the
dense matrix in (6.14).
In Carpenter, Lustig, and Mulvey [1991], increasing numbers of scenarios
were included into a network formulation of a ﬁnancial decision problem.
They used the variable splitting option with an additional observation that
many of the Tk columns were zero and that the corresponding variables need
not be split. By splitting only those variables with nonzero Tk entries, they
developed a partial splitting model that proved most eﬀective. Their results
with this partial splitting model show an approximately linear increase in
speed-up for using split variables compared to the original primal form
with the interior point code OB1 (Lustig, Marsten, and Shanno [1991]).
For 18 scenarios, the speed-up was 1.48, while for 72 scenarios of the same
problem, the partial splitting speed-up was 11.82.
Carpenter et al. also used the Schur complement approach and achieved
additional speed-ups over partial splitting, although the additional speed-
up was about the same (essentially two) for all numbers of scenarios. They
did, however, report an order of magnitude increase in a measure of primal
1The dual problem may no longer have a bounded set of optima causing some
theoretical diﬃculties for convergence results. In practice, bounds are placed on
the variables to guarantee convergence.


## Page 209

190
5. Two-Stage Linear Recourse Problems
TABLE 1. Speed-ups for the Proposition 6 factorization over the primal and dual
interior point method solutions.
Problem
Number of
Speed-Ups Over:
Scenarios
Primal
Dual
SC205.02
8
2.156
0.315
SC205.03
16
7.101
0.331
SC205.04
32
26.753
0.379
SC205.05
64
> 30
0.404
SCRS8.02
8
1.571
0.224
SCRS8.03
16
9.396
0.263
SCRS8.04
32
> 30
0.150
SCAGR7.02
8
4.426
0.395
SCAGR7.03
16
15.840
0.439
SCAGR7.04
32
> 30
0.507
SCAGR7.05
64
> 30
0.727
SCTAP.02
8
3.164
0.850
SCTAP.03
16
12.825
1.054
SCTAP.04
32
> 30
1.250
SCSD8.01
4
*
2.691
* Algorithm for primal problem did not converge.
infeasibility due to numerical instability with the basic Schur complement
approach.
In Birge and Holmes [1992], the dual approach and the primal factoriza-
tion of Birge and Qi are compared. We repeat the results of some of these
problems in Table 1. The problems are a test set of stochastic programs
based on the multistage problems compiled by Ho and Loute [1981]. They
represent problems in economic development, agriculture, energy model-
ing, structural design, traﬃc assignment, and production scheduling. The
problems are solved as multistage stochastic programs in Birge [1985b] with
a small number of scenarios. For the interior point tests reported in Ta-
ble 1, they were formed as two-stage problems with increasing numbers of
second-stage realizations or scenarios.
Table 1 shows the number of scenarios in each problem and the speed-
up, or the ratio of solution times for solving each problem in the original
primal, and the dual form to the time for solutions using the factorization
in Proposition 6. An aﬃne scaling form (without a centering term) of the
interior point method given earlier was implemented in FORTRAN on an
IBM 3090 at the University of Michigan. The program used SPARSPAK
(Chu et al. [1984]) to solve the systems of equations.
Table 1 shows that the dual form appears to be the most eﬃcient. How-
ever, in some cases, this matrix became too large for the MTS operating


## Page 210

5.6 Basis Factorization Methods
191
system that the machine runs under. This was the case for larger versions of
SCSD8, which has seven times as many columns as rows. Also, notice that
the factorization approach appears relatively more eﬃcient as the problem
size increases. It, therefore, appears that either of these approaches may be
used, although many columns would favor the factorization in (6.16), while
many rows would favor taking the dual.
The speed-ups over the primal form in Table 1 are especially dramatic.
They increase superlinearly in all classes of problems tested. In compari-
son to Lustig et al.’s results, it appears that either the dual form or the
factorization in (6.16) is most eﬃcient because they appear clearly to oﬀer
superlinear speed-ups. Of course, some problems may exist where vari-
able splitting is preferred. Other approaches include an augmented system
approach (Czyzyk, Fourer, and Mehrotra [1995]) that appears to have ef-
ﬁciency comparable to the factorization in (6.16) and improved stability.
Yang and Zenios [1995] have, however, demonstrated substantial speed-ups
using the Proposition 6 factorization with parallel processors.
We should note that the solution times for factorization and the dual
approach for the problems in Table 1 are still signiﬁcantly greater than
times for using the L-shaped method, although, for the larger problems,
they were faster than the MINOS extreme point algorithm. There may, of
course, also be some exceptions where these procedures outperform decom-
position. The key reason for this decomposition advantage appears to be
the ability to solve multiple subproblems quickly after one subproblem is
solved because many subproblems have the same optimal basis. Because a
basis requires an extreme point, this type of approach does not seem possi-
ble for interior point methods. Interior point methods that allow repeated
solutions for many subproblems and use the same search direction in these
problems may, however, oﬀer similar advantages to decomposition methods.
Research is continuing into these alternative interior point approaches.
Exercises
1. Compare the number of operations to solve (6.3) using (6.4) and
(6.5) compared to solving (6.3) as an unstructured linear system of
equations.
2. Give a similar basis factorization scheme to (6.4) and (6.5) to solve
the backward transformation, (σT , πT )B = (cT
B, qT
B), for a basis cor-
responding to columns B from the constraint matrix of (1.1).
3. Describe an eﬃcient updating procedure for any possible combination
of entering and leaving columns in the basis matrix of (6.3) using the
factorization scheme in (6.4) and (6.5).


## Page 211

192
5. Two-Stage Linear Recourse Problems
4. Find the number of arithmetic operations for a single step of the
interior point method using (6.16). Compare this to the number of
arithmetic operations if no special factorization is used.
5. Compare the sizes of the adjacency matrices in (6.14) and (6.26). As-
suming that each matrix A, Tk, and W is completely dense, compare
the number of nonzero entries in these two matrices.
5.7
Special Cases—Simple Recourse and Network
Problems
In many stochastic programming problems, special structure provides addi-
tional computational advantages. The most common structures that allow
for further eﬃciencies are simple recourse and network problems. The key
features of these problems are separability of any nonlinear objective terms
and eﬃcient matrix computations.
Separability is the key to simple recourse computations. In Section 3.1,
we described how these problems involve a recourse function that separates
into components for each random variable. The stochastic program with
simple recourse can then be written as:
min z = cT x +
m2

i=1
Ψi(χi)
(7.1)
s.t. Ax = b,
Tx −χ = 0,
x ≥0,
where Ψi(χi) =

hi≤χi q−(χi −hi)dF(hi)+

hi>χi q+(hi −χi)dF(hi). Using
this form of the objective in χ, we can substitute in (3.1.9) to obtain:
Ψi(χi) = q+
i ¯hi −(q+
i −qiFi(χi))χi −qi

hi≤χi
hidF(hi),
(7.2)
where ¯hi = E[hi].
The separable objective terms in (7.1) oﬀer advantages for computation.
In the next chapter, we discuss nonlinear programming techniques that
can apply when the random variables are continuous. Linear programming-
based procedures can, however, be used when the random variables have a
ﬁnite number of values. In this section, we assume that each hi can take
on the values, hi,j, j = 1, . . . , Ki with probabilities, pi,j.
Wets [1983a] gave the basic framework for computation of ﬁnitely dis-
tributed simple recourse problems as a linear program with upper bounded


## Page 212

5.7 Special Cases—Simple Recourse and Network Problems
193
variables. The idea is to split χi into values corresponding to each interval,
[hi,j, hi,j+1], so that
χi =
Ki

j=0
χi,j, χi,0 ≤hi,1, 0 ≤χi,j ≤hi,j+1 −hi,j, 0 ≤χi,Ki.
(7.3)
The objective coeﬃcients correspond to the slope of Ψ(χi) in each of these
intervals. They are
di,0 = −q+
i , di,j = −q+
i + qi(
j

l=1
pi,l), j = 1, . . . , Ki.
(7.4).
The piecewise linear program with these objective coeﬃcients and variables
is
minz = cT x +
m2

i=1
((
Ki

j=0
di,jχi,j) + q+
i ¯hi)
(7.5)
s.t. Ax = b,
Tx −χ = 0,
x ≥0 and (7.3).
The equivalence of (7.1) and (7.5) is given in the following theorem.
Theorem 7. Problems (7.1) and (7.5) have the same optimal values and
sets of optimal solutions, (x∗, χ∗).
Proof: We ﬁrst show any solution (x, χ1, . . . , χm2) to (7.1) corresponds to a
solution (x, χ1, . . . , χm2, χ1,1, . . . , χm2,Km2) to (7.5) with the same objective
value. We then also show the reverse to complete the proof. Suppose (x, χ)
feasible in (1). If hi,j ≤χi < hi,j+1 for some 1 ≤j ≤Ki, then let χi,0 =
hi,1, χi,l = hi,l+1 −hi,l, 1 ≤l ≤j −1, χi,j = χi −hi,j and χi,l = 0, l ≥j +1.
If χi < hi,0, then let χi,0 = χi, χi,l = 0, l ≥1. In this way, we satisfy (7.3).
If χi ≥hi,1, the variable i objective term in (7.5) with these values is
then
q+
i ¯hi −q+
i (hi,1+
j−1

l=1
(hi,l+1 −hi,l) + (χi −hi,j))
+qi[(
j−1

l=1
[(
l

k=1
pi,k)(hi,l+1 −hi,l)] +
j

k=1
pi,k(χi −hi,j)]
= q+
i ¯hi −q+
i χi + qi[([
j−1

k=1
pi,k[
j−1

l=k
(hi,l+1 −hi,l) −hi,j]]
−pi,jhi,j +
j

k=1
pi,kχi]


## Page 213

194
5. Two-Stage Linear Recourse Problems
= q+
i ¯hi −q+
i χi −qi(
j

k=1
pi,khi,k) + qi(
j

k=1
pi,k)χi)
= q+
i ¯hi −q+
i χi −qi

hi≤χi
hidF(hi) + qiFi(χi)χi
= Ψi(χi),
(7.6)
where the last equality follows from substitution in (7.2).
If χi < hi,1, then the objective term is q+
i ¯hi −q+
i χi which again agrees
with Ψi(χi) from (7.2). Hence, any feasible (x, χ) in (7.1) corresponds to a
feasible (x, χ) (where χ is extended into the components for each interval)
in (7.5).
Suppose now that some (x∗, χ∗) is optimal in (7.5). Because each qi > 0
and pi,j > 0, for hi,j ≤χ∗
i < hi,j+1 for some 1 ≤j ≤Ki, we must
have χ∗
i,0 = hi,1, χ∗
i,l = hi,l+1 −hi,l, 1 ≤l ≤j −1, χ∗
i,j = χ∗
i −hi,j and
χ∗
i,l = 0, l ≥j + 1. If not, then χ∗
i,l < hi,l+1 −hi,l −δ for some l ≤j −1 and
χ∗
i,¯l > δ > 0 for some ¯l ≥j + 1. A feasible change of increasing χ∗
i,l by δ
and decreasing χ∗
i,¯l by δ yields an objective decrease of δqi
	¯l
s=l+1 pi,s and
would contradict optimality. Hence, we must have that the ith objective
term in (7.5) is again Ψi(χ∗
i ). Similarly, this must be true if χ∗
i < hi,1.
Therefore, any optimal solution in (7.1) corresponds to a feasible solution
with the same objective value in (7.5), and any optimal solution in (7.5)
corresponds to a feasible solution with the same objective value in (7.1).
Their optima must then correspond.
This formulation as an upper bounded variable linear program can lead
to signiﬁcant computational eﬃciencies. An implementation in Kallberg,
White, and Ziemba [1982] uses this approach in a short-term ﬁnancial
planning model with 12 random variables with three realizations, each
corresponding to uncertain cash requirements and liquidation costs. They
solve the stochastic model with problem (7.5) in approximately 1.5 times
the eﬀort to solve the corresponding mean value linear program with ex-
pected values substituted for all random variables. This result suggests that
stochastic programs with simple recourse can be solved in a time of about
the same order of magnitude as a deterministic linear program ignoring
randomness.
Further computational advantages for these problems are possible by
treating the special structure of the χi,j variables as χi variables with
piecewise, linear convex objective terms. Fourer [1985, 1988] presents an
eﬃcient simplex method approach for these problems. This implementa-
tion lends further support to the similar mean value problem–stochastic
program order of magnitude claim.
Decomposition methods can also be applied to the simple recourse prob-
lem with ﬁnite distributions, although solution times better than the mean-
value linear programming solution would generally be diﬃcult to obtain.


## Page 214

5.7 Special Cases—Simple Recourse and Network Problems
195
As mentioned in Section 3, the multicut approach oﬀers some advantage for
the L-shaped algorithm (in terms of major iterations), but solution times
are generally at best comparable with the mean-value linear program time.
For generalized programming, because Ψ(χ) = 	m2
i=1 Ψi(χi) and each
Ψi(χi) is easily evaluated, the subproblem in (5.10) is equivalent to ﬁnding
χν
i such that
−πν
i ∈∂Ψi(χν
i ).
(7.7)
From (7.4) and the argument in Proposition 5.1, ∂Ψi(χi) = {di,j} for
hi,j < χi < hi,j+1 and ∂Ψi(χi) = [di,j−1, di,j] for hi,j = χi. Thus, we can
choose χν
i = hi,j for di,j−1 ≤−πν
i ≤di,j, j = 1, . . . , Ki. If πν
i < −q+
i ,
then the value in (5.10) is unbounded. The algorithm chooses ζs+1
i
= −1,
and Ψ+
0,i(−1) = q+
i . In this way, generalized programming can be imple-
mented easily, but would appear similar to the piecewise linear approach
given earlier. The advantage of generalized programming is more apparent,
however, when continuous distributions cause nonlinearities as we discuss
in the next chapter.
In network problems, the simple recourse formulation can be even more
eﬃciently solved. Suppose, for example, that the random variables hi cor-
respond to random demands at m2 destinations, that the variables xst are
ﬂows from s to t, Ax = b corresponds to the network constraints for all
source nodes, transshipment nodes, and destinations with known demands,
and that Tx represents all the ﬂows entering the destinations with random
demand. By adding the constraint,
m2

i=1
(
li

j=1
χi,j) −

sources s

t
xst = −

known demand destinations r
demand(r),
(7.8)
every variable in (7.5) corresponds to a ﬂow so that (7.5) becomes a network
linear program. Hence, eﬃcient network codes can be applied directly to
(7.5) in this case.
When T has gains and losses, (7.5) is a generalized network. This problem
was one of the ﬁrst types of practical stochastic linear programs solved when
Ferguson and Dantzig [1956] used the generalized network form to give an
eﬃcient procedure for allocating aircraft to routes (ﬂeet assignment). We
describe this problem to show the possibilities inherent in the stochastic
program structure.
The problem includes m1 aircraft and m2 routes. The decision variables
are xsr aircraft s allocated to route r. The number of aircraft s available is
bs, the passenger capacity of aircraft s on route r is tsr, and the uncertain
passenger demand is hr. Hence, the ith row of Ax = b is 	m2
r=1 xir = bi.
The jth row of Tx −χ = 0 is 	m1
s=1 tsjxsj −χj = 0.
The key observation about this problem is that the basis corresponds
to a pseudo-rooted spanning forest (see, e.g., Bazaraa, Jarvis, and Sherali
[1990]). For this problem, the simplex steps solve with trees and one-trees


## Page 215

196
5. Two-Stage Linear Recourse Problems
in an eﬃcient manner. For example, suppose m1 = 3, m2 = 3, b = (2, 2, 2),
t1· = (200, 100, 300), t2· = (300, 100, 200), and t3· = (400, 100, 150), pi,j =
0.5, and h1,1 = 500, h1,2 = 700, h2,1 = 200, h2,2 = 400, h3,1 = 200,
h3,2 = 400. A basic solution is x1,1 = 1, x1,2 = 1, x2,1 = 1, x2,2 = 1,
x3,3 = 4/3, and χ3,1 = 100 with all other variables nonbasic. This basis is
illustrated in Figure 4. The forest consists of a cycle and a subtree. Exercises
1, 2, and 3 explore this example in more detail.
FIGURE 4. Graph of basic arcs for aircraft-route assignment example.
For general network problems, Sun, Qi and Tsai [1990] describe a piecewise
linear network method that allows the use of network methods and does
not require adding the additional arcs that correspond to the χi,j values.
Other generalizations for network structured problems allow continuous
distributions and apply directly to the nonlinear problem. We discuss these
methods in more detail in the next chapter.
The methods all apply to simple recourse problems in which the ﬁrst-
stage variables represent a network. Another class of problems includes
network constraints in the second (and following) stages. These problems
are called network recourse problems. In this case, some computational
advantages are again possible.
Most computational experience with solving these problems directly has
been with the L-shaped method. The eﬃciencies occur in constructing fea-
sibility constraints, in generating facets of the polyhedral convex recourse
function, and in solving multiple recourse problems using small Schur com-
plement updates of a network basis. These procedures are described in Wal-
lace [1986b]. Other methods for network recourse problems involve nonlin-
ear programming-based procedures. We will also describe these approaches
in the next chapter.
Exercises
1. Show that any basis for the aircraft allocation problem consists of a
collection of m1 + m2 basic variables that correspond to a collection
of trees and one-trees.


## Page 216

5.7 Special Cases—Simple Recourse and Network Problems
197
2. Describe a procedure for ﬁnding the values of basic variables, multi-
pliers, reduced costs, and entering and leaving basic variables for the
structure in the aircraft allocation problem.
3. Solve the aircraft allocation problem using the procedure in (7.2)
starting at the basis given with cost data corresponding to c1· =
(300, 200, 100), c2· = (400, 100, 300), c3· = (200, 100, 300), q+
i
= 25,
q−
i = 0 for all i. You may ﬁnd it useful to use the graph to compute
the appropriate values.


## Page 217



## Page 218

6
Nonlinear Programming
Approaches to Two-Stage Recourse
Problems
In Chapter 5, we considered methods that were fundamentally large-scale
linear programming procedures. When the stochastic program includes
nonlinear terms or when continuous random variables are explicitly in-
cluded, a ﬁnite-dimensional linear programming deterministic equivalent
no longer exists. In this case, we must use some nonlinear programming
types of procedures.
This chapter describes the basic nonlinear programming approaches ap-
plied to stochastic programs. In Sections 1 and 2, we begin by describing
enhancements of the L-shaped method to include a quadratic regulariza-
tion term and to allow for quadratic objective terms. Section 3 describes
methods based on the stochastic program Lagrangian. Section 4 gives pro-
cedures that are specially constructed for simple recourse problems, while
Section 5 describes some other basic approaches.
6.1
Regularized Decomposition
Regularized decomposition is a method that combines a multicut approach
for the representation of the second-stage value function with the inclusion
in the objective of a quadratic regularizing term. This additional term is
included to avoid two classical drawbacks of the cutting plane methods. One
is that initial iterations are often ineﬃcient. The other is that iterations may
become degenerate at the end of the process. Regularized decomposition


## Page 219

200
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
was introduced by Ruszczy´nski [1986]. We present a somewhat simpliﬁed
version of his algorithm using the notation of Section 5.3.
The Regularized Decomposition Method
Step 0. Set r = ν = 0, s(k) = 0 for all k = 1, · · · , K. Select a1, a feasible
solution.
Step 1. Set ν = ν + 1. Solve the regularized master program
min cT x +
K

k=1
θk + 1
2∥x −aν∥2
(1.1)
s.t. Ax= b,
Dℓx≥dℓ,
ℓ= 1, . . . , r,
Eℓ(k)x + θk≥eℓ(k),
ℓ(k) = 1, . . . , s(k),
x≥0 .
Let (xν, θν) be an optimal solution to (1.1) where (θν)T = (θν
1, · · · , θν
K)T is
the vector of θk’s. If s(k) = 0 for some k, θν
k is ignored in the computation.
If cT xν + eT θν = cT aν + Q(aν), stop; aν is optimal.
Step 2. As before, if a feasibility cut (5.1.3) is generated, set aν+1 = aν
(null infeasible step), and go to Step 1.
Step 3. For k = 1, . . . , K, solve the linear subproblem (5.1.9). Compute
Qk(xν). If (5.3.5) holds, add an optimality cut (5.3.4) using formulas (5.3.6)
and (5.3.7). Set s(k) = s(k + 1).
Step 4. If (5.3.5) does not hold for any k, then aν+1 = xν (exact serious
step); go to Step 1.
Step 5. If cT xν + Q(xν) ≤cT aν + Q(aν), then aν+1 = xν (approximate
serious step); go to Step 1. Else, aν+1 = aν (null feasible step), go to
Step 1.
Observe that when a serious step is made, the value Q(aν+1) should be
memorized, so that no extra computation is needed in Step 1 for the test
of optimality. Note also that a more general regularization would use a
term of the form α∥x −aν∥2 with α > 0. This would allow tuning of the
regularization with the other terms in the objective. As will be illustrated
in Exercise 2, regularized decomposition works better when a reasonable
starting point is chosen.
Example 1
Consider Exercise 1 of Section 5.3. Take a1 = −0.5 as a starting point. It
corresponds to the solution of the problems with ξ = ¯ξ with probability 1.
We have Q(a1) = 3/8.


## Page 220

6.1 Regularized Decomposition
201
Iteration 1: Cuts θ1 ≥0, θ2 ≥−3
4x are added. Let a2 = a1.
Iteration 2: The regularized master is
min θ1 + θ2 + 1
2(x + 0.5)2
s.t. θ1 ≥0, θ2 ≥−3
4x
with solution x2 = 0.25 : θ1 = 0, θ2 = −3/16. A cut θ2 ≥0 is added. As
Q(0.25) = 0 < Q(a1), a3 = 0.25 (approximate serious step 1).
Iteration 3: The regularized master is
min θ1 + θ2 + 1
2(x −0.25)2
s.t. θ1 ≥0, θ2 ≥−3
4x, θ2 ≥0
with solution x3 = 0.25, θ1 = 0, θ2 = 0. Because θν = Q(aν), a solution is
found.
In Exercise 1, the L-shaped and multicut methods are compared. The
value of a starting point is given in Exercise 2.
We now describe the main results needed to prove convergence of the
regularized decomposition to an optimal solution when it exists. For no-
tational convenience, we drop the ﬁrst-stage linear terms cT x in the rest
of the section. This poses no theoretical diﬃculty, as we may either deﬁne
θk = pk(cT x + Qk(x)), k = 1, · · · , K or add a (K + 1)th term θK+1 = cT x.
With this notation, the original problem can be written as
min Q(x) =
K

k=1
pkQk(x)
(1.2)
s.t. (5.1.2), x ≥0,
and Qk(x) = min{qT
k y|Wy = hk −Tkx, y ≥0}. This is equivalent to
min eT θ =
K

k=1
θk
(1.3)
s.t. (5.1.2), (5.1.3), (5.3.4), x ≥0,
provided all possible cuts (5.1.3) and (5.3.4) are included.
The regularized master program is
min η(x, θ, aν) =
K

k=1
θk + 1
2∥x −aν∥2
(1.4)
s.t. (5.1.2), (5.1.3), (5.3.4), x ≥0.


## Page 221

202
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
Note, however, that in the regularized master, only some of the potential
cuts (5.1.3) and (5.3.4) are included. We follow the proof in Ruszczy´nski
[1986].
Lemma 1. eT θν ≤η(xν, θν, aν) ≤Q(aν).
Proof:
The ﬁrst inequality simply comes from ∥xν −aν∥2 ≥0. We then
observe that aν always satisﬁes (5.1.2), (5.1.3), as a1 is feasible and the se-
rious steps always pick feasible aνs. The solution (aν, ˆθ) obtained by choos-
ing ˆθk = pkQk(aν), k = 1, · · · , K necessarily satisﬁes all constraints (5.3.4)
as θk is a lower bound on pkQk(·). Thus, η(xν, θν, aν) ≤η(aν, ˆθ, aν) =
Q(aν).
Lemma 2. If the algorithm stops at Step 1, then aν solves the original
problem (1.2).
Proof: By Lemma 1 and the optimality criterion, eT θν = Q(aν) (remember
the linear term cT x has been dropped). It follows that eT θν = η(xν, θν, aν),
which implies ∥xν−aν∥2 = 0, hence xν = aν. Thus, aν solves the regularized
master (1.4) with the cuts (5.1.3) and (5.3.4) available at iteration ν. The
cone of feasible directions at aν does not include any direction of descent of
η(x, θ, aν). The cone of feasible directions at xν for problem (1.3) is included
in the cone of feasible directions at iterations ν of the regularized master
((1.4) contains fewer cuts). Moreover, the gradient of the regularizing term
vanishes at aν. Thus, the descent directions of the regularized program
(1.4) are the same as the descent directions of (1.3). Hence, aν solves (1.3),
which means aν solves the original program (1.2).
Lemma 3. If there is a null step at iteration ν, then
η(xν+1, θν+1, aν+1) > η(xν, θν, aν) .
Proof:
Because the objective function of the regularized master is strictly
convex, program (1.4) has a unique solution. A null step at iteration ν may
be either a null infeasible step or a null feasible step. In the ﬁrst case, a
cut (5.1.3) is added that renders xν infeasible. In the second case, a cut
(5.3.4) is added that renders (xν, θν) infeasible. Thus, as the previous so-
lution becomes infeasible and the solution is unique, the objective function
necessarily increases.
Lemma 4. If the number of serious steps is ﬁnite, the algorithm stops at
Step 1.
Proof: If the number of serious steps is ﬁnite, there exists some ν0 such that
aν = aν0 for all ν ≥ν0. By Lemma 3, this implies the objective function of
the regularized master strictly increases at each iteration ν, ν ≥ν0. Because


## Page 222

6.1 Regularized Decomposition
203
there are only ﬁnitely many possible cuts (5.1.3) and (5.3.4), the algorithm
must stop.
Lemma 5. The number of approximate serious steps is ﬁnite.
Proof:
By deﬁnition of Step 5, the value of Q(·) does not increase in an
approximate serious step (remember that the term cT x is dropped here).
Approximate serious steps only happen when Q(xν)̸ = eT θν. This can only
happen ﬁnitely many times because the number of cuts (5.3.4) is ﬁnite.
Lemma 6. If the algorithm does not stop, then either Q(aν) tends to −∞
as ν →∞or the sequence {aν} converges to a solution of the original
problem.
Proof:
(i) Let us ﬁrst consider the case in which the original problem has
solution ˆx. Deﬁne ˆθ by ˆθk = pkQk(ˆx). Thus (ˆx, ˆθ) solves (1.3). Also (ˆx, ˆθ)
must be feasible for the regularized master for all ν. Because (xν, θν) is
the solution of the regularized master at iteration ν, the derivative of η at
(xν, θν) in the direction (ˆx −xν, ˆθ −θν) must be non-negative, i.e.,
(xν −aν)T (ˆx −xν) + eT ˆθ −eT θν ≥0
or
(xν −aν)T (xν −ˆx) ≤Q(ˆx) −eT θν,
(1.5)
because eT ˆθ = Q(ˆx).
Let S be the set of iterations at which serious steps occur. In view of
Lemma 5, without loss of generality, we may consider such a set where all
serious steps are exact. Because, for an exact serious step, eT θν = Q(xν),
(5.3.5) does not hold for any k, and xν = aν+1 by deﬁnition of the step,
for all ν ∈S, (1.5) may be rewritten as
(aν+1 −aν)T (aν+1 −ˆx) ≤Q(ˆx) −Q(aν+1).
By properties of sums of sequences,
∥aν+1 −ˆx∥2 = ∥aν −ˆx∥2 + 2(aν+1 −aν)T (aν+1 −ˆx) −∥aν+1 −aν∥2.
By dropping the last terms and using the inequality, for all ν ∈S,
∥aν+1 −ˆx∥2≤∥aν −ˆx∥2 + 2(aν+1 −aν)T (aν+1 −ˆx)
(1.6)
≤∥aν −ˆx∥2 + 2(Q(ˆx) −Q(aν+1)).
Because Q(ˆx) ≤Q(aν+1) for all ν, ∥aν+1 −ˆx∥≤∥aν −ˆx∥, i.e., the sequence
{aν} is bounded.
Now (1.6) can be rearranged as
2(Q(aν+1) −Q(ˆx)) ≤∥aν −ˆx∥2 −∥aν+1 −ˆx∥2.


## Page 223

204
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
Summing up both sides for ν ∈S, it can be seen that

ν∈S
(Q(aν+1) −Q(ˆx)) < ∞,
which implies Q(aν+1) →Q(ˆx) for some subsequence {aν}, ν ∈S1 where
S1 ⊆S. Therefore, there must exist an accumulation point ˆa of {aν} with
Q(ˆa) = Q(ˆx). All aν are feasible, hence ˆa is feasible and ˆa may substitute
for ˆx in (1.6) implying ∥aν+1 −ˆa∥≤∥aν −ˆa∥, which shows that ˆa is the
only accumulation point of {aν}.
ii) Now assume that the original problem is unbounded but {Q(aν)} is
bounded. Thus one can ﬁnd a feasible ˆx and an ε > 0 such that Q(ˆx) ≤
Q(aν)−ε , ∀ν. Then (1.6) gives ∥aν+1 −ˆx∥2 ≤∥aν −ˆx∥2 −2ε, which yields
a contradiction as ν →∞, ν ∈S.
Lemma 7. If the algorithm does not stop and Q{aν} is bounded, there
exists ν0 such that if a serious step occurs at ν ≥ν0, then the solution
(xν, θν) of (1.4) is also a solution of (1.4) without the regularizing term.
Proof:
Let Kν denote the set of (x, θ) that satisfy all constraints (5.1.2),
(5.1.3), (5.3.4) at iteration ν. The problem (1.4) without the regularizing
term is thus:
min eT θ
s.t. (x, θ) ∈Kν.
(1.7)
Assume Lemma 7 is false. It is thus possible to ﬁnd an inﬁnite set S such
that, for all ν ∈S, a serious step occurs and the solution (xν, θν) to (1.4)
is not optimal for (1.7).
Let K∗
ν denote the normal cone to the cone of feasible directions for Kν
at (xν, θν). Nonoptimality of (xν, θν) means that the negative gradient of
the objective in (1.7), −d =

0
−e
̸
∈K∗
ν. As this holds for all ν ∈S,
−d̸ ∈∪ν∈S K∗
ν .
(1.8)
Now Kν is polyhedral. There can only be a ﬁnite number of constraints
(5.1.2) and cuts (5.1.3) and (5.3.4). Thus, the right-hand-side of (1.8) is the
union of a ﬁnite number of closed sets and, hence, is closed. There exists
an ε > 0 such that
B(−d, ε) ∩K∗
ν = ∅, ∀ν ∈S,
(1.9)
where B(−d, ε) denotes the ball of radius ε centered at −d. On the other
hand, (xν, θν) solves (1.4); hence,
−∇η(xν, θν, aν) ∈K∗
ν, ∀ν ∈S .
(1.10)


## Page 224

6.1 Regularized Decomposition
205
By Lemma 6, aν →ˆx. By Lemma 5, there exists a ν0 such that for ν ≥
ν0, eT θν = Q(aν) for all serious steps. Hence, at serious steps ν ≥ν0, we
have
Q(aν) ≥η(xν, θν, aν) = 1
2∥aν −xν∥2 + eT θν
= 1
2∥xν −aν∥2 + Q(aν).
This implies xν →aν, ∀ν ∈S. Hence,
∇η(xν, θν, aν) →d ∀ν ∈S,
and (1.10) contradicts (1.9).
Theorem 8. If the original problem has a solution, then the algorithm
stops after a ﬁnite number of iterations. Otherwise, it generates a sequence
of feasible points {aν} such that Q(aν) tends to −∞as ν →∞.
Proof:
By Lemma 2, the algorithm may only stop at a solution. Suppose
the original problem has a solution but the algorithm does not stop. By
Lemma 6, {aν} converges to a solution ˆx. Lemma 5 implies that for all ν
large enough, all serious steps are exact, i.e.,
Q(aν+1) = eT θν.
By Lemma 7, for ν large enough, xν also solves (1.4) without the regular-
izing term implying
eT θν ≤Q(ˆx),
because problem (1.4) without the regularizing term is a relaxation of the
original problem. Because Q(ˆx) ≤Q(aν) for all ν, it follows that, for ν large
enough, Q(xν) = Q(ˆx). Thus, no more serious steps are possible, which by
Lemma 4 implies ﬁnite termination. The unbounded case was proved in
Lemma 6.
Implementation of the regularized decomposition algorithm poses a num-
ber of practical questions, such as controlling the size of the master reg-
ularized problem and numerical stability. An implementation using a QR
factorization and an active set strategy is described in Ruszczy´nski [1986].
On the problems tested by the author (see also Ruszczy´nski [1993b]) the
regularized decomposition method outperforms all other methods. This in-
cludes a regularized version of the L-shaped method, the L-shaped method,
or the multicut method. It is conﬁrmed in the experiments made by Kall
and Mayer [1996].
Exercises
1. Check that, with the same starting point, both the L-shaped and the
multicut methods require ﬁve iterations in Example 1.


## Page 225

206
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
2. The regularized decomposition only makes sense with a reasonable
starting point. To illustrate this, consider the same example taking
as starting point a highly negative value, e.g., a1 = −20. At Iteration
1, the cuts θ1 ≥−x−1
2
and θ2 ≥−3
4x are created. Observe that,
for many subsequent iterations, no new cuts are generated as the
sequence of trial points aν move from −20 to −75
4 , then −70
4 , −65
4 , · · ·
each time by a change of
5
4, until reaching 0, where new cuts will
be generated. Thus a long sequence of approximate serious steps is
taken.
3. As we mentioned in the introduction of this section, the regularized
decomposition algorithm works with a more general regularizing term
of the form α
2 ∥x −aν∥2.
(a) Observe that the proof of convergence relies on strict convexity
of the objective function (Lemma 3), thus α > 0 is needed. It
also relies on ∇α
2 ∥xν −aν∥2 →0 as xν →aν, which is simply
obtained by taking a ﬁnite α. The algorithm can thus be tuned
for any positive α and α can vary within the algorithm.
(b) Taking the same starting point and data as in Exercise 2, show
that by selecting diﬀerent values of α, any point in ] −20, 20]
can be obtained as a solution of the regularized master at the
second iteration (where 20 is the upper bound on x and the ﬁrst
iteration only consists of adding cuts on θ1 and θ2).
(c) Again taking the same starting point and data as in Exercise
2, how would you take α to reduce the number of iterations?
Discuss some alternatives.
(d) Let α = 1 for Iterations 1 and 2. As of Iteration 2, consider the
following rule for changing α dynamically. For each null step, α
is doubled. At each exact step, α is halved. Show why this would
improve the performance of the regularized decomposition in the
case of Exercise 2. Consider the starting point x1 = −0.5 as in
Example 1 and observe that the same path as before is followed.
6.2
The Piecewise Quadratic Form of the
L-Shaped Method
In this section, we consider two-stage quadratic stochastic programs of the
form
min z(x) = cT x + 1
2xT Cx+ Eξ[min[qT (ω)y(ω) + 1
2yT (ω)D(ω)y(ω)]] (2.1)


## Page 226

6.2 The Piecewise Quadratic Form of the L-Shaped Method
207
s.t. Ax = b,
T(ω)x + Wy(ω) = h(ω),
x ≥0,
y(ω) ≥0,
where c, C, A, b, and W are ﬁxed matrices of size n1 × 1, n1 × n1, m1 ×
n1, m1 × 1, and m2 × n2, respectively and q, D, T, and h are random ma-
trices of size n2 × 1, n2 × n2, m2 × n1, and m2 × 1, respectively. Compared
to the linear case deﬁned in (3.1.1), only the objective function is mod-
iﬁed. As usual, the random vector ξ is obtained by piecing together the
random components of q, D, T, and h. Although more general cases could
be studied, we also make the following two assumptions.
Assumption 9. The random vector ξ has a discrete distribution.
Recall that an n × n matrix M is positive semi-deﬁnite if xT Mx ≥0 for
all x ∈ℜn and M is positive deﬁnite if xT Mx > 0 for all 0̸ = x ∈ℜn.
Assumption 10. The matrix C is positive semi-deﬁnite and the matrices
D(ω) are positive semi-deﬁnite for all ω. The matrix W has full row rank.
The ﬁrst assumption guarantees the existence of a ﬁnite decomposition
of the second-stage feasibility set K2. The second assumption guarantees
that the recourse functions are convex and well-deﬁned.
We may again deﬁne the recourse function for a given ξ(ω) by:
Q(x, ξ(ω))= min{qT (ω)y(ω) + 1
2yT (ω)D(w)y(w)|
(2.2)
T(ω)x + Wy(ω) = h(ω), y(ω) ≥0},
(2.3)
which is −∞or +∞if the problem is unbounded or infeasible, respectively.
The expected recourse function is
Q(x) = EξQ(x,ξ)
with the convention +∞+ (−∞) = +∞.
The deﬁnitions of K1 and K2 are as in Section 3.4. Theorem 3.32 and
Corollaries 3.34 and 3.35 apply, i.e., Q(x) is a convex function in x and
K2 is convex. Of greater interest to us is the fact that Q(x) is piecewise
quadratic. Loosely stated, this means that K2 can be decomposed in poly-
hedral regions called the cells of the decomposition and in addition to being
convex, Q(x) is quadratic on each cell.
Example 2
Consider the following quadratic stochastic program
min z(x) = 2x1 + 3x2 + Eξ min{−6.5y1 −7y2 + y2
1
2 + y1y2 + y2
2
2 }


## Page 227

208
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
s.t. 3x1 + 2x2 ≤15, y1 ≤x1 , y2 ≤x2
x1 + 2x2 ≤8, y1 ≤ξ1 , y2 ≤ξ2
x1 + x2 ≥0, x1, x2 ≥0, y1 , y2 ≥0.
This problem consists of ﬁnding some product mix (x1, x2) that satisﬁes
some ﬁrst-stage technology requirements. In the second stage, sales cannot
exceed the ﬁrst-stage production and the random demand. In the second
stage, the objective is quadratic convex because the prices are decreas-
ing with sales. We might also consider ﬁnancial problems where minimiz-
ing quadratic penalties on deviations from a mean value leads to eﬃcient
portfolios.
Assume that ξ1 can take the three values 2, 4, and 6 with probability
1/3, that ξ2 can take the values 1, 3, and 5 with probability 1/3, and that
ξ1 and ξ2 are independent of each other. For very small values of x1 and x2,
it always is optimal in the second stage to sell the production, y1 = x1 and
y2 = x2. More precisely, for 0 ≤x1 ≤2 and 0 ≤x2 ≤1, y1 = x1, y2 = x2
is the optimal solution of the second stage for all ξ. If needed, the reader
may check this using the Karush-Kuhn-Tucker conditions.
Thus, Q(x, ξ) = −6.5x1 −7x2 + x2
1
2 + x1x2 + x2
2
2 for all ξ and Q(x) =
−6.5x1 −7x2 + x2
1
2 + x1x2 + x2
2
2 . Here, the cell is {(x1, x2)|0 ≤x1 ≤2, 0 ≤
x2 ≤1}. Within that cell, Q(x) is quadratic.
Deﬁnition 11. A ﬁnite closed convex complex K is a ﬁnite collection of
closed convex sets, called the cells of K, such that the intersection of two
distinct cells has an empty interior.
Deﬁnition 12. A piecewise convex program is a convex program of the
form inf{z(x)|x ∈S} where f is a convex function on IRn and S is a closed
convex subset of the eﬀective domain of f with nonempty interior.
Let K be a ﬁnite closed convex complex such that
(a) the n-dimensional cells of K cover S,
(b) either f is identically −∞or for each cell Cν of the complex there
exists a convex function zν(x) deﬁned on S and continuously
diﬀerentiable on an open set containing Cν which satisﬁes
i. z(x) = zν(x) ∀x ∈Cν, and
ii. ∇zν(x) ∈∂z(x) ∀x ∈Cν.
Deﬁnition 13. A piecewise quadratic function is a piecewise convex func-
tion where on each cell Cν the function zν is a quadratic form.


## Page 228

6.2 The Piecewise Quadratic Form of the L-Shaped Method
209
Taking Example 2, we have both Q(x) and z(x) piecewise quadratic. On
C1 = {0 ≤x1 ≤2, 0 ≤x2 ≤1},
Q1(x) = −6.5x1 −7x2 + x2
1
2 + x1x2 + x2
2
2
and z1(x) = −4.5x1 −4x2 + x2
1
2 + x1x2 + x2
2
2 .
Deﬁning a polyhedral complex was ﬁrst done by Walkup and Wets [1967]
for the case of stochastic linear programs. Based on this decomposition,
Gartska and Wets [1974] proved that the optimal solution of the second
stage is a continuous, piecewise linear function of the ﬁrst-stage decisions
and showed that Q(x, ξ) is piecewise quadratic in x. It follows that under
Assumption 1, Q(x) and z(x) are also piecewise quadratic in x.
For the sake of completeness, observe that z(x) is not always maxν zν(x).
To this end, consider
z(x) =

z1(x) = x
2
when 0 ≤x ≤2,
z2(x) = (x −1)2
when x ≥2.
This function is easily seen to be piecewise quadratic. On (0, 1/2), z(x) =
z1(x) while max{z1(x), z2(x)} = z2(x).
An algorithm
In this section, we study a ﬁnitely convergent algorithm for piecewise
quadratic programs (Louveaux [1978]).
Algorithm PQP
Initialization: Let S1 = S, x0 ∈S, ν = 1.
Iteration ν:
i. Obtain Cν, a cell of the decomposition of S containing xν−1.
Let zν(.) be the quadratic form on Cν.
ii. Let xν ∈arg min{zν(x)|x ∈Sν} and wν ∈arg min{zν(x)|x
∈Cν}. If wν is the limiting point of a ray on which zν(x) is
decreasing to −∞, the original PQP is unbounded and the
algorithm terminates.
iii. If
∇T zν(wν)(xν −wν) = 0,
(2.4)
then stop; wν is an optimal solution.
iv. Let Sν+1 = Sν ∩{x|∇T zν(wν)x ≤∇T zν(wν)wν}. Let ν =
ν + 1; go to Step i.
Thus, contrary to the L-shaped method in the linear case, the subgradi-
ent inequality is not applied at the current iterate point xν. Instead, it is


## Page 229

210
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
applied at wν, a point where zν(.) is minimal on Cν. Under some prac-
tical conditions on the constructions of the cells, the algorithm is ﬁnitely
convergent.
We ﬁrst prove that the condition,
∇T zν(wν)x ≤∇T zν(wν)wν,
(2.5)
is a necessary condition for optimality of x.
Because ∇zν(wν) ∈∂z(wν), the subgradient inequality applied at wν
implies that z(x) ≥z(wν) + ∇T zν(wν)(x −wν) for all x. Now, x is a
minimizer of z(.) only if z(x) ≤z(wν). This implies that x is a minimizer of
z(.) only if ∇T zν(wν)(x−wν) ≤0, which is precisely (2.5). Thus, a solution
x ∈arg min{z(x)|x ∈Sν} is also a solution x ∈arg min{z(x)|x ∈S}.
We next show that any solution x ∈arg min{zν(x)|x ∈Sν} is a solu-
tion ∈arg min{z(x)|x ∈Sν} (and thus by the argument, a solution is in
arg min{z(x)|x ∈S}) if x ∈Cν.
By deﬁnition, x ∈arg min{zν(x)|x ∈Sν} is a solution of a quadratic
convex program whose objective is continuously diﬀerentiable on Sν; it
must satisfy the condition ∇T zν(x)(x −x) ≥0, ∀x ∈Sν. If x ∈Cν, then
∇zν(x) ∈∂z(x). Applying the subgradient inequality for z(.) at x implies
z(x) ≥z(x) + ∇T zν(x)(x −x) ≥z(x) ∀x ∈Sν .
Thus, if x ∈Cν, it is a solution to the original problem.
Finally, if the optimality condition (2.4) holds, applying the gradient
inequality to the quadratic convex function zν(.) at wν implies
zν(xν) ≥zν(wν) + ∇T zν(wν)(xν −wν) = zν(wν) ,
which proves wν ∈arg min{zν(x)|x ∈Sν}. Thus, wν is (another) minimizer
of zν(.) on Sν. As wν ∈Cν, the conclusion implies it is a solution to
the original problem. A more detailed proof, including properties of the
successive sets Sν and a discussion of the construction of full dimensional
cells of a piecewise quadratic program, can be found in Louveaux [1978].
Exercises
1. For Example 2, consider the values x1 = 4.5, x2 = 0. Check that
around these values, y2 = x2 for all ξ2, and
y1 =

ξ1
if ξ1 = 2 or 4,
x1
if ξ1 = 6
are the optimal second-stage decisions. Check that the corresponding
cell is deﬁned as
{(x1, x2)|4 ≤x1 ≤6, 0 ≤x2 ≤1, x1 + x2 ≤6.5}


## Page 230

6.2 The Piecewise Quadratic Form of the L-Shaped Method
211
and
z(x) = −29
3 −x1
6 −2x2 + x2
1
6 + x1x2
3
+ x2
2
2 .
2. We now apply the PQP algorithm to the problem of Example 2.
Initialization: x0 = (0, 0); ν = 1
S1 = S = {x|3x1 + 2x2 ≤15, x1 + 2x2 ≤8, x1, x2 ≥0}.
Iteration 1:
As we saw earlier, C1 = {x|0 ≤x1 ≤2, 0 ≤x2 ≤1} and z1(x) =
−4.5x1 −4x2 + x2
1
2 + x1x2 + x2
2
2 . Using the classical Karush-Kuhn-
Tucker condition, we obtain x1 = (4.5, 0)T and w1 = (2, 1)T ∈C1.
Hence, ∇T z1(w1) = (−1.5, −1), ∇T z1(w1)(x1 −w1) = −2.75̸ = 0,
and
S2 = S ∩{x| −1.5x1 −x2 ≤−4}.
Iteration 2:
As we saw in Exercise 1, x1 ∈C2 = {x|4 ≤x1 ≤6, 0 ≤x2 ≤
1, x1 + x2 ≤6.5} and
z2(x) = −29
3 −x1
6 −2x2 + x2
1
6 + x1x2
3
+ x2
2
2 .
We obtain x2 =
 22
19, 43
19
T , a point where the optimality constraint
−1.5x1 −x2 ≤−4 is binding. We also obtain w2 =

4, 2
3
T ∈C2,
∇T z2(w2) = (25/18, 0)T , and (2.3) does not hold.
S3 = S2 ∩

x|25
18x1 ≤100
18

.
Iteration 3:
i. We now obtain x2 ∈C3 = {x|0 ≤x1 ≤2, 1 ≤x2 ≤3}. In
the second stage, y1 = x1∀ξ1, y2 = x2 when ξ2 ≥3 and
y2 = 1 when ξ2 = 1, so that
z3(x) = −13
6 −25
6 x1 −5
3x2 + x2
1
2 + 2x1x2
3
+ x2
2
3 .
ii. x3 = (4, 0)T ; w3 = w1 = (2, 1)T .
iii. S4 = S3 ∩{x| −3
2x1 + x2
3 ≤−8
3}.
Iteration 4:
i. x3 ∈C4 = {x|2 ≤x1 ≤4, 0 ≤x2 ≤1}.
z4(x) = −11
3 −7
3x1 −10
3 x2 + x2
1
3 + 2x1x2
3
+ x2
2
2 .
ii. x4 ≃(2.18, 1.81)T , a point where −3
2x1 + x2
3 = −8
3.
w4 = (2.5, 1).


## Page 231

212
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
iii. S5 = S4 ∩{x| −2x2
3
≤−2
3}.
Iteration 5:
i. x4 ∈C5 = {x|2 ≤x1 ≤4, 1 ≤x2 ≤3} ∩S.
z5(x) = −101
18 −19
9 x1 −11
9 x2 + x2
1
3 + 4x1x2
9
+ x2
2
3 .
ii. x5 = w5 = (2.5, 1)T is an optimal solution to the problem.
FIGURE 1. The cells and PQP cuts of Example 2.
The PQP iterations for the example are shown in Figure 1. The thin-
ner lines represent the limits of cells and the constraints containing
S. The heavier lines give the optimality cuts, OCν, for ν = 1, 2, 3, 4.
A few comments are in order:
(a) Observe that the objective values of the successive iterate
points are not necessarily monotone decreasing. As an example,
z1(w1) = −8.5 and z2(w2) = −71
9 > z1(w1).
(b) A stronger version of (2.4) can be obtained. Let z = minν{z(wν)}
be the best known solution at iteration ν. Starting from the sub-
gradient inequality at wν,
z(x) ≥z(wν) + ∇zT
ν (wν)(x −wν)


## Page 232

6.2 The Piecewise Quadratic Form of the L-Shaped Method
213
and observing that z(x) ≤z is a necessary condition for opti-
mality, we obtain an updated cut,
∇T zν(wν)x ≤∇T zν(wν)wν + z −z(wν).
(2.6)
Updating is quite easy, as it only involves the right-hand sides
of the cuts.
As an example, at Iteration 2, the cut could be
updated from
25x1
18
≤100
18 to 25
18x1 ≤100
18 −8.5 + 71
9 ,
namely, 25x1
18
≤89
18. Similarly, at Iteration 4, z becomes −103
12
and the right-hand sides of all previously imposed cuts can be
modiﬁed by

−103
12 + 8.5

, i.e., by −1
12. In the example, the up-
dating does not change the sequence of iterations.
(c) The number of iterations is strongly dependent on the starting
point. In particular, if one cell exists such that the minimizer of
its quadratic form over S is in fact within the cell, then starting
from that cell would mean that a single iteration would suﬃce.
In Example 2, this is not the case. However, starting from {x|2 ≤
x1 ≤4, 1 ≤x2 ≤3} would require only two iterations. This is
in fact a reasonable starting cell. Indeed, the intersection of the
two nontrivial constraints deﬁning S,
3x1 + 2x2 ≤15, x1 + 2x2 ≤8,
is the point (3.5, 2.25) that belongs to that cell. (An alternative
would be to start from the minimizer of the mean value problem
on S.)
(d) If we observe the graphical representation of the cells and of the
cuts, we observe that the cuts each time eliminate all points of
a cell, except possibly the point wν at which they are imposed,
and possibly other points on a face of dimension strictly less than
n1. (Working with updated cuts (2.6) sometimes also eliminates
the point wν at which it is imposed.) The ﬁnite termination of
the algorithm is precisely based on the elimination of one cell
at each iteration. (We leave aside the question of considering
cells of full dimension n1.) There is thus no need at iteration
ν to start from a cell containing xν−1. In fact, any cell not yet
considered is a valid candidate. One reasonable candidate could
be the cell containing xν−1 + wν−1
2
, for example, or any convex
combination of xν−1 and wν−1.
3. Consider the farming example of Section 1.1. As in Exercise 1.1, as-
sume that prices are inﬂuenced by quantities. As an individual, the


## Page 233

214
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
farmer has little inﬂuence on prices, so he may reasonably consider
the current solution optimal. If we now consider that all farmers read
this book and optimize their choice of crop the same way, increases
of sales will occur in parallel for all farmers, bringing large quanti-
ties together on the market. Taking things to an extreme, this means
that changes in the solution are replicated by all farmers. Assume a
decrease in selling prices of $0.03 per ton of grain and of $0.06 per
ton of corn brought into the market by each individual farmer. As-
sume the selling price of beets and purchase prices are not aﬀected
by quantities.
Show that the PQP algorithm reaches the solution in one iteration
when the starting point is taken as {x1, x2, x3|80 ≤x2 ≤100; 250 ≤
x3 ≤300; x1+x2+x3 = 500}. (Remark: Although only one iteration is
needed, calculations are rather lengthy. Observe that constant terms
are not needed to obtain the optimal solution.)


## Page 234

6.3 Methods Based on the Stochastic Program Lagrangian
215
6.3
Methods Based on the Stochastic Program
Lagrangian
Again consider the general nonlinear stochastic program given in (3.4.1),
which we repeat here without equality constraints to simplify the following
discussion:
inf z =
f 1(x) + Q(x)
s. t.
g1
i (x) ≤0,
i = 1, . . . , m1,
(3.1)
where Q(x) = Eω[Q(x, ω)] and
Q(x, ω) =
inf f 2(y(ω), ω) s. t.
b2
i (x, ω) + g2
i (y(ω), ω)
≤0, i = 1, . . . , m2,
(3.2)
with the continuity assumptions mentioned in Section 3.4.
In general, we can consider a variety of approaches to (3.1) based on avail-
able nonlinear programming methods. For example, we may consider gra-
dient projection, reduced gradient methods, and straightforward penalty-
type procedures, but these methods all assume that gradients of Q are
available and relatively inexpensive to acquire. Clearly, this is not the case
in stochastic programs because each evaluation may involve solving several
problems (3.2). Lagrangian approaches have been proposed to avoid this
problem.
The basic idea behind the Lagrangian approaches is to place the ﬁrst-
and second-stage links into the objective so that repeated subproblem opti-
mizations are avoided in ﬁnding search directions. To see how this approach
works, consider writing (3.1) in the following form:
inf z = f 1(x) + Eω[f 2(y(ω), ω)]
s. t. g1
i (x)≤0, i = 1, . . . , m1,
b2
i (x, ω) + g2
i (y(ω), ω)≤0, i = 1, . . . , m2, a. s.
(3.3)
If we let (λ, π) be a multiplier vector associated with the constraints, then
we can form a dual problem to (3.3) as:
max
π(ω)≥0 w = θ(π),
(3.4)
where
θ(π) =
infx,y z =
f 1(x) + Eω[f 2(y(ω), ω)]
+Eω[	m2
i=1 π(ω)i(b2
i (x, ω) + g2
i (y(ω), ω))]
s. t.
g1
i (x) ≤0, i = 1, . . . , m1.
(3.5)
We show duality in the ﬁnite distribution case in the following theorem.
Theorem 14. Suppose the stochastic nonlinear program (3.1) with all
functions convex has a ﬁnite optimal value and a point strictly satisfying


## Page 235

216
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
all constraints, and suppose Ω= {1, . . . , K} with P{ω = i} = pi. Then
z ≥w for every feasible x, y1, . . . , yK in (3.1-2) and π1, . . . , πK feasible in
(3.4), and their optimal values coincide, z∗= w∗.
Proof:
From the general optimality conditions (see, e.g., Bazaraa and
Shetty [1979, Theorem 6.2.1]), the result follows by noting that we may
take x satisfying the ﬁrst-period constraints as a general convex constraint
set X so that only the second-period constraints are placed into the dual.
We also divide any multipliers on the second-period constraints in (3.3) by
pi if they correspond to ω = i. In this way, the expectation over ω in (3.5)
is obtained.
Now, we can follow a dual ascent procedure in (3.4). This takes the form
of a subgradient method. We note that
∂θ(¯π) = co{(ζ1
1, . . . , ζ1
m2)T , . . . , (ζK
1 , . . . , ζK
m2)T },
(3.6)
where co denotes the convex hull,
ζk
i = b2
i (¯x, k) + g2
i (¯yk, k),
(3.7)
and (¯x, ¯y1, . . . , ¯yK) solves the problem in (3.5) given π = ¯π. This again
follows from standard theory as in, for example, Bazaraa and Shetty [1979,
Theorem 6.3.7].
We can now describe a basic gradient method for the dual problem. For
our purposes, we assume that (3.5) always has a unique solution.
Basic Lagrangian Dual Ascent Method
Step 0. Set π0 ≥0, ν = 0 and go to Step 1.
Step 1. Given π = πν in (3.5), let the solution be (xν, yν
1, . . . , yν
K). Let ˆπk
i =
0 if πν,k
i
= 0 and b2
i (xν, k) + g2
i (yν
k, k) ≤0, and ˆπk
i = b2
i (xν, k) + g2
i (yν
k, k),
otherwise. If ˆπk = 0 for all k, stop.
Step 2. Let λν minimize θ(πν + λˆπ) over πν + λˆπ ≥0, λ ≥0. Let πν+1 =
πν + λνˆπ, ν = ν + 1, and go to Step 1.
Assuming the unique solution property, this algorithm always produces
an ascent direction in θ. The algorithm either converges ﬁnitely to an op-
timal solution or, assuming a bounded set of optima, produces an inﬁnite
sequence with all limit points optimal (see Exercise 1). For the case of
multiple optima for (3.5), some nondiﬀerentiable procedure must be used.
In this case, one could consider ﬁnding the maximum norm subgradient
to be assured of ascent or one could use various bundle-type methods (see
Section 4).
The basic hope for computational eﬃciency in the dual ascent procedure
is that the number of dual iterations is small compared to the number


## Page 236

6.3 Methods Based on the Stochastic Program Lagrangian
217
of function evaluations that might be required by directly attacking (3.1)
and (3.2). Substantial time may be spent solving (3.5) but that should be
somewhat easier than solving (3.1) because the linking constraints appear
in the objective instead of hard constraints. Overall, however, this type of
procedure is generally slow due to our using only a single-point linearization
of θ. This observation has led to other types of Lagrangian approaches to
(3.1) that use more global or second-order information.
Rockafellar and Wets [1986] suggested one such procedure for a special
case of (3.5) where f 1(x) = cT x + 1
2xT Cx and y(ω) can be eliminated so
that the second and third objective terms in (3.5) are:
Φ(π, x) = Eω[π(ω)T (h(ω) −T(ω)x) −1
2π(ω)T D(ω)π(ω)].
(3.8)
In fact, this is always possible if b2(x, ω) = T(ω)x, g2(y(ω), ω) = Wy(ω) −
h(ω), and f2(y(ω), ω)) = q(ω)T y(ω) + 1
2y(ω)T D(ω)y(ω) (Exercise 2). The
dual problem in (3.4) is then
max
π≥0
inf
{x|g1(x)≤0}[cT x + 1
2xT Cx + Φ(π, x)].
(3.9)
In fact, Rockafellar and Wets allowed more general constraints on π that
may depend on ω.
Their approach is, however, not to restrict the search to a single search
direction but to allow optimization over a low dimensional set in [ℜm2
+ ]Ω.
At iteration ν, they replace [ℜm2
+ ]Ωby Πν, and iteratively update this ap-
proximation by including not just the gradient direction of the Lagrangian
but the best π(ω) for the ﬁxed value of x = xν in Φ(π, x). This point, πν+1,
is used to create the new Πν. The process repeats as follows.
Lagrangian
Finite
Generation
Method
for
Linear-Quadratic
Stochastic Programs
Step 0. Choose Π0, set ν = 0, and go to Step 1.
Step 1. Solve (3.9) with the constraint, π ∈Πν, in place of π ≥0. Let
the solution be (πν, xν) with value, LBν = θ(πν) (a lower bound on the
optimal objective value).
Step 2. Find πν+1(ω) for each ω to maximize [π(ω)T (h(ω) −T(ω)xν) −
1
2π(ω)T D(ω)π(ω)] over π(ω) ≥0. (Notice that this optimization ﬁnds
maxπ≥0 Φ(π, xν).) Let UBν = cT xν + 1
2xν,T Cxν + Φ(πν+1, xν) (an up-
per bound on the optimal objective value). If UBν −LBν < ǫ, then stop
with an ǫ-optimal solution.


## Page 237

218
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
Step 3. Update Πν to Πν+1 by ensuring that Πν+1 includes πν and πν+1
(and any other part but not necessarily all of Πν). Let ν = ν + 1, and go
to Step 1.
An implementation of this algorithm is described in King [1988a]. The
method was used successfully to solve practical water management prob-
lems concerning Lake Balaton in Hungary (Somly´ody and Wets [1988]).
The algorithm produces a convergent sequence to an optimum provided
that the set Πν+1 is suﬃciently large and the matrix C is positive deﬁnite
(enforcing strict convexity). In general, the choice of Πν+1 is similar to those
in cutting plane methods. On linear pieces of the objective, restricting Πν+1
too severely may lead to cycling. The alternatives discussed in Eaves and
Zangwill [1971] can be used to control this.
The ﬁnite generation method is similar to other methods based on inner
linearization approaches in nonlinear programming such as the restricted
simplicial decomposition approach (Ventura and Hearn [1993]). This proce-
dure essentially replaces the line search in the Topkis-Veinott [1967] feasible
direction method with a search over a simplex. The ﬁnite generation algo-
rithm is analogously an enhancement over basic Lagrangian dual ascent
methods. Both the ﬁnite generation and restricted simplicial decomposi-
tion methods tend to avoid the zigzagging behavior that often occurs in
methods based on single point linearizations.
Another method for speeding convergence is to enforce strictly convex
terms in the objective. Rockafellar and Wets discussed methods for adding
quadratic terms to the matrices C and D(ω) so that these matrices become
positive deﬁnite. In this way, the ﬁnite generation method becomes a form
of augmented Lagrangian procedure. We next discuss the basic premise
behind these procedures.
In an augmented Lagrangian approach, one generally adds a penalty
r∥(b2
i (¯x, k) + g2
i (¯yk, k))+∥2 to θ(π) and performs the iterations including
this term. The advantage (see the discussion in Dempster [1988]) is that
Newton-type steps can be applied because we would obtain a nonsingular
Hessian. The result should generally be that convergence becomes super-
linear in terms of the dual objective without a signiﬁcantly greater compu-
tational burden over the Lagrangian approach.
The computational experience reported by Dempster suggests that few
dual iterations need be used but that a more eﬀective alternative was to
include explicit nonanticipative constraints as in (3.4.4) and to place these
constraints into the objective instead of the full second-period constraints.
In this way, θ becomes
θ′(ρ) = inf z =f 1(x) +
K

k=1
pk[f 2(yk, k)]


## Page 238

6.3 Methods Based on the Stochastic Program Lagrangian
219
+
K

k=1
[ρT
k (x −xk) + r/2∥x −xk∥2]
s. t. g1
i (x) ≤0, i = 1, . . . , m1,
b2
i (xk, k) + g2
i (yk, k) ≤0, i = 1, . . . , m2,
k = 1, . . . , K.
(3.10)
Notice how in (3.10) the only links between the nonanticipative x decision
and the scenario k decisions are in the (x −xk) objective terms. Dempster
suggests solving this problem approximately on each dual iteration by iter-
ating between searches in the x variables and search in the xk, yk variables.
In this way, the augmented Lagrangian approach of solving (3.10) to ﬁnd
a dual ascent Newton-type direction achieves superlinear convergence in
dual iterations. The only problem may come in the time to construct the
search directions through solutions of (3.10).
This method also resembles the progressive hedging algorithm of Rock-
afellar and Wets [1991]. Their method achieves a full separation of the
separate scenario problems for each iteration and, therefore, has consider-
ably less work at each iteration. However, the number of iterations as we
shall see, may be greater. The method appears to oﬀer many computa-
tional advantages at least for structured problems as reported by Mulvey
and Vladimirou [1991a]. The key to this method’s success is that individual
subproblem structure is maintained throughout the algorithm. Related im-
plementations by Nielsen and Zenios [1993a, 1993b] on parallel processors
demonstrate possibilities for parallelism and the solution of large problems.
The basic progressive hedging method begins with a nonanticipative so-
lution ˆxν and a multiplier ρν. The nonanticipative (but not necessarily fea-
sible) solution is used in place of x in (3.10). The ﬁrst-period constraints
are also split into each xk. In this way, we obtain a subproblem:
inf z =
K

k=1
pk[f 1(xk) + f 2(yk, k)+ρν,T
k
(xk −ˆxν) + r/2∥xk −ˆxν∥2]
s. t. g1
i (xk)≤0, i = 1, . . . , m1, k = 1, . . . , K,
b2
i (xk, k) + g2
i (yk, k)≤0, i = 1, . . . , m2, k = 1, . . . , K.
(3.11)
Now (3.11) splits directly into subproblems for each k so these can be
treated separately.
Supposing that (xν+1
k
, yν+1
k
) solves (3.11). We obtain a new nonantici-
pative decision by taking the expected value of xν+1 as ˆxν+1 and step in ρ
by ρν+1 = ρν + (xν+1 −ˆxν+1).
The steps then are simply stated as follows.
Progressive Hedging Algorithm
Step 0. Suppose some nonanticipative x0, some initial multiplier ρ0, and
r > 0. Let ν = 0. Go to Step 1.


## Page 239

220
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
Step 1. Let (xν+1
k
, yν+1
k
) for k = 1, . . . , K solve (3.11). Let ˆxν+1 = (ˆxν+1,1,
. . . , ˆxν+1,K)T where ˆxν+1,k = 	K
l=1 plxν+1,l for all k = 1, . . . , K.
Step 2. Let ρν+1 = ρν + r(xν+1,k −ˆxν+1). If ˆxν+1 = ˆxν and ρν+1 = ρν,
then, stop; ˆxν and ρν are optimal. Otherwise, let ν = ν + 1 and go to 1.
The convergence of this method is based on Rockafellar’s proximal point
method [1976a]. The basis for this approach is not dual ascent but the
contraction of the pair, (ˆxν+1, ρν+1), about an optimal point. The key is
that the algorithm mapping can be described as (Πxν+1, ρν+1/r) = (I −
V )−1(Πxν, ρν/r), where V is a maximal monotone operator and Π is the
diagonal matrix of probabilities corresponding to xk and ρk, i.e, where
Π(k−1)n1+i,(k−1)n1+i = pk for i = 1, . . . , n1 and k = 1, . . . , K.
To describe this approach we ﬁrst deﬁne a maximal monotone operator
at V (see Minty [1961] for more general details) such that for any pairs
(w, z) where z ∈V (w) and (w′, z′) for z′ ∈V (w′), we have
(w −w′)T V (z −z′) ≥0.
(3.12)
The key point here is that if we have a Lagrangian function l(x, y) that is
convex in x and concave in y, then the subdiﬀerential set of l(x, y) at (¯x, ¯y)
deﬁned by
{(ζ, η)|ζT (x −¯x) + l(¯x, ¯y) ≤l(x, ¯y), ∀x; ηT (y −¯y) + l(¯x, ¯y) ≥l(¯x, y), ∀y}
(3.13)
yields a maximal monotone operator by
V (¯x, ¯y) = {(ζ, η)}
(3.14)
for (ζ, −η) ∈∂l(¯x, ¯y) (Exercise 3).
The second result that follows for maximal monotone operators is that
a contraction mapping can be deﬁned on it by taking (I −V )−1(x, y) to
obtain (x′, y′), or, equivalently, where (x′ −x, y′ −y) ∈V (x′, y′). The
contraction result (Exercise 4) is that, if V is maximal monotone, then, for
all (x′, y′) = (I −(1/r)V )−1(x, y) and (¯x′, ¯y′) = (I −V )−1(¯x, ¯y),
∥(x′ −¯x′, y′ −¯y′)∥2 ≤(x −¯x, y −¯y)T (x′ −¯x′, y′ −¯y′).
(3.15)
These results then play the fundamental role in the following proof of con-
vergence.
Theorem 15. The progressive hedging algorithm, applied to (3.1) with the
same conditions as in Theorem 14, converges to an optimal solution, x∗, ρ∗,
(or terminates ﬁnitely with an optimal solution) and, at each iteration that
does not terminate in Step 2,
∥(Πˆxν+1, ρν+1/r) −(Πx∗, ρ∗/r)∥< ∥(Πˆxν, ρν/r) −(Πx∗, ρ∗)/r∥.
(3.16)


## Page 240

6.3 Methods Based on the Stochastic Program Lagrangian
221
Proof: As stated, the key is to ﬁnd the associated Lagrangian and to show
that the iterations follow the mapping as in (3.15). For the Lagrangian,
deﬁne
l(¯x, ¯ρ) = infx
(1/r)z(x) + ¯ρT Πx
s. t.
JΠx −¯x = 0,
(3.17)
where z(x) is deﬁned as 	K
k=1[f 1(xk) + Q(xk, k)] for feasible xk and as
+∞otherwise, Π is deﬁned as the diagonal probability matrix, and J is
the matrix corresponding to column sums, Jr,s equal one if r
(mod n1) =
s
(mod n1) and zero otherwise. We want to show that (Π(ˆxν−ˆxν+1), (ρν−
ρν+1)/r) ∈∂l(Πˆxν+1, ρν+1/r), so we can use the contraction property in
(3.15) from the maximal monotone operator deﬁned on ∂l(Πˆxν+1, ρν+1/r).
Note that, for ¯x = Πˆxν and ¯ρ = ρν/r = 	ν
i=1(xi −ˆxi), ¯xT ¯ρ = ˆxν,T
Π(	ν
i=1(xi −ˆxi)) = (x′)ν,T JΠ(	ν
i=1(xi −ˆxi)) for (x′)ν,T = (1/K)ˆxν,T .
Because JΠxi = ˆxi, we have ¯xT ¯ρ = 0. We can thus add the term, ¯xT ¯ρ to
the objective in (3.17) without changing the problem. We then obtain:
η ∈∂¯ρl(¯x, ¯ρ) ⇔−Π¯ρ ∈(1/r)∂z(Π−1(−η) + ¯x) + πT JΠ,
(3.18)
where JΠ(Π−1(−η)) = ¯x and π is some multiplier. For ∂¯xl(¯x, ¯ρ), ζ =
−πT JΠ, and some π,
ζ ∈∂¯xl(¯x, ¯ρ) ⇔ζ −Π¯ρ ∈(1/r)∂Z(x′),
(3.19)
for some JΠx′ = ˆx. We combine (3.18) and (3.19) to obtain that (ζ, η) ∈
∂l(¯x, ¯ρ) if
ζ −Π¯ρ ∈(1/r)∂z(Π−1(−η) + ¯x).
(3.20)
We wish to show that
Π(ˆxν −ˆxν+1) −Πρν+1/r ∈(1/r)∂z(Π−1(ρν+1 −ρν)/r + ˆxν+1).
(3.21)
From the algorithm,
−Πρν ∈∂z(xν+1) + rΠ(xν+1 −ˆxν).
(3.22)
Substituting, ρν+1 = ρν + r(xν+1 −ˆxν+1), we obtain from (3.22),
−Πρν+1 + rΠ(xν+1 −ˆxν+1) ∈∂z(xν+1) + rΠ(xν+1 −ˆxν),
(3.23)
which, after eliminating rΠxν+1 from both sides, coincides with (3.21).
By the nonexpansive property, there exists (Πx∗, ρ∗/r), a ﬁxed point
of this mapping. By substituting into (3.15), with (Πx∗, ρ∗/r) = (I −
V )(Πx∗, ρ∗/r) and (Πˆxν+1, ρν+1/r) = (I −V )(Πˆxν, ρν/r), we have (Ex-
ercise 5):
∥(Πˆxν+1, ρν+1/r) −(Πx∗, ρ∗/r)∥< ∥(Πˆxν, ρν+1/r) −(Πx∗, ρ∗/r)∥. (3.24)
Our result follows if (x∗, ρ∗) is indeed a solution of (3.1). Note that in
this case, we must have 0 = xν+1 −ˆxν+1 = xν+1 −ˆxν, so, from (3.22),


## Page 241

222
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
−Πρ∗∈∂z(x∗). From Theorem 3.2.5, optimality in (3.1) is equivalent
to ρT Π ∈∂z(x∗) for some ρ, where JΠρ = 0, which is true because
JΠ(−ρ∗) = −	
ν JΠ(xν+1 −xν) = 0. Hence, we obtain optimality. The
method converges as desired.
We note that Rockafellar and Wets obtained these results by deﬁning
an inner product as < ρ, x > = ρT Πx and using appropriate operations
with this deﬁnition. They also show that, in the linear-quadratic case, the
convergence to optimality is geometric.
Variants of this method are possible by considering other inner products
and projection operators. For example, we can let ˆ¯x
ν+1 be the standard
orthogonal projection of xν+1 into the null space of JΠ. This value is the
simple average of xν+1
k
values, so that ˆ¯x
ν+1
k
(i) = (1/K) 	K
k=1 xν+1
k
(i) for
all k = 1, . . . , K. The multiplier update is then:
ρν+1 = ρν + rΠ−1(xν+1 −ˆ¯x
ν+1).
(3.25)
One can again obtain the maximal monotone operator property, and, ob-
serving that Jxν+1 = Jˆ¯x
ν+1, obtain JΠρ∗= 0 and optimality.
Example 3
The algorithm’s geometric convergence may require many iterations even
on small problems as we show in the following small example. Suppose we
can invest $10,000 in either of two investments, A or B. We would like
a return of $25,000, but the investments have diﬀerent returns according
to two future scenarios. In the ﬁrst scenario, A returns just the initial
investment while B returns 3 times the initial investment. In the second
scenario, A returns 4 times the initial investment and B returns twice the
initial investment.The two scenarios are considered equally likely. To reﬂect
our goal of achieving $25,000, we use an objective that squares any return
less than $25,000. The overall formulation is then:
min z =
0.5(y2
1 + y2
2)
s. t.
xA + xB ≤10,
xA + 3xB + y1 ≥25,
4xA + 2xB + y2 ≥25,
xA, xB, y1, y2 ≥0.
(3.26)
Clearly, this problem has an optimal solution at x∗
A = 2.5 and x∗
B = 7.5
with an objective value z∗= 0. A single iteration of Step 1 in the basic
Lagrangian method is all that would be required to solve this problem for
any positive π value. A single iteration is also all that would be necessary in
the augmented Lagrangian problem in (3.10). The price for this eﬃciency
is, however, the incorporation of all subproblems into a single master prob-
lem. Progressive hedging on the other hand maintains completely separate
subproblems. We will follow the ﬁrst two iterations of PHA for r = 2 here.


## Page 242

6.3 Methods Based on the Stochastic Program Lagrangian
223
Iteration 0:
Step 0. Begin with a multiplier vector of ρ0 = 0, and let x0
1 = (x0
1A, x0
1B) =
(0, 10)T and let x0
2 = (x0
2A, x0
2B) = (10, 0)T . The initial value of ˆx0 =
(5, 5)T .
Step 1. We wish to solve:
min(1/2)[y2
1 + y2
2 + (x1
1A −5)2 + (x1
1B −5)2+(x1
2A −5)2 + (x1
2B −5)2]
s. t. x1
1A + x1
1B≤10,
x1
2A + x1
2B≤10,
x1
1A + 3x1
1B −y1≥25,
4x1
2A + 2x1
2B −y2≥25,
x1
1A, x1
1B, x1
2A, x1
2B, y1, y2 ≥0.
(3.27)
This problem splits into separate subproblems for x1
1A, x1
1B, y1 and x1
2A,
x1
2B, y2, as mentioned earlier. For x1
1A, x1
1B, y1 feasible in (3.27), the K-K-T
conditions are that there exist λ1 ≥0, λ2 ≥0 such that
2(x1
1A −5) + λ1 −λ2≥0,
2(x1
1B −5) + λ1 −3λ2≥0,
2y1 −λ2≥0,
(2(x1
1A −5) + λ1 −λ2)x1
1A= 0,
(2(x1
1B −5) + λ1 −3λ2)x1
1B= 0,
(2y1 −λ2)y1= 0,
(x1
1A + x1
1B −10)λ1= 0,
(x1
1A + 3x1
1B −y1 −25)λ2= 0,
(3.28)
which has a solution of (x1
1A, x1
1B, y1) = (10/3, 20/3, 5/3) and (λ1, λ2) =
(20/3, 10/3). Similar conditions exist for the second subproblem, which has
a solution (x1
2A, x1
2B, y2) = (5, 5, 0). We then let (ˆx1
iA, ˆx1
iB) = (4 1
6, 5 5
6) for
i = 1, 2.
Step 2. The new multiplier is ρ1 = (ρ1
1A, ρ1
1B, ρ1
2A, ρ1
2B)T = 2((10/3 −
25/6), (20/3 −35/6), (5 −25/6), (5 −35/6))T = (−5/3, 5/3, 5/3, −5/3)T .
Iteration 2:
Step 1. The ﬁrst subproblem is now
min y2
1 −(5/3)(x2
1A −25/6) + (5/3)(x2
1B −35/6)+(x2
1A −25/6)2
+(x2
1B −35/6)2
s. t. x2
1A + x2
1B≤10,
x2
1A + 3x2
1B −y1≥25,
x2
1A, x2
1B, y1≥0,
(3.29)
which again has an optimal solution, (x2
1A, x2
1B, y2
1) = (10/3, 20/3, 5/3).
Curiously, we also have the second subproblem solution of (x2
2A, x2
2B, y2
2) =
(10/3, 20/3, 0). In this case, (ˆx2
iA, ˆx2
iB) = (10/3, 20/3) for i = 1, 2.


## Page 243

224
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
TABLE 1. PHA iterations for Example 3.
k
ˆxk
A
ˆxk
B
ρk
1A
ρk
1B
xk
1A
xk
1B
xk
2A
xk
2B
= −ρk
2A
= −ρk
2B
0
5.0
5.0
0.0
0.0
3.33
6.67
5.0
5.0
1
4.17
5.83
-1.67
1.67
3.33
6.67
3.33
6.67
2
3.33
6.67
-1.67
1.67
3.06
6.94
2.50
7.50
3
2.78
7.22
-1.11
1.11
2.78
7.22
2.41
7.59
4
2.59
7.41
-0.74
0.74
2.65
7.35
2.41
7.59
5
2.53
7.47
-0.49
0.49
2.59
7.41
2.43
7.57
6
2.50
7.50
-0.33
0.33
2.56
7.44
2.45
7.55
7
2.50
7.50
-0.22
0.22
2.54
7.46
2.46
7.54
8
2.50
7.50
-0.15
0.15
2.53
7.48
2.48
7.52
9
2.50
7.50
-0.10
0.10
2.52
7.48
2.48
7.52
10
2.50
7.50
-0.07
0.07
2.51
7.49
2.49
7.51
11
2.50
7.50
-0.04
0.04
2.51
7.49
2.49
7.51
12
2.50
7.50
-0.03
0.03
2.50
7.50
2.50
7.50
Step 2. Because the subproblems returned the same solution, ρ2 = ρ1. We
continue because the x values changed, even though we took no multiplier
step.
The full iteration values are given in Table 1. Notice how the method
achieves convergence in the x values before the ρ values have converged.
Also, notice how the convergence appears to be geometric. This type of per-
formance appears to be typical of PHA. It should be noted again, however,
that the iterations are quite simple and that little overhead is required.
Exercises
1. Show that the basic dual ascent method converges to an optimal
solution under the conditions given.
2. Show that (3.4) can be reduced to (3.9) when b2(x, ω) = T(ω)x,
g2(y(ω), ω) = Wy(ω) −h(ω), f 2(y(ω), ω)) = q(ω)T y(ω) + 1
2y(ω)T
D(ω)y(ω), and D is positive deﬁnite.
3. Show that V as deﬁned in (3.14) is a maximal monotone operator.
4. Prove the contraction property in (3.15).
5. Use (3.15) to obtain (3.24).
6. Apply the dual ascent method and the augmented Lagrangian
method with problem (3.10) to the example in (3.26). Start with


## Page 244

6.4 Nonlinear Programming in Simple Recourse Problems
225
zero multipliers (ρ), positive π, and positive penalty r. Show that
each obtains an optimal solution in at most one iteration.
6.4
Nonlinear Programming in Simple Recourse
Problems
The previous sections considered basically nonlinear problems that could be
modeled with deterministic equivalents when the number of random vari-
able realizations was ﬁnite. As mentioned in Chapter 5, the simple recourse
problem may allow computation even when the underlying distribution is
continuous. Recall that the simple recourse problem has the form:
min z = cT x +
m2

i=1
Ψi(χi)
(4.1)
s.t. Ax = b,
Tx −χ = 0,
x ≥0,
where Ψi(χi) =

hi≤χi q−(χi −hi)dF(hi)+

hi>χi q+(hi −χi)dF(hi). Using
this form of the objective in χ, we again substitute in (3.1.9) to obtain:
Ψi(χi) = q+
i ¯hi −(q+
i −qiFi(χi))χi −qi

hi≤χi
hidFi(hi).
(4.2)
The most direct methods for solving (4.1) are to use standard nonlinear
programming techniques. We brieﬂy describe some of the alternatives here.
The most common procedures applied here are single-point linearization
approaches, such as the Frank-Wolfe method, multiple-point linearization,
such as generalized linear programming, and active set or reduced vari-
able methods, similar to simplex method extensions. Other methods are
described in Nazareth and Wets [1986].
The Frank-Wolfe method for simple recourse problems appears in Wets
[1966] and Ziemba [1970]. The basic procedure is to approximate the ob-
jective using the gradient and to solve a linear program to ﬁnd a search
direction. The algorithm contains the following basic steps. We assume that
each random variable hi has an absolutely continuous distribution function
Fi so that each Ψi is diﬀerentiable. In this case, the gradient of Ψ(Tx) is
easily calculated as ∇Ψ(Tx) = (q+ −q)T ( ¯F)T, where ¯F = diag{Fi(Ti·x)},
the diagonal matrix of the probability that hi is below Ti·x.
Frank-Wolfe Method for Simple Recourse Problems
Step 0. Suppose a feasible solution x0 to (4.1). Let ν = 0. Go to Step 1.


## Page 245

226
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
Step 1. Let ˆxν solve:
min z = (cT + (q+ −q)T ( ¯F ν)T)x
(4.3)
s.t. Ax = b,
x ≥0,
where ¯F ν = diag{Fi(Ti·xν)}.
Step 2. Find xν+1 to minimize cT (xν + λ(ˆxν −xν)) + 	m2
i=1 Ψi(T(xν +
λ(ˆxν −xν))) over 0 ≤λ ≤1. If xν+1 = xν, stop with an optimal solution.
Otherwise, let ν = ν + 1 and return to Step 1.
The basis for this approach is that x∗is optimal in (4.1) if and only if x∗
solves (4.3) with x∗= xν. If xν is not a solution of (4.1), then xν+1̸ = xν,
and descent occurs along ˆxν −xν. Exercise 1 asks for the details of this
convergence result.
The L-shaped method and generalized linear programming can be con-
sidered extensions of the linearization approach that use multiple points
of linearization. We have already considered the L-shaped method in some
detail in the previous chapter. For generalized programming, the key ad-
vantage is that Ψ(χ) is separable. Williams [1966] and Beale [1961] observed
the advantage of this property and gave generalized programming proce-
dures for speciﬁc problems. In the case of the general problem in (4.1), the
master problem of (3.5.6)–(3.5.9) becomes
min zν = cT x +
m2

j=1
(
rj

i=1
µjiΨ0+
j (ζji) +
sj

i=1
λjiΨj(χji))
(4.4)
s.t. Ax = b,
(4.5)
Ti·x −
rj

i=1
µjiζji −
sj

i=1
λjiχji = 0, j = 1, . . . , m2,
(4.6)
sj

i=1
λji = 1,
(4.7)
x, µji ≥0, i = 1, . . . , rj; λji ≥0, i = 1, . . . , sj, j = 1, . . . , m2,
where we can divide the components of χ in the constraints because of the
separability.
We then have a subproblem of the form in (3.5.10) for each j:
min
χj Ψj(χj) + πν
j χj −ρν
j .
(4.8)
We can create an entering column whenever any of the values in (4.8) is
negative. If all are non-negative, then the algorithm again terminates with
an optimal value.


## Page 246

6.4 Nonlinear Programming in Simple Recourse Problems
227
Example 4
As an example of generalized programming, suppose the following situation.
We have $400 to buy boxes of blueberries ($5 per box) and cherries ($7 per
box) from a farmer. We take the berries to the town market where we hope
to sell them ($11 per blueberry box and $15 per cherry box). Any unsold
berries at the end of the market day can be sold to a local baker ($3 per
blueberry box and $5 per cherry box).
The demand for berries is stochastic. We assume that blueberry demand
during market hours is uniformly distributed between 10 and 30 boxes
and that cherry demand is uniformly distributed between 20 and 40 boxes.
In the simple recourse problem, the correlation between these demands
does not aﬀect the recourse function value, so we only need this marginal
information.
The initial decisions are x1, the number of boxes of blueberries to buy,
and x2, the number of boxes of cherries to buy. The full problem is then to
ﬁnd x∗, χ∗to
min z = 2x1 + 2x2 + Ψ1(χ1) + Ψ2(χ2)
(4.9)
s.t. 5x1 + 7x2 ≤400,
x1 −χ1 = 0,
x2 −χ2 = 0,
x1, x2 ≥0,
where
Ψ1(χ1) =
 −8χ1
if χ1 ≤10,
1
5χ2
1 −12χ1 + 20
if 10 ≤χ1 ≤30,
−160
if χ1 ≥30,
∇Ψ1(χ1) =
 −8
if χ1 ≤10,
2
5χ1 −12
if 10 ≤χ1 ≤30,
0
if χ1 ≥30,
Ψ2(χ2) =
 −10χ2
if χ2 ≤20,
1
4χ2
2 −20χ1 + 100
if 20 ≤χ2 ≤40,
−300
if χ2 ≥40,
and
∇Ψ2(χ2) =
 −10
if χ2 ≤20,
1
2χ2 −20
if 20 ≤χ2 ≤40,
0
if χ2 ≥40.
The generalized programming method follows these iterations.
Iteration 0:
Step 0. We start with (4.4)–(4.7) with ν = rj = sj = 0.
Step 1. The obvious solution is x0 = (0, 0)T with multipliers, π0 = ρ0 =
(0, 0)T .


## Page 247

228
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
Step 2. Setting π0
i = −∇Ψi(χ11), we obtain χ11 = 30 and χ21 = 40 with
Ψ1(χ11) = −160 and Ψ2(χ21) = −300 and clearly Ψj(χj,sj+1)+πν
j χj,sj+1−
ρν
j < 0 for each j = 1, 2. Now, s1 = s2 = 1, ν = 1 and we repeat.
Iteration 1:
Step 1. We assume that we can dispose of berries (to avoid creating an
infeasibility in (4.4)–(4.7)). The master problem then has the form:
min z = 2x1 + 2x2 −160λ11 −300λ21
(4.10)
s.t. 5x1 + 7x2 ≤400,
x1 −30λ11 ≥0,
x2 −40λ21 ≥0,
λ11 = 1,
λ21 = 1,
x1, x2, λ11, λ21 ≥0.
The solution is z1 = −300, x1 = (24, 40)T , λ11 = 0.8, λ21 = 1.0, π1 =
(5.333, 6.667)T and ρ1 = (0, −33.333)T .
Step 2. Setting π0
i = −∇Ψi(χ11), we obtain χ12 = 16.667 and χ22 = 26.667
with Ψ1(χ11) = −124.4 and Ψ2(χ22) = −255.55. Again, Ψj(χj,sj+1) +
πν
j χj,sj+1 −ρν
j < 0 for each j = 1, 2 with Ψ(χ12) + π1
1χ12 −ρ1
1 = −35.5 and
Ψ(χ22) + π1
2χ22 −ρ1
2 = −44.4. Now, s1 = s2 = 2, ν = 2.
Iteration 2:
Step 1. The new master problem is:
min z = 2x1 + 2x2 −160λ11 −124.4λ12
−300λ21 −255.55λ22
(4.11)
s.t. 5x1 + 7x2 ≤400,
x1 −30λ11 −16.667λ12 ≥0,
x2 −40λ21 −26.667λ22 ≥0,
λ11 + λ12 = 1,
λ21 + λ22 = 1,
x1, x2, λ11, λ12, λ21, λ22 ≥0.
The solution is z2 = −316.0, x2 = (24, 40)T , λ2
11 = 0.55, λ2
12 = 0.45, λ2
21 =
1.0, π2 = (2.667, 2.934)T and ρ2 = (−80.0, −182.6)T .
Step 2. Setting π2
i = −∇Ψi(χi,si+1), we obtain χ13 = 23.33 and χ23 =
34.13 with Ψ1(χ13) = −151.1 and Ψ2(χ23) = −291.4. Here, Ψ1(χ13) +
π2
1χ13 −ρ2
1 = −8.88 and Ψ2(χ23) + π2
2χ23 −ρ2
2 = −8.61. Now, s1 = s2 = 3,
ν = 3.


## Page 248

6.4 Nonlinear Programming in Simple Recourse Problems
229
Iteration 3:
Step 1. The new master problem is:
min z = 2x1 + 2x2 −160λ11 −124.4λ12 −151.1λ13
−300λ21 −255.55λ22 −291.4λ23
(4.12)
s.t. 5x1 + 7x2 ≤400,
x1 −30λ11 −16.667λ12 −23.333λ13 ≥0,
x2 −40λ21 −26.667λ22 −34.133λ23 ≥0,
λ11 + λ12 + λ13 = 1,
λ21 + λ22 + λ23 = 1,
x1, x2, λij ≥0.
The solution is z3 = −327.57, x3 = (23.333, 34.133)T , λ3
13 = 1.00, λ3
23 =
1.0, π3 = (2.0, 2.0)T and ρ3 = (−104.44, −223.13)T .
Step 2. Setting π3
i = −∇Ψi(χi,si+1), we obtain χ14 = 25 and χ24 = 36 with
Ψ1(χ14) = −155 and Ψ2(χ24) = −296. Here, Ψ1(χ14)+π3
1χ14 −ρ3
1 = −0.56
and Ψ2(χ24) + π3
2χ24 −ρ3
2 = −0.87. Now, s1 = s2 = 4, ν = 3.
Iteration 4:
Step 1. We add λ14 and λ24 with their objective and constraint entries to
(4.12) to obtain the same form of the master problem. The solution is now
z4 = −329, x4 = (25, 36)T , λ4
14 = 1.00, λ4
24 = 1.0, π4 = (2.0, 2.0)T and
ρ4 = (−105, −224)T .
Step 2. Because π4 = π3, we obtain χi5 = χi4, and Ψi(χi5)+π4
i χi5 −ρ4
i = 0
for i = 1, 2. Hence, no columns can be added. We stop with the optimal
solution, x∗= (25, 36)T with objective value z∗= 329.
Notice that in this example the budget constraint is not binding. We
only spend $377 of the total possible, $400. If we had solved this problem
as separate news vendor problems in each type of berry, we would have
obtained the same solution. In fact, this is one of the suggestions for initial
tenders to start the generalized programming process (see Birge and Wets
[1984] and Nazareth and Wets [1986]). In this case, we would terminate on
the ﬁrst step with this initial oﬀer.
Notice also that the algorithm appears to converge quite quickly here.
In general, the retention of information about gradients at many points
should improve convergence over techniques that use only local informa-
tion. Second-order information is also valuable, assuming twice diﬀeren-
tiable functions. This is the motivation behind Beale’s [1961] approach of
quadratic approximation. His method is another form of the generalized
programming approach for convex separable functions.
The other procedures speciﬁcally used on the simple recourse problem
concern some form of active set or simplex based strategy. Wets [1966] and


## Page 249

230
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
Ziemba [1970] give the basic reduced gradient or convex simplex method
procedure. This method consists of computing a search direction corre-
sponding to a change in the value of a nonbasic variable (assuming only ba-
sic variables change concomitantly). The basis is changed if the line search
implies that basic variable becomes zero. Otherwise, the nonbasic vari-
able’s value is updated and other nonbasic variables are checked for possible
descent.
A diﬀerent approach is given by Qi [1986], who suggests alternating be-
tween the solution of a linear program with χ ﬁxed and the solution of a
reduced variable convex program. The linear program is to ﬁnd
min
x cT x+Ψ(χν)
s. t. Ax= b,
Tx= χν,
x≥0,
(4.13)
to obtain xν+1 = (xν
B, xν
N), where xν
N = 0. Then solve the reduced convex
program:
min
x,χ cT x+Ψ(χ)
s. t. Ax= b,
Tx= χ,
xB ≥0,xN = 0
(4.14)
to obtain ˆxν+1, χν+1. The algorithm is the following.
Alternating Algorithm for Simple Recourse Problems
Step 0. Let ν = 0, choose a feasible solution x0 to (4.13) and let χ0 be part
of a solution to (4.14) with N deﬁned according to x0. Go to Step 1.
Step 1. Solve (4.13). Let Xν+1 = {x optimal in (4.13) }. Choose xν+1 ∈
Xν+1 such that cT xν+1 + Ψ(Txν+1) < cT xν + Ψ(Txν). If none exists, then
stop. Otherwise, go to Step 2.
Step 2. Solve (4.14) with N deﬁned for xν+1 to obtain χν+1. Let ν = ν + 1
and return to 1.
The algorithm converges to an optimal solution because xν+1 can always
be found with cT xν+1 + Ψ(Txν+1) < cT xν + Ψ(Txν) whenever xν is not
optimal (Exercise 5). Of course, the algorithm’s advantage is when the
number of ﬁrst-period variables n1 is much greater than the number of
second-period random variables m2, so that problem (4.14) does represent
a computation savings over solving (4.1) directly.
This algorithm (and indeed the convex simplex method) raises the possi-
bility for multiple optima of the linear program (degeneracy). In this case,
many solutions may be searched before improvement is found. In tests of


## Page 250

6.5 Other Nonlinear Programming–Based Methods
231
partitioning in discretely distributed general stochastic linear programming
problems (Birge [1985b]), this problem was found to overcome computa-
tional advantages of reducing the working problem size. The approach has,
therefore, not been followed extensively in practice although it may, of
course, oﬀer eﬃcient computation on some problems.
Other methods for simple recourse have built on the special structure.
For transportation constraints, Qi [1985] gives a method based on using
the forest structure of the basis to obtain a search direction and improved
forest solution. This method only requires the solution of one-dimensional
monotone equations apart from standard tree solutions. Piecewise linear
techniques as in Sun, Qi, and Tsai [1990] can also be adapted here to general
network structures and used in conjunction with Qi’s forest procedure to
produce a convergent algorithm.
Exercises
1. Show that the Frank-Wolfe method for the simplex recourse problem
converges to an optimal solution (assuming that one exists).
2. Solve the example in (4.9) using the L-shaped method.
3. Solve the example in (4.9) using the Frank-Wolfe method.
4. In the general stochastic linear programming model (with ﬁxed T,
(3.1.5)), show that solving (4.13) with χν = χ∗yields an optimal
solution x∗. Use this to show that there always exists a solution to
(3.1.5) with at most m1+m2 nonzero variables (Murty [1968]). What
does this imply for retaining cuts in the L-shaped method?
5. Show that the alternating algorithm for simple recourse problems
converges to an optimal solution assuming that the support of h is
compact. (Hint:From any xν, consider a path to x∗, use the convexity
of Ψ, and consider the solution as xν is approached from x∗.)
6.5
Other Nonlinear Programming–Based
Methods
In the previous sections, we considered cutting plane methods and La-
grangian methods for problems with discrete random variables and simple
recourse-based techniques for problems with continuous random variables.
Other nonlinear programming procedures can also be applied to stochastic
programs, although these other procedures have not received as much at-
tention in stochastic programming problems. A notable exception is No¨el
and Smeers’ [1987] multistage combined inner linearization and augmented


## Page 251

232
6. Nonlinear Programming Approaches to 2-Stage Recourse Problems
Lagrangian procedure, which we will describe in more detail in the next
chapter.
The diﬃculty with discrete random variables is that Ψ or Q generally
loses diﬀerentiability. In this case, derivative-based methods cannot apply.
As we saw, the L-shaped method and other cutting plane approaches are
a standard approach that requires only subgradient information. We also
saw that augmented Lagrangian techniques can smooth nondiﬀerentiable
functions.
Explicit nondiﬀerentiable methods include the nonmonotonic reduced
subgradient procedure considered by Ermoliev [1983]. Another possibility
is to use bundles of subgradients as in Lemar´echal [1978] and Kiwiel [1983].
In fact, results by Plambeck et al. [1996] show good performance for bundle
methods in practical stochastic programs.
Nonsmooth generalizations of the Frank-Wolfe procedure are also pos-
sible. These and other options are described in detail in Demyanov and
Vasiliev [1981].
With general continuous random variables or with large numbers of dis-
crete random vector realizations, direct nonlinear programming procedures
generally break down because of diﬃculties in evaluating function and
derivative values. In these cases, one must rely on approximation. These
approximations either take the form of bounds on the actual function val-
ues or are in some sense statistical estimates of the actual function values.
We present these approaches in Chapters 9 to 11.


## Page 252

7
Multistage Stochastic Programs
As the Chapter 1 examples demonstrate, many operational and planning
problems involve sequences of decisions over time. The decisions can re-
spond to realizations of outcomes that are not known
a priori. The re-
sulting model for optimal decision making is then a multistage stochastic
program. In Section 3.5, we gave some of the basic properties of multistage
problems. In this chapter, we explore the variety of solution procedures
that have been proposed speciﬁcally for multistage stochastic programs.
In general, the methods for two-stage problems generalize to the multi-
stage case but include additional complications. Because of these diﬃcul-
ties, we will describe only those methods that have shown some success in
implementations.
As stated in Section 3.5, the multistage stochastic linear program with a
ﬁnite number of possible future scenarios still has a deterministic equiva-
lent linear program. However, as the graph in Figure 3.4 began to suggest,
the structure of this problem is somewhat more complex than that of the
two-stage problem. The extensive form does not appear readily accessible
to manipulations such as the factorizations for extreme or interior point
methods that were described in Chapter 5. The overhead for these pro-
cedures appears diﬃcult to overcome (see Birge [1980] for a discussion of
multistage basis factorization and its requirements).
The methods that appear most promising are again based on decom-
positions, some form of Lagrangian relaxation, and uses of separability.
In Section 1, we describe the basic nested decomposition procedures for
multistage stochastic linear programs. Section 2 describes approaches for
multistage nonlinear problems again based on nested decomposition and


## Page 253

234
7. Multistage Stochastic Programs
the progressive hedging algorithm or Lagrangian approach. Section 3 con-
siders the use of block separability in these problems and describes the
special case of simple recourse or full separability.
7.1
Nested Decomposition Procedures
Nested decomposition procedures were proposed for deterministic models
by Ho and Manne [1974] and Glassey [1973]. These approaches are essen-
tially inner linearizations that treat all previous periods as subproblems to
a current period master problem. The previous periods generate columns
that can be used by the current-period master problem.
A diﬃculty with these primal nested decomposition or inner linearization
methods is that the set of inputs may be fundamentally diﬀerent for diﬀer-
ent last period realizations. Because the number of last period realizations
is the total number of scenarios in the problem, these procedures are not
well adapted to the bunching procedures described in Section 5.4. Some
success has been achieved, however, by No¨el and Smeers [1987], as we will
describe, by applying inner linearization to the dual, which is again outer
linearization of the primal problem.
The general primal approach is, therefore, to use an outer linearization
built on the two-stage L-shaped method. Louveaux [1980] ﬁrst performed
this generalization for multistage quadratic problems, as we discuss in Sec-
tion 2. Birge [1985b] extended the two-stage method in the linear case as in
the following description. The approach also appears in Pereira and Pinto
[1985].
The basic idea of the nested L-shaped or Benders decomposition method
is to place cuts on Qt+1(xt) in (3.5.3) and to add other cuts to achieve
an xt that has a feasible completion in all descendant scenarios. The cuts
represent successive linear approximations of Qt+1. Due to the polyhedral
structure of Qt+1, this process converges to an optimal solution in a ﬁnite
number of steps.
In general, for every stage t = 1, . . . , H−1 and each scenario at that stage,
k = 1, . . . , N t, we have the following master problem, which generates cuts
to stage t and proposals for stage t + 1:
min (ct
k)T xt
k + θt
k
(1.1)
s. t. W txt
k = ht
k −T t−1
k
xt−1
a(k),
(1.2)
Dt
k,jxt
k ≥dt
k,j, j = 1, . . . , rt
k,j,
(1.3)
Et
k,jxt
k + θt
k ≥et
k,j, j = 1, . . . , st
k,j,
(1.4)
xt
k ≥0,
(1.5)
where a(k) is the ancestor scenario of k at stage t −1, xt−1
a(k) is the current
solution from that scenario, and where for t = 1, we interpret b = h1−T 0x0


## Page 254

7.1 Nested Decomposition Procedures
235
as initial conditions of the problem. We may refer also to the stage H
problem in which θH
k and constraints (1.3) and (1.4) are not present. To
designate the period and scenario of the problem in (1.1)–(1.5), we also
denote this subproblem, NLDS(t, k).
We ﬁrst describe a basic algorithm for iterating among these stages. We
then discuss some enhancements of this basic approach. In the following,
Dt(j), denotes the period t descendants of a scenario j at period t −1.
We assume that all variables in (3.5.1) have ﬁnite upper bounds to avoid
complications presented by unbounded solutions (although, again, these
can be treated as in Van Slyke and Wets [1969]).
Nested
L-Shaped
Method
for
Multistage
Stochastic
Linear
Programs
Step 0. Set t = 1, k = 1, rt
k = st
k = 0, add the constraint θt
k = 0 to
(1.1)–(1.5) for all t and k, and let DIR = FORE. Go to Step 1.
Step 1. Solve the current problem, NLDS(t, k). If infeasible and t = 1, then
stop; problem (3.5.1) is infeasible. If infeasible and t > 1, then let rt−1
a(k) =
rt−1
a(k) + 1, let DIR = BACK. Let the infeasibility condition be obtained
by a dual basic solution, πt
k, ρt
k ≥0, such that (πt
k)T W t + (ρt
k)T Dt
k ≤0
but (πt
k)T (ht
k −T t−1
k
xt−1
a(k)) + (ρt
k)T dt
k > 0. Let Dt−1
a(k),rt−1
a(k) = (πt
k)T T t−1
k
,
dt−1
a(k),rt−1
a(k) = πt
kht
k + (ρt
k)T dt
k. Let t = t −1, k = a(k) and return to Step 1.
If feasible, update the values of xt
k, θt
k, and store the value of the com-
plementary basic dual multipliers on constraints (1.2)–(1.4) as (πt
k, ρt
k, σt
k),
respectively. If k < Kt, let k = k + 1, and return to (1.1). Otherwise,
(k = Kt), if DIR = FORE and t < H, let t = t + 1 and return. If t = H,
let DIR = BACK. Go to Step 2.
Step 2. For all scenarios j = 1, . . . , Kt−1 at t −1, compute
Et−1
j
=

k∈Dt(j)
pt
k
pt−1
j
(πt
k)T T t−1
k
and
et−1
j
=

k∈Dt(j)
pt
k
pt−1
j
[(πt
k)T ht
k +
rk

i=1
(ρt
ki)T dt
ki +
sk

i=1
(σt
ki)T et
ki].
The current conditional expected value of all scenario problems in Dt(j)
is then ¯θt−1
j
= et−1
j
−Et−1
j
xt−1
j
. If the constraint θt−1
j
= 0 appears in
NLDS(t −1, j), then remove it, let st−1
j
= 1, and add a constraint (1.4)
with Et−1
j
and et−1
j
to NLDS(t −1, j).


## Page 255

236
7. Multistage Stochastic Programs
If ¯θt−1
j
> θt−1
j
, then let st−1
j
= st−1
j
+ 1 and add a constraint (1.4) with
Et−1
j
and et−1
j
to NLDS(t −1, j). If t = 2 and no constraints are added
to NLDS(1) (j = K1 = 1), then stop with x1
1 optimal. Otherwise, let
t = t −1, k = 1. If t = 1, let DIR = FORE. Go to Step 1.
Many alternative strategies are possible in this algorithm in terms of
determining the next subproblem (1.1)–(1.5) to solve. For feasible solutions,
the preceding description explores all scenarios at t before deciding to move
to t −1 or t + 1. For feasible iterations, the algorithm proceeds from t
in the direction of DIR until it can proceed no further in that direction.
This is the “fast-forward-fast-back” procedure proposed by Wittrock [1983]
for deterministic problems and implemented with success by Gassmann
[1990] for stochastic problems. One may alternatively enforce a move from
t to t −1 (“fast-back”) or from t to t + 1 (“fast-forward”) whenever it
is possible. From experiments conducted by Gassmann [1990], the fast-
forward-fast-back sequencing protocol seems to work better than either of
these alternatives. Morton [1994] compares with other alternative protocols
and reaches much the same conclusion.
For infeasible solutions at some stage, this algorithm immediately returns
to the ancestor problem to see whether a feasible solution can be generated.
This alternative appears practical because subsequent iterations with a
currently infeasible solution do not seem worthwhile.
We note that much of this algorithm can also run in parallel. We refer to
Ruszczy´nski [1993a] who describes parallel procedures in detail. Again, one
should pay attention in parallel implementations to the possible additional
work for solving similar subproblems as we mentioned in Chapter 5. The
convergence of this method is relatively straightforward, as given in the
following.
Theorem 1. If all Ξt are ﬁnite and all xt have ﬁnite upper bounds, then
the nested L-shaped method converges ﬁnitely to an optimal solution of
(3.5.1).
Proof:
First, we wish to demonstrate that all cuts generated by the al-
gorithm are valid outer linearizations of the feasible regions and objec-
tives in (3.5.3). By induction on t, suppose that all feasible cuts (1.3) gen-
erated by the algorithm for periods t or greater are valid. For t = H,
no cuts are present so this is true for the last period. In this case,
for any πt
k, ρt
k ≥0 such that (πt
k)T W t + (ρt
k)T Dt
k ≤0, we must have
(πt
k)T (ht
k −T t−1
k
xt−1
a(k))+(ρt
k)T dt
k ≤0 to maintain feasibility. Because this is
the cut added, these cuts are valid for t −1. Thus, the induction is proved.
Now, suppose the cuts in (1.1, 1.4) are an outer linearization of Qt+1
k
(xt
k)
for t or greater and all k. In this case, for any (πt
k, ρt
k, σt
k) feasible in (1.1)–
(1.5) for t and k, (πt
k)T (ht
k −T t
kxt−1
a(k)) + 	rk
i=1(ρt
ki)T dt
ki + 	sk
i=1(σt
ki)T et
ki is


## Page 256

7.1 Nested Decomposition Procedures
237
a lower bound on Qt
a(k)(xt−1
a(k), k) for any xt−1
a(k), each k, and a(k). Thus, we
must have
Qt
a(k)(xt−1
a(k))≥

k∈Dt(a(k))
( pt
k
pt−1
a(k)
)((πt
k)T (ht
k −T t
kxt−1
a(k))
+
rk

i=1
(ρt
ki)T dt
ki +
sk

i=1
(σt
ki)T et
ki),
(1.6)
which says that θt−1
k
≥−Et−1
a(k)xt−1
a(k) + et−1
a(k), as found in the algorithm.
Thus, again, we achieve a valid cut on Qt−1
a(k) for any a(k), completing the
induction.
Now, suppose that the algorithm terminates. This can only happen if
(1.1)–(1.5) is infeasible for t = 1 or if each subproblem for t = 2 has
been solved and no cuts are generated. In the former case, the problem
is infeasible, because the cuts (1.1,1.3) are all outer linearizations of the
feasible region. In the latter case, we must have θ1 = Q2(x1), the condition
for optimality.
For ﬁniteness, proceed by induction. Suppose that at stage t, at most a
ﬁnite number of cuts from stage t + 1 to H can be generated for each k
at t. For H, this is again trivially true. Because at most a ﬁnite number
of cuts are possible at each k, at most a ﬁnite number of basic solutions,
(πt
k, ρt
k, σt
k), can be generated to form cuts for a(k). Thus, at most a ﬁnite
number cuts can be generated for all a(k) at t −1, again completing the
induction.
The proof is complete by noting that every iteration of Step 1 or 2
produces a new cut. Because there is only a ﬁnite number of possible cuts,
the procedure stops ﬁnitely.
The nested L-Shaped method has many features in common with the
standard two-stage L-shaped algorithm. There are, however, peculiarities
about the multistage method. We consider the following example in some
detail to illustrate these features. In particular, we should note that the
two-stage method always produces cuts that are supports of the function
Q if the subproblem is solved to optimality. In the multistage case, with the
sequencing protocol just given, we may not actually generate a true support
so that the cut may lie strictly below the function being approximated.
Example 1
Suppose we are planning production of air conditioners over a three month
period. In each month, we can produce 200 air conditioners at a cost of
$100 each. We may also use overtime workers to produce additional air
conditioners if demand is heavy, but the cost is then $300 per unit. We have
a one-month lead time with our customers, so that we know that in Month


## Page 257

238
7. Multistage Stochastic Programs
1, we should meet a demand of 100. Orders for Months 2 and 3 are, however,
random, depending heavily on relatively unpredictable weather patterns.
We assume this gives an equal likelihood in each month of generating orders
for 100 or 300 units.
We can store units from one month for delivery in a subsequent month,
but we assume a cost of $50 per unit per month for storage. We assume
also that all demand must be met. Our overall objective is to minimize the
expected cost of meeting demand over the next three months. (We assume
that the season ends at that point and that we have no salvage value
or disposal cost for any leftover items. This resolves the end-of-horizon
problem here.)
Let xt
k be the regular-time production in scenario k at month t, let yt
k
be the number of units stored from scenario k at month t, let wt
k be the
overtime production in scenario k at month t, and let dt
k be the demand
for month t under scenario k. The multistage stochastic program in deter-
ministic equivalent form is:
min x1 + 3.0w1 + 0.5y1+
2

k=1
p2
k(x2
k + 3.0w2
k + 0.5y2
k)
+
4

k=1
p3
k(x3
k + 3.0w3
k)
s. t. x1≤2,
x1 + w1 −y1= 1,
y1 + x2
k + w2
k −y2
k= d2
k,
(1.7)
x2
k≤2, k = 1, 2,
y2
a(k) + x3
k + w3
k −y3
k= d3
k,
x3
k≤2, k = 1, . . . , 4,
xt
k, yt
k, wt
k≥0, k = 1, . . . , Kt, t = 1, 2, 3,
where a(k) = 1, if k = 1, 2 at period 3, a(k) = 2 if k = 3, 4 at period
3, p2
k = 0.5, k = 1, 2, p3
k = 0.25, k = 1, . . . , 4, d2
1 = 1, d2
2 = 3, and
d3 = (1, 3, 1, 3)T .
The nested L-shaped method applied to (1.7) follows these steps for the
ﬁrst two iterations. We list an iteration at each change of DIR.
Step 0. All subproblems NLDS(t, k) have the explicit θt
k = 0 constraint.
DIR = FORE.


## Page 258

7.1 Nested Decomposition Procedures
239
Iteration 1:
Step 1. Here t = 1, k = 1. The subproblem NLDS(1, 1) is:
min x1 + 3w1 + 0.5y1 + θ1
s. t. x1 ≤2,
x1 + w1 −y1 = 1,
x1, w1, y1 ≥0,
θ1 = 0,
(1.8)
which has the solution x1 = 1; other variables are zero.
Step 1. Now, t = 2, k = 1, and NLDS(2, 1) is
min x2
1 + 3w2
1 + 0.5y2
1 + θ2
1
s. t. x2
1 ≤2,
x2
1 + w2
1 −y2
1 = 1,
x2
1, w2
1, y2
1 ≥0,
θ2
1 = 0,
(1.9)
which has the solution, x2
1 = 1; other variables are zero.
Step 1. Here, t = 2, k = 2, and NLDS(2, 2) is
min x2
2 + 3w2
2 + 0.5y2
2 + θ2
2
s. t. x2
2 ≤2,
x2
2 + w2
2 −y2
2 = 3,
x2
2, w2
2, y2
2 ≥0,
θ2
2 = 0,
(1.10)
which has the solution, x2
2 = 2, w2
2 = 1; other variables are zero.
Step 1. Next, t = 3, k = 1. NLDS(3, 1) is
min x3
1 + 3w3
1 + 0.5y3
1 + θ3
1
s. t. x3
1 ≤2,
x3
1 + w3
1 −y3
1 = 1,
x3
1, w3
1, y3
1 ≥0,
θ3
1 = 0,
(1.11)
which has the solution, x3
1 = 1; other primal variables are zero. The com-
plementary basic dual solution is π3
1 = (0, 1)T .


## Page 259

240
7. Multistage Stochastic Programs
Step 1. Next, t = 3, k = 2. NLDS(3, 2) has the same form as NLDS(3, 1),
except we replace the second constraint with x3
2+w3
2−y3
2 = 3. It has the so-
lution, x3
2 = 2, w3
2 = 1; other primal variables are zero. The complementary
basic dual solution is π3
2 = (−2, 3)T .
Step 1. For t = 3, k = 3, we have the same subproblem and solution as
t = 3, k = 1, so x3
3 = 1; other primal variables are zero. The complementary
basic dual solution is π3
3 = (0, 1)T .
Step 1. For t = 3, k = 4, we have the same subproblem and solution
as t = 3, k = 2, x3
4 = 2, w3
4 = 1; other primal variables are zero. The
complementary basic dual solution is π3
4 = (−2, 3)T . Now, DIR = BACK,
and we go to Step 2.
Iteration 2:
Step 2. For scenario j = 1 and t −1 = 2, we have
E2
11 = (0.25
0.5 )(π3
1T 3
1 + π3
2T 3
2 )
= (0.5) ( 0
1 )

0
0
0
0
0
1

+ (0.5) ( −2
3 )

0
0
0
0
0
1

= ( 0
0
2 )
(1.12)
and
e2
11 = (0.25
0.5 )(π3
1h3
1 + π3
2h3
2)
= (0.5) ( 0
1 )

2
1

+ (0.5) ( −2
3 )

2
3

= 3,
(1.13)
which yields the constraint, 2y2
1 + θ2
1 ≥5, to add to NLDS(2, 1).
For scenario j = 2 at t −1 = 2, we have the same, E2
21 = ( 0
0
2 ),
e2
21 = 3. Now t = 2 and k = 1.
Step 1. NLDS(2, 1) is now:
min x2
1 + 3w2
1 + 0.5y2
1 + θ2
1
s. t. x2
1 ≤2,
x2
1 + w2
1 −y2
1 = 1,
2y2
1 + θ2
1 ≥3,
x2
1, w2
1, y2
1 ≥0,
(1.14)
which has an optimal basic feasible solution, x2
1 = 2, y2
1 = 1, θ2
1 = 1,
w2
1 = 0, with complementary dual values, π2
1 = (−0.5, 1.5)T , σ2
11 = 1.


## Page 260

7.1 Nested Decomposition Procedures
241
Step 1. NLDS(2, 2) has the same form as (1.14) except that the demand
constraint is x2
2 +w2
2 −y2
2 = 3. The optimal basic feasible solution found to
this problem is x2
2 = 2, w2
2 = 1, θ2
2 = 3, y2
2 = 0, with complementary dual
values, π2
2 = (−2, 3)T , σ2
11 = 1. We continue in DIR = BACK to Step 2.
Step 2. For scenario t −1 = 1, we have
E1
1 = (0.5)(π2
1T 2
1 + π2
2T 2
2 )
= (0.5) ( −0.5
1.5 )

0
0
0
0
0
1

+ (0.5) ( −2
3 )

0
0
0
0
0
1

= ( 0
0
2.25 )
(1.15)
and
e1
1 = (0.5)(π2
1h2
1 + π2
2h2
2) + (0.5)(σ2
11e2
11 + σ2
21e2
21)
= (0.5) ( −0.5
1.5 )

2
1

+ (0.5) ( −2
3 )

2
3

+ (0.5)((1)(3) + (1)3)
= (0.5)(0.5 + 5 + 6) = 5.75,
(1.16)
which yields the constraint, 2.25y1 + θ1 ≥5.75, to add to NLDS(1).
Step 1. NLDS(1) is now:
min x1 + 3w1 + 0.5y1 + θ1
s. t. x1 ≤2,
x1 + w1 −y1 = 1,
2.25y1 + θ1 ≥5.75,
x1, w1, y1 ≥0,
(1.17)
with optimal basis feasible solution, x1 = 2, y2 = 1, w1 = 0, θ1 = 3.5.
DIR = FORE.
This procedure continues through six total iterations to solve the prob-
lem. At the last iteration, we obtain ¯θ1 = 3.75 = θ1, so no new cuts are
generated for Period 1. We stop with a current solution as optimal, x1∗= 2,
y1∗= 1, z∗= 2.5+3.75 = 6.25. In Exercise 1, we ask the reader to generate
each of the cuts.
Following the nested L-shaped method completely takes many steps in
this example, six iterations or changes of direction corresponding to three
forward passes and three backward passes. Figure 1 illustrates the process
and provide some insight into nested decomposition performance.
In Figure 1, the solid line gives the objective value in (1.7) as a function
of total production prod1 = x1 + w1 in the ﬁrst period. The dashed lines


## Page 261

242
7. Multistage Stochastic Programs
correspond to the cuts made by the algorithm (Cut 1,2). The ﬁrst cut
was 2.25y1 + θ ≥5.75 from (1.15)–(1.16) on Iteration 2. Because y1 =
x1 + w1 −1, we can substitute for y1 to obtain, 2.25x1 + 2.25w1 + θ ≥8.
The objective in (1.17) is z1 = x1 + 3w1 + 0.5y1 + θ, so, combined with
1 ≤x1 ≤2, we can substitute θ ≥8 −2.25(prod1) to obtain z1(prod1) =
7.5 + (1.5) min{2, prod1} + 3.5(prod1 −2)+ −2.25prod1, where prod1 ≥1.
This can also be written as:
z1(prod1) =

7.5 −0.75prod1
if prod1 ≤2,
3.5 + 1.25prod1
if prod1 > 2,
(1.18)
which corresponds to the wide dashed line (Cut 1) in Figure 1.
FIGURE 1. The ﬁrst period objective function (solid line) for the example and
cuts (dashed lines) generated by the nested L-shaped method.
The second cut occurs on Iteration 4 (verify this in Exercise 1) as 2x1 +
2w1 + θ ≥7.75, which yields z1(prod1) = x1 + 3w1 + 0.5y2 + θ ≥7.25 +
(1.5) min{2, prod1} + 3.5(prod1 −2)+ −2prod1 or
z1(prod1) ≥

7.25 −0.5prod1
if prod1 ≤2,
3.25 + 1.5prod1
if prod1 > 2.
(1.19)
This cut corresponds to the narrow width dashed line (Cut 2) in Figure 1.
The optimal value and solution in terms of prod1 can be read from Figure
1 as each cut is added. With only Cut 1, the lowest value of z1 occurs
when prod1 = 2. With Cuts 1 and 2, the minimum is also achieved at
prod1 = 2. Note that the ﬁrst cut is not, however, a facet of the objective
function’s graph. The cuts meet the objective at prod1 = 1 and prod1 = 2,


## Page 262

7.1 Nested Decomposition Procedures
243
respectively, but they need not even do this, as we mentioned earlier (see
Exercise 2). The other parts of the Period 1 cuts are generated from bounds
on Q2
2.
This example illustrates some of the features of the nested L-shaped
method. Besides our not being guaranteed of obtaining a support of the
function at each step, another possible source of delay in the algorithm’s
convergence is in degeneracy. As the example illustrates, the solutions at
each step occur at the links of the piecewise linear pieces generated by the
method (Exercises 4 and 5). At these places, many bases may be optimal
so that several bases may be repeated. Some remedies are possible, as in
Birge [1980] and, for deterministic problems, Abrahamson [1983].
As with the standard two-stage L-shaped method, the nested L-shaped
method acquires its greatest gains by combining the solutions of many
subproblems through bunching (or sifting). Birge [1985b] reported order of
magnitude speed-ups over MINOS solutions of the deterministic equivalent
problems. Gassmann [1990] reported even more signiﬁcant speed-ups by
taking advantage of the fast-forward-fast-back procedure and implementing
bunching in an extremely eﬃcient manner.
We note that multicuts may also be valuable here, although the full po-
tential of this approach has not been explored in a computational study.
Infanger [1991, 1994] has also suggested the uses of generating many cuts
simultaneously when future scenarios all have similar structure. This pro-
cedure may make bunching eﬃcient for periods other than H by making
every constraint matrix identical for all scenarios in a given period. In this
way, only objective and right-hand side constraint coeﬃcients vary among
the diﬀerent scenarios.
In terms of primal decomposition, we mentioned the work of No¨el and
Smeers at the outset of this chapter. They apply nested Dantzig-Wolfe de-
composition to the dual of the original problem. As we saw in Chapter 5,
this is equivalent to applying outer linearization to the primal problem.
The only diﬀerence is that they allow for some nonlinear terms in their
constraints, which would correspond to a nonlinear objective in the pri-
mal model. Because the problems are still convex, nonlinearity does not
really alter the algorithm. The only problem may be in the ﬁniteness of
convergence.
The advantage of a primal or dual implementation generally rests in
the problem structure, although primal or dual simplex may be used in
either method, making them indistinguishable. Gassmann presents some
indication that dual iterations may be preferred in bunching. In general,
many primal columns and few rows would tend to favor a primal approach
(outer linearization as in the L-shaped method) while few columns and
many rows would tend to favor a dual approach. In any case, the form of
the algorithm and all proofs of convergence apply to either form.


## Page 263

244
7. Multistage Stochastic Programs
Exercises
1. Continue Example 1 with the nested L-shaped method until you ob-
tain an optimal solution.
2. Construct a multistage example in which a cut generated by the sec-
ond period in following in the nested L-shaped method does not meet
Q1(x1) for any value of x1, i.e., −E1
1x1 + e1
1 < Q(x1).
3. Show that the situation in (1.1) is not possible if the fast-forward
protocol is always followed.
4. Suppose a feasibility cut (1.3) is active for xt
k for any t and k. Show
that every basic feasible solution of NLDS(t+1, j) with input xt
k for
some scenario j ∈Dt+1(k) must be degenerate.
5. Suppose two optimality cuts (1.4) are active for (xt
k, θt
k) for any t
and k. Show that either the subproblems generate a new cut with
¯θt
k > θt
k or an optimal solution of NLDS(t + 1, j) with input xt
k for
some scenario j ∈Dt+1(k) must be degenerate.
6. Using four processors, what eﬃciency can be gained by solving the
preceding example in parallel? Find the utilization of each processor
and the speed-up of elapsed time, assuming each subproblem requires
the same solution time.
7. Suppose θ1 is broken into separate components for Q2
1 and Q2
2 as in
the two-stage multicut approach. How does that alter the solution of
the example?
7.2
Quadratic Nested Decomposition
Decomposition techniques for multistage nonlinear programs are available
for the case in which the objective function is quadratic convex, the con-
straint set polyhedral, and the random variables discrete. For the sake of
clarity, we repeat the recursive deﬁnition of the deterministic equivalent
program, already given in Section 3.5.
(MQSP)
min z1(x1) = (c1)T · x1 + (x1)T D1x1 + Q2(x1)
(2.1)
s.t. W 1x1 = h1
x1 ≥0,
where Qt(xt−1, ξt(ω)) =
min(ct(ω))T xt(ω)+(xt(ω))T Dt(ω)xt(ω) + Qt+1(xt+1)
s.t. W txt(ω) = ht(ω) −T t−1(ω)xt−1
xt(ω) ≥0,
(2.2)


## Page 264

7.2 Quadratic Nested Decomposition
245
Qt+1(xt) = Eξt+1Qt+1(xt, ξt+1(ω)) , t = 1, · · · , H −1,
(2.3)
and
QH(xH−1) = 0.
(2.4)
In MQSP, Dt is an nt × nt matrix. All other matrices have the dimen-
sions deﬁned in the linear case. The random vector, ξt(ω), is formed by the
elements of ct(ω), ht(ω), T t−1(ω), and Dt(ω). We keep the notation that
ξt is an Nt-vector on (Ω, At, P), with support Ξt. Finally, we again deﬁne
Kt = {xt|Qt+1(xt) < ∞}.
We also deﬁne zt(xt) = (ct)T xt + (xt)T Dtxt + Qt+1(xt).
Theorem 2. If the matrices Dt(ω) are positive semi-deﬁnite for all ω ∈Ω
and t = 1, · · · , H, then the sets Kt and the functions Qt+1(xt) are convex
for t = 1, · · · , H −1. If Ξt is also ﬁnite for t = 2, · · · , H, then Kt is poly-
hedral. Moreover zt(xt) is either identically −∞or there exists a decompo-
sition of Kt into a polyhedral complex such that the tth-stage deterministic
equivalent program (2.2) is a piecewise quadratic program.
Proof: The piecewise quadratic property of (2.2) is obtained by inductively
applying to each cell of the polyhedral complex of Kt the result that if zt(.)
is a ﬁnite positive semi-deﬁnite quadratic form, there exists a piecewise
aﬃne continuous optimal decision rule for (2.2). All others results were
given in Section 3.5.
We now describe a nested decomposition algorithm for MQSP ﬁrst pre-
sented in Louveaux [1980]. For simplicity in the presentation of the algo-
rithms, we assume relatively complete recourse. This means that we skip
the step that consists of generating feasibility cuts. If needed, those cuts
are generated exactly as in the multistage linear case. We keep the notation
of a(k) for the ancestor scenario of k at stage t −1. As in Section 7.1, ct
k,
Dt
k, and Qt+1
k
represent realizations of ct, Dt, and Qt+1 for scenario k and
xt
k is the corresponding decision vector. In Stage 1, we use the notations,
z1 and z1
1 and x1 and x1
1, as equivalent.
Nested PQP Algorithm for MQSP
Step 0. Set t = 1, k = 1, C1 = S1 = K1. Choose x1
1 ∈K1.
Step 1. If t = H, go to Step 2. For i = t + 1, · · · , H, let k = 1, zi
1(xi
1) =
(ci
1)T xi
1 + (xi
1)T Di
1xi
1 and Ci
1(xi−1
a(1)) = Si
1(xi−1
a(1)) = Ki(xi−1
a(1)). Choose xi
1 ∈
Ki(xi−1
a(1)). Set t = H.
Step 2. Find v ∈arg min{zt
k(xt
k)|xt
k ∈St
k(xt−1
a(k))}. Find w ∈arg min{zt
k(xt
k) |
xt
k ∈Ct
k(xt−1
a(k))}. If w is the limiting point on a ray on which zt
k(.) is de-
creasing to −∞, then (DEP)t
k is unbounded and the algorithm terminates.


## Page 265

246
7. Multistage Stochastic Programs
Step 3. If ∇T zt
k(w)(v −w) = 0, go to Step 4. Otherwise, redeﬁne
St
k(xt−1
a(k)) ←St
k(xt−1
a(k)) ∩{xt
k|∇T zt
k(w)(xt
k −w) ≤0}.
Let xt
k = v, zt
k = (ct
k)T xt
k + (xt
k)T Dt
kxt
k and Ct
k = Kt(xt−1
a(k)). Go to Step 1.
Step 4. If t = 1, stop; w is an optimal ﬁrst-period decision. Otherwise,
ﬁnd the cell Gt
k(xt−1
a(k)) containing w and the corresponding quadratic form
Qt
k(xt−1
a(k)). Redeﬁne
zt−1
a(k)(xt−1
a(k)) ←zt−1
a(k)(xt−1
a(k)) + pt
kQt
k(xt−1
a(k))
Ct−1
a(k)(xt−1
a(k)) ←Ct−1
a(k)(xt−1
a(k)) ∩Gt
a(k)(xt−1
k
) .
If k = Kt, let t ←t −1, go to Step 2. Otherwise, let k ←k + 1, zt
k(xt
k) =
(ct
k)T xt
k +(xt
k)T Dt
kxt
k, Ct
k = St
k(xt−1
a(k)) = Kt(xt−1
a(k)). Choose xt
k ∈St
k(xt−1
a(k)).
Go to Step 1.
Theorem 3. The nested PQP algorithm terminates in a ﬁnite number of
steps by either detecting an unbounded solution or ﬁnding an optimal solu-
tion of the multistage quadratic stochastic program with relatively complete
recourse.
Proof: The proof of the ﬁnite convergence of the PQP algorithm in Section
6.2 amounts to showing that Step 2 of the algorithm can be performed at
most a ﬁnite number of times. The same result holds for a given piecewise
quadratic program (2.2) in the nested sequence. The theorem follows from
the observations that there is only a ﬁnite number of diﬀerent problems
(2.2) and that all other steps of the algorithm are ﬁnite.
Numerical experiments are reported in Louveaux [1980]. It should be
noted that the MQSP easily extends to the multistage piecewise convex
case. The limit there is that the objective function and the description of
the cell are usually much more diﬃcult to obtain. One simple example is
proposed in Exercise 3.
It is interesting to observe that MQSP has a tendency to require few
iterations when the quadratic terms play a signiﬁcant role and a good
starting point is chosen. (This probably relates to the good behavior of
regularized decomposition.)
Example 1 (continued)
Assume that the cost of overtime is now quadratic (for example, larger
increases of salary are needed to convince more people to work overtime).
We replace everywhere 3.0wt
k by 2.0wt
k + (wt
k)2. Assume all other data are
unchanged. Take as the starting point a situation where 0 ≤y1 ≤1, 0 ≤
y2
k ≤1, k = 1, 2. (It is relatively easy to see what the corresponding values


## Page 266

7.2 Quadratic Nested Decomposition
247
for the other ﬁrst- and second-stage variables should be.) We now proceed
backward. Let t = 3.
i) t = 3, k = 1. We solve
min x3
1 + 2w3
1 + (w3
1)2
s.t. y2
1 + x3
1 + w3
1 = 1, x3
1 ≤2,
x3
1, w3
1 ≥0 ,
where inventory at the end of Period 3 has been omitted for simplicity. The
solution is easily seen to be x3
1 = 1−y2
1, w3
1 = 0 and is valid for 0 ≤y2
1 ≤1.
It follows that
Q3
1(y2
1) = 1 −y2
1 .
ii) t = 3, k = 2. We solve
min x3
2 + 2w3
2 + (w3
2)2
s.t. y2
1 + x3
2 + w3
2 = 3, x3
2 ≤2,
x3
2, w3
2 ≥0 .
The solution is now x3
2 = 2, w3
2 = 1 −y2
1, valid for 0 ≤y2
1 ≤1. It yields
Q3
2(y2
1) = 4 −2y2
1 + (1 −y2
1)2.
Combining (i) and (ii), we obtain
Q2
1(y2
1) = 1
2Q3
1(y2
1) + 1
2Q3
2(y2
1) = 5
2 −3
2y2
1 + (1 −y2
1)2
2
and
C2
1(y2
1) = {y2
1|0 ≤y2
1 ≤1}.
iii) and iv) Because the randomness is only in the right-hand side, we
conclude that cases (iii) and (iv) are identical to (i) and (ii), respectively.
Hence,
Q2
2(y2
2) = 5
2 −3
2y2
2 + (1 −y2
2)2
2
and C2
2(y2
2) = {y2
2|0 ≤y2
2 ≤1}.
t = 2
i) t = 2, k = 1. The objective z2
1 is computed as
z2
1 = x2
1 + 2w2
1 + (w2
1)2 + 0.5y2
1 + 5
2 −3
2y2
1 + (1 −y2
1)2
2
,
i.e.,
z2
1 = 5
2 + x2
1 + 2w2
1 + (w2
1)2 −y2
1 + (1 −y2
1)2
2
.
The constraint sets are
S2
1 = {x2
1, w2
1, y2
1|y1 + x2
1 + w2
1 −y2
1 = 1 , 0 ≤x2
1 ≤2, x2
1, w2
1, y2
1 ≥0}


## Page 267

248
7. Multistage Stochastic Programs
and
C2
1 = S2
1 ∩{0 ≤y2
1 ≤1}.
The solution v of minimizing z2
1(.) over S2
1 is
y2
1 = 1, x2
1 = 2 −y1.
Because the solution belongs to C2
1, we can take w = v. (Beware that w
without superscript and subscript corresponds to the optimal solution on a
cell deﬁned in Step 2, while w with superscript and subscript corresponds
to overtime.) Thus, this point satisﬁes the optimality criterion in Step 3.
It yields
Q2
1(y1) = 5
2 + 2 −y1 −1 = 7
2 −y1 and
C2
1(y1) = {y1|0 ≤y1 ≤2}.
ii) t = 2, k = 2. The objective z2
2 is similarly computed as
z2
2 = 5
2 + x2
2 + 2w2
2 + (w2
2)2 −y2
2 + (1 −y2
2)2
2
.
The constraint set
S2
2 = {x2
2, w2
2, y2
2|y1 + x2
2 + w2
2 −y2
2 = 3, 0 ≤x2
2 ≤2, x2
2, w2
2, y2
2 ≥0}
only diﬀers in the right-hand side of the inventory constraint with
C2
2 = S2
2 ∩{0 ≤y2
2 ≤1} .
The solution v is now x2
2 = 2, w2
2 = 1 −y1, y2
2 = 0. Again v ∈C2
2, so that
we have w = v, which satisﬁes the optimality criterion in Step 3. It yields
Q2
2(y1) = 5
2 + 2 + 2(1 −y1) + (1 −y1)2 + 1
2 = 7 −2y1 + (1 −y1)2
C2
2(y1) = {y1|0 ≤y1 ≤1}.
t = 1.
The current objective function is computed as
z1 = 21/4 −y1 + (1 −y1)2
2
+ x1 + 2w1 + (w1)2.
The constraint sets are
S1
1 = {x1, w1, y1|x1 + w1 −y1 = 1, x1 ≤2, x1, w1, y1 ≥0},
C1
1 = S1
1 ∩{0 ≤y1 ≤1}.
The solution v of minimizing z1 over S1
1 is
x1 = 2, y1 = 1, w1 = 0 ,
with objective value z1 =
25
4 . Because this solution belongs to C1, it is
the optimal solution of the problem. Thus, no cut has ever been needed to
optimize the problem.


## Page 268

7.2 Quadratic Nested Decomposition
249
Block Separability
The deﬁnition of block separability was given in Section 3.5. It permits a
separate calculation of the recourse functions for the aggregate level deci-
sions and the detailed level decisions. This is an advantage in terms of the
number of variables and constraints, but often it makes the computation
of the recourse functions and of the cells of the decomposition much easier
in the case of a quadratic multistage program. This has been exploited in
Louveaux [1986] and Louveaux and Smeers [1997].
We will illustrate a further beneﬁt. It also consists of separating the ran-
dom vectors. Consider the production of one single product. Now, assume
the product cannot be stored (as in the case of a perishable good) or that
the policy of the ﬁrm is to use a just-in-time system of production so that
only a ﬁxed safety stock is kept at the end of each period.
Assume that units are such that one worker produces exactly one prod-
uct per stage. Two elements are uncertain: labor cost and demand. Labor
cost is currently 2 per period. Next period, labor cost may be 2 or 3, with
equal probability. Current revenue is 5 per product in normal time and 4
in overtime. Overtime is possible for up to 50% of normal time. Demand is
a uniform continuous random variable within (0,200) and (0,100), respec-
tively, for the next two periods. The original workforce is 50. Hiring and
ﬁring is possible once a period, at the cost of one unit each. Clearly, the
labor decision is the aggregate level decision.
To keep notation in line with Section 3.5, we consider a three-stage model.
In Stage 1, the decision about labor is made, say for Year 1. Stage 2 consists
of production of Year 1 and decision about labor for Year 2. Stage 3 only
consists of production of Year 2. Let ξt
1 be labor cost in stage t, while ξt
2 is
the demand in stage t. Let wt be the workforce in stage t. Then,
Qt
w(wt−1,ξt
1)= min |wt −wt−1| + ξt
1wt + Qt+1(wt) ,
(2.5)
Qt+1(wt)= Eξ
t+1[Qt+1
w (wt,ξt+1
1
) + Qt+1
y
(wt,ξt+1
2
)],
(2.6)
and Qt+1
y
(wt,ξt+1
1
) is minus the expected revenue of production in stage
t + 1 given a workforce wt and a demand scenario ξt+1
2
. It is obtained as
follows.
Let Dt represent the maximal demand in stage t (200 for t = 2, 100 for
t = 3). Observe that the expectation of ξt
2 is Dt/2 because ξt
2 is uniformly
continuous over [0, Dt]. If wt ≥Dt, all demand can be satisﬁed with normal
time. If wt ≤Dt ≤1.5wt, demand up to wt is satisﬁed with normal time,
the rest in overtime. Finally, if Dt ≥1.5wt, normal time is possible up to a
demand of wt, overtime from wt to 1.5wt, and extra demand is lost. Taking
expectations over these cases, we obtain
Qt+1
y
(wt) =


## Page 269

250
7. Multistage Stochastic Programs
Eξ
t+1[Qt+1
y
(wt, ξt+1
2
)] =





−2.5Dt
if wt ≥Dt,
(wt)2
2Dt −wt −2Dt
if wt ≤Dt ≤1.5wt,
5(wt)2
Dt
−7wt
if 1.5wt ≤Dt.
This problem can now be solved with the MQSP algorithm. Assume w0 =
50, w1 ≥50.
Let Stage (2,1) represent the ﬁrst labor scenario in Stage 2, i.e., ξ2
1 = 2.
The problem consists of ﬁnding
min |w2 −w1| + 2w2 + Q3(w2)
s.t. w2 ≥0.
We compute Q3(w2) = Q3
y(w2) =
5(w2)2
100
−7w2, for w2 ≤
200
3 , because
D3 = 100. We also replace |w2 −w1| by an explicit expression in terms of
hiring (h2) and ﬁring (f 2). The problem in Stage (2,1) now reads:
Q2
w(w1, 1) = min h2 + f 2 −5w2 + 5(w2)2
100
s.t. w2 −h2 + f 2 = w1
w2 ≥0, h2 ≥0, f 2 ≥0.
Under this form, the problem is clearly quadratic convex (remember w2 is w
in Stage 2, not the square of w). Classical Karush-Kuhn-Tucker conditions
give the optimal solution w2 = w1, as long as 40 ≤w1 ≤60. Then
Q2
w(w1, 1) = −5w1 + 5(w1)2
100
.
Similarly, in Scenario (2,2) where ξ2
1 = 3, the solution of
min |w2 −w1| + 3w2 + Q3(w2)
s.t. w2 ≥0
is w2 = 50, f 2 = w1 −50, as long as w1 ≥50. Then
Q2
w(w1, 2) = w1 −125,
and
Q2
w(w1) = −125
2
−2w1 + 2.5(w1)2
100
,
which is valid within C2 = {50 ≤w1 ≤60}.
The Stage 1 objective is min h1 + f 1 + 2w1 + Q2
y(w1) + Q2
w(w1), so that
the Stage 1 problem reads
min h1 + f 1 −7w1 + (w1)2
20
−125
2
s.t. w1 −h1 + f 1 = 50,
w1, h1, f 1 ≥0 .


## Page 270

7.3 Other Approaches to Multiple Stages
251
Its optimal solution, w1 = 60, h1 = 10, belongs to C2 and is thus also the
optimal solution of the global problem with objective value −292.5.
Exercises
1. Consider Example 1 with quadratic terms as in this section and take
1 ≤y1 ≤2, 1 ≤y2
1 ≤2, 0 ≤y2
2 ≤1 as a starting point. Show that
the following steps are generated. Obtain 0.5Q3
1(y2
1) + 0.5Q3
2(y2
1) =
5
4 −1
4y2
1. In t = 2, k = 1, solution v is x2
1 = 0, y2
1 = y1 −1 while w is
y2
1 = 1, x2
1 = 2−y1, both with w2
1 = 0. A cut x2
1+2w2
1+ 1
4y2
1 ≤9
4 −y1 is
added. The new starting point is v, which corresponds to 0 ≤y2
1 ≤1.
Then the case t = 2, k = 1 is as in the text, yielding
Q2
1(y1) = 7
2 −y1 and C2
1(y1) = {0 ≤y1 ≤2}.
In t = 2, k = 2, the calculations appear in the text, we ob-
tain Q2
2(y1) = 6 −y1 and C2(y1) = {1 ≤y1 ≤3}. Thus, in
t = 1, z1 = x1 + 2w1 + (w1)2 + 19
4 −y1/2 and C = {1 ≤y1 ≤2}.
Again, the solution v : x1 = 1, y1 = 0, w1 = 0 does not coincide with
w : x1 = 2, y1 = 1, w1 = 0. A cut x1 −y1
2 + w1 ≤3/2 is generated.
The new starting point now coincides with the one in the text and
the solution is obtained in one more iteration.
2. Does the block separable property depend on having a single prod-
uct? To help answer this question, take the example in the block
separability paragraph and assume a second product with revenue
0.6 in normal time and 0.3 in overtime. One worker produces 10 such
products in one stage. Obtain Qt+1
y
(wt),
(a) if demand in Period t is known to be 400;
(b) if demand in Period t is uniform continuous within [0, 500] and
[0, 100], respectively, for the two periods.
3. In the case of one product, obtain Qt+1
y
(wt) if demand follows a
negative exponential distribution with known parameter λ. Based on
Louveaux [1978], extend the MQSP to the piecewise convex case,
then solve the problem with λ = 0.01 and 0.02 for the two periods.
7.3
Other Approaches to Multiple Stages
Many two-stage methods may also be enhanced for multiple stages using
some form of block separability. One such approach assumes deviations
from some mean value can be corrected by a penalty only relating to the
current period. This method basically applies a simple recourse strategy in


## Page 271

252
7. Multistage Stochastic Programs
every period. For example, in Kallberg, White and Ziemba [1982] and Kusy
and Ziemba [1986], penalties are imposed to meet ﬁnancial requirements
in each period of a short-term ﬁnancial planning model. With this type
of penalty, the various simple recourse methods may be applied to achieve
eﬃcient computation.
Other methods that seem particularly adapted for multiple stages in-
clude some strict separation of solutions for diﬀerent scenarios by imposing
nonanticipativity constraints explicitly. For example, the progressive hedg-
ing algorithm (PHA) is easily adapted by simply deﬁning the projection,
Π, to project onto the space of nonanticipative solutions by deﬁning it as
the conditional expectation of all solutions at time t that correspond to the
same history up to t.
The PHA is particularly well-adapted for problems, such as networks,
where maintaining the original problem structure in each scenario problem
leads to eﬃciency. Computational experience on such models (see Mulvey
and Vladimirou [1991b]) indicates that PHA may perform well in these
circumstances.
Another approach for multistage problems that appears to have par-
ticular potential for nonlinear problems is a method from Mulvey and
Ruszczy´nski [1995] called diagonal quadratic approximation (DQA). This
method approximates quadratic penalty terms in a Lagrangian type of ob-
jective so that each subproblem is again easy to solve and can be spread
across a wide array of distributed processors. DQA appears to have par-
ticular advantages for nonlinear problems because it requires few addi-
tional assumptions. Computational results suggest it is even useful for linear
problems.
Exercise
1. Show how to implement PHA on Example 1. Follow three iterations
of the algorithm.


## Page 272

8
Stochastic Integer Programs
As seen in Section 3.3, properties for stochastic integer programs are scarce.
The absence of general eﬃcient methods reﬂects this diﬃculty. Some tech-
niques have been proposed that address speciﬁc problems or use a particular
property. Clearly, much work needs to be done to solve integer stochastic
programs eﬃciently. The available techniques described here provide ele-
ments of answers to start solving some of the integer programs. This ﬁeld
is expected to evolve a great deal in the future.
8.1
Integer L-Shaped Method
In this section, we present a general scheme for solving stochastic inte-
ger programs. For the sake of completeness, we recall the deﬁnition of a
stochastic integer program as
(SIP)
min
x∈X z = cT x + Eξ min {q(ω)T y|Wy = h(ω) −T(ω)x, y ∈Y }
s. t. Ax = b,
where the deﬁnitions of c, b,ξ, A, W, T, and h are as before. However, X
and/or Y contains some integrality or binary restrictions on x and/or y.
We may again deﬁne a deterministic equivalent program of the form:
(DEP)
min
x∈X z = cT x + Q(x)
s. t. Ax = b,


## Page 273

254
8. Stochastic Integer Programs
with Q(x) the expected value of the second stage deﬁned as in Section 3.1.
Let ¯X be the polytope deﬁned by the set of constraints in X other than
those deﬁning the ﬁrst-stage variable type. Hence, with continuous ﬁrst-
stage variables, X = ¯X ∩ℜn1
+ , and for problems with integer ﬁrst-stage
variables, X = ¯X ∩Zn1
+ . At a given stage of the algorithm, we consider the
current problem (CP):
(CP)
min cT x + θ
(1.1)
s. t. Ax = b,
(1.2)
Dlx ≥dl, l = 1, · · · , r,
(1.3)
Elx + θ ≥el, l = 1, · · · , s,
(1.4)
x ≥0, θ ∈ℜ.
(1.5)
The current problem is obtained from DEP by three relaxations: the inte-
grality restrictions are relaxed in x ≥0, the restriction x ∈¯X is relaxed in
a number of constraints (1.3) called feasibility cuts, and the exact deﬁnition
of Q(x) is relaxed in a polyhedral representation by θ and the constraints
(1.4) called optimality cuts.
Relaxing the integrality requirement is the basis of any branch and cut or
branch and bound scheme. Integrality is recovered by the handling scheme
which creates a number of nodes we call pendant as long as they have not
been fully examined. The principle of branch and bound can be found in,
for example, Taha [1992].
First-stage constraints include Ax = b and x ∈¯X. Constraints put in ¯X
are precisely those that are typically relaxed. This is the case when they
are not known in advance, as for the induced constraints. It is also the
case for constraints that are well known but so numerous that it would
be unrealistic to impose all of them from the beginning. Relaxing these
constraints is thus a matter of reducing their number so that only those
needed along the way are imposed. Such is the case for subtour elimination
constraints in vehicle routing problems or for valid inequalities derived
by polyhedral combinatoric arguments (see, e.g., Nemhauser and Wolsey
[1988]).
Deﬁnition 1. A set of feasibility cuts is said to be valid at x if there exists
a ﬁnite r such that
x ∈{x|Dlx ≥dl, l = 1, · · · , r} implies x ∈¯X.
Note that weaker forms of validity may exist. In particular, if X = ¯X ∩Zn1
+ ,
x ∈{x|Dlx ≥dl, l = 1, · · · , r} ∩Zn1
+ implies x ∈X is a suﬃcient condition
for validity, which may be weaker than Deﬁnition 1.
Relaxing the exact representation of Q(x) by a polyhedral representation
is exactly what is done in the L-shaped or Benders decomposition method.
That it extends to the stochastic integer case will be indicated later in this
section.


## Page 274

8.1 Integer L-Shaped Method
255
Deﬁnition 2. A set of optimality cuts is said to be valid at x ∈X if there
exists a ﬁnite s such that
(x, θ) ∈{(x, θ)|Elx + θ ≥el, l = 1, · · · , s}
implies θ ≥Q(x).
Assumption 3. For ﬁxed x, Q(x) is computable in a ﬁnite number of
steps.
Integer L-shaped Method
Step 0. Set r = s = ν = 0, ¯z = ∞. The value of θ is set to −∞or
to an appropriate lower bound and is ignored in the computation. A list
is created that contains only a single pendant node corresponding to the
initial subproblem.
Step 1. Select some pendant node in the list as the current problem; if none
exists, stop.
Step 2. Set ν = ν + 1. Solve the current problem. If the current problem
has no feasible solution, fathom the current node; go to Step 1. Otherwise,
let (xν, θν) be an optimal solution.
Step 3. Check for any relaxed constraint violation. If one exists, add one
feasibility cut (1.3), set r = r + 1, and go to Step 2. If cT xν + θν > ¯z,
fathom the current problem and go to Step 1.
Step 4. Check for integrality restrictions. If a restriction is violated, create
two new branches following the usual branch and cut procedure. Append
the new nodes to the list of pendant nodes, and go to Step 1.
Step 5. Compute Q(xν) and zν = cT xν + Q(xν). If zν < ¯z, update ¯z = zν.
Step 6. If θν ≥Q(xν), then fathom the current node and return to Step 1.
Otherwise, impose one optimality cut (1.4), set s = s + 1, and return to
Step 2.
Proposition 4. Under Assumption 3, for any problem for which a valid
set of feasibility cuts and a valid set of optimality cuts exist, the integer
L-shaped method yields an optimal solution (when one exists) in a ﬁnite
number of steps.
Proof:
Finiteness comes directly from the fact that each of the three re-
laxations can be recovered in a ﬁnite way and that Step 5 is ﬁnite under
Assumption 3.
As we will see next, a multicut approach is often preferred. It suﬃces
then to replace the objective (1.1) and the optimality cuts (1.4) by their
multicut equivalents (5.3.1) and (5.3.4). Also, a valid set of optimality cuts


## Page 275

256
8. Stochastic Integer Programs
must exist for each realization of the random vector. This addition creates
no extra theoretical diﬃculty.
A set of valid feasibility cuts and optimality cuts is known to exist in
the continuous case and forms the basis of the classical L-shaped method
(Section 5.1). These cuts are based on duality theory in linear program-
ming. They can also be used in the case where only the ﬁrst-stage variables
contain some integrality restrictions. This oﬀers an interesting alternative
to the cutting plane method used in Wollmer [1980]. The ﬁrst application
of the integer L-shaped method was proposed by Laporte and Louveaux
[1993] for the case of binary ﬁrst- and second-stage decision variables. A
full characterization of the integer L-shaped method based on general du-
ality theory can be found in Carøe and Tind [1996]. A stochastic version
of the branch and cut method using statistical estimation of the recourse
function instead of exact evaluation can be found in Norkin, Ermoliev, and
Ruszczy´nski [1997]. We now present a simpliﬁed version of Carøe and Tind
[1996] for feasibility and optimality cuts based on second-stage branch and
bound decomposition when the random variable is discrete. We also include
a number of observations from Laporte and Louveaux [1993].
a. Feasibility cuts
As usual, let K2(ξ) denote the second-stage feasibility set for a given ξ and
K2 = ∩ξ∈ΞK2(ξ). Let also C2(ξ) denote the set of ﬁrst-stage decisions that
are feasible for the continuous relaxation of the second stage, i.e.,
C2(ξ) = {x|∃y s. t. Wy = h(ω) −T(ω)x, y ≥0}.
Clearly, K2(ξ) ⊂C2(ξ), and any induced constraint valid for C2(ξ) is also
valid for K2(ξ). Also, detecting that some point x ∈C2(ξ) does not belong
to K2(ξ) is relatively easy, as only a phase one problem is needed:
(P1)
w(x, ξ) = min eT v+ + eT v−
s. t. Wy + v+ −v−= h(ω) −T(ω)x,
y ∈Zn2
+ , v+, v−≥0.
(1.6)
As usual, x ∈K2(ξ) if and only if w(x, ξ) = 0. If x̸ ∈K2(ξ), we would
like to generate a feasibility cut. Let (y, v+, v−) be a solution to (P1), and
because x̸ ∈K2(ξ), we have w(x, ξ) = eT v+ + eT v−> 0. If y ∈Zn2
+ , then
a cut of the form (5.1.3) can be generated. If y̸ ∈Zn2
+ , then some of the
components of y are not integer. A branch and bound algorithm can be
applied to (P1). This will generate a branching tree where, at each node,
additional simple upper or lower bounds are imposed on some variables.
Let ρ = 1, . . . , R index all terminal nodes, i.e., nodes that have no suc-
cessors, of the second-stage branching tree. Let Y ρ be the corresponding
subregions. They form a partition of ℜn2
+ , i.e., ℜn2
+
= ∪ρ=1,...,RY ρ and


## Page 276

8.1 Integer L-Shaped Method
257
Y ρ ∩Y σ = ∅, ρ̸ = σ. Now, x ∈K2(ξ) if and only if x ∈∪ρ=1,...,RKρ
2(ξ),
where
Kρ
2(ξ) = {x|∃y ∈Y ρ s. t. Wy ≤h(ω) −T(ω)x, y ≥0}.
However, because Y ρ is obtained from ℜn2
+ by some branching process, it
is deﬁned by adding a number of bounds to some components of y. Thus,
Kρ
2(ξ) is a polyhedron for which linear cuts are obtained through a classical
separation or duality argument. It follows that x ∈K2(ξ) if and only if at
least one among R sets of cuts is satisﬁed.
In practice, one constructs the branching tree of the second stage asso-
ciated with one particular ¯x and generates one cut per terminal node of
the restricted tree. This means that one ﬁrst-stage feasibility cut (8.1.3)
corresponds to the requirement that one out of R cuts is satisﬁed. As ex-
pected, this takes the form of a Gomory function. It can be embedded in a
linear programming scheme by the addition of extra binary variables, one
for each of the R cuts, as follows. Assume the ρth cut is represented by
uT
ρ x ≤dρ. One introduces R binary variables, δ1, . . . , δR. The requirement
that at least one of the R cuts is satisﬁed is equivalent to
uT
ρ x ≤dρ + Mρ(1 −δρ), ρ = 1, . . . , R,
R

ρ=1
δρ ≥1,
δρ ∈{0, 1},ρ = 1, . . . , R,
where Mρ is a large number such that uT
ρ x ≤dρ + Mρ, ∀x ∈K1.
Finally, observe that x ∈K2 if and only x ∈K2(ξ), ∀ξ ∈Ξ. As in the
continuous case (Section 5.2), it is sometimes enough to consider x ∈K2(ξ)
for one particular ξ.
Example 1
Consider again Example 3.3, when the second stage is deﬁned as
−y1 + y2 ≤ξ −x1,
y1 + y2 ≤2 −x2,
y1, y2 ≥0 and integer,
where ξ takes on the values 1 and 2 with equal probability 0.5. It suﬃces
here to consider x ∈K2(1) because K2(1) ⊂K2(2). First, consider x =
(2, 2)T . From Section 5.2, we ﬁnd a violated continuous induced constraint:
x1 + x2 ≤3.


## Page 277

258
8. Stochastic Integer Programs
Next, consider x = (1.4, 1.6)T . Problem (P1) is
min v1 + v2
s. t. −y1 + y2 −v1 ≤−0.4,
y1 + y2 −v2 ≤0.4,
y1, y2 ≥0 and integer,
where v1 and v2 correspond to v−in (1.6) and v+ is not needed due to the
inequality form of the constraints. The optimal solution of the continuous
relaxation of (P1) is given by the following dictionary:
w = v1 + v2,
y1 = 0.4 + y2 + s1 −v1,
s2 = 0 −2y2 −s1 + v1 + v2.
Its solution is w = 0, which implies x ∈C2(1). However, y1 is not integer.
Branching creates two nodes, y1 ≤0 and y1 ≥1, respectively. In the ﬁrst
branch, the bound y1 ≤0 creates the additional constraint y1 + s3 = 0.
After one dual iteration, the following optimal dictionary is obtained:
w = 0.4 + y2 + s1 + s3 + v2,
y1 = 0 −s3,
s2 = 0.4 −y2 + s3 + v2,
v1 = 0.4 + y2 + s1 + s3.
Associating the dual variables (−1, 0, −1) with the right-hand sides (1−x1,
2 −x2, 0), one obtains the feasibility cut, x1 −1 ≤0, for this branch.
Similarly, in the second branch, the bound y1 ≥1 creates a constraint
y1 −s3 = 1. After two dual iterations, the optimal dictionary is:
w = 0.6 + y2 + s2 + s3 + v1,
y1 = 1 + s3,
v2 = 0.6 + y2 + s2 + s3,
s1 = 0.6 −y2 + s3 + v1.
Associating the dual variables (0, −1, 1) to the right-hand sides (1 −x1,
2−x2, 1), one obtains the feasibility cut, x2 −1 ≤0, for the second branch.
Thus, R = 2, as the solutions in the two nodes satisfy the integrality
requirement and are thus terminal. The feasibility cut is thus, as required,
that either x1 −1 ≤0 or x2 −1 ≤0 must be satisﬁed. Because we also have
x1 ≤2 and x2 ≤2, we may take M1 = M2 = 1 so that we have to impose


## Page 278

8.1 Integer L-Shaped Method
259
the following set of conditions:
x1 ≤2 −δ1,
x2 ≤2 −δ2,
δ1 + δ2 ≥1,
δ1, δ2 ∈{0, 1}.
b. Optimality cuts
We consider here a multicut approach,
θ =
K

k=1
θk,
where, as usual, K denotes the cardinality of Ξ. We search for optimality
cuts on a given θk. Based on branching on the second-stage problem, one
obtains a partition of ℜn2
+ into R terminal nodes Y ρ = {y|aρ ≤y ≤bρ},
ρ = 1, . . . , R. The objective value of the second-stage program over Y ρ is
Qρ(xν, ξk) = min{qT y|Wy = h(ξk) −T(ξk)xν, aρ ≤y ≤bρ}.
It is the solution of a linear program that by classical duality theory is also
Qρ(xν, ξk) = (πρ)T (h(ξk) −T(ξk)xν) + (πρ)T aρ + (¯πρ)T bρ},
where πρ, πρ, and ¯πρ are the dual variables associated with the original
constraints, lower and upper bounds on y ∈Y ρ, respectively.
To simplify notation, we represent this expression as:
Qρ(xν, ξk) = (σρ
k)T xν + τ ρ
k ,
with (σρ
k)T = −(πρ)T T(ξk) and τ ρ
k = (πρ)T h(ξk) + (πρ)T aρ + (¯πρ)T bρ.
By duality theory, we know that Qρ(x, ξk) ≥(σρ
k)T xν + τ ρ
k . Moreover,
Q(x, ξk) = minρ=1,...,R Qρ(x, ξk). Thus,
θk ≥pk( min
ρ=1,...,R(σρ
k)T xν + τ ρ
k ).
(1.7)
Note that some of the terminal nodes may be infeasible, in which case their
dual solutions contain unbounded rays with dual objective values going to
∞, so that the minimum is in practice restricted to the feasible terminal
nodes.
This expression takes the form of a Gomory function, as expected. Again,
it unfortunately requires R extra binary variables to be included in a mixed
integer linear representation.


## Page 279

260
8. Stochastic Integer Programs
Example 2
Consider the second-stage program
Eξ min{−8y1−9y2 s. t. 3y1+2y2 ≤ξ, −y1+y2 ≤x1, y2 ≤x2, y ≥0, integer}.
Consider the value ξ1 = 8 and ¯x = (0, 6)T . The optimal dictionary of the
continuous relaxation of the second-stage program is:
z = −136/5 + 17s1/5 + 11s2/5,
y1 = 8/5 −s1/5 + 2s2/5,
y2 = 8/5 −s1/5 −3s2/5,
s3 = 22/5 + s1/5 + 3s2/5,
where s1, s2, and s3 are the slack variables of the three constraints. Branch-
ing on y1 gives two nodes, y1 ≤1 and y1 ≥2, which turn out to be the only
two terminal nodes. For the ﬁrst node, adding the constraint y1 + s4 = 1
yields the following dictionary after one dual iteration:
z = −17 + 9s2 + 17s4,
s1 = 3 + 2s2 + 5s4,
y2 = 1 −s2 −s4,
s3 = 5 + s2 + s4,
y1 = 1 −s4.
We thus have dual variables (0, −9, 0) associated with the right-hand side
(8, x1, x2) of the constraints and −17 associated with the bound 1 on y1.
Hence, Q1(¯x, 8) = −9x1 −17.
Similarly, we add y1 −s4 = 2 for the second node. We obtain:
z = −25 + 9/2s1 + 11/2s4,
y1 = 2 + s4,
y2 = 1 −s1/2 −3/2s4,
s3 = 5 + s1/2 + 3/2s4,
s2 = 1 + s1/2 + 5/2s4.
We now have dual variables, (−9/2, 0, 0), associated with the right-hand
side (8, x1, x2) of the constraints and 11/2 associated with the lower bound
2 on y1. Hence, Q2(¯x, 8) = −25. Applying (1.7), we conclude that
θ1 ≥p1 min(−9x1 −17, −25),
where p1 is the probability of ξ = ξ1.


## Page 280

8.1 Integer L-Shaped Method
261
c. Lower bounding functionals
Lower bounding functionals are simply valid inequalities that apply to
Q(x). As ﬁniteness of the integer L-shaped method is obtained through
the optimality cuts (1.4) or their variants, no special requirement is needed
for lower bounding functionals.
It is not even required that they be binding at at least one point. On the
other hand, they should be eﬀective in describing a valid bound other than
the existing ones in a suﬃciently large region. Lower bounding functionals
can often be derived from the context of the problem. Such is the case, for
example, in a priori optimization problems (Laporte, Louveaux, and Mer-
cure [1994]) and in a location problem with stochastic demands (Laporte,
Louveaux, and Van Hamme [1994]).
For problems whose second stage is best described as a mathematical
program (rather than an implicit or closed form expression), lower bound-
ing functionals are easily derived from the related continuous problem. As
before, let
Q(x, ξ(ω))= min
y {q(ω)T y|Wy = h(ω) −T(ω)x, y ≥0 and integer}
(1.8)
with Q(x)= EξQ(x,ξ).
(1.9)
We introduce the following notation for the solution to the continuous
relaxation of the second-stage program,
C(x, ξ(ω))= min
y {q(ω)T y|Wy = h(ω) −T(ω)x, y ≥0}
(1.10)
with C(x)= EξC(x,ξ),
(1.11)
with the usual conventions for infeasible and unbounded cases and +(∞)+
(−∞) = +(∞) for the expectation.
Proposition 5. Any continuous L-shaped optimality cut is a valid lower
bound on Q(x).
Proof:
First note that Q(x, ξ) ≥C(x, ξ) for all x and all ξ, where this
result also holds if some problems are unbounded or infeasible. Taking
expectations implies Q(x) ≥C(x). The conclusion follows by applying the
continuous L-shaped optimality cut to C(x), namely,
Q(x) ≥C(x) ≥C(xν) + ∂C(xν)T (x −xν),
(1.12)
where xν is any ﬁrst-stage feasible solution.
Corollary 6. The following is a valid lower bounding functional on Q(x):
θ ≥C(xν) + ∂C(xν)(x −xν).
(1.13)


## Page 281

262
8. Stochastic Integer Programs
Example 2 (continued)
From the optimal continuous relaxation of the second stage for ξ1, we obtain
a continuous optimality cut (1.13),
θ1 ≥p1(−136/5 −11/5x1),
which is more restrictive than p1 min(−9x1 −17, −25) for x1 ≥1.5.
8.2
Simple Integer Recourse
As seen in Section 3.3, a two-stage stochastic program with simple integer
recourse can be transformed into
min cT x+
m

i=1
Ψi(χi)
s. t. Ax = b,Tx = χ, x ∈X ⊂Zn1
+ ,
(2.1)
where
Ψi(χi) = q+
i ui(χi) + q−
i vi(χi)
(2.2)
with
ui(χi) = E⌈ξi −χi⌉+,
(2.3)
deﬁned as the expected shortage, and
vi(χi) = E⌈χi −ξi⌉+,
(2.4)
deﬁned as the expected surplus. As before, we assume
q+
i ≥0, q−
i ≥0.
Also from Section 3.3, we know that the values of the expected shortage and
surplus can be computed in ﬁnitely many steps, either exactly or within a
prespeciﬁed tolerance ε.
Before turning to algorithms, we still need some results concerning the
functions Ψi; for simplicity in the exposition we omit the index i. As we also
know from Section 3.3, the function Ψ is generally not convex and is even
discontinuous when ξ has a discrete distribution. It turns out, however,
that some form of convexity exists between function values evaluated in
(not necessarily integer) points that are integer length apart. Thus, let
x0 ∈ℜbe an arbitrary point. Let i ∈Z be some integer.
Deﬁne x1 = x0 + i, and for any j ∈Z, j ≤i, xλ = x0 + j. Equivalently,
we may deﬁne
xλ = λx0 + (1 −λ)x1,
λ = (i −j)/i.


## Page 282

8.2 Simple Integer Recourse
263
In the following, we will use x as an argument for Ψ as if Tx = Ix = χ
without losing generality. We make T explicit again when we speak of a
general problem and not just the second stage.
Proposition 7. Let x0 ∈ℜ, i, j ∈Z with j ≤i, x1 = x0 + i, xλ = x0 + j.
Then
Ψ(xλ) ≤λΨ(x0) + (1 −λ)Ψ(x1)
(2.5)
with λ = (i −j)/i.
Proof: We prove that Ψ(x+1)−Ψ(x) is a nondecreasing function of x. We
leave it as an exercise to infer that this is a suﬃcient condition for (2.5) to
hold. Using (3.3.16) and (3.3.17), we respectively obtain u(x + 1) −u(x) =
−(1−F(x)) and v(x+1)−v(x) = ˆF(x+1), where F is again the cumulative
distribution function of ξ and ˆF is deﬁned as in Section 3.3. With this,
Ψ(x + 1) −Ψ(x) = q−ˆF(x + 1) −q+(1 −F(x)).
The result follows as q+ ≥0, q−≥0 and ˆF and F are nondecreasing.
This means that we can draw a piecewise linear convex function through
points that are integer length apart. Such a convex function is called a
ρ-approximation rooted at x if it is drawn at points x ± κ, κ integer. In
Figures 1 and 2, we provide the ρ-approximations rooted at x = 0 and
x = 0.5, respectively, for the case in Example 3.1.
FIGURE 1. The ρ-approximation rooted at x = 0.
If we now turn to discrete random variables, we are interested in the dif-
ferent possible fractional values associated with a random variable. As an
example, if ξ can take on the values 0.0, 1.0, 1.2, 1.6, 2.0, 2.2, 2.6, and 3.2
with some given probability, then the only possible fractional values are
0.0, 0.2, and 0.6. Let s1 < s2 < · · · < sS denote the S ordered possible
fractional values of ξ. Deﬁne sS+1 = 1. Let the extended list of fractionals
be all points of the form j + sl, j ∈Z, 1 ≤l ≤S. This extended list is a
countable list that contains many more elements than the possible values
of ξ. In the example, 0.2, 0.6, 3.0, 3.6, 4.0, 4.2, · · · are in the extended list of
fractionals but are not possible values of ξ.


## Page 283

264
8. Stochastic Integer Programs
FIGURE 2. The ρ-approximation rooted at x = 0.5.
Lemma 8. Let ξ be a discrete random variable. Assume that S is ﬁnite.
Let a ∈ℜ. Deﬁne frac by a = ⌊a⌋+ frac and deﬁne j by sj ≤frac < sj+1.
Then
Ψ(x) is constant within the open interval (⌊a⌋+ sj, ⌊a⌋+ sj+1) ,
Ψ(x) ≥max {Ψ(⌊a⌋+ sj), Ψ(⌊a⌋+ sj+1) },
∀x ∈(⌊a⌋+ sj, ⌊a⌋+ sj+1).
Proof:
The proof can be found in Louveaux and van der Vlerk [1993].
The lemma states that Ψ(x) is piecewise constant in the open interval
between two consecutive elements of the extended list of fractionals and
that the values in points between two consecutive elements of that list are
always greater than or equal to the values of Ψ(·) at these two consecutive
elements in the extended list. The reader can easily observe this property
in the examples that have already been given.
Corollary 9. Let ξ be a random variable with S = 1. Let ρ(·) be a ρ-
approximation of Ψ(·) rooted at some point in the support of ξ. Then
ρ(x) ≤Ψ(x), ∀x ∈ℜ.
Moreover, ρ is the convex hull of the function Ψ.
Proof:
The function ρ is a lower bound of Ψ by Lemma 5. It is the convex
hull of Ψ because it is convex, piecewise linear, and it coincides with Ψ in
all points at integer distance from the root.
Among the cases where S = 1, the most natural one in the context of
simple integer recourse is when ξ only takes on integer values. A well-known
such case is the Poisson distribution. Then the ρ-approximation rooted at
any integer point is the piecewise linear convex hull of Ψ that coincides
with Ψ at all integer points.
We use Proposition 7 and Corollary 9 to derive ﬁnite algorithms for two
classes of stochastic programs with simple integer recourse.


## Page 284

8.2 Simple Integer Recourse
265
a. χs restricted to be integer
Integral χ is a natural assumption, because one would typically expect ﬁrst-
stage variables to be integer when second-stage variables are integer. It suf-
ﬁces then for T to have integer coeﬃcients. By deﬁnition of a ρ-approxima-
tion rooted at an integer point, solving (2.1) is thus equivalent to solving
min{cT x +
m2

i=1
ρi(χi)|Ax = b, χ = Tx, x ∈X},
(2.6)
where T is such that x ∈X implies χ is integer, and ρi is a ρ-approximation
of Ψi rooted at an integer point.
Because the objective in (2.6) is piecewise linear and convex, problem
(2.6) can typically be solved by a dual decomposition method such as
the L-shaped method. We recommend using the multicut version because
we are especially concerned with generating individual cut information for
each subproblem that may require many cuts. This amounts to solving a
sequence of current problems of the form
min
x∈X,θ∈ℜm2{cT x +
m2

i=1
θi|Ax = b, χ = Tx,
Eilχi + θi ≥eil, i = 1, · · · , m2, l = 1, · · · , si}.
(2.7)
In this problem, the last set of constraints consists of optimality cuts. They
are used to deﬁne the epigraph of Ψi, i = 1, · · · , m2. Optimality cuts are
generated only as needed. If χν
i is a current iterate point with θν
i < Ψi(χν
i ),
then an additional optimality cut is generated by deﬁning
Eik = Ψi(χν
i ) −Ψi(χν
i + 1)
(2.8)
and
eik = (χν
i + 1)Ψi(χν
i ) −χν
i Ψi(χν
i + 1),
(2.9)
which follows immediately by looking at a linear piece of the graph of Ψi.
The algorithm iteratively solves the current problem (2.7) and generates
optimality cuts until an iterate point (χν, θν) is found such that θν
i =
Ψi(χν
i ), i = 1, · · · , m2. It is important to observe that the algorithm is
applicable for any type of random variable for which Ψis can be computed.
Example 3
Consider two products, i = 1, 2, which can be produced by two machines
j = 1, 2. Demand for both goods follows a Poisson distribution with expec-
tation 3. Production costs (in dollars) and times (in minutes) of the two


## Page 285

266
8. Stochastic Integer Programs
products on the two machines are as follows:
Machine
1
2
Product 1
3
2
2
4
5
Cost/Unit
Machine
Finishing
1
2
1
2
Product 1
20
25 4
7
2
30
25 6
5
Time/Unit Time/Unit
The total time for each machine is limited to 100 minutes. After machining,
the products must be ﬁnished. Finishing time is a function of the machine
used, with total available ﬁnishing time limited to 36 minutes. Production
and demand correspond to an integer number of products. Product 1 sells
at $4 per unit. Product 2 sells at $6 per unit. Unsold goods are lost.
Deﬁne xij = number of units of product i produced on machine j and
yi(ξ) = amount of product i sold in state ξ. The problem reads as follows:
min 3x11 + 2x12 + 4x21 + 5x22 + Eξ{−4y1(ξ) −6y2(ξ)}
s. t. 20x11 + 30x21 ≤100, y1(ξ) ≤ξ1,
25x12 + 25x22 ≤100, y2(ξ) ≤ξ2,
4x11 + 7x12 + 6x21 + 5x22 ≤36, y1(ξ) ≤x11 + x12,
xij ≥0 integer, y2(ξ) ≤x21 + x22,
y1(ξ), y2(ξ) ≥0 integer.
Letting y+
i (ξ) = ξi −yi(ξ), one obtains an equivalent formulation,
min 3x11 + 2x12 + 4x21 + 5x22 + Eξ{4y+
1 (ξ) + 6y+
2 (ξ)} −30
s. t. 20x11 + 30x21 ≤100, y+
1 (ξ) ≥ξ1 −χ1,
25x12 + 25x22 ≤100, y+
2 (ξ) ≥ξ2 −χ2,
4x11 + 7x12 + 6x21 + 5x22 ≤36, y+
1 (ξ), y+
2 (ξ) ≥0 and integer,
x11 + x12 = χ1,
x21 + x22 = χ2,
xij ≥0 and integer.
This representation puts the problem under the form of a simple recourse
model with expected shortage only.
Let us start with the null solution, xij = 0, χi = 0, i, j = 1, 2 with
θi = −∞, i = 1, 2. We compute u(0) = E⌈ξ⌉+ = µ+ = 3; hence
Ψ1(0) = 12, Ψ2(0) = 18, where we have dropped the constant, −30, from


## Page 286

8.2 Simple Integer Recourse
267
the objective for these computations. To construct the ﬁrst optimality
cuts, we also compute u(1) = u(0) −1 + F(0) = 2 + .05 = 2.05. Thus,
E11 = 4(3 −2.05) = 3.8, e11 = 4(1 ∗3 −0 ∗2.05) = 12, deﬁning the opti-
mality cut θ1 + 3.8χ1 ≥12. As χ2 = χ1, E21 and e21 are just 1.5 times E11
and e1, respectively, yielding the optimality cut θ2 + 5.7χ2 ≥18.
The current problem becomes
min 3x11 + 2x12 + 4x21 + 5x22 −30 + θ1 + θ2
s. t.
20x11 + 30x21 ≤100,
25x12 + 25x22 ≤100,
4x11 + 7x12 + 6x21 + 5x22 ≤36,
x11 + x12 = χ1,
x21 + x22 = χ2,
θ1 + 3.8χ1 ≥12,
θ2 + 5.7χ2 ≥18,
xij ≥0, integer.
We obtain the solution x11 = 0, x12 = 4, x21 = 1, x22 = 0, θ1 = −3.2, θ2 =
12.3. We compute u(4) = u(0) + 	3
l=0(F(l) −1) = 0.31936 and Ψ1(4) =
1.277 > θ1. A new optimality cut is needed for Ψ1(·). Because Ψ(5) =
0.5385, the cut is 0.739χ1 + θ1 ≥4.233. We also have u(1) = 2.05, hence
Ψ2(1) = 12.3 = θ2, so no new cut is generated for Ψ2(·).
At the next iteration, with the extra optimality cut on θ1, we obtain a
new solution of the current problem as x11 = 0, x12 = 2, x21 = 3, x22 = 0,
θ1 = 4.4, θ2 = 0.9. Here, two new optimality cuts are needed:
2.312χ1 + θ1 ≥9.623
and
2.117χ2 + θ2 ≥10.383.
The next iteration gives x11 = 0, x12 = 3, x21 = 2, x22 = 0, θ1 = 2.688,
θ2 = 6.6 as a solution of the current problem. Because Ψ2(2) = 7.5 > θ2, a
new cut is generated, i.e., 3.467χ2 + θ2 ≥14.435. The next iteration point
is x11 = 0, x12 = 3, x21 = 2, x22 = 0, θ1 = 2.688, θ2 = 7.5, which is the
optimal solution with total objective value −5.812.
b. The case where S = 1, χ not integral
Details can again be found in Louveaux and van der Vlerk [1993]; we illus-
trate the results with an example. Consider Example 3 but with the xijs
continuous. Because we still assume the random variables follow a Poisson
distribution, the example indeed falls into the category S = 1; only integer
realizations are possible.
For a given component i, the ρi-approximation rooted at an integer de-
ﬁnes the convex hull of the function Ψi(.). All optimality cuts deﬁned at


## Page 287

268
8. Stochastic Integer Programs
integer points are thus valid inequalities. If we take Example 3 again and
impose all optimality cuts at integer points, the continuous solution is
x11 = 0, x12 = 3, x21 = 2, x22 = 0, and no extra cuts are needed here.
Now assume the objective coeﬃcients of x12 and x21 are 1 and 4.5 (instead
of 2 and 4). The solution of the stochastic program with continuous ﬁrst-
stage decisions and all optimality cuts imposed at integer points becomes
x11 = 0, x12 = 4, x21 = 1.33, x22 = 0, and thus, χ1 = 4, χ2 = 1.33.
We now illustrate how to deal with a noninteger value of some χi. Now,
u(1.33) = 3 −1 + F(0) = 2.05 and therefore Ψ2(1.33) = 12.3 > θ2 . This
requires imposing a new optimality cut. By Lemma 8, we know Ψ2(.) is
constant within (1, 2) with value 12.3.
Let δa = 1 if χ2 > 1 and 0 otherwise,
δb = 1 if χ2 < 2 and 0 otherwise.
The cut imposes that θ2 ≥12.3 if 1 < χ2 < 2, i.e., if δa = δb = 1. This is
realized by the following constraints:
χ2 ≤1 + 10δa,χ2 ≥(1 + ǫ)δa,
χ2 ≤10 −(8 + ǫ)δb,χ2 ≥2 −2δb,
θ2 ≥12.3 −100(2 −δa −δb),
where 10 and 100 are suﬃciently large numbers to serve as bounds on
χ2 and −θ2, respectively, and ǫ is a very small number. Thus, deﬁning a
function Ψi(.) to be constant in some interval requires two extra binary
variables and three extra constraints. It is thus reasonable to ﬁrst consider
optimality cuts that deﬁne the convex hull.
Continuing the example, we solve the current problem with the three
additional constraints. The solution is x11 = 0, x12 = 3.43, x21 = 2, x22 = 0
with χ1 = 3.43, χ2 = 2, θ1 = 2.08, θ2 = 7.5. Thus, one more set of cuts
is needed to deﬁne Ψ1 in the interval (3, 4). The ﬁnal solution is x11 =
0, x12 = 3, x21 = 1, x22 = 0, θ1 = 2.689, θ2 = 12.3, and z = −7.51.
8.3
Binary First-Stage Variables
In this section, we present optimality cuts derived by Laporte and Louveaux
[1993] for problems with a binary ﬁrst stage. These cuts are weaker than
those deﬁned by the integer L-shaped method. On the other hand, they
apply even if the random variables take on many realizations, a situation
where the integer L-shaped method would be ineﬃcient. Observe that at
this level no restriction is imposed on the second-stage problem. However,
in addition to Assumption 3, we need the existence of a lower bound.
Assumption 10. There exists a ﬁnite lower bound L satisfying
L ≤min
x {Q(x)|Ax = b, x ∈X}.


## Page 288

8.3 Binary First-Stage Variables
269
Assumption 3 seems like a minimal assumption one can make. In practice,
however, it is far from being satisﬁed in all circumstances. As an example, if
the second stage consists of a mixed integer program and the random vari-
ables are continuous, no general method is yet available to obtain Q(x).
On the other hand, many examples that satisfy Assumption 3 are avail-
able, in particular for location and routing problems. In Assumption 10,
no requirement is made that the bound L should be tight, although it is
desirable to have L as large as possible. Examples of how to ﬁnd L will be
given later.
Proposition 11. Let xi = 1, i ∈S, and xi = 0, i̸ ∈S be some ﬁrst-stage
feasible solution. Let qS = Q(x) be the corresponding recourse function
value. Deﬁne the optimality cut as
θ ≥(qS −L)(

i∈S
xi −

i̸∈S
xi) −(qS −L)(|S| −1) + L.
(3.1)
Then the set of optimality cuts (3.1) deﬁned for all ﬁrst-stage feasible so-
lutions is a valid set of optimality cuts.
Proof:
Deﬁne
δ(x, S) =

i∈S
xi −

i̸∈S
xi.
(3.2)
Now, δ(x, S) is always less than or equal to |S|. It is equal to |S| only if
xi = 1, i ∈S, and xi = 0, i̸ ∈S. In that case, the right-hand side of (3.1)
takes the value qS and the constraint θ ≥qS is valid as Q(x) = qS. In all
other cases, δ(x, S) is smaller than or equal to |S| −1, which implies that
the right-hand side of (3.1) takes a value smaller than or equal to L, which
by Assumption 2 is a valid lower bound on Q(x) for all feasible x. The
result follows from the fact that there is only a ﬁnite (although potentially
very large) number of ﬁrst-stage decisions.
Readers more familiar with geometrical representations may see (3.1) as
a half-space, in the (δ, θ) space, situated above a line going through the
two points (|S|, qS) and (|S| −1, L).
Example 4
Consider a two-stage program, where the second stage is given by
min −2y1 −3y2,
s. t. y1 + 2y2 ≤ξ1 −x1,
y1 ≤ξ2 −x2
y ≥0, integer.
Assume ξ = (2, 2)T or (4, 3)T with equal probability 1/2 each. Find a lower
bound L on Q(x) and derive a cut of type (3.1) if the current iterate point
is x = (0, 1)T .


## Page 289

270
8. Stochastic Integer Programs
1. The second stage is equivalent to −max 2y1 + 3y2. Because the ﬁrst-
stage decisions are binary, largest values of ys are obtained with x =
(0, 0)T . To obtain a lower bound L, we simply drop the requirement
that y should be integer and solve
min −2y1 −3y2
s.t. y1 + 2y2 ≤ξ1,
y1 ≤ξ2,
y1, y2 ≥0.
For ξ = (2, 2)T , the solution is y = (2, 0)T and Q(x, ξ) = −4, while
for ξ = (4, 3)T , the solution is y = (3, 0.5)T with Q(x, ξ) = −7.5. This
results in L = 0.5 ∗(−4) + 0.5 ∗(−7.5) = −5.75. (Alternatively, in
this simple example, we may have maintained the requirement that
y is integer and obtained the better bound L = −5.5. In general, this
approach seems more diﬃcult to implement. We continue here with
L = −5.75.)
2. Here, δ(x, S) = x2 −x1 because x1 = 0 and x2 = 1. For ξ = (2, 2)T ,
the second stage becomes
min −2y1 −3y2
s.t. y1 + 2y2 ≤2,
y1 ≤1,
y1, y2 ≥0, integer
with solution y = (0, 1)T and Q(x, ξ) = −3. For ξ = (4, 3)T , the
second stage becomes
min −2y1 −3y2
s.t. y1 + 2y2 ≤4,
y1 ≤2,
y1, y2 ≥0, integer
with solution y = (2, 1)T and Q(x, ξ) = −7. We conclude that qS =
−5 and that the optimality cut (3.1) reads
θ ≥0.75(x2 −x1) −5.75.
From a theoretical and practical point of view, it is not satisfactory to
have a method that could lead to considering all ﬁrst-stage feasible decision
vectors. Improvements can be sought in two directions. One way is to ﬁnd
more eﬃcient optimality cuts. The second approach is to append lower
bounding functionals.


## Page 290

8.3 Binary First-Stage Variables
271
a. Improved optimality cuts
Improvement on (3.1) can be obtained when more information is available
on Q(x), such as other bounds.
Deﬁne the set N(s, S) of so-called s-neighbors of S as the set of solutions
{x|Ax = b, x ∈X, δ(x, S) = |S| −s}, where δ(x, S) is as in (3.2). Let
λ(s, S) ≤minx∈N(s,S) Q(x), s = 0, · · · , |S| with λ(0, S) = qS.
Proposition 12. Let xi = 1, i ∈S, xi = 0, i̸ ∈S be some solution with
qS = Q(x). Deﬁne a = max {qS −λ(1, S), (qS −L)/2}. Then
θ ≥a(

i∈S
xi −

i̸∈S
xi) + qS −a|S|
(3.3)
is a valid optimality cut.
Proof:
For an s-neighbor, the right-hand side of (3.3) is equal to qS −as.
This is a valid lower bound on Q(x). This is obvious for s = 0. When s = 1,
qS −a is, by construction, bounded above by qS −(qS −λ(1, S)) = λ(1, S),
which by deﬁnition is a lower bound on 1-neighbors. When s = 2, qS −2a ≤
qS −2(qS −L)/2 = L. Finally, for s ≥3, qS −as ≤qS −2a, because a ≥0.
Hence, qS −as ≤L. Convergence is again guaranteed by θ ≥qS when
δ(x, S) = |S| and (3.3) improves on (3.1) for all 1-neighbors. The reader
more familiar with geometrical representations may now see (3.3) as a half-
space in the (δ, θ) space, situated above a line going through the two points
(|S|, qS) and (|S| −1, λ(1, S)) when a = qS −λ(1, S), or the two points
(|S|, qS) and (|S| −2, L) when a = (qS −L)/2.
A further improvement for s-neighbors is sometimes possible.
Proposition 13. Let xi = 1, i ∈S, xi = 0, i̸ ∈S be some solution with
qS = Q(x). Let 1 ≤t ≤|S| be some integer. Then (3.3) holds with
a = max{max
s≤t (qS −λ(s, S))/s; (qS −L)/(t + 1)}.
(3.4)
Proof: As before, for an s-neighbor, the right-hand side of (3.3) is qS −as.
By (3.4), as ≥qS −λ(s, S), for all s ≤t. Thus, qS −as ≤λ(s, S), which,
by deﬁnition, is a lower bound on Q(x) for all s-neighbors. When s ≥
t + 1, qS −as ≤L, and (3.3) remains valid.
As computing λ(s, S) for s ≤t with t large may prove diﬃcult, the
following proposition is sometimes useful.
Proposition 14. Deﬁne λ(0, S) = qS. Assume qS > λ(1, S). Then, if
λ(s −1, S) −λ(s, S) is nonincreasing in s for all 1 ≤s ≤⌊(qS −L)/(qS −
λ(1, S))⌋, (3.3) holds with a = qS −λ(1, S).
Proof:
We have to show that in applying Proposition 13, the maximum
in (3.4) is obtained for qS −λ(1, S). Let t = ⌊(qS −L)/(qS −λ(1, S))⌋. For


## Page 291

272
8. Stochastic Integer Programs
s ≤t, qS −λ(s, S) = 	s
i=1 (λ(i−1, S)−λ(i, S)). By assumption, each term
of the sum is smaller than the ﬁrst term of the sum, i.e., λ(0, S)−λ(1, S) =
qS−λ(1, S) so the total is less than s times this ﬁrst term. By deﬁnition of t,
we have t+1 ≥(qS −L)/(qS −λ(1, S)), or qS −λ(1, S) ≥(qS −L)/(t+1).
Clearly, much of the implementation is problem-dependent. We illustrate
here the use of these propositions in one example.
Example 5
Let i = 1, · · · , n denote n inputs and j = 1, · · · , m denote m outputs. Each
input can be used to produce various outputs. First-stage decisions are
represented by binary variables xij with costs cij and are equal to 1 if i is
used to produce j and equal to 0 otherwise. If input i is used for at least
one output, some ﬁxed cost fi is paid. To this end, the auxiliary variable zi
is deﬁned equal to 1 if input i is used and 0 otherwise. The level of output j
obtained when xij = 1 is a non-negative random variable ξij. A penalty rj
is incurred whenever the level of output j falls below a required threshold
dj. This is represented by the second-stage variable yξ
j taking the value 1.
The problem can be deﬁned as:
min
n

i=1
fizi +
n

i=1
m

j=1
cijxij + Eξ(
m

j=1
rjyξ
j )
(3.5)
s.t. xij ≤zi,
i = 1, · · · , n,
j = 1, · · · m,
(3.6)
n

i=1
ξijxij + djyξ
j ≥dj,
j = 1, · · · , m,
(3.7)
xij, zi, yξ
j ∈{0, 1},
i = 1, · · · , n,
j = 1, · · · , m,
(3.8)
where, in practice, the xij variables are only deﬁned for the possible com-
binations of inputs and outputs. In this problem, the second-stage recourse
function only depends on the x decisions so that the z variables may be
left over in our analysis of optimality cuts. Moreover, the second stage is
easily computed as
Q(x) =
m

j=1
rjP(

i∈S(j)
ξij < dj),
(3.9)
where
S(j) = {i|xij = 1}.
Let S = ∪m
j=1{(i, j)|i ∈S(j)}. To apply the propositions, we search for
lower bounds, λ(s, S), on the recourse function for all s-neighbors. To bound
qS −λ(1, S), observe that 1-neighbors can be obtained in two distinct ways.
The ﬁrst way is to have one xij, with (i, j) ∈S, going from one to zero
and all other xijs being unchanged. This implies for that particular j that,


## Page 292

8.3 Binary First-Stage Variables
273
in (3.9), P(	
i∈S(j) ξij < dj) increases in the neighboring solution, as S(j)
would contain one fewer term. Thus, for this type of 1-neighbor, Q(x) is
increased.
The second way is to have one xij, with (i, j) not in S, going from zero to
one, all other xijs being unchanged. For that particular j, P(	
i∈S(j) ξij <
dj) decreases in the neighboring solution. To bound the decrease of Q(x),
we simply assume P(	
i∈S(j) ξij < dj) vanishes so that
qS −λ(1, S) ≤max
j {rjP(

i∈S(j)
ξij < dj)}.
(3.10)
Also observe that in this example, Proposition 14 applies. Indeed, qS −
λ(s, S) can be taken as the sum of the s largest values of {rjP(	
i∈S(j) ξij <
dj)}. It follows that λ(s −1, S) −λ(s, S) is nonincreasing in s.
Moreover, in this example, we can also ﬁnd lower bounding functionals.
By looking at (3.7), the optimal solution of the continuous relaxation of
the second stage is easily seen to be
yξ
j = rj(dj −
n

i=1
ξijxij)+/dj, j = 1, . . . , m,
and therefore,
C(x) = Eξ[

j
rj(dj −
n

i=1
ξijxij)+/dj].
(3.11)
In fact, we just need to compute
C(x) = Eξ

j
rj(dj −

i∈S(j)
ξij)+/dj.
(3.12)
From (3.11), we may immediately apply Corollary 6 as
θ ≥qS +

ij∈S
aij(xij −1) +

ij̸∈S
aijxij
(3.13)
with
aij = −rj/djEξ[ξijP(

l∈S(j)
l̸=i
ξlj ≤dj −ξij)], i ∈S(j),
aij = −rj/djEξ[ξijP(

l∈S(j)
ξlj < dj)], i̸ ∈S(j),
and
qS = C(x) as in (3.12).


## Page 293

274
8. Stochastic Integer Programs
Example 6
We take Example 5 and consider the following numerical data. Let n =
4, m = 6, fi = 10, for all i, rj = 40 for all j. Let the cij coeﬃcients take
values between 5 and 15 as follows:
j =
1
2
3
4
5
6
i =
1
10 12
8
6
5
14
2
8
5
10
15 9
12
3
7
14
4
11 15
8
4
5
8
12 10 10 10.
Assume the ξij are independent Poisson random variables with parameters
j = 1 2 3 4 5 6
i =
1
4 4 5 3 3 8
2
5 2 4 8 5 6
3
2 8 3 4 7 5
4
3 5 6 4 6 5
and, ﬁnally, let the demands dj be given by
j =
1
2
3
4
5
6
dj
8
4
6
3
5
8.
As already said, we may apply Proposition 14 to this example. A second
possibility is to use the separability of Q(x) as
Q(x) =
m

j=1
Qj(x)
(3.14)
with
Qj(x) = rjP(

i∈S(j)
ξij < dj).
(3.15)
Bounding each Qj(x) separately, we deﬁne
θ =
m

j=1
θj
(3.16)
and use Propositions 13 or 14 to deﬁne a valid set of cuts for each θj
separately. Indeed, for one particular j, we have
θj = rjP(

i∈S(j)
ξij < dj)
(3.17)
and
λj(1, S) = rj min
t̸∈S(j) P(

i∈S(j)
ξij + ξtj < dj),
(3.18)


## Page 294

8.3 Binary First-Stage Variables
275
where λj(1, S) denotes a lower bound on Qj(x) for 1-neighbors of the cur-
rent solution obtained by changing xijs for that particular j only. Note that
in practice ﬁnding t is rather easy. Indeed, because all random variables are
independent Poisson, t is simply given by the random variable ξtj, t̸ ∈S(j),
with the largest parameter value.
We illustrate the generation of cuts for j = 1. First, a lower bound is
obtained by letting xi1 = 1, for all i. This gives L1 = 1.265.
Assume a starting solution xij = 0, all i, j. For j = 1, the probability in
the right-hand side of (3.15) is 1. Thus, Q1(x) = r1 = 40. Cut (3.3) becomes
θ1 ≥40 −19.368(x11 + x21 + x31 + x41) with the coeﬃcient a = 19.368
obtained from (qS,1 −L1)/2, where qS,1 is the notation for the value of
Q1(x). The continuous cut (3.13) is
θ1 ≥40 −20x11 −25x21 −10x31 −15x41.
The next iterate point is, e.g., x11 = 1, x21 = 0, x31 = 0, x41 = 1. Cut (3.3)
becomes θ1 ≥−16.788 + 20.368(x11 −x21 −x31 + x41) with the coeﬃcient
a = 20.368 now obtained from (qS,1 −λ1(1, S)) while the continuous cut
(3.13) is
θ1 ≥29.164 −11.974x11 −14.968x21 −5.987x31 −8.981x41.
Cut (3.3) is stronger than (3.13) at the current iterate point with value
23.948 instead of 8.309. Also, as the coeﬃcient a comes from (qS,1−λ1(1, S)
and λ1(1, S) is obtained when x21 becomes 1, (3.3) gives an exact bound on
the solution x11 = 1, x21 = 1, x31 = 0, x41 = 1. It provides a nontrivial but
nonbinding bound for other cases, such as x11 = 0, x21 = x31 = x41 = 1.
On the other hand, (3.13) provides a nontrivial (but nonbinding) bound
for some cases such as x11 = 0, x21 = 1, x31 = 1, x41 = 0, where (3.3) does
not.
The algorithm for the full example with six outputs was simulated by
adding cuts each time a new iterate point was found, then restarting the
branch and bound. Cuts (3.3) and (3.13) were added each time the amount
of violation exceeded 0.1. The number of iterate points is dependent on
the strategies used in the branch and bound. For this example, the largest
number of iterate points was 21. In that case, the mean number of cuts
per output was 6.833 cuts of type (3.13) and 2.5 cuts (3.3). As extreme
cases, 10 improved optimality cuts were imposed for Output 1 and only 4
for Output 2, while 4 continuous cuts were imposed for Output 3 and only
1 for Output 5.
The optimal solution is x11 = x13 = x15 = x16 = x21 = x22 = x24 =
x41 = x42 = x43 = x45 = x46 = 1; all other xijs are zero with ﬁrst-stage
cost 140 and penalty 13.26, for a total of 153.26. It strongly diﬀers from the
solution of the deterministic problem where outputs equal expected values:
x11 = x12 = x13 = x14 = x16 = x21 = x23 = x25 = 1 with ﬁrst-stage cost
97. The reason is that in the stochastic case, even if the expected output


## Page 295

276
8. Stochastic Integer Programs
exceeds demand, the probability that the demand is not met is nonzero. In
fact, the solution of the deterministic problem has a penalty of 87.59 for a
total cost of 184.59 and a VSS of 31.33.
Exercises
1. Construct the cuts from the integer L-shaped method for Example 4,
associated with the point (0, 1)T .
Compare the results by checking the bound on θ1 + θ2 by the
integer L-shaped method and the bound in Example 4 on θ by (3.1)
for the four possible points, (0, 0), (0, 1), (1, 0), (1, 1) and, for some
continuous points, (1/2, 1/2), (1.2, 0), (0, 1.2), for example.
2. Extending (3.18), we obtain
λj(s, S) = rjP(

i∈S(j)
ξij +

t∈J
ξtj < dj),
(3.19)
where J contains the indices of the s pairs ij, i̸ ∈S(j), with largest
parameter values. Show that the assumptions of Proposition 13 hold.
3. Indicate why the wait-and-see solution cannot be reasonably com-
puted in Example 5.
8.4
Other Approaches
a. Extensive forms and decomposition
Because structural properties of problems with mixed integer second-stage
programs are unknown, problems of this type have been solved in practice
by decomposing the second-stage variables into their discrete parts and
continuous parts. Assuming a mixed second stage with binary variables,
one can divide y(ω)T = (yB(ω)T , yC(ω)T ) where yB(ω) is the vector of
binary variables and yC(ω) the vector of continuous variables. Partitioning
q and W in a similar fashion, the classical two-stage program becomes
min z =cT x + EξqT
B(ω)yB(ω) + EξQ(x, yB(ω), ω)
s.t. Ax = b,
x ∈X, yB(ω) ∈YB(ω),
where
Q(x, yB(ω), ω) = min{qT
C(ω)yC(ω)
s. t. WCyC(ω) ≤h(ω) −T(ω)x −WByB(ω), yC(ω) ∈YC(ω)}.


## Page 296

8.4 Other Approaches
277
When ξ is a discrete random variable, this amounts to writing down the
extensive form for the second-stage binary variables. When the number of
realizations of ξ remains low, such a program is still solvable by the ordinary
L-shaped method. An extension of this idea to a three-stage problem in
the case of acquisition of resources can be found in Bienstock and Shapiro
[1988].
The same idea applies for multistage stochastic programs having the
block separable property deﬁned in Section 3.5, provided the discrete vari-
ables correspond to the aggregate level decisions and the continuous vari-
ables correspond to the detailed level decisions. Then the multistage pro-
gram is equivalent to a two-stage stochastic program, where the ﬁrst stage
is the extensive form of the aggregate level problems and the value func-
tion of the second stage for one realization of the random vector is the sum,
weighted by the appropriate probabilities of the detailed level recourse func-
tions for that realization and all its successors. This result is detailed in
Louveaux [1986], where examples are provided.
Example 7
As an illustration, consider the warehouse location problem similar to those
studied in Section 2.4. As usual, let
xj =

1
if plant j is open,
0
otherwise,
with ﬁxed-cost cj, and vj, the size of plant j, with unit investment cost gj,
be the ﬁrst-stage decision variables. Assume k = 1, · · · , K realizations of the
demands dk
i in the second stage. Let yk
ij be the fraction of demand dk
i served
from j, with unit revenue qij (see Section 2.4c). Now, assume the possibility
exists in the second stage to extend open plants by an extra capacity (size)
of ﬁxed value ej at cost rj. For simplicity, assume this extension can be
made immediately available (zero construction delay).
To this end, let
wk
j =
 1
if extra capacity is added to j
when the second-stage realization is k,
0
otherwise.
The two-stage stochastic program would normally read as
max −
n

j=1
cjxj −
n

j=1
gjvj +
K

k=1
pk

max
m

i=1
n

j=1
qijyk
ij −
n

j=1
rjwk
j




## Page 297

278
8. Stochastic Integer Programs
s. t.
n

j=1
yk
ij ≤1, k = 1, · · · , K, i = 1, . . . , m,
xj ∈{0, 1}, vj ≥0, j = 1, · · · , n,
m

i=1
dk
i yk
ij −ejwk
j ≤vj, k = 1, · · · , K, j = 1, · · · , n,
0 ≤yk
ij ≤xj, i = 1 · · · , m, j = 1 · · · , n,
k = 1 . . . , K,
wk
j ≤xj, j = 1, · · · , n, k = 1, · · · , K
wk
j ∈{0, 1}, j = 1, · · · , n, k = 1 . . . , K.
Using the extensive form for the binary variables, wk
j s transforms it into
max −
n

j=1
cjxj −
n

j=1
gjvj −
n

j=1
K

k=1
pkrjwk
j +
K

k=1
pk max
n

i=1
n

j=1
qijyk
ij
s. t. xj ∈{0, 1}, vj ≥0, j = 1, . . . , n,
n

j=1
yk
ij ≤1,i = 1, . . . , m, k = 1, . . . , K,
wk
j ≤xj,
m

i=1
dk
i yk
ij ≤vj + ejwk
j , j = 1, . . . , n,
k = 1, . . . , K,
wk
j ∈{0, 1},0 ≤yk
ij ≤xj, i = 1, . . . , m, j = 1, . . . , n,
k = 1, . . . , K.
Thus, at the price of expanding the ﬁrst-stage program, one obtains a
second stage that enjoys the good properties of continuous programs.
b. Asymptotic analysis
Approximation methods are commonly used in deterministic combinatorial
optimization. This is justiﬁed by the fact that a large class of problems is
known to be NP-hard. Loosely stated, for this class of problems, it is very
unlikely that an algorithm will be found that would solve the problem in a
number of operations polynomial in the problem data. This means that an
exact solution of these problems can only be found for instances of small
size. If the second stage of a stochastic problem corresponds to an NP-hard
problem, it is pointless to design an exact method that would require the
solution of the second stage for each realization of the random variable.


## Page 298

8.4 Other Approaches
279
Approximation methods are typically based on the probabilistic error of
some heuristic. We now illustrate one example, taken from Stougie [1987].
It is a hierarchical scheduling problem.
The ﬁrst stage consists of determining the number x of identical ma-
chines at a unit cost of c. In the second stage, when the machines are
available, they are used in parallel to process n jobs. The second stage
consists of determining the optimal scheduling of the jobs. It is assumed
that the processing times ξj are identically and independently distributed
random variables with ﬁnite expectation µ and ﬁnite second moment. The
second-stage objective consists of minimizing the completion time of the
job completed last, also known as the makespan.
If we denote by Q(x,ξ) the optimal makespan when x machines are avail-
able and the processing times are given by ξ (a vector of n components),
the hierarchical scheduling problem takes the usual format
min
x {cx + Q(x)|x ∈Z+}.
(4.1)
Clearly, the diﬃculty is in ﬁnding Q(x). The idea is then to base the choice
of x on an approximation of Q(x), obtained as follows. The total eﬀective
processing time is always equal to 	n
j=1 ξj, whatever schedule is chosen. If
the workload can be equally divided between the machines, the makespan
is equal to
n
j=1ξj
x
. The approximation consists of taking this (idealistic)
situation for Q(x, ξ). Because processing times are independent and iden-
tically distributed with expectation µ, this corresponds to approximating
Q(x) by nµ/x. The original problem (4.1) becomes
min
x {cx + nµ
x |x ∈Z+}.
(4.2)
The optimal solution to (4.2), denoted by xa for an approximate solution,
is easily seen to be either ⌊
 nµ
c ⌋or ⌈
 nµ
c ⌉, whichever gives the smallest
value of cx + nµ/x. There is no doubt that xa may not always coincide
with x∗, a solution to (4.1) and that nµ
x
may strongly diﬀer from Q(x).
The reader may solve Exercise 2 to see this in a simple example.
On the other hand, this approximate solution has interesting asymptotic
properties obtained by bounding Q(x) and letting n tend to inﬁnity. We
have already observed that nµ
x
is a lower bound on Q(x). To obtain an
upper bound, consider using the longest processing time ﬁrst (LPT) rule in
the second stage. This means that for a given vector of processing times, the
jobs are ordered in decreasing processing times, then at each step assigned
to the earliest available machine. If the workload is unevenly distributed,
all jobs are started at last at
n
j=1 ξj
x
. The job that is completed last has a
processing time bounded by ξmax = maxj=1,···,n ξj.
It follows that
	n
j=1 ξj
x
≤Q(x, ξ) ≤QH(x, ξ) ≤
	n
j=1 ξj
x
+ ξmax,
(4.3)


## Page 299

280
8. Stochastic Integer Programs
where QH(x, ξ) denotes the makespan obtained when using the LPT
heuristic.
Each term in (4.3) is divided by n and the limit when n tends to inﬁnity
is taken:
lim
n→∞
1
n
	n
j=1 ξj
x
≤lim
n→∞
Q(x, ξ)
n
≤lim
n→∞
QH(x, ξ)
n
≤lim
n→∞
$
1
n
	n
j=1 ξj
x
+ 1
nξmax
%
.
(4.4)
By the strong law of large numbers (see, e.g., Chung [1974]), the ﬁrst term
equals µ
x with probability one. Convergence theorems on order statistics
(see, e.g., Galambos [1978]) show that limn→∞
ξmax
n
= 0 with probability
one. Hence, limn→∞
Q(x)
n
= µ
x, with probability one. It follows that indeed
µ
x asymptotically coincides with Q(x)
n .
Now deﬁne zH = cxa + QH(xa) and z∗= cx∗+ Q(x∗). Adding cx to
each term in (4.3), then taking expectations, it follows that
cx + nµ
x ≤cx + Q(x) ≤cx + QH(x) ≤cx + nµ
x + E(ξmax),
from which it turns out that
2√nµc ≤z∗≤zH ≤2√nµc + E(ξmax),
and, ﬁnally,
zH −z∗
z∗
≤E(ξmax)
√2nµc .
(4.5)
Under the assumption that the processing times have a ﬁnite second mo-
ment, the right-hand side tends to zero as n →∞, which proves the asymp-
totic optimality of xa.
It can also be proven that zH not only tends to z∗but also to WS,
the wait-and-see value. This property has received the name of asymptotic
clairvoyancy (Lenstra, Rinnooy Kan, and Stougie [1984]). The asymptotic
analysis of heuristics of other problems can be found in Rinnooy Kan and
Stougie [1988]. A more recent study in the context of location routing is
given by Simchi-Levi [1992]. One should be aware that in several cases, the
results are truly asymptotic in the sense that they only apply for very large
values of n. Psaraftis [1984] gives one such example.
c. Final comment
Many other approaches can be tried to solve stochastic integer programs.
To cite just some, one may consider that Markov chains could be used for


## Page 300

8.4 Other Approaches
281
the analysis of multistage models with ﬁnite state space and ﬁnite action
set. Also, dynamic programming may be a relevant tool to solve small or
specially structured stochastic integer programs; see Lageweg et al. [1988]
or Takriti [1994], as an example. One may also consider using Lagrangian
decomposition techniques.
Exercises
1. In Example 7, assume a given construction delay for the warehouses
in the second stage. Is it still possible to decompose the second stage?
2. Consider the hierarchical scheduling problem with n = 3 jobs. As-
sume the processing times are i.i.d. with a Bernoulli distribution with
probability 1/2. It follows that the number of jobs requiring one unit
of time is 0, 1, 2, or 3 with probability 1/8, 3/8, 3/8, and 1/8, respec-
tively. (The other jobs require no processing time.)
(a) Construct a table for x = 0, 1, 2, or 3 and ξ corresponding to 0,
1, 2, or 3 processing times equal to 1. Obtain Q(x) and compare
with nµ/x. What is the largest relative error?
(b) Obtain x∗and xa for c = 0.7, 0.4, and 0.2, respectively. For each
case, compare the decisions and, when relevant, the relative error
in using xa instead of x∗.


## Page 301



## Page 302

Part IV
Approximation and
Sampling Methods
283


## Page 303



## Page 304

9
Evaluating and Approximating
Expectations
The evaluation of the recourse function or the probability of satisfying a
set of constraints can be quite complicated. This problem is basically one
of numerical integration in high dimensions corresponding to the random
variables. The general problem requires some form of approximation. Gen-
eral quadrature formulas do not ﬁt the structure of stochastic programs
because they typically apply to smooth functions in low dimensions that
may not have any known convexity properties. In Section 1 of this chapter,
we review some basic procedures, but in convex stochastic programs, we
often do not have diﬀerentiability of the recourse function. Other forms of
numerical integration are needed.
In the remaining sections of this chapter, we consider approximations
that give lower and upper bounds on the expected recourse function value
in two-stage problems. The intent of these procedures is to provide progres-
sively tighter bounds until some a priori tolerance has been achieved. This
chapter focuses on results for two-stage problems, while Chapter 11 dis-
cusses the multistage case. In Chapter 10, we will describe approximations
built on Monte Carlo sampling.
Section 2 in this chapter discusses the most common type of approxi-
mations built on discretizations of the probability distribution. The lower
bounds are extensions of midpoint approximations, while the upper bounds
are extensions of trapezoidal approximations. The bounds are reﬁned using
partitions of the region. Other improvements are possible using more tightly
constrained moment problem models of the approximation, as described in
Section 5.


## Page 305

286
9. Evaluating and Approximating Expectations
Section 3 discusses computational uses for bounds. The goal is to place
the bounds eﬀectively into computational methods. We present uses of
the bounds in the L-shaped method, inner linearizations, and separable
nonlinear programming procedures.
Section 4 discusses some basic bounding approaches for probabilistic con-
straints. General forms are presented brieﬂy. These methods are based on
fundamental inequalities from probability.
Section 5 presents a variety of extensions of the previous bounding ap-
proaches. It presents bounds based on approximations of the recourse func-
tion. The basic idea is to bound the objective function above and below
by functions that are simply integrated, such as separable functions. We
present the basic separable piecewise linear upper bounding function and
various methods based on this approach. We also discuss results for par-
ticular moment problem solutions. We consider bounds based on second
moment information and allowances for unbounded support regions.
Section 6 in this chapter gives basic results on convergence of approxi-
mations and bounding procedures. Most of the following results are based
on these convergence ideas.
9.1
Direct Solutions with Multiple Integration
In this section, we again consider the basic stochastic program in the form
min
x {cT x + Q(x)|Ax = b, x ≥0},
(1.1)
where Q is the expected recourse function,

Ω[Q(x, ω)]P(dω), where we use
P(dω) in place of dF(ω) to allow for general probability measure conver-
gence. We again have Q(x, ω) =
min
y(ω){q(ω)T y(ω)|Wy(ω) = h(ω) −T(ω)x, y(ω) ≥0},
(1.2)
where we assume two stages and no probabilistic constraints for now.
As we mentioned previously, we can always treat (1.1) as a standard
nonlinear program if we can evaluate Q(x) and perhaps its derivatives.
The major diﬃculty of stochastic programming is, of course, just such an
evaluation. These function evaluations all involve multiple integration with
potentially large numbers (on the order of 1000 or more) of random vari-
ables. This section considers some of the basic techniques from numerical
integration that have been attempted in the context of stochastic pro-
gramming. Remaining sections consider various approximations that lead
to computable problems.
Numerical integration
procedures are generally built around formulas
that apply only in small dimensions (see, e.g., Stroud [1971]). For some
special functions deﬁned over speciﬁc regions, eﬃcient computations are


## Page 306

9.1 Direct Solutions with Multiple Integration
287
possible, but these results do not generally carry over to the more general
setting of the integrand, Q(x, ω). This function is piecewise linear in (1.2)
as a function of ω and, hence, has many nondiﬀerentiable points. The error
analysis from standard smooth integrations (built on Peano’s rule) cannot
apply. In fact, quadrature formulas built on low-order polynomials
may
produce poor results when other simple calculations are exact (Exercise 1).
Generalizations of the basic trapezoid and midpoint approaches in nu-
merical integration obtain bounds, however, when convexity properties of
Q are exploited. Problem structure is in fact a key to obtaining computable
approximations of the multiple integral.
The simple recourse example is the best case for exploitation of problem
structure. In this case, Q(x, ω), becomes separable into functions of each
component of h(ω), the right-hand side vector in (1.2). We obtain Q(x) =
	m2
i=1 Qi(x) as in (3.1.9), which only requires integration with respect to
each hi separately. As we described in Chapter 6, this allows the use of
general nonlinear programming algorithms.
In general, the stochastic linear program recourse function can also be
written in terms of bases in W. Suppose the set of bases in W is {Bi, i ∈I}.
Let πi(ω)T = qT
BiB−1
i
. Then
Q(x, ω) = max
i {πi(ω)T (h(ω) −T(ω)x)|πi(ω)T W ≤q(ω)},
(1.3)
where, if q(ω) is constant (i.e., not random), the evaluation reduces to
ﬁnding the maximum value of the inner product over the same feasible set
for all ω. With q(ω) constant,
Q(x) =

i∈I

Ωi
{πT
i (h(ω) −T(ω)x)}P(dω),
(1.4)
where Ωi = {ω|πT
i (h(ω) −T(ω)x) ≥πT
j (h(ω) −T(ω)x), j̸ = i}. The inte-
grand in (1.4) is linear, so we have
Q(x) =

i
πT
i (¯hi −¯Tix),
(1.5)
where ¯hi =

Ωi hiP(dω) and ¯Ti =

Ωi TiP(dω). Thus, if each Ωi can be
found, then the numerical integration reduces to ﬁnding the expectations of
the random parameters over the regions Ωi, i.e., the conditional expectation
on Ωi.
The Ωi are indeed polyhedral (Exercise 2). This yields direct procedures
if these regions are simple enough to have explicit integration formulas.
Unfortunately, this is not the case for the Ωi regions that are common
in stochastic programs with recourse. In problems with probabilistic con-
straints, however, there are possibilities for creating deterministic equiva-
lents when the data are, for example, normal as in Theorem 3.18. In general,
we must use some form of approximation.


## Page 307

288
9. Evaluating and Approximating Expectations
In the following chapters, we explore several methods for approximating
the value function and its subgradient in stochastic programming. The
basic approaches are either approximations with known error bounds or
approximations based on Monte Carlo procedures that may have associated
conﬁdence intervals. In the remainder of this chapter and Chapter 11, we
will explore bounding approaches, while in Chapter 10 we also consider
methods based on sampling.
Exercises
1. The principle of Gaussian quadrature is to ﬁnd points and weights
on those points that yield the correct integral over all polynomials
of a certain degree. For example, we can solve for points, ξ1, ξ2, and
weights, p1, p2, so that we have a probability (p1 +p2 = 1) and distri-
bution that matches the mean, (p1ξ1+p2ξ2 = ¯ξ), the second moment,
(p1ξ2
1+p2ξ2
2 = ¯ξ(2)), and the third moment, (p1ξ3
1+p2ξ3
2 = ¯ξ(3)). Solve
this for a uniform distribution on [0, 1] to yield the two points, 0.211
and 0.788, each with probability 0.5.
(a) Verify that this distribution matches the expectation of any
polynomial up to degree three over [0, 1].
(b) Consider a piecewise linear function, f, with two linear pieces
and 0 ≤f(ξ) ≤1 for 0 ≤ξ ≤1. How large a relative error can
the Gaussian quadrature points give? Can you use two other
points that are better?
2. Show that each Ωi is polyhedral.
9.2
Discrete Bounding Approximations
The most common procedures in stochastic programming approximations
are to ﬁnd some relatively low cardinality discrete set of realizations that
somehow represents a good approximation of the true underlying distri-
bution or whatever is known about this distribution. The basic procedures
are extensions of Jensen’s inequality ([1906], generalization of the midpoint
approximation) and an inequality due to Edmundson [1956] and Madansky
[1959], the Edmundson-Madansky inequality, a generalization of the trape-
zoidal approximation. For convex functions in ξ, Jensen provides a lower
bound while Edmundson-Madansky provides an upper bound. Signiﬁcant
reﬁnements of these bounds appear in Huang, Ziemba, and Ben-Tal [1977],
Kall and Stoyan [1982] and Frauendorfer [1988b].
We refer to a general integrand g(x,ξ). Our goal is to bound E(g(x)) =
Eξ[g(x,ξ)] =

Ξ g(x,ξ)P(dξ). The basic ideas are to partition the sup-
port Ξ into a number of diﬀerent regions (analogous to intervals in one-


## Page 308

9.2 Discrete Bounding Approximations
289
dimensional integration) and to apply bounds in each of those regions. We
let the partition of Ξ be Sν = {Sl, l = 1, . . . , ν}. Deﬁne ξl = E[ξ|Sl] and
pl = P[ξ ∈Sl]. The basic lower bounding result is the following.
Theorem 1. Suppose that g(x, ·) is convex for all x ∈D. Then
E(g(x)) ≥
ν

l=1
plg(x, ξl).
(2.1)
Proof:
Write E(g(x)) as
E(g(x)) =
ν

l=1

Sl g(x,ξ)P(dξ)
=
ν

l=1
plE[g(x,ξ)|Sl]
≤
ν

l=1
plg(x, E[ξ|Sl]),
(2.2)
where the last inequality follows from Jensen’s inequality that the expec-
tation of a convex function of some argument is always greater than or
equal to the function evaluated at the expectation of its argument, i.e.,
E(g(ξ)) ≥g(E(ξ)) (see Exercise 1).
This result applies directly to approximating Q(x) by Qν(x)
=
	ν
l=1 plQ(x, ξl). The approximating distribution P ν is the discrete dis-
tribution with atoms, i.e., points ξl of probability pl > 0 for l = 1, . . . , ν.
By choosing Sν+1 so that each Sl ∈Sν+1 is completely contained in some
Sl′ ∈Sν, the approximations actually improve, i.e.,
E(g(x)) ≥Eν+1(g(x)) ≥Eν(g(x)).
(2.3)
Various methods can achieve convergence in distribution of the P ν to P.
An example is given in Exercise 2.
In general, the goal of reﬁning the partition from ν to ν + 1 is to achieve
as great an improvement as possible. We will describe the basic approaches;
more details appear in Birge and Wets [1986], Frauendorfer and Kall [1988],
and Birge and Wallace [1986].
Three basic decisions are to choose the cell, Sν∗∈Sν, in which to make
the partition, to choose the direction in which to split, Sν∗, and to choose
the point at which to make the split.
The reader should note that this section contains notation speciﬁc to
bounding procedures. To keep the notation manageable, we reuse some from
previous sections, including a and b for endpoints of rectangular regions and
c for points within these intervals at which to subdivide the region. For


## Page 309

290
9. Evaluating and Approximating Expectations
ease of exposition, suppose that the sets Sl are all rectangular, deﬁned by
[al
1, bl
1]×· · ·×[al
N, bl
N]. The most basic reﬁnement scheme for l = ν∗is to ﬁnd
i∗and cl
i∗so that Sl(ν) splits into Sl(ν+1) = [al
1, bl
1]×· · · [al
i∗, cl
i∗]×[al
N, bl
N]
and Sν+1(ν + 1) = [al
1, bl
1] × · · · [cl
i∗, bl
i∗] × [al
N, bl
N].
If we also have an upper bound UB(Sl) ≥E[g(x, ξ)|ξ ∈Sν
l ] for each
cell Sl, then the most likely choice for Sν∗is the cell that maximizes
pl(UB(Sl) −g(x, ξl)), which bounds the error attributable to the approx-
imation on Sl. Reducing this greatest partition error appears to oﬀer the
most hope in reducing the error on the ν + 1 approximation.
The direction choice is less clear. The general idea is to choose a di-
rection in which the function g is “most nonlinear.” The use of sub-
gradient (dual price) information for this process was discussed in Birge
and Wets [1986]. Frauendorfer and Kall [1988] improved on this and re-
ported good results by considering all 2m+1 pairs, (αj, βj), of vertices
of Sl, where αj = (γl
1, . . . , al
i, . . . , γl
N) and βj = (γl
1, . . . , bl
i, . . . , γl
N) with
γl
i = al
i or bl
i. Given x, they assume a dual vector, παj, at Q(x, αj) and
πβj at Q(x, βj). Because these represent subgradients of the recourse func-
tion Q(x, ·), we have Q(x, βj) −(Q(x, αj) + πT
αj(βj −αj)) = ǫ1
j ≥0 and
Q(x, αj) −(Q(x, βj) + πT
βj(αj −βj)) = ǫ2
j ≥0. They then choose k∗
that maximizes min{ǫ1
k, ǫ2
k} over k. They let i∗be i such that αk∗and
βk∗diﬀer in the ith coordinate. The position ci∗is then chosen so that
Q(x, βk∗) + πT
βk∗(ci∗−bi∗) = Q(x, αk∗) + πT
αk∗(ci∗−ai∗). (See Figure 1,
where we use π for the subgradient at (a1, b2) and ρ for the subgradient at
(a1, a2).) The general idea is then to choose the direction that yields the
maximum of the minimum of linearization errors in each direction.
FIGURE 1. Choosing the direction according to the maximum of the minimum
linearization errors.


## Page 310

9.2 Discrete Bounding Approximations
291
Reﬁnement schemes clearly depend on having upper bounds available.
These bounds are generally based on convexity properties of g and the
ability to obtain each ξ in terms of the extreme points. The fundamental
result is the following theorem that also appears in Birge and Wets [1986].
In the following, we use P as the measure on Ωinstead of Ξ because we
wish to obtain a diﬀerent measure derived from this. In context, this change
should not cause confusion. We also let extΞ be the set of extreme points
of coΞ and E is Borel ﬁeld of extΞ, in this case, the collections of all subsets
of extΞ.
Theorem 2. Suppose that ξ →g(x, ξ) is convex and Ξ is compact. For all
ξ ∈Ξ, let φ(ξ, ·) be a probability measure on (extΞ, E), such that

e∈extΞ
eφ(ξ, de) = ξ,
(2.4)
and ω →φ(ξ(ω), A) is measurable for all A ∈E. Then
E(g(x)) ≤

e∈extΞ
g(x, e)λ(de),
(2.5)
where λ is the probability measure on E deﬁned by
λ(A) =

Ω
φ(ξ(ω), A)P(dω).
(2.6)
Proof:
Because g is convex in ξ, for φ,
g(x, ξ) ≤

e∈extΞ
g(x, e)φ(ξ, de).
(2.7)
Substituting ξ(ω) for ξ and integrating with respect to P the result in (2.5)
is obtained.
This result states that if we can choose the appropriate φ and ﬁnd λ, we
can produce an upper bound. The key is to make the calculation of λ as
simple as possible. Of course, the cardinality of extΞ may also play a role
in the computability of the bound.
One way to reduce the cardinality of the supporting extreme points
is simply to choose the extreme point that has the highest value as an
upper bound. Let this upper bound be UBmax(x) = supe∈extΞ g(x, e) ≥

e∈extΞ g(x, e)λ(de) ≥E(g(x)) from Theorem 2, regardless of the partic-
ular λ. While UBmax may only involve a single extreme point, it is often
a poor bound (see the result from Exercise 3). Its calculation also often
involves evaluating all the extreme points to maximize the convex function
g(x, ·).


## Page 311

292
9. Evaluating and Approximating Expectations
In general, bounds built on the result in Theorem 2 construct the prob-
ability measure λ so that each extreme point ej of Ξ has some weight,
pj = λ(ej). The following bounds, described in more detail in Birge and
Wets [1986], ﬁnd these weights in various cases. The ﬁrst is general but
involves some optimization. The second involves simplicial regions, and the
third uses rectangular regions.
Because λ is constructed to be consistent with the distribution of ξ, we
must have that

Ω
ξ(ω)P(dω) =

Ω

e∈extΞ
eφ(ξ(ω), de)P(dω)
=

e∈extΞ
e

Ω
φ(ξ(ω), de)P(dω)
=

e∈extΞ
eλ(de).
(2.8)
Hence, λ ∈P = {µ|µ is a probability measure on E, and Eµ[e] = ¯ξ}. The
next upper bound, originally suggested by Madansky [1960] and extended
by Gassmann and Ziemba [1986], builds on this idea by ﬁnding an upper
bound through a linear program to maximize the objective expectation
over all probability measures in P. We write this bound as UBmean, where
UBmean(x) =
max
p1,...,pK
K

k=1
pkg(x, ek)
s. t.
K

k=1
pkek= ¯ξ,
K

k=1
pk= 1,
pk ≥0,k = 1, . . . , K.
(2.9)
As we shall see in Section 5, the probability measure that optimizes the
linear program in (2.9) is the solution of a moment problem in which only
the ﬁrst moment is known. Another interpretation of this bound is that
it represents the worst possible outcome if only the mean of the random
variable is known. Optimizing with this bound, therefore, brings some form
of risk avoidance if no other distribution information is available.
Assuming that the dimension of coΞ is N, Carath´eodory’s theorem states
that ¯ξ must be expressable as a convex combination of at most N +1 points
in extΞ. Finding these N + 1 points may, however, again involve compu-
tations for the values at all extreme points. The number of extreme point
representations may be much higher than N +1 if Ξ is, for example, rectan-
gular, but lower if, for example, Ξ is a simplex, i.e., a convex combination of
N +1 points, ξi, i = 1, . . . , N +1, such that ξi −ξ1 are linearly independent


## Page 312

9.2 Discrete Bounding Approximations
293
for i > 1. The representation of interior points is, in fact, unique. Indeed,
the pj in this case are called the barycentric coordinates of ¯ξ.
Although Ξ may not be simplicial itself, it is often possible to extend
Q(x, ·) from Ξ to some simplex Σ including Ξ. The bound obtained with
this approach is written UBΣ. In this bound, the number of points used in
the evaluation remains one more than the dimension of the aﬃne hull of
Ξ. Frauendorfer [1989, 1992] gives more details about this form of approx-
imation and various methods for its reﬁnement.
Often, Ξ is given as a rectangular region. In this case, the number of
extreme points is 2N. The number of simplices containing ¯ξ may also be
exponential in N. With relatively complete information about the corre-
lations among random variables, however, bounds can be obtained that
assign the same weight to each extreme point of Ξ (or a rectangular enclos-
ing region), regardless of the value of x. This attribute is quite beneﬁcial in
algorithms where x may change frequently as an optimal solution is sought.
The basic bounds for rectangular regions follow Edmundson and Madan-
sky, for which, the name Edmundson-Madansky (E-M) bound is used. They
begin with the trapezoidal type of approximation on an interval. Here, if
Ξ = [a, b], we can easily construct φ(ξ, ·) in Theorem 2 as φ(ξ, a) = π(ξ)
and φ(ξ, b) = 1 −π(ξ), where π(ξ) = b−ξ
b−a. Integrating over ω, we obtain
λ(a) =

Ω
φ(ξ(ω), a)P(dω)
=

Ω
b −ξ(ω)
b −a
P(dω)
= b −¯ξ
b −a.
(2.10)
We then also have λ(b) =
¯ξ−a
b−a. The bound obtained is UBEM(x) =
λ(a)g(x, a) + λ(b)g(x, b) ≥E(g(x)). Observe in Figure 2 that this bound
represents approximating the integrand g(x, ·) with the values formed as
convex combinations of extreme point values. This is the same procedure
as in trapezoidal approximation for numerical integration except that the
endpoint weights may change for nonuniform probability distributions.
The E-M bound on an interval extends easily to multiple dimensions,
where Ξ = [a1, b1] × · · · × [aN, bN] if either g(x, ·) is separable in the com-
ponents of ξ, in which case, the bound is applied in each component sepa-
rately, or the components of ξ are stochastically independent. In this case,
the bound is developed in each component i = 1 to N in order so that the
full independent ξi bound contains the product of all combinations of each
interval bound, i.e.,
UBEM−I(x) =

e∈extΞ
(ΠN
i=1
|¯ξi −ei|
bi −ai
)g(x, e),
(2.11)
where Ξ is again assumed polyhedral.


## Page 313

294
9. Evaluating and Approximating Expectations
FIGURE 2. Example of the Edmundson-Madansky bound on an interval.
Example 1
We now consider an example to illustrate the bounds. Consider the follow-
ing recourse problem with only h random:
Q(x,ξ) =
min
y+
1 + y−
1
+y+
2 + y−
2
+y3
s. t.
y+
1 −y−
1
+y3
= h1 −x1,
y+
2 −y−
2
+y3
= h2 −x2,
y+
1 , y−
1 ,
y+
2 , y−
2 ,
y3
≥0,
where hi is independently uniformly distributed on [0, 1] for i = 1, 2.
FIGURE 3. Optimal basis regions of Example 1.
The solution of this problem is illustrated in Figure 3. Here, the optimal
bases are B1 corresponding to (y+
1 , y3), B2 corresponding to (y+
2 , y3), B3


## Page 314

9.2 Discrete Bounding Approximations
295
corresponding to (y+
1 , y−
2 ), B4 corresponding to (y−
1 , y+
2 ), and B5 corre-
sponding to (y−
1 , y−
2 ). Figure 3 shows the regions in which each of these
bases is optimal.
Suppose ¯x = (0.3, 0.3)T . Then integrating Q(¯x,ξ) yields Q(¯x) = 0.466.
Our initial lower bound is LB1 = Q(¯x, ξ = ¯h = (0.5, 0.5)T = 0.2.
The upper bounds can be found using the values at the extreme points
of the support of h. These values are Q(¯x, (0, 0)T ) = 0.6, Q(¯x, (0, 1)T ) =
1.0, Q(¯x, (1, 0)T ) = 1.0, and Q(¯x, (1, 1)T ) = 0.7. For UBmax
1
(¯x), we must
take the highest of these values; hence UBmax
1
(¯x) = 1.0. For UBmean
1
,
notice that ¯h = (1/2)(1, 0)T + (1/2)(0, 1)T , so UBmean
1
(¯x) = UBmax
1
(¯x) =
1.0. For UBEM
1
, each extreme point is weighted equally, so UBEM
1
(¯x) =
(1/4)(1 + 1 + .7 + .6) = 0.825. For the simplicial approximation, let Σ =
co{(0, 0), (2, 0), (0, 2)}, which includes the support of h. In this case, the
weights on the extreme points are λ(0, 0) = 0.5 and λ(2, 0) = λ(0, 2) = 0.25.
The resulting upper bound is UBΣ(¯x) = 0.5(.6) + 0.25(2)(2) = 1.3.
To reﬁne the bounds, we consider the dual multipliers at each ex-
treme point. At (0, 0), they are (−1, −1). At (1, 0), they are (1, −1). At
(0, 1), they are (−1, 1). At (1, 1), both bases B1 and B2 are optimal,
so the multipliers are (0, 1), (1, 0), or any convex combination. The lin-
earization along the line segment from (0, 0) to (1, 0) is the minimum of
Q(¯x, (1, 0)T ) −(Q(¯x, (0, 0)T ) + (−1, −1)T (1, 0) = 1 −(0.6 −1) = 1.4 and
Q(¯x, (0, 0)T )−(Q(¯x, (1, 0)T )+(1, −1)T (−1, 0) = 0.6−(1−1) = 0.6. Hence,
the minimum error on (0, 0) to (1, 0) is 0.6. Similarly, for (0, 0) to (0, 1),
the error is 0.6. From (1, 0) to (1, 1), the minimum error is 0.3 if the (0, 1)
subgradient is used at (1, 1); however, the minimum error on (0, 1) to (1, 1)
is then min{1 −(0.7 −1), 0.7 −(1 −1)} = 0.7. Thus, the maximum of these
errors over each edge of the region is 0.7 for the edge (0, 1) to (1, 1).
To ﬁnd the value of c∗
1 to split the interval [a1 = 0, b1 = 1], we need to
ﬁnd where Q(¯x, (0, 1)T ) −c∗
1 = Q(¯x, (1, 1)T ) + (c∗
1 −1) or where 1 −c∗
1 =
0.7−1+c∗
1, i.e., where c∗
1 = 0.65. We obtain two regions, S1 = [0, 0.65]×[0, 1]
and S2 = [0.65, 1] × [0, 1], with p1 = 0.65 and p2 = 0.35.
The Jensen lower bound is now LB2 = 0.65(Q(¯x, (0.325, 0.5)T )) +
(0.35)(Q(¯x, (0.825, 0.5)T )) = 0.65(0.2) + 0.35(0.525) = 0.31375. The up-
per bounds are UBmax
2
(¯x) = 0.65(1) + 0.35(1) = 1, UBmean
2
(¯x) =
0.65(0.5)(1 + 0.65) + 0.35(0.5)(1 + 0.7) = 0.83375, and UBEM
2
(¯x) =
0.65(0.25)(1 + 0.7 + 0.65 + 0.6) + 0.35(0.25)(0.7 + 0.7 + 1 + .65) = 0.74625.
(The simplicial bound is not given because we have split the region into
rectangular parts.) Exercise 3 asks for these computations to continue until
the lower and upper bounds are within 10% of each other.
Exercises
1. For Example 1, ¯x = (0.1, 0.7)T , compute Q(¯x), the Jensen lower
bound, and the upper bounds, UBmean, UBmax, UBEM, and UBΣ.


## Page 315

296
9. Evaluating and Approximating Expectations
2. Prove Jensen’s inequality, E(g(ξ)) ≥g(E(ξ)), by taking an expecta-
tion of the points on a supporting hyperplane to g(ξ) at g(E(ξ)).
3. Follow the splitting rules for Example 1 until the Edmundson-
Madansky upper and Jensen lower bounds are within 10% of each
other. Compare UBEM to UBmax on each step.
9.3
Using Bounds in Algorithms
The bounds in Section 2 can be used in algorithms in a variety of ways.
We describe three basic procedures in this section: (1) uses of lower bounds
in the L-shaped method with stopping criteria provided by upper bounds;
(2) uses of upper bounds in generalized programming with stopping rules
given by lower bounds; and (3) uses of the dual formulation in the separable
convex hull function. The ﬁrst two approaches are described in Birge [1983]
while the last is taken from Birge and Wets [1989].
The L-shaped method as described in Chapter 5 is based on iteratively
providing a lower bound on the recourse objective, Q(x). If a lower bound,
QL(x), is used in place of Q(x), then clearly for any supports, ELx+eL, if
QL(x) ≥ELx+eL, Q(x) ≥ELx+eL. Thus, any cuts generated on a lower
bounding approximation of Q(x) remain valid throughout a procedure that
reﬁnes that lower bounding approximation. This observation leads to the
following algorithm. We suppose that QL
j (x) and QU
j (x) are approximating
lower and upper bounding approximations such that limj→∞QL
j (x) = Q(x)
and limj→∞QU
j (x) = Q(x). We suppose that P L
j is the jth lower bounding
approximation measure so that QL
j (x) =

ΩQL
j (x,ξ)P L
j (dω).
L-Shaped Method with Sequential Bounding Approximations
Step 0. Set r = s = v = k = 0.
Step 1. Set ν = ν + 1. Solve the linear program (3.1)–(3.3):
min z = cT x + θ
(3.1)
s.t. Ax = b,
Dℓx ≥dℓ,
ℓ= 1, . . . , r,
(3.2)
Eℓx + θ ≥eℓ,
ℓ= 1, . . . , s,
(3.3)
x ≥0,
θ ∈ℜ.
Let (xν, θν) be an optimal solution. If no constraint (3.3) is present, θ is
set equal to −∞and is ignored in the computation.


## Page 316

9.3 Using Bounds in Algorithms
297
Step 2. Let the support of ξ for the current lower bounding approximation
be Ξj. For any ξj = (hj, Tj, qj) ∈Ξj, solve the linear program
min w1 = eT v+ + eT v−
(3.4)
s.t. Wy + Iv+ −Iv−= hj −Tjxν,
(3.5)
y ≥0,
v+ ≥0,
v−≥0,
where eT = (1, . . . , 1), until, for some ξj, the optimal value w1 > 0.
Let σν be the associated simplex multipliers and deﬁne
Dr+1 = (σν)T Tj
(3.6)
and
dr+1 = (σν)T hj
(3.7)
to generate a feasibility cut of type (3.2). Set r = r + 1 and return to Step
1. If for all ξj w1 = 0, go to Step 3.
Step 3. Find QL
j (xν) =

ΩQL
j (xν,ξ)P L
j (dω), the jth lower bounding ap-
proximation. Suppose −(πν(ξ))T T ∈∂xQL
j (xν,ξ) (the simplex multipliers
associated with the optimal solution of the recourse problem). Deﬁne
Es+1 =

Ω
(πν(ξ))T TP L
j (dω)
(3.8)
and
es+1 =

Ω
(πν(ξ))T hP L
j (dω).
(3.9)
Let wν = es+1 −Es+1xν = QL
j (xν). If θν ≥wν, xν is optimal, relative to
the lower bound; go to Step 4. Otherwise, set s = s + 1 and return to Step
1.
Step 4. Find QU
j (xν) =

ΩQU
j (xν,ξ)P U
j (ω), the jth upper bounding ap-
proximation. If θν ≥QU
j (xν), stop; xν is optimal. Otherwise, reﬁne the
lower and upper bounding approximations from ν to ν + 1. Let ν = ν + 1.
Go to Step 3.
This form of the L-shaped method follows the same steps as the standard
L-shaped method, except that we add an extra check with the upper bound
to determine the stopping conditions. We also describe the calculation of
QL
j somewhat generally to allow for more general types of approximating
distributions and approximating recourse functions, QL
j (xν,ξ).


## Page 317

298
9. Evaluating and Approximating Expectations
Example 2
Consider Example 1 from Chapter 5, where:
Q(x, ξ) =

ξ −x
if x ≤ξ,
x −ξ
if x > ξ,
(3.10)
cT x = 0, and 0 ≤x ≤10. Instead of a discrete distribution on ξ, however,
assume that ξ is uniformly distributed on [0, 5]. For the bounding approxi-
mation, we use the Jensen lower bound and Edmundson-Madansky upper
bound for QL and QU, respectively. We use the reﬁnement procedure to
split the cell that contributes most to the diﬀerence between QL and QU.
We split this cell at the intersection of the supports from the two extreme
points of this cell (here, interval).
The sequence of iterations is as follows.
Iteration 1:
Here, x1 = 0. Find QL
1 (0) = Q(0, ¯ξ = 2.5) = 2.5. E1 = −∂xQL
1 (0, 2.5) =
−(−1) and e1 = −∂xQL
1 (0, 2.5)(h = 2.5) = −(−1)(2.5) = 2.5. Add the cut:
θ ≥2.5 −x.
(3.11)
Iteration 2:
Here, x2 = 10, θ = −7.5, but QL
1 (10) = Q(10, ¯ξ = 2.5) = 7.5. At this
point, the subgradient of QL
1 (10) is 1. E2 = −∂xQL
1 (10, 2.5) = −1, and
e1 = −∂xQL
1 (0, 2.5)(h = 2.5) = −(1)(2.5) = −2.5. Add the cut:
θ ≥−2.5 + x.
(3.12)
Iteration 3:
Here, x3 = .25, θ = 0, QL
1 (2.5) = Q(.25, ¯ξ = 2.5) = 0. Hence we meet
the condition for optimality of the ﬁrst lower bounding approximation.
Now, go to Step 4 and consider the ﬁrst upper bounding approximation
with equal weights of 0.5 on ξ = 0 and ξ = 5. In this case, QU
1 (2.5) =
0.5 ∗(Q(2.5, 0) + Q(2.5, 5)) = 2.5. Thus, we must reﬁne the approximation.
Using the subgradient of −1 at ξ = 0 and 1 at ξ = 5, split at c∗= 2.5.
The new lower bounding approximation has equal weights of 0.5 on
ξ = 1.25 and ξ = 3.75. In this case, QL
2 (2.5) = 0.5 ∗(Q(2.5, 1.25) +
Q(2.5, 3.75)) = 1.25. Now, we add the cut E2 = 0.5(−∂xQ(2.5, 1.25) −
∂xQ(2.5, 3.75)) = 0 and e1 = 0.5(−∂xQ(2.5, 1.25)(1.25) −∂xQ(2.5, 3.75)
(3.75)) = (0.5)(−1.25 + 3.75) = 1.25. Thus, we add the cut:
θ ≥1.25.
(3.13)
Iteration 4:
Here, keep x4 = x3 = 2.5 (although other optima are possible) and θ =
1.25. Again, QL
2 (2.5) = 1.25, so proceed to Step 4.


## Page 318

9.3 Using Bounds in Algorithms
299
Checking the upper bound, we ﬁnd that the upper bound places equal
weights on the endpoints of each interval, [0, 2.5] and [2.5, 5]. Thus,
QU
2 (2.5) = 0.5 ∗(Q(2.5, 2.5)) + (0.25) ∗(Q(2.5, 0) + Q(2.5, 5)) = 1.25, and
θ = QU
2 (2.5). Stop with an optimal solution.
The steps are illustrated in Figure 4. We show the true Q(x) as a solid
line, with dashed lines representing the approximations (lower and upper).
Note that the method may not have converged as quickly if we had chosen
some point other than x4 = x3 = 2.5. The upper and lower bounds meet
at this point, because we chose the division precisely at the link between
the linear pieces of the recourse function Q(x, ·).
FIGURE 4. Example of L-Shaped method with sequential approximation.
Bounds with generalized programming
In generalized linear programming, the same types of procedures can be ap-
plied. The diﬀerence is that because the generalized programming method
uses inner linearization instead of outer linearization, the bounds used
should be upper bounds. We would thus substitute ΨU
j for Ψ in (5.5.6).
The same steps are followed again with ΨU
j until optimality relative to ΨU
j
is achieved. At this point, as in Step 4 of the L-shaped method with se-
quential bounding approximations, overall convergence is tested by solving
(5.5.10) with a lower bounding ΨL
j in place of Ψ. If this value is again non-
negative, then the procedure stops. If not, reﬁnement is made until a new
upper bounding column is generated or no solution of (5.5.10) is negative
for a lower bounding approximation.
As stated in Chapter 5, generalized programming is most useful if the
recourse function, Ψ(χ), is separable in the components of χ. The separable
upper bounding procedure is a natural use for this approach. A separable
lower bound can be obtained by using a supporting hyperplane. This leads
to the Jensen lower bound.


## Page 319

300
9. Evaluating and Approximating Expectations
This generalized programming approach applies most directly when a sin-
gle basis separable approximation is used. With the convex hull operation,
we would still have the problem of evaluating this function. This diﬃculty
is, however, overcome by dualizing the problem. In this case, we suppose
that the original problem using a set D of bases is to ﬁnd x ∈ℜn1, χ ∈ℜm2
to
min
cT x
+co{ΨD, D ∈D}(χ)
s. t.
Ax
= b,
Tx
−χ
= 0,
x
≥0.
(3.14)
The main result is the following theorem. Recall the conjugate function
deﬁned in Section 2.9.
Theorem 3. A dual program to (3.14) is to ﬁnd σ ∈ℜm1, π ∈ℜm2 to
max
σT b
−sup{Ψ∗
D, D ∈D}(−π)
s. t.
σT A
+πT T
≤cT ,
(3.15)
where Ψ∗
D is the conjugate function and (3.14) and (3.15) have equal opti-
mal values.
Proof:
Let γ(χ) = co{ΨD, D ∈D}(χ). Then a dual to (3.14) (see, e.g.,
Geoﬀrion [1971], Rockafellar [1974]) is
max
π,σ { inf
x≥0,χ[cT x + γ(χ) + σT (b −Ax) + πT (χ −Tx)]},
which is equivalently
max
π,σ { inf
x≥0,χ[(cT −σT A −πT T)x + σT (b) −(−πT χ −γ(χ))]}
=
max
σT A+πT T ≤cT{σT b −γ∗(−π)}.
(3.16)
Problem (3.16) immediately gives (3.15) because (co{ΨD, D ∈D}(χ))∗(−π)
= sup{Ψ∗
D, D ∈D}(−π) (Rockafellar [1969, Theorem 16.5]).
Problem (3.15) only involves ﬁnding the supremum of convex functions,
which is again a convex function. The main diﬃculty is in ﬁnding expres-
sions for the Ψ∗
D. These are, however, relatively straightforward to evaluate
(Exercise 2). They can be used in a variety of optimization procedures, but
the objective is nondiﬀerentiable. In Birge and Wets [1989], this diﬃculty
is overcome by making each Ψ∗
D a lower bound on some parameter that
replaces sup{Ψ∗
D, D ∈D} in the objective.
The main reﬁnement choice in the separable optimization procedure us-
ing (3.15) is to determine how to update the set D. Choices of bases that
are optimal for ¯ξ and then ¯ξ±δeiσi for increasing values of δ appear to give
a rich set D as in Birge and Wets [1989]. Any sense of optimal reﬁnements
or basis choice is, however, an open question.


## Page 320

9.4 Bounds in Chance-Constrained Problems
301
Exercises
1. Consider Example 2 where we redeﬁne Q as
Q(x,ξ) =

2(ξ −x)
if x ≤ξ,
x −ξ
if x > ξ,
with ξ uniformly distributed on [0, 5], cT x = 0, and 0 ≤x ≤10.
Follow the L-shaped sequential approximation method until achieving
a solution with two signiﬁcant digits of accuracy.
2. Find Ψ∗
D(−π) and ∂Ψ∗
D(−π). A useful set may be γDi(p)
=
{y|PDi(y)−≤p ≤PDi(y)}.
3. Use the dualization procedure to solve a stochastic linear program
with cT x = x, 0 ≤x ≤1, and the recourse function in Example 1.
9.4
Bounds in Chance-Constrained Problems
Our procedures have so far concentrated on methods for recourse problems
as we have throughout this book. In many cases, of course, probabilistic
constraints may also be in the formulation or may be the critical part of
the model. The basic results are aimed at ﬁnding some inequalities ˜Ax ≥˜h
(or, perhaps, nonlinear inequalities) that imply that P{Ax ≥h} ≤α. In
Section 3.2, we found some deterministic equivalents for speciﬁc forms of
the distribution, but these are not always available. In these cases, it is
useful to have upper and lower bounds on P{Ax ≥h} for any x such that
˜Ax ≤˜h.
The bounds in this case are generally of two types: bounds for a single
inequality such as P{Aix ≥hi} and bounds for the set of inequalities in
terms of results in lower dimensions. In algorithms, (see Pr´ekopa [1988]),
it is often common to place the probabilistic constraint into the objective
and to use a Lagrangian relaxation or parametric solution procedure.
For bounds with a single constraint, the basic results are extensions of
Chebyshev’s inequality. We refer to Hoeﬀding [1963] and Pint´er [1989] for
many of these results. The basic Chebyshev inequality is (see, e.g., Feller
[1971, section V.7]) that if ξ has a ﬁnite second moment, then
P{|ξ| ≥a} ≤E[ξ2]
a2
,
(4.1)
and for σ2, the variance of ξ,
P{|ξ −¯ξ| ≥a} ≤σ2
a2 .
(4.2)


## Page 321

302
9. Evaluating and Approximating Expectations
Another useful inequality is the one-sided inequality that
P{ξ −¯ξ ≥a} ≤
σ2
σ2 + a2 .
(4.3)
To apply (4.2) and (4.3) in the context of stochastic programming, we
suppose that we can represent Aix ≥hi as ξ0 + ξT x ≥r0 + rT x, where
Aij = ξj −tj and hi = −ξ0 + r0, to distinguish random elements from
those that are not random and to allow us to set ¯ξj = 0 for j = 0, . . . , n. If
ξ has covariance matrix, C, then the variance of ξ0 + ξT x is ˆxT Cˆx, where
ˆx =

1
x

. In this case, substituting ˆxT Cˆx for σ2 and r0 + rT x = ˆrT ˆx for
r in (4.3) yields:
P{Aix ≥hi} ≤
ˆxT Cˆx
ˆxT Cˆx + (ˆrT ˆx)2 ,
(4.4)
which implies that if x satisﬁes
ˆxT Cˆx(1 −α) ≤α(ˆrT ˆx)2,
(4.5)
then
P{Aix ≥hi} ≤α.
(4.6)
Alternatively, if
P{Aix ≥hi} ≥α,
(4.7)
then
ˆxT Cˆx(1 −α) ≥α(ˆrT ˆx)2.
(4.8)
Thus, adding constraint (4.8) in place of (4.7) in a stochastic program
allows a large feasible region and in a minimization problem, would produce
a lower bound on the objective value with constraint (4.7). For an upper
bound, we could note that P{Aix ≥hi} ≥α is equivalent to P{Aix ≤
hi} ≤1 −α or P{hi −Aix ≥0} ≤1 −α. We just replace the previous ξ
and t with −ξ and −t and replace α with (1 −α) to obtain that if
ˆxT Cˆx(α) ≤(1 −α)(ˆrT ˆx)2,
(4.9)
then (4.7). Hence, replacing (4.7) with (4.9) yields a smaller region and an
upper bound in a minimization problem.
Other information, such as ranges, can also be used to obtain sharper
bounds. A particularly useful inequality (see, again, Feller [1971]) is that,
for any function u(ξ) such that u(ξ) > ǫ > 0, for all ξ ≥t,
P{ξ ≥t} ≤1
ǫ E[u(ξ)].
(4.10)
In fact, using, u(ξ) = (ξ + σ2
a )2 yields (4.3) from (4.10). A diﬃculty in
using bounds based on (4.3) is that the constraint in (4.8) or (4.9) may be


## Page 322

9.4 Bounds in Chance-Constrained Problems
303
quite diﬃcult to include in an optimization problem. Various linearizations
around certain values of x of this constraint can be used in place of (4.8) or
(4.9). Other approaches, as in Pint´er [1989], are based on the expectations
of exponential functions of ξi that can in turn be bounded using the Jensen
inequality.
Given these approaches or deterministic equivalents for a single inequal-
ity as in Section 3.2, we wish to ﬁnd approximations for multiple inequali-
ties, P{Ax ≤h}. With relatively few inequalities and special distributions,
such as the multivariate gamma described in Sz´antai [1986], deterministic
equivalents can again be found. The general cases are, however, most of-
ten treated with approximations based on Boole-Bonferroni inequalities. A
thorough description is found in Pr´ekopa [1988].
We suppose that A ∈ℜm×n and that h ∈ℜm. The Boole-Bonferroni
inequality bounds are based on evaluating P{Aix ≤hi} and P{Aix ≤
hi, Ajx ≤hj} for each i and j and using these values to bound the complete
expression P{Ax ≤h}. To distinguish among the rows of A, we let Aij =
ξi
j −ti
j and hi = −ξi
0 + ti
0. A main result is then the following.
Theorem 4. Given these assumptions,
P{Ax ≤h} = 1 −(a −2b
m) + λ[(c −1)a
c + 1
−2(−m + c(c + 1))b
m(c(c + 1))
],
(4.11)
a =

1≤i≤m+1
P(ηi > si(x)),
b =

1≤i<j≤m+1
P(ηi > si(x),ηi > sj(x)),
c = ⌊2b
a ⌋,
0 ≤λ ≤1,
ηi = (ξi)T ˆx,
si(x) = (ri)T ˆx.
Proof:
Denote the event ηi ≤si(x) by Ai. Then
P(Ax ≤h) = P(A1 · · · Am) = 1 −P( ˆA1 + ... + ˆAm),
(4.12)
where ˆS for a set S indicates the complement of A, i.e., the set of points
not in A.
By the inequality of Dawson and Sankoﬀ[1967] ((7) of Pr´ekopa [1988]),
P( ˆA1 + ... + ˆAm) ≥
2
c + 1a −
2
c(c + 1)b,
(4.13)


## Page 323

304
9. Evaluating and Approximating Expectations
where
a =

1≤i≤m
P( ˆAi) =

1≤i≤m
P(ηi > si(x)),
b =

1≤i<j≤m
P( ˆAi · ˆAj)
=

1≤i<j≤m
P(ηi > si(x),ηj > sj(x)),
c = ⌊2b
a ⌋.
Similarly, by the inequality of Sathe, Pradhan, and Shah [1980] ((8) of
Pr´ekopa [1988]),
P( ˆA1 + ... + ˆAm) ≤a −2
mb.
(4.14)
Combining (4.12)–(4.14), we obtain (4.11).
We may use (4.11) to approximate P{Ax ≤h} by assigning a in [0, 1],
e.g., 0.5. With the marginal distribution of ηi and the joint distribution of
ηi and ηj, we can again use bounds on the variances of these random vari-
ables to calculate bounds from (4.11). Of course, with normally distributed
random variables, we may again obtain the ηi to be normally distributed
or may obtain such limiting distributions (see, e.g., Salinetti [1983]). In
this case, besides the exact results in Section 3.2, we should mention the
specializations of Gassmann [1988] and De´ak [1980]. They also combine
these inequalities with Monte Carlo simulation schemes (see, e.g., Rubin-
stein [1981]). In general, the inequalities from (4.11) can reduce the variance
of Monte Carlo schemes. For this approach and the bivariate gamma, we
again refer to Sz´antai [1986].
Before closing this section, we should also mention that approximating
probabilities is also quite useful in recourse problems because the gradient
of the linear recourse function with ﬁxed q and T is simply a weighted
probability of given bases’ optimality. From Theorem 3.11, if x is in the
interior of K2, then
∂Q(x) = Eξ[−π(ξ)T T]=
J

j=1
−πjTP{(πj)T (h −Tx)
≥πT (h −Tx), ∀πT W ≤q},
(4.15)
where {π1, . . . , πJ} is the set of extreme values of {π|πT W ≤q}. Because
(πj)T = (W j)−1qT is optimal, if and only if (W j)−1(h−Tx) ≥0, the result
reduces to ﬁnding the probability that (W j)−1(h −Tx) ≥0. This observa-
tion can be useful in guiding algorithms based on subgradient information.
This idea is explored in Birge and Qi [1995].


## Page 324

9.5 Generalized Bounds
305
Other model forms also lead to bounds of this type that can in some
cases be stronger because of the structure of A. A particular case is when
A represents a network. In this case, bounds on project network completion
times can be found in Maddox and Birge [1991]. These bounds, as well as
those given earlier, can be derived from solutions of a generalized moment
problem. That is one of the main topics of the generalizations in the next
section.
Exercises
1. Derive (4.10).
2. Deﬁne u in (4.10) as u(ξ) = cσ2 −(ξ −u+t
2 )2, where it is known,
however, that ξ ≤U = βa, a.s., for some ﬁnite β. For given β and a,
can you ﬁnd c such that (4.10) gives a better bound with this u than
with the u used to obtain (3.3)?
3. Suppose ξi, i = 1, 2, 3, are jointly multivariate normally distributed
with zero means and variance-covariance matrix
C =


1
.25
−.25
.25
1
−.5
−.25
−.5
1

.
Use Theorem 4 to bound P{ξ ≤1, i = 1, 2, 3}. What is the exact
result? (Hint:Try a transformation to independent normal random
variables.)
9.5
Generalized Bounds
a. Extensions of basic bounds
When the components of ξ are correlated, a bound is still tractable (see
Frauendorfer [1988b]), although somewhat more diﬃcult to evaluate. In
this subsection, we give the necessary generalizations. The notation here is
particularly cumbersome, although the results are straightforward.
For the general results, we deﬁne:
η(e, ξi) =

(ξi −ai)
if ei = ai,
(bi −ξi)
if ei = bi.
(5.1)
Then we have (Exercise 1) that
φ(ξ, e) = ΠN
i=1
η(e, ξi)
(bi −ai).
(5.2)


## Page 325

306
9. Evaluating and Approximating Expectations
The λ(e) values can be found by integrating over ω. This may involve all
products of the ξi components. Deﬁning M = {M|M ⊂{1, . . . , N}}, and
ρM = E[Πi∈Mξi] −Πi∈M ¯ξi, we obtain the general E-M extension:
UBEM−D(x)= UBEM−I(x) +

e∈extΞ
1
ΠN
i=1(bi −ai)
{

M∈M
[Πi̸∈M(−1)
ei−ai
bi−ai (ai(ei −ai
bi −ai
) + bi( bi −ei
bi −ai
))
×Πi∈M(−1)1−ei−ai
bi−ai ]ρM}g(x, e).
(5.3)
Notice, in (5.3), that if the components of ξ are independent, then ρM = 0
for all M and UBEM−D(x) = UBEM−I(x), as expected.
Each of these upper bounds is a solution of a corresponding moment
problem in which the highest expected function value is found over all
probability distributions with the given moment information. The upper
bounds derived so far all used ﬁrst moment information plus some infor-
mation about correlations. In Subsection c, we will explore the possibilities
for higher moments and methods for constructing bounds with this addi-
tional information.
For diﬀerent support regions, Ξ, we can combine the bounds or use en-
closing regions as we mentioned in terms of simplicial approximation. To
apply the bounds in a convergent method, the partitioning scheme in The-
orem 1 is again applied. Instead of applying the bounds on Ξ in its entirety,
they are applied on each Sl. The dimension of these cells may, however,
make computations quite cumbersome, especially if the Sl have exponential
numbers of extreme points. For this reason, algorithms primarily concen-
trate on a lower bounding approximation for most computations and only
use the upper bound to check optimality and stopping conditions.
So far, we have only considered convex g(x, ·). In the recourse problem,
Q(x, ξ(ω)) is generally convex in h(ω) and T(ω) but concave in q(ω). In
this general case, the Jensen-type bounds provide an upper bound on Q
in terms of q while the extreme point bounds provide lower bounds in q.
We can combine these results with the convex function results to obtain
overall bounds by, for example, determining UB(x) =

ΩUB(x, q)P(dω)
where UB(x, q) = UBh,T(Q(x,ξ)), where the last upper bound is taken
with respect to the h and T with q ﬁxed. The diﬃculty of evaluating

ΩUB(x, q)P(dω) may determine the success of this eﬀort. In the case of
q independent of h and T, it is simple. In other cases, linear upper bounding
hulls may be constructed to allow relatively straightforward computation
(Frauendorfer [1988a]) or extensions of the approach in UBmean may be
used (Edirisinghe [1991]).
For the procedure in Frauendorfer [1988a], assume that Ξ is compact
and rectangular with q ∈Ξ1 = [c1, d1] × · · · × [cn2, dn2] and (h, T)T ∈
Ξ2 = [a1, b1] × · · · × [aN−n2, bN−n2]. For convenience here, we consider T


## Page 326

9.5 Generalized Bounds
307
as a single vector of all components in order, T1·, . . . , Tm2·. We also delete
transposes on vectors when they are used as function arguments.
Let the extreme points of the support of q be el, 1, . . . , L, and the extreme
points of the support of (h, T) be ej, k = 1, . . . , K. In this case, because
Q(x, ·) is convex in (h, T), for any el, we can take any support π(el) such
that π(el)T W ≤el and obtain a lower bound on Q(x, (el, h, T)) as
π(el)T (h −Tx) ≤Q(x, (el, h, T))).
(5.4)
We can also let φ(q, el) = Πn2
i=1
η(el,qi)
(di−ci), where η is as deﬁned earlier with
c replacing a and d replacing b. Because for any (h, T), Q(x, (q, h, T)) is
concave in q, we have that
Q(x, (q, h, T)) ≥
L

l=1
φ(q, el)Q(x, (el, h, T)) ≥
L

l=1
φ(q, el)π(el)T (h −Tx),
(5.5)
where we note that π(el) need not depend on (h, T). A bound is obtained
by integrating over (h(ω), T(ω)) in (5.5), so that
Q(x) ≥
L

l=1

Ω
Πn2
i=1
η(el, qi)
(di −ci)π(el)T (h −Tx)P(dω).
(5.6)
Note the terms in (5.6) just involve products of the components of q and
each component of h or Tx singly. Following Frauendorfer [1988a], we let
L = {Λ|Λ ⊂{1, . . . , n2}} and deﬁne
cΛ(el) =
1
Πn2
i=1(di −ci)[Πi̸∈Λ(−1)
el,i−ci
di−ci (ci
el,i −ci
di −ci
+ di
di −el,i
di −ci
)]
× [Πi∈Λ(−1)1−
el,i−ci
di−ci ],
(5.7)
mλ =

Ω
Πi∈ΛqiP(dω),
(5.8)
and
mj,λ =

Ω
hjΠi∈ΛqiP(dω),
(5.9)
where j = 1, . . . , m2. We may also include stochastic components of T in
place of hj in (5.9). For simplicity, however, we only consider h stochastic
next.
Assuming that 	
Λ∈L cΛ(el)mΛ > 0 for all l = 1, . . . , L, the integration
in (5.6) yields a lower bound. With the deﬁnitions in (5.7)–(5-9), we can


## Page 327

308
9. Evaluating and Approximating Expectations
deﬁne a general dependent lower bound, LBq,h(x), as
LBq,h(x) =
L

l=1
(

Λ∈L
cΛ(el)mλ)[
m2

j=1
π(el, j)(
	
Λ∈L cΛ(el)mj,λ
	
Λ∈L cΛ(el)mλ
−(Tx)j)]
=
L

l=1
(

Λ∈L
cΛ(el)mλ)Q(x, el,
	
Λ∈L cΛ(el)mj,λ
	
Λ∈L cΛ(el)mλ
)
≤Q(x),
(5.10)
where π(el) is chosen so that
Q(x, el,
	
Λ∈L cΛ(el)mj,λ
	
Λ∈L cΛ(el)mλ
) = [
m2

j=1
π(el, j)(
	
Λ∈L cΛ(el)mj,λ
	
Λ∈L cΛ(el)mλ
−(Tx)j)].
When 	
Λ∈L cΛ(el)mλ = 0, we also have 	
Λ∈L cΛ(el)mj,λ = 0 (Exercise
5) making the lth component of the bound zero in that case. A completely
analogous upper bound is also available then.
Dependency can be removed if the random variables, h, can be written
as linear transformations of independent random variables. Here, the in-
dependent case needs only to be slightly altered. A discussion appears in
Birge and Wallace [1986].
The diﬃculty with the upper bounds for convex g(x, ·) and the other
bounds with concave components is that they minimally require function
evaluations at the support of the random vectors. They also may require
joint moment information that is not available. These factors make bounds
based on extreme points unattractive for practical computation with more
than a small number of random elements. As we saw earlier, in the case
of simplicial support, we can reduce the eﬀort to only being linear in the
dimension of the support, but the bounds generally become imprecise.
Another problem with the upper bounds described so far in this chapter
is that they require bounded support. In Subsection c, we will describe gen-
eralizations to eliminate this requirement for Edmundson-Madansky types
of bounds. In the next subsection, we consider other bounds that do not
have this limitation. They are based on exploiting separable structure in
the problem. The goal in this case is to avoid exponential growth in eﬀort
as the number of random variables increases. The bounds of Section 3 are
still quite useful for low dimensions.
b. Bounds based on separable functions
As we observed earlier, simple recourse problems are especially attractive
because they only require simple integrals to evaluate. The basic idea in
this section is to construct approximating functions that are separable and,


## Page 328

9.5 Generalized Bounds
309
therefore, easy to integrate. This idea can be extended to separate low-
dimension approximations, which can then be combined with the bounds
in Section 3.
In the simple recourse problem (Section 3.1d), we noticed that Ψ(χ) can
be written as
Ψ(χ) =
m2

i=1
Ψi(χi),
(5.11)
in the case when only h is random in the recourse problem. We again
consider this case and build approximations on it. These results appear in
Birge and Wets [1986, 1989], Birge and Wallace [1988], and, for network
problems, Wallace [1987].
The basic simple recourse approximation is to consider an optimal re-
sponse to changes in each component of h separately and to combine those
responses into an approximating function. For the ith component of h, this
response is the pair of optimal solutions, yi,+, yi,−, to:
min qT y
s. t. Wy =±ei,
(5.12)
y≥0,
where ei is the ith coordinate direction, yi,+ corresponds to a right-hand
side of ei, and yi,−corresponds to a right-hand side of −ei. Thus, for any
value hi of hi, the approximating response of yi,+(hi −χi) if hi ≥χi and
yi,−(χi −hi) if hi < χi. We have thus used the positive homogeneity of
ψ(χ, h + χ).
Using yi,+ and yi,−, we then obtain the approximate simple recourse
functions:
ψI(i)(χi, hi) =

qT yi,+(hi −χi)
if hi ≥χi,
qT yi,−(χi −hi)
if hi < χi,
(5.13)
which are integrated to form
ΨI(i)(χi) =

hi
ψI(i)(χi, hi)Pi(dhi),
(5.14)
where we let Pi be the marginal probability measure of hi. Note that the
calculation in (5.14) only requires the conditional expectation of hi on each
interval (−∞, χi] and (χi, ∞) and the expectation of these intervals.
The ΨI(i) functions combine to form
ΨI(χ) =
m2

i=1
ΨI(i)(χi),
(5.15)
which is a simple recourse function. The next theorem states the main
result of this section.


## Page 329

310
9. Evaluating and Approximating Expectations
Theorem 5. The function ΨI(χ) constructed in (5.13)–(5.15) represents
an upper bound on the recourse function Ψ(χ), i.e.,
Ψ(χ) ≤ΨI(χ),
(5.16)
for all χ.
Proof: Consider the solution yI = 	m2
i=1[yi,+(hi−χi)++yi,−(−)(hi−χi)−].
Note that yI is feasible in the recourse problem for h. Thus
Ψ(χ) =

Ω
ψ(χ, h)P(dω)
≤

Ω
qT yIP(dω) =
m2

i=1
ΨI(χi) = ΨI(χ).
(5.17)
The result in Theorem 5 is straightforward but useful. In particular, we
can construct other approximations that use diﬀerent representations of
a solution to the recourse problem with right-hand side h −χ. A partic-
ularly useful type of this approximation is to consider a set of vectors,
V = {v1, . . . , vν}, such that any vector in ℜm2 can be written as a non-
negative linear combination of the vectors in V . This deﬁnes V as a positive
linear basis of ℜm2. For such V , we suppose that yV,i solves:
min qT y
s. t. Wy= vi,
(5.18)
y≥0.
We can then represent any h −χ in terms of non-negative combinations
of the vi or W times the corresponding non-negative combination of the
yV,i. Thus, we construct a feasible solution that responds separately to the
components of V .
If V is a simplex, the construction of h −χ from V corresponds to a
barycentric coordinate system. Bounds based on this idea are explored in
Dul´a [1991]. Another option is to let V be the set of positive and negative
components of a basis D = [d1| · · · |dm2] of ℜm2, or, V = {d1, . . . , dm2, −d1,
. . . , −dm2}. This yields solutions, yD,i,+, to (5.18) when vi = di and yD,i,−
when vi = −di. To use these in approximating a recourse problem solution
with right-hand side, h −χ, we want the values of ζ such that Dζ = h −χ
or ζ = D−1(h −χ). Then the weight on di is ζi if ζi ≥0 and the weight on
−di is −ζi if ζi < 0. We thus construct simple recourse-type functions,
ψDi(ζi) =

qT yD,i,+(ζi)
if ζi ≥0,
qT yD,i,−(−ζi)
if ζi < 0,
(5.19)
which are integrated to form
ΨDi(χ) =

ζ i
ψDi(ζi)PDi(dζi),
(5.20)


## Page 330

9.5 Generalized Bounds
311
where PDi is the marginal probability measure of ζi. Again, these are added
to create a new upper bound,
ΨD(χ) =
m2

i=1
ΨDi(χ) ≥Ψ(χ).
(5.21)
Now, computation of ΨD relies on the ability to ﬁnd the distribution of
ζi. In special cases, such as when h is normally distributed, then ζ, the
aﬃne transformation of a normal vector is also normally distributed so that
the marginal ζi can be easily calculated. In other cases, full distributional
information of h may not be known. In this case, ﬁrst or higher moments of
ζi can be calculated and bounds such as those in Section 2 or those based
on the moment problem in Subsection c, can be used. In either case, the
calculation of ΨD reduces to evaluating or bounding the expectation of a
function of a single random variable.
Of course, if a set of bases, D, is available, then the best bound within
this set can be used. In fact, the convex hull of all approximations, ΨD, for
D ∈D, is also a bound. We write this function as:
co{ΨD, D ∈D}(χ)= inf{
K

i=1
λiΨDi(χi)|
K

i=1
λiχi = χ,
j

i=1
λi = 1, λi ≥0, i = 1, . . . , K},
(5.22)
where D = {D1, . . . , Dj}. This deﬁnition yields the following.
Theorem 6. For any set D of linear bases of ℜm2,
Ψ(χ) ≤co{ΨD, D ∈D}(χ).
(5.23)
Proof:
From earlier,
Ψ(χi) ≤ΨDi(χi)
(5.24)
for each i = 1, . . . , K and choice of χi. By convexity of Ψ, Ψ(χ) ≤
	j
i=1 λiΨ(χi) where
K

i=1
λiχi = χ,
j

i=1
λi = 1, λi ≥0, i = 1, . . . , K.
(5.25)
Combining (5.24) and (5.25) with the deﬁnition in (5.22) yields (5.23).
From Theorem 6, we continue to add bases Di to D to improve the bound
on Ψ(χ). Even if D(W), the set of all bases in W are included; however,
the bound is not exact. In this case, co{ψD(D−1(h −χ))|D ∈D(W)} =


## Page 331

312
9. Evaluating and Approximating Expectations
ψ(χ, h) because ψ(χ, h) = qT y∗= qT (D∗)−1(h −χ) for some D∗∈D(W).
However,
Ψ(χ) =

co{ψD(D−1(h −χ))|D ∈D(W)}P(dh)
≤co{

ψD(D−1(h −χ))P(dh)|D ∈D(W)}
= co{ΨD, D ∈D}(χ),
(5.26)
where the inequality is generally strict except for unusual cases (such as Ψ
linear in χ).
As we shall see in an example later, the main intention of this approxi-
mation is to provide a means to ﬁnd the optimal x value. Thus, the most
important consideration is whether the subgradients of co{ΨD, D ∈D}(χ)
are approximately the same as those for Ψ(χ). In this case, the approxima-
tion appears to perform quite well (see Birge and Wets [1989]).
Example 1 (continued)
Let us consider Example 1 again, as in Section 2. The optimal bases
and their regions of optimality were given there. In this case, we let
D1 = B1, D2 = B2, and D3 = B3. Note that this last approxima-
tion is derived for B4 and B5 because they correspond to the same
positive linear basis as [B3, −B3]. At χ = (0.3, 0.3)T , we can evaluate
each of the bounds, ΨDi. For i = 1, we have (D1)−1 =

1
−1
0
1

,
so that ζ1
1 = h1 −h2 and ζ1
2 = h2 −χ2 = h2 −0.3. In this case,
yD1,1,+ = (y+
1 , y−
1 , y+
2 , y−
2 , y3)T = (1, 0, 0, 0, 0)T , yD1,1,−= (0, 1, 0, 0, 0)T ,
yD1,2,+ = (0, 0, 0, 0, 1)T , and yD1,2,−= (0, 1, 0, 1, 0)T . Integrating out each
ζ1
i , we obtain ΨD1(0.3, 0.3) = 0.668. Symmetrically, ΨD2(0.3, 0.3) = 0.668.
For ΨD3(0.3, 0.3), we note that each component is simply the probability
that hi ≤0.3 times the conditional expectation of hi −0.3 given hi ≤0.3
plus the probability that hi > 0.3 times the conditional expectation of
hi −0.3 given hi > 0.3. Thus, ΨD3(0.3, 0.3) = 2[(0.3)(0.15)+(0.7)(0.35)] =
0.580.
Comparing the best of these bounds with those in the previous chapters
leads to a more accurate approximation. We should note, however, that
this approach requires more distributional information.
Taking convex hulls can produce even better bounds. The convex hull
operation is, however, a nonconvex optimization problem. The dual gives
some computational advantage. To give an idea of the advantage of the con-
vex hull, however, consider Figure 5, where the graphs of ΨDi are displayed
with that of Ψ as functions of χ1 for χ2 = 0.1. Note how the convex hull
of the graphs of the approximations appears to have similar subgradients


## Page 332

9.5 Generalized Bounds
313
to that of Ψ. This observation appears to hold quite generally, as indicated
by the computational tests in Birge and Wets [1989].
FIGURE 5. Graphs of Ψ (solid line) and the approximations, ΨDi (dashed lines).
The separable bounds in ΨDi can also be enhanced by, for example, in-
cluding ﬁxed values (due to known entries in h) into the right-hand sides
of (5.18). Other possibilities are to combine the component approximations
on an interval instead of assuming that they may apply for all positive mul-
tiples of the vi. In this case, the solution for some interval of vi multiples
can serve as a constraint for determining solutions for the next vi+1. This
procedure is carried out in Birge and Wallace [1988]. It appears especially
useful for problems with bounded random variables and networks (Wallace
[1987]).
To improve on these bounds and obtain some form of convergence re-
quires relaxation of complete separability. For example, pairs of random
variables can be considered together. In this way, more precise bounds can
be found. Determination of these terms is, however, problem-speciﬁc. In
general, the structure of the problem must be used to obtain the most
eﬃcient improvements on the basic separable approximation bounds.
So far, we have presented bounds for the recourse function with a ﬁxed
χ value. In the next subsection, we consider how to combine these approxi-
mations into solution algorithms where x varies from iteration to iteration.
In the case of the separable bounds, this implementation results from a
dualization that turns the diﬃcult convex hull operation into a simpler
supremum operation.


## Page 333

314
9. Evaluating and Approximating Expectations
c. Extensions with general moments
Many other bounds are possible in addition to those presented so far. A
general form for many of these bounds is found through the solution of an
abstract linear program, called a generalized moment problem. This prob-
lem provides the lowest or highest expected probabilities or objective values
that are possible given certain distribution information that can be written
as generalized moments. In this subsection, we present this basic frame-
work, some results using second moments, and generalizations to nonlinear
functions. Concepts from measure theory appear again in this development.
To obtain bounds that hold for all distributions with certain properties,
we can ﬁnd p ∈P a set of probability measures on (Ξ, BN) to extremize a
moment problem. We let BN be the Borel ﬁeld of ℜN where ℜN ⊃Ξ. We
use probability measures deﬁned directly on BN to simplify the following
discussion. We wish to ﬁnd
P ∈P a set of probability measures on (Ξ, BN) s. t.

Ξ
vi(ξ)P(dξ) ≤αi, i = 1, . . . , s,

Ξ
vi(ξ)P(dξ) = βi, i = s + 1, . . . , M,
(5.27)
to maximize

Ξ
g(ξ)P(dξ),
where M is ﬁnite and the vi are bounded, continuous functions. A solution
of (5.27) obtains an upper bound on the expectation of g with respect to
any probability measure satisfying the conditions given earlier. We could
equally well have posed this to ﬁnd a lower bound.
Problem (5.27) is a generalized moment problem (Krein and Nudel’man
[1977]). When the vi are powers of ξ, the constraints restrict the moments
of ξ with respect to P. In this context, (5.27) determines an upper bound
when only limited moment information on a distribution is available.
Problem (5.27) can also be interpreted as an abstract linear program, i.e.,
a linear program deﬁned over an abstract space, because the objective and
constraints are linear functions of the probability measure. The solution is
then an extreme point in the inﬁnite-dimensional space of probability mea-
sures. The following theorem, proven in Karr [1983, Theorem 2.1], gives
the explicit solution properties. We state it without proof because our main
interests here are in the results and not the particular form of these solu-
tions. Readers with statistics backgrounds may compare the result with the


## Page 334

9.5 Generalized Bounds
315
Neyman-Pearson lemma and the proof of the optimality conditions as in
Dantzig and Wald [1951]. For details on the weak∗topology that appears
in the theorem, we refer the reader to Royden [1968].
Theorem 7. Suppose Ξ is compact. Then the set of feasible measures in
(5.27), P, is convex and compact (with respect to the weak∗topology), and P
is the closure of the convex hull of the extreme points of P. If g is continuous
relative to Ξ, then an optimum (maximum or minimum) of

Ξ g(x,ξ)P(dξ)
is attained at an extreme point of P. The extremal measures of P are those
measures that have ﬁnite support, {ξ1, . . . , ξL}, with L ≤M + 1, such that
the vectors






v1(ξ1)
v2(ξ1)
...
vM(ξ1)
1






, · · · ,






v1(ξL)
v2(ξL)
...
vM(ξL)
1






(5.28)
are linearly independent.
Kemperman [1968] showed that the supremum is attained under more
general continuity assumptions and provides conditions for P to be
nonempty. Dupaˇcov´a (formerly ˇZ´aˇckov´a) [1976, 1977, 1966] pioneered the
use of the moment problem as a bounding procedure for stochastic pro-
grams in her work on a minimax approach to stochastic programming.
She showed that (5.27) attains the Edmundson-Madansky bound (and the
Jensen bound if the objective is minimized) when the only constraint in
(5.27) is v1 = ξ, i.e., the constraints ﬁx the ﬁrst moment of the proba-
bility measure. She also provided some properties of the solution with an
additional second moment constraint (v2(x) = ξ2) for a speciﬁc objective
function g. Frauendorfer’s [1988b] results can be viewed as solutions of
(5.27) when the constraints satisfy all of the joint moment conditions.
To solve (5.27) generally, we consider a generalized linear programming
procedure.
Generalized Linear Programming Procedure for the Generalized
Moment Problem (GLP)
Step 0. Initialization. Identify a set of L ≤M + 1 linearly independent
vectors as in (5.28) that satisfy the constraints in (5.27). (Note that a phase
one–objective (Dantzig [1963]) may be used if such a starting solution is
not immediately available. For N = 1, the Gaussian quadrature points may
be used.) Let r = L, ν = 1; go to 1.


## Page 335

316
9. Evaluating and Approximating Expectations
Step 1. Master problem solution. Find p1 ≥0, . . . , pr ≥0 such that
r

l=1
pl = 1,
r

l=1
vl(ξl)pl ≤βi, i = 1, . . . , s,
r

l=1
vl(ξl)pl = βi, i = s + 1, . . . , M, and
z =
r

l=1
g(ξl)pl is maximized.
(5.29)
Let {pj
1, . . . , pj
r} attain the optimum in (5.29), and let {σj, πj
1, . . . , πj
M} be
the associated dual multipliers such that
σj +
M

i=1
πj
i vi(ξl) = g(ξl), if pl > 0, l = 1, . . . , r,
σj +
M

i=1
πj
i vi(ξl) ≥g(ξl), if pl = 0, l = 1, . . . , r,
πj
i ≥0, i = 1, . . . , s.
(5.30)
Step 2. Subproblem solution. Find ξr+1 that maximizes
γ(ξ, σj, πj) = g(ξ) −σj −
M

i=1
πj
i vi(ξ).
(5.31)
If γ(ξr+1, σj, πj) > 0, let r = r + 1, ν = ν + 1 and go to Step 1. Otherwise
stop; {pj
1, . . . , pj
r} are the optimal probabilities associated with {ξ1, . . . , ξr}
in a solution to (5.27).
As we saw in Chapter 3, the generalized programming approach is useful
in problems with a potentially large number of variables. This approach
is used in Ermoliev, Gaivoronski, and Nedeva [1985] to solve a class of
problems (5.27). The diﬃculty in GLP is in the solution of the subprob-
lem (5.31), which generally involves a nonconvex function. Birge and Wets
[1986] describe how to solve (5.31) with constrained ﬁrst and second mo-
ments, if convexity properties of γ can be identiﬁed. Cipra [1985] describes
other methods for this problem based on discretizations and random selec-
tions of candidate points, xi. Dul´a [1991] gives results when g is sublinear
and has simplicial level sets. Kall [1991] gives the results for sublinear,
polyhedral functions with known generators. Edirisinghe [1996] also ﬁnds


## Page 336

9.5 Generalized Bounds
317
bounds using second moment information that is somewhat looser than the
generalized moment solution.
Kall’s result is useful when the optimal recourse problem multipliers are
known, so that
Q(x,ξ) =
max
i=1,...,K πT
i (h −Tx),
(5.32)
where we again assume that ξ = h or that T and q are known. Kall’s result
pertains to having known means for all hi and a limit ρ on the total second
moment, deﬁned as
ρ =

Ξ
∥ξ∥2P(dξ).
(5.33)
The moment problem becomes:
sup
P ∈P

Ω
Q(x, ξ)P(dξ)
s. t.

Ξ
ξP(dξ) = ¯h and (5.33),
(5.34)
where P is a set of probability measures with support, Ξ.
Kall shows that the solution of (5.34) with Q deﬁned as in (5.32) is
equivalent to the following ﬁnite-dimensional optimization problem:
inf
y∈ℜm{ max
i=1,...,K
(
ρ −2(¯h)T Tx + ∥Tx∥2∥πi −y∥+ (¯h −Tx)T y}.
(5.35)
Dul´a obtained similar results for strictly simplicial Q. Note that when
¯h = Tx, this reduces to a form of location problem to minimize the max-
imum weighted distance from πi to y. The solution to (5.34) may involve
calculations with each of these recourse problem solutions, but the result-
ing distribution P that solves (5.34) still has only m2 +2 points of support.
These are found by solving for the Karush-Kuhn-Tucker conditions for
problem (5.34), where the y values correspond to multipliers for the mean
value constraints.
Other bounds are also possible for diﬀerent types of objective functions.
In particular, we consider functions built around separable properties. The
use of the generalized programming formulation is limited in multiple di-
mensions because of the diﬃculty in solving subproblem (5.32). These com-
putational disadvantages for large values of N suggest that a looser but
more computationally eﬃcient upper bound on the value of (5.27) may be
more useful than solving (5.27) exactly for large N.
If a separable function, η(x) = 	N
i=1 ηi(x(i)), is available, it oﬀers an
obvious advantage by only requiring single integrals, as we stated earlier.
Here, we would also like to show that these bounds can be extended to non-
linear recourse functions. We suppose that the recourse function becomes
some general g(ξ(ω)), where
g(ξ) = inf
y {q(y)|g(y) ≤ξ}.
(5.36)


## Page 337

318
9. Evaluating and Approximating Expectations
In this case, we would like to ﬁnd η(ξ) = 	N
i=1 ηi(ξ(i)) ≥g(ξ) where each
ηi(ξ(i)) is a convex function. Methods for constructing these functions to
bound the optimal value of a linear program with random right-hand sides
were discussed in Subsection b. We next give the results for the general
problem in (5.36).
Lemma 8. If g is deﬁned as in (5.36), then g is a convex function of ξ.
Proof:
Let y1 solve the optimization problem in (5.36) for ξ1 and let y2
solve the corresponding problem for ξ2. Consider ξ = λξ1 + (1 −λ)ξ2. In
this case, g(λy1 + (1 −λ)y2) ≤λg(y1) + (1 −λ)g(y2) ≤λξ1 + (1 −λ)ξ2. So
g(λξ1 + (1 −λ)ξ2) ≤q(λy1 + (1 −λ)y2) ≤λg(ξ1) + (1 −λ)g(ξ2), giving the
result.
Let
ηi(ξ(i)) ≡1
N g(Nξ(i)ei),
(5.37)
which is the optimal value of a parametric mathematical program. The
following theorem shows that these values supply the separable bound re-
quired. Related bounds are possible by deﬁning ηi with other right scalar
multiples, gλi(ξ(i)ei) (see Rockafellar [1969] for general properties), where
	N
i=1 λi = 1. The following proof below is easily extended to these cases
and to translations of the constraints and explicit variable bounds.
Theorem 9. The function η(ξ) = 	N
i=1 ηi(ξ(i)) ≥g(ξ), where g is deﬁned
as in (5.36).
Proof:
In this case, let yi(ξ(i)) solve (5.36), where ξ(ω) = Nξ(i)ei. Then,
g(
N
i=1 yi(ξ(i))
N
) ≤	N
i=1( 1
N )[g(yi(ξ(i))] ≤	N
i=1( 1
N )Nξ(i)ei = ξ. Next, let
y∗solve (5.36) for ξ in the right-hand side of the constraints. By feasibility
of 	N
i=1
yi(ξ(i))
N
, g(ξ) = q(y∗) ≤q(	N
i=1
yi(ξ(i))
N
) ≤	N
i=1( 1
N )q(yi(ξi)) =
	N
i=1 ηi(ξ(i)) = η(ξ).
This result demonstrates that a parametric optimization of (5.36) in
i = 1, . . . , N yields an upper bound on g(ξ) for any ξ. The bound may
be tight, as in some examples for stochastic linear programs as given in
Subsection b.
Generalizations of the stochastic linear program bound as in Subsection
b can also be given for the general bound in Theorem 9. For example, we
may apply a linear transformation T to ξ to obtain u = Tξ. The con-
straints become g(y) ≤G−1(u). To use any bound of the general type in
Theorem 9 to bound

ℜN g(ξ)dg(ξ) requires a bound on

ℜηi(ξ(i)) dFi(ξi)
or

ℜµi(u(i))dFui(u(i)), where Fi is the marginal distribution on ξi and
Fui is the marginal distribution on u(i). Because it may be diﬃcult to ﬁnd
the distribution of u, the generalized moment problem can be solved to
obtain bounds on each integral in ℜ. Generalized linear programming may
solve this problem but can be ineﬃcient. To simplify this process, in Birge


## Page 338

9.5 Generalized Bounds
319
and Dul´a [1991], it is shown that a large class of functions requires only
two points of support in the bounding distribution. A single line search can
determine these points and give a bound on f over all distributions with
bounded ﬁrst and second moments for the marginals.
We develop bounds following Birge and Dul´a [1991] on

ηi(x(i))
dFi(x(i)) by referring to g as a function on ℜ(N = 1). We then con-
sider the moment problem (5.27) with s = 0, and M = 2 and where the
constraints correspond to known ﬁrst and second moments. In other words,
we wish to ﬁnd:
U = supQ∈P

Ξ g(ξ)P(dξ)

Ξ ξP(dξ)
= ¯ξ,

Ξ ξ2P(dx)
= ¯ξ(2),
(5.38)
where P ∈P is the set of probability measures on (Ξ, B1), the ﬁrst moment
of the true distribution is ¯ξ, and the second moment is ¯ξ(2).
A generalization of Carath´eodory’s theorem (Valentine [1964]) for the
convex hull of connected sets tells us that y∗can be expressed as a convex
combination of at most three extreme points of C, giving us a special case
of Theorem 9. Therefore, an optimal solution to (5.38) can be written,
{ξ∗, p∗}, where the points of support, ξ∗= {ξ∗
1, ξ∗
2, ξ∗
3} have probabilities,
p∗= {p∗
1, p∗
2, p∗
3}. An optimal solution may, however, have two points of
support. A function that has this property for a given instance of (5.27)
is called a two–point support function. We will give suﬃcient conditions
for a function to have this two-point support property. This property then
allows a simpliﬁed solution of (5.38). It is given in the next theorem which
is proven in Birge and Dul´a [1991].
Theorem 10. If g is convex with derivative g′ deﬁned as a convex function
on [a, c) and as a concave function on (c, b] for Ξ = [a, b] and a ≤c ≤b,
then there exists an optimal solution to (5.38) with at most two support
points, {ξ1, ξ2}, with positive probabilities, {p1, p2}.
A corollary of Theorem 10 is that any function g that has a convex or
concave derivative has the two-point support property. The class of func-
tions that meets the criteria of Theorem 10 contains many useful examples,
such as:
1. Polynomials deﬁned over ranges with at most one third-derivative
sign change.
2. Exponential functions of the form, c0ec1ξ, c0 ≥0.
3. Logarithmic functions of the form, logj(cξ), for any j ≥0.
4. Certain hyperbolic functions such as sinh(cξ), c, ξ ≥0, cosh(cx).


## Page 339

320
9. Evaluating and Approximating Expectations
5. Certain trigonometric and inverse trigonometric functions such as
tan−1(cξ), c, ξ ≥0.
In fact, Theorem 10 can be applied to provide an upper bound on the
expectation of any convex function with known third derivative when the
distribution function has a known third moment, ¯ξ(3). Suppose a > 0 (if
not, then this argument can be applied on [a, 0] and [0, b]); then let g(ξ) =
βξ3 + g(ξ). The function g is still convex on [0, b) for β ≥0. By deﬁning
β ≥(−1/6) min(0, infξ∈[a,b] f ′′′(ξ)), g′ is convex on [a, b], and an upper
bound, UB(g), on Eg(ξ) has a two-point support. The expectation of g is
then bounded by
Eg(ξ) ≤UB(g) −β ¯ξ(3).
(5.39)
The conditions in Theorem 10 are only suﬃcient for a two–point support
function. They are not necessary (see Exercise 8). Note also that not all
functions are two-point support functions (although bounds using (3.4)
are available). A function requiring three support points, for example, is
g(ξ) = (1/2) −

(1/4) −(ξ −(1/2))2 (Exercise 9).
Given that a function is a two-point support function, the points {ξ1, ξ2}
can be found using a line search to ﬁnd a maximum.
For the special case of piecewise linear functions, the points, ξ1, ξ2, can be
found analytically. In this case, suppose that g(ξ) = ψSR(h, χ), the simple
recourse function deﬁned by:
ψSR(h, χ) =

q−(χ −h)
if h ≤χ,
q+(h −χ)
if h > χ.
(5.40)
Consider the nonintersecting intervals, A = (0, ¯ξ(2)/(2¯ξ)), B = [¯ξ(2)/(2¯ξ),
(1 −¯ξ(2))/(2(1 −¯ξ))], and C = ((1 −¯ξ(2))/(2(1 −¯ξ)), 1). The points of
support for this semilinear, convex function deﬁned on [0, 1] are
{ξ∗
1, ξ∗
2} =



{0, ¯ξ(2)/¯ξ}
if χ ∈A,
{χ −d, χ + d}
if χ ∈B,
{(¯ξ −¯ξ(2))/(1 −¯ξ), 1}
if χ ∈C,
(5.41)
where d =

χ2 −2χ¯ξ + ¯ξ(2). This result can be obviously extended to
other ﬁnite intervals. Inﬁnite intervals can also be solved analytically for
these semilinear, convex functions. For X = [0, ∞) , the results are as in
(5.41) with B = [¯ξ(2)/(2¯ξ), ∞) and C = ∅. For the interval (−∞, ∞), the
points of support are those for interval B in (5.41). We note that special
cases for these supports of semilinear, convex functions were considered in
Jagganathan [1977] and Scarf [1958].
Other bounds are also possible using the generalized moment problem
framework. One possible approach is to use piecewise linear constraints on
the quadratic functions deﬁning second-moment constraints as in (5.38).
This approach is described in Birge and Wets [1987] which also considers


## Page 340

9.5 Generalized Bounds
321
unbounded regions that lead to measures that are limiting solutions to
(5.27) but that may not actually be probability measures but are instead
nonnegative measures with weights on extreme directions of Ξ. An example
is given in Exercise 12.
To see how these bounds are constructed for unbounded regions, weights
can be placed on extreme recession directions, rj, j = 1, . . . , J, such that
ξ+βrj ∈Ξ for all ξ ∈Ξ and rj not expressable in non-negative multiples of
other recession directions. Then, if the recourse function Q has a recession
function, rcQ(x, rj) ≥
Q(x,ξ+βrj)−Q(x,ξ)
β
for all β > 0, then Q(x, ξ) ≤
	
k=1,...,K λjQ(x, ej) + 	
j=1,...,J µjrcQ(x, rj), when ξ = 	
k=1,...,K λjej +
	
j=1,...,J µjrj, 	
k=1,...,K λj = 1, λj, µj ≥0. Now, an analogous result
to Theorem 1 can be constructed where λj =

Ξ λ(ξ, ej)P(dξ) and µj =

Ξ µ(ξ, rj)P(dξ) are constructed from measures λ(ξ, ·) and µ(ξ, ·) such that
ξ = 	
k=1,...,K ejλ(ξ, ej) + 	
j=1,...,J rjµj(ξ, rj) for all ξ ∈Ξ.
With piecewise linear functions, vi(ξ) = βilξ + βil on Ξl, l = 1, . . . , L,
P[Ξl] = pl,

Ξ
vi(ξ)P(dξ) =
L

l=1

e∈extΞl
βileλl(e) +

r∈rcΞl
βilrµl(r) −βilpl,
(5.42)
where λl(e) is a weight on the extreme point e in Ξl and µl(r) is a weight
on extreme direction r of Ξl. From (5.42), we can use a piecewise linear vi
to bound nonlinear v from below. If

Ξ
v(ξ)P(dξ) ≤¯v,
(5.43)
then

Ξ
vi(ξ)P(dξ) ≤¯v.
(5.44)
Thus, we can use (5.44) in place of (5.43) to obtain an upper bound on
a moment problem. The advantage of (5.44) is that we need only use the
extreme values of the Ξl from (5.42) in (5.44).
Other types of bounds are also possible that depend on diﬀerent types
of functions, such as lower piecewise linear functions (see Marti [1975] or
Birge and Wets [1986]). Stochastic dominance of probability distributions
can also be used to construct bounds, although this tends to be diﬃcult in
higher dimensions (see Birge and Wets [1986, section 7]). Another alterna-
tive is to identify optimization procedures that improve among all possible
distributions (see, e.g., Marti [1988]). Still other procedures are possible
using conjugate function information directly; Birge and Teboulle [1989]
use nonlinear functions that are otherwise not easily evaluated.
We have not yet considered approximations based on sampling ideas.
Many possibilities exist in this area as well. We will describe these bounds
and algorithms based on them in Chapter 10.


## Page 341

322
9. Evaluating and Approximating Expectations
Exercises
1. Verify the derivation of η(ξ, ·) in (5.2).
2. Derive the result in (5.3).
3. Consider the sugar beet recourse function, Q3, in Section 1.1. Suppose
that the selling price above 6000 is actually a random variable, q,
that has mean 10 and is distributed on [5, 15]. Suppose also that
E[qr3] = 250. Use (5.9) to derive a lower bound on Q3(300).
4. Verify the result of the integration in (5.5) given in (5.9).
5. Verify that 	
Λ∈L cΛ(el)mΛ = 0 implies 	
Λ∈L cΛ(el)mj,Λ = 0 and
that, if both are nonzero, then

Λ∈L cΛ(el)mj,Λ

Λ∈L cΛ(el)mΛ is in the closure of the
support of h.
6. Find the functions ΨDi as functions of χ for each i as in the ex-
ample. Also ﬁnd the optimal value function Ψ in terms of χ. Graph
these functions as functions of χ2 for values of χ1 = 0.j, j = 0, . . . , 9.
Compare the convex hulls of the approximations with the graph
of Ψ.
7. Using the data for Example 1, solve (5.34) to determine an upper
bound with the total second-moment constraint.
8. Construct a two-point support function that does not meet the con-
ditions in Theorem 3.
9. Show that g(ξ) = (1/2) −

(1/4) −(ξ −(1/2))2 requires three sup-
port points to obtain the best upper bound with mean of 0.5 and
variance of 1/6 on Ξ = [0, 1].
10. Find the Edmundson-Madansky and two-moment bounds for the ξ
uniform on Ξ = [0, 1] and the following functions: e−ξ, ξ3, sin(π(ξ +
1)).
11. Use the results in Theorems 9 and 10 to bound the following nonlinear
recourse function with the form in (5.38). We suppose in this case that
g(ξ1, ξ2) =
 min(ξ1 −1)2 + (ξ2 −2)2
s. t. ξ2
1 + ξ2
2 −1 ≤ξ1,
(ξ1 −1)2 + ξ2
2 −1 ≤ξ2.
12. Suppose that it is known that the ξi are non-negative, that ¯ξi = 1,
and that ¯ξ(2)
i
= 1.25. In this case, we would like an upper bound on
the expected performance E(g(ξ). We construct a bound by ﬁrst ﬁnd-
ing ηi(ξi) as in (5.37). This problem may correspond to determining


## Page 342

9.6 General Convergence Properties
323
a performance characteristic of a part machined by two circular mo-
tions centered at (0, 0) and (1, 0), respectively. Here, the performance
characteristic is proportional to the distance from the ﬁnished part
to another object at (2, 1). The square of the radii of the tool motions
is ξi + 1, where ξi is a non-negative random variable associated with
the machines’ precision.
13. As an example of using (5.41), consider Example 1, but assume that
Ξ is the entire non-negative orthant and that each ξi is exponentially
distributed with mean 0.5. Use a piecewise linear lower bound on
the individual second moments that is zero for 0 ≤ξi ≤0.5, and
2ξi −1 for ξ ≥0.5. Solve the moment problem using these regions to
obtain an upper bound for all expected recourse functions with the
same means and variances as the exponential. Also, solve the moment
problem with only mean constraints and compare the results.
9.6
General Convergence Properties
For the following bounding discussions, we use a general function notation
because these results hold quite broadly. The discussion in this section
follows Birge and Qi [1995], which gives a variety of results on convergence
of probability measures. Other references are Birge and Wets [1986] and
King and Wets [1991]. This section is fundamental for theoretical properties
of convergence of approximations.
We consider the expectational functional E(g(·)) = E{g(·,ξ))}, where ξ
is a random vector with support Ξ ⊆ℜN and g is an extended real-valued
function on ℜn × Ξ. Here,
E(g(x)) =

g(x,ξ)P(dξ),
(6.1)
where P is a probability measure deﬁned on ℜn.
We assume that E(g(·)) (which represents the recourse function Q) is
diﬃcult to evaluate because of the complications involved in g and the
dimension of Ξ. The basic goal in most approximations is to approximate
(6.1) by
Eν(g(x)) =

g(x,ξ)P ν(dξ),
(6.2)
where {P ν, ν = 1, ....} is a sequence of probability measures converging in
distribution to the probability measure P. By convergence in distribution,
we mean that

g(ξ)P ν(dξ) →

g(ξ)P(dξ) for all bounded continuous g on
Ξ. For more general information on convergence of distribution functions,
we refer to Billingsley [1968].
In the following, we use E0 and P 0 instead of E and P for convenience.
If C ⊆ℜn is a closed convex set, then Ψ∗
C is the support function of C,


## Page 343

324
9. Evaluating and Approximating Expectations
deﬁned by Ψ∗(g|C) = sup{< x, g >: x ∈C}. A sequence of closed convex
sets {Cν : ν = 1, ...} in ℜn is said to converge to a closed convex set C in
ℜn if for any g ∈ℜn,
lim
ν→+∞Ψ∗(g|Cν) = Ψ∗(g|C).
One may easily prove the following proposition that is stated without proof.
Proposition 11. Suppose that C and Cν, for ν = 1, ..., are closed convex
sets in ℜn. The following two statements are equivalent:
(a) Cν converges to C as ν →+∞;
(b) a point x ∈C if and only if there are xν ∈Cν such that xν →x.
This notion of set convergence is important in the study of convergence
of functions. We say that a sequence of functions, {gν; ν = 1, . . .}, epi-
converges to function, g, if and only if the epigraphs, epi gν = {(x, β)|β ≥
gν(x)}, of the functions converge as sets to the epigraph of g, epi g =
{(x, β)|β ≥g(x)}. Epi-convergence has many important properties, which
are explored in detail in Wets [1980a] and Attouch and Wets [1981]. A chief
property (Exercise 1) is that any limit point of minima of gν is a minimum
of g.
In the following, we restrict our attention to convex integrands g al-
though extensions to nonconvex functions are also possible as in Birge and
Qi [1995]. In this case, one can use the generalized subdiﬀerential in the
sense of Clarke [1983] or other deﬁnitions as in Michel and Penot [1984] or
Mordukhovich [1988]. The next theorem appears in Birge and Wets [1986]
with some extensions in Birge and Qi [1995]. Other results of this type
appear in Kall [1987].
Theorem 12. Suppose that
(i) {P ν, ν = 1, ....} converges in distribution to P;
(ii) g(x, ·) is continuous on Ξ for each x ∈D, where
D = {x : E(g(x)) < +∞} = {x : g(x, ξ) < +∞, a.s.};
(iii) g(·, ξ) is locally Lipschitz on D with Lipschitz constant independent of
ξ;
(iv) for any x ∈D and ǫ > 0, there exists a compact set Sǫ and νǫ such
that for all ν ≥νǫ,

Ξ\Sǫ
|g(x,ξ)|P ν(dξ) < ǫ,
and with Vx = {ξ : g(x, ξ) = +∞}, P(Vx) > 0 if and only if P ν(Vx) > 0 for
ν = 0, 1, ....
Then
(a) Eν(g(·)) epi- and pointwise converges to E(g(·)); if x, xν ∈D for ν =
1, 2, ... and xν →x, then
lim
ν→∞Eν(g(xν)) = E(g(x));


## Page 344

9.6 General Convergence Properties
325
(b) Eν(g(·)), where ν = 0, 1, ..., is locally Lipschitz on D; furthermore, for
each x ∈D, {∂Eν(g(x)) : ν = 0, 1, ....} is bounded;
(c) if xν ∈D minimizes Eν(g(x)) for each ν and x is a limiting point of
{xν}, then x minimizes E(g(x)).
Proof:
First, we establish pointwise convergence of the expectation func-
tionals. Suppose x ∈D and consider Sǫ as in the hypothesis. Let Mǫ =
supξ∈Sǫ |g(x, ξ)|, which is ﬁnite for g continuous and Sǫ compact. Construct
a bounded and continuous function,
gǫ(ξ) =



g(x, ξ)
if |g(x, ξ)| ≤Mǫ,
Mǫ
if |g(x, ξ)| > Mǫ,
−Mǫ
if |g(x, ξ)| < −Mǫ.
By convergence in distribution, βν
ǫ →βǫ, for βν
ǫ =

Ξ gǫ(ξ)P ν(dξ) and
βǫ =

Ξ gǫ(ξ)P(dξ). Let βν =

Ξ g(x, ξ)P ν(dξ). Noting that for ν > νǫ,

Ξ\Sǫ gǫ(ξ)P ν(dξ) < ǫ,
|βν −βν
ǫ | < 2ǫ.
(6.3)
We also have that
|β −βǫ| < 2ǫ.
(6.4)
From the convergence of the βν, there exists some ¯νǫ such that for all
ν ≥¯νǫ,
|βν
ǫ −βǫ| < 2ǫ.
(6.5)
Combining (6.3), (6.4), and (6.5) for any ν > max{¯νǫ, νǫ},
|β −βν| < 6ǫ,
which establishes that Eν(g(x)) →E(g(x)) for any x ∈D.
To establish epi-convergence, from (b) of Proposition 11, we need to
show that if x ∈D and h ≥E(g(x)), then there exists xν ∈D and hν ≥
Eν(g(xν)) such that (xν, hν) →(x, h), and, if xν ∈D and hν ≥Eν(g(xν))
such that (xν, hν) →(x, h), then x ∈D and h ≥E(g(x)). The former
follows by letting xν = x and hν = Eν(g(x)) + (h −E(g(x))) and using
pointwise convergence. The latter follows from pointwise convergence and
continuity because ν = limν hν ≥limν Eν(g(xν)) = limν[(Eν(g(xν)) −
Eν(g(x)) + (Eν(g(x)) −E(g(x))) + E(g(x))] = E(g(x)).
For (b), again let x, xν ∈D, xν →x. For any x ∈D, y, and z close to x,
ν = 0, 1, ...,
|Eν(g(y)) −Eν(g(z))|
≤

|g(y,ξ) −g(z,ξ)|P ν(dξ)
≤

Lx∥y −z∥P ν(dξ)
=Lx∥y −z∥,


## Page 345

326
9. Evaluating and Approximating Expectations
where Lx is the Lipschitz constant of g(·, ξ) near x, which is indepen-
dent of ξ by (iii). By (ii) and (iii), x is in the interior of the domain
of Eν(g(x)). Hence, (see Theorem 23.4 in Rockafellar [1969]), the subd-
iﬀerential ∂Eν(g(x)) is a nonempty, compact convex set, for each ν. The
two-norms of subgradients in these subdiﬀerentials are bounded by Lx.
By (b), Eν(g(x)) are lower semicontinuous functions. By (a), Eν(g(x))
epi-converges to E(g(x)). We get the conclusion of (c) from the statement
in Exercise 1. This completes the proof.
This result also extends directly to nonconvex functions, as we men-
tioned earlier. In terms of stochastic programming computations, the most
useful result may be (c), which implies convergence of optima for approxi-
mating distributions. Actually achieving optimality for each approximation
may be time-consuming. One might, therefore, be interested in achieving
convergence of subdiﬀerentials. This may allow suboptimization for each
approximating distribution.
In the case of closed convexity, Wets showed in Theorem 3 of Wets [1980a]
that if g, gν : ℜn →ℜ∪{+∞}, ν = 1, 2, ..., are closed convex functions
and {gν} epi-converges to g, then the graphs of the subdiﬀerentials of gν
converge to the graph of the subdiﬀerential of g, i.e., for any convergent
sequence {(xν, uν) : uν ∈∂gν(xν)} with (x, u) as its limit, one has u ∈
∂g(x); for any (x, u) with u ∈∂g(x), there exists at least one such sequence
{(xν, uν) : uν ∈∂gν(xν)} converging to it.
However, in general, it is not true that
∂g(x) = lim
ν→∞∂gν(x)
(6.6)
even if x ∈int(dom(g)) (See Exercise 2). However, if g is G-diﬀerentiable
at x, (6.6) is true. This is the following result from Birge and Qi [1995].
Theorem 13. Suppose that g, gν : ℜn →ℜ∪{+∞}, ν = 1, 2, ..., are
closed convex functions and {gν} epi-converges to g. Suppose further that
g is G-diﬀerentiable at x. Then
∇g(x) = lim
ν→∞∂gν(x).
(6.7)
In fact, for any x ∈int(dom(g)), there exists νx such that for any ν ≥νx,
∂gν(x) is nonempty, and {∂gν(x) : ν ≥νx} is bounded. Thus, for any x ∈
int(dom(g)), the right hand side of (6.7) is nonempty and always contained
in the left-hand side of (6.7). But equality does not necessarily hold by our
example. We also state the following result in Corollary 2.5 of Birge and
Qi [1995].
Corollary 14. Suppose the conditions of Theorem 2 and that g(·, ξ) is
convex for each ξ ∈Ξ. Then for D = dom(E(g(·))),
(d) there is a Lebesgue zero-measure set D1 ⊆D such that E(g(x)) is G-
diﬀerentiable on D \ D1, E(g(x)) is not G-diﬀerentiable on D1, and for


## Page 346

9.6 General Convergence Properties
327
each x ∈D \ D1
lim
ν→∞∂Eν(g(x)) = ∇E(g(x));
(e) for each x ∈D,
∂E(g(x)) = { lim
ν→∞uν : uν ∈∂Eν(g(xν)), xν →x}.
Proof: By closed convexity of g(·, ξ), Eν(g(x)) are also closed convex for all
ν. Now (d) follows Theorem 13 and the diﬀerentiability property of convex
functions, and (e) follows Theorem 3 of Wets [1980a].
Many other results are possible using Theorem 13 and results on epi-
convergence. As an example, we consider convergence of sampled problem
minima following King and Wets [1991]. Let P ν be an empirical measure
derived from an independent series of random observations {ξ1, ..., ξν} each
with common distribution P. Then, for all x,
Eν(g(x)) = 1
ν
ν

i=1
g(x, ξi).
Let (Ξ, A, P) be a probability space completed with respect to P. A closed-
valued multifunction G mapping Ξ to ℜn is called measurable if for all closed
subsets C ⊆ℜn, one has
G−1(C) := {ξ ∈Ξ : G(ξ) ∩C̸ = ∅} ∈A.
In the following, “with probability one” refers to the sampling probability
measure on {ξ1, ..., ξν, ...} that is consistent with P (see King and Wets
[1991] for details). Applying Theorem 2.3 of King and Wets [1991] and
Corollary 14, we have the following.
Corollary 15. Suppose for each ξ ∈Ξ, g(·, ξ) is closed convex and the
epigraphical multifunction ξ →epi g(·, ξ) is measurable. Let Eν(g(x)) be
calculated by (6.2). If there exists ¯x ∈dom(Eν(g(x))) and a measurable
selection ¯u(ξ) ∈∂g(¯x,ξ) with

∥¯u(ξ)∥P(dξ) ﬁnite, then the conclusions of
Corollary 14 hold with probability one.
King and Wets [1991] applied their results to the two-stage stochastic
program with ﬁxed recourse repeated here as
min cT x +

Q(x,ξ)P(dξ)
s. t. Ax = b,
x ≥0,
(6.8)
where x ∈ℜn and
Q(x,ξ) = inf{q(ξ)T y|Wy = h(ξ) −T(ξ)x, y ∈ℜn2
+ }
(6.9)


## Page 347

328
9. Evaluating and Approximating Expectations
It is a ﬁxed recourse problem because W is deterministic. Combining their
Theorem 3.1 with our Corollary 14, we have the following.
Corollary 16. Suppose that the stochastic program (6.8) has ﬁxed recourse
(6.9) and that for all i, j, k, the random variables qiζj and qiTjk have
ﬁnite ﬁrst moments. If there exists a feasible point ¯x of (6.9) with the
objective function of (6.9) ﬁnite, then the conclusions of Corollary 14 hold
with probability one for
g(x, ξ) = cT x + Q(x, ξ) + δ(x),
where δ(x) = 0 if Ax = b, x ≥0, δ(x) = +∞otherwise.
By Theorem 3.1 of King and Wets [1991], one may solve the approxima-
tion problem
min cT x + 1
ν
ν

i=1
Q(x, ξi)
s. t. Ax = b,
x ≥0,
(6.10)
instead of solving (6.8). If the solution of (6.10) converges as ν tends to
inﬁnity, then the limiting point is a solution of (6.8). Alternatively, by
Corollary 16, one may directly solve (6.8) with a nonlinear programming
method and use
cT x + 1
ν
ν

i=1
Q(x, ξi)
and
c + 1
ν
ν

i=1
∂xQ(x, ξi)
as approximate objective function values and subdiﬀerentials of (6.8) with
ν = ν(k) at the kth step. Notice that −uT T(ξi) ∈∂xQ(x, ξi) if and only
if u is an optimal dual solution of (6.9) with ξ = ξi. In this way, one may
directly solve the original problem using the subgradients −uT T(ξi) and
the probability that each is optimal (equivalently that the corresponding
basis is primal feasible). The calculation is therefore reduced to obtaining
the probability of satisfying a system of linear inequalities, which can be
approximated well (see Pr´ekopa [1988] and Section 4). This procedure may
allow computation without calculating the actual objective value, which
may involve a more diﬃcult multiple integral.
These results give some general idea about the uses of approximations in
stochastic programming. We can also introduce approximating functions,
gν, such that gν converges to g pointwise in D. Similar convergence results
are also obtained there. The general rule is that approximating distribu-
tion functions that converge in distribution (even with probability one)


## Page 348

9.6 General Convergence Properties
329
to the true distribution function lead to convergence of optima and, for
diﬀerentiable points, convergence of subgradients.
Exercises
1. Prove that if gν epi-converges to g and x∗is a limit point of {xν},
where xν ∈arg min gν = {x|gν(x) ≤inf gν}, then x∗∈arg min g.
2. Construct an example where gν epi-converges to g but ∂g(x)̸ =
limν ∂gν(x).
3. Consider the basic bounding method in Section 2. Suppose that Ξ is
compact and that for any ǫ > 0, there exists some νǫ such that for all
ν ≥νǫ, diamSl ≤ǫ for all Sl ∈Sν. Show that this implies that P ν
converges to P in distribution.


## Page 349



## Page 350

10
Monte Carlo Methods
Each function value in a stochastic program can involve a multidimensional
integral with extremely high dimensions. Because Monte Carlo simulation
appears to oﬀer the best possibilities for higher dimensions (De´ak [1988]),
it seems to be the natural choice for use in stochastic programs. In this
chapter, we describe some of the basic approaches built on sampling meth-
ods. The key feature is the use of statistical estimates to obtain conﬁdence
intervals on results. Some of the material uses probability measure theory
which is necessary to develop the analytical results.
The ﬁrst section describes the basic results for statistical analyses of
stochastic programs. We consider a stochastic program formed with a set
of random observations and the asymptotic properties of optimal solutions
to those problems. In general, these problems can be solved using any
technique that might apply to the sampled problems.
Section 2 considers methods based on the L-shaped method without
resolving each problem in each period. We ﬁrst consider possibilities for
estimating the cuts using a large number of samples for each cut. We then
consider the stochastic decomposition method (Higle and Sen [1991b]) that
forms many cuts with few additional samples on each iteration.
Section 3 considers methods based on the stochastic quasi-gradient,
which can be viewed as a generalization of the steepest descent method.
These approaches have a wide variety of applications that extend beyond
stochastic programming.
In Section 4, we consider extensions of Monte Carlo methods to include
analytical evaluations exploiting problem structure in probabilistic con-


## Page 351

332
10. Monte Carlo Methods
straint estimation and empirical sample information for methods that may
use updated information in dynamic problems.
10.1
General Results for Sampled Problems
We begin by considering a stochastic program in the following basic form:
inf
x∈X

Ξ
g(x,ξ)P(dξ),
(1.1)
where X ⊂ℜn and ξ is now deﬁned on the probability space (Ξ, B, P) so
that we can work directly with ξ instead of through ω. Suppose that (1.1)
has an optimal solution, x∗.
A natural approach to solving (1.1) is to consider an approximate prob-
lem derived by taking ν samples from ξ. The discrete distribution with
these samples could be P ν, which would allow us to apply the results in
Chapter 9 to obtain convergence of the ν problem optimal solutions to the
optimal solution in (1.1). We would like even more, however, to describe
distributional properties of these solutions so that we can construct con-
ﬁdence intervals in place of the (probability one) bounds found in Chap-
ter 9.
We therefore wish to consider a sample {ξi} of independent observations
of ξ that are used in the approximate problem:
inf
x∈X(1
ν )
ν

i=1
g(x, ξi).
(1.2)
Suppose that xν is the random vector of solutions to (1.2) with independent
random samples, ξi, i = 1, . . . , ν. The general question considered in King
and Rockafellar [1993] is to ﬁnd a distribution u such that √ν(xν −x∗)
converges to u in distribution. Properties of u can then be used to derive
conﬁdence intervals for x∗from an observation of xν.
We give the main result without proof. The interested reader can refer
to King and Rockafellar [1993] and, for the statistical origin, Huber [1967].
Theorem 1. Suppose that g(·, ξ) is convex and twice continuously diﬀer-
entiable, X is a convex polyhedron, ∇g : Ξ × ℜn →ℜn:
i. is measurable for all x ∈X;
ii. satisﬁes the Lipschitz condition that there exists some a :
Ξ →ℜ,

Ξ |a(ξ)|2P(dξ) < ∞, |∇g(x1, ξ) −∇g(x2, ξ)| ≤
a(ξ)|x1 −x2|, for all x1, x2 ∈X;
iii. satisﬁes that there exists x ∈X such that

Ξ |g(x,ξ)|2P(dξ) <
∞; and, for G∗=

∇2g(x∗,ξ)P(dξ),
iv. (x1 −x2)T G∗(x1 −x2) > 0, ∀x1̸ = x2, x1, x2 ∈X.


## Page 352

10.1 General Results for Sampled Problems
333
Then the solution xν to (1.2) satisﬁes:
√ν(xν −x∗) →u,
(1.3)
where u is the solution to:
min
1
2uT G∗u + cT u
s. t.
Ai·ui ≤0, i ∈I(x∗), uT ∇¯g∗= 0,
(1.4)
X = {x|Ax ≤b}, (x∗, π∗) solve ∇

Ξ g(x∗,ξ)P(dξ) + (π∗)T A = 0, π∗≥0,
Ax∗≤b, I(x∗) = {i|Ai·x∗= bi}, ∇¯g∗=

∇g(x∗,ξ)P(dξ), and c is
distributed normally N(0, Σ∗) with Σ∗=

(∇g(x∗,ξ) −∇g∗)(∇g(x∗,ξ) −
∇g∗)T P(dξ).
Proof:
See King and Rockafellar [1993, Theorem 3.2].
Example 1
Suppose that X = [a, ∞), ξ is normally distributed N(0, 1), and g(x, ξ) =
(x −ξ)2. Problem (1.1) then becomes:
inf
x≥a

Ξ
(x −ξ)2
√
2π
e−ξ2
2 dξ,
(1.5)
where we substituted for P the standard normal density with mean zero
and unit standard deviation.
Because the expectation in (1.5) is just x2+1, for a ≥0, the clear solution
is x∗= a. For a < 0, x∗= 0. In this case, ∇g(x∗, ξ) = −2(x −ξ), G∗= 2,
A = [−1], and ∇¯g∗= −2x. The variance of c is Σ∗= Eξ[(2ξ)2] = 4. The
asymptotic distribution u then solves:
min
u2 + cT u
s. t.
u ≥0 if x∗= a, u(−2x∗) = 0.
(1.6)
For a > 0, the solution of (1.6) is u∗= 0 so that asymptotically
√ν(xν −x∗) →0 in distribution. If a = 0, then note that because c/2
is N(0, 1), the overall result is that asymptotically the estimate, √νxν, for
(1.5) approaches a distribution with a probability mass of 0.50 at 0 and a
density for the normal distribution, N(0, 1), over (0, ∞). Exercise 1 asks
the reader to ﬁnd the asymptotic distribution for a < 0. In each case, the
actual distribution of xν can be found and compared to the asymptotic
result (see Exercise 2).
Many other results along these lines are possible (see, e.g., Dupaˇcov´a
and Wets [1988]). They often concern the stability of the solutions with
respect to the underlying probability distribution. For example, one might
only have observations of some random parameter but may not know the
parameter’s distribution. This type of analysis appears in Dupaˇcov´a [1984],
R¨omisch and Schultz [1991a], and the survey in Dupaˇcov´a [1990].


## Page 353

334
10. Monte Carlo Methods
Another useful result is to have asymptotic properties of the opti-
mal approximation value. For this, suppose that z∗is the optimal value
of (1.1) and zν is the random optimal value of (1.2). We use prop-
erties of g and ξi so that each g(x, ξi) is an independent and identi-
cally distributed observation of g(x,ξ), and g(x,ξ) has ﬁnite variance,
V arg(x) =

Ξ |g(x,ξ)|2P(dξ) −(Eg(x))2. We can thus apply the central
limit theorem to state that √ν[( 1
ν ) 	ν
i=1 g(x, ξi) −

Ξ g(x,ξ)P(dξ)] con-
verges to a random variable with distribution, N(0, V arg(x)). Moreover,
with the condition in Theorem 1, the random function on x deﬁned by
√ν[( 1
ν ) 	ν
i=1 g(x, ξi) −

Ξ g(x,ξ)P(dξ)] is continuous. We can then derive
the following result of Shapiro [1991, Theorem 3.3].
Theorem 2. Suppose that X is compact and g satisﬁes the following con-
ditions:
i. g(x, ·) is measurable for all x ∈X;
ii. there exists some a : Ξ →ℜ,

Ξ |a(ξ)|2P(dξ) < ∞,
|g(x1, ξ) −g(x2, ξ)| ≤a(ξ)|x1 −x2|, for all x1, x2 ∈X;
iii. for some x0 ∈X,

g(x0,ξ)P(dξ) < ∞;
and Eg(x) has a unique minimizer x0 ∈X. Then √ν[zν −z∗] converges in
distribution to a normal N(0, V arg(x0)).
Further results along these lines are possible using the speciﬁc structure
of g for the recourse problem as in (3.1.1). For example, if K1 is bounded
and Q has a strong convexity property, R¨omisch and Schultz [1991b] show
that the distance between the optimizing sets in (1.1) and (1.2) can be
bounded.
Given the results in Theorems 1 and 2 and some bounds on the vari-
ances and covariances, one can construct asymptotic conﬁdence intervals
for solutions using (1.2). All the previous discrete methods can be applied
to (1.2) to obtain solutions as ν increases. Various procedures can be used
in incrementing ν and solving the resulting approximation (1.2).
In the next sections, this need to solve (1.2) completely is avoided so that
the optimization and sampling are performed somewhat simultaneously.
First, we describe methods for doing this with the L-shaped method, then
we consider stochastic quasi-gradient approaches.
As a ﬁnal note, we should mention that analogous procedures can be
built around quasi-random sequences that seek to ﬁll a region of inte-
gration with approximately uniformly spaced points. The result is that
errors are asymptotically about of the order log(ν)/ν instead of 1/√ν
(see Niederreiter [1978]). The diﬃculty is in the estimation of the con-
stant term but quasi-Monte Carlo appears to work quite well in practice
(see Fox [1986] and Birge [1994]). In terms of expected performance over
broad function classes, quasi–Monte Carlo performs with the same order of
complexity (Wo´zniakowski [1991]). For the following methods, we may sub-


## Page 354

10.2 Using Sampling in the L-Shaped Method
335
stitute quasi-random sequences for pseudo-random sequences for practical
implementations.
Exercises
1. For Example 1, ﬁnd the asymptotic result from Theorem 1 for
√ν(xν −x∗) for a < 0.
2. For Example 1, derive the actual distribution of √ν(xν −x∗) for
a feasible region x ≥a in each case of a, a < 0, a = 0 and a >
0. Find the limits of these distributions and verify the result from
Theorem 1.
3. Consider a news vendor problem as in Section 1.1. Suppose this
problem is solved using a sampling approach. The sampled problem
with continuous cumulative distribution function F ν has a solution
at (F ν)−1( s−a
s−r ) = xν. Find the distribution of this quantile and show
how to construct a conﬁdence interval around x∗.
10.2
Using Sampling in the L-Shaped Method
The disadvantage of sampling approaches that solve the νth approximation
completely is that some eﬀort might be wasted on optimizing when the
approximation is not accurate. An approach to avoid these problems is to
use sampling within another algorithm without complete optimization. A
natural candidate is to embed sampling into the L-shaped method, which
often works well for discrete distributions. We consider two such approaches
in this section. The ﬁrst uses importance sampling to reduce variance in
deriving each cut based on a large sample (see Dantzig and Glynn [1990]).
The second approach uses a single sample stream to derive many cuts that
eventually drop away as iteration numbers increase (Higle and Sen [1991b]).
a. Importance sampling
The ﬁrst approach, by Dantzig and Glynn, is to sample Q in the L-shaped
method instead of actually computing it. Techniques to reduce the variance,
called importance sampling (see, e.g., Rubinstein [1981] and De´ak [1990]),
can then be used to achieve converging results. Given an iterate xs, the
result is an estimate, Qν(xs) = ( 1
ν (	ν
i=1 Q(xs, ξi)), and an estimate of
∇Q(xs) as ¯πν
s = ( 1
ν
	ν
i=1 πi
s) where πi
s ∈∂Q(xs, ξi). Now, for Q convex in
x, one obtains
Q(x, ξi) ≥Q(xs, ξi) + (πi
s)T (x −xs)
(2.1)


## Page 355

336
10. Monte Carlo Methods
for all x. We also have that
Qν(x) = (1
ν )(
ν

i=1
Q(x, ξi)) ≥Qν(xs) + (¯πν
s )T (x −xs) = LBν
s (x),
(2.2)
where, by the central limit theorem, √ν times the right-hand side is asymp-
totically normally distributed with a mean value,
√ν(Q(xs) + ∇Q(xs)T (x −xs)),
(2.3)
which is a lower bound on √νQ(x), and a variance, ρs(x).
Note that the cut placed on Q(x) as the right-hand side of (2.2) is a
support of Q with some error,
Q(x) ≥Qν(xs) + (¯πν
s )T (x −xs) −ǫs(x),
(2.4)
where ǫs(x) is an error term with zero mean and variance equal to 1
ν ρs(x).
Of course, the error term is not known. At iteration s, the L-shaped method
involves the solution of:
min
cT x
+θ
s. t.
Ax
= b,
Dlx
≥dl, l = 1, . . . , r,
Elx
+θ
≥el, l = 1, . . . , s,
x ≥0,
(2.5)
where Dl, dl is a feasibility cut as in (5.1.7)–(5.1.8), El = −¯πl, and el =
Qν(xl) + (¯πl)T (−xl), where we count iterations only when a ﬁnite Qν(xs)
is found. Note that the generation of feasibility cuts occurs whenever ξi is
sampled and Q(xl, ξi) is ∞.
We suppose that (2.5) is solved to yield xs+1 and θs+1, where
θs+1 = max
l
{el −Elxs+1},
(2.6)
where each el −Elxs+1 can be viewed as a sample from a normally dis-
tributed random variable with mean at most Q(xs+1) and variance at most
1
ν (σmax(xs+1))2 = 1
ν (maxl ρl(xs+1)). Note that θs+1 is a maximum of these
random variables so the solution of (2.5) has a bias that may skew results
for large s. Conﬁdence intervals can, however, be developed based on cer-
tain assumptions about the functions and the supports.
If the variances become small, one can stop with a high conﬁdence so-
lution. Other approaches may also be used. Infanger [1991] makes several
assumptions that can lead to tighter conﬁdence intervals on the optimal
value. Solutions of large problems appear in Dantzig and Infanger [1991]
with these assumptions.
Variances and any form of conﬁdence interval may be quite large when
crude Monte Carlo samples are used as indicated earlier. Dantzig and Glynn


## Page 356

10.2 Using Sampling in the L-Shaped Method
337
[1990] proposed the use of importance sampling to reduce the variance.
Their results indicate that the variance can be reduced quite substantially
with this technique.
In importance sampling, the goal is to replace a sample using the distri-
bution of ξ with one that uses an alternative distribution that places more
weight in the areas of importance. To see this, suppose that ξ has a density
f(ξ) over Ξ so that we are trying to ﬁnd:
Q(x) =

Ξ
Q(x, ξ)f(ξ)dξ.
(2.7)
The crude Monte Carlo technique generates each sample ξi according to
the distribution given by density f.
In importance sampling, a new probability density g(ξ) is introduced
that is somewhat similar to Q(x, ξ) and such that g(ξ) > 0 whenever
Q(x, ξ)f(ξ)̸ = 0. We then generate samples ξi according to this distribution
while writing the integral as:
Q(x) =

Ξ
Q(x, ξ)f(ξ)
g(ξ)
g(ξ)dξ.
(2.8)
In this case, we generate random samples from the distribution with density
g(ξ). Note that if g(ξ) = Q(x, ξ)f(ξ)/Q(x), then every sample ξi(imp)
under importance sampling yields an importance sampling expectation,
Q1
imp(x) = Q(x).
Of course, if we could generate samples from the density Q(x, ξ)/Q(x),
we would already know Q(x). We can, however, use approximations such
as the sublinear approximations in Section 9.5 that may be close to Q(x)
and should result in lower variances for Qν
imp over Qν. This approximation
is the approach suggested in Infanger [1991].
In the sublinear approximation approach, the approximating density g(ξ)
is chosen as
g(ξ) =
m2

i=1
ψI(i)((Tx)i·, hi)/ΨI(Tx).
(2.9)
In this way, much lower variances can result in comparison to the crude
Monte Carlo approach. One complication is, however, in generating a ran-
dom sample from the density in (2.9). The general techniques for generating
such random vectors is to generate sequentially from the marginal distri-
butions conditionally, ﬁrst choosing ξ1 with the ﬁrst marginal, g1(ξ1) =

ξ2,...,ξN g(ξ)dξ. Then, sequentially, ξi is chosen with density, gi(ξi|ξ1, . . . ,
ξi−1). Remember that in each case, a random sample with density gi(ξi)
on an interval Ξi of ℜcan be found by choosing from a uniform ran-
dom sample u from [0, 1] and then taking ξ such that G(ξ) = u where
G(x) =
 x
−∞gi(ξi)dξi.


## Page 357

338
10. Monte Carlo Methods
Example 2
Consider Example 1 of Section 9.2 with x1 = x2 = x. We consider both
the crude Monte Carlo approach and the importance sampling using the
sublinear approximation for g(ξ). In this case, g(ξ) is actually chosen to
depend on x as gx(ξ) deﬁned by:
gx(ξ) =
|x −ξ1| + |x −ξ2|
Eξ[|x −ξ1| + |x −ξ2|].
(2.10)
For comparison, we ﬁrst consider the L-shaped method with ξi chosen by
crude Monte Carlo from the original uniform density on [0, 1] × [0, 1] and
by the importance sampling method with distribution gx(ξ) in (2.10). The
results appear in Figure 1 for the solution xs at each iteration s of the crude
Monte Carlo and importance sampling L-shaped method with ν = 500 on
each L-shaped iteration. The ﬁgures show up to 101 L-shaped iterations,
which involve more than 50,000 recourse problem solutions.
In Figure 1, the crude Monte Carlo iteration values x appear as x(crude)
while the importance sampling iterations appear as x(imp). We also include
the optimal solution x∗=
√
2 −1 on the graph. Note that x(imp) is very
close to x∗from just over 40 iterations while x(crude) does not appear
to approach this accuracy within 100 iterations. Note that x(imp) begins
to deteriorate after 80 iterations as the accumulation of cuts increases the
probability that some cuts are actually above Q(x).
The advantage of importance sampling can also be seen in Figure 2, which
compares the optimal value Q(x∗) with sample values, Qν(xν), with crude
Monte Carlo denoted as Q(crude) and Qν
imp(xν) with importance sampling
denoted as Q(imp). Note that the crude Monte Carlo values have a much
wider variance, in fact, double the variance of the importance sampling
results. Also note that in both sampling methods, the estimates have a
mean close to the optimal value after 40 iterations.
The results in Figures 1 and 2 indicate that sampled cuts in the L-shaped
method can produce fairly accurate results but that convergence to optimal
values may require large numbers of samples for each cut even for small
problems. One diﬃculty is that initial cuts with small numbers of samples
may limit convergence unless they are removed in favor of more accurate
cuts. One procedure to avoid this problem is gradually to remove initial
cuts as the algorithm progresses. This is the intent of the next approach.
b. Stochastic decomposition
The alternative considered in Higle and Sen [1991b] is to generate many
cuts with small numbers of additional samples on each cut and to adjust
these cuts to drop as the algorithm continues processing. Their method
is called stochastic decomposition. They assume complete recourse and a


## Page 358

10.2 Using Sampling in the L-Shaped Method
339
FIGURE 1. Solutions for crude Monte Carlo and importance sampling.
FIGURE 2. Objective values for crude Monte Carlo and importance sampling.


## Page 359

340
10. Monte Carlo Methods
known (probability one) lower bound on Q(x, ξ) (e.g., 0). They also assume
that the set of dual solutions to the recourse problem (3.1.1) is bounded
and that K1 and Ξ are also compact.
With these assumptions, the basic stochastic decomposition method gen-
erates iterates, xk, and observations, ξk. We can state the basic stochastic
decomposition method in the following way.
Basic Stochastic Decomposition Method
Step 1. Set ν = 0, ξ0 = ¯ξ, and let x1 solve
min
Ax=b,x≥0{cT x + Q(x, ξ0)}.
(2.12)
Step 2. Let ν = ν + 1 and let ξν be an independent sample generated
from ξ. Find Qν(xν) = 1
ν
	ν
s=1 Q(xν, ξs) = 1
ν
	ν
s=1(πν
s )T (ξs −Txν). Let
Eν = 1
ν
	ν
s=1(πν
s )T T and eν = 1
ν
	ν
s=1(πν
s )T ξs.
Step 3. Update all previous cuts by Es ←
ν−1
ν Es and es ←
ν−1
ν es for
s = 1, . . . , ν −1.
Step 4. Solve the L-shaped master problem as in (2.5) to obtain xν+1. Go
to Step 2.
This method diﬀers slightly from the basic method in Higle and Sen
[1991b] in our assuming πν
s to be optimal dual solutions in each iteration.
Higle and Sen allow a restricted set of dual optima that may decrease the
solution eﬀort (with perhaps fewer eﬀective cuts).
The main convergence result is contained in the following theorem.
Theorem 3. Assuming complete recourse, Q(x, ξ) ≥0, bounded dual so-
lutions to (3.1.1), K1 and Ξ compact, there exists a subsequence, {xνj},
of the iterates of the basic stochastic decomposition method such that every
limit point of {xνj} solves the recourse problem (3.1.1) with probability one.
Proof: We follow the proof of Theorem 4 in Higle and Sen [1991b]. We use
their Theorem 3 (Exercise 5), which gives the existence of a subsequence
of {xν} such that
lim
ν→∞θν −max
l=1,...,ν(el
ν−1 −El
ν−1xν) = 0.
(2.12)
Suppose {xνj} is a subsequence of the subsequence achieving (2.12) such
that limj xνj = ˆx where Aˆx = b, x ≥0. This occurs for some subsequence
by compactness. From x∗optimal,
cT x∗+ Q(x∗) ≤cT ˆx + Q(ˆx).
(2.13)


## Page 360

10.2 Using Sampling in the L-Shaped Method
341
Note that because Q(x, ξ) ≥0 for all ξ ∈Ξ and Q(x, ξi) ≥πT (hi −Tx) for
any πT W ≤q and any sample ξi, for any 1 ≤s ≤ν,
ν

i=1
Q(x, ξi) ≥
s

i=1
πT (hi −Tx),
(2.14)
where π is any feasible multiplier in the recourse problem for ξi. From
(2.14), it follows that 1
ν
	ν
i=1 Q(x, ξi) ≥eν
l −Eν
l x for all l and ν, where Eν
l
and eν
l are the components of Cut l on Iteration ν. Therefore,
cT x + max
l=1,...,ν(eν
l −Eν
l x) ≤cT ˆx + 1
ν
ν

i=1
Q(x, ξi).
(2.15)
As ν increases, 1
ν
	
i=1ν Q(x, ξi) →Q(x), so
lim sup
ν
[cT x∗+ max
l=1,...,ν(eν
l −Eν
l x∗)] ≤cT x∗+ Q(x∗),
(2.16)
with probability one. We can also show that (Exercise 6)
lim
j cT xνj + max
l=1,...,ν(eν
l −Eν
l xνj) = cT ˆx + Q(ˆx),
(2.17)
with probability one. Thus, (2.16), (2.17), and the fact that xνj minimizes
cT x + maxl=1,...,ν−1(eν−1
l
−Eν−1
l
x) over feasible x yield
cT x∗+ Q(x∗)≤cT ˆx + Q(ˆx)
≤lim sup
ν
[cT x∗+ max
l=1,...,ν(eν
l −Eν
l x∗)] ≤cT x∗+ Q(x∗),(2.18)
which proves the result.
One diﬃculty in this basic method is that convergence to an optimum
may only occur on a subsequence. To remedy this, Higle and Sen suggest
retaining an incumbent solution that changes whenever the objective func-
tion falls below the best known value so far. The incumbent is updated each
time a suﬃcient decrease in the νth iteration objective value is obtained.
They also show that the sequence of incumbents contains a subsequence
with optimal limit points, and then show how this subsequence can be iden-
tiﬁed. Various approaches may be used for practical stopping conditions,
such as the statistical veriﬁcation tests for optimality conditions in Higle
and Sen [1991a].
Example 2 (continued)
We again consider Example 1 from Section 9.2. The basic stochastic de-
composition method results appear in Figures 3 and 4. In Figure 3, both
the basic result xν and the incumbent solution, xν(incumbent), which is


## Page 361

342
10. Monte Carlo Methods
adjusted whenever a solution after the ﬁrst 100 iterations improves the
previous best estimate by 1%. Figure 3 also gives the optimal solution, x∗.
The total number of iterations yields about 50,000 subproblem solutions,
which is approximately equal to the total number of iterations in Figures 1
and 2. Note that the raw solutions xν oscillate rapidly, while the incumbent
solutions settle close to x∗quite quickly after their initiation at ν = 100.
The objective value estimates, θν, Qν, and Qν(xν(inc)) for the incum-
bent, and the optimal objective value, Q(x∗), appear in Figure 4. Note that
the θν values from the master problem have wide oscillations. The Qν(xν)
values have lower but signiﬁcant variation. The incumbent objective values,
however, show low variation that begins to approach the optimum.
FIGURE 3. Solutions for the stochastic decomposition method.
Exercises
1. Prove Theorem 3. Show ﬁrst that eventually the objective value of
(2.5) for xνn at iteration νn is the same as the objective value of (2.5)
for xνn at iteration νn−1.
2. Show how to sample from the density gx(ξ) as the sum of the absolute
values |x −ξi|, i = 1, 2 for Example 2.


## Page 362

10.3 Stochastic Quasi-Gradient Methods
343
FIGURE 4. Objective values for the stochastic decomposition method.
3. Consider Example 1 in Section 5.1 with ξ uniformly distributed on
[1, 5]. Apply the crude Monte Carlo L-shaped method to this problem
for 100 iterations with 100 samples per cut. What would the result
be with importance sampling in this case?
4. Apply both the crude Monte Carlo and importance sampling ap-
proaches to Example 3 of Section 9 with both x1 and x2 decision
variables. First, use 100 samples for each cut for 100 iterations and
then compare to results with an increase to 500 samples per cut.
5. Prove that there exists a subsequence of iterates {xν} in the basic
stochastic decomposition method with the assumptions so that (2.12)
holds.
6. Suppose a subsequence of iterates xνj →ˆx in the basic stochastic
decomposition method. Prove that (2.17) holds.
7. Apply the basic stochastic decomposition method to Example 1 in
Section 5.1 with ξ uniformly distributed on [1, 5]. Record the sequence
of iterations until 10 consecutive iterations are within 1% of the op-
timal objective value.
10.3
Stochastic Quasi-Gradient Methods
Stochastic quasi-gradient methods represent one of the ﬁrst computational
developments in stochastic programming. They apply to a broad class of


## Page 363

344
10. Monte Carlo Methods
problems and represent extensions of stochastic approximation methods
(see, e.g., Dupaˇc [1965] and Kushner [1971]). Our treatment will be brief be-
cause the emphasis in this book is on methods that exploit the structure of
deterministic equivalent or approximation problems. Ermoliev [1988] pro-
vides a more complete survey of these methods.
Stochastic quasi-gradient methods (SQG) apply to a general mathemat-
ical program of the form:
min
x∈X⊂ℜn go(x)
s.t. gi(x) ≤0, i = 1, . . . , m,
(3.1)
where we assume that each gi is convex. We suppose that an initial point,
xo ∈X, is given. The method generates a sequence of points, {xν}, that
converges to an optimal solution of (3.1).
Given a history at time ν, (xo, . . . , xν), the method selects function es-
timates, ηi(ν), and subgradient estimates, βi(ν), such that
E[ηi(ν) | (xo, . . . , xν)] = gi(xν) + ai(ν)
(3.2)
and
E[βi(ν) | (xo, . . . , xν)] + bi(ν) ⊂∂gi(xν),
(3.3)
where ai(ν), bi(ν) may depend on (xo, . . . , xν) but must satisfy
ai(ν) →0 and ∥bi(ν) ∥→0.
(3.4)
When bi(ν)̸ = 0, βi(ν) is called a stochastic quasi-gradient. Otherwise,
βi(ν) is a stochastic subgradient.
We ﬁrst consider the method when all constraints are deterministic and
represented in X. Thus, Problem (3.1) becomes
min
x∈X⊂ℜn go(x).
(3.5)
The method requires a projection onto X represented by
ΠX(y) = arg min
x {∥x −y ∥2| x ∈X}.
In the basic method, a sequence of step sizes {ρν} is given. The stochastic
quasi-gradient method deﬁnes a stochastic sequence of iterates, {xν}, by
xν+1 = ΠX[xν −ρνβo(ν)],
(3.6)
where we interpret the projection as operating separately on each element
ω ∈Ω, so that xν+1(ω) = ΠX[(x(ω)ν −ρνβo(ω)(ν))].
To place all these results into the two-stage recourse problem as in (1.1.2),
let X = {x|Ax = b, x ≥0}, go(x) =

go(x,ξ)P(dξ) where
go(x,ξ) = inf
y {qT y | Wy = h −Tx, y ≥0}.


## Page 364

10.3 Stochastic Quasi-Gradient Methods
345
Thus, we can use βi
0(x) such that βi
0(x)T (hi −Tix) = go(x,ξi),βi
0(x)T ω ≤
qi for a sample ξi composed of the components, hi, Ti, and qi. The stochas-
tic quasi-gradient method takes a step in this direction and then projects
back onto K1. In the following example and the exercises, we explore the
use of this approach.
For these examples, we use an estimate of the objective value by taking
a moving average of the last 500 samples, Qν−ave(xν) = 	499
i=0 Q(xν −i,
ξν−i)/500. Changes in this estimate (or the lack thereof) can be used to
evaluate the convergence of stochastic quasi-gradient methods. Gaivoronski
[1988] discusses various practical approaches in this regard.
Example 2 (continued)
We consider the same example and apply the stochastic quasi-gradient
method. On each step ν, a random sample ξν is taken with βo(ν) ∈
∇Q(xν, ξν). For X = {x|0 ≤x ≤1}, the projection operation yields
xν+1 = min(1, max(xν + ρνβo(ν), 0)). Figures 5 and 6 show these itera-
tions for solutions xν and objective estimates, Qν−ave for every multiple
of 500 iterations up to 50,000 so that total numbers of recourse problem
solutions are the same as in Figures 1 to 4.
FIGURE 5. Solutions for the stochastic quasi-gradient method.


## Page 365

346
10. Monte Carlo Methods
FIGURE 6. Objective values for the stochastic quasi-gradient method.
Note that the iterations in Figure 5 appear to approach x∗much more
quickly than the results in Figures 1 to 4. They also seem to show lower
variances in the objective estimates in Figure 6, although these results
are not converging to zero variance because the sample length 500 is not
changing. To achieve convergence or greater conﬁdence in a solution, the
number of samples in the estimate must increase.
While the results in Figures 5 and 6 indicate that stochastic quasi-
gradient methods may be more eﬀective than the decomposition methods,
we should note that this example is quite low in dimension. For higher
dimensions, the results are often quite diﬀerent. In general, stochastic
quasi-gradient methods exhibit similar behavior to subgradient optimiza-
tion methods that often have slow convergence properties in higher dimen-
sion problems. They are, nonetheless, easy to implement and can give good
results, especially in small problems.
In the rest of this section, we discuss the theory behind the stochastic
quasi-gradient method convergence. The exercises consider examples for
using SQG.
The basic method in (3.6) traces back to the unconstrained methods of
Robbins-Monro [1951]. The main device in demonstrating convergence of
{xν} to a point in X∗is the use of a stochastic quasi-Feyer sequence (see
Ermoliev [1969]), a sequence of random vectors, {wν}, deﬁned in (Ω, Σ, P)
such that for a set W ⊂ℜn, E[∥wo ∥2] < +∞, and any w ∈W,
E{∥w −wν+1 ∥2| wo, . . . , wν}
≤∥w −wν ∥2 +γν, ν = 0, 1, . . . ,


## Page 366

10.3 Stochastic Quasi-Gradient Methods
347
γν ≥0,
∞

ν=0
E[γν] < +∞.
(3.7)
The following result shown in Ermoliev [1976] is the basis for the conver-
gence results.
Theorem 4. If {wν} is a stochastic quasi-Feyer sequence for a set W,
then
(a) {∥w −wν+1 ∥2} converges with probability one for any set w ∈
W, and E[∥w −wν ∥2] < c < +∞,
(b) the set of limit points of {wν(ω)} is nonempty for almost all
ω ∈Ω.
(c) if ¯w1(ω) and ¯w2(ω) are two distinct limit points of {wν(ω)}
such that ¯w1(ω)̸ ∈W, ¯w2(ω)̸ ∈W, then W ⊂H, a hyperplane
such that η = {w | αT w = α0}, ∥¯w1(ω) −Πη( ¯w1(ω)) ∥= ∥
¯w2(ω) −Πη( ¯w2(ω)) ∥, where Πη denotes projections onto η.
We can now state the most basic convergence result.
Theorem 5. Given the following:
(a) go(x) is convex and continuous,
(b) X is a convex compact set,
(c) the parameters, ρν, and γ0(ν) =
inf
x∗∈X∗β0(ν)T (xν −x∗), satisfy
with probability one,
ρν > 0,
∞

ν=0
ρν = +∞,
∞

ν=0
E[ρν | γ0(ν) | +
(ρν)2 ∥β0(ν) ∥2] < ∞,
(3.8)
then, with probability one, for any ¯x(ω) = lim
νi xνi(ω), ¯x(ω) ∈X∗.
Proof: First note that for −u(ω) ≡xν(ω)+ρνβν
0 (ω)−xν+1(ω), uT (ω)(xν+1(ω)−
x) ≤0 for any x ∈X by the nearest point property (see, e.g., Bazaraa and
Shetty [1979, Theorem 2.3.1]).
We can write
∥x∗−xν+1 ∥2 = ∥x∗−xν ∥2 −2ρνβνT
0 (x∗−xν)
+ρν2 ∥βν
0 ∥2 −2uT (x∗−xν −ρνβν
0) + uT u,
(3.9)
where uT (x∗−xν −ρνβν
0) = uT (x∗−xν+1) + uT u. Thus,
∥x∗−xν+1 ∥= ∥x∗−xν ∥2 −2ρνβνT
0 (x∗−xν)


## Page 367

348
10. Monte Carlo Methods
+ρν2 ∥βν
0 ∥2 −2uT (x∗−xν+1)
−uT u
≤∥x∗−xν ∥2 −2ρνβνT
0 (x∗−xν)
+ρν2 ∥βν
0 ∥2 .
(3.10)
Taking expectations in (3.10) yields
E
)
∥x∗−xν+1 ∥
*
≤E
)
∥x∗−xν ∥2*
−2ρνE[βνT
0 (x∗−xν)]
+ρν2E
)
∥βν
0 ∥2*
,
(3.11)
≤E
)
∥x∗−xν ∥2*
+ νE
)
(ρν | γ(ν) | +(ρν)2) ∥βν
0 ∥)
*
,
where ν is a constant. Now (3.11) implies that {xν} is a stochastic quasi-
Feyer sequence for X∗. Applying Theorem 4, we have ∥x∗−xν+1 ∥2
converging with probability one for any x∗∈X∗and {xν} almost always
has a limit point. We just need to show that one limit point is in X∗by
Theorem 4c.
To show this, note that
E
)
∥x∗−xν+1 ∥2*
≤E [∥x∗−xo ∥] + 2E
" ν

ν=0
ρi(β0(i)T (x∗−xi))
#
+ν
ν

i=0
Eρ2
i ∥β0(i) ∥2
≤E [∥x∗−xo ∥] + 2E
" ν

i=0
ρν(go(x∗) −go(xi))
#
+ν
ν

i=0
E
)
ρi | γ(i) | +ρ2
ν ∥β0(i) ∥2*
,
(3.12)
where we note that go(x∗) ≤go(xi). Hence
∞

i=0
go(xi) −go(x∗) < ∞, or
there must exist a subsequence {xνi} such that xνi(ω) →xi ∈X∗for
almost all ω ∈Ω.
The general method can be ampliﬁed in a variety of ways. Condition (c)
can be relaxed to remove the ﬁniteness of
∞

ν=0
ρ2
ν when γ(ν) = 0 for all ν,
but the convergence is for

ν xνρν

ν ρν
(see Uriasiev [1988]).
Two important aspects of stochastic quasi-gradient implementations are
the determinations of step sizes and stopping rules. Various adaptive step


## Page 368

10.4 Sampling Extensions with Analytical and Empirical Observations
349
sizes are considered by Mirzoachmedov and Uriasiev [1983]. For stopping
rules, we refer to Pﬂug [1988], where details appear.
The results describe the use of stopping times {τǫ}, to yield uniform
asymptotic level α conﬁdence regions, deﬁned by
lim
ε→0 inf
x0 P{∥xτǫ −x∗∥≤ε} ≥1 −α.
(3.13)
Deterministic step size rules do not, unfortunately, produce such uniform
conﬁdence intervals. Instead, Pﬂug shows that an oscillation test stopping
rule does obtain such conﬁdence regions. In this rule, a test is performed to
check whether the iterates are oscillating without objective improvement.
The key is building consistent estimates of the objective Hessian at x∗
and the covariance matrix of objective errors. For other issues concerning
implementation, we refer to Gaivoronski [1988].
Exercises
1. Consider Example 1 in Section 5.1. Find the projection of a point
onto X = {x|0 ≤x ≤10}. Solve this problem using the stochastic
quasi-gradient method until 20 consecutive iterations are within 1%
of the optimal solution.
2. Consider Example 2, where both x1 and x2 can be chosen instead of
x = x1 = x2. Follow the stochastic quasi-gradient method again until
20 consecutive iterations are within 1% of the optimal solution.
3. Prove Theorem 4.
4. Consider Example 1 in Section 5.1. Find the projection of a point
onto X = {x|0 ≤x ≤10}. Solve this problem using the stochastic
quasi-gradient method until three consecutive iterations are within
1% of the optimal solution.
10.4
Sampling Extensions: Uses with Analytical
and Empirical Observations
Monte Carlo sampling procedures can be enhanced by including some forms
of analytical computations or allowing for empirical sampling to improve
distribution information. These approaches have a wide variety of uses in
probabilistically constrained problems. The goal is to produce eﬃcient es-
timates of probabilities that involve multidimensional integrals with useful
decompositions. In general, the goal is to use problem structure to obtain
signiﬁcant decreases in sample variance. Various approaches have been sug-
gested. As examples, we refer to De´ak [1980], Gassmann [1988], and Sz´antai
[1986].


## Page 369

350
10. Monte Carlo Methods
We brieﬂy describe Sz´antai’s method here. The basic idea is to use
Bonferroni-type inequalities to write the probability of a set with many
constraints in terms of sums and diﬀerences of integrals of subsets of the
constraints, as we described in Section 9.5. In sampling procedures, these
alternative estimates allow for signiﬁcant variance reduction.
For Sz´antai’s approach, suppose we wish to ﬁnd
p = P[A = A1 ∩. . . ∩Am] =

A
dF(ξ).
(4.1)
Sz´antai takes three estimates of p:
1. ˆp1—a direct Monte Carlo sample;
2. ˆp2—ﬁnding the ﬁrst-order Bonferroni terms, 1 −
m

i=1
P( ˆAi), directly
and sampling from higher-order terms;
3. ˆp3—Calculating the ﬁrst- and second-order terms explicitly, 1 −
m

i=1
P( ˆAi) +

i<j
P( ˆAi ∩ˆAj), and sampling from higher order terms.
Sampling from all higher order terms may be diﬃcult, but Sz´antai shows
that the eﬀort may be reduced at each sample ξj to ﬁnding ˆn(j) deﬁned
as the number of constraints violated by ξj, i.e., ˆn(j) =
N

i=1
1{ξj̸∈Ai}. With
this quantity deﬁned, we can deﬁne unbiased estimates, i.e., estimates whose
expectations have no error, using the following:
γ1 = 1
ν
ν

j=1
max{0, 1 −ˆn(j)},
(4.2)
γ2 = 1
ν
ν

j=1
max{0, ˆn(j) −1},
(4.3)
and
γ3 = 1
ν
ν

j=1
max{0, ˆn(j) −1}ˆn(j) −2)
2
.
(4.4)
These quantities are then used to form unbiased estimates:
ˆp1 = γ1,
(4.5)
ˆp2 = 1 −
m

i=1
P[ ˆAi] + γ2,
(4.6)


## Page 370

10.4 Sampling Extensions with Analytical and Empirical Observations
351
ˆp3 = 1 −
m

i=1
P[ ˆAi] +

i<j

P[ ˆAi ∩ˆAj] −γ3.
(4.7)
These three estimators are combined to form
ˆp4 = λ1ˆp1 + λ2ˆp2 + (1 −λ1 −λ2)ˆp3,
(4.8)
where the weights λ1 and λ2 are chosen to minimize the variance of ˆp4. They
are calculated using the sample covariance matrix of (γ1, γ2, γ3), which we
denote as C = [cij]. In this case, λ1 =
µ1
µ1+µ2+µ3 , λ1 =
µ2
µ1+µ2+µ3 , where
µ1 = c12(c33 −c23) + c22(c13 −c33) + c23(c23 −c13),
(4.9)
µ2 = c11(c23 −c33) + c12(c33 −c13) + c13(c123 −c23),
(4.10)
and
µ3 = c11(c23 −c22) + c12(c12 −c23) + c13(c22 −c12).
(4.11)
The result is that ˆp4 can have signiﬁcantly lower variance than standard
Monte Carlo. In fact, Sz´antai obtains eﬃciencies (variance ratios) of 100
and higher, implying that the same error can be obtained with ˆp4 in 1% of
the number of samples for using ˆp1 alone.
This approach combines analytical techniques with simulation to produce
lower variance. Another approach is to use empirical sample information.
This is the area studied in Jagganathan [1985], where some sample infor-
mation can be used in a Bayesian framework to determine probabilities of
underlying distributions. These may be used for probabilistic constraints,
for recourse functions, or for both.
As an example, consider the basic two-stage model in (3.1.1), where the
distribution function of ξ is F(ξ,η), where η is a k-vector of unknown
parameters with prior distribution function, G(·). Given an observation,
ˆξl = (ξ1, . . . , ξl), we can deﬁne a posterior distribution, Gl(·|ˆξl). Using
this, we may obtain an improved solution.
Without sample information, we would have the solution to (3.1.1) as
R(G) = min
x∈K1{cT x +

η

ξ
Q(x,ξ)F(ξ,η)G(dη)}.
(4.12)
However, using ˆξ
l, which we assume has a conditional distribution given by
W(ˆξ
l, η) for some value η of η, we obtain a value with sample information
as
Rl(G) =

η
[ min
x∈K1{cT x +

η

ξ
Q(x,ξ)F(dξ,η)Gl(dη|¯ξl)}]W(dˆξ
l,η)G(dη).
(4.13)


## Page 371

352
10. Monte Carlo Methods
The diﬀerence Rl(G) −R(G) is the expected value of sample information.
This represents the additional expected value from observing the sample
information. This type of analysis can also be extended to problems with
probabilistic constraints.
A diﬀerent use of sample information is for dynamic problems that may
change over time. In these cases, future characteristics, such as product de-
mand, may not be known with certainty but they can be predicted roughly
using past experience. These problems were examined by Cipra [1991], who
also considered the possibility that more recent information might be more
valuable than older information.
For example, consider the news vendor problem in Section 1.1. Suppose
the demand occurs as ξt for periods t = 1, . . . , H. At time H, suppose that
ξH = (ξ1, . . . , ξH) have been observed. The news vendor wishes to place an
order based on these observations. One solution might be to use a discount
factor, β ∈(0, 1), to choose x(H) to
min
x≥0(
H−1

i=0
βi((a −s)x + (s −r)(x −ξH−i)+)).
(4.14)
The solution of this problem is straightforward (Exercise 5). Alternative
perspectives on the value of empirical observations can also be introduced,
as could Bayesian approaches as in (4.13). For another view of decisions
made over time, refer to Jagganathan [1991].
Exercises
1. Show that ˆpi are unbiased estimators of the probability p in (4.1).
2. Suppose that γi, i = 1, 2, 3, are independent standard gamma random
variables with parameters, ηi, i = 1, 2, 3. Let xi = γ1 + γi+1 for
i = 1, 2. Give a one dimensional integral that represents P[xi ≤
wi, i = 1, 2] using cumulative gamma distribution functions in the
integrand.
3. The result in Exercise 2 allows calculations of ˆp2. For example, sup-
pose that yi, i = 1, 2, 3, 4 in Exercise 2 and xi = y1 + yi+1 for
i = 1, 2, 3. Find ˆp4 for p = P[xi ≤zi, i = 1, 2, 3] when zi = 6,
i = 1, 2, 3, and ηi = 3, i = 1, 2, 3, 4. Also, ﬁnd sample variances for
increasing sample sizes and compare to the sample variances for ˆp1.
4. Suppose that ξ is known to take on a ﬁnite number K of possible
values but the probabilities ηi of these values are not known but have
a Dirichlet prior distribution. Show how to ﬁnd R(G) and Rl(G) in
this case.
5. Find the solution to (4.14). (Hint: Order the observed demands.)


## Page 372

11
Multistage Approximations
Most decision problems involve eﬀects that carry over from one time to an-
other. Sometimes, as in the power expansion problem of Section 1.3, random
eﬀects can be conﬁned to a single period so that recourse is block separa-
ble. In other cases, however, this separation is not possible. For example,
power may be stored by pumping water into the reservoir of a hydroelec-
tric station when demand is low. In this way, decisions in one period are
inﬂuenced by decisions in previous periods.
Problems with this type of linkage among periods are the subject of
this chapter. We again wish to derive approximations that can be used to
bound the error involved in any decision based on the approximate problem
solution. In Chapter 10, we saw that the number of random variables can
lead to rapidly growing problems. In this chapter, we have the additional
eﬀect that the number of periods leads to exponential increases in problem
size even if the number of realizations in each period remains constant (see
Figure 3.3).
We can again construct bounds based on the properties of the multistage
recourse functions. These analogues of the basic Jensen and Edmundson-
Madansky bounds are given in Section 1. They correspond to ﬁxing values
at means or extreme values of the support of the random vectors in each
period.
Keeping the number of periods ﬁxed may not lead to suﬃcient reductions
in problem size, especially if no time is clearly the end of the problem. This
case would mean facing either an uncertain or an inﬁnite horizon decision
problem. These problems can also be approximated by aggregating several


## Page 373

354
11. Multistage Approximations
periods together. Section 2 describes this procedure to obtain both upper
and lower bounds.
The bounds of Sections 1 and 2 can all be viewed as discretization
procedures. We can also construct separable bounds that do not require
discretization as in Chapter 9. These bounds correspond to separable re-
sponses to any changes in the problem. They are described in Section 3.
In multistage problems, speciﬁc problem forms and structures can again
lead to substantial savings. We describe uses of the form of production
problems and vehicle allocation problems in Section 4.
11.1
Bounds Based on the Jensen and
Edmundson-Madansky Inequalities
The basic Jensen and Edmundson-Madansky inequalities can be extended
to multiple periods directly. The principle is to use Jensen’s inequality (or
a feasible dual solution) to derive the lower bound and construct a fea-
sible primal solution using extreme points to construct the upper bound.
To present these results, we consider the linear case ﬁrst, although exten-
sions to nonlinear, convex problems are directly possible. We use concepts
from measure theory in the following discussion. Readers without this back-
ground may skip to the declarations to ﬁnd the major results for actual
implementations.
The multistage stochastic linear program is to ﬁnd x = (xT
0 , xT
1 , . . . , xT
H)T
to
min cT
0 x0 + EΩ[cT
1 x1 + · · ·+cT
HxH]
s. t. A0x0= b0,
Bt−1xt−1 + Atxt= ht,
t = 1, . . . , H, a.s.,
xt −EΩt[xt]= 0,
(1.1)
t = 1, . . . , H, a.s.,
xt≥0,
t = 1, . . . , H, a.s.,
where we have used the explicit nonanticipativity constraints as in (3.5.9).
We have also assumed that the recourse within each period At is known
and not random.
The basic Jensen bound again follows by assuming a partition of Ω, the
support vector of all random components. Here, we write Ωas Ω= Ω1×· · ·×
ΩH. We suppose that Ωt = {ωt = (ω1, . . . , ωt)|ωi ∈Ωi, i = 1, . . . , t}. In this
way, we can characterize all events up to time t by measurability with re-
spect to the Borel ﬁeld deﬁned by Ωt, Σt. We assume that Ωt is partitioned
as Ωt = St,1∪· · ·∪St,νt and that St,i = ∪j∈Dt+1(i){ωt|(ωt, ωt+1) ∈St+1,j} so


## Page 374

11.1 Bounds Based on the Jensen and Edmundson-Madansky Inequalities
355
that the partitions are consistent from one period to another. We construct
measurable decisions at time t if they are constant over each St,j.
Next, assume that pt,i = P[St,i], ct = ct, and that ESt,i[(ht, Bt)] =
(¯ht,i, ¯Bt,i) for all t and i. The problem then is to ﬁnd:
min cT
0 x0 +
ν1

i=1
p1,icT
1 x1,i + · · ·+
νH

i=1
pH,icT
HxH,i
s. t. A0x0= b0,
¯Bt−1,ixt−1,i + Atxt,j= ¯ht,j,
t = 1, . . . , H,i = 1, . . . , lt−1,
(1.2)
j ∈Dt+1(i),
xt,i≥0,
i = 1, . . . , νt,t = 1, . . . , H.
The ﬁrst result is that (1.2) provides a lower bound on the optimal solution
in (1.1) provided the expectations of (¯ht,i, ¯Bt,i) are independent of the past.
If not, then the conditional expectation form in (1.2) may not actually
achieve a bound.
Theorem 1. Given that ESt,i[(ht, Bt)] = (¯ht,i, ¯Bt,i) = ESt,j[(ht, Bt)] for
all St,i and St,j that have a common outcome at time t, i.e., such that
(ωt−1, ωt) ∈St,j if and only if there exist some (ˆωt−1, ωt) ∈St,j. The
optimal value of (1.2) with the deﬁnitions given earlier provides a lower
bound on the optimal value of (1.1).
Proof: Suppose an optimal solution x∗to (1.2) with optimal dual variables
(π∗
t,i) corresponding to constraints in (1.2) with right-hand sides, ¯ht,i (b0 if
t = 0). By dual feasibility in (1.2),
pt,ict ≥π∗T
t,i At +

j∈Dt+1(i)
π∗T
t+1,j ¯Bt+1,j,
(1.3)
for every (t, i). Let πt(ω) = 	νt
i=1 1ωt∈St,i[π∗
t,i/pt,i], where 1S(w) = 1
if w ∈S and 0 otherwise. We also have ρt(ω) = −	νt
i=1 1ωt∈St,i [π∗T
t,i
Bt,i(ω)/pt,i]+	
i′|i′∈Dt−1(At−1(i)[π∗T
t,i′ ¯Bt,i/pt−1,At−1(i)]. Note how the ρ vari-
ables represent nonanticipativity.
The condition for dual feasibility from the multistage version of Theorem
3.13 (see Exercise 1) is that
ct(ω) −πT
t (ω)At −πT
t+1(ω)Bt+1(ω) −ρt+1(ω) ≥0, a.s.,
(1.4)
and
EΣt[ρt+1(ω)] = 0.
(1.5)


## Page 375

356
11. Multistage Approximations
Substituting in the right-hand side of (1.4) yields:
ct −[π∗T
t,i /pt,i]At −[π∗T
t+1,j/pt+1,j]Bt+1,j(ω) + [π∗T
t+1,j/pt+1,j]Bt+1,j(ω)
−

j|j∈Dt(i)
[π∗T
t+1,j ¯Bt+1,j/pt,i]
(1.6)
for each St,i and j ∈Dt(i), which is non-negative from (1.3). Also, by their
deﬁnition and the assumption that integration of Bt+1,j(ω) over varying
St,i does not change its conditional outcome,
EΣt[ρt+1(ω)]=

j∈Dt(i)
[π∗T
t+1,j/pt+1,j] ¯Bt+1,jpt+1,j
−

j|j∈Dt(i)
pt,1[π∗T
t+1,j ¯Bt+1,j/pt,i] = 0
(1.7)
yielding (1.5). Hence, we have constructed a dual feasible solution whose
objective value is a lower bound on the objective value of (1.1) by the
multistage version of Theorem 3.13. Because this value is the same as the
optimal value in (1.2), we obtain the result.
Thus, lower bounds can be constructed in the same way for multistage
problems as for two-stage problems, provided the data have serial inde-
pendence. Such independence is not necessary if only right-hand sides vary
because the dual feasibility is not aﬀected in that case. The key procedure
is in developing a dual feasible solution (lower bounding support function).
Upper bounds can follow as before by constructing primal feasible solu-
tions. These bounds can also be used in conjunction with the lower bounds
to obtain bounds when objective coeﬃcients (ct) are also random.
To develop the upper bounds, the basic result is an extension of Theorem
9.2. We assume the following general form in which the decision variables
x are explicit functions of the random outcome parameters, ξ:
inf
x∈N EΞ[
T

t=0
ft(xt(ξ), xt+1(ξ),ξt+1)],
(1.8)
where the random vector ξ = (ξ1, . . . ,ξH+1) has an associated probability
space, (Ξ, Σ, P), N is the space of nonanticipative decisions, ft is convex,
and ξt+1 is measurable with respect to Σt+1 and ξt+1 ∈Ξt+1, which is
compact, convex, and has extreme points, extΞt, with Borel ﬁeld, Et+1. In
this representation, x nonanticipative means that xt(ξ(ω)) is Σt-measurable
for all t. It could also be described in terms of measurability with respect
to Σt, the Borel ﬁeld deﬁned by the history process ξt = (ξ1, . . . ,ξt).
Suppose that e = (e1, . . . , eH)T where each et ∈extΞt. The set of all
such extreme points is written extΞ. Suppose x′ = (x′
1, . . . , x′
H), where


## Page 376

11.1 Bounds Based on the Jensen and Edmundson-Madansky Inequalities
357
x′
t : extΞt →ℜnt. We say that x′ is extreme point nonanticipative, or
x′ ∈N ′, if x′
t is measurable with respect to the Borel ﬁeld, Et, on extΞ,
deﬁned by (e1, . . . , et), where ej ∈extΞj (for t = 0, this will be with respect
to {∅, extΞ}). With these deﬁnitions, we obtain the following result.
Theorem 2. Suppose that ξ →ft(xt, xt+1, ξt+1) is convex for t =
0, . . . , H, Ξt is compact, convex, and has extreme points, extΞt. For all
ξt ∈Ξt, let φ(ξ, ·) be a probability measure on (extΞ, E) where E is the
Borel ﬁeld of extΞ, such that

e∈extΞ
eφ(ξ, de) = ξ,
(1.9)
and ξ →φ(ξ, A) is measurable with respect to Σt for all A ∈Et. Then there
exists, x ∈N, such that xt(ξ) =

e∈extΞ x′
t(e)φ(ξ, de),
E[
T

t=0
ft(xt, xt+1,ξt+1)] ≤

e∈extΞ
T

t=0
ft(x′
t, x′
t+1, et+1)]λ(de),
(1.10)
where x′ is extreme point nonanticipative and λ is the probability measure
on E deﬁned by
λ(A) =

Ξ
ν(ξ, A)P(dξ).
(1.11)
Proof:
We must ﬁrst show that x as deﬁned in the theorem is nonantic-
ipative, or that xt(ξ) is Σt-measurable. This follows because x′
t(e) is Et-
measurable, and, for any A ∈Et, φ(ξ, A) is Σt-measurable. Because each
ft is convex, for any ξ,
ft(xt(ξ), xt+1(ξ), ξt+1) = ft(

e∈extΞ
x′
t(e)φ(ξ, de),

e∈extΞ
x′
t+1(e)φ(ξ, de),

e∈extΞ
et+1φ(ξ, de))
≤

e∈extΞ
ft(x′
t(e), x′
t+1(e), et+1)φ(ξ, de).
(1.12)
Integrating with respect to P, the result in (1.10) is obtained.
As in Chapter 9, we implement the result in Theorem 2 by ﬁnding an
appropriate φ and then solving the following approximation problem.
inf
x′∈N ′

extΞ
[
H

t=0
ft(xt(e), xt+1(e), et+1)]λ(de)
(1.13)
to ﬁnd an upper bound on the value in (1.8). One can also reﬁne these
bounds by taking partitions of Ξ.


## Page 377

358
11. Multistage Approximations
The simplest type of bound from Theorem 2 is the extension of the
Edmundson-Madansky bound on rectangular regions with independent
components. For this bound, we assume that all components, ξt(i), are
stochastically independent and distributed on [at(i), bt(i)]. In this case, we
can deﬁne
νEM−I(ξ, e) = ΠH
t=1Πmt
i=1
|ξt(i) −et(i)|
(bt(i) −at(i)),
(1.14)
so that
λEM−I(e) = ΠH
t=1Πmt
i=1
|¯ξt(i) −et(i)|
(bt(i) −at(i)).
(1.15)
It is easy to check that this ν meets the nonanticipative measurability
requirements. Problem 1.13 now can be written as:
inf
x [
H

t=0
(
I1

i1=1
· · ·
It+1

it+1=1
[
It+2

it+2=1
+ · · · +
IH+1

iH+1=1
λ(ei1, . . . , eiH+1)]
ft(xt(i1, . . . , it), xt+1(i1, . . . , it+1), eit+1)],
(1.16)
where xt(i1, . . . , it) corresponds to the tth-period decision depending on the
outcomes in extreme point combination eis from each period s = 1, . . . , H.
This places the nonanticipativity back into the problem implicitly.
Example 1
To see how this bound might be implemented, consider Example 1 in Sec-
tion 7.1. Suppose that demand is uniformly and independently distributed
on [1, 3] in each period. In this case, we obtain a decision vector (xt
s, wt
s, yt
s)
in period t for scenario s = 2i1 + i2 for i1 and i2 in {1, 2}. Problem (7.1.7)
is, therefore, the upper bounding problem (1.16) for this uniform distribu-
tion case, yielding an upper bound of 6.25. In this case, the lower bound
using the expected demand value of two in each period is three. In Exercise
2, you are asked to reﬁne these bounds until they are within 25% of each
other.
Other extreme point combinations are clearly also possible in multiperiod
problems as they are in single-period problems. Extensions to dependent
random variables and ft concave in some arguments can also be made.
The bounds given in this section so far apply only to ﬁxed numbers
of periods. When periods are combined, we call the resulting problem an
aggregated problem. These problems are described in the next section.
Exercises
1. Consider the multistage stochastic linear program in the form of (1.1).
Prove the multistage version of Theorem 3.13.


## Page 378

11.2 Bounds Based on Aggregation
359
2. Reﬁne the extreme point (Edmundson-Madansky) and conditional
expectation (Jensen) bounds on partitions for Example 1 from Section
7.1 until the upper bound is within 25% of the lower bound.
11.2
Bounds Based on Aggregation
The main motivation for aggregation bounds is to deal with problems with
many (perhaps an inﬁnite number of) periods by combining periods to ob-
tain a simpler approximate problem with fewer periods. The basic proce-
dures in this chapter appear in Birge [1985a] and Birge [1984]. They follow
the general aggregation results in Zipkin [1980a, 1980b]. Similar methods,
especially for dealing with inﬁnite horizon problems, appear in Grinold
([1976, 1983, 1986]). Generalizations appear in Wright [1994].
To derive both upper and lower bounds in this framework, we consider
a special form for the multistage problem in (3.5.1). We allow feasibility
by adding a penalty variable yt that can achieve feasibility in each period.
This notion of model robustness is quite common, although the penalty
parameter q may be quite high. The form of the multistage stochastic
linear program in this case is:
min z = cT x1 + Eξ[
H

t=2
ρt−1(cT xt(ξ2, . . . ,ξt)+qT yt(ξ2, . . . ,ξt))]
s. t. Wx1≥h1,
Txt−1(ξ2, . . . ,ξt−1) + Wxt(ξ2, . . . ,ξt) + yt(ξ2, . . . ,ξt)≥ξt,
t = 2, . . . , H,
x1 ≥0; xt(ω) ≥0, a.s.,t = 2, . . . , H,
yt(ω) ≥0, a.s.,t = 2, . . . , H,
(2.1)
where c is a known vector in ℜn1, h1 is a known vector in ℜm1, ξt(ω) =
ht(ω) is a random m-vector deﬁned on (Ω, Σt, P) (where Σt ⊂Σt+1) for
all t = 2, . . . , H, and T and W are known m×n matrices. We also suppose
that Ξt is the support of ξt. The parameter ρ is a discount factor.
Note that in (2.1), we assume that the parameters T, W, c, and q are
all constant across time (with objective coeﬃcients varying only with the
discount factor). This assumption is basically made to simplify the following
presentation. Varying parameters are possible with little additional work.
The key observation for these bounds is that an optimal solution in (2.1)
is no lower than
π1h1 + Eξ[
H

t=2
(πt(ξ2, . . . ,ξt))Tξt]
(2.2)


## Page 379

360
11. Multistage Approximations
for any (π1, . . . , πt(ξ2, . . . ,ξt), . . . , πT (ξ2, . . . ,ξT )) ≥0 a.s. that satisﬁes
(π1)T W + Eξ[π2(ξ2)]T T ≤cT ,
πt(ξ2, . . . ,ξt)T W + Eξ|(ξ2,...,ξt)[πt+1(ξ2, . . . ,ξt+1)]T T ≤ρt−1cT ,
t = 2, . . . , H −1,
π(ξ2, . . . ,ξH)T W ≤ρH−1cT ,
π(ξ2, . . . ,ξH)T W ≤ρH−1qT .
(2.3)
You are asked to show that (2.2) subject to (2.3) provides a bound in
Exercise 1.
The basic idea behind the aggregation bounds is that we can either con-
struct solutions (x, y) that are feasible in (2.1) or solutions π that are
feasible in (2.3). As before, the former provide upper bounds, while the
latter provide lower bounds.
The other assumption we make is that some set of ﬁnite upper bounds
exists in xt so that for any x∗optimal in (2.1):
x∗
t (ξ2, . . . ,ξt) ≤ut(ξ2, . . . ,ξt).
(2.4)
In most problems, some form of bound satisfying (2.4) can be found. The
tightness of this bound may, however, signiﬁcantly aﬀect the bounding
results.
The basic bound is ﬁrst to assume that the Jensen type of conditional
expectation bound has been applied in each period. We illustrate this with
a single partition, although ﬁner partitions are possible. We also collapse
everything into a two-period problem. Less aggregated models are con-
structed in the same way. Note in the following that H is quite arbitrary
and, assuming ﬁnite sums, could even be inﬁnite.
The problem is formed by deﬁning aggregate variables, ˆX1, ˆX2, and ˆY 2,
and parameters,
ˆW = (
H

t=2
ρt−2)W + (
H

t=2
ρt−2)T, ˆI = (
H

t=2
ρt−2I),
ˆc = (
H

t=2
ρt−1)c, ˆq = (
H

t=2
ρt−1)q, ˆξ = (
H

t=2
ρt−2 ¯ξt).
The resulting aggregate approximation problem is:
min cT ˆX1 + ˆcT ˆX2ˆqT ˆY 2
s. t. W ˆX1≥h1,
(2.5)
T ˆX1 + ˆW ˆX2 + ˆT ˆY 2≥ˆξ,
ˆX1, ˆX2, ˆY 2≥0.


## Page 380

11.2 Bounds Based on Aggregation
361
Suppose (2.5) has an optimal solution (X∗
1, X∗
2, Y ∗
w) with multipliers, Π∗.
These solutions are not directly feasible in (2.1) or (2.3), but feasible so-
lutions can be easily constructed from them. To do so, we need only let
ˆx1 = X∗
1, ˆxt(ξ2, . . . , ξt) = X∗
2 , and ˆyt(ξ2, . . . , ξt) = Y ∗
2 for all t and ξ. We
also let ˆπ1 = Π∗
1 and ˆπt(ξ2, . . . , ξt) = ρt−2Π∗
2 for all t and ξ. In this way,
the value of (2.5) is the same as
ˆz = cT ˆx1 + EΞ[
H

t=2
ρt−1(cT ˆxt(ξ2, . . . ,ξt) + qT ˆxt(ξ2, . . . ,ξt))],
(2.6)
which forms the basis for our bounds. The result is contained in the fol-
lowing theorem.
Theorem 3. Let z∗be a ﬁnite optimal value for (2.1). Then
ˆz + ǫ+ ≥z∗≥ˆz −ǫ−,
(2.7)
where
ǫ−= −
H

t=2
n

j=1
[

Ξ
[min{ρt−1cj −ρt−2Π∗
2W·j −ρt−1Π∗
2T·j, 0}ut(j)(ξ)]P(dξ)]
and
ǫ+ =
H

t=2
n

j=1
[

Ξ
[max{−W·jX∗
2 −T·jX∗
2 −Y ∗
2 (j) + ξt, 0}ρt−1q(j)]P(dξ)].
The proof of this theorem is Exercise 2. The basic idea is to write out z∗
in terms of (x∗, y∗) and to add on ˆπt(ξ)T (ξt −Wx∗
t (ξ) −y∗
t −Tx∗
t−1(ξ))
terms, which are all nonpositive. This yields ǫ−. The upper bound comes
from showing that {ˆxt(ξ), ˆyt(ξ) + max{−W·jX∗
2 −T·jX∗
2 −Y ∗
2 (j) + ξt, 0}}
is always feasible in (2.1).
These bounds can be quite useful, but the penalty and variable bound
assumptions may not be apparent in many problems. Sometimes bounds on
groups of variables are possible and can be useful. In other cases, properties
of the constraint matrices can be exploited to obtain other bounds similar
to those in Theorem 3. Several of these ideas are presented in Birge [1985a].
Example 2
In production/inventory problems, these values are especially easy to ﬁnd,
as in Birge [1984]. Consider a basic problem of the form
min z
= Eξ[
H

t=1
ρt−1(−ctxt(ξ)+qtyt
+(ξ) + rtst(ξ))]


## Page 381

362
11. Multistage Approximations
s. t.
xt −st≤kt, a.s.,
wt−1 + xt −wt= 0, a.s.,
zt≥bt, a.s.,
yt−1
+
+ xt −yt
+= ξt, a.s.,
t = 1, . . . , H,
yt−1
+ , xt, st, wt≥0, a.s.;
t = 1, . . . , H;
yt
+, yt
−, xt, st, wt,all Σt measurable
t = 1, . . . , H,
(2.8)
where xt represents total production, st represents overtime production, wt
is cumulative production, bt is a lower bound to achieve a service reliability
criterion (see Bitran and Yanasse [1984]), ct, qt, and rt are cost parameters,
and ξt is the random demand.
For problems with the form in (2.7), it is possible to ﬁnd bounds on all
primal and dual variables for an optimal solution. These bounds can then
be used with Theorem 3. Exercises 3, 4, and 5 explore the aggregation
bounds in this context more fully.
Exercises
1. Verify that a non-negative π satisfying the conditions in (2.3) provides
a bound on (2.1)’s optimal value through (2.2).
2. Prove Theorem 3.
3. Find bounds on all optimal variable values in (2.7) as functions of
the parameters and previous realizations.
4. Using the bounds in (2.3), construct bounds based on Theorem 3
for a problem with four periods, uniform demand on [8000, 10, 000],
bt = t(9500), p = 19, h = 0.4, q = 9.5, ρ = 0.9, and k = 9000.
5. It is not necessary to take expectations before aggregating periods.
Using the example in (2.7), construct bounds with a two-period prob-
lem that uses a weighted sum of future demands in the ﬁrst period.
What type of stochastic program is this?
11.3
Bounds Based on Separable Responses
In this section, we extend the basic separable bounds presented in Section
9.5b to multistage problems. The main idea is to use the two-stage method
repeatedly to approximate the objective function by separable functions.
For linear problems, this leads to sublinear or piecewise linear functions
as in Section 9.5b. Functions without recession directions (e.g., quadratic


## Page 382

11.3 Bounds Based on Separable Responses
363
functions) would require some type of nonlinear (e.g., quadratic) function
that should again be easily integrable, requiring, for example, limited mo-
ment information (second moments for quadratic functions). We consider
the linear case (following Birge [1989]).
The goal is to construct a problem that is separable in the components
of the random vector. In each period t, a decision, xt, is made subject to
the constraints, Atxt = ξt −Bt−1xt−1, xt ≥0, where ξt is the realization of
random constraints and xt−1 was the decision in period t−1. The objective
contribution from this decision is cT
t xt. We can view this decision as a
response to the input, ηt = ξt −Bt−1xt−1. The period t decision, xt, then
becomes a function of this input, so xt(ω) becomes xt(ηt). Problem (2.2)
becomes
min cT
1 x1 + E[cT
2 x2(η2) + ... + cT
HxH(ηH)]
s. t. A1x1 = b1,
Atxt(ηt) = ηt,
t = 2, . . . , H, a.s.,
ηt = ξt −Bt−1xt−1(ηt−1),
t = 2, . . . , H, a.s.,
xt(η) ≥0, t = 1, . . . , H.
The optimization problem is to determine the correct response to ηt. The
two-stage method given in Section 9.5b gives a response that is separable
in the components of ξ = η2. In multiple stages, ξ is replaced by ηt for
period t. The response must consider future actions and costs, so it is no
longer simply optimization of the second-period problem.
The dimension of η = (η2, . . . ,ηH) makes direct solution diﬃcult in
general. An upper bound is, however, obtained for any feasible response,
i.e., decision vectors, xt(ηt), that satisfy Atxt(ηt) = ηt, xt(ηt) ≥0, a.s.,
where ηt = ξt −Bt−1xt−1(ηt−1) for all t. The two-stage method can be
used to obtain feasible responses that are separable in the components of
ηt, i.e., where xt(ηt) = 	
i xi
t(ηt(i)).
One choice is to let xi
t(ηt(i)) solve
min cT
t xt s. t. Atxt = ηt(i)e(i), xt ≥β,
(3.1)
where e(i) is the ith unit vector and β depends on choices for the other
xi
t. Program (3.1) is a parametric linear program in ηt(i). It is particularly
easy to solve if β = 0. In this case, xi
t(ηt(i)) is linear for positive and
negative ηt(i). We suppose this case and let the optimal solutions be x±i
t
when ηt(i) = ±1.
A solution can be obtained if we can ﬁnd the distribution of the ηt(i)
given responses determined by solutions of (3.1). The resulting problem to


## Page 383

364
11. Multistage Approximations
solve is
min c1x1 +
T

t=2
mt

i=1

ψi
t(ηt(i))P(dηt(i))
s. t. A1x1 = b1, x1 ≥0,
(SL)
where ψi
t(ηt(i)) = ctx+i
t ηt(i) if ηt(i) ≥0, and ψi
t(ηt(i)) = ctx−i
t (−ηt(i)) if
ηt(i) ≤0. Assuming that the distribution of ηt is known in this approxi-
mation, we can ﬁnd ηt+1. Initially, η2 = ξ2 −B1x1, which has the same
distributional form as ξ2. In general, ηt+1(j) is given by:
ηt+1(j) = ξt+1(j) −Bt(j, ·)[
mt

i=1
(x+i
t 1ηt(i)≥0 + x−i
t 1ηt(i)<0)(|ηt(i)|)]. (3.2)
Note that the values in (3.2) are linear functions of ηt on the regions where
ηt has constant sign. We can, therefore, construct ηt+1 as a function of ηt by
overlaying these linear transformations of random variables. For normally
distributed data, this may be possible because the transformation does
not aﬀect the distribution class. For other distributions, it is more diﬃcult.
Even in the normal case, however, we have diﬀerent distribution parameters
for all possible sign combinations of all random variables in previous period
inputs. Exponential growth of the calculations in the number of periods is
not avoided.
Because the approximation given earlier may be diﬃcult to compute
even with normal distributions, it may be necessary to approximate the
distribution of ηt+1 . We can use bounds on the P{ηt(i) ≥0} and on
the moments conditional on ηt(i) ≥or < 0. Given these values, moment
problems can be solved to calculate corresponding values for ηt+1 and to
bound ψi
t (see Birge and Wets [1989]). Any other bounds on the input
(Btxt) from period t to period t + 1 can also be used to obtain crude
bounds on the ψ values.
Note that certain problems, such as networks, may have very few nonze-
ros in the Bt(j, ·) term in (3.1) (because they have a close-to-simple recourse
structure). The random input vector ηt+1 may be easily calculable for these
problems.
Another looser but more implementable bound can be obtained by forc-
ing a feasible and separable response in all future periods depending on a
single random variable in the current period. This eliminates the problem
of characterizing the distribution of inputs to all periods. It does, however,
force a dependency in future periods that may increase the bound.


## Page 384

11.3 Bounds Based on Separable Responses
365
To develop this response function, let Xt(±i) be an optimal solution,
(xt, . . . , xH), (t > 1), to:
min
cT
t xt
+...
+cT
HxH
s. t.
Atxt
= ±ei,
Btxt
+At+1xt+1
= 0,
· · ·
...
AHxH
= 0,
xτ ≥0,
τ = t, . . . , H.
(3.3)
Now deﬁne
zi
t(ˆξt(i)) =

ξt−ˆξt(i)>0
{CT
t Xt(+i)(ξt(i) −ˆξt(i))
+

ξt−ˆξt(i)≤0
{CT
t Xt(−i)(−ξt(i) + ˆξt(i)),
where Ct = (ct, . . . , cH). An upper bound on the objective value of (3.1) is
obtained by solving the separable nonlinear program:
min
cT
1 x1
. . . + cT
HxH
+ 	
t
	
i(zi
t(ˆξt(i))
s. t.
A1x1
= b,
Btxt
+At+1xt+1
−ˆξt+1
= 0,
t = 1, . . . , H −1,
xt ≥0,
t = 1, . . . , H.
ˆξ ∈Ξ,
(3.4)
where Ξ is the support set of the random variables. Note that if we drop
the nonlinear term in the objective and replace ˆξ in the constraints with
a ﬁxed valued of E[ξ], then we can obtain a lower bound on the optimal
objective value in (3.1) (see Birge and Wets [1986]). We should note that
in some cases, we may not have a solution to (3.3) for ±ei but may only
have a solution for +ei, e.g. In this case, ˆξt+1(i) could be constrained to be
less than the minimum possible value of ξt(i).
In (3.4), we are solving to determine a centering point, ˆξ, that obtains
minimum cost if we assume the response to any variation from ˆξ is a solution
of (3.3). By allowing some variation of the choice of centering point, a “best”
approximation of this type is found. The value of (3.4) is an upper bound
because the composition of the xt solutions from (3.4) and the Xt values
used in the z terms yield a feasible solution for all ξ.
This procedure may also be implemented as responses to several scenar-
ios. In this case, the random vectors are partitioned as in Section 1. The
partitions may also be part of the higher-level optimization problem so that
in some way a “best” partition can be found.
The points used within the partitions may be chosen as expected values,
in which case the solution without penalty terms is again a lower bound


## Page 385

366
11. Multistage Approximations
on the optimal objective value. For an upper bound, this vector may be
allowed to take on any value in the partition.
The use of multiple scenarios enters directly into the progressive hedging
approach of Rockafellar and Wets (see Section 6.2). This can be used to
solve the top-level problem and to approach a solution that is optimal for a
given set of partitions and the piecewise linear penalty structure presented
here.
Computations are then restricted to optimizing separable nonlinear func-
tions subject to linear constraints. Implementations can be based on pre-
vious procedures (such as decomposition).
The basic framework for the upper bounding procedures given earlier is
to construct a feasible solution that is easily integrated. Other procedures
for constructing such feasible responses are possible. For example, Wallace
and Yan [1993] suppose two types of restrictions of the set of solutions
to obtain bounds. The ﬁrst is to suppose only a subset of variables is
used within a period, as, for example, with the penalty terms used for
aggregation bounds in Section 2. The other approach is to suppose that
all realizations from period to period must meet some common constraint
on values passed between periods. This procedure eﬀectively divides the
multistage problem into a sequence of two-stage problems. It appears to
work well on problems with many stages.
Exercise
1. Use the separable function approach and (3.4) to construct an upper
bound on Example 1 with uniform demand distributions.
11.4
Bounds for Speciﬁc Problem Structures
To achieve further improvements in bounding multistage stochastic pro-
grams requires taking advantage of the speciﬁc structure of the problem
considered. For Example 2 in Section 2, we considered a basic produc-
tion problem that allows the construction of bounds on optimal primal
and dual variables that can then be used in constructing optimal objective
value bounds as in (2.7). Other bounds and approximations using similar
production problem structures are also possible. We explore some of those
bounds developed by Ashford [1984], following Beale, Forrest, and Tay-
lor [1980], and Bitran and Yanasse [1984], and Bitran and Sarkar [1988].
These bounds can be viewed as extensions of the aggregation-type bounds
in Section 2.
Extensions of the separable approximation bounds in Section 3 for spe-
cially structured problems are also possible. We consider these possibilities


## Page 386

11.4 Bounds for Speciﬁc Problem Structures
367
in the context of vehicle allocation problems as developed by Powell [1988]
and Frantzeskakis and Powell [1990, 1993].
a. Production problems
The ﬁrst type of extension of the production problem we consider is the
model used in Ashford [1984] which is a slight generalization of (2.8). It is
also an extension of similar work by Beale, Forrest, and Taylor [1980] on a
production problem similar to (2.8). The model is to
min z
= Eξ[
T

t=1
(−ctxt(ξ)−qtyt(ξ))]
s. t. Atyt−1 + Btxt−yt ≤ξt, a.s.,
(4.1)
t = 1, . . . , H,
yt ≥lt, ut ≥xt ≥0, a.s.,t = 1, . . . , H,
where xt represents production and related variables and yt represents
the state (e.g., inventory) after realizing demands, ξt. Both variables are
bounded, although yt may only have trivial bounds. One upper bound
directly analogous to that in Theorem 3 can be constructed using this
structure (see Exercise 1).
A lower bound on the optimal value of (4.1) can be obtained simply
by substituting expected values for the random elements in (4.1). Ashford
also presents an improved lower bound, however, that forms the basis for an
approximation procedure. This bound consists of solving a reduced problem:
min zRED(G1, . . . , GH)
=
T

t=1
(−ctxt −qtyt)
s. t. Atyt−1 + Btxt −wt= ¯ξ
t, t = 1, . . . , H,
(4.2)
−yt −wt≤−ft(wt −lt),
t = 1, . . . , H,
ut ≥xt ≥0, a.s., t = 1, . . . , H,
where the Gt are mt-vectors of given distribution functions, Git, i =
1, . . . , mt, and ft = (f1t, . . . , fmt,t), with
fit(ηi) =
 −ηi
∞
(ηi + ζ)dGit(ζ),
(4.3)
for i = 1, . . . , mt.
The bound in (4.2) is chosen by ﬁrst determining the distribution func-
tion, Git. If G∗
t is the vector of distribution functions of Atyt−1,∗+Btxt,∗−
ξt for an optimal solution (y∗, x∗) of (4.1), then the following theorem holds.
Theorem 4. The solution zRED(G∗
1, . . . , G∗
H) provides a lower bound on
the optimal solution z∗in (4.1) and zRED(G∗
1, . . . , G∗
H) ≥z(¯ξ), the solution


## Page 387

368
11. Multistage Approximations
of the expected value problem, i.e., (4.1) with all random variables replaced
by their expectations.
Proof:
Exercise 2.
It is possible to make the approximation in (4.2) into a deterministic
equivalent of (4.1) if appropriate penalties are placed on the violation of
bound constraints on xt, but the calculation of this and of the bound given
by Theorem 1 requires information about the optimal solutions which is
not known. Another bound is, however, obtainable by substituting Gξ(t),
the distribution function vector, corresponding to (ξt −¯ξt) (see Exercise
3).This represents the beginning of an approximation when the ξt vectors
are normally distributed. The approximation successively estimates param-
eters of a normal approximation of the distribution of Atyt−1,∗+Btxt,∗−ξt
from t to t+1. This procedure continues until little improvement occurs in
this updating procedure. Computational results with this procedure show
signiﬁcant savings over dynamic programming calculations.
This process can be viewed as a form of dynamic programming ap-
proximation using the input to each period’s decisions as the quantity,
Atyt−1,∗+Btxt,∗−ξt. In this way, it is also similar to the response method
given in Section 3. An alternative approach is to build approximations of
the value function from period to period. One application to problems with
uncertainties in the Bt−1 matrix in (4.1) appears in Beale, Dantzig, and
Watson [1986]. The bounds developed by Bitran et al. follow these produc-
tion examples closely. The model is again of the form in (2.8).
b. Vehicle allocation problems
Vehicle allocation problems provide a diﬀerent problem structure that al-
lows speciﬁc bound construction. These problems can be represented as
multistage network problems with only arc capacities random. A formula-
tion would then be the same as (1.1). The matrices At correspond to ﬂows
leaving nodes in period t while Bt corresponds to ﬂow entering nodes in
period t + 1. The only exception is in the last period for which AH just
gathers ﬂow into ending nodes. For simplicity, this model assumes that all
ﬂow requires one period to move between nodes.
The xt(ij) decisions are then ﬂows from i in period t to j in period
t + 1. The randomness involves the demand from i to j in period t. We
assume that xt(ij) = xf
t (ij)+xe
t(ij), where xf
t (ij) represents full loads (or
vehicles) and xt(ij)e represents empty vehicles (assuming that fractional
vehicle loads are feasible). For demand of ξt(ij), we would have xf
t (ij) ≤
ξt(ij). The costs cf
t (ij) and ce
t(ij) then correspond to the unit values of
moving full and empty vehicles from i to j at t. The result is that vehicles
are conserved in (4.4). The decisions generally depend on the locations of
vehicles at any point in time.


## Page 388

11.4 Bounds for Speciﬁc Problem Structures
369
Frantzeskakis and Powell [1993] consider several alternative approxima-
tions of (4.4). First, one could solve the expected value problem to obtain
ˆxt values. These corresponding decisions can be used regardless of realized
demand (as, e.g., in Bitran and Yanasse [1984]). Then the xt values could
be split into full and empty parts, xt = ¯xt, xf
t (ij) = max{¯xt(ij),ξt(ij)},
according to realized demand to produce both upper and lower bounds.
This could be viewed as a generalization of a simple recourse strategy;
hence Powell and Frantzeskakis refer to it as the simple recourse strategy.
Another approach is simply to solve the mean value problem, but only
actually to send a vehicle from i to j at t if there is suﬃcient demand. In
this way, xf
t (ij) = max{¯xt(ij),ξt(ij)}, but xt(ij) = xf
t (ij) whenever i̸ = j.
This strategy is called null recourse.
A further strategy is called nodal recourse, in which a set of decisions or
a policy, δt(i), is deﬁned for each node i at all times t. This policy would
be a list of options for ﬂow from i at t. The list would be a ranking of full
loads (i.e., preferred nodes, j1(i), . . . jk(i)) if capacity is available followed
by an alternative for any remaining empty vehicles.
This preference structure can be constructed using a separable approx-
imation from period t + 1 to H. In period H, we can begin by assigning
some salvage/ﬁnal value −cH(i) to vehicles on the arcs corresponding to
travel from one node to itself.
At period H −1, the value of sending a full load from i to j is simply
−cf
H−1(ij)−cH(j). Including empty loads in the obvious way and ordering
in decreasing orders for each p determines the strategy at H −1. Now, given
the distributions of ξH−1, these values yield an expected value function
for vehicles at i at t. The argument of this function is a state variable,
yH−1(i). With the function deﬁned, similar decisions on expected values of
loads from i to j can be made in period H −2. A dynamic programming
recursion would be to ﬁnd Qt(yt) = Eξt[Qt(yt,ξt)] where:
Qt(yt,ξt) =
min
xt,yt
−cT
t xt + Qt+1(yt+1)
s. t. Atxt = yt,
(4.4)
Btxt −yt+1 = 0,
ξt ≥xt ≥0.
If Qt+1(yt+1) is linear with coeﬃcients, ¯Qt+1(i) in each component i of
yt+1 as it is for t = H −1, then the optimal solution to (4.4) is given by
the increasing ordering of cf
t (ij)+ ˆQt+1(j) with each successive xf
t (ij) used
up to the minimum of yt(i) and ξt(ij) according to this realization of ξt.
The key is then to construct a linear approximation to Qt+1(yt+1).
With a linearization, the entire strategy can be simply carried back to
the ﬁrst period. Overall, this represents a feasible but not optimal strategy
because it avoids calculating the full nonlinear value of each yH−1(i). The
objective function values are not, however, calculated fully because of the
linearization.


## Page 389

370
11. Multistage Approximations
One way to compute a linearization is to assume an input value ˆyt(i) and
to ﬁnd the probability of each option multiplied by the expected linearized
value of that option. Using this to determine the recourse value at each
stage can lead to a lower bound at each stage and overall when the ﬁrst-
period problem is solved (see Exercise 4). An upper bounding linearization
is also possible. This is analogous to the Edmundson-Madansky approach
(Exercise 5).
Frantzeskakis and Powell [1993] mention that extensions of nodal re-
course can apply to general network problems. These procedures are similar
to the separable bounding procedures presented in Section 3. They again
rely on building responses to random variation that depend separately on
the random components and that are also feasible.
Other types of network structure can also yield bounds in speciﬁc cases.
For PERT networks (see, e.g., Taha [1992]), for example, a typical problem
is to balance the beneﬁts of early completion against the possible penalty
costs of exceeding a due date or promise date. In these problems, a nat-
ural separation occurs that allows calculation despite the interconnected
structure of paths and possibly correlated times. Klein Haneveld [1986]
considers bounds on expected tardiness penalties with mean constraints.
Maddox and Birge extend this analysis to bounds with second moment in-
formation (Birge and Maddox [1995, 1996]) and to bounding probabilities
of tardiness (Maddox and Birge [1991]).
The basic principle throughout this and Chapter 10 is to use convexity of
objective and constraints. Relax the problem and substitute expectations
properly to obtain a lower bound. Restrict the problem and maintain a
feasible solution (as perhaps a combination of extremal solutions) to obtain
an upper bound. Many more bounding approximations are possible based
on these fundamental observations.
Exercises
1. Let At+ be the matrix composed of the positive elements of At in
(4.1) (with zeros elsewhere). Use this to construct a bound on any
feasible dual variable value with βt = 	H
τ=t(+τ−1
s=t (As+)T )qτ, where
+t−1
s=t(As+)T = I. Combine this with Theorem 3 to obtain an upper
bound on the optimal objective value using the solution to the mean
value problem.
2. Prove Theorem 4.
3. Show that zRED(Gξ
1, . . . , Gξ
H) ≤z∗.
4. To construct a lower bound for nodal recourse, assume a projected
value, ˆyt(i) of yt(i) (as, e.g., an average of incoming and outgoing
loads). Find an expression (in terms of the demand distributions on


## Page 390

11.4 Bounds for Speciﬁc Problem Structures
371
the ranked full load alternatives) for the expected value (assuming
linearized future costs) of an additional vehicle beyond ˆyt(i). Show
that this procedure gives a lower bound on (4.4) when t = 1.
5. Show how an upper bounding linearization can be constructed for
(4.4) using a linearization of Qt+1(yt+1). (Note: You can assume a
constant number of total vehicles.)
6. Consider a three-period example with ﬁve total vehicles, three nodes
(cities), and salvage values, c3(1) = 2, c3(2) = 1, and c3(3) = 4.
Currently, two vehicles are at A, two vehicles are at B, and one vehicle
is at C. Suppose demand in each period is uniform on the integers
from zero to ξmax(ij), where ξmax(ij) has the following values:
To j =
1
2
3
From i =
1
0
2
3
2
2
0
2
3
3
3
0.
Suppose the costs (negative of proﬁts) on each route for a full truck
are
To j =
1
2
3
From i =
1
0
−1
−2
2
−1
0
−3
3
−2
−3
0.
Empty load costs are
To j =
1
2
3
From i =
1
0
1
2
2
1
0
3
3
2
3
0.
Use the lower and upper bounding procedures in Exercises 4 and 5
to construct upper and lower bounds on (4.4) for these data.


## Page 391



## Page 392

Part V
A Case Study
373


## Page 393



## Page 394

12
Capacity Expansion
This chapter presents a case study of a stochastic programming study for
a manufacturing ﬁrm. The study was to determine a method for allocating
capacity for diﬀerent products in diﬀerent plants. This process is known as
adding ﬂexible capacity. In general, ﬂexible capacity represents primarily
option value and cannot be evaluated by standard methods of discounting
cash ﬂows (see, e.g., Myers [1984]). Because of correlations among the ran-
dom variables, it is necessary to evaluate recourse actions, which are then
used in the analysis.
This chapter’s study is similar to the earlier study by Eppen, Martin,
and Schrage [1989] in terms of our development. We follow the same steps
although our risk characterization is somewhat diﬀerent from that of Eppen
and coworkers.
The chapter is divided into four sections. In the ﬁrst section, we describe
the model development and the use of an option value model perspective for
the evaluation of ﬂexible capacity. The second section describes the method
for approximating the distribution of the random variables. A key feature
here is that the distribution is not completely known so that methods based
on the moment problem solutions in Section 9.5 are necessary. The third
section compares solution methods for varying numbers of scenarios, while
the fourth section presents analysis of the results and suggestions for future
studies.


## Page 395

376
12. Capacity Expansion
12.1
Model Development
The manufacturer faces the situation of having certain plants with installed
capacity to produce speciﬁc products. The problem is to determine whether
additional capacity should be installed at a plant where no capacity for a
product currently exists. This additional capacity will allow the plant to
continue production if demand for the new product is higher than existing
capacity at other plants and if the demand for products at the new plant
is lower than the existing plant capacity.
As an example, consider Figure 1. Here, there are two products, A and
B, and three plants, 1, 2, and 3. The solid lines in the diagram indicate
that each plant currently produces only a single product. We could assume
that each of the plants is built to meet the mean demand exactly. In that
case, if demand for a product exceeds the mean, potential sales are lost.
FIGURE 1. Adding ﬂexible capacity at Plant 2.
By building additional capacity at Plant 2 for Product B (the dotted line
in Figure 1), if demand for product A is lower than the mean and demand
for product B is higher than its mean, then the excess Product B demand
can be produced at Plant 2 and fewer sales would be lost. That is the basic
goal of ﬂexible capacity. Other relevant measures (apart from net expected
value gains) are the use of the plants (the fraction of installed capacity
actually used) and the number of sales lost for each product type.
The decision problem is to trade oﬀthe costs of adding capacity against
the potential revenue from additional sales due to the extra capacity. As
mentioned in the introduction, this basic problem has been considered by
Eppen et al., who applied a mixed integer, stochastic linear programming
model. A more general study in the context of ﬂexible capacity appears in
Fine and Freund [1990].
The model considered here is the form used in the analysis by Jordan
and Graves [1991]. This model includes eight plants and sixteen products.
The original installed capacities for the products at each of the plants are
indicated in Figure 2. The total capacity in these plants and the expected
demands are given in Table 1.
Given this network characterization, the model is to determine where to
install additional capacity to maximize the value added to the ﬁrm by


## Page 396

12.1 Model Development
377
FIGURE 2. Original product-plant installed capacity.
TABLE 1. Total plant capacities and expected demands.
Plant
Capacity
Product
Mean
Product
Mean
Demand
Demand
(1000s)
(1000s)
(1000s)
1
380
A
320
I
140
2
230
B
150
J
160
3
250
C
270
K
60
4
230
D
110
L
35
5
240
E
220
M
40
6
230
F
110
N
35
7
230
G
120
O
30
8
240
H
80
P
180


## Page 397

378
12. Capacity Expansion
these capacity decisions. A standard net present value approach for this
is, however, inadequate. In such an approach, the expected revenue for a
capacity decision would be calculated and then discounted to the present
to determine a net present value. Diﬃculties with doing this, however,
are that the correlations among the products and other capacity decisions
make a sequential analysis of independent capacity decisions inadequate
and asymmetric revenue character of a ﬂexible capacity return does not
match the requirements for a net present value.
For this latter reasoning, consider Figure 3. In this ﬁgure, we show poten-
tial demand and expected revenues as linearly related so that each product
has some ﬁxed operating proﬁt (excluding ﬁxed capacity costs). The distri-
bution of the potential demand is also indicated in Figure 3. The result is
that revenues are not symmetric but are essentially truncated at the capac-
ity limit. With revenues of this form, a direct use of the capital asset pricing
model (see, e.g., Sharpe [1964]) to determine a discount factor cannot be
fully justiﬁed. Instead we need to use an option value approach. (For basic
background, see Jarrow and Rudd [1983]. A detailed explanation of the use
of options in capacity planning appears in Birge [1995].)
FIGURE 3. Demand and revenue relationship with limited capacity.
The diagram of returns in Figure 3 has the basic form of the position
diagram of holding an asset and selling a call option at the value of the
capacity. The call option would allow an investor to purchase the revenue
from potential sales at the ﬁxed price of the revenue from sales at full
capacity. The call, therefore, has value whenever the demand exceeds the
capacity.
With multiple products, the revenue from combinations of the sales
becomes a more complicated type of option (or, in general, contingency
claim), but it can still be evaluated. In some cases, in fact (see Andreou
[1990]), analytical formulas may exist to evaluate the beneﬁt of ﬂexible
capacity.


## Page 398

12.1 Model Development
379
Our general approach is to assume, as in the Black-Scholes model (see
Black and Scholes [1973] and Cox and Ross [1976]), that a riskless hedging
strategy is possible. This assumption requires the ability to trade both the
option and the underlying asset in perfectly divisible amounts. While such
a market is most likely not possible in all asset categories, it does appear
to represent a fairly consistent approximation of value calculations and is
used for the purposes here.
Given the risk-neutral assumption and other basic assumptions (see Jar-
row and Rudd [1983], Hull [1997]), an option value can be calculated by
assuming that the value of an option in a risk-neutral environment is the
same as an option value in a setting with risk. In this way, we can evaluate
the asset as if it grew at the riskfree rate and ﬁnd an option value under
this situation that will be equivalent to the option value in the situation
with risk aversion.
To carry out this analysis for the situation here, we must calculate the
current value of all potential sales (revenue from any potential demand
without capacity restrictions) and then assume that this value grows at the
riskfree rate. To do so, we would discount sales without capacity restriction
at a discount rate consistent with the total market risk (variance) of sales.
Suppose this rate is r; then revenue in time t is discounted by a factor ( 1
r)t.
Now, assuming risk neutrality, the value of these sales would increase at an
annual rate of rf, the riskfree rate.
The net eﬀect of these two adjustment is that the revenue from Period t
sales corresponds to a demand distribution that is shifted by a multiplier,
( 1+rf
1+r )t (see Figure 4). Note that if the capacity is high, the revenue eﬀect
is also just a shift by ( 1+rf
1+r )t, but this is now discounted at the riskfree
rate by (
1
1+rf )t. The original discount factor, ( 1
r)t, is then retained.
FIGURE 4. Demand distribution shift.
The more interesting eﬀect of this shift is when capacity is low. In fact, if
capacity is very low, the revenue is eﬀectively deterministic. In this case,


## Page 399

380
12. Capacity Expansion
when the demand distribution is shifted, it has no eﬀect on revenue. How-
ever, in this case, the revenues are again discounted with the riskfree factor,
(
1
1+rf )t. The result is that the low-capacity (and hence low-risk) revenue
stream is discounted at the riskfree rate.
This model clearly is consistent in these two extremes of abundant or very
limited capacity. When capacity limits some but not all potential revenue,
the eﬀect is a moderate discounting. In this way, risk can be captured in
terms of overall market eﬀect. Other risk measures, such as downside risk,
can also be used but generally require more complicated models.
In our model, instead of shifting the demand distribution and discounting
at the riskfree rate, it is often simpler to increase the capacity by multiply-
ing the capacity by ( 1+r
1+rf )t and then discounting with ( 1
r)t. This approach
is used in this example because fewer data needed modiﬁcation than would
be required with demand shifts. Capacities in the following formulations
are assumed to be adjusted in this way.
With this framework for assessing risk, we can now describe the stochas-
tic programming formulation of this model. The basic decisions are to deter-
mine whether to equip plants with new ﬁxtures. This decision corresponds
to determining whether a product is produced at a plant.
We describe the model in the AMPL formulation that appears in Figure
5. The “SETS” in that model are the names of the products and plants.
The parameters include the number of scenarios, the regular and overtime
capacity of the plants, the demand for each product under each scenario, the
cost of additional ﬁxtures for each product to be produced at each plant,
the capital budget, the operating proﬁt on each product, the additional
cost for overtime production, and the probabilities of the scenarios. We
represent discounting with an amortization factor. This factor is varied
according to the lifetime of each product.
The current model assumes that each product will be produced with
the same demand pattern through the same time horizon. The model also
assumes that capacity decisions only occur now and not in the future. In
this way, we essentially build a two-stage model although it may actually
encompass several periods of demand. In this way, sales in each period are
discounted by some factor ρ(H) that depends on the horizon length H
and the discount rate r. We divide the objective by γ(H) so that the ﬁrst-
stage decision is multiplied by amort =
1
γ(H) and the second-stage decision
corresponds to a single year’s revenues. This was again used to modify as
few data items as necessary.
The most fundamental decision is to determine where each prod-
uct may be produced. We designate this binary variable variable as
y(plant, product). The next variables determine regular and overtime pro-
duction of each product at each plant and in each scenario.
The objective to maximize is simply the expected revenues with a regular
operating proﬁt factor minus the additional costs for overtime production


## Page 400

12.1 Model Development
381
# This is a capacity planning model for assigning products to plants.
# SETS
set product;
set plant;
# PARAMETERS
param no scenarios;
param capacity{plant}; # CAPACITY OF PLANT
param ot capacity{plant}; # OVERTIME CAPACITY
param demand{product,1..no scenarios}; # DEMAND FOR PRODUCT
# UNDER SCENARIO
param cap cost{plant,product}; # CAPITAL COST
param cap budget; # CAPITAL BUDGET
param profit{product}; # PROFIT FROM EACH PRODUCT
param otcost{product}; # OVERTIME OPERATING COSTS
param prob{1..no scenarios}; # PROBABILITY OF SCENARIO
param amort; # AMORTIZATION FACTOR
#
var y{plant,product}¿= 0; # 1 = j IS PRODUCED AT i, 0 OTHERWISE
#integer y
var reg prod{plant,product,1..no scenarios}¿= 0; #REGULAR
# PRODUCTION
var ot prod{plant,product,1..no scenarios} ¿= 0; #OVERTIME
# PRODUCTION
# OBJECTIVE
maximize opt val:
- amort*cap cost[i,j]*y[i,j] + sum{i in plant} sum{j in product} sum{k in
1..no scenarios} (prob[k]*profit[j]*(reg prod[i,j,k] + ot prod[i,j,k])
- otcost[j]*prob[k]*ot prod[i,j,k])
;
# CONSTRAINTS
subject to
#
under bud{k in 1..no scenarios}:
sum{i in plant}sum{j in product} y[i,j]*cap cost[i,j] ¡= cap budget;
#
no gdemand{j in product, k in 1..no scenarios}:
sum{i in plant} (reg prod[i,j,k] + ot prod[i,j,k]) ¡= demand[j,k];
#
j atplant{i in plant,j in product, k in 1..no scenarios}:
(reg prod[i,j,k] + ot prod[i,j,k]) ¡= y[i,j]*(capacity[i]
+ ot capacity[i]);
#
r eq rcap{i in plant, k in 1..no scenarios}:
sum{j in product} reg prod[i,j,k] ¡= capacity[i];
#
ot eq otc{i in plant, k in 1..no scenarios}:
sum{j in product} ot prod[i,j,k] ¡= ot capacity[i];
FIGURE 5. AMPL model of capacity problem.


## Page 401

382
12. Capacity Expansion
and the stage-one capital costs. The constraints state that the capital ex-
penditure is under budget. They also limit production of speciﬁc products
by demand and plant capacity multiplied by the binary variable of whether
the product can be produced at a given plant. Total regular and overtime
production within a plant are also limited.
Given the model in Figure 5, the next problem is to determine the data to
drive the model. The basic assumption is that the data concerning costs and
operating proﬁts are relatively well known. Some variations might occur,
but it is generally decided that these changes can be accommodated by
varying the parameters after solving an initial model. The major driving
random factor is considered to be demand. Thus, much of the stochastic
modeling eﬀort considers demand scenario generation as described in the
next section.
12.2
Demand Distribution Modeling
Demand forecasting in this situation is a clear case of limited distribution
information. Historical data may exist on some older products but newer
product forecasts must be based on other techniques. In general, the level
of information is at most an expected value for demand on each product,
an estimate of a variance, and some general guidelines for correlation coef-
ﬁcients. No other distributional information would be available.
The general variance information followed Jordan and Graves [1991] in
assuming 40% of the expected demand as a standard deviation for a single
product demand. Correlation coeﬃcients were assumed to be 0.3 for prod-
ucts in groups, A–F, G–M, and N–P. For products from diﬀerent groups,
a 0.0 correlation coeﬃcient was assumed.
To accommodate this limited distribution information, the basic approx-
imation framework of a generalized moment problem as in Section 9.5 is
used. Instead of building a bound, however, the goal was to ﬁnd a ﬁxed a
number of points that match the given moments as closely as possible. The
basic generalized linear programming is used to ﬁrst pick the set of points
and then ﬁnd weights to minimize deviations from the moment values.
New points are generated by a local optimization procedure (which is not
necessarily optimal because the problem is not convex). Full optimization
of the scenario set is not considered necessary due to the lack of precision in
the moment estimates. The resulting solutions, with as few as six scenarios,
gives fairly consistent results, although fewer scenarios lead to some loss
of the hedging nature of the stochastic solution. Other types of sensitivity
analyses are described in Section 4.


## Page 402

12.4 Results and Extensions
383
TABLE 2. Capacity planning solution times.
Stages
Scenarios
Rows
Columns
OSL
ND-UM
(CPUs)
(CPUs)
2
4
478
966
4.7
1.7
2
8
894
1.8E03
11.9
2.5
2
16
1.7E03
3.5E03
35.4
3.6
3
36
4.4E03
9.0E03
230.7
15.2
3
256
2.8E04
5.7E04
12361
140.5
4
4096
4.5E05
9.2E05
Failed
5024
12.3
Computational Comparisons
For the computational experiments, the basic procedure uses the integer
programming capability of IBM’s OSL (IBM [1991]). This software enabled
solutions of relatively large capacity expansion models, although most anal-
yses considered the six-scenario problem in order to have relatively quick
turnaround times for varying parameter combinations on the RS6000 pro-
cessors.
The linear programming relaxations of the basic model in Figure 5 were
also solved using the nested decomposition method, ND-UM (Birge et al.
[1994]), which uses the OSL solver for each subproblem. Because the OSL
solver also follows the integer programming path, we only present the linear
programming times for varying numbers of scenarios. For this experiment
we also consider multiple-stage versions of the problem, although we did not
solve the integer versions of these multiple-stage stochastic programs. In
the multistage problems, the decisions in each period can consider previous
capacity installations with possible learning about the form of demand and
inventories carried from one period to the next. These interperiod ties mean
that block separability does not apply.
Table 2 indicates a clear advantage for decomposition in these problems.
The results on large problems represent orders of magnitude speed-ups over
the straightforward simplex method approach in OSL. While these results
do not occur in all practical problems, they are illustrative of the poten-
tial for special-purpose stochastic programming codes. The next section
considers the analysis of the solutions.
12.4
Results and Extensions
The solution process began by assuming a given value of the amortiza-
tion factor and then trying to establish a stable scenario set with which
the solution did not change as more scenarios are included. With this set


## Page 403

384
12. Capacity Expansion
established, the amortization factor was varied to observe possible eﬀects
from early product retirement or lengthy product lifetimes.
At high amortization factors, products have short lifetimes and little
incentive for ﬂexible capacity exists. In this model, only a single additional
capacity (J at 7) was added for amortization close to one. For amortizations
of one-half, two additional capabilities are added (P at 5 and G at 3). As
the amortization factor declines, more capacity is added. When amort is
0.2, a total of nine capacities are added. At amort= 0.1, 11 capabilities are
added.
These results, in some sense, rank the priority for adding additional ca-
pacity. This information was considered for the actual capacity decision.
Other factors are also considered to evaluate the capacity decision com-
pletely. The expected number of lost sales and expected utilizations are also
considered. These values give the decision makers more information about
the value of ﬂexible capacity. In general, ﬂexible capacity increases both
values. In this model, utilizations increased to 98% and lost sales declined
by 80% as ﬂexibility was added up to amortization factors of 0.1.
This model represents an important application of stochastic program-
ming in capacity planning. The actual model was provided to a manufac-
turer for use in evaluating the eﬀect of ﬂexible capacity. Some other exten-
sions, such as intermediate-stage capacity additions and variable product
lifetimes, could represent the actual situation more fully, but this simple
model gives much of the information used for actual decision making.


## Page 404

Appendix A
Sample Distribution Functions
This appendix gives the basic distributions used in the text. We provide
their means and variances.
A.1
Discrete Random Variables
Uniform: U[1,n]
P(ξ = i) = 1
n, i = 1, . . . , n, n ≥1,
with E[ξ] = n+1
2
and V ar[ξ] = n2−1
12 .
Binomial: Bi(n,p)
P(ξ = i) =

n
i

pi(1 −p)n−i, i = 0, 1, . . . , n; 0 < p < 1,
with E[ξ] = np and V ar[ξ] = np(1 −p).
Poisson: P(λ)
P(ξ = i) = e−λ λi
i! , λ > 0, i = 0, 1, . . . ,
with E[ξ] = λ and V ar[ξ] = λ.


## Page 405

386
Appendix A. Sample Distribution Functions
A.2
Continuous Random Variables
Uniform: U[0,a]
f(ξ) = 1
a, 0 ≤ξ ≤a, a > 0,
with E[ξ] = a
2 and V ar[ξ] = a2
12.
Exponential: exp(λ)
f(ξ) = λe−λξ, 0 ≤ξ, λ > 0,
with E[ξ] = 1
λ and V ar[ξ] = ( 1
λ)2.
Normal: N(µ,σ2)
f(ξ) =
1
√
2πσ2 e−(ξ−µ)2
2σ2 , σ > 0,
with E[ξ] = µ and V ar[ξ] = σ2.
Gamma: G(α, β)
f(ξ) =
1
β2Γ(α)ξα−1e
−ξ
β , α > 0, β > 0,
where Γ(α) =
 ∞
0
xα−1e−xdx, α > 0, E[ξ] = αβ and V ar[ξ] = αβ2.


## Page 406

References
[1] P.G. Abrahamson, “A Nested Decomposition Approach for Solving Stair-
case Linear Programs,” Ph.D. Dissertation, Stanford University (1983).
[2] S.A. Andreou, “A capital budgeting model for product-mix ﬂexibility,”
Journal of Manufacturing and Operations Management 3 (1990) pp. 5–23.
[3] K.M. Anstreicher, “A combined Phase I–Phase II projective algorithm for
linear programming,” Mathematical Programming 43 (1989) pp. 209–223.
[4] K.M. Anstreicher, “A standard form variant, and safeguarded linesearch, for
the modiﬁed Karmarkar algorithm,” Mathematical Programming 47 (1990)
pp. 337–351.
[5] K.M. Anstreicher, “Strict monotonicity and improved complexity in the
standard form projective algorithm for linear programming,” Mathematical
Programming 62 (1993) pp. 517–536.
[6] K.A. Ariyawansa and D.D. Hudson, “Performance of a benchmark par-
allel implementation of the Van Slyke and Wets algorithm for two-stage
stochastic programs on the Sequent/Balance,” Concurrency Practice and
Experience 3 (1991) pp. 109–128.
[7] R. Ashford, “Bounds and an approximate solution method for multi-stage
stochastic production problems,” Warwick Papers in Industry, Business and
Administration, No. 15, University of Warwick, Coventry, UK (1984).
[8] H. Attouch and R.J Wets, “Approximation and convergence in nonlinear
optimization” in: O.L. Mangasarian, R.R. Meyer and S.M. Robinson, Eds.,
Nonlinear programming, 4 (Academic Press, New York–London, 1981) pp.
367–394.


## Page 407

388
References
[9] M. Avriel and A.C. Williams, “The value of information and stochastic
programming,” Operations Research 18 (1970) pp. 947–954.
[10] E.R. Barnes, “A variation on Karmarkar’s algorithm for solving linear pro-
gramming problems,” Mathematical Programming 36 (1986) pp. 174–182.
[11] M.S. Bazaraa and C.M. Shetty, Nonlinear Programming: Theory and Algo-
rithms (John Wiley, Inc., New York, NY, 1979).
[12] M.S. Bazaraa, J.J. Jarvis, and H.D. Sherali, Linear Programming and Net-
work Flows (John Wiley, Inc., New York, NY, 1990).
[13] E.M.L. Beale, “On minimizing a convex function subject to linear inequal-
ities,” J. Royal Statistical Society, Series B 17 (1955) pp. 173–184.
[14] E.M.L. Beale, “The use of quadratic programming in stochastic linear pro-
gramming,” Rand Report P-2404-1, The Rand Corporation (1961).
[15] E.M.L. Beale, J.J.H. Forrest, and C.J. Taylor, “Multi-time-period stochas-
tic programming” in: M.A.H. Dempster, Ed., Stochastic Programming (Aca-
demic Press, New York, NY, 1980) pp. 387–402.
[16] E.M.L. Beale, G.B. Dantzig, and R.D. Watson, “A ﬁrst order approach to
a class of multi-time-period stochastic programming problems,” Mathemat-
ical Programming Study 27 (1986) pp. 103–117.
[17] R. Bellman, Dynamic Programming (Princeton University Press, Princeton,
NJ, 1957).
[18] A. Ben-Tal and M. Teboulle, “Expected utility, penalty functions, and du-
ality in stochastic nonlinear programming,” Management Science 32 (1986)
pp. 1445–1466.
[19] J. F. Benders, “Partitioning procedures for solving mixed-variables pro-
gramming problems,” Numerische Mathematik 4 (1962) pp. 238–252.
[20] B. Bereanu, “Some numerical methods in stochastic linear programming
under risk and uncertainty” in: M.A.H. Dempster, Ed., Stochastic Pro-
gramming (Academic Press, New York, NY, 1980) pp. 169–205.
[21] J.O. Berger, Statistical Decision Theory and Bayesian Analysis (Springer-
Verlag, New York, NY, 1985).
[22] O. Berman, R.C. Larson, and S.S. Chiu, “Optimal server location on a
network operating as a M/G/1 queue,” Operations Research 33 (1985) pp.
746–770.
[23] D. Bertsimas, P. Jaillet, and A. Odoni, “A priori optimization,” Operations
Research 38 (1990) pp. 1019–1033.
[24] D. Bienstock and J.F. Shapiro, “Optimizing resource acquisition decisions
by stochastic programming,” Management Science 34 (1988) pp. 215–229.


## Page 408

References
389
[25] P. Billingsley, Convergence of Probability Measures (John Wiley, Inc., New
York, NY, 1968).
[26] J.R. Birge, “Solution Methods for Stochastic Dynamic Linear Programs,”
Ph.D. Dissertation and Technical Report SOL 80-29, Systems Optimization
Laboratory, Stanford University (Stanford, CA 94305, 1980).
[27] J.R. Birge, “The value of the stochastic solution in stochastic linear pro-
grams with ﬁxed recourse,” Mathematical Programming 24 (1982) pp. 314–
325.
[28] J.R. Birge, “Using sequential approximations in the L-shaped and gener-
alized programming algorithms for stochastic linear programs,” Technical
Report 83-12, Department of Industrial and Operations Engineering, Uni-
versity of Michigan (Ann Arbor, MI, 1983).
[29] J.R. Birge, “Aggregation in stochastic production problems,” Proceedings of
the 11th IFIP Conference on System Modelling and Optimization (Springer-
Verlag, New York, 1984).
[30] J.R. Birge, “Aggregation in stochastic linear programming,” Mathematical
Programming 31 (1985a) pp. 25–41.
[31] J.R. Birge, “Decomposition and partitioning methods for multi–stage
stochastic linear programs,” Operations Research 33 (1985b) pp. 989–1007.
[32] J.R. Birge, “Exhaustible recourse models with uncertain returns from ex-
ploration investment” in: Y. Ermoliev and R. Wets, Eds., Numerical Tech-
niques for Stochastic Optimization (Springer-Verlag, Berlin, 1988a) pp.
481–488.
[33] J.R. Birge, “The relationship between the L-shaped method and dual basis
factorization for stochastic linear programming” in: Y. Ermoliev and R.
Wets, Eds., Numerical Techniques for Stochastic Optimization (Springer-
Verlag, Berlin, 1988b) pp. 267–272.
[34] J.R. Birge, “Multistage stochastic planning models using piecewise linear
response functions” in: G. Dantzig and P. Glynn, Eds., Resource Planning
under Uncertainty for Electric Power Systems (NSF, 1989).
[35] J.R. Birge, “Quasi-Monte Carlo methods for option evaluation,” Technical
Report, Department of Industrial and Operations Engineering , University
of Michigan (Ann Arbor, MI, 1994).
[36] J.R. Birge, “Option methods for incorporating risk into linear planning
models,” Technical Report 95-8, Department of Industrial and Operations
Engineering, University of Michigan (Ann Arbor, MI, 1995).
[37] J.R. Birge and M.A.H. Dempster, “Optimality conditions for match-up
strategies in stochastic scheduling and related dynamic stochastic opti-
mization problems,” Technical Report 92-58, Department of Industrial and
Operations Engineering, University of Michigan (Ann Arbor, MI, 1992).


## Page 409

390
References
[38] J.R. Birge, C.J. Donohue, D.F. Holmes, and O.G. Svintsiski, “A paral-
lel implementation of the nested decomposition algorithm for multistage
stochastic linear programs,” Technical Report 94-1, Department of Indus-
trial and Operations Engineering, University of Michigan (Ann Arbor, MI,
1994), also Mathematical Programming 75 (1996), pp. 327–352.
[39] J.R. Birge and J. Dul´a, “Bounding separable recourse functions with lim-
ited distribution information,” Annals of Operations Research 30 (1991) pp.
277–298.
[40] J.R. Birge, R.M. Freund, and R.J. Vanderbei, “Prior reduced ﬁll-in in the
solution of equations in interior point algorithms,” Operations Research
Letters 11 (1992) pp. 195–198.
[41] J.R. Birge and D.F. Holmes, “Eﬃcient solution of two-stage stochastic lin-
ear programs using interior point methods,” Computational Optimization
and Applications 1 (1992) pp. 245–276.
[42] J.R. Birge and F.V. Louveaux, “A multicut algorithm for two-stage stochas-
tic linear programs,” European Journal of Operations Research 34 (1988)
pp. 384–392.
[43] J.R. Birge and M.J. Maddox, “Bounds on Expected Project Tardiness,”
Operations Research 43 (1995) pp. 838–850.
[44] J.R. Birge and M.J. Maddox, “Using second moment information in
stochastic scheduling” in: G. Yin and Q. Zhang, Eds., Recent Advances
in Control and Manufacturing Systems (Springer-Verlag, New York, NY,
1996) pp. 99–120.
[45] J.R. Birge and L. Qi, “Computing block-angular Karmarkar projections
with applications to stochastic programming,” Management Science 34
(1988) pp. 1472–1479.
[46] J.R. Birge and L. Qi, “Semiregularity and generalized subdiﬀerentials
with applications to optimization,” Mathematics of Operations Research
18 (1993) pp. 982–1006.
[47] J.R. Birge and L. Qi, “Subdiﬀerential convergence in stochastic programs,”
SIAM J. Optimization 5 (1995) pp. 436–453.
[48] J.R. Birge and M. Teboulle, “Upper bounds on the expected value of a
convex function using subgradient and conjugate function information,”
Mathematics of Operations Research 14 (1989) pp. 745–759.
[49] J.R. Birge and S.W. Wallace, “Reﬁning bounds for stochastic linear pro-
grams with linearly transformed independent random variables,” Opera-
tions Research Letters 5 (1986) pp. 73–77.
[50] J.R. Birge and S.W. Wallace, “A separable piecewise linear upper bound for
stochastic linear programs,” SIAM Journal on Control and Optimization 26
(1988) pp. 725–739.


## Page 410

References
391
[51] J.R. Birge and R.J-B Wets, “Approximations and error bounds in stochastic
programming” in: Y. Tong, Ed., Inequalities in Statistics and Probability
(IMS Lecture Notes—Monograph Series, 1984) pp. 178–186.
[52] J.R. Birge and R.J-B Wets, “Designing approximation schemes for stochas-
tic optimization problems, in particular, for stochastic programs with re-
course,” Mathematical Programming Study 27 (1986) pp. 54–102.
[53] J.R. Birge and R.J-B Wets, “Computing bounds for stochastic program-
ming problems by means of a generalized moment problem,” Mathematics
of Operations Research 12 (1987) pp. 49–162.
[54] J.R. Birge and R.J-B Wets, “Sublinear upper bounds for stochastic pro-
grams with recourse,” Mathematical Programming 43 (1989) pp. 131–149.
[55] G.R. Bitran and D. Sarkar, “On upper bounds of sequential stochastic
production planning problems,” European Journal of Operational Research
34 (1988) pp. 191–207.
[56] G.R. Bitran and H. Yanasse, “Deterministic approximations to stochastic
production problems,” Operations Research 32 (1984) pp. 999–1018.
[57] C.E. Blair and R.G. Jeroslow, “The value function of an integer program,”
Mathematical Programming 23 (1982) pp. 237–273.
[58] F. Black and M. Scholes, “The pricing of options and corporate liabilities,”
Journal of Political Economy 81 (1973) pp. 737–654.
[59] D. Blackwell, “Discounted dynamic programming,” Annals of Mathematical
Statistics 36 (1965) pp. 226–235.
[60] C. Borell, “Convex set functions in d-spaces,” Periodica Mathematica Jun-
garica 6 (1975) pp. 111–136.
[61] S.L. Brumelle and J.I. McGill, “Airline seat allocation with multiple nested
fare classes,” Operations Research 41 (1993) pp. 127–137.
[62] C.C. Carøe and J. Tind, “L-shaped decomposition of two-stage stochas-
tic programs with integer recourse,” Mathematical Programming 83 (1998)
pp. 407–424; Technical Report, Institute of Mathematics, University of
Copenhagen (Copenhagen, Denmark, 1996).
[63] T. Carpenter, I. Lustig, and J. Mulvey, “Formulating stochastic programs
for interior point methods,” Operations Research 39 (1991) pp. 757–770.
[64] H.P. Chao, “Exhaustible resource models: the value of information,” Oper-
ations Research 29 (1981) pp. 903–923.
[65] A. Charnes and W.W. Cooper, “Chance-constrained programming,” Man-
agement Science 5 (1959) pp. 73–79.
[66] A. Charnes and W.W. Cooper, “Deterministic equivalents for optimizing
and satisﬁcing under chance constraints,” Operations Research 11 (1963)
pp. 18–39.


## Page 411

392
References
[67] A. Charnes and W.W. Cooper, “Response to ‘Decision problems under
risk and chance constrained programming: dilemmas in the transition’,”
Management Science 29 (1983) pp. 750–753.
[68] A. Charnes, W.W. Cooper, and G.H. Symonds, “Cost horizons and cer-
tainty equivalents: an approach to stochastic programming of heating oil,”
Management Science 6 (1958) pp. 235–263.
[69] I.C. Choi, C.L. Monma, and D.F. Shanno, “Further development of a
primal-dual interior point method,” ORSA Journal on Computing 2 (1990)
pp. 304–311.
[70] E. Chu, A. George, J. Liu, and E. Ng, “SPARSPAK: Waterloo sparse matrix
package user’s guide for SPARSPAK-A,” Research Report CS-84-36, De-
partment of Computer Science, University of Waterloo (Waterloo, Ontario,
1984).
[71] K. L. Chung, A Course in Probability Theory (Academic Press, New York,
NY, 1974).
[72] V. Chv´atal, Linear Programming (Freeman, New York/San Francisco, CA,
1980).
[73] T. Cipra, “Moment problem with given covariance structure in stochastic
programming,” Ekonom.-Mat. Obzor 21 (1985) pp. 66–77.
[74] T. Cipra, “Stochastic programming with random processes,” Annals of Op-
erations Research 30 (1991) pp. 95–105.
[75] F. Clarke, Optimization and Nonsmooth Analysis (John Wiley, Inc., New
York, NY, 1983).
[76] J. Cox and S. Ross, “The valuation of options for alternative stochastic
processing,” Journal of Financial Economics 3 (1976) pp. 145–166.
[77] J. Czyzyk, R. Fourer, and S. Mehrotra, “A study of the augmented system
and column-splitting approaches for solving two-stage stochastic linear pro-
grams by interior-point methods,” ORSA Journal on Computing 7 (1995)
pp. 474–490.
[78] G.B. Dantzig, “Linear programming under uncertainty,” Management Sci-
ence 1 (1955) pp. 197–206.
[79] G.B. Dantzig, Linear Programming and Extensions (Princeton University
Press, Princeton, NJ, 1963).
[80] G.B. Dantzig and P. Glynn, “Parallel processors for planning under uncer-
tainty,” Annals of Operations Research 22 (1990) pp. 1–21.
[81] G.B. Dantzig and G. Infanger, “Large-scale stochastic linear programs—
Importance sampling and Benders decomposition” in: C. Brezinski and U.
Kulisch, Eds., Computational and applied mathematics, I (Dublin, 1991)
(North-Holland, Amsterdam, 1991) pp. 111–120.


## Page 412

References
393
[82] G.B. Dantzig and A. Madansky, “On the solution of two–stage linear pro-
grams under uncertainty,” Proceedings of the Fourth Berkeley Symposium
on Mathematical Statistics and Probability, (University of California Press,
Berkeley, CA, 1961).
[83] G.B. Dantzig and A. Wald, “On the fundamental lemma of Neyman and
Pearson,” The Annals of Mathematical Statistics 22 (1951) pp. 87–93.
[84] G.B. Dantzig and P. Wolfe, “The decomposition principle for linear pro-
grams,” Operations Research 8 (1960) pp. 101–111.
[85] D. Dawson and A. Sankoﬀ, “An inequality for probabilities,” Proceedings
of the American Mathematical Society 18 (1967) pp. 504–507.
[86] I. De´ak, “Three-digit accurate multiple normal probabilities,” Numerische
Mathematik 35 (1980) pp. 369–380.
[87] I. De´ak, “Multidimensional integration and stochastic programming,” in:
Y. Ermoliev and R. Wets, Eds., Numerical Techniques for Stochastic Opti-
mization (Springer-Verlag, Berlin, 1988) pp. 187–200.
[88] I. De´ak, Random Number Generators and Simulation (Akad´emiai Kiad´o,
Budapest, 1990).
[89] M.H. DeGroot, Optimal Statistical Decisions (McGraw-Hill, New York, NY,
1970).
[90] M.A.H. Dempster, “Introduction to Stochastic Programming” in: M.A.H.
Dempster, Ed., Stochastic Programming (Academic Press, New York, NY,
1980) pp. 3–59.
[91] M.A.H. Dempster, “The expected value of perfect information in the opti-
mal evolution of stochastic problems” in: M. Arato, D. Vermes, and A.V.
Balakrishnan, Eds., Stochastic Diﬀerential Systems (Lecture Notes in In-
formation and Control, Vol. 36, 1981) pp. 25–40.
[92] M.A.H. Dempster, “On stochastic programming II: dynamic problems un-
der risk,” Stochastics 25 (1988) pp. 15–42.
[93] M.A.H. Dempster and Papagaki-Papoulias, “Computational experience
with an approximate method for the distribution problem” in: M.A.H.
Dempster, Ed., Stochastic Programming (Academic Press, New York, NY,
1980) pp. 223–243.
[94] V.F. Demyanov and L.V. Vasiliev, Nediﬀerentsiruemaya optimizatsiya
(Nondiﬀerentiable optimization) (Nauka, Moscow, 1981).
[95] I.I. Dikin, “Iterative solution of problems of linear and quadratic program-
ming,” Soviet Mathematics Doklady 8 (1967) pp. 674–675.
[96] J.H. Dul´a, “An upper bound on the expectation of simplicial functions of
multivariate random variables,” Mathematical Programming 55 (1991) pp.
69–80.


## Page 413

394
References
[97] V. Dupaˇc, “A dynamic stochastic approximation method,” Annals of Math-
ematical Statistics 6 (1965) pp. 1695–1702.
[98] J. Dupaˇcov´a, “Minimax stochastic programs with nonconvex nonseparable
penalty functions” in: A. Pr´ekopa, Ed., Progress in Operations Research
(Janos Bolyai Math. Soc., 1976) pp. 303–316.
[99] J. Dupaˇcov´a, “The minimax approach to stochastic linear programming
and the moment problem,” Ekonom.-Mat. Obzor 13 (1977) pp. 297–307.
[100] J. Dupaˇcov´a, “Stability in stochastic programming with recourse-contamin-
ated distributions,” Mathematical Programming Study 28 (1984) pp. 72–83.
[101] J. Dupaˇcov´a, “Stability and sensitivity analysis for stochastic program-
ming,” Annals of Operations Research 27 (1990) pp. 115–142.
[102] J. Dupaˇcov´a and R.J-B Wets, “Asymptotic behavior of statistical estima-
tors and of optimal solutions of stochastic optimization problems,” Annals
of Statistics 16 (1988) pp. 1517–1549.
[103] B.C. Eaves and W.I. Zangwill, “Generalized cutting plane algorithms,”
SIAM J. Control 9 (1971) pp. 529–542.
[104] N.C.P. Edirisinghe, “Essays on Bounding Stochastic Programming Prob-
lems,” Ph.D. Dissertation, The University of British Columbia (1991).
[105] N.C.P. Edirisinghe, “New second-order bounds on the expectation of saddle
functions with applications to stochastic linear programming,” Operations
Research 44 (1996) pp. 909–922.
[106] H.P. Edmundson, “Bounds on the expectation of a convex function of a ran-
dom variable,” RAND Corporation Paper 982, Santa Monica, CA (1956).
[107] M. Eisner and P. Olsen, “Duality for stochastic programming interpreted
as l.p. in Lp-space,” SIAM Journal of Applied Mathematics 28 (1975) pp.
779–792.
[108] G.D. Eppen, R.K. Martin, and L. Schrage, “A scenario approach to capacity
planning,” Operations Research 37 (1989) pp. 517–527.
[109] Y. Ermoliev, “On the stochastic quasigradient method and quasi-Feyer se-
quences,” Kibernetika 5 (2) (1969) pp. 73–83 (in Russian; also published in
English as Cybernetics 5 (1969) pp. 208–220).
[110] Y. Ermoliev, Methods of Stochastic Programming (Nauka, Moscow (in Rus-
sian) 1976).
[111] Y. Ermoliev, “Stochastic quasigradient methods and their applications to
systems optimization,” Stochastics 9 (1983) pp. 1–36.
[112] Y. Ermoliev, “Stochastic quasigradient methods.” (SC) in: Y. Ermoliev and
R. Wets, Eds., Numerical Techniques for Stochastic Optimization (Springer-
Verlag, Berlin, 1988) pp. 141–186.


## Page 414

References
395
[113] Y. Ermoliev, A. Gaivoronski, and C. Nedeva, “Stochastic optimization
problems with partially known distribution functions,” SIAM Journal on
Control and Optimization 23 (1985) pp. 377–394.
[114] Y. Ermoliev and R. Wets, “Introduction” in: Y. Ermoliev and R. Wets,
Eds., Numerical Techniques for Stochastic Optimization (Springer-Verlag,
Berlin, 1988).
[115] L.F. Escudero, P.V. Kamesam, A.J. King, and R.J-B Wets, “Production
planning via scenario modeling,” Annals of Operations Research 43 (1993)
pp. 311–335.
[116] W. Feller, An Introduction to Probability Theory and Its Applications (John
Wiley, Inc., New York, NY, 1971).
[117] A. Ferguson and G.B. Dantzig, “The allocation of aircraft to routes: an
example of linear programming under uncertain demands,” Management
Science 3 (1956) pp. 45–73.
[118] C.H. Fine and R.M. Freund, “Optimal investment in product-ﬂexible man-
ufacturing capacity,” Management Science 36 (1990) pp. 449–466.
[119] S.D. Fl˚am, “Nonanticipativity in stochastic programming,” Journal of Op-
timization Theory and Applications 46 (1985) pp. 23–30.
[120] S.D. Fl˚am, “Asymptotically stable solutions to stochastic problems of
Bolza” in: F. Archetti, G. Di Pillo, and M Lucertini, Eds., Stochastic Pro-
gramming (Lecture Notes in Information and Control 76, 1986) pp. 184–193.
[121] W. Fleming and R. Rischel, Deterministic and Stochastic Control (Springer-
Verlag, New York, NY, 1975).
[122] R. Fourer, “A simplex algorithm for piecewise-linear programming. I:
derivation and proof,” Mathematical Programming 33 (1985) pp. 204–233.
[123] R. Fourer, “A simplex algorithm for piecewise-linear programming. II:
ﬁniteness, feasibility, and degeneracy,” Mathematical Programming 41
(1988) pp. 281–315.
[124] R. Fourer, D.M. Gay, and B.W. Kernighan, AMPL: A Modeling Language
for Mathematical Programming (Scientiﬁc Press, South San Francisco, CA,
1993).
[125] B. Fox, “Implementation and relative eﬃciency of quasirandom sequence
generators,” ACM Transactions on Mathematical Software 12 (1986) pp.
362–376.
[126] L. Frantzeskakis and W. Powell, “A successive linear approximation proce-
dure for stochastic, dynamic vehicle allocation problems,” Transportation
Science 24 (1990) pp. 40–57.
[127] L.F. Frantzeskakis and W.B. Powell, “Bounding procedures for multistage
stochastic dynamic networks,” Networks 23 (1993) pp. 575–595.


## Page 415

396
References
[128] K. Frauendorfer, “Solving SLP recourse problems:The case of stochastic
technology matrix, RHS, and objective,” Proceedings of 13th IFIP Con-
ference on System Modelling and Optimization (Springer-Verlag, Berlin,
1988a).
[129] K. Frauendorfer, “Solving S.L.P. recourse problems with arbitrary mul-
tivariate distributions – the dependent case,” Mathematics of Operations
Research 13 (1988b) pp. 377–394.
[130] K. Frauendorfer, “A simplicial approximation scheme for convex two-stage
stochastic programming problems,” Manuskripte, Institut f¨ur Operations
Research, University of Zurich (Zurich, 1989).
[131] K. Frauendorfer, Stochastic Two-Stage Programming (Lecture Notes in Eco-
nomics and Mathematical Systems 392, 1992).
[132] K. Frauendorfer and P. Kall, “A solution method for SLP recourse problems
with arbitrary multivariate distributions—the independent case,” Problems
in Control and Information Theory 17 (1988) pp. 177–205.
[133] A.A. Gaivoronski, “Implementation of stochastic quasigradient methods”
in: Y. Ermoliev and R. Wets, Eds., Numerical Techniques for Stochastic
Optimization (Springer-Verlag, Berlin, 1988) pp. 313–352.
[134] J. Galambos, The Asymptotic Theory of Extreme Order Statistics (John
Wiley, Inc., New York, 1978).
[135] S.J. Gartska, “An economic interpretation of stochastic programs,” Math-
ematical Programming 18 (1980) pp. 62–67.
[136] S.J. Gartska and D. Rutenberg, “Computation in discrete stochastic pro-
grams with recourse,” Operations Research 21 (1973) pp. 112–122.
[137] S.J. Gartska and R.J-B Wets, “On decision rules in stochastic program-
ming,” Mathematical Programming 7 (1974) pp. 117–143.
[138] H.I. Gassmann, “Conditional probability and conditional expectation of a
random vector” in: Y. Ermoliev and R. Wets, Eds., Numerical Techniques
for Stochastic Optimization (Springer-Verlag, Berlin, 1988) pp. 237–254.
[139] H.I. Gassmann, “Optimal harvest of a forest in the presence of uncertainty,”
Canadian Journal of Forest Research 19 (1989) pp. 1267–1274.
[140] H.I. Gassmann, “MSLiP: a computer code for the multistage stochastic
linear programming problem,” Mathematical Programming 47 (1990) pp.
407–423.
[141] H.I. Gassmann and W.T. Ziemba, “A tight upper bound for the expecta-
tion of a convex function of a multivariate random variable,” Mathematical
Programming Study 27 (1986) pp. 39–53.
[142] D.M. Gay, “A variant of Karmarkar’s linear programming algorithm for
problems in standard form,” Mathematical Programming 37 (1987) pp. 81–
90.


## Page 416

References
397
[143] M. Gendreau, G. Laporte, and R. S´eguin, “Stochastic vehicle routing,”
European Journal of Operational Research 88 (1996) pp. 3–12.
[144] A.M. Geoﬀrion, “Elements of large-scale mathematical programming,”
Management Science 16 (1970) pp. 652–675.
[145] A.M. Geoﬀrion, “Duality in nonlinear programming: a simpliﬁed applica-
tions-oriented development,” SIAM Rev. 13 (1971) pp. 1–37.
[146] C.R. Glassey, “Nested decomposition and multistage linear programs,”
Management Science 20 (1973) pp. 282–292.
[147] R.C. Grinold, “A new approach to multi-stage stochastic linear programs,”
Mathematical Programming Study 6 (1976) pp. 19–29.
[148] R.C. Grinold, “Model building techniques for the correction of end eﬀects in
multistage convex programs,” Operations Research 31 (1983) pp. 407–431.
[149] R.C. Grinold, “Inﬁnite horizon stochastic programs,” SIAM Journal on
Control and Optimization 24 (1986) pp. 1246–1260.
[150] J.M. Harrison, Brownian Motion and Stochastic Flow Systems (John Wiley,
Inc., New York, NY, 1985).
[151] J.M. Harrison and L.M. Wein, “Scheduling networks of queues:Heavy traﬃc
analysis of a two-station closed network,” Operations Research 38 (1990)
pp. 1052–1064.
[152] D. Haugland and S.W. Wallace, “Solving many linear programs that diﬀer
only in the righthand side,” European Journal of Operational Research 37
(1988) pp. 318–324.
[153] D.P. Heyman and M.J. Sobel, Stochastic Models in Operations Research,
Volume II, Stochastic Optimization (McGraw-Hill, New York, NY, 1984).
[154] J. Higle and S. Sen, “Statistical veriﬁcation of optimality conditions for
stochastic programs with recourse,” Annals of Operations Research 30
(1991a) pp. 215–240.
[155] J. Higle and S. Sen, “Stochastic decomposition: an algorithm for two stage
linear programs with recourse,” Mathematics of Operations Research 16
(1991b) pp. 650–669.
[156] J.-B. Hiriart-Urruty, “Conditions n´ecessaires d’optimalit´e pour un pro-
gramme stochastique avec recours,” SIAM Journal on Control and Op-
timization 16 (1978) pp. 317–329.
[157] J.K. Ho and E. Loute, “A set of staircase linear programming test prob-
lems,” Mathematical Programming 20 (1981) pp. 245–250.
[158] J.K. Ho and A.S. Manne, “Nested decomposition for dynamic models,”
Mathematical Programming 6 (1974) pp. 121–140.


## Page 417

398
References
[159] W. Hoeﬀding, “Probability inequalities for sums of bounded random vari-
ables,” Journal of the American Statistical Association 58 (1963) pp. 13–30.
[160] A. Hogan, J. Morris, and H. Thompson, “Decision problems under risk
and chance constrained programming: dilemmas in the transition,” Man-
agement Science 27 (1981) pp. 698–716.
[161] A. Hogan, J. Morris, and H. Thompson, “Reply to Professors Charnes and
Cooper concerning their response to ‘Decision problems under risk and
chance constrained programming: dilemmas in the transition’,” Manage-
ment Science 30 (1984) pp. 258–259.
[162] R.A. Howard, Dynamic Programming and Markov Processes (MIT Press,
Cambridge, MA, 1960).
[163] C.C. Huang, W. Ziemba, and A. Ben-Tal, “Bounds on the expectation of
a convex function of a random variable: with applications to stochastic
programming,” Operations Research 25 (1977) pp. 315–325.
[164] P.J. Huber, “The behavior of maximum likelihood estimates under nonstan-
dard conditions,” Proceedings of the Fifth Berkeley Symposium on Mathe-
matical Statistics and Probability, (University of California, Berkeley, CA,
1967).
[165] J.C. Hull, Options, Futures and Other Derivatives, third edition, (Prentice-
Hall, Upper Saddle River, NJ, 1997).
[166] G. Infanger, “Monte Carlo (importance) sampling within a Benders de-
composition algorithm for stochastic linear programs; Extended version:
including results of large-scale problems,” Technical Report SOL 91-6, Sys-
tems Optimization Laboratory, Stanford University (Stanford, CA, 1991).
[167] G. Infanger, Planning under Uncertainty: Solving Large-Scale Stochastic
Linear Programs (Boyd and Fraser, Danvers, MA, 1994).
[168] International Business Machines Corp., “Optimization Subroutine Library
Guide and Reference, Release 2,” document SC23-0519-02, International
Business Machines Corp. (Armonk, NY, 1991).
[169] R. Jagganathan, “A minimax procedure for a class of linear programs under
uncertainty,” Operations Research 25 (1977) pp. 173–177.
[170] R. Jagganathan, “Use of sample information in stochastic recourse and
chance-constrained programming models,” Management Science 31 (1985)
pp. 96–108.
[171] R. Jagganathan, “Linear programming with stochastic processes as param-
eters as applied to production planning,” Annals of Operations Research 30
(1991) pp. 107–114.
[172] P. Jaillet, “A priori solution of a traveling salesman problem in which a
random subset of the customers are visited,” Operations Research 36 (1988)
pp. 929–936.


## Page 418

References
399
[173] R.A. Jarrow and A. Rudd, Option Pricing (Irwin, Homewood, IL, 1983).
[174] J.L. Jensen, “Sur les fonctions convexes et les in´egalit´es entre les valeurs
moyennes,” Acta. Math. 30 (1906) pp. 175–193.
[175] W.C. Jordan and S.C. Graves, “Principles on the beneﬁts of manufacturing
process ﬂexibility,” Technical Report GMR-7310, General Motors Research
Laboratories, Warren, MI (1991).
[176] P. Kall, Stochastic Linear Programming (Springer-Verlag, Berlin, 1976).
[177] P. Kall, “Computational methods for solving two-stage stochastic linear
programming problems,” Journal of Applied Mathematics and Physics 30
(1979) pp. 261–271.
[178] P. Kall, “Stochastic programs with recourse: an upper bound and the re-
lated moment problem,” Zeitschrift f¨ur Operations Research 31 (1987) pp.
A119–A141.
[179] P. Kall, “An upper bound for stochastic linear programming using ﬁrst
and total second moments,” Annals of Operations Research 30 (1991) pp.
267–276.
[180] P. Kall and J. Mayer, “SLP-IOR: an interactive model management system
for stochastic linear programs,” Mathematical Programming 75 (1996) pp.
221–240.
[181] P. Kall and D. Stoyan, “Solving stochastic programming problems with re-
course including error bounds,” Math. Operationsforsch. Statist. Ser. Op-
tim. 13 (1982) pp. 431–447.
[182] P. Kall and S.W. Wallace, Stochastic Programming (John Wiley and Sons,
Chichester, UK, 1994).
[183] J.G. Kallberg, R.W. White, and W.T. Ziemba, “Short term ﬁnancial plan-
ning under uncertainty,” Management Science 28 (1982) pp. 670–682.
[184] J.G. Kallberg and W.T. Ziemba, “Comparison of alternative utility func-
tions in portfolio selection problems,” Management Science 29 (1983) pp.
1257–1276.
[185] M. Kallio and E. Porteus, “Decomposition of arborescent linear programs,”
Mathematical Programming 13 (1977) pp. 348–356.
[186] R.E. Kalman , Topics in Mathematical System Theory (McGraw-Hill, New
York, NY, 1969).
[187] E. Kao and M. Queyranne, “Budgeting costs of nursing in a hospital,”
Management Science 31 (1985) pp. 608–621.
[188] N. Karmarkar, “A new polynomial-time algorithm for linear programming,”
Combinatorica 4 (1984) pp. 373–395.


## Page 419

400
References
[189] A. Karr, “Extreme points of certain sets of probability measure, with ap-
plications,” Mathematics of Operations Research 8 (1983) pp. 74–85.
[190] J. Kemperman, “The general moment problem, a geometric approach,”
Annals of Mathematical Statistics 39 (1968) pp. 93–122.
[191] A.I. Kibzun and Y.S. Kan, Stochastic Programming Problems with Proba-
bility and Quantile Functions (John Wiley Inc., Chichester, UK, 1996).
[192] A.I. Kibzun and V.Yu. Kurbakovskiy, “Guaranteeing approach to solving
quantile optimization problems,” Annals of Operations Research 30 (1991)
pp. 81–93.
[193] A. King, “Finite generation method” in: Y. Ermoliev and R. Wets, Eds.,
Numerical Techniques for Stochastic Optimization (Springer-Verlag, Berlin,
1988a) pp. 295–312.
[194] A. King, “Stochastic programming problems:Examples from the literature”
in: Y. Ermoliev and R. Wets, Eds., Numerical Techniques for Stochastic
Optimization (Springer-Verlag, Berlin, 1988b) pp. 543–567.
[195] A. King and R.T. Rockafellar, “Asymptotic theory for solutions in gener-
alized M-estimation and stochastic programming,” Mathematics of Opera-
tions Research 18 (1993) pp. 148–162.
[196] A.J. King and R.J-B Wets, “Epiconsistency of convex stochastic programs,”
Stochastics and Stochastics Reports 34 (1991) pp. 83–92.
[197] K.C. Kiwiel, “An aggregate subgradient method for nonsmooth convex min-
imization,” Mathematical Programming 27 (1983) pp. 320–341.
[198] W.K. Klein Haneveld, Duality in Stochastic Linear and Dynamic Pro-
gramming (Lecture Notes in Economics and Mathematical Systems 274,
Springer-Verlag, Berlin, 1985).
[199] W.K. Klein Haneveld, “Robustness against dependence in PERT: an appli-
cation of duality and distributions with known marginals,” Mathematical
Programming Study 27 (1986) pp. 153–182.
[200] M.G. Krein and A.A. Nudel’man, The Markov Moment Problem and Ex-
tremal Problems (Translations of Mathematical Monographs 50, 1977).
[201] H. Kushner, Introduction to Stochastic Control (Holt, New York, NY, 1971).
[202] M. Kusy and W.T. Ziemba, “A bank asset and liability management
model,” Operations Research 34 (1986) pp. 356–376.
[203] B.J. Lageweg, J.K. Lenstra, A.H.G. Rinnooy Kan, and L. Stougie, “Stochas-
tic integer programming by dynamic programming” in: Y. Ermoliev and R.
Wets, Eds., Numerical Techniques for Stochastic Optimization (Springer-
Verlag, Berlin, 1988) pp. 403–412.


## Page 420

References
401
[204] G. Laporte and F.V. Louveaux, “The integer L-shaped method for stochas-
tic integer programs with complete recourse,” Operations Research Letters
13 (1993) pp. 133–142.
[205] G. Laporte, F.V. Louveaux, and H. Mercure, “Models and exact solutions
for a class of stochastic location-routing problems,” European Journal of
Operational Research 39 (1989) pp. 71–78.
[206] G. Laporte, F.V. Louveaux, and H. Mercure, “An exact solution for the a
priori optimization of the probabilistic traveling salesman problem,” Oper-
ations Research 42 (1994) pp. 543–549.
[207] G. Laporte, F.V. Louveaux, and L. Van Hamme, “Exact solution to a loca-
tion problem with stochastic demands,” Transportation Science 28 (1994)
pp. 95–103.
[208] L. Lasdon, Optimization Theory for Large Systems (Macmillan, New York,
NY, 1970).
[209] C. Lemar´echal, “Bundle methods in nonsmooth optimization” in: Nons-
mooth optimization (Proc. IIASA Workshop) (Pergamon, Oxford-Elmsford,
New York, NY, 1978) pp. 79–102.
[210] J.K. Lenstra, A.H.G. Rinnooy Kan, and L. Stougie, “A framework for the
probabilistic analysis of hierarchical planning systems,” Annals of Opera-
tion Research 1 (1984) pp. 23–42.
[211] F.V. Louveaux, “Piecewise convex programs,” Mathematical Programming
15 (1978) pp. 53–62.
[212] F.V. Louveaux, “A solution method for multistage stochastic programs with
recourse with application to an energy investment problem,” Operations
Research 28 (1980) pp. 889–902.
[213] F.V. Louveaux, “Multistage stochastic programs with block-separable re-
course,” Mathematical Programming Study 28 (1986) pp. 48–62.
[214] F.V. Louveaux and D. Peeters, “A dual-based procedure for stochastic fa-
cility location,” Operations Research 40 (1992) pp. 564–573.
[215] F.V. Louveaux and Y. Smeers, “Optimal investments for electricity gener-
ation:A stochastic model and a test-problem” in: Numerical Techniques for
Stochastic Optimization (Springer-Verlag, Berlin, 1988) pp. 33–64.
[216] F.V. Louveaux and Y. Smeers, “Stochastic optimization for the introduc-
tion of a new energy technology,” Stochastics (to appear) (1997).
[217] F.V. Louveaux and M. van der Vlerk, “Stochastic programming with simple
integer recourse,” Mathematical Programming 61 (1993) pp. 301–325.
[218] I.J. Lustig, R.E. Marsten, and D.F. Shanno, “Computational experience
with a primal-dual interior point method for linear programming,” Linear
Algebra and Its Application 152 (1991) pp. 191–222.


## Page 421

402
References
[219] A. Madansky, “Bounds on the expectation of a convex function of a multi-
variate random variable,” Annals of Mathematical Statistics 30 (1959) pp.
743–746.
[220] A. Madansky, “Inequalities for stochastic linear programming problems,”
Management Science 6 (1960) pp. 197–204.
[221] M. Maddox and J.R. Birge, “Bounds on the distribution of tardiness in a
PERT network,” Technical Report, Department of Industrial and Opera-
tions Engineering, University of Michigan (Ann Arbor, MI, 1991).
[222] O. Mangasarian and J.B. Rosen, “Inequalities for stochastic nonlinear pro-
gramming problems,” Operations Research 12 (1964) pp. 143–154.
[223] A.S. Manne, “Waiting for the breeder” in: Review of Economic Studies
Symposium (1974) pp. 47–65.
[224] A.S. Manne and R. Richels, Buying Greenhouse Insurance—The Economic
Costs of Carbon Dioxide Emission Limits (MIT Press, Cambridge, MA,
1992).
[225] H.M. Markowitz, Portfolio Selection; Eﬃcient Diversiﬁcation of Invest-
ments (John Wiley, Inc., New York, NY, 1959).
[226] K. Marti, “Approximationen von Entscheidungsproblemen mit linearer
Ergebnisfunktion und positiv homogener, subadditiver Verlusfunktion,”
Zeitschrift f¨ur Wahrscheinlichkeitstheorie und Verwandte Gebiete 31 (1975)
pp. 203–233.
[227] K. Marti, Descent Directions and Eﬃcient Solutions in Discretely Dis-
tributed Stochastic Programs, (Lecture Notes in Economics and Mathemat-
ical Systems 299, Springer-Verlag, Berlin, 1988).
[228] L. McKenzie, “Turnpike theory,” Econometrica 44 (1976) pp. 841–864.
[229] P. Michel and J.-P. Penot, “Calcul sous-diﬀ´erentiel pour des fonctions
lipschitziennes et non lipschitziennes,” Comptes Rendus des Seances de
l’Acad´emie des Sciences Paris. Serie 1. Math´ematique 298 (1984) pp. 269–
272.
[230] J. Miller and H. Wagner, “Chance-constrained programming with joint
chance constraints,” Operations Research 12 (1965) pp. 930–945.
[231] G.J. Minty, “On the maximal domain of a ‘monotone’ function,” Michigan
Mathematics Journal 8 (1961) pp. 135–137.
[232] F. Mirzoachmedov and S. Uriasiev, “Adaptive step-size control for stochas-
tic optimization algorithm,” Zhurnal vicisl. mat. i mat. ﬁz. 6 (1983) pp.
1314–1325 (in Russian).
[233] B. Mordukhovich, “Approximation methods and extremum conditions in
nonsmooth control systems,” Soviet Mathematics Doklady 36 (1988) pp.
164–168.


## Page 422

References
403
[234] D.P. Morton, “An enhanced decomposition algorithm for multistage
stochastic hydroelectric scheduling,” Technical Report NPSOR-94-001, De-
partment of Operations Research, Naval Postgraduate School (Monterey,
CA, 1994).
[235] J.M. Mulvey and A. Ruszczy´nski, “A new scenario decomposition method
for large scale stochastic optimization,” Operations Research 43 (1995) pp.
477–490.
[236] J.M. Mulvey and H. Vladimirou, “Stochastic network optimization models
for investment planning,” Annals of Operations Research 20 (1989) pp. 187–
217.
[237] J.M. Mulvey and H. Vladimirou, “Applying the progressive hedging algo-
rithm to stochastic generalized networks,” Annals of Operations Research
31 (1991a) pp. 399–424.
[238] J.M. Mulvey and H. Vladimirou, “Solving multistage stochastic networks:
an application of scenario aggregation,” Networks 21 (1991b) pp. 619–643.
[239] J.M. Mulvey and H. Vladimirou, “Stochastic network programming for
ﬁnancial planning problems,” Management Science 38 (1992) pp. 1642–
1664.
[240] B.A. Murtagh and M.A. Saunders, “MINOS 5.0 User’s Guide,” Technical
Report SOL 83-20, Systems Optimization Laboratory, Stanford University
(Stanford, CA, 1983).
[241] K.G. Murty, “Linear programming under uncertainty: a basic property of
the optimal solution,” Z. Wahrscheinlichkeitstheorie und Verw. Gebiete 10
(1968) pp. 284–288.
[242] K.G. Murty, Linear Programming (John Wiley, Inc., New York, NY, 1983).
[243] S.C. Myers, “Finance theory and ﬁnancial strategy,” Interfaces 14:1 (1984)
pp. 126–137.
[244] J.L. Nazareth and R.J-B Wets, “Algorithms for stochastic programs: the
case of nonstochastic tenders,” Mathematical Programming Study 28 (1986)
pp. 1–28.
[245] G.L. Nemhauser and L.A. Wolsey, Integer and Combinatorial Optimization
(Wiley-Interscience, New York, NY, 1988).
[246] H. Niederreiter, “Quasi–Monte Carlo methods and pseudorandom num-
bers,” Bulletin of the American Mathematical Society 84 (1978) pp. 957–
1041.
[247] S.S. Nielsen and S.A. Zenios, “A massively parallel algorithm for nonlinear
stochastic network problems,” Operations Research 41 (1993a) pp. 319–337.


## Page 423

404
References
[248] S.S. Nielsen and S.A. Zenios, “Proximal minimizations with D-functions
and the massively parallel solution of linear stochastic network programs,”
International Journal of Supercomputing and Applications 7 (1993b) pp.
349–364.
[249] M.-C. No¨el and Y. Smeers, “Nested decomposition of multistage nonlinear
programs with recourse,” Mathematical Programming 37 (1987) pp. 131–
152.
[250] V.I. Norkin, Y.M. Ermoliev, and A. Ruszczy´nski, “On optimal allocation of
indivisibles under uncertainty,” Operations Research 46 (1998) pp. 381–395.
[251] S. Parikh, Lecture Notes on Stochastic Programming (University of Califor-
nia, Berkeley, CA, 1968).
[252] M.V.F. Pereira and L.M.V.G. Pinto, “Stochastic optimization of a mul-
tireservoir hydroelectric system—A decomposition approach,” Water Re-
sources Research 21 (1985) pp. 779–792.
[253] G.Ch. Pﬂug, “Stepsize rules, stopping times and their implementation in
stochastic quasigradient algorithms” in: Y. Ermoliev and R. Wets, Eds.,
Numerical Techniques for Stochastic Optimization (Springer-Verlag, Berlin,
1988) pp. 353–372.
[254] J. Pint´er, “Deterministic approximations of probability inequalities,”
ZOR—Methods and Models of Operations Research, Series Theory 33
(1989) pp. 219–239.
[255] E.L. Plambeck, B-R. Fu, S.M. Robinson, and R. Suri, “Sample-path opti-
mization of convex stochastic performance functions,” Mathematical Pro-
gramming 75 (1996) pp. 137–176.
[256] W.B. Powell, “A comparative review of alternative algorithms for the dy-
namic vehicle allocation program” in: B. Golden and A. Assad, Eds., Vehicle
Routing: Methods and Studies (North-Holland, Amsterdam, 1988).
[257] A. Pr´ekopa, “Logarithmic concave measures with application to stochastic
programming,” Acta. Sci. Math. (Szeged) 32 (1971) pp. 301–316.
[258] A. Pr´ekopa, “Contributions to the theory of stochastic programs,” Mathe-
matical Programming 4 (1973) pp. 202–221.
[259] A. Pr´ekopa, “Programming under probabilistic constraints with a random
technology matrix,” Mathematische Operationsforschung und Statistik 5
(1974) pp. 109–116.
[260] A. Pr´ekopa, “Logarithmically concave measures and related topics” in:
M.A.H. Dempster, Ed., Stochastic Programming (Academic Press, New
York, NY, 1980).
[261] A. Pr´ekopa, “Boole-Bonferroni inequalities and linear programming,” Op-
erations Research 36 (1988) pp. 145–162.


## Page 424

References
405
[262] A. Pr´ekopa, Stochastic Programming (Kluwer Academic Publishers, Dor-
drecht, Netherlands, 1995).
[263] A. Pr´ekopa and T. Sz´antai, “On optimal regulation of a storage level with
application to the water level regulation of a lake,” Survey of Mathemat-
ical Programming (Proc. Ninth Internat. Math. Programming Sympos.,
Budapest, 1976), Vol. 2 (North-Holland, Amsterdam, 1976).
[264] H.N. Psaraftis, “On the practical importance of asymptotic optimality in
certain heuristic algorithms,” Networks (1984) pp. 587–596.
[265] H.N. Psaraftis, G.G. Tharakan, and A. Ceder, “Optimal response to oil
spills: the strategic decision case,” Operations Research 34 (1986) pp. 203–
217.
[266] L. Qi, “Forest iteration method for stochastic transportation problem,”
Mathematical Programming Study (1985) pp. 142–163.
[267] L. Qi, “An alternating method for stochastic linear programming with sim-
ple recourse,” Stochastic Processes and Their Applications 841 (1986) pp.
183–190.
[268] H. Raiﬀa, Decision Analysis (Addison-Wesley, Reading, MA, 1968).
[269] H. Raiﬀa and R. Schlaifer, Applied Statistical Decision Theory (Harvard
University, Boston, MA, 1961).
[270] A.H.G. Rinnooy Kan and L. Stougie, “Stochastic integer programming”
in: Y. Ermoliev and R. Wets, Eds., Numerical Techniques for Stochastic
Optimization (Springer-Verlag, Berlin, 1988) pp. 201–213.
[271] H. Robbins and S. Monro, “A stochastic approximation method,” Annals
of Mathematical Statistics 22 (1951) pp. 400–407.
[272] S.M. Robinson and R.J-B Wets, “Stability in two-stage stochastic program-
ming,” SIAM Journal on Control and Optimization 25 (1987) pp. 1409–
1416.
[273] R.T. Rockafellar, Convex Analysis (Princeton University Press, Princeton,
NJ, 1969).
[274] R.T. Rockafellar, Conjugate Duality and Optimization (Society for Indus-
trial and Applied Mathematics, Philadelphia, PA, 1974).
[275] R.T. Rockafellar, “Monotone operators and the proximal point algorithm,”
SIAM Journal on Control and Optimization 14 (1976a) pp. 877–898.
[276] R.T. Rockafellar, Integral Functionals, Normal Integrands and Measurable
Selections (Lecture Notes in Mathematics 543, 1976b).
[277] R.T. Rockafellar and R.J-B Wets, “Stochastic convex programming: basic
duality,” Paciﬁc Journal of Mathematics 63 (1976a) pp. 173–195.


## Page 425

406
References
[278] R.T. Rockafellar and R.J-B Wets, “Stochastic convex programming, rela-
tively complete recourse and induced feasibility,” SIAM Journal on Control
and Optimization 14 (1976b) pp. 574–589.
[279] R.T. Rockafellar and R.J-B Wets, “A Lagrangian ﬁnite generation tech-
nique for solving linear-quadratic problems in stochastic programming,”
Mathematical Programming Study 28 (1986) pp. 63–93.
[280] R.T. Rockafellar and R.J-B Wets, “Scenarios and policy aggregation in
optimization under uncertainty,” Mathematics of Operations Research 16
(1991) pp. 119–147.
[281] W. R¨omisch and R. Schultz, “Distribution sensitivity in stochastic pro-
gramming,” Mathematical Programming 50 (1991a) pp. 197–226.
[282] W. R¨omisch and R. Schultz, “Stability analysis for stochastic programs,”
Annals of Operations Research 31 (1991b) pp. 241–266.
[283] S.M. Ross, Introduction to Stochastic Dynamic Programming (Academic
Press, New York, London, 1983).
[284] H.L. Royden, Real Analysis (Macmillan, London, NY, 1968).
[285] R.Y. Rubinstein, Simulation and the Monte Carlo Method (John Wiley Inc.,
New York, NY, 1981).
[286] A. Ruszczy´nski, “A regularized decomposition for minimizing a sum of
polyhedral functions,” Mathematical Programming 35 (1986) pp. 309–333.
[287] A. Ruszczy´nski, “Parallel decomposition of multistage stochastic program-
ming problems,” Mathematical Programming 58 (1993a) pp. 201–228.
[288] A. Ruszczy´nski, “Regularized decomposition of stochastic programs: al-
gorithmic techniques and numerical results,” Working Paper WP-93-21,
International Institute for Applied Systems Analysis, Laxenburg, Austria
(1993b).
[289] G. Salinetti, “Approximations for chance constrained programming prob-
lems,” Stochastics 10 (1983) pp. 157–169.
[290] Y.S. Sathe, M. Pradhan, and S.P. Shah, “Inequalities for the probability of
the occurrence of at least m out of n events,” Journal of Applied Probability
17 (1980) pp. 1127–1132.
[291] H. Scarf, “A minimax solution of an inventory problem” in: K.J. Arrow, S.
Karlin, and H. Scarf, Eds., Studies in the Mathematical Theory of Inventory
and Production (Stanford University Press, Stanford, CA, 1958).
[292] R. Schultz, “Continuity properties of expectation functionals in stochastic
integer programming,” Mathematics of Operations Research 18 (1993) pp.
578–589.
[293] A. Shapiro, “Asymptotic analysis of stochastic programs,” Annals of Op-
erations Research 30 (1991) pp. 169–186.


## Page 426

References
407
[294] W.F. Sharpe, “Capital asset prices: a theory of market equilibrium under
conditions of risk,” Journal of Finance 19 (1964) pp. 425–442.
[295] D. Simchi-Levi, “Hierarchical planning for probabilistic distribution sys-
tems in the Euclidean spaces,” Management Science 38 (1992) pp. 198–211.
[296] L. Somly´odi and R.J-B Wets, “Stochastic optimization models for lake eu-
trophication management,” Operations Research 36 (1988) pp. 660–681.
[297] L. Stougie, Design and Analysis of Algorithms for Stochastic Integer Pro-
gramming (Centrum voor Wiskunde en Informatica, Amsterdam, 1987).
[298] B. Strazicky, “Some results concerning an algorithm for the discrete re-
course problem,” in: M.A.H. Dempster, Ed., Stochastic Programming (Aca-
demic Press, New York, NY, 1980).
[299] A.H. Stroud, Approximate Calculation of Multiple Integrals (Prentice-Hall,
Inc., Englewood Cliﬀs, NJ, 1971).
[300] J. Sun, L. Qi, and K-H. Tsai, “Solving stochastic transshipment problems
as network piecewise linear programs,” Technical Report, School of Mathe-
matics, The University of New South Wales (Kensington, UNSW, Australia,
1990).
[301] G.H. Symonds, “Chance-constrained equivalents of stochastic programming
problems,” Operations Research 16 (1968) pp. 1152–1159.
[302] T. Sz´antai, “Evaluation of a special multivariate gamma distribution func-
tion,” Mathematical Programming Study 27 (1986) pp. 1–16.
[303] G. Taguchi, Introduction to Quality Engineering (Asian Productivity Cen-
ter, Tokyo, Japan, 1986).
[304] G. Taguchi, E.A. Alsayed, and T. Hsiang, Quality Engineering in Produc-
tion Systems (McGraw-Hill Inc., New York, NY, 1989).
[305] H.A. Taha, Operations Research: An Introduction, Fifth edition (Macmil-
lan, New York, NY, 1992).
[306] S. Takriti, “On-line solution of linear programs with varying right-hand
sides,” Ph.D. Dissertation, Department of Industrial and Operations Engi-
neering, University of Michigan (Ann Arbor, MI, 1994).
[307] M.J. Todd and B.P. Burrell, “An extension of Karmarkar’s algorithm for
linear programming using dual variables,” Algorithmica 1 (1986) pp. 409–
424.
[308] D.M. Topkis and A.F. Veinott, Jr., “On the convergence of some feasi-
ble Eddirection algorithms for nonlinear programming,” SIAM Journal on
Control 5 (1967) pp. 268–279.
[309] C. Toregas, R. Swain, C. Revelle, and L. Bergmann, “The location of emer-
gency service facilities,” Operations Research 19 (1971) pp. 1363–1373.


## Page 427

408
References
[310] S. Uriasiev, “Adaptive stochastic quasigradient methods” in: Y. Ermoliev
and R. Wets, Eds., Numerical Techniques for Stochastic Optimization
(Springer-Verlag, Berlin, 1988) pp. 373–384.
[311] F.A. Valentine, Convex Sets (McGraw-Hill Inc., New York, NY, 1964).
[312] R. Van Slyke and R.J-B Wets, “L-shaped linear programs with application
to optimal control and stochastic programming,” SIAM Journal on Applied
Mathematics 17 (1969) pp. 638–663.
[313] R.J. Vanderbei, M.S. Meketon, and B.A. Freedman, “A modiﬁcation of Kar-
markar’s linear programming algorithm,” Algorithmica 1 (1986) pp. 395–
407.
[314] P. Varaiya and R.J-B Wets, “Stochastic dynamic optimization approaches
and computation” in: M. Iri and K. Tanabe, Eds., Mathematical Program-
ming: Recent Developments and Applications (Kluwer, Dordrecht, Nether-
lands, 1989) pp. 309–332.
[315] J.A. Ventura and D.W. Hearn, “Restricted simplicial decomposition for
convex constrained problems,” Mathematical Programming 59 (1993) pp.
71–85.
[316] J. Von Neumann and O. Morgenstern, Theory of Games and Economic
Behavior (Princeton University Press, Princeton, NJ, 1944).
[317] A. Wald, Statistical Decision Functions (John Wiley, Inc. New York, NY,
1950).
[318] D. Walkup and R.J-B Wets, “Stochastic programs with recourse,” SIAM
Journal on Applied Mathematics 15 (1967) pp. 1299–1314.
[319] D. Walkup and R.J-B Wets, “Stochastic programs with recourse II: on
the continuity of the objective,” SIAM Journal on Applied Mathematics 17
(1969) pp. 98–103.
[320] S.W. Wallace, “Decomposing the requirement space of a transportation
problem into polyhedral cones,” Mathematical Programming Study 28
(1986a) pp. 29–47.
[321] S.W. Wallace, “Solving stochastic programs with network recourse,” Net-
works 16 (1986b) pp. 295–317.
[322] S.W. Wallace, “A piecewise linear upper bound on the network recourse
function,” Networks 17 (1987) pp. 87–103.
[323] S.W. Wallace and R.J-B Wets, “Preprocessing in stochastic programming:
the case of linear programs,” ORSA Journal on Computing 4 (1992) pp.
45–59.
[324] S.W. Wallace and T.C. Yan, “Bounding multi-stage stochastic programs
from above,” Mathematical Programming 61 (1993) pp. 111–129.


## Page 428

References
409
[325] R.J-B Wets, “Programming under uncertainty: the equivalent convex pro-
gram,” SIAM Journal on Applied Mathematics 14 (1966) pp. 89–105.
[326] R.J-B Wets, “Characterization theorems for stochastic programs,” Mathe-
matical Programming 2 (1972) pp. 166–175.
[327] R.J-B Wets, “Stochastic programs with ﬁxed recourse: the equivalent de-
terministic problem,” SIAM Review 16 (1974) pp. 309–339.
[328] R.J-B Wets, “Convergence of convex functions, variational inequalities and
convex optimization problems” in: R.W. Cottle, F. Giannessi and J.-L.
Lions, Eds., Variational Inequalities and Complementarity Problems (John
Wiley, Inc., New York, NY, 1980a) pp. 375–404.
[329] R.J-B Wets, “Stochastic multipliers, induced feasibility and nonanticipa-
tivity in stochastic programming” in: M.A.H. Dempster, Ed., Stochastic
Programming (Academic Press, New York, NY, 1980b).
[330] R.J-B Wets, “Solving stochastic programs with simple recourse,” Stochas-
tics 10 (1983a) pp. 219–242.
[331] R.J-B Wets, “Stochastic programming: solution techniques and approxima-
tion schemes” in: A. Bachem, M. Gr¨otschel, and B. Korte, Eds., Mathemat-
ical Programming: State-of-the-Art 1982 (Springer-Verlag, Berlin, 1983b)
pp. 560–603.
[332] R.J-B Wets, “Large-scale linear programming techniques in stochastic pro-
gramming” in: Y. Ermoliev and R. Wets, Eds., Numerical Techniques for
Stochastic Optimization (Springer-Verlag, Berlin, 1988).
[333] R.J-B Wets, “Stochastic programming” in: G.L. Nemhauser, A.H.G. Rin-
nooy Kan, and M.J. Todd, Eds., Optimization (Handbooks in Operations
Research and Management Science; Vol. 1, North–Holland, Amsterdam,
Netherlands, 1990).
[334] R.J-B Wets and C. Witzgall, “Algorithms for frames and lineality spaces
of cones,” Journal of Research of the National Bureau of Standards Section
B 71B (1967) pp. 1–7.
[335] A.C. Williams, “A stochastic transportation problem,” Operations Research
11 (1963) pp. 759–770.
[336] A.C. Williams, “Approximation for stochastic linear programming,” SIAM
Journal on Applied Mathematics 14 (1966) pp. 668.
[337] R.J. Wittrock, “Advances in a nested decomposition algorithm for solving
staircase linear programs,” Technical Report SOL 83-2, Systems Optimiza-
tion Laboratory, Stanford University (Stanford, CA, 1983).
[338] R. Wollmer, “Two stage linear programming under uncertainty with 0-
1 integer ﬁrst stage variables,” Mathematical Programming 19 (1980) pp.
279–288.


## Page 429

410
References
[339] H. Wo´zniakowski, “Average-case complexity of multivariate integration,”
Bulletin of the American Mathematical Society (new series) 24 (1991) pp.
185–194.
[340] S.E. Wright, “Primal-dual aggregation and disaggregation for stochastic
linear programs,” Mathematics of Operations Research 19 (1994) pp. 893–
908.
[341] D. Yang and S.A. Zenios, “A scalable parallel interior point algorithm
for stochastic linear programming and robust optimization,” Report 95-07,
Department of Public and Business Administration, University of Cyprus
(Nicosia, Cyprus, 1995).
[342] Y. Ye, “Karmarkar’s algorithm and the ellipsoid method,” Operations Re-
search Letters 6 (1987) pp. 177–182.
[343] Y. Ye and M. Kojima, “Recovering optimal dual solutions in karmarkar’s
polynomial algorithm for linear programming,” Mathematical Programming
39 (1987) pp. 305–317.
[344] J. ˇZ´aˇckov´a, “On minimax solutions of stochastic linear programming prob-
lems,” ˇCasopis pro Pˇestov´an´i Matematiky 91 (1966) pp. 423–430.
[345] S.A. Zenios, Financial Optimization (Cambridge University Press, Cam-
bridge, UK, 1992).
[346] W.T. Ziemba, “Computational algorithms for convex stochastic programs
with simple recourse,” Operations Research 18 (1970) pp. 414–431.
[347] W.T. Ziemba and R.G. Vickson, Stochastic Optimization Models in Finance
(Academic Press, New York, NY, 1975).
[348] P. Zipkin, “Bounds for row-aggregation in linear programming,” Operations
Research 28 (1980a) pp. 903–916.
[349] P. Zipkin, “Bounds on the eﬀect of aggregating variables in linear pro-
grams,” Operations Research 28 (1980b) pp. 403–418.


## Page 430

Author Index
Abrahamson, 243
Andreou, 378
Anstreicher, 183, 184
Ariyawansa, 174
Ashford, 366, 367
Attouch, 324
Avriel, 145
Barnes, 183
Bazaraa, 95, 100, 126, 195, 216, 347
Beale, 54, 226, 229, 366–368
Bellman, 69
Ben-Tal, 61, 288
Benders, 157
Bereanu, 90
Berger, 67
Berman, 63
Bertsimas, 64
Bienstock, 277
Billingsley, 323
Birge, 99, 132, 134, 142, 144–146,
166, 167, 179, 182, 183, 185,
186, 189, 190, 229, 231, 233,
234, 243, 289–292, 296, 300,
304, 305, 308, 309, 312, 313,
316, 319–321, 323, 324, 326,
327, 334, 359, 361, 363–365,
370, 378, 383
Bitran, 362, 366, 369
Black, 379
Blackwell, 70
Blair, 110
Borell, 105
Brumelle, 43
Burrell, 183
Carøe, 256
Carpenter, 187, 189
Ceder, 61
Chao, 144
Charnes, 25, 42, 104, 107
Chiu, 63
Choi, 187
Chu, 190
Chung, 50, 280
Chv´atal, 52, 76
Cipra, 316, 352
Clarke, 324
Cooper, 25, 42, 104, 107
Cox, 379
Czyzyk, 191


## Page 431

412
Author Index
Dantzig, 42, 52, 54, 157, 174, 176,
195, 314, 315, 335, 336, 368
Dawson, 303
De´ak, 304, 331, 350
DeGroot, 67
Dempster, 71, 90, 94, 132, 134, 218
Demyanov, 232
Dikin, 183
Dul´a, 310, 316, 319
Dupaˇc, 344
Dupaˇcov´a, 315, 333
Eaves, 218
Edirisinghe, 306, 316
Edmundson, 288, 293
Eisner, 100
Eppen, 62, 375, 376
Ermoliev, 43, 232, 256, 316, 344,
346, 347
Escudero, 42
Feller, 301, 302
Ferguson, 42, 195
Fine, 376
Fl˚am, 132, 134, 135
Fleming, 71
Forrest, 366, 367
Fourer, 26, 191, 194
Fox, 334
Frantzeskakis, 367, 369, 370
Frauendorfer, 288–290, 293,
305–307, 315
Freedman, 183
Freund, 189, 376
Gaivoronski, 316, 345
Galambos, 280
Gartska, 71, 108, 174
Gassmann, 43, 167, 170, 174, 236,
243, 292, 304, 350
Gay, 26, 183, 184
Gendreau, 121
Geoﬀrion, 174, 300
Glassey, 234
Glynn, 335, 336
Graves, 376, 382
Grinold, 132, 359
Harrison, 72
Haugland, 174
Hearn, 218
Heyman, 69
Higle, 331, 335, 338, 340, 341
Hiriart-Urruty, 99
Ho, 190, 234
Hoeﬀding, 301
Hogan, 107
Holmes, 186, 190
Howard, 70
Huang, 288
Huber, 332
Hudson, 174
IBM, 383
Infanger, 243, 336, 337
Jagganathan, 320, 351, 352
Jaillet, 64
Jarrow, 378, 379
Jarvis, 195
Jensen, 140, 288
Jeroslow, 110
Jordan, 376, 382
Kall, 69, 91, 94, 179, 205, 288–290,
316, 324
Kallberg, 20, 105, 194, 252
Kallio, 130
Kalman, 71
Kan, 104
Kao, 43
Karmarkar, 183, 184
Karr, 314
Kemperman, 315
Kernighan, 26
Kibzun, 104
King, 43, 218, 323, 327, 328, 332,
333
Kiwiel, 232
Klein Haneveld, 100, 370
Kojima, 184
Krein, 314
Kurbakovskiy, 104
Kushner, 71, 344
Kusy, 252
Lageweg, 281
Laporte, 120, 121, 256, 261, 268


## Page 432

Author Index
413
Larson, 63
Lasdon, 166
Lemar´echal, 232
Lenstra, 280
Loute, 190
Louveaux, 34, 59, 115, 120, 130,
144, 166, 167, 209, 210, 234,
245, 246, 249, 251, 256, 261,
264, 267, 268, 277
Lustig, 187, 189, 191
Madansky, 138, 140, 174, 288, 292,
293
Maddox, 305, 370
Mangasarian, 140
Manne, 42, 144, 234
Markowitz, 61
Marsten, 189
Marti, 321
Martin, 62, 375
Mayer, 205
McGill, 43
McKenzie, 134
Mehrotra, 191
Meketon, 183
Mercure, 120, 261
Michel, 324
Miller, 106
Minty, 220
Mirzoachmedov, 349
Monma, 187
Monro, 346
Mordukhovich, 324
Morgenstern, 61
Morris, 107
Morton, 236
Mulvey, 20, 187, 189, 219, 252
Murtagh, 95
Murty, 52, 231
Myers, 375
Nazareth, 178, 225, 229
Nedeva, 316
Nemhauser, 110, 254
Niederreiter, 334
Nielsen, 219
No¨el, 231, 234, 243
Norkin, 256
Nudel’man, 314
Odoni, 64
Olsen, 100
Papagaki-Papoulias, 90
Parikh, 106, 107
Peeters, 59
Penot, 324
Pereira, 234
Pﬂug, 349
Pint´er, 301, 303
Pinto, 234
Plambeck, 232
Porteus, 130
Powell, 367, 369, 370
Pradhan, 304
Pr´ekopa, 25, 42, 105, 106, 301, 303,
304, 329
Psaraftis, 61, 280
Qi, 99, 185, 186, 190, 196, 230, 231,
304, 323, 324, 326, 327
Queyranne, 43
Raiﬀa, 68, 138
Richels, 42
Rinnooy Kan, 280
Rishel, 71
Robbins, 346
Robinson, 97
Rockafellar, 90, 98–100, 124, 125,
132, 133, 217, 219, 220, 300,
318, 326, 332, 333, 366
R¨omisch, 97, 333, 334
Rosen, 140
Ross, 69, 379
Royden, 97, 314
Rubinstein, 304
Rudd, 378, 379
Ruszczy´nski, 200, 202, 205, 236,
252, 256
Rutenberg, 174
Salinetti, 304
Sankoﬀ, 303
Sarkar, 366
Sathe, 304
Saunders, 95
Scarf, 320
Schlaifer, 138


## Page 433

414
Author Index
Scholes, 379
Schrage, 62, 375
Schultz, 97, 120, 333, 334
S´eguin, 121
Sen, 331, 335, 338, 340, 341
Shah, 304
Shanno, 187, 189
Shapiro, 277, 334
Sharpe, 378
Sherali, 195
Shetty, 95, 100, 126, 216, 347
Simchi-Levi, 280
Smeers, 34, 144, 231, 234, 243, 249
Sobel, 69
Somly´ody, 42, 218
Stougie, 112, 120, 279, 280
Stoyan, 288
Strazicky, 179
Stroud, 286
Sun, 196, 231
Symonds, 42, 108
Sz´antai, 42, 303, 304, 350
Taguchi, 37
Taha, 254, 370
Takriti, 281
Taylor, 366, 367
Teboulle, 61, 321
Tharakan, 61
Thompson, 107
Tind, 256
Todd, 183
Topkis, 218
Toregas, 65
Tsai, 196, 231
Uriasiev, 348, 349
Valentine, 319
van der Vlerk, 115, 120, 264, 267
Van Hamme, 261
Van Slyke, 157, 235
Vanderbei, 183, 189
Varaiya, 28
Vasiliev, 232
Veinott, 218
Ventura, 218
Vickson, 20
Vladimirou, 20, 219, 252
Von Neumann, 61
Wagner, 106
Wald, 67, 314
Walkup, 87, 88, 90, 209
Wallace, 69, 171, 174, 196, 289,
308, 309, 313, 366
Watson, 368
Wein, 72
Wets, 28, 42, 43, 71, 87–92, 94,
96–100, 103, 105, 108, 132,
157, 170, 171, 174, 179, 192,
209, 217–219, 225, 229, 235,
289–292, 296, 300, 309, 312,
313, 316, 320, 321, 323, 324,
326–328, 333, 364–366
White, 194, 252
Williams, 58, 145, 226
Wittrock, 236
Witzgall, 92
Wolfe, 157
Wollmer, 256
Wolsey, 110, 254
Wo´zniakowski, 334
Wright, 359
Yan, 366
Yanasse, 362, 366, 369
Yang, 191
Ye, 183, 184
ˇZ´aˇckov´a, 315
Zangwill, 218
Zenios, 20, 191, 219
Ziemba, 20, 105, 194, 225, 230, 252,
288, 292
Zipkin, 359


## Page 434

Subject Index
ρ-approximation, 263
A priori optimization, 64, 261
a.s., see almost surely
absolutely continuous, 91, 112
abstract linear program, 314
aﬃne, 77
hull, 77, 293
space, 77
aﬃne scaling, see scaling
aggregation, 32, 359
almost surely, 54, 103
ancestor, 130, 234, 245
annuity, 32
approximation, 41, 118, 278, 285
polynomial, 287
trapezoidal, 293
arborescent, 130
artiﬁcial variable, 74
atom, 289
augmented Lagrangian, see
Lagrangian
Ball, 77
barycentric, 310
coordinates, 293
basis, 73
working, 181
factorization, 179
Bayesian, 351
Benders decomposition, see
decomposition
block angular, 157
block separable, see separable
Boole-Bonferroni inequalities, see
inequality
Borel ﬁeld, 291
bounded, 77
bounding, see bounds
bounds, 145, 323, 362, 365
branch and bound, 254
branch and cut, 254
bunching, 114, 170, 243
Capacity, 375
capacity expansion, 129, 174
capital asset pricing model, 378
Carath´eodory’s theorem, 292, 319
cell, 207, 245, 289
central limit theorem, 334
chance constraint, see probabilistic
constraint
Chebyshev inequality, see inequality
clairvoyancy, 280


## Page 435

416
Subject Index
closed, 77
column splitting, 186
compact, 77
complement, 303
complementarity, 75, 108
complementary, 177, 235
slackness, 75
complete recourse, see recourse
complexity, 184
concave, 20, 23, 77
conditional expectation, see
expectation
cone, 77
conﬁdence interval, 104
conjugate, 79, 300
connected, 104, 319
contingency claim, 378
continuous, 14
relaxation, 256, 261
time, 72
control, 20, 28
convergence, 79
epi, see epi-convergence
in distribution, 323
pointwise, 79
convex, 14, 34, 123
combination, 76
function, 77
proper, 77
hull, 76, 176, 216, 300, 312, 319
set, 76
simplex method, 230
cumulative probability distribution,
17
cut, 199
feasibility, 158, 254
optimality, 158, 254, 255, 259
valid, 254
Dantzig-Wolfe, see decomposition
decision, 52
analysis, 67, 69, 138
rule, 71
theory, 68
tree, 25
decomposition, 129, 194
Benders, 157, 254
Dantzig-Wolfe, 157, 174, 243
nested, 234, 245, 383
regularized, 199, 246
stochastic, see stochastic
degeneracy, 243
density, 51
derivative, 17
descendant, 130, 235
deterministic, 29
equivalent, 35, 65, 84, 86, 104,
106, 120, 128, 156, 233
program, 55
model, 20, 25, 26, 32
diagonal quadratic approximation,
252
dictionary, 73
diﬀerentiable, 16, 77, 91, 120
continuously, 332
G- or Gˆateaux, 78
dimension, 77
directional derivative, 77, 127
Hadamard, 78
discount, 359, 375, 378
discounting, 19
discrete variables, see integer
variables
distribution
Dirichlet, 352
function, 17
problem, 90, 138
dom, see eﬀective domain
downside risk, see risk, downside
dual, 75, 187, 312
ascent, 216
block angular, 157
Lagrangian, 78
program, 300
simplex, 76
duality, 52, 125, 256
gap, 100
strong, 79
weak, 79
dynamic, 29
program, 69, 128
E-model, 104
Edmundson-Madansky bound, see
inequality
eﬀective domain, 77, 124
emergency, 63, 65
empirical measure, 327


## Page 436

Subject Index
417
end eﬀects, 32, 238, 359
energy, 42, 144
entering variable, 73
EPEV, see expectation of pairs
expected value
epi-convergence, 324
epigraph, 77, 324
essentially bounded, 97, 133
event, 50, 85
EVPI, see expected value of perfect
information
exhaustible resources, 144
expectation, 11, 51
conditional, 287, 309, 355, 360
of pairs expected value, 148
expected
shortage, 115
surplus, 115
value
problem, 139
solution, 10, 24, 139
value of perfect information, 9,
137
value of sample information, 352
ext, see extreme
extensive form, see stochastic
program
extremal measure, 315
extreme
point, 73, 175, 291
rays, 175
Factorization, 185, 205
basis, see basis
failure rate, 106
Farkas lemma, 76, 127
feasibility
cut, see cut
set, 85, 124, 129
elementary, 86
second-stage, 86, 112, 207
feasible region, 76
Fenchel duality, 125
ﬁnance, 20, 129, 194, 252
ﬁnite generation, 217
ﬁrst-stage, 8, 10, 85
binary, 18, 268
decision, 52
ﬂeet assignment, 42, 195
forestry, 43
Frank-Wolfe method, 225
free, 75
full decomposability, 170
G-diﬀerentiable, see diﬀerentiable
generalized
network, 26, 195
programming, 176, 195, 226, 299,
315, 382
moment, see moment
Gomory function, 110, 257
gradient, 77
Hedging, 9, 379
here-and-now, 138
Hessian, 78
heuristic, 279
history process, 133
horizon, 21, 25, 32, 128, 238
hull
convex, 264
hyperplane, 77
supporting, 78
Implicit representation, see
stochastic program
importance sampling, 335
improving direction, 76
independence
linear, 315
indicator function, 76
induced constraint, 62, 164
inequality
Bonferroni, 350
Boole-Bonferroni, 303
Chebyshev, 301
Edmundson-Madansky, 288, 293,
354
Jensen, 140, 288, 303, 354
infeasible, 74
inﬁnite horizon, 359
inner linearization, 157, 174, 218,
234
int, see interior
integer variables, 36
integrable, 125
function, 97
integration


## Page 437

418
Subject Index
integration (continued)
multiple, 286
numerical, 286
interior, 77
interior point methods, 179
Jensen’s inequality, 140
just-in-time, 249
K-K-T, see Karush-Kuhn-Tucker
Kalman ﬁltering, 71
Karush-Kuhn-Tucker, 15, 78, 95,
211, 250, 317
L-shaped, 90, 156, 254, 296
integer, 253, 255
Lagrangian, 78, 215, 252
augmented, 218
large-scale optimization, 130, 156
large-scale programming, see
large-scale optimization
leaving variable, 73
Lebesgue measure, 327
level set, 316
linear
program, 5, 51
quadratic, 217
Gaussian, 71
linearization, 225
Lipschitz, 78, 90, 332
locally, 78
local, 78
location, 55, 63, 65, 261
logarithmically concave, 105
lower semicontinuous, 124, 326
Major iteration, 167
makespan, 279
mapping
multifunction, 327
marginal, 309
value, 75
Markov decision process, 69, 132
mathematical expectation, see
expectation
maximal monotone operator, 220
mean value problem, see expected
value problem
mean-variance model, 61
measurable, 97, 122, 327
measure, 49, 97
mixed integer, 259, 276
modeling language, 26
moment, 51
generalized, 305, 314, 382
second, 288
Monte Carlo
method, 331
multicut, 166, 199, 243, 259, 265
multifunction, 327
multiple integration, see integration
multiplier, 75, 158, 235
dual, 316
multistage, 18, 25, 29, 59, 128, 233,
277
Nested decomposition, see
decomposition
network, 192, 195, 252, 305
generalized, see generalized
network
news vendor, 14, 15, 229
newsboy, see news vendor
node
pendant, 254
terminal, 256
nonanticipative, 21, 25, 26, 71, 96,
125, 128, 133, 187, 218, 354
nonanticipativity, see nonanticipa-
tive
nonconvex, 324
nondiﬀerentiable, 287
nonlinear, 20, 28, 41, 122, 225, 363
programming, 76, 287
normal
cone, 96, 125, 204
distribution, 106, 119, 304
numerical integration, see
integration
numerical stability, 205
Oil spills, 61
optimality conditions, 93
optimality cut, see cut
option value, 375
outer linearization, 157, 234
P-model, 104


## Page 438

Subject Index
419
PAIRS problem, 146
parallel, 77
processing, 174, 236
parametric optimization, 318
partial splitting, 189
penalty, 71
pendant, see node
period, 59
PERT network, 305, 370
phase
one, 73, 163, 256, 315
two, 74
piecewise
constant, 117
linear, 23, 78, 89, 117, 287
quadratic, see quadratic
pivot, 73
polar matrix, 89
polynomial approximation, see
approximation
pos, see positive hull
positive
deﬁnite, 207, 218
hull, 88, 162
linear basis, 310
semi-deﬁnite, 207, 245
positively homogeneous, 90, 309
possibility interpretation, 86
power generation, 28, 164
preprocessing, 174
price eﬀect, 18
primal-dual, 100
probabilistic
constraint, 35, 103, 120, 287, 301
programming, 4, 25, 64
probability, 50
space, 49, 50
production, 42, 361
progressive hedging, 219, 252
projection, 77, 133, 344
proper convex function, 94
proximal point method, 220
pseudo-random, 335
Quadratic, 28, 41, 78, 199, 244
piecewise, 206
quadrature, 287
quantile, 17, 51, 104
quasi-concave, 105
quasi-gradient, see stochastic
quasi-random, 334, 335
Random
variable, 49, 52, 61
continuous, 11, 16, 34, 51, 84
discrete, 11, 34, 50, 84, 118
normal, 336
vector, 10, 11, 87
rc, see recession cone
recession
cone, 94
direction, 94, 177
recourse, 138
block separable, see separable
complete, 92, 164
ﬁxed, 11, 84, 123, 128, 142
function, 11, 85
matrix, 84
network, 196
nonlinear, see nonlinear
problem, 24
program, 52
relatively complete, 92, 125
simple, 41, 42, 58, 92, 107, 192,
225, 251, 287, 309, 369
integer, 114, 262
rectangular region, 293
recursion, 128
reduced gradient, 230
reﬁnement, 290, 300
regularity, 78, 123, 126
condition, 99
regularized decomposition, see
decomposition
relative interior, 125
reliability, 35, 41, 106
ri, see relative interior
risk
aversion, 19, 61, 379
downside, 62
neutral, 379
robust, 71
routing, 120, 254
S-neighbors, 271
salvage value, 32, 369
sample information, 352
sampling measure, 327


## Page 439

420
Subject Index
scaling
aﬃne, 183
scenario, 21, 22, 50, 61, 129, 138,
146
reference, 146
scheduling, 279
Schur complement, 186, 196
second moment, 87, 129
second-stage, 8, 10, 52, 85, 89
integer, 18
value function, 55
separability, see separable
separable, 78, 114, 177, 226, 274,
287, 293, 299, 308, 362
block, 20, 130, 277
function, 93
shadow price, 75
shortage, 262
sifting, 174
simple recourse, see recourse
simplex, 292, 310
algorithm, 73
simplicial region, 292
slack variables, 73
Slater condition, 78, 123
solution, 73
basic, 73
feasible, 73
optimal, 73
SPEV, see sum of pairs expected
values
sports, 43
stability, 96
staﬃng, 43
stage, 52, 59, 70, 128
state, 70, 71, 129
of the world, 50
variables, 28
static, 29
statistical decision theory, 67
stochastic
decomposition, 338
independence, 293
program
extensive form, 8, 11, 62, 156,
233
implicit representation, 11, 63
integer, 109
with recourse, 122, 128
quasi-gradient, 343
queue median, 63
subgradient, see subgradient
stopping criteria, 296
strategic, 50
subadditive, 110
subdiﬀerential, 78, 93
generalized, 324
subgradient, 78, 125, 141, 209, 304,
344
method, 216
stochastic, 344
sublinear, 316
suboptimization, 326
sum of pairs expected values, 146
support, 54, 84, 128, 156
supporting hyperplane, see
hyperplane, 159
surplus, 262
Technology matrix, 84
tender, 85, 114, 178, 229
terminal conditions, 128
time horizon, see horizon
total second moment, 317
totally unimodular, 113
translation, 77
transportation, 231
model, 58
trapezoidal approximation, see
approximation
traveling salesperson problem, 64
tree, 21
decision, 22
two-point support, 319
two-stage, 59, 84
stochastic program with recourse,
10, 54, 122
Unbiased estimates, 350
unbounded, 73
utility, 20, 23, 25, 61, 69, 70
V-model, 104
valid, 255
value
of information, 127
function, 11, 89, 110


## Page 440

Subject Index
421
of the stochastic solution, 10, 18,
139
variance, 51
vehicle allocation, 367
VSS, see stochastic solution
Wait-and-see, 138, 276, 280
water resource, 42, 218
working basis, see basis
worst case, 19, 184
Yield management, 43
