#!/usr/bin/env python3
"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

EXAMPLES:

  Input: [1,1,2]
  Output: [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]

NOTE:
  - Work on permutation.py first.

REFERENCE:
 - https://leetcode.com/problems/permutations-ii/ (Medium)
 - https://www.geeksforgeeks.org/distinct-permutations-string-set-2/

"""

from typing import List


class Solution:
    def permute_unique(self, nums: List[int]) -> List[List[int]]:
        """Use a set to track visited characters."""
        if not nums:
            return []

        def helper(vals):
            """Returns a list of lists"""
            n = len(vals)
            if n == 1:
                return [vals]
            else:
                results = list()
                visited = set()
                for i in range(n):
                    if vals[i] in visited:
                        continue
                    v = vals.pop(i)     # remove the i-th elmeent
                    for r in helper(vals):
                        results.append([v] + r)
                    vals.insert(i, v)   # backtrack
                    visited.add(v)

                return results

        return helper(nums)


def main():
    test_data = [
        [1, 1, 2],
        [3, 3, 0, 3],
        [2, 2, 1, 1],
    ]

    sol = Solution()
    for nums in test_data:
        print("# Input = {}".format(nums))
        print("  Output = {}".format(sol.permute_unique(nums)))


if __name__ == "__main__":
    main()
