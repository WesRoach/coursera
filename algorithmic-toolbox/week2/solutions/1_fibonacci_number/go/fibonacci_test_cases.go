package fibonacci

type inputTest struct {
	input    int64
	expected int64
}

var fibonacciTestCases = []inputTest{
	{
		input:    3,
		expected: 2,
	},
	{
		input:    9,
		expected: 34,
	},
	{
		input:    10,
		expected: 55,
	},
	{
		input:    45,
		expected: 1134903170,
	},
	// {
	// 	input:    331,
	// 	expected: 668996615388005031531000081241745415306766517246774551964595292186469,
	// },
}
