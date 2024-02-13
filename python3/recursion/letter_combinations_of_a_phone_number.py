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

letter_map = {
    '0': '',
    '1': '',
    '2': 'BCD',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '*': '',
    '#': '',
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def helper(digits: str, i:int, prefix: str, results: List):
            if i >= len(digits):
                results.append(prefix)
                return
            for c in letter_map[digits[i]]:
                helper(digits, i+1, prefix + c, results)                            

        results = []
        helper(digits, 0, "", results)
        return results


def main():
    test_data = [
        "23",
        "1",
        '',
    ]

    ob1 = Solution()
    for digits in test_data:
        print(f"# Input = '{digits}'")
        print(f"  Output v1 = {ob1.letterCombinations(digits)}")


if __name__ == "__main__":
    main()
