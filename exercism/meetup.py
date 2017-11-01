"""
    Python 3 solution to the Exercism 'meetup' exercise
"""

from datetime import date

WEEKDAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
MONTHDAYS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
CARDINALS = ("1st", "2nd", "3rd", "4th", "5th")

def meetup_day(year, month, dow, which):
    """
    return date object representing the day of the meetup
    """
    day = WEEKDAYS.index(dow[:3]) - date(year, month, 1).weekday() + 1

    if which == "last":
        limit = MONTHDAYS[month - 1] - 7

        if is_leap_year(year):
            limit += 1

    elif which == "teenth":
        limit = 12

    else:
        limit = CARDINALS.index(which) * 7

    while day <= limit:
        day += 7

    return date(year, month, day)

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
## Oh boy.  The difficulty of this exercise is rated at 1 on a scale 1-10.
##
## One guy didn't even try.  Another lifted an answer from elsewhere.
## Those that were orginal imported datetime and calendar and usually re.
## Some used arrays of dates.
##
## None had a while loop to make an adjustment.
##
## Only helpful example ... use initial letter of cardinals instead of an index.
##
##     week = int(which[0])
##
