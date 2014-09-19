# coding=utf-8

"""
Problem

You need to check the start or end of a string for specific text patterns, such as filename extensions, 
URL schemes, and so on.

Solution

A simple way to check the beginning or end of a string is to use the str.startswith() or str.endswith() 
methods. For example:
"""
filename = 'game.py'
filename.endswith('.py')
# Returns True
filename.startswith('file:')
# Returns False
url = 'http://www.python.org'
url.startswith('http')
# Returns True

"""
If you need to check against multiple choices, simply provide a tuple of possibilities to startswith() or 
endswith():
"""
import os
filenames = os.listdir('.')
print(filenames)
# ['startgame.py', 'time.py', 'fire.c', 'fire.h']
[name for name in filenames if name.endswith(('.c', '.h'))]
# Returns ['fire.c', 'fire.h']
any(name.endswith('.py') for name in filenames)
# True

"""
Here is another example:
"""
from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

"""
Oddly, this is one part of Python where a tuple is actually required as input. If you happen to have the 
choices specified in a list or set, just make sure you convert them using tuple() first. For example:
"""
choices = ['http:', 'ftp:']
url.startswith(choices)
# Traceback (most recent call last):
#   File "<stdin>", line 53, in <module>
# TypeError: startswith first arg must be str or a tuple of str, not list
url.startswith(tuple(choices))
# Returns True

"""
Discussion

The startswith() and endswith() methods provide a very convenient way to perform basic prefix and suffix 
checking. Similar operations can be performed with slices, but are far less elegant. For example:
"""
filename2 = 'solo.txt'
filename2[-4:] == '.txt'
# Returns True
url[:5] == 'http:' or url[:6] == 'https:' or url[:4 == 'ftp:']
# True

"""
You might also be inclined to use regular expressions as an alternative. For example:
"""
re.match('http:|https:|ftp:', url)
# Returns <_sre.SRE_Match object; span=(0, 5), match='http:'>

"""
This works, but is often overkill for simple matching. Using this recipe is simpler and runs faster.

Last, but not least, the startswith() and endswith() methods look nice when combined with other 
operations, such as common data reductions. For example, this statement that checks a directory 
for the presence of certain kinds of files:
"""
if any(name.endswith(('.c', '.h')) for name in listdir('.')):
    pass
