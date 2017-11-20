"""
    Python 3 solution to the Exercism 'atbash cypher' exercise
"""
def _makeatbashtable():
    """
    create a character translation table for the atbash cypher
    """
    alpha = "abcdefghijklmnopqrstuvwxyz"

    inplace = list(alpha)
    inplace.reverse()

    return str.maketrans(alpha, ''.join(inplace))

def encode(plain_text):
    """
    encode plain text using the atbash cypher
    """
    atbash = _makeatbashtable()

    ciphered = ''.join([C.lower().translate(atbash) for C in plain_text if C.isalnum()])

    def fives(ciphered):
        """
        split result into chunks of five letters and return them one at a time
        """
        while ciphered:
            yield ciphered[:5]
            ciphered = ciphered[5:]

    return ' '.join(fives(ciphered))


def decode(ciphered_text):
    """
    decode text encoded using the atbash cypher
    """
    atbash = _makeatbashtable()

    plain = ''.join([C.lower().translate(atbash) for C in ciphered_text if not C.isspace()])

    return plain

##
## The encode/decode algorithms are very similar.
##
## I've use str.translate() to convert and factor out into a subroutine the
## construction of the translation table.  It is difficult to justify including
## any more common code.
##
## Lots of variation here.  All the elements of a solution I used are there
## somewhere but so are all the elements I rejected.
##
## Many solutions had two translation tables.  Tut, tut.
##
## At least one (other than mine) had a generator.  Hurray.
##
