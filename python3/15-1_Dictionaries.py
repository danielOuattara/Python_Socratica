# !bin/bash
# Daniel OUATTARA
# 02 03 2020
#

"""
Python Date storage:
 > Set
 > List
 > Tuples
 > Dictionary

 Dictionaries:
"""

# Methods for creating dictionaries:
# -----------------------------------
# 1. use curly brackets: {key1: value1, key2: value2}
# 2. dict contractor: dict(key1=value, key2=value2)

#  FriendFace post:
'''
user_id = 209
message = "D5 E5 F6 G4 Z10"
language = "English"
datetime = "20200302T175730"
location = (44.5896574, -36.768876)
'''
#  Method 1:

post = {
    "user_id": 209,
    "message": "D5 E5 F6 G4 Z10",
    "gender": "female",
    "language": "English",
    "datetime": "20200302T175730",
    "location": (44, 5896574, -36.768876),
}

print('post =', post)
print('type post =', type(post))


#  Method 2:

post2 = dict(
    message="SS cotopaxi",  # Notice: key value not require quotes
    language="english"  # Notice: key value not require quotes
)

print('post2 =', post2)

# Adding new item, key with quote are required  in brackets
post2["User_id"] = 209
# Adding another item, key with quote required in brackets
post2["datetime"] = '20200302T191045Z'
print('post2 =', post2)

#  Accessing Data in Dictionaries

print(post["message"])
#  print(post2["location"])  # cause crash: location keyError not in post2


#  use of "if" statement to avoid KeyError, if any !


if 'location' in post2:
    print(post2["location"])
else:
    print("The post2 dictionary does not contain a location key")

# use of try to except KeyError, if any !

try:
    print(post2["location"])
except KeyError:
    print("The post2 dictionary does not contain a location key")


print(100 * '=')
#  help(dict)
dict_zero = dict()


print(dir(dict_zero))

print(100 * '=')
print(help(dict_zero))

print(100 * '=')

# To find a value for a specific key, if it exists in the dictionary
print(post.get('user_id', None))
print(post.get('loc', None))

print('post =', post, '\n')

#  Iterate over all the key values:

for key in post.keys():
    value = post[key]
    print(key, '=', value)
print('\n')

#  Iterate over all the key values:

for key, value in post.items():
    print(key, '=', value)

print('\n')

#  Remove items from dictionary

#  help(dict.pop)
post.pop('location')
print('post=', post)
post.pop('price', None)
print('post=', post)

help(dict.popitem)

post.popitem()('gender', 'female')
print('post=', post)


#  help(dict.clear)
post.clear()
print('post=', post)
