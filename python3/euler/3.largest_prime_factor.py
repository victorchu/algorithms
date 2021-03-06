#!/usr/bin/env python3
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Note:
  - This problem is a little bit tricky.
  - Can be a little bit challenging on the first time.

Reference:
  - https://projecteuler.net/problem=3
  - https://www.geeksforgeeks.org/find-largest-prime-factor-number/

"""

import math


class Solution:

    def method_v1(self, n:int) -> int:
        """Brute force.  It doesn't work well on large numbers."""
        primes = list()
        factors = list()
        for i in range(2,n+1):
            is_prime = True
            for p in primes:
                if i % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
                if n % i == 0:
                    print(f"[DEBUG] found {i} (n = {n})")
                    factors.append(i)
        return factors[-1]

    def method_v2(self, n:int) -> int:
        """Try to be a little bit smarter.

        Here we first try to find the next prime, and then check if it is a factor.
        Every time we find a factor (f), we divide the number (n) it by the factor.
        """
        def find_prime_factors(i0, n, primes, factors):
            """Find one factor at a time."""

            next_factor = None
            for i in range(i0, n+1):
                # Search for the next prime
                is_prime = True
                for p in primes:
                    if i % p == 0:
                        is_prime = False
                        break
                    
                # Found a new prime number
                if is_prime:
                    primes.append(i)

                    # Check if this prime is a factor
                    is_factor = False
                    if n % i == 0:
                        next_factor = i
                        break

            # Handle the factor
            if next_factor:
                while n % next_factor == 0:
                    print(f"[DEBUG] found {next_factor} (n = {n})")
                    # Reduce the value of n by the factor
                    n = n // next_factor
                    factors.append(next_factor)

                find_prime_factors(next_factor + 1, n, primes, factors)

        primes = list()
        factors = list()
        find_prime_factors(2, n, primes, factors)
        return factors[-1]

    def method_v3(self, n:int) -> int:
        """The solution posted on geeksforgeeks.

        A very smart solution.... likely the optimal one.

        Time complexity: O(sqrt(n)).
        """
        ans = None

        # Handle 2
        while (n % 2 == 0):
            print(f"[DEBUG] found 2 (n = {n})")
            n = n // 2
            ans = 2

        # Handle 3 and above.  
        # 1. The next prime must be an odd number (since we have handled 2)..
        # 2. The max possible factor (other than n) is sqrt(n)
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                print(f"[DEBUG] found {i} (n = {n})")
                n = n // i
                ans = i

        # Handle the remainder
        if n > 2:
            print(f"[DEBUG] found {n} (n = {n})")
            ans = n

        return ans


def main():
    test_data = [
        3 * 3 * 3 * 3 * 5 * 5 * 5 * 5 * 7 * 11 * 11,
        13195,
        600851475143
    ]

    sol = Solution()
    for n in test_data:
        print("# Input: {}".format(n))
        if  n < 1000000:
            print("  - Output v1: {}".format(sol.method_v1(n)))
        print("  - Output v2: {}".format(sol.method_v2(n)))
        print("  - Output v3: {}".format(sol.method_v3(n)))


if __name__ == "__main__":
    main()
