class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        count = Counter(stones)
        for i in jewels :
            result += count.get(i,0)
        return result
