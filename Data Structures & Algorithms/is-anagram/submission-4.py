class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hMap = {}

        for i in range(len(s)):
            hMap[s[i]] = hMap.get(s[i], 0) + 1
            hMap[t[i]] = hMap.get(t[i], 0) - 1

        for c in hMap.values():
            if c != 0:
                return False

        return True