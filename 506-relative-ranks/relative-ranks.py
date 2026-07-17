class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if not score: return 0
        res = []
        b = {value: index for index, value in enumerate(sorted(score, reverse=True))}
        for i in score:
            if b[i]  == 0:
                res.append("Gold Medal")
            elif b[i] == 1:
                res.append("Silver Medal")
            elif b[i] == 2:
                res.append("Bronze Medal")
            else:
                res.append(f"{b[i]+1}")
        return res