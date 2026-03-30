class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit() or len(token) >= 2:
                stack.append(int(token))
            else:
                if token == '+':
                    b = stack.pop()
                    a = stack.pop()

                    stack.append(a + b)

                elif token == '-':
                    b = stack.pop()
                    a = stack.pop()

                    stack.append(a - b)

                elif token == '*':
                    b = stack.pop()
                    a = stack.pop()

                    stack.append(a * b)

                elif token == '/':
                    b = stack.pop()
                    a = stack.pop()

                    stack.append(int(a / b))

        return stack[0]