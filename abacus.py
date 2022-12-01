""" This is the maths module tool. """

import math
from scipy.special import lambertw


def factorial(x):
    DOMAIN_LOWER_BOUND = 3      # find the actual lower bound
    if x < DOMAIN_LOWER_BOUND:
        return math.factorial(x)
    return int(ramanujan_approx(x))


def inv_factorial(x):
    return int(inv_sterling_approx(x))


ONE_SIXTH = 1/6
ONE_THIRTIETH = 1/30
SQRT_PI = math.sqrt(math.pi)
INV_E = 1/math.e
def ramanujan_approx(x):
    """ Ramanujan approximation for factorial. 
        TODO:
            - verify algorithm works
    """

    return (SQRT_PI * (x * INV_E) ** x) * (((8 * x + 4) * x + 1) * x + ONE_THIRTIETH)**ONE_SIXTH


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