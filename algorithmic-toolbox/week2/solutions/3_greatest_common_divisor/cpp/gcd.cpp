#include <iostream>
#include <cassert>

int gcd_naive(int a, int b)
{
    int current_gcd = 1;
    for (int d = 2; d <= a && d <= b; d++)
    {
        if (a % d == 0 && b % d == 0)
        {
            if (d > current_gcd)
            {
                current_gcd = d;
            }
        }
    }
    return current_gcd;
}

int gcd_fast(int a, int b)
{
    int tmp_swap = 0;
    while (b > 0)
    {
        // a, b = b, a % b
        tmp_swap = b;
        b = a % b;
        a = tmp_swap;
    }
    return a;
}

void test_solution()
{
    assert(gcd_fast(18, 35) == 1);
    assert(gcd_fast(28851538, 1183019) == 17657);
    assert(gcd_fast(1827116622, 251772294) == 6);
}

int main()
{
    // test_solution();

    int a, b;
    std::cin >> a >> b;
    std::cout << gcd_fast(a, b) << std::endl;

    return 0;
}
