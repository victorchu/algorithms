#!/usr/bin/env python3
#
# This is the easist sort.
# Complexity: n + (n-1) + (n-2) ... + 1 = (n + 1) * n / 2 ~= O(n^2)
#
# Solve the math:
#  y = n + (n-1) + ... +   2   + 1
#  y = 1 +   2   + ....+ (n-1) + n
# 2y = (n+1) * n
#  y = (n+1) * n / 2
# 

def bubble_down(arr):
    """In each round, move the largest number down to the bottom.
    A special part of this approach that we only swap neighboring points.
    The reference point is always the largest value found thus far.
    
    """
    a = arr.copy()
    n = len(a)
    for i in range(n-1):
        # Always start from the top for each iteration
        swapped = False

        for j in range(0, n-i-1):
            k = j + 1
            if a[j] > a[k]:
                # swap with neighbor
                a[k], a[j] = a[j], a[k]
                swapped = True

        if not swapped:
            print("x Early termination when i = {}".format(i))
            break
    return a


def bubble_up(arr):
    """In each round, move the smallest number to the top.
    I found this implementation is easier to understand, since
    i is fixed.
    """
    a = arr.copy()
    n = len(arr)

    for i in range(n-1):
        swapped = False
        for j in range(i+1, n):
            if a[i] > a[j]:
                # swith with the top element
                a[i], a[j] = a[j], a[i]
                swapped = True

        if not swapped:
            print("x Early termination when i = {}".format(i))
            break

    return a


def main():
    # test arrays
    arrs = [
            [4, 1, 3, 2, 5],
            [4, 2, 3, 5, 1],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1]
        ]
    ans = [1, 2, 3, 4, 5]

    for arr in arrs:
        s1 = bubble_down(arr)
        note = "pass" if s1 == ans else "** FAILED **"
        print("sort down {} => {} ... {}".format(arr, s1, note))
        s2 = bubble_down(arr)
        note = "pass" if s2 == ans else "** FAILED **"
        print("sort up   {} => {} ... {}".format(arr, s2, note))


if __name__ == '__main__':
    main()

