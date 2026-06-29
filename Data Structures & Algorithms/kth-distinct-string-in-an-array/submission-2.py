class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = []
        freq = {}

        for a in arr:
            freq[a] = freq.get(a, 0) + 1

        for key in freq:
            if freq[key] == 1:
                k -= 1
                if k == 0:
                    return key

        return ''