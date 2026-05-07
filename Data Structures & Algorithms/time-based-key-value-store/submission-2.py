class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store.get(key, [])

        l = 0
        r = len(vals) - 1

        res = ""
        while l <= r:
            m = l + (r - l) // 2

            if vals[m][0] == timestamp:
                return vals[m][1]

            if timestamp < vals[m][0]:
                r = m - 1
            else:
                res = vals[m][1]
                l = m + 1

        return res