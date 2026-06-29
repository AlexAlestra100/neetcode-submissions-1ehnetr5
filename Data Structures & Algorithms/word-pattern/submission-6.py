class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(s) != len(pattern):
            return False

        ptow = {}
        wtop = {}

        for i, c in enumerate(pattern):
            if c not in ptow and s[i] not in wtop:
                ptow[c] = s[i]
                wtop[s[i]] = c
            elif c in ptow and s[i] in wtop and ptow[c] == s[i] and wtop[s[i]] == c:
                continue
            else:
                return False

        return True