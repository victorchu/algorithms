"""
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
  Input: num1 = "2", num2 = "3"
  Output: "6"

Example 2:
  Input: num1 = "123", num2 = "456"
  Output: "56088"
 
Constraints:
 - 1 <= num1.length, num2.length <= 200
 - num1 and num2 consist of digits only.
 - Both num1 and num2 do not contain any leading zero, except the number 0 itself.

 Technologies:
  - ord()
  - str.lstrip('0')
  - map()

"""

class Solution:
    def multiply_v1(self, num1: str, num2: str) -> str:
        """Allocate a vector to store the numerical results."""
        # Handle special cases
        if num1 == '0' or num2 == '0':
            return '0'
        
        len1, len2 = len(num1), len(num2)
        n = len1 + len2
        prod = [0] * n   # normal order
        ord0 = ord('0')

        # Multiplication w/o worrying about carry
        for j, c2 in enumerate(num2[::-1]):
            for i, c1 in enumerate(num1[::-1]):
                k = n - i - j - 1
                prod[k] += (ord(c1) - ord0) * (ord(c2) - ord0)

        # Handle carries
        for k in range(n-1, -1, -1):
            if prod[k] >= 10:
                prod[k-1] += prod[k] // 10
                prod[k] %= 10

        # Convert back to string and strip leading zeroes
        prod_str = ''.join(map(str, prod))
        return prod_str.lstrip('0')

    def multiply_v2(self, num1: str, num2: str) -> str:
        """Cheating."""
        return str(int(num1) * int(num2))


def main():
    test_data = [
        ['2', '3', '6'],
        ['123', '456', '56088'],
        ['9133', '0', '0'],
        ['0', '52', '0'],
    ]

    ob1 = Solution()
    for num1, num2, prod in test_data:
        print(f"# Input = {num1}, {num2} => {prod}")
        print(f"  output v1 = {ob1.multiply_v1(num1, num2)}")
        print(f"  output v2 = {ob1.multiply_v2(num1, num2)}")


if __name__ == "__main__":
    main()
