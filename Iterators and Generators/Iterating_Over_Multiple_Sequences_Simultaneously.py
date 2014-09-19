# coding=utf-8

"""
Problem

You want to iterate over the items contained in more than one sequence at a time.

Solution

To iterate over more than one sequence simultaneously, use the zip() function. For example:
"""
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
	print(x, y)
# (1, 101)
# (5, 78)
# (4, 37)
# (2, 15)
# (10, 62)
# (7, 99)

"""
zip(a, b) works by creating an iterator that produces tuples (x, y) where x is taken from a and y is taken from b. 
Iteration stops whenever one of the input sequences is exhausted. Thus, the length of the iteration is the same as 
the length of the shortest input. For example:
"""
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a,b):
	print(i)
# (1, 'w')
# (2, 'x')
# (3, 'y')

"""
If this behavior is not desired, use itertools.izip_longest() instead. For example:
"""
from itertools import izip_longest
for i in izip_longest(a, b):
	print(i)
# (1, 'w')
# (2, 'x')
# (3, 'y')
# (None, 'z')
for i in izip_longest(a ,b, fillvalue=0):
	print(i)
# (1, 'w')
# (2, 'x')
# (3, 'y')
# (0, 'z')


"""
Discussion

zip() is commonly used whenever you need to pair data together. For example, suppose you have a list of column headers 
and column values like this:
"""
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]

"""
Using zip(), you can pair the values together to make a dictionary like this:
"""
s = dict(zip(headers,values))

"""
Alternatively, if you are trying to produce output, you can write code like this:
"""
for name, val in zip(headers, values):
	print(name, '=', val)
# ('name', '=', 'ACME')
# ('shares', '=', 100)
# ('price', '=', 490.1)

"""
It’s less common, but zip() can be passed more than two sequences as input. For this case, the resulting tuples have 
the same number of items in them as the number of input sequences. For example:
"""
c = [1, 2, 3]
d = [10, 11, 12]
e = ['x', 'y', 'z']
for i in zip(c, d, e):
	print(i)
# (1, 10, 'x')
# (2, 11, 'y')
# (3, 12, 'z')

"""
Last, but not least, it’s important to emphasize that zip() creates an iterator as a result. If you need the paired 
values stored in a list, use the list() function. For example:
"""
zip(c, d)
# Returns <zip object at 0x1074952a8>
list(zip(c, d))
# Returns [(1, 10), (2, 11), (3, 12)]
