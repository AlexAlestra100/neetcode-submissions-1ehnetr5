class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxArea = 0

        while l < r:
            left = heights[l]
            right = heights[r]

            currHeight = min(left, right)
            currWidth = r - l

            currArea = currHeight * currWidth
            maxArea = max(currArea, maxArea)

            if left < right:
                l += 1
            else:
                r -= 1

        return maxArea