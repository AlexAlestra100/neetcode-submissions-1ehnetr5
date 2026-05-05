class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = {}

        for c in s1:
            s1Freq[c] = s1Freq.get(c, 0) + 1

        s2Freq = {}
        l = 0
        for r in range(len(s2)):
            s2Freq[s2[r]] = s2Freq.get(s2[r], 0) + 1

            while r - l >= len(s1):
                s2Freq[s2[l]] -= 1
                l += 1

            if s1Freq.items() <= s2Freq.items():
                return True

        return False