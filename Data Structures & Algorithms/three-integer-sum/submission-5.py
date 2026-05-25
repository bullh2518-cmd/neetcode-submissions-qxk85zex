class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        Results = []

        for i in range(len(nums) - 2):
            Left = i + 1
            Right = len(nums) - 1
            while Left < Right:
                if nums[i] + nums[Right] + nums[Left] == 0:
                    trip = sorted([nums[Left], nums[Right], nums[i]])
                    if trip not in Results:
                            Results.append(trip)
                    Left +=1
                    Right -=1
                elif  nums[i] + nums[Right] + nums[Left] < 0:
                    Left +=1
                else:
                    Right -=1
        return Results 