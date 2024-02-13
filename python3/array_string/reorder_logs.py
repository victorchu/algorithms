#!/usr/bin/env python3
"""
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

  - Each word after the identifier will consist only of lowercase letters, or;
  - Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.  It is
guaranteed that each log has at least one word after its identifier.

Reorder the logs so that:
  - All of the letter-logs come before any digit-log.
  - The letter-logs are ordered lexicographically ignoring identifier, with the
    identifier used in case of ties.
  - The digit-logs should be put in their original order.

Return the final order of the logs.

EXAMPLES:
  Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
  Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

REFERENCE:
  - https://leetcode.com/problems/reorder-data-in-log-files/ (Easy)

"""

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_ranking_key(log: str) -> str:
            """Return a key that can be used to sort the log records.

              - numeric: return None; no sorting needed.
              - letter: return <payload>|<identifier>
            """
            items = log.split(' ', maxsplit=2)
            if items[1].isnumeric():
                return None
            else:
                payload = ' '.join(items[1:])
                return "{}|{}".format(payload, items[0])

        # Pre-processing the logs
        numeric_logs = list()
        letter_logs = dict()
        for log in logs:
            key = get_ranking_key(log)
            if not key:
                numeric_logs.append(log)
            else:
                letter_logs[key] = log

        # Sort and combine
        output = []
        for key, log in sorted(letter_logs.items()):
            output.append(log)
        output.extend(numeric_logs)
        return output


def main():
    test_data = [
        ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
            "let2 own kit dig", "let3 art zero"],
    ]

    sol = Solution()
    for logs in test_data:
        print("# Input = {}".format(logs))
        print("  Output = {}".format(sol.reorderLogFiles(logs)))


if __name__ == "__main__":
    main()
