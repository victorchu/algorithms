"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

  [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
  ]

REFERENCE:
  - https://leetcode.com/problems/generate-parentheses/ (Medium)
  - https://guides.codepath.org/compsci/Generate-Parentheses
  - https://en.wikipedia.org/wiki/Catalan_number

"""

from typing import List

class Solution:
    def generateParenthesis_v1(self, n: int) -> List[str]:
        """Use recursion.
        
        Time Complexity: O(4^n / sqrt(n)).
        Space complexity: O(n) -- the depth of the recursive call stack.
        """
        def helper(nl: int, nr: int, s: str, results: List[str]):
            """Helper.
            
            :param nl: number of remaining left parenthesis.
            :param nl: number of remaining right parenthesis.
            :param s: current combination
            :param results: A list of completed combinations.
            """
            if (nl == 0) and (nr == 0):
                results.append(s)
            else:
                if (nl > 0):
                    helper(nl-1, nr, s + '(', results)
                if (nl < nr):
                    helper(nl, nr-1, s + ')', results)

        results = list()
        helper(n, n, '', results)
        return results


def main():
    test_data = [
        3,
        1,
        5,
    ]

    ob1 = Solution()
    for n in test_data:
        print(f"# Input  : {n}")
        print(f"  Output v1 : {ob1.generateParenthesis_v1(n)}")


if __name__ == "__main__":
    main()
