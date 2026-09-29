from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # Every path contains exactly m + n - 1 characters.
        # A valid parentheses string has even length.
        if (m + n - 1) % 2 == 1:
            return False

        # prev[j] = possible balances at cell (i - 1, j)
        prev = [set() for _ in range(n)]

        for i in range(m):
            curr = [set() for _ in range(n)]

            for j in range(n):
                # Starting cell
                if i == 0 and j == 0:
                    if grid[i][j] == '(':
                        curr[j].add(1)
                    continue

                # Get balances from the two possible previous cells.
                possible = set()

                if i > 0:
                    possible.update(prev[j])      # from above

                if j > 0:
                    possible.update(curr[j - 1])  # from left

                change = 1 if grid[i][j] == '(' else -1

                # Number of cells remaining after this cell.
                remaining = (m - 1 - i) + (n - 1 - j)

                for balance in possible:
                    new_balance = balance + change

                    # A valid parentheses string can never
                    # have a negative prefix balance.
                    if new_balance < 0:
                        continue

                    # Not enough cells remain to close all
                    # currently open parentheses.
                    if new_balance > remaining:
                        continue

                    curr[j].add(new_balance)

            prev = curr

        return 0 in prev[n - 1]