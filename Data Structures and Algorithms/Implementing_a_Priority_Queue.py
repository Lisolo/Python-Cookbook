# coding=utf-8


"""
Problem

You want to implement a queue that sorts items by a given priority and always returns 
the item with the highest priority on each pop operation.

Solution

The following class uses the heapq module to implement a simple priority queue:
"""
import heapq

class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

"""
Here is an example of how it might be used:
"""
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('cat'), 1)
q.push(Item('dragon'), 5)
q.push(Item('tiger'), 4)
q.push(Item('dog'), 1)
print(q.pop())
# Item('dragon')
print(q.pop())
# Item('tiger')
print(q.pop())
# Item('cat')
print(q.pop())
# Item('dog')
"""
Observe how the first pop() operation returned the item with the highest priority. 
Also observe how the two items with the same priority (foo and grok) were returned 
in the same order in which they were inserted into the queue.
"""

"""
Discussion

The core of this recipe concerns the use of the heapq module. 
The functions heapq.heappush() and heapq.heappop() insert and remove items from a 
list _queue in a way such that the first item in the list has the smallest priority 
(as discussed in “Finding the Largest or Smallest N Items”). 
The heappop() method always returns the "smallest" item, 
so that is the key to making the queue pop the correct items. 
Moreover, since the push and pop operations have O(log N) complexity where N is the 
number of items in the heap, 
they are fairly efficient even for fairly large values of N.

In this recipe, the queue consists of tuples of the form (-priority, index, item). 
The priority value is negated to get the queue to sort items from highest priority to lowest priority. 
This is opposite of the normal heap ordering, which sorts from lowest to highest value.

The role of the index variable is to properly order items with the same priority level. 
By keeping a constantly increasing index, the items will be sorted according to the order 
in which they were inserted. 
However, the index also serves an important role in making the comparison operations work 
for items that have the same priority level.

To elaborate on that, instances of Item in the example can't be ordered. For example:
"""
a = Item('rabbit')
b = Item('wolf')
print(a < b)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unorderable types: Item() < Item()

"""
If you make (priority, item) tuples, they can be compared as long as the priorities are different. 
However, if two tuples with equal priorities are compared, 
the comparison fails as before. For example:
"""
a2 = (5, Item('lion'))
b2 = (3, Item('snake'))
print(a2 < b2)
# False
c2 = (5, Item('bears'))
print(a2 < c2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unorderable types: Item() < Item()

"""
By introducing the extra index and making (priority, index, item) tuples, 
you avoid this problem entirely since no two tuples will ever have the same value for index 
(and Python never bothers to compare the remaining tuple values once the result of comparison 
can be determined):
"""
a3 = (1, 0, Item('hawk'))
b3 = (5, 1, Item('orangutan'))
c3 = (1, 2, Item('monkey'))
print(a3 < b3)
# True
print(a3 < c3)
# True
"""
If you want to use this queue for communication between threads, 
you need to add appropriate locking and signaling. 
See "Communicating Between Threads" for an example of how to do this.

The documentation for the heapq module has further examples and discussion 
concerning the theory and implementation of heaps.
"""
