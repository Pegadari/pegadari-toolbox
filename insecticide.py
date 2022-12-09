""" This is the debugger tool module. """

from time import time

import logging


def heartbeat(period: float, last_pulse, index: any, name="") -> float:
    """ Debugs a heartbeart of the iterator using the logging module.
    
        Args:
            period: seconds between pulses
            last_pulse: UNIX time of last pulse
            index: the progress through the loop
            name: name to differentiate heartbeats
            
        Returns:
            UNIX time of last pulse

        Usage:
        >>> last_pulse = 0
        >>> for i in range(30):
                sleep(0.5)
                last_pulse = heartbeat(5, last_pulse, i, name="demo")
        demo: 0
        demo: 10
        demo: 20
    
        TODO:
            - proper logging
    """

    if time() - last_pulse > period:
        print(f"{name}: {index}")
        return time()
    return last_pulse


# TESTING
# from time import sleep
# last_pulse = 0
# for i in range(50):
#     sleep(0.5)
#     last_pulse = heartbeat(5, last_pulse, i, "demo")