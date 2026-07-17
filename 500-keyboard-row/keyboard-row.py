class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = 'qwertyuiop'
        b = 'asdfghjkl'
        c = 'zxcvbnm'
        res = []
        for i in words:
            if all(ch in a for ch in i.lower()):
                res.append(i)
            elif all(ch in c for ch in i.lower()):
                res.append(i)
            elif all(ch in b for ch in i.lower()):
                res.append(i)
        return res