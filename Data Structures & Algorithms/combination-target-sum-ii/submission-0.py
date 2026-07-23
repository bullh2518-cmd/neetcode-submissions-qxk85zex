class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol, res = [], []
        n = len(candidates)
        candidates.sort()

        def backtrack(i):
            if sum(sol) == target:
                res.append(sol[:])
                return
            if i >= n:
                return
            if sum(sol) > target:
                return

            for j in range(i, n):
                    
                    if j > i and candidates[j] == candidates[j - 1]:
                        continue
                        
                    #choices
                    sol.append(candidates[j])
                    backtrack(j + 1)
                    sol.pop()

        backtrack(0)
        return res