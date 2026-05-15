class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        countT = {}
        window = {}
        valid = 0

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        res = [-1, -1]
        resLen = float('inf')

        l = 0
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                valid += 1

            while valid == len(countT):
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    valid -= 1

                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float('inf') else ''