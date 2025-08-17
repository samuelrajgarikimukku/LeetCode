class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', ']':'[','}':'{'}
        st = []

        for c in s:
            if c not in hashmap:
                st.append(c)
            else:
                if st == []:
                    return False
                else:
                    popped = st.pop()
                    if popped != hashmap[c]:
                        return False 
        return not st 

        