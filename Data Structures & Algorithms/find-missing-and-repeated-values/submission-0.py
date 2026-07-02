class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m = {}

        for row in grid:
            for n in row:
                m[n] = m.get(n, 0) + 1

        miss = 0
        dup = 0

        for n in range(1, len(m) + 2):
            if n not in m:
                miss = n
            elif m[n] > 1:
                dup = n

        return [dup, miss]