from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build the Trie
        for word in words:
            current = root

            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()

                current = current.children[char]

            # Store the complete word at its final node
            current.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(row, col, node):
            char = board[row][col]

            # The current board character is not part of any remaining word
            if char not in node.children:
                return

            next_node = node.children[char]

            # We found a complete word
            if next_node.word is not None:
                result.append(next_node.word)

                # Prevent adding the same word multiple times
                next_node.word = None

            # Mark the cell as visited
            board[row][col] = "#"

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and board[new_row][new_col] != "#"
                ):
                    dfs(new_row, new_col, next_node)

            # Backtrack: restore the original character
            board[row][col] = char

            # Optional Trie pruning
            if not next_node.children and next_node.word is None:
                del node.children[char]

        # Try starting a word from every board cell
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return result