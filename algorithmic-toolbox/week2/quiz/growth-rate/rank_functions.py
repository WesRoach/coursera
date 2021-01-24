import math


def rank_functions(funcs: list, n: int = 100_000_000):
    outcomes = sorted([(f(n), idx) for idx, f in enumerate(funcs)])
    return [t[1] + 1 for t in outcomes]


# Sample outcome
rank = rank_functions([lambda n: n ** 2, lambda n: n, lambda n: n ** 3])
print(rank)

# Question 1
rank = rank_functions(
    [
        lambda n: n ** 3,
        lambda n: n ** 0.3,
        lambda n: n,
        lambda n: n ** 0.5,
        lambda n: (n ** 2) / n ** 0.5,
        lambda n: n ** 2,
    ]
)
print(rank)

# Question 2
rank = rank_functions(
    [
        lambda n: 3 ** n,
        lambda n: n * math.log2(n),
        lambda n: math.log(n, 4),
        lambda n: n,
        lambda n: 5 ** math.log2(n),
        lambda n: n ** 2,
        lambda n: n ** 0.5,
        lambda n: 2 ** (2 * n),
    ],
    10_000_000,
)
print(rank)
