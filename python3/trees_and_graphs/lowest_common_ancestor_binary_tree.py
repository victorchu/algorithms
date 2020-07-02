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

        Need to traverse the tree twice.
        Complexity: O(n) x 2
        """
        def find_path(node: TreeNode, target: TreeNode, path: List[TreeNode]) -> bool:
            """Find the path to the specified node."""
            if not node:
                return False

            path.append(node)
            if node == target:
                return True

            if find_path(node.left, target, path) or find_path(node.right, target, path):
                return True

            # remove the node from the path.
            path.pop()
            return False

        if not root:
            return None

        path_p = list()
        path_q = list()
        lca = None
        if find_path(root, p, path_p) and find_path(root, q, path_q):
            for a, b in zip(path_p, path_q):
                if a != b:
                    break
                lca = a
        return lca

    def lowestCommonAncestor_v2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """Use one traversal of binary tree to search for both nodes.

        Warning: this method assumes both p & q exist in the tree.
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

    def lowestCommonAncestor_v3(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """A variation of v2.

        This algorithm also makes one traversal.  The helper function returns a tuple:
          - number of node found.
          - known LCA.

        v2 is quicker, since it stops on finding any of the target node.
        v3, however, is thourough.  It traverse the whole tree and make sure that
        both target nodes are found.

        Complexity: O(n)
        """
        def findLCA(node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            if node == None:
                return (0, None)

            # Search both branches
            ln, llca = findLCA(node.left, p, q)
            rn, rlca = findLCA(node.right, p, q)
            n, lca = 0, None

            if llca:
                return ln, llca
            elif rlca:
                return rn, rlca
            else:
                n = ln + rn
                if node == p or node == q:
                    n += 1
                if n == 2:
                    lca = node

            return n, lca

        _, lca = findLCA(root, p, q)
        return lca


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
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 9, None],
    ]

    sol = Solution()
    for vals, p_val, q_val, ans in test_data:
        root = make_tree(vals)
        p = find_node(root, p_val)
        q = find_node(root, q_val)

        print("# Input: root = {}, p = {}, q = {} (ans = {})".format(vals, p_val, q_val, ans))
        lca = sol.lowestCommonAncestor_v1(root, p, q)
        print("  Output v1 = {})".format(lca.val if lca else "None"))
        lca = sol.lowestCommonAncestor_v2(root, p, q)
        print("  Output v2 = {})".format(lca.val if lca else "None"))
        lca = sol.lowestCommonAncestor_v3(root, p, q)
        print("  Output v3 = {})".format(lca.val if lca else "None"))


if __name__ == "__main__":
    main()
