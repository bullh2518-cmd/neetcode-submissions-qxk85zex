class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
      sol, res = [], []
      letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
      }
      if not digits:
        return res
      

      def backtrack(start):
        if start == len(digits):
          res.append("".join(sol))
          return

        for char in letters[digits[start]]:
              sol.append(char)       # make the choice
              backtrack(start + 1)   # process the next digit
              sol.pop()              # undo the choice

      backtrack(0)
      return res
            


