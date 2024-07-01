
"""urllib"""


from urllib import request, parse


resp = request.urlopen('https://www.google.com/search?q=socratica')

print(f'resp.code = {resp.code}')  # 200
print(f'resp.length = {resp.length}')  # None


# ---------------------------------------------------


# for item in dir(parse):
#     print(item)

"""DefragResult
DefragResultBytes
ParseResult
ParseResultBytes
ResultBase
SplitResult
SplitResultBytes
_ALWAYS_SAFE
_ALWAYS_SAFE_BYTES
_DefragResultBase
_NetlocResultMixinBase
_NetlocResultMixinBytes
_NetlocResultMixinStr
_ParseResultBase
_Quoter
_ResultMixinBytes
_ResultMixinStr
_SplitResultBase
_UNSAFE_URL_BYTES_TO_REMOVE
__all__
__builtins__
__cached__
__doc__
__file__
__getattr__
__loader__
__name__
__package__
__spec__
_asciire
_byte_quoter_factory
_checknetloc
_coerce_args
_decode_args
_encode_result
_hexdig
_hextobyte
_hostprog
_implicit_encoding
_implicit_errors
_noop
_portprog
_splitattr
_splithost
_splitnetloc
_splitnport
_splitparams
_splitpasswd
_splitport
_splitquery
_splittag
_splittype
_splituser
_splitvalue
_to_bytes
_typeprog
clear_cache
functools
namedtuple
non_hierarchical
parse_qs
parse_qsl
quote
quote_from_bytes
quote_plus
re
scheme_chars
splitattr
splithost
splitnport
splitpasswd
splitport
splitquery
splittag
splittype
splituser
splitvalue
sys
to_bytes
types
unquote
unquote_plus
unquote_to_bytes
unwrap
urldefrag
urlencode  <<---
urljoin
urlparse
urlsplit
urlunparse
urlunsplit
uses_fragment
uses_netloc
uses_params
uses_query
uses_relative
warnings"""


'''
https://youtu.be/LosIGgon_KM?si=jlHuYx7miQx8qSrI&t=335

'''

params = {'si': 'jlHuYx7miQx8qSrI', 't': 355}
query_string = parse.urlencode(params)

print(f'query_string = {query_string}')

video_url = f'https://youtu.be/LosIGgon_KM?{query_string}'

resp = request.urlopen(video_url)

print(f'resp.isclosed() = {resp.isclosed()}')  # False

print(f'resp.code = {resp.code}')  # 200

html = resp.read().decode('utf-8')

print('html = ',  html[:500])
