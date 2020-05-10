#!/usr/bin/env python3
"""
QUESTION:

Convert a Binary Search Tree (BST) to a sorted Circular Doubly-Linked List in place.

The node of a tree structure has three attributes: val, left, right.
You can think of the 'left' and 'right' pointers as synonymous to the
'predecessor' (prev) and 'successor' (next) pointers in a doubly-linked list. 

For a "circular" doubly linked list, the predecessor of the first element
is the last element, and the successor of the last element is the
first element.

We want to do the transformation in place. After the transformation,
the left pointer of the tree node should point to its predecessor,
and the right pointer should point to its successor. You should
return the pointer to the smallest element of the linked list.

EXAMPLE:

  Input:
           [4]
           /  \
         [2]   [5]
        /   \ 
      [1]   [3]

  Output:
                 +-------------------------------+
                 |                               v
      [head] -> [1] <-> [2] <-> [3] <-> [4] <-> [5]
                 ^                               |
                 +-------------------------------+
  
TECHNIQUES:
  - In-order tree traversal.
  - Double linked-list.

"""

from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @property
    def prev(self):
        """Define prev as an alias to left"""
        return self.left

    @prev.setter
    def prev(self, val):
        self.left = val

    @property
    def next(self):
        """Define next as an alias to right"""
        return self.right

    @next.setter
    def next(self, val):
        self.next = val


class Solution:

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        Use in-order to traverse the tree.
        Then, convert one-by-one into the double linked-list structure.

        LeetCode: 32 ms, 14.9 MB, beats 84.54%.
        """
        def process_node(head, node):
            """Helper function."""
            # Process the left branch
            if node.left:
                process_node(head, node.left)

            # Process this node
            if head.left:
                # Append this node to the tail (head.left)
                head.left.right = node
                node.left = head.left
                head.left = node
            else:
                # Handle the first node.
                head.left = head.right = node

            # Process the right branch
            if node.right:
                process_node(head, node.right)

        # The head node. 
        # - head.right points to the first node.  
        # - head.left points to the tail node.
        head = Node(None)

        # Make sure that root is not empty
        if root:
            # Build the double linked-list.
            process_node(head, root)
            # Connect the first node with the last node
            head.right.left = head.left
            head.left.right = head.right

        # Return the first node
        return head.right


# ---------------------------
#   Main & Helper Functions
# ---------------------------
def make_bst(vals: List) -> Node:
    """Create a BST from a value list."""
    def add(node, val):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                add(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                add(node.right, val)
    if vals:
        root = Node(vals[0])
        for val in vals[1:]:
            add(root, val)
    else:
        root = None
    return root


def bst_to_list(root: 'Node') -> None:
    """Convert a BST to a value list, follow the layer by layer order."""
    vals = list()
    queue = [root]
    while queue:
        p = queue.pop(0)
        vals.append(p.val)
        if p.left:
            queue.append(p.left)
        if p.right:
            queue.append(p.right)
    return vals


def cdl_to_list(head: 'Node') -> None:
    """Convert a circular double linked-list to a list."""
    vals = list()
    p = head
    while p:
        vals.append(p.val)
        p = p.next
        if p == head:
            break
    return vals


def main():
    """Main function"""

    # Test data
    test_data = [
        [4, 2, 5, 1, 3],
        [2, 1, 3],
        [],
        [1],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
    ]

    sol = Solution()
    for vals in test_data:
        root = make_bst(vals)

        print("\n# Input  = {}".format(vals))

        cdl = sol.treeToDoublyList(root)
        out_vals = cdl_to_list(cdl)
        print("  Output = {}".format(out_vals))


if __name__ == "__main__":
    main()
