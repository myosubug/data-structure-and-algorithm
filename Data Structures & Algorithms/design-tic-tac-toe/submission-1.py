class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n for i in range(n)]
        self.win_counter = n
        self.length = n
        

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        if self.check_win(player, row, col):
            return player
        return 0
    
    def check_win(self, player_number, cur_row, cur_col):
        direction = [(0,1),(1,0),(1,1),(1,-1)]
        row, col = cur_row, cur_col
        for dx, dy in direction:
            counter = 1

            row, col = cur_row  +dx, cur_col + dy
            while 0 <= row < self.length and 0 <= col < self.length and self.board[row][col] == player_number:
                counter += 1
                row += dx
                col += dy

            row, col = cur_row -dx, cur_col - dy
            while 0 <= row < self.length and 0 <= col < self.length and self.board[row][col] == player_number:
                counter += 1
                row -= dx
                col -= dy

            if counter >= self.win_counter:
                return True
        
        return False



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
