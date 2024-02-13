#!/usr/bin/env python3
"""
Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.

Example 1:
  Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
  Output: Following are the two valid topological sorts for the given graph:
  1) 3, 2, 0, 1
  2) 3, 2, 1, 0

Example 2:
  Input: Vertices=5, Edges=[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]
  Output: Following are all valid topological sorts for the given graph:
  1) 4, 2, 3, 0, 1
  2) 4, 3, 2, 0, 1
  3) 4, 3, 2, 1, 0
  4) 4, 2, 3, 1, 0
  5) 4, 2, 0, 3, 1

Ref: https://www.educative.io/courses/grokking-the-coding-interview/m25rBmwLV00
"""
from collections import defaultdict
from typing import List


class Solution:

    def topological_sort(self, vertices: int, edges: List[List[int]]):
        """Use in degrees to find the order."""
        sortedOrder = []
        if vertices <= 0:
            return sortedOrder

        # a. Build the graph and inDegres.
        inDegree = {i: 0 for i in range(vertices)}  # count of incoming edges
        graph = defaultdict(list)

        for parent, child in edges:
            graph[parent].append(child)  # put the child into it's parent's list
            inDegree[child] += 1  # increment child's inDegree

        # b. Find all vertices with 0 in-degrees
        queue = [k for (k,v) in inDegree.items() if v==0]

        # c. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
        # if a child's in-degree becomes zero, add it to the sources queue
        while queue:
            vertex = sources.pop(0)
            sortedOrder.append(vertex)
            for child in graph[vertex]:  # get the node's children to decrement their in-degrees
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    queue.append(child)

        # topological sort is not possible as the graph has a cycle
        if len(sortedOrder) != vertices:
            return []

        return sortedOrder


def main():
    data_set = [
        [4, [[3, 2], [3, 0], [2, 0], [2, 1]]],
        [5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]],
        [7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]],
    ]
    ob1 = Solution()
    for vertices, edges in data_set:
        print(f"Input: vertices={vertices}, edges={edges}")
        print(f"  Topological sort: {ob1.topological_sort(vertices, edges)}")


main()
