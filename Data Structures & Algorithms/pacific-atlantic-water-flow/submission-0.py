from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_que = deque()
        p_seen = set()

        a_que = deque()
        a_seen = set()

        m, n = len(heights), len(heights[0])

        # Pacific: top row
        for j in range(n):
            p_que.append((0, j))
            p_seen.add((0, j))

        # Pacific: left column
        for i in range(1, m):
            p_que.append((i, 0))
            p_seen.add((i, 0))

        # Atlantic: right column
        for i in range(m):
            a_que.append((i, n - 1))
            a_seen.add((i, n - 1))

        # Atlantic: bottom row
        for j in range(n - 1):
            a_que.append((m - 1, j))
            a_seen.add((m - 1, j))

        def get_coords(que, seen):
            while que:
                i, j = que.popleft()

                for i_off, j_off in [
                    (1, 0),
                    (0, 1),
                    (-1, 0),
                    (0, -1)
                ]:
                    r = i + i_off
                    c = j + j_off

                    if (
                        0 <= r < m
                        and 0 <= c < n
                        and heights[r][c] >= heights[i][j]
                        and (r, c) not in seen
                    ):
                        seen.add((r, c))
                        que.append((r, c))

            return seen

        p_coords = get_coords(p_que, p_seen)
        a_coords = get_coords(a_que, a_seen)

        result = p_coords & a_coords

        return [[r, c] for r, c in result]