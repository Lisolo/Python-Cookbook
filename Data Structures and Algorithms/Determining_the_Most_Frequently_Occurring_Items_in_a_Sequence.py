# coding=utf-8

"""
Problem

You have a sequence of items, and you’d like to determine the most frequently occurring items in the 
sequence.

Solution

The collections.Counter class is designed for just such a problem. It even comes with a handy 
most_common() method that will give you the answer.

To illustrate, let’s say you have a list of words and you want to find out which words occur most often. 
Here’s how you would do it:
"""
from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]

"""
Discussion

As input, Counter objects can be fed any sequence of hashable input items. Under the covers, 
a Counter is a dictionary that maps the items to the number of occurrences. For example:
"""
word_counts['around']
# 2
word_counts['not']
# 1

"""
If you want to increment the count manually, simply use addition:
"""
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1
print(word_counts['not'])
# 2

"""
Or, alternatively, you could use the update() method:
"""
word_counts.update(morewords)

"""
A little-known feature of Counter instances is that they can be easily combined using various 
mathematical operations. For example:
"""
a = Counter(words)
b = Counter(morewords)
print(a)
# Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2,
#          "you're": 1, "don't": 1, 'under': 1, 'not': 1})
print(b)
# Counter({'eyes': 1, 'looking': 1, 'are': 1, 'in': 1, 'not': 1, 'you': 1,
#          'my': 1, 'why': 1})
# Combine counts
c = a+ b
print(c)
# Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'not': 2,
#          'around': 2, "you're": 1, "don't": 1, 'in': 1, 'why': 1,
#          'looking': 1, 'are': 1, 'under': 1, 'you': 1})
# Subtract counts
d = a - b
print(d)
# Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2,
#          "you're": 1, "don't": 1, 'under': 1})

"""
Needless to say, Counter objects are a tremendously useful tool for almost any kind of problem where 
you need to tabulate and count data. You should prefer this over manually written solutions involving 
dictionaries.
"""
