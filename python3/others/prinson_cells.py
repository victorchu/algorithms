#!/usr/bin/env python3
"""
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

    If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
    Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

 

EXAMPLES:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]


REFERENCE:
  - https://leetcode.com/problems/prison-cells-after-n-days/ (Medium)

"""

from typing import List


class Solution:
    def prisonAfterNDays_v1(self, cells: List[int], N: int) -> List[int]:
        """Use arrays."""
        num_cells = len(cells)
        working_cells = [
            cells.copy(),
            [0] * num_cells
        ]
        for i in range(1, N+1):
            curr_idx = i % 2
            curr_cells = working_cells[curr_idx]
            prev_cells = working_cells[1 - curr_idx]
            curr_cells[0] = curr_cells[-1] = 0
            for j in range(1, num_cells-1):
                curr_cells[j] = 1 if prev_cells[j-1] == prev_cells[j+1] else 0

        curr_idx = N % 2
        return working_cells[curr_idx]

    def prisonAfterNDays_v2(self, cells: List[int], N: int) -> List[int]:
        """Use bitwise operations and check for cycles."""
        def encode(cells):
            x = 0
            for c in cells:
                x = (x << 1) | c
            return x
            
        def decode(x):
            #return [int(c) for c in bin(x)[2:].zfill(8)]
            s = '{:08b}'.format(x)
            return [int(c) for c in s[-8:]]

        if N <= 0:
            return cells
        
        x = encode(cells)
        seq = [x]
        xmap = {x: 0}

        for i in range(1, N+1):
            xL = x << 1
            xR = x >> 1
            x = ~ (xL ^ xR) & 0b01111110

            if x in xmap:
                i0 = xmap[x]
                period = i - i0
                iN = i0 + (N - i0) % period
                x = seq[iN]
                print("[DEBUG] Found cycle from {} to {}".format(i0, i))
                break
            else:
                seq.append(x)
                xmap[x] = i

        return decode(x)

    def prisonAfterNDays_v3(self, cells: List[int], N: int) -> List[int]:
        """Use different encode and decode functions."""
        def encode(cells):
            x = 0
            for c in cells:
                x <<= 1
                if c == 1:
                    x |= 0b1
            return x
            

def main():
    test_data = [
        [[0,1,0,1,1,0,0,1], 7], # exp: [0,0,1,1,0,0,0,0]
        [[0,0,1,1,1,1,0,0], 8], # exp: [0,0,0,1,1,0,0,0]
        [[0,1,0,1,1,0,0,1], 1000000000],
    ]

    sol = Solution()
    for cells, N in test_data:
        print("# Input: {}, N={} ".format(cells, N))
        if N < 100:
            print("  Output v1: {}".format(sol.prisonAfterNDays_v1(cells, N)))
        print("  Output v2: {}".format(sol.prisonAfterNDays_v2(cells, N)))


if __name__ == "__main__":
    main()
