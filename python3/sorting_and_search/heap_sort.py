#!/usr/bin/env python3
#
# Heap Sort.
#
# Method:
# 1. Create a max heap.
# 2. Move the head (largest element) to the bottom.  
#    Reduce the heap size by 1 (thus excluding the largest element at the bottom).
# 3. Re-heapify the heap from the top.
# 4. Repeat steps 2, 3 until the heap is empty.
#
# Ref: https://www.geeksforgeeks.org/heap-sort/
#

def heapify(a, n, k):
    """To build a max heap.

    :param a: heap (array); will be modified.
    :param n: size of the heap
    :param k: position to be heapify.
    """
    i_max = k
    i_left = 2 * k + 1  # index to the left child
    i_right = 2 * k + 2  # index to the right child

    # Compare left child with the current max.
    if i_left < n and a[i_left] > a[i_max]:
        i_max = i_left
    # Compare right child with the current max.
    if i_right < n and a[i_right] > a[i_max]:
        i_max = i_right

    # Any swap?  Need to continue to heapify.
    if i_max != k:
        # Move the largest child to the top
        a[k], a[i_max] = a[i_max], a[k]
        # Adjust the children heap that is affected by the swap
        heapify(a, n, i_max)

def heap_sort(arr):
    # 1) Build a Max Heap
    a = arr.copy()
    n = len(arr)

    # Start with the layer above the bottom layer.
    # We may start from the bottom and it won't hurt.
    for k in reversed(range(0, n//2)):
        heapify(a, n, k)

    # 2) Sort - moving current max from the head to the end; reduce heap size by 1.
    for j in reversed(range(0, n)):
        a[0], a[j] = a[j], a[0]
        heapify(a, j, 0)

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
        s1 = heap_sort(arr)
        status = "pass" if s1 == ans else "** FAILED **"
        print("- heap_sort {} => {} ... {}".format(arr, s1, status))


if __name__ == '__main__':
    main()

