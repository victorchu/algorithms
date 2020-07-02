#!/usr/bin/env python3
"""
Given a binary tree, return the zigzag (spiral) level order traversal of its nodes' values
(ie, from left to right, then right to left for the next level and alternate between).

EXAMPLES:

             [1]
            /   \
         [2]     [3]
         /       / \
       [4]     [5] [6]

  Input: root = [1,2,3,4,None,5,6]
  Output: [[1], [3,2], [4,5,6]]

REFERNECE:
  - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/ (Medium)

"""

from typing import List
from shared_utils import TreeNode, make_tree


class Solution:

    def zigzagLevelOrder_v1(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        output = []
        level = 1
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

            if level % 2 == 0:
                output.append(list(reversed(vals)))
            else:
                output.append(vals)
            level += 1

        return output

    def zigzagLevelOrder_v2(self, root: TreeNode) -> List[List[int]]:
        """Use recursion."""

        def zot(nodes, level, output):
            if not nodes:
                return
            vals = []
            next_queue = []
            for node in nodes:
                vals.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            if level % 2 == 0:
                vals.reverse()
            output.append(vals)
            zot(next_queue, level + 1, output)

        output = []
        zot([root], 1, output)
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
        print("  Output v1 = {}".format(sol.zigzagLevelOrder_v1(root)))
        print("  Output v2 = {}".format(sol.zigzagLevelOrder_v2(root)))


if __name__ == "__main__":
    main()
