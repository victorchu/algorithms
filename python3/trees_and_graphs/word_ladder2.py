#!/usr/bin/env python3
"""
Given two words (beginWord and endWord), and a dictionary's word list, find all
shortest transformation sequence(s) from beginWord to endWord, such that:

  - Only one letter can be changed at a time.
  - Each transformed word must exist in the word list.

Note:
  - Return an empty list if there is no such transformation sequence.
  - All words have the same length.
  - All words contain only lowercase alphabetic characters.
  - You may assume no duplicates in the word list.
  - You may assume beginWord and endWord are non-empty and are not the same.

EXAMPLES

  Input: 
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
  Output:
    [
      ["hit","hot","dot","dog","cog"],
      ["hit","hot","lot","log","cog"]
    ]

  Input: 
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log"]
  Output: []
  Explanation: The endWord "cog" is not in wordList.


HINTS:
  - Need to build a reverse index to speed up matching.
  - Use bread-first search.
  - There may be multiple way to reach a node. Thus, need to track all of these paths.

Ref:
  - https://leetcode.com/problems/word-ladder-ii/ (Hard)
  - https://leetcode.com/problems/word-ladder (Medium)
  - https://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/

"""

from typing import List
from collections import defaultdict


class Solution:

    def findLadders_v1(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """Naive BFS."""
        if endWord not in wordList:
            return []

        # Create the pattern to words mapping
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                graph[word[:i] + "*" + word[i+1:]].append(word)

        ans = []
        queue = {beginWord: [[beginWord]]}
        visited = {beginWord}
        while queue and not ans:
            temp_queue = defaultdict(list)
            for word, paths in queue.items():
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for node in graph.get(word[:i] + "*" + word[i+1:], []):
                        if node == endWord:
                            for path in paths:
                                ans.append(path + [node])
                        if node in visited:
                            continue
                        # Note that there can be more than one way to reach to this node.
                        # Thus, paths is a list of lists (sequences)
                        for path in paths:
                            temp_queue[node].append(path + [node])
            # Has to be updated level-by-level
            visited |= set(temp_queue.keys())
            queue = temp_queue
        return ans

    def findLadders_v2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """Two-end BFS."""
        if endWord not in wordList:
            return []

        # Build index
        graph = dict()
        for word in wordList:
            for i in range(len(word)):
                graph.setdefault(word[:i] + "*" + word[i+1:], []).append(word)

        ans = []
        queue0 = {beginWord: [[beginWord]]}
        queue1 = {endWord: [[endWord]]}
        visited = {beginWord, endWord}
        reverse = False

        while queue0 and queue1 and not ans:
            temp_queue = defaultdict(list)
            for word, seq in queue0.items():
                for i in range(len(word)):
                    for node in graph.get(word[:i] + "*" + word[i+1:], []):
                        # Front and end queues intersept
                        if node in queue1:
                            for x in seq:
                                for y in queue1[node]:
                                    path = y + \
                                        x[::-1] if reverse else x + y[::-1]
                                    ans.append(path)

                        if node in visited:
                            continue

                        # Append node to the seq.
                        # Here we don't need to worry if it is reversed or not.
                        for x in seq:
                            temp_queue[node].append(x + [node])

            # has to be updated level-by-level
            visited |= set(temp_queue.keys())
            queue0 = temp_queue

            # Swap front queue and rear queue
            queue0, queue1 = queue1, queue0
            reverse = not reverse

        return ans


def main():
    test_data = [
        ['hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']],  # 2
        ['hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']],  # []
        ["red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]],  # 3
    ]

    sol = Solution()
    for beginWord, endWord, wordList in test_data:
        print("# Input: {}, {}, {}".format(beginWord, endWord, wordList))
        print("  Output v1 = {}".format(
            sol.findLadders_v1(beginWord, endWord, wordList)))
        print("  Output v2 = {}".format(
            sol.findLadders_v2(beginWord, endWord, wordList)))


if __name__ == "__main__":
    main()
