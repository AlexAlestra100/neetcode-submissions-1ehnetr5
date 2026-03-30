class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        a = 0
        b = a

        sum = 0
        res = float('inf')

        while b < len(nums):
            sum += nums[b]

            if sum >= target:
                if len(nums[a:b + 1]) < res:
                    res = len(nums[a:b + 1])

                a += 1
                sum = 0
                b = a
            else:
                b += 1

        if res > len(nums) and sum < target:
            return 0

        return res