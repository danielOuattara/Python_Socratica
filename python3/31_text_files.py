# !bin/bash
# Daniel OUATTARA
# 28 06 2024


"""
read & write in files
---------------------------

# Text files
- plain text
- XML
- JSON
- source code
- etc ...

# Binary Files
- compiled code
- app data
- media files (images, audio, video)
- etc ...


"""


# sprint(help(open))

# open and read the content of a file
print('------------------------------')

file = open('./31_text_files/guido_bio.txt')
content = file.read()
file.close()

print(content)


# safer and efficient than previous: file auto close in any case
print('------------------------------')

with open('./31_text_files/guido_bio.txt') as file_object:
    bio = file_object.read()

print(bio)
print('------------------------------')

# what happens when trying to open a file that does not exist ?

# with open('./31_text_files/not_exist.txt') as file_not_exits:
#     text = file_not_exits.read()

# --> FileNotFoundError: [Errno 2] No such file or directory: './31_text_files/not_exist.txt'

#  Solution

# ---
try:
    with open('./31_text_files/not_exist.txt') as file_not_exits:
        text = file_not_exits.read()

except FileNotFoundError:
    text = None

print(f'text: {text}')
print('------------------------------')
# ---

try:
    with open('./31_text_files/guido_bio.txt') as file_not_exits:
        text = file_not_exits.read()

except FileNotFoundError:
    text = None

print(f'text: {text}')
print('------------------------------')


# Oceans to file

oceans = ['Pacific', 'Atlantic', 'Indian', 'Antarctic', 'Arctic']

with open('./31_text_files/oceans.txt', 'w') as file:
    for ocean in oceans:
        file.write(f'{ocean}\n')
