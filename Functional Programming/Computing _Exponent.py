"""
Problem

Mathematically we can define exponent of a number in terms of its smaller power.
"""
def exp(x, n):
	"""
    Computes the result of x raised to the power of n.

        >>> exp(2, 3)
        8
        >>> exp(3, 2)
        9
	"""
	if n == 0:
		return 1
	else:
		return x * exp(x, n -1)

def fast_exp(x, n):
	if n == 0:
		return 1
	elif n % 2 == 0:
		return fast_exp(x*x, n/2)
	else:
		return x * fast_exp(x, n-1)