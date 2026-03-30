class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = ((r - l) // 2) + l
            mVal = nums[m]

            if mVal < target:
                l = m + 1
            elif mVal > target:
                r = m - 1
            else:
                return m

        return -1