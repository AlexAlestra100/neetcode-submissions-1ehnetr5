class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prevTemp = stack.pop()
                res[prevTemp[0]] = i - prevTemp[0]
            stack.append([i, temp])

        return res