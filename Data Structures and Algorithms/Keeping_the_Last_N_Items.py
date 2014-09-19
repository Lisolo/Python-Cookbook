# coding=utf-8


"""
Problem

You want to keep a limited history of the last few items seen during iteration or 
during some other kind of processing.

Solution

Keeping a limited history is a perfect use for a collections.deque. 
For example, the following code performs a simple text match on a sequence of lines 
and yields the matching line along with the previous N lines of context when found:
"""
def search(lines, pattern, history=5):
    from collections import deque
    previous_lines = deque(maxlen=history)
    for line in lines:
	if pattern in line:
	    yield line, previous_lines
	previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
	for line, prevlines in search(f, 'python', 5):
		for pline in prevlines:
		    print(pline, end='')
		print(line, end='')
		print('-'*20)

"""
Discussion

When writing code to search for items, it is common to use a generator function involving yield, 
as shown in this recipe’s solution. 
This decouples the process of searching from the code that uses the results. 
If you’re new to generators, see "Creating New Iteration Patterns with Generators".

Using deque(maxlen=N) creates a fixed-sized queue. 
When new items are added and the queue is full, the oldest item is automatically removed. 
For example:
"""
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
# deque([1, 2, 3], maxlen=3)
q.append(4)
print(q)
# deque([2, 3, 4], maxlen=3)
q.append(5)
print(q)
# deque([3, 4, 5], maxlen=3)

"""
Although you could manually perform such operations on a list (e.g., appending, deleting, etc.), 
the queue solution is far more elegant and runs a lot faster.

More generally, a deque can be used whenever you need a simple queue structure. 
If you don’t give it a maximum size, you get an unbounded queue that lets you append and pop items 
on either end. 
For example:
"""
q2 = deque()
q2.append(1)
q2.append(2)
q2.append(3)
print(q2)
# deque([1, 2, 3])
q2.appendleft(4)
print(q2)
# deque([4, 1, 2, 3])
print(q2.pop())
# 3
print(q2)
# deque([4, 1, 2])
print(q2.popleft())
# 4
"""
Adding or popping items from either end of a queue has O(1) complexity. 
This is unlike a list where inserting or removing items from the front of the list is O(N).
"""
