class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = {}
        l = 0 
        max_w = 0 

        for r in range(n):
            count[s[r]] = 1 + count.get(s[r],0)

            while (r-l+1) - max(count.values()) > k :
                count[s[l]] -=1 
                l += 1 
            
            max_w = max(max_w, (r-l+1))
        
        return max_w