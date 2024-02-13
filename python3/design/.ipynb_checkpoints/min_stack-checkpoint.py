#!/usr/bin/env python3
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

  - push(x) -- Push element x onto stack.
  - pop() -- Removes the element on top of the stack.
  - top() -- Get the top element.
  - getMin() -- Retrieve the minimum element in the stack.

EXAMPLES:
  Input
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

  Output
    [None,None,None,None,-3,None,0,-2]

  Explanation
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()   # return -3
    minStack.pop()
    minStack.top()      # return 0
    minStack.getMin()   # return -2

HINTS:
  - We need a structure to track all of the min values.
    One candidate is a stack.
    Another is a list of (position, min_value)

REFERENCE:
  - https://leetcode.com/problems/min-stack/ (Easy)

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()  # store actual values
        self.hist = list()   # track min value changes
        self.curr_min = None
        

    def push(self, x: int) -> None:
        """Push a value to the stack."""
        self.stack.append(x)
        if self.curr_min is None or x < self.curr_min:
            self.hist.append([len(self.stack), x])
            self.curr_min = x

    def pop(self) -> None:
        """Remove the element on the top of the stack."""
        if self.stack:
            n = len(self.stack)
            self.stack.pop()
            if self.hist[-1][0] == n:
                self.hist.pop()
                self.curr_min = self.hist[-1][1] if self.hist else None

    def top(self) -> int:
        """Get the top element."""
        return self.stack[-1] if self.stack else None
        
    def getMin(self) -> int:
        return self.curr_min


def main():
    
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())


if __name__ == "__main__":
    main()
