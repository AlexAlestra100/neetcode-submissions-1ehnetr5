class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            if num - 1 not in nums:
                longest = 1
                nextL = num + 1
                while nextL in nums:
                    longest += 1
                    nextL += 1

                res = max(longest, res)


        return res