class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = []

        for n in nums:
            if n in dup:
                return True
            dup.append(n)

        return False