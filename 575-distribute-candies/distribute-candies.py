class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        a = len(set(candyType))
        b = min(a, len(candyType)//2)
        return b
        