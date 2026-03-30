class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0

        if not heights:
            return area

        stack = []

        for i, h in enumerate(heights):
            needI = i
            while stack and stack[-1][1] > h:
                cVal = stack.pop()
                currArea = cVal[1] * (i - cVal[0])
                area = max(area, currArea)
                needI = cVal[0]

            stack.append([needI, h])

        while stack:
            val = stack.pop()
            length = len(heights) - val[0]
            area = max(area, val[1] * length)

        return area