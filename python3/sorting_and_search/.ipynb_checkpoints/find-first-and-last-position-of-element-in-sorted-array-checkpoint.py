#!/usr/bin/env python3
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?
 

Example 1:

  Input: nums = [5,7,7,8,8,10], target = 8
  Output: [3,4]
  Example 2:

  Input: nums = [5,7,7,8,8,10], target = 6
  Output: [-1,-1]
  Example 3:

  Input: nums = [], target = 0
  Output: [-1,-1]
 

Constraints:
  0 <= nums.length <= 105
  -109 <= nums[i] <= 109
  nums is a non-decreasing array.
  -109 <= target <= 109

Reference:
  - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""

from typing import List


class Solution:
    def searchRange_v1(self, nums: List[int], target: int) -> List[int]:
        """Linear search. Time complexity=O(n)."""
        ans = [-1, -1]
        for i, x in enumerate(nums):
            if (x == target):
                if ans[0] == -1:
                    ans[0] = i
                ans[1] = i
            elif x > target:
                break

        return ans


    def searchRange_v2(self, nums: List[int], target: int) -> List[int]:
        """Improved recursion and binary search.

        Only use a single array to track positions.
        Also, try to stop the binary search early.

        Complexity = O(log n).  Memory complext = O(1)
        """
        def helper(nums, i0, i1, target, ans):
            # Termination condition
            if i0 == i1:
                if nums[i0] == target:
                    if ans[0] == -1:
                        ans[0] = i0
                        ans[1] = i1
                    else:
                        if i0 < ans[0]:
                            ans[0] = i0
                        if i1 > ans[1]:
                            ans[1] = i1
            else:
                m = (i0 + i1) // 2
                if nums[m] >= target:
                    helper(nums, i0, m, target, ans)
                if nums[m+1] <= target:
                    helper(nums, m+1, i1, target, ans)

        # Validate the inputs
        ans = [-1, -1]
        if nums:
            helper(nums, 0, len(nums)-1, target, ans)
        return ans

def main():
    test_data = [
        [[5,7,7,8,8,10], 8],   # [3, 4]
        [[5,7,7,8,8,10], 6],   # [-1, -1]
        [[5,7,7,8,8,10], 10],  # [5, 5]
        [[], 0], # [-1, -1]
    ]

    sol = Solution()
    for nums, target in test_data:
        print("# Input: nums={}, target={}".format(nums, target))
        print("  - Output v1: {}".format(sol.searchRange_v1(nums, target)))
        print("  - Output v2: {}".format(sol.searchRange_v2(nums, target)))


if __name__ == "__main__":
    main()
