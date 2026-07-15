class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        r = l = ch = 0
        while r < len(s) and l < len(g):
            if g[l] <= s[r]:
                ch += 1
                l += 1
            r += 1
        return ch


