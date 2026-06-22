class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) >= 2:
            bigS = heapq.heappop(max_heap)
            smallS = heapq.heappop(max_heap)

            if bigS != smallS:
                diff = bigS - smallS
                heapq.heappush(max_heap, diff)

        if not max_heap:
            return 0

        return -max_heap[0]