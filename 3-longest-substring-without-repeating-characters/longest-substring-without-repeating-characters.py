class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 
        l = 0 
        sett = set()

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1 

            w = (r - l) + 1 
            longest = max(longest, w)
            sett.add(s[r])
            
        return longest