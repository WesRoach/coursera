#include <iostream>
#include <cassert>

long long lcm_naive(int a, int b)
{
    for (long l = 1; l <= (long long)a * b; ++l)
        if (l % a == 0 && l % b == 0)
            return l;

    return (long long)a * b;
}

long long gcd(long long a, long long b)
{
    long long tmp_swap = 0;
    while (b > 0)
    {
        // a, b = b, a % b
        tmp_swap = b;
        b = a % b;
        a = tmp_swap;
    }
    return a;
}

long long lcm_fast(long long a, long long b)
{
    return (a * b) / gcd(a, b);
}

void test_solution()
{
    assert(lcm_fast(6, 8) == 24);
    assert(lcm_fast(761457, 614573) == 467970912861);
}

int main()
{
    // test_solution();
    int a, b;
    std::cin >> a >> b;
    // std::cout << lcm_naive(a, b) << std::endl;
    std::cout << lcm_fast(a, b) << std::endl;
    return 0;
}
