#!/usr/bin/env python3
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

  Symbol       Value
  I             1
  V             5
  X             10
  L             50
  C             100
  D             500
  M             1000

For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II.
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

  - I can be placed before V (5) and X (10) to make 4 and 9. 
  - X can be placed before L (50) and C (100) to make 40 and 90. 
  - C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

EXAMPLES:

  3 => "III"
  4 => "IV"
  9 => "IX"
  58 => "LVIII"
  1994 => "MCMXCIV"

Ref:
  - https://leetcode.com/problems/integer-to-roman/ (Medium)

"""


class Solution:

    def intToRoman(self, num: int) -> str:
        """Simple solution."""
        symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '']
        i = 0

        queue = []
        while num:
            # Get a value < 10
            d = num % 10
            if d == 4:
                queue.insert(0, symbols[i] + symbols[i+1])
            elif d == 9:
                queue.insert(0, symbols[i] + symbols[i+2])
            elif d < 4:
                queue.insert(0, symbols[i] * d)
            else:
                queue.insert(0, symbols[i+1] + symbols[i] * (d - 5))
            i += 2
            num = num // 10
        return ''.join(queue)


def main():
    test_data = [
        [3, 'III'],
        [4, 'IV'],
        [8, 'VIII'],
        [9, 'IX'],
        [58, 'LVIII'],
        [1994, 'MCMXCIV'],
    ]

    sol = Solution()
    for num, ans in test_data:
        print("# Input = {}".format(num))
        print("  Output v1 =", sol.intToRoman(num))


if __name__ == "__main__":
    main()
