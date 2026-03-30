class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        keys = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for c in s:
            if stack and stack[len(stack) - 1] == keys.get(c, 0):
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0