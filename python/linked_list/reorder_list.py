#!/usr/bin/env python3
"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
  Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
  Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

"""

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


# ----------------
#   Main
# ----------------
def lnode2str(p: ListNode) -> str:
    """Convert a ListNode to a string."""
    x = list()
    while (p):
        x.append(str(p.val))
        p = p.next
    return "({})".format(", ".join(x))


def make_list(a: List) -> ListNode:
    """Convert a Python list to a ListNode list."""
    p = prehead = ListNode()
    for x in a:
        p.next = p = ListNode(x)
    return prehead.next


def main():
    """Main function"""

    test_data = [
        make_list([]),
        make_list([1]),
        make_list([1,2]),
        make_list([1,2,3,4]),
        make_list([1,2,3,4,5]),
    ]

    sol = Solution()
    for head in test_data:
        print("\n# Inputs: {}".format(lnode2str(head)))

        # head will be modified.
        sol.reorderList(head)
        print(" output = {}".format(lnode2str(head)))


if __name__ == "__main__":
    main()
