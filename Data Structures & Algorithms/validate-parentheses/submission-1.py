class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if stack:
                tempC = stack[-1]
                if tempC == '(' and c == ')':
                    stack.pop()
                elif tempC == '{' and c == '}':
                    stack.pop()
                elif tempC == '[' and c == ']':
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        return len(stack) == 0