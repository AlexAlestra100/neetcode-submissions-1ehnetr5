class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        q = deque()

        for i, t in enumerate(tickets):
            q.append([i, t])

        while q:
            left = q.popleft()
            count += 1
            left[1] -= 1

            if left[1] == 0:
                if left[0] == k:
                    return count
                continue
            
            q.append(left)

        return count
