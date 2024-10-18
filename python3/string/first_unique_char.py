#!/usr/bin/env python3
"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
May optionally return the unique character as well

EXAMPLES:

  s = "leetcode"
  return 0, 'l'

  s = "loveleetcode",
  return 2, 'v'

  s = "aabbcc"
  return -1, ''

  s = ""
  return -1, ''

REFERENCE:
  - https://leetcode.com/problems/first-unique-character-in-a-string/ (Easy)

"""

from collections import Counter, defaultdict
from typing import Tuple


class Solution:
    def firstUniqCha_1(self, s: str) -> Tuple[int, str]:
        """ Use a Counter to counte the number of occurance.
        Time Complexity: O(n), Space Complexity: O(1)
        """
        c = Counter(s)
        for i, x in enumerate(s):
            if c[x] == 1:
                return i, x
        return -1, ''
    
    def firstUniqCha_2(self, s: str) -> Tuple[int, str]:
        """Use defaultdict to count"""
        c = defaultdict(int)
        for x in s:
            c[x] += 1
        for i, x in enumerate(s):
            if c[x] == 1:
                return i, x
        return -1, ''


def main():
    test_data = [
        'leetcode',
        'loveleetcode',
        'aabbcc',
        '',
    ]

    ob1 = Solution()
    for s in test_data:
        print(f"# Input ='{s}'")
        print(f"  output 1 = {ob1.firstUniqCha_1(s)}")
        print(f"  output 2 = {ob1.firstUniqCha_2(s)}")


if __name__ == "__main__":
    main()
