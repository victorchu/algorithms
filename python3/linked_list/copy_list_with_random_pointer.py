#!/usr/bin/env python3
"""
You are given a Double Link List with one pointer of each node pointing to the next node just
like in a single link list. The second pointer however CAN point to any node in the list and
not just the previous node. 

Now write a program in O(n) time to duplicate (clone) this list.
That is, write a program which will create a copy of this list.
All of those random pointers need to point to the same corresponing
nodes in the new list.

EXAMPLES:
   Each node has 'val', 'next', and 'random' attributes.
   Only the [val, random] will be shown in the example:

   Input 1 = (7,None) -> (13,0) -> (11,4) -> (10,2) -> (1,0) -> None

   Input 2 = (1,1) -> (2,1) -> None

REF:
  - https://leetcode.com/problems/copy-list-with-random-pointer/ (Medium)
  - https://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/

"""

from typing import List


class Node:
    def __init__(self, x:int, next:'Node'=None, random:'Node'=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def copyRandomList_v1(self, head: 'Node') -> 'Node':
        """Dictionary & Array.

        Helper data structures:
        - Dictionary: {original_node: index}
        - Array: [new_node]

        Then, origina_node -> original_random_node -> index -> new_random_node

        Use 3 x O(n) extra space.
        LeatCode: 36ms, 14.4 MB, beats 64%.
        """
        new_nodes = list()
        prehead = Node(0)

        # Convert random pointers to indexes.
        index_map = dict()
        p = head
        q = prehead
        i = 0
        while p:
            # Update index map
            index_map[p] = i
            i += 1

            # Clone node with value & keep a copy in new_nodes
            q.next = q = Node(p.val)
            new_nodes.append(q)
            p = p.next

        # Update the random pointer
        p = head
        q = prehead.next
        while (p and q):
            # Get random index
            r = p.random
            if r is not None:
                i = index_map[r]
                q.random = new_nodes[i]
            p = p.next
            q = q.next

        return prehead.next

    def copyRandomList_v2(self, head: 'Node') -> 'Node':
        """Dictionary.

        Use a dictionay to connect original list with the new list.
        It doesn't need to know the index position of the random link.
        This may not be faster than v1.

        Use 2 x O(n) extra space.
        LeatCode: 32 ms, 14.4 MB, beats 86.78%.
        """
        prehead = Node(0)

        # Convert random pointers to indexes.
        node_map = dict()
        p = head
        q = prehead
        while p:
            # Here we copy both the value and the random pointer
            q.next = q = Node(p.val, None, p.random)
            node_map[p] = q
            p = p.next

        # Update the random pointer
        q = prehead.next
        while q:
            # This is the random pointer from the original list
            r = q.random
            if r is not None:
                # Use the dictionary to get the corresponding node
                q.random = node_map[r]
            q = q.next

        return prehead.next

# ----------------
#   Main
# ----------------
def make_list(a: List) -> 'Node':
    """Create
    :param a: a list of (val,random) pairs
    """
    p = prehead = Node(0)
    # Build the single list and keep them in Python list
    tmp_list = list()
    for x in a:
        p.next = p = Node(x[0])
        tmp_list.append(p)

    # Handle the random attribute
    p = prehead.next
    n = len(tmp_list)
    for x in a:
        i = x[1]
        if i is not None and i < n:
            p.random = tmp_list[i]
        else:
            p.random = None
        p = p.next

    return prehead.next


def get_val_random_list(p: Node) -> str:
    """Convert a ListNode to a string."""

    head = p
    # Store the list in a dictionary
    index_map = dict()
    i = 0
    while p:
        index_map[p] = i
        i += 1
        p = p.next
        
    # Build a list of (val, random_index)
    retvals = list()
    p = head
    while (p):
        val = p.val
        r = p.random
        random_index = index_map[r] if (r in index_map) else None
        retvals.append([val, random_index])
        p = p.next

    return retvals


def main():
    """Main function"""

    test_data = [
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        [[1, 1], [2, 1]],
        [[3, None], [3, 0], [3, None]],
        [],
    ]

    sol = Solution()
    for x in test_data:
        print("# Input =", x)
        head = make_list(x)
        print("  1> =", get_val_random_list(sol.copyRandomList_v1(head)))
        print("  2> =", get_val_random_list(sol.copyRandomList_v2(head)))


if __name__ == "__main__":
    main()
