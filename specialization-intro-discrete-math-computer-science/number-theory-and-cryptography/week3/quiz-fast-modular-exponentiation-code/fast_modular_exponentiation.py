def FastModularExponentiationBKM(b, k, m):
    """Computest b**2**k % m using only 2k modular multiplications.
    """
    # Start with `c = b mod m`
    c = b % m

    # Repeat k times: `c = c**2 mod m`
    i = 0
    while i < k:
        c = (c ** 2) % m
        i += 1

    return c


def FastModularExponentiationBEM(b, e, m):
    """Computes `b^e mod m` using around `2*log2(e)` modular multiplications.
    """
    # 1) Rewrite `e` in binary form
    binary = [x for x in bin(e)][2:]
    # if e == 16, binary == ['1', '0', '0', '0', '0']

    # 2) Compute `b**2**k mod m` for all `2**k <= e`
    max_exponent = len(binary) - 1
    exponents = []
    for idx, exp in enumerate(range(max_exponent, -1, -1)):
        if binary[idx] == "1":
            exponents.append(exp)
    computes = [FastModularExponentiationBKM(b, k, m) for k in exponents]

    # 3) Multiply all results for `2**k` in binary representation of `e`
    result = 1
    for x in computes:
        result *= x

    return result % m
