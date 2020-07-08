#!/usr/bin/env python3
"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

EXAMPLES:

  Input:  nums=[2, 7, 11, 15], target = 9,
  Output:  [0, 1]   # nums[0] + nums[1]

  Input:  nums=[3, 2, 4], target = 6,
  Output:  [1, 2]

  Input:  nums=[3, 3], target = 6,
  Output:  [0, 1]

HINTS:
  - A really brute force way would be to search for all possible pairs of
    numbers but that would be too slow.  Again, it's best to try out brute force
    solutions for just for completeness.  It is from these brute force solutions
    that you can come up with optimizations.

  - If we fix one number x, does the input array contain (target - x)?
    Can we change our array somehow so that this search becomes faster?

  - Can we use additional space to speed up the search?

REFERENCE:
  - https://leetcode.com/problems/two-sum/ (Easy)

"""

from typing import List
from collections import defaultdict, Counter

class Solution:
    def twoSum_v1(self, nums: List[int], target: int) -> List[int]:
        """Use a nested loop."""
        n = len(nums)
        for i in range(0, n-1):
            y = target - nums[i]
            for j in range(i+1, n):
                if y == nums[j]:
                    return [i, j]
        return []

    def twoSum_v2(self, nums: List[int], target: int) -> List[int]:
        """Use a dictionary to speed up the process.
        This versin is fast.
        """
        # Search for answer
        seen = dict()
        for i, x in enumerate(nums):
            y = target - x
            if y in seen:
                j = seen[y]
                return [j, i]
            seen[x] = i
        return []


def main():
    test_data = [
        [[2, 7, 11, 15], 9],
        [[2, 7, 11, 15], 22],
        [[3, 2, 4], 6],
        [[3, 3], 6],
    ]

    sol = Solution()
    for nums, target in test_data:
        print("# Input: nums={}, target={}".format(nums, target))
        print("  Output v1 = {}".format(sol.twoSum_v1(nums, target)))
        print("  Output v2 = {}".format(sol.twoSum_v2(nums, target)))


if __name__ == "__main__":
    main()
