#!/usr/bin/env python3
"""
You are asked to cut off trees in a forest for a golf event. The forest is
represented as a non-negative 2D map, in this map:

  - 0 represents the obstacle can't be reached.
  - 1 represents the ground can be walked through.
  - The place with number bigger than 1 represents a tree can be walked through,
    and this positive number represents the tree's height.

In one step you can walk in any of the four directions top, bottom, left and
right also when standing in a point which is a tree you can decide whether or
not to cut off the tree.

You are asked to cut off all the trees in this forest in the order of tree's
height - always cut off the tree with lowest height first. And after cutting,
the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you
need to walk to cut off all the trees. If you can't cut off all the trees,
output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least
one tree needs to be cut off.

EXAMPLES:

  Input: 
  [
    [1, 2, 3],
    [0, 0, 4],
    [7, 6, 5]
  ]
  Output: 6
  
  Input: 
  [
    [1, 2, 3],
    [0, 0, 0],
    [7, 6, 5]
  ]
  Output: -1
  
  Input: 
  [
    [2, 3, 4],
    [0, 0, 5],
    [8, 7, 6]
  ]
  Output: 6
  Explanation: You started from the point (0,0) and you can cut off the tree
     in (0,0) directly without walking.


REFERENCE:
  - https://leetcode.com/problems/cut-off-trees-for-golf-event/

"""

from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        nrows = len(forest)
        ncols = len(forest[0])

        def get_distance(forest, start_pos, end_pos):
            """BFS for finding the shorted steps from start to end."""
            if start_pos == end_pos:
                return 0
            queue = [start_pos]
            visited = [[False] * ncols for _ in range(nrows)]
            visited[start_pos[0]][start_pos[1]] = True
            steps = 0
            while queue:
                # process one layer at a time
                n = len(queue)
                for _ in range(n):
                    r0, c0 = queue.pop(0)
                    if r0 == end_pos[0] and c0 == end_pos[1]:
                        return steps
                    for dr in [-1, 1]:
                        r = r0 + dr
                        c = c0
                        if r >= 0 and r < nrows and not visited[r][c] and forest[r][c] > 0:
                            queue.append([r, c])
                            visited[r][c] = True
                    for dc in [-1, 1]:
                        r = r0
                        c = c0 + dc
                        if c >= 0 and c < ncols and not visited[r][c] and forest[r][c] > 0:
                            queue.append([r, c])
                            visited[r][c] = True
                # Increment the step
                steps += 1
            return -1

        # Preprocess forest to get the visitation order
        tree_map = dict()
        for r in range(nrows):
            for c in range(ncols):
                v = forest[r][c]
                if v > 1:
                    tree_map[v] = [r, c]

        # Iterate through all of the threes
        pos = (0, 0)
        total_steps = 0
        for v in sorted(tree_map.keys()):
            to_pos = tree_map[v]
            steps = get_distance(forest, pos, to_pos)
            if steps < 0:
                return -1
            total_steps += steps
            pos = to_pos

        return total_steps


def main():
    test_data = [
        [[[1, 2, 3], [0, 0, 4], [7, 6, 5]], 6],
        [[[1, 2, 3], [0, 0, 0], [7, 6, 5]], -1],
        [[[2, 3, 4], [0, 0, 5], [8, 7, 6]], 6],
    ]

    sol = Solution()
    for forest, ans in test_data:
        print("# Input = {} (ans={})".format(forest, ans))
        print("  Output = {}".format(sol.cutOffTree(forest)))


if __name__ == "__main__":
    main()
