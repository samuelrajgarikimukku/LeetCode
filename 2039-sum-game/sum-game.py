class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num) // 2

        left = num[:n]
        right = num[n:]

        diff = sum(int(c) for c in left if c != '?') \
             - sum(int(c) for c in right if c != '?')

        q1 = left.count('?')
        q2 = right.count('?')

        return diff != 9 * (q2 - q1) // 2 if (q1 - q2) % 2 == 0 else True