#!/usr/bin/env python3
"""
Given a sorted dictionary (array of words) of an alien language, find order of characters in the language.

EXAMPLES:

    Input: words = ["baa", "abcd", "abca", "cab", "cad"]
    Output: "bdac""

    Input: words = ["z", "x"]
    Output: "zx"

    Input: words = ["z"]
    Output: "z"

    Input: words = ["z", "x", "z"]
    Output: ""
    Reason: Circula relationship.

    Input: words = ["abc", "ab"]
    Output: ""
    Reason: The 2nd word 'ab' is a prefix of the 1st. This is not valid.


NOTE:
 - You may assume all letters are in lowercase.
 - If the order is invalid, return an empty string.
 - There may be multiple valid order of letters, return any one of them is fine.

APPROACHES:
  1. Extract dependency rules from the input.
  2. Putting dependency rules into a graph with letters as nodes and
     dependencies as edges. 
  3. Also track the number of inputs for each node.
  4. Topologically sorting the graph nodes, starting with those without
     any inputs.
 
TECHNIQUES:
  - Topological sortting.

REFERENCE
 - https://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/
 - https://www.geeksforgeeks.org/topological-sorting/
 - https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm

"""

from typing import List
from collections import defaultdict, Counter, deque


class Node:
    def __init__(self, val):
        self.val = val
        self.edges = set()
        self.in_degree = 0


class Solution:

    def alienOrder_v1(self, words: List[str]) -> str:
        """Use a Node structure to store the graph data."""
        # Step 0. Create nodes
        nodes = dict()
        for c in set([c for w in words for c in w]):
            nodes[c] = Node(c)

        # Step 1. Build the edges (dependency)
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if (c1 != c2):
                    n1 = nodes[c1]
                    if (c2 not in n1.edges):
                        n1.edges.add(c2)
                        nodes[c2].in_degree += 1
                    break
            else:
                if len(w2) < len(w1):
                    return ''

        # Step 2. Topology Sorting
        results = list()
        queue = [n for n in nodes.values() if n.in_degree == 0]
        while queue:
            n = queue.pop(0)
            results.append(n.val)
            for c in n.edges:
                n2 = nodes[c]
                n2.in_degree -= 1
                if n2.in_degree == 0:
                    queue.append(n2)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(results) < len(nodes):
            return ""

        return ''.join(results)

    def alienOrder_v2(self, words: List[str]) -> str:
        """Use two  structures (dict and Counter) to store the information."""
        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for w1, w2 in zip(words, words[1:]):
            for c, d in zip(w1, w2):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break

        # Check that second word isn't a prefix of first word. E.g. 'holly' ad 'ho'd
        # This is an invalid case and returns ''
        else:
            if len(w2) < len(w1):
                return ""

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""

        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)


# ---------------------------
#   Main & Helper Functions
# ---------------------------
def main():
    """Main function"""

    # Test data
    test_data = [
        [["baa", "abcd", "abca", "cab", "cad"], "bdac"],
        [["wrt", "wrf", "er", "ett", "rftt"], "wertf"],
        [["z", "x"], "zx"],
        [["z", "x", "z"], ""],  # circular
        [["za", "zb", "ca", "cb"], "abzc"],
        [["abc", "ab"], ""],    # 2nd word is a prefix of 1st. Thus, invalid
        [["z", "z"], "z"],
        [["zy", "zx"], "zyx"],
        [["ab", "adc"], "abcd"],
        [["ri", "xz", "qxf", "jhsguaw", "dztqrbwbm",
            "dhdqfb", "jdv", "fcgfsilnb", "ooby"], ""],
    ]

    sol = Solution()
    for words, expected in test_data:
        print("# Input  = {}".format(words))
        out1 = sol.alienOrder_v1(words)
        out2 = sol.alienOrder_v2(words)
        print("  v1 = '{}' : {}".format(
            out1, 'ok' if len(out1) == len(expected) else 'ERROR'))
        print("  v2 = '{}' : {}".format(
            out2, 'ok' if len(out2) == len(expected) else 'ERROR'))


if __name__ == "__main__":
    main()
