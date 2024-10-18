"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

Ref:
 - https://leetcode.com/problems/add-two-numbers/ (Medium)
 - https://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/

"""

from linked_list_utils import *


class Solution:
    def addTwoNumbers_v1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Direct summaration, node by node."""
        p = prehead = ListNode()
        carry = 0
        while l1 or l2 or carry:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            p.next = ListNode(s % 10)
            p = p.next
            carry = s // 10
        return prehead.next
    
    def addTwoNumbers_v2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Convert lists to integers and then conver the sume of integers back to a list.
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
        """Convert to int, then string. This is simplier than the previous one."""
        def to_int(p: ListNode) -> int:
            n = 0
            w = 1
            while(p):
                n = w * p.val + n
                w *= 10
                p = p.next
            return n

        # sum of two linked lists        
        sum_str = str(to_int(l1) + to_int(l2))

        # Convert it back to a linked list
        head = None
        for c in sum_str[::-1]:
            if not head:
                p = head = ListNode(int(c))
            else:
                p.next = ListNode(int(c))
                p = p.next
        return head


def main():
    """Main function"""

    test_data = [
        [[2,4,3],[5,6,4],[7,0,8]],
        [[0],[0],[0]],
        [[9,9,9,9,9,9,9],[9,9,9,9],[8,9,9,9,0,0,1]]
    ]

    ob1 = Solution()
    for a1, a2, ans in test_data:
        l1 = list2lnode(a1)
        l2 = list2lnode(a2)
        print(f"\n# Inputs: {a1}, {a2} ...... {ans}")
        print(f"  Output v1 = {lnode2list(ob1.addTwoNumbers_v1(l1, l2))}")
        print(f"  Output v2 = {lnode2list(ob1.addTwoNumbers_v2(l1, l2))}")
        print(f"  Output v3 = {lnode2list(ob1.addTwoNumbers_v3(l1, l2))}")


if __name__ == "__main__":
    main()
