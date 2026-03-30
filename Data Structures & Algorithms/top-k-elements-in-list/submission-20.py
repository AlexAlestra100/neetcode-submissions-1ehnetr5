class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}

        for num in nums:
            hMap[num] = hMap.get(num, 0) + 1

        freq = {x: [] for x in range(len(nums) + 1, 0, -1)}

        for key, val in hMap.items():
            freq[val].append(key)

        res = []

        for val in freq.values():
            for num in val:
                if k == 0:
                    return res

                res.append(num)
                k -= 1

        return res