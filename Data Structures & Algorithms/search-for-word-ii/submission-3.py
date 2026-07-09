class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = {}

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

        def dfs(r, c, curr, word):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in seen or board[r][c] not in curr.children:
                return

            ch = board[r][c]
            word += board[r][c]
            curr = curr.children[ch]
            seen.add((r, c))

            dfs(r + 1, c, curr, word)
            dfs(r - 1, c, curr, word)
            dfs(r, c + 1, curr, word)
            dfs(r, c - 1, curr, word)

            if curr.word:
                res.add(word)
                curr.word = False

            seen.remove((r, c))

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root, '')

        return list(res)