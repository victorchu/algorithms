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
    """Create a binary tree from a list of values."""
    def add_children(node, i, vals, n):
        i_left = 2 * i + 1
        i_right = 2 * i + 2

        if (i_left < n) and (vals[i_left] is not None):
            node.left = TreeNode(vals[i_left])
            add_children(node.left, i_left, vals, n)
        if (i_right < n) and (vals[i_right] is not None):
            node.right = TreeNode(vals[i_right])
            add_children(node.right, i_right, vals, n)

    if vals:
        root = TreeNode(vals[0])
        add_children(root, 0, vals, len(vals))
    else:
        root = None
    return root


def tree_to_list(root: TreeNode) -> List:
    """Convert a tree back to a list of values.
       Missing nodes will be filled with None.
       This function is used to check the tree node.
    """
    queue = [[0, root]]  # (index, node)
    vals = list()

    while queue:
        i, node = queue.pop(0)
        # print("[DEBUG] checking i={}, node val={}, left={}, right={}".format(i, node.val, node.left, node.right))
        while len(vals) < i:
            vals.append(None)   # pad missing nodes
        vals.append(node.val)
        if node.left:
            queue.append([2 * i + 1, node.left])
        if node.right:
            queue.append([2 * i + 2, node.right])

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
