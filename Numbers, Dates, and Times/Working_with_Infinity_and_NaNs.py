# coding=utf-8

"""
Problem

You need to create or test for the floating-point values of infinity, negative infinity, or NaN 
(not a number).

Solution

Python has no special syntax to represent these special floating-point values, but they can be created 
using float(). For example:
"""
a = float('inf')
b = float('-inf')
c = float('nan')
print(a)
# inf
print(b)
# -inf
print(c)
# nan

"""
To test for the presence of these values, use the math.isinf() and math.isnan() functions. For example:
"""
math.isinf(a)
# Returns True
math.isnan(c)
# Returns True

"""
Discussion

For more detailed information about these special floating-point values, you should refer to the IEEE 754 
specification. However, there are a few tricky details to be aware of, especially related to comparisons 
and operators.

Infinite values will propagate in calculations in a mathematical manner. For example:
"""
print(a + 45)
# inf
print(a * 10)
# inf
print(10 / a)
# 0.0

"""
However, certain operations are undefined and will result in a NaN result. For example:
"""
print(a / a)
# nan
print(a + b)
# nan

"""
NaN values propagate through all operations without raising an exception. For example:
"""
print(c + 23)
# nan
print(c / 2)
# nan
print(c * 2)
# nan
math.sqrt(c)
# Returns nan

"""
A subtle feature of NaN values is that they never compare as equal. For example:
"""
d = float('nan')
print(c == d)
# False
print(c is d)
# False

"""
Because of this, the only safe way to test for a NaN value is to use math.isnan(), as shown in this recipe.

Sometimes programmers want to change Python’s behavior to raise exceptions when operations result in an 
infinite or NaN result. The fpectl module can be used to adjust this behavior, but it is not enabled in 
a standard Python build, it’s platform-dependent, and really only intended for expert-level programmers. 
See the online Python documentation for further details.
"""
