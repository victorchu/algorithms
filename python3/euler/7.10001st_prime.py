#!/usr/bin/env python3
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Note:
  - The follwing prime features are important for optimization:
    . The first prime is 2. Other prims are odd numbers.
    . The max prime factor is sqrt(n)

  - May use divmod(x, y) to get both the quotient (x // y) and the remainder (x % y) in one shot.
    E.g. divmode(10, 3) will return 3, 1. Factor testing can stop when (q <= y).

Reference:
  - https://projecteuler.net/problem=7

"""

import math


class Solution:
    def method_v1(self, n):
        if n < 1:
            return None

        def next_prime_after_2(i, primes):
            while True:
                is_prime = True
                for p in primes:
                    q, r = divmod(i, p)
                    if r == 0:
                        is_prime = False
                        break
                    # Early termination of the loop
                    if q <= p:
                        break

                if is_prime == True:
                    primes.append(i)
                    break
                else:
                    i += 2

        # Handle 2
        primes = list()
        primes.append(2)
        i = 3

        # Handle others, must be odd numbers
        while len(primes) < n:
            next_prime_after_2(i, primes)
            print(f"[DEBUG] found {primes[-1]:4d} (# {len(primes)})")
            i = primes[-1] + 2

        return primes[-1]

def main():
    test_data = [
        6,
        10001
    ]

    sol = Solution()
    for data in test_data:
        print("# Input: {}".format(data))
        print("  - Output v1: {}".format(sol.method_v1(data)))


if __name__ == "__main__":
    main()
