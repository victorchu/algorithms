#!/usr/bin/env python3
"""
Given a collection of intervals, merge all overlapping intervals.

EXAMPLES:

  Input: [[1,3], [2,6], [8,10], [15,18]]
  Output: [[1,6], [8,10], [15,18]]
  Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

  Input: [[1,4], [4,5]]
  Output: [[1,5]]
  Explanation: Intervals [1,4] and [4,5] are considered overlapping.

REFERENCE:
  - https://leetcode.com/problems/merge-intervals/ (Medium)

"""

from typing import List


class Solution:
    def merge_v1(self, intervals: List[List[int]]) -> List[List[int]]:
        """Sort.
        A simple method will take O(N^2), comparing each element with the other.
        If we sort the intervals first, it will be O(N log(N)) + O(N).
        Here we use the built-in sort method.  Alternatively, we may write
        our own sort method (like merge sort) and make some modifications.
        """
        ans = []
        if not intervals:   # validate input
            return ans

        # Get the first element
        it = iter(sorted(intervals))    # will sort on the first value!
        curr = next(it) 

        # Iterate through the rest
        for x in it:
            # Compare two consecutive intervals.
            if x[0] <= curr[1]:   
                if x[1] > curr[1]:
                    curr[1] = x[1]
            else:
                ans.append(curr)
                curr = x
        ans.append(curr)
        return ans

    def merge_v2(self, intervals: List[List[int]]) -> List[List[int]]:
        """Simple O(N^2) method."""
        visited = set()
        ans = []
        for i, x in enumerate(intervals):
            if i in visited:
                continue
            visited.add(i)
            for j in range(i+1, len(intervals)):
                if j in visited:
                    continue
                y = intervals[j]

                # Check if x and y overlap
                if y[0] > x[1] or y[1] < x[0]:
                    continue
                else:
                    x[0] = min(x[0], y[0])
                    x[1] = max(x[1], y[1])
                    visited.add(j)
            ans.append(x)
        return ans


def main():
    test_data = [
        [[1, 3], [8, 10], [2, 6], [15, 18], [2, 4], [9, 11]],
        [[1, 4], [4, 5]],
        [[1, 4], [2, 3]],
        [[2, 3]],
        [],
    ]

    sol = Solution()
    for intervals in test_data:
        print("# Input  : {}".format(intervals))
        print("  - Output v1: {}".format(sol.merge_v1(intervals)))
        print("  - Output v2: {}".format(sol.merge_v2(intervals)))
        print()


if __name__ == "__main__":
    main()
