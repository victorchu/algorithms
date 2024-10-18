"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 
Constraints:
  - 1 <= s.length <= 105
  - s consists of lowercase English letters.

Technologies:
  - Recurssion
  - Reverse string s[::-1]

"""

class Solution:
    def validPalindrome_v1(self, s: str) -> bool:
        """Compare one character at a time. Use recursion.
        
        Time: O(n), Space: O(n) due to recursion
        """
        # Special case
        if not s:
            return True
        
        def helper(s, i: int, j: int, skip: int) -> bool:
            if j <= i:
                return True
            if s[i] == s[j]:
                return helper(s, i+1, j-1, skip)
            elif skip > 0:
                return helper(s, i+1, j, skip-1) or helper(s, i, j-1, skip-1)
            else:
                return False

        return helper(s, 0, len(s) - 1, 1)    
    
    def validPalindrome_v2(self, s: str) -> bool:
        """Use a loop to handle the recursion.  Still one character at a time.
        
        Time: O(n), Space: O(n)
        """
        # Special case
        if not s:
            return True
        
        q = [(0, len(s) - 1, 1)]
        while q:
            (i, j, skip) = q.pop()
            if (j <= i):
                return True
            if s[i] == s[j]:
                q.append([i+1, j-1, skip])
            elif skip:
                q.append([i+1, j, 0])
                q.append([i, j-1, 0])
        return False

    def validPalindrome_v3(self, s: str) -> bool:
        """Add string comparison. This faster than the above two.
        
        Time: O(n), Space: O(n)
        """
        if s == s[::-1]:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                skipL = s[i+1:j+1]
                skipR = s[i:j]
                return skipL==skipL[::-1] or skipR==skipR[::-1]
        return True


def main():
    """Main function"""
    test_data = [
        "aba",
        "abca",
        "caba",
        "abc",
        "acbda",
        ""
    ]

    sol = Solution()
    for s in test_data:
        print(f"\n# Input: '{s}'")
        print(f"  Output: {sol.validPalindrome_v1(s)}")
        print(f"  Output: {sol.validPalindrome_v2(s)}")
        print(f"  Output: {sol.validPalindrome_v3(s)}")


if __name__ == "__main__":
    main()
