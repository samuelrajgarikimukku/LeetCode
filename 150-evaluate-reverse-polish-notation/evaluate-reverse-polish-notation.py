class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []

        for i in range(n):
            if tokens[i] == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif tokens[i] == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif tokens[i] == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            elif tokens[i] == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(tokens[i]))
            
        return stack[0]