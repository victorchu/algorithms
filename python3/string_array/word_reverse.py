#!/usr/bin/env python3
"""
Reverse words in a string.
There are many possible ways, with different costs on time & space.

Examples:
  Input:  "the sky is blue"
  Output: "blue is sky the"

Key functions:

Ref:
  - https://www.programcreek.com/2014/05/leetcode-reverse-words-in-a-string-ii-java/ 
"""


import re


class Solution:
    def reverse_v1(self, s):
        """Convert to a word list first.
        Time is O(n).  Space is O(n)
        """
        a = re.split(r'\s+', s)
        i = 0
        j = len(a) - 1
        while (i < j):
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

        retval = ' '.join(a)
        return retval


    def reverse_v2(self, s):
        """Word reverse followed by a sentence reverse.
        Time is O(n).  Space is O(1).
        """
        def reverse(a, i, j):
            while (i < j):
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        # Convert string to an list
        a = list(s)

        # Reverse individual words, delimited by spaces.
        i = 0
        n = len(a)
        while i < n:
            for j in range(i+1, n):
                # Found a space
                if a[j] == ' ':
                    reverse(a, i, j-1)
                    i = j + 1
                    break
                # Reached end of the sentence
                elif j == n-1:
                    reverse(a, i, j)
                    i = j + 1

        # Reverse sentence
        reverse(a, 0, len(a)-1)

        # Convert a list back to a string
        return ''.join(a)



def main():
    """Main function"""
    test_data = ["be to not or be To",
                 "forever is Life", "Is That All is Love"]
    sol = Solution()
    for s in test_data:
        print("\n# Input = '{}':".format(s))
        print(" v1> '{}'".format(sol.reverse_v1(s)))
        print(" v2> '{}'".format(sol.reverse_v2(s)))


if __name__ == "__main__":
    main()
