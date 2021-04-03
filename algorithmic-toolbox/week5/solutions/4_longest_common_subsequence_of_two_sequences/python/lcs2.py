import pprint


def lcs2(s, t):
    D = [[None for x in range(0, len(t) + 1)] for y in range(0, len(s) + 1)]
    for i in range(0, len(s) + 1):
        D[i][0] = 0
    for j in range(0, len(t) + 1):
        D[0][j] = 0

    # forward fill table
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            indel_left = D[i][j - 1]
            indel_top = D[i - 1][j]
            match_diag = D[i - 1][j - 1] + 1
            mismatch_diag = D[i - 1][j - 1]
            if s[i - 1] == t[j - 1]:
                D[i][j] = max(match_diag, indel_left, indel_top)
            else:
                D[i][j] = max(mismatch_diag, indel_left, indel_top)

    # print(" ", [0, *t])
    # for idx, row in enumerate(D):
    #     if idx < 1:
    #         print(" ", row)
    #     else:
    #         print(s[idx - 1], row)

    return D[len(s)][len(t)]


if __name__ == "__main__":
    _ = input()
    a = list(map(int, input().split()))
    _ = input()
    b = list(map(int, input().split()))

    print(lcs2(a, b))
