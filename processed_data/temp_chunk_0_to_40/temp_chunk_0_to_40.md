# temp_chunk_0_to_40



## Page 1

Convex Optimization


## Page 2



## Page 3

Convex Optimization
Stephen Boyd
Department of Electrical Engineering
Stanford University
Lieven Vandenberghe
Electrical Engineering Department
University of California, Los Angeles


## Page 4

cambridge university press
Cambridge, New York, Melbourne, Madrid, Cape Town, Singapore, S˜ao Paolo, Delhi
Cambridge University Press
The Edinburgh Building, Cambridge, CB2 8RU, UK
Published in the United States of America by Cambridge University Press, New York
http://www.cambridge.org
Information on this title: www.cambridge.org/9780521833783
© Cambridge University Press 2004
This publication is in copyright. Subject to statutory exception
and to the provisions of relevant collective licensing agreements,
no reproduction of any part may take place without
the written permission of Cambridge University Press.
First published 2004
Seventh printing with corrections 2009
Printed in the United Kingdom at the University Press, Cambridge
A catalogue record for this publication is available from the British Library
Library of Congress Cataloguing-in-Publication data
Boyd, Stephen P.
Convex Optimization / Stephen Boyd & Lieven Vandenberghe
p. cm.
Includes bibliographical references and index.
ISBN 0 521 83378 7
1. Mathematical optimization. 2. Convex functions. I. Vandenberghe, Lieven. II. Title.
QA402.5.B69 2004
519.6–dc22
2003063284
ISBN 978-0-521-83378-3 hardback
Cambridge University Press has no responsiblity for the persistency or accuracy of URLs
for external or third-party internet websites referred to in this publication, and does not
guarantee that any content on such websites is, or will remain, accurate or appropriate.


## Page 5

For
Anna, Nicholas, and Nora
Dani¨el and Margriet


## Page 6



## Page 7

Contents
Preface
xi
1
Introduction
1
1.1
Mathematical optimization . . . . . . . . . . . . . . . . . . . . . . . .
1
1.2
Least-squares and linear programming
. . . . . . . . . . . . . . . . . .
4
1.3
Convex optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
1.4
Nonlinear optimization
. . . . . . . . . . . . . . . . . . . . . . . . . .
9
1.5
Outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
1.6
Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
I
Theory
19
2
Convex sets
21
2.1
Aﬃne and convex sets . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
2.2
Some important examples . . . . . . . . . . . . . . . . . . . . . . . . .
27
2.3
Operations that preserve convexity . . . . . . . . . . . . . . . . . . . .
35
2.4
Generalized inequalities . . . . . . . . . . . . . . . . . . . . . . . . . .
43
2.5
Separating and supporting hyperplanes . . . . . . . . . . . . . . . . . .
46
2.6
Dual cones and generalized inequalities . . . . . . . . . . . . . . . . . .
51
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
59
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
60
3
Convex functions
67
3.1
Basic properties and examples
. . . . . . . . . . . . . . . . . . . . . .
67
3.2
Operations that preserve convexity . . . . . . . . . . . . . . . . . . . .
79
3.3
The conjugate function . . . . . . . . . . . . . . . . . . . . . . . . . .
90
3.4
Quasiconvex functions . . . . . . . . . . . . . . . . . . . . . . . . . . .
95
3.5
Log-concave and log-convex functions
. . . . . . . . . . . . . . . . . . 104
3.6
Convexity with respect to generalized inequalities . . . . . . . . . . . . 108
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113


## Page 8

viii
Contents
4
Convex optimization problems
127
4.1
Optimization problems
. . . . . . . . . . . . . . . . . . . . . . . . . . 127
4.2
Convex optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
4.3
Linear optimization problems . . . . . . . . . . . . . . . . . . . . . . . 146
4.4
Quadratic optimization problems . . . . . . . . . . . . . . . . . . . . . 152
4.5
Geometric programming . . . . . . . . . . . . . . . . . . . . . . . . . . 160
4.6
Generalized inequality constraints . . . . . . . . . . . . . . . . . . . . . 167
4.7
Vector optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
5
Duality
215
5.1
The Lagrange dual function . . . . . . . . . . . . . . . . . . . . . . . . 215
5.2
The Lagrange dual problem . . . . . . . . . . . . . . . . . . . . . . . . 223
5.3
Geometric interpretation
. . . . . . . . . . . . . . . . . . . . . . . . . 232
5.4
Saddle-point interpretation . . . . . . . . . . . . . . . . . . . . . . . . 237
5.5
Optimality conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
5.6
Perturbation and sensitivity analysis
. . . . . . . . . . . . . . . . . . . 249
5.7
Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253
5.8
Theorems of alternatives
. . . . . . . . . . . . . . . . . . . . . . . . . 258
5.9
Generalized inequalities . . . . . . . . . . . . . . . . . . . . . . . . . . 264
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273
II
Applications
289
6
Approximation and ﬁtting
291
6.1
Norm approximation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291
6.2
Least-norm problems
. . . . . . . . . . . . . . . . . . . . . . . . . . . 302
6.3
Regularized approximation
. . . . . . . . . . . . . . . . . . . . . . . . 305
6.4
Robust approximation . . . . . . . . . . . . . . . . . . . . . . . . . . . 318
6.5
Function ﬁtting and interpolation . . . . . . . . . . . . . . . . . . . . . 324
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 343
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 344
7
Statistical estimation
351
7.1
Parametric distribution estimation
. . . . . . . . . . . . . . . . . . . . 351
7.2
Nonparametric distribution estimation
. . . . . . . . . . . . . . . . . . 359
7.3
Optimal detector design and hypothesis testing
. . . . . . . . . . . . . 364
7.4
Chebyshev and Chernoﬀbounds
. . . . . . . . . . . . . . . . . . . . . 374
7.5
Experiment design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 384
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 392
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 393


## Page 9

Contents
ix
8
Geometric problems
397
8.1
Projection on a set
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 397
8.2
Distance between sets . . . . . . . . . . . . . . . . . . . . . . . . . . . 402
8.3
Euclidean distance and angle problems . . . . . . . . . . . . . . . . . . 405
8.4
Extremal volume ellipsoids
. . . . . . . . . . . . . . . . . . . . . . . . 410
8.5
Centering
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 416
8.6
Classiﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 422
8.7
Placement and location . . . . . . . . . . . . . . . . . . . . . . . . . . 432
8.8
Floor planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 438
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 446
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 447
III
Algorithms
455
9
Unconstrained minimization
457
9.1
Unconstrained minimization problems
. . . . . . . . . . . . . . . . . . 457
9.2
Descent methods
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 463
9.3
Gradient descent method . . . . . . . . . . . . . . . . . . . . . . . . . 466
9.4
Steepest descent method . . . . . . . . . . . . . . . . . . . . . . . . . 475
9.5
Newton’s method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 484
9.6
Self-concordance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 496
9.7
Implementation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 508
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 513
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 514
10 Equality constrained minimization
521
10.1 Equality constrained minimization problems
. . . . . . . . . . . . . . . 521
10.2 Newton’s method with equality constraints . . . . . . . . . . . . . . . . 525
10.3 Infeasible start Newton method . . . . . . . . . . . . . . . . . . . . . . 531
10.4 Implementation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 542
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 556
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 557
11 Interior-point methods
561
11.1 Inequality constrained minimization problems
. . . . . . . . . . . . . . 561
11.2 Logarithmic barrier function and central path
. . . . . . . . . . . . . . 562
11.3 The barrier method . . . . . . . . . . . . . . . . . . . . . . . . . . . . 568
11.4 Feasibility and phase I methods . . . . . . . . . . . . . . . . . . . . . . 579
11.5 Complexity analysis via self-concordance . . . . . . . . . . . . . . . . . 585
11.6 Problems with generalized inequalities . . . . . . . . . . . . . . . . . . 596
11.7 Primal-dual interior-point methods . . . . . . . . . . . . . . . . . . . . 609
11.8 Implementation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 615
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 621
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 623


## Page 10

