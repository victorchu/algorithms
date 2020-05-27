#!/usr/bin/env python3
"""
Given a dictionary, and two words ‘start’ and ‘target’ (both of same length).
Find length of the 'smallest' chain from ‘start’ to ‘target’ if it exists,
such that adjacent words in the chain only differ by one character and
each word in the chain is a valid word i.e., it exists in the dictionary.
It may be assumed that the ‘target’ word exists in dictionary and
length of all dictionary words is same.

Example:

Input:  dictionary = {POON, PLEE, SAME, POIE, PLEA, PLIE, POIN}
        start = TOON
        target = PLEA
Output: 7
Explanation: TOON - POON - POIN - POIE - PLIE - PLEE - PLEA

Key functions:
  - list.append(): append to the end of the list.
  - list.pop(): pop the first element from the list (queue)
  - set.add()
  - zip(word1, word2): character pair iterator.

Ref:
  - https://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/
  - https://www.programcreek.com/2012/12/leetcode-word-ladder/
"""


def distance(w1, w2):
    """Return the distance of two words (of the same length)."""
    n = 0
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            n += 1
    return n


def find(start, target, valid_words):
    """Perform a Bread-First Search (BFS) to guarantee the optimal solution.

    Complexity is O(n^2 m), where n is the number of words in the dictionary
    and m is the length of the word.
    The worst case, each word in the dictionary needs to check with each other.
    Thus, O(n^2).  The cost to get the distance of two words is m.

    :param start: start word
    :param target: target word
    :param valid_words: list of valid words (dictionary)
    :return: n, path
    """
    # Make sure that target is in the dictionary
    word_set = set(valid_words + [target])

    # Use a queue to support a width-first search
    # Each element in the queue is a potential path.
    queue = [[start]]
    visit_set = set([start])
    path = list()

    print("find({}, {}) in {}".format(start, target, valid_words))
    while queue and not path:
        # Get the first element (history) from the queu
        h = queue.pop()
        curr = h[-1]    # the last word in the history (search path)

        # Find the next candidate
        for w in word_set:
            # The word cannot be in the visit set
            # Alternatively, we can iterate through (word_set - visit_set).
            # Or, we can keep removing elements from the word_set.
            if w in visit_set:
                continue

            # Found a new candidate
            if distance(curr, w) == 1:
                # Update the history; need to make a copy
                new_hist = h.copy() + [w]
                # Check if we have found the target
                if (w == target):
                    path = new_hist
                    break
                else:
                    print(" + {}".format(new_hist))
                    queue.append(new_hist)
                    visit_set.add(w)
    n = len(path)
    print("===> {}, {}".format(n, path))


def main():
    d1 = ['POON', 'PLEE', 'SAME', 'POIE', 'PLEA', 'PLIE', 'POIN']
    find('TOON', 'PLEA', d1)
    find('TOON', 'PLIE', d1)
    find('POON', 'PLEA', d1)
    find('SAMI', 'PLEA', d1)

    d2 = ['hot', 'dot', 'dog', 'lot', 'log']
    find('hit', 'cog', d2)
    find('hit', 'dog', d2)


if __name__ == "__main__":
    main()
