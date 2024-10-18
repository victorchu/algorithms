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
  Input: digits = "23"
  Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

  Input: digits = ""
  Output: []

  Input: digits = "2"
  Output: ["a","b","c"]

Constraints:
  0 <= digits.length <= 4
  digits[i] is a digit in the range ['2', '9'].
  
REFERENCE:
 - https://leetcode.com/problems/letter-combinations-of-a-phone-number/ (Medium)
 - https://www.geeksforgeeks.org/iterative-letter-combinations-of-a-phone-number/

"""

from typing import List

letter_map = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """Recursion"""

        def helper(digits, i, comb: str, results: List[str]):
            if i >= len(digits):
                results.append(comb)
            else:
                chars = letter_map.get(digits[i], '')
                if chars:
                    for c in chars:
                        helper(digits, i+1, comb+c, results)
                else:
                    # May throw exception here
                    # raise Exception(f"Invalid digit {digits[i]}")
                    helper(digits, i+1, comb+'_', results)

        results = []
        helper(digits, 0, '', results)
        return results


def main():
    test_data = [
        "23",
        "243",
        "2",
        '',
    ]

    ob1 = Solution()
    for digits in test_data:
        print(f"# Input = '{digits}'")
        print(f"  Output v1 = {ob1.letterCombinations(digits)}")


if __name__ == "__main__":
    main()
