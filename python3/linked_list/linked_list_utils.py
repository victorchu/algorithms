"""
Shared utililities for Linked Lists.
"""
from __future__ import annotations
from typing import List


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other: ListNode):
        return (self.val < other.val)

    def __le__(self, other: ListNode):
        return(self.val <= other.val)
    

def lnode2list(p: ListNode) -> list:
    """Convert a ListNode to a list."""
    x = list()
    while (p):
        x.append(p.val)
        p = p.next
    return x


def lnode2str(p: ListNode, delim=", ") -> str:
    """Convert a ListNode to a string."""
    x = lnode2list(p)
    return f"({delim.join(x)})"


def list2lnode(vals: list):
    p = head = None
    for v in vals:
        if not head:
            p = head = ListNode(v)
        else:
            p.next = ListNode(v)
            p = p.next
    return head


def make_linked_list(vals: list):
    return list2lnode(vals)


def make_linked_lists(lists):
    return [list2lnode(vals) for vals in lists]


