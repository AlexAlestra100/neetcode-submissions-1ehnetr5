class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hMap = {}

        # for num in nums:
        #     hMap[num] = hMap.get(num, 0) + 1

        # freq = {x: [] for x in range(len(nums) + 1, 0, -1)}

        # for key, val in hMap.items():
        #     freq[val].append(key)

        # res = []

        # for val in freq.values():
        #     for num in val:
        #         if k == 0:
        #             return res

        #         res.append(num)
        #         k -= 1

        # return res
        hashT = {}

        for n in nums:
            hashT[n] = 1 + hashT.get(n, 0)


        freq = []

        for num, count in hashT.items():
            freq.append([count, num])

        freq.sort()

        res = []

        for i in range(len(freq) - 1, -1, -1):
            if len(res) < k:
                res.append(freq[i][1])

        return res