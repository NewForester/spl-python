<!-- spl-python by NewForester:  programming examples in Python 3 -->

# Script Programming Language - Python

Programming examples written in [Python 3](https://en.wikipedia.org/wiki/Python3).

The examples are implemented as scripts and so can be run directly from the shell:

```bash
    $ ./hello.py NewForester "Big Bad World"
    Hello NewForester
    Hello Big Bad World
```

Each example comes with a [pyunit](https://docs.python.org/3/library/unittest.html) unit test module.

```bash
    $ python3 TestHello.py              # run unit test for hello.py
```

All modules are documented for use with [pydoc](https://docs.python.org/3/library/pydoc.html).

```bash
    $ pydoc3 hello                      # print documentation for hello.py
    $ pydoc3 TestHello                  # print documentation for TestHello.py
```

All modules have been put through [pylint](https://www.pylint.org/) with default configuration.

```bash
    $ pylint hello                      # check hello.py for code smells
    $ pylint TestHello                  # check TestHello.py for code smells
```

---

Module          | Contents
------          | --------
hello           | a simple routine inspired by the K&R Hello World program
fib_exponential | a recursive Fibonacci function with exponential time complexity
fib_linear      | a recursive Fibonacci function with linear time complexity

---

Caveat: on my system a gremlin lurks.  His activity means that:

```bash
    $ pydoc3 ./hello.py
```

does not do as it should:  what is displayed ignores the documentation inside "./hello.py".

The workaround is to delete the Python 3 module cache and do it again as suggested above:

```bash
    $ rm -f __pycache__
    $ pydoc3 hello
```

---

*spl-python* by NewForester licensed under the MIT Licence.

<!-- EOF -->
