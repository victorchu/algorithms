/**
 * Merge sort is O(N logN), very efficient.
 * It divides the array into halves until it becomese 1 element.
 * Then merge two at a time back.
 */
package sorting_and_search;

import java.util.Arrays;

public class MergeSort {

    /**
     * Copy a sub-array.
     * @param a Array
     * @param l Left index, inclusive.
     * @param r Right index, inclusive.
     * @return A newly created array with contents a[l,...,r]
     */
    public static int[] copySubArray(int[] a, int l, int r) {
        int n = r - l + 1;
        int[] s = new int[n];
        for (int i = l, k = 0; i <= r; ++i, ++k) {
            s[k] = a[i];
        }
        return s;
    }

    /**
     * Merge two sorted sub-arrays.
     * First is a[l,...,m].  Second is a[m+1,...,r]
     * @param a Array, which will be modified.
     * @param l Left index.
     * @param m Middle index.
     * @param r Right index, inclusive.
     */
    public static void merge(int[] a, int l, int m, int r) {
        // Create tmp arrays
        int[] a1 = copySubArray(a, l, m);
        int[] a2 = copySubArray(a, m+1, r);

        int i = 0, j = 0, k = l;
        while (i < a1.length && j < a2.length) {
            if (a1[i] < a2[j]) {
                a[k++] = a1[i++];
            }
            else {
                a[k++] = a2[j++];
            }
        }

        // Handle remaining in a1
        while (i < a1.length) {
            a[k++] = a1[i++];
        }

        // Handle remaining in a2
        while (j < a2.length) {
            a[k++] = a2[j++];
        }
    }

    /**
     * Merge sort a sub array a[l,...,r]
     * @param a Array to be sorted.
     * @param l Left index, inclusive.
     * @param r Right index, inclusive.
     */
    public static void sort(int[] a, int l, int r) {
        // Termination condition
        if (l >= r) {
            return;
        }
        // Sort left & right
        int m = (l + r) / 2;  // middle index
        sort(a, l, m);
        sort(a, m+1, r);
        // Merge sorted left and right
        merge(a, l, m, r);
    }

    /**
     * Merge sort an array.
     * @param a Array to be sorted.
     */
    public static void sort(int[] a) {
        sort(a, 0, a.length-1);
    }

    /**
     * The main function.
     * @param args
     */
    public static void main(String[] args) {
        // Test data
        int[][] data = {
                {3, 2, 1, 5, 6, 4},
                {4, 1, 3, 6, 2, 5},
                {6, 5, 4, 3, 2, 1},
                {1, 2, 3, 4, 5, 6},
        };

        for (int[] a: data) {
            int[] r = a.clone();
            System.out.println("# Sorting " + Arrays.toString(a));
            MergeSort.sort(r);
            System.out.println("  => " + Arrays.toString(r));
        }
    }
}
