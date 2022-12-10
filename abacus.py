""" This is the maths tool module. """

import math
from math import sqrt
from scipy.special import lambertw

from timeit import timeit


# ---------- FIBONACCI ---------- #
FIBONACCI_PHI = (1+sqrt(5)) / 2
FIBONACCI_PSI = 1 - FIBONACCI_PHI       # (1-sqrt(5)) / 2
INV_SQRT_5 = 1 / sqrt(5)
def fibonacci(n):
    """ Return the nth Fibonacci number.
        For an explanation, see https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression
    """

    return int((FIBONACCI_PHI**n - FIBONACCI_PSI**n) * INV_SQRT_5)


# ---------- FACTORIAL ---------- #
def inv_factorial(x: float) -> float:
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


# ---------- HYPEROPERATIONS ---------- #
def super_sqrt(radicand: int) -> float:
    """ Return the super square-root of the argument (reverse of 2nd tetration).
        For an explanation, see https://en.wikipedia.org/wiki/Tetration#Square_super-root.
    """

    log_radicand = math.log(radicand)
    return int(log_radicand / lambertw(log_radicand).real)      # if returned value is 1 less than actual value, use round() instead of int()


# def main():
#     x = 23
#     repetitions = 10000000
#     func1 = fibonacci1
#     func2 = fibonacci2
#     func3 = fibonacci3
#     func4 = fibonacci4
#     time1 = timeit(lambda: func1(x), number=repetitions)
#     time2 = timeit(lambda: func2(x), number=repetitions)
#     time3 = timeit(lambda: func3(x), number=repetitions)
#     time4 = timeit(lambda: func4(x), number=repetitions)
#     print(time1)
#     print(time2)
#     print(time3)
#     print(time4)
#     print(func1(x))
#     print(func2(x))
#     print(func3(x))
#     print(func4(x))


# if __name__ == "__main__":
    # main()
