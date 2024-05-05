#!/usr/bin/env python3
"""
Given a non-empty array of integers, return the k most frequent elements.

EXAMPLES:

  Input: nums = [1,1,1,2,2,3], k = 2
  Output: [1,2]

  Input: nums = [1], k = 1
  Output: [1]

NOTE:
 - You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
 - Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
 - It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
 - You can return the answer in any order.

REFERENCE:
  - https://leetcode.com/problems/top-k-frequent-elements/ (Medium)

"""

from typing import List
from collections import defaultdict, Counter


class Solution:
    def topKFrequent_v1(self, nums: List[int], k: int) -> List[int]:
        """Use a dictionary. Complexity = O(N) + O(N log N)"""
        # Convert to a dictionary
        d = defaultdict(int)
        for x in nums:
            d[x] += 1

        # Sort the dictionary by values
        r = [x for x in sorted(d, key=d.get, reverse=True)]
        return r[0:k]
    
    def topKFrequent_v2(self, nums: List[int], k: int) -> List[int]:
        """Use a dictionary and then use a heap.
        Complexity = O(N) + O(N log K).
        """
        d = defaultdict(int)
        for x in nums:
            d[x] += 1
            
        # Use a "min" heap to track the most frequent K
        heap = []
        for x, freq in d.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, x))
            elif freq > heap[0][0]:
                # heapq.heappushpop(heap, (freq, x))
                heapq.heapreplace(heap, (freq, x))
                
        heap.sort(reverse=True)
        return [x[1] for x in heap]
    
    def topKFrequent_v3(self, nums: List[int], k: int) -> List[int]:
        """Use the Counter module.
        Complexity: most_common uses heap as well.
        """
        # Counter is a lightweight dictionary
        c = Counter(nums)
        # It has a builtin method to return the most common (k,v).
        # We only want to keep the key part
        return [item[0] for item in c.most_common(k)]


def main():
    test_data = [
        [[1, 1, 1, 2, 2, 3, 4, 5], 1],
        [[1, 1, 1, 2, 2, 3, 4, 5], 2],
        [[1, 1, 1, 2, 2, 3, 4, 5], 3],
        [[1], 1],
    ]

    sol = Solution()
    for nums, k in test_data:
        print("# Input: nums={}, k={}".format(nums, k))
        print("  Output = {}".format(sol.topKFrequent_v1(nums, k)))
        print("  Output = {}".format(sol.topKFrequent_v2(nums, k)))
        print("  Output = {}".format(sol.topKFrequent_v3(nums, k)))


if __name__ == "__main__":
    main()
