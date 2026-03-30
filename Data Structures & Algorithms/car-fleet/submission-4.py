class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return 0

        stack = []

        cars = sorted(zip(position, speed), reverse=True)

        for car in cars:
            t = (target - car[0]) / car[1]
            if not stack or (stack and stack[-1] < t):
                stack.append(t)

        return len(stack)