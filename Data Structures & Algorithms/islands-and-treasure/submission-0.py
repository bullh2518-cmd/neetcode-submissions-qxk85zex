from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        frontier = deque()
        visited = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    frontier.append((i,j, 0))

        while frontier:
            r, c, d = frontier.popleft()

            if r >= n or r < 0 or c >= m or c < 0 or grid[r][c] == -1 or  tuple((r,c)) in visited:
                continue

            visited.add((r, c))
            grid[r][c] = d

            for dc, dr in [(1,0), (0,1), (-1,0), (0, -1)]:
                frontier.append((r + dr, c + dc, d + 1))