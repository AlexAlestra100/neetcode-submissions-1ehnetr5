class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l = 1
        r = len(nums)

        while l <= r:
            mid = l + (r - l) // 2

            count = 0
            for num in nums:
                if num >= mid:
                    count += 1

            if count == mid:
                return mid

            if count < mid:
                r = mid - 1
            else:
                l = mid + 1

        return -1