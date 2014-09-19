# coding=utf-8


"""
Problem

You want to make a dictionary that maps keys to more than one value (a so-called "multidict").

Solution

A dictionary is a mapping where each key is mapped to a single value. 
If you want to map keys to multiple values, you need to store the multiple values in another 
container such as a list or set. For example, you might make dictionaries like this:
"""

d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}

e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}

"""
The choice of whether or not to use lists or sets depends on intended use. 
Use a list if you want to preserve the insertion order of the items. 
Use a set if you want to eliminate duplicates (and don’t care about the order).

To easily construct such dictionaries, you can use defaultdict in the collections module. 
A feature of defaultdict is that it automatically initializes the first value so you can 
simply focus on adding items. For example:
"""
from collections import defaultdict

d2 = defaultdict(list)
d2['a'].append(1)
d2['a'].append(2)
d2['b'].append(4)
# defaultdict(<type 'list'>, {'a': [1, 2], 'b': [4]})

d3 = defaultdict(set)
d3['a'].add(1)
d3['a'].add(2)
d3['b'].add(4)
# defaultdict(<type 'set'>, {'a': set([1, 2]), 'b': set([4])})

"""
One caution with defaultdict is that it will automatically create dictionary entries for 
keys accessed later on (even if they aren’t currently found in the dictionary). 
If you don’t want this behavior, you might use setdefault() on an ordinary dictionary instead. 
For example:
"""
d4 = {}    # A regular dictionary
d4.setdefault('a', []).append(1)
d4.setdefault('a', []).append(2)
d4.setdefault('b', []).append(4)
print(d4)
# {'a': [1, 2], 'b': [4]}
"""
However, many programmers find setdefault() to be a little unnatural—not to mention the fact that 
it always creates a new instance of the initial value on each invocation (the empty list [] in the example).
"""

"""
Discussion

In principle, constructing a multivalued dictionary is simple. However, initialization of the first 
value can be messy if you try to do it yourself. For example, you might have code that looks like this:
""" 
d5 = {}
for key, value in pairs:
    if key not in d:
        d5[key] = []
    d5[key].append(value)

"""
Using a defaultdict simply leads to much cleaner code:
"""
d6 = defaultdict(list)
for key, value in pairs:
    d6[key].append(value)
"""
This recipe is strongly related to the problem of grouping records together in data processing problems. 
See "Grouping Records Together Based on a Field" for an example.
"""
