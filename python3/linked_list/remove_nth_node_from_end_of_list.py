#!/usr/bin/env python3
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Examples:

  Input: head = [1,2,3,4,5], n = 2
  Output: [1,2,3,5]
  Example 2:

  Input: head = [1], n = 1
  Output: []
  Example 3:

  Input: head = [1,2], n = 1
  Output: [1]


Constraints:

 . The number of nodes in the list is sz.
 . 1 <= sz <= 30
 . 0 <= Node.val <= 100
 . 1 <= n <= sz

Follow up: Could you do this in one pass?

REFERENCE:
  - https://leetcode.com/problems/remove-nth-node-from-end-of-list/ (Medium)

"""

from typing import List
from linked_list_utils import *


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """Use two pointers; one is n-step ahead of the other."""
        # Sanity check
        if not head:
            return head

        # Use a pre-head to hold the beginning of the list
        prehead = ListNode(None, head)

        # Create two pointers; p2 is n-step ahead of p1
        p1 = prehead
        p2 = p1
        for _ in range(n):
            p2 = p2.next

        # Move both pointers until p2 reaches the end.
        while p2.next:
            p2 = p2.next
            p1 = p1.next

        # Remove the element next to p1
        p1.next = p1.next.next
        return prehead.next


# ----------------
#   Main
# ----------------
def main():
    """Main function"""

    test_data = [
        [[1,2,3,4,5], 2], # Output: [1,2,3,5]
        [[1], 1],   # Output: []
        [[1,2], 1], # Output: [1]
    ]

    sol = Solution()
    for vals, n in test_data:
        print("\n# Inputs: {}, n = {}".format(vals, n))

        head = make_linked_list(vals)
        out = sol.removeNthFromEnd(head, n)
        print("  Output: {}".format(lnode2str(out)))


if __name__ == "__main__":
    main()
