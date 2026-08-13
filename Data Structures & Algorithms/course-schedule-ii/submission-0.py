from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        order = []

        for a, b in prerequisites:
            g[a].append(b)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        def dfs(i):
            if states[i] == VISITING:
                return False
            elif states[i] == VISITED:
                return True
            states[i] = VISITING

            for nei in g[i]:
                if not dfs(nei):
                    return False

            states[i] = VISITED
            order.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order

            
