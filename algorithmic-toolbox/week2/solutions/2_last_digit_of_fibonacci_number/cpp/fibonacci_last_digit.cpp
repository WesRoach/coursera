#include <iostream>
#include <cassert>

int get_fibonacci_last_digit_fast(int n)
{
    if (n <= 1)
    {
        return n;
    }
    int prev = 0;
    int current = 1;
    int swap = 0;
    for (int i = 1; i < n; ++i)
    {
        swap = current;
        current = (current + prev) % 10;
        prev = swap;
    }
    return current;
}

void test_solution()
{
    assert(get_fibonacci_last_digit_fast(3) == 2);
    assert(get_fibonacci_last_digit_fast(10) == 5);
    assert(get_fibonacci_last_digit_fast(45) == 0);
    assert(get_fibonacci_last_digit_fast(311) == 9);
    assert(get_fibonacci_last_digit_fast(327305) == 5);
}

int main()
{
    // test_solution();
    int n;
    std::cin >> n;
    int c = get_fibonacci_last_digit_fast(n);
    std::cout << c << '\n';
}
