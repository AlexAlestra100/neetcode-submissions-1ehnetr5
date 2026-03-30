class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(index, path, count):
            if count == target:
                res.append(path[:])
                return

            if count > target or index == len(nums):
                return

            path.append(nums[index])
            backtrack(index, path, count + nums[index])

            path.pop()
            backtrack(index + 1, path, count)

        backtrack(0, [], 0)

        return res