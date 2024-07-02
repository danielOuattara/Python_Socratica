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
    'm!sha',
    'm!sha23',
]


# Search for a sequence first name & last name

regex = r'^\w+\s+\w+$'
for name in names:
    match = re.search(regex, name)
    if match:
        print(name)

print('----')


# Search for a sequence first name & last name with group

regex = r'^(\w+)\s+(\w+)$'
for name in names:
    match = re.search(regex, name)
    if match:
        # print(name)
        # print(match.group())
        print(match.group(1))
        print(match.group(2))

print('----')

# Search for a sequence first name & last name with named group

regex = r'^(?P<first_name>\w+)\s+(?P<last_name>\w+)$'
for name in names:
    match = re.search(regex, name)
    if match:
        # print(name)
        # print(match.group())
        print(match.group('first_name'))
        print(match.group('last_name'))

print('----')


# detect last name
regex = r'^[a-zA-Z!]+$'

for name in names:
    if re.search(regex, name):
        print(name)
