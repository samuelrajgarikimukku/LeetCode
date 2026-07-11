class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min(strs,key=len)
        word = ""

        for i in range(len(n)):
            for s in strs:
                if s[i] != n[i]:
                    return word
            word += n[i]
        return word



        
        