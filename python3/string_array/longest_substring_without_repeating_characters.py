#!/usr/bin/env python3
"""
Given a string, find the length of the longest substring without repeating characters.

Examples:
  Input: "abcabcbb"
  Output: 3
  Explanation: "abc".

Ref:
- https://leetcode.com/problems/longest-substring-without-repeating-characters/ (Medium)
- https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/

"""


class Solution:

    def method_v1(self, s: str) -> int:
        """Simple, brute force method.

        Complexity: 
           All combinations: n + (n-1) + (n-2) ... + 1 ~= n(n-1)/2
           Then it takes time to check validity O(n)
           Total is O(n^3)
        """
        def is_valid(s: str):
            char_set = set(s)
            return len(char_set) == len(s)

        max_len = 0
        substr = ''
        n = len(s)
        for i in range(n):
            for j in range(i+max_len+1, n+1):
                tmp = s[i:j]
                if is_valid(tmp):
                    max_len = j - i
                    substr = tmp
                else:
                    break
        #print("[DEBUG] len = {}, substr = {}".format(max_len, substr))
        return max_len

    def method_v2(self, s: str) -> int:
        """Linear time.
        Here we track the current substring. 
        Then deal with the next character, on whether
        it is new or repeated.  Adjust the current substring accordingly.
        """
        curr_len, max_len = 0, 0
        i = 0               # point to begin of the substring.
        visited = set()     # use a set to track characters in the substring

        # Iterate through the string; use j to track the current position
        for j, c in enumerate(s):
            if c in visited:
                # find the location of the repeated character
                for k in range(i, j):
                    x = s[k]
                    if x == c:
                        i = k + 1
                        break
                    else:
                        visited.remove(x)
                        curr_len -= 1
            else:
                visited.add(c)
                curr_len += 1
                if curr_len > max_len:
                    max_len = curr_len
        return max_len


# ----------------
#   Main
# ----------------
def main():
    """Main function"""
    test_data = ["abcabcbb",
                 "bbbbb",
                 "pwwkew"]
    obj = Solution()
    for s in test_data:
        print("# Checking '{}':".format(s))
        print("  - method 1> '{}'".format(obj.method_v1(s)))
        print("  - method 2> '{}'".format(obj.method_v2(s)))


if __name__ == "__main__":
    main()
