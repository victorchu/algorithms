#!/usr/bin/env python3
"""
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

EXAMPLES:

  Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
  Output: True

REFERENCE:
  - https://leetcode.com/problems/valid-square/ (Medium)
  - https://www.geeksforgeeks.org/check-given-four-points-form-square/

"""

from typing import List
import numpy as np


class Solution:
    def validSquare_v1(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # Sort the points to make them clockwise or counter clockwise.
        a = np.array([p1, p2, p3, p4])
        idx = np.lexsort((a[:, 1], a[:, 0]))
        idx[3], idx[2] = idx[2], idx[3]
        a = a[idx]

        # Get the difference between two consecutive points
        dx = a[0][0] - a[-1][0]
        dy = a[0][1] - a[-1][1]
        is_square = True
        for pi, pj in zip(a[:-1], a[1:]):
            new_dx = pj[0] - pi[0]
            new_dy = pj[1] - pi[1]

            if (abs(new_dy) != abs(dx)) or \
                (abs(new_dx) != abs(dy)) or \
                (new_dy * new_dx != -dx * dy) or \
                    (new_dx == 0 and new_dy == 0):
                is_square = False
                break
            dx = new_dx
            dy = new_dy
        return is_square

    def validSquare_v2(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """Use distance."""
        # Sort the points to make them clockwise or counter clockwise.
        a = np.array([p1, p2, p3, p4])
        idx = np.lexsort((a[:, 1], a[:, 0]))
        idx[3], idx[2] = idx[2], idx[3]
        a = a[idx]

        def dist_sq(p, q):
            return (p[0] - q[0])**2 + (p[1] - q[1]) ** 2

        # Get the difference between two consecutive points
        r1 = dist_sq(a[0], a[1])
        if r1 == 0:
            return False

        r2 = dist_sq(a[1], a[2])
        if r1 != r2:
            return False

        r3 = dist_sq(a[2], a[3])
        if r2 != r3:
            return False

        r4 = dist_sq(a[3], a[0])
        if r3 != r4:
            return False

        d = dist_sq(a[0], a[2])
        if d != 2 * r1:
            return False

        return True

    def validSquare_v3(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """Same as v2, but doesn't use np to sort."""
        # Sort the points to make them clockwise or counter clockwise.
        a = [p1, p2, p3, p4]
        a.sort(key=lambda x: x[1])
        a.sort(key=lambda x: x[0])
        a[2], a[3] = a[3], a[2]

        def dist_sq(p, q):
            return (p[0] - q[0])**2 + (p[1] - q[1]) ** 2

        # Get the difference between two consecutive points
        r1 = dist_sq(a[0], a[1])
        if r1 == 0:
            return False

        r2 = dist_sq(a[1], a[2])
        if r1 != r2:
            return False

        r3 = dist_sq(a[2], a[3])
        if r2 != r3:
            return False

        r4 = dist_sq(a[3], a[0])
        if r3 != r4:
            return False

        d = dist_sq(a[0], a[2])
        if d != 2 * r1:
            return False

        return True


def main():
    test_data = [
        [[1, 1], [1, 0], [0, 1], [0, 0]],
        [[0, 1], [1, 0], [-1, 0], [0, -1]],
        [[1, 2], [2, -1], [-1, -2], [-2, 1]],
        [[1, 2], [2, -1], [-1, -2], [-3, 1]],
        [[0, 0], [0, 0], [0, 0], [0, 0]],
    ]

    sol = Solution()
    for points in test_data:
        print("# Input = {}".format(points))
        print("  Output = {}".format(sol.validSquare_v1(*points)))
        print("  Output = {}".format(sol.validSquare_v2(*points)))
        print("  Output = {}".format(sol.validSquare_v3(*points)))


if __name__ == "__main__":
    main()
