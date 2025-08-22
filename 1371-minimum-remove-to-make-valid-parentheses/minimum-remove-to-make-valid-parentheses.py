class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        cnt = 0

        for i in s :
            if i == "(":
                cnt += 1 
                st.append(i)
            elif i == ")" and cnt > 0:
                cnt -= 1 
                st.append(i)
            elif i != ")":
                st.append(i)
        
        result = []
        for i in st[::-1]:
            if i == "(" and cnt > 0:
                cnt -= 1 
            else:
                result.append(i)
        return "".join(result[::-1])