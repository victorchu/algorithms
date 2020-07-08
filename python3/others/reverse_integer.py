#!/usr/bin/env python3
"""
Given a 32-bit signed integer, reverse digits of an integer.

EXAMPLES:

  Input: 123
  Output: 321

  Input: -123
  Output: -321

  Input: 120
  Output: 21

NOTE:
  - Assume we are dealing with an environment which could only store integers
    within the 32-bit signed integer range: [−2^31,  2^31 − 1].
  - For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

REFERENCE:
  - https://leetcode.com/problems/reverse-integer/ (Easy)

"""

from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        a = list(str(x))
        i0 = 1 if a[0] == '-' else 0
        i1 = len(a) - 1
        while (i0 < i1):
            a[i0], a[i1] = a[i1], a[i0]
            i0 += 1
            i1 -= 1

        result = int(''.join(a))
        if (result <= -2**31) or (result >= (2**31-1)):
            result = 0
        return result


def main():
    test_data = [
        123,
        -123,
        120,
    ]

    sol = Solution()
    for x in test_data:
        print("# Input : {}".format(x))
        print("  Output: {}".format(sol.reverse(x)))


if __name__ == "__main__":
    main()
