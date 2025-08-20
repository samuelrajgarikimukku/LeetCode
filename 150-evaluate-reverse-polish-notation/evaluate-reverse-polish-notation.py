class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []

        for i in tokens:
            if i in "+-*/":
                b = stack.pop()
                a = stack.pop()

            if i == '+':
                stack.append(a+b)
            elif i == '-':
                stack.append(a-b)
            elif i == '*':
                stack.append(a*b)
            elif i == "/":
                stack.append(int(a/b))
            else:
                stack.append(int(i))

        return stack[0]