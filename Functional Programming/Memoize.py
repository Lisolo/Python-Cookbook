# coding=utf-8

"""
Problem

Suppose we want to get rid of the redundant computation by caching the result of fib 
when it is called for the first time and reuse it when it is needed next time. 
Doing this is very popular in functional programming world and it is called memoize.
"""
def fib(n):
	if n is 0 or n is 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

def memoize(f):
	cache = {}
	def g(x):
		if x not in cache:
			cache[x] = f(x)
		return cache(x)
	return g

fib = trace(fib)
fib = memoize(fib)
print fib(4)