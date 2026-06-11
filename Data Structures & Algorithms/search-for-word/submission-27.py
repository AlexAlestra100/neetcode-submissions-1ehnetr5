class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        COLS = len(board)
        ROWS = len(board[0])

        def backtrack(c, r, i):
            if i == len(word):
                return True

            if 0 <= c < COLS and 0 <= r < ROWS and board[c][r] == word[i]:
                board[c][r] = '#'

                if (backtrack(c + 1, r, i + 1) or
                    backtrack(c - 1, r, i + 1) or
                    backtrack(c, r + 1, i + 1) or
                    backtrack(c, r - 1, i + 1)):
                    return True

                board[c][r] = word[i]
            return False
        for col in range(COLS):
            for row in range(ROWS):
                if backtrack(col, row, 0):
                    return True

        return False