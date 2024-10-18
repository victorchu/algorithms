""" 
Given two integers dividend and divisor, divide two integers without using multiplication, 
division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. 
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

Example 1:
    Input: dividend = 10, divisor = 3
    Output: 3
    Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
    Input: dividend = 7, divisor = -3
    Output: -2
    Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:
    -2^31 <= dividend, divisor <= 2^31 - 1
    divisor != 0

Technologies:
  - Shift operators: << >>
  - Pay attention to the constraints and the edge cases.

Ref:
  * https://leetcode.com/problems/divide-two-integers/ (Medium)

"""

class Solution:
    def divide_v1(self, dividend: int, divisor: int) -> int:
        """Repeated exponential searches.
        
        Time Complexity: O(log^2 N).  Space: O(1)
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Make all values negative
        sign = 1
        if dividend > 0:
            sign = -sign
            dividend = -dividend
        if divisor > 0:
            sign = -sign
            divisor = -divisor

        quotient = 0 
        while dividend <= divisor:
            step_size, multiple = divisor, 1
            while dividend <= (step_size << 1):
                # multiple by 2
                step_size <<= 1
                multiple <<= 1
            
            dividend -= step_size
            quotient += multiple

        if sign < 0:
            quotient = -quotient

        return quotient

    def divide_v2(self, dividend: int, divisor: int) -> int:
        """Adding power of 2. Use space to save repeated computation.
        
        Time Complexity: O(log N).  Space: O(log N)
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Make all values negative
        sign = 1
        if dividend > 0:
            sign = -sign
            dividend = -dividend
        if divisor > 0:
            sign = -sign
            divisor = -divisor

        steps = list()
        multiples = list()
        step, multiple = divisor, 1
        while dividend <= step:
            steps.append(step)
            multiples.append(multiple)
            step <<= 1
            multiple <<= 1

        quotient = 0 
        for step, multiple in zip(steps[::-1], multiples[::-1]):
            if dividend <= step:
                dividend -= step
                quotient += multiple

        if sign < 0:
            quotient = -quotient

        return quotient

    def divide_v3(self, dividend: int, divisor: int) -> int:
        """Adding power of 2.  Save the lists.
        
        Time Complexity: O(log N).  Space: O(1)
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Make all values negative
        sign = 1
        if dividend > 0:
            sign = -sign
            dividend = -dividend
        if divisor > 0:
            sign = -sign
            divisor = -divisor

        step, multiple = divisor, 1
        while dividend <= (step << 1):
            step <<= 1
            multiple <<= 1

        quotient = 0 
        while (dividend <= divisor) and (multiple >= 1):
            if dividend <= step:
                dividend -= step
                quotient += multiple
            step >>= 1
            multiple >>= 1

        if sign < 0:
            quotient = -quotient

        return quotient


def main():
    test_data = [
        [10, 3, 3],
        [10000, -3, -3333],
        [7, -3, -2],
        [-2147483648, -1, 2147483647],
        [-2147483648, 1, -2147483648]
    ]

    ob1 = Solution()
    for dividend, divisor, ans in test_data:
        print(f"\n# Input = {dividend}, {divisor} ---> {ans}")
        print(f"  output v1 = {ob1.divide_v1(dividend, divisor)}")
        print(f"  output v2 = {ob1.divide_v2(dividend, divisor)}")
        print(f"  output v3 = {ob1.divide_v3(dividend, divisor)}")


if __name__ == "__main__":
    main()

