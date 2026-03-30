class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sNums = set(nums)

        return len(sNums) != len(nums)