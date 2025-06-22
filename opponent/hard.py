from opponent.base import BaseAI
from opponent.ml_model import MLModel


class MLAI(BaseAI):
    def __init__(self, symbol):
        super().__init__(symbol)
        self.model_handler = MLModel()

    def get_move(self, board):
        flat_board = self._encode_board(board)
        predictions = self.model_handler.predict(flat_board)

        legal_moves = [(r, c) for r in range(3) for c in range(3)
                       if board[r][c] == " "]

        move_scores = {}
        for row, col in legal_moves:
            idx = row * 3 + col
            move_scores[(row, col)] = predictions[idx]

        if move_scores:
            best_move = max(move_scores, key=move_scores.get)
            return best_move
        return None

    def _encode_board(self, board):
        encoding = {'X': 1, 'O': -1, ' ': 0}
        return [encoding[cell] for row in board for cell in row]
