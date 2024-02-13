#!/usr/bin/env python3
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

EXAMPLES:

  Input: nums = [4,5,6,7,0,1,2], target = 0
  Output: 4

  Input: nums = [4,5,6,7,0,1,2], target = 3
  Output: -1

REFERENCE:
  - https://leetcode.com/problems/search-in-rotated-sorted-array/ (Medium)

"""

from typing import List


class Solution:
    def search_v1(self, nums: List[int], target: int) -> int:
        """Binary search with special logic. This is quite complicated."""

        def helper(nums, target, left, right) -> int:
    
            if left > right:
                return -1
            mid = (left + right) // 2
            x = nums[mid]
            # print(f"[DEBUG] min = {x}, target={target}")
            if x == target:
                return mid
            elif nums[right] > nums[left]:
                # In a normal array
                if x > target:
                    return helper(nums, target, left, mid-1)  # search left
                else:
                    return helper(nums, target, mid+1, right) # search right
            else:
                # In a rotated array. There are six different conditions.
                # Use an example to analyze (e.g. 5 6 7 8 9 0 1 2 3 4)
                if (x > target):
                    if (nums[right] > x) or (nums[left] <= target):
                        return helper(nums, target, left, mid-1)  # search left
                    else:
                        return helper(nums, target, mid+1, right) # search right
                else:
                    if (nums[right] >= x) or (nums[left] > nums[right]):
                        return helper(nums, target, mid+1, right) # search right
                    else:
                        return helper(nums, target, left, mid-1)  # search left            
    
        return helper(nums, target, 0, len(nums) - 1)

    def search_v2(self, nums: List[int], target: int) -> int:
        """Locate the pivot location (the min of the array).

        This may be a little bit slower (two binary searches), yet
        the logic is less mind-boggling.
        Compute: O(log N).
        """
        def get_pivot_index(nums, l, r) -> int:
            if l > r:
                return -1
            if nums[l] <= nums[r]:
                return l            
            m = (l + r) // 2
            if nums[m] < nums[r]:
                return get_pivot_index(nums, l, m)
            else:
                return get_pivot_index(nums, m + 1, r)
            
        def binary_search(nums, target, l, r) -> int:
            if l > r:
                return -1
            m = (l + r) // 2
            x = nums[m]
            if x == target:
                return m
            elif x > target:
                return binary_search(nums, target, l, m - 1)  # searc left
            else:
                return binary_search(nums, target, m + 1, r)  # searc right

        if not nums:
            return -1
        n = len(nums)
        pivot_idx = get_pivot_index(nums, 0, n - 1)
        if target <= nums[-1]:
            return binary_search(nums, target, pivot_idx, n - 1)
        elif target >= nums[0]:
            return binary_search(nums, target, 0, pivot_idx - 1)
        else:
            return -1


def main():
    test_data = [
        [[2, 3, 4, 5, 6, 7, 8, 9, 1], 3, 1],
        [[0, 1, 2, 4, 5, 6, 7], 6, 5],
        [[4, 5, 6, 7, 0, 1, 2], 6, 2],
        [[6, 8, 10, 0, 2, 4], 0, 3],
        [[6, 8, 10, 0, 2, 4], 8, 1],
        [[6, 8, 10, 0, 2, 4], 9, -1],
        [[6, 8, 10, 0, 2, 4], 12, -1],
        [[6, 8, 10, 0, 2, 4], 5, -1],
        [[1], 1, 0],
        [[], 5, -1],

    ]

    ob1 = Solution()
    for nums, target, ans in test_data:
        print(f"# Input  : {nums}, target={target} (ans={ans})")
        print(f"  Output v1: {ob1.search_v1(nums, target)}")
        print(f"  Output v2: {ob1.search_v2(nums, target)}")


if __name__ == "__main__":
    main()
