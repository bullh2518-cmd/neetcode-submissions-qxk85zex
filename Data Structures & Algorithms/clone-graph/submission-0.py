"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        start = node
        old_to_new = {}

        stack = [start]
        seen = {start}

        # First pass: create a clone of every node
        while stack:
            old_node = stack.pop()

            old_to_new[old_node] = Node(old_node.val)

            for nei in old_node.neighbors:
                if nei not in seen:
                    seen.add(nei)
                    stack.append(nei)

        # Second pass: connect the cloned nodes
        for old_node, new_node in old_to_new.items():
            for nei in old_node.neighbors:
                new_nei = old_to_new[nei]
                new_node.neighbors.append(new_nei)

        return old_to_new[start]