class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = ((r - l) // 2) + l

            if nums[l] < nums[m] and nums[m] < nums[r] or nums[l] > nums[m] and nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1

            res = min(res, nums[m])

        return res