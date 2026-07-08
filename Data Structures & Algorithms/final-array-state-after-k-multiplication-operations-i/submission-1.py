class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        tups = []
        for i in range(len(nums)):
            tups.append((nums[i], i))
        
        heapq.heapify(tups)
        
        while k > 0:
            v, i = heapq.heappop(tups)
            v *= multiplier
            heapq.heappush(tups, (v, i))

            k -= 1

        res = [1] * len(nums)
        for val, idx in tups:
            res[idx] = val

        return res