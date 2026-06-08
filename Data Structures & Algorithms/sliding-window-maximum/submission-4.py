class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        L = 0
        R = k - 1
        res = []

        while R < len(nums):
            window = nums[L:R + 1]
            res.append(max(window))
            L += 1
            R += 1

            if R == len(nums): break

        return res 
