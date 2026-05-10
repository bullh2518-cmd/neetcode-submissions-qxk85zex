class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_nums = {}

        for i, n in enumerate(nums):
            Diff = target - n

            if Diff in map_nums:
                return [map_nums[Diff], i]

            map_nums[n] = i