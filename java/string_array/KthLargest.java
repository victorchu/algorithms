/**
 * Find the kth largest element in an unsorted array.
 * Note that it is the kth largest element in the sorted order, not the kth distinct element.
 *
 * For example, given [3,2,1,5,6,4] and k = 2, return 5.
 *
 * Ref:
 * - https://www.programcreek.com/2014/05/leetcode-kth-largest-element-in-an-array-java/
 */

import java.util.Arrays;
import java.util.PriorityQueue;

public class KthLargest {

    /**
     * Sort the array first then find the k-th.
     * Complexity is O(n log(n)).
     *
     * @param a
     * @param k
     * @return
     */
    public int method1(int[] a, int k) {
        int[] a_sorted = a.clone();  // Clone first so as not to alter the original.
        Arrays.sort(a_sorted);
        return a_sorted[a.length - k];
    }

    /**
     * This method uses a min heap (priority queue).
     * The complexity is O(n log(k)) if we insert every element into the heap.
     * On conditional insert, it can be as low as O(k log(k))
     *
     * @param a An array
     * @param k Selection index (one based).
     * @return k-th largest element.
     */
    public int method2(int[] a, int k) {
        // Create a priority queue with an initial capacity k.
        // Elements of the queue are ordered according to their natural order,
        // or by a Comparator. Thus the smallest element is at the head.
        PriorityQueue<Integer> q = new PriorityQueue<Integer>(k);

        for (int e: a) {
            // Insert an element into the queue if it is not full.
            // Otherwise, insert if the new element is larger than the head.
            if (q.size() < k || e > q.peek()) {
                q.offer(e);
            }

            if (q.size() > k) {
                // Retrieve and remove the head (smallest) element from the queue.
                // Thus, we always keep the largest k elements in the queue.
                q.poll();
            }
        }
        // Return the head element, which is the k-th largest element.
        return q.peek();
    }

    public static void main(String[] args) {
        KthLargest obj = new KthLargest();
        int[] a = {3, 2, 1, 5, 6, 4};

        System.out.println("\n# Testing " + Arrays.toString(a));
        for (int k = 1; k <= a.length; ++k) {
            System.out.format("- method1(k=%d) = %d\n", k, obj.method1(a, k));
            System.out.format("- method2(k=%d) = %d\n", k, obj.method2(a, k));
        }
    }
}
