#!/usr/bin/env python3
"""
Given an array with n objects colored red, white or blue, sort them in-place so
that objects of the same color are adjacent, with the colors in the order red,
white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

EXAMPLES:

  Input: [2,0,2,1,1,0]
  Output: [0,0,1,1,2,2]

Follow up:

  - A rather straight forward solution is a two-pass algorithm using counting sort.
    First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
    array with total number of 0's, then 1's and followed by 2's.
  - Could you come up with a one-pass algorithm using only constant space?

REFERENCE:
  - https://leetcode.com/problems/sort-colors/ (Medium)

"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        i0 = -1
        i2 = len(nums)

        i = i0 + 1
        while i < i2:
            if nums[i] == 0:
                # Swap 0 to the next 0 position at the front
                i0 += 1
                nums[i0], nums[i] = nums[i], nums[i0]
                i += 1
            elif nums[i] == 2:
                # Swap 2 to the next 2 position at the bottom
                # Do not increment i here since we have not checked the swapped number
                i2 -= 1
                nums[i2], nums[i] = nums[i], nums[i2]
            else:
                i += 1


def main():
    test_data = [
        [2, 0, 2, 1, 1, 0],
        [1, 2, 0],
    ]

    sol = Solution()
    for nums in test_data:
        print("# Input  = {}".format(nums))
        sol.sortColors(nums)
        print("  Output = {}".format(nums))


if __name__ == "__main__":
    main()
