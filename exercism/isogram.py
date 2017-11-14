"""
    Python 3 solution to the Exercism 'isogram' exercise
"""
def is_isogram(string):
    """
    return true if 'string' is an isogram
    """
    string = string.lower()

    return not any(string.count(c) != 1 for c in string if c.isalpha())

##
## Pylint complained about my use of map + lambda.
## Apparently deprecated in favour of list comprehensions
## but generator expressions, as here, are to be preferred.
##
