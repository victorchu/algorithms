#!/usr/bin/env python3
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?

EXAMPLES:

  Input: numCourses = 2, prerequisites = [[1,0]]
  Output: true
  Explanation: There are a total of 2 courses to take. 
               To take course 1 you should have finished course 0. So it is possible.

  Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
  Output: false
  Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

HINTS:
  - This problem is equivalent to finding if a cycle exists in a directed graph.
    If a cycle exists, no topological ordering exists and therefore it will be
    impossible to take all courses.
  - Can use BFS or DFS.

REFERENCE:
  - https://leetcode.com/problems/course-schedule/ (Medium)
  - https://www.geeksforgeeks.org/topological-sorting/
  - https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
  - https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm
  - https://www.coursera.org/specializations/algorithms

"""

from typing import List
from collections import defaultdict


class Solution:
    def canFinish_v1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """DFS with two sets.
        This method primarily searches for loops.
        - First, build a graph based on prequisites.
        - Given any course number n, traverse the graph use DFS.
        - Yet, use a working set to track all of the nodes are being process.
        - If DFS hits any of node in the working set, it is a loop. 
        """
        # Build a graph with a dictionary.  Each node has a list of edges.
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        # Use two sets to track processed and working nodes.
        processed = set()
        working_set = set()

        def dfs(n):
            """Use DFS to traverse the graph, starting from Node n."""
            if n in processed:
                return True
            if n in working_set:
                return False

            # Add current node to the working set and continue to traverse.
            # We shall not run into this node during the traversal.
            working_set.add(n)
            edges = graph[n]
            for m in edges:
                if not dfs(m):
                    return False

            # On finishing BFS, remove the current node from the working set.
            # And mark it as processed.
            working_set.remove(n)
            processed.add(n)
            return True

        # Visit every single node (class number).
        # If the traversal function returns False if it detects a loop.
        for n in range(numCourses):
            if not dfs(n):
                return False

        return True

    def canFinish_v2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """Khan's algorithm.

        - Track the in-degree (number of incoming edges) for each node.
        - Start with those with in-degree 0.
        - Reduce the in-degree for connected node.
        - This is more of a BFS.
        - Loops will not be reachable.
        """

        # Build up the graph and update the in-degree.
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for p, q in prerequisites:
            indegrees[q] += 1
            graph[p].append(q)

        # Find nodes with 0 in-degree
        queue = [i for i in range(numCourses) if indegrees[i] == 0]
        stack = queue.copy()  # sorted nodes
        while queue:
            n = queue.pop(0)
            edges = graph[n]
            for m in edges:
                indegrees[m] -= 1
                if indegrees[m] == 0:
                    queue.append(m)
                    stack.append(m)
            
        return len(stack) == numCourses


def main():
    test_data = [
  		[2, [[1,0]]],   # True
  		[2, [[1,0], [0,1]]],    # False
  		[3, [[0,1], [0,2], [1,2]]],    # True
        [7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]], # True
    ]

    sol = Solution()
    for numCourses, prerequisites in test_data:
        print("# Input: n={}, pre={}".format(numCourses, prerequisites))
        print("  Output v1 = {}".format(sol.canFinish_v1(numCourses, prerequisites)))
        print("  Output v2 = {}".format(sol.canFinish_v2(numCourses, prerequisites)))


if __name__ == "__main__":
    main()
