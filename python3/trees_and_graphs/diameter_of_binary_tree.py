#!/usr/bin/env python3
"""
Given a binary tree, you need to compute the length of the diameter of the tree. 

The diameter of a binary tree (sometimes called the width) is the length
(number of edges) of the longest path between any two end nodes.
A path with 4 nodes will have a length of 3.
This path may or may not pass through the root.
It is also possible to have multple paths with the same length.

EXAMPLES:

             [1]
            /   \
         [2]     [3]
         / \
       [4] [5]

  Input: [1, 2, 3, 4, 5]
  Output: 3, which is the length of the path [4,2,1,3] or [5,2,1,3]

                [6]
                /
             [1]
            /   \
         [2]     [3]
         / \       \
       [4] [5]      [7]

  Input: [6, 1, None, 2, 3, 4, 5, None, 7]
  Output: 4, which is the length of the path [4,2,1,3,7] or [5,2,1,3,7]

             [3]
                \
                 [2]
                /   \
              [1]   [4]

  Input: [3, None, 2, 1, 4],
  Output: 2

REFERNECE:
  - https://leetcode.com/problems/diameter-of-binary-tree/ (Easy)
  - https://www.geeksforgeeks.org/diameter-of-a-binary-tree/

"""

from typing import List
from shared_utils import TreeNode, make_tree, tree_to_list


class Solution:

    def diameterOfBinaryTree_v1(self, root: TreeNode) -> List[str]:
        """Depth first search with bookkeeping on vertical and horizontal lengths."""

        def search_longest_path(node):
            """Return maximum vertical lengths and horizontal lengths in number of nodes."""
            if not node:
                return 0, 0

            # Search left and right
            left_v, left_h = search_longest_path(node.left)
            right_v, right_h = search_longest_path(node.right)

            # Combine results
            max_v = 1 + max(left_v, right_v)
            max_h = max(left_h, right_h, 1 + left_v + right_v)

            return max_v, max_h

        if not root:
            return 0

        # Combine final results
        max_v, max_h = search_longest_path(root)
        max_nodes = max(max_v, max_h)
        diameter = max_nodes - 1

        return diameter


def main():
    """Main function"""

    # Test data
    test_data = [
        [1, 2, 3, 4, 5],
        [6, 1, None, 2, 3, 4, 5, None, 7],
        [3, None, 2, 1, 4],
    ]

    sol = Solution()
    for vals in test_data:
        root = make_tree(vals)
        print("\n# Input: {}".format(vals))
        print("=> Output v1 = {}".format(sol.diameterOfBinaryTree_v1(root)))


if __name__ == "__main__":
    main()
