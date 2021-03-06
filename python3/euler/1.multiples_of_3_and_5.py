#!/usr/bin/env python3
"""
If we list all the natural numbers below 10 that are multiples of
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Follow up:
  - Propose more than one method to solve this problem.
  - Can you solve this problem analytically?

Comment:
  - This problem is simple and elegant.

Ref:
  - https://projecteuler.net/problem=1

"""

from typing import List


class Solution:

    def method1(self, n):
        """Use division.

        Complexity: O(N)
        """
        ans = 0
        for i in range(3, n):
            if (i % 3 == 0) or (i % 5 == 0):
                ans += i
        return ans

    def method2(self, n):
        """Use multifications.

        Complexity O(N/3) + O(N/5) = O(N)
        """
        values = set()
        for i in range(3, n, 3):
            values.add(i)
        for j in range(5, n, 5):
            values.add(j)
        return sum(values)

    def method3(self, n):
        """Get the theoretical answer.

        Complexity: O(1)
        """
        def get_multiples_of_x(x, n):
            num_values = n // x
            lb = x
            ub = n - (n % x)
            total = (lb + ub) * num_values / 2
            return int(total)

        s3 = get_multiples_of_x(3, n)
        s5 = get_multiples_of_x(5, n)
        s15 = get_multiples_of_x(15, n)
        return s3 + s5 - s15


def main():
    test_data = [
        10,
        1000,
    ]
    s = Solution()
    for n in test_data:
        print(f"# Input  : {n}")
        print(f"  Output 1: {s.method1(n)}")
        print(f"  Output 2: {s.method2(n)}")
        print(f"  Output 3: {s.method3(n)}")


if __name__ == "__main__":
    main()
