#!/usr/bin/env python3
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

EXAMPLES:
  Input: [1,8,6,2,5,4,8,3,7]
  Output: 49

HINTS:
  - There is an O(N) solution.

REFERENCE:
  - https://leetcode.com/problems/container-with-most-water/ (Medium)

"""

from typing import List


class Solution:
    def maxArea_v1(self, height: List[int]) -> int:
        """A simple solution."""
        max_area = 0
        n = len(height)
        h_prev = 0
        for i in range(0, n-1):
            hi = height[i]
            if hi <= h_prev:
                continue
            for j in range(i+1, n):
                hj = height[j]
                h = min(hi, hj)
                area = (j - i) * h 
                if area > max_area:
                    max_area = area
                    h_prev = h

        return max_area

    def maxArea_v2(self, height: List[int]) -> int:
        """Use two pointers. Move the one with shorter height."""
        max_area = 0
        n = len(height)
        i = 0
        j = n - 1
        while i < j:
            hi = height[i]
            hj = height[j]
            h = min(hi, hj)
            area = (j - i) * h
            if area > max_area:
                max_area = area

            # move the pointer with a shorter height
            if hi < hj:
                i += 1
            else:
                j -= 1

        return max_area


def main():
    test_data = [
        [1,8,6,2,5,4,8,3,7],
    ]

    sol = Solution()
    for heights in test_data:
        print("# Input = {}".format(heights))
        print("  Output v1 = {}".format(sol.maxArea_v1(heights)))
        print("  Output v2 = {}".format(sol.maxArea_v2(heights)))


if __name__ == "__main__":
    main()
