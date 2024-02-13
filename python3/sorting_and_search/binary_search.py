#!/usr/bin/env python3
"""
Given a sorted (in ascending order) integer array nums of n elements
and a target value, write a function to search target in nums. If
target exists, then return its index, otherwise return -1.


Examples:

  Input: nums = [-1,0,3,5,9,12], target = 9
  Output: 4
  Explanation: 9 exists in nums and its index is 4


  Input: nums = [-1,0,3,5,9,12], target = 2
  Output: -1
  Explanation: 2 does not exist in nums so return -1
 
Note:
  - You may assume that all elements in nums are unique.
  - n will be in the range [1, 10000].
  - The value of each element in nums will be in the range [-9999, 9999].

Reference:
  - https://leetcode.com/problems/binary-search/ (Easy)
  - https://www.geeksforgeeks.org/binary-search/

"""

from typing import List

class Solution:

    def helper(nums, target, l, r):
        """Search the target in [l, r], where r >= l."""
        # Termination condition
        if l > r:
            return -1
        # Check the middle point.
        m = (l + r) // 2
        z = nums[m]
        if z == target:
            return m
        elif z < target:
            # search the right-hand side.
            return helper(nums, target, m + 1, r)
        else:
            # search the left-hand side.
            return helper(nums, target, l, m - 1)

    # Optionally, check some boundary conditions.
    if not nums or (target < nums[0]) or (target > nums[-1]):
        return -1

    # Search the full array.
    return helper(nums, target, 0, len(nums)-1)

    def search_v2(self, nums: List[int], target: int):
        """Loop.  All of the concepts are the same."""  
        # Optionally check the boundary conditions
        if not nums or (target < nums[0]) or (target > nums[-1]):
            return -1
        
        L, R = 0, len(nums)-1
        while L <= R:
            mid = (L + R) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                L = mid + 1
            else: 
                R = mid - 1
        return -1


def main():
    a = [-1, 0, 3, 5, 9, 12]
    test_data = [
        [a, 9],
        [a, 2],
        [a, -1],
        [[1, 2], 1],
        [[1, 2], 2],
        [[1], 1],
        [[1], 2],        
    ]

    ob1 = Solution()
    for arr, target in test_data:
        print(f"# Input: {arr}, target = {target}")
        print("  - Output v1 = {}".format(ob1.search_v1(arr, target)))
        print("  - Output v2 = {}".format(ob1.search_v2(arr, target)))


if __name__ == '__main__':
    main()


