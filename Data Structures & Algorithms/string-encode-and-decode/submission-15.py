class Solution:

    def encode(self, strs: List[str]) -> str:
        mainS = ''
        for s in strs:
            mainS += str(len(s)) + '#' + s
        print(mainS)

        return mainS

    def decode(self, s: str) -> List[str]:
        mainS = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            i = j + 1
            j = i + length

            mainS.append(s[i:j])

            i = j

        print(mainS)

        return mainS