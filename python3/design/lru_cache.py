#!/usr/bin/env python3
"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

  get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
      otherwise return -1.

  put(key, value) - Set or insert the value if the key is not already present.  When the cache
      reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
  - Could you do both operations in O(1) time complexity?

EXAMPLES:

  cache = LRUCache(2)
  cache.put(1, 1)
  cache.put(2, 2)
  cache.get(1)       # returns 1
  cache.put(3, 3)    # evicts key 2
  cache.get(2)       # returns -1 (not found)
  cache.put(4, 4)    # evicts key 1
  cache.get(1)       # returns -1 (not found)
  cache.get(3)       # returns 3
  cache.get(4)       # returns 4

  cache = LRUCache(2)
  cache.get(2)       # returns -1
  cache.put(2, 6)
  cache.get(1)       # returns -1
  cache.put(1, 5)
  cache.put(1, 2)    # replace 5 with 2
  cache.get(1)       # returns 2
  cache.get(2)       # returns 6


TECHNOLOGIES:
  - double-linked list
  - collections.OrderedDcit

REFERENCE:
  - https://leetcode.com/problems/lru-cache/ (Medium)

"""


class DNode:
    """Define a double-linked list node"""

    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return "({})".format(self.val)


class DList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def dump(self, reverse=True):
        vals = []
        p = self.head
        while p:
            vals.append(str(p))
            p = p.next

        if not vals:
            vals.append('None')
        print("[HEAD] {} (size={})".format(" <-> ".join(vals), self.size))

        if reverse:
            vals = []
            p = self.tail
            while p:
                vals.append(str(p))
                p = p.prev
            if not vals:
                vals.append('None')
            print("[TAIL] {}".format(" <-> ".join(vals)))

    def insert(self, val):
        """Insert a node to the front."""
        node = DNode(val)
        # Link with the current head
        if self.head:
            node.next = self.head
            self.head.prev = node
        # Assign the node as the new head
        self.head = node

        # Handle tail
        if not self.tail:
            self.tail = node

        self.size += 1

    def move_to_head(self, node):
        """Move the specified node to head.
        Assumes that the specified node is part of the DList.
        """
        # Special case: no action
        if self.head == node or not self.head:
            return

        # Remove the node from the current position
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # Adjust the tail
        if self.tail == node:
            self.tail = node.prev

        # Insert this node to the front
        self.head.prev = node
        node.next = self.head
        self.head = node
        node.prev = None

    def pop(self):
        """Remove the tail node."""
        if not self.tail:
            return

        # Handle tail
        node = self.tail
        if node.prev:
            node.prev.next = None
        self.tail = node.prev

        # Handle head
        if self.head == node:
            self.head = None

        self.size -= 1

    @staticmethod
    def test():
        """Unit test"""
        dl = DList()
        dl.dump()
        dl.insert(1, 1)
        dl.dump()
        dl.insert(2, 2)
        dl.dump()
        dl.move_to_head(dl.tail)
        dl.dump()
        dl.pop()
        dl.dump()


class LRUCache_v1:
    """Use a custom implementation of DList."""

    def __init__(self, capacity: int):
        self.dlist = DList()
        self.map = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """Get the value corresponding to the specified key.

        Get the value (will always be positive) of the key if the key exists
        in the cache, otherwise return -1.
        """
        if key in self.map:
            node = self.map[key]
            val = node.val[1]
            self.dlist.move_to_head(node)
        else:
            val = -1

        return val

    def put(self, key: int, value: int) -> None:
        """Add a (key, value) pair to the cache.

        Set or insert the value if the key is not already present.  When the cache
        reached its capacity, it should invalidate the least recently used item
        before inserting a new item.

        Note that the same key put be put multiple times with different values.
        The later value shall replace the previous one.
        """
        # Check if the key exist
        if key in self.map:
            node = self.map[key]
            node.val[1] = value
            self.dlist.move_to_head(node)

        else:
            # Drop the least recently used
            if len(self.map) >= self.capacity:
                del self.map[self.dlist.tail.val[0]]
                self.dlist.pop()

            # Insert a new node.
            # Note that we store (key, value) into the value part of the node.
            # The key will be needed when we exceed the capacity.
            self.dlist.insert([key, value])
            self.map[key] = self.dlist.head


class LRUCache_v2:
    """Use the OrderedDict module from collections."""

    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            val = self.cache[key]
            del self.cache[key]
            self.cache[key] = val
            return val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)  # FIFO order
            self.cache[key] = value
        else:
            # Delete and then reinsert into the cache
            del self.cache[key]
            self.cache[key] = value


def lru_driver(cmds, args, ver='v1'):
    obj = None
    for cmd, arg in zip(cmds, args):
        #print("[DEBUG] processing cmd = {}, arg = {}".format(cmd, arg))
        if cmd == 'LRUCache':
            print("LRUCache_{}({})".format(ver, *arg))
            if ver == 'v1':
                obj = LRUCache_v1(*arg)
            elif ver == 'v2':
                obj = LRUCache_v2(*arg)
        elif cmd == 'put':
            print(" - put({})".format(arg))
            obj.put(*arg)
        elif cmd == 'get':
            val = obj.get(*arg)
            print(" - get({}) = {}".format(arg, val))


def main():
    # DList.test()

    test_data = [
        [["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]],
        # expected: [null,null,null,1,null,-1,null,-1,3,4]

        [["LRUCache", "get", "put", "get", "put", "put", "get", "get"],
            [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]]
        # expected: [null, -1, null, -1, null, null, 2, 6]
    ]

    for cmds, args in test_data:
        lru_driver(cmds, args, "v1")
        lru_driver(cmds, args, "v2")


if __name__ == "__main__":
    main()
