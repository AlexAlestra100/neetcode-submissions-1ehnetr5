class Solution:
    def isPalindrome(self, s: str) -> bool:
        lS = s.lower()
        print(lS)
        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            print(p1, p2)
            print(lS[p1], lS[p2])
            if lS[p1].isalnum():
                if lS[p2].isalnum():
                    print(s[p2])
                    if lS[p1] != lS[p2]:
                        return False
                    else:
                        p1 += 1
                        p2 -= 1
                else:
                    p2 -= 1
            else:
                p1 += 1

        return True