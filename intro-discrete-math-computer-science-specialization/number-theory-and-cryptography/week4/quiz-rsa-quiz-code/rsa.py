from functools import reduce
import math


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


def PowMod(a, n, modulo):
    """Computes `a^n mod{modulo}`
    """
    # 1) Rewrite `e` in binary form
    binary = [x for x in bin(n)][2:]
    # if e == 16, binary == ['1', '0', '0', '0', '0']

    # 2) Compute `b**2**k mod m` for all `2**k <= e`
    max_exponent = len(binary) - 1
    exponents = []
    for idx, exp in enumerate(range(max_exponent, -1, -1)):
        if binary[idx] == "1":
            exponents.append(exp)
    computes = [FastModularExponentiationBKM(a, k, modulo) for k in exponents]

    # 3) Multiply all results for `2**k` in binary representation of `e`
    result = 1
    for x in computes:
        result *= x

    return result % modulo


def ConvertToInt(message: str) -> int:
    """Converts message to an int"""
    lst = []
    for ch in message:
        hv = hex(ord(ch)).replace("0x", "")
        if len(hv) == 1:
            hv = "0" + hv
        lst.append(hv)
    return int(reduce(lambda x, y: x + y, lst), base=16)


# Converts hex to string
def toStr(s):
    return s and chr(int(s[:2], base=16)) + toStr(s[2:]) or ""


def ConvertToStr(m: int) -> str:
    hx = hex(m)[2:]
    return toStr(hx)


def Encrypt(message, modulo, exponent):
    """
    Question 1
    ----------

    Implement RSA encryption with the given public key `modulo`, `exponent`.

    You have access to the function `PowMod(a,n,modulo)` which computes
    `a^n mod{modulo}` using the fast modular exponentiation algorithm
    from the previous module. You also have access to the function
    `ConvertToInt(message)` which converts a text message to an integer.

    You need to fix the implementation of the function
    `Encrypt(message, modulo, exponent)` to return the integer
    `ciphertext` according to RSA encryption algorithm.
    """
    return PowMod(ConvertToInt(message), exponent, modulo)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def InvertModulo(a, n):
    """
    Accepts coprime integers `a` and `n` as inputs

    Returns
    -------

    `b`, such that `ab ≡ 1 mod n`
    """
    g, x, y = egcd(a, n)
    if g != 1:
        raise Exception("modular inverse does not exist")
    else:
        return x % n


def Decrypt(ciphertext, p, q, exponent):
    """
    Question 2

    Implement RSA decryption with the given private key `p`, `q`, `exponent`.

    You have access to the function `ConvertToStr(m)` which converts
    from integer `m` to the plaintext `message`. You also have access
    to the function `InvertModulo(a, n)` which takes coprime integers `a`
    and `n` as inputs and returns integer `b` such that
    `ab ≡ 1 mod n`. You also have access to the function `PowMod(a, n, modulo)`
    which computes `a^n mod{modulo}` using fast modular exponentiation.

    You need to fix the implementation of the function
    `Decrypt(ciphertext, p, q, exponent)` to decrypt the `message` which
    was encrypted using the public key `(n=p⋅q, e=exponent)`.
    """
    n = p * q
    comp = (p - 1) * (q - 1)
    d = InvertModulo(exponent, comp)
    return ConvertToStr(PowMod(ciphertext, d, n))


def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
    """
    Question 3
    ----------

    Secret agent Alice has sent one of the following messages to the
    center:

        `attack`
        `don't attack`
        `wait`

    Alice has ciphered her message using public key `modulo`, `exponent`,
    that is available to you, and you have intercepted her ciphertext.
    You want to know what was the content of her message. You have
    access to the function `Encrypt(message, modulo, exponent)` which
    takes in a message as a string and returns a big integer as a ciphertext.
    It uses RSA encryption with public key `modulo`, `exponent`.
    In the starter code, you have an example usage of the function
    `Encrypt`.

    You also have function `DecipherSimple(ciphertext, modulo, exponent, potential_messages)`
    implemented in the starter code. You need to fix this implementation
    to solve the problem. It should take the `ciphertext` sent from
    Alice to the center, the public key `modulo`, `exponent` and the
    set of potential messages that Alice could have sent, and return
    the message that Alice encrypted and sent as a string.
    For example, if Alice took message "wait", encrypted it with the
    given `modulo` and `exponent`, and got number 139763215139763215
    as the ciphertext, you will need to return the string "wait"
    given the `ciphertext=139763215`, `modulo`, `exponent` and
    `potential_messages = ["attack", "don't attack", "wait"]`.
    """
    for message in potential_messages:
        if ciphertext == Encrypt(message, modulo, exponent):
            return message
    return "don't know"


