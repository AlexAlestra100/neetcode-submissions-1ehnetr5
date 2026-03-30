class Solution:
    def getDistance(self, x1, x2, target):
        p1 = x1[0]
        p2 = x2[0]

        v1 = x1[1]
        v2 = x2[1]

        vD = v1 - v2
        if vD <= 0:
            return False

        xD = (p2 - p1) / vD

        return p1 + (v1 * xD) <= target

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        if not position or not speed:
            return len(stack)

        pvs = sorted(zip(position, speed))

        for pv in pvs[::-1]:
            if not stack or (stack and not self.getDistance(pv, stack[-1], target)):
                stack.append(pv)

        return len(stack)
