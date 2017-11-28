"""
    Python 3 solution to the Exercism 'sum of multiples' exercise

    The routines hcf and lcm used with permission. © NewForester, 2017
"""

from itertools import combinations
from functools import reduce

# ------------------------------

def     hcf(A, B):
    """
    Highest Common Factor by the Euclid method

    Note: math.gcd() is Python 3.5 and later
    """
    if B == 0:
        return abs(A)

    return hcf(B, A % B)

# --------------

def     lcm(A, B):
    """
    Lowest Common Multiple
    """
    return A * B / hcf(A, B)

# ------------------------------

def sum_of_multiples(limit, numbers):
    """
    return the sum of multiples, up to limit, of any divisors from numbers
    """
    # ensure numbers is sorted on ascending order

    numbers = sorted(numbers)

    # eliminate bigger numbers that are a multiple of a smaller number

    numbers = [value for ii, value in enumerate(numbers)
                        if all(value % nn != 0 for nn in numbers[:ii])]

    def sof_multiples(nn):
        """
        sum of multiples of nn up to limit
        """
        cof_multiples = (limit - 1) // nn
        return nn * ((cof_multiples * cof_multiples + cof_multiples) // 2)

    def lcmof_combos(length):
        """
        generator of the lcm of each combination from numbers of size length
        """
        return (reduce(lcm, combo, 1) for combo in combinations(numbers, length))

    def sof_combos(length):
        """
        sum of the sum of multiples of all combinations from numbers of size length
        """
        return sum(sof_multiples(lcm) for lcm in lcmof_combos(length) if lcm <= limit)

    def alternating_sum(values):
        """
        alternating sum of a list of values
        """
        return abs(reduce(lambda x, y: 0 - x + y, values, 0))

    # the sum of the sum of the sum of ...

    return alternating_sum(sof_combos(length) for length in range(1, len(numbers) + 1))

##
## Here is an iteration that takes this exercise a tad more seriously:
##
## - still memory efficient - no sets, no collections
## - looks long but isn't really
## - comments make it look difficult to understand 'cos it probably is
## - with respect to limit, execution time is O(1) :) :)
## - with respect to len(numbers) it is probably around O(n2 ) =:O
##
## I bet it would give any Counter based implementation a run for its money.
##
