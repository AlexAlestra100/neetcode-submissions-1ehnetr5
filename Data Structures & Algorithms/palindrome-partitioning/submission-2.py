class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, path):
            if i >= len(s):
                res.append(path[:])
                return

            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    path.append(s[i:j + 1])
                    backtrack(j + 1, path)
                    path.pop()

        backtrack(0, [])

        return res