#!/usr/bin/env python3
"""
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.

EXAMPLES:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

    ^                         
    |                    +--+
    |        +--+WW WW WW|  +--+WW+--+
    |  +--+WW|  +--+WW+--+     +--+  +--+
    +--+  +--+     +--+                 +----->
     0  1  0  2  1  0  1  3  k2  1  2  1          

REFERENCE:
  - https://leetcode.com/problems/trapping-rain-water/ (Hard)

"""

from typing import List


class Solution:
    def trap_v1(self, height: List[int]) -> int:
        # max height seen from left
        left_height = []
        max_height = 0
        for h in height:
            if h >= max_height:
                max_height = h
            left_height.append(max_height)

        # max height seen from right
        n = len(height)
        right_height = [0] * n
        max_height = 0
        for j in range(n-1, -1, -1):
            h = height[j]
            if h >= max_height:
                max_height = h
            right_height[j] = max_height

        # The actual water level is the minimum of the above two
        water_levels = [min(h1, h2) for (h1, h2) in zip(left_height, right_height)]

        # Water trapped amount = water_level - height
        trap_levels = [w - h for (w, h) in zip(water_levels, height)]
        return sum(trap_levels)

    def trap_v2(self, height: List[int]) -> int:
        """The same v1 logic written in recurssion."""
        def get_water(height, i, n, left_height):
            """Return water trapped max right height."""
            if i == n:
                return 0, 0

            # Update the max height seen from the left
            h = height[i]
            left_height = max(left_height, h)

            # Get the amount and the max height from the right
            amount, right_height = get_water(height, i+1, n, left_height)

            # Add the water level at this position
            right_height = max(right_height, h)
            amount += min(left_height, right_height) - h

            return amount, right_height

        ans, _ = get_water(height, 0, len(height), 0)
        return ans

    def trap_v3(self, height: List[int]) -> int:
        """TBD: use two pointers."""
        pass


def main():
    test_data = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    ]

    sol = Solution()
    for height in test_data:
        print("# Input = {}".format(height))
        print("  Output v1 = {}".format(sol.trap_v1(height)))
        print("  Output v2 = {}".format(sol.trap_v2(height)))


if __name__ == "__main__":
    main()
