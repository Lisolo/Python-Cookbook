# coding=utf-8

"""
Problem

You want an object to support customized formatting through the format() function and string method.

Solution

To customize string formatting, define the __format__() method on a class. For example:
"""
_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
    }

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

"""
Instances of the Date class now support formatting operations such as the following:

>>> d = Date(2014, 9, 25)
>>> format(d)
'2012-12-21'
>>> format(d, 'mdy')
'12/21/2012'
>>> 'The date is {:ymd}'.format(d)
'The date is 2014-9-25'
>>> 'The date is {:mdy}'.format(d)
'The date is 9/25/2014'
>>>
"""

"""
Discussion

The __format__() method provides a hook into Python’s string formatting functionality. 
It’s important to emphasize that the interpretation of format codes is entirely up to the class itself. 
Thus, the codes can be almost anything at all. 
For example, consider the following from the datetime module:

>>> from datetime import date
>>> d = date(2014, 09, 25)
>>> format(d)
'2014-09-25'
>>> format(d,'%A, %B %d, %Y')
'Thursday, September 25, 2014'
>>> 'The end is {:%d %b %Y}. Goodbye'.format(d)
'The end is 25 Sep 2014. Goodbye'
>>>
"""

"""
There are some standard conventions for the formatting of the built-in types. 
See the documentation for the string module for a formal specification.
"""