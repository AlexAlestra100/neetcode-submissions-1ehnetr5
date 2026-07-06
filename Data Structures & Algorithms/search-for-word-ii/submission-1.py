class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True

        ROWS = len(board)
        COLS = len(board[0])

        res = set()
        seen = set()

        def backtrack(r, c, curr, word):
            if 0 > r or r >= ROWS or 0 > c or c >= COLS or (r, c) in seen or board[r][c] not in curr.children:
                return

            seen.add((r, c))
            curr = curr.children[board[r][c]]
            word += board[r][c]

            if curr.word:
                res.add(word)

            backtrack(r + 1, c, curr, word)
            backtrack(r - 1, c, curr, word)
            backtrack(r, c + 1, curr, word)
            backtrack(r, c - 1, curr, word)

            seen.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, root, '')

        return list(res)