class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        res = max(piles)
        r = res

        while l <= r:
            m = ((r - l) // 2) + l

            hours = 0
            for p in piles:
                hours += -(-p // m)

            if hours <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1

        return res