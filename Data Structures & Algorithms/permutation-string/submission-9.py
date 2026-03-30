class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        chars = {}
        windowStr = {}

        for x in range(ord('a'), ord('z') + 1):
            chars[chr(x)] = chars.get(chr(x), 0)
            windowStr[chr(x)] = windowStr.get(chr(x), 0)

        for c1 in s1:
            chars[c1] += 1

        l = 0
        r = l

        while r < len(s2):
            while (r - l + 1) > len(s1):
                windowStr[s2[l]] -= 1
                l += 1
            
            windowStr[s2[r]] += 1

            if chars == windowStr:
                return True

            r += 1

        return False