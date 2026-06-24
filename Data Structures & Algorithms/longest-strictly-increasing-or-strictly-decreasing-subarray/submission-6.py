class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
            if not nums:
                return 0
            
            max_streak = 1
            inc = 1
            dec = 1
            
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    inc += 1
                    dec = 1
                elif nums[i] > nums[i + 1]:
                    dec += 1
                    inc = 1
                else:
                    inc = 1
                    dec = 1
                    
                max_streak = max(max_streak, inc, dec)
                
            return max_streak