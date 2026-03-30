class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        if len(s) != len(t):
            return False

        for c in range(len(s)):
            hash1[s[c]] = 1 + hash1.get(s[c], 0)
            hash2[t[c]] = 1 + hash2.get(t[c], 0)

        return hash1 == hash2