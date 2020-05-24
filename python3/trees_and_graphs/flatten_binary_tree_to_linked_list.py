#!/usr/bin/env python3
"""
Given a binary tree, flatten it to a linked list in-place.

EXAMPLE:

         [1] 
        /    \ 
      [2]    [5]
     /   \      \
   [3]   [4]    [6]

  Output: [1] -- [2] -- [3] -- [4] -- [5] -- [6] -- None
          /     /      /      /      /      /
        None  None   None   None   None   None

  Use the in-order traversal.
  Change all of the left links to None.

TECHNIQUE:
  - stack

"""

from typing import List
from shared_utils import TreeNode, make_tree, right_list


class Solution:

    def flatten_v1(self, root: TreeNode) -> None:
        """An in-order approach."""

        def flatten_helper(node: TreeNode) -> None:
            left = node.left
            right = node.right
            if left:
                flatten_helper(left)
                # Move the flattened left to the right
                node.left = None
                node.right = left
            if right:
                flatten_helper(right)
                # Append to the end of the new right branch
                if left:
                    n = node.right
                    while n:
                        if n.right is None:
                            n.right = right
                            break
                        n = n.right
        if root:
            flatten_helper(root)

    def flatten_v2(self, root: TreeNode) -> None:
        """Use a stack to change the priority of the links."""
        if not root:
            return

        stack = [root]
        while stack:
            curr = stack.pop()

            # Push both children to the stack.
            # The right goes before the left, since we want to deal with the left first.
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

            # Link back from the top of the stack
            if stack:
                curr.right = stack[-1]
                curr.left = None


# ---------------------------
#   Main & Helper Functions
# ---------------------------
def main():
    """Main function"""

    # Test data
    test_data = [
        [1, 2, 5, 3, 4, None, 6]
    ]

    sol = Solution()
    for vals in test_data:
        print("# Input = {}".format(vals))
        root = make_tree(vals)
        sol.flatten_v1(root)
        print("  Output v1 = {}".format(right_list(root)))

        root = make_tree(vals)
        sol.flatten_v2(root)
        print("  Output v2 = {}".format(right_list(root)))


if __name__ == "__main__":
    main()
