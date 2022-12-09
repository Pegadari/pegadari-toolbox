""" This is the debugger tool module. """

from time import time

import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)


# logging.setLevel(logging.DEBUG)



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
            - tidy code
            - ammend docstring
    """

    if time() - last_pulse > period:
        # print(f"{name}: {index}")
        logger.debug(f"{name}:{index}")
        # logging.debug(f"{name}: {index}")
        return time()
    return last_pulse


# TESTING
# from time import sleep
# last_pulse = 0
# for i in range(50):
#     sleep(0.5)
#     last_pulse = heartbeat(5, last_pulse, i, "demo")