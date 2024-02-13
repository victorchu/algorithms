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
    def search(self, board: List[List[str]], word: str) -> bool:

        def dfs(board, word, i, j, k, visited, n_rows, n_cols) -> bool:
            if k >= len(word):
                return True
            if board[i][j] != word[k]:
                return False

            visited[i][j] = True
            for next_i in [i-1, i+1]:
                if (next_i < 0) or (next_i >= n_rows):
                    continue
                for next_j in [j-1, j+1]:
                    if (next_j < 0) or (next_j >= n_cols):
                        continue            
                    if visited[next_i][next_j] == True:
                        continue
                    if dfs(board, word, next_i, next_j, k+1, visited, n_rows, n_cols):
                        return True
            visited[i][j] = False  # Restore the visited state.
            return False
        
        # Find a starting position
        n_rows = len(board)
        n_cols = len(board[0])
        visited = [ [False] * len(r) for r in board ]
        for i, row in enumerate(board):
            for j in range(len(row)):
                if dfs(board, word, i, j, 0, visited, n_rows, n_cols):
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
