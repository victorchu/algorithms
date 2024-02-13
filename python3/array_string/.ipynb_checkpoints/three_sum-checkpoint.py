#!/usr/bin/env python3
"""
Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

NOTE:
  - The solution set must not contain duplicate triplets.

EXAMPLES:
  Input  = [-1, 0, 1, 2, -1, -4],
  Output = [ [-1, 0, 1], [-1, -1, 2] ]

REFERENCE:
  - https://leetcode.com/problems/3sum/ (Medium)
  - https://en.wikipedia.org/wiki/3SUM

"""

from typing import List
from collections import defaultdict, Counter

class Solution:
    def threeSum_v1(self, nums: List[int]) -> List[List[int]]:
        """Simple method, yet slow."""
        # Create value to index map
        def two_sum(nums, i0, target) -> List[int]:
            """Find two sum that equals the target."""
            res = []
            seen = dict()
            for i in range(i0, len(nums)-1):
                x = nums[i]
                y = target - x
                if y in seen:
                    res.append([x,y])
                seen[x] = i
            return res

        ans = list()
        for k in range(len(nums)-2):
            x = nums[k]
            res2 = two_sum(nums, k+1, -x)
            if res2:
                for a in res2:
                    v = sorted([x, *a])
                    if not v in ans:
                        ans.append(v)
        return ans
            
    def threeSum_v2(self, nums: List[int]) -> List[List[int]]:
        """Quadratic algorithm posted on Wikipedia.

        Complexity: O(N^2 + N log N)
        """
        nums.sort()
        n = len(nums)
        ans = list()
        for i in range(n-2):
            a = nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                b = nums[j]
                c = nums[k]
                s = a + b + c
                if s == 0:
                    v = [a, b, c]
                    if v not in ans:
                        ans.append(v)
                    j += 1
                    k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        return ans


    def threeSum_v3(self, nums: List[int]) -> List[List[int]]:
        """A small variation of v2.

          - Move two sum to a function.
          - Break when the first value becomes positive.

        Complexity: O(N^2 + N log N)
        """
        def two_sum2(nums, i, target):
            i = i
            j = len(nums) - 1
            res = []
            while i < j:
                x = nums[i]
                y = nums[j]
                s = x + y
                if s == target:
                    res.append([x, y])
                    i += 1
                    j -= 1
                elif s > target:
                    j -= 1
                else:
                    i += 1
            return res

        nums.sort()
        n = len(nums)
        ans = list()
        for i in range(n-2):
            a = nums[i]
            if a > 0:
                break
            res = two_sum2(nums, i+1, -a)
            if res:
                for r in res:
                    v = [a, *r]
                    if not v in ans:
                        ans.append(v)
        return ans

    def threeSum_v4(self, nums: List[int]) -> List[List[int]]:
        """LeetCode solution."""
        res = []
        found, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        min_val = min((val1, val2, complement))
                        max_val = max((val1, val2, complement))
                        if (min_val, max_val) not in found:
                            found.add((min_val, max_val))
                            res.append([val1, val2, complement])
                    seen[val2] = i
        return res


def main():
    test_data = [
        [-1, 0, 1, 2, -1, -4],
    ]

    sol = Solution()
    for nums in test_data:
        print("# Input: nums={}".format(nums))
        print("  Output v1 = {}".format(sol.threeSum_v1(nums)))
        print("  Output v2 = {}".format(sol.threeSum_v2(nums)))
        print("  Output v3 = {}".format(sol.threeSum_v3(nums)))
        print("  Output v4 = {}".format(sol.threeSum_v4(nums)))


if __name__ == "__main__":
    main()
