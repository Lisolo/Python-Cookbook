# coding=utf-8

"""
Problem

You have data inside of a sequence, and need to extract values or reduce the sequence using some criteria.

Solution

The easiest way to filter sequence data is often to use a list comprehension. For example:
"""
mylist = [1, 14, -6, 9, -4, 12, 23, -11]
[n for n in mylist if n > 0]
# Returns [1, 14, 9, 12, 23]
[n for n in mylist if n < 0]
# Returns [-6, -4, -11]

"""
One potential downside of using a list comprehension is that it might produce a large result if the 
original input is large. If this is a concern, you can use generator expressions to produce the 
filtered values iteratively. For example:
"""
pos = (n for n in mylist if n > 0)
print(pos)
# <generator object <genexpr> at 0x00D09198>
for x in pos:
    print(x)
# 1
# 14
# 9
# 12
# 23

"""
Sometimes, the filtering criteria cannot be easily expressed in a list comprehension or generator 
expression. For example, suppose that the filtering process involves exception handling or some 
other complicated detail. For this, put the filtering code into its own function and use the 
built-in filter() function. For example:
"""
values = ['5', '7', '-12', '-', '8', 'SOLO', '9']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)
# Outputs ['5', '7', '-12', '8', '9']
"""
filter() creates an iterator, so if you want to create a list of results, make sure you also use list() 
as shown.
"""

"""
Discussion

List comprehensions and generator expressions are often the easiest and most straightforward ways to 
filter simple data. They also have the added power to transform the data at the same time. 
For example:
"""
import math
[math.sqrt(n) for n in mylist if n > 0]
# Returns [1.0, 3.741657386773914, 3.0, 34641016151377544, 4.795831523312719]

"""
One variation on filtering involves replacing the values that don’t meet the criteria with a new value 
instead of discarding them. For example, perhaps instead of just finding positive values, you want to 
also clip bad values to fit within a specified range. This is often easily accomplished by moving the 
filter criterion into a conditional expression like this:
"""
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
# [1, 14, 0, 12, 23, 0]
clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)
# [0, 0, -6, 0, -4, 0, 0, -11]

"""
Another notable filtering tool is itertools.compress(), which takes an iterable and an accompanying 
Boolean selector sequence as input. As output, it gives you all of the items in the iterable where 
the corresponding element in the selector is True. This can be useful if you’re trying to apply 
the results of filtering one sequence to another related sequence. For example, suppose you 
have the following two columns of data:
"""
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

"""
Now suppose you want to make a list of all addresses where the corresponding count value was greater 
than 5. Here’s how you could do it:
"""
from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)
# [False, False, True, False, False, True, True, False]
list(compress(addresses, more5))
# Returns ['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']
"""
The key here is to first create a sequence of Booleans that indicates which elements satisfy the desired 
condition. The compress() function then picks out the items corresponding to True values.

Like filter(), compress() normally returns an iterator. Thus, you need to use list() to turn the results 
into a list if desired.
"""
