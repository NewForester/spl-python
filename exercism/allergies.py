"""
    Python 3 solution to the Exercism 'allergies' exercise
"""
ALLERGIES = (
    'eggs',             # (1)
    'peanuts',          # (2)
    'shellfish',        # (4)
    'strawberries',     # (8)
    'tomatoes',         # (16)
    'chocolate',        # (32)
    'pollen',           # (64)
    'cats',             # (128)
)

class Allergies(object):
    """
    allergy test results
    """
    def __init__(self, score):
        self._score = score

    def is_allergic_to(self, item):
        """
        return true if the named allergy is among this object's allergies
        """
        return 1 << ALLERGIES.index(item) & self._score != 0

    @property
    def lst(self):
        """
        return this object's allergies as a list of names
        """
        return [item for item in ALLERGIES if self.is_allergic_to(item)]

##
## Several other solutions had one line methods but mine was the only one to
## express one in terms of the other.
##
## Almoat all used a dictionary but I decided it was not worth the effort.
## Each solution used the dictionary differently.
##
