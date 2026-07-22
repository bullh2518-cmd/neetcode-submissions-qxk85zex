class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            #Go Down the left side 
            backtrack(i+1)

            #pick a num
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()


        backtrack(0)
        return res