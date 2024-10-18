"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]
    Explanation: [4,9] is also accepted.
 

Constraints:
    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000

Reference:
  - https://leetcode.com/problems/intersection-of-two-arrays/
"""
from typing import List 


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Use Set."""
        s = set(nums1)
        t = set(nums2)
        return list(s & t)
    

def main():
    test_data = [
        [[1,2,2,1], [2, 2], [2]],
        [[4,9,5], [9,4,9,8,4], [9, 4]]
    ]

    ob1 = Solution()
    for nums1, nums2, ans in test_data:
        print(f"\n# Input = {nums1}, {nums2} ...... {ans}")
        print(f"  output 1 = {ob1.intersection(nums1, nums2)}")


if __name__ == "__main__":
    main()

