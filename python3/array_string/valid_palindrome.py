#!/usr/bin/env python3
"""
QUESTION:

Given a string, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

EXAMPLES:

Input: "A man, a plan, a canal: Panama"
Output: true

Input: "race a car"
Output: false

TECHNOLOGIES:

  - str.isalnum()
  - str.tolower()

"""

from typing import List


class Solution:
    def isPalindrome_v1(self, s: str) -> bool:
        """Search for valid characters from both sides and then compare.
        Also use has_x and has_y to check which side we are searching.
        """
        i = 0
        j = len(s) - 1 if s else 0
        retval = True

        has_x = has_y = False
        while (i < j):
            # Get the next letter from the head
            if not has_x:
                x = s[i].lower()
                if x.isalnum():
                    has_x = True
                else:
                    i += 1
                    continue

            # Get the next letter from the tail
            if not has_y:
                y = s[j].lower()
                if y.isalnum():
                    has_y = True
                else:
                    j -= 1
                    continue

            # Compare x & y
            if has_x and has_y and (x != y):
                retval = False
                break
            else:
                has_x = has_y = False
                i += 1
                j -= 1

        return retval

    def isPalindrome_v2(self, s: str) -> bool:
        """Pre-process the string.
        Speed = O(n). Space = O(n)"""
        a = [c for c in s.lower() if c.isalnum()]
        n = len(a)
        i, j = 0, n - 1
        while i < j:
            if a[i] != a[j]:
                return False
            i += 1
            j -= 1
        return True    
    
    
def main():
    """Main function"""
    test_data = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "a.",
        "",
        " ",
        "0P"
    ]

    sol = Solution()
    for s in test_data:
        print("\n# Input: '{}':".format(s))
        print("  Output: {}".format(sol.isPalindrome_v1(s)))
        print("  Output: {}".format(sol.isPalindrome_v2(s)))


if __name__ == "__main__":
    main()
