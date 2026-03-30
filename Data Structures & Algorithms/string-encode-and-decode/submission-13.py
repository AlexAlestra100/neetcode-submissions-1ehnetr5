class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s = s + str(len(i)) + '#' + i
        return s

    def decode(self, s: str) -> List[str]:
        print(s)
        sL = []
        i = 0
        l = ''
        while i < len(s):
            if s[i] == '#':
                f = i + 1
                e = int(l) + f
                sL.append(s[f:e])
                i = e
                l = ''
            else:
                l = l + s[i]
                i += 1

        return sL