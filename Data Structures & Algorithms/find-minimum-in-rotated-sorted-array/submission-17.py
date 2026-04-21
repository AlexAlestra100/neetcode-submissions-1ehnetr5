class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            m = ((r - l) // 2) + l

            print(nums[l], nums[m], nums[r])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

            res = min(res, nums[m])

        return res