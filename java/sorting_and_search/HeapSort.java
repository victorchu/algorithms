/**
 * Heap sort is a comparison based sorting technique based on Binary Heap data structure.
 * It is similar to selection sort where we first find the maximum element and place
 * the maximum element at the end. We repeat the same process for remaining element.
 *
 * Ref:
 * - https://www.geeksforgeeks.org/heap-sort/
 */
import java.util.Arrays;

public class HeapSort {
    /**
     * Max heapify an array at the specified location.
     * It is assumed that all of the children are already heapified.
     *
     * @param a Array as a heap.
     * @param n Size of the heap.
     * @param k The position to be heapified.
     */
    private static void heapify(int[] a, int n, int k) {
        int i_max = k;  // index the current maximum
        int i_left = 2 * k + 1;
        int i_right = 2 * k + 2;

        // Compare the left child with the max
        if (i_left < n && a[i_left] > a[i_max]) {
            i_max = i_left;
        }
        // Compare the right child with the max
        if (i_right < n && a[i_right] > a[i_max]) {
            i_max = i_right;
        }

        // Check if any child is the new maximum
        if (i_max != k) {
            int tmp = a[k];
            a[k] = a[i_max];
            a[i_max] = tmp;

            // Recursively heapify the sub-tree
            heapify(a, n, i_max);
        }
    }

    /**
     * Heap-sort an array.
     *
     * @param a The array to be sorted (and thus modified).
     */
    public static int[] sort(int[] a) {
        // Convert the array to a max heap
        int n = a.length;
        for (int k = n / 2; k >= 0; --k) {
            heapify(a, n, k);
        }

        // Move the head (the max) to the bottom; one at a time.
        for (int j = n - 1; j >= 0; --j) {
            int tmp = a[j];
            a[j] = a[0];
            a[0] = tmp;

            // Heapify on a reduced heap to move the next largest element
            // to the top.  Note that elements at the bottom will not be touched.
            heapify(a, j, 0);
        }
        return a;
    }

    public static void main(String[] args) {
        // Test data
        int[][] data = {
                {3, 2, 1, 5, 6, 4},
                {4, 1, 3, 6, 2, 5},
                {6, 5, 4, 3, 2, 1},
                {1, 2, 3, 4, 5, 6},
        };

        for (int[] a: data) {
            System.out.println("# Heap Sorting " + Arrays.toString(a));
            System.out.println("  => " + Arrays.toString(HeapSort.sort(a)));
        }
    }
}

