#!/usr/bin/env python3
"""
Given a sorted array nums, remove the duplicates in-place such that
each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

Examples:
  Input:  [1,1,2]
  Output: [1,2,...], 2 

  Input:  [0,0,1,1,1,2,2,2,3,4,],
  Output: [0,1,2,3,4,...], 5 


Technologies:

Ref:
  - https://www.programcreek.com/2014/05/leetcode-reverse-words-in-a-string-ii-java/ 
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Use n and to track the previus unique position and value."""
        n = 0
        prev = None
        for x in nums:
            if x != prev:
                nums[n] = prev = x
                n += 1
        return n


def main():
    """Main function"""
    test_data = [
        [1,1,2],
        [0,0,1,1,1,2,2,3,3,4],
        [1],
        [1,1,1,1,1],
        []
    ]

    sol = Solution()
    for nums in test_data:
        print("\n# Input = '{}':".format(nums))

        n = sol.removeDuplicates(nums)
        if n > 0:
            print(" output> nums={}, n={}".format(nums[0:n], n))
        else:
            print(" output> nums={}, n={}".format(nums, n))


if __name__ == "__main__":
    main()
