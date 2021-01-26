#include <iostream>
#include <cassert>

int fibonacci_sum_squares(long long n)
{
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current = 1;
    long long swap = 0;

    long long r = n % 60; // 60 is the Pisano Period for modulo m=10

    for (long long i = 0; i < r; ++i)
    {
        swap = current;
        current = (previous + current) % 10;
        previous = swap;
    }

    return (previous * current) % 10;
}

void test_solution()
{
    assert(fibonacci_sum_squares(7) == 3);
    assert(fibonacci_sum_squares(73) == 1);
    assert(fibonacci_sum_squares(1234567890) == 0);
}

int main()
{
    // test_solution();

    long long n = 0;
    std::cin >> n;
    std::cout << fibonacci_sum_squares(n);
}
