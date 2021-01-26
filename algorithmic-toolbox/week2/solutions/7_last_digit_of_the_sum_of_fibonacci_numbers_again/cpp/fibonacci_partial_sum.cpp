#include <iostream>
#include <cassert>

long long get_fibonacci_partial_sum(long long start, long long end)
{

    long long prev = 0;
    long long current = 1;
    long long swap = 0;

    long long sum = 0;

    for (long long i = 2; i < end + 1; ++i)
    {
        swap = current;
        current = (current + prev) % 10;
        prev = swap;
        if (i >= start)
        {
            sum = sum + current;
        }
    }
    return sum % 10;
}

void test_solution()
{
    assert(get_fibonacci_partial_sum(3, 7) == 1);
    assert(get_fibonacci_partial_sum(10, 10) == 5);
    assert(get_fibonacci_partial_sum(10, 200) == 2);
}

int main()
{
    // test_solution();

    long long start, end;
    std::cin >> start >> end;
    std::cout << get_fibonacci_partial_sum(start, end) << '\n';
}
