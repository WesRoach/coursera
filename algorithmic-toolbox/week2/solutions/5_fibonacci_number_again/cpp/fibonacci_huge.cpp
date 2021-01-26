#include <iostream>
#include <cassert>

long long fibonacci_pisano_period_length(long long m)
{
    long long pisano_length = 0;
    long long prev = 0;
    long long current = 1;
    long long tmp_swap = 0;
    while (true)
    {
        tmp_swap = current;
        current = (current + prev) % m;
        prev = tmp_swap;
        ++pisano_length;
        if (current == 1 && prev == 0)
        {
            return pisano_length;
        }
    }
}

long long fibonacci(long long n)
{
    if (n <= 1)
    {
        return n;
    }
    long long prev = 0;
    long long current = 1;
    long long swap = 0;
    for (long long i = 1; i < n; ++i)
    {
        swap = current;
        current = current + prev;
        prev = swap;
    }
    return current;
}

long long fibonacci_mod(long long n, long long m)
{
    if (n <= 1)
    {
        return n;
    }
    long long prev = 0;
    long long current = 1;
    long long swap = 1;
    for (long long i = 1; i < n; ++i)
    {
        swap = current;
        current = (current + prev) % m;
        prev = swap;
    }
    return current;
}

long long fibonacci_mod_m(long long n, long long m)
{
    long long pisano_length = fibonacci_pisano_period_length(m);
    long long remainder = n % pisano_length;
    return fibonacci_mod(remainder, m);
}

void test_solution()
{
    assert(fibonacci(10) == 55);
    assert(fibonacci_pisano_period_length(2) == 3);
    assert(fibonacci_pisano_period_length(3) == 8);
    assert(fibonacci_mod_m(239, 1000) == 161);
    assert(fibonacci_mod_m(2816213588, 239) == 151);
}

int main()
{
    // test_solution();

    long long n, m;
    std::cin >> n >> m;
    std::cout << fibonacci_mod_m(n, m) << '\n';
}
