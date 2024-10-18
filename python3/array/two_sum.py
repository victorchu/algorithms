#!/usr/bin/env python3
"""
Given an array of integers, find two
numbers such that they add up to a specific target number.

The function twoSum should return indices (zero based) of the two numbers such that
they add up to the target, where index1 must be less than index2.

"""

import numpy as np
from typing import List
from collections import defaultdict, Counter


class Solution:
    def twoSum_v1(self, nums: List[int], target: int) -> List[int]:
        """Use a nested loop.
        Time complexity O(n^2).  Space complexity = O(1).
        """
        n = len(nums)
        for i in range(0, n-1):
            y = target - nums[i]
            for j in range(i+1, n):
                if y == nums[j]:
                    return [i, j]
        return []

    def twoSum_v2(self, nums: List[int], target: int) -> List[int]:
        """Use a dictionary to speed up the process.
        Time complexity = O(n).  Space complexity = O(n)
        """
        # Search for answer
        seen = dict()
        for i, x in enumerate(nums):
            y = target - x
            if y in seen:
                j = seen[y]
                return [i, j] if i < j else [j, i] 
            seen[x] = i
        return []

    def twoSum_v3(self, nums: List[int], target: int) -> List[int]:
        """Sorted. Use np.argsort() to track the original index after sorting.
        Time complexity = O(n log n + n). Space complexity = O(1).
        """
        idx = np.argsort(nums)  # need to preserve the index
        i, j = 0, len(nums) - 1
        while i < j:
            x = nums[idx[i]] + nums[idx[j]]
            if x == target:
                i1 = idx[i]
                i2 = idx[j]
                return (i1, i2) if i1 < i2 else (i2, i1)
            elif x > target:
                j -= 1
            else:
                i += 1
        return ()


def main():
    test_data = [
        [[2, 11, 15, 7], 9, [0, 3]],
        [[2, 11, 15, 7], 22, [2, 3]],
        [[3, 2, 4], 6, [1, 2]],
        [[3, 3], 6, [0, 1]],
    ]

    ob1 = Solution()
    for nums, target, ans in test_data:
        print(f"# Input: nums={nums}, target={target}, ans={ans}")
        print(f"  - v1 = {ob1.twoSum_v1(nums, target)}")
        print(f"  - v2 = {ob1.twoSum_v2(nums, target)}")
        print(f"  - v3 = {ob1.twoSum_v3(nums, target)}")



if __name__ == "__main__":
    main()
