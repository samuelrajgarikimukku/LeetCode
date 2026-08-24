class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # prefix[i] = sum of stones[0:i+1]
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # dp represents the best score difference
        # starting from the current position.
        dp = prefix[n - 1]

        # At position i, Alice/Bob can take stones[0:i+1].
        # We only need to keep the best value seen so far.
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)

        return dp