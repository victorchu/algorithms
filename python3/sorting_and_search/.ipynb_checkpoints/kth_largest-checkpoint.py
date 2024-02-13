#!/usr/bin/env python3
"""
Find the kth largest element in an unsorted array.

NOTE:
  - It is the kth largest element in the sorted order, not the kth largest distinct element.

EXAMPLES:
  Input: [3,2,1,5,6,4] and k = 2
  Output: 5     # 6,[5]

  Input: [3,2,3,1,2,4,5,5,6] and k = 4
  Output: 4     # 6,5,5,[4],... note that 5 occupies two positions

REFERENCE:
  - https://leetcode.com/problems/kth-largest-element-in-an-array/ (Medium)
  - https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

"""

from typing import List
import heapq


class Solution:
    def findKthLargest_v1(self, nums: List[int], k: int) -> int:
        """Sort first. Then pick up the desired position. O(N log M).
        """
        # Use the built-in sort method here.
        nums.sort()
        return nums[-k]

    def findKthLargest_v2(self, nums: List[int], k: int) -> int:
        """Use a min heap to track the largest k elements. O(N log k)."""
        h = list()   # heap
        for i, x in enumerate(nums):
            if i < k:
                heapq.heappush(h, x)
            elif x > h[0]:
                # pop and push; it doesn't change the size of h.
                heapq.heapreplace(h, x)
        return h[0]


def main():
    test_data = [
        [[3, 2, 1, 5, 6, 4], 2, 5],
        [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4]
    ]

    ob1 = Solution()
    for nums, k, ans in test_data:
        print(f"# Input: nums={nums}, k={k}, ans={ans}")
        print(f"  Output v1 = {ob1.findKthLargest_v1(nums, k)}")
        print(f"  Output v2 = {ob1.findKthLargest_v2(nums, k)}")


if __name__ == "__main__":
    main()
