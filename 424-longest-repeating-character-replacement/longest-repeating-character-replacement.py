class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        count = {}
        max_w = 0 
        n = len(s)

        for r in range(n):
            count[s[r]] = 1 + count.get(s[r],0)

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1 
                l +=1 
            
            max_w = max((r-l+1),max_w)

        return max_w