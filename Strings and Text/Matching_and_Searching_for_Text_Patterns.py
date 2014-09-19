# coding=utf-8


"""
Problem

You want to match or search text for a specific pattern.

Solution

If the text you’re trying to match is a simple literal, you can often just use the basic string methods, 
such as str.find(), str.endswith(), str.startswith(), or similar. For example:
"""
text = 'yeah, but no, but yeah, but no, but yeah'

# Exact match
text == 'yeah'
# Returns False

# Match at start or end
text.startswith('yeah')
# Returns True
text.endswith('no')
# Returns False

# Search for the location of the first occurrence
text.find('no')
# Returns 10

"""
For more complicated matching, use regular expressions and the re module. To illustrate the basic 
mechanics of using regular expressions, suppose you want to match dates specified as digits, 
such as "11/27/2012." Here is a sample of how you would do it:
"""
text2 = '08/05/2014'
text3 = 'Aug 05, 2014'

import re
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
# yes
if re.match(r'\d+/\d+/\d+', text3):
    print('yes')
else:
    print('no')
# no

"""
If you’re going to perform a lot of matches using the same pattern, it usually pays to precompile the 
regular expression pattern into a pattern object first. For example:
"""
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text2):
    print('yes')
else:
    print('no')
# yes
if datepat.match(text3):
    print('yes')
else:
    print('no')
# no

"""
match() always tries to find the match at the start of a string. If you want to search text for all 
occurrences of a pattern, use the findall() method instead. For example:
"""
text4 = 'Today is 08/05/2014. PyCon starts 03/13/2013.'
datepat.findall(text4)
# Returns ['08/05/2014', '03/13/2013']

"""
When defining regular expressions, it is common to introduce capture groups by enclosing parts of the 
pattern in parentheses. For example:
"""
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

"""
Capture groups often simplify subsequent processing of the matched text because the contents of each 
group can be extracted individually. For example:
"""
m = datepat.match('08/05/2014')
print(m)
# <_sre.SRE_Match object; span=(0, 10), match='08/05/2014'>

# Extract the contents of each group
m.group(0)
# Rturns '08/05/2014'
m.group(1)
# Returns '08'
m.group(2)
# Returns '05'
m.group(3)
# Returns '2014'
m.groups()
# Returns ('08', '05', '2014')
month, day, year = m.groups()

# Find all matches (notice splitting into tuples)
datepat.findall(text4)
# Returns [('08', '05', '2014'), ('03', '13', '2013')]
for month, day, year in datepat.findall(text4):
    print('{}-{}-{}'.format(year, month, day))
# 2014-08-05
# 2013-03-13

"""
The findall() method searches the text and finds all matches, returning them as a list. If you want to 
find matches iteratively, use the finditer() method instead. For example:
"""
for m in datepat.finditer(text4):
    print(m.groups())
# ('08', '05', '2014')
# ('03', '13', '2013')

"""
Discussion

A basic tutorial on the theory of regular expressions is beyond the scope of this book. However, this 
recipe illustrates the absolute basics of using the re module to match and search for text. The 
essential functionality is first compiling a pattern using re.compile() and then using methods 
such as match(), findall(), or finditer().

When specifying patterns, it is relatively common to use raw strings such as r'(\d+)/(\d+)/(\d+)'. 
Such strings leave the backslash character uninterpreted, which can be useful in the context of 
regular expressions. Otherwise, you need to use double backslashes such as '(\\d+)/(\\d+)/(\\d+)'.

Be aware that the match() method only checks the beginning of a string. It’s possible that it will 
match things you aren’t expecting. For example:
"""
m2 = datepat.match('08/05/2014solo')
print(m2)
# <_sre.SRE_Match object; span=(0, 10), match='08/05/2014'>
m2.group()
# Returns '08/05/2014'

"""
If you want an exact match, make sure the pattern includes the end-marker ($), as in the following:
"""
datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)$')
datepat2.match('08/05/2014solo')
datepat2.match('08/05/2014')
# <_sre.SRE_Match object; span=(0, 10), match='08/05/2014'>

"""
Last, if you’re just doing a simple text matching/searching operation, you can often skip the 
compilation step and use module-level functions in the re module instead. For example:
"""
re.findall(r'(\d+)/(\d+)/(\d+)', text4)
# [('08', '05', '2014'), ('03', '13', '2013')]

"""
Be aware, though, that if you’re going to perform a lot of matching or searching, it usually pays to 
compile the pattern first and use it over and over again. The module-level functions keep a cache of 
recently compiled patterns, so there isn’t a huge performance hit, but you’ll save a few lookups and 
extra processing by using your own compiled pattern.
"""
