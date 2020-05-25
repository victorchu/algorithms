#!/usr/bin/env python3
"""
You want to build a house on an empty land which reaches all buildings
in the shortest amount of distance. You can only move up, down,
left and right. You are given a 2D grid of values 0, 1 or 2, where:

  - Each 0 marks an empty land which you can pass by freely.
  - Each 1 marks a building which you cannot pass through.
  - Each 2 marks an obstacle which you cannot pass through.


EXAMPLE:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

    1 - 0 - 2 - 0 - 1
    |   |   |   |   |
    0 - 0 - 0 - 0 - 0
    |   |   |   |   |
    0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.

TECHNOLOGIES:
  - Use Bread First Search (BFS) to get the distances from each building.

REFERNECE:
  - https://leetcode.com/problems/shortest-distance-from-all-buildings/description/ (Hard)

"""

from typing import List
import numpy as np


class Solution:

    def shortestDistance_v1(self, grid: List[List[int]]) -> int:
        """Use Bread First Search (BFS)."""

        def zeros(nrows, ncols, val=0):
            """Create a zero grid for distance tracking."""
            return [[val] * ncols for _ in range(nrows)]

        def bfs(i, j):
            """Bread-first search."""
            dist = 0
            queue = [[i, j, dist]]  # push distance into the queue
            visited = zeros(nrows, ncols, val=False)
            visited[i][j] = True
            building_count = 1
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            while queue:
                i0, j0, dist = queue.pop(0)
                sum_dist[i0][j0] += dist
                num_visits[i0][j0] += 1
                
                # Explore neighbors
                dist += 1
                for di, dj in directions:
                    i = i0 + di
                    j = j0 + dj

                    # Skip invalid positions
                    if (i < 0) or (i >= nrows) or (j < 0) or (j >= ncols):
                        continue

                    # Skip visited positions
                    if visited[i][j]:
                        continue
                    visited[i][j] = True

                    # Track the number of buildings
                    if grid[i][j] == 1:
                        building_count += 1

                    # Push the next valid position into the queue
                    elif grid[i][j] == 0:
                        queue.append([i, j, dist])

            return building_count == num_buildings

        if (not grid) or (not grid[0]):
            return -1

        # Preparation
        nrows, ncols = len(grid), len(grid[0])
        sum_dist = zeros(nrows, ncols)     # grid of cumulated distance
        num_visits = zeros(nrows, ncols)   # number of visits
        num_buildings = sum([1 for i in range(nrows) for j in range(ncols) if grid[i][j] == 1])

        # Explore from each building
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 1:
                    if not bfs(i, j):
                        return -1

        # Get the min distance
        min_dist = -1
        for i in range(nrows):
            for j in range(ncols):
                if (grid[i][j] == 0) and (num_visits[i][j] == num_buildings):
                    dist = sum_dist[i][j]
                    if (min_dist < 0) or (dist < min_dist):
                        min_dist = dist

        return min_dist

    def shortestDistance_v2(self, grid: List[List[int]]) -> int:
        """BFS, yet explicitly process one distance layer at a time."""

        def zeros(nrows, ncols, val=0):
            """Create a zero grid for distance tracking."""
            return [[val] * ncols for _ in range(nrows)]

        def bfs(i, j):
            """Bread-first search."""
            dist = 0
            queue = [[i, j]]
            visited = zeros(nrows, ncols, val=False)
            visited[i][j] = True
            building_count = 1
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            while queue:
                # Process all positions belong to the same distance layer.
                # Store new positions into a new queue.
                next_queue = []
                while queue:
                    i0, j0 = queue.pop(0)
                    sum_dist[i0][j0] += dist
                    num_visits[i0][j0] += 1
                
                    # Explore neighbors
                    for di, dj in directions:
                        i = i0 + di
                        j = j0 + dj

                        # Skip invalid positions
                        if (i < 0) or (i >= nrows) or (j < 0) or (j >= ncols):
                            continue

                        # Skip visited positions
                        if visited[i][j]:
                            continue
                        visited[i][j] = True

                        # Track the number of buildings
                        if grid[i][j] == 1:
                            building_count += 1

                        # Push the next valid position into the new queue
                        elif grid[i][j] == 0:
                            next_queue.append([i, j])

                # Update queue and increment the distance
                queue = next_queue
                dist += 1

            # Must have visisted all of the buildings
            return building_count == num_buildings

        # Begin of function
        if (not grid) or (not grid[0]):
            return -1

        # Preparation
        nrows, ncols = len(grid), len(grid[0])
        sum_dist = zeros(nrows, ncols)     # grid of cumulated distance
        num_visits = zeros(nrows, ncols)   # number of visits
        num_buildings = sum([1 for i in range(nrows) for j in range(ncols) if grid[i][j] == 1])

        # Explore from each building
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 1:
                    if not bfs(i, j):
                        return -1

        # Get the min distance
        min_dist = -1
        for i in range(nrows):
            for j in range(ncols):
                if (grid[i][j] == 0) and (num_visits[i][j] == num_buildings):
                    dist = sum_dist[i][j]
                    if (min_dist < 0) or (dist < min_dist):
                        min_dist = dist

        return min_dist


# ---------------------------
#   Main & Helper Functions
# ---------------------------
def main():
    """Main function"""

    # Test data
    test_data = [
        [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]],
        [[1]],
        [[0,2,1],[1,0,2],[0,1,0]],
        [[1,1,1,1,1,0],[0,0,0,0,0,1],[0,1,1,0,0,1],[1,0,0,1,0,1],[1,0,1,0,0,1],[1,0,0,0,0,1],[0,1,1,1,1,0]],
        [[1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,1],[1,1,1,1,1,1,0,1],[1,0,0,0,1,1,0,1],[1,0,1,1,1,1,0,1],[1,0,1,0,0,1,0,1],[1,0,1,1,1,1,0,1],[1,0,0,0,0,0,0,1],[0,1,1,1,1,1,1,0]],
    ]

    sol = Solution()
    for grid in test_data:
        print("# Input =\n{}".format(np.array(grid)))
        print("  Output v1 =", sol.shortestDistance_v1(grid))
        print("  Output v2 =", sol.shortestDistance_v2(grid))


if __name__ == "__main__":
    main()
