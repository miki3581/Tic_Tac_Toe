from .base import BaseAI
import random


class MediumAI(BaseAI):
    def get_move(self, board):
        # Najpierw blokuj wygraną przeciwnika
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = self.opponent_symbol
                    if self.check_win(board, self.opponent_symbol):
                        board[r][c] = " "
                        return (r, c)
                    board[r][c] = " "

        # W przeciwnym razie — losowy ruch
        empty = [
            (r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
        return random.choice(empty) if empty else None

    def check_win(self, b, sym):
        return any(
            all(b[i][j] == sym for j in range(3)) or
            all(b[j][i] == sym for j in range(3)) for i in range(3)
        ) or all(b[i][i] == sym for i in range(3)) or all(
            b[i][2 - i] == sym for i in range(3))
