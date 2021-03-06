#!/usr/bin/env python3
"""
Given two words (beginWord and endWord), and a dictionary's word list, find the
length of shortest transformation sequence from beginWord to endWord, such that:

  - Only one letter can be changed at a time.
  - Each transformed word must exist in the word list.

Note:
  - Return 0 if there is no such transformation sequence.
  - All words have the same length.
  - All words contain only lowercase alphabetic characters.
  - You may assume no duplicates in the word list.
  - You may assume beginWord and endWord are non-empty and are not the same.

EXAMPLES

  Input: beginWord = "hit", endWord = "cog",
      wordList = ["hot","dot","dog","lot","log","cog"]
  Output: 5
  Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog" (length = 5)

  Input: beginWord = "hit", endWord = "cog", 
      wordList = ["hot","dot","dog","lot","log"]
  Output: 0
  Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

Ref:
  - https://leetcode.com/problems/word-ladder (Hard)
  - https://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/

"""

from typing import List
from collections import defaultdict


class Solution:

    def ladderLength_v1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """Perform a Bread-First Search (BFS) to guarantee the optimal solution.

        Complexity is O(n^2 m), where n is the number of words in the dictionary
        and m is the length of the word.
        For the worst case, each word in the dictionary needs to check with each other.
        Thus, O(n^2).  The cost to get the distance of two words is m.
        """
        def word_distance(w1, w2):
            """Return the distance of two words (of the same length)."""
            n = 0
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    n += 1
            return n

        if beginWord == endWord:
            return 1

        queue = [beginWord]
        visited = set([beginWord])
        length = 2
        while queue:
            n = len(queue)
            for i in range(n):
                curr = queue.pop(0)
                for w in wordList:
                    if w in visited:
                        continue
                    if word_distance(curr, w) == 1:
                        if w == endWord:
                            return length
                        else:
                            queue.append(w)
                            visited.add(w)
            length += 1

        return 0

    def ladderLength_v2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """Use word patterns to speed up distance comparison.
        E.g., 
            h*t -> [hit, hat, hot, ...]
            do* -> [dog, dot, ...]
        """

        # Sanity check
        if endWord not in wordList:
            return 0

        # Pre-process all words and built indices
        graph = defaultdict(list)   # patterns back to words
        for word in wordList:
            for i in range(len(word)):
                pattern = word[0:i] + '*' + word[i+1:]
                graph[pattern].append(word)

        # Begin to search
        queue = [beginWord]
        visited = set()
        length = 1
        while queue:
            for word in queue:
                for i in range(len(word)):
                    pattern = word[0:i] + '*' + word[i+1:]
                    for node in graph[pattern]:
                        if node == endWord:
                            return length + 1
                        elif node in visited:
                            continue
                        else:
                            queue.append(node)
                            visited.add(node)
            length += 1
        return 0

    def ladderLength_v3(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """Two-side BFS -- search from both begin and end.

        Use two queues -- queue0 and queue1. 
        Then either use a flag to indicate the direction or swap these two queues.
        """

        # Sanity check
        if endWord not in wordList:
            return 0

        graph = defaultdict(list)   # patterns back to words
        for word in wordList:
            for i in range(len(word)):
                pattern = word[0:i] + '*' + word[i+1:]
                graph[pattern].append(word)

        # Begin to search
        queue0 = [beginWord]
        queue1 = [endWord]
        visited = set([beginWord, endWord])
        length = 1

        while queue0 and queue1:
            tmp_queue = list()
            for word in queue0:
                for i in range(len(word)):
                    pattern = word[0:i] + '*' + word[i+1:]
                    for node in graph[pattern]:
                        if node in queue1:
                            return length + 1
                        elif node in visited:
                            continue
                        else:
                            tmp_queue.append(node)
                            visited.add(node)
            length += 1
            queue0 = tmp_queue

            # Swap queues
            queue0, queue1 = queue1, queue0

        return 0


def main():
    test_data = [
        ['hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'], 5],
        ['hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log'], 0],
        ["red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"], 4],
        ['qa', 'sq', ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln",
         "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo",
         "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh",
         "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb",
         "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh",
         "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex",
         "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"], 5],
    ]

    sol = Solution()
    for beginWord, endWord, wordList, ans in test_data:
        print("# Input: {}, {}, {} ({})".format(
            beginWord, endWord, wordList, ans))
        print("  Output v1 = {}".format(
            sol.ladderLength_v1(beginWord, endWord, wordList)))
        print("  Output v2 = {}".format(
            sol.ladderLength_v2(beginWord, endWord, wordList)))
        print("  Output v3 = {}".format(
            sol.ladderLength_v3(beginWord, endWord, wordList)))


if __name__ == "__main__":
    main()
