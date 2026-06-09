class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(opened, closed, form):
            if closed == 0:
                res.append(''.join(form))
                return

            if opened > 0:
                form.append('(')
                backtrack(opened - 1, closed, form)
                form.pop()

            if closed > opened:
                form.append(')')
                backtrack(opened, closed - 1, form)
                form.pop()

        backtrack(n - 1, n, ['('])
        return res