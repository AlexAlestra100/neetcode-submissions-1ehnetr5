# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res = []
#         nums.sort()

#         def dfs(i, numset, s):
#             if s == target:
#                 res.append(list(numset))
#                 return

#             for j in range(i, len(nums)):
#                 if s + nums[j] > target:
#                     return

#                 s += nums[j]
#                 numset.append(nums[j])
#                 dfs(j, numset, s)

#                 s -= nums[j]
#                 numset.pop()

#         dfs(0, [], 0)
#         return res

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, numset, total):
            if total == target:
                res.append(list(numset))
                return
            elif i >= len(nums) or total > target:
                return

            total += nums[i]
            numset.append(nums[i])
            dfs(i, numset, total)

            total -= nums[i]
            numset.pop()
            dfs(i + 1, numset, total)


        dfs(0, [], 0)

        return res