#!/usr/bin/env python3
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example:

 Input:  nums1 = [1, 12, 15, 26, 38]
        nums2 = [2, 13, 17, 30, 45]
 Output: 16

Key functions:
  . np.mean(array)
  . np.median(array)
  . // : integer division
  . %  : mod

Ref:
  . https://www.geeksforgeeks.org/median-of-two-sorted-arrays/
  . https://leetcode.com/problems/median-of-two-sorted-arrays/
"""


import numpy as np
from typing import List


class Solution:
    def method1(self, nums1: List[int], nums2:List[int]) -> float:
        """Merge two arrays.

        Complexity is O(n).
        LeetCode: 144 ms (beats 8.52%), 29MB.
        """
        # Find the medium positions [k1, k2] in the merged array.
        n = len(nums1)
        m = len(nums2)
        total_len = n + m

        if total_len % 2 == 1:
            k1 = k2 = total_len // 2 
        else:
            k1 = total_len // 2 - 1
            k2 = k1 + 1

        #   i for nums1, j for nums2, and k for the merged array.
        i, j, k = 0, 0, 0

        # Use a list to store median elements
        median = 0
        for k in range(k2+1):
            if (i < n) and (j < m):
                if nums1[i] < nums2[j]:
                    x = nums1[i]
                    i += 1
                else:
                    x = nums2[j]
                    j += 1
            elif i < n:
                x = nums1[i]
                i += 1
            else:
                x = nums2[j]
                j += 1

            if k >= k1:
                median += x

        if k1 != k2:
            median /= 2.0
        return median


# ----------------
#   Main
# ----------------
def main():
    """Main function"""
    sample_data = [
        [[1, 12, 15, 26, 38], [2, 13, 17, 30, 45]],
        [[1, 3], [2]],
        [[], [1]],
        [[2], []],
        [[3], [-2, -1]],
        [[1, 2], [-1, 3]],
    ]

    sol = Solution()
    for nums1, nums2 in sample_data:
        print("# Finding median of {} and {}".format(nums1, nums2))
        print(" v1 => {}".format(sol.method1(nums1, nums2)))


if __name__ == "__main__":
    main()
