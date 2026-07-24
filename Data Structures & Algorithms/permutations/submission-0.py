class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)


        def backtrack(i):
            if i >= n:
                return

            if len(sol) == n:
                res.append(sol[:])
                return

            for num in nums:
                if not num in sol:
                    sol.append(num)
                    backtrack(i)
                    sol.pop()
        
        backtrack(0)
        return res