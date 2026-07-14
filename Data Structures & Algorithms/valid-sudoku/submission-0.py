class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        group_dict = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (
                    board[row][col] in row_dict[row] or
                    board[row][col] in col_dict[col] or
                    board[row][col] in group_dict[(row // 3, col // 3)]
                ):
                    return False
                row_dict[row].add(board[row][col])
                col_dict[col].add(board[row][col])
                group_dict[(row // 3, col // 3)].add(board[row][col])
        
        return True

