class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = { chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        count2 = { chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

        for i in range(len(s1)):
            count1[s1[i]] += 1
            count2[s2[i]] += 1

        match = 0

        for c in range(ord('a'), ord('z') + 1):
            if count1[chr(c)] == count2[chr(c)]:
                match += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if match == 26:
                return True

            r2 = s2[r]
            count2[r2] += 1
            if count2[r2] == count1[r2]:
                match += 1
            elif count2[r2] == count1[r2] + 1:
                match -= 1
            
            l2 = s2[l]
            count2[l2] -= 1
            if count2[l2] == count1[l2]:
                match += 1
            elif count2[l2] == count1[l2] - 1:
                match -= 1

            l += 1

        return match == 26