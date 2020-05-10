#!/usr/bin/env python3
#
# Quick Sort: 
#    select pivot, then partition the segment into two parts:
#    smaller part, and the larger part.
#    Complexity: N log(N)
#
# Ref: https://www.geeksforgeeks.org/quick-sort/
#

def partition(a, i0, i1):
    pivot_val = a[i1]

    # Move smaller values to the left
    # The final position of the lower-side is tracked by last_low_idx
    last_low_idx = i0 - 1
    for i in range(i0, i1):
        if a[i] < pivot_val:
            last_low_idx += 1
            if last_low_idx != i:
                a[last_low_idx], a[i] = a[i], a[last_low_idx]

    # Swap with the pivot
    pivot_idx = last_low_idx + 1
    a[pivot_idx], a[i1] = a[i1], a[pivot_idx]
    return pivot_idx   


def quick_sort_helper(a, i0, i1):
    """Select last element as the pivot and move elements
       So that elements on the left are smaller, and
       elements on the right are lerger.
       Then, run recursion to process the left-hand side and the right-hand-side.
    """
    if i0 < i1:
        i_pivot = partition(a, i0, i1)
        quick_sort_helper(a, i0, i_pivot - 1)
        quick_sort_helper(a, i_pivot + 1, i1)


def quick_sort(arr):
    a = arr.copy()
    n = len(a)
    quick_sort_helper(a, 0, n-1)
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
        s1 = quick_sort(arr)
        status = "pass" if s1 == ans else "** FAILED **"
        print("quick_sort {} => {} ... {}".format(arr, s1, status))


if __name__ == '__main__':
    main()

