"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        for i in range(rows):
            if target in matrix[i]:
                return True
        
        return False
        
        
        """
        cols = len(matrix[0])
        midr = int(rows//2)
        midc = int(cols//2)
        
        
        if (matrix[midr][midc] > target):
            for i in range(midr):
                for j in range(midc):
                    if matrix[i][j] == target:
                        return True
            
        elif (matrix[midr][midc] < target):
            for i in range(midr+1, rows):
                for j in range(midc+1, cols):
                    if matrix[i][j] == target:
                        return True
            
        elif (matrix[midr][midc] == target):
            return True
        
        return False
        """