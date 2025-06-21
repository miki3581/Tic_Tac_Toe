from .base import BaseAI


class HardAI(BaseAI):
    def get_move(self, board):
        best_score = -float('inf')
        best_move = None
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = self.symbol
                    score = self.minimax(board, False)
                    board[r][c] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (r, c)
        return best_move

    def minimax(self, board, is_maximizing):
        winner = self.check_winner(board)
        if winner == self.symbol:
            return 1
        elif winner == self.opponent_symbol:
            return -1
        elif all(cell != " " for row in board for cell in row):
            return 0

        if is_maximizing:
            best = -float('inf')
            for r in range(3):
                for c in range(3):
                    if board[r][c] == " ":
                        board[r][c] = self.symbol
                        score = self.minimax(board, False)
                        board[r][c] = " "
                        best = max(best, score)
            return best
        else:
            best = float('inf')
            for r in range(3):
                for c in range(3):
                    if board[r][c] == " ":
                        board[r][c] = self.opponent_symbol
                        score = self.minimax(board, True)
                        board[r][c] = " "
                        best = min(best, score)
            return best

    def check_winner(self, b):
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != " ":
                return b[i][0]
            if b[0][i] == b[1][i] == b[2][i] != " ":
                return b[0][i]
        if b[0][0] == b[1][1] == b[2][2] != " ":
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] != " ":
            return b[0][2]
        return None
