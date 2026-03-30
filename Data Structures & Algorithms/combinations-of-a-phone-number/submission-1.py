class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        # diff = ord('a') + (9 - 2) * 3

        # print(diff, chr(diff))

        def backtrack(i, path):
            if i == len(digits):
                if path:
                    res.append(path)
                return

            start_ord = ord('a') + (int(digits[i]) - 2) * 3

            if digits[i] in ('8', '9'):
                start_ord += 1

            backtrack(i + 1, path + chr(start_ord))

            backtrack(i + 1, path + chr(start_ord + 1))

            backtrack(i + 1, path + chr(start_ord + 2))

            if digits[i] in ('7', '9'):
                backtrack(i + 1, path + chr(start_ord + 3))

            return

        backtrack(0, '')

        return res