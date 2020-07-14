#!/usr/bin/env python3
"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once in a word.

Example:

  Input: 
  board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
  ]
  words = ["oath","pea","eat","rain"]
  
  Output: ["eat","oath"]

REFERENCE:
  - https://leetcode.com/problems/word-search-ii/

"""

from collections import defaultdict
from typing import List


class Trie:
    class Node:
        def __init__(self, is_end=False):
            self.links = defaultdict(type(self))
            self.word = None

    def __init__(self):
        """Initialize your data structure here."""
        self.head = type(self).Node()
        self.size = 0

    def __len__(self):
        return self.size

    def __bool__(self):
        """Use __nonzero__ for Python 2"""
        return self.size > 0

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        p = self.head
        for c in word:
            p = p.links[c]
        if not p.word:
            p.word = word
            self.size += 1

    def remove(self, word: str) -> None:
        """Delete specified word."""
        def dfs(node, word, i) -> bool:
            """Return True if it is a leaf."""
            if i == len(word):
                node.word = None
                self.size -= 1
                return True if len(node.links) == 0 else False

            c = word[i]
            if c in node.links:
                child = node.links[c]
                is_leaf = dfs(child, word, i+1)
                if is_leaf:
                    del node.links[c]
                return True if (len(node.links) == 0 and not node.word) else False
            return False

        dfs(self.head, word, 0)

    def dump(self):
        """Dump all words in the trie."""
        def dfs(node: Trie.Node):
            if node.word:
                print(" - {}".format(node.word))
            for child in node.links.values():
                dfs(child)
        print("Tree dump (size = {})".format(self.size))
        dfs(self.head)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        nrows = len(board) 
        ncols = len(board[0])
        visited = [[False] * ncols for _ in range(nrows)]
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def build_trie(words):
            trie = Trie()
            for word in words:
                trie.insert(word)
            return trie


        def bfs(i, j, node, visited, res):
            """Search at position (i,j). Use node to find the neighboring letters."""
            if node.word:
                res.add(node.word)

            if len(node.links) == 0:
                return

            visited[i][j] = True
            for di, dj in deltas:
                i1 = i + di
                j1 = j + dj
                if i1 >= 0 and i1 < nrows and j1 >= 0 and j1 < ncols \
                        and not visited[i1][j1] and board[i1][j1] in node.links:
                    c = board[i1][j1]
                    bfs(i1, j1, node.links[c], visited, res)

            visited[i][j] = False

        # Begin Search
        trie = build_trie(words)
        head = trie.head
        output = []
        for i in range(nrows):
            for j in range(ncols):
                c = board[i][j]
                if c in head.links:
                    res = set()
                    bfs(i, j, head.links[c], visited, res)
                    if res:
                        for word in res:
                            trie.remove(word)
                        output.extend(res)
        return output


# ------------
#  Drivers
# ------------
def test_trie():
    t = Trie()
    print("len(t) = {}, bool(t) = {}".format(len(t), bool(t)))
    t.insert('dig')
    t.insert('dog')
    t.insert('dogs')
    t.insert('dogs')
    t.insert('oath')
    print("len(t) = {}, bool(t) = {}".format(len(t), bool(t)))
    t.dump()
    t.remove('dogs')
    t.dump()
    t.remove('dog')
    t.remove('dig')
    t.remove('oath')
    t.dump()


def test_word_search():
    board1 = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    test_data = [
        [board1, ["oath", "pea", "eat", "rain"]],
        [[['a']], ['a']],
    ]

    sol = Solution()
    for board, words in test_data:
        print("# Input  : words = {}".format(words))
        for r in board:
            print("  {}".format(r))
        print("  Output : {}".format(sol.findWords(board, words)))


def main():
    #test_trie()
    test_word_search()


if __name__ == "__main__":
    main()
