#!/usr/bin/env python3
"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the 
first non-whitespace character is found. Then, starting from this character,
takes an optional initial plus or minus sign followed by as many numerical 
digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral
number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral
number, or if no such sequence exists because either str is empty or it contains
only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
 - Only the space character ' ' is considered as whitespace character.
 - Assume we are dealing with an environment which could only store integers within the
   32-bit signed integer range: [−2^31,  2^31 − 1].
 - If the numerical value is out of the range of representable values,
   INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.

Examples:
  "42" -> 42
  "    -42" -> -42
  "4193 with words" -> 4193
  "words and 987" -> 0
  "-91283472332" -> -2147483648

Ref:
 - https://www.geeksforgeeks.org/string-to-integer-in-java-parseint/
 - https://leetcode.com/problems/string-to-integer-atoi/

"""
from typing import List
import re


class Solution:

    def myAtoi_v1(self, s: str) -> int:
        """This update the value for each discovered integer.
        """
        # Note: in Python the plain int type is unbounded!
        min_val = -2**31
        max_val = -min_val - 1

        val = 0
        sign = 1
        n = len(s)
        i = 0  # current position

        # Skip empty string
        for j in range(n):
            if s[j] == ' ':
                i += 1
            else:
                break
            
        # Handle sign
        if i < n:
            if s[i] == '+':
                sign = 1
                i += 1
            elif s[i] == '-':
                sign = -1
                i += 1

        # Handle numbers
        for j in range(i, n):
            c = s[j]
            if c.isdigit():
                x = int(c)
                if val == 0:
                    val = sign * x
                elif sign > 0:
                    val = 10 * val + x
                    if val > max_val:
                        val = max_val
                        break
                else:
                    val = 10 * val - x
                    if val < min_val:
                        val = min_val
                        break
            else:
                break
        return val

    def myAtoi_v2(self, s: str) -> int:
        """Use regex and ptyhon int function to convert.
        This relies a lot of existing library...
        This method beats 90% of the python3 submissions in LeetCode.
        Yet, it may not be a good solution for interviews.
        """
        val = 0
        pat = r'^ *([-+]?\d+)'
        m = re.match(pat, s)
        if m:
            val = int(m.group(0))
            min_val = -2147483648
            max_val = 2147483647
            if val < min_val:
                val = min_val
            elif val > max_val:
                val = max_val
        return val


    def myAtoi_v3(self, s: str) -> int:
        """This one doesn't use regex.  Yet it sill use the Python int to convert."""
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        signs = ["-", "+"]
        s = s.strip()
        sign = 1
        num_str = ""
        val = 0
        
        for i, c in enumerate(s):
            if i == 0 and c in signs:
                sign = 1 if c == '+' else -1
            elif c.isnumeric():
                num_str += c
            else:
                break
        
        if num_str != "":
            val = int(num_str) * sign
            if val > INT_MAX:
                val = INT_MAX
            elif val < INT_MIN:
                val = INT_MIN
        return val


# ----------------
#   Main
# ----------------
def main():
    """Main function"""
    test_data = [
        "42",
        "    -42",
        "    +42",
        "4193 with words",
        "words and 987",
        "-91283472332",
        ""
        ]

    sol = Solution()
    for s in test_data:
        print("# Input = '{}'".format(s))
        print("  Output 1 =", sol.myAtoi_v1(s))
        print("  Output 2 =", sol.myAtoi_v2(s))
        print("  Output 3 =", sol.myAtoi_v3(s))


if __name__ == "__main__":
    main()

