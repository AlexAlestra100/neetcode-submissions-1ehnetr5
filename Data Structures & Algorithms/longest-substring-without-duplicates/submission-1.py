class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        box = set()
        l = 0
        r = l
        mLen = 0

        while r < len(s):
            while s[r] in box:
                box.remove(s[l])
                l += 1
            box.add(s[r])
            mLen = max(mLen, r - l + 1)
            r += 1

        return mLen