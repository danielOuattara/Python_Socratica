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


# Scan for blocks of lower case letters

regex = r'[a-z]+'
for name in names:
    matches = re.findall(regex, name)
    if matches:
        print(matches)

print('----')


# Scan fro blocks of lower case letters

regex = r'[a-z]+'
for name in names:
    matches = re.finditer(regex, name)
    for match in matches:
        print(match)

print('----')
