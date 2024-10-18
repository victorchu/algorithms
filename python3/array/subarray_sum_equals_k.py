"""
Given an array of integers nums and an integer k, return the total number of 
subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2

Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2
 
Constraints:
    1 <= nums.length <= 2 * 104
    -1000 <= nums[i] <= 1000    # array values can be negative!
    -107 <= k <= 107            # k can also be negative

Hints:
  * Brute force won't work on a large array (time out).
  * Use a hash table to store the "values" for sums from first element
    the ith element.

Ref:
  * https://www.geeksforgeeks.org/number-subarrays-sum-exactly-equal-k/


"""

from typing import List
from collections import Counter


class Solution:
    def subarraySum_v1(self, nums: List[int], k: int) -> int:
        """Ues brute force, which will cause time out.
        
        Time complexity: O(n^2). Space: O(1)
        """
        retval = 0
        n = len(nums)
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                if curr_sum == k:
                    retval += 1
        return retval

    def subarraySum_v2(self, nums: List[int], k: int) -> int:
        """Use a counter to store accumulate sums from the 
           the beginning.
        
        Time complexity: O(n), Space: O(n)
        """
        res = 0
        prev_sums = Counter()
        curr_sum = 0
        for x in nums:
            curr_sum += x
            if curr_sum == k:
                res += 1

            # E.g., 15 - 10 = 5.  If there is any prev_sum is 5, we can exclude
            # that part to get the target value.
            res += prev_sums[curr_sum - k]
            prev_sums[curr_sum] += 1

        return res


def main():
    test_data = [
        [[1, 1, 1], 2, 2],
        [[1, 2, 3], 3, 2],
    ]

    ob1 = Solution()
    for nums, k, ans in test_data:
        print(f"\n# Input: nums={nums}, k={k} ...... {ans}")
        print(f"  output v1 = {ob1.subarraySum_v1(nums, k)}")
        print(f"  output v2 = {ob1.subarraySum_v2(nums, k)}")


if __name__ == "__main__":
    main()
