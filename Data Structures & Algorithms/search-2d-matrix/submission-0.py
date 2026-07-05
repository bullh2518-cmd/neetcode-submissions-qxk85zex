class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        left  =  0
        right = n * m - 1

        while left <= right:
            middle = (left + right) // 2
            
            row = middle // m
            col = middle % m
            value = matrix [row][col]

            if value == target:
                return True
            elif value < target:
                left = middle + 1
            else:
                right = middle - 1

        return False
