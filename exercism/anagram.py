"""
    Python 3 solution to the Exercism 'anagram' exercise
"""
def detect_anagrams(word, candidates):
    """
    return the list of candidates that are anagrams of word
    """
    (lower, length) = (word.lower(), len(word))

    slower = sorted(lower)

    def check_anagram(wanabee):
        """
        check lower case candidate
        """
        if len(wanabee) != length:
            return False
        if wanabee == lower:
            return False
        return sorted(wanabee) == slower

    return [C for C in candidates if check_anagram(C.lower())]

##
## I used sorted for comparison purposes.  Is there a better way ?
##
## Not among the exercises I saw.  None checked the length, several sorted
## the word for every candidate.  I think all would take longer to run.
##