x
Contents
Appendices
631
A Mathematical background
633
A.1
Norms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 633
A.2
Analysis
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 637
A.3
Functions
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 639
A.4
Derivatives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 640
A.5
Linear algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 645
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 652
B Problems involving two quadratic functions
653
B.1
Single constraint quadratic optimization . . . . . . . . . . . . . . . . . 653
B.2
The S-procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 655
B.3
The ﬁeld of values of two symmetric matrices . . . . . . . . . . . . . . 656
B.4
Proofs of the strong duality results . . . . . . . . . . . . . . . . . . . . 657
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 659
C Numerical linear algebra background
661
C.1
Matrix structure and algorithm complexity . . . . . . . . . . . . . . . . 661
C.2
Solving linear equations with factored matrices . . . . . . . . . . . . . . 664
C.3
LU, Cholesky, and LDLT factorization
. . . . . . . . . . . . . . . . . . 668
C.4
Block elimination and Schur complements . . . . . . . . . . . . . . . . 672
C.5
Solving underdetermined linear equations . . . . . . . . . . . . . . . . . 681
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 684
References
685
Notation
697


## Page 11

Preface
This book is about convex optimization, a special class of mathematical optimiza-
tion problems, which includes least-squares and linear programming problems. It
is well known that least-squares and linear programming problems have a fairly
complete theory, arise in a variety of applications, and can be solved numerically
very eﬃciently. The basic point of this book is that the same can be said for the
larger class of convex optimization problems.
While the mathematics of convex optimization has been studied for about a
century, several related recent developments have stimulated new interest in the
topic. The ﬁrst is the recognition that interior-point methods, developed in the
1980s to solve linear programming problems, can be used to solve convex optimiza-
tion problems as well. These new methods allow us to solve certain new classes
of convex optimization problems, such as semideﬁnite programs and second-order
cone programs, almost as easily as linear programs.
The second development is the discovery that convex optimization problems
(beyond least-squares and linear programs) are more prevalent in practice than
was previously thought.
Since 1990 many applications have been discovered in
areas such as automatic control systems, estimation and signal processing, com-
munications and networks, electronic circuit design, data analysis and modeling,
statistics, and ﬁnance. Convex optimization has also found wide application in com-
binatorial optimization and global optimization, where it is used to ﬁnd bounds on
the optimal value, as well as approximate solutions. We believe that many other
applications of convex optimization are still waiting to be discovered.
There are great advantages to recognizing or formulating a problem as a convex
optimization problem. The most basic advantage is that the problem can then be
solved, very reliably and eﬃciently, using interior-point methods or other special
methods for convex optimization. These solution methods are reliable enough to be
embedded in a computer-aided design or analysis tool, or even a real-time reactive
or automatic control system. There are also theoretical or conceptual advantages
of formulating a problem as a convex optimization problem. The associated dual
problem, for example, often has an interesting interpretation in terms of the original
problem, and sometimes leads to an eﬃcient or distributed method for solving it.
We think that convex optimization is an important enough topic that everyone
who uses computational mathematics should know at least a little bit about it.
In our opinion, convex optimization is a natural next topic after advanced linear
algebra (topics like least-squares, singular values), and linear programming.


## Page 12

xii
Preface
Goal of this book
For many general purpose optimization methods, the typical approach is to just
try out the method on the problem to be solved.
The full beneﬁts of convex
optimization, in contrast, only come when the problem is known ahead of time to
be convex. Of course, many optimization problems are not convex, and it can be
diﬃcult to recognize the ones that are, or to reformulate a problem so that it is
convex.
Our main goal is to help the reader develop a working knowledge of
convex optimization, i.e., to develop the skills and background needed
to recognize, formulate, and solve convex optimization problems.
Developing a working knowledge of convex optimization can be mathematically
demanding, especially for the reader interested primarily in applications. In our
experience (mostly with graduate students in electrical engineering and computer
science), the investment often pays oﬀwell, and sometimes very well.
There are several books on linear programming, and general nonlinear pro-
gramming, that focus on problem formulation, modeling, and applications. Several
other books cover the theory of convex optimization, or interior-point methods and
their complexity analysis. This book is meant to be something in between, a book
on general convex optimization that focuses on problem formulation and modeling.
We should also mention what this book is not. It is not a text primarily about
convex analysis, or the mathematics of convex optimization; several existing texts
cover these topics well. Nor is the book a survey of algorithms for convex optimiza-
tion. Instead we have chosen just a few good algorithms, and describe only simple,
stylized versions of them (which, however, do work well in practice). We make no
attempt to cover the most recent state of the art in interior-point (or other) meth-
ods for solving convex problems. Our coverage of numerical implementation issues
is also highly simpliﬁed, but we feel that it is adequate for the potential user to
develop working implementations, and we do cover, in some detail, techniques for
exploiting structure to improve the eﬃciency of the methods. We also do not cover,
in more than a simpliﬁed way, the complexity theory of the algorithms we describe.
We do, however, give an introduction to the important ideas of self-concordance
and complexity analysis for interior-point methods.
Audience
This book is meant for the researcher, scientist, or engineer who uses mathemat-
ical optimization, or more generally, computational mathematics. This includes,
naturally, those working directly in optimization and operations research, and also
many others who use optimization, in ﬁelds like computer science, economics, ﬁ-
nance, statistics, data mining, and many ﬁelds of science and engineering. Our
primary focus is on the latter group, the potential users of convex optimization,
and not the (less numerous) experts in the ﬁeld of convex optimization.
The only background required of the reader is a good knowledge of advanced
calculus and linear algebra. If the reader has seen basic mathematical analysis (e.g.,
norms, convergence, elementary topology), and basic probability theory, he or she
should be able to follow every argument and discussion in the book. We hope that


## Page 13

Preface
xiii
readers who have not seen analysis and probability, however, can still get all of the
essential ideas and important points. Prior exposure to numerical computing or
optimization is not needed, since we develop all of the needed material from these
areas in the text or appendices.
Using this book in courses
We hope that this book will be useful as the primary or alternate textbook for
several types of courses. Since 1995 we have been using drafts of this book for
graduate courses on linear, nonlinear, and convex optimization (with engineering
applications) at Stanford and UCLA. We are able to cover most of the material,
though not in detail, in a one quarter graduate course. A one semester course allows
for a more leisurely pace, more applications, more detailed treatment of theory,
and perhaps a short student project. A two quarter sequence allows an expanded
treatment of the more basic topics such as linear and quadratic programming (which
are very useful for the applications oriented student), or a more substantial student
project.
This book can also be used as a reference or alternate text for a more traditional
course on linear and nonlinear optimization, or a course on control systems (or
other applications area), that includes some coverage of convex optimization. As
the secondary text in a more theoretically oriented course on convex optimization,
it can be used as a source of simple practical examples.
Acknowledgments
We have been developing the material for this book for almost a decade. Over the
years we have beneﬁted from feedback and suggestions from many people, including
our own graduate students, students in our courses, and our colleagues at Stanford,
UCLA, and elsewhere. Unfortunately, space limitations and shoddy record keeping
do not allow us to name everyone who has contributed.
However, we wish to
particularly thank A. Aggarwal, V. Balakrishnan, A. Bernard, B. Bray, R. Cottle,
A. d’Aspremont, J. Dahl, J. Dattorro, D. Donoho, J. Doyle, L. El Ghaoui, P. Glynn,
M. Grant, A. Hansson, T. Hastie, A. Lewis, M. Lobo, Z.-Q. Luo, M. Mesbahi, W.
Naylor, P. Parrilo, I. Pressman, R. Tibshirani, B. Van Roy, L. Xiao, and Y. Ye.
J. Jalden and A. d’Aspremont contributed the time-frequency analysis example
in §6.5.4, and the consumer preference bounding example in §6.5.5, respectively.
P. Parrilo suggested exercises 4.4 and 4.56. Newer printings beneﬁted greatly from
Igal Sason’s meticulous reading of the book.
We want to single out two others for special acknowledgment.
Arkadi Ne-
mirovski incited our original interest in convex optimization, and encouraged us
to write this book. We also want to thank Kishan Baheti for playing a critical
role in the development of this book. In 1994 he encouraged us to apply for a Na-
tional Science Foundation combined research and curriculum development grant,
on convex optimization with engineering applications, and this book is a direct (if
delayed) consequence.
Stephen Boyd
Stanford, California
Lieven Vandenberghe
Los Angeles, California


## Page 14



## Page 15

