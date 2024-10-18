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
        """Linear search. 
        
        Time complexity=O(n). Space: O(1)
        """
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
        """Binary search.

        Time Complexity = O(log n).  
        Space Complexity = O(log n) -- call stacks.
        """
        def helper(nums: List[int], target: int, L: int, R: int, ans: List[int]):
            if L > R:
                return
            
            # Get middle value
            m = (L + R) // 2
            val = nums[m]

            # update the answer
            if val == target:
                ans[0] = m if (ans[0] == -1) else min(ans[0], m)
                ans[1] = max(ans[1], m)

            # Continue to search regardless of the match status
            if val >= target:
                helper(nums, target, L, m-1, ans)
            if val <= target:
                helper(nums, target, m+1, R, ans)

        ans = [-1, -1]
        helper(nums, target, 0, len(nums)-1, ans)
        return ans


def main():
    test_data = [
        [[5,7,7,8,8,10], 8, [3,4]],
        [[5,7,7,8,8,10], 6, [-1,-1]],
        [[5,7,7,8,8,10], 10, [5,5]],
        [[], 0, [-1,-1]],
    ]

    ob1 = Solution()
    for nums, target, ans in test_data:
        print(f"\n# Input: nums={nums}, target={target}, ans={ans}")
        print(f"  - Output v1: {ob1.searchRange_v1(nums, target)}")
        print(f"  - Output v2: {ob1.searchRange_v2(nums, target)}")


if __name__ == "__main__":
    main()
