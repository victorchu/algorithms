#!/usr/bin/env python3
"""
Given an integer array nums, find the contiguous subarray (containing at least
one number, at most k) which has the largest sum and return its sum.

EXAMPLES:

  Input: 6, [-2, 1, -3, 4, -1, 2, 1, -5, 4],
  Output: 6
  Explanation: [4, -1, 2, 1] has the largest sum = 6.

  Input: 3, [-2, 1, -3, 4, -1, 2, 1, -5, 4],
  Output: 5
  Explanation: [4, -1, 2]

  Input: 2, [-2, 1, -3, 4, -1, 2, 1, -5, 4],
  Output: 4
  Explanation: [4]

FOLLOW UP:

If you have figured out the O(n) solution, try coding another solution
using the divide and conquer approach, which is more subtle.

REFERENCE:
  - Codility

"""
from typing import List


class Solution:
    def max_subarray(self, k, nums: List[int]) -> int:
        """Get incremental solution.  
        Time complexity = O(N).  Space complexity = O(1)."""
        curr_sum = max_sum = 0
        i = 0
        for j, x in enumerate(nums):
            if  j - i >= k:
                curr_sum -= nums[i]
                i += 1
            if curr_sum < 0:
                curr_sum = x
                i = j
            else:
                curr_sum += x
            max_sum = max(curr_sum, max_sum)
            # print(f"[DEBUG] i={i}, j={j}, x={x:2d}, curr={curr_sum:2d}, max={max_sum:2d}")
        return max_sum


def main():
    test_data = [
        [6, [-2, 1, -3, 4, -1, 2, 1, -5, 4], 6],  # [4, -1, 2, 1]
        [3, [-2, 1, -3, 4, -1, 2, 1, -5, 4], 5],  # [4, -1, 2]
        [2, [-2, 1, -3, 4, -1, 2, 1, -5, 4], 4],  # [4]
        [6, [], 0],
    ]

    sol = Solution()
    for k, nums, ans in test_data:
        print(f"# Input = {k}, {nums} (ans={ans})")
        print(f"  Output = {sol.max_subarray(k, nums)}")


if __name__ == "__main__":
    main()
