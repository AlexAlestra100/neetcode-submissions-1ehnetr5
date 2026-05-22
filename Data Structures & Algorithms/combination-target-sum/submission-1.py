class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, numset, s):
            if i >= len(nums) and s == target and numset not in res:
                res.append(list(numset))
                return
            elif i >= len(nums) or s > target:
                return

            s += nums[i]
            numset.append(nums[i])
            dfs(i, numset, s)
            dfs(i + 1, numset, s)

            s -= nums[i]
            numset.pop()
            dfs(i + 1, numset, s)

        dfs(0, [], 0)

        return res