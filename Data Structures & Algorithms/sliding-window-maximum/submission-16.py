class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        l = 0
        for r, n in enumerate(nums):
            while q and q[-1] < n:
                q.pop()

            q.append(n)

            if r - l + 1 == k:
                res.append(q[0])

                if nums[l] == q[0]:
                    q.popleft()

                l += 1

        return res