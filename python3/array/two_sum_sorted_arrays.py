#!/usr/bin/env python3
"""
Given an array of integers that is already sorted in ascending order, find two
numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add
up to the target, where index1 must be less than index2.

Note:
  - Your returned answers (both index1 and index2) are one-based.
  - You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:
  Input: numbers = [2,7,11,15], target = 9
  Output: [1,2]
  Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


REFERENCE:
  - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ (Easy)

"""

from typing import List


class Solution:
    def twoSum_v1(self, numbers: List[int], target: int) -> List[int]:
        """Use two pointers.

        Time complexity: O(N).  Storage O(1).

        Note that if the array is not sorted, sorting will take O(N logN),
        making this method less efficient.
        """
        i1, i2 = 0, len(numbers) - 1
        while i1 < i2:
            s = numbers[i1] + numbers[i2]
            if s == target:
                return [i1 + 1, i2 + 1]
            elif s > target:
                i2 -= 1
            else:
                i1 += 1
        return []

    def twoSum_v2(self, numbers: List[int], target: int) -> List[int]:
        """Use a dictionary.  The array doesn't need to be sorted.

        Note that the dictionary contains visited values only.
        This method can handle duplicated values.

        Time complexity: O(N).  Storage O(N).
        """
        seen = dict()   # {num: index}
        for i, x in enumerate(numbers, start=1):
            y = target - x
            if y in seen:
                j = seen[y]
                return [j, i]
            seen[x] = i
        return []


def main():
    test_data = [
        [[2, 7, 11, 15], 9, [1, 2]],
        [[2, 7, 7, 11, 15], 14, [2, 3]],
    ]

    sol = Solution()
    for numbers, target, ans in test_data:
        print("# Input: numbers={}, target={}, ans={}".format(numbers, target, ans))
        print("  Output v1 = {}".format(sol.twoSum_v1(numbers, target)))
        print("  Output v2 = {}".format(sol.twoSum_v2(numbers, target)))


if __name__ == "__main__":
    main()
