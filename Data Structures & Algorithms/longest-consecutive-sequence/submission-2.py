class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = []
        if len(nums) == 0:
            return 0
        for i in nums:
            count = 1
            current = i
            while current + 1 in nums:
                count += 1
                current +=1

            answer.append(count)

        return (max(answer))