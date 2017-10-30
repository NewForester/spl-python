"""
    Python 3 solution to the Exercism 'run length encoding' exercise
"""

def countwhile(predicate, iterable):
    """
    return count of leading characters that satisfy the predicate
    """
    count = 0
    for character in iterable:
        if predicate(character):
            count += 1
        else:
            break
    return count


def decode(string):
    """
    decode run length encoded string and return result
    """
    result = ""

    while string:
        digits = countwhile(lambda c: c.isdigit(), string)
        count = string[:digits]
        letter = string[digits]
        string = string[digits + 1:]

        result += int(count) * letter if digits else letter

    return result


def encode(string):
    """
    encode string as per run length encoding and return result
    """
    result = ""

    while string:
        letter = string[0]
        count = countwhile(lambda c: c == letter, string)
        string = string[count:]

        result += "{0}{1}".format(count, letter) if count > 1 else letter

    return result

##
## The solutions I glanced at showed a lot of variation so this exercise
## clearly gave people a lot of trouble.
##
## None had a common subroutine (e.g. countwhile).  All iterated through
## input one character at a time.
##
## One chap used join and was congratulated on how Pythonesque his code was
## but I don't see that:
##
##    ''.join([out, ('' if num == 1 else str(num)), prev])
##
## is Pythonesque in comparison with:
##
##    ('' if num == 1 else str(num)).join([out, prev])
##
