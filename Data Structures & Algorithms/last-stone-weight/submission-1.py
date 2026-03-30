class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negated = [-x for x in stones]

        heapq.heapify(negated)

        while len(negated) > 1:
            x = -heapq.heappop(negated)
            y = -heapq.heappop(negated)

            diff = x - y

            if diff > 0:
                heapq.heappush(negated, -diff)

        if len(negated) == 0:
            return 0

        return -negated[0]