Chapter 1
Introduction
In this introduction we give an overview of mathematical optimization, focusing on
the special role of convex optimization. The concepts introduced informally here
will be covered in later chapters, with more care and technical detail.
1.1
Mathematical optimization
A mathematical optimization problem, or just optimization problem, has the form
minimize
f0(x)
subject to
fi(x) ≤bi,
i = 1, . . . , m.
(1.1)
Here the vector x = (x1, . . . , xn) is the optimization variable of the problem, the
function f0 : Rn →R is the objective function, the functions fi : Rn →R,
i = 1, . . . , m, are the (inequality) constraint functions, and the constants b1, . . . , bm
are the limits, or bounds, for the constraints. A vector x⋆is called optimal, or a
solution of the problem (1.1), if it has the smallest objective value among all vectors
that satisfy the constraints: for any z with f1(z) ≤b1, . . . , fm(z) ≤bm, we have
f0(z) ≥f0(x⋆).
We generally consider families or classes of optimization problems, characterized
by particular forms of the objective and constraint functions. As an important
example, the optimization problem (1.1) is called a linear program if the objective
and constraint functions f0, . . . , fm are linear, i.e., satisfy
fi(αx + βy) = αfi(x) + βfi(y)
(1.2)
for all x, y ∈Rn and all α, β ∈R. If the optimization problem is not linear, it is
called a nonlinear program.
This book is about a class of optimization problems called convex optimiza-
tion problems. A convex optimization problem is one in which the objective and
constraint functions are convex, which means they satisfy the inequality
fi(αx + βy) ≤αfi(x) + βfi(y)
(1.3)


## Page 16

2
1
Introduction
for all x, y ∈Rn and all α, β ∈R with α + β = 1, α ≥0, β ≥0. Comparing (1.3)
and (1.2), we see that convexity is more general than linearity: inequality replaces
the more restrictive equality, and the inequality must hold only for certain values
of α and β. Since any linear program is therefore a convex optimization problem,
we can consider convex optimization to be a generalization of linear programming.
1.1.1
Applications
The optimization problem (1.1) is an abstraction of the problem of making the best
possible choice of a vector in Rn from a set of candidate choices. The variable x
represents the choice made; the constraints fi(x) ≤bi represent ﬁrm requirements
or speciﬁcations that limit the possible choices, and the objective value f0(x) rep-
resents the cost of choosing x. (We can also think of −f0(x) as representing the
value, or utility, of choosing x.) A solution of the optimization problem (1.1) corre-
sponds to a choice that has minimum cost (or maximum utility), among all choices
that meet the ﬁrm requirements.
In portfolio optimization, for example, we seek the best way to invest some
capital in a set of n assets. The variable xi represents the investment in the ith
asset, so the vector x ∈Rn describes the overall portfolio allocation across the set of
assets. The constraints might represent a limit on the budget (i.e., a limit on the
total amount to be invested), the requirement that investments are nonnegative
(assuming short positions are not allowed), and a minimum acceptable value of
expected return for the whole portfolio. The objective or cost function might be
a measure of the overall risk or variance of the portfolio return.
In this case,
the optimization problem (1.1) corresponds to choosing a portfolio allocation that
minimizes risk, among all possible allocations that meet the ﬁrm requirements.
Another example is device sizing in electronic design, which is the task of choos-
ing the width and length of each device in an electronic circuit. Here the variables
represent the widths and lengths of the devices. The constraints represent a va-
riety of engineering requirements, such as limits on the device sizes imposed by
the manufacturing process, timing requirements that ensure that the circuit can
operate reliably at a speciﬁed speed, and a limit on the total area of the circuit. A
common objective in a device sizing problem is the total power consumed by the
circuit. The optimization problem (1.1) is to ﬁnd the device sizes that satisfy the
design requirements (on manufacturability, timing, and area) and are most power
eﬃcient.
In data ﬁtting, the task is to ﬁnd a model, from a family of potential models,
that best ﬁts some observed data and prior information. Here the variables are the
parameters in the model, and the constraints can represent prior information or
required limits on the parameters (such as nonnegativity). The objective function
might be a measure of misﬁt or prediction error between the observed data and
the values predicted by the model, or a statistical measure of the unlikeliness or
implausibility of the parameter values. The optimization problem (1.1) is to ﬁnd
the model parameter values that are consistent with the prior information, and give
the smallest misﬁt or prediction error with the observed data (or, in a statistical


## Page 17

1.1
Mathematical optimization
3
framework, are most likely).
An amazing variety of practical problems involving decision making (or system
design, analysis, and operation) can be cast in the form of a mathematical opti-
mization problem, or some variation such as a multicriterion optimization problem.
Indeed, mathematical optimization has become an important tool in many areas.
It is widely used in engineering, in electronic design automation, automatic con-
trol systems, and optimal design problems arising in civil, chemical, mechanical,
and aerospace engineering. Optimization is used for problems arising in network
design and operation, ﬁnance, supply chain management, scheduling, and many
other areas. The list of applications is still steadily expanding.
For most of these applications, mathematical optimization is used as an aid to
a human decision maker, system designer, or system operator, who supervises the
process, checks the results, and modiﬁes the problem (or the solution approach)
when necessary. This human decision maker also carries out any actions suggested
by the optimization problem, e.g., buying or selling assets to achieve the optimal
portfolio.
A relatively recent phenomenon opens the possibility of many other applications
for mathematical optimization. With the proliferation of computers embedded in
products, we have seen a rapid growth in embedded optimization. In these em-
bedded applications, optimization is used to automatically make real-time choices,
and even carry out the associated actions, with no (or little) human intervention or
oversight. In some application areas, this blending of traditional automatic control
systems and embedded optimization is well under way; in others, it is just start-
ing. Embedded real-time optimization raises some new challenges: in particular,
it requires solution methods that are extremely reliable, and solve problems in a
predictable amount of time (and memory).
1.1.2
Solving optimization problems
A solution method for a class of optimization problems is an algorithm that com-
putes a solution of the problem (to some given accuracy), given a particular problem
from the class, i.e., an instance of the problem. Since the late 1940s, a large eﬀort
has gone into developing algorithms for solving various classes of optimization prob-
lems, analyzing their properties, and developing good software implementations.
The eﬀectiveness of these algorithms, i.e., our ability to solve the optimization prob-
lem (1.1), varies considerably, and depends on factors such as the particular forms
of the objective and constraint functions, how many variables and constraints there
are, and special structure, such as sparsity. (A problem is sparse if each constraint
function depends on only a small number of the variables).
Even when the objective and constraint functions are smooth (for example,
polynomials) the general optimization problem (1.1) is surprisingly diﬃcult to solve.
Approaches to the general problem therefore involve some kind of compromise, such
as very long computation time, or the possibility of not ﬁnding the solution. Some
of these methods are discussed in §1.4.
There are, however, some important exceptions to the general rule that most
optimization problems are diﬃcult to solve. For a few problem classes we have


## Page 18

4
1
Introduction
eﬀective algorithms that can reliably solve even large problems, with hundreds or
thousands of variables and constraints. Two important and well known examples,
described in §1.2 below (and in detail in chapter 4), are least-squares problems and
linear programs. It is less well known that convex optimization is another exception
to the rule: Like least-squares or linear programming, there are very eﬀective
algorithms that can reliably and eﬃciently solve even large convex problems.
1.2
Least-squares and linear programming
In this section we describe two very widely known and used special subclasses of
convex optimization: least-squares and linear programming. (A complete technical
treatment of these problems will be given in chapter 4.)
1.2.1
Least-squares problems
A least-squares problem is an optimization problem with no constraints (i.e., m =
0) and an objective which is a sum of squares of terms of the form aT
i x −bi:
minimize
f0(x) = ∥Ax −b∥2
2 = Pk
i=1(aT
i x −bi)2.
(1.4)
Here A ∈Rk×n (with k ≥n), aT
i are the rows of A, and the vector x ∈Rn is the
optimization variable.
Solving least-squares problems
The solution of a least-squares problem (1.4) can be reduced to solving a set of
linear equations,
(AT A)x = AT b,
so we have the analytical solution x = (AT A)−1AT b. For least-squares problems
we have good algorithms (and software implementations) for solving the problem to
high accuracy, with very high reliability. The least-squares problem can be solved
in a time approximately proportional to n2k, with a known constant. A current
desktop computer can solve a least-squares problem with hundreds of variables, and
thousands of terms, in a few seconds; more powerful computers, of course, can solve
larger problems, or the same size problems, faster. (Moreover, these solution times
will decrease exponentially in the future, according to Moore’s law.) Algorithms
and software for solving least-squares problems are reliable enough for embedded
optimization.
In many cases we can solve even larger least-squares problems, by exploiting
some special structure in the coeﬃcient matrix A. Suppose, for example, that the
matrix A is sparse, which means that it has far fewer than kn nonzero entries. By
exploiting sparsity, we can usually solve the least-squares problem much faster than
order n2k. A current desktop computer can solve a sparse least-squares problem


