#!/usr/bin/env python3
"""
Given a value N, if we want to make change for N cents, and we have infinite supply of each of
S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change?

EXAMPLES:
  Input: S = {1, 2, 3}, N = 4
  Output: 4 
  Explaination: {1,1,1,1}, {1,1,2}, {2,2,}, {1,3}

  Input:  S = {2, 5, 3, 6}, N = 10
  Output: 5
  Explaination: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.


HINTS:
  - Need to use a table to avoid duplications.
  - Try to build all possible combinations from bottoms up.

REFERENCE:
  - https://www.geeksforgeeks.org/coin-change-dp-7/

"""

from typing import List


class Solution:
    def coinChange_v1(self, coins: List[int], amount: int) -> int:
        """Use a 2-D table to track the status -- one column for each coin.

        Time complexity: O(nm) and space consumption is O(nm),
        where n is the amount and m is the number of coins.

        Examples:
          Input: S = {1, 2, 3}, N = 4

              | 1  2  3
            --+--------
            0 | 1  1  1
            1 | 1  1  1
            2 | 1  2  2
            3 | 1  2  3
            4 | 1  3  4

        """

        # Build a table for tracking
        m = len(coins)
        table = [[0] * m for _ in range(amount+1)]
        for j in range(m):
            table[0][j] = 1

        # Process one coin at a time.
        for j, c in enumerate(coins):
            for i in range(1, amount+1):
                # There are two ways to reach this amount (i)
                # 1. With coin c.
                x = table[i-c][j] if i >= c else 0
                # 2. Without coin c.
                y = table[i][j-1] if j > 0 else 0
                table[i][j] = x + y

        return table[-1][-1]

    def coinChange_v2(self, coins: List[int], amount: int) -> int:
        """Use a 1-D table to track the status. 

        This is an improvement over v1.
        Time complexity is the same, O(nm). Yet it uses less space: O(n).

        Example (use a 2D table to show how the 1D table evolves with each coin).

          Input: S = {1, 2, 3}, N = 4

              |    1  2  3
            --+------------->
            0 | 1  1  1  1
            1 | 0  1  1  1
            2 | 0  1 (2) 2
            3 | 0  1  2 (3)
            4 | 0  1 (3) 4
              V

          Since only one column is updated at a time, we may use only
          a 1D table to track the status.

        """

        # Build a table for tracking
        m = len(coins)
        table = [1] + [0] * amount

        # Process one coin at a time
        for c in coins:
            # See if this coin can be used a build a value i <= amount,
            # where i is both an index and an amount.
            # Also note that there is an offset.
            for i in range(c, amount+1):
                # Increment the table value if this coin can contribute
                # to the current amount.
                table[i] += table[i-c]

        return table[-1]


def main():
    test_data = [
        [[1, 2, 3], 4, 4],
        [[2, 5, 3, 6], 10, 5],
        [[1, 2, 5], 100, 541],
        [[88, 227, 216, 96, 209, 172, 259], 6928, 67079],
    ]

    sol = Solution()
    for coins, amount, ans in test_data:
        print("# Input = {}, {}. Ans = {}".format(coins, amount, ans))
        print("  Output = {}".format(sol.coinChange_v1(coins, amount)))
        print("  Output = {}".format(sol.coinChange_v2(coins, amount)))


if __name__ == "__main__":
    main()
