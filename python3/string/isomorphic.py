#!/usr/bin/env python3
"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.


Examples:
  "egg" and "add" are isomorphic. ('e'->'a', 'g'->'d')
  "foo" and "bar" are not.  ('f'->'b', 'o'->'a', 'o'->'r'???)

Key functions:
  - dict(): dictionary/hashmap.
  - len(dict) : number of key-value pairs in the dictionary.
  - dict.values(): an array of values.
  - zip(s1, s2): to iterate from charaters in two strings.
  - set(): store unique values

Ref:
  - https://leetcode.com/problems/isomorphic-strings/ (Easy)
  - https://www.geeksforgeeks.org/check-if-two-given-strings-are-isomorphic-to-each-other/

"""


import re


class Solution:
    def is_isomorphic_v1(self, s1: str, s2: str) -> bool:
        """Use two dictionaries for tracking.

        Time Complexity: O(n), Space Complexity: O(number of unique characters)
        """
        if len(s1) != len(s2):
            return False
        d1 = dict()
        d2 = dict()   # this can be a set
        for c1, c2 in zip(s1, s2):
            if c1 in d1:
                # Check if it matches the existing mapping
                if d1[c1] == c2:
                    continue
                else:
                    return False
            else:
                # Found a new mapping
                if c2 not in d2:
                    d1[c1] = c2  # forward mapping
                    d2[c2] = c1  # reverse mapping
                else:
                    return False

        return True
    
    def is_isomorphic_v2(self, s1: str, s2: str) -> bool:
        """Use one dictionarie. Then validate the the values are unique.

        Time Complexity: O(n), Space Complexity: O(number of unique characters)
        """
        if len(s1) != len(s2):
            return False
        d = dict()
        for c1, c2 in zip(s1, s2):
            if c1 in d:
                if d[c1] != c2:
                    return False
            else:
                d[c1] = c2
        if len(d) != len(set(d.values())):
            return False
        return True


def main():
    test_data = [
        ['egg', 'add'],
        ['aabc', 'xxyx'],
        ['foo', 'bar']
    ]

    ob1 = Solution()
    for s1, s2 in test_data:
        print(f"# Input = '{s1}', '{s2}'")
        print(f"  output v1 = {ob1.is_isomorphic_v1(s1, s2)}")
        print(f"  output v2 = {ob1.is_isomorphic_v2(s1, s2)}")


if __name__ == "__main__":
    main()
