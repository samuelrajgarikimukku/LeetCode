class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        b = dict()
        l = 0
        max_len = 0
        for r in range(len(s)):
            if s[r] in b:
                b[s[r]] += 1 
            else:
                b[s[r]] = 1
            while max(b.values()) > 2:
                b[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len

        