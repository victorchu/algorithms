"""
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.


Example 1:
    Input: n = 5, bad = 4
    Output: 4
    Explanation:
    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true
    Then 4 is the first bad version.

Example 2:
    Input: n = 1, bad = 1
    Output: 1
 

Constraints:

1 <= bad <= n <= 2^31 - 1

Reference:
  - https://leetcode.com/problems/first-bad-version/

"""

from typing import List


class Solution:
    def firstBadVersion_v1(self, n: int) -> int:
        """Binary search with recursion.

        Time Complexity = O(log n).  
        Space Complexity = O(log n) -- call stacks.
        """
        def helper(L: int, R: int, ans: List[int]):
            if L > R:
                return
            
            m = (L + R) // 2
            if isBadVersion(m):
                ans[0] = min(ans[0], m)
                helper(L, m-1, ans)
            else:
                helper(m+1, R, ans)

        ans = [n]
        helper(1, n, ans)
        return ans[0]

    def firstBadVersion_v2(self, n: int) -> int:
        """Binary search with Loop.

        Time Complexity: O(log N).  Space: O(1)
        """
        ans = n
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans



BAD_VERSION = -1
def isBadVersion(version: int) -> bool:
    return version == BAD_VERSION


def main():
    global BAD_VERSION
    test_data = [
        [5, 4],
        [1, 1]
    ]

    ob1 = Solution()
    for n, bad in test_data:
        BAD_VERSION = bad
        print(f"# Input: n={n} ...... ans={bad}")
        print(f"  - Output v1: {ob1.firstBadVersion_v1(n)}")
        print(f"  - Output v2: {ob1.firstBadVersion_v2(n)}")
        print()


if __name__ == "__main__":
    main()