def DecipherSmallPrime(ciphertext, modulo, exponent):
    """
    Question 4
    ----------

    Alice is using RSA encryption with a public key `modulo`, `exponent`
    such that `modulo=p⋅q` with one of the primes `p` and `q` being
    less than `1_000_000`, and you know about it.
    You want to break the cipher and decrypt her message.

    You can use the function `Decrypt(ciphertext, p, q, e)` which
    decrypts the `ciphertext` given the private key `p`, `q` and the
    public exponent `e`.

    You are also given the function
    `DecipherSmallPrime(ciphertext, modulo, exponent)`, and you need
    to fix its implementation so that it can decipher the `ciphertext`
    in case when one of the prime factors of the public modulo is
    smaller than `1_000_000`.
    """
    if modulo % 2 == 0:
        small_prime = 2
        big_prime = modulo // 2
        return Decrypt(ciphertext, small_prime, big_prime, exponent)
    for small_prime in range(3, 1_000_000, 2):
        big_prime = modulo // small_prime
        if big_prime * small_prime == modulo:
            return Decrypt(ciphertext, small_prime, big_prime, exponent)
    return "don't know"


def IntSqrt(n):
    """Returns the largest int `x` such that x^2 <= n"""
    return int(math.isqrt(n))


def DecipherSmallDiff(ciphertext, modulo, exponent):
    """
    Question 5
    ----------

    Alice is using RSA encryption with a public key `modulo`, `exponent`
    such that `modulo=p⋅q` with `∣p−q∣<5000`, and you know about it.
    You want to break the cipher and decrypt her message.

    You have access to the function `Decrypt(ciphertext, p, q, e)`
    which decrypts the `ciphertext` given the private key `p`, `q` and
    the public exponent `e`. You also have access to the function
    `IntSqrt(n)` which takes integer `n` and returns the largest
    integer `x` such that `x^2 ≤ n`.

    You are also given the function
    `DecipherSmallDiff(ciphertext, modulo, exponent)`, and you need to
    fix its implementation so that it can decipher the `ciphertext`
    in case when the difference beteween prime factors of the public
    modulo is smaller than `5000`.
    """
    small_prime = IntSqrt(modulo)
    if small_prime % 2 == 0:
        small_prime -= 1
    big_prime = small_prime
    while big_prime - small_prime < 5000:
        current_modulo = big_prime * small_prime
        if current_modulo == modulo:
            return Decrypt(ciphertext, small_prime, big_prime, exponent)
        elif current_modulo > modulo:
            small_prime -= 2
        elif current_modulo < modulo:
            big_prime += 2


def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)


def DecipherCommonDivisor(
    first_ciphertext,
    first_modulo,
    first_exponent,
    second_ciphertext,
    second_modulo,
    second_exponent,
):
    """
    Question 6
    ----------

    You've discovered that the first prime number `p` for the private
    key was generated with the same algorithm and the same random seed
    by two different senders Alice and Angelina due to insufficient
    randomness, while the second prime `q` is different for those two
    private keys. You want to break both ciphers and decipher messages
    from both Alice and Angelina.

    You are given the function `Decrypt(ciphertext, p, q, e)` which
    decrypts the ciphertextciphertext given the private key `p`, `q`
    and the public exponent `e`.

    You are also given the function DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo, second_exponent).

    You need to fix its implementation so that it can decipher both
    `first_ciphertext` and `second_ciphertext` in case when
    `first_modulo` and `second_modulo` share a prime factor.
    """
    common_prime = GCD(first_modulo, second_modulo)
    if first_modulo % common_prime == 0 and second_modulo % common_prime == 0:
        q1 = first_modulo // common_prime
        q2 = second_modulo // common_prime
        return (
            Decrypt(first_ciphertext, common_prime, q1, first_exponent),
            Decrypt(second_ciphertext, common_prime, q2, second_exponent),
        )
    return ("unknown message 1", "unknown message 2")


# Quiz Question 7
def ExtendedEuclid(a, b):
    if b == 0:
        x, y = 1, 0
    else:
        (p, q) = ExtendedEuclid(b, a % b)
        x = q
        y = p - q * (a // b)

    return (x, y)


def ChineseRemainderTheorem(n1, r1, n2, r2):
    (x, y) = ExtendedEuclid(n1, n2)
    n = r1 * n2 * y + r2 * n1 * x
    return n % (n1 * n2)


def DecipherHastad(
    first_ciphertext, first_modulo, second_ciphertext, second_modulo
):
    """
    Question 7
    ----------

    Bob has sent the same message to Alice and Angelina using two
    different public keys `(n_1, e=2)` and `(n_2, e=2)` with the
    same exponent `e=2`. Implement Hastad's broadcast attack
    from the lectures for this case to decipher the message using
    the intercepted ciphertexts `first_ciphertext` and `second_ciphertext`.

    You have access to the function `ConvertToStr(m)` which converts
    an integer to a plaintext message. You also have access to the
    function `ChineseRemainderTheorem(n_1, r_1, n_2, r_2)` which
    takes two coprime modulos `n_1` and `n_2` and two corresponding
    remainders `r_1` and `r_2`, and returns such integer `r` that
    `r ≡ r_1 mod{n_1}`, and `r ≡ r_2 mod{n_2}` and `0 ≤ r < n_1 * n_2`.
    You also have access to the function `IntSqrt(n)` which takes an
    integer `n` and returns the largest integer `x` such that `x^2 ≤ n`.

    Fix the implementation of the function `DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo)`
    to return the message that Bob has encrypted and sent.
    """
    # Fix this implementation
    r = ChineseRemainderTheorem(
        first_modulo, first_ciphertext, second_modulo, second_ciphertext
    )
    return ConvertToStr(IntSqrt(r))
