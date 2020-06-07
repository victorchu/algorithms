#!/usr/bin/env python3
"""
Given a collection of distinct integers, return all possible permutations.

EXAMPLES:

  Input: [1,2,3]
  Output: [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]

REFERENCE:
 - https://leetcode.com/problems/permutations/ (Medium)
 - https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

"""

from typing import List


class Solution:
    def permute_v1(self, nums: List[int]) -> List[List[int]]:
        """Use pop and insert to manipuate the list."""
        if not nums:
            return []

        def helper(vals):
            """Returns a list of lists"""
            n = len(vals)
            if n == 1:
                # the termination condition; need to return a list of list(s)
                return [vals]
            elif n == 2:
                # an optionally step to speed up the process
                return [vals, [vals[1], vals[0]]]
            else:
                results = list()
                for i in range(n):
                    v = vals.pop(i)     # remove the i-th elmeent
                    for r in helper(vals):
                        results.append([v] + r)
                    vals.insert(i, v)   # backtrack

                return results

        return helper(nums)

    def permute_v2(self, nums: List[int]) -> List[List[int]]:
        """Use swap and index to manipulate the status."""
        if not nums:
            return []

        def helper(nums, i, n, results):
            if i == n - 1:
                results.append(nums.copy())
            else:
                for j in range(i, n):
                    nums[i], nums[j] = nums[j], nums[i]
                    helper(nums, i+1, n, results)
                    nums[i], nums[j] = nums[j], nums[i]  # backtrack

        results = list()
        helper(nums, 0, len(nums), results)
        return results


def main():
    test_data = [
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4],
        [],
        None,
    ]

    sol = Solution()
    for nums in test_data:
        print("# Input = {}".format(nums))
        print("  Output v1 = {}".format(sol.permute_v1(nums)))
        print("  Output v2 = {}".format(sol.permute_v2(nums)))


if __name__ == "__main__":
    main()
