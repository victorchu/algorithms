#!/usr/bin/env python3

def find_recursive(arr, x):
    """Find x in arr.

    Use recurssion.

    :param arr: an sorted array.
    :param x: an element to be searched.
    :return: index of x in arr if found; otherwise, -1.
    """
    def binary_search(arr, x, i0, i1):
        """A helper function.
        It is guaranteed that x > arr[i0] and x < arr[i1]
        """
        # termination condition
        if i1 <= i0 + 1:
            return -1
        else:
            # Get the middle point
            i2 = int((i0 + i1) / 2)
            x2 = arr[i2]

            # Found the value
            if x == x2:
                return i2
            # search the right half
            elif x > x2:
                return binary_search(arr, x, i2, i1)
            # search the left half
            else:
                return binary_search(arr, x, i0, i2)

    i0 = 0;
    i1 = len(arr) - 1
    x0 = arr[i0]
    x1 = arr[i1]

    # Check the "base cases"
    if x == x0:
        return i0
    elif x == x1:
        return i1
    elif x < x0 or x > x1:
        return -1
    else:
        # Start the binary search
        return binary_search(arr, x, i0, i1)


def find_iterative(arr, x):
    """Find x in arr.  Use loop.

    :param arr: an sorted array.
    :param x: an element to be searched.
    :return: index of x in arr if found; otherwise, -1.
    """
    i0 = 0;
    i1 = len(arr) - 1
    x0 = arr[i0]
    x1 = arr[i1]

    # Check initial conditions
    if x == x0:
        return i0
    elif x == x1:
        return i1
    elif x < x0 or x > x1:
        return -1
    else:
        retval = -1
        while i1 > i0 + 1:
            i2 = int((i0+i1)/2)
            x2 = arr[i2]
            if x2 == x:
                retval = i2
                break
            elif x > x2:
                i0 = i2
            else:
                i1 = i2
        return retval
        

def dump(arr):
    """Dump the array values and indices"""
    print("arr = {}".format(arr))
    for i, x in enumerate(arr):
        print(" x={} => {}".format(x, i))


def main():
    arr = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15]
    x_vals = arr + [0, 7, 9, 11, 13, 14, 16]
    dump(arr)

    print("# Recursive implementaiton")
    for x in x_vals:
        idx = find_recursive(arr, x)
        print("- find({:2d}) => {:2d}".format(x, idx))

    print("# Iterative (loop) implementation")
    for x in x_vals:
        idx = find_iterative(arr, x)
        print("- find({:2d}) => {:2d}".format(x, idx))


if __name__ == '__main__':
    main()


