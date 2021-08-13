package fibonacci

type inputTest struct {
	input    int64
	expected int64
}

var getFibonacciLastDigitFastTestCases = []inputTest{
	{
		input:    3,
		expected: 2,
	},
	{
		input:    9,
		expected: 4,
	},
	{
		input:    10,
		expected: 5,
	},
	{
		input:    45,
		expected: 0,
	},
	{
		input:    331,
		expected: 9,
	},
	{
		input:    327305,
		expected: 5,
	},
}
