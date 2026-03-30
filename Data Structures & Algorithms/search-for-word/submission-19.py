class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False

        def reCalcBoard(r, c):
            board[r][c] = '#'
            modBoard = []
            if r > 0:
                modBoard.append([board[r - 1][c]])
            if c > 0 or c < len(board[r]):
                li = []
                if c > 0:
                    li.append(board[r][c - 1])
                li.append(board[r][c])
                if c < len(board[r]) - 1:
                    li.append(board[r][c + 1])
                if li:
                    modBoard.append(li)
            if r < len(board) - 1:
                modBoard.append([board[r + 1][c]])

            return modBoard

        def backtrack(i, bd, qd=None):
            nonlocal res
            if i == len(word):
                res = True
                return

            for r, arr in enumerate(bd):
                for c, char in enumerate(arr):
                    if word[i] == char:
                        if not qd:
                            newBoard = reCalcBoard(r, c)
                            qdr = (r, c)
                            backtrack(i + 1, newBoard, qdr)
                            board[r][c] = word[i]
                        else:
                            newR, newC = qd
                            if r == 0:
                                if len(arr) > 1:
                                    if c == 0:
                                        newC -= 1
                                    else:
                                        newC += 1
                                else:
                                    newR -= 1
                            if r > 0:
                                if len(arr) > 1:
                                    if c == 0:
                                        newC -= 1
                                    else:
                                        newC += 1
                                else:
                                    newR += 1
                            newBoard = reCalcBoard(newR, newC)
                            qdr = (newR, newC)
                            backtrack(i + 1, newBoard, qdr)
                            board[newR][newC] = word[i]
                        if res:
                            return

        backtrack(0, board)

        return res
