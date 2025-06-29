from .base import BaseAI
import random


class MediumAI(BaseAI):
    """
    Klasa AI o średnim poziomie trudności.
    Blokuje wygrane przeciwnika i wykonuje losowy ruch, jeśli nie ma zagrożeń.
    Dziedziczy po BaseAI.
    """
    def get_move(self, board):
        """
        Zwraca ruch AI na podstawie stanu planszy.

        Args:
            board (list): Aktualny stan planszy (3x3).

        Returns:
            tuple: Ruch w formacie (wiersz, kolumna)
            lub None, jeśli brak dostępnych pól.
        """
        for symbol in [self.symbol, self.opponent_symbol]:
            for r in range(3):
                for c in range(3):
                    if board[r][c] == " ":
                        board[r][c] = symbol
                        if self.check_win(board, symbol):
                            board[r][c] = " "
                            return (r, c)
                        board[r][c] = " "
        empty = [
            (r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
        return random.choice(empty) if empty else None

    def check_win(self, board, symbol):
        """
        Sprawdza, czy dany symbol wygrał na planszy.

        Args:
            board (list): Aktualny stan planszy (3x3).
            symbol (str): Symbol gracza ('X' lub 'O').

        Returns:
            bool: True jeśli symbol wygrał, False w przeciwnym razie.
        """
        for i in range(3):
            if all(board[i][j] == symbol for j in range(3)):
                return True
            if all(board[j][i] == symbol for j in range(3)):
                return True
        if all(board[i][i] == symbol for i in range(3)):
            return True
        if all(board[i][2 - i] == symbol for i in range(3)):
            return True
        return False