## Page 19

1.2
Least-squares and linear programming
5
with tens of thousands of variables, and hundreds of thousands of terms, in around
a minute (although this depends on the particular sparsity pattern).
For extremely large problems (say, with millions of variables), or for problems
with exacting real-time computing requirements, solving a least-squares problem
can be a challenge. But in the vast majority of cases, we can say that existing
methods are very eﬀective, and extremely reliable. Indeed, we can say that solving
least-squares problems (that are not on the boundary of what is currently achiev-
able) is a (mature) technology, that can be reliably used by many people who do
not know, and do not need to know, the details.
Using least-squares
The least-squares problem is the basis for regression analysis, optimal control, and
many parameter estimation and data ﬁtting methods. It has a number of statistical
interpretations, e.g., as maximum likelihood estimation of a vector x, given linear
measurements corrupted by Gaussian measurement errors.
Recognizing an optimization problem as a least-squares problem is straightfor-
ward; we only need to verify that the objective is a quadratic function (and then
test whether the associated quadratic form is positive semideﬁnite).
While the
basic least-squares problem has a simple ﬁxed form, several standard techniques
are used to increase its ﬂexibility in applications.
In weighted least-squares, the weighted least-squares cost
k
X
i=1
wi(aT
i x −bi)2,
where w1, . . . , wk are positive, is minimized.
(This problem is readily cast and
solved as a standard least-squares problem.) Here the weights wi are chosen to
reﬂect diﬀering levels of concern about the sizes of the terms aT
i x −bi, or simply
to inﬂuence the solution.
In a statistical setting, weighted least-squares arises
in estimation of a vector x, given linear measurements corrupted by errors with
unequal variances.
Another technique in least-squares is regularization, in which extra terms are
added to the cost function. In the simplest case, a positive multiple of the sum of
squares of the variables is added to the cost function:
k
X
i=1
(aT
i x −bi)2 + ρ
n
X
i=1
x2
i ,
where ρ > 0. (This problem too can be formulated as a standard least-squares
problem.)
The extra terms penalize large values of x, and result in a sensible
solution in cases when minimizing the ﬁrst sum only does not. The parameter ρ is
chosen by the user to give the right trade-oﬀbetween making the original objective
function Pk
i=1(aT
i x−bi)2 small, while keeping Pn
i=1 x2
i not too big. Regularization
comes up in statistical estimation when the vector x to be estimated is given a prior
distribution.
Weighted least-squares and regularization are covered in chapter 6; their sta-
tistical interpretations are given in chapter 7.


## Page 20

6
1
Introduction
1.2.2
Linear programming
Another important class of optimization problems is linear programming, in which
the objective and all constraint functions are linear:
minimize
cT x
subject to
aT
i x ≤bi,
i = 1, . . . , m.
(1.5)
Here the vectors c, a1, . . . , am ∈Rn and scalars b1, . . . , bm ∈R are problem pa-
rameters that specify the objective and constraint functions.
Solving linear programs
There is no simple analytical formula for the solution of a linear program (as there
is for a least-squares problem), but there are a variety of very eﬀective methods for
solving them, including Dantzig’s simplex method, and the more recent interior-
point methods described later in this book. While we cannot give the exact number
of arithmetic operations required to solve a linear program (as we can for least-
squares), we can establish rigorous bounds on the number of operations required
to solve a linear program, to a given accuracy, using an interior-point method. The
complexity in practice is order n2m (assuming m ≥n) but with a constant that is
less well characterized than for least-squares. These algorithms are quite reliable,
although perhaps not quite as reliable as methods for least-squares. We can easily
solve problems with hundreds of variables and thousands of constraints on a small
desktop computer, in a matter of seconds. If the problem is sparse, or has some
other exploitable structure, we can often solve problems with tens or hundreds of
thousands of variables and constraints.
As with least-squares problems, it is still a challenge to solve extremely large
linear programs, or to solve linear programs with exacting real-time computing re-
quirements. But, like least-squares, we can say that solving (most) linear programs
is a mature technology. Linear programming solvers can be (and are) embedded in
many tools and applications.
Using linear programming
Some applications lead directly to linear programs in the form (1.5), or one of
several other standard forms. In many other cases the original optimization prob-
lem does not have a standard linear program form, but can be transformed to an
equivalent linear program (and then, of course, solved) using techniques covered in
detail in chapter 4.
As a simple example, consider the Chebyshev approximation problem:
minimize
maxi=1,...,k |aT
i x −bi|.
(1.6)
Here x ∈Rn is the variable, and a1, . . . , ak ∈Rn, b1, . . . , bk ∈R are parameters
that specify the problem instance. Note the resemblance to the least-squares prob-
lem (1.4). For both problems, the objective is a measure of the size of the terms
aT
i x −bi. In least-squares, we use the sum of squares of the terms as objective,
whereas in Chebyshev approximation, we use the maximum of the absolute values.


## Page 21

1.3
Convex optimization
7
One other important distinction is that the objective function in the Chebyshev
approximation problem (1.6) is not diﬀerentiable; the objective in the least-squares
problem (1.4) is quadratic, and therefore diﬀerentiable.
The Chebyshev approximation problem (1.6) can be solved by solving the linear
program
minimize
t
subject to
aT
i x −t ≤bi,
i = 1, . . . , k
−aT
i x −t ≤−bi,
i = 1, . . . , k,
(1.7)
with variables x ∈Rn and t ∈R.
(The details will be given in chapter 6.)
Since linear programs are readily solved, the Chebyshev approximation problem is
therefore readily solved.
Anyone with a working knowledge of linear programming would recognize the
Chebyshev approximation problem (1.6) as one that can be reduced to a linear
program. For those without this background, though, it might not be obvious that
the Chebyshev approximation problem (1.6), with its nondiﬀerentiable objective,
can be formulated and solved as a linear program.
While recognizing problems that can be reduced to linear programs is more
involved than recognizing a least-squares problem, it is a skill that is readily ac-
quired, since only a few standard tricks are used. The task can even be partially
automated; some software systems for specifying and solving optimization prob-
lems can automatically recognize (some) problems that can be reformulated as
linear programs.
1.3
Convex optimization
A convex optimization problem is one of the form
minimize
f0(x)
subject to
fi(x) ≤bi,
i = 1, . . . , m,
(1.8)
where the functions f0, . . . , fm : Rn →R are convex, i.e., satisfy
fi(αx + βy) ≤αfi(x) + βfi(y)
for all x, y ∈Rn and all α, β ∈R with α+β = 1, α ≥0, β ≥0. The least-squares
problem (1.4) and linear programming problem (1.5) are both special cases of the
general convex optimization problem (1.8).
1.3.1
Solving convex optimization problems
There is in general no analytical formula for the solution of convex optimization
problems, but (as with linear programming problems) there are very eﬀective meth-
ods for solving them. Interior-point methods work very well in practice, and in some
cases can be proved to solve the problem to a speciﬁed accuracy with a number of


## Page 22

