'''
Python provides two levels of access to network services. At a low level, you
can access the basic socket support in the underlying operating system, which
allows you to implement clients and servers for both connection-oriented and
connectionless protocols.

Python also has libraries that provide higher-level access to specific
application-level network protocols, such as FTP, HTTP, and so on.
(resource: https://www.tutorialspoint.com/python/python_networking.htm)

=====================================socket=====================================
A socket is one endpoint of a two-way communication link between two programs
running on the network. A socket is bound to a port number so that the TCP layer
can identify the application that data is destined to be sent to. An endpoint is
a combination of an IP address and a port number.

A socket is much like a file, except that a single socket provides a two-way
connection between two programs. You can both read from and write to the same
socket. If you write something to a socket, it is sent to the application at the
other end of the socket. If you read from the socket, you are given the data
which the other application has sent.

To create a socket, you must use the socket.socket() function available in
socket module, which has the general syntax −
+------------------------------------------------------------------+
| cSocket = socket.socket (socket_family, socket_type, protocol=0) |
+------------------------------------------------------------------+

The following code is like dialing a phone number; doesn't do anything else:

+----------------------------Example----------------------------+
| import socket                                                 |
| cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   |
| cSocket.connect(('data.pr4e.org', 80))                        |
+---------------------------------------------------------------+

Domain:
These constants represent the address (and protocol) families:
socket.AF_UNIX
socket.AF_INET: These sockets account for at least 99% of the sockets in use
socket.AF_INET6

Type:
socket.SOCK_STREAM: for connection-oriented protocols
socket.SOCK_DGRAM: for connectionless protocols
socket.SOCK_RAW
socket.SOCK_RDM
socket.SOCK_SEQPACKET

Protocol:
Typically zero, this may be used to identify a variant of a protocol within a
domain and type. This is usually left out, defaulting to 0.

Server Socket Methods:
cSocket.bind(): This method binds address (hostname, port number pair) to socket.
cSocket.listen(): This method sets up and start TCP listener.
cSocket.accept(): This passively accept TCP client connection, waiting until
                  connection arrives (blocking).

Client Socket Methods:
cSocket.connect(): This method actively initiates TCP server connection.

General Socket Methods:
cSocket.recv(): This method receives TCP message
cSocket.send(): This method transmits TCP message
cSocket.recvfrom(): This method receives UDP message
cSocket.sendto(): This method transmits UDP message
cSocket.close(): This method closes socket
socket.gethostname(): Returns the hostname.

=================================urllib.request=================================
The module urllib.request is a Python module for fetching URLs.
It offers a very simple interface, in the form of the urlopen function.
This is capable of fetching URLs using a variety of different protocols.
Let’s take a look at a simple way to fetch the contents of a specific URL:
+----------------------------Example-----------------------------+
|import urllib.request                                           |
|# Open the connection to the URL                                |
|response = urllib.request.urlopen('http://www.python.org')      |
|# used the urlconnection to read all the data into a variable   |
|html = response.read().decode().split('\n')                     |
|# go through all the lines in the variable (content of the URL) |
|For linein html:                                                |
|    print(line)                                                 |
|# Like a file...                                                |
+----------------------------------------------------------------+

There are 2 handy functions that can be used with the reponse object returned
when we call urlopen(). They are info() and geturl()
Let’s take a look at an example of how to use them:
+-----------------------------------Example------------------------------------+
|import urllib.request                                                         |
|# Open the connection to the URL                                              |
|response = urllib.request.urlopen('http://www.python.org')                    |
|# use the info() function in order to obtain information about the urlfetched.|
|print (response.info())                                                       |
|# use the geturl() function to get the actual URL retrieved                   |
|print (response.geturl())                                                     |
+------------------------------------------------------------------------------+

By using the info() function you can also get to specific headers in the
returned URL
+-----------------------------------Example------------------------------------+
|import urllib.request                                                         |
|# Open the connection to the URL                                              |
|response = urllib.request.urlopen('http://www.python.org')                    |
|# use the info() function in order to obtain information about the urlfetched.|
|headers = response.info()                                                     |
|# use the geturl() function to get the actual URL retrieved                   |
|print (headers["Date"])                                                       |
|print (headers["Content-Type"])                                               |
+------------------------------------------------------------------------------+

=================================beautifulsoup==================================
The module beautifulsoup allows us to navigate html pages in a very convenient
way. We do not have to program the details of finding specific tags and extract
content, beautifulsoup does that for us.

Let’s take a look at a trivial example of using beautifulsoup to extract all <a>
tags from the html of a web page.
+------------------Example-------------------+
|import urllib.request                       |
|from bs4 import BeautifulSoup               |
|url= 'http://httpbin.org'                   |
|response = urllib.request.urlopen(url)      |
|html = response.read()                      |
|soup = BeautifulSoup(html, "html.parser")   |
|a_tags= soup('a')                           |
|for rows in a_tags:                         |
|    print(rows)                             |
+--------------------------------------------+

Let’s explore couple of other features of beautifulsoup. Lets get a specific
element inside a tag and the content of the tag (its value).
+-------------------Example--------------------+
|import urllib.request                         |
|from bs4 import BeautifulSoup                 |
|url= 'http://httpbin.org'                     |
|response = urllib.request.urlopen(url)        |
|html = response.read()                        |
|soup = BeautifulSoup(html, "html.parser")     |
|a_tags= soup('a')                             |
|for rows in a_tags:                           |
|    print(rows.get('href'))                   |
|    print(rows.contents)                      |
+----------------------------------------------+

Another helpful method, findAll():
+-------------------Example--------------------+
|import urllib.request                         |
|from bs4 import BeautifulSoup                 |
|url= 'http://httpbin.org'                     |
|response = urllib.request.urlopen(url)        |
|html = response.read()                        |
|soup = BeautifulSoup(html, "html.parser")     |
|#trying findall()                             |
|a_tags= soup.findAll('a')                     |
|for rows in a_tags:                           |
|    print(rows.get('href'))                   |
|    print(rows.contents)                      |
+----------------------------------------------+

**************************About Characters and Strings**************************
ASCII:
We refer to "8 bits of memory as a "byte" of memory – (i.e. my disk drive
contains 3 Terabytes of memory) The ord() function tells us the numeric value of
a simple ASCII character:

>>> print(ord('H'))
72
>>> print(ord('e'))
101
>>> print(ord('\n'))
10
>>>

Multi-Byte Characters:
To represent the wide range of characters computers must handle we represent
characters with more than one byte:
* UTF-16 – Fixed length - Two bytes
* UTF-32 – Fixed Length - Four Bytes
* UTF-8 – 1-4 bytes
 - Upwards compatible with ASCII
 - Automatic detection between ASCII and UTF-8
 - UTF-8 is recommended practice for encoding    data to be exchanged between systems

Python 2 versus Python 3

  Python 2.7.10           Python 3.5.1
------------------      ------------------
>>> x = b'abc'          >>> x = b'abc'
>>> type(x)             >>> type(x)
<type 'str'>            <class 'bytes'>
>>> x = '이광춘'         >>> x = '이광춘'
>>> type(x)             >>> type(x)
<type 'str'>            <class 'str'>
>>> x = u'이광춘'        >>> x = u'이광춘'
>>> type(x)             >>> type(x)
<type 'unicode'>        <class 'str'>

* In Python 3, all strings internally are UNICODE
* Working with string variables in Python programs and reading data from files
  usually "just works"
* When we talk to a network resource using sockets or talk to a database we have
  to encode and decode data (usually to UTF-8)

Python Strings to Bytes:
* When we talk to an external resource like a network socket we send bytes, so we
  need to encode Python 3 strings into a given character encoding
* When we read data from an external resource, we must decode it based on the
  character set so it is properly represented in Python 3 as a string

  while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    mystring = data.decode()
    print(mystring)
'''
