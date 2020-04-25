#!/usr/bin/env python3
#
# Reverse a string without affecting special characters.
# Any character that is not a letter ([a-z], [A-Z]) is considered special.
#
# Key functions:
# - str.isalpha()
# - list.append()
# - list.pop()
#
# Ref:
# - https://www.geeksforgeeks.org/reverse-a-string-without-affecting-special-characters/
#
import logging
logger = logging.getLogger(__name__)


def is_normal_char(c):
    """My implementation of str.isalpha() function."""
    return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')


def reverse_simple(s):
    """A simple implementation that needs a stack.

    Complexity O(n). This method needs extra space (a stack).
    It also needs to check each character twice if it is special.

    :param s: The input string
    """
    # Helper spaces
    normal_list = list()
    output_list = list()

    # First iteration: push normal characters to a list
    for c in s:
        if c.isalpha():
            normal_list.append(c)

    # Second iteration: build the output list
    for c in s:
        if c.isalpha():
            output_list.append(normal_list.pop())
        else:
            output_list.append(c)

    # Use join to convert an array to a string.
    retval = "".join(output_list)

    logger.info("reversed string = {}".format(retval))
    return retval


def reverse_smart_v1(s):
    """A smart implementaiton.

    This is a smart reverse method that doesn't take extra space.
    But, string is immutable.  So it is not that simple.
    We still need to convert it to a character array first.

    Complexity: O(n).

    :param s: The input string
    """
    # Convert string to a list, since string is immutable
    a = list(s)

    i = 0            # index from the left-hand side
    j = len(a) - 1   # index from the right-hand side
    while (i < j):
        if not a[i].isalpha():
            i += 1
        elif not a[j].isalpha():
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    retval = "".join(a)
    logger.info("reversed string = {}".format(retval))
    return retval


def reverse_smart_v2(s):
    """A variation of the the smart implementaiton.

    This method uses 3 while loops.  
    Yet logically, this seems to be easier to understand.

    Complexity: O(n).

    :param s: The input string
    """
    # Convert string to a list, since string is immutable
    a = list(s)

    i = 0            # index from the left-hand side
    j = len(a) - 1   # index from the right-hand side

    while i < j:
        # Find the next normal character from the left
        while not a[i].isalpha():
            i += 1
        # Find the next normal character from the right
        while not a[j].isalpha():
            j -= 1
        # Swap normal characters
        if i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    retval = "".join(a)
    logger.info("reversed string = {}".format(retval))
    return retval


def main():
    """Main function"""

    # Initialize logging
    fmt = "%(asctime)s %(levelname)s [%(funcName)s] %(message)s"
    #fmt = "%(asctime)s %(levelname)s [%(module)s:%(funcName)s] %(message)s"
    datefmt = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.DEBUG)

    # Loop through sample strings
    test_samples = ["> yp paHeB!", "(E!V)#@I.L/$y :-> ojnE"]

    for s in test_samples:
        logger.info("## Reversing {} ...".format(s))
        r = reverse_simple(s)
        r = reverse_smart_v1(s)
        r = reverse_smart_v2(s)


if __name__ == "__main__":
    main()
