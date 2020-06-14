#!/usr/bin/env python3
"""
Remove all elements from a linked list of integers that have value val.

EXAMPLES:
  Input:  1->2->6->3->4->5->6, val = 6 
  Output: 1->2->3->4->5->6

REFERENCE:
  - https://leetcode.com/problems/remove-linked-list-elements/ (Easy)

"""

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prehead = ListNode(None, head)
        prev = prehead
        p = head
        while p:
            if p.val == val:
                prev.next = p.next
            else:
                prev = p
            p = p.next

        return prehead.next


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
        [make_list([]), 0],
        [make_list([1,2,6,3,4,5,6]), 6],
        [make_list([1,2,6,3,4,5,6]), 1],
    ]

    sol = Solution()
    for head, val in test_data:
        print("\n# Inputs: {}, val= {}".format(lnode2str(head), val))

        out = sol.removeElements(head, val)
        print("  Output: {}".format(lnode2str(out)))


if __name__ == "__main__":
    main()
