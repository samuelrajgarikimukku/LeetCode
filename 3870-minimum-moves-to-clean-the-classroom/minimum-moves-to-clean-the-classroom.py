from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        # Find start and number all litter cells
        litter = []
        sr = sc = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter.append((r, c))

        k = len(litter)

        if k == 0:
            return 0

        # Map litter position -> bit index
        litter_id = {
            pos: i for i, pos in enumerate(litter)
        }

        full_mask = (1 << k) - 1

        # BFS state:
        # (row, col, collected_mask, remaining_energy)
        q = deque()
        q.append((sr, sc, 0, energy))

        # best[r][c][mask] = maximum energy
        # with which we have reached this state.
        best = [
            [
                [-1] * (1 << k)
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        best[sr][sc][0] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        moves = 0

        while q:
            for _ in range(len(q)):
                r, c, mask, e = q.popleft()

                # All litter collected
                if mask == full_mask:
                    return moves

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Outside grid
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    # Obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    # Can't move with zero energy
                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        idx = litter_id[(nr, nc)]
                        nmask |= (1 << idx)

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    # Already reached this state with
                    # at least as much energy
                    if best[nr][nc][nmask] >= ne:
                        continue

                    best[nr][nc][nmask] = ne
                    q.append((nr, nc, nmask, ne))

            moves += 1

        return -1