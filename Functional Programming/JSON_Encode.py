# coding=utf-8

"""
Problem

Here is an example of JSON record.
{
    "name": "Advanced Python Training",
    "date": "October 13, 2012",
    "completed": false,
    "instructor": {
        "name": "Anand Chitipothu",
        "website": "http://anandology.com/"
    },
    "participants": [
        {
            "name": "Participant 1",
            "email": "email1@example.com"
        },
        {
            "name": "Participant 2",
            "email": "email2@example.com"
        }
    ]
}
It looks very much like Python dictionaries and lists. There are some differences though. Strings are always enclosed in double quotes, 
booleans are represented as true and false.

The standard library module json provides functionality to work in JSON. 
Lets try to implement it now as it is very good example of use of recursion.
"""
def json_encode(data):
	if isinstance(data, bool):
		if data:
			return "true"
		else:
			return "false"
	elif isinstance(data, (int, float)):
		return str(data)
	elif isinstance(data, str):
		return '"' + escape_string(data) + '"'
	elif isinstance(data, list):
		return "[" + ", ".join(json_encode(d) for d in data) + "]"
	else:
		raise TypeError("%s is not JSON serializable" % repr(data))

def escape_string(s):
	"""Escapes double-quote, tab and new line characters in a string."""
	s = s.replace('"', '\\"')
	s = s.replace("\t", "\\t")
	s = s.replace("\n", "\\n")
	return s