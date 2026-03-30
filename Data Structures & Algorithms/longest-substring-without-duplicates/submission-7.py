class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        res = 0

        l = 0
        r = 1

        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
            else:
                while s[l] != s[r]:
                    l += 1
                l += 1
                r += 1

            res = max(res, len(s[l:r]))

        return res