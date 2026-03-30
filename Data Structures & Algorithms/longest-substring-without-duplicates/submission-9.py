class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        res = 0

        seen = set()

        p1 = p2 = 0

        while p2 < len(s):
            if s[p2] in seen:
                while s[p1] != s[p2]:
                    seen.remove(s[p1])
                    p1 += 1
                seen.remove(s[p1])
                p1 += 1
            seen.add(s[p2])
            p2 += 1
            res = max(res, p2 - p1)

        return res