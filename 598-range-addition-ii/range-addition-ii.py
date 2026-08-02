class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops: return m*n
        X,Y = inf, inf
        for x,y in ops:
            X = min(X,x)
            Y = min(Y,y)
        return X * Y

        