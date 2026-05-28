class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, numset, total):
            if total == target:
                res.append(list(numset))
                return

            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    return
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                numset.append(candidates[j])
                backtrack(j + 1, numset, total + candidates[j])
                numset.pop()

        backtrack(0, [], 0)

        return res