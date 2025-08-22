class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []

        for c in s:
            if c == '(':
                st.append(0)
            else:
                if st[-1] == 0:
                    st.pop()
                    st.append(1)
                else:
                    temp = 0 
                    while st[-1] != 0:
                        temp += st.pop()
                    st.pop()
                    st.append(2*temp)
        return sum(st)