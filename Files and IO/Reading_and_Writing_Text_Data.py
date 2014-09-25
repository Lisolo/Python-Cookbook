# coding=utf-8

"""
Problem

You need to read or write text data, possibly in different text encodings such as ASCII, UTF-8, or UTF-16.

Solution

Use the open() function with mode rt to read a text file. For example:
"""
# Read the entire file as a single string
with open('somefile.txt', 'rt') as f:
    data = f.read()

# Iterate over the lines of the file
with open('somefile.txt', 'rt') as f2:
    for line in f2:
        # process line
        pass

"""
Similarly, to write a text file, use open() with mode wt to write a file, 
clearing and overwriting the previous contents (if any). For example:
"""
# Write chunks of text data
with open('somefile.txt', 'wt') as f3:
    f3.write(text1)
    f3.write(text2)

# Redirected print statement
with open('somefile.txt', 'wt') as f4:
    print(line1, file=f4)
    print(line2, file=f4)

"""
To append to the end of an existing file, use open() with mode at.

By default, files are read/written using the system default text encoding, as can be found in 
sys.getdefaultencoding(). On most machines, this is set to utf-8. If you know that the text you 
are reading or writing is in a different encoding, supply the optional encoding parameter to open(). For example:
"""
with open('somefile.txt', 'rt', encoding='latin-1') as f5:
    pass

"""
Python understands several hundred possible text encodings. However, some of the more common encodings are 
ascii, latin-1, utf-8, and utf-16. UTF-8 is usually a safe bet if working with web applications. 
ascii corresponds to the 7-bit characters in the range U+0000 to U+007F. 
latin-1 is a direct mapping of bytes 0-255 to Unicode characters U+0000 to U+00FF. 
latin-1 encoding is notable in that it will never produce a decoding error when reading text of 
a possibly unknown encoding. Reading a file as latin-1 might not produce a completely correct text decoding, 
but it still might be enough to extract useful data out of it. Also, if you later write the data back out, 
the original input data will be preserved.
"""

"""
Discussion

Reading and writing text files is typically very straightforward. 
However, there are a number of subtle aspects to keep in mind. 
First, the use of the with statement in the examples establishes a context in which the file will be used.
When control leaves the with block, the file will be closed automatically. 
You don’t need to use the with statement, but if you don’t use it, make sure you remember to close the file:
"""
f6 = open('somefile.txt', 'rt')
data2 = f6.read()
f6.close()

"""
Another minor complication concerns the recognition of newlines, which are different on Unix and Windows 
(i.e., \n versus \r\n). By default, Python operates in what’s known as "universal newline" mode. 
In this mode, all common newline conventions are recognized, and newline characters are converted to 
a single \n character while reading. Similarly, the newline character \n is converted to 
the system default newline character on output. If you don’t want this translation, 
supply the newline='' argument to open(), like this:
"""
# Read with disabled newline translation
with open('somefile.txt', 'rt', newline='') as f7:
    pass

"""
To illustrate the difference, here’s what you will see on a Unix machine if you read the contents of 
a Windows-encoded text file containing the raw data hello world!\r\n:
"""
# Newline translation enable (the default)
f8 = open('hello.txt', 'rt')
f8.read()
# Returns 'hello world!\n'

# Newline translation disabled
g = open('hello.txt', 'rt', newline='')
g.read()
# Returns 'hello world!\r\n'

"""
A final issue concerns possible encoding errors in text files. When reading or writing a text file, 
you might encounter an encoding or decoding error. For instance:
"""
f9 = open('sample.txt', 'rt', encoding='ascii')
f9.read()
# Traceback (most recent call last):
#   File "<stdin>", line 101, in <module>
#   File "/usr/local/lib/python3.3/encodings/ascii.py", line 26, in decode
#     return codecs.ascii_decode(input, self.errors)[0]
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position
# 12: ordinal not in range(128)

"""
If you get this error, it usually means that you’re not reading the file in the correct encoding. 
You should carefully read the specification of whatever it is that you’re reading and check that 
you’re doing it right (e.g., reading data as UTF-8 instead of Latin-1 or whatever it needs to be). 
If encoding errors are still a possibility, you can supply an optional errors argument to open() 
to deal with the errors. Here are a few samples of common error handling schemes:
"""
# Replace bad chars with Unicode U+fffd replacement char
f10 = open('sample.txt', 'rt', encoding='ascii', errors='replace')
f10.read()
# Returns 'Solo Li!'

# Ignore bad chars entirely
g2 = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
g2.read()
# Returns 'Solo Li!'

"""
If you’re constantly fiddling with the encoding and errors arguments to open() and doing lots of hacks, 
you’re probably making life more difficult than it needs to be. The number one rule with text is that 
you simply need to make sure you’re always using the proper text encoding. When in doubt, 
use the default setting (typically UTF-8).
"""
