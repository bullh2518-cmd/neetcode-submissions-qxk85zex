import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxheap = []
        queue = deque()
        time = 0
       
        for count in freq.values():
            heapq.heappush(maxheap, -count)

        while maxheap or queue:
            time += 1
            if maxheap:
                count = heapq.heappop(maxheap)
                count += 1

                if count != 0:
                    ready = n + time
                    queue.append([count, ready])
            
            if queue and queue[0][1] <= time :
                count, ready = queue.popleft()
                heapq.heappush(maxheap, count)

        return time

