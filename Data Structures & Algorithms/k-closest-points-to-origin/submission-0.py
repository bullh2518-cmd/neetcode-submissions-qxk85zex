import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x1, y1 = 0, 0
        results = []
        heapq.heapify(results)
        for x, y in points:
            distance = math.sqrt((x1 - x)**2 + (y1 - y)**2)
            heapq.heappush(results, (distance, x, y))

        answer = []
        for i in range(k):
            distance, x, y = heapq.heappop(results)
            answer.append([x,y])
        return answer

            



