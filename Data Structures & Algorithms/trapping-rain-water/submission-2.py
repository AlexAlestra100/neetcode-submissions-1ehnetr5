class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        if not height:
            return res

        p1 = 0
        p2 = len(height) - 1
        p1Max = height[p1]
        p2Max = height[p2]

        while p1 < p2:
            if p1Max < p2Max:
                p1 += 1
                p1Max = max(p1Max, height[p1])
                res += p1Max - height[p1] 
            else:
                p2 -= 1
                p2Max = max(p2Max, height[p2])
                res += p2Max - height[p2] 
        return res