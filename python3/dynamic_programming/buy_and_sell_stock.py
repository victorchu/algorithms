#!/usr/bin/env python3
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one
and sell one share of the stock), design an algorithm to find the maximum
profit.

Note that you cannot sell a stock before you buy one.

EXAMPLES:

  Input: [7,1,5,3,6,4]
  Output: 5
  Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
               Not 7-1 = 6, as selling price needs to be larger than buying price.


  Input: [7,6,4,3,1]
  Output: 0
  Explanation: In this case, no transaction is done, i.e. max profit = 0.

REFERENCE:
  - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ (Easy)

"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Track current min price and the max profit."""
        if not prices:
            return 0
        min_price = max(prices)
        max_profit = 0
        for p in prices:
            # Adjust the min price. Yet, we cannot sell on the same day.
            if p < min_price:
                min_price = p            
            # Calculate the profit
            else:
                max_profit = max(max_profit, p - min_price)
        return max_profit


def main():
    test_data = [
        [[7, 1, 5, 3, 6, 4], 5],
        [[7, 6, 4, 3, 1], 0],
        [[], 0],
    ]

    ob1 = Solution()
    for prices, ans in test_data:
        print(f"# Input = {prices} (ans={ans})")
        print(f"  Output = {ob1.maxProfit(prices)}")


if __name__ == "__main__":
    main()
