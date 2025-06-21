class BaseAI:
    def __init__(self, symbol):
        self.symbol = symbol
        self.opponent_symbol = "X" if symbol == "O" else "O"

    def get_move(self, board):
        raise NotImplementedError("get_move nie zaimplementowane")
