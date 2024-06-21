# !bin/bash
# Daniel OUATTARA
# 21 06 2024
#


""""
Logging
---------

<< Hope for the best, and plan for the worst with logging ! >>

Purpose: write status messages to a file or other output stream 
         about which part of the code have executed and what 
         problems may have arisen

Levels: Debug, Info, Warning, Error, Critical

NOTSET     0
DEBUG     10
INFO      20
WARNING   30
ERROR     40
CRITICAL  50

"""

import logging


# for item in dir(logging):
#     print(item)

"""
NOTE: while reading above output, keep in mind:
- uppercase items are constants
- capitalize items are classes
- lowercase items are methods
"""

#  Create & configure a logger
#  ============================

# #(1). Basic config, no name first
#  logging.basicConfig(filename="17_lumberjack.log")


# # (2) NOTE: basicConfig set the default log level to WARNING = 30
#  logging.basicConfig(filename="17_lumberjack.log", level=logging.DEBUG)


# # (3). adding a LOG_FORMAT
# LOG_FORMAT = "%(levelname)s %(asctime)s %(message)s"
# logging.basicConfig(
#     filename="17_lumberjack.log",
#     level=logging.DEBUG,
#     format=LOG_FORMAT
# )


# (4). The log file is created by default in append mode
# LOG_FORMAT = "%(levelname)s %(asctime)s %(message)s"
# logging.basicConfig(
#     filename="17_lumberjack.log",
#     level=logging.DEBUG,
#     format=LOG_FORMAT,
#     filemode='w'
# )


# (5). Now change the level to logging.ERROR:
#      you will see logs from ERROR up to CRITICAL
LOG_FORMAT = "%(levelname)s %(asctime)s %(message)s"
logging.basicConfig(
    filename="17_lumberjack.log",
    level=logging.ERROR,
    format=LOG_FORMAT,
    filemode='w'
)

# (6). back to logging.debug
LOG_FORMAT = "%(levelname)s %(asctime)s %(message)s"
logging.basicConfig(
    filename="17_lumberjack.log",
    level=logging.DEBUG,
    format=LOG_FORMAT,
    filemode='w'
)


# create a logger object
logger = logging.getLogger()  # no name provided for logger

logger.info('Our first logging message')

print(logger.level)


logger.debug("This is a armless debug message")
logger.info("Just some useful info")
logger.warning("I'm sorry, this action is dangerous")
logger.error("Did you just tru to divide by zero")
logger.critical("The entire internet is worldly down...")
