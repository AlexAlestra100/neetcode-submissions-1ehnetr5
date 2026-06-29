class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        t = None

        for n in nums:
            currT = True if n % 2 == 0 else False

            if t != currT:
                t = currT
            else:
                return False

        return True