#!/usr/bin/env python3
"""
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.


TECHNIQUES:
  - 

REFERENCE:
  - https://www.geeksforgeeks.org/clone-an-undirected-graph/
  - https://leetcode.com/problems/clone-graph/ (Medium)
 
"""

from typing import List


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def cloneGraph_v1(self, node: Node) -> Node:
        """Use a queue."""
        if not node:
            return None

        node_map = dict()  # value to new node map
        queue = [node]
        # track node values that have been added to the queue
        in_queue = set([node.val])
        clone_head = None

        while queue:
            curr = queue.pop(0)
            val = curr.val

            # Get the clone of this node
            if val not in node_map:
                node_map[val] = curr_clone = Node(val)
                if clone_head is None:
                    clone_head = curr_clone
            else:
                curr_clone = node_map[val]

            # Handle neighbors
            for nbr_node in curr.neighbors:
                val = nbr_node.val
                # Clone  the neighbor node
                if val not in node_map:
                    node_map[val] = nbr_clone = Node(val)
                else:
                    nbr_clone = node_map[val]

                curr_clone.neighbors.append(nbr_clone)

                # Add the neighbor node to the queue
                if val not in in_queue:
                    queue.append(nbr_node)
                    in_queue.add(val)

        return clone_head

    def cloneGraph_v2(self, node: Node) -> Node:
        """Use recurssion."""
        if not node:
            return None

        node_map = dict()

        def clone_node(src_node):
            if src_node in node_map:
                return node_map[src_node]

            node_map[src_node] = new_node = Node(src_node.val)

            for nbr_node in src_node.neighbors:
                new_node.neighbors.append(clone_node(nbr_node))

            return new_node

        return clone_node(node)


# --------------
#  Utilities
# --------------
def make_graph(adj_list):
    """Create a Graph from the adjacent lists.
       The node values is index + 1."""
    node_map = dict()
    head = None

    # Create nodes
    for v in range(1, len(adj_list)+1):
        node = Node(v)
        node_map[v] = node
        if not head:
            head = node

    # Connect with neighbors
    for i, neighbors in enumerate(adj_list):
        v = i + 1
        node = node_map[v]
        for x in neighbors:
            if not x in node_map:
                raise Exception("Invalid node value: {}".format(x))
            node.neighbors.append(node_map[x])

    return head


def graph_to_list(head):
    """Convert a graph back to an adj_list."""
    adj_map = dict()
    queue = [head]
    while queue:
        node = queue.pop(0)
        if node.val in adj_map:
            continue
        adj_vals = list()
        for x in node.neighbors:
            adj_vals.append(x.val)
            if x.val not in adj_map:
                queue.append(x)
        adj_map[node.val] = adj_vals

    ret_list = list()

    for i, v in enumerate(sorted(adj_map.keys())):
        if v != i + 1:
            raise Exception("Missing node value: {}".format(i + 1))
        ret_list.append(adj_map[v])

    return ret_list


def main():
    test_data = [
        [[2, 4], [1, 3], [2, 4], [1, 3]]
    ]

    sol = Solution()
    for adj_list in test_data:
        print("# Input = {}".format(adj_list))
        node = make_graph(adj_list)
        print("  Clone v1 = {}".format(graph_to_list(sol.cloneGraph_v1(node))))
        print("  Clone v2 = {}".format(graph_to_list(sol.cloneGraph_v2(node))))


if __name__ == "__main__":
    main()
