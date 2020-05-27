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
 - Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

EXAMPLES:

  "III" = 3
  "IV" = 4
  "IX" = 9
  "LVIII" = L:50 + V:5 + III:3 = 58
  "MCMXCIV" = M:1000 + CM:900 + XC:90 + IV:4 = 1994

Ref:
 -  https://leetcode.com/problems/roman-to-integer/ (Easy)

"""


class Solution:
    val_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt_v1(self, s: str) -> int:
        """Look back.

        LeetCode runtime: 44ms, 13.8 MB. (beats 77.6%)
        """
        total_val = 0
        prev_val = 0

        for i, c in enumerate(s):
            curr_val = self.val_map[c]
            total_val += curr_val

            # Check previous values for special cases
            if (prev_val > 0) and (prev_val < curr_val):
                total_val -= 2 * prev_val

            # Move current value and symbol to prev.
            prev_val = curr_val

        return total_val

    def romanToInt_v2(self, s: str) -> int:
        """Use reversed order.

        LeetCode: 36ms, 13.9 MB; beats 96.82%.
        """
        result = 0
        prev = 0

        for c in reversed(s):
            v = self.val_map[c]
            if v >= prev:
                result += v
            else:
                result -= v
            prev = v

        return result


# ----------------
#   Main
# ----------------
def main():
    """Main function"""
    test_data = [
        "III",
        "IV",
        "IX",
        "LVIII",
        "MCMXCIV"
    ]

    sol = Solution()
    for s in test_data:
        print("# Input = '{}'".format(s))
        print("  Output v1 =", sol.romanToInt_v1(s))
        print("  Output v2 =", sol.romanToInt_v2(s))


if __name__ == "__main__":
    main()
