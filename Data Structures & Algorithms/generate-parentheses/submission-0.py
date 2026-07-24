class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []

        open_count = 0
        close_count = 0

        def backtrack(open_count, close_count):
            if len(sol) == 2 * n:
                res.append("".join(sol))
                return

            if open_count < n:
                sol.append("(")
                backtrack(open_count + 1, close_count)
                sol.pop()


            if close_count < open_count:
                sol.append(")")
                backtrack(open_count, close_count + 1)
                sol.pop()

        backtrack(open_count, close_count)
        return res

