#!/usr/bin/env python3
"""
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

EXAMPLES:

             [1]
            /   \
         [2]     [3]
         /       / \
       [4]     [5] [6]

  Input: root = [1,2,3,4,None,5,6]
  Output: [[1], [2,3], [4,5,6]]

REFERNECE:
  - https://leetcode.com/problems/binary-tree-level-order-traversal/ (Medium)

"""

from typing import List
from shared_utils import TreeNode, make_tree


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        output = []
        while queue:
            num_nodes = len(queue)
            vals = []
            for i in range(num_nodes):
                node = queue.pop(0)
                vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(vals)

        return output


def main():
    """Main function"""

    # Test data
    test_data = [
        [1,2,3,4,None,5,6],
        [3,9,20,None,None,15,7],
    ]

    sol = Solution()
    for vals in test_data:
        root = make_tree(vals)
        print("# Input: root = {}".format(vals))
        print("  Output v1 = {}".format(sol.levelOrder(root)))


if __name__ == "__main__":
    main()
