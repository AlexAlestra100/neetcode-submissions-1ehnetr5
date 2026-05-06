class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = {ord('a') + i: 0 for i in range(26)}
        count2 = {ord('a') + i: 0 for i in range(26)}

        for i in range(len(s1)):
            count1[ord(s1[i])] += 1
            count2[ord(s2[i])] += 1

        match = 0

        for c in range(ord('a'), ord('z') + 1):
            if count1[c] == count2[c]:
                match += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if match == 26:
                return True

            cr = ord(s2[r])
            count2[cr] += 1
            if count1[cr] == count2[cr]:
                match += 1
            elif count1[cr] + 1 == count2[cr]:
                match -= 1

            cl = ord(s2[l])
            count2[cl] -= 1
            if count1[cl] == count2[cl]:
                match += 1
            elif count1[cl] - 1 == count2[cl]:
                match -= 1

            l += 1

        return match == 26