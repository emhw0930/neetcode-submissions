class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        for row_block in range(3):
            for col_block in range(3):
                seen = set()
                for row in range(9):
                    for col in range(9): 
                        if row // 3 == row_block and col // 3 == col_block:
                            if board[row][col] == ".":
                                continue
                            if board[row][col] in seen:
                                return False
                            seen.add(board[row][col])
        return True
        