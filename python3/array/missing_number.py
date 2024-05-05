#!/usr/bin/env python3
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
the one that is missing from the array.

EXAMPLES:

  Input: [3,0,1]
  Output: 2

  Input: [9,6,4,2,3,5,7,0,1]
  Output: 8

  Input: [0]
  Output: 1

Note:
  - Value n itself can be missing.
  - Your algorithm should run in linear runtime complexity.
  - Could you implement it using only constant extra space complexity?

REFERENCE:
  - https://leetcode.com/problems/missing-number/ (Easy)

"""

from typing import List
from collections import Counter


class Solution:
    def missingNumber_v1(self, nums: List[int]) -> int:
        """Use a set"""
        s = set()
        n = nums[0]
        for x in nums:
            s.add(x)
            if x > n:
                n = x

        for i in range(n+1):
            if not i in s:
                return i
        return n + 1

    def missingNumber_v2(self, nums: List[int]) -> int:
        """Use Counter."""
        counter = Counter(nums)
        n = max(counter)
        for i in range(n+1):
            if not i in counter:
                return i
        return n + 1

    def missingNumber_v3(self, nums: List[int]) -> int:
        """Use sum."""
        n = max(nums)
        if len(nums) > n:
            return n + 1

        partial_sum = sum(nums)
        full_sum = sum(range(0, n+1))
        return full_sum - partial_sum


def main():
    test_data = [
        [3, 0, 1],
        [9, 6, 4, 2, 3, 5, 7, 0, 1],
        [0],
    ]

    sol = Solution()
    for nums in test_data:
        print("# Input  : {}".format(nums))
        print("  Output v1: {}".format(sol.missingNumber_v1(nums)))
        print("  Output v2: {}".format(sol.missingNumber_v2(nums)))
        print("  Output v3: {}".format(sol.missingNumber_v3(nums)))


if __name__ == "__main__":
    main()
