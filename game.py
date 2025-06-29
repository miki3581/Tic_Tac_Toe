class TicTacToe:
    """Klasa reprezentująca grę w kółko-krzyżyk."""

    def __init__(self, opponent, player_symbol):
        """
        Inicjalizuje grę z przeciwnikiem oraz symbolem gracza i AI.

        Args:
            opponent (BaseAI): Obiekt przeciwnika AI.
            player_symbol (str): Symbol gracza ('X' lub 'O').
        """
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.opponent = opponent
        self.player_symbol = player_symbol
        self.ai_symbol = "O" if self.player_symbol == "X" else "X"
        self.winner = None
        self.winning_line = None

    def make_move(self, row, col):
        """
        Wykonuje ruch na planszy, sprawdza zwycięzcę i przełącza gracza.

        Args:
            row (int): Wiersz, w którym ma być wykonany ruch.
            col (int): Kolumna, w której ma być wykonany ruch.

        Returns:
            bool: True jeśli ruch został wykonany,
                  False jeśli pole jest zajęte lub gra jest zakończona.
        """
        if self.board[row][col] != " " or self.winner:
            return False
        self.board[row][col] = self.current_player
        if self.check_winner(row, col):
            self.winner = self.current_player
        elif self.is_draw():
            self.winner = None
        self.current_player = "O" if self.current_player == "X" else "X"
        return True

    def make_ai_move(self):
        """Wykonuje ruch AI, jeśli to jego tura."""
        if not self.winner and self.current_player == self.opponent.symbol:
            move = self.opponent.get_move(self.board)
            if move:
                self.make_move(*move)

    def switch_player(self):
        """Przełącza aktualnego gracza."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, row, col):
        """
        Sprawdza, czy aktualny gracz wygrał po wykonaniu ruchu.

        Args:
            row (int): Wiersz, w którym został wykonany ruch.
            col (int): Kolumna, w której został wykonany ruch.

        Returns:
            bool: True jeśli gracz wygrał, False w przeciwnym razie.
        """
        b = self.board
        p = b[row][col]

        def line(cells):
            return all(b[r][c] == p for r, c in cells)

        patterns = [
            [(row, i) for i in range(3)],
            [(i, col) for i in range(3)],
            [(i, i) for i in range(3)],
            [(i, 2 - i) for i in range(3)]
        ]
        for pattern in patterns:
            if pattern and line(pattern):
                self.winning_line = (pattern[0], pattern[-1])
                return True
        return False

    def is_draw(self):
        """
        Sprawdza, czy gra zakończyła się remisem.

        Returns:
            bool: True jeśli gra zakończyła się remisem,
                  False w przeciwnym razie.
        """
        board_full = all(cell != " " for row in self.board for cell in row)
        return board_full and not self.winner
