#!/usr/bin/env python3
"""
Given an unsorted array A of size N that contains only non negative integers,
find a continuous sub-array that adds to a given number S and return the left
and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on
moving from left to right.

Note:
- You have to return an ArrayList consisting of two elements left and right.
  In case no such subarray exists return an array consisting of element -1.

Example 1:

  Input:
    N = 5, S = 12
    A[] = {1,2,3,7,5}
  Output: 2 4
  Explanation: The sum of elements from 2nd position to 4th position is 12.

Example 2:

  Input:
    N = 10, S = 15
    A[] = {1,2,3,4,5,6,7,8,9,10}
  Output: 1 5
  Explanation: The sum of elements from 1st position to 5th position is 15.

Your Task:

You don't need to read input or print anything.
The task is to complete the function subarraySum() which takes arr, N, and S as 
input parameters and returns an ArrayList containing the starting and ending positions of the first such occurring subarray from the left where sum equals to S. The two indexes in the array should be according to 1-based indexing. If no such subarray is found, return an array consisting of only one element that is -1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
  1 <= N <= 105
  0 <= Ai <= 109
  0<= S <= 109

Ref: 
  - https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/
"""

class Solution:
    def subArraySum(self, arr, n, s): 
        if s < 0:
            return [-1]

        iL, iR = 0, -1
        total = 0
        for iR in range(0, n):
            total += arr[iR]
            
            while total > s:
                total -= arr[iL]
                iL += 1

            if total == s and iL <= iR:
                return (iL+1, iR+1)

        return [-1]
        

def main():
    test_data = [
        [[1,2,3,7,5], 5, 12],
        [[1,2,3,4,5,6,7,8,9,10], 10, 15],
        [[1,2,3,4,5,6,7,8,9,10], 10, 16],
        [[1,2,3,4,5,6,7,8,9,10], 10, 16, [-1]],
        [[1,2,3,4,5,6,7,8,9,10], 10, 0, [-1]],
        [[1, 0], 2, 0, [2,2]]    ]

    sol = Solution()
    for (arr, n, s) in test_data:
        print(f"# Input  : {arr}, {n}, {s}")
        print(f"  Output: {sol.subArraySum(arr, n, s)}")


if __name__ == "__main__":
    main()