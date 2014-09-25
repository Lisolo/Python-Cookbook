# coding=utf-8

"""
Problem

Many unix commands have a typical pattern. They accept multiple filenames as arguments, 
does some processing and prints the lines back. Some examples of such commands are cat and grep.
"""
def unixcommand(f):
	def g(filenames):
		print(out for line in readlines(filenames)
			               for out in f(line))
	return g

@unixcommand
def cat(line):
	yield line

@unixcommand
def lowercase(line):
	yield line.lower()
