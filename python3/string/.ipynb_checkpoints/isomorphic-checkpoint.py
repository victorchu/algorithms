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
    def is_isomorphic_v1(self, s1, s2):
        """Use two dictionaries.

        Time is O(n). Storage is O(unique characters)
        """
        if len(s1) == len(s2):
            m1 = dict()
            m2 = dict()
            retval = True

            for c1, c2 in zip(s1, s2):
                if (c1 in m1) and m1[c1] != c2:
                    retval = False
                    break
                elif (c2 in m2) and m2[c2] != c1:
                    retval = False
                    break
                else:
                    m1[c1] = c2
                    m2[c2] = c1
        else:
            retval = False
        return retval


    def is_isomorphic_v2(so, s1, s2):
        """Use one dictionary.  Then, check if the values are unique.

        Time is O(n). Storage is O(unique characters)
        """
        if len(s1) == len(s2):
            m = dict()
            retval = True

            # Check one-way mapping.
            # Yet, different chars from s1 can map to the same char in s2.
            for c1, c2 in zip(s1, s2):
                if (c1 in m) and m[c1] != c2:
                    retval = False
                    break
                else:
                    m[c1] = c2

            # Check the number of unique values
            if len(m) != len(set(m.values())):
                retval = False
        else:
            retval = False
        return retval


def main():
    test_data = [
        ['egg', 'add'],
        ['aab', 'xxy'],
        ['foo', 'bar']
    ]

    sol = Solution()
    for s1, s2 in test_data:
        print("# Are '{}' and '{}' isomorphic?".format(s1, s2))
        print("(1) {}".format(sol.is_isomorphic_v1(s1, s2)))
        print("(2) {}".format(sol.is_isomorphic_v2(s1, s2)))


if __name__ == "__main__":
    main()
