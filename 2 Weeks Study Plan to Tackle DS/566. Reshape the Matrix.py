# -*- coding: utf-8 -*-
"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix 
into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number 
of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix 
in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the 
new reshaped matrix; Otherwise, output the original matrix.

"""

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        columns = len(mat[0])
        arr1 = []
        arr2 =[]
        if rows*columns == r*c:
            for i in range(rows):
                for j in range(columns):
                    arr1.append(mat[i][j])
            for i in range(r):
                arr3 = []
                for j in range(c):
                    arr3.append(arr1[i*c + j])   
                arr2.append(arr3)
            
            return arr2
            
        return mat