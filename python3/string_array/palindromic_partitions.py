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

from typing import List


class Solution:
    def find_palindromic_partitions(self, s: str) -> List[List]:
        """Find and print all palidromes in a strings.

        We can print the partitions when we found them.
        Or, we can return them as a list of lists.

        """
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


        def helper(palindrome_list, s):
            # Use a list of lists to store all results.
            lists = list()
            if len(s) == 0:
                # Reached the end of the string. Print the palindrom list.
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
        return lists


# ----------------
#   Main
# ----------------
def main():
    """Main function"""
    test_samples = ["nitin", "geeks", "aaracecar"]

    sol = Solution()
    for s in test_samples:
        print("# Checking {} ...".format(s))
        partitions = sol.find_palindromic_partitions(s)
        for p in partitions:
            print(" - {}".format(p))


if __name__ == "__main__":
    main()
