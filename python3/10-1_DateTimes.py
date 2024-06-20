# bin/bash !
# Daniel OUATTARA
# 24 02 2020
# Socratica-Python3.x

import sys  # bring a library of system functions
import datetime

"""
https://docs.python.org/3.11/library/datetime.html

"""

'''Datetime :
   ==========

  > help('modules')  # to see all available modules
   
  > import datetime  # import 'datetime' module
   
  > dir()  # check that 'datetime' is imported

  > dir(datetime)  
  
  > help(datetime.date)  # date class info
'''

gvr = datetime.date(1956, 1, 31)
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)

my_date = datetime.datetime(1983, 12, 15)
print(my_date)

my_date = datetime.date(1983, 12, 15)
print(my_date)

mill = datetime.date(2000, 1, 1)

dt = datetime.timedelta(days=100)
deltaTime = mill + dt
print("deltaTime =", deltaTime)

# Python displays date format by default: year, month, day
# you can define your own format:

#  Old style:
print("ownDateFormat :", gvr.strftime("%A, %B %d, %Y"))

#  New style:
message = "GVR was born on {: %A, %B %d, %Y}"
print(message.format(gvr))

launchDate = datetime.date(2017, 3, 30)
launchTime = datetime.time(22, 27, 0)
launchDateTime = datetime.datetime(2017, 3, 30, 22, 27, 0)

print("launchDate :", launchDate)
print("launchTime :", launchTime)
print("launchDateTime :", launchDateTime)

# Current dateTime in Zulu (UTC)
now = datetime.datetime.today()
print("now = ", now)
print("now.microsecond = ", now.microsecond)

# Convert string to datetime:
# datetime|M, datetime|C, strptime()|Meth.

moonLanding = "7/20/1969"
moonLandingDatetime = datetime.datetime.strptime(moonLanding, "%m/%d/%Y")
print("moonLandingDatetime :", moonLandingDatetime)
print(type(moonLanding))
print(type(moonLandingDatetime))
