#!/usr/bin/env python3
"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from
some starting node to any node in the tree along the parent-child
connections. The path must contain at least one node and does not
need to go through the root.

EXAMPLE:

         [1]
        /   \ 
      [2]   [3]

  Input: [1, 2, 3]
  Output: 6

         [-10] 
        /    \ 
      [9]   [20]
           /    \ 
         [15]    [7]

  Input: [-10, 9, 20, None, None, 15, 7]
  Output: 42   # [15]-[20]-[7]

TECHNIQUES:
  - Consider all possible combinations.

REFERENCE:
  - https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/
  - https://leetcode.com/problems/binary-tree-maximum-path-sum/ (Hard)

 
"""

from typing import List
from shared_utils import TreeNode, make_tree, tree_to_list


class Solution:

    def maxPathSum(self, root: TreeNode) -> int:

        def helper(node: TreeNode):
            """A helper function.

            :return: (vmax, hmax), where 
               vmax is the max from a vertical path
               hmax is the max from a horizontal path (including both left & right)
            """
            # Use lists to store all candidate vmax and hmax values
            if node.left or node.right:
                vvals = [node.val]
                hvals = [node.val]

                if node.left:
                    left_vmax, left_hmax = helper(node.left)
                    left_fmax_plus = left_vmax + node.val
                    hvals.append(left_hmax)
                    hvals.append(left_fmax_plus)
                    vvals.append(left_fmax_plus)

                if node.right:
                    right_vmax, right_hmax = helper(node.right)
                    right_vmax_plus = right_vmax + node.val
                    hvals.append(right_hmax)
                    hvals.append(right_vmax_plus)
                    vvals.append(right_vmax_plus)

                if node.left and node.right:
                    hvals.append(node.val + left_vmax + right_vmax)

                vmax = max(vvals)
                hmax = max(hvals)
            else:
                vmax, hmax = node.val, node.val
            return vmax, hmax

        if not root:
            return 0

        vmax, hmax = helper(root)
        return max(vmax, hmax)


def main():
    test_data = [
        [[1, 2, 3], 6],
        [[-10, 9, 20, None, None, 15, 7], 42],
        [[2, -1], 2],
    ]

    sol = Solution()
    for vals, ans in test_data:
        print("# Input = {}".format(vals))
        root = make_tree(vals)
        print("  Output v1 = {}  (expected = {})".format(
            sol.maxPathSum(root), ans))
        #print("  Output v2 = {}".format(sol.isValidBST_v2(root)))


if __name__ == "__main__":
    main()
