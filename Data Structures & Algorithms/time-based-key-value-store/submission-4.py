class TimeMap:

    def __init__(self):
        self.timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamps:
            self.timestamps[key] = []
        self.timestamps[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        
        arr = self.timestamps.get(key, [])

        l = 0
        r = len(arr) - 1

        while l <= r:
            m = l + (r - l) // 2

            if arr[m][1] == timestamp:
                return arr[m][0]

            if arr[m][1] < timestamp:
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1

        return res