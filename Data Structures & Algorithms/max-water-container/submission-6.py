class Solution:
    def maxArea(self, heights: List[int]) -> int:     
        n = len(heights)
        l = 0
        r = n - 1
        max_area = 0

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            a = w * h
            max_area = max(max_area, a)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_area 