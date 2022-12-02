""" This is the maths module tool. """

import math
from scipy.special import lambertw


def inv_factorial(x):
    return int(inv_sterling_approx(x))


ONE_HALF = 1/2
INV_SQRT_2PI = 1 / math.sqrt(2*math.pi)
INV_E = 1/math.e
def inv_sterling_approx(x):
    """ Rearranged Stirling's approximation.
        https://math.stackexchange.com/questions/430167/is-there-an-inverse-to-stirlings-approximation
        TODO:
            - verify algorithm works
            - finish reading maths paper and implement their findings instead
    """

    log_ = math.log(x * INV_SQRT_2PI)
    return log_ / (lambertw(INV_E * log_).real) - ONE_HALF

    # to find the lowest factorial base that goes into x, first try rounding the output, then rounding the other way
    # OR just round both ways and take the correct one
    # https://core.ac.uk/download/pdf/215383011.pdf