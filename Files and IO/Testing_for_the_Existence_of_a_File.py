# coding=utf-8

"""
Problem

You need to test whether or not a file or directory exists.

Solution

Use the os.path module to test for the existence of a file or directory. For example:
"""
import os
os.path.exists('/etc/passwd')
# Returns True
os.path.exists('/tmp/spam')
# Returns False

"""
You can perform further tests to see what kind of file it might be. 
These tests return False if the file in question doesn’t exist:
"""
# Is a regular file
os.path.isfile('/etc/passwd')
# Returns True

# Is a directory
os.path.isdir('/etc/passwd')
# Returns False

# Is a symbolic link
os.path.islink('/usr/local/bin/python3')
# Returns False

# Get the file linked to
os.path.realpath('/usr/local/bin/python3')
# Returns '/usr/local/bin/python3'

"""
If you need to get metadata (e.g., the file size or modification date), that is also available in the os.path module.
"""
os.path.getsize('/etc/passwd')
# Returns 1995
os.path.getmtime('/etc/passwd')
# Returns 1405332301.8715763
import time
time.ctime(os.path.getmtime('/etc/passwd'))
# Returns 'Mon Jul 14 18:05:01 2014'

"""
Discussion

File testing is a straightforward operation using os.path. Probably the only thing to be aware of 
when writing scripts is that you might need to worry about permissions—especially for operations 
that get metadata. For example:
"""
os.path.getsize('/Users/solo/Destop/foo.txt')
# Traceback (most recent call last):
#   File "<stdin>", line 57, in <module>
#   File "/usr/local/lib/python3.3/genericpath.py", line 49, in getsize
#     return os.stat(filename).st_size
# PermissionError: [Errno 13] Permission denied: '/Users/guido/Desktop/foo.txt'
