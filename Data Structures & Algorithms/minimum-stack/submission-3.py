class MinStack:

    def __init__(self):
        self.currMin = []
        self.currStack = []
        

    def push(self, val: int) -> None:
        self.currStack.append(val)
        val = min(val, self.currMin[-1] if self.currMin else val)
        self.currMin.append(val)

    def pop(self) -> None:
        self.currStack.pop()
        self.currMin.pop()

    def top(self) -> int:
        return self.currStack[-1]
        

    def getMin(self) -> int:
        return self.currMin[-1]