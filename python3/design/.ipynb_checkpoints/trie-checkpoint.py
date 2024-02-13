#!/usr/bin/env python3
"""
Implement a trie (pronounce 'try', aka prefix tree) with insert, search,
and startsWith methods.

Example:

    trie = Trie()

    trie.insert("apple")
    trie.search("apple")   // returns true
    trie.search("app")     // returns false
    trie.startsWith("app") // returns true
    trie.insert("app")   
    trie.search("app")     // returns true

Note:

  - You may assume that all inputs are consist of lowercase letters a-z.
  - All inputs are guaranteed to be non-empty strings.


REFERENCE:
  - https://leetcode.com/problems/implement-trie-prefix-tree/ (Medium)
  - https://www.geeksforgeeks.org/trie-insert-and-search/

"""
from collections import defaultdict


class Trie_v1:
    """Use dict for links.

    Runtime > 14.39%; memory < 16.16%
    """

    class Node:
        def __init__(self, is_end=False):
            self.links = defaultdict(type(self))
            self.is_end = is_end

    def __init__(self):
        """Initialize your data structure here."""
        self.head = type(self).Node()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        p = self.head
        for c in word:
            p = p.links[c]
        p.is_end = True

    def search(self, word: str) -> bool:
        """Returns if the word is in the trie. """
        p = self.head
        for c in word:
            if not c in p.links:
                return False
            p = p.links[c]
        return p.is_end

    def startsWith(self, prefix: str) -> bool:
        """Returns if there is any word in the trie that starts with the given prefix."""
        p = self.head
        for c in prefix:
            if not c in p.links:
                return False
            p = p.links[c]
        return True


class Trie_v2:
    """Use an array of size 26 as links (for 26 letters).

    Runtime > 22.78%; memory < 11.77%
    """

    class Node:
        def __init__(self, is_end=False):
            self.links = [None] * 26
            self.is_end = is_end

    def __init__(self):
        """Initialize your data structure here."""
        self.head = self._get_node()

    def _get_node(self):
        return type(self).Node()

    def _get_index(self, c):
        return ord(c) - ord('a')

    def insert(self, word: str) -> None:
        """Inserts a word into the trie. """
        p = self.head
        for c in word:
            idx = self._get_index(c)
            if not p.links[idx]:
                p.links[idx] = self._get_node()
            p = p.links[idx]
        p.is_end = True

    def search(self, word: str) -> bool:
        """Returns if the word is in the trie."""
        p = self.head
        for c in word:
            idx = self._get_index(c)
            if not p.links[idx]:
                return False
            p = p.links[idx]
        return p.is_end

    def startsWith(self, prefix: str) -> bool:
        """Returns if there is any word in the trie that starts with the given prefix. """
        p = self.head
        for c in prefix:
            idx = self._get_index(c)
            if not p.links[idx]:
                return False
            p = p.links[idx]
        return True


# ----------------
#   Unit Tests
# ----------------
def test_search(trie, word):
    print("- search({}) = {}".format(word, trie.search(word)))


def test_startsWith(trie, prefix):
    print("- startsWith({}) = {}".format(prefix, trie.startsWith(prefix)))


def test_trie(trie):
    print("# Testing", type(trie).__name__)
    trie.insert("apple")
    test_search(trie, "apple")
    test_search(trie, "app")
    test_search(trie, "banana")

    trie.insert("app")
    test_startsWith(trie, "apple")
    test_startsWith(trie, "app")
    test_startsWith(trie, "banana")
    print()


def main():
    test_trie(Trie_v1())
    test_trie(Trie_v2())


if __name__ == "__main__":
    main()
