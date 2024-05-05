#!/usr/bin/env python3
"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:
  Input:  1->2->4, 1->3->5
  Output: 1->1->2->3->4->5

Ref:
  - https://leetcode.com/problems/merge-two-sorted-lists/ (Easy)
  - https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/

"""

from linked_list_utils import *


class Solution:

    def mergeTwoLists_v1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """This approach is quite standard.

        Complexity: O(n).
        """
        # Create a pre-head to simply the remaining process
        prehead = p = ListNode()

        # When both l1 & l2 are valid
        while (l1 and l2):
            if (l1.val < l2.val):
                p.next = p = ListNode(l1.val)
                l1 = l1.next
            else:
                p.next = p = ListNode(l2.val)
                l2 = l2.next
        # Handle the remaining part of l1
        while l1:
            p.next = p = ListNode(l1.val)
            l1 = l1.next

        # Handle the remaining part of l2
        while l2:
            p.next = p = ListNode(l2.val)
            l2 = l2.next

        # Return the node after the pre-head
        return prehead.next

    def mergeTwoLists_v2(self, p: ListNode, q: ListNode, dedupe=True) -> ListNode:
        """Compact code with one loop.  Support dedupping.

        Complexity: O(n).
        """
        def append(curr, x):
            if not dedupe or (curr.val == None) or (curr.val != x.val):
                curr.next = ListNode(x.val)
                curr = curr.next
            return curr
                
        head = ListNode(None)
        curr = head
        while (p or q):
            if p and (not q or (p.val < q.val)):
                curr = append(curr, p)
                p = p.next
            else:
                curr = append(curr, q)
                q = q.next

        return head.next


# ----------------
#   Main
# ----------------
def main():
    """Main function"""

    test_data = [
        [ListNode(1, ListNode(2, ListNode(4))),
         ListNode(1, ListNode(3, ListNode(5)))],
    ]

    sol = Solution()
    methods = [sol.mergeTwoLists_v1, sol.mergeTwoLists_v2]
    for l1, l2 in test_data:
        print("\n# Inputs: l1={}, l2={}".format(lnode2str(l1), lnode2str(l2)))
        for i, f in enumerate(methods, start=1):
            merged_list = f(l1, l2)
            print(f" - v{i} > {lnode2str(merged_list)}")


if __name__ == "__main__":
    main()
