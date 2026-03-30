class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            print(stack)
            if t == '+':
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            elif t == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif t == '*':
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            elif t == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(float(a) / b))
            else:
                stack.append(int(t))

        return stack[0]