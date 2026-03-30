class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}

        for c1 in s:
            if c1 in map1:
                map1[c1] += 1
            else:
                map1[c1] = 1

        print(map1)

        for c2 in t:
            if c2 in map2:
                map2[c2] += 1
            else:
                map2[c2] = 1

        return map1 == map2