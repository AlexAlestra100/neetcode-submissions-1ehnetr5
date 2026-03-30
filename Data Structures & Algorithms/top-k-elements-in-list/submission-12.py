class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ret = []

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        freq = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
        
        for tup in freq:
            if len(ret) == k:
                return ret
            ret.append(tup[0])

        return ret