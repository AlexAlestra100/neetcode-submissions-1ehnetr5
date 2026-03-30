class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = post = 1

        for n in range(len(nums)):
            if n == 0:
                res[n] = pre
                pre *= nums[n]
            else:
                res[n] = pre
                pre *= nums[n]
            
        for rN in range(len(nums) - 1, -1, -1):
            res[rN] *= post
            post *= nums[rN]

        return res