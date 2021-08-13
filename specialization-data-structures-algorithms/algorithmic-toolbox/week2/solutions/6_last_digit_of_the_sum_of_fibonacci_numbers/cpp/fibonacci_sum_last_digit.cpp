#include <iostream>
#include <cassert>
#include <vector>
#include <numeric>
#include <cmath>

using std::vector;

template <typename T>
std::vector<T> slice(std::vector<T> const &v, int m, int n)
{
    auto first = v.cbegin() + m;
    auto last = v.cbegin() + n + 1;

    std::vector<T> vec(first, last);
    return vec;
}

vector<int> fib_pisano_period(int m)
{
    vector<int> pisano_period = {0, 1};
    long long prev = 0;
    long long current = 1;
    long long swap = 0;
    while (true)
    {
        swap = current;
        current = (current + prev) % m;
        prev = swap;
        if (current == 1 && prev == 0)
        {
            return slice(pisano_period, 0, pisano_period.size() - 1);
        }
        pisano_period.push_back(current);
    }
}

void print_vector(vector<int> v)
{
    for (int i = 0; i < v.size(); ++i)
    {
        std::cout << v.at(i) << " ";
    }
    std::cout << "\n";
}

long long fibonacci_sum(long long n)
{
    if (n <= 1)
    {
        return n;
    }
    vector<int> pisano_period = fib_pisano_period(n);

    long long pisano_period_sum = 0;
    for (auto &n : pisano_period)
        pisano_period_sum += (long long)n;

    long long pisano_period_remainder_sum = 0;
    for (int i = 0; i < (n % 60) + 1; ++i)
    {
        pisano_period_sum = pisano_period_sum + (long long)pisano_period.at(i);
    }

    return ((pisano_period_sum * (long long)floor(n / (long long)60)) + pisano_period_remainder_sum) % (long long)10;
}

void test_solution()
{
    assert(fibonacci_sum(832564823476) == 3);
}

int main()
{
    // print_vector(fib_pisano_period(n));
    // test_solution();

    long long n = 0;
    std::cin >> n;
    std::cout << fibonacci_sum(n);
}
