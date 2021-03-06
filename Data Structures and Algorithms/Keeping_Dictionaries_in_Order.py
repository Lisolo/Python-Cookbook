# coding=utf-8

"""
Problem

You want to create a dictionary, and you also want to control the order of items 
when iterating or serializing.

Solution

To control the order of items in a dictionary, you can use an OrderedDict from 
the collections module. It exactly preserves the original insertion order of data 
when iterating. For example:
"""

from collections import OrderedDict

d = OrderedDict()
d['bird'] = 1
d['rabbit'] = 2
d['tiger'] = 4
d['monkey'] = 3

# Outputs "bird 1", "rabbit 2", "tiger 4", "monkey 3"
for key in d:
    print(key, d[key])

"""
An OrderedDict can be particularly useful when you want to build a mapping that you may 
want to later serialize or encode into a different format. For example, if you want to 
precisely control the order of fields appearing in a JSON encoding, first building the 
data in an OrderedDict will do the trick:
"""
import json
print(json.dumps(d))
# {"bird": 1, "rabbit": 2, "tiger": 4, "monkey": 3}

"""
Discussion

An OrderedDict internally maintains a doubly linked list that orders the keys according to 
insertion order. When a new item is first inserted, it is placed at the end of this list. 
Subsequent reassignment of an existing key doesn’t change the order.

Be aware that the size of an OrderedDict is more than twice as large as a normal dictionary 
due to the extra linked list that’s created. Thus, if you are going to build a data structure 
involving a large number of OrderedDict instances (e.g., reading 100,000 lines of a CSV file 
into a list of OrderedDict instances), you would need to study the requirements of your application 
to determine if the benefits of using an OrderedDict outweighed the extra memory overhead.
"""
