package fibonacci

import "testing"

func TestFibonacci(t *testing.T) {
	for _, test := range fibonacciTestCases {
		res := Fibonacci(test.input)
		if res != test.expected {
			t.Errorf("Fibonacci(%v), expected: %v, actual: %v", test.input, test.expected, res)
		}
	}
}

func BenchmarkFibonacci(b *testing.B) {
	for i := 0; i < b.N; i++ {
		for _, test := range fibonacciTestCases {
			Fibonacci(test.input)
		}
	}
}
