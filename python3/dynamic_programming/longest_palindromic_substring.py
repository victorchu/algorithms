#!/usr/bin/env python3
"""
Given a string s, find the longest palindromic substring in s.

EXAMPLES:

  Input: "babad"
  Output: "bab"
  Note: "aba" is also a valid answer.

  Input: "cbbd"
  Output: "bb"

HINTS:
  - How can we reuse a previously computed palindrome to compute a larger palindrome?
    (This is the key concept in dynamic programming.)
  - If “aba” is a palindrome, is “xabax” and palindrome? Similarly is “xabay” a palindrome?
  - Complexity based hint:
    If we use brute-force and check whether for every start and end position a substring is
    a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks.
    Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.

REFERENCE:
  - https://leetcode.com/problems/longest-palindromic-substring/ (Medium)
  - https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/


"""

from typing import List


class Solution:
    def longestPalindrome_v1(self, s: str) -> str:
        """Use a set to track known palindromes."""

        # Store all known palindromes
        S = set([''])

        def helper(s, i, n, max_len, longest):
            # Termination condition
            if i >= n:
                return longest

            c = s[i]
            if c in S:
                # The char exists in s[0:i].
                for j in range(i):
                    # Search for c
                    if s[j] == c:
                        # Get the string in between and check if it is a known palindrome
                        inner_str = s[j+1:i]
                        if inner_str in S:
                            # Get the new palindrome and check its length
                            p = c + inner_str + c
                            S.add(p)
                            if len(p) > max_len:
                                max_len = len(p)
                                longest = p
            else:
                # This is a new char
                S.add(c)
                if max_len == 0:
                    max_len = 1
                    longest = c

            return helper(s, i+1, n, max_len, longest)

        if not s:
            return ''
        return helper(s, 0, len(s), 0, '')

    def longestPalindrome_v2(self, s: str) -> str:
        """Based on an implementation found on LeetCode.
        The core concept is to expand, from 1 char to 2 chars,
        since a palindrome can have even or odd length.
        """
        start = 0
        end = 0
        ct = 0

        def expand(s, i, j):
            """Expamdn from s[i:j], where j <= i + 1

            Return: (length, new i, new j) the longest palindrome found.
            """

            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return j-i-1, i+1, j-1

        for i in range(len(s)):
            l1, s1, e1 = expand(s, i, i)
            l2, s2, e2 = expand(s, i, i+1)
            if l1 > ct:
                ct, start, end = l1, s1, e1
            if l2 > ct:
                ct, start, end = l2, s2, e2

        return s[(start):(end+1)]


def main():
    test_data = [
        ['babad', 'bab'],
        ['cbbd', 'bb'],
    ]

    sol = Solution()
    for s, ans in test_data:
        print("# Input = {}  (ans = {})".format(s, ans))
        print("  Output = {}".format(sol.longestPalindrome_v1(s)))
        print("  Output = {}".format(sol.longestPalindrome_v2(s)))


if __name__ == "__main__":
    main()
