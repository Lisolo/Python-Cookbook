# coding=utf-8

"""
Problem

You have a sequence of dictionaries or instances and you want to iterate over the data in 
groups based on the value of a particular field, such as date.

Solution

The itertools.groupby() function is particularly useful for grouping data together like this. 
To illustrate, suppose you have the following list of dictionaries:
"""
rows = [
    {'address': '5412 N CLARK', 'date': '08/01/2014'},
    {'address': '5148 N CLARK', 'date': '08/04/2014'},
    {'address': '5800 E 58TH', 'date': '08/02/2014'},
    {'address': '2122 N CLARK', 'date': '08/03/2014'},
    {'address': '5645 N RAVENSWOOD', 'date': '08/02/2014'},
    {'address': '1060 W ADDISON', 'date': '08/02/2014'},
    {'address': '4801 N BROADWAY', 'date': '08/01/2014'},
    {'address': '1039 W GRANVILLE', 'date': '08/04/2014'},
]

"""
Now suppose you want to iterate over the data in chunks grouped by date. To do it, first sort 
by the desired field (in this case, date) and then use itertools.groupby():
"""
from operator import itemgetter
from itertools import groupby

# Sort by the desired field first
rows.sort(key=itemgetter('date')) 

# Iterate in groups
for date, items in groupby(rows,key=itemgetter('date')):
    print(date)
    for x in items:
        print('    ', x)

"""
08/01/2014
    {'date': '08/01/2014', 'address': '5412 N CLARK'}
    {'date': '08/01/2014', 'address': '4801 N BROADWAY'}
08/02/2014
    {'date': '08/02/2014', 'address': '5800 E 58TH'}
    {'date': '08/02/2014', 'address': '5645 N RAVENSWOOD'}
    {'date': '08/02/2014', 'address': '1060 W ADDISON'}
08/03/2014
    {'date': '08/03/2014', 'address': '2122 N CLARK'}
08/04/2014
    {'date': '08/04/2014', 'address': '5148 N CLARK'}
    {'date': '08/04/2014', 'address': '1039 W GRANVILLE'}
"""

"""
Discussion

The groupby() function works by scanning a sequence and finding sequential "runs" of identical 
values (or values returned by the given key function). On each iteration, it returns the value 
along with an iterator that produces all of the items in a group with the same value.

An important preliminary step is sorting the data according to the field of interest. 
Since groupby() only examines consecutive items, failing to sort first won’t group the records 
as you want.

If your goal is to simply group the data together by dates into a large data structure that 
allows random access, you may have better luck using defaultdict() to build a multidict, 
as described in "Mapping Keys to Multiple Values in a Dictionary". For example:
"""
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

"""
This allows the records for each date to be accessed easily like this:
"""
for r in rows_by_date['08/01/2014']:
    print(r)
# {'date': '08/01/2014', 'address': '5412 N CLARK'}
# {'date': '08/01/2014', 'address': '4801 N BROADWAY'}

"""
For this latter example, it’s not necessary to sort the records first. Thus, if memory is no concern, 
it may be faster to do this than to first sort the records and iterate using groupby(). 
"""
