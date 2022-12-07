""" This is the debugger tool module. """

from time import time

import logging


def iter_check(seconds: float, iterator: any, last_check_time, name="") -> float:
    """ ...
        eg.
        last_check_time = 0
        for i in range(1000):
            sleep(0.1)
            last_check_time = iter_check(10, i, last_check_time, name="demo")
    
        TODO:
            - docstring
            - proper logging
    """

    if time() - last_check_time > seconds:
        print(f"{name}: {iterator}")
        return time()
    return last_check_time


# TESTING
# from time import sleep
# last_check_time = 0
# for i in range(1000):
#     sleep(0.1)
#     last_check_time = iter_check(10, i, last_check_time, name="demo")