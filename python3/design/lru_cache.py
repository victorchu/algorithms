#!/usr/bin/env python3
"""
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

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


# ------------------
#  Helper Classes
# ------------------

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

    def dump(self):
        vals = []
        p = self.head
        while p:
            vals.append(str(p))
            p = p.next
        print("[DList] {} (size={})".format(" <-> ".join(vals), self.size))

    def append(self, val):
        """Append a node to the end."""
        node = DNode(val)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1
        return node

    def remove(self, node):
        """Move the specified node to head.
        Assumes that the specified node is part of the DList.
        """
        if not node:
            return

        # Remove the node from the current position
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        self.size -= 1

    def pop(self, last=False):
        """Remove the tail node or the head node."""
        if last:
            self.remove(self.tail)
        else:
            self.remove(self.head)


class MyOrderedDict:
    """My implementation of OrderedDict.
    Use a DList to track the key orders.
    """

    def __init__(self):
        self.dlist = DList()
        self.cache = dict()     # {key: [val, node]}

    def __len__(self):
        return len(self.cache)

    def __contains__(self, key):
        return key in self.cache

    def __getitem__(self, key):
        x = self.cache[key]
        return x[0]

    def __setitem__(self, key, val):
        """This function does not change the order."""
        if key in self.cache:
            x = self.cache[key]
            x[1] = val
        else:
            self.cache[key] = [val, self.dlist.append(key)]

    def __delitem__(self, key):
        if key in self.cache:
            val, node = self.cache[key]
            self.dlist.remove(node)
            del self.cache[key]

    def popitem(self, last=True):
        if last:
            self.__delitem__(self.dlist.tail.val)
        else:
            self.__delitem__(self.dlist.head.val)


# ------------------
#  LRU Caches
# ------------------

class LRUCache_v1:
    """Use DList to track the key order."""

    def __init__(self, capacity: int):
        self.dlist = DList()    # used to track key orders
        self.cache = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """Get the value corresponding to the specified key.
        Refresh the key order.
        """
        if key in self.cache:
            val, node = self.cache[key]
            self.dlist.remove(node)

            node = self.dlist.append(key)
            self.cache[key] = [val, node]
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
        if key in self.cache:
            _, node = self.cache[key]
            self.dlist.remove(node)
            self.cache[key] = [value, self.dlist.append(value)]
        else:
            if len(self.cache) >= self.capacity:
                oldest_key = self.dlist.head.val
                del self.cache[oldest_key]
                self.dlist.pop(last=False)
            self.cache[key] = [value, self.dlist.append(key)]


class LRUCache_v2:
    """Use OrderedDict from collections."""

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


class LRUCache_v3:
    """Use MyOrderedDict."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = MyOrderedDict()

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


def dlist_test():
    print("# DList Test")
    dl = DList()
    dl.dump()
    dl.append([1, 1])
    dl.append([2, 2])
    dl.append([3, 3])
    dl.dump()
    dl.pop(last=True)
    dl.dump()
    dl.pop(last=False)
    dl.dump()
    print()


def lru_driver(cmds, args, ver='v1'):
    obj = None
    for cmd, arg in zip(cmds, args):
        #print("[DEBUG] processing cmd = {}, arg = {}".format(cmd, arg))
        if cmd == 'LRUCache':
            print("# LRUCache_{}({})".format(ver, *arg))
            if ver == 'v1':
                obj = LRUCache_v1(*arg)
            elif ver == 'v2':
                obj = LRUCache_v2(*arg)
            elif ver == 'v3':
                obj = LRUCache_v3(*arg)

        elif cmd == 'put':
            print(" - put({})".format(arg))
            obj.put(*arg)

        elif cmd == 'get':
            val = obj.get(*arg)
            print(" - get({}) = {}".format(arg, val))

    print()


def lru_test():
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
        lru_driver(cmds, args, "v3")


def main():
    dlist_test()
    lru_test()


if __name__ == "__main__":
    main()
