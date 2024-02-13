#!/usr/bin/env python3
"""
Convert a non-negative integer to its english words representation.
Given input is guaranteed to be less than 2^31 - 1.

EXAMPLES:
  Input: 123
  Output: "One Hundred Twenty Three"

  Input: 12345
  Output: "Twelve Thousand Three Hundred Forty Five"

  Input: 1234567
  Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

  Input: 1234567891
  Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

HINTS:
  - Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
  - Group the number by thousands (3 digits). You can write a helper function
    that takes a number less than 1000 and convert just that chunk to words.
  - There are many edge cases. What are some good test cases? Does your code
    work with input such as 0? Or 1000010? (middle chunk is zero and should not be
    printed out)

REFERENCE:
  - https://leetcode.com/problems/integer-to-english-words/ (Medium)
  - https://en.wikipedia.org/wiki/Names_of_large_numbers

"""

from typing import List


class Solution:
    def numberToWords(self, num: int) -> str:
        number_names = [
            "Thousand",
            "Million",      # 10^6
            "Billion",      # 10^9
            "Trillion",     # 10^12
            "Quadrillion",  # 10^15
            "Quintillion",  # 10^18
            "Sextillion",   # 10^21
            "Septillion",   # 10^24
            "Octillion",    # 10^27
            "Noiillion",    # 10^30
        ]
        tens = {
            10: "Ten",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }
        teens = {
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
        }
        digits = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
        }

        def process_hundreds(num):
            """Process a numer in [1, 999]"""

            # Hundreds
            words = []
            h = num // 100
            if h > 0:
                words.append(digits[h])
                words.append('Hundred')
            n2 = num % 100

            # Teens
            if n2 > 10 and n2 < 20:
                words.append(teens[n2])
            # Others
            else:
                d = n2 // 10
                if d > 0:
                    words.append(tens[10 * d])

                n3 = n2 % 10
                if n3 > 0:
                    words.append(digits[n3])

            return " ".join(words) if words else ''

        if num == 0:
            return "Zero"

        words = []
        i = -1
        while num > 0:
            n999 = num % 1000
            if n999 > 0:
                if i >= 0:
                    unit_name = number_names[i]
                    words.append(unit_name)
                w = process_hundreds(n999)
                words.append(w)
            i += 1
            num = num // 1000

        return ' '.join(reversed(words))


def main():
    test_data = [
        123,
        312,
        12345,
        1234567,
        1234567891,
        0,
    ]

    sol = Solution()
    for num in test_data:
        print("# Input = {}".format(num))
        print("  Output = {}".format(sol.numberToWords(num)))


if __name__ == "__main__":
    main()
