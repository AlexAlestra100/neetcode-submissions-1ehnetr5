class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, pals):
            if i >= len(s):
                res.append(pals.copy())
                return

            for j in range(i + 1, len(s) + 1):
                pal = s[i:j]

                if pal == pal[::-1]:
                    pals.append(pal)
                    backtrack(j, pals)
                    pals.pop()

        backtrack(0, [])

        return res