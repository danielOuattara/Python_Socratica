# !bin/bash
# Daniel OUATTARA
# 28 06 2024


"""urllib"""


import urllib
from urllib import request

# for item in dir(urllib):
#     print(item)

print('------------------------')

"""
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__path__
__spec__
error
parse
request
response
"""

# print(help(urllib))


# for item in dir(request):
#     print(item)

"""
AbstractBasicAuthHandler
AbstractDigestAuthHandler
AbstractHTTPHandler
BaseHandler
CacheFTPHandler
ContentTooShortError
DataHandler
FTPHandler
FancyURLopener
FileHandler
HTTPBasicAuthHandler
HTTPCookieProcessor
HTTPDefaultErrorHandler
HTTPDigestAuthHandler
HTTPError
HTTPErrorProcessor
HTTPHandler
HTTPPasswordMgr
HTTPPasswordMgrWithDefaultRealm
HTTPPasswordMgrWithPriorAuth
HTTPRedirectHandler
HTTPSHandler
MAXFTPCACHE
OpenerDirector
ProxyBasicAuthHandler
ProxyDigestAuthHandler
ProxyHandler
Request
URLError
URLopener
UnknownHandler
__all__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
__version__
_cut_port_re
_ftperrors
_have_ssl
_localhost
_noheaders
_opener
_parse_proxy
_proxy_bypass_macosx_sysconf
_randombytes
_safe_gethostbyname
_splitattr
_splithost
_splitpasswd
_splitport
_splitquery
_splittag
_splittype
_splituser
_splitvalue
_thishost
_to_bytes
_url_tempfiles
addclosehook
addinfourl
base64
bisect
build_opener
contextlib
email
ftpcache
ftperrors
ftpwrapper
getproxies
getproxies_environment
hashlib
http
install_opener
io
localhost
noheaders
os
parse_http_list
parse_keqv_list
pathname2url
posixpath
proxy_bypass
proxy_bypass_environment
quote
re
request_host
socket
ssl
string
sys
tempfile
thishost
time
unquote
unquote_to_bytes
unwrap
url2pathname
urlcleanup
urljoin
urlopen  # <--
urlparse
urlretrieve
urlsplit
urlunparse
warnings
"""

# print(help(request))


# urlopen() example

response = request.urlopen('https://www.wikipedia.org/')

print(f'type(response)= {type(response)}')


print('--------------------------------')

# for item in dir(response):
#     print(item)

"""__abstractmethods__
__class__
__del__
__delattr__
__dict__
__dir__
__doc__
__enter__
__eq__
__exit__
__format__
__ge__
__getattribute__
__getstate__
__gt__
__hash__
__init__
__init_subclass__
__iter__
__le__
__lt__
__module__
__ne__
__new__
__next__
__reduce__
__reduce_ex__
__repr__
__setattr__
__sizeof__
__str__
__subclasshook__
_abc_impl
_checkClosed
_checkReadable
_checkSeekable
_checkWritable
_check_close
_close_conn
_get_chunk_left
_method
_peek_chunked
_read1_chunked
_read_and_discard_trailer
_read_chunked
_read_next_chunk_size
_read_status
_readinto_chunked
_safe_read
_safe_readinto
begin
chunk_left
chunked
close
closed
code  # << 200s, 300s, 400s, 500s 
debuglevel
detach
fileno
flush
fp
getcode
getheader
getheaders
geturl
headers
info
isatty
isclosed
length  # << in bytes
msg
peek  # << to see a small part of the response
read  # << to read the response
read1
readable
readinto
readinto1
readline
readlines
reason
seek
seekable
status
tell
truncate
url
version
will_close
writable
write
writelines"""


print(f'response.code = {response.code}')  # 200
print(f'response.length = {response.length}')  # 78322

print('--------------------------------')

print(f'response.peek() = {response.peek()}')

print('--------------------------------')

data = response.read()
print(f'type(data) = {type(data)}')

print('--------------------------------')

print(f'len(data)= {len(data)}')  # 78322

print('--------------------------------')

html = data.decode('utf-8')
print(f'type(html) = {type(html)}')

print('--------------------------------')

print('html = \n', html)

print('--------------------------------')
# try to read the response as second time ?

data = response.read()
print(f'type(data)= {type(data)}')
print(f'len(data)= {len(data)}')  # 78322
