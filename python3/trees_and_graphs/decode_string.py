#!/usr/bin/env python3
"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square
brackets is being repeated exactly k times. Note that k is guaranteed to be a
positive integer.

You may assume that the input string is always valid; No extra white spaces, square
brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and
that digits are only for those repeat numbers, k.  For example, there won't be
input like 3a or 2[4].

Examples:

  Input: s = "3[a]2[bc]"
  Output: "aaabcbc"

  Input: s = "3[a2[c]]"
  Output: "accaccacc"

  Input: s = "2[abc]3[cd]ef"
  Output: "abcabccdcdcdef"

  Input: s = "abc3[cd]xyz"
  Output: "abccdcdcdxyz"

Constraints:

 - 1 <= s.length <= 30
 - s consists of lowercase English letters, digits, and square brackets '[]'.
 - s is guaranteed to be a valid input.
 - All the integers in s are in the range [1, 300].

Reference:
  - https://leetcode.com/problems/decode-string/ (Medium)

"""

from typing import List


class Solution:
    def decodeString_v1(self, s: str) -> str:
        """Use recurssion.  Similar to a DFS traversal."""

        def decode(s, i):
            """Decode string s from position i.
            :param s: string to be decoded until ']' or end of the string.
            :param i: start position.
            :return: decoded string and the final position.
            """
            ans, k = '', ''
            while i < len(s):
                c = s[i]
                if c.isdigit():
                    k += c
                elif c == '[':
                    encoded_string, i = decode(s, i+1)
                    ans += int(k) * encoded_string
                    k = ''
                elif c == ']':
                    return ans, i
                else:
                    ans += c
                i += 1
            return ans, i
        ans, _ = decode(s, 0)
        return ans

    def decodeString_v2(self, s: str) -> str:
        """Use stack and loop.
        Note that using a stack is almost identical to using recurssion.
        """
        stack = list()

        a, k = [''] * 2      # character & number buffers
        for c in s:
            if c.isalpha():
                a += c
            elif c.isdigit():
                k += c
            elif c == '[':
                stack.append([a, int(k)])
                a, k = '', ''   # clear buffers
            elif c == ']':
                prev_a, prev_k = stack.pop()
                a = prev_a + prev_k * a
            else:
                raise Exception(f"Unexpected character {c}")
        return a


def main():
    test_data = [
        "3[a]2[bc]",
        "3[a2[c]]",
        "2[abc]3[cd]ef",
        "abc3[cd]xyz",
    ]

    sol = Solution()
    for s in test_data:
        print("# Input: {}".format(s))
        print("  - Output v1: {}".format(sol.decodeString_v1(s)))
        print("  - Output v2: {}".format(sol.decodeString_v2(s)))


if __name__ == "__main__":
    main()
