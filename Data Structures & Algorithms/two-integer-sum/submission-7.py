class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashS = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashS:
                return [hashS[diff], i]
            hashS[num] = i