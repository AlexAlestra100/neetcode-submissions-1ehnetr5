class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        # Pruning: Frequency check (This is a 2026 must-have for LeetCode)
        from collections import Counter
        board_counts = Counter(c for r in board for c in r)
        if any(board_counts[char] < count for char, count in Counter(word).items()):
            return False

        def backtrack(r, c, i):
            # Base Case
            if i == len(word):
                return True

            # Boundary and Match Check
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            # 1. Instead of reCalcBoard, modify in-place (The "Backtrack")
            temp = board[r][c]
            board[r][c] = '#'

            # 2. Use Direct Coordinate Math (This replaces your complex qd logic)
            # This is significantly faster than building newBoard list objects
            found = (backtrack(r + 1, c, i + 1) or 
                     backtrack(r - 1, c, i + 1) or 
                     backtrack(r, c + 1, i + 1) or 
                     backtrack(r, c - 1, i + 1))

            # 3. Restore the board
            board[r][c] = temp
            return found

        # Main Loop: Only scan the board ONCE here
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True
        return False