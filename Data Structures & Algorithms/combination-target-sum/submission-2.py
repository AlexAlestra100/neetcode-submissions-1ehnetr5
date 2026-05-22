# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res = []
#         nums.sort()

#         def dfs(i, s):
#             if i >= len(nums) or s > target:
#                 return

#             for j in range(i, len(nums)):
#                 if nums[j] > target:
#                     return

                

#                 dfs(i + 1, s)

#         dfs(0, 0)
#         return res
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, numset, s):
            if s == target:
                res.append(list(numset))
                return
            elif i >= len(nums) or s > target:
                return

            s += nums[i]
            numset.append(nums[i])
            dfs(i, numset, s)

            s -= nums[i]
            numset.pop()
            dfs(i + 1, numset, s)

        dfs(0, [], 0)

        return res