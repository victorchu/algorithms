#!/usr/bin/env python3
"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Examples:

  Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
  Output: [[1,5],[6,9]]

  Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
  Output: [[1,2],[3,10],[12,16]]
  Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

  Input: intervals = [], newInterval = [5,7]
  Output: [[5,7]]

  Input: intervals = [[1,5]], newInterval = [2,3]
  Output: [[1,5]]

  Input: intervals = [[1,5]], newInterval = [2,7]
  Output: [[1,7]]
 
Constraints:

  - 0 <= intervals.length <= 104
  - intervals[i].length == 2
  - 0 <= intervals[i][0] <= intervals[i][1] <= 105
  - intervals is sorted by intervals[i][0] in ascending order.
  - newInterval.length == 2
  - 0 <= newInterval[0] <= newInterval[1] <= 105

REFERENCE:
  - https://leetcode.com/problems/insert-interval/

"""

from typing import List


class Solution:
    def insert_v1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """Linear search."""
        # Special case
        if not intervals:
            return [newInterval]

        # Find the insert position
        found_position = False
        inserted = False

        ans = list()
        for i, interval in enumerate(intervals):
            # Search for insert position
            if not found_position:
                if newInterval[0] <= interval[0]:   # insert before
                    found_position = True
                elif newInterval[0] <= interval[1]: # insert & merge
                    found_position = True
                    newInterval[0] = interval[0]
                else:
                    ans.append(interval)
                    continue

            # Merge with existing intervals
            if interval[0] <= newInterval[1]:
                if interval[1] > newInterval[1]:
                    newInterval[1] = interval[1] 
                continue

            # No merge; so insert into the answer
            else:
                if not inserted:
                    ans.append(newInterval)
                    inserted = True
                ans.append(interval)
                
        if not inserted:
            ans.append(newInterval)

        return ans


def main():
    test_data = [
      [[[1,3],[6,9]], [2,5]],
      [[[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]],
      [ [], [5,7]],
      [ [[1,5]], [2,3]],
      [ [[1,5]], [2,7]],
    ]

    sol = Solution()
    for intervals, new_interval in test_data:
        print("# Input  : {}, new={}".format(intervals, new_interval))
        print("  - Output v1: {}".format(sol.insert_v1(intervals.copy(), new_interval.copy())))
        print()


if __name__ == "__main__":
    main()
