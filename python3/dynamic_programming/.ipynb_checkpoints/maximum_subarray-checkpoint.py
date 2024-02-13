#!/usr/bin/env python3
"""
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

EXAMPLES:

  Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
  Output: 6
  Explanation: [4, -1, 2, 1] has the largest sum = 6.

FOLLOW UP:

If you have figured out the O(n) solution, try coding another solution
using the divide and conquer approach, which is more subtle.

REFERENCE:
  - https://leetcode.com/problems/maximum-subarray/ (Easy)

"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Get incremental solution."""
        if not nums:
            return 0

        curr_sum = max_sum = None
        for x in nums:
            # Initial condition
            if curr_sum is None:
                curr_sum = max_sum = x
                continue

            # Get the maximum sum ending at i
            # If the previous sum was negative, start from scratch.
            if curr_sum <= 0:
                curr_sum = x
            else:
                curr_sum += x

            # Compare with the overall maxium
            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum


def main():
    test_data = [
        [[-2, 1, -3, 4, -1, 2, 1, -5, 4], 6],
        [[], 0],
    ]

    sol = Solution()
    for nums, ans in test_data:
        print("# Input = {} (ans={})".format(nums, ans))
        print("  Output = {}".format(sol.maxSubArray(nums)))


if __name__ == "__main__":
    main()
