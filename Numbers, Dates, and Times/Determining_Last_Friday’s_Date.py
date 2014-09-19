# coding=utf-8


"""
Problem

You want a general solution for finding a date for the last occurrence of a day of the week. Last Friday, 
for example.

Solution

Python’s datetime module has utility functions and classes to help perform calculations like this. 
A decent, generic solution to this problem looks like this:
"""
from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wendesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

"""
Using this in an interpreter session would look like this:
"""
datetime.today()   # For reference
# Returns datetime.datetime(2014, 8, 7, 14, 54, 50, 250000)
get_previous_byday('Monday')
# Returns datetime.datetime(2014, 8, 4, 14, 56, 17, 656250)
get_previous_byday('Tuesday')
# Returns datetime.datetime(2014, 8, 5, 14, 56, 17, 656250)
get_previous_byday('Thursday')
# Returns datetime.datetime(2014, 7, 31, 14, 56, 19, 171875)

"""
The optional start_date can be supplied using another datetime instance. For example:
"""
get_previous_byday('Sunday', datetime(2014, 12, 23))
# Returns datetime.datetime(2014, 12, 21, 0, 0)

"""
Discussion

This recipe works by mapping the start date and the target date to their numeric position in the week 
(with Monday as day 0). Modular arithmetic is then used to figure out how many days ago the target 
date last occurred. From there, the desired date is calculated from the start date by subtracting 
an appropriate timedelta instance.

If you’re performing a lot of date calculations like this, you may be better off installing the 
python-dateutil package instead. For example, here is an example of performing the same 
calculation using the relativedelta() function from dateutil:
"""
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
d = datetime.now()
print(d)
# 2014-08-07 15:05:28.546875

# Next Friday
print(d + relativedelta(weekday=FR))
# 

# Last Friday
print(d + relativedelta(weekday=FR(-1)))
# 
