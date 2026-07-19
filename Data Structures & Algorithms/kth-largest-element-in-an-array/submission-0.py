import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        for j in range(k):
            Kth = heapq.heappop(nums)

        return -Kth
        