class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxList = []
        q = deque()

        l = 0
        r = l

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                print(l)
                print(q[0])
                print()
                q.popleft()

            if (r + 1) >= k:
                maxList.append(nums[q[0]])
                l += 1
            
            r += 1

        return maxList