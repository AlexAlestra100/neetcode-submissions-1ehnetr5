class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}

        for num in nums:
            hMap[num] = hMap.get(num, 0) + 1

        buckets = []

        for i, v in hMap.items():
            buckets.append([v, i])

        buckets.sort()

        print(buckets)

        freq = []

        for j in range(len(buckets) - 1, -1, -1):
            if len(freq) < k:
                freq.append(buckets[j][1])

        return freq