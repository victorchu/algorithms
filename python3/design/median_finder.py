#!/usr/bin/env python3
"""
Median is the middle value in an ordered integer list. If the size of the list
is even, there is no middle value. So the median is the mean of the two middle
value.

For example,

  [2,3,4], the median is 3
  [2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

  - void addNum(int num) - Add a integer number from the data stream to the data structure.
  - double findMedian() - Return the median of all elements so far.

Example:

  addNum(1)
  addNum(2)
  findMedian() -> 1.5
  addNum(3) 
  findMedian() -> 2

Follow up:

  - If all integer numbers from the stream are between 0 and 100, how would you optimize it?
  - If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

REFERENCE:
  - https://leetcode.com/problems/find-median-from-data-stream/ (Hard)
  - https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
  - https://www.python-course.eu/python3_abstract_classes.php

"""


import heapq
from abc import ABC, abstractmethod


# -----------------
#  Median Finder
# -----------------
class MedianFinder(ABC):
    """The abstract class."""
    @abstractmethod
    def addNum(self, num: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def findMedian(self) -> float:
        raise NotImplementedError


class MedianFinder_v1(MedianFinder):
    """Use an array.  Sort as needed."""

    def __init__(self):
        self.nums = list()

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        n = len(self.nums)
        if n % 2 == 0:
            i1 = n // 2
            i0 = i1 - 1
            median = (self.nums[i0] + self.nums[i1]) / 2
        else:
            i = n // 2
            median = self.nums[i]
        return median


class MedianFinder_v2(MedianFinder):
    """Store the number in a sorted array."""

    def __init__(self):
        self.nums = list()

    def addNum(self, num: int) -> None:
        self.nums.append(num)

        # Keep the array sorted
        n = len(self.nums)
        for i in range(n-2, -1, -1):
            if self.nums[i] <= num:
                break
            self.nums[i], self.nums[i+1] = self.nums[i+1], self.nums[i]

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 0:
            i1 = n // 2
            i0 = i1 - 1
            median = (self.nums[i0] + self.nums[i1]) / 2
        else:
            i = n // 2
            median = self.nums[i]
        return median


class MedianFinder_v3(MedianFinder):
    """Two heaps.

    A max-heap to store smaller half of the input number.
    A min-heap to store the larger half of the input numbers.
    Then balance these two heaps.

    Note that heapq is a min heap. To use it as a max heap, 
    negate all of the values.

    Time complexity: O(log n) for each insertion.

    LeetCode runtime: 204 ms > 76.73%; mem 25.4 MB < 5.18%.
    """

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def _balance(self) -> None:
        """Balance heaps so that the size difference <= 1"""
        while len(self.max_heap) - len(self.min_heap) > 1:
            num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, num)

        while len(self.min_heap) - len(self.max_heap) > 1:
            num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -num)

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

    def findMedian(self) -> float:
        self._balance()
        n1 = len(self.max_heap)
        n2 = len(self.min_heap)
        if n1 == n2:
            median = (-self.max_heap[0] + self.min_heap[0]) / 2
        elif n1 > n2:
            median = -self.max_heap[0]
        else:
            median = self.min_heap[0]
        return median


class MedianFinder_v4(MedianFinder):
    """Two heaps -- custom MinHeap and MaxHeap.

    This version is more object oriented, yet can be a little bit slower.
    LeetCode runtime: 424 ms > 19.45%; mem 25.9 MB < 5.18%.
    """

    def __init__(self):
        self.max_heap = MaxHeap()
        self.min_heap = MinHeap()

    def _balance(self) -> None:
        """Balance heaps so that the size difference <= 1"""
        while len(self.max_heap) - len(self.min_heap) > 1:
            self.min_heap.heappush(self.max_heap.heappop())

        while len(self.min_heap) - len(self.max_heap) > 1:
            self.max_heap.heappush(self.min_heap.heappop())

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= self.max_heap[0]:
            self.max_heap.heappush(num)
        else:
            self.min_heap.heappush(num)

    def findMedian(self) -> float:
        self._balance()
        n1 = len(self.max_heap)
        n2 = len(self.min_heap)
        if n1 == n2:
            median = (self.max_heap[0] + self.min_heap[0]) / 2
        elif n1 > n2:
            median = self.max_heap[0]
        else:
            median = self.min_heap[0]
        return median


# -------
#  Heap
# -------
class Heap(ABC):
    @abstractmethod
    def heappush(self, x):
        raise NotImplementedError

    @abstractmethod
    def heappop(self):
        raise NotImplementedError

    @abstractmethod
    def __getitem__(self, i):
        raise NotImplementedError

    @abstractmethod
    def __len__(self):
        raise NotImplementedError


class MinHeap(Heap):
    def __init__(self):
        self.data = []

    def heappush(self, x):
        heapq.heappush(self.data, x)

    def heappop(self):
        return heapq.heappop(self.data)

    def __getitem__(self, i):
        return self.data[i]

    def __len__(self):
        return len(self.data)


class MaxHeap(MinHeap):
    class MaxObj(object):
        def __init__(self, val):
            self.val = val

        def __lt__(self, other):
            return self.val > other.val

        def __eq__(self, other):
            return self.val == other.val

    def heappush(self, x):
        heapq.heappush(self.data, MaxHeap.MaxObj(x))

    def heappop(self):
        return heapq.heappop(self.data).val

    def __getitem__(self, i):
        return self.data[i].val


# -----------------
#  Test Driver
# -----------------
def test_heaps():
    vals = [2, 3, 1]
    for obj in [MinHeap(), MaxHeap()]:
        print("# Testing {} on {}".format(type(obj).__name__, vals))
        for v in vals:
            obj.heappush(v)
        print(" - obj[0]  = {}  (len = {})".format(obj[0], len(obj)))
        while obj:
            print(" - heappop = {}  (len = {})".format(obj.heappop(), len(obj)))


def test_media_finders():
    def driver(obj, data):
        output = []
        for x in data:
            obj.addNum(x)
            output.append(obj.findMedian())
        print("  Output {} = {}".format(type(obj).__name__, output))

    test_data = [
        [2, 3, 4],
        [2, 4, 3],
        [0, 0],
    ]
    for data in test_data:
        print("# Input = {}".format(data))
        driver(MedianFinder_v1(), data)
        driver(MedianFinder_v2(), data)
        driver(MedianFinder_v3(), data)
        driver(MedianFinder_v4(), data)


def main():
    test_heaps()
    test_media_finders()


if __name__ == "__main__":
    main()
