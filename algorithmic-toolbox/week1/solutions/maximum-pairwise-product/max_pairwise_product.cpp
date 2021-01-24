#include <iostream>
#include <vector>
#include <algorithm>

long long MaxPairwiseProduct(const std::vector<int> &numbers)
{
    long long max_product = 0;
    int n = numbers.size();

    for (int first = 0; first < n; ++first)
    {
        for (int second = first + 1; second < n; ++second)
        {
            max_product = std::max(max_product,
                                   ((long long)numbers[first]) * numbers[second]);
        }
    }

    return max_product;
}

long long MaxPairwiseProductFast(const std::vector<int> &numbers)
{
    long long larger = std::max(numbers[0], numbers[1]);
    long long smaller = std::min(numbers[0], numbers[1]);
    int n = numbers.size();

    for (int i = 2; i < n; ++i)
    { // iterate through all numbers and find the largest 2
        if (numbers[i] > larger)
        {                        // if current number is larger than the larger number
            smaller = larger;    // set the smaller number = to current larger
            larger = numbers[i]; // set the /new/ larger number to current
        }
        else if (numbers[i] > smaller) // if current number is larger than smaller
            smaller = numbers[i];      // replace small with current number
    }
    return smaller * larger;
}

int main()
{
    // Stress Test Loop
    // while (true)
    // {
    //     int n = rand() % 10 + 2;
    //     std::cout << n << "\n";
    //     std::vector<int> a;
    //     for (int i = 0; i < n; ++i)
    //     {
    //         a.push_back(rand() % 100000);
    //     }
    //     for (int i = 0; i < n; ++i)
    //     {
    //         std::cout << a[i] << " ";
    //     }
    //     std::cout << "\n";
    //     long long res1 = MaxPairwiseProduct(a);
    //     long long res2 = MaxPairwiseProductFast(a);
    //     if (res1 != res2)
    //     {
    //         std::cout << "Wrong Answer: " << res1 << " " << res2 << "\n";
    //         break;
    //     }
    //     else
    //     {
    //         std::cout << "OK\n";
    //     }
    // }
    int n; // Collect n from std input
    std::cin >> n;
    std::vector<int> numbers(n); // create vector/array of size n
    for (int i = 0; i < n; ++i)
    { // fill vector with numbers
        std::cin >> numbers[i];
    }

    std::cout << MaxPairwiseProductFast(numbers) << "\n"; // Calculate over vector
    return 0;
}
