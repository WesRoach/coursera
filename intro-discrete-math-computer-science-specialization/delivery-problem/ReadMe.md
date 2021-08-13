# Delivery Problem

We’ll implement (in Python) together efficient programs for a problem needed by delivery companies all over the world millions times per day — the travelling salesman problem. The goal in this problem is to visit all the given places as quickly as possible. How to find an optimal solution to this problem quickly? We still don’t have provably efficient algorithms for this difficult computational problem and this is the essence of the P versus NP problem, the most important open question in Computer Science. Still, we’ll implement several solutions for real world instances of the travelling salesman problem. While designing these solutions, we will rely heavily on the material learned in the courses of the specialization: proof techniques, combinatorics, probability, graph theory. We’ll see several examples of using discrete mathematics ideas to get more and more efficient solutions.

Do you have technical problems? Write to us: coursera@hse.ru

## Traveling Salesman Problem

We start this module with the definition of mathematical model of the delivery problem — the classical traveling salesman problem (usually abbreviated as TSP). We'll then review just a few of its many applications: from straightforward ones (delivering goods, planning a trip) to less obvious ones (data storage and compression, genome assembly). After that, we will together take the first steps in implementing programs for TSP.

### Learning Objectives

- Give examples of various statements of the delivery problem
- Practice implementing brute force solutions
- Solve the delivery problem on small instances

## Exact Algorithms

We'll see two general techniques applied to the traveling salesman problem. The first one, branch and bound, is a classical approach in combinatorial optimization that is used for various problems. It can be seen as an improvement of the brute force search: we try to construct a permutation piece by piece, but at each step we check whether it still makes sense to continue constructing the permutation (if it doesn't, we just cut off the current branch). The second one, dynamic programming, is arguably the most popular algorithmic technique. It solves a problem by going through a collection of smaller subproblems.

### Learning Objectives

- Develop dynamic programming solutions
- Develop branch and bound solutions
- Develop combinatorial algorithms

## Approximation Algorithms

As we've seen in the previous modules, solving the traveling salesman problem exactly is hard. In fact, we don't even expect an efficient solution in the nearest future. For this reason, it makes sense to ask: is it possible to find efficiently a solution that is probably suboptimal, but at the same time is close to optimal? It turns out that the answer is yes! We'll learn two algorithms. The first one guarantees to find quickly a solution which is at most twice longer than the optimal one. The second algorithms does not have such guarantees, but it is known to work pretty well in practice.

### Learning Objectives

- Develop approximation algorithms
- Develop local search solutions
- Compare exact and approximate algorithms
