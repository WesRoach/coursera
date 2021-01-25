package fibonacci

import "testing"

func TestGetFibonacciLastDigitFast(t *testing.T) {
	for _, test := range getFibonacciLastDigitFastTestCases {
		res := GetFibonacciLastDigitFast(test.input)
		if res != test.expected {
			t.Errorf("GetFibonacciLastDigitFast(%v), expected: %v, actual: %v", test.input, test.expected, res)
		}
	}
}

func BenchmarkGetFibonacciLastDigitFast(b *testing.B) {
	for i := 0; i < b.N; i++ {
		for _, test := range getFibonacciLastDigitFastTestCases {
			GetFibonacciLastDigitFast(test.input)
		}
	}
}
