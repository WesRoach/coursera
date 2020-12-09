def sequence(have="MARINE"):
    string = [x for x in have]
    for tup in [(0, 1), (2, 3), (1, 2), (2, 3), (4, 5)]:
        string[tup[0]], string[tup[1]] = string[tup[1]], string[tup[0]]

    return "".join(string)


print(sequence())
