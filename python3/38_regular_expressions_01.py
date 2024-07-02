# Daniel OUATTARA
# 01 07 2024


import re


# for item in dir(re):
#     print(item)


"""
Regular Expressions
--------------------


A
ASCII
DEBUG
DOTALL
I
IGNORECASE
L
LOCALE
M
MULTILINE
Match
NOFLAG
Pattern
RegexFlag
S
Scanner
T
TEMPLATE
U
UNICODE
VERBOSE
X
_MAXCACHE
__all__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__path__
__spec__
__version__
_cache
_casefix
_compile
_compile_repl
_compiler
_constants
_expand
_parser
_pickle
_special_chars_map
_subx
compile
copyreg
enum
error
escape
findall
finditer
fullmatch
functools
match
purge
search
split
sub
subn
template
--------

examples:

^S.+a
S[a-t]*$
\w{9}


^ $       ::   describe a position
\w  [a-t] ::    "     a set of characters
+ * {9}   ::    "     a quantifiers
\d        ::   matches 0 to 9
\d\d      ::   matches 0 to 9 consecutive
\s        ::   matches one space character
\w        ::   matches one in a-z A-Z 0-9 _
^\w\w\w\s ::   matches 4 word and 1 space char

-- quantifiers

*         :: 0+
?         :: 0 or 1
+         :: 1 or plus
{n}       :: exactly n-occurrences


[aeiouy]{2}
^\w{7}$
\w{7}

"""


names = [
    'Fin Bindeballe',
    'Geir Anders Berge',
    'HappyCodingRobot',
    'Ron Cromberge',
    'Sohil'
]


# Search for a sequence first name & last name

for name in names:
    if re.search(r'^\w+\s+\w+$', name):
        print(name)

print('----')

# Search for a sequence first name & last name

regex = r'^\w+\s+\w+$'
for name in names:
    match = re.search(regex, name)
    if match:
        print(match)
        print(name)

print('----')

# Search for word char sequence starting with C

regex = r'C\w*'
for name in names:
    match = re.search(regex, name)
    if match:
        print(name)
        print(match.start())
        print(match.end())
        print(match.span())
        print(match.group())

print('----')
