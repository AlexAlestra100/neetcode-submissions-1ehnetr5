class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        st = set()

        l = r = 0
        while r < len(s):
            while s[r] in st:
                st.remove(s[l])
                l += 1

            st.add(s[r])
            r += 1
            res = max(res, r - l)

        return res