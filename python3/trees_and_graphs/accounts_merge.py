#!/usr/bin/env python3
"""
Given a list of accounts. Each element accounts[i] is a list of strings, where the
first element accounts[i][0] is a name, and the rest of the elements are emails
of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to
the same person if there is some email that is common to both accounts.

After merging the accounts, return the accounts in the following format:
  - The first element of each account is the name.
  - The rest of the elements are emails in sorted order.
The accounts themselves can be returned in any order.

NOTE:
  1. Name is not a unique identifier. Different accounts may share the same name.
  2. Each account is only associated with one name.

EXAMPLE:

Input: accounts = [
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["John", "johnnybravo@mail.com"],
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["Mary", "mary@mail.com"]]

Output: [
    ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
    ["John", "johnnybravo@mail.com"],
    ["Mary", "mary@mail.com"]]


TECHNIQUES:
  - dict
  - set
  - sorted

REFERNECE:
  - https://leetcode.com/problems/accounts-merge/ (Medium)
  - https://www.geeksforgeeks.org/find-same-contacts-in-a-list-of-contacts/

"""

from collections import defaultdict
from typing import List


class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """Use a dicationary to track the email to account mapping.

        This implementation bests 97.78% of python3 submissions in LeetCode.
        """
        if not accounts:
            return list()

        # The result.  Source accounts will not be modified.
        tmp_list = []
        email_map = dict()  # Maps email to tmp records index

        for a in accounts:
            match_set = set()   # indices of matched records

            # Search for existing email
            for e in a[1:]:
                if e in email_map:
                    idx = email_map[e]
                    match_set.add(idx)

            if match_set:
                match_list = sorted(match_set)
                i = match_list[0]
                rec = tmp_list[i]

                # Merge existing duplications
                for j in match_list[1:]:
                    duplicated = tmp_list[j]
                    rec[1] |= duplicated[1]  # union the emails
                    for e in duplicated[1]:  # update the email map
                        email_map[e] = i
                    duplicated.clear()      # clear the duplicated record

                # Merge the new record
                rec[1] |= set(a[1:])    # union with the existing emails
                for e in set(a[1:]):    # update the email map
                    email_map[e] = i
            else:
                # Create a new record: [name, set([emails]) ]
                rec = [a[0], set(a[1:])]
                tmp_list.append(rec)
                for e in a[1:]:
                    email_map[e] = len(tmp_list) - 1

        # Prepare final results; skip empty records
        results = [[a[0], *sorted(a[1])] for a in tmp_list if a]
        return results


# ---------------------------
#   Main & Helper Functions
# ---------------------------
def main():
    """Main function"""

    # Test data
    test_data = [
        [["John", "johnsmith@mail.com", "john00@mail.com"],
         ["John", "johnnybravo@mail.com"],
         ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
         ["Mary", "mary@mail.com"]],            # 3 accounts
        [['Alex', 'Alex5@m.co', 'Alex4@m.co', 'Alex0@m.co'],
            ['Ethan', 'Ethan3@m.co', 'Ethan3@m.co', 'Ethan0@m.co'],
            ['Kevin', 'Kevin4@m.co', 'Kevin2@m.co', 'Kevin2@m.co'],
            ['Gabe', 'Gabe0@m.co', 'Gabe3@m.co', 'Gabe2@m.co'],
            ['Gabe', 'Gabe3@m.co', 'Gabe4@m.co', 'Gabe2@m.co']],   # 4 accounts
        [["David", "David0@m.co", "David1@m.co"],
            ["David", "David3@m.co", "David4@m.co"],
            ["David", "David4@m.co", "David5@m.co"],
            ["David", "David2@m.co", "David3@m.co"],
            ["David", "David1@m.co", "David2@m.co"]]   # 1 account
    ]

    sol = Solution()
    for accounts in test_data:
        print("\n# Input: {}".format(accounts))
        print("=> Output v1 = {}".format(sol.accountsMerge(accounts)))


if __name__ == "__main__":
    main()
