from bisect import bisect_left, bisect_right


class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)

        if n <= 1:
            return 0

        # Prefix sums
        prefix = [0] * (n + 1)
        for i, x in enumerate(stoneValue):
            prefix[i + 1] = prefix[i] + x

        # dp[i][j] = best score for interval [i, j]
        dp = [[0] * n for _ in range(n)]

        # left_max[i][j] =
        # max(dp[i][k] + prefix[k+1]) for i <= k <= j
        left_max = [[0] * n for _ in range(n)]

        # right_max[i][j] =
        # max(dp[k][j] - prefix[k]) for i <= k <= j
        right_max = [[0] * n for _ in range(n)]

        # Base cases: one stone -> score 0
        for i in range(n):
            left_max[i][i] = prefix[i + 1]
            right_max[i][i] = -prefix[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                total = prefix[j + 1] - prefix[i]

                # Find the largest split where:
                # left_sum <= right_sum
                #
                # prefix[k+1] - prefix[i] <= total / 2
                limit = (2 * prefix[i] + total) // 2

                pos = bisect_right(
                    prefix,
                    limit,
                    i + 1,
                    j + 1
                )

                # pos is an insertion position, so the last valid
                # split point is pos - 2.
                k = min(pos - 1, j) - 1

                if k >= i:
                    dp[i][j] = left_max[i][k] - prefix[i]

                # Find the first split where:
                # right_sum <= left_sum
                #
                # prefix[k+1] - prefix[i] >= total / 2
                limit = (2 * prefix[i] + total + 1) // 2

                pos = bisect_left(
                    prefix,
                    limit,
                    i + 1,
                    j + 1
                )

                if pos <= j:
                    dp[i][j] = max(
                        dp[i][j],
                        right_max[pos][j] + prefix[j + 1]
                    )

                # Update range maxima
                left_max[i][j] = max(
                    left_max[i][j - 1],
                    dp[i][j] + prefix[j + 1]
                )

                right_max[i][j] = max(
                    right_max[i + 1][j],
                    dp[i][j] - prefix[i]
                )

        return dp[0][n - 1]