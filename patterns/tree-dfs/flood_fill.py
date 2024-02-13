#!/usr/bin/env python3
"""
An image is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of
the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels (also
with the same color as the starting pixel), and so on. Replace the color of all
of the aforementioned pixels with the newColor.

At the end, return the modified image.

EXAMPLES:

  Input: image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1, sc = 1, newColor = 2
  Output: [[2,2,2],[2,2,0],[2,0,1]]
  Explanation: The image is 

       [[1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]]

    From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
    by a path of the same color as the starting pixel are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected
    to the starting pixel.

REFERENCE:
  - https://leetcode.com/problems/flood-fill/ (Easy)

"""

from typing import List


class Solution:
    def floodFill_v1(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """Use queue"""
        nrows = len(image)
        ncols = len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        image[sr][sc] = newColor

        queue = [(sr, sc)]
        deltas = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            r0, c0 = queue.pop(0)
            for (dr,dc) in deltas:
                r = r0 + dr
                c = c0 + dc
                if (r < 0) or (r >= nrows) or (c < 0) or (c >= ncols):
                    continue
                if image[r][c] == oldColor:
                    image[r][c] = newColor
                    queue.append([r,c])

        return image

    def floodFill_v2(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """Use recursion"""
        nrows = len(image)
        ncols = len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image

        def dfs(r, c):
            if image[r][c] != oldColor:
                return

            image[sr][sc] = newColor
            if r > 0: dfs(r-1, c)
            if r + 1 < nrows: dfs(r+1, c)
            if c > 0: dfs(r, c-1)
            if c + 1 < ncols: dfs(r, c+1)

        dfs(sr, sc)
        return image


def main():
    test_data = [
        [[[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2],
    ]

    sol = Solution()
    for image, sr, sc, newColor in test_data:
        print("# Input: image={}, sr={}, sc={}, newColor={}".format(image, sr, sc, newColor))
        print("  Output v1 = {}".format(sol.floodFill_v1(image, sr, sc, newColor)))
        print("  Output v2 = {}".format(sol.floodFill_v2(image, sr, sc, newColor)))


if __name__ == "__main__":
    main()
