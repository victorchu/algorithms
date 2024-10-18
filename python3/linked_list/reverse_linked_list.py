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
# from linked_list.linked_list_utils import *


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
        p = head
        while p.next:
            tmp = p.next  # will make it a new head
            p.next = tmp.next
            tmp.next = head
            head = tmp
        return head

    def reverseList_v3(self, head: ListNode) -> ListNode:
        """Inplace + Recursion."""
        def helper(p, head):
            if not p or not p.next:
                return head
            tmp = p.next
            p.next = tmp.next
            tmp.next = head
            return helper(p, tmp)

        return helper(head, head)


def main():
    """Main function"""

    test_data = [
        [1, 2, 3, 4, 5],
    ]

    ob1 = Solution()
    for data in test_data:
        print(f"\n# Input: {data}")
        print(f"  Output v1a: {lnode2list(ob1.reverseList_v1a(list2lnode(data)))}")
        print(f"  Output v1b: {lnode2list(ob1.reverseList_v1b(list2lnode(data)))}")
        print(f"  Output v2:  {lnode2list(ob1.reverseList_v2(list2lnode(data)))}")
        print(f"  Output v3:  {lnode2list(ob1.reverseList_v3(list2lnode(data)))}")


if __name__ == "__main__":
    main()
