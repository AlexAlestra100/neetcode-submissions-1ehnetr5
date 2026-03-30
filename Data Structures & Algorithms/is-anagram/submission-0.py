class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map1 = {}
        map2 = {}

        for c in s:
            if c not in map1:
                map1[c] = 1
            map1[c] += 1

        for c in t:
            if c not in map2:
                map2[c] = 1
            map2[c] += 1

        print(map1, map2)

        return map1 == map2