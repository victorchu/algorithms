#!/usr/bin/env python3
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

  Input: [0,1,0,3,12]
  Output: [1,3,12,0,0]

Note:
  1. You must do this in-place without making a copy of the array.
  2. Minimize the total number of operations.

Ref:
 - https://www.geeksforgeeks.org/move-zeroes-end-array/
 - https://leetcode.com/problems/move-zeroes/

"""
from typing import List


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """A two pointer approach.

        :param nums: number array; modify in place.
        """
        n = len(nums)
        i = -1  # the last non-zero position

        # 1. Iterate through the array and move non-zero values to the front.
        for j in range(n):
            x = nums[j]
            if x != 0:
                i += 1
                if j != i:
                    nums[i] = x

        # 2. Pad the remaining with zeros.
        for j in range(i+1, n):
            nums[j] = 0


# ----------------
#   Main
# ----------------
def main():
    """Main function"""
    test_data = [[0,1,0,3,12]]
    obj = Solution()
    for nums in test_data:
        print("# Input =", nums)
        out = nums.copy()   # copy first
        obj.moveZeroes(out)
        print("  Output =", out)


if __name__ == "__main__":
    main()

