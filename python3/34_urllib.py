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
urlopen  #
urlparse
urlretrieve
urlsplit
urlunparse
warnings
"""

# print(help(request))


# urlopen() example

response = request.urlopen('https://www.wikipedia.org/')
print('--------------------------------')

print(type(response))


print('--------------------------------')

for item in dir(response):
    print(item)

print('--------------------------------')

print(response.code)  # 200
print(response.length)  # 78322


print('--------------------------------')

print(response.peek())

print('--------------------------------')

data = response.read()
print(type(data))
print(len(data))  # 78322


print('--------------------------------')

html = data.decode('utf-8')
print(type(html))

print('--------------------------------')

print(html)

print('--------------------------------')
# try to read the response as second time ?

data = response.read()
print(type(data))
print(len(data))  # 78322
