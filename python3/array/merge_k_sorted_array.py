#!/usr/bin/env python3
#
# Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
#
# Example 1:
#   Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
#   Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
#
# Example 2:
#   Input: L1=[5, 8, 9], L2=[1, 7]
#   Output: [1, 5, 7, 8, 9]
#
# Variation:
#  - Can change lists to linked lists. Then store (x, p)
#
# Ref:
#  - https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/
#  - https://www.geeksforgeeks.org/merge-k-sorted-linked-lists-set-2-using-min-heap/
#

import heapq
from typing import List


class Solution:
    def merge_v1(self, lists : List[list]) -> list:
        """Naive 1 - merging two at a time.
        
        Time Complexity: O(N^(K-1)) - traversing N times for K-1 lists.
        Auxilary Space: N * (K-1) ?
        """
        def merge_arrays(arr1: list , arr2: list) -> list:
            merged_arr = []
            i, j = 0, 0
            while (i < len(arr1)) and (j < len(arr2)):
                if (arr1[i] < arr2[j]):
                    merged_arr.append(arr1[i])
                    i += 1
                else:
                    merged_arr.append(arr2[j])
                    j += 1
            # Handle remaining of the array
            merged_arr.extend(arr1[i:])
            merged_arr.extend(arr2[j:])
            return merged_arr
        
        results = lists[0]
        for arr2 in lists[1:]:
            results = merge_arrays(results, arr2)
        return results    
            
    def merge_v2(self, lists : List[list]) -> list:
        """Naive 2 - merging two at a time. Yet try to save space.
        
        Time Complexity: O(N^(K-1)) - traversing N times for K-1 lists.
        Auxilary Space: N
        """
        def merge_arrays(arr1: list , arr2: list, m, n) -> list:
            """ Merge arr2 into the end of arr1, assuming that arr1 has enough space.
            Note: popularte arr1 from the end.
            """
            arr1.extend([0] * n)  # extend arr1 first
            i, j, k = m-1, n-1, m+n-1
            while i >= 0 and j >= 0:
                if (arr1[i] > arr2[j]):
                    arr1[k] = arr1[i]
                    i -= 1
                else:
                    arr1[k] = arr2[j]
                    j -= 1
                k -= 1

            # Handle remaining of the arr2
            while k >= 0:
                arr1[k] = arr2[k]
                k -= 1

            return arr1
        
        results = lists[0].copy()
        for arr2 in lists[1:]:
             merge_arrays(results, arr2, len(results), len(arr2))
        return results  

    def merge_v3(self, lists : List[list]) -> list:
        """ Use a min heap for tracking.
        
        Time Complexity: O(N * K * log(K))
        Auxilary Space: O(K + N)
        """
        heap = []
        results = []
        
        # Initialize a min heap
        i = 0
        for l in lists:
            heapq.heappush(heap, [l[i], i, l])
    
        while heap:
            # Pop the first (smallest) element from the heap
            x, i, l = heapq.heappop(heap)
            results.append(x)
            
            # Push the next element from the list into the heap
            i += 1
            if (i < len(l)):
                heapq.heappush(heap, [l[i], i, l])

        return results
    
    
def main():
    test_data = [
        [[2, 6, 8], [3, 6, 7], [1, 3, 4]],
        [[5, 8, 9], [1, 7]],
    ]

    ob1 = Solution()
    for lists in test_data:
        print(f"# Input  : {lists}")
        print(f"  Output : {ob1.merge_v1(lists)}")        
        print(f"  Output : {ob1.merge_v2(lists)}")        
        print(f"  Output : {ob1.merge_v3(lists)}")        


if __name__ == '__main__':
    main()
