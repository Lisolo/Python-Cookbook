# coding=utf-8


"""
Problem

You want to search for and replace a text pattern in a string.

Solution

For simple literal patterns, use the str.replace() method. For example:
"""
text = 'yeah, but no, but yeah, but no, but yeah'
text.replace('yeah', 'yep')
# Returns 'yep, but no, but yep, but no, but yep'

"""
For more complicated patterns, use the sub() functions/methods in the re module. To illustrate, suppose 
you want to rewrite dates of the form "11/27/2012" as "2012-11-27." Here is a sample of how to do it:
"""
text2 = 'Today is 08/05/2014. PyCon starts 03/13/2013.'
import re
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text2)
# Returns 'Today is 2014-08-05. PyCon starts 2013-03-13.'

"""
The first argument to sub() is the pattern to match and the second argument is the replacement pattern. 
Backslashed digits such as \3 refer to capture group numbers in the pattern.

If you’re going to perform repeated substitutions of the same pattern, consider compiling it first for 
better performance. For example:
"""
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2', text2)
# Returns 'Today is 2014-08-05. PyCon starts 2013-03-13.'

"""
For more complicated substitutions, it’s possible to specify a substitution callback function instead. 
For example:
"""
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
datepat.sub(change_date, text2)
# Returns 'Today is 05 Aug 2014. PyCon starts 13 Mar 2013.'

"""
As input, the argument to the substitution callback is a match object, as returned by match() or find(). 
Use the .group() method to extract specific parts of the match. The function should return the 
replacement text.

If you want to know how many substitutions were made in addition to getting the replacement text, 
use re.subn() instead. For example:
"""
newtext, n = datepat.subn(r'\3-\1-\2', text2)
print(newtext)
# 'Today is 2014-08-05. PyCon starts 2013-3-13.'
print(n)
# 2

"""
Discussion

There isn’t much more to regular expression search and replace than the sub() method shown. The trickiest 
part is specifying the regular expression pattern—something that’s best left as an exercise to the reader. 
"""
