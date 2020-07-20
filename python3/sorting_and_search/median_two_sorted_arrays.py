#!/usr/bin/env python3
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

EXAMPLES:

  nums1 = [1, 3]
  nums2 = [2]
  The median is 2.0

  nums1 = [1, 2]
  nums2 = [3, 4]
  The median is (2 + 3)/2 = 2.5

Ref:
  - https://leetcode.com/problems/median-of-two-sorted-arrays/ (Hard)
  - https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
  - https://www.geeksforgeeks.org/median-two-sorted-arrays-different-sizes-ologminn-m/

"""


import numpy as np
from typing import List


class Solution:

     def findMedianSortedArrays_v1(self, nums1: List[int], nums2: List[int]) -> float:
        """Merge sort.

        Time complexity: O(m + n), space complexity O(1)
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


def main():
    """Main function"""
    sample_data = [
        [[1, 3], [2]],
        [[1, 12, 15, 26, 38], [2, 13, 17, 30, 45]],
        [[1, 2], [-1, 3]],
        #[[], [1]],
        #[[2], []],
        #[[3], [-2, -1]],
    ]

    sol = Solution()
    for nums1, nums2 in sample_data:
        print("# Input: {}, {}".format(nums1, nums2))
        print("  Output v1 = {}".format(sol.findMedianSortedArrays_v1(nums1, nums2)))


if __name__ == "__main__":
    main()
