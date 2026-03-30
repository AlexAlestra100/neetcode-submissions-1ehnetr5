class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res = []

        def backtrack(i, path):
            if i == len(digits):
                res.append(path)
                return

            start_ord = ord('a') + (int(digits[i]) - 2) * 3
            if digits[i] in ('8', '9'): start_ord += 1
            
            num_letters = 4 if digits[i] in ('7', '9') else 3

            for j in range(num_letters):
                backtrack(i + 1, path + chr(start_ord + j))

        backtrack(0, '')
        return res