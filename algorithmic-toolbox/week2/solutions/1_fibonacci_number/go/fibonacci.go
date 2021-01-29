package main

import "fmt"

// Fibonacci calcualtes the nth Fibonacci number
func Fibonacci(n int64) int64 {
	if n <= 1 {
		return n
	}
	// 0 1 2 3 4 : n (index)
	// 0 1 1 2 3 : value
	prev, current := int64(0), int64(1)
	for i := int64(1); i < n; i++ {
		current, prev = current+prev, current
	}
	return current
}

func main() {
	var n int64
	fmt.Scan(&n)

	fmt.Println(Fibonacci(n))
}
