class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hMap = {}

        for n in nums:
            if n in hMap:
                return True
            
            hMap[n] = hMap.get(n, 0) + 1

        return False