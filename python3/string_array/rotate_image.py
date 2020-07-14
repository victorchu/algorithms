#!/usr/bin/env python3
"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

NOTE:
  - You have to rotate the image in-place, which means you have to modify the
    input 2D matrix directly. DO NOT allocate another 2D matrix and do the
    rotation.

EXAMPLES:
  Given input matrix = 
  [
    [1,2,3],
    [4,5,6],
    [7,8,9]
  ],
  rotate the input matrix in-place such that it becomes:
  [
    [7,4,1],
    [8,5,2],
    [9,6,3]
  ]

  Given input matrix =
  [
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
  ], 
  rotate the input matrix in-place such that it becomes:
  [
    [15,13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7,10,11]
  ]

HINT:
  - Value at position (r, c) will be moved to position (c, n - 1 -r) after rotation.
    It is composed of two steps:
    1. Rotation only: move it to (c, -r).
    2. Shift it up (n - 1) steps: move it (c, n - 1 - r)
  - Similarly, position (r, c) will be replaced by the value from (n - 1 - c, r)
  - A different perspective:
    1. Swap row r with row n - 1 - r.  Thus (r, c) becomes (n - 1 - r, c)
    2. Flip on the diagnal line, thus (n - 1 -r, c) becomes (c, n - 1 - r)

REFERENCE:
  - https://leetcode.com/problems/rotate-image/ (Medium)
  - https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/

"""

from typing import List


class Solution:

    def rotate_v1(self, matrix: List[List[int]]) -> None:
        """Process layer by layer."""
        def get_from_position(r, c, n):
            return n - 1 - c, r

        def rotate_border(matrix, offset, n):
            """Rotate the border layer of the matrix"""
            if n - 2 * offset <= 1:
                return

            for c in range(offset, n - offset - 1):
                r = offset
                tmp = matrix[r][c]
                for _ in range(3):
                    r0, c0 = get_from_position(r, c, n)
                    matrix[r][c] = matrix[r0][c0]
                    r, c = r0, c0
                matrix[r][c] = tmp
            rotate_border(matrix, offset + 1, n)

        rotate_border(matrix, 0, len(matrix))

    def rotate_v2(self, matrix: List[List[int]]) -> None:
        # Change (r, c) to (n - 1 - r, c) by swapping rows
        n = len(matrix)
        for i in range(n//2):
            j = n - 1 - i
            matrix[i], matrix[j] = matrix[j], matrix[i]

        # Flip around the diagonal line, thus
        # changing (n - 1 - r, c) to (c, n - 1 - r)
        for r in range(1, n):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


def main():
    test_data = [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [ 5,  1,  9, 11],
            [ 2,  4,  8, 10],
            [13,  3,  6,  7],
            [15, 14, 12, 16]
        ],
    ]

    def copy_matrix(matrix):
        res = []
        for r in matrix:
            res.append(r.copy())
        return res

    def print_matrix(name, matrix, indent='  '):
        print("{} [".format(name))
        for r in matrix:
            r_formated = ", ".join(["{:2d}".format(x) for x in r])
            print("{}{}[{}],".format(indent, indent, r_formated))
        print("{}]".format(indent))

    sol = Solution()
    for matrix_orig in test_data:
        print_matrix("# Input =", matrix_orig)

        # v1
        matrix = copy_matrix(matrix_orig)
        sol.rotate_v1(matrix)
        print_matrix("  Output v1 =", matrix)

        # v2
        matrix = copy_matrix(matrix_orig)
        sol.rotate_v2(matrix)
        print_matrix("  Output v2 =", matrix)


if __name__ == "__main__":
    main()
