class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0

        stack = []

        for i, h in enumerate(heights):
            curr = [i, h]
            while stack and stack[-1][1] > h:
                pI, pH = stack.pop()
                w = i - pI
                res = max(res, w * pH)
                if h != 0:
                    curr[0] = pI
            stack.append(curr)

        while stack:
            pI, pH = stack.pop()
            print(pI, pH)
            w = len(heights) - pI
            res = max(res, w * pH)

        return res