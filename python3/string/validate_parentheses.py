#!/usr/bin/env python3
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

  - Open brackets must be closed by the same type of brackets.
  - Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

EXAMPLES:

    Input: "()"
    Output: true

    Input: "()[]{}"
    Output: true

    Input: "(]"
    Output: false

    Input: "([)]"
    Output: false

    Input: "{[]}"
    Output: true

REFERENCE:
  - https://leetcode.com/problems/valid-parentheses/ (Easy)

"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_set = (['(', '{', '['])
        parenthesis_map = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in open_set:
                stack.append(c)
            elif c in parenthesis_map:
                c_open = parenthesis_map[c]
                if stack and c_open == stack.pop():
                    continue
                else:
                    return False
        return True if not stack else False


def main():
    test_data = [
        '()',
        '()[]{}',
        '(]',
        '(])]',
        ')(',
        '({[]})',
        'x(a{b[c]d}e)f',
    ]

    sol = Solution()
    for s in test_data:
        print("# Input  : {}".format(s))
        print("  Output : {}".format(sol.isValid(s)))


if __name__ == "__main__":
    main()
