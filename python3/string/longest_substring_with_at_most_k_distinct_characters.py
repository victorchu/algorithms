"""
Given a string s and an integer k, return the length of the longest substring of s
that contains at most k distinct characters.

Example 1:
    Input: s = "eceba", k = 2
    Output: 3
    Explanation: The substring is "ece" with length 3.

Example 2:
    Input: s = "aa", k = 1
    Output: 2
    Explanation: The substring is "aa" with length 2.
 
Constraints:
    1 <= s.length <= 5 * 104
    0 <= k <= 50

Technologies:
  * Counter()
  * max()
  * double pointers

"""

from collections import Counter

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """Double pointer + book keeping."""
        c = Counter()
        max_len = 0
        l = 0

        for r in range(len(s)):
            # Expand one
            c[s[r]] += 1
                    
            # Shrink (by moving the left pointer)
            while len(c) > k:
                x = s[l]
                if c[x] > 1:
                    c[x] -= 1
                else:
                    del c[x]
                l += 1

            # Check length
            max_len = max(max_len, r - l + 1)

        return max_len                    
    

def main():
    test_data = [
        ["eceba", 2, 3],
        ["aa", 1, 2],
        ["", 3, 0]
    ]

    ob1 = Solution()
    for s, k, ans in test_data:
        print(f"\n# Input = {s}, {k} ...... {ans}")
        print(f"  output = {ob1.lengthOfLongestSubstringKDistinct(s, k)}")


if __name__ == "__main__":
    main()

