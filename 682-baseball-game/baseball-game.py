class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []

        for n in operations:
            if n == 'C':
                st.pop()
            elif n == 'D':
                st.append(st[-1] * 2 )
            elif n == '+':
                st.append(st[-1] + st[-2])
            else :
                st.append(int(n))
            
        return sum(st)
