#!/usr/bin/env python3
"""
Given a string S and a string T, find the minimum window in S which will contain
all the characters in T in complexity O(n).

EXAMPLES:
  Input: S = "ADOBECODEBANC", T = "ABC"
  Output: "BANC"

  Input: S = "AA", T = "AA"
  Output: "AA"

NOTE:
  - T may have duplicated letters.
  - If there is no such window in S that covers all characters in T, return the empty string "".
  - If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

HINTS:
  - Use two pointers to create a window of letters in S, which would have all the characters from T.

  - Since you have to find the minimum window in S which has all the characters
    from T, you need to expand and contract the window using the two pointers and
    keep checking the window for all the characters. This approach is also called
    Sliding Window Approach.

    L ------------------------ R , Suppose this is the window that contains all characters of T 
                          
            L----------------- R , this is the contracted window.
                                   We found a smaller window that still contains all the characters in T
                                   When the window is no longer valid, start expanding again using the right pointer. 

REFERENCE:
  - https://leetcode.com/problems/minimum-window-substring/ (Hard)

"""
from collections import Counter


class Solution:

    def minWindow_v1(self, s: str, t: str) -> str:
        """Use a sliding window defined by two pointers.

        Time complexity: O(|s| + |t|)
        Space complexity: O(|s| + |t|)
        """
        ns = len(s)
        counter_t = Counter(t)  # target
        counter_w = Counter()   # sliding window
        required = len(counter_t)   # number of distinct characters in t
        formed = 0              # number of characters satisfied in the window

        min_window = ''
        min_size = None
        l, r = 0, 0   # left and right pointer

        while r < ns:
            # Expand by moving the r one step at a time
            c = s[r]
            if c in counter_t:
                counter_w[c] += 1
                if counter_w[c] == counter_t[c]:
                    formed += 1

            # Contract by moving the l pointer
            while l <= r and formed == required:
                c = s[l]
                if c in counter_t:
                    # Check the new window
                    window = s[l:r+1]
                    n = len(window)
                    if not min_size or n < min_size:
                        min_size = n
                        min_window = window

                    # Remove the current char.
                    if counter_w[c] == counter_t[c]:
                        formed -= 1
                    counter_w[c] -= 1
                l += 1

            r += 1

        return min_window


def main():
    test_data = [
        ["ADOBECODEBANC", "ABC", "BANC"],
        ["A", "A", "A"],
        ["AA", "AA", "AA"],
    ]

    sol = Solution()
    for s, t, ans in test_data:
        print("# Input  : {}, {} --- {}".format(s, t, ans))
        print("  Output v1: '{}'".format(sol.minWindow_v1(s, t)))


if __name__ == "__main__":
    main()
