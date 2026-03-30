class Solution:
    def isValid(self, s: str) -> bool:
        hMap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for c in s:
            if c in hMap:
                if not stack or hMap[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0