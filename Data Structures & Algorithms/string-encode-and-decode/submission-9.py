class Solution:

    def encode(self, strs: List[str]) -> str:
        enC = ""

        for s in strs:
            enC += str(len(s)) + "#" + s

        return enC

    def decode(self, s: str) -> List[str]:
        deC = []

        i = 0
        j = ""

        while i < len(s):
            if s[i] != "#":
                j += s[i]
                i += 1
            else:
                print(f"j: {j}, i: {i}, calcWord: {s[i + 1:int(j) + i + 1]}")
                deC.append(s[i + 1:int(j) + i + 1])
                i = int(j) + 1 + i
                j = ""

        return deC