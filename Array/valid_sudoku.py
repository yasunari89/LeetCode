from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        top_lefts = []
        for i in range(3):
            for j in range(3):
                top_lefts.append([3*i, 3*j])
        for top_left in top_lefts:
            if not self.boxValid(top_left):
                return False
        for i in range(10):
            if not self.rowValid(i):
                return False
        for i in range(10):
            if not self.colValid(i):
                return False
        return True
        
    
    def boxValid(self, left_top: List[int]) -> bool:
        hash_table = {}
        for i in range(3):
            row = left_top[0] + i
            for j in range(3):
                col = left_top[1] + j
                num = self.board[row][col]
                if num in hash_table and num != '.':
                    return False
                else:
                    hash_table[num] = 1
        return True
    
    def rowValid(self, row: int) -> bool:
        hash_table = {}
        for num in self.board[row]:
            if num in hash_table and num != '.':
                return False
            else:
                hash_table[num] = 1
        return True
    
    def colValid(self, col: int) -> bool:
        hash_table = {}
        for row in range(10):
            num = self.board[row][col]
            if num in hash_table and num != '.':
                return False
            else:
                hash_table[num] = 1
        return True
    
        
        