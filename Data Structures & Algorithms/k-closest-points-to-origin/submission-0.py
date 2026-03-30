class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            heapq.heappush(minHeap, [dist, x, y])

        res = []

        diff = len(minHeap) - k

        while len(minHeap) > diff:
            # dist, x, y = heapq.heappop(minHeap)
            # res.append([x, y])
            res.append(heapq.heappop(minHeap)[1:3])

        return res