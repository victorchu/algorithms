#!/usr/bin/env python3
"""
There are 2 sorted arrays A and B of size n each. Write an algorithm
to find the median of the array obtained after merging the above 2
arrays(i.e. array of length 2n). The complexity should be O(log(n)).

Example:

Input:  ar1 = [1, 12, 15, 26, 38]
        ar2 = [2, 13, 17, 30, 45]
Output: 16

Key functions:
  . np.mean(array)
  . np.median(array)
  . // : integer division
  . %  : mod

Ref:
  . https://www.geeksforgeeks.org/median-of-two-sorted-arrays/
"""


import logging
import numpy as np

logger = logging.getLogger(__name__)


def median(a):
    """My median function. An alternative is np.median()  """
    n = len(a)
    m = n // 2
    # logger.debug("a = {}, n = {}, m = {}".format(a, n, m))
    return a[m] if (n % 2 == 1) else (a[m-1] + a[m]) / 2.0


def method1(ar1, ar2):
    """Merge two arrays.

    Complexity is O(n).
    """
    # Find the medium positions [m1, m2] in the merged array.
    n = len(ar1)
    m1 = n - 1
    m2 = n
    logger.debug("Median indices = [{}, {}]".format(m1, m2))

    # Merge two array and track the positions:
    #   i for ar1, j for ar2, and k for the merged array.
    i, j, k = 0, 0, 0

    # Use a list to store median elements
    medians = list()

    while k <= m2:
        if (i < n) and (j < n):
            if ar1[i] < ar2[j]:
                x = ar1[i]
                i += 1
                k += 1
            else:
                x = ar2[j]
                j += 1
                k += 1
        elif i < n:
            x = ar1[i]
            i += 1
            k += 1
        else:
            x = ar2[j]
            j += 1
            k += 1

        if k > m1:
            logger.debug("Found k = {}, x = {}".format(k, x))
            medians.append(x)

    return np.mean(medians)


def method2(ar1, ar2):
    """Compare the medians of the two arrays and remove irrelevant parts.

    The key concept is that the median is the 'middle' value.
    Given two medians m1 and m2 from two arrays.
    If m1 < m2, then the first half of array 1 and 2nd half of the
    array 2 can be safely removed.

    E.g.
       1. [1, 12, 15, 16, 26, 38] (15.5) & [2, 13, 16, 17, 30, 45] (16.5)
       2. [16, 26, 38] (26) & [2, 13, 16] (13)
       3. [16, 26] (21) & [13, 16] (14.5)
       4. [16] & [16]

    Complexity is O(log(n)).
    """
    def helper(a1, a2):
        n = len(a1)

        # Termination condition
        if n == 1:
            logger.debug("End of search with {} & {}".format(a1, a2))
            return (a1[0] + a2[0]) / 2.0

        # Compare the medians
        m1 = median(a1)
        m2 = median(a2)
        logger.debug("Comparing {} ({}) with {} ({})".format(a1, m1, a2, m2))

        k = n // 2
        if n % 2 == 0:
            k1 = k2 = k
        else:
            k1 = k
            k2 = k + 1

        if m1 == m2:
            return m1
        elif m1 > m2:
            # Remove the larger half of a1 and the smaller half of a2.
            return helper(a1[0:k2], a2[k1:])
        else:
            # Remove the smaller half of a1 and the larger half of a2.
            return helper(a1[k1:], a2[0:k2])

    m = helper(ar1, ar2)
    return m


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

    sample_data = [
        [[1, 12, 15, 26, 38], [2, 13, 17, 30, 45]],
        [[1, 12, 15, 16, 26, 38], [2, 13, 16, 17, 30, 45]],
        [[1, 12, 16, 26, 38], [2, 13, 16, 30, 45]],
        [[1, 2, 12, 13, 15], [17, 26, 30, 38, 45]],
    ]
    for ar1, ar2 in sample_data:
        logger.info("# Finding median of {} and {}".format(ar1, ar2))
        logger.info("(1) {}".format(method1(ar1, ar2)))
        logger.info("(2) {}".format(method2(ar1, ar2)))


if __name__ == "__main__":
    main()
