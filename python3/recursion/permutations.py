"""
Given an array nums of distinct integers, return all the possible 
permutations. You can return the answer in any order.

Example 1:
  Input: nums = [1,2,3]
  Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
   Input: nums = [0,1]
   Output: [[0,1],[1,0]]

Example 3:
  Input: nums = [1]
  Output: [[1]]
 
Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
  
REFERENCE:
 - https://leetcode.com/problems/permutations/description/ (Medium)

"""

from typing import List


class Solution:
    def permute_v1(self, nums: List[int]) -> List[List[int]]:
        def helper(nums: List[int], comp: List[int], results: List[List[int]]):
            if not nums:
                results.append(comp.copy())
            else:
                for i, x in enumerate(nums):
                    comp.append(x)
                    helper(nums[0:i] + nums[i+1:], comp, results)
                    # restore comp
                    comp.pop()

        results = list()
        helper(nums, [], results)
        return results

    def permute_v2(self, nums: List[int]) -> List[List[int]]:
        def helper(nums: List[int], comp: List[int], results: List[List[int]]):
            if not nums:
                results.append(comp.copy())
            else:
                for _ in range(len(nums)):
                    x = nums.pop(0)
                    comp.append(x)
                    helper(nums, comp, results)
                    # restore comp & nums
                    comp.pop()
                    nums.append(x)

        results = list()
        helper(nums, [], results)
        return results
    
    
def main():
    test_data = [
        [1, 2, 3],
        [0, 1],
        [1]
    ]

    ob1 = Solution()
    for nums in test_data:
        print(f"# Input = {nums}")
        print(f"  Output v1 = {ob1.permute_v1(nums)}")
        print(f"  Output v2 = {ob1.permute_v2(nums)}")


if __name__ == "__main__":
    main()

