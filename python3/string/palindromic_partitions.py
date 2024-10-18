"""
# Palindromic Partitions

Partition a string such that every substring of the partition is a palindrome.

"A palindrome is a word, number, phrase, or other sequence of characters which
reads the same backward as forward, such as madam, racecar." -- Wikipedia

EXAMPLES:
```
Input: "aab"
Output: [
    ['a', 'a', 'b'],
    ['aa', 'b']
]

Input: "nitin"
Output: [
    ['n', 'i', 't', 'i', 'n'],
    ['n', 'iti', 'n'],
    ['nitin']
]

Input:  "geeks"
Output: [
    ['g', 'e', 'e', 'k', 's'],
    ['g', 'ee', 'k', 's']
]
```
  
REFERENCE:
  - https://leetcode.com/problems/palindrome-partitioning/ (Medium)
  - https://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/ (Hard)
  - https://en.wikipedia.org/wiki/Palindrome
"""

from typing import List


class Solution:
    def find_all_v1(self, s: str) -> List[List]:
        """Recursion, brute force.
        Time Complexity = O(N * 2^N).  Space Complexity = O(N^2)
        """
        def is_palindrome(s):
            """Check if the specified string is a palindrome"""
            n = len(s)
            return all([s[i] == s[n-i-1] for i in range(n//2)])

        def helper(s, curr_partition: list, result: List[list]):
            if len(s) == 0:
                result.append(curr_partition)

            # Iterate through all sub-strings starting from the beginning            
            for i in range(1, len(s)+1):
                entry = s[0:i]
                if is_palindrome(entry):
                    helper(s[i:], curr_partition + [entry], result)

        # Use the helper function to handle all of the work.
        result = []
        helper(s, list(), result)
        return result

    def find_all_v2(self, s: str) -> List[List]:
        """Merge. This is not more efficient; yet it uses different techniques.
        Time complexity = O(N * 2^N).  Space complexity = O(N^2)
        """
        
        def solver(arr: List[str], result: List):
            # print(f"[DEBUG] Checking {arr} ...")
            if arr not in result:
                result.append(arr)
            else:
                return
            if len(arr) <= 1:
                return
            
            for i in range(len(arr)-1):
                #  Merge right
                if arr[i] == arr[i+1][::-1]:
                    new_arr = arr[:i] + [arr[i] + arr[i+1]] + arr[i+2:]
                    solver(new_arr, result)
                # Merge left and right
                if (i > 0) and (arr[i-1] == arr[i+1][::-1]):
                    new_arr = arr[:i-1] + [arr[i-1] + arr[i] + arr[i+1]] + arr[i+2:]
                    solver(new_arr, result)
            
        result = list()
        solver(list(s), result)
        return result

    def find_all_v3(self, s: str) -> List[List]:
        """Merge. Same as v2; but use a set to store the results.
        The set can only store tuples not lists.
        Tuple manipulation is a little bit tricky.
        """
        def solver(arr: List[str], result: set):
            if (len(arr) <= 1) or (arr in result):
                return
            result.add(arr)

            for i in range(len(arr)-1):
                #  Merge right
                if arr[i] == arr[i+1][::-1]:
                    new_arr = arr[:i] + tuple([arr[i] + arr[i+1]]) + arr[i+2:]
                    solver(new_arr, result)
                # Merge left and right
                if (i > 0) and (arr[i-1] == arr[i+1][::-1]):
                    new_arr = arr[:i-1] + tuple([arr[i-1] + arr[i] + arr[i+1]]) + arr[i+2:]
                    solver(new_arr, result)

        result = set()
        solver(tuple(s), result)
        return list(result)

               
def main():
    """Main function"""
    test_samples = [
        "aab",
        "nitin",
        "geeks",
        "aaracecar",
    ]
    
    def print_partitions(partitions, title):
        print(f"  + {title}")
        for i, p in enumerate(partitions):
            print(f"    {i}. {p}")

    sol = Solution()
    for s in test_samples:
        print(f"# Checking '{s}' ...")
        print_partitions(sol.find_all_v1(s), "v1")
        print_partitions(sol.find_all_v2(s), "v2")
        print_partitions(sol.find_all_v3(s), "v3")
        print()


if __name__ == "__main__":
    main()
