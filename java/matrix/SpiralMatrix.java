package matrix;
/**
 * Given a matrix of m x n elements (m rows, n columns),
 * return all elements of the matrix in spiral order.
 *
 * For example,
 *   Input = {{1, 2, 3}, {8, 9, 4}, {7, 6, 5}}
 *   Return = {1, 2, 3, 4, 5, 6, 7, 8, 9}
 *
 * Technologies:
 * - Arrays.deepToString()
 * - Enum
 *
 * Reference:
 * - https://www.programcreek.com/2013/01/leetcode-spiral-matrix-java/
 */

import java.util.Arrays;
import java.util.ArrayList;

public class SpiralMatrix {

    /**
     * Use a Enum to track the direction.
     */
    public enum Direction {
        RIGHT(0),
        BOTTOM(1),
        LEFT(2),
        TOP(3);

        private final int id;
        Direction(int id) {
            this.id = id;
        }

        /**
         * Move to the next direction, following their id values.
         * @return Next Direction enum.
         */
        public Direction next() {
            return values()[(this.id + 1) % 4];
        }
    }

    public static ArrayList<Integer> spiral(int[][] matrix) {

        ArrayList<Integer> result = new ArrayList<>();

        if(matrix==null||matrix.length==0||matrix[0].length==0)
            return result;

        int num_rows = matrix.length;
        int num_cols = matrix[0].length;

        // The boundary indexes
        int left = 0;
        int right = num_cols - 1;
        int top = 0;
        int bottom = num_rows - 1;

        // Track the direction. 0:right, 1:bottom, 2:left, 3:top
        Direction direction = Direction.RIGHT;

        while (result.size() < num_rows*num_cols) {
            // On the top, moving toward the right
            if (direction == Direction.RIGHT) {
                for (int j = left; j <= right; j++) {
                    result.add(matrix[top][j]);
                }
                top++;
            }
            // On the right, moving toward the bottom
            else if (direction == Direction.BOTTOM) {
                for (int i = top; i <= bottom; i++) {
                    result.add(matrix[i][right]);
                }
                right--;
            }
            // On the bottom, moving toward the left
            else if (direction == Direction.LEFT) {
                for (int j = right; j >= left; j--) {
                    result.add(matrix[bottom][j]);
                }
                bottom--;
            }
            // On the left, moving toward the top
            else if (direction == Direction.TOP) {
                for (int i = bottom; i >= top; i--) {
                    result.add(matrix[i][left]);
                }
                left++;
            }
            direction = direction.next();
        }
        return result;
    }

    /**
     * Test that we can move from one direction to the next in
     * the expected order.
     */
    public static void direction_test() {
        System.out.println("\n# Direction test:");
        for (Direction dir : Direction.values()) {
            System.out.format("- %s => %s\n", dir, dir.next());
        }
    }

    /**
     * Spiral matrix test function.
     */
    public static void spiral_test() {
        // Test data
        int[][][] test_data = {
                {{1, 2, 3}, {8, 9, 4}, {7, 6, 5}},
                {{1,2,3,4}, {12,13,14,5}, {11,16,15,6}, {10,9,8,7}},
        };

        // Run
        for (int[][] m : test_data) {
            System.out.println("\n# Input = " + Arrays.deepToString(m));
            System.out.println("Spiral => " + spiral(m));
        }
    }

    public static void main(String[] args) {
        direction_test();
        spiral_test();
    }
}
