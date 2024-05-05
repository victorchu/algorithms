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
  - https://leetcode.com/problems/rotate-array/ (Easy)
  - https://www.programcreek.com/2015/03/rotate-array-in-java/ 

"""

class Solution:
    def _rotate_k(self, a, k):
        """Helper function."""
        return a[-k:] + a[0:-k]


    def rotate_v1(self, a, k):
        """Rotate one at a time using an extra array.
        Time is O(n*k).  Space is O(n).
        """
        for i in range(k % len(a)):
            a = self._rotate_k(a, 1)
        return a


    def rotate_v2(self, a, k):
        """One single rotate with an extra array.
        Time is O(n).  Space is O(n).
        """
        return self._rotate_k(a, k % len(a))


    def rotate_v3(self, a, k, clone=True):
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


    def rotate_v4(self, a, k, clone=True):
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
def main():
    a = list(range(7))
    sol = Solution()
    for k in [0, 2, 4, 8]:
        print("# RIGHT-ROTATING {} for {} times".format(a, k))
        print("(1) {}".format(sol.rotate_v1(a, k)))
        print("(2) {}".format(sol.rotate_v2(a, k)))
        print("(3) {}".format(sol.rotate_v3(a, k)))
        print("(4) {}".format(sol.rotate_v4(a, k)))


if __name__ == "__main__":
    main()
