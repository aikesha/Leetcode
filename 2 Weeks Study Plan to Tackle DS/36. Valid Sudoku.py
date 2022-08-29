"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sub_sqs = [[set() for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':                
                    
                    if board[i][j] in rows[i]: # row repeat
                        return False
                    else:
                        rows[i].add(board[i][j])

                    if board[i][j] in cols[j]: # col repeat
                        return False
                    else:
                        cols[j].add(board[i][j])
                    
                    if board[i][j] in sub_sqs[i//3][j//3]: #subsquare repeat
                        return False
                    else:
                        sub_sqs[i//3][j//3].add(board[i][j])
                    
        return True