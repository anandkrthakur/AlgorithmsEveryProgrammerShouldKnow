#include <stdio.h>

// Iterative function to calculate gcd of two numbers
// using euclid's algortihm
int euclid(int a, int b)
{
	int q, r;

	// the algorithm stops when reaching a zero remainder
	while (b > 0)
	{
		q = a / b;		// quotient
		r = a - q * b;	// remainder

		// or we can simply use (a % b) to calculate r

		// a becomes b and b becomes r (a % b)
		a = b;
		b = r;
	}

	return a;
}

int main()
{
	int a = 2740;
	int b = 1760;

	printf("euclid(%d, %d) = %d", a, b, euclid(a, b));

	return 0;
}