#!/usr/bin/env python3
"""
Given a paragraph and a list of banned words, return the most frequent word that
is not in the list of banned words.  It is guaranteed there is at least one word
that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of
punctuation.  Words in the paragraph are not case sensitive.  The answer is in
lowercase.

EXAMPLES:
  Input: 
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
  Output: "ball"

HINTS:
  - Any non-letter character shall be treated as a delimiter.
    Alternative, we can use (white spaces, ! ? , . ;) for this problem.

REFERENCE:
  - https://leetcode.com/problems/most-common-word/ (Easy)

"""

import re
from collections import defaultdict, Counter
from typing import List


class Solution:
    def mostCommonWord_v1(self, paragraph: str, banned: List[str]) -> str:
        """Regex and dictionary."""
        # Pre-processing words
        banned_set = set(banned)
        words = [w.lower() for w in re.split(r'[^\w]+', paragraph) if w]
        words = [w for w in words if w not in banned_set]

        # Get word counts
        count = defaultdict(int)
        for w in words:
            count[w] += 1

        # Find the most common word
        common_word = None
        max_count = 0
        for w, c in count.items():
            if c > max_count:
                max_count = c
                common_word = w
        return common_word

    def mostCommonWord_v2(self, paragraph: str, banned: List[str]) -> str:
        """Regex and max (with key)"""
        banned_set = set(banned)
        words = [w.lower() for w in re.split(r'[^\w]+', paragraph) if w]
        words = [w for w in words if w not in banned_set]
        count = defaultdict(int)
        for w in words:
            count[w] += 1
        return max(count, key=count.get)

    def mostCommonWord_v3(self, paragraph: str, banned: List[str]) -> str:
        """Regex and Counter."""
        banned_set = set(banned)
        words = [w.lower() for w in re.split(r'[^\w]+', paragraph) if w]
        words = [w for w in words if w not in banned_set]
        counter = Counter(words)
        return counter.most_common(1)[0][0]


def main():
    test_data = [
        ["Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]],
        ["Bob. hIt baLl", ["bob", "hit"]],
    ]

    sol = Solution()
    for paragraph, banned in test_data:
        print("# Input: {}, {}".format(paragraph, banned))
        print("  Output v1 = {}".format(
            sol.mostCommonWord_v1(paragraph, banned)))
        print("  Output v2 = {}".format(
            sol.mostCommonWord_v2(paragraph, banned)))
        print("  Output v3 = {}".format(
            sol.mostCommonWord_v3(paragraph, banned)))


if __name__ == "__main__":
    main()
