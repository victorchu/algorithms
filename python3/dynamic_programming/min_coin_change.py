#!/usr/bin/env python3
"""
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

EXAMPLES:
  Input: coins = [1, 2, 5], amount = 11
  Output: 3 
  Explanation: 11 = 5 + 5 + 1

  Input: coins = [2], amount = 3
  Output: -1

  Input: coins = [1], amount = 0
  Output: 0

Constraints:
    1 <= coins.length <= 12
    1 <= coins[i] <= 2^31 - 1
    0 <= amount <= 10^4

REFERENCE:
  - https://leetcode.com/problems/coin-change/ (Medium)
  - https://www.geeksforgeeks.org/coin-change-dp-7/
  - https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/?ref=lbp

"""
from typing import List


class Solution:
    def coinChange_v1(self, coins: List[int], amount: int) -> int:
        """Use a 1-D table to track the status. 

        This is an improvement over v1.
        Time complexity is the same, O(nm). Yet it uses less space: O(n).

        Examples using 2D tables to show how the 1D tables evolves with each coin.
        The table values are the minimum number of coins required for the target amount.

          Input: coins = [1, 2, 5], amount = 11
          Output: 3 
          Explanation: 11 = 5 + 5 + 1

                  |     1  2  5
                --+--------------->
                0 |  0  0  0  0
                1 | -1  1  1  1
                2 | -1  2  1  1
                3 | -1  3  2  2
                4 | -1  4  2  2
                5 | -1  5  3  1
                6 | -1  6  3  2
                7 | -1  7  4  2
                8 | -1  8  4  3
                9 | -1  9  5  3
               10 | -1 10  5  2
               11 | -1 11  6  3

          Input: coins = [2], amount = 2
          Output: -1 

                  |      2 
                --+---------->
                0 |  0   0
                1 | -1  -1
                2 | -1   1
                3 | -1  -1

        """

        # Build a table for tracking
        table = [0] + [-1] * amount

        # Process one coin at a time
        for j, c in enumerate(coins):
            for i in range(c, amount+1):
                # Increment the table value if this coin can contribute
                # to the current amount.
                x = table[i]
                y = table[i-c] + 1 if table[i-c] >= 0 else -1

                if x > 0 and y > 0:
                    table[i] = min(x, y)
                elif x > 0:
                    table[i] = x
                elif y > 0:
                    table[i] = y

        return table[-1]

    def coinChange_v2(self, coins: List[int], amount: int) -> int:
        """Use a 1-D table to track the status. 

        Similar to v1, yet here we initialize the table to a MAX value.
        """

        # Build a table for tracking
        MAX = amount + 1
        table = [0] + [MAX] * amount

        # Process one coin at a time
        for j, c in enumerate(coins):
            for i in range(c, amount+1):
                x = table[i-c] + 1 if table[i-c] != MAX else MAX
                y = table[i]
                table[i] = min(x, y)

        return table[-1] if table[-1] < MAX else -1

    def coinChange_v3(self, coins: List[int], amount: int) -> int:
        """Get the optimal restul for each amount starting from 1.

        This is similar to v2, yet swaps the order of the double loop.
        """
        # Build a table for tracking
        MAX = amount + 1
        table = [0] + [MAX] * amount

        # Build the optimal results from 1 to amount
        for i in range(1, amount+1):
            # Get the optimal results from each coin
            vals = [table[i-c] + 1 for c in coins if c <= i]
            # Select the best (smallest)
            table[i] = min(vals) if vals else MAX

        return table[-1] if table[-1] < MAX else -1


def main():
    test_data = [
        [[1, 2, 5], 11, 3],
        [[1, 2, 5, 9, 10], 18, 2],
        [[2], 3, -1],
        [[1, 2, 5], 17, 4],
        [[1, 2, 5], 100, 20],
        [[88, 227, 216, 96, 209, 172, 259], 6928, 27],
    ]

    sol = Solution()
    for coins, amount, ans in test_data:
        print("# Input = {}, {}. Ans = {}".format(coins, amount, ans))
        print("  Output = {}".format(sol.coinChange_v1(coins, amount)))
        print("  Output = {}".format(sol.coinChange_v2(coins, amount)))
        print("  Output = {}".format(sol.coinChange_v3(coins, amount)))


if __name__ == "__main__":
    main()
