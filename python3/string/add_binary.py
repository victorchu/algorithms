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
  - max(), v.insert(), v.append()
  - a.zfill(n)d
  - reversed(s), v.reverse(), s[::-1]
  - zip(a, b) 
  - itertools.zip_longest(a, b, fillvalue='0')
  - int(str, base=2)
  - bin(n)

REFERENCE:
  - https://leetcode.com/problems/add-binary/ (Easy)
  - https://www.geeksforgeeks.org/python-program-to-add-two-binary-numbers/

"""

import itertools


class Solution:
    def addBinary_v1a(self, a: str, b: str) -> str:
        """Pad zeros. Procss at the character level."""
        # Pad the shorter string with zeros '0'.
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
    
    def addBinary_v1b(self, a: str, b: str) -> str:
        """Pad zeros. Procss at the character level."""
        # Pad the shorter string with zeros '0'.
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)

        carry = 0
        result = ''
        for x, y in zip(a[::-1], b[::-1]):
            s = int(x) + int(y) + carry
            result = ('1' if s % 2 else '0') + result
            carry = s // 2
        if carry > 0:
            result = '1' + result
        return result

    def addBinary_v2a(self, a, b):
        """Use itertools.zip_longest"""
        v = []
        carry = 0
        for x, y in itertools.zip_longest(reversed(a), reversed(b), fillvalue='0'):
            s = int(x) + int(y) + carry
            v.insert(0, str(s % 2))
            carry = s // 2
        if carry:
            v.insert(0, '1')
        return ''.join(v)
    
    def addBinary_v2b(self, a, b):
        """Use itertools.zip_longest"""
        out = []
        carry = 0
        for x, y in itertools.zip_longest(a[::-1], b[::-1], fillvalue='0'):
            s = int(x) + int(y) + carry
            out.append(str(s % 2))
            carry = s // 2
        if carry:
            out.append('1')
        return ''.join(out[::-1])

    def addBinary_v3(self, a: str, b: str) -> str:
        """Use the native binary operation with string/int conversions.
        Time Complexity: O(n).  Space: O(n)
        """
        return bin(int(a, 2) + int(b, 2))[2:]  # skip leading '0b'


def main():
    """Main function"""
    test_data = [
        ('11', '1'),
        ('1010', '1011')
    ]

    sol = Solution()
    for a, b in test_data:
        print(f"\n# Input: a={a}, b={b}")
        print(f"  Output v1a: {sol.addBinary_v1a(a, b)}")
        print(f"  Output v1b: {sol.addBinary_v1b(a, b)}")
        print(f"  Output v2a: {sol.addBinary_v2a(a, b)}")
        print(f"  Output v2b: {sol.addBinary_v2a(a, b)}")
        print(f"  Output v3 : {sol.addBinary_v3(a, b)}")


if __name__ == "__main__":
    main()
