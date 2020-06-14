#!/usr/bin/env python3
"""
Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated sequence
of one or more dictionary words.

Note:
  - The same word in the dictionary may be reused multiple times in the segmentation.
  - You may assume the dictionary does not contain duplicate words.

EXAMPLES:

  Input: s = "leetcode", wordDict = ["leet", "code"]
  Output: true   # "leet code".

  Input: s = "applepenapple", wordDict = ["apple", "pen"]
  Output: true  # apple pen apple

  Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
  Output: false

REFERENCE:
  - https://leetcode.com/problems/word-break/ (Medium)
  - https://www.geeksforgeeks.org/word-break-problem-dp-32/

"""

from typing import List


class Solution:
    def wordBreak_v1(self, s: str, wordDict: List[str]) -> bool:
        """Recursion. 

        The worst performance is trying all of the 2^(n-1) partitions.
        There are quite duplications in the pervious implementaiotn.  E.g.

            + 'abcde'
                 - 'bcde' -> ['cde', 'de', 'e', '']
                 - 'cde'
                 - 'de'
                 - 'e'
                 - ''

        """
        def wb(s):
            if s == '':
                return True

            for i in range(1, len(s) + 1):
                if (s[:i] in wordDict) and wb(s[i:]):
                    return True

            return False

        return wb(s)

    def wordBreak_v2(self, s: str, wordDict: List[str]) -> bool:
        """Dynamic programming.

        Here, we try to build up from bottom up.
        """

        if not s:
            return True
        # Convert list to set for faster processing
        wordSet = set(wordDict)
        # Use a list to record breakable substrings
        valid_positions = [0]
        n = len(s)
        for j in range(1, n+1):
            for i in reversed(valid_positions):
                if s[i:j] in wordSet:
                    valid_positions.append(j)
                    break
        return valid_positions[-1] == n

    def wordBreak_v3(self, s: str, wordDict: List[str]) -> bool:
        """Dynamic programming.

        A small variation from the previous approach.
        It tries to reach to the end of the string from each known
        working position.
        """

        if not s:
            return True

        # Convert list to set for faster processing
        wordSet = set(wordDict)

        # Use a list to record breakable substrings
        n = len(s)
        wb = [True] + [False] * n
        for i in range(1, n+1):

            if not wb[i] and (s[0:i] in wordSet):
                wb[i] = True

            if wb[i]:
                for j in range(i+1, n+1):
                    if not wb[j] and s[i:j] in wordSet:
                        wb[j] = True
            if wb[n]:
                return True

        return False


def main():
    dict1 = ["mobile", "samsung", "sam", "sung", "man", "mango", "icecream", "and",
             "go", "i", "like", "ice", "cream"]
    test_data = [
        ['leetcode', ['leet', 'code'], True],
        ['applepenapple', ['apple', 'pen'], True],
        ['catsandog', ['cat', 'cats', 'dog', 'sand', 'and'], False],
        ['ilikesamsung', dict1, True],
        ['iiiiiiii', dict1, True],
        ['ilikelikeimangoiii', dict1, True],
        ['samsungandmango', dict1, True],
        ['samsungandmangok', dict1, False],
        ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
         ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"], False],
    ]

    sol = Solution()
    for s, wordDict, ans in test_data:
        print("# Input = {} (ans={})".format(s, ans))
        if len(s) < 20:
            print("  Output = {}".format(sol.wordBreak_v1(s, wordDict)))
        print("  Output = {}".format(sol.wordBreak_v2(s, wordDict)))
        print("  Output = {}".format(sol.wordBreak_v3(s, wordDict)))


if __name__ == "__main__":
    main()
