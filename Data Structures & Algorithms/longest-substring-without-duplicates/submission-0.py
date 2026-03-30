class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        r = l
        maxL = 0

        while r < len(s):
            print(charSet)
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxL = max(maxL, r - l + 1)
            r += 1
        return maxL