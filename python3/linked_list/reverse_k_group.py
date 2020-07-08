#!/usr/bin/env python3
"""
Given a linked list, reverse the nodes of a linked list k at a time and return
its modified list.

k is a positive integer and is less than or equal to the length of the linked
list. If the number of nodes is not a multiple of k then left-out nodes in the
end should remain as it is.

Example:

  Given this linked list: 1->2->3->4->5
  For k = 2, you should return: 2->1->4->3->5
  For k = 3, you should return: 3->2->1->4->5

Note:
  - Only constant extra memory is allowed.
  - You may not alter the values in the list's nodes, only nodes itself may be changed.

REFERENCE:
  - https://leetcode.com/problems/reverse-nodes-in-k-group/ (Hard)

"""

from typing import List
from linked_list_utils import *


class Solution:

    def reverseKGroup_v1(self, head: ListNode, k: int) -> ListNode:
        """Double pointer."""
        # Find the reverse head
        p = head
        for i in range(k-1):
            if p:
                p = p.next
        rhead = p

        # The list doesn't have k nodes
        if not rhead:
            return head

        # Start to reverse in group.
        p1 = head
        p2 = rhead.next  # points to k nodes ahead
        tail = head      # the current tail position
        prev = None
        i = 1
        while p1:
            tmp = p1.next
            p1.next = prev
            prev = p1

            # Reached end of a k-group
            if i % k == 0:
                if p2:
                    # Connect the tail with the next k-group
                    tail.next = p2
                    tail = tmp
                    prev = None
                else:
                    # Don't have another k-group.  Connect with the remaining.
                    tail.next = tmp
                    break

            i += 1
            p1 = tmp
            if p2:
                p2 = p2.next

        return rhead

    def reverseKGroup_v2(self, head: ListNode, k: int) -> ListNode:
        """Double pointer."""
        # Find the reverse head
        p = head
        for i in range(k-1):
            if p:
                p = p.next
        if not p:
            return head

        # Pointers
        rhead = p
        rtail = head
        p2 = rhead  # the head of the next k-group
        p1 = head

        while p1:
            # Reverse one k-group
            prev = None
            for _ in range(k):
                tmp_next = p1.next
                p1.next = prev
                prev = p1
                p1 = tmp_next
                if p2:
                    p2 = p2.next

            # Connect k-groups
            if p2:
                rtail.next = p2
                tail = p1
            else:
                rtail.next = p1
                break

        return rhead


def main():
    """Main function"""

    test_data = [
        [[1, 2, 3, 4, 5], 2],
        [[1, 2, 3, 4, 5], 3],
        [[1, 2, 3, 4, 5], 5],
        [[1, 2, 3, 4, 5], 6],
        [[1, 2, 3, 4, 5], 1],
    ]

    obj = Solution()
    for data, k in test_data:
        print("\n# Input: {}, k = {}".format(data, k))
        head = make_linked_list(data)
        print("  Output v1: {}".format(lnode2str(obj.reverseKGroup_v1(head, k))))
        head = make_linked_list(data)
        print("  Output v2: {}".format(lnode2str(obj.reverseKGroup_v2(head, k))))


if __name__ == "__main__":
    main()
