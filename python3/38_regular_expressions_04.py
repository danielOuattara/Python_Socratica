# Daniel OUATTARA
# 01 07 2024


import re


# for item in dir(re):
#     print(item)


"""
Regular Expressions
--------------------

examples:

^S.+a
S[a-t]*$
\w{9}


^ $       :: describe a position
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
    'Brian Daugette',
    'Veronica Supersonica',
    'Tony Gasparovic',
    'Partick German',
    'm!sha'
]


urls = [
    'https://www.socratica.com',
    'http://www.socratica.org',
    'file://pop3test.email.path',
    'com.socratica.www_https'
]

#  Test if string starts with 'http' or 'https'

"""
re.match = match(pattern, string, flags=0)

Try to apply the pattern at the start of the string, returning
a Match object, or None if no match was found.
"""

regex = r'https?'

for url in urls:
    match = re.match(regex, url)
    print(match)

print('-----')  # OR

for url in urls:
    if re.match(regex, url):
        print(url)

print('---------------------------------')


""""
re.fullmatch = fullmatch(pattern, string, flags=0)

Try to apply the pattern to all of the string, returning
a Match object, or None if no match was found."""


regex = r'https?://w{3}?\.\w+\.(org|com)'

for url in urls:
    match = re.fullmatch(regex, url)
    print(match)

print('-----')  # OR

for url in urls:
    if re.fullmatch(regex, url):
        print(url)

print('---------------------------------')
