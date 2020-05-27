#!/usr/bin/env python3
"""
Evaluate the value of an arithemetric expression in Reverse Polish Notation.

Valid operators are: + - * /
Each operand may be an integer or another expression.

Examples:
  ['2', '1', '+', '3', '*'] -> ((2 + 1) * 3) -> 9
  ['4', '13', '5', '/', '+'] -> (4 + (13 / 5)) -> 6

Key functions:
  - list.append()
  - list.pop()
  - // : integer operator
  - int(str): convert string to integer

Ref:
  - https://leetcode.com/problems/evaluate-reverse-polish-notation/ (Medium)

"""

import re


class Solution:
    def eval_rpn(self, tokens):
        """Evaluate a reverse polish notation.

        Time is O(n).  Space is O(1)
        """
        stack = list()
        operators = ['+', '-', '*', '/']
        try:
            for x in tokens:
                if x in operators:
                    b = stack.pop()
                    a = stack.pop()
                    if x == '+':
                        stack.append(a + b)
                    elif x == '-':
                        stack.append(a - b)
                    elif x == '*':
                        stack.append(a * b)
                    elif x == '/':
                        stack.append(a // b)
                    else:
                        raise Exception('Invalid operator {}'.format(x))
                else:
                    stack.append(int(x))
            return stack.pop()
        except:
            raise Exception("Invalid notation array {}".format(notation_array))


def main():
    test_data = [
        ['2', '1', '+', '3', '*'],
        ['4', '13', '5', '/', '+']
    ]
    sol = Solution()
    for x in test_data:
        y = sol.eval_rpn(x)
        print("> evaluate: {} -> {}".format(x, y))


if __name__ == "__main__":
    main()
