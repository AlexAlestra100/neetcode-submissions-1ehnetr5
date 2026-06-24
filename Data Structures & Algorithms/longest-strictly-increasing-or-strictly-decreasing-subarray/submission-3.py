class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        m = 0

        inc = 0
        dec = 0

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] < nums[i]:
                inc += 1
                dec = 1
            elif i > 0 and nums[i - 1] > nums[i]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1

            m = max(m, inc, dec)

        return m