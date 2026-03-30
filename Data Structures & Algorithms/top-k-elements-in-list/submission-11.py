class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        hMap = {}
        freq = [[] for n in range(len(nums) + 1)]

        for num in nums:
            if num not in hMap:
                hMap[num] = 1
            else:
                hMap[num] += 1

        for key in hMap:
            freq[hMap[key]].append(key)

        sol = []

        print(hMap)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                if len(sol) < k:
                    sol.append(n)

        return sol