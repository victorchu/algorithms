#!/usr/bin/env python3
"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique
(except for the order that it is in.)

EXAMPLES:

  Input: points = [[1,3],[-2,2]], K = 1
  Output: [[-2,2]]
  Explanation:
    - The distance between (1, 3) and the origin is sqrt(10).
    - The distance between (-2, 2) and the origin is sqrt(8).
    - Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
    - We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

REFERENCE:
  - https://leetcode.com/problems/k-closest-points-to-origin/ (Medium)

"""

import math
import heapq
from typing import List


class Solution:
    def kClosest_v1(self, points: List[List[int]], K: int) -> List[List[int]]:
        """Use dictionary: {dist: [point]}"""
        dist_map = dict()
        for p in points:
            dist = math.sqrt(p[0]**2 + p[1]**2)
            dist_map[dist] = p
        i = 0
        ans = []
        for d, p in sorted(dist_map.items()):
            ans.append(p)
            i += 1
            if i >= K:
                break
        return ans

    def kClosest_v2(self, points: List[List[int]], K: int) -> List[List[int]]:
        """Use min heap."""
        heap = list()
        for p in points:
            dist = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(heap, [dist, p])
        i = 0
        ans = []
        for _ in range(K):
            d, p = heapq.heappop(heap)
            ans.append(p)
        return ans

    def kClosest_v3(self, points: List[List[int]], K: int) -> List[List[int]]:
        """Use max heap to keep K elements only."""
        heap = list()
        for p in points:
            dist_sq = p[0] * p[0] + p[1] * p[1]
            if len(heap) < K:
                heapq.heappush(heap, [-dist_sq, p])
            elif dist_sq < -heap[0][0]:
                heapq.heappushpop(heap, [-dist_sq, p])
        return [p for d, p in heap]


def main():
    test_data = [
        [[[1, 3], [-2, 2]], 1],
        [[[1, 3], [-2, 2], [2,3]], 2],
    ]

    sol = Solution()
    for points, K in test_data:
        print("# Input  : {}, {}".format(points, K))
        print("  Output v1: {}".format(sol.kClosest_v1(points, K)))
        print("  Output v2: {}".format(sol.kClosest_v2(points, K)))
        print("  Output v3: {}".format(sol.kClosest_v3(points, K)))


if __name__ == "__main__":
    main()
