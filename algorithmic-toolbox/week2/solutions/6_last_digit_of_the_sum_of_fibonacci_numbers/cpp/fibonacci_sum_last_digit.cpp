#include <iostream>

long long fibonacci_sum(long long n)
{
    if (n <= 1)
    {
        return n;
    }
    long long prev = 0;
    long long current = 1;
    long long swap = 0;
    long long sum = 1;
    for (long long i = 1; i < n; ++i)
    {
        swap = current;
        current = (current + prev) % 10;
        prev = swap;
        sum = sum + current;
    }
    return sum % 10;
}

int main()
{
    long long n = 0;
    std::cin >> n;
    std::cout << fibonacci_sum(n);
}
