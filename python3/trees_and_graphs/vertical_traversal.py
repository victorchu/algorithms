#!/usr/bin/env python3
"""
Given a binary tree, return the vertical order traversal of its nodes' values.
(ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

EXAMPLES:

             [3]
            /   \
         [2]    [6]
        /   \   /  \
      [1]   [4][5]  [7]

  Input: [3, 2, 6, 1, 4, 5, 7]
  Output: [[1], [2], [3, 4, 5], [6], [7]]

             [3]
            /   \
         [2]    [6]
                /  \
              [5]   [7]

  Input: [3, 2, 6, None, None, 5, 7]
  Output: [[2], [3, 5], [6], [7]]

NOTE:
  - Each left link shifts the vertical position one step to the left.
  - Each right link shifts the vertical position one step to the right.

TECHNIQUES:
  - Breadth-first traversal.

REFERNECE:
  - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/ (Medium)
  - https://www.geeksforgeeks.org/print-binary-tree-vertical-order/
  - https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/

"""

from typing import List
from shared_utils import TreeNode, make_tree, tree_to_list
from collections import defaultdict


class Solution:

    def verticalOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return list()

        v_map = defaultdict(list)
        queue = [[root, 0]]
        while queue:
            node, pos = queue.pop(0)
            v_map[pos].append(node.val)
            if node.left:
                queue.append([node.left, pos-1])
            if node.right:
                queue.append([node.right, pos+1])

        results = [v_map[i] for i in sorted(v_map.keys())]
        return results


# ---------------------------
#   Main & Helper Functions
# ---------------------------
def main():

    test_data = [
        [3, 2, 6, 1, 4, 5, 7],
        [3, 2, 6, None, None, 5, 7],
    ]

    sol = Solution()
    for vals in test_data:
        root = make_tree(vals)
        print("\n# Input: {}".format(vals))
        print("=> Output v1 = {}".format(sol.verticalOrder(root)))


if __name__ == "__main__":
    main()
