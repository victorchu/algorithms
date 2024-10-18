#!/usr/bin/env python3
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

EXAMPLES:

         [2]
        /   \ 
      [1]   [3]
  
  Input: [2, 1, 3]
  Output: True
  -------------------

         [5] 
        /   \ 
      [1]   [4]
           /   \ 
         [3]   [6]

  Input: [5, 1, 4, None, None, 3, 6]
  Output: False
  -------------------

         [1] 
        / 
      [1]

  Input: [1, 1]
  Output: False; duplicated values are not allowed in this problem.

TECHNIQUES:
  - Track the valid range for each node.
  - Use float('inf') and float('-inf') to get infinity.  Alternatively, use math.inf

REFERNECE:
  - https://leetcode.com/problems/validate-binary-search-tree/ (Medium)

"""

from typing import List
from shared_utils import TreeNode, make_tree, tree_to_list


class Solution:

    def isValidBST_v1(self, root: TreeNode) -> bool:
        """A depth-first approach.  Return bounds from the helper function."""

        def validate_node(node: TreeNode) -> bool:
            val = node.val
            lb, ub = val, val
            status = True

            if node.left:
                lstatus, llb, lub = validate_node(node.left)
                if lstatus and lub < val:
                    lb = llb
                else:
                    return False, lb, ub

            if node.right:
                rstatus, rlb, rub = validate_node(node.right)
                if rstatus and rlb > val:
                    ub = rub
                else:
                    return False, lb, ub

            return status, lb, ub

        if not root:
            return True

        status, _, _ = validate_node(root)
        return status

    def isValidBST_v2(self, root: TreeNode) -> bool:
        """A depth-first approach. Pass bounds to the helper function."""

        def validate_node(node: TreeNode, lb: float, ub: float) -> bool:
            val = node.val
            if val <= lb or val >= ub:
                return False

            is_valid = True
            if node.left:
                is_valid = validate_node(node.left, lb, val)
            if is_valid and node.right:
                is_valid = validate_node(node.right, val, ub)
            return is_valid

        if not root:
            return True

        return validate_node(root, float('-inf'), float('inf'))

    def isValidBST_v3(self, root: TreeNode) -> bool:
        """A breadth-first approach."""

        if not root:
            return True

        # Put [node, lower bound, upper bound] into the queue
        queue = [[root, float('-inf'), float('inf')]]
        is_valid = True

        while queue:
            node, lb, ub = queue.pop(0)
            val = node.val
            if (val <= lb) or (val >= ub):
                is_valid = False
                break
            if node.left:
                queue.append([node.left, lb, val])
            if node.right:
                queue.append([node.right, val, ub])
        return is_valid


# ---------------------------
#   Main & Helper Functions
# ---------------------------
def main():
    """Main function"""

    # Test data
    test_data = [
        [2, 1, 3],
        [5, 1, 4, None, None, 3, 6],
        [1, 1]
    ]

    sol = Solution()
    for vals in test_data:
        print("# Input = {}".format(vals))
        root = make_tree(vals)
        print("  Output v1 = {}".format(sol.isValidBST_v1(root)))
        print("  Output v2 = {}".format(sol.isValidBST_v2(root)))
        print("  Output v3 = {}".format(sol.isValidBST_v3(root)))


if __name__ == "__main__":
    main()
