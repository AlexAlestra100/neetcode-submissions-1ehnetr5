class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numbers = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []

        def backtrack(i, combo):
            if i >= len(digits):
                if combo:
                    res.append(''.join(combo))
                return res
            for c in numbers[digits[i]]:
                combo.append(c)
                backtrack(i + 1, combo)
                combo.pop()
        
        backtrack(0, [])

        return res