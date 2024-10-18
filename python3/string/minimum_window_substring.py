"""
# Minimum Window Substring

Given a (long) string S and a (short) string T, find the minimum window (substring) in S
which will contain all the characters in T in complexity O(n).

EXAMPLES:
```
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Input: S = "AA", T = "AA"
Output: "AA"

Input: S = "AB", T = "CDEFGAB"
Output: ""
```

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
```
L -------------- R , Move R until it contains all characters of T
        L------- R , Move L until the last point that it still contains T. (This is a candidate)
         L-------R , Move L further until it doesn't contain T.
         L---------------R , Move R again until it contains T.
```
REFERENCE:
  - https://leetcode.com/problems/minimum-window-substring/ (Hard)

"""

from collections import Counter


class Solution:

    def minWindow_v1(self, s: str, t: str) -> str:
        """Sliding window.
        Use Container to track the contents.
        Use a special logic "curr_distinct_chars" to check completeness.

        Time complexity: O(|s| + |t|)
        Space complexity: O(|s| + |t|)
        """
        counter_t = Counter(t)
        counter_w = Counter()
        num_distinct_chars = len(counter_t)
        curr_distinct_chars = 0

        min_window = ''
        l, r = 0, 0   # left and right pointer

        while r < len(s):
            c = s[r]
            counter_w[c] += 1
            if counter_w[c] == counter_t[c]:
                curr_distinct_chars += 1

            # Contract by moving the l pointer
            while l <= r and curr_distinct_chars == num_distinct_chars:
                window = s[l:r+1]
                if not min_window or (len(window) < len(min_window)):
                    min_window = window

                # Remove the current char.
                c = s[l]
                if counter_w[c] == counter_t[c]:
                    curr_distinct_chars -= 1
                counter_w[c] -= 1
                l += 1

            r += 1

        return min_window

    def minWindow_v2(self, s: str, t: str) -> str:
        """Sliding window.
        Use a function to check if one container includes another.
        """

        def contains(c1: Counter, c2: Counter) -> bool:
            """Check if c1 is a superset of c2."""
            return all([c1[k] >= v for k, v in c2.items()])

        counter_t = Counter(t)
        counter_w = Counter()
        l = 0
        min_window = ''
        for r, c in enumerate(s):
            counter_w[c] += 1
            while contains(counter_w, counter_t) and (l <= r):
                win = s[l:r+1]
                if not min_window or (len(win) < len(min_window)):
                    min_window = win
                counter_w[s[l]] -= 1
                l += 1
        return min_window


def main():
    test_data = [
        ["ADOBECODEBANC", "ABC", "BANC"],
        ["A", "A", "A"],
        ["AA", "AA", "AA"],
        ["AB", "CDEFGAB", ""],
    ]

    ob1 = Solution()
    for s, t, ans in test_data:
        print(f"# Input  : {s}, {t} (ans='{ans}')")
        print(f"  - output v1 = '{ob1.minWindow_v1(s, t)}'")
        print(f"  - output v2 = '{ob1.minWindow_v2(s, t)}'")


if __name__ == "__main__":
    main()

