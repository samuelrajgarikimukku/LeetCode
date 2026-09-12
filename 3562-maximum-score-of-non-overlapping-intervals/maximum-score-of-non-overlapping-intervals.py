from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # [left, right, weight, original_index]
        arr = [
            [l, r, w, i]
            for i, (l, r, w) in enumerate(intervals)
        ]

        # Sort by starting position
        arr.sort()

        starts = [x[0] for x in arr]

        # next[i] = first interval whose left > arr[i].right
        nxt = [0] * n
        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        # dp[i][k] = best result using intervals from i onward,
        # choosing at most k intervals.
        #
        # Store (score, tuple(indices)).
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        def better(a, b):
            # Higher score is better.
            # If scores are equal, lexicographically smaller indices are better.
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            return a if a[1] < b[1] else b

        for i in range(n - 1, -1, -1):
            for k in range(1, 5):
                # Skip this interval
                skip = dp[i + 1][k]

                # Take this interval
                j = nxt[i]
                score = arr[i][2]
                indices = (arr[i][3],)

                if j <= n:
                    score += dp[j][k - 1][0]
                    indices += dp[j][k - 1][1]

                take = (score, tuple(sorted(indices)))

                dp[i][k] = better(skip, take)

        return list(dp[0][4][1])