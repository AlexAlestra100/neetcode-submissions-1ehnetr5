class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[c][r] == '.':
                    continue

                if (board[c][r] in row[r] or
                    board[c][r] in col[c] or
                    board[c][r] in square[c//3, r//3]):
                    return False

                row[r].add(board[c][r])
                col[c].add(board[c][r])
                square[c//3, r//3].add(board[c][r])
        
        return True