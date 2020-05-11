#!/usr/bin/env python3
"""
TASK:

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal
numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing
16 bits. The groups are separated by colons (":"). For example, the address
2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among
four hexadecimal digits and some low-case characters in the address to upper-case ones, so
2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper
cases).

However, we don't replace a consecutive group of zero value with a single empty group using two
consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an
invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address
02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

EXAMPLES:
  Input: "172.16.254.1"
  Output: "IPv4"

  Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"
  Output: "IPv6"

  Input: "256.256.256.256"
  Output: "Neither"

TECHNOLOGIES:

  - isdigit()

REFERENCE:
  - https://docs.python.org/2/library/re.html
"""

import re
from typing import List


class Solution:
    def validIPAddress_v1(self, IP: str) -> str:
        """
        :@return: {'IPv4', 'IPv6', 'Neither'}
        """
        def validIPv4(IP):
            is_valid = True
            elements = IP.split('.')
            if len(elements) != 4:
                is_valid = False
            else:
                p = re.compile('^[1-9]\d{0,2}$')
                for e in elements:
                    if not ((e == '0') or (p.match(e) and int(e) < 256)):
                        is_valid = False
                        break
            return is_valid

        def validIPv6(IP):
            is_valid = True
            elements = IP.split(':')
            if len(elements) != 8:
                is_valid = False
            else:
                p = re.compile('^[0-9a-fA-F]{1,4}$')
                for e in elements:
                    if not p.match(e):
                        is_valid = False
                        break
            return is_valid

        if '.' in IP and validIPv4(IP):
            return 'IPv4'
        if ':' in IP and validIPv6(IP):
            return 'IPv6'
        return 'Neither'

        

def main():
    test_data = [
        "172.16.254.1",
        "255.255.255.255",
        "10.0.0.1",
        "256.256.256.256",
        "072.16.254.1",
        "172.16.254",
        "172.16.254.abc",
        "2001:0db8:85a3:0:0:8A2E:0370:7334",
        "0db8:85a3:0:0:8A2E:0370:7334",
        "2001::85a3:0:0:8A2E:0370:7334",
        "02001:0db8:85a3:0000:0000:8a2e:0370:7334",
    ]

    sol = Solution()
    for IP in test_data:
        print("# Input: '{}':".format(IP))
        print("  v1> {}".format(sol.validIPAddress_v1(IP)))
        print("  v2> {}".format(sol.validIPAddress_v2(IP)))


if __name__ == "__main__":
    main()
