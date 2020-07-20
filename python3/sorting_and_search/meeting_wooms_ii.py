#!/usr/bin/env python3
"""
Given an array of meeting time intervals consisting of start and end times
[[s1,e1), [s2,e2), ...] (si < ei), find the minimum number of conference rooms
required.

EXAMPLES:

  Input: [[0, 30], [5, 10], [15, 20]]
  Output: 2

  Input: [[7, 10], [2, 4]]
  Output: 1

  Input: [13, 15], [1, 13]
  Output: 1
  Note: The end time is not inclusive.

HINTS:
  - Think about how we would approach this problem in a very simplistic way. We
    will allocate rooms to meetings that occur earlier in the day v/s the ones
    that occur later on, right?

  - If you've figured out that we have to sort the meetings by their start time,
    the next thing to think about is how do we do the allocation?
    There are two scenarios possible here for any meeting. Either there is no
    meeting room available and a new one has to be allocated, or a meeting room has
    freed up and this meeting can take place there.

  - An important thing to note is that we don't really care which room gets
    freed up while allocating a room for the current meeting. As long as a room is
    free, our job is done.
    We already know the rooms we have allocated till now and we also know when are
    they due to get free because of the end times of the meetings going on in those
    rooms. We can simply check the room which is due to get vacated the earliest
    amongst all the allocated rooms.

  - Following up on the previous hint, we can make use of a min-heap to store
    the end times of the meetings in various rooms.
    So, every time we want to check if any room is free or not, simply check the
    topmost element of the min heap as that would be the room that would get
    free the earliest out of all the other rooms currently occupied.
    If the room we extracted from the top of the min heap isn't free, then no other
    room is. So, we can save time here and simply allocate a new room.

REFERENCE:
  - https://leetcode.com/problems/meeting-rooms-ii/ (Medium)

"""

from typing import List
import heapq


class Solution:
    def minMeetingRooms_v1(self, intervals: List[List[int]]) -> int:
        """Sort + min heap."""
        heap = []
        for start, end in sorted(intervals):
            if not heap:
                heapq.heappush(heap, end)
            else:
                if start >= heap[0]:
                    heapq.heappop(heap)
                heapq.heappush(heap, end)
        return len(heap)


def main():
    test_data = [
        [[[0, 30], [5, 10], [15, 20]], 2],
        [[[7, 10], [2, 4]], 1],
        [[[6, 15], [13, 20], [6, 17]], 3],
        [[[13, 15], [1, 13]], 1],
    ]

    sol = Solution()
    for intervals, ans in test_data:
        print("# Input  : {} (ans = {})".format(intervals, ans))
        print("  Output v1: {}".format(sol.minMeetingRooms_v1(intervals)))


if __name__ == "__main__":
    main()
