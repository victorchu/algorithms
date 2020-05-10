#!/usr/bin/env python3
"""
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order (clockwise).

For example, given the following matrix:

  [[1, 2, 3],
   [8, 9, 4],
   [7, 6, 5]]

Return [1,2,3,4,5,6,7,8,9]

Comment: A lot of book-keeping. This is not a good interview question.

Key functions:
  - % : mode operator

Ref:
  - https://www.programcreek.com/2013/01/leetcode-spiral-matrix-java/
"""


import logging
import re

logger = logging.getLogger(__name__)


def spiral_v1(m):
    """
    Complexity O(n).  Space O(n)
    :param m: Assumed to be a rectangular matrix.
    """
    spiral = list()
    if len(m) == 0:
        return spiral;

    nrows = len(m)
    ncols = len(m[0])
    directions = ['right', 'bottom', 'left', 'top']
    limits = {'right':ncols-1, 'bottom':nrows-1, 'left':0, 'top':0}
    idx_dir = 0 # start with rightward.

    i, j, k = 0, 0, 0
    while k < nrows * ncols:
        direction = directions[idx_dir]
        # At the top, moving toward the right
        if direction == 'right':
            idx0 = limits['left']
            idx1 = limits['right']
            v = [m[i][x] for x in range(idx0, idx1+1)]
            j = idx1
            spiral += v
            k += len(v)
            idx_dir = (idx_dir + 1) % 4
            limits['top'] += 1

        # At the right, moving toward the bottom
        elif direction == 'bottom':
            idx0 = limits['top']
            idx1 = limits['bottom']
            v = [m[x][j] for x in range(idx0, idx1+1)]
            spiral += v
            i = idx1
            k += len(v)
            idx_dir = (idx_dir + 1) % 4
            limits['right'] -= 1
            
        # At the bottom, moving toward the left
        elif direction == 'left':
            idx0 = limits['right']
            idx1 = limits['left']
            v = [m[i][x] for x in range(idx0, idx1-1, -1)]
            spiral += v
            j = idx1
            k += len(v)
            idx_dir = (idx_dir + 1) % 4
            limits['bottom'] -= 1

        # At the left, moving toward the top
        elif direction == 'top':
            idx0 = limits['bottom']
            idx1 = limits['top']
            v = [m[x][j] for x in range(idx0, idx1-1, -1)]
            spiral += v
            i = idx1
            k += len(v)
            idx_dir = (idx_dir + 1) % 4
            limits['left'] += 1
    return spiral


def spiral_v2(m):
    """Similar to spiral_v1, but provides some generalization.
    The code is not much shorter than spiral_v1.

    Complexity O(n).  Space O(n)
    :param m: Assumed to be a rectangular matrix.
    """
    spiral = list()
    if len(m) == 0:
        return spiral;

    nrows = len(m)
    ncols = len(m[0])
    directions = ['right', 'bottom', 'left', 'top']
    limits = {'right':ncols-1, 'bottom':nrows-1, 'left':0, 'top':0}
    idx_dir = 0 # start with rightward.

    def helper_v2(m, i, j, idx_dir): 
        # Get from and to index
        from_key = directions[(idx_dir+2) % 4]
        to_key = directions[idx_dir]
        idx0 = limits[from_key]
        idx1 = limits[to_key]

        # Copy elements.  It is hard to generalize this section.
        if to_key == 'right':
            v = [m[i][x] for x in range(idx0, idx1+1)]
            j = idx1
        elif to_key == 'bottom':
            v = [m[x][j] for x in range(idx0, idx1+1)]
            i = idx1
        elif to_key == 'left':
            v = [m[i][x] for x in range(idx0, idx1-1, -1)]
            j = idx1
        elif to_key == 'top':
            v = [m[x][j] for x in range(idx0, idx1-1, -1)]
            i = idx1

        # Adjust limits
        limit_key = directions[(idx_dir + 3) % 4]
        if limit_key in ['left', 'top']:
            limits[limit_key] += 1
        else:
            limits[limit_key] -= 1

        # Change direction
        idx_dir = (idx_dir + 1) % 4

        # DEBUG info
        #logger.debug("To={}, i={}, j={}, v={}".format(to_key, i, j, v))
        #logger.debug("limits key={}, dict={}".format(limit_key, limits))

        return v, i, j, idx_dir

    i, j, k = 0, 0, 0
    while k < nrows * ncols:
        v, i, j, idx_dir = helper_v2(m, i, j, idx_dir)
        spiral += v
        k += len(v)

    return spiral


# ----------------
#   Main
# ----------------
def init_logging():
    fmt = "%(asctime)s %(levelname)s [%(funcName)s] %(message)s"
    datefmt = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.DEBUG)


def main():
    """Main function"""
    init_logging()

    test_data =[
        [[1,2,3], [8,9,4], [7,6,5]],
        [[1,2,3,4], [12,13,14,5], [11,16,15,6],[10,9,8,7]],
        [],
    ]

    for m in test_data:
        logger.info("# Input = {}".format(m))
        logger.info("Spiral v1 => {}".format(spiral_v1(m)))
        logger.info("Spiral v2 => {}".format(spiral_v2(m)))


if __name__ == "__main__":
    main()
