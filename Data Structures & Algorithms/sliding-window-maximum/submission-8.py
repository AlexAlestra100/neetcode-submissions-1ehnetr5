class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxList = []

        l = 0
        r = k

        while r <= len(nums):
            temp = nums[l : r]
            print(temp)
            tempMax = max(temp)
            print(tempMax)
            maxList.append(tempMax)
            print()

            l += 1
            r += 1

        return maxList