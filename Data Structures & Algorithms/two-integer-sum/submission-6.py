class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        map_nums = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in map_nums:
                    return [map_nums[diff], i]

            map_nums[n] = i
