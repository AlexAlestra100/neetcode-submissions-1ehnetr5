class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            res = c
            if c == '+':
                b = int(stack.pop())
                a = int(stack.pop())
                res = a + b

            elif c == '-':
                b = int(stack.pop())
                a = int(stack.pop())
                res = a - b

            elif c == '*':
                b = int(stack.pop())
                a = int(stack.pop())
                res = a * b

            elif c == '/':
                b = int(stack.pop())
                a = int(stack.pop())
                res = math.trunc(a / b)

            stack.append(res)

        return int(stack[0])