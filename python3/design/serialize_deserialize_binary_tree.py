#!/usr/bin/env python3
"""
Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work. You
just need to ensure that a binary tree can be serialized to a string and this
string can be deserialized to the original tree structure.

EXAMPLES:

                           [1]
                         /     \
                     [2]         [3]
                     / \        /   \
                [None] [None] [4]   [5]

            data = [1, 2, 3, None, None, 4, 5],


                          [1]
                        /     \
                     [3]     [None]
                    /   \ 
                [None]  [4]

            data = [1, 3, None, None, 4],


                         [3]
                        /   \
                   [None]    [2]
                            /   \
                          [1]   [4]

            data = [3, None, 2, 1, 4],

REFERENCE:
  - https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

"""


class TreeNode:
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def __init__(self):
        pass

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        queue = [root] 
        data = list()
        while queue:
            tmp_queue = list()
            for node in queue:
                if not node:
                    data.append(None)
                    continue

                data.append(node.val)
                tmp_queue.append(node.left)
                tmp_queue.append(node.right)

            if any(tmp_queue):
                queue = tmp_queue
            else:
                break

        # Remove trailing None
        while data and data[-1] == None:
            data.pop()
        return data

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        if not data or data[0] is None:
            return None

        root = TreeNode(data[0])
        queue = [root]

        n = len(data)
        k = 1
        while queue and k < n:
            node = queue.pop(0)
            # Left
            if k < n:
                if data[k] is not None:
                    node.left = TreeNode(data[k])
                    queue.append(node.left)
                k += 1
            # Right
            if k < n:
                if data[k] is not None:
                    node.right = TreeNode(data[k])
                    queue.append(node.right)
                k += 1
        return root
        

def main():
    test_data = [
        [3, None, 2, 1, 4],
        [1, 2, 3, None, None, 4, 5],
        [1, 2, 3, None, None, 4, 5, 6, 7],
        [1, 3, None, None, 4],
    ]

    obj = Codec()
    for data in test_data:
        print("# Input  : {}".format(data))
        root = obj.deserialize(data)
        print("  Output : {}".format(obj.serialize(root)))


if __name__ == "__main__":
    main()
