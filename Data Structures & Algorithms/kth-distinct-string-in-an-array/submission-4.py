class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        m = {}

        for c in arr:
            m[c] = m.get(c, 0 ) + 1

        for key, val in m.items():
            print(key, val)
            if val == 1:
                if k <= 1:
                    return key
                k -= 1

        return ''