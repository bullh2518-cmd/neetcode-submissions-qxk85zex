class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if sum(sol) == target:
                res.append(sol[:])
                return
            if i >= n:
                return
            if sum(sol) > target:
                return
            #skip--
            backtrack(i + 1)

            #make a choice
            sol.append(nums[i])
            backtrack(i)
            sol.pop()
            
        backtrack(0)
        return res