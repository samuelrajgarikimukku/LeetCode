class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" :return ""

        counT, window = {}, {}

        for c in t :
            counT[c] = 1+ counT.get(c,0)

        have, need = 0, len(counT)
        result, resultlen = [-1,-1], float('inf')
        l =0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in counT and window[c] == counT[c]:
                have += 1 
            
            while have == need :
                if (r-l+1) < resultlen:
                    result = [l,r]
                    resultlen = (r-l+1)
                
                window[s[l]] -= 1 
                if s[l] in counT and window[s[l]] < counT[s[l]]:
                    have -= 1 
                l += 1 
        l,r = result
        return s[l:r+1] if resultlen != float('inf') else ""