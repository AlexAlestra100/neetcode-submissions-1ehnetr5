class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}

        s = ''.join(sorted(s))

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        odd = 0
        even = len(s)

        for key, val in freq.items():
            if val % 2 == 0:
                even = min(even, val)
            else:
                odd = max(odd, val)

        return odd - even