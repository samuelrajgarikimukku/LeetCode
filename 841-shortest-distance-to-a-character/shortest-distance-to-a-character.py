class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        res = [n] * n

        # Left -> Right
        prev = -n

        for i in range(n):
            if s[i] == c:
                prev = i

            res[i] = i - prev

        # Right -> Left
        prev = 2 * n

        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i

            res[i] = min(res[i], prev - i)

        return res