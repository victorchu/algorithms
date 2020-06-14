#!/usr/bin/env python3
"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

  Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
  Output: 7 -> 0 -> 8
  Explanation: 342 + 465 = 807.

Ref:
 - https://leetcode.com/problems/add-two-numbers/ (Medium)
 - https://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/
"""



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    val_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def addTwoNumbers_v1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Parallel processing two lists.  
        Convert the results directly to the output link list.

        LeatCode: 72ms, 14 MB, beats 66.51%
        """
        result = None
        p = None
        carry = 0

        while (l1 and l2):
            v = l1.val + l2.val + carry
            carry = v // 10
            v %= 10

            # Add to result
            if p:
                p.next = ListNode(v)
                p = p.next
            else:
                p = ListNode(v)
                result = p

            # Move link list pointer
            l1 = l1.next
            l2 = l2.next

        # If l1 and l2 are not of the same length
        for q in [l1, l2]:
            while q:
                v = q.val + carry
                carry = v // 10
                v %= 10

                # Add to result
                if p:
                    p.next = ListNode(v)
                    p = p.next
                else:
                    p = ListNode(v)
                    result = p
                q = q.next

        # Final carry
        if carry:
            p.next = ListNode(carry)

        return result

    def addTwoNumbers_v2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Convert lists to integers and then conver the sume of integers back to a list.

        LeetCode: 68 ms, 13.7 MB; beats 84.47%.
        """
        def to_int(l: ListNode) -> int:
            """Convert a ListNode to an integer"""
            val = 0
            base = 1
            while l:
                val += l.val * base
                base *= 10
                l = l.next
            return val

        def to_ListNode(n: int) -> ListNode:
            """Convert an integer back to a ListNode, in reverse order."""
            head = None
            if n == 0:
                head = ListNode(n)
            else:
                v = n % 10
                n = n // 10
                head = ListNode(v)
                p = head

                while (n != 0):
                    # Get the least digit
                    v = n % 10
                    n = n // 10

                    # Add to the ListNode
                    p.next = ListNode(v)
                    p = p.next
            return head

        v1 = to_int(l1)
        v2 = to_int(l2)
        result = to_ListNode(v1 + v2)
        return result

    def addTwoNumbers_v3(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Use a "prehead" to simplify the logic.

        LeatCode: 64 ms, 14 MB; beats 94.54%
        """
        p = prehead = ListNode()
        carry = 0

        # Use or to reduce the number of loops
        while l1 or l2:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next

            carry = s // 10
            p.next = ListNode(s % 10)
            p = p.next

        # Handle the final carry
        if carry:
            p.next = ListNode(carry)

        # Return the next of the prehead
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


def main():
    """Main function"""

    test_data = [
        [ListNode(2, ListNode(4, ListNode(3))),
         ListNode(5, ListNode(6, ListNode(4)))],
        [ListNode(2, ListNode(4, ListNode(8))),
         ListNode(5, ListNode(6, ListNode(4)))],
        [ListNode(0), ListNode(7, ListNode(3))]
    ]

    sol = Solution()
    for l1, l2 in test_data:
        print("\n# Inputs: l1={}, l2={}".format(lnode2str(l1), lnode2str(l2)))
        print(" - v1 > {}".format(lnode2str(sol.addTwoNumbers_v1(l1, l2))))
        print(" - v2 > {}".format(lnode2str(sol.addTwoNumbers_v2(l1, l2))))
        print(" - v3 > {}".format(lnode2str(sol.addTwoNumbers_v3(l1, l2))))


if __name__ == "__main__":
    main()
