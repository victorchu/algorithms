"""
Given a collection of intervals, merge all overlapping intervals.

EXAMPLES:

  Input: [[1,3], [2,6], [8,10], [15,18]]
  Output: [[1,6], [8,10], [15,18]]
  Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

  Input: [[1,4], [4,5]]
  Output: [[1,5]]
  Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
    1 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti <= endi <= 10^4

REFERENCE:
  - https://leetcode.com/problems/merge-intervals/ (Medium)

"""

from typing import List


class Solution:    
    def merge_v1(self, intervals: List[List[int]]) -> List[List[int]]:
        """Sorted and merge. A compact version.

        Time Complexity: O(N log(N)) + O(N).  Space: O(N)
        """
        out = []
        for x in sorted(intervals, key=lambda x: x[0]):
            if out and x[0] <= out[-1][1]:
                out[-1][1] = max(x[1], out[-1][1])
            else:
                out.append(x)
        return out


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
        print(f"# Input  : {intervals}")
        print(f"  - Output v1: {sol.merge_v1(intervals)}")
        # print(f"  - Output v2: {sol.merge_v2(intervals)}")
        print()


if __name__ == "__main__":
    main()
