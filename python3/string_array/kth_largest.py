#!/usr/bin/env python3
"""
Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example, given [3,2,1,5,6,4] and k = 2, return 5.

Ref:
 - https://leetcode.com/problems/kth-largest-element-in-an-array/ (Medium)
 - https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

"""

import heapq


class Solution:
    def method1(self, a, k):
        """Sort first. Then pick up the desired position.
        :param a: Array
        :param k: Index to the k-th largest position.
        """
        # Use the built-in sort method here.
        a.sort()
        n = len(a)
        return a[n - k]


    def method2(sol, a, k):
        """Use a min heap as implemented in heapq library."""
        h = list()   # heap
        for i, x in enumerate(a):
            if i < k or x > h[0]:
                heapq.heappush(h, x)
        return h[0]



def main():
    a = [3, 2, 1, 5, 6, 4]

    sol = Solution()
    print("# Checking {}".format(a))
    for k in range(1, len(a)+1):
        print("- method1(k={}) = {}".format(k, sol.method1(a, k)))
        print("- method2(k={}) = {}".format(k, sol.method1(a, k)))


if __name__ == "__main__":
    main()
