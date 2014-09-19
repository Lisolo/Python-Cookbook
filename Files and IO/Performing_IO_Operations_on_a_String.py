# coding=utf-8


"""
Problem

You want to feed a text or binary string to code that’s been written to operate on file-like objects instead.

Solution

Use the io.StringIO() and io.BytesIO() classes to create file-like objects that operate on string data. 
For example:
"""
import io
s = io.StringIO()
s.write('Hello World\n')
# Returns 12
print('This is a test', file=s)
# 15

# Get all of the data written so far
s.getvalue()
# 'Hello World\nThis is a test\n'

# Wrap a file interface around an existing string
s = io.StringIO('Hello\nWorld\n')
s.read(4)
# Returns 'Hell'
s.read()
# Returns 'o\nWorld\n'

"""
The io.StringIO class should only be used for text. If you are operating with binary data, 
use the io.BytesIO class instead. For example:
"""
s2 = io.BytesIO()
s2.write(b'binary data')
# Returns 11
s2.getvalue()
# b'binary data'

"""
Discussion

The StringIO and BytesIO classes are most useful in scenarios where you need to mimic a normal file for some reason.
For example, in unit tests, you might use StringIO to create a file-like object containing test data 
that’s fed into a function that would otherwise work with a normal file.

Be aware that StringIO and BytesIO instances don’t have a proper integer file-descriptor. Thus, 
they do not work with code that requires the use of a real system-level file such as a file, pipe, or socket.
"""