8
1
Introduction
operations that does not exceed a polynomial of the problem dimensions. (This is
covered in chapter 11.)
We will see that interior-point methods can solve the problem (1.8) in a num-
ber of steps or iterations that is almost always in the range between 10 and 100.
Ignoring any structure in the problem (such as sparsity), each step requires on the
order of
max{n3, n2m, F}
operations, where F is the cost of evaluating the ﬁrst and second derivatives of the
objective and constraint functions f0, . . . , fm.
Like methods for solving linear programs, these interior-point methods are quite
reliable. We can easily solve problems with hundreds of variables and thousands
of constraints on a current desktop computer, in at most a few tens of seconds. By
exploiting problem structure (such as sparsity), we can solve far larger problems,
with many thousands of variables and constraints.
We cannot yet claim that solving general convex optimization problems is a
mature technology, like solving least-squares or linear programming problems. Re-
search on interior-point methods for general nonlinear convex optimization is still
a very active research area, and no consensus has emerged yet as to what the best
method or methods are. But it is reasonable to expect that solving general con-
vex optimization problems will become a technology within a few years. And for
some subclasses of convex optimization problems, for example second-order cone
programming or geometric programming (studied in detail in chapter 4), it is fair
to say that interior-point methods are approaching a technology.
1.3.2
Using convex optimization
Using convex optimization is, at least conceptually, very much like using least-
squares or linear programming. If we can formulate a problem as a convex opti-
mization problem, then we can solve it eﬃciently, just as we can solve a least-squares
problem eﬃciently. With only a bit of exaggeration, we can say that, if you formu-
late a practical problem as a convex optimization problem, then you have solved
the original problem.
There are also some important diﬀerences. Recognizing a least-squares problem
is straightforward, but recognizing a convex function can be diﬃcult. In addition,
there are many more tricks for transforming convex problems than for transforming
linear programs.
Recognizing convex optimization problems, or those that can
be transformed to convex optimization problems, can therefore be challenging.
The main goal of this book is to give the reader the background needed to do
this. Once the skill of recognizing or formulating convex optimization problems is
developed, you will ﬁnd that surprisingly many problems can be solved via convex
optimization.
The challenge, and art, in using convex optimization is in recognizing and for-
mulating the problem. Once this formulation is done, solving the problem is, like
least-squares or linear programming, (almost) technology.


## Page 23

1.4
Nonlinear optimization
9
1.4
Nonlinear optimization
Nonlinear optimization (or nonlinear programming) is the term used to describe
an optimization problem when the objective or constraint functions are not linear,
but not known to be convex.
Sadly, there are no eﬀective methods for solving
the general nonlinear programming problem (1.1). Even simple looking problems
with as few as ten variables can be extremely challenging, while problems with a
few hundreds of variables can be intractable. Methods for the general nonlinear
programming problem therefore take several diﬀerent approaches, each of which
involves some compromise.
1.4.1
Local optimization
In local optimization, the compromise is to give up seeking the optimal x, which
minimizes the objective over all feasible points. Instead we seek a point that is
only locally optimal, which means that it minimizes the objective function among
feasible points that are near it, but is not guaranteed to have a lower objective
value than all other feasible points. A large fraction of the research on general
nonlinear programming has focused on methods for local optimization, which as a
consequence are well developed.
Local optimization methods can be fast, can handle large-scale problems, and
are widely applicable, since they only require diﬀerentiability of the objective and
constraint functions. As a result, local optimization methods are widely used in
applications where there is value in ﬁnding a good point, if not the very best. In
an engineering design application, for example, local optimization can be used to
improve the performance of a design originally obtained by manual, or other, design
methods.
There are several disadvantages of local optimization methods, beyond (possi-
bly) not ﬁnding the true, globally optimal solution. The methods require an initial
guess for the optimization variable. This initial guess or starting point is critical,
and can greatly aﬀect the objective value of the local solution obtained. Little
information is provided about how far from (globally) optimal the local solution
is. Local optimization methods are often sensitive to algorithm parameter values,
which may need to be adjusted for a particular problem, or family of problems.
Using a local optimization method is trickier than solving a least-squares prob-
lem, linear program, or convex optimization problem. It involves experimenting
with the choice of algorithm, adjusting algorithm parameters, and ﬁnding a good
enough initial guess (when one instance is to be solved) or a method for producing
a good enough initial guess (when a family of problems is to be solved). Roughly
speaking, local optimization methods are more art than technology. Local opti-
mization is a well developed art, and often very eﬀective, but it is nevertheless an
art. In contrast, there is little art involved in solving a least-squares problem or
a linear program (except, of course, those on the boundary of what is currently
possible).
An interesting comparison can be made between local optimization methods for
nonlinear programming, and convex optimization. Since diﬀerentiability of the ob-


## Page 24

10
1
Introduction
jective and constraint functions is the only requirement for most local optimization
methods, formulating a practical problem as a nonlinear optimization problem is
relatively straightforward. The art in local optimization is in solving the problem
(in the weakened sense of ﬁnding a locally optimal point), once it is formulated.
In convex optimization these are reversed: The art and challenge is in problem
formulation; once a problem is formulated as a convex optimization problem, it is
relatively straightforward to solve it.
1.4.2
Global optimization
In global optimization, the true global solution of the optimization problem (1.1)
is found; the compromise is eﬃciency. The worst-case complexity of global opti-
mization methods grows exponentially with the problem sizes n and m; the hope
is that in practice, for the particular problem instances encountered, the method is
far faster. While this favorable situation does occur, it is not typical. Even small
problems, with a few tens of variables, can take a very long time (e.g., hours or
days) to solve.
Global optimization is used for problems with a small number of variables, where
computing time is not critical, and the value of ﬁnding the true global solution is
very high. One example from engineering design is worst-case analysis or veriﬁca-
tion of a high value or safety-critical system. Here the variables represent uncertain
parameters, that can vary during manufacturing, or with the environment or op-
erating condition. The objective function is a utility function, i.e., one for which
smaller values are worse than larger values, and the constraints represent prior
knowledge about the possible parameter values. The optimization problem (1.1) is
the problem of ﬁnding the worst-case values of the parameters. If the worst-case
value is acceptable, we can certify the system as safe or reliable (with respect to
the parameter variations).
A local optimization method can rapidly ﬁnd a set of parameter values that
is bad, but not guaranteed to be the absolute worst possible. If a local optimiza-
tion method ﬁnds parameter values that yield unacceptable performance, it has
succeeded in determining that the system is not reliable. But a local optimization
method cannot certify the system as reliable; it can only fail to ﬁnd bad parameter
values. A global optimization method, in contrast, will ﬁnd the absolute worst val-
ues of the parameters, and if the associated performance is acceptable, can certify
the system as safe. The cost is computation time, which can be very large, even
for a relatively small number of parameters. But it may be worth it in cases where
the value of certifying the performance is high, or the cost of being wrong about
the reliability or safety is high.
1.4.3
Role of convex optimization in nonconvex problems
In this book we focus primarily on convex optimization problems, and applications
that can be reduced to convex optimization problems. But convex optimization
also plays an important role in problems that are not convex.


## Page 25

1.5
Outline
11
Initialization for local optimization
One obvious use is to combine convex optimization with a local optimization
method. Starting with a nonconvex problem, we ﬁrst ﬁnd an approximate, but
convex, formulation of the problem. By solving this approximate problem, which
can be done easily and without an initial guess, we obtain the exact solution to the
approximate convex problem. This point is then used as the starting point for a
local optimization method, applied to the original nonconvex problem.
Convex heuristics for nonconvex optimization
Convex optimization is the basis for several heuristics for solving nonconvex prob-
lems. One interesting example we will see is the problem of ﬁnding a sparse vector
x (i.e., one with few nonzero entries) that satisﬁes some constraints. While this is
a diﬃcult combinatorial problem, there are some simple heuristics, based on con-
vex optimization, that often ﬁnd fairly sparse solutions. (These are described in
chapter 6.)
Another broad example is given by randomized algorithms, in which an ap-
proximate solution to a nonconvex problem is found by drawing some number of
candidates from a probability distribution, and taking the best one found as the
approximate solution. Now suppose the family of distributions from which we will
draw the candidates is parametrized, e.g., by its mean and covariance. We can then
pose the question, which of these distributions gives us the smallest expected value
of the objective? It turns out that this problem is sometimes a convex problem,
and therefore eﬃciently solved. (See, e.g., exercise 11.23.)
Bounds for global optimization
Many methods for global optimization require a cheaply computable lower bound
on the optimal value of the nonconvex problem. Two standard methods for doing
this are based on convex optimization. In relaxation, each nonconvex constraint
is replaced with a looser, but convex, constraint. In Lagrangian relaxation, the
Lagrangian dual problem (described in chapter 5) is solved. This problem is convex,
and provides a lower bound on the optimal value of the nonconvex problem.
1.5
Outline
The book is divided into three main parts, titled Theory, Applications, and Algo-
rithms.
1.5.1
Part I: Theory
In part I, Theory, we cover basic deﬁnitions, concepts, and results from convex
analysis and convex optimization. We make no attempt to be encyclopedic, and
skew our selection of topics toward those that we think are useful in recognizing


