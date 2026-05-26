class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                return True

        return False