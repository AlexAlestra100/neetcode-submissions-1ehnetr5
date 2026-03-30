class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            l = len(s)
            res += (str(l) + '#' + s)

        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        sLen = len(s)
        strs = []

        print(s)

        while i < sLen:
            j = i
            # 10#HelloWorld3#who
            while s[i] != '#':
                i += 1
            length = int(s[j:i])
            start = i + 1
            end = length + start
            strs.append(s[start:end])
            i = end

        return strs