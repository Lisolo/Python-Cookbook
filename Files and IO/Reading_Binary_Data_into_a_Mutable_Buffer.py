# coding=utf-8


"""
Problem

You want to read binary data directly into a mutable buffer without any intermediate copying. 
Perhaps you want to mutate the data in-place and write it back out to a file.

Solution

To read data into a mutable array, use the readinto() method of files. For example:
"""
import os.path

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

"""
Here is an example that illustrates the usage:
"""
# write a sample file
with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('sample.bin')
print(buf)
# Hello World
buf[0:5] = b'Hallo'
print(buf)
# Hallo World

with open('newsample.bin', 'wb') as f2:
    f2.write(buf)

"""
Discussion

The readinto() method of files can be used to fill any preallocated array with data. 
This even includes arrays created from the array module or libraries such as numpy. 
Unlike the normal read() method, readinto() fills the contents of an existing buffer 
rather than allocating new objects and returning them. Thus, you might be able to 
use it to avoid making extra memory allocations. For example, if you are reading 
a binary file consisting of equally sized records, you can write code like this:
"""
record_size = 32            # Size of each record (adjust value)

buf2 = bytearray(record_size)
with open('somefile', 'rb') as f3:
    while True:
        n = f3.readinto(buf2)
        if n < record_size:
            break
        # Use the contents of buf2

"""
Another interesting feature to use here might be a memoryview, which lets you make zero-copy slices 
of an existing buffer and even change its contents. For example:
"""
m1 = memoryview(buf)
m2 = m1[-5:]
m2[:] = b'WORLD'
print(buf)
# Hello WORLD

"""
One caution with using f.readinto() is that you must always make sure to check its return code, 
which is the number of bytes actually read.

If the number of bytes is smaller than the size of the supplied buffer, 
it might indicate truncated or corrupted data (e.g., if you were expecting an exact number of bytes to be read).

Finally, be on the lookout for other "into" related functions in various library modules 
(e.g., recv_into(), pack_into(), etc.). Many other parts of Python have support for direct I/O 
or data access that can be used to fill or alter the contents of arrays and buffers.

See "Reading Nested and Variable-Sized Binary Structures" for a significantly more advanced example 
of interpreting binary structures and usage of memoryviews.
"""
