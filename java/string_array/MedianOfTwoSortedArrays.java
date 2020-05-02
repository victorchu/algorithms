/*
There are 2 sorted arrays A and B of size n each. Write an algorithm
to find the median of the array obtained after merging the above 2
arrays(i.e. array of length 2n). The complexity should be O(log(n)).

Example:

Input:  ar1 = [1, 12, 15, 26, 38]
        ar2 = [2, 13, 17, 30, 45]
Output: 16

Key functions:
  . np.mean(array)
  . np.median(array)
  . // : integer division
  . %  : mod

Ref:
  . https://www.geeksforgeeks.org/median-of-two-sorted-arrays/
*/

import java.util.Arrays;

class MedianOfTwoSortedArrays
{
    /* Constructor */
    public MedianOfTwoSortedArrays() {
    }

    /*
    Method 1 - merge two arrays.
    */
    public double method1(int[] a1, int[] a2) {
        System.out.println("# Method 1:");
        int n = a1.length;
        double median = 0;

        for (int i = 0, j = 0, k = 0; k <= n; ++k) {
            int x;
            if (i < n & j < n) {
                if (a1[i]  < a2[j]) {
                    x = a1[i];
                    i += 1;
                }
                else {
                    x = a2[j];
                    j += 1;
                }
            }
            else if (i < n) {
                x = a1[i];
                i += 1;
            }
            else {
                x = a2[j];
                j += 1;
            }
            System.out.format("[DEBUG] i = %d, j = %d, k = %d, x = %d\n", i, j, k, x);
            if (k >= n - 1) {
                System.out.println("[DEBUG] Appending median " + x);
                median += x;
            }
        }
        median /= 2.0;
        System.out.println("=> Median = " + median);
        return median;
    }

    /*
    Method 2 - 
	Compare the medians of the two arrays and remove irrelevant parts.

    The key concept is that the median is the 'middle' value.
    Given two medians m1 and m2 from two arrays.
    If m1 < m2, then the first half of array 1 and 2nd half of the
    array 2 can be safely removed.

    E.g.
       1. [1, 12, 15, 16, 26, 38] (15.5) & [2, 13, 16, 17, 30, 45] (16.5)
       2. [16, 26, 38] (26) & [2, 13, 16] (13)
       3. [16, 26] (21) & [13, 16] (14.5)
       4. [16] & [16]

    Complexity is O(log(n)).
    */
    public double method2(int[] a1, int[] a2) {
        double median = 0;

        System.out.println("# Method 2:");
        int n = a1.length;
        median = method2_helper(a1, 0, n, a2, 0, n);
        System.out.println("=> Median = " + median);
        return median;
    }

	public double method2_helper(int[] a1, int i0, int i1, int[] a2, int j0, int j1) {

        // Termination condition
		int n = i1 - i0;
		if (n == 1) {
			System.out.format("[DEBUG] Terminating with [%d], [%d]\n", a1[i0], a2[j0]);
			double m = (a1[i0] + a2[j0]) / 2.0;
			return m;
		}
        // Get the medians
        double m1 = getMedian(a1, i0, i1);
        double m2 = getMedian(a2, j0, j1);
        System.out.format("[DEBUG] comparing %s (%.1f) with %s (%.1f)\n",
            Arrays.toString(Arrays.copyOfRange(a1, i0, i1)), m1,
            Arrays.toString(Arrays.copyOfRange(a2, j0, j1)), m2);

        if (m1 == m2) {
            return m1;
        }
        else {
            int k = (int)(n / 2);
            if (n % 2 != 0) {
                k += 1;
            }
            if (m1 > m2) {
                return method2_helper(a1, i0, i0 + k, a2, j1 - k, j1);
            }
            else {
                return method2_helper(a1, i1 - k, i1, a2, j0, j0 + k);
            }
        }
	}

	/* get the median of the specified array.
	   i0 : begin index of the array.
	   i1 : end index of the array.
	   Note: i1 - i0 = the length of the array.
	*/
	public double getMedian(int[] a, int i0, int i1) {
		double retval;
		int n = (i1 - i0);
		if (n % 2 == 0) {
			int k = i0 + (int)(n / 2) - 1;
			retval = (a[k] + a[k+1]) / 2.0;
		}
		else {
			int k = i0 + (int)(n / 2);
			retval = a[k];
		}
		return retval;
	}


    /* Main */
    public static void main(String[] args)
    {
        MedianOfTwoSortedArrays m = new MedianOfTwoSortedArrays();

        // Testing data
        int[][] a1s ={
            {1, 12, 15, 26, 38},
            {1, 12, 15, 16, 26, 38},
            {1, 12, 16, 26, 38},
            {1, 2, 12, 13, 15},
        };
        int[][] a2s = {
            {2, 13, 17, 30, 45},
            {2, 13, 16, 17, 30, 45},
            {2, 13, 16, 30, 45},
            {17, 26, 30, 38, 45},
        };
        // Try two different methods
        for (int i = 0; i < a1s.length; ++i) {
            int[] a1 = a1s[i];
            int[] a2 = a2s[i];
            System.out.format("\n### Testing %s and %s\n", Arrays.toString(a1), Arrays.toString(a2));
            m.method1(a1, a2);
            m.method2(a1, a2);
        }
    }

}


