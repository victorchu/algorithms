#!/usr/bin/env python3
"""
Given a singly linked list L: L0 -> L1 -> ... -> Ln-1 -> Ln,
reorder it to: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

You may not modify the values in the list's nodes, only nodes itself may be changed.

EXAMPLES:
  Input:  1->2->3->4, 
  Output: 1->4->2->3

Example 2:
  Input:  1->2->3->4->5
  Output: 1->5->2->4->3

REFERENCE:
  - https://leetcode.com/problems/reorder-list/ (Medium)

"""

from typing import List
from linked_list_utils import *


class Solution:

    def reorderList(self, head: ListNode) -> None:
        """Use a stack to help.

        LeatCode: 84 ms, 23.2 MB, runtime beats 97.80%
        """
        # Special case when the head is empty
        if not head:
            return

        # Copy ListNode to a Python list
        stack = list()
        p = head
        while p:
            stack.append(p)
            p = p.next
        n = len(stack)

        # Re-construct the list
        i = 0
        j = len(stack) - 1

        # Handle pairs
        p = head
        while (i < j - 1):
            tmp = p.next
            p.next = q = stack.pop()
            q.next = p = tmp
            j -= 1
            i += 1

        # Handle the final one from the stack
        if (i < j):
            p.next = q = stack.pop()
            p = q
            j -= 1

        # Terminate the last node.
        p.next = None


def main():
    """Main function"""

    test_data = [
        [],
        [1],
        [1, 2],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
    ]

    sol = Solution()
    for data in test_data:
        print("\n# Inputs: {}".format(data))

        head = make_linked_list(data)
        sol.reorderList(head)
        print("  Output: {}".format(lnode2str(head)))


if __name__ == "__main__":
    main()
