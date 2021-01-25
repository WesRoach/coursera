package fibonacci

import "fmt"

// GetFibonacciLastDigitFast calcualtes the last digit of the nth Fibonacci number
func GetFibonacciLastDigitFast(n int64) int64 {
	if n <= 1 {
		return n
	}
	// 0 1 2 3 4 : n (index)
	// 0 1 1 2 3 : value
	prev, current := int64(0), int64(1)
	for i := int64(1); i < n; i++ {
		current, prev = (current+prev)%10, current
	}
	return current
}

func main() {
	var n int64
	fmt.Scan(&n)

	fmt.Println(GetFibonacciLastDigitFast(n))
}
