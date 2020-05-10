#!/usr/bin/env python3
"""
Given a string, find all possible palindromic partitions of given string.

Examples:
  Input: nitin
  Output: n i t i n
          n iti n
          nitin

  Input:  geeks
  Output: g e e k s
          g ee k s

Key functions:
  str[i:j] -- substring

Ref:
  - https://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/

"""

import logging
logger = logging.getLogger(__name__)


def is_palindrome(s):
    """Check if the specified string is a palindrome"""
    retval = True
    i = 0
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            retval = False
            break
    return retval


def find_palindromic_partitions(s):
    """Find and print all palidromes in a strings.

    We can print the partitions when we found them.
    Or, we can return them as a list of lists.

    """
    def helper(palindrome_list, s):
        # Use a list of lists to store all results.
        lists = list()
        if len(s) == 0:
            # Reached the end of the string. Print the palindrom list.
            #logger.debug("FOUND {}".format(palindrome_list))
            #lists += [palindrome_list]
            lists.append(palindrome_list)
        else:
            for i in range(1, len(s)+1):
                # Iterate through all sub-strings starting from the beginning
                entry = s[0:i]
                # If it is an palindrome, use recursion to handle the rest of the string
                if is_palindrome(entry):
                    new_list = palindrome_list + [entry]
                    lists += helper(new_list, s[i:])
        return lists

    # Use the helper function to handle all of the work.
    # Start with an empty list
    lists = helper(list(), s)
    for l in lists:
        logger.info("> {}".format(l))


# ----------------
#  Test Functions
# ----------------
def test_is_palindrome():
    """Test is_palindrome()"""
    test_samples = ["n", "nx", "nin", "nitin", "nice"]
    for s in test_samples:
        r = is_palindrome(s)
        logger.info("is_palindrom({}) = {}".format(s, r))


def test_print_palindromic_partitions():
    """Test print_palindromic_partitions() """

    # Loop through sample strings
    test_samples = ["nitin", "geeks", "aaracecar"]

    for s in test_samples:
        logger.info("## Checking {} ...".format(s))
        find_palindromic_partitions(s)


# ----------------
#   Main
# ----------------
def init_logging():
    fmt = "%(asctime)s %(levelname)s [%(funcName)s] %(message)s"
    datefmt = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.DEBUG)


def main():
    """Main function"""
    init_logging()
    # test_is_palindrome()
    test_print_palindromic_partitions()


if __name__ == "__main__":
    main()
