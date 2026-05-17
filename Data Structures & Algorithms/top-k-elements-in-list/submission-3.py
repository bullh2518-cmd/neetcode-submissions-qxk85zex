import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        joint = []

        for num in count:
            if count[num] > 0:
                joint.append((-count[num], num))
        
        heapq.heapify(joint)

        res = []

        for i in range(k):
            freq, num = heapq.heappop(joint)
            res.append(num)
        return res
        
            