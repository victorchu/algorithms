"""
Shared utililities for Linked Lists.
"""
from __future__ import annotations
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other: ListNode):
        return (self.val < other.val)

    def __le__(self, other: ListNode):
        return(self.val <= other.val)
    

def lnode2str(p: ListNode) -> str:
    """Convert a ListNode to a string."""
    x = list()
    while (p):
        x.append(str(p.val))
        p = p.next
    return "({})".format(", ".join(x))


def make_linked_list(vals):
    p = prehead = ListNode()
    for v in vals:
        p.next = ListNode(v)
        p = p.next
    return prehead.next


def make_linked_lists(lists):
    return [make_linked_list(vals) for vals in lists]


