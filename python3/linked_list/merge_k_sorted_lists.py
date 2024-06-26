#!/usr/bin/env python3
"""
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.

Example:

  Input: [(1,4,5), (1,3,4), (2,6)]
  Output: [1,1,2,3,4,4,5,6]

Ref:
  - https://leetcode.com/problems/merge-k-sorted-lists/ (Hard)

"""
import heapq
from queue import PriorityQueue
from typing import List
from linked_list_utils import *


class Solution:

    def mergeKLists_v1(self, lists: List[ListNode]) -> ListNode:
        """Merge two linked-lists at a time -- Divide and conquer.

        LeetCode: runtime 144 ms > 40.27%; mem 17.7 MB < 42.99%
        """
        def merge_two_lists(p:ListNode, q:ListNode) -> ListNode:
            r = prehead = ListNode()
            while p or q:
                if p and q:
                    if p.val < q.val:
                        r.next = p
                        p = p.next
                    else:
                        r.next = q
                        q = q.next
                elif p:
                    r.next = p
                    p = p.next
                else:
                    r.next = q
                    q = q.next
                r = r.next
            return prehead.next

        if not lists:
            return None

        queue = lists[:]   # prefer to call it a queue
        while len(queue) > 1:
            p = queue.pop(0)
            q = queue.pop(0)
            r = merge_two_lists(p, q)
            queue.append(r)

        return queue[0]

    def mergeKLists_v2(self, lists: List[ListNode]) -> ListNode:
        """Use a heap to store lists (not nodes).
        One possible benefit is that the heap remains small, thus could be
        more efficient.
        """
        class NodeObj:
            """A wrapper that has comparison functions defined."""
            def __init__(self, node): 
                self.head = node
                
            def __eq__(self, other):
                return self.head.val == other.head.val
            
            def __lt__(self, other):
                return self.head.val < other.head.val

        if not lists: return None

        heap = [NodeObj(node) for node in lists if node]
        heapq.heapify(heap)
        head = p = None
        while heap:
            obj = heapq.heappop(heap)
            # Build the new list
            if not head:
                head = obj.head
                p = head
            else:
                p.next = obj.head
                p = p.next
            
            # Modify the existing list and push back to the heap
            obj.head = obj.head.next
            if obj.head:
                heapq.heappush(heap, obj)
        return head
    
    def mergeKLists_v3(self, lists: List[ListNode]) -> ListNode:
        # Store all nodes into a min heap
        h = []
        i = 0
        for p in lists:
            while p:
                heapq.heappush(h, (p.val, i, p))
                p = p.next
                i += 1

        # Popup one by one
        head, p = None, None
        while h:
            v = heapq.heappop(h)
            if not head:
                head = v[-1]
                p = head
            else:
                p.next = v[-1]
                p = p.next
        return head
    
    def mergeKLists_v4(self, lists: List[ListNode]) -> ListNode:
        """Same as v2, replacing heapq with PriorityQueue."""
        if not lists: return None

        queue = PriorityQueue()
        i = 0
        for node in lists:
            if node:
                queue.put((node.val, i, node))
                i += 1

        r = prehead = ListNode()
        while not queue.empty():
            val, _, node = queue.get()
            r.next = node
            r = r.next
            if node.next:
                node = node.next
                queue.put((node.val, i, node))
                i += 1
        return prehead.next


# ---------------------
#  Utilities and Tests
# ---------------------
def main():
    """Main function"""

    test_data = [
        [(1,4,5), (1,3,4), (2,6)],
        [(1,3),(4,5,6),(8,)],
    ]

    sol = Solution()
    for vals in test_data:
        print("\n# Inputs: {}".format(vals))
        print("  Output v1 = {}".format(lnode2str(sol.mergeKLists_v1(make_linked_lists(vals)))))
        print("  Output v2 = {}".format(lnode2str(sol.mergeKLists_v2(make_linked_lists(vals)))))
        print("  Output v3 = {}".format(lnode2str(sol.mergeKLists_v3(make_linked_lists(vals)))))
        print("  Output v3 = {}".format(lnode2str(sol.mergeKLists_v4(make_linked_lists(vals)))))


if __name__ == "__main__":
    main()
