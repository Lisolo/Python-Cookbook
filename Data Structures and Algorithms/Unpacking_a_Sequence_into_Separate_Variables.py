# coding=utf-8


"""
Problem

You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.

Solution

Any sequence (or iterable) can be unpacked into variables using a simple assignment operation. 
The only requirement is that the number of variables and structure match the sequence. For example:
"""
p = (4, 5)
x, y = p
print x, y
# 4 5

data = ['SOLO', 50, 91.2, (2014, 07, 30)]
name, shares, price, (year, mon, day) = data
print(name, year, mon, day)
#'SOLO' 2014 7 30

p2 = (4, 5)
x, y, z = p2
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: need more than 2 values to unpack
"""

"""
Discussion

Unpacking actually works with any object that happens to be iterable, 
not just tuples or lists. 
This includes strings, files, iterators, and generators. For example:
"""
s = 'Hello'
a, b, c, d, e = s
print(a, b, e)
# 'H' 'e' 'o'

"""
When unpacking, you may sometimes want to discard certain values. 
Python has no special syntax for this, but you can often just pick a throwaway variable name for it. 
For example:
"""
data = ['SOLO', 50, 91.2, (2014, 07, 30)]
_, shares, price, _ = data
print(shares, price)
# 50 91.2

"""
However, make sure that the variable name you pick isn’t being used for something else already.
"""
