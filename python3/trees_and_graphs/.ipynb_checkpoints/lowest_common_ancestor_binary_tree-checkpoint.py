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
        """Find the ancestor path. Each ancestor has two matches in its subtree.
        Complexity: O(n)
        """
        def dfs(node, targets, path) -> int:
            """Returns number of matches under the node and update the ancester path.
            """
            if not node:
                return 0
            path.append(node)
            v = 1 if node in targets else 0
            v += dfs(node.left, targets, path)
            if v != 2:
                v += dfs(node.right, targets, path)
            if v != 2:
                path.pop()
            return v
        
        path = []  # ancestor path
        dfs(root, {p, q}, path)
        # print(f"[DEBUG] path to LCA = {[x.val for x in path]}")
        return path[-1] if path else None


# ---------------------------
#   Main & Helper Functions
# ---------------------------
def main():
    """Main function"""
    test_data = [
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3],
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 6, 4, 5],
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5],
        [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 9, None],
    ]

    sol = Solution()
    methods = [sol.lowestCommonAncestor_v1, sol.lowestCommonAncestor_v2]
    for vals, p_val, q_val, ans in test_data:
        root = make_tree(vals)
        p = find_node(root, p_val)
        q = find_node(root, q_val)

        print("# Input: root = {}, p = {}, q = {} (ans = {})".format(vals, p_val, q_val, ans))
        for i, f in enumerate(methods, start=1):
            lca = f(root, p, q)
            status = 'PASS' if lca==ans or (lca and lca.val==ans) else 'ERROR'
            print(f"  - Output {i} = {lca.val if lca else None} --- {status}")


if __name__ == "__main__":
    main()
