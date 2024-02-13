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
        """Binary search with special logic."""

        if not nums:
            return -1

        def helper(nums, l, r, target):
            if l >= r - 1:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    return -1

            m = (l + r) // 2
            x = nums[m]
            #print("[DEBUG] search {} : {}".format(nums[l:r+1], x))
            if x == target:
                return m

            elif nums[l] <= nums[r]:
                # Regular binary search
                if target > x:
                    return helper(nums, m, r, target)
                else:
                    return helper(nums, l, m, target)

            elif target >= nums[l]:
                # Target in left array
                if (target > x and x >= nums[l]) or (target < x and x <= nums[r]):
                    return helper(nums, m, r, target)
                else:
                    return helper(nums, l, m, target)

            elif target <= nums[r]:
                # Target in right array
                if (target > x and x <= nums[r]) or (target < x and x >= nums[l]):
                    return helper(nums, m, r, target)
                else:
                    return helper(nums, l, m, target)

            else:
                return -1

        return helper(nums, 0, len(nums) - 1, target)

    def search_v2(self, nums: List[int], target: int) -> int:
        """Locate the pivot location (the min of the array).

        This may be a little bit slower (two binary searches), yet
        the logic is less mind-boggling.
        """
        def find_pivot(nums, l, r):
            if nums[l] <= nums[r]:
                return l
            elif l >= r-1:
                if nums[l] >= nums[r]:
                    return r
                else:
                    return -1

            m = (l + r) // 2
            x = nums[m]
            if x > nums[l]:
                return find_pivot(nums, m, r)
            else:
                return find_pivot(nums, l, m)

        def binary_search(nums, l, r, target):
            if l >= r - 1:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    return -1

            m = (l + r) // 2
            x = nums[m]
            if target >= x:
                return binary_search(nums, m, r, target)
            else:
                return binary_search(nums, l, m, target)

        if not nums:
            return -1
        n = len(nums)
        i = find_pivot(nums, 0, n-1)
        #print("[DEBUG] pivot index = {}".format(i))

        if target <= nums[n-1]:
            return binary_search(nums, i, n-1, target)
        elif target >= nums[0]:
            return binary_search(nums, 0, i-1, target)
        else:
            return -1


def main():
    test_data = [
        [[2, 3, 4, 5, 6, 7, 8, 9, 1], 3],
        [[0, 1, 2, 4, 5, 6, 7], 6],
        [[4, 5, 6, 7, 0, 1, 2], 6],
        [[6, 8, 10, 0, 2, 4], 0],
        [[6, 8, 10, 0, 2, 4], 8],
        [[6, 8, 10, 0, 2, 4], 9],
        [[6, 8, 10, 0, 2, 4], 12],
        [[6, 8, 10, 0, 2, 4], 5],
        [[1], 1],
        [[], 5],

    ]

    sol = Solution()
    for nums, target in test_data:
        print("# Input  : {}, {}".format(nums, target))
        print("  Output v1: {}".format(sol.search_v1(nums, target)))
        print("  Output v2: {}".format(sol.search_v2(nums, target)))


if __name__ == "__main__":
    main()
