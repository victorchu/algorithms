#!/usr/bin/env python3
"""

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common
ancestor is defined between two nodes p and q as the lowest node
in T that has both p and q as descendants (where we allow a node
to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


EXAMPLES:

              [3]
             /   \
         [5]      [1]
         / \      / \
       [6] [2]  [0] [8]
           / \ 
         [7] [4] 

  Input: root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 3
  Output: 3

  Input: root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 4
  Output: 5

TECHNIQUES:
  - Depth first search.

REFERNECE:
  - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/ (Medium)
  - https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/

"""

from typing import List
from shared_utils import TreeNode, make_tree, find_node, tree_to_list


class Solution:

    def lowestCommonAncestor_v1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """By finding paths from root to p and from root to q.

        Complexity: O(n)
        """
        def path_vals(path: List[TreeNode]):
            return [x.val for x in path]

        def find_path(node: TreeNode, target: TreeNode, path: List[TreeNode]) -> bool:
            """Find the path to the specified node."""
            path.append(node)
            if node == target:
                return True

            if (node.left and find_path(node.left, target, path)) or \
                    (node.right and find_path(node.right, target, path)):
                return True

            # remote the node from the path.
            path.pop()
            return False

        lca = None
        if root:
            path_p = list()
            path_q = list()
            if find_path(root, p, path_p) and find_path(root, q, path_q):
                for a, b in zip(path_p, path_q):
                    if a != b:
                        break
                    lca = a
        return lca

    def lowestCommonAncestor_v2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """Use one traversal of binary tree to search for both nodes.

        Complexity: O(n)
        """
        def findLCA(node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            if node == None:
                return None
            if node == p or node == q:
                return node

            # Search both branches
            left_lca = findLCA(node.left, p, q)
            right_lca = findLCA(node.right, p, q)

            # If both return valid values, this node is the LCA
            if left_lca and right_lca:
                return node
            # Otherwise, take the lca from one branch.
            elif left_lca:
                return left_lca
            else:
                return right_lca

        return findLCA(root, p, q)


# ---------------------------
#   Main & Helper Functions
# ---------------------------
def main():
    """Main function"""

    # Test data
    test_data = [
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3],
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 6, 4, 5],
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5],
    ]

    sol = Solution()
    for vals, p_val, q_val, ans in test_data:
        root = make_tree(vals)
        p = find_node(root, p_val)
        q = find_node(root, q_val)

        print("# Input: root = {}, p = {}, q = {}".format(vals, p_val, q_val))
        lca = sol.lowestCommonAncestor_v1(root, p, q)
        print("  Output v1 = {}   (ans: {})".format(
            lca.val if lca else "None", ans))
        lca = sol.lowestCommonAncestor_v2(root, p, q)
        print("  Output v2 = {}   (ans: {})".format(
            lca.val if lca else "None", ans))


if __name__ == "__main__":
    main()
