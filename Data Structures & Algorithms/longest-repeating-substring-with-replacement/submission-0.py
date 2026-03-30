class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxL = 0

        l = 0
        r = l
        maxF = 0

        hMap = {}

        while r < len(s):
            hMap[s[r]] = 1 + hMap.get(s[r], 0)
            maxF = max(maxF, hMap[s[r]])

            while (r - l + 1) - maxF > k:
                hMap[s[l]] -= 1
                l += 1

            maxL = max(maxL, r - l + 1)
            r += 1

        return maxL