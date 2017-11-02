"""
    Python 3 solution to the Exercism 'rotational cypher' exercise
"""
def rotate(text, key):
    """
    return text encrypted using key and the rotational cypher method
    """
    def encrypt(char, key):
        """
        encrypt a single character using key and the rotational cypher method
        """
        if char.islower():
            base = 'a'

        elif char.isupper():
            base = 'A'

        else:
            return char

        return chr((ord(char) - ord(base) + key) % 26  + ord(base))

    return ''.join([encrypt(c, key) for c in text])

##
## Quite a variation in solutions.
##
## Mine was not the only solution with a list comprehension and a join.
##
## Almost half constructed a look-up table, the others used ord() and chr().
##
## Three different approaches to look-up table constructions.
##
## One used str.maketrans() and str.translate().  Nice.
##
## The look-up tables were built for each call.  Tut.
##
