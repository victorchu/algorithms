#!/usr/bin/env python3
"""
Evaluate 'Reverse Polish Notations'.
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
  - https://www.programcreek.com/2012/12/leetcode-evaluate-reverse-polish-notation/

"""


import logging
import re

logger = logging.getLogger(__name__)


def eval_rpn(tokens):
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


# ----------------
#   Main
# ----------------
def init_logging():
    fmt = "%(asctime)s %(levelname)s [%(funcName)s] %(message)s"
    datefmt = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.DEBUG)


def main():
    """Main function"""
    init_logging()

    test_data = [
        ['2', '1', '+', '3', '*'],
        ['4', '13', '5', '/', '+']
    ]
    for x in test_data:
        y = eval_rpn(x)
        logger.info("> evaluate: {} -> {}".format(x, y))


if __name__ == "__main__":
    main()
