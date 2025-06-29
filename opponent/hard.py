from opponent.base import BaseAI
from opponent.ml_model import MLModel


class MLAI(BaseAI):
    """
    Klasa AI o wysokim poziomie trudności
    Wykorzystuje model ML do podejmowania decyzji.
    Dziedziczy po BaseAI.
    """
    def __init__(self, symbol):
        """
        Inicjalizuje AI z symbolem gracza i ładuje model ML.

        Args:
            symbol (str): Symbol AI ('X' lub 'O').
        """
        super().__init__(symbol)
        self.model_handler = MLModel()

    def get_move(self, board):
        """
        Zwraca najlepszy ruch na podstawie przewidywań modelu ML.

        Args:
            board (list): Aktualny stan planszy (3x3).

        Returns:
            tuple: Najlepszy ruch w formacie (wiersz, kolumna)
            lub None, jeśli brak ruchów.
        """
        flat_board = self._encode_board(board)
        predictions = self.model_handler.predict(flat_board, self.symbol)

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
        """
        Przekształca planszę w wektor cech dla modelu ML.

        Args:
            board (list): Aktualny stan planszy (3x3).

        Returns:
            list: Płaska reprezentacja planszy jako wektor cech.
        """
        return [
            1 if cell == self.symbol
            else -1 if cell == self.opponent_symbol else 0
            for row in board for cell in row
        ]
