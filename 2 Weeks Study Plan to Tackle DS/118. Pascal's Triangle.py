# -*- coding: utf-8 -*-
"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
    
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascal = list([1]*i for i in range(1, numRows + 1))
        
        for i in range(2, numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        
        return pascal