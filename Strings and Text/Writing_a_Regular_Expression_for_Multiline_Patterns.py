# coding=utf-8

"""
Problem

You’re trying to match a block of text using a regular expression, but you need the match to span multiple 
lines.

Solution

This problem typically arises in patterns that use the dot (.) to match any character but forget to 
account for the fact that it doesn’t match newlines. For example, suppose you are trying to match 
C-style comments:
"""
import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
              multiline comment */
'''
comment.findall(text1)
# Returns [' this is a comment ']
comment.findall(text2)
# Returns []

"""
To fix the problem, you can add support for newlines. For example:
"""
comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')
comment2.findall(text2)
# Returns [' this is a\n              multiline comment ']

"""
In this pattern, (?:.|\n) specifies a noncapture group (i.e., it defines a group for the purposes of 
matching, but that group is not captured separately or numbered).
"""

"""
Discussion

The re.compile() function accepts a flag, re.DOTALL, which is useful here. It makes the . in a regular 
expression match all characters, including newlines. For example:
"""
comment3 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
comment3.findall(text2)
# Returns [' this is a\n              multiline comment ']

"""
Using the re.DOTALL flag works fine for simple cases, but might be problematic if you’re working with 
extremely complicated patterns or a mix of separate regular expressions that have been combined together 
for the purpose of tokenizing, as described in "Tokenizing Text". If given a choice, it’s usually better 
to define your regular expression pattern so that it works correctly without the need for extra flags.
"""
