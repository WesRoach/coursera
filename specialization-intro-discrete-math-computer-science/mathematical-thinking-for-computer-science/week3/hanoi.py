def hanoi(num):
    """
    Return steps to solve hanoi tower of `num` height.
    """
    # Create disks; Larger number == larger disk
    # list.pop() will return the top disk
    discs = [x for x in range(num, 0, -1)]
    towers = [discs, [], []]
    rounds = []

    rounds.append(towers)

    print_rounds(rounds)


cnt = 0


def solve_toh(n, source, destination, auxiliary):
    global cnt
    if n == 1:
        print(f"Move disk 1 from source {source} to destination {destination}")
        cnt += 1
        return
    solve_toh(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from source {source} to destination {destination}")
    cnt += 1
    solve_toh(n - 1, auxiliary, destination, source)


def print_rounds(rounds):
    """Prints supplied list of lists"""
    for idx, rnd in enumerate(rounds):
        print(f"## Round {idx + 1} ##")
        for tower in rnd:
            print(tower)


solve_toh(6, 1, 3, 2)
print(cnt)
