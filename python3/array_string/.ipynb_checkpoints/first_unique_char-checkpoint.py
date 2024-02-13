#!/usr/bin/env python3
"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

EXAMPLES:

  s = "leetcode"
  return 0.

  s = "loveleetcode",
  return 2.

REFERENCE:
  - https://leetcode.com/problems/first-unique-character-in-a-string/ (Easy)

"""

from typing import List
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        counter = Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        else:
            return -1


def main():
    test_data = [
        'leetcode',
        'loveleetcode',
        'aabbcc',
        '',
    ]

    sol = Solution()
    for s in test_data:
        print("# Input  = {}".format(s))
        print("  Output = {}".format(sol.firstUniqChar(s)))


if __name__ == "__main__":
    main()
