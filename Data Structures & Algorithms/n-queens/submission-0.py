class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for i in range(n)]

        cols = set()
        posDiags = set()
        negDiags = set()

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or r + c in posDiags or r - c in negDiags:
                    continue

                cols.add(c)
                posDiags.add(r + c)
                negDiags.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1)

                cols.remove(c)
                posDiags.remove(r + c)
                negDiags.remove(r - c)
                board[r][c] = '.'

        backtrack(0)

        return res