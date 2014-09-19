"""
Problem

Suppose we want to trace all the calls to the fib function. We can write a higher order function to return a new function, 
which prints whenever fib function is called.
"""
def trace(f):
	f.indent = 0
	def g(x):
		print '|  ' * f.indent + '|--', f.__name__, x
		f.indent += 1
		value = f(x)
		print '|  ' * f.indent + '|--', 'return', repr(value)
		f.indent -= 1
		return value
	return g

@trace
def fib(n):
	if n is 0 or n is 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

"""
fib = trace(fib)
"""
print fib(4)

"""
Suppose we want to get rid of the redundant computation by caching the result of fib 
when it is called for the first time and reuse it when it is needed next time. 
Doing this is very popular in functional programming world and it is called memoize.
"""
def memoize(f):
	cache = {}
	def g(x):
		if x not in cache:
			cache[x] = f(x)
		return cache[x]
	return g

fib = memoize(fib)
print fib(4)