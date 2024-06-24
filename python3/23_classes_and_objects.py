# !bin/bash
# Daniel OUATTARA
# 24 06 2024


""""""


import datetime


class User:
    pass


# user_1 is an instance of the class User
user_1 = User()

# first_name & last_name are data attached to an instance
user_1.first_name = "John"
user_1.last_name = "Doe"


print(user_1.first_name)

print(user_1.last_name)


#

user_2 = User()
user_2.first_name = "Jana"
user_2.last_name = "Roberts"

print(f'{user_2.first_name} {user_2.last_name}')

user_1.age = 37

user_2.favorite_book = "2001: A space Odyssey"

"""
Class Features
---------------
> init method
> Methods
> Initialization
> Help text

"""

# -----------------------------------------------------


class User_2:
    """"Docstring:
    A member of FriendFace.
    For now we are only storing name and birthday 

    """

    def __init__(self, full_name, birthday) -> None:
        self.name = full_name
        self.birthday = birthday  # yyyymmdd

        # Extract first and last names

        name_pieces = full_name.split(' ')
        (self.first_name, self.last_name) = name_pieces

    def age(self):
        """Return the age ot the user in years """
        today = datetime.date(2024, 6, 24)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:])
        date_of_birth = datetime.date(yyyy, mm, dd)
        age_in_days = (today - date_of_birth).days
        age_in_years = age_in_days / 365
        return int(age_in_years)


sara = User_2(full_name='Sara Conor', birthday="19710315")

print(f'{sara.name} {sara.birthday}')
print(f'{sara.first_name}')
print(f'{sara.last_name}')


print(help(User_2))

print(sara.age())
