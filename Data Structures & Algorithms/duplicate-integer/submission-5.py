class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hMap = {}

        for num in nums:
            if num in hMap:
                return True
            hMap[num] = 1

        return False