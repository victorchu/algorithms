#!/usr/bin/env python3
"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two
independent subsets A and B such that every edge in the graph has one node in A
and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for
which the edge between nodes i and j exists.  Each node is an integer between 0
and graph.length - 1.  There are no self edges or parallel edges: graph[i] does
not contain i, and it doesn't contain any element twice.

EXAMPLES:

  Input: [[1,3], [0,2], [1,3], [0,2]]
        0----1
        |    |
        |    |
        3----2
  Output: true
  Explanation: We can divide the vertices into two groups: {0, 2} and {1, 3}.

  Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
        0----1
        | \  |
        |  \ |
        3----2
  Output: false
  Explanation: We cannot find a way to divide the set of nodes into two independent subsets.

NOTE:
  - There can be isolated points and separated sub-graphs.

REFERENCE:
  - https://leetcode.com/problems/is-graph-bipartite/ (Medium)
  - https://www.geeksforgeeks.org/bipartite-graph/
  - https://en.wikipedia.org/wiki/Bipartite_graph
     
"""

from typing import List


class Solution:

    def isBipartite_v1(self, graph: List[List[int]]) -> bool:
        """Use two sets to track two groups."""

        if not graph:
            return False

        node_sets = [set(), set()]
        visited = [False] * len(graph)

        for k in range(len(graph)):
            if visited[k]: continue
            queue = [[k, 0]]

            for i, set_idx in queue:
                alt_set_idx = (set_idx + 1) % 2
                this_set = node_sets[set_idx]
                alt_set = node_sets[alt_set_idx]

                # Handle this node
                if i in alt_set:
                    return False
                this_set.add(i)
                visited[i] = True

                # Handle edges
                for j in graph[i]:
                    if not visited[j]:
                        queue.append([j, alt_set_idx])

        return True


    def isBipartite_v2(self, graph: List[List[int]]) -> bool:
        """Use one color array to track two colors (0, 1)."""

        if not graph:
            return False

        colors = [-1] * len(graph)

        for k in range(len(graph)):
            if colors[k] != -1: continue
            queue = [[k, 0]]

            for i, color in queue:
                alt_color = 1 - color
                if colors[i] == alt_color:
                    return False
                colors[i] = color

                for j in graph[i]:
                    if colors[j] == -1:
                        queue.append([j, alt_color])

        return True


def main():
    test_data = [
        [[[1,3], [0,2], [1,3], [0,2]], True],
        [[[1,2,3], [0,2], [0,1,3], [0,2]], False],
        [[[1],[0,3],[3],[1,2]], True],
        [[[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]], False],
    ]

    sol = Solution()
    for graph, ans in test_data:
        print("# Input = {}".format(graph))
        print("  Output v1 = {}".format(sol.isBipartite_v1(graph), ans))
        print("  Output v2 = {}".format(sol.isBipartite_v2(graph), ans))
        print("  Answer = {}".format(ans))


if __name__ == "__main__":
    main()