## Page 26

12
1
Introduction
and formulating convex optimization problems. This is classical material, almost
all of which can be found in other texts on convex analysis and optimization. We
make no attempt to give the most general form of the results; for that the reader
can refer to any of the standard texts on convex analysis.
Chapters 2 and 3 cover convex sets and convex functions, respectively.
We
give some common examples of convex sets and functions, as well as a number of
convex calculus rules, i.e., operations on sets and functions that preserve convexity.
Combining the basic examples with the convex calculus rules allows us to form
(or perhaps more importantly, recognize) some fairly complicated convex sets and
functions.
In chapter 4, Convex optimization problems, we give a careful treatment of op-
timization problems, and describe a number of transformations that can be used to
reformulate problems. We also introduce some common subclasses of convex opti-
mization, such as linear programming and geometric programming, and the more
recently developed second-order cone programming and semideﬁnite programming.
Chapter 5 covers Lagrangian duality, which plays a central role in convex opti-
mization. Here we give the classical Karush-Kuhn-Tucker conditions for optimality,
and a local and global sensitivity analysis for convex optimization problems.
1.5.2
Part II: Applications
In part II, Applications, we describe a variety of applications of convex optimization,
in areas like probability and statistics, computational geometry, and data ﬁtting.
We have described these applications in a way that is accessible, we hope, to a broad
audience. To keep each application short, we consider only simple cases, sometimes
adding comments about possible extensions. We are sure that our treatment of
some of the applications will cause experts to cringe, and we apologize to them
in advance. But our goal is to convey the ﬂavor of the application, quickly and
to a broad audience, and not to give an elegant, theoretically sound, or complete
treatment. Our own backgrounds are in electrical engineering, in areas like control
systems, signal processing, and circuit analysis and design. Although we include
these topics in the courses we teach (using this book as the main text), only a few
of these applications are broadly enough accessible to be included here.
The aim of part II is to show the reader, by example, how convex optimization
can be applied in practice.
1.5.3
Part III: Algorithms
In part III, Algorithms, we describe numerical methods for solving convex opti-
mization problems, focusing on Newton’s algorithm and interior-point methods.
Part III is organized as three chapters, which cover unconstrained optimization,
equality constrained optimization, and inequality constrained optimization, respec-
tively. These chapters follow a natural hierarchy, in which solving a problem is
reduced to solving a sequence of simpler problems. Quadratic optimization prob-
lems (including, e.g., least-squares) form the base of the hierarchy; they can be


## Page 27

1.5
Outline
13
solved exactly by solving a set of linear equations. Newton’s method, developed in
chapters 9 and 10, is the next level in the hierarchy. In Newton’s method, solving
an unconstrained or equality constrained problem is reduced to solving a sequence
of quadratic problems. In chapter 11, we describe interior-point methods, which
form the top level of the hierarchy. These methods solve an inequality constrained
problem by solving a sequence of unconstrained, or equality constrained, problems.
Overall we cover just a handful of algorithms, and omit entire classes of good
methods, such as quasi-Newton, conjugate-gradient, bundle, and cutting-plane al-
gorithms. For the methods we do describe, we give simpliﬁed variants, and not the
latest, most sophisticated versions. Our choice of algorithms was guided by several
criteria. We chose algorithms that are simple (to describe and implement), but
also reliable and robust, and eﬀective and fast enough for most problems.
Many users of convex optimization end up using (but not developing) standard
software, such as a linear or semideﬁnite programming solver. For these users, the
material in part III is meant to convey the basic ﬂavor of the methods, and give
some ideas of their basic attributes. For those few who will end up developing new
algorithms, we think that part III serves as a good introduction.
1.5.4
Appendices
There are three appendices. The ﬁrst lists some basic facts from mathematics that
we use, and serves the secondary purpose of setting out our notation. The second
appendix covers a fairly particular topic, optimization problems with quadratic
objective and one quadratic constraint. These are nonconvex problems that never-
theless can be eﬀectively solved, and we use the results in several of the applications
described in part II.
The ﬁnal appendix gives a brief introduction to numerical linear algebra, con-
centrating on methods that can exploit problem structure, such as sparsity, to gain
eﬃciency. We do not cover a number of important topics, including roundoﬀanaly-
sis, or give any details of the methods used to carry out the required factorizations.
These topics are covered by a number of excellent texts.
1.5.5
Comments on examples
In many places in the text (but particularly in parts II and III, which cover ap-
plications and algorithms, respectively) we illustrate ideas using speciﬁc examples.
In some cases, the examples are chosen (or designed) speciﬁcally to illustrate our
point; in other cases, the examples are chosen to be ‘typical’. This means that the
examples were chosen as samples from some obvious or simple probability distri-
bution. The dangers of drawing conclusions about algorithm performance from a
few tens or hundreds of randomly generated examples are well known, so we will
not repeat them here. These examples are meant only to give a rough idea of al-
gorithm performance, or a rough idea of how the computational eﬀort varies with
problem dimensions, and not as accurate predictors of algorithm performance. In
particular, your results may vary from ours.


## Page 28

14
1
Introduction
1.5.6
Comments on exercises
Each chapter concludes with a set of exercises. Some involve working out the de-
tails of an argument or claim made in the text. Others focus on determining, or
establishing, convexity of some given sets, functions, or problems; or more gener-
ally, convex optimization problem formulation. Some chapters include numerical
exercises, which require some (but not much) programming in an appropriate high
level language. The diﬃculty level of the exercises is mixed, and varies without
warning from quite straightforward to rather tricky.
1.6
Notation
Our notation is more or less standard, with a few exceptions. In this section we
describe our basic notation; a more complete list appears on page 697.
We use R to denote the set of real numbers, R+ to denote the set of nonnegative
real numbers, and R++ to denote the set of positive real numbers. The set of real
n-vectors is denoted Rn, and the set of real m × n matrices is denoted Rm×n. We
delimit vectors and matrices with square brackets, with the components separated
by space. We use parentheses to construct column vectors from comma separated
lists. For example, if a, b, c ∈R, we have
(a, b, c) =


a
b
c

= [ a
b
c ]T ,
which is an element of R3. The symbol 1 denotes a vector all of whose components
are one (with dimension determined from context). The notation xi can refer to
the ith component of the vector x, or to the ith element of a set or sequence of
vectors x1, x2, . . .. The context, or the text, makes it clear which is meant.
We use Sk to denote the set of symmetric k × k matrices, Sk
+ to denote the
set of symmetric positive semideﬁnite k × k matrices, and Sk
++ to denote the set
of symmetric positive deﬁnite k × k matrices.
The curled inequality symbol ⪰
(and its strict form ≻) is used to denote generalized inequality: between vectors,
it represents componentwise inequality; between symmetric matrices, it represents
matrix inequality. With a subscript, the symbol ⪯K (or ≺K) denotes generalized
inequality with respect to the cone K (explained in §2.4.1).
Our notation for describing functions deviates a bit from standard notation,
but we hope it will cause no confusion. We use the notation f : Rp →Rq to mean
that f is an Rq-valued function on some subset of Rp, speciﬁcally, its domain,
which we denote dom f. We can think of our use of the notation f : Rp →Rq as
a declaration of the function type, as in a computer language: f : Rp →Rq means
that the function f takes as argument a real p-vector, and returns a real q-vector.
The set dom f, the domain of the function f, speciﬁes the subset of Rp of points
x for which f(x) is deﬁned. As an example, we describe the logarithm function
as log : R →R, with dom log = R++. The notation log : R →R means that


## Page 29

1.6
Notation
15
the logarithm function accepts and returns a real number; dom log = R++ means
that the logarithm is deﬁned only for positive numbers.
We use Rn as a generic ﬁnite-dimensional vector space.
We will encounter
several other ﬁnite-dimensional vector spaces, e.g., the space of polynomials of a
variable with a given maximum degree, or the space Sk of symmetric k×k matrices.
By identifying a basis for a vector space, we can always identify it with Rn (where
n is its dimension), and therefore the generic results, stated for the vector space
Rn, can be applied. We usually leave it to the reader to translate general results
or statements to other vector spaces. For example, any linear function f : Rn →R
can be represented in the form f(x) = cT x, where c ∈Rn. The corresponding
statement for the vector space Sk can be found by choosing a basis and translating.
This results in the statement: any linear function f : Sk →R can be represented
in the form f(X) = tr(CX), where C ∈Sk.


