class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, numset, s):
            if s == target:
                res.append(list(numset))
                return

            for j in range(i, len(nums)):
                if s + nums[j] > target:
                    return

                numset.append(nums[j])
                s += nums[j]
                dfs(j, numset, s)
                numset.pop()
                s -= nums[j]

        dfs(0, [], 0)
        return res