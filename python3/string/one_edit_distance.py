"""
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

 * Insert exactly one character into s to get t.
 * Delete exactly one character from s to get t.
 * Replace exactly one character of s with a different character to get t.
 
Example 1:

    Input: s = "ab", t = "acb"
    Output: true
    Explanation: We can insert 'c' into s to get t.

    Input: s = "", t = ""
    Output: false
    Explanation: We cannot get t from s by only one step.
 
Constraints:

   0 <= s.length, t.length <= 104
   s and t consist of lowercase letters, uppercase letters, and digits.
"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """Use double pointers moving from both side. The final difference shall be one."""
        len1 = len(s)
        len2 = len(t)
        n = min(len1, len2)
        move1, move2 = 0, 0  # tracking the number of successful moves
        # Forward
        for i in range(n):
            if s[i] == t[i]:
                move1 = i + 1
            else:
                break
        # Backward
        for j in range(1, n-move1+1):
            if s[-j] == t[-j]:
                move2 = j
            else:
                break
        # Gaps
        gap1 = len1 - move1 - move2
        gap2 = len2 - move1 - move2
        print(f"[DEBUG] m1={move1}, m2={move2}, gap1={gap1}, gap2={gap2}")

        # Verification
        if (gap1 == 1 and gap2 <= 1 and gap2 >= 0) or (gap2 == 1 and gap1 <= 1 and gap1 >= 0):
            return True
        else:
            return False
        

def main():
    test_data = [
        ["ab", "acb", True],
        ["acb", "ab", True],
        ["abc", "awc", True],
        ["abd", "axbxd", False],
        ["abc", "abc", False],
        ["", "", False]
    ]

    ob1 = Solution()
    for s, t, ans in test_data:
        print(f"\n# Input = '{s}', '{t}' ...... {ans}")
        print(f"  output 1 = {ob1.isOneEditDistance(s, t)}")


if __name__ == "__main__":
    main()

