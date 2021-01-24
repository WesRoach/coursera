package main

import (
	"fmt"
)

// Min calculates the min value of two ints
func Min(x, y int64) int64 {
	if x < y {
		return x
	}
	return y
}

// Max calculates the max value of two ints
func Max(x, y int64) int64 {
	if x > y {
		return x
	}
	return y
}

// MaxPairwiseProduct calcualtes the max pairwise product from a given array
func MaxPairwiseProduct(numbers []int64) int64 {
	larger := Max(numbers[0], numbers[1])
	smaller := Min(numbers[0], numbers[1])

	for i := 2; i < len(numbers); i++ {
		if numbers[i] > larger {
			smaller = larger
			larger = numbers[i]
		} else if numbers[i] > smaller {
			smaller = numbers[i]
		}
	}
	return smaller * larger
}

func main() {
	var n int
	fmt.Scan(&n)

	numbers := make([]int64, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&numbers[i])
	}

	// for i := range numbers {
	// 	fmt.Println(numbers[i])
	// }

	fmt.Println(MaxPairwiseProduct(numbers))

}
