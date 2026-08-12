class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != "O":
                return

            board[r][c] = "T"

            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Find O's connected to the border
        for r in range(m):
            for c in range(n):
                if (
                    board[r][c] == "O"
                    and (r == 0 or r == m - 1 or c == 0 or c == n - 1)
                ):
                    capture(r, c)

        # Capture surrounded O's
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Restore safe O's
        for r in range(m):
            for c in range(n):
                if board[r][c] == "T":
                    board[r][c] = "O"

        