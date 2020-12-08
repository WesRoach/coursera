def sum_values(fn=lambda n: n * (n + 1)):
    summ = 0
    for n in range(1, 100):
        summ += 1 / fn(n)
    return summ


print(sum_values())
