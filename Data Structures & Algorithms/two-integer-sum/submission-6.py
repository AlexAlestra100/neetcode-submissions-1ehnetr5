class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        box = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in box:
                return [box[diff], i]
            box[num] = i