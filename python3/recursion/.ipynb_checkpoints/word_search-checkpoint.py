#!/usr/bin/env python3
"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

EXAMPLES:

  board =
  [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
  ]
  
  Given word = "ABCCED", return True.
  Given word = "SEE", return True.
  Given word = "ABCB", return False.
  Given word = "ABCESEEEFS", return True

REFERENCE:
  - https://leetcode.com/problems/word-search/

"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True

        n_rows = len(board)
        n_cols = len(board[0])
        visited = [[False] * n_cols for _ in range(n_rows)]
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Locate start positions
        def get_start_positions(c):
            start_positions = []
            for i in range(n_rows):
                for j in range(n_cols):
                    if board[i][j] == c:
                        start_positions.append([i, j])
            return start_positions

        # Helper function
        def helper(word, i, j, k, visited) -> bool:
            if k >= len(word):
                return True

            # Search for the next letter
            visited[i][j] = True
            c = word[k]
            for di, dj in deltas:
                i1 = i + di
                j1 = j + dj
                if i1 >= 0 and i1 < n_rows and j1 >= 0 and j1 < n_cols \
                        and not visited[i1][j1] and board[i1][j1] == c:
                    if helper(word, i1, j1, k+1, visited):
                        return True

            # On failed attempt, need to reset the visited status.
            visited[i][j] = False
            return False

        # Start to search
        start_positions = get_start_positions(word[0])
        for i, j in start_positions:
            if helper(word, i, j, 1, visited):
                return True
        return False


def main():
    board1 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    test_data = [
        [board1, 'ABCCED', True],
        [board1, 'SEE', True],
        [board1, 'ABCB', False],
        [board1, 'ABCESEECFSAD', True],
    ]

    sol = Solution()
    for board, word, ans in test_data:
        print("# Input  : word = {} (ans = {})".format(word, ans))
        for r in board:
            print("  {}".format(r))
        print("  Output : {}".format(sol.exist(board, word)))


if __name__ == "__main__":
    main()
