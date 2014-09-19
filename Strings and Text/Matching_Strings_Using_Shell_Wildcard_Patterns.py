# coding=utf-8


"""
Problem

You want to match text using the same wildcard patterns as are commonly used when working in Unix shells 
(e.g., *.py, Dat[0-9]*.csv, etc.).

Solution

The fnmatch module provides two functions—fnmatch() and fnmatchcase()—that can be used to perform such 
matching. The usage is simple:
"""
from fnmatch import fnmatch, fnmatchcase
fnmatch('solo.txt', '*.txt')
# Returns True
fnmatch('solo.txt', '?olo.txt')
# Returns True
fnmatch('Data1.csv', 'Data[0-9]*')
# Returns True
names = ['Data2.csv', 'Data3.csv', 'start.py', 'config.ini']
[name for name in names if fnmatch(name, 'Data*.csv')]
# Returns ['Data2.csv', 'Data3.csv']

"""
Normally, fnmatch() matches patterns using the same case-sensitivity rules as the system’s underlying 
filesystem (which varies based on operating system). For example:
"""
# On OS X (Mac)
fnmatch('solo.txt', '*.TXT')
# Returns False
# On Linux
fnmatch('solo.txt', '*.TXT')
# Returns True

""""
If this distinction matters, use fnmatchcase() instead. It matches exactly based on the lower- and 
uppercase conventions that you supply:
"""
fnmatchcase('solo.txt', '*.TXT')
# Returns False

"""
An often overlooked feature of these functions is their potential use with data processing of nonfilename 
strings. For example, suppose you have a list of street addresses like this:
"""
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

"""
You could write list comprehensions like this:
"""
[addr for addr in addresses if fnmatch(addr, '* ST')]
# Returns ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
[addr for addr in addresses if fnmatch(addr, '54[0-9][0-9] *CLARK*')]
# Returns ['5412 N CLARK ST']

"""
Discussion

The matching performed by fnmatch sits somewhere between the functionality of simple string methods and 
the full power of regular expressions. If you’re just trying to provide a simple mechanism for allowing 
wildcards in data processing operations, it’s often a reasonable solution.

If you’re actually trying to write code that matches filenames, use the glob module instead. See 
"Getting a Directory Listing".
"""
