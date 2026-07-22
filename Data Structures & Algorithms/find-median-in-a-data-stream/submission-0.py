import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
            heapq.heappush(self.small, -num)
            q = heapq.heappop(self.small)

            heapq.heappush(self.large, -q)

            if len(self.large) > len(self.small):
                w = heapq.heappop(self.large)
                heapq.heappush(self.small, -w)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]

        elif len(self.small) == len(self.large):
            s = -self.small[0]
            l = self.large[0]
            return (s + l) / 2

        