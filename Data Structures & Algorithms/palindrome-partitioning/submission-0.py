class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        path = []

        palindrome = [[False] * n for _ in range(n)]

        for left in range(n - 1, -1, -1):
            for right in range(left, n):
                if s[left] == s[right]:
                    if right - left <= 2 or palindrome[left + 1][right - 1]:
                        palindrome[left][right] = True

        def backtrack(start):
            if start == n:
                res.append(path[:])
                return

            for end in range(start, n):
                if not palindrome[start][end]:
                    continue

                path.append(s[start:end + 1])
                backtrack(end + 1)
                path.pop()

        backtrack(0)
        return res