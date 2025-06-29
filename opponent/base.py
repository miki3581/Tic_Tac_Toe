class BaseAI:
    """Klasa bazowa dla AI w grze kółko-krzyżyk."""
    def __init__(self, symbol):
        """
        Inicjalizuje AI z symbolem gracza i przeciwnika.
        Args:
            symbol (str): Symbol AI ('X' lub 'O')."""
        self.symbol = symbol
        self.opponent_symbol = "X" if symbol == "O" else "O"

    def get_move(self, board):
        """
        Metoda do uzyskania ruchu AI.

        Args:
            board (list): Aktualny stan planszy (3x3).

        Returns:
            tuple: Ruch w formacie (wiersz, kolumna)
            lub None, jeśli brak ruchów.
        """
        raise NotImplementedError("Ruch przeciwnika nie zaimplementowany")
