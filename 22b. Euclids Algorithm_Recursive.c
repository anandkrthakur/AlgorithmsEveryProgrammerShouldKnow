#include <stdio.h>

// Recursive function to calculate gcd of two numbers
// using euclid's algortihm
int euclid(int a, int b)
{
	if (b <= 0)
		return a;

	int q = a / b;		// quotient
	int r = a - q * b;	// remainder

	// or we can simply use a % b to calculate r

	// a becomes b and b becomes r (a % b)
	return euclid(b, r);
}

int main()
{
	int a = 2740;
	int b = 1760;

	printf("euclid(%d, %d) = %d", a, b, euclid(a, b));

	return 0;
}