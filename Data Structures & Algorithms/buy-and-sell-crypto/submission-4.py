class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        p1 = 0
        p2 = 1

        while p2 <= len(prices) - 1:
            lowV = prices[p1]
            highV = prices[p2]

            if lowV > highV:
                p1 = p2
            else:
                profit = highV - lowV
                res = max(res, profit)
            p2 += 1

        return res