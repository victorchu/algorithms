#!/usr/bin/env python3
"""
Given a string S, return the "reversed" string where all characters that are not
a letter stay in the same place, and all letters reverse their positions.

EXAMPLES
  Input: "ab-cd"
  Output: "dc-ba"

Key functions:
  - str.isalpha()
  - list.append()
  - list.pop()
 
REFERENCE
  - https://leetcode.com/problems/reverse-only-letters/ (Easy)
  - https://www.geeksforgeeks.org/reverse-a-string-without-affecting-special-characters/

"""


class Solution:
    def reverse_v1(self, s):
        """A simple implementation that needs a stack.

        Complexity O(n). This method needs extra space (a stack).
        It also needs to check each character twice if it is special.

        :param s: The input string
        """
        # Helper spaces
        normal_list = list()
        output_list = list()

        # First iteration: push normal characters to a list
        for c in s:
            if c.isalpha():
                normal_list.append(c)

        # Second iteration: build the output list
        for c in s:
            if c.isalpha():
                output_list.append(normal_list.pop())
            else:
                output_list.append(c)

        # Use join to convert an array to a string.
        retval = "".join(output_list)

        print("reversed string = {}".format(retval))
        return retval

    def reverse_v2(self, s):
        """A smart implementaiton.

        This is a smart reverse method that doesn't take extra space.
        But, string is immutable.  So it is not that simple.
        We still need to convert it to a character array first.

        Complexity: O(n).

        :param s: The input string
        """
        # Convert string to a list, since string is immutable
        a = list(s)

        i = 0            # index from the left-hand side
        j = len(a) - 1   # index from the right-hand side
        while (i < j):
            if not a[i].isalpha():
                i += 1
            elif not a[j].isalpha():
                j -= 1
            else:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        retval = "".join(a)
        print("reversed string = {}".format(retval))
        return retval

    def reverse_v3(self, s):
        """A variation of the the smart implementaiton.

        This method uses 3 while loops.  
        Yet logically, this seems to be easier to understand.

        Complexity: O(n).

        :param s: The input string
        """
        # Convert string to a list, since string is immutable
        a = list(s)

        i = 0            # index from the left-hand side
        j = len(a) - 1   # index from the right-hand side

        while i < j:
            # Find the next normal character from the left
            while not a[i].isalpha():
                i += 1
            # Find the next normal character from the right
            while not a[j].isalpha():
                j -= 1
            # Swap normal characters
            if i < j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        retval = "".join(a)
        print("reversed string = {}".format(retval))
        return retval


def main():
    """Main function"""

    test_samples = [
        "> yp paHeB!",
        "(E!V)#@I.L/$y :-> ojnE"
    ]

    sol = Solution()
    for s in test_samples:
        print("## Reversing {} ...".format(s))
        print("Output v1 =", sol.reverse_v1(s))
        print("Output v2 =", sol.reverse_v2(s))
        print("Output v3 =", sol.reverse_v3(s))


if __name__ == "__main__":
    main()
