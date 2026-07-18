import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)

        if not stones:
            return None

        if len(stones) == 1:
            return stones[0]

        for i in range(n):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)

        while len(stones) >  1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                result = x - y
                heapq.heappush(stones, result)
        if stones:
            return -stones[0]

        return 0


