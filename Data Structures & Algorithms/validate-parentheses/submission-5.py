class Solution:
    def isValid(self, s: str) -> bool:
        sStack = []

        mapping = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        
        for c in s:
            if c in mapping:
                if sStack and sStack[-1] == mapping[c]:
                    sStack.pop()
                else:
                    return False
            else:
                sStack.append(c)

        return len(sStack) == 0