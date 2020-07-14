#!/usr/bin/env python3
"""
Find the index of a substring.

Return the index of the first occurrence of needle (substring) in haystack (string),
or -1 if needle (substring) is not part of haystack (string).

EXAMPLES:

  Input: haystack = "hello", needle = "ll"
  Output: 2

  Input: haystack = "aaaaa", needle = "bba"
  Output: -1

Clarification:

  - What should we return when needle is an empty string? This is a great question to ask during an interview.
  - For the purpose of this problem, we will return 0 when needle is an empty string.
    This is consistent to C's strstr() and Java's indexOf().

REFERENCE:
  - https://leetcode.com/problems/implement-strstr/ (Easy)

"""

from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        nsub = len(needle)
        nstr = len(haystack)
        ans = -1
        for i in range(nstr - nsub + 1):
            eq = True
            for j in range(nsub):
                if haystack[i+j] != needle[j]:
                    eq = False
                    break
            if eq:
                ans = i
                break
        return ans


def main():
    test_data = [
        ['hello', 'll'],
        ['hello', 'bba'],
    ]

    sol = Solution()
    for haystack, needle in test_data:
        print("# Input  : {}, {}".format(haystack, needle))
        print("  Output : {}".format(sol.strStr(haystack, needle)))


if __name__ == "__main__":
    main()
