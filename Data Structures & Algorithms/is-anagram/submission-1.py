class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash1 = {}
        hash2 = {}

        for c in s:
            if c in hash1:
                hash1[c] = hash1[c] + 1
            else:
                hash1[c] = 1
        
        for c in t:
            if c in hash2:
                hash2[c] = hash2[c] + 1
            else:
                hash2[c] = 1

        return hash1 == hash2