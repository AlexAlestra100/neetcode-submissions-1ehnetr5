class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        numSet = set(nums)

        for num in nums:
            length = 1
            if num - length not in numSet:
                while num + length in numSet:
                    length += 1

                longest = max(length, longest)
        
        return longest