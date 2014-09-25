# coding=utf-8

"""
Problem

You have a CIDR network address such as "123.45.67.89/27," and you want to generate a range of all the IP addresses that it represents 
(e.g., "123.45.67.64," "123.45.67.65," …, "123.45.67.95").

Solution

The ipaddress module can be easily used to perform such calculations. For example:
"""
import ipaddress
net = ipaddress.ip_network('123.45.67.64/27')
for a in net:
    print(a)
# 123.45.67.64
# 123.45.67.65
# 123.45.67.66
# 123.45.67.67
# ...
# ...
# 123.45.67.92
# 123.45.67.93
# 123.45.67.94
# 123.45.67.95

net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
for a in net6:
    print(a)
# 12:3456:78:90ab:cd:ef01:23:30
# 12:3456:78:90ab:cd:ef01:23:31
# 12:3456:78:90ab:cd:ef01:23:32
# 12:3456:78:90ab:cd:ef01:23:33
# 12:3456:78:90ab:cd:ef01:23:34
# 12:3456:78:90ab:cd:ef01:23:35
# 12:3456:78:90ab:cd:ef01:23:36
# 12:3456:78:90ab:cd:ef01:23:37

"""
Network objects also allow indexing like arrays. For example:
"""
print(net.num_addresses)
# 32
print(net[0])
# 123.45.67.64
print(net[1])
# 123.45.67.65
print(net[-1])
# 123.45.67.95
print(net[-2])
# 123.45.67.94

"""
In addition, you can perform operations such as a check for network membership:
"""
a = ipaddress.ip_address('123.45.67.69')
print(a in net)
# True
b = ipaddress.ip_address('123.45.67.123')
print(b in net)
# False

"""
An IP address and network address can be specified together as an IP interface. For example:
"""
inet = ipaddress.ip_interface('123.45.67.73/27')
print(inet.network)
# 123.45.67.64/27
print(inet.ip)
# 123.45.67.73

"""
Discussion

The ipaddress module has classes for representing IP addresses, networks, and interfaces. 
This can be especially useful if you want to write code that needs to manipulate network addresses in some way 
(e.g., parsing, printing, validating, etc.).

Be aware that there is only limited interaction between the ipaddress module and other network-related modules, 
such as the socket library. In particular, it is usually not possible to use an instance of IPv4Address as a substitute for address string. 
Instead, you have to explicitly convert it using str() first. For example:

>>> a = ipaddress.ip_address('127.0.0.1')
>>> from socket import socket, AF_INET, SOCK_STREAM
>>> s = socket(AF_INET, SOCK_STREAM)
>>> s.connect((a, 8080))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'IPv4Address' object to str implicitly
>>> s.connect((str(a), 8080))
>>>
"""