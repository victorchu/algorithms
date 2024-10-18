"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
    Input: x = 2.00000, n = 10
    Output: 1024.00000

Example 2:
    Input: x = 2.10000, n = 3
    Output: 9.26100

Example 3:
    Input: x = 2.00000, n = -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25
 
Constraints:
    -100.0 < x < 100.0
    -2^31 <= n <= 2^31-1
    n is an integer.
    Either x is not zero or n > 0.
    -10^4 <= x^n <= 10^4

Reference:
  - https://leetcode.com/problems/powx-n/description/ (Medium)

"""


class Solution:
    def myPow_v1(self, x: float, n: int) -> float:
        """Store x^1, x^2, x^4, ... in an array.

        Time Complexity: O(log(n)) - similar to binary search.
        Space Complexity: O(log(n)) - for the arrays
        """
        # Handle negative n
        if n < 0:
            x = 1.0 / x
            n = -n
    
        # Save x, x^2, x^4, ... in an array
        p, k = x, 1
        powers = [p]
        numbers = [k]
        while k <= n:
            p = p * p
            k = k + k
            powers.insert(0, p)
            numbers.insert(0, k)

        ans = 1
        for p, k in zip(powers, numbers):
            if k <= n:
                n -= k
                ans *= p

        if n != 0:
            raise Exception(f"Unexpected, remaining value of n = {n}")

        return ans

    def myPow_v2(self, x: float, n: int) -> float:
        """Reduce the space usage.

        Time Complexity: O(log(n)) - similar to binary search.
        Space Complexity: O(1)
        """
        # Handle negative n
        if n < 0:
            x = 1.0 / x
            n = -n
    
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans *= x
            x *= x
            n = n // 2
    
        return ans
    

def main():
    test_data = [
        [2.0, 10, 1024.0],
        [2.1, 3, 9.261],
        [2.0, -2, 0.25]
    ]

    ob1 = Solution()
    for x, n, ans in test_data:
        print(f"\n# Input = {x}, {n} ...... {ans}")
        print(f"  output 1 = {ob1.myPow_v1(x, n)}")
        print(f"  output 2 = {ob1.myPow_v2(x, n)}")


if __name__ == "__main__":
    main()

