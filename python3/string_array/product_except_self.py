#!/usr/bin/env python3
"""
TASK:

Given an array nums of n integers where n > 1,  return an array output such that
output[i] is equal to the product of all the elements of nums except nums[i].

Example:

  Input:  [1,2,3,4]
  Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any
prefix or suffix of the array (including the whole array) fits in
a 32 bit integer.

Note: 
 - Please solve it without division and in O(n).

Follow up:
 - Could you solve it with constant space complexity?
   Hint: the output array does not count as extra space for the purpose of space
   complexity analysis.

"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Store fowards and backwards.

        Use two array to store the foward products and backward products.

            fwd = [
                1,
                num[0],
                num[0] * num[1],
                ...
                num[0] * num[1] * ... num[n-1]
            ]

            bwd = [
                1,
                num[n-1],
                num[n-1] * num[n-2],
                ...
                num[n-1] * num[n-2] * ... num[0]
            ]

        Building these two arrays takes 2 * O(n). 
        They have all of the components that we need to build the final results.

            results = [
                fwd[0] * bwd[n-1],
                fwd[1] * bwd[n-2],
                ...,
                fwd[n-1] * bwd[0]
            ]

        Again, the complexity is O(n).
        The final time complexity is 3 * O(n) which is in the order of O(n).

        Space complexity is 2 O(n).  This can be reduced if:
          1. Use the output array for fwd.
          2. Re-use the input array for bwd.

        """
        # Use an array to store forward products.
        def _cum_products(nums, forward=True):
            p = 1
            a = [p]
            n = len(nums)
            r = range(0, n-1) if forward else range(n-1, 0, -1)
            for i in r:
                p *= nums[i]
                a.append(p)
            return a

        # Have two cumulated products, forward and backwards
        fwd = _cum_products(nums, True)
        bwd = _cum_products(nums, False)

        # Now, construct the final results
        n = len(nums)
        j = n - 1
        results = list()
        for i in range(n):
            results.append(fwd[i] * bwd[j])
            j -= 1
        return results


def main():
    """Main function"""
    test_data = [
        [1,2,3,4],
        [0,2,3,4],
        [1,-1] * 10,
        [1, 2],
    ]

    sol = Solution()
    for nums in test_data:
        print("\n# Input: {}:".format(nums))
        print("  Output: {}".format(sol.productExceptSelf(nums)))


if __name__ == "__main__":
    main()
