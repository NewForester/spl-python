"""
    Python 3 solution to the Exercism exercise 'largest-series-product'
"""

from functools import reduce

def largest_product(series, size):
    """
    return the largest product of `size` consecutive digits fron `series`
    """
    if size < 0:
        raise ValueError

    def product(digits):
        """
        return the product of the numbers in a string of `digits`
        """
        return reduce(lambda x, y: x * int(y), digits, 1)

    def generate_slice():
        """
        generate substrings of `series` that are `size` digits long
        """
        ii = len(series) - size
        while ii >= 0:
            yield series[ii : ii + size]
            ii -= 1

    return max(product(slice) for slice in generate_slice())

##
## Seems simple and straight forward enough.
##
## Clever solutions were in one line with max around reduce-with-lambda being
## fed from a list comprehension based on a range.
##
## The variation went as a far as a double for loop with no library functions.
## One solution even used temporary storage.
##
## None separated the product out into a simple, clear, one line routine.
## None used a generate function as I did.
## None worked backwards through the input.
##
## None separated the three simple ideas so they could be present clearly.
##
