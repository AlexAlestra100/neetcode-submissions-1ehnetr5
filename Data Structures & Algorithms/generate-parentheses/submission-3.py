class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(op, cl, path):
            if op == cl == n:
                res.append(path)
                return

            if cl <= op and op < n:
                backtrack(op + 1, cl, path + '(')

                backtrack(op, cl + 1, path + ')')

            elif cl < n:
                backtrack(op, cl + 1, path + ')')

        backtrack(1, 0, '(')

        return res