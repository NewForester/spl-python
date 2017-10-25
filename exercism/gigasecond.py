"""
    Python 3 solution to the Exercism 'gigasecond' exercise
"""
from datetime import timedelta

def add_gigasecond(birth_date):
    """
    add a gigasecond to a date in datetime.datetime format
    and return the result in the same format
    """
    return birth_date + timedelta(seconds=10**9)

##
## It seems everyone found this trivial.
## The main difference was the representation of 1E9.
## I think I prefer 1E9 over 10**9
##
