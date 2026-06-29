class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = []
        freq = {}

        for a in arr:
            freq[a] = freq.get(a, 0) + 1

        for key in freq:
            if freq[key] == 1:
                res.append(key)

        return res[k - 1] if len(res) >= k else ''