class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        count = 0
        extra = False
        print(freq)
        for val in freq.values():
            if val > 1:
                s = val // 2
                s *= 2
                count += s
                if val - s > 0:
                    extra = True
            elif val == 1:
                extra = True

        return count if not extra else count + 1