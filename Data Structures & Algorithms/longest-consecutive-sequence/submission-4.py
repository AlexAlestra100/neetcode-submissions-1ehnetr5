class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        numSet = set(nums)

        for num in nums:
            length = 1
            curr = num
            if curr - 1 not in numSet:
                while curr + 1 in numSet:
                    length += 1
                    curr += 1

                longest = max(length, longest)
        
        return longest