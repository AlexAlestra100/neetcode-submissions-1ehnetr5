class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, numset, total):
            if total == target:
                res.append(list(numset))
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return

                total += nums[j]
                numset.append(nums[j])

                backtrack(j, numset, total)

                total -= nums[j]
                numset.pop()

        backtrack(0, [], 0)

        return res