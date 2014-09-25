# coding=utf-8

"""
Problem

You have a byte string and you need to unpack it into an integer value. Alternatively, you need to convert 
a large integer back into a byte string.

Solution

Suppose your program needs to work with a 16-element byte string that holds a 128-bit integer value. 
For example:
"""
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

"""
To interpret the bytes as an integer, use int.from_bytes(), and specify the byte ordering like this:
"""
len(data)
# Returns 16
int.from_bytes(data, 'little')
# Returns 69120565665751139577663547927094891008
int.form_bytes(data, 'big')
# Returns 94522842520747284487117727783387188

"""
To convert a large integer value back into a byte string, use the int.to_bytes() method, specifying the 
number of bytes and the byte order. For example:
"""
x = 94522842520747284487117727783387188
x.to_bytes(16, 'big')
# Returns b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
x.to_bytes(16, 'little')
# Returns b'4\x00#\x00\x01\xef\xcd\x00\xab\x90x\x00V4\x12\x00'

"""
Discussion

Converting large integer values to and from byte strings is not a common operation. However, it sometimes 
arises in certain application domains, such as cryptography or networking. For instance, IPv6 network 
addresses are represented as 128-bit integers. If you are writing code that needs to pull such values 
out of a data record, you might face this problem.

As an alternative to this recipe, you might be inclined to unpack values using the struct module, as 
described in "Reading and Writing Binary Arrays of Structures". This works, but the size of integers 
that can be unpacked with struct is limited. Thus, you would need to unpack multiple values and 
combine them to create the final value. For example:
"""
import struct
hi, lo = struct.unpack('>QQ', data)
print((hi << 64) + lo)
# 94522842520747284487117727783387188

"""
The specification of the byte order (little or big) just indicates whether the bytes that make up the 
integer value are listed from the least to most significant or the other way around. This is easy to 
view using a carefully crafted hexadecimal value:
"""
x2 = 0x01020304
x2.to_bytes(4, 'big')
# Returns b'\x01\x02\x03\x04'
x.to_bytes(4, 'little')
# Returns b'\x04\x03\x02\x01'

"""
If you try to pack an integer into a byte string, but it won’t fit, you’ll get an error. You can use the 
int.bit_length() method to determine how many bits are required to store a value if needed:
"""
x3 = 523 ** 23
print(x3)
# 335381300113661875107536852714019056160355655333978849017944067
x3.to_bytes(16, 'little')
# Traceback (most recent call last):
#   File "<stdin>", line 73, in <module>
# OverflowError: int too big to convert
x3.bit_length()
# 208
nbytes, rem = divmod(x3.bit_length(), 8)
if rem:
    nbytes += 1
x3.to_bytes(nbytes, 'little')
# Returns b'\x03X\xf1\x82iT\x96\xac\xc7c\x16\xf3\xb9\xcf...\xd0'
