class TicTacToe:

    def __init__(self, n: int):
        self.row = defaultdict(list)
        self.col = defaultdict(list)
        self.dia = defaultdict(list)
        for i in range(n):
            self.row[i] = [0] * n
            self.col[i] = [0] * n
        self.dia[0] = [0] * n
        self.dia[1] = [0] * n
        self.state = None
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        if self.state:
            return self.state
        if player == 2:
            player = -1
        self.row[row][col] = player
        self.col[col][row] = player
        if row == col:
            self.dia[0][col] = player
        if self.n - row - 1 == col:
            self.dia[1][col] = player
        if sum(self.row[row]) == self.n or sum(self.col[col]) == self.n or sum(self.dia[0]) == self.n or sum(self.dia[1]) == self.n:
            self.state = 1
            return 1
        elif sum(self.row[row]) == -self.n or sum(self.col[col]) == -self.n or sum(self.dia[0]) == -self.n or sum(self.dia[1]) == -self.n:
            self.state = 2
            return 2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
