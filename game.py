class TicTacToe:
    def __init__(self, opponent=None):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None
        self.winning_line = None
        self.opponent = opponent

    def make_move(self, row, col):
        if self.board[row][col] == " " and not self.winner:
            self.board[row][col] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            else:
                self.switch_player()

                # Jeśli teraz ruch należy do AI, wykonaj go automatycznie
                if (self.opponent and self.current_player ==
                        self.opponent.symbol and not self.winner):
                    ai_move = self.opponent.get_move(self.board)
                    if ai_move:
                        self.make_move(*ai_move)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        b = self.board
        p = self.current_player

        for i in range(3):
            if all(b[i][j] == p for j in range(3)):
                self.winning_line = ((i, 0), (i, 2))
                return True
            if all(b[j][i] == p for j in range(3)):
                self.winning_line = ((0, i), (2, i))
                return True

        if all(b[i][i] == p for i in range(3)):
            self.winning_line = ((0, 0), (2, 2))
            return True
        if all(b[i][2 - i] == p for i in range(3)):
            self.winning_line = ((0, 2), (2, 0))
            return True

        return False

    def is_draw(self):
        board_full = all(cell != " " for row in self.board for cell in row)
        return board_full and not self.winner

    def reset(self):
        self.__init__(self.opponent)
