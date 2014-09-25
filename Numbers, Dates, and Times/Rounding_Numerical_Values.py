# coding=utf-8

"""
Problem

You want to round a floating-point number to a fixed number of decimal places.

Solution

For simple rounding, use the built-in round(value, ndigits) function. For example:
"""
round(1.23, 1)
# Returns 1.2
round(1.27, 1)
# Returns 1.3
round(-1.27, 1)
# Returns -1.3
round(1.25361, 3)
# Returns 1.254

"""
When a value is exactly halfway between two choices, the behavior of round is to round to the nearest 
even digit. That is, values such as 1.5 or 2.5 both get rounded to 2.

The number of digits given to round() can be negative, in which case rounding takes place for tens, 
hundreds, thousands, and so on. For example:
"""
a = 1627731
round(a, -1)
# Returns 1627730
round(a, -2)
# Returns 1627700
round(a, -3)
# Returns 1628000

"""
Discussion

Don’t confuse rounding with formatting a value for output. If your goal is simply to output a numerical 
value with a certain number of decimal places, you don’t typically need to use round(). Instead, just 
specify the desired precision when formatting. For example:
"""
x = 1.23456
format(x, '0.2f')
# Returns '1.23'
format(x, '0.3f')
# Returns '1.235'
print('value is {:0.3f}'.format(x))
# 'value is 1.235'

"""
Also, resist the urge to round floating-point numbers to "fix" perceived accuracy problems. For example, 
you might be inclined to do this:
"""
b = 2.1
c = 4.2
d = b + c
print(d)
# 6.300000000000001
d = round(d, 2)       # "Fix result (???)"
print(d)
# 6.3

"""
For most applications involving floating point, it’s simply not necessary (or recommended) to do this. 
Although there are small errors introduced into calculations, the behavior of those errors are understood 
and tolerated. If avoiding such errors is important (e.g., in financial applications, perhaps), consider 
the use of the decimal module, which is discussed in the next recipe.
"""
