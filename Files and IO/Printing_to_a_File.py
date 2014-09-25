# coding=utf-8

"""
Problem

You want to redirect the output of the print() function to a file.

Solution

Use the file keyword argument to print(), like this:
"""
with open('somefile.txt', 'rt') as f:
    print('Hello World!', file=f)

"""
Discussion

There’s not much more to printing to a file other than this. However, make sure that the file is opened in text mode. 
Printing will fail if the underlying file is in binary mode.
"""
