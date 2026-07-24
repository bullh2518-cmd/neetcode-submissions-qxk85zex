class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        nums.sort()
        def backtrack(i):

            res.append(sol[:])
            
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                sol.append(nums[j])
                backtrack(j + 1)
                sol.pop()
        backtrack(0)
        return res
                    
            