## Page 30

16
1
Introduction
Bibliography
Least-squares is a very old subject; see, for example, the treatise written (in Latin) by
Gauss in the 1820s, and recently translated by Stewart [Gau95]. More recent work in-
cludes the books by Lawson and Hanson [LH95] and Bj¨orck [Bj¨o96]. References on linear
programming can be found in chapter 4.
There are many good texts on local methods for nonlinear programming, including Gill,
Murray, and Wright [GMW81], Nocedal and Wright [NW99], Luenberger [Lue84], and
Bertsekas [Ber99].
Global optimization is covered in the books by Horst and Pardalos [HP94], Pinter [Pin95],
and Tuy [Tuy98]. Using convex optimization to ﬁnd bounds for nonconvex problems is
an active research topic, and addressed in the books above on global optimization, the
book by Ben-Tal and Nemirovski [BTN01, §4.3], and the survey by Nesterov, Wolkowicz,
and Ye [NWY00]. Some notable papers on this subject are Goemans and Williamson
[GW95], Nesterov [Nes00, Nes98], Ye [Ye99], and Parrilo [Par03]. Randomized methods
are discussed in Motwani and Raghavan [MR95].
Convex analysis, the mathematics of convex sets, functions, and optimization problems, is
a well developed subﬁeld of mathematics. Basic references include the books by Rockafel-
lar [Roc70], Hiriart-Urruty and Lemar´echal [HUL93, HUL01], Borwein and Lewis [BL00],
and Bertsekas, Nedi´c, and Ozdaglar [Ber03]. More references on convex analysis can be
found in chapters 2–5.
Nesterov and Nemirovski [NN94] were the ﬁrst to point out that interior-point methods
can solve many convex optimization problems; see also the references in chapter 11. The
book by Ben-Tal and Nemirovski [BTN01] covers modern convex optimization, interior-
point methods, and applications.
Solution methods for convex optimization that we do not cover in this book include
subgradient methods [Sho85], bundle methods [HUL93], cutting-plane methods [Kel60,
EM75, GLY96], and the ellipsoid method [Sho91, BGT81].
The idea that convex optimization problems are tractable is not new. It has long been rec-
ognized that the theory of convex optimization is far more straightforward (and complete)
than the theory of general nonlinear optimization. In this context Rockafellar stated, in
his 1993 SIAM Review survey paper [Roc93],
In fact the great watershed in optimization isn’t between linearity and nonlin-
earity, but convexity and nonconvexity.
The ﬁrst formal argument that convex optimization problems are easier to solve than
general nonlinear optimization problems was made by Nemirovski and Yudin, in their
1983 book Problem Complexity and Method Eﬃciency in Optimization [NY83].
They
showed that the information-based complexity of convex optimization problems is far
lower than that of general nonlinear optimization problems. A more recent book on this
topic is Vavasis [Vav91].
The low (theoretical) complexity of interior-point methods is integral to modern research
in this area. Much of the research focuses on proving that an interior-point (or other)
method can solve some class of convex optimization problems with a number of operations
that grows no faster than a polynomial of the problem dimensions and log(1/ǫ), where
ǫ > 0 is the required accuracy. (We will see some simple results like these in chapter 11.)
The ﬁrst comprehensive work on this topic is the book by Nesterov and Nemirovski
[NN94]. Other books include Ben-Tal and Nemirovski [BTN01, lecture 5] and Renegar
[Ren01]. The polynomial-time complexity of interior-point methods for various convex
optimization problems is in marked contrast to the situation for a number of nonconvex
optimization problems, for which all known algorithms require, in the worst case, a number
of operations that is exponential in the problem dimensions.


## Page 31

Bibliography
17
Convex optimization has been used in many applications areas, too numerous to cite
here. Convex analysis is central in economics and ﬁnance, where it is the basis of many
results. For example the separating hyperplane theorem, together with a no-arbitrage
assumption, is used to deduce the existence of prices and risk-neutral probabilities (see,
e.g., Luenberger [Lue95, Lue98] and Ross [Ros99]). Convex optimization, especially our
ability to solve semideﬁnite programs, has recently received particular attention in au-
tomatic control theory.
Applications of convex optimization in control theory can be
found in the books by Boyd and Barratt [BB91], Boyd, El Ghaoui, Feron, and Balakrish-
nan [BEFB94], Dahleh and Diaz-Bobillo [DDB95], El Ghaoui and Niculescu [EN00], and
Dullerud and Paganini [DP00]. A good example of embedded (convex) optimization is
model predictive control, an automatic control technique that requires the solution of a
(convex) quadratic program at each step. Model predictive control is now widely used in
the chemical process control industry; see Morari and Zaﬁrou [MZ89]. Another applica-
tions area where convex optimization (and especially, geometric programming) has a long
history is electronic circuit design. Research papers on this topic include Fishburn and
Dunlop [FD85], Sapatnekar, Rao, Vaidya, and Kang [SRVK93], and Hershenson, Boyd,
and Lee [HBL01]. Luo [Luo03] gives a survey of applications in signal processing and
communications. More references on applications of convex optimization can be found in
chapters 4 and 6–8.
High quality implementations of recent interior-point methods for convex optimization
problems are available in the LOQO [Van97] and MOSEK [MOS02] software packages,
and the codes listed in chapter 11. Software systems for specifying optimization prob-
lems include AMPL [FGK99] and GAMS [BKMR98].
Both provide some support for
recognizing problems that can be transformed to linear programs.


## Page 32



## Page 33

Part I
Theory


## Page 34



## Page 35

Chapter 2
Convex sets
2.1
Aﬃne and convex sets
2.1.1
Lines and line segments
Suppose x1̸ = x2 are two points in Rn. Points of the form
y = θx1 + (1 −θ)x2,
where θ ∈R, form the line passing through x1 and x2. The parameter value θ = 0
corresponds to y = x2, and the parameter value θ = 1 corresponds to y = x1.
Values of the parameter θ between 0 and 1 correspond to the (closed) line segment
between x1 and x2.
Expressing y in the form
y = x2 + θ(x1 −x2)
gives another interpretation: y is the sum of the base point x2 (corresponding
to θ = 0) and the direction x1 −x2 (which points from x2 to x1) scaled by the
parameter θ. Thus, θ gives the fraction of the way from x2 to x1 where y lies. As
θ increases from 0 to 1, the point y moves from x2 to x1; for θ > 1, the point y lies
on the line beyond x1. This is illustrated in ﬁgure 2.1.
2.1.2
Aﬃne sets
A set C ⊆Rn is aﬃne if the line through any two distinct points in C lies in C,
i.e., if for any x1, x2 ∈C and θ ∈R, we have θx1 + (1−θ)x2 ∈C. In other words,
C contains the linear combination of any two points in C, provided the coeﬃcients
in the linear combination sum to one.
This idea can be generalized to more than two points. We refer to a point
of the form θ1x1 + · · · + θkxk, where θ1 + · · · + θk = 1, as an aﬃne combination
of the points x1, . . . , xk. Using induction from the deﬁnition of aﬃne set (i.e.,
that it contains every aﬃne combination of two points in it), it can be shown that


## Page 36

