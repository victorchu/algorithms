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
from linked_list_utils import *


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
def main():
    """Main function"""

    test_data = [
        [[], 0],
        [[1,2,6,3,4,5,6], 6],
        [[1,2,6,3,4,5,6], 1],
    ]

    sol = Solution()
    for vals, val in test_data:
        print("\n# Inputs: {}, val to remove = {}".format(vals, val))

        head = make_linked_list(vals)
        out = sol.removeElements(head, val)
        print("  Output: {}".format(lnode2str(out)))


if __name__ == "__main__":
    main()
