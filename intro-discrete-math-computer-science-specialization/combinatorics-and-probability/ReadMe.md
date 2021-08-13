# Combinatorics and Probability

Counting is one of the basic mathematically related tasks we encounter on a day to day basis. The main question here is the following. If we need to count something, can we do anything better than just counting all objects one by one? Do we need to create a list of all phone numbers to ensure that there are enough phone numbers for everyone? Is there a way to tell that our algorithm will run in a reasonable time before implementing and actually running it? All these questions are addressed by a mathematical field called Combinatorics.

In this course we discuss most standard combinatorial settings that can help to answer questions of this type. We will especially concentrate on developing the ability to distinguish these settings in real life and algorithmic problems. This will help the learner to actually implement new knowledge. Apart from that we will discuss recursive technique for counting that is important for algorithmic implementations.

One of the main `consumers’ of Combinatorics is Probability Theory. This area is connected with numerous sides of life, on one hand being an important concept in everyday life and on the other hand being an indispensable tool in such modern and important fields as Statistics and Machine Learning. In this course we will concentrate on providing the working knowledge of basics of probability and a good intuition in this area. The practice shows that such an intuition is not easy to develop.

In the end of the course we will create a program that successfully plays a tricky and very counterintuitive dice game.

As prerequisites we assume only basic math (e.g., we expect you to know what is a square or how to add fractions), basic programming in python (functions, loops, recursion), common sense and curiosity. Our intended audience are all people that work or plan to work in IT, starting from motivated high school students.

Do you have technical problems? Write to us: coursera@hse.ru

## Week 1 - Basic Counting

Suppose we need to count certain objects. Can we do anything better than just list all the objects? Do we need to create a list all phone numbers to check whether there are enough phone numbers for everyone? Is there a way to tell whether our algorithm will run in a reasonable time before implementing and actually running it? All these questions are addressed by a mathematical field called Combinatorics. In this module we will give an introduction to this field that will help us to answer basic versions of the above questions.

### Learning Objectives

- Use basic methods of combinatorics to count objects
- Count the number of objects in basic combinatorial settings
- Categorize counting problems into basic combinatorial settings
- Apply standard operations to sets of objects


## Week 2 - Binomial Coefficients

In how many ways one can select a team of five students out of ten students? What is the number of non-negative integers with at five digits whose digits are decreasing? In how many ways one can get from the bottom left cell to the top right cell of a 5x5 grid, each time going either up or to the right? And why all these three numbers are equal? We'll figure this out in this module!

### Learning Objectives

- Compute binomial coefficients
- Compute number of subsets
- Apply the binomial theorem
- Develop programs for generating combinatorial objects

## Week 3 - Advanced Counting

We have already considered most of the most standard settings in Combinatorics, that allow us to address many counting problems. However, successful application of this knowledge on practice requires considerable experience in this kind of problems. In this module we will address the final standard setting in our course, combinations with repetitions, and then we will gain some experience by discussing various problems in Combinatorics.

### Learning Objectives

- Use standard combinatorial settings in counting problems
- Categorize counting problems into standard combinatorial settings
- Count number of objects via standard combinatorial settings
- Combine several combinatorial settings to solve counting problems

## Week 4 - Probability

The word "probability" is used quite often in the everyday life. However, not always we can speak about probability as some number: for that a mathematical model is needed. What is this mathematical model (probability space)? How to compute probabilities (if the model is given)? How to judge whether the model is adequate? What is conditional probability and Bayes' theorem? How our plausible reasoning can be interpreted in terms of Bayes' theorem? In this module we cover these questions using some simple examples of probability spaces and real life sutiations.

### Learning Objectives

- Propose a probability space for a given probability setting
- Compute probabilities in simple cases with equiprobable outcomes
- Judge whether a probabilistic model is adequate for a practical situation
- Find the values of conditional probabilities in simple example

## Week 5 - Random Variables

In the previous module we discussed how to compute probabilities of random events. But in many practical situation we are interested not only in positive or negative outcome, but also in some quantitative characteristics of an outcome. Among these cases are number of steps of an algorithms, number of points that one can win in the games involving any kind of randomness, all quantitative characteristics of a random person in some group of people. Basically settings of this kind arise in all situations when (a) any kind of uncertainty is presented (b) we are interested in quantitative characteristics. The mathematical model for this is called random variables. And we will discuss them in this module.

### Learning Objectives

- Use linearity to compute expected values
- Estimate probability using expected values
- Distinguish random variables in random experiments
- Compute expected values of random of radom variables

## Week 6 - Project: Dice Games

In this module, we will apply accumulated knowledge to create a project solving a certain dice game. The game is very simple: two players pick a dice each from a given pool of dices with various numbers on their sides. Then each player throws his dice and the one with the greater number on his dice wins. The game looks very simple and it seems that it is very easy to play this game optimally once we know our pool of dices. Yet it turns out that this intuition is overwhelmingly wrong: the game turns out to be very counterintuitive. In this module we will discuss the game in detail and create a program that finds an optimal strategy to play the game on a given pool of dices.

### Learning Objectives

- Create a program playing a dice game
- Use probability theory in programming project
- Determine a winning strategy in a dice game
