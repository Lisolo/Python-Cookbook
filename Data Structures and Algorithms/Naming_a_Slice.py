# coding=utf-8

"""
Problem

Your program has become an unreadable mess of hardcoded slice indices and you want to clean it up.

Solution

Suppose you have some code that is pulling specific data fields out of a record string with fixed fields 
(e.g., from a flat file or similar format):
"""
######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25     ..........'
cost = int(record[20:32] * float(record[40:48]))

"""
Instead of doing that, why not name the slices like this?
"""
SHARES = slice(20, 32)
PRICE = slice(40, 48)

cost2 = int(record[SHARES]) * float(record[PRICE])

"""
In the latter version, you avoid having a lot of mysterious hardcoded indices, and what you’re doing 
becomes much clearer.
"""

"""
Discussion

As a general rule, writing code with a lot of hardcoded index values leads to a readability and 
maintenance mess. For example, if you come back to the code a year later, you’ll look at it and 
wonder what you were thinking when you wrote it. The solution shown is simply a way of more clearly 
stating what your code is actually doing.

In general, the built-in slice() creates a slice object that can be used anywhere a slice is allowed. 
For example:
"""
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
# [2, 3]
print(items[a])
# [2, 3]
items[a] = [10, 11]
print(items)
# [0, 1, 10, 11, 4, 5, 6]
del items[a]
print(items)
# [0, 1, 4, 5, 6]

"""
If you have a slice instance s, you can get more information about it by looking at its s.start, 
s.stop, and s.step attributes, respectively. For example:
"""
a2 = slice(10, 50, 2)
print(a2.start)
# 10
print(a2.stop)
# 50
print(a2.step)
# 2

"""
In addition, you can map a slice onto a sequence of a specific size by using its indices(size) method. 
This returns a tuple (start, stop, step) where all values have been suitably limited to fit within 
bounds (as to avoid IndexError exceptions when indexing). For example:
"""
s = 'HelloWorld'
a3 = slice(5, 10, 2)
a3.indices(len(s))
# (5, 10, 2)
for i in range(*a3.indices(len(s))):
    print(s[i])
# w
# r
# d
