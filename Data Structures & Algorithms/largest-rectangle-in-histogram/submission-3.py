class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []

        for i, h in enumerate(heights):
            pair = [i, h]
            while stack and stack[-1][1] > h:
                currI, currH = stack.pop()
                width = i - currI
                area = max(area, width * currH)
                if h != 0:
                    pair[0] = currI
            stack.append(pair)

        while stack:
            currI, currH = stack.pop()
            width = len(heights) - currI
            area = max(area, width * currH)

        return area