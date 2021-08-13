def edit_distance(s, t):
    # create 2-dimensional array of length of s, t
    # fill first row and first column with sequentially increasing values
    # s = 'ab', t = 'cde'
    #       | c | d | e
    #   | 0 | 1 | 2 | 3
    # a | 1 |
    # b | 2 |
    D = [[None for x in range(0, len(t) + 1)] for y in range(0, len(s) + 1)]
    for i in range(0, len(s) + 1):
        D[i][0] = i
    for j in range(0, len(t) + 1):
        D[0][j] = j

    # forward fill table
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            insertion = D[i][j - 1] + 1
            deletion = D[i - 1][j] + 1
            match = D[i - 1][j - 1]
            mismatch = D[i - 1][j - 1] + 1
            if s[i - 1] == t[j - 1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)

    return D[len(s)][len(t)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
