class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}

        for num in nums:
            hMap[num] = hMap.get(num, 0) + 1
        
        sortedMap = list(sorted(hMap, key=hMap.get, reverse=True))
        res = []

        for key in sortedMap:
            if k == 0:
                return res
            res.append(key)
            k -= 1

        return res