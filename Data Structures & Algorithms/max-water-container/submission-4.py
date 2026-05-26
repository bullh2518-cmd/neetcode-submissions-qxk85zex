class Solution:
    def maxArea(self, heights: List[int]) -> int:     
        answer = []
        if len(heights) <= 1:
            return 0
        else:
            left = 0
            right = left + 1
            while right < len(heights):
                if heights[left] >= heights[right]:
                    Area = heights[right] * (right - left)
                    answer.append(Area)
                    right += 1
                elif heights[right] >= heights[left]:
                    Area = heights[left] * (right - left)
                    answer.append(Area)
                    right += 1
                if right == len(heights):
                    left += 1
                    right = left + 1
        return max(answer)
            