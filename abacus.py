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


def ramanujan_approx(x):
    """ Ramanujan approximation for factorial. 
        TODO:
            - verify algorithm works
            - should I use 1./30. and 1./6.
            - should I use constant instead of 1/30 and 1/6, like in the fast inverse square root
    """

    fact = (math.sqrt(math.pi) * (x / math.e) ** x) * (((8 * x + 4) * x + 1) * x + 1/30)**(1/6)
    return fact


def inv_sterling_approx(x):
    """ Rearranged Stirling's approximation.
        https://math.stackexchange.com/questions/430167/is-there-an-inverse-to-stirlings-approximation
        TODO:
            - verify algorithm works
            - should I use 1./2.
            - should I use constant instead of 1/2 and math.sqrt(2*math.pi) like in the fast inverse square root
            - should I calculate 1/math.e so I only need to multiply instead of divide
            - finish reading maths paper and implement their findings instead
    """

    log_ = math.log(x / math.sqrt(2*math.pi))
    return log_ / (lambertw(1/math.e * log_).real) - 1/2

    # to find the lowest factorial base that goes into x, first try rounding the output, then rounding the other way
    # OR just round both ways and take the correct one
    # https://core.ac.uk/download/pdf/215383011.pdf
