#!/usr/bin/env python3
"""
Remove the 'minimum' number of invalid parentheses in order to make the input string valid.
Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

EXAMPLES:

  Input: "()())()"
  Output: ["()()()", "(())()"]

  Input: "(a)())()"
  Output: ["(a)()()", "(a())()"]

  Input: ")("
  Output: [""]

HINTS:
  - Since we don't know which of the brackets can possibly be removed, we try out all the options!

  - We can use recursion to try out all possibilities for the given expression.
    For each of the brackets, we have 2 options:
    1. We keep the bracket and add it to the expression that we are building on the fly during recursion.
    2. OR, we can discard the bracket and move on.  

  - Can we find the number of misplaced parentheses and use it in our solution
    to speed up the recursion?

  - Can we find the number of misplaced parentheses and use it in our solution

  - For every left parenthesis, we should have a corresponding right parenthesis.
    We can make use of two counters which keep track of misplaced left and right parenthesis
    and in one iteration we can find out these two values.  For example,

        0 1 2 3 4 5 6 7
        ( ) ) ) ( ( ( )  
        i = 0, left = 1, right = 0
        i = 1, left = 0, right = 0
        i = 2, left = 0, right = 1
        i = 3, left = 0, right = 2
        i = 4, left = 1, right = 2
        i = 5, left = 2, right = 2
        i = 6, left = 3, right = 2
        i = 7, left = 2, right = 2

    We have 2 misplaced left and 2 misplaced right parentheses.

  - We found out that the exact number of left and right parenthesis that has to be
    removed to get a valid expression. So, e.g. in a 1000 parentheses string, if there are 2
    misplaced left and 2 misplaced right parentheses, after we are done discarding 2 left
    and 2 right parentheses, we will have only one option per remaining character in the
    expression i.e. to consider them. We can't discard them.

REFERENCE:
 - https://leetcode.com/problems/remove-invalid-parentheses/ (Hard)

"""

from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def get_num_misplaced(s):
            left, right = 0, 0
            for c in s:
                if c == '(':
                    left += 1
                elif c == ')':
                    if left > 0:
                        left -= 1
                    else:
                        right += 1
            #print("[DEBUG] misplaced: left={}, right={}".format(left, right))
            return left, right

        def helper(pre, s, rm_left, rm_right, mp_left, mp_right):
            # termination conditions
            if mp_right > 0:
                # This cannot be resolved.
                return []
            elif (rm_left > total_mp_left) or (rm_right > total_mp_right):
                # We have removed more than the allowed quota
                return []
            elif not s:
                # s is empty
                if (mp_left == 0) and (mp_right == 0):
                    return [pre]
                else:
                    return []

            results = []
            c = s[0]
            if c == '(':
                # remove left
                results.extend(
                    helper(pre, s[1:], rm_left + 1, rm_right, mp_left, mp_right))
                # keep left
                results.extend(
                    helper(pre + c, s[1:], rm_left, rm_right, mp_left + 1, mp_right))
            elif c == ')':
                # remove right
                results.extend(
                    helper(pre, s[1:], rm_left, rm_right + 1, mp_left, mp_right))
                # keep right
                if mp_left > 0:
                    results.extend(
                        helper(pre + c, s[1:], rm_left, rm_right, mp_left - 1, mp_right))
                else:
                    results.extend(
                        helper(pre + c, s[1:], rm_left, rm_right, mp_left, mp_right + 1))
            else:
                # keep the non-parenthesis character
                results.extend(
                    helper(pre + c, s[1:], rm_left, rm_right, mp_left, mp_right))

            # Remove duplications
            return list(set(results))

        if not s:
            return ['']

        total_mp_left, total_mp_right = get_num_misplaced(s)
        return helper('', s, 0, 0, 0, 0)


def main():
    test_data = [
        "()())()",
        "(a)())()",
        ")(",
        "",
        "(a)))(((b)",
    ]

    sol = Solution()
    for s in test_data:
        print("# Input = {}".format(s))
        print("  Output = {}".format(sol.removeInvalidParentheses(s)))


if __name__ == "__main__":
    main()
