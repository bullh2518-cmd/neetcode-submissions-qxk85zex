class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_set = set()

        for numbers in nums:
            if numbers in num_set:
                return numbers
            
            num_set.add(numbers)

        return None