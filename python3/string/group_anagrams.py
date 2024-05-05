#!/usr/bin/env python3
"""
Given an array of strings, group anagrams together.

EXAMPLES:

  Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
  Output:
  [
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
  ]

Note:
  - All inputs will be in lowercase.
  - The order of your output does not matter.

REFERENCE:
  - https://leetcode.com/problems/group-anagrams/ (Medium)
  - https://www.geeksforgeeks.org/python-program-to-sort-a-string/

"""

from typing import List
from collections import defaultdict
from functools import reduce


class Solution:

    def groupAnagrams_v1(self, strs: List[str]) -> List[List[str]]:
        """Use join + sorted to sort the string."""
        # Add the strings into a dictionary, using sorted value as the key
        d = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            d[key].append(s)

        # Return the values as a list of lists
        return list(d.values())

    def groupAnagrams_v2(self, strs: List[str]) -> List[List[str]]:
        """Use reduce + sorted to sort the string."""
        # Add the strings into a dictionary, using sorted value as the key
        d = defaultdict(list)
        for s in strs:
            key = reduce(lambda x, y: x + y, sorted(s))
            d[key].append(s)

        # Return the values as a list of lists
        return [v for v in d.values()]


def main():
    test_data = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
    ]

    sol = Solution()
    for strs in test_data:
        print("# Input  : {}".format(strs))
        print("  Output v1: {}".format(sol.groupAnagrams_v1(strs)))
        print("  Output v2: {}".format(sol.groupAnagrams_v2(strs)))


if __name__ == "__main__":
    main()
