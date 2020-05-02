#!/usr/bin/env python3
"""
Right-rotate an array by k steps.

Examples:
  Input:  [0, 1, 2, 3, 4, 5, 6], k = 2
  Output: [5, 6, 0, 1, 2, 3, 4]

Key functions:
  - reversed(series)
  - array slices: a[i,j], a[i:], a[-k], ...

Ref:
  - https://www.programcreek.com/2015/03/rotate-array-in-java/ 
"""

import logging
logger = logging.getLogger(__name__)


def _rotate_k(a, k):
    """Helper function."""
    return a[-k:] + a[0:-k]


def rotate_v1(a, k):
    """Rotate one at a time using an extra array.
    Time is O(n*k).  Space is O(n).
    """
    for i in range(k % len(a)):
        a = _rotate_k(a, 1)
    return a


def rotate_v2(a, k):
    """One single rotate with an extra array.
    Time is O(n).  Space is O(n).
    """
    return _rotate_k(a, k % len(a))


def rotate_v3(a, k, clone=True):
    """The bubble method.
    Time is O(n * k).  Space is O(1).
    """
    def _bubble(a):
        tmp = a[-1]
        for j in reversed(range(1, len(a))):
            a[j] = a[j-1]
        a[0] = tmp

    if clone:
        a = a.copy()
    for i in range(k % len(a)):
        _bubble(a)
    return a


def rotate_v4(a, k, clone=True):
    """The double reverse method.

    Time is O(n * 2).  Space is O(1).
    """
    def _reverse(a, i, j):
        while (i < j):
            a[j], a[i] = a[i], a[j]
            i += 1
            j -= 1

    if clone:
        a = a.copy()
    k = k % len(a)
    n = len(a)
    _reverse(a, 0, n-k-1)
    _reverse(a, n-k, n-1)
    _reverse(a, 0, n-1)
    return a


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

    a = list(range(7))
    for k in [0, 2, 4, 8]:
        logger.info("# RIGHT-ROTATING {} for {} times".format(a, k))
        logger.info("(1) {}".format(rotate_v1(a, k)))
        logger.info("(2) {}".format(rotate_v2(a, k)))
        logger.info("(3) {}".format(rotate_v3(a, k)))
        logger.info("(4) {}".format(rotate_v4(a, k)))


if __name__ == "__main__":
    main()
