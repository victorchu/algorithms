#!/usr/bin/env python3
"""
Reverse a singly linked list.

Example:

  Input: 1->2->3->4->5->NULL
  Output: 5->4->3->2->1->NULL

Follow up:
  - A linked list can be reversed either iteratively or recursively.
    Could you implement both?

REFERENCE:
  - https://leetcode.com/problems/reverse-linked-list/ (Easy)

"""

from typing import List
from linked_list_utils import *


class Solution:

    def reverseList_v1a(self, head: ListNode) -> ListNode:
        """Use stack."""
        if not head:
            return

        # Put into a stack
        stack = list()
        p = head
        while p:
            stack.append(p)
            p = p.next

        # Build the new order
        p = prehead = ListNode()
        while stack:
            node = stack.pop()
            p.next = node
            p = p.next
        p.next = None

        return prehead.next

    def reverseList_v1b(self, head: ListNode) -> ListNode:
        """Use stack."""
        if not head:
            return

        # Put into a stack
        stack = list()
        p = head
        while p:
            stack.append(p)
            p = p.next

        # Build the new order
        head, p = None, None
        while stack:
            node = stack.pop()
            if not head:
                head = node
                p = head
            else:
                p.next = node
                p = p.next
        p.next = None

        return head

    def reverseList_v2(self, head: ListNode) -> ListNode:
        """Inplace."""
        prev = None
        p = head
        while p:
            tmp = p.next    # pointer to the next node
            p.next = prev   # point to the previous node
            prev = p
            p = tmp
        return prev

    def reverseList_v3(self, head: ListNode) -> ListNode:
        """Inplace + Recursion."""
        def helper(node, prev):
            if not node:
                return prev
            tmp = node.next
            node.next = prev
            return helper(tmp, node)

        return helper(head, None)


def main():
    """Main function"""

    test_data = [
        [1, 2, 3, 4, 5],
    ]

    obj = Solution()
    for data in test_data:
        print("\n# Input: {}".format(data))

        print("  Output v1a: {}".format(lnode2str(obj.reverseList_v1a(make_linked_list(data)))))
        print("  Output v1b: {}".format(lnode2str(obj.reverseList_v1b(make_linked_list(data)))))
        print("  Output v2:  {}".format(lnode2str(obj.reverseList_v2(make_linked_list(data)))))
        print("  Output v3:  {}".format(lnode2str(obj.reverseList_v3(make_linked_list(data)))))


if __name__ == "__main__":
    main()
