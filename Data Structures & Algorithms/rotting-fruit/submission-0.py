from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        frontier = deque()
        fresh_fruit = 0
        num_min = 0

        # Find all rotten oranges + count fresh oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    frontier.append((i, j))
                elif grid[i][j] == 1:
                    fresh_fruit += 1

        if fresh_fruit == 0:
            return 0

        # BFS layer by layer
        while frontier and fresh_fruit > 0:
            q_len = len(frontier)
            num_min += 1

            for _ in range(q_len):
                i, j = frontier.popleft()

                for r, c in [
                    (i, j + 1),
                    (i + 1, j),
                    (i, j - 1),
                    (i - 1, j)
                ]:

                    # Skip invalid cells or cells that aren't fresh
                    if (
                        r >= n or r < 0 or
                        c >= m or c < 0 or
                        grid[r][c] != 1
                    ):
                        continue

                    # Rot the fresh orange
                    grid[r][c] = 2
                    fresh_fruit -= 1
                    frontier.append((r, c))

        if fresh_fruit == 0:
            return num_min

        return -1