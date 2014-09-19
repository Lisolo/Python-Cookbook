# coding=utf-8


"""
Problem

You need to access various services via HTTP as a client. For example, 
downloading data or interacting with a REST-based API.

Solution

For simple things, it’s usually easy enough to use the urllib.request module. 
For example, to send a simple HTTP GET request to a remote service, do something like this:
"""
from urllib import request, parse

# Base URL being accessed
url = 'http://httpbin.org/get'

# Dictionary of query parameters (if any)
parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}

# Encode the query string
querystring = parse.urlencode(parms)

# Make a GET request and read the response
u = request.urlopen(url+'?' + querystring)
resp = u.read()

"""
If you need to send the query parameters in the request body using a POST method, 
encode them and supply them as an optional argument to urlopen() like this:
"""
# Make a POST request and read the response
u2 = request.urlopen(url, querystring.encode('ascii'))
resp2 = u2.read()

"""
If you need to supply some custom HTTP headers in the outgoing request such as a change to the user-agent field, 
make a dictionary containing their value and create a Request instance and pass it to urlopen() like this:
"""
# Extra headers
headers = {
    'User-agent' : 'non/ofyourbusiness',
    'Spam' : 'Eggs'
}

req = request.Request(url, querystring.encode('ascii'), headers=headers)

# Make a request and read the response
u3 = request.urlopen(req)
resp3 = u3.read()

"""
If your interaction with a service is more complicated than this, you should probably look at the requests library. 
For example, here is equivalent requests code for the preceding operations:
"""
import requests

# Base URL being accessed
url2 = 'http://httpbin.org/post'

resp4 = requests.post(url2, data=parms, headers=headers)

# Decoded text returned by the request
text = resp4.text

"""
A notable feature of requests is how it returns the resulting response content from a request. 
As shown, the resp.text attribute gives you the Unicode decoded text of a request. However, 
if you access resp.content, you get the raw binary content instead. On the other hand, 
if you access resp.json, then you get the response content interpreted as JSON.

Here is an example of using requests to make a HEAD request and extract a few fields of header data from the response:
"""
resp5 = requests.head('http://www.python.org/index.html')

status = resp5.status_code
last_modified = resp5.headers['last-modified']
content_type = resp5.headers['content-type']
content_length = resp5.headers['content-length']

"""
Here is a requests example that executes a login into the Python Package index using basic authentication:
"""
resp6 = requests.get('http://pypi.python.org/pypi?:action=login',
                    auth=('solo','pssword'))

"""
Here is an example of using requests to pass HTTP cookies from one request to the next:
"""
# First request
resp6 = requests.get(url2)

# Second requests with cookies received on first requests
resp7 = requests.get(url2, cookies=resp6.cookies)

"""
Last, but not least, here is an example of using requests to upload content:
"""
files = {'file': ('data.csv', open('data.csv', 'rb'))}

r = requests.post(url2, files=files)

"""
Discussion

For really simple HTTP client code, using the built-in urllib module is usually fine. 
However, if you have to do anything other than simple GET or POST requests, 
you really can’t rely on its functionality. This is where a third-party module, 
such as requests, comes in handy.

For example, if you decided to stick entirely with the standard library instead of a library like requests, 
you might have to implement your code using the low-level http.client module instead. 
For example, this code shows how to execute a HEAD request:
"""
from http.client import HTTPConnection

c = HTTPConnection('www.python.org', 80)
c.request('HEAD', '/index.html')
resp8 = c.getresponse()

print('Status', resp8.status)
for name, value in resp8.getheaders():
    print(name, value)

"""
Similarly, if you have to write code involving proxies, authentication, cookies, and other details, 
using urllib is awkward and verbose. For example, here is a sample of code that authenticates to 
the Python package index:
"""
auth = request.HTTPBasicAuthHandler()
auth.add_password('pypi', 'http://pypi.python.org', 'solo', 'password')
opener = request.build_opener(auth)

r2 = request.Request('http://pypi.python.org/pypi?:action=login')
u2 = opener.open(r2)
resp9 = u2.read()

# From here. You can access more pages using opener

"""
Frankly, all of this is much easier in requests.

Testing HTTP client code during development can often be frustrating because of all 
the tricky details you need to worry about (e.g., cookies, authentication, headers, encodings, etc.). 
To do this, consider using the httpbin service. This site receives requests and then echoes information 
back to you in the form a JSON response. Here is an interactive example:
"""
r3 = requests.get('http://httpbin.org/get?name=Daven&n=37',
     headers = {'User-agent': 'goaway/1.0'})
resp10 = r3.json
resp10['headers']
# {'User-Agent': 'goaway/1.0', 'Content-Length': '', 'Content-Type': '',
# 'Accept-Encoding': 'gzip, deflate, compress', 'Connection':
# 'keep-alive', 'Host': 'httpbin.org', 'Accept': '*/*'}
resp10['args']
# {'name': 'Dave', 'n': '37'}

"""
Working with a site such as httpbin.org is often preferable to experimenting with a real site—especially 
if there’s a risk it might shut down your account after three failed login attempts 
(i.e., don’t try to learn how to write an HTTP authentication client by logging into your bank).

Although it’s not discussed here, requests provides support for many more advanced HTTP-client protocols, 
such as OAuth. The requests documentation is excellent (and frankly better than anything that could 
be provided in this short space). Go there for more information.
"""
