"""
    Python 3 solution to the Exercism exercise 'leap'
"""
def is_leap_year(year):
    """
    return true if 'year' is a leap year
    """
    if year % 4:
        return False
    if year % 100:
        return True
    if year % 400:
        return False
    return True

##
## This second iteration only added the comments to shut pylint up.
## Most other solutions made this look much more complex with
## multi-levels of if ... else or used of and in conditions.
##
