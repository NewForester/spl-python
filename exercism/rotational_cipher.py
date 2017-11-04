"""
    Python 3 solution to the Exercism 'rotational cypher' exercise
"""

LOWER_ALPHA = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rotate(text, key):
    """
    return text encrypted using key and the rotational cypher method
    """
    key = key % 26

    lower = LOWER_ALPHA[key:] + LOWER_ALPHA[:key]
    upper = UPPER_ALPHA[key:] + UPPER_ALPHA[:key]

    table = str.maketrans(LOWER_ALPHA + UPPER_ALPHA, lower + upper)

    return text.translate(table)

##
## New iteration that uses the translate table support of the string type.
## Someone liked this.  So do I:  straight line code.
##
