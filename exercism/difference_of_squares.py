"""
    Python 3 solution to the Exercism 'difference of squares' exercise
"""
def square_of_sum(nn):
    """
    return the square of the sum of the integers [1,nn]
    """
    return ((nn / 2) * (nn + 1)) ** 2


def sum_of_squares(nn):
    """
    return sum of the squares of the integers [1,nn]
    """
    return sum ([X**2 for X in range(1, nn + 1)])


def difference(nn):
    """
    return the difference between the square of sums and the sum of squares
    """
    return square_of_sum(nn) - sum_of_squares(nn)

##
## In sum_of_squares(), the [ and ] mark a list comprehension.  Replace then
## with  parentheses and I'd have a generator expression.  Then there would be
## two pairs of parentheses and I could remove one of them.
##
## List comprehensions were pinched from functional programming languages.
## They supersede map() and filter() and don't use lambda so nice 'n' readable.
## But list comprehensions yield lists so are memory greedy.  Generator
## expressions yield an iterable so restoring the yin and yang of Python.
##
