"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

  * For example, for arr = [1,2,3], the following are all the permutations of arr: 
    [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their 
lexicographical order, then the next permutation of that array is the permutation that follows it in 
the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest
possible order (i.e., sorted in ascending order).

  * For example, the next permutation of arr = [1,2,3] is [1,3,2].
  * Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
  * While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a
    lexicographical larger rearrangement. 

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Examples:
    Input: nums = [1,2,3]
    Output: [1,3,2]

    Input: nums = [1,3,2]
    Output: [2,1,3]

    Input: nums = [3,2,1]
    Output: [1,2,3]

    Input: nums = [1,1,5]
    Output: [1,5,1]

    Input: nums = [1,3,4,2]
    Output: [1,4,2,3]
 
Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 100

Technologies:
    nums[i:] = sorted(nums[i:])
    nums.sort()
    swap: x[i], x[j] = x[j], x[i]
    for ... else
"""

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """Find values to swap, then sort the rest.
        Time Complexity: O(n^2), Space: O(n) 
        """
        def find_swap_index(nums, start_idx) -> int:
            """The index to the smallest number larger than a threshold"""
            threshold = nums[start_idx-1]
            swap_idx = -1
            swap_val = 101   # the maximum value + 1, per the constraint
            for i in range(start_idx, len(nums)):
                val = nums[i]
                if (val > threshold) and (threshold < swap_val):
                    swap_idx = i
                    swap_val = val
            return swap_idx
            
        def permute(nums, ref_idx) -> bool:
            swap_idx = find_swap_index(nums, ref_idx + 1)
            if swap_idx >= 0:
                nums[ref_idx], nums[swap_idx] = nums[swap_idx], nums[ref_idx]
                nums[ref_idx+1:] = sorted(nums[ref_idx+1:])
                return True
            else:
                return False

        for i in range(len(nums)-2, -1, -1):
            if permute(nums, i):
                break
        else:
            nums.sort()


def main():
    test_data = [
        [[1,3,2], [2,1,3]],
        [[1,2,3], [1,3,2]],
        [[3,2,1], [1,2,3]],
        [[1,1,5], [1,5,1]],
        [[1,3,4,2], [1,4,2,3]],
    ]

    ob1 = Solution()
    for nums, ans in test_data:
        print(f"\n# Input = {nums}, Expected = {ans}")
        x = nums.copy()
        ob1.nextPermutation(x)
        print(f"  output v1 = {x} ...... {'ok' if x==ans else 'ERROR'}")


if __name__ == "__main__":
    main()

