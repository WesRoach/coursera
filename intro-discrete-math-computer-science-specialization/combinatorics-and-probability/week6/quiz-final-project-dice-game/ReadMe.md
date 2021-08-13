# Project Overview

In this series of three programming tasks, we will implement together a program that will play optimally in a tricky dice game! You program will be given a list of dices and will decide who chooses the dice first (you or your opponent).

When the dices are chosen, we will simulate 10000 throws. Each time your number is greater, you get $1 from your opponent. Conversely, each time your number is smaller, you pay $1 to your opponent.

Your ultimate goal is to implement a program that always wins in such a simulation.

## First Task: Compare Two Die

Implement a function that takes two dices as input and computes two values: the first value is the number of times the first dice wins (out of all possible 36 choices), the second value is the number of times the second dice wins. We say that a dice wins if the number on it is greater than the number on the other dice.

To debug your implementation, use the following test cases:

### Sample 1

```python
dice1 = [1, 2, 3, 4, 5, 6], dice2 = [1, 2, 3, 4, 5, 6]
count_wins(dice1, dice2)
>> (15, 15)
```

### Sample 2

```python
dice1 = [1, 1, 6, 6, 8, 8], dice2 = [2, 2, 4, 4, 9, 9]
count_wins(dice1, dice2)
>> (16, 20)
```

## Second Task: Is there the Best Dice?

Now, your goal is to check whether among the three given dices there is one that is better than the remaining two dices.

Implement a function that takes a list of dices and checks whether there is dice (in this list) that is better than all other dices. We say that a dice is better than another one, if it wins more frequently (that is, out of all 36 possibilities, it wins in aa cases, while the second one wins in bb cases, and a>ba>b). If there is such a dice, return its (0-based) index. Otherwise, return -1.

Use the following datasets for debugging:

### Sample 1

```python
dices = [[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]
find_the_best_dice(dices)
>> -1
```

### Sample 2

```python
dices = [[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]
find_the_best_dice(dices)
>> 2
```

### Sample 3


```python
dices = [
    [3, 3, 3, 3, 3, 3],
    [6, 6, 2, 2, 2, 2],
    [4, 4, 4, 4, 0, 0],
    [5, 5, 5, 1, 1, 1],
]
find_the_best_dice(dices)
>> -1
```

## Third Task: Implement a Strategy

You are now ready to play!

Implement a function that takes a list of dices (possibly more than three) and returns a strategy. The strategy is a dictionary:

If, after analyzing the given list of dices, you decide to choose a dice first, set strategy["choose_first"] to True and set strategy["first_dice"] to be the (0-based) index of the dice you would like to choose

If you would like to be the second one to choose a dice, set strategy["choose_first"] to False. Then, specify, for each dice that your opponent may take, the dice that you would take in return. Namely, for each i from 0 to len(dices)-1, set strategy[i] to an index j of the dice that you would take if the opponent takes the i-th dice first.

Use the following datasets for debugging:

### Sample 1

```python
compute_strategy(
    [
        [1, 1, 4, 6, 7, 8],
        [2, 2, 2, 6, 7, 7],
        [3, 3, 3, 5, 5, 8]
    ]
)
>> {'choose_first': False, 0: 1, 1: 2, 2: 0}
```

### Sample 2

```python
compute_strategy(
    [
        [4, 4, 4, 4, 0, 0],
        [7, 7, 3, 3, 3, 3],
        [6, 6, 2, 2, 2, 2],
        [5, 5, 5, 1, 1, 1]
    ]
)
>> {'choose_first': True, 'first_dice': 1}
```

Note that your answers do not have to coincide with the answers above. First, the order of elements does not matter in the dictionary. Second, the dictionary might contain extra information that is not required in the statement of the problem. For example, {0: 3, 'first_dice': 1, 'choose_first': True} is also a correct output in Sample 2.
