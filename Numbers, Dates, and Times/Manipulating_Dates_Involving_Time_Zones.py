# coding=utf-8

"""
Problem

You had a conference call scheduled for December 21, 2012, at 9:30 a.m. in Chicago. At what local time did 
your friend in Bangalore, India, have to show up to attend?

Solution

For almost any problem involving time zones, you should use the pytz module. This package provides the 
Olson time zone database, which is the de facto standard for time zone information found in many 
languages and operating systems.

A major use of pytz is in localizing simple dates created with the datetime library. For example, here is 
how you would represent a date in Chicago time:
"""
from datetime import datetime
from pytz import timezone
d = datetime(2014, 8, 8, 9, 23, 0)
print(d)
# 2014-08-08 09:23:00

# Localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localized(d)
print(loc_d)

"""
Once the date has been localized, it can be converted to other time zones. To find the same time in 
Bangalore, you would do this:
"""
