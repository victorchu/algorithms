#!/usr/bin/env python3
"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

  Input: a = "11", b = "1"
  Output: "100"

Example 2:

  Input: a = "1010", b = "1011"
  Output: "10101"

Technologies:
  - reversed()
  - zip(a, b) 
  - itertools.zip_longest(a, b, fillvalue='0')
  - int(str, base=2)
  - bin(n)

REFERENCE:
  - https://leetcode.com/problems/add-binary/ (Easy)

"""

import itertools


class Solution:
    def addBinary_v1(self, a: str, b: str) -> str:
        """Procss at the character level."""
        # Pad the shorter string with zeros.
        n = len(a)
        m = len(b)
        if n > m:
            b = '0' * (n - m) + b
        elif n < m:
            a = '0' * (m - n) + a

        carry = 0
        out = list()
        for x, y in zip(reversed(a), reversed(b)):
            s = int(x) + int(y) + carry
            out.insert(0, str(s % 2))
            carry = s // 2

        if carry > 0:
            out.insert(0, '1')
        return ''.join(out)

    def addBinary_v2(self, a: str, b: str) -> str:
        """Use itertools.zip_longest"""
        carry = 0
        out = list()
        for x, y in itertools.zip_longest(reversed(a), reversed(b), fillvalue='0'):
            s = int(x) + int(y) + carry
            out.insert(0, str(s % 2))
            carry = s // 2

        if carry > 0:
            out.insert(0, '1')
        return ''.join(out)

    def addBinary_v3(self, a: str, b: str) -> str:
        """Convert to integers."""
        x = int(a, 2)
        y = int(b, 2)
        z = x + y
        return bin(z)[2:]


def main():
    """Main function"""
    test_data = [
        ('11', '1'),
        ('1010', '1011')
    ]

    sol = Solution()
    for a, b in test_data:
        print("\n# Input: a={}, b={}".format(a, b))
        print("  Output v1: {}".format(sol.addBinary_v1(a, b)))
        print("  Output v2: {}".format(sol.addBinary_v2(a, b)))
        print("  Output v3: {}".format(sol.addBinary_v3(a, b)))


if __name__ == "__main__":
    main()
