class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr = 0
        nums.sort()

        for n in nums:
            if n != curr:
                return curr

            curr += 1

        return curr