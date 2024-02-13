#!/usr/bin/env python3
"""
Given two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
You may assume nums1 and nums2 cannot be both empty.

Followup:
  - The overall run time complexity should be O(log(m+n)).

EXAMPLES:

  nums1 = [1, 3]
  nums2 = [2]
  The median is 2.0

  nums1 = [1, 2]
  nums2 = [3, 4]
  The median is (2 + 3)/2 = 2.5

Note:
  - The O(m + n) solution is easy.
  - The O(log(m+n)) solution is tedious.

Ref:
  - https://leetcode.com/problems/median-of-two-sorted-arrays/ (Hard)
  - https://www.geeksforgeeks.org/median-of-two-sorted-arrays/ (same size)
  - https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
  - https://www.geeksforgeeks.org/median-two-sorted-arrays-different-sizes-ologminn-m/

"""


import numpy as np
from typing import List


class Solution:

     def findMedianSortedArrays_v1(self, nums1: List[int], nums2: List[int]) -> float:
        """Merge sort two arrays.  Then get the middle point.
        Time: O(m + n). Space O(m + n)
        """
        a = list()
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        while (i < n) or (j < m):
            if  (j >= m) or (i < n and nums1[i] < nums2[j]):
                a.append(nums1[i])
                i += 1
            else:
                a.append(nums2[j])
                j += 1

        l = len(a)
        k = l // 2
        return a[k] if (l % 2 == 1) else (a[k-1] + a[k]) / 2.0

     def findMedianSortedArrays_v2(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Merge sort and stop when reaching the middle point(s).
        Only need to store values associated with the median.

        Time complexity: O(m + n), space complexity O(1)
        """
        # Find the medium positions [k1, k2] in the merged array.
        n, m = len(nums1), len(nums2)
        total_len = n + m

        # Get the median indices
        if total_len % 2 == 1:
            k1 = k2 = total_len // 2
        else:
            k2 = total_len // 2
            k1 = k2 - 1

        # Use a list to store median elements
        median = 0
        i, j, = 0, 0
        for k in range(k2 + 1):
            if  (j >= m) or (i < n and nums1[i] < nums2[j]):
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
        print("  - Output v1 = {}".format(sol.findMedianSortedArrays_v1(nums1, nums2)))
        print("  - Output v2 = {}".format(sol.findMedianSortedArrays_v2(nums1, nums2)))
        print()


if __name__ == "__main__":
    main()
