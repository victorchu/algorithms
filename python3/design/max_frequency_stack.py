#!/usr/bin/env python3
"""
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

  - push(int x), which pushes an integer x onto the stack.
  - pop(), which removes and returns the most frequent element in the stack.
    If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.

EXAMPLES:
  Input:
    cmds = ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"],
    args = [[], [5], [7], [5], [7], [4], [5], [], [], [], []],

  Output: [null,null,null,null,null,null,null,5,7,5,4]

  Explanation:
    After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

    pop() -> returns 5, as 5 is the most frequent.
    The stack becomes [5,7,5,7,4].

    pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
    The stack becomes [5,7,5,4].

    pop() -> returns 5.
    The stack becomes [5,7,4].

    pop() -> returns 4.
    The stack becomes [5,7].

NOTE:
  - Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
  - It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
  - The total number of FreqStack.push calls will not exceed 10000 in a single test case.
  - The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
  - The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.

REFERENCE:
  - https://leetcode.com/problems/maximum-frequency-stack/ (Hard)

"""
from collections import Counter


class FreqStack:
    """Use a stack of stacks -- one substack for each frequency."""

    def __init__(self):
        self.counter = Counter()
        self.stacks = []

    def push(self, x: int) -> None:
        freq = self.counter[x] + 1
        if freq <= len(self.stacks):
            stack = self.stacks[freq-1]
            stack.append(x)
        else:
            self.stacks.append([x])
        self.counter[x] += 1

    def pop(self) -> int:
        stack = self.stacks[-1]
        x = stack.pop()
        if not stack:
            self.stacks.pop()
        self.counter[x] -= 1
        return x


def driver(cmds, args, ver='v1'):
    obj = None
    output = []
    for cmd, arg in zip(cmds, args):
        if cmd == 'FreqStack':
            obj = FreqStack(*arg)
            output.append(None)
        elif cmd == 'push':
            output.append(obj.push(*arg))
        elif cmd == 'pop':
            output.append(obj.pop(*arg))
    return output


def main():
    test_data = [
        [["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"],
         [[], [5], [7], [5], [7], [4], [5], [], [], [], []],
         [None, None, None, None, None, None, None, 5, 7, 5, 4]
         ],
    ]

    for cmds, args, ans in test_data:
        print("# Input: ".format(cmds, args, ans))
        print("  - cmds = {}".format(cmds))
        print("  - args = {}".format(args))
        print("  - ans  = {}".format(ans))
        print("  Output:  {}".format(driver(cmds, args)))


if __name__ == "__main__":
    main()
