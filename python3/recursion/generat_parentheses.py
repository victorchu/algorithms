#!/usr/bin/env python3
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

  [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
  ]

REFERENCE:
  - https://leetcode.com/problems/generate-parentheses/ (Medium)

"""

from typing import List


class Solution:
    def generateParenthesis_v1(self, n: int) -> List[str]:
        """Helper return a list. """
        def helper(pre, l, r) -> List[str]:
            """Helper function
            :param l: Number of left parenthesis that can be used.
            :param r: Number of right parenthesis that can be used.
            """
            # Termination condition
            if l == 0 and r == 0:
                return [pre]

            # Explore left and right
            output = []
            if l > 0:
                output.extend(helper(pre + '(', l-1, r+1))
            if r > 0:
                output.extend(helper(pre + ')', l, r-1))
            return output

        return helper('', n, 0)

    def generateParenthesis_v2(self, n: int) -> List[str]:
        """Pass the output list to the helper."""
        def helper(pre, l, r, output) -> List[str]:
            if l == 0 and r == 0:
                output.append(pre)
            if l > 0:
                helper(pre + '(', l-1, r+1, output)
            if r > 0:
                helper(pre + ')', l, r-1, output)

        output = []
        helper('', n, 0, output)
        return output


def main():
    test_data = [
        3,
        1,
        5,
    ]

    sol = Solution()
    for n in test_data:
        print("# Input  : {}".format(n))
        print("  Output v1 : {}".format(sol.generateParenthesis_v1(n)))
        print("  Output v2 : {}".format(sol.generateParenthesis_v2(n)))


if __name__ == "__main__":
    main()
