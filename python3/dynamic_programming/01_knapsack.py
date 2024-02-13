#!/usr/bin/env python3
"""
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack with a 
capacity ‘C.’ The goal is to get the maximum profit out of the knapsack items. 
Each item can only be selected once, as we don’t have multiple quantities of any item.

Let’s take Merry’s example, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

  Items: { Apple, Orange, Banana, Melon }
  Weights: { 2, 3, 1, 4 }
  Profits: { 4, 5, 3, 7 }
  Knapsack capacity: 5

Let’s try to put various combinations of fruits in the knapsack, such that their total weight is not more than 5:

  Apple + Orange (total weight 5) => 9 profit
  Apple + Banana (total weight 3) => 7 profit
  Orange + Banana (total weight 4) => 8 profit
  Banana + Melon (total weight 5) => 10 profit

This shows that Banana + Melon is the best combination as it gives us the maximum profit, and the total weight does not exceed the capacity.

Problem Statement:

Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a
subset of these items which will give us maximum profit such that their 
cumulative weight is not more than a given number ‘C.’ Each item can only be selected once,
which means either we put an item in the knapsack or we skip it.

Reference:
  - https://www.educative.io/courses/grokking-the-coding-interview/gkZNLjV2kBk

"""

from typing import List

class Solution:
    def solve_knapsack(self, profits: List[int], weights: List[int], capacity: int) -> int:
        """Bottom-up approach.
        
        Use 2-D array dp to track the maximum profit for given i (item index) and c (capacity).
        Built up the matrix from low indices to high indices.
        
        dp[i][c] can be reached by two ways:
          - without adding an item; thus, it is same as dp[i-1][c]
          - adding item i, thus, it is dp[i-1][c - weight[i]] + profit[i]

        The final value is the maxium of the above two. Thus,
          
            dp[i][c] = max(dp[i-1][c], dp[i-1][c - weight[i]] + profit[i])   (1)
            
        The base lines:
          - capacity = 0;  dp[i][0] = 0 for all i.
          - dp[0][c] = profit[0] if if c >= weight[0]
          
        The remaining can be filled with Equation (1).
        """
        # Sanity check
        n = len(profits)
        if capacity <= 0 or n == 0 or len(weights) != n:
            return 0
        
        # Initialize the dp
        dp = [[0] * (capacity + 1) for _ in range(n)]
        
        # Fill in first item. Accept it if it is less than the capacity
        for c in range(1, capacity+1):
            if weights[0] <= c:
                dp[0][c] = profits[0]

        # Fill up the remaining of the dp usig the equaion.
        for i in range(1, n):
            w = weights[i]
            p = profits[i]
            for c in range(capacity + 1):
                i0 = i - 1
                c0 = c - w
                v1 = dp[i0][c]
                v2 = dp[i0][c0] + profits[i] if c0 >= 0 else 0
                dp[i][c] = max(v1, v2)
        print(f"[DEBUG] dp = {dp}")
        self.get_selected_items(profits, weights, capacity, dp)
        return dp[n-1][capacity]

    def get_selected_items(self, profits, weights, capacity, dp):
        items = []
        c = capacity
        for i in range(len(profits)-1, -1, -1):
            if (i == 0 and dp[i][c] > 0) or (dp[i][c] > dp[i-1][c]):
                items.append(i)
                c -= weights[i]
        sel_weights = [weights[i] for i in items]
        sel_profits = [profits[i] for i in items]
        print(f"[DEBUG] selected items = {items}, weights = {sel_weights}, profits = {sel_profits}")
    

def main():
    profits_1 = [1, 6, 10, 16]
    weights_1 =  [1, 2, 3, 5]
    test_data = [
        [profits_1, weights_1, 5],
        [profits_1, weights_1, 6],
        [profits_1, weights_1, 7],
    ]
    ob1 = Solution()
    for profits, weights, capacity in test_data:
        print(f"Inputs: profits={profits}, weights={weights}, capacity={capacity}")
        print(f"Outputs: max profit = {ob1.solve_knapsack(profits, weights, capacity)}")

        
if __name__ == "__main__":
    main()
