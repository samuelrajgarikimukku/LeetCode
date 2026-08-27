class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = []

        for i in range(len(s)):
            distance = float('inf')
            for j in range(len(s)):
                if s[j] == c:
                    distance = min(distance, abs(i-j))
            res.append(distance)
            
        return res
        