class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for row in board:
            row_set = set()

            for num in row:
                if num == ".":
                    continue

                if num in row_set:
                    return False

                row_set.add(num)

        # Check columns
        for c in range(9):
            col_set = set()

            for r in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                if num in col_set:
                    return False

                col_set.add(num)

        # Check 3x3 boxes
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                box_set = set()

                for r in range(row_start, row_start + 3):
                    for c in range(col_start, col_start + 3):
                        num = board[r][c]

                        if num == ".":
                            continue

                        if num in box_set:
                            return False

                        box_set.add(num)

        return True