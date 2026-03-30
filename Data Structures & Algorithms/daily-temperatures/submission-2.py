class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for i, t in enumerate(temperatures):
            print('stack:', stack)
            print('Current:', i, t)
            while stack and stack[-1][1] < t:
                prevI, prevT = stack.pop()
                print(prevI, prevT)

                res[prevI] = i - prevI

            stack.append([i, t])

        return res