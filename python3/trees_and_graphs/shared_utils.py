"""
Shared utililities.
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree(vals: List) -> TreeNode:
    """Create a binary tree from a list of values.

    Examples:

     - vals = [1, 2, 3, 4, 5]

                 [1]
                /   \
             [2]     [3]
             / \
           [4] [5]

    - vals = [3, None, 2, 1, 4]

                 [3]
                /   \
           [None]    [2]
                    /   \
                  [1]   [4]

    """
    if not vals:
        return None

    root = TreeNode(vals[0])
    queue = [root]
    n = len(vals)
    k = 1   # index to the next value in the array
    while queue:
        node = queue.pop(0)
        if k < n:
            if vals[k] is not None:
                node.left = TreeNode(vals[k])
                queue.append(node.left)
            k += 1
        if k < n:
            if vals[k] is not None:
                node.right = TreeNode(vals[k])
                queue.append(node.right)
            k += 1
        else:
            break
    return root


def tree_to_list(root: TreeNode) -> List:
    """Convert a tree back to a list of values.
       This is the reverse of the make_tree function.
    """
    if not root:
        return list()

    queue = [root] 
    vals = list()
    while queue:
        node = queue.pop(0)
        if not node:
            vals.append(None)
            continue
        vals.append(node.val)

        if node.left or node.right:
            queue.append(node.left)
            queue.append(node.right)

    # Remove the None at the tail
    if vals[-1] is None:
        vals.pop()

    return vals


def right_list(root: TreeNode) -> List:
    """Only collect values from the right"""
    vals = list()
    n = root
    while n:
        vals.append(n.val)
        if n.right:
            vals.append(n.left)
        n = n.right
    return vals


def find_node(root: TreeNode, val) -> TreeNode:
    """Find the node with the specified value."""
    result = None
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.val == val:
            result = node
            break
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
