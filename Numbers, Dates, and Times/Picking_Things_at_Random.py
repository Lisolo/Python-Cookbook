# coding=utf-8


"""
Problem

You want to pick random items out of a sequence or generate random numbers.

Solution

The random module has various functions for random numbers and picking random items. For example, to pick 
a random item out of a sequence, use random.choice():
"""
import random
values = [1, 2 ,3 , 4, 5, 6]
print(random.choice(values))
# 6
print(random.choice(values))
# 5
print(random.choice(values))
# 3
print(random.choice(values))
# 4
print(random.choice(values))
# 2

"""
To take a sampling of N items where selected items are removed from further consideration, 
use random.sample() instead:
"""
print(random.sample(values, 2))
# [4, 2]
print(random.sample(values, 2))
# [2, 3]
print(random.sample(values, 3))
# [1, 2, 5]
print(random.sample(values, 3))
# [3, 6, 2]

"""
If you simply want to shuffle items in a sequence in place, use random.shuffle():
"""
random.shuffle(values)
print(values)
# [3, 1, 2, 4, 6, 5]
random.shuffle(values)
print(values)
# [5, 4, 3, 1, 6, 2]

"""
To produce random integers, use random.randint():
"""
print(random.randint(0,10))
# 0
print(random.randint(0,10))
# 3
print(random.randint(0,10))
# 9
print(random.randint(0,10))
# 6
print(random.randint(0,10))
# 10
print(random.randint(0,10))
# 1

"""
To produce uniform floating-point values in the range 0 to 1, use random.random():
"""
print(random.random())
# 0.0823746551903
print(random.random())
# 0.548121373928
print(random.random())
# 0.416048790693

"""
To get N random-bits expressed as an integer, use random.getrandbits():
"""
print(random.getrandbits(200))
# 335837000776573622800628485064121869519521710558559406913275

"""
Discussion

The random module computes random numbers using the Mersenne Twister algorithm. This is a deterministic 
algorithm, but you can alter the initial seed by using the random.seed() function. For example:
"""
random.seed()            # Seed based on system time or os.urandom()
random.seed(12345)       # Seed based on integer given
random.seed(b'bytedata') # Seed based on byte data

"""
In addition to the functionality shown, random() includes functions for uniform, Gaussian, and other 
probabality distributions. For example, random.uniform() computes uniformly distributed numbers, 
and random.gauss() computes normally distributed numbers. Consult the documentation for 
information on other supported distributions.

Functions in random() should not be used in programs related to cryptography. If you need such 
functionality, consider using functions in the ssl module instead. For example, ssl.RAND_bytes() 
can be used to generate a cryptographically secure sequence of random bytes.
"""
