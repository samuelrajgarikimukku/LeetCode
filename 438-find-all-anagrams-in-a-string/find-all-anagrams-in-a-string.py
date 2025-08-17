class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return [] 
            
        counT, window = {}, {}
        l = 0
        result = []
        for i in range(len(p)):
            counT[p[i]] = 1 + counT.get(p[i],0)
            window[s[i]] = 1 + window.get(s[i],0)

        if counT == window:
            result.append(l)
        
        for r in range(len(p),len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            window[s[l]] -= 1 
        
            if window[s[l]] == 0:
                window.pop(s[l])
            l += 1 

            if window == counT :
                result.append(l)
        
        return result