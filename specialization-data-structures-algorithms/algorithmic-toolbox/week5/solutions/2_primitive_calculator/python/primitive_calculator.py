from collections import namedtuple
import operator


def flawed_optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1

    return len(sequence) - 1, tuple(reversed(sequence))


Operation = namedtuple("Operation", "forward, reverse, value")


def optimal_sequence(n):
    # forward_dp_step_count[i] = "number of steps to reach value of i"
    dp_step_count = [-1]
    dp_step_count.append(0)  # n of 1 requires 0 steps
    dp_step_count.append(1)  # n of 2 requires 1 step
    dp_step_count.append(1)  # n of 3 requires 1 step

    # dp_step_operation[i] is operator used at step
    # (forward-operator, reverse-operator, value)
    dp_step_operation = [
        Operation(operator.add, operator.sub, 0),  # value 0 irrelevant
        Operation(operator.add, operator.sub, 0),  # value 1 requires no operators
        Operation(operator.mul, operator.floordiv, 2),  # value 2 requires mul(1, 2)
        Operation(operator.mul, operator.floordiv, 3),  # value 3 requires mul(1, 3)
    ]

    if n < 4:
        return dp_step_count[n], (n,)

    for i in range(4, n + 1):
        # list containing steps from operation
        ls = []
        ls.append((dp_step_count[i - 1], 1, Operation(operator.add, operator.sub, 1)))
        if i % 2 == 0:
            ls.append(
                (
                    dp_step_count[i // 2],
                    2,
                    Operation(operator.mul, operator.floordiv, 2),
                )
            )
        if i % 3 == 0:
            ls.append(
                (
                    dp_step_count[i // 3],
                    3,
                    Operation(operator.mul, operator.floordiv, 3),
                )
            )

        min_ls = min(ls)
        dp_step_count.append(min_ls[0] + 1)
        dp_step_operation.append(min_ls[2])

    # Create path through operations to n
    pathing_n = n
    path = [pathing_n]
    while pathing_n != 1:
        operation = dp_step_operation[pathing_n]
        pathing_n = operation.reverse(pathing_n, operation.value)
        path.append(pathing_n)

    return dp_step_count[n], tuple(reversed(path))


if __name__ == "__main__":
    n = int(input())
    operations, sequence = optimal_sequence(n)
    print(operations)
    for x in sequence:
        print(x, end=" ")
