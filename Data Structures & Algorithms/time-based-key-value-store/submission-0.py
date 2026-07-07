class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []

        self.hashmap[key].append([value, timestamp])    

    def get(self, key: str, timestamp: int) -> str:
        values = self.hashmap.get(key, [])

        result = ""

        for value, stored_time in values:
            if stored_time <= timestamp:
                result = value
            else:
                break
        return result