# coding=utf-8


"""
Problem

You want to eliminate the duplicate values in a sequence, but preserve the order of the remaining items.

Solution

If the values in the sequence are hashable, the problem can be easily solved using a set and a generator. 
For example:
"""
def dequpe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

"""
Here is an example of how to use your function:
"""
a = [1, 5, 2, 1, 9, 1, 5, 10]
list(dequpe(a))

"""
This only works if the items in the sequence are hashable. If you are trying to eliminate duplicates in a 
sequence of unhashable types (such as dicts), you can make a slight change to this recipe, as follows:
"""
def dequpe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

"""
Here, the purpose of the key argument is to specify a function that converts sequence items into a 
hashable type for the purposes of duplicate detection. Here’s how it works:
"""
a2 = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
list(dequpe2(a2, key=lambda d: (d['x'],d['y'])))
# Returns [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
list(dequpe2(a2, key=lambda d: (d['x'])))
# Returns [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

"""
This latter solution also works nicely if you want to eliminate duplicates based on the value of a 
single field or attribute or a larger data structure.
"""

"""
Discussion

If all you want to do is eliminate duplicates, it is often easy enough to make a set. For example:
"""
set(a)
# Returns {1, 2, 10, 5, 9}

"""
However, this approach doesn’t preserve any kind of ordering. So, the resulting data will be scrambled 
afterward. The solution shown avoids this.

The use of a generator function in this recipe reflects the fact that you might want the function to be 
extremely general purpose—not necessarily tied directly to list processing. For example, if you want to 
read a file, eliminating duplicate lines, you could simply do this:
"""
with open('somefile.txt', 'r') as f:
    for line in dequpe(f):
        print(line)
