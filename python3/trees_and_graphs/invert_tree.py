#!/usr/bin/env python3
"""
Invert a binary tree

EXAMPLES:

  Input: root = [4,2,7,1,3,6,9]

             [4]
            /   \
         [2]     [7]
         / \     / \
       [1] [3] [6] [9]

  Output = [4,7,2,9,6,3,1]

             [4]
            /   \
         [7]     [2]
         / \     / \
       [9] [6] [3] [1]

TRIVIA:

  - This problem was inspired by [this original tweet](https://twitter.com/mxcl/status/608682016205344768)
    by Max Howell:
    
      Google: 90% of our engineers use the software you wrote (Homebrew),
      but you can’t invert a binary tree on a whiteboard so f*** off.

REFERNECE:
  - https://leetcode.com/problems/invert-binary-tree/ (Easy)

"""

from typing import List
from shared_utils import TreeNode, make_tree, tree_to_list


class Solution:

    def invertTree_v1(self, root: TreeNode) -> TreeNode:
        """Invert in place ."""
        def invert(node):
            node.left, node.right = node.right, node.left
            if node.left:
                invert(node.left)
            if node.right:
                invert(node.right)

        invert(root)
        return root

    def invertTree_v2(self, root: TreeNode) -> TreeNode:
        """Clone and invert."""
        def invert(node) -> TreeNode:
            node_copy = TreeNode(node.val)
            if node.left:
                node_copy.right = invert(node.left)
            if node.right:
                node_copy.left = invert(node.right)
            return node_copy

        return invert(root)


# ---------------------------
#   Main & Helper Functions
# ---------------------------
def main():
    """Main function"""

    # Test data
    test_data = [
        [4, 2, 7, 1, 3, 6, 9],
    ]

    sol = Solution()
    for vals in test_data:
        print("# Input: root = {}".format(vals))

        root = make_tree(vals)
        output_v1 = sol.invertTree_v1(root)
        print("  Output v1 = {} (orig = {})".format(
            tree_to_list(output_v1), tree_to_list(root)))

        root = make_tree(vals)
        output_v2 = sol.invertTree_v2(root)
        print("  Output v2 = {} (orig = {})".format(
            tree_to_list(output_v2), tree_to_list(root)))


if __name__ == "__main__":
    main()
