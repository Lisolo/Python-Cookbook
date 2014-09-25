# coding=utf-8

"""
Problem

You have code that needs to perform simple time conversions, like days to seconds, hours to minutes, 
and so on.

Solution

To perform conversions and arithmetic involving different units of time, use the datetime module. 
For example, to represent an interval of time, create a timedelta instance, like this:
"""
from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
# 2
print(c.seconds)
# 37800
print(c.seconds / 3600)
# 10.5
print(c.total_seconds() / 3600)
# 58.5

"""
If you need to represent specific dates and times, create datetime instances and use the standard 
mathematical operations to manipulate them. For example:
"""
from datetime import datetime
d = datetime(2014, 8, 7)
print(d + timedelta(days=10))
# 2014-08-17 00:00:00

e = datetime(2014, 12, 21)
f = e - d
print(f.days)
# 136
now = datetime.today()
print(now)
# 2014-08-07 11:11:40.953000
print(now + timedelta(minutes=50))
# 2014-08-07 12:01:40.953000

"""
When making calculations, it should be noted that datetime is aware of leap years. For example:
"""
a2 = datetime(2012, 3, 1)
b2 = datetime(2012, 2, 28)
a2 - b2
# Returns datetime.timedelta(2)
(a2 - b2).days
# Returns 2
c2 = datetime(2013, 3, 1)
d2 = datetime(2013, 2, 28)
(c2 - d2).days
# Returns 1

"""
Discussion

For most basic date and time manipulation problems, the datetime module will suffice. If you need to 
perform more complex date manipulations, such as dealing with time zones, fuzzy time ranges, 
calculating the dates of holidays, and so forth, look at the dateutil module.

To illustrate, many similar time calculations can be performed with the dateutil.relativedelta() function. 
However, one notable feature is that it fills in some gaps pertaining to the handling of months 
(and their differing number of days). For instance:
"""
a3 = datetime(2014, 8, 7)
a3 + timedelta(months=1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'months' is an invalid keyword argument for this function

from dateutil.relativedelta import relativedelta
a3 + relativedelta(months=+1)
# Returns datetime.datetime(2014, 9, 7, 0, 0)
a3 + relativedelta(months=+4)
# Returns datetime.datetime(2014, 12, 7, 0, 0)

# Time between two dates
b3 = datetime(2014, 12, 25)
c3 = b3 - a3
print(c3)
# 140 days, 0:00:00
c3 = relativedelta(b3, a3)
c3
# Returns relativedelta(months=+4, days=+19)
c3.months
# Returns 4
c3.days
# Returns 19
