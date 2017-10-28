"""
    Python 3 solution to the Exercism 'bob' exercise
"""
def hey(phrase):
    """
    Bob is a lackadaisical teenager with limited conversational skills
    """
    phrase = phrase.strip()

    if phrase == "":
        return "Fine. Be that way!"

    if phrase.upper() == phrase and phrase.lower() != phrase:
        return "Whoa, chill out!"

    if phrase.endswith("?"):
        return "Sure."

    return "Whatever."

##
## This looks so much neater in Python than Erlang or Haskell.
## Pretty much all solutions followed the same pattern although some
## people did not know about strip() and none used endswith().
## One use nested ternary if ... else.  Ugly.
##
