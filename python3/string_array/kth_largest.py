#!/usr/bin/env python3
"""
Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example, given [3,2,1,5,6,4] and k = 2, return 5.

Ref:
  https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
  https://www.programcreek.com/2014/05/leetcode-kth-largest-element-in-an-array-java/
"""

import logging
import heapq

logger = logging.getLogger(__name__)


def method1(a, k):
    """Sort first. Then pick up the desired position.
    :param a: Array
    :param k: Index to the k-th largest position.
    """
    # Use the built-in sort method here.
    a.sort()
    n = len(a)
    return a[n - k]


def method2(a, k):
    """Use a min heap as implemented in heapq library."""
    h = list()   # heap
    for i, x in enumerate(a):
        if i < k or x > h[0]:
            heapq.heappush(h, x)
    return h[0]


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

    a = [3, 2, 1, 5, 6, 4]
    logger.info("# Checking {}".format(a))
    for k in range(1, len(a)+1):
        logger.info("- method1(k={}) = {}".format(k, method1(a, k)))
        logger.info("- method2(k={}) = {}".format(k, method1(a, k)))


if __name__ == "__main__":
    main()