22
2
Convex sets
x1
x2
θ = 1.2
θ = 1
θ = 0.6
θ = 0
θ = −0.2
Figure 2.1 The line passing through x1 and x2 is described parametrically
by θx1 + (1 −θ)x2, where θ varies over R. The line segment between x1 and
x2, which corresponds to θ between 0 and 1, is shown darker.
an aﬃne set contains every aﬃne combination of its points: If C is an aﬃne set,
x1, . . . , xk ∈C, and θ1 + · · · + θk = 1, then the point θ1x1 + · · · + θkxk also belongs
to C.
If C is an aﬃne set and x0 ∈C, then the set
V = C −x0 = {x −x0 | x ∈C}
is a subspace, i.e., closed under sums and scalar multiplication. To see this, suppose
v1, v2 ∈V and α, β ∈R. Then we have v1 + x0 ∈C and v2 + x0 ∈C, and so
αv1 + βv2 + x0 = α(v1 + x0) + β(v2 + x0) + (1 −α −β)x0 ∈C,
since C is aﬃne, and α + β + (1 −α −β) = 1. We conclude that αv1 + βv2 ∈V ,
since αv1 + βv2 + x0 ∈C.
Thus, the aﬃne set C can be expressed as
C = V + x0 = {v + x0 | v ∈V },
i.e., as a subspace plus an oﬀset. The subspace V associated with the aﬃne set C
does not depend on the choice of x0, so x0 can be chosen as any point in C. We
deﬁne the dimension of an aﬃne set C as the dimension of the subspace V = C−x0,
where x0 is any element of C.
Example 2.1 Solution set of linear equations. The solution set of a system of linear
equations, C = {x | Ax = b}, where A ∈Rm×n and b ∈Rm, is an aﬃne set. To
show this, suppose x1, x2 ∈C, i.e., Ax1 = b, Ax2 = b. Then for any θ, we have
A(θx1 + (1 −θ)x2)
=
θAx1 + (1 −θ)Ax2
=
θb + (1 −θ)b
=
b,
which shows that the aﬃne combination θx1 + (1 −θ)x2 is also in C. The subspace
associated with the aﬃne set C is the nullspace of A.
We also have a converse: every aﬃne set can be expressed as the solution set of a
system of linear equations.


## Page 37

2.1
Aﬃne and convex sets
23
The set of all aﬃne combinations of points in some set C ⊆Rn is called the
aﬃne hull of C, and denoted aﬀC:
aﬀC = {θ1x1 + · · · + θkxk | x1, . . . , xk ∈C, θ1 + · · · + θk = 1}.
The aﬃne hull is the smallest aﬃne set that contains C, in the following sense: if
S is any aﬃne set with C ⊆S, then aﬀC ⊆S.
2.1.3
Aﬃne dimension and relative interior
We deﬁne the aﬃne dimension of a set C as the dimension of its aﬃne hull. Aﬃne
dimension is useful in the context of convex analysis and optimization, but is not
always consistent with other deﬁnitions of dimension. As an example consider the
unit circle in R2, i.e., {x ∈R2 | x2
1 + x2
2 = 1}. Its aﬃne hull is all of R2, so its
aﬃne dimension is two. By most deﬁnitions of dimension, however, the unit circle
in R2 has dimension one.
If the aﬃne dimension of a set C ⊆Rn is less than n, then the set lies in
the aﬃne set aﬀC̸ = Rn. We deﬁne the relative interior of the set C, denoted
relint C, as its interior relative to aﬀC:
relint C = {x ∈C | B(x, r) ∩aﬀC ⊆C for some r > 0},
where B(x, r) = {y | ∥y −x∥≤r}, the ball of radius r and center x in the norm
∥· ∥. (Here ∥· ∥is any norm; all norms deﬁne the same relative interior.) We can
then deﬁne the relative boundary of a set C as cl C \ relint C, where cl C is the
closure of C.
Example 2.2 Consider a square in the (x1, x2)-plane in R3, deﬁned as
C = {x ∈R3 | −1 ≤x1 ≤1, −1 ≤x2 ≤1, x3 = 0}.
Its aﬃne hull is the (x1, x2)-plane, i.e., aﬀC = {x ∈R3 | x3 = 0}. The interior of C
is empty, but the relative interior is
relint C = {x ∈R3 | −1 < x1 < 1, −1 < x2 < 1, x3 = 0}.
Its boundary (in R3) is itself; its relative boundary is the wire-frame outline,
{x ∈R3 | max{|x1|, |x2|} = 1, x3 = 0}.
2.1.4
Convex sets
A set C is convex if the line segment between any two points in C lies in C, i.e.,
if for any x1, x2 ∈C and any θ with 0 ≤θ ≤1, we have
θx1 + (1 −θ)x2 ∈C.


## Page 38

24
2
Convex sets
Figure 2.2 Some simple convex and nonconvex sets. Left. The hexagon,
which includes its boundary (shown darker), is convex. Middle. The kidney
shaped set is not convex, since the line segment between the two points in
the set shown as dots is not contained in the set. Right. The square contains
some boundary points but not others, and is not convex.
Figure 2.3 The convex hulls of two sets in R2. Left. The convex hull of a
set of ﬁfteen points (shown as dots) is the pentagon (shown shaded). Right.
The convex hull of the kidney shaped set in ﬁgure 2.2 is the shaded set.
Roughly speaking, a set is convex if every point in the set can be seen by every other
point, along an unobstructed straight path between them, where unobstructed
means lying in the set. Every aﬃne set is also convex, since it contains the entire
line between any two distinct points in it, and therefore also the line segment
between the points. Figure 2.2 illustrates some simple convex and nonconvex sets
in R2.
We call a point of the form θ1x1 + · · · + θkxk, where θ1 + · · · + θk = 1 and
θi ≥0, i = 1, . . . , k, a convex combination of the points x1, . . . , xk. As with aﬃne
sets, it can be shown that a set is convex if and only if it contains every convex
combination of its points. A convex combination of points can be thought of as a
mixture or weighted average of the points, with θi the fraction of xi in the mixture.
The convex hull of a set C, denoted conv C, is the set of all convex combinations
of points in C:
conv C = {θ1x1 + · · · + θkxk | xi ∈C, θi ≥0, i = 1, . . . , k, θ1 + · · · + θk = 1}.
As the name suggests, the convex hull conv C is always convex. It is the smallest
convex set that contains C: If B is any convex set that contains C, then conv C ⊆
B. Figure 2.3 illustrates the deﬁnition of convex hull.
The idea of a convex combination can be generalized to include inﬁnite sums, in-
tegrals, and, in the most general form, probability distributions. Suppose θ1, θ2, . . .


## Page 39

2.1
Aﬃne and convex sets
25
satisfy
θi ≥0,
i = 1, 2, . . . ,
∞
X
i=1
θi = 1,
and x1, x2, . . . ∈C, where C ⊆Rn is convex. Then
∞
X
i=1
θixi ∈C,
if the series converges. More generally, suppose p : Rn →R satisﬁes p(x) ≥0 for
all x ∈C and
R
C p(x) dx = 1, where C ⊆Rn is convex. Then
Z
C
p(x)x dx ∈C,
if the integral exists.
In the most general form, suppose C ⊆Rn is convex and x is a random vector
with x ∈C with probability one. Then E x ∈C. Indeed, this form includes all
the others as special cases. For example, suppose the random variable x only takes
on the two values x1 and x2, with prob(x = x1) = θ and prob(x = x2) = 1 −θ,
where 0 ≤θ ≤1. Then E x = θx1 + (1 −θ)x2, and we are back to a simple convex
combination of two points.
2.1.5
Cones
A set C is called a cone, or nonnegative homogeneous, if for every x ∈C and θ ≥0
we have θx ∈C. A set C is a convex cone if it is convex and a cone, which means
that for any x1, x2 ∈C and θ1, θ2 ≥0, we have
θ1x1 + θ2x2 ∈C.
Points of this form can be described geometrically as forming the two-dimensional
pie slice with apex 0 and edges passing through x1 and x2. (See ﬁgure 2.4.)
A point of the form θ1x1 + · · · + θkxk with θ1, . . . , θk ≥0 is called a conic
combination (or a nonnegative linear combination) of x1, . . . , xk. If xi are in a
convex cone C, then every conic combination of xi is in C. Conversely, a set C is
a convex cone if and only if it contains all conic combinations of its elements. Like
convex (or aﬃne) combinations, the idea of conic combination can be generalized
to inﬁnite sums and integrals.
The conic hull of a set C is the set of all conic combinations of points in C, i.e.,
{θ1x1 + · · · + θkxk | xi ∈C, θi ≥0, i = 1, . . . , k},
which is also the smallest convex cone that contains C (see ﬁgure 2.5).


## Page 40

26
2
Convex sets
0
x1
x2
Figure 2.4 The pie slice shows all points of the form θ1x1 + θ2x2, where
θ1, θ2 ≥0. The apex of the slice (which corresponds to θ1 = θ2 = 0) is at
0; its edges (which correspond to θ1 = 0 or θ2 = 0) pass through the points
x1 and x2.
0
0
Figure 2.5 The conic hulls (shown shaded) of the two sets of ﬁgure 2.3.
