#!/usr/bin/env python3
"""
Given two strings text1 and text2, return the length of their longest common
subsequence (LCS).

A subsequence of a string is a new string generated from the original string
with some characters(can be none) deleted without changing the relative order of
the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is
not). A common subsequence of two strings is a subsequence that is common to
both strings.

If there is no common subsequence, return 0.

EXAMPLES:
	Input: text1 = "abcde", text2 = "ace" 
	Output: 3  
	Explanation: LCS is "ace"

	Input: text1 = "abc", text2 = "abc"
	Output: 3
	Explanation: LCS is "abc"

	Input: text1 = "abc", text2 = "def"
	Output: 0
	Explanation: No LCS.

Constraints:
    1 <= text1.length <= 1000
    1 <= text2.length <= 1000
    The input strings consist of lowercase English characters only.

REFERENCE:
  - https://leetcode.com/problems/longest-common-subsequence/ (Medium)
  - https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/


"""

from typing import List


class Solution:
    def longestCommonSubsequence_v1(self, text1: str, text2: str) -> int:
        """Brute force. Complexity is O(n * 2^n). """
        def get_all_seq(pre: str, text: str) -> List[str]:
            # termination conditions
            if not text:
                return [pre]
            r = []
            c = text[0]
            r.extend(get_all_seq(pre + c, text[1:]))
            r.extend(get_all_seq(pre, text[1:]))
            return r

        # Find  all combinations
        s1 = set(get_all_seq('', text1))
        s2 = set(get_all_seq('', text2))

        # Find LCS
        lcs = ''
        n = 0
        for x in s1:
            if len(x) < n:
                continue
            if x in s2:
                lcs = x
                n = len(x)

        # print("LCS =", lcs)
        return n

    def longestCommonSubsequence_v2(self, text1: str, text2: str) -> int:
        """Use recursion.  Slow."""
        def lcs(n, text1, text2):
            if not text1 or not text2:
                return n

            for i, c in enumerate(text1):
                # find a c that also is in text2
                j = text2.find(c)
                if j < 0:
                    continue

                # use it
                n1 = lcs(n+1, text1[i+1:], text2[j+1:])
                # or not
                n2 = lcs(n, text1[i+1:], text2)
                n = max(n1, n2)
                break

            return n

        return lcs(0, text1, text2)

    def longestCommonSubsequence_v3(self, text1: str, text2: str) -> int:
        """The Optimal Structure method from geeksforgeeks.org.

        The logic is simple and elegant!  Yet there are duplicated calls.
        Complexity O(2^n).
        """
        def lcs(text1, text2, m, n):
            # termination condition
            if m == 0 or n == 0:
                return 0
            elif text1[m-1] == text2[n-1]:
                return 1 + lcs(text1, text2, m-1, n-1)
            else:
                return max(lcs(text1, text2, m, n-1), lcs(text1, text2, m-1, n))

        return lcs(text1, text2, len(text1), len(text2))

    def longestCommonSubsequence_v4(self, text1: str, text2: str) -> int:
        """Use a (n+1) x (m+1) matrix to track the status.
        Complexity is O(n x m).

        Input: "abcde", "ace" 

                 a  b  c  d  e
              0  0  0  0  0  0
           a  0 (1) 1  1  1  1
           c  0  1  1 (2) 2  2
           e  0  1  1  2  2 (3)

        Input: 'aggtab', 'gxtxayb'

                 a  g  g  t  a  b
              0  0  0  0  0  0  0
           g  0  0 (1)(1) 1  1  1
           x  0  0  1  1  1  1  1
           t  0  0  1  1 (2) 2  2
           x  0  0  1  1  2  2  2
           a  0 (1) 1  1  2 (3) 3
           y  0  1  1  1  2  3  3
           b  0  1  1  1  2  3 (4)

        """
        def lcs(x, y):
            m = len(x)
            n = len(y)
            L = [[0]*(n+1) for i in range(m+1)]

            for i in range(1, m+1):
                for j in range(1, n+1):
                    if x[i-1] == y[j-1]:
                        # carry from upper left
                        L[i][j] = L[i-1][j-1] + 1
                    else:
                        # carry from left or top
                        L[i][j] = max(L[i-1][j], L[i][j-1])
            return L[m][n]

        return lcs(text1, text2)


def main():
    test_data = [
        ['abcde', 'ace'],
        ['abc', 'abc'],
        ['abc', 'def'],
        ['abcdgh', 'aedfhr'],
        ['aggtab', 'gxtxayb'],
        ["pcbmdupybalwpkbidypqbwhefijytypwdwbsharqdurkrslqlqla",
            "jodcpirubsryvudgpwncrmtypatunqpkhehuhkdmbctyxghsfktaz"],

    ]

    sol = Solution()
    for t1, t2 in test_data:
        print("# Input = {}, {}".format(t1, t2))

        if len(t1) < 10 and len(t2) < 10:
            # These methods are not efficient enough to handle complex cases
            print("  Output = {}".format(sol.longestCommonSubsequence_v1(t1, t2)))
            print("  Output = {}".format(sol.longestCommonSubsequence_v2(t1, t2)))
            print("  Output = {}".format(sol.longestCommonSubsequence_v3(t1, t2)))

        # This can handle all cases
        print("  Output = {}".format(sol.longestCommonSubsequence_v4(t1, t2)))


if __name__ == "__main__":
    main()
