#!/usr/bin/env python3
"""
Given an input string (s) and a pattern (p),
implement regular expression matching with support for '.' and '*'.

  '.' Matches any single character.
  '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

NOTE:
  - s could be empty and contains only lowercase letters a-z.
  - p could be empty and contains only lowercase letters a-z, and characters like . or *.

EXAMPLES:

  Input: s = "aa", p = "a"
  Output: False
  Explanation: "a" does not match the entire string "aa".

  Input: s = "aa", p = "a*"
  Output: True
  Explanation: '*' means zero or more of the preceding element, 'a'.
			   Therefore, by repeating 'a' once, it becomes "aa".

  Input: s = "ab", p = ".*"
  Output: True
  Explanation: ".*" means "zero or more (*) of any character (.)".

  Input: s = "aab", p = "c*a*b"
  Output: True
  Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

  Input: s = "mississippi", p = "mis*is*p*."
  Output: False
  Explanation: p cannot cover the the 'i' in the square brackets -- mississ[i]ppi"

REFERENCE:
  - https://leetcode.com/problems/regular-expression-matching/ (Hard)

"""


import numpy as np
from typing import List


class Solution:
    def isMatch_v1(self, s: str, p: str) -> bool:
        """Recursion."""
        class PatternNode:
            """Use a class to represent a unit in the pattern. """
            def __init__(self, val, star=False):
                self.val = val
                self.star = star

            def __str__(self):
                return self.val + '*' if self.star else self.val

            def match(self, c):
                return self.val == c or self.val == '.'

            def is_match_all(self):
                return self.star and (self.val == '.')

        def parse_pattern(p):
            """Compile and compact the pattern string."""
            plist = list()
            i, n = 0, len(p)
            while i < n:
                c1 = p[i]
                if i < n - 1:
                    c2 = p[i+1]
                    if c2 == '*':
                        plist.append(PatternNode(c1, True))
                        i += 2
                    else:
                        plist.append(PatternNode(c1))
                        i += 1
                else:
                    plist.append(PatternNode(c1))
                    i += 1
            return plist

        def combine_patterns(plist):
            """Remove redundancy in the pattern."""
            result = list()
            prev = None
            for x in plist:
                if prev and x.star and prev.star:
                    if x.val == prev.val or prev.val == '.':
                        continue
                    if x.val == '.':
                        for j in range(len(result)-1, -1, -1):
                            if result[j].star:
                                del result[j]
                            else:
                                break
                result.append(x)
                prev = x
            return result
                
        def match(s, plist):
            # Termination conditions
            if not s:
                if not plist:
                    return True
                for x in plist:
                    if not x.star:
                        return False
                return True
            elif not plist:
                return False

            c = s[0]
            x = plist[0]
            # print("[DEBUG] {} vs {}".format(s, str(x)))

            # Handle non-star
            if not x.star:
                if x.match(c):
                    return match(s[1:], plist[1:])
                else:
                    return False
                
            # Handle star
            else:
                if x.match(c):
                    # May use the star as zero or many
                    return match(s[1:], plist) or match(s, plist[1:])
                else:
                    # Skip the star pattern (*=0) due to mismatch
                    return match(s, plist[1:])

        plist = combine_patterns(parse_pattern(p))
        #print(" - parsed pattern =", ", ".join(["[{}]".format(str(x)) for x in plist]))
        return match(s, plist)

    def isMatch_v2(self, s: str, p: str) -> bool:
        """Use a matrix to track all possible combinations.
        Complexity is O(nxm)

        Examples:

        Input: s = "aab", p = "c*a*b" => True

               a a b
             T F F F
           c F F F F
           * T F F F
           a F T F F
           * T T T F
           b F F F T

        Input: s = "aabxc", p = "a*.*c" => True

               a a b x c
             T F F F F F
           a F T F F F F
           * T T T F F F
           . F T T T F F
           * T T T T T T
           c F F F F F T 

        Input: s = 'mississippi', p = 'mis*is*p*.' => False (missed an 'i')

               m i s s i s s i p p i
             T F F F F F F F F F F F
           m F T F F F F F F F F F F
           i F F T F F F F F F F F F
           s F F F T F F F F F F F F
           * F F F T T F F F F F F F
           i F F F F F T F F F F F F 
           s F F F F F F T F F F F F
           * F F F F F F T T F F F F  <-- last valid match (T) at s
           p F F F F F F F F F F F F  <-- disconnected from T
           . F F F F F F F F F F F F

        """
        np = len(p)
        ns = len(s)

        # Create a status matrix of (np+1) x (ns+1), covering
        # all possible ways to match. 
        dp = [[False] * (ns + 1) for _ in range(np + 1)]

        # Initialize corner cases when len(s) == 0
        dp[0][0] = True
        for i in range(2, np + 1):
            dp[i][0] = dp[i-2][0] and (p[i-1] == '*')
        
        for x in range(np):
            i = x + 1
            for y in range(ns):
                j = y + 1
                # Non-star: check the diagnal (upper-left) status
                if p[x] != '*':
                    dp[i][j] = \
                        dp[i-1][j-1] and \  
                        (p[x] == s[y] or p[x] == '.')
                # Star.
                else:
                    dp[i][j] = \
                        dp[i-2][j] or \     # 1. no use
                        dp[i-1][j] or \     # 2. first use
                        (dp[i][j-1] and (p[x-1] == s[y] or p[x-1] == '.'))  # 3. repeated use

        return dp[-1][-1]


def main():
    """Main function"""
    sample_data = [
        ['ab', 'b*.*', True],
        ['ab', '.*b*c', False],
        ['aa', 'a', False],
        ['aa', 'a*', True],
        ['ab', '.*', True],
        ['a', 'ab*', True],
        ['aab', 'c*a*b', True],
        ['mississippi', 'mis*is*p*.', False],
        ['bbbbba', '.*a*a', True],
        ['aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c', False],
        ["cbaacacaaccbaabcb", "c*b*b*.*ac*.*bc*a*", True]
    ]

    sol = Solution()
    for s, p, expected in sample_data:
        print("# Input = '{}', '{}'".format(s, p))

        ans = sol.isMatch_v1(s, p)
        print("  Output v1 = {} : {}".format(ans, 'OK' if ans==expected else '*** WRONG ***'))
        ans = sol.isMatch_v2(s, p)
        print("  Output v2 = {} : {}".format(ans, 'OK' if ans==expected else '*** WRONG ***'))


if __name__ == "__main__":
    main()
