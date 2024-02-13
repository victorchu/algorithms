#!/usr/bin/env python3
"""
Given a binary tree, return all root-to-leaf paths.

EXAMPLES:

             [1]
            /   \
         [2]     [3]
           \
           [5]

  Input: root = [1, 2, 3, None, 5]
  Output: ["1->2->5", "1->3"]

TECHNIQUES:
  - Basic tree traversal plus information collection.

REFERNECE:
  - https://leetcode.com/problems/binary-tree-paths/ (Easy)
  - https://www.geeksforgeeks.org/given-a-binary-tree-print-all-root-to-leaf-paths/

"""

from typing import List
from shared_utils import TreeNode, make_tree


class Solution:

    def binaryTreePaths_v1(self, root: TreeNode) -> List[str]:
        """Find all paths from root to leaves"""
        def get_paths(node, path) -> List[str]:
            if node is None:
                return []

            # Update the path
            if path:
                path += "->" + str(node.val)
            else:
                path = str(node.val)

            # Explore left and right branch
            if node.left or node.right:
                left_paths = get_paths(node.left, path)
                right_paths = get_paths(node.right, path)
                return left_paths + right_paths
            else:
                return [path]

        return get_paths(root, '')

    def binaryTreePaths_v2(self, root: TreeNode) -> List[str]:
        """Re-use a single list.  This greatly improves the performance."""
        def get_paths(node, path, paths):
            if node is None:
                return

            # Update the path
            if path:
                path += "->" + str(node.val)
            else:
                path = str(node.val)

            if not node.left and not node.right:
                paths.append(path)
            else:
                get_paths(node.left, path, paths)
                get_paths(node.right, path, paths)

        paths = list()
        get_paths(root, '', paths)
        return paths


# ---------------------------
#   Main & Helper Functions
# ---------------------------
def main():
    """Main function"""

    # Test data
    test_data = [
        [1, 2, 3, None, 5],
    ]

    sol = Solution()
    for vals in test_data:
        root = make_tree(vals)
        print("# Input: {}".format(vals))
        print("  Output v1 = {}".format(sol.binaryTreePaths_v1(root)))
        print("  Output v2 = {}".format(sol.binaryTreePaths_v2(root)))


if __name__ == "__main__":
    main()
