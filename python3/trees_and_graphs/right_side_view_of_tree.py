#!/usr/bin/env python3
"""
Given a binary tree, imagine yourself standing on the right side
of it, return the values of the nodes you can see ordered from top
to bottom.

EXAMPLE:

         [1] 
        /   \ 
      [2]   [3]
        \      \ 
         [5]   [4]

  Input: [1, 2, 3, None, 5, None, 4]
  Output: [1, 3, 4]


TECHNIQUES:

REFERNECE:
  - https://www.geeksforgeeks.org/print-right-view-binary-tree-2/
  - https://leetcode.com/problems/binary-tree-right-side-view/ (Medium)

"""

from typing import List
from shared_utils import TreeNode, make_tree, tree_to_list


class Solution:

    def rightSideView_v1(self, root: TreeNode) -> List[int]:
        """Process nodes layer by layer."""
        if not root:
            return list()

        curr_layer = [root]
        side_view = list()
        while curr_layer:
            # Get last element and add to the side view
            side_view.append(curr_layer[-1].val)

            # Update thew node layer with nodes from the next layer
            next_layer = []
            for n in curr_layer:
                if n.left:
                    next_layer.append(n.left)
                if n.right:
                    next_layer.append(n.right)
            curr_layer = next_layer

        return side_view


# ---------------------------
#   Main & Helper Functions
# ---------------------------
def main():
    """Main function"""

    # Test data
    test_data = [
        [1, 2, 3, None, 5, None, 4],
        [1, 2, 3, None, 5],
    ]

    sol = Solution()
    for vals in test_data:
        print("# Input = {}".format(vals))
        root = make_tree(vals)
        print("  View v1 = {}".format(sol.rightSideView_v1(root)))


if __name__ == "__main__":
    main()
