from .base import BaseAI
import random
import time

random.seed(time.time())


class EasyAI(BaseAI):
    """
    Klasa AI o łatwym poziomie trudności.
    Wybiera losowy ruch z dostępnych pól.
    Dziedziczy po BaseAI.
    """
    def get_move(self, board):
        """
        Zwraca losowy ruch AI spośród dostępnych pól.

        Args:
            board (list): Aktualny stan planszy (3x3).

        Returns:
            tuple: Ruch w formacie (wiersz, kolumna)
            lub None, jeśli brak dostępnych pól.
        """
        empty = [
            (r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
        if not empty:
            return None
        return random.choice(empty)
