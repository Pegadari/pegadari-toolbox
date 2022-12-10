""" This is the debugger tool module. """

from time import time
import logging


# create logger with level debug and default formatting
# verbose naming to avoid namespace collisions
insecticide_logger = logging.getLogger(__name__)
insecticide_logger.setLevel(logging.DEBUG)
insecticide_console_handler = logging.StreamHandler()
insecticide_console_handler.setLevel(logging.DEBUG)
insecticide_formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
insecticide_console_handler.setFormatter(insecticide_formatter)
insecticide_logger.addHandler(insecticide_console_handler)


def heartbeat(period: float, last_pulse, index: any, name="heartbeat") -> float:
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
                last_pulse = heartbeat(5, last_pulse, i, name="heartbeat_demo")
        DEBUG:insecticide:heartbeat_demo:0
        DEBUG:insecticide:heartbeat_demo:10
        DEBUG:insecticide:heartbeat_demo:20
    """

    # on pulse, log heartbeat and update last pulse time
    if time() - last_pulse > period:
        insecticide_logger.debug(f"{name}:{index}")
        return time()
    # else change nothing
    return last_pulse