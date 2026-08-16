class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        c0, c1, c2 = count

        if c0 % 2 == 0:
            # Alice needs at least one stone of each
            # non-zero remainder.
            return c1 > 0 and c2 > 0

        # With an odd number of 0-mod-3 stones,
        # Alice wins only if the two groups differ by > 2.
        return abs(c1 - c2) > 2