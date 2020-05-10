#!/usr/bin/env python3
#
# Merge sort is O(N logN), very efficient.
# It divides the array into halves until it becomese 1 element.
# Then merge two at a time back.
# 
# History:
#  - 2019-07-28  First implementation.
#

def merge_sort(a):
    """Merge Sort, no helper function.
    This is a cleaner implementation

    :param a: The array that will be sorted, and modified.
    """
    # Check the termination condition
    if len(a) <= 1: 
        return

    #------------------
    # Split the Array
    #------------------
    mid = len(a) // 2    # floor division
    L = a[:mid]   # left copy.  Slicing does copying
    R = a[mid:]   # right copy

    # Merge sort left array.  The array will be modified.
    merge_sort(L)
    # Merge sort right array.  The array will be modified.
    merge_sort(R)

    #---------------------
    # Merge Sorted Arrays
    #---------------------
    nL = len(L)
    nR = len(R)
    i = j = k = 0

    # Copy data from temp arrays L & R
    while i < nL and j < nR:
        if L[i] < R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    # Check remaining elements in L
    while i < nL:
        a[k] = L[i]
        i += 1
        k += 1

    # Check remaining elements in R
    while j < nR:
        a[k] = R[j]
        j += 1
        k += 1

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

    for a in arrs:
        s = a.copy()
        merge_sort(s)
        note = "pass" if s == ans else "** FAILED **"
        print("- mrege_sort {} => {} ... {}".format(a, s, note))


if __name__ == '__main__':
    main()

