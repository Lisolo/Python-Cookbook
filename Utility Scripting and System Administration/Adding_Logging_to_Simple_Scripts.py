# coding=utf-8

"""
Problem

You want scripts and simple programs to write diagnostic information to log files.

Solution

The easiest way to add logging to simple programs is to use the logging module. For example:
"""
import logging

def main():
	logging.basicConfig(
		filename='app.log',
		level=logging.ERROR
	)