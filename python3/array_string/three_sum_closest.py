#!/usr/bin/env python3
"""
Given an array nums of n integers and an integer target, find three integers in
nums such that the sum is closest to target. Return the sum of the three
integers. You may assume that each input would have exactly one solution.

EXAMPLE:

  Input: nums = [-1,2,1,-4], target = 1
  Output: 2
  Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Constraints:

    3 <= nums.length <= 10^3
    -10^3 <= nums[i] <= 10^3
    -10^4 <= target <= 10^4

REFERENCE:
  - https://leetcode.com/problems/3sum-closest/ (Medium)

"""

from typing import List
from collections import defaultdict, Counter


class Solution:
    def threeSumClosest_v1(self, nums: List[int], target: int) -> int:
        """Quadratic algorithm posted on Wikipedia.

        Complexity: O(N^2 + N log N)
        """
        nums.sort()
        n = len(nums)
        ans = float('inf')
        min_delta = ans

        for i in range(n-2):
            a = nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                b = nums[j]
                c = nums[k]
                s = a + b + c

                # Compare with the known closest sum
                delta = abs(s - target)
                print(
                    f"[DEBUG] {a:3d} + {b:3d} + {c:3d} = {s:3d} (|delta| = {delta:3d})")
                if delta < min_delta:
                    min_delta = delta
                    ans = s

                # Determine which pointer to move
                if s == target:
                    return ans
                elif s > target:
                    k -= 1
                else:
                    j += 1
        return ans


def main():
    test_data = [
        [[-1, 2, 1, -4], 1, 2],
        [[1, 2, 4, 8, 16, 32, 64, 128], 82, 82]
    ]

    sol = Solution()
    for nums, target, ans in test_data:
        print("# Input: nums={}, target={}, ans={}".format(nums, target, ans))
        print("  Output v1 = {}".format(sol.threeSumClosest_v1(nums, target)))


if __name__ == "__main__":
    main()
