class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i != "]":
                stack.append(i)
            else:
                st = ""
                while stack[-1] != '[':
                    st = stack.pop()  + st
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*st)
        return ''.join(stack)