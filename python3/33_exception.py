# !bin/bash
# Daniel OUATTARA
# 28 06 2024


"""
- If you fail to plan, you are planning to fail

- If you fail to plan for failure, you are planning to fail as engineer


SyntaxError: invalid syntax
ZeroDivisionError
FileNotFoundError
TypeError
ValueError


try:

except:

else:

finally:


"""


#   Example: read binary data
# ----------------------------

import logging
import time

# create Logger
logging.basicConfig(filename="33_exception.log", level=logging.DEBUG)

logger = logging.getLogger()


def read_file_timed(path):
    """Return the content of the file at 'path' and measure time required"""
    start_time = time.time()
    try:
        file = open(path, mode='rb')
        data = file.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise

    finally:
        file.close()
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info(
            f'Time required for {path} file = {dt * 1_000:.6f} ms')


data = read_file_timed('./33_gvr.jpg')
data = read_file_timed('./33_gvr_2.jpg')
