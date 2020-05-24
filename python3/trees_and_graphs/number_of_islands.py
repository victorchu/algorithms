#!/usr/bin/env python3
"""
Given a 2d grid map of '1's (land) and '0's (water), count the
number of islands. An island is surrounded by water and is formed
by connecting adjacent lands horizontally or vertically. You may
assume all four edges of the grid are all surrounded by water.

EXAMPLES:

  Input:
    11110
    11010
    11000
    00000

  Output: 1

  Input:
    11000
    11000
    00100
    00011

  Output: 3

  Input:
    00101
    10111
    11100
    10011

  Output: 2

NOTE:
  - Diagal connections don't count.

TECHNIQUES:
  - DFS: depth first search + visitation tracking.

REFERNECE:
  - https://leetcode.com/problems/number-of-islands/ (Medium)
  - https://www.geeksforgeeks.org/find-number-of-islands/

"""

from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # Create another grid for status tracking
        visited = [[False] * len(r) for r in grid]
        num_rows = len(grid)
        num_cols = len(grid[0])

        def dfs(row_idx, col_idx):
            """Search all 4 directions surrounding the specified cell location."""
            # Check if it is already visited
            if visited[row_idx][col_idx]:
                return
            visited[row_idx][col_idx] = True

            # Return on reaching the water
            if grid[row_idx][col_idx] != '1':
                return

            # Explore all of the four directions
            if col_idx > 0:
                dfs(row_idx, col_idx - 1)
            if col_idx < num_cols - 1:
                dfs(row_idx, col_idx + 1)
            if row_idx > 0:
                dfs(row_idx - 1, col_idx)
            if row_idx < num_rows - 1:
                dfs(row_idx + 1, col_idx)

        # Iterate through the whole grid
        count = 0
        for row_idx, row in enumerate(grid):
            for col_idx, v in enumerate(row):
                if visited[row_idx][col_idx]:
                    continue
                if v == '1':
                    count += 1
                    dfs(row_idx, col_idx)
                else:
                    visited[row_idx][col_idx] = True

        return count

# ---------------------------
#   Main & Helper Functions
# ---------------------------


def string_list_to_grid(str_list):
    return [[c for c in s] for s in str_list]


def main():
    """Main function"""

    # Test data
    test_data = [
        ['11110',
         '11010',
         '11000',
         '00000'],
        ['11000',
            '11000',
            '00100',
            '00011'],
        ['00101',
            '10111',
            '11100',
            '10011'],
    ]

    sol = Solution()
    for str_list in test_data:
        grid = string_list_to_grid(str_list)
        print("# Input = [")
        for r in grid:
            print("  {},".format(r))
        print("]")

        print("  Output v1 = {}".format(sol.numIslands(grid)))


if __name__ == "__main__":
    main()
