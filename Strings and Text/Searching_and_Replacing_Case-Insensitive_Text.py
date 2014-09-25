# coding=utf-8

"""
Problem

You need to search for and possibly replace text in a case-insensitive manner.

Solution

To perform case-insensitive text operations, you need to use the re module and supply the re.IGNORECASE 
flag to various operations. For example:
"""
text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python', text, flags=re.IGNORECASE)
# Returns ['PYTHON', 'python', 'Python']
re.sub('python', 'snake', text, flags=re.IGNORECASE)
# Returns 'UPPER snake, lower snake, Mixed snake'

"""
The last example reveals a limitation that replacing text won’t match the case of the matched text. 
If you need to fix this, you might have to use a support function, as in the following:
"""
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

"""
Here is an example of using this last function:
"""
re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
# Returns 'UPPER SNAKE, lower snake, Mixed Snake'

"""
Discussion

For simple cases, simply providing the re.IGNORECASE is enough to perform case-insensitive matching. 
However, be aware that this may not be enough for certain kinds of Unicode matching involving case 
folding. See "Working with Unicode Characters in Regular Expressions" for more details.
"""
