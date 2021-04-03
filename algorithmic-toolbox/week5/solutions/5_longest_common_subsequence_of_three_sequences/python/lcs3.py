# import pprint


def lcs3(s, t, v):
    D = [
        [[0 for x in range(0, len(v) + 1)] for y in range(0, len(t) + 1)]
        for z in range(0, len(s) + 1)
    ]

    # forward fill table
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            for k in range(1, len(v) + 1):
                indel_top = D[i - 1][j][k]
                indel_left = D[i][j - 1][k]
                indel_top_left = D[i][j][k - 1]

                match_diag = D[i - 1][j - 1][k - 1] + 1
                mismatch_diag = D[i - 1][j - 1][k - 1]

                if s[i - 1] == t[j - 1] and t[j - 1] == v[k - 1]:
                    D[i][j][k] = max(match_diag, indel_left, indel_top, indel_top_left)
                else:
                    D[i][j][k] = max(
                        mismatch_diag, indel_left, indel_top, indel_top_left
                    )

    # pprint.pprint(D)

    return D[len(s)][len(t)][len(v)]


if __name__ == "__main__":
    _ = input()
    a = list(map(int, input().split()))
    _ = input()
    b = list(map(int, input().split()))
    _ = input()
    c = list(map(int, input().split()))

    print(lcs3(a, b, c))
