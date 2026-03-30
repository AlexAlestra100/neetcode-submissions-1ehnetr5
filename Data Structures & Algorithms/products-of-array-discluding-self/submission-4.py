class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        pre = 1

        for num in nums:
            res.append(pre)
            pre *= num

        post = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res