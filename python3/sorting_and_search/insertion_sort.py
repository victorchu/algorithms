#!/usr/bin/env python3
#
# Insertion Sort.
# It behaviors very much like how we sort cards in our hands.
# 

def insertion_sort1(arr):
    """Insert into a new array."""
    def insert_to_array(x, a):
        """Insert x into a in the proper oder.
        Note that x may turn out to be the last element.  Thus, it will be appeneded.
        """
        if x < a[-1]:
            for j, y in enumerate(a):
                if x < y:
                    a.insert(j, x)
                    break
        else:
            a.append(x)

    n = len(arr)
    a = list()
    a.append(arr[0])
    for i in range(1, n):
        insert_to_array(arr[i], a)

    return a


def insertion_sort2(arr):
    """In-place replacement by shifting values"""
    n = len(arr)
    a = arr.copy()
    for i in range(1, n):
        x = a[i]
        if x < a[i-1]:
            j = i - 1
            while j >= 0 and a[j] > x:
                a[j+1] = a[j]
                j -= 1
            a[j+1] = x
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
        s1 = insertion_sort1(arr)
        note = "pass" if s1 == ans else "** FAILED **"
        print("sort1 {} => {} ... {}".format(arr, s1, note))

        s2 = insertion_sort2(arr)
        note = "pass" if s2 == ans else "** FAILED **"
        print("sort2 {} => {} ... {}".format(arr, s2, note))


if __name__ == '__main__':
    main()

