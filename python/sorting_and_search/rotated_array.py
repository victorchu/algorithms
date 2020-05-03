#!/usr/bin/env python3
"""
Problem:
   An element in a sorted array can be found in O(log n) time via
    binary search. But suppose we rotate an ascending order sorted array
    at some pivot unknown to you beforehand. So for instance, 1 2 3 4
    5 might become 3 4 5 1 2. Devise a way to find an element in the
    rotated array in O(log n) time.

Strategy:
  - It will be easier if we divide it into two cases:
    (a) the target is on the upper part (x >= x0)
    (b) the target is on the lower part (x <= x1)

  - Then we can check either the right condition or the left condition.
    One of them can be easier.
    (a) right for upper.
    (b) left for lower

History:
  - 2019-07-27 Finished firist implementaiton after thinking/trying for a while. 
               This is tricker than the standard binary search.
               Key is divide and conquer.

"""

DEBUG = False
#DEBUG = True

def find_recursive(arr, x):
    """Find x in arr.

    Use recurssion.

    :param arr: an sorted array.
    :param x: an element to be searched.
    :return: index of x in arr if found; otherwise, -1.
    """
    def helper(arr, x, i0, i1):
        """A helper function.
        It is guaranteed that x > arr[i0] and x < arr[i1]
        """
        x0 = arr[i0]
        x1 = arr[i1]

        # termination condition
        if i1 <= i0 + 1:
            return -1
        else:
            # Get the middle point
            i2 = int((i0 + i1) / 2)
            x2 = arr[i2]
            if DEBUG: print("[DEBUG] - checking arr[{}] = {}".format(i2, x2))

            # Found the value
            if x == x2:
                return i2

            # x in the upper area
            if x > x0:
                if x > x2 and x2 > x0:
                    if DEBUG: print("[DEBUG]   -> upper right: arr[{}, {}] = [{}, {}] ".format(i2, i1, x2, x1))
                    return helper(arr, x, i2, i1)
                else:
                    if DEBUG: print("[DEBUG]   -> upper left: arr[{}, {}] = [{}, {}] ".format(i0, i2, x0, x2))
                    return helper(arr, x, i0, i2)

            # x in the lower area
            elif x < x1:
                # The right condition is more complicated in that x may be less than x2
                if (x > x2 and x2 < x1) or (x2 > x0):
                    if DEBUG: print("[DEBUG]   -> lower right: arr[{}, {}] = [{}, {}] ".format(i2, i1, x2, x1))
                    return helper(arr, x, i2, i1)
                else:
                    if DEBUG: print("[DEBUG]   -> lower left: arr[{}, {}] = [{}, {}] ".format(i0, i2, x0, x2))
                    return helper(arr, x, i0, i2)

                # Alternativly, we can use the following (left condition):
                #if x < x2 and x2 < x1:
                #    if DEBUG: print("[DEBUG]   -> lower left: arr[{}, {}] = [{}, {}] ".format(i0, i2, x0, x2))
                #    return helper(arr, x, i0, i2)
                #else:
                #    if DEBUG: print("[DEBUG]   -> lower right: arr[{}, {}] = [{}, {}] ".format(i2, i1, x2, x1))
                #    return helper(arr, x, i2, i1)

            else:
                # No solution
                return -1

    i0 = 0
    i1 = len(arr) - 1
    x0 = arr[i0]
    x1 = arr[i1]

    # Check boundary conditions
    if x == x0:
        return i0
    elif x == x1:
        return i1

    # Recursion
    else:
        return helper(arr, x, i0, i1)


def find_iterative(arr, x):
    """Find x in arr.

    Use loop (iterative)

    :param arr: an sorted array.
    :param x: an element to be searched.
    :return: index of x in arr if found; otherwise, -1.
    """

    i0 = 0
    i1 = len(arr) - 1
    x0 = arr[i0]
    x1 = arr[i1]

    if x == x0:
        return i0
    elif x == x1:
        return i1

    retval = -1
    c = 0
    n = len(arr)
    while (i1 - i0) > 1:
        i2 = int((i0 + i1) / 2)
        x2 = arr[i2]
        if DEBUG: print("[debug] checking [{}, {}, {}]".format(x0, x2, x1))

        # termination condition
        if x == x2:
            retval = i2
            break
        
        # x is in the upper arrea
        if x > x0:
            # upper-right
            if x > x2 and x2 > x0:
                if DEBUG: print("[debug] -> upper right")
                i0 = i2
                x0 = x2
            # upper-left
            else:
                if DEBUG: print("[debug] -> upper left")
                i1 = i2
                x1 = x2

        # x is in the lower arrea
        elif x < x1:
            # lower-left
            if x < x2 and x2 < x1:
                if DEBUG: print("[debug] -> lower left")
                i1 = i2
                x1 = x2
            else:
                if DEBUG: print("[debug] -> lower right")
                i0 = i2
                x0 = x2
        else:
            # invalid case
            break

        # Check the counter
        c += 1
        if c >= n:
            print("ERROR - too many loops {}".format(c))
            raise Exception("Infinite loop")

    return retval


def dump(arr):
    """Dump the array values and indices"""
    print("arr = {}".format(arr))
    for i, x in enumerate(arr):
        print(" x={} => {}".format(x, i))


def main():
    arr = [10, 12, 15, 1, 2, 3, 4, 5, 6, 8]
    non_arr = [0, 7, 9, 11, 13, 14, 16]
    x_vals = arr + non_arr
    answers = list(range(len(arr))) + [-1] * len(non_arr)
    dump(arr)

    print("\n## Recursive")
    for x, ans in zip(x_vals, answers):
        if DEBUG: print("# Searching for {}...".format(x))
        idx = find_recursive(arr, x)
        rating = "right" if idx == ans else "** WRONG **"
        print("- find({:2d}) => {:2d} (ans = {:2d}) ... {}".format(x, idx, ans, rating))

    print("\n## Iterative (Loop)")
    for x, ans in zip(x_vals, answers):
        if DEBUG: print("# Searching for {}...".format(x))
        idx = find_iterative(arr, x)
        rating = "right" if idx == ans else "** WRONG **"
        print("- find({:2d}) => {:2d} (ans = {:2d}) ... {}".format(x, idx, ans, rating))


if __name__ == '__main__':
    main()


