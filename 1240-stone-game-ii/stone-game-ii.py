class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp[i][M] = maximum stones the current player can get
        # starting from index i with M
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):

                # Can take all remaining piles
                if i + 2 * M >= n:
                    dp[i][M] = suffix[i]
                    continue

                best = 0

                # Try taking X piles
                for X in range(1, 2 * M + 1):
                    if i + X > n:
                        break

                    next_M = max(M, X)

                    # Opponent's maximum stones
                    opponent = dp[i + X][next_M]

                    # We get everything except what opponent gets
                    current = suffix[i] - opponent

                    best = max(best, current)

                dp[i][M] = best

        return dp[0][1]