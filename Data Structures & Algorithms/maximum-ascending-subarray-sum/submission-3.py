class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s = m = 0
        for i, n in enumerate(nums):
            if i > 0 and n <= nums[i - 1]:
                    m = max(m, s)
                    s = 0
            s += n
        
        m = max(m, s)

        return m