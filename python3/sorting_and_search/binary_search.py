"""
Given a sorted (in ascending order) integer array nums of n elements
and a target value, write a function to search target in nums. If
target exists, then return its index, otherwise return -1.

Examples:

  Input: nums = [-1,0,3,5,9,12], target = 9
  Output: 4
  Explanation: 9 exists in nums and its index is 4

  Input: nums = [-1,0,3,5,9,12], target = 2
  Output: -1
  Explanation: 2 does not exist in nums so return -1
 
Note:
  - You may assume that all elements in nums are unique.
  - n will be in the range [1, 10000].
  - The value of each element in nums will be in the range [-9999, 9999].

Reference:
  - https://leetcode.com/problems/binary-search/ (Easy)
  - https://www.geeksforgeeks.org/binary-search/

"""
from typing import List

class Solution:

    def search_v1(self, nums: List[int], target: int):
        """Recursion.
        
        Time Complexity: O(log N).  Space Complexity: O(log N)
        """
        def helper(nums: List[int], target: int, left: int, right: int) -> int:
            if right < left:
                return -1
            
            middle = (right + left) // 2
            value = nums[middle]
            if value == target:
                return middle
            if value > target:
                return helper(nums, target, left, middle - 1)
            else:
                return helper(nums, target, middle + 1, right)
            
        return helper(nums, target, 0, len(nums)-1)

    def search_v2(self, nums: List[int], target: int):
        """Iterative / Loop.
        
        Time Complexity: O(log N).  Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            val = nums[middle]
            if val == target:
                return middle
            elif val > target:
                # search left
                right = middle - 1
            else:
                # right right
                left = middle + 1
        else:
            return -1


def main():
    a = [-1, 0, 3, 5, 9, 12]
    test_data = [
        [a, 9, 4],
        [a, 2, -1],
        [a, -1, 0],
        [[1, 2], 1, 0],
        [[1, 2], 2, 1],
        [[1], 1, 0],
        [[1], 2, -1],        
    ]

    ob1 = Solution()
    for arr, target, ans in test_data:
        print(f"# Input: {arr}, target={target} --> {ans}")
        print(f"  - Output v1 = {ob1.search_v1(arr, target)}")
        print(f"  - Output v2 = {ob1.search_v2(arr, target)}")


if __name__ == '__main__':
    main()
