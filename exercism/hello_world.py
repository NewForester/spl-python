"""
    Python 3 solution to the Exercism exercise 'hello-world'
"""
def hello(name=''):
    """
    return "Hello, World!" - there are no tests with name not empty
    """
    if name:
        return "Hello, {}!".format(name)

    return "Hello, World!"

##
## The first iteration ignored the optional parameter:
## there were no tests that used it.
##
