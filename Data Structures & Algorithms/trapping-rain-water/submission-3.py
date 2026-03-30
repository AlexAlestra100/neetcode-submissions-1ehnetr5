class Solution:
    def trap(self, height: List[int]) -> int:
        maxWater = 0

        if not height:
            return maxWater

        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                maxWater += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                maxWater += maxR - height[r]

        return maxWater