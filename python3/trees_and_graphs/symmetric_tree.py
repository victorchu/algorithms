#!/usr/bin/env python3
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

EXAMPLES:

             [1]
            /   \
         [2]     [2]
         / \     / \
       [3] [4] [4] [3]

  Input: root = [1,2,2,3,4,4,3]
  Output: True

             [1]
            /   \
         [2]     [2]
           \       \
           [3]     [3]

  Input: root = [1,2,2,None,3,None,3]
  Output: False

FOLLOW UP:
  - Solve it both recursively and iteratively.

REFERNECE:
  - https://leetcode.com/problems/symmetric-tree/ (Easy)

"""

from typing import List
from shared_utils import TreeNode, make_tree


class Solution:

    def isSymmetric_v1(self, root: TreeNode) -> bool:
        """Iterative bread-first search."""
        if not root:
            return True
        queue = [root]
        while queue:
            # Process one layer at a time
            num_nodes = len(queue)
            vals = []
            for i in range(num_nodes):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    vals.append(node.left.val)
                else:
                    vals.append(None)
                if node.right:
                    queue.append(node.right)
                    vals.append(node.right.val)
                else:
                    vals.append(None)

            # Check if the next layer is symmetric
            i0, i1 = 0, len(vals) - 1
            while i0 < i1:
                if vals[i0] != vals[i1]:
                    return False
                i0 += 1
                i1 -= 1

        return True

    def isSymmetric_v2(self, root: TreeNode) -> bool:
        """Bread-first search with recurssion."""

        def bfs(nodes: List[TreeNode]) -> bool:
            """Check one layer at a time."""
            # Termination condition
            if not nodes:
                return True

            # Check if this layer is symmetric.  Node can be None.
            i0, i1 = 0, len(nodes) - 1
            while i0 < i1:
                n1 = nodes[i0]
                n2 = nodes[i1]
                v1 = n1.val if n1 else None
                v2 = n2.val if n2 else None
                if v1 != v2:
                    return False
                i0 += 1
                i1 -= 1

            # Build the next layer
            next_layer = []
            for node in nodes:
                if node:
                    next_layer.append(node.left)
                    next_layer.append(node.right)

            return bfs(next_layer)

        return bfs([root])


# ---------------------------
#   Main & Helper Functions
# ---------------------------
def main():
    """Main function"""

    # Test data
    test_data = [
        [1,2,2,3,4,4,3],
        [1,2,2,None,3,None,3],
    ]

    sol = Solution()
    for vals in test_data:
        root = make_tree(vals)
        print("# Input: root = {}".format(vals))
        print("  Output v1 = {}".format(sol.isSymmetric_v1(root)))
        print("  Output v2 = {}".format(sol.isSymmetric_v2(root)))


if __name__ == "__main__":
    main()
