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

class Solution:
    def merge_v1(self, lists : List[list]) -> list:
        """ Use a heap for tracking.
        
        Time Complexity: O(N * K * log(K))
        Auxilary Space: O(K) + N
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
        

if __name__ == '__main__':
    main()

