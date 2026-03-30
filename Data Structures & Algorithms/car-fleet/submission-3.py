class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        if not position or not speed:
            return len(stack)

        pvs = sorted(zip(position, speed))

        for p, v in pvs[::-1]:
            t = (target - p) / v
            print(p, v, stack, t)
            if not stack or (stack and stack[-1] < t):
                stack.append(t)

        return len(stack)
