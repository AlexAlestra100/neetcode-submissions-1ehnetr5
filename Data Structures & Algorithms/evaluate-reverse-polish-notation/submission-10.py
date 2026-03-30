class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            print(stack)
            print(token)
            if token.isdigit() or len(token) >= 2:
                print('added to stack')
                stack.append(int(token))
            else:
                print('operation')
                if token == '+':
                    print('+')
                    b = stack.pop()
                    a = stack.pop()
                    print(a, b)

                    stack.append(a + b)

                elif token == '-':
                    print('-')
                    b = stack.pop()
                    a = stack.pop()
                    print(a, b)

                    stack.append(a - b)

                elif token == '*':
                    print('*')
                    b = stack.pop()
                    a = stack.pop()
                    print(a, b)

                    stack.append(a * b)

                elif token == '/':
                    print('/')
                    b = stack.pop()
                    a = stack.pop()
                    print(a, b)

                    stack.append(int(a / b))

        return stack[0]