"""
    Python 3 solution to the Exercism exercise 'say'
"""
def say(number):
    """
    print out a number as words in North American English using short scale terms
    """
    number = int(number)

    if number < 0 or number >= 1e12:
        raise ValueError

    if number == 0:
        return "zero"

    def quotient_and_remainder(number, divisor):
        """
        return the integer quotient and remainder of dividing number by divisor
        """
        divisor = int(divisor)
        remainder = number % divisor
        quotient = (number - remainder) // divisor

        return quotient, remainder

    def say_term(which, terms):
        """
        return a term from a tuple of strings as a list of one element
        """
        return terms[which : which + 1]

    def say_tens(number):
        """
        return a string representing a number less than 100 in English
        """
        terms = []
        quotient, remainder = quotient_and_remainder(number, 10)

        if quotient == 1:
            terms += say_term(remainder,
                ("ten", "eleven", "twelve", "thirteen", "fourteen",
                    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"))

        else:
            if quotient:
                terms += say_term(quotient,
                    ("units", "teens", "twenty", "thirty", "forty",
                        "fifty", "sixty", "seventy", "eighty", "ninety"))

            if remainder:
                terms += say_term(remainder,
                    ("zero", "one", "two", "three", "four",
                        "five", "six", "seven", "eight", "nine"))

        return '-'.join(terms)

    def say_hundreds(number, final=False):
        """
        return a string representing a number less than 1000 in English
        """
        terms = []
        quotient, remainder = quotient_and_remainder(number, 100)

        if quotient:
            terms += [say_tens(quotient), "hundred"]

        if remainder:
            if quotient or final:
                terms += ["and"]

            terms += [say_tens(remainder)]

        return terms

    # now finally convert a number less than a million million

    terms = []

    quotient, remainder = quotient_and_remainder(number, 1e9)
    if quotient:
        terms += say_hundreds(quotient) + ["billion"]

    quotient, remainder = quotient_and_remainder(remainder, 1e6)
    if quotient:
        terms += say_hundreds(quotient) + ["million"]

    quotient, remainder = quotient_and_remainder(remainder, 1e3)
    if quotient:
        terms += say_hundreds(quotient) + ["thousand"]

    if remainder:
        terms += say_hundreds(remainder, terms != [])

    return ' '.join(terms)

##
## A long solution but not challenging exercise.
##
## This uses join very effectively but the refactoring to arrive at this was
## lengthy.
##
## A few students didn't even bother.  Those that did used a similar number of
## lines of code.
##
