# coding=utf-8

"""
Problem

You need to convert or output integers represented by binary, octal, or hexadecimal digits.

Solution

To convert an integer into a binary, octal, or hexadecimal text string, use the bin(), oct(), or hex() 
functions, respectively:
"""
x = 1234
bin(x)
# Returns '0b10011010010'
oct(x)
# Returns '0o2322'
hex(x)
# Returns '0x4d2'

"""
Alternatively, you can use the format() function if you don’t want the 0b, 0o, or 0x prefixes to appear. 
For example:
"""
format(x, 'b')
# Returns '10011010010'
format(x, 'o')
# Returns '2322'
format(x, 'x')
# Returns '4d2'

"""
Integers are signed, so if you are working with negative numbers, the output will also include a sign. 
For example:
"""
x2 = -1234
format(x2, 'b')
# Returns '-10011010010'
format(x2, 'x')
# Returns '-4d2'

"""
If you need to produce an unsigned value instead, you’ll need to add in the maximum value to set the bit 
length. For example, to show a 32-bit value, use the following:
"""
format(2**32 + x, 'b')
# Returns '11111111111111111111101100101110'
format(2**32 + x, 'x')
# Returns 'fffffb2e'

"""
To convert integer strings in different bases, simply use the int() function with an appropriate base. 
For example:
"""
int('4d2', 16)
# Returns 1234
int('10011010010', 2)
# Returns 1234

"""
Discussion

For the most part, working with binary, octal, and hexadecimal integers is straightforward. Just remember 
that these conversions only pertain to the conversion of integers to and from a textual representation. 
Under the covers, there’s just one integer type.

Finally, there is one caution for programmers who use octal. The Python syntax for specifying octal values 
is slightly different than many other languages. For example, if you try something like this, you’ll get 
a syntax error:
"""
import os
os.chmod('script.py', 0755)
#   File "<stdin>", line 1
#     os.chmod('script.py', 0755)
                           ^
# SyntaxError: invalid token

"""
Make sure you prefix the octal value with 0o, as shown here:
"""
os.chomd('script.py', 0o0755)
