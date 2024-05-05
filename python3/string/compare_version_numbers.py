#!/usr/bin/env python3
"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1; otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is
the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to
be 0. For example, version number 3.4 has a revision number of 3 and 4 for its
first and second level revision number.  Its third and fourth level revision
number are both 0.

EXAMPLES:

  Input: version1 = "0.1", version2 = "1.1"
  Output: -1

  Input: version1 = "1.0.1", version2 = "1"
  Output: 1

  Input: version1 = "7.5.2.4", version2 = "7.5.3"
  Output: -1

  Input: version1 = "1.01", version2 = "1.001"
  Output: 0

  Input: version1 = "1.0", version2 = "1.0.0"
  Output: 0

Note:
  - Version strings are composed of numeric strings separated by dots . and this numeric strings may have leading zeroes.
  - Version strings do not start or end with dots, and they will not be two consecutive dots.

REFERENCE:
  - https://leetcode.com/problems/compare-version-numbers/ (Medium)
  - https://stackoverflow.com/questions/1277278/is-there-a-zip-like-function-that-pads-to-longest-length-in-python

"""

from typing import List
from itertools import zip_longest


class Solution:
    def compareVersion_v1(self, version1: str, version2: str) -> int:
        """Use itertools.zip_longest"""
        nums1 = [int(x) for x in version1.split('.')]
        nums2 = [int(x) for x in version2.split('.')]

        for v1, v2 in zip_longest(nums1, nums2, fillvalue=0):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0

    def compareVersion_v2(self, version1: str, version2: str) -> int:
        """Use itertools.zip_longest"""
        nums1 = [int(x) for x in version1.split('.')]
        nums2 = [int(x) for x in version2.split('.')]
        n1 = len(nums1)
        n2 = len(nums2)
        n = max(n1, n2)

        for i in range(n):
            v1 = nums1[i] if i < n1 else 0
            v2 = nums2[i] if i < n2 else 0
            if v1 == v2:
                continue
            else:
                return 1 if v1 > v2 else -1
        return 0


def main():
    test_data = [
        ['0.1', '1.1'],
        ['1.0.1', '1'],
        ['7.5.2.4', '7.5.3'],
        ['1.01', '1.001'],
        ['1.0', '1.0.0'],
    ]

    sol = Solution()
    for version1, version2 in test_data:
        print("# Input  : '{}' vs '{}'".format(version1, version2))
        print("  Output : {}".format(sol.compareVersion_v1(version1, version2)))
        print("  Output : {}".format(sol.compareVersion_v2(version1, version2)))


if __name__ == "__main__":
    main()
