class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pMap = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in pMap and stack and stack[-1] == pMap[c]:
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0