# coding=utf-8


"""
Problem

You need to execute a reduction function (e.g., sum(), min(), max()), but first need to transform or 
filter the data.

Solution

A very elegant way to combine a data reduction and a transformation is to use a generator-expression 
argument. For example, if you want to calculate the sum of squares, do the following:
"""
nums = [1, 2, 3, 4, 5]
result = sum(x * x for x in nums)

"""
Here are a few other examples:
"""
# Determine if any .py files exits in a directory
import os
files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)

"""
Discussion

The solution shows a subtle syntactic aspect of generator expressions when supplied as the single 
argument to a function (i.e., you don’t need repeated parentheses). For example, these statements 
are the same:
"""
result2 = sum((x * x for x in nums))   # Pass generator-expr as argument
result = sum(x * x for x in nums)     # More elegant syntax

"""
Using a generator argument is often a more efficient and elegant approach than first creating a temporary 
list. For example, if you didn’t use a generator expression, you might consider this alternative 
implementation:
"""
result3 = sum([x * x for x in nums])

"""
This works, but it introduces an extra step and creates an extra list. For such a small list, it might 
not matter, but if nums was huge, you would end up creating a large temporary data structure to only 
be used once and discarded. The generator solution transforms the data iteratively and is therefore 
much more memory-efficient.

Certain reduction functions such as min() and max() accept a key argument that might be useful in 
situations where you might be inclined to use a generator. For example, in the portfolio example, 
you might consider this alternative:
"""
# Original: Returns 20
min_shares = min(s['shares'] for s in portfolio)

# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares2 = min(portfolio, key=lambda s: s['shares'])
