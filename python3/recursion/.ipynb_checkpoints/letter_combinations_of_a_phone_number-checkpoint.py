#!/usr/bin/env python3
"""
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 0 and 1 do not map to any letters.

   [    / 1]  [abc / 2]  [def / 3]
   [ghi / 4]  [jkl / 5]  [mno / 6]
   [pqrs/ 7]  [tuv / 8]  [wxyz/ 9]
   [    / *]  [    / 0]  [    / #]

EXAMPLES:
  Input: "23"
  Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

REFERENCE:
 - https://leetcode.com/problems/letter-combinations-of-a-phone-number/ (Medium)
 - https://www.geeksforgeeks.org/iterative-letter-combinations-of-a-phone-number/

"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        number_pad = {
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': [],
        }

        def expand(pre, digits, i, n) -> List[str]:
            if i >= n:
                return [pre]

            combinations = list()
            digit = digits[i]
            letters = number_pad[digit]
            i += 1
            for c in letters:
                combinations.extend(expand(pre + c, digits, i, n))
            return combinations

        if digits is None or digits == '':
            return []

        return expand('', digits, 0, len(digits))


def main():
    test_data = [
        "23",
        "1",
        '',
    ]

    sol = Solution()
    for digits in test_data:
        print("# Input = {}".format(digits))
        print("  Output v1 = {}".format(sol.letterCombinations(digits)))


if __name__ == "__main__":
    main()
