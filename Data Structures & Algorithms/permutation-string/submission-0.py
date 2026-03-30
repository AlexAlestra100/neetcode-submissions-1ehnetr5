class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = {}

        for c in s1:
            map1[c] = 1 + map1.get(c, 0)
        
        l = 0
        r = l

        while r < len(s2):
            map2 = {}
            while r - l + 1 <= len(s1) and r < len(s2):
                map2[s2[r]] = 1 + map2.get(s2[r], 0)
                r += 1
            print(map2)
            if map1 == map2:
                return True
            l += 1
            r = l

        return False