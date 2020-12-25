# Mathematical Thinking in Computer Science

## Week 1 - Making Convincing Arguments

Why some arguments are convincing and some others are not? What makes an argument convincing? How can you establish your argument in such a way that there is no room for doubt left? How can mathematical thinking help with this? In this section, we start digging into these questions. Our goal is to learn by examples how to understand proofs, how to discover them on your own, how to explain them, and — last but not least — how to enjoy them: we will see how a small remark or a simple observation can turn a seemingly non-trivial question into an obvious one.how to discover them on your own

### Learning Objectives

- Distinguish between proofs and bla-bla-bla talk
- Develop simple proofs by example
- Explain a proof to a willing audience
- Analyze the requirements and narrow the search space

## Week 2 - How to Find an Example?

How can we be certain that an object with certain requirements exist? One way to show this, is to go through all objects and check whether at least one of them meets the requirements. However, in many cases, the search space is enormous. A computer may help, but some reasoning that narrows the search space is important both for computer search and for "bare hands" work. In this module, we will learn various techniques for showing that an object exists and that an object is optimal among all other objects. As usual, we'll practice solving many interactive puzzles. We'll show also some computer programs that help us to construct an example.

### Learning Objectives

- Give examples of proving optimality
- Develop backtracking programs
- Practice finding optimal solutions

## Week 3 - Recursion and Induction

We'll discover two powerful methods of defining objects, proving concepts, and implementing programs — recursion and induction. These two methods are heavily used in discrete mathematics and computer science. In particular, you will see them frequently in algorithms — for analysing correctness and running time of algorithms as well as for implementing efficient solutions. For some computational problems (e.g., exploring networks), recursive solutions are the most natural ones. The main idea of recursion and induction is to decompose a given problem into smaller problems of the same type. Being able to see such decompositions is an important skill both in mathematics and in programming. We'll hone this skill by solving various problems together.

### Learning Objectives

- Develop recursive programs
- Give examples of recursive definitions and programs
- Use recursion to solve computational problems
- Compute various sums using mathematical induction
- Explain flaws in proofs based on mathematical induction
- Modify the problem statement to make it more general and apply mathematical induction to find the answer and prove it is correct

## Week 4 - Logic

We have already invoked mathematical logic when we discussed how to make convincing arguments by giving examples. This week we will turn mathematical logic full on. We will discuss its basic operations and rules. We will see how logic can play a crucial and indispensable role in creating convincing arguments. We will discuss how to construct a negation to the statement, and you will see how to win an argument by showing your opponent is wrong with just one example called counterexample!. We will see tricky and seemingly counterintuitive, but yet (an unintentional pun) logical aspects of mathematical logic. We will see one of the oldest approaches to making convincing arguments: Reductio ad Absurdum.

### Learning Objectives

- Analyze logical containment of statements
- Prove statements using proof by contradiction
- Use pigeonhole principle in the proofs
- Use logical reasoning to reformulate and evaluate statements

## Week 5 - Invariants

"There are things that never change". Apart from being just a philosophical statement, this phrase turns out to be an important idea that can actually help. In this module we will see how it can help in problem solving. Things that do not change are called invariants in mathematics. They form an important tool of proving with numerous applications, including estimating running time of programs and algorithms. We will get some intuition of what they are, see how they can look like, and get some practice in using them.

### Learning Objectives

- Give examples of invariants in mathematics
- Apply invariants in proofs
- Prove statements using invariants

## Week 6 - Solving a 15-Puzzle

In this module, we consider a well known 15-puzzle where one needs to restore order among 15 square pieces in a square box. It turns out that the behaviour of this puzzle is determined by mathematics: it is solvable if and only if the corresponding permutation is even. We will learn the basic properties of even and odd permutations. The task is to implement a program that determines whether a permutation is even or odd. There is also a more difficult bonus task: to implement a program that actually computes a solution (sequence of moves) for a given position assuming that this position is solvable.

### Learning Objectives

- Produce a code based on some mathematical argument
- Prove the basic results about permutatios and their parity
- Design a program that works with simple python data structures
