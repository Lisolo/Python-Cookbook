# coding=utf-8


"""
Problem

You want to iterate over items in an iterable, but the first few items aren’t of interest and you just 
want to discard them.

Solution

The itertools module has a few functions that can be used to address this task. The first is the itertools.
dropwhile() function. To use it, you supply a function and an iterable. The returned iterator discards 
the first items in the sequence as long as the supplied function returns True. Afterward, the entirety 
of the sequence is produced.

To illustrate, suppose you are reading a file that starts with a series of comment lines. For example:
"""
with open('somefile.txt') as f:
    for line in f:
        print(line, end='')
"""
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode.  At other times, this information is provided by
# Open Directory.
...
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
"""

"""
If you want to skip all of the initial comment lines, here’s one way to do it:
"""
from itertools import dropwhile
with open('somefile.txt') as f2:
    for line in dropwhile(lambda line: line.startswith('#'), f2):
        print(line, end='')
# nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
# root:*:0:0:System Administrator:/var/root:/bin/sh

"""
This example is based on skipping the first items according to a test function. If you happen to know the 
exact number of items you want to skip, then you can use itertools.islice() instead. For example:
"""
from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)
# 1
# 4
# 10
# 15

"""
In this example, the last None argument to islice() is required to indicate that you want everything 
beyond the first three items as opposed to only the first three items (e.g., a slice of [3:] as 
opposed to a slice of [:3]).
"""

"""
Discussion

The dropwhile() and islice() functions are mainly convenience functions that you can use to avoid writing 
rather messy code such as this:
"""
with open('somefile.txt') as f3:
    # Skip over initial comments
    while True:
        line2 = next(f, '')
        if not line2.startswith('#'):
            break

    # Process remaining lines
    while line2:
        # Replace with useful processing
        print(line2, end='')
        line2 = next(f3, None)

"""
Discarding the first part of an iterable is also slightly different than simply filtering all of it. 
For example, the first part of this recipe might be rewritten as follows:
"""
with open('somefile.txt') as f4:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')

"""
This will obviously discard the comment lines at the start, but will also discard all such lines 
throughout the entire file. On the other hand, the solution only discards items until an item no 
longer satisfies the supplied test. After that, all subsequent items are returned with no filtering.

Last, but not least, it should be emphasized that this recipe works with all iterables, including those 
whose size can’t be determined in advance. This includes generators, files, and similar kinds of objects.
"""
