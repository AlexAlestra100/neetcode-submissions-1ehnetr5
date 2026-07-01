class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        map1 = {}
        map2 = {}

        for c in s:
            map1[c] = map1.get(c, 0) - 1

        for c in t:
            map2[c] = map2.get(c, 0) - 1

        large = map1 if len(s) > len(t) else map2
        small = map1 if len(s) < len(t) else map2

        for key in large:
            if key not in small:
                return key
            if large[key] - small[key] != 0:
                return key