#!/usr/bin/env python3
"""
There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi]
this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs,
return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them.
If it is impossible to finish all courses, return an empty array.

Examples:
  Input: numCourses = 2, prerequisites = [[1,0]]
  Output: [0,1]
  Explanation: There are a total of 2 courses to take.
    To take course 1 you should have finished course 0. So the correct course order is [0,1].

  Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
  Output: [0,2,1,3]
  Explanation: There are a total of 4 courses to take.
    To take course 3 you should have finished both courses 1 and 2.
    Both courses 1 and 2 should be taken after you finished course 0.
    So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

  Input: numCourses = 1, prerequisites = []
  Output: [0]

Constraints:
 . 1 <= numCourses <= 2000
 . 0 <= prerequisites.length <= numCourses * (numCourses - 1)
 . prerequisites[i].length == 2
 . 0 <= ai, bi < numCourses
 . ai != bi
 . All the pairs [ai, bi] are distinct.

NOTE:
  - This is a Topological sorting problem.
  - This can be difficult if you don't know Khan's algorithm.

REFERENCE:
  - https://leetcode.com/problems/course-schedule-ii/ (Medium)
  - https://www.geeksforgeeks.org/topological-sorting/
  - https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
  - https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm
  - https://www.coursera.org/specializations/algorithms

"""

from typing import List
from collections import defaultdict


class Solution:
    def findOrder_v1(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """Khan's algorithm.

        - Track the in-degree (number of incoming edges) for each node.
        """

        # Build up a directional graph putting prequisites at the top.
        graph = [[] for _ in range(numCourses)]
        # Also track in-degress.  
        indegrees = [0] * numCourses
        for q, p in prerequisites:
            indegrees[q] += 1
            graph[p].append(q)

        # Start with courses having 0 in-degree, those don't have any pre-requisites.
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
            
        return stack if len(stack) == numCourses else []


def main():
    test_data = [
  		[2, [[1,0]]],   # [0, 1]
  		[2, [[1,0], [0,1]]],    # []
        [4, [[1,0],[2,0],[3,1],[3,2]]],  # [0,1,2,3] or [0,2,1,3]
  		#[3, [[0,1], [0,2], [1,2]]],      # 
        #[7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]], # 
    ]

    sol = Solution()
    for numCourses, prerequisites in test_data:
        print("# Input: n={}, pre={}".format(numCourses, prerequisites))
        print("  Output v1 = {}".format(sol.findOrder_v1(numCourses, prerequisites)))


if __name__ == "__main__":
    main()
