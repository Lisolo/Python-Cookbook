# coding=utf-8


"""
Problem

You need to manipulate pathnames in order to find the base filename, directory name, absolute path, and so on.

Solution

To manipulate pathnames, use the functions in the os.path module. Here is an interactive example that 
illustrates a few key features:
"""
import os
path = '/Users/beazley/Data/data.csv'

# Get the last component of the path
os.path.basename(path)
# Returns 'data.csv'

# Join path components together
os.path.join('tmp', 'data', os.path.basename(path))
# Returns 'tmp/data/data.csv'

# Expand the user's home directory
path = '~/Data/data.csv'
os.path.expanduser(path)
# Returns '/home/solo/Data/data.csv'

# Split the file extension
os.path.splitext(path)
# Returns ('~/Data/data', '.csv')

"""
Discussion

For any manipulation of filenames, you should use the os.path module instead of trying to 
cook up your own code using the standard string operations. In part, this is for portability. 
The os.path module knows about differences between Unix and Windows and can reliably deal with 
filenames such as Data/data.csv and Data\data.csv. Second, you really shouldn’t spend your time 
reinventing the wheel. It’s usually best to use the functionality that’s already provided for you.

It should be noted that the os.path module has many more features not shown in this recipe. 
Consult the documentation for more functions related to file testing, symbolic links, and so forth.
"""
