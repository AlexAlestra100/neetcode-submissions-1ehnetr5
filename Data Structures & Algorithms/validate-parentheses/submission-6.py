class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        mp = {']':'[', '}':'{', ')':'('}

        for c in s:
            if c in mp:
                if st and st[-1] == mp[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)

        return